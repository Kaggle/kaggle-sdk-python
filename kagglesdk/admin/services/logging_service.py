from kagglesdk.admin.types.logging_service import CreateLogMessageRequest, CreateLogMessageResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LoggingClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_log_message(self, request: CreateLogMessageRequest = None) -> CreateLogMessageResponse:
    r"""
    Creates a sample log message (useful for testing log reporters).

    Args:
      request (CreateLogMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateLogMessageRequest()

    return self._client.call("admin.LoggingService", "CreateLogMessage", request, CreateLogMessageResponse)
