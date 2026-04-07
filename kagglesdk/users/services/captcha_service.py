from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.captcha_service import GetCaptchaConfigRequest, GetCaptchaConfigResponse, VerifyCaptchaRequest, VerifyCaptchaResponse

class CaptchaClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_captcha_config(self, request: GetCaptchaConfigRequest = None) -> GetCaptchaConfigResponse:
    r"""
    Args:
      request (GetCaptchaConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCaptchaConfigRequest()

    return self._client.call("users.CaptchaService", "GetCaptchaConfig", request, GetCaptchaConfigResponse)

  def verify_captcha(self, request: VerifyCaptchaRequest = None) -> VerifyCaptchaResponse:
    r"""
    Uses reCaptcha V3 (background only)

    Args:
      request (VerifyCaptchaRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VerifyCaptchaRequest()

    return self._client.call("users.CaptchaService", "VerifyCaptcha", request, VerifyCaptchaResponse)
