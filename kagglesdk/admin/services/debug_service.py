from kagglesdk.admin.types.debug_service import AskGeminiRequest, GeminiResponse, SendEmailRequest, SendEmailResponse, ThrowCanonicalExceptionRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DebugClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def throw_canonical_exception(self, request: ThrowCanonicalExceptionRequest = None):
    r"""
    Args:
      request (ThrowCanonicalExceptionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ThrowCanonicalExceptionRequest()

    self._client.call("admin.DebugService", "ThrowCanonicalException", request, None)

  def send_email(self, request: SendEmailRequest = None) -> SendEmailResponse:
    r"""
    Args:
      request (SendEmailRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SendEmailRequest()

    return self._client.call("admin.DebugService", "SendEmail", request, SendEmailResponse)

  def ask_gemini(self, request: AskGeminiRequest = None) -> GeminiResponse:
    r"""
    Args:
      request (AskGeminiRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AskGeminiRequest()

    return self._client.call("admin.DebugService", "AskGemini", request, GeminiResponse)
