from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_proxy_api_service import ApiCreateDefaultModelProxyTokenRequest, ApiCreateDefaultModelProxyTokenResponse

class ModelProxyApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_default_model_proxy_token(self, request: ApiCreateDefaultModelProxyTokenRequest = None) -> ApiCreateDefaultModelProxyTokenResponse:
    r"""
    Creates a default MP token for local usage. Safety features:
    1) 2h TTL
    2) Requires Persona + Phone verification
    3) Limits model access to 'kaggle-benchmarks-local'
    (see cloud/kaggle/modelproxy/backends/config/config.gcl)
    4) Caches requests so each user can only have a single active token

    Args:
      request (ApiCreateDefaultModelProxyTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateDefaultModelProxyTokenRequest()

    return self._client.call("models.ModelProxyApiService", "CreateDefaultModelProxyToken", request, ApiCreateDefaultModelProxyTokenResponse)
