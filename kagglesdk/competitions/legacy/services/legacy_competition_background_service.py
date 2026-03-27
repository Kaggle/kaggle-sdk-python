from kagglesdk.competitions.legacy.types.legacy_background_operation import BackgroundOperation
from kagglesdk.competitions.legacy.types.legacy_competition_background_service import GetBackgroundOperationRequest, WaitBackgroundOperationRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LegacyCompetitionBackgroundClient(object):
  r"""
  Loosely based on
  https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto
  Prefixed with 'Background' to avoid conflict with that one.
  Has historically only been used by Competitions but could eventually be made
  into an official (non-Legacy) service.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def wait_background_operation(self, request: WaitBackgroundOperationRequest = None) -> BackgroundOperation:
    r"""
    Args:
      request (WaitBackgroundOperationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = WaitBackgroundOperationRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionBackgroundService", "WaitBackgroundOperation", request, BackgroundOperation)

  def get_background_operation(self, request: GetBackgroundOperationRequest = None) -> BackgroundOperation:
    r"""
    Args:
      request (GetBackgroundOperationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBackgroundOperationRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionBackgroundService", "GetBackgroundOperation", request, BackgroundOperation)
