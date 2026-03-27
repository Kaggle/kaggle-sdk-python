import json
import os
import requests
import threading
import time
from kagglesdk.kaggle_env import get_endpoint, get_env, KaggleEnv
from kagglesdk.kaggle_object import KaggleObject
from typing import Type


def _headers_to_str(headers):
    return "\n".join(f"{k}: {v}" for k, v in headers.items())


def _get_apikey_creds():
    apikey_filename = os.path.expanduser("~/.kaggle/kaggle.json")
    if not os.path.exists(apikey_filename):
        return None

    kaggle_json = None
    with open(apikey_filename) as apikey_file:
        kaggle_json = apikey_file.read()

    if not kaggle_json or not kaggle_json.strip():
        return None

    api_key_data = json.loads(kaggle_json)
    username = api_key_data["username"]
    api_key = api_key_data["key"]
    return username, api_key


def _read_secret(env_var):
    secret = os.getenv(env_var)
    if secret is not None and os.path.isfile(secret):
        with open(secret, "r") as f:
            secret = f.read().strip()
    if secret is None:
        raise Exception(f"Must set {env_var}")
    return secret


class KaggleHttpClient(object):
    _transient_errors = (
        requests.exceptions.ConnectionError,
        requests.exceptions.Timeout,
    ) + tuple(requests.exceptions.HTTPError for code in range(500, 600))
    _xsrf_cookie_name = "XSRF-TOKEN"
    _csrf_cookie_name = "CSRF-TOKEN"
    _xsrf_cookies = (_xsrf_cookie_name, _csrf_cookie_name)
    _xsrf_header_name = "X-XSRF-TOKEN"
    # IAP tokens are good for 1 hour: https://cloud.google.com/docs/authentication/token-types#at-lifetime
    # Refresh it before an hour to make sure long-running notebooks can still reach Kaggle.
    _initial_iap_token_refresh_interval_sec = 30 * 60  # 30 mins
    _iap_token_refresh_interval_sec = 55 * 60  # 55 mins

    def __init__(self, env: KaggleEnv = None, verbose: bool = False, renew_iap_token=None, user_agent="kaggle-api/v2.0.0"):
        self._env = env or get_env()
        self._signed_in = None
        self._endpoint = get_endpoint(self._env)
        self._verbose = verbose
        self._session = None
        self._auth = self._build_auth(renew_iap_token)
        self._user_agent = user_agent

    def call(
        self,
        service_name: str,
        request_name: str,
        request: KaggleObject,
        response_type: Type[KaggleObject],
    ):
        self._init_session()
        http_request = self._prepare_request(service_name, request_name, request)

        def caller():
            return self._session.send(http_request)

        http_response = KaggleHttpClient.call_with_retry(caller)

        response = self._prepare_response(response_type, http_response)
        return response

    @staticmethod
    def call_with_retry(caller, max_retries=5, retry_delay_sec=3):
        for attempt in range(max_retries):
            try:
                return caller()
            except KaggleHttpClient._transient_errors as e:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay_sec)
                    retry_delay_sec *= 2
                else:
                    raise

    def _prepare_request(self, service_name: str, request_name: str, request: KaggleObject):
        request_url = self._get_request_url(service_name, request_name)
        http_request = requests.Request(
            method="POST",
            url=request_url,
            json=request.__class__.to_dict(request),
            headers=self._session.headers,
            cookies=self._get_xsrf_cookies(),
            auth=self._auth,
        )
        prepared_request = http_request.prepare()
        self._print_request(prepared_request)
        return prepared_request

    def _get_xsrf_cookies(self):
        cookies = requests.cookies.RequestsCookieJar()
        for cookie in self._session.cookies:
            if cookie.name in KaggleHttpClient._xsrf_cookies:
                cookies[cookie.name] = cookie.value
        return cookies

    def _prepare_response(self, response_type, http_response):
        self._print_response(http_response)
        http_response.raise_for_status()
        if response_type is None:  # Method doesn't have a return type
            return None
        return response_type.from_json(http_response.text)

    def _print_request(self, request):
        if not self._verbose:
            return
        self._print("---------------------Request----------------------")
        self._print(f"{request.method} {request.url}\n{_headers_to_str(request.headers)}\n\n{request.body}")
        self._print("--------------------------------------------------")

    def _print_response(self, response, body=True):
        if not self._verbose:
            return
        self._print("---------------------Response---------------------")
        self._print(f"{response.status_code}\n{_headers_to_str(response.headers)}")
        if body:
            self._print(f"\n{response.text}")
        self._print("--------------------------------------------------")

    def _print(self, message: str):
        if self._verbose:
            print(message)

    def __enter__(self):
        self._init_session()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self._session is not None:
            self._session.close()

    def _init_session(self):
        if self._session is not None:
            return self._session

        self._session = requests.Session()
        self._session.headers.update(
            {
                "User-Agent": self._user_agent,
                "Content-Type": "application/json",
            }
        )

        self._fill_xsrf_token()

    def _fill_xsrf_token(self):
        initial_get_request = requests.Request(
            method="GET",
            url=self._endpoint,
            headers=self._session.headers,
            auth=self._auth,
        )
        prepared_request = initial_get_request.prepare()
        self._print_request(prepared_request)

        http_response = self._session.send(prepared_request)

        self._print_response(http_response, body=False)
        http_response.raise_for_status()

        self._session.headers.update(
            {
                KaggleHttpClient._xsrf_header_name: self._session.cookies[KaggleHttpClient._xsrf_cookie_name],
            }
        )

    class AutoRefreshBearerAuth(requests.auth.AuthBase):

        def __init__(
            self,
            name,
            header,
            token,
            refresh_func=None,
            initial_refresh_interval_sec=None,
            refresh_interval_sec=None,
            verbose=False,
        ):
            self._name = name
            self._header = header
            self._token = token
            self._refresh_func = refresh_func
            self._initial_refresh_interval_sec = initial_refresh_interval_sec
            self._refresh_interval_sec = refresh_interval_sec
            self._verbose = verbose
            if refresh_func and refresh_interval_sec:
                self._refresh_thread = threading.Thread(target=self._refresh_token_loop)
                self._refresh_thread.daemon = True
                self._refresh_thread.start()

        @staticmethod
        def create(
            name,
            header,
            env_var,
            refresh_func=None,
            initial_refresh_interval_sec=None,
            refresh_interval_sec=None,
            verbose=None,
        ):
            token = _read_secret(env_var)
            return KaggleHttpClient.AutoRefreshBearerAuth(
                name,
                header,
                token,
                refresh_func,
                initial_refresh_interval_sec,
                refresh_interval_sec,
                verbose,
            )

        def _refresh_token_loop(self):
            refresh_interval_sec = self._initial_refresh_interval_sec
            while True:
                time.sleep(refresh_interval_sec)
                refresh_interval_sec = self._refresh_interval_sec
                self._token = self._refresh_token()

        def _refresh_token(self):
            self._print(f"Will try to renew {self._name} token...")
            try:
                token = self._refresh_func().token
                if token:
                    self._print(f"Successfully renewed {self._name} token")
                else:
                    self._print(f"Got an empty response on {self._name} token renewal attempt")
                return token
            except Exception as e:
                self._print(f"Error during {self._name} token renewal: {e}")
                raise

        def _print(self, message):
            if self._verbose:
                print(message)

        def __call__(self, r):
            r.headers[self._header] = f"Bearer {self._token}"
            return r

    class MultiAuth(requests.auth.AuthBase):

        def __init__(self, auths):
            self._auths = auths

        def __call__(self, r):
            for auth in self._auths:
                r = auth(r)
            return r

    def _build_api_auth(self):
        api_token_auth = KaggleHttpClient.AutoRefreshBearerAuth.create(
            name="API",
            header="Authorization",
            env_var="KAGGLE_API_TOKEN",
            verbose=self._verbose,
        )
        if api_token_auth is not None:
            return api_token_auth

        apikey_creds = _get_apikey_creds()
        if apikey_creds is not None:
            return apikey_creds

        return None

    def _build_iap_auth(self, renew_iap_token):
        if self._env not in (
            KaggleEnv.STAGING,
            KaggleEnv.ADMIN,
            KaggleEnv.QA,
            KaggleEnv.LOCAL,
        ):
            return None
        return KaggleHttpClient.AutoRefreshBearerAuth.create(
            name="IAP",
            header="Proxy-Authorization",
            env_var="KAGGLE_IAP_TOKEN",
            refresh_func=renew_iap_token,
            initial_refresh_interval_sec=KaggleHttpClient._initial_iap_token_refresh_interval_sec,
            refresh_interval_sec=KaggleHttpClient._iap_token_refresh_interval_sec,
            verbose=self._verbose,
        )

    def _build_auth(self, renew_iap_token):
        auths = [self._build_api_auth()]
        iap_auth = self._build_iap_auth(renew_iap_token)
        if iap_auth is not None:
            auths.append(iap_auth)
        return KaggleHttpClient.MultiAuth(auths)

    def _get_request_url(self, service_name: str, request_name: str):
        # On prod, API endpoints are served under https://api.kaggle.com/v1,
        # but on staging/admin/local, they are served under http://localhost/api/v1.
        base_url = self._endpoint if self._env == KaggleEnv.PROD else f"{self._endpoint}/api"
        return f"{base_url}/v1/{service_name}/{request_name}"
