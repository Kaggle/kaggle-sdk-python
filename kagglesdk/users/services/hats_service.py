from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.hats_service import DismissHatsRequest, DismissHatsResponse, DismissSurveyRequest, DismissSurveyResponse, GetUserHatsStatusRequest, GetUserHatsStatusResponse

class HatsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_user_hats_status(self, request: GetUserHatsStatusRequest = None) -> GetUserHatsStatusResponse:
    r"""
    Args:
      request (GetUserHatsStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserHatsStatusRequest()

    return self._client.call("users.HatsService", "GetUserHatsStatus", request, GetUserHatsStatusResponse)

  def dismiss_hats(self, request: DismissHatsRequest = None) -> DismissHatsResponse:
    r"""
    Args:
      request (DismissHatsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DismissHatsRequest()

    return self._client.call("users.HatsService", "DismissHats", request, DismissHatsResponse)

  def dismiss_survey(self, request: DismissSurveyRequest = None) -> DismissSurveyResponse:
    r"""
    Args:
      request (DismissSurveyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DismissSurveyRequest()

    return self._client.call("users.HatsService", "DismissSurvey", request, DismissSurveyResponse)
