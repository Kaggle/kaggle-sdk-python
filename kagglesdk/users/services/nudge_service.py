from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.nudge_service import AddNudgeRequest, AddNudgeResponse, CheckCustomNudgeRequest, CheckCustomNudgeResponse, CheckForNudgeRequest, CheckForNudgeResponse, GetNudgeConfigRequest, GetNudgeConfigResponse, ReactToNudgeRequest, ReactToNudgeResponse, ShowingNudgeRequest, ShowingNudgeResponse, TestBigQueryNudgeRequest, TestBigQueryNudgeResponse

class NudgeClient(object):
  r"""
  Service for nudges (pop-up dismissible prompts to the user)
  Currently only used for Employer/Organization Info nudges, but extensible to
  others
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def check_for_nudge(self, request: CheckForNudgeRequest = None) -> CheckForNudgeResponse:
    r"""
    Check if a user has any available nudges to show

    Args:
      request (CheckForNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckForNudgeRequest()

    return self._client.call("users.NudgeService", "CheckForNudge", request, CheckForNudgeResponse)

  def react_to_nudge(self, request: ReactToNudgeRequest = None) -> ReactToNudgeResponse:
    r"""
    Log what a user did with the nudge (ie did they ignore? accept?)

    Args:
      request (ReactToNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReactToNudgeRequest()

    return self._client.call("users.NudgeService", "ReactToNudge", request, ReactToNudgeResponse)

  def showing_nudge(self, request: ShowingNudgeRequest = None) -> ShowingNudgeResponse:
    r"""
    Report that a user is seeing a particular nudge
    This should only be called once by the frontend for a particular user/nudge
    pair

    Args:
      request (ShowingNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ShowingNudgeRequest()

    return self._client.call("users.NudgeService", "ShowingNudge", request, ShowingNudgeResponse)

  def check_custom_nudge(self, request: CheckCustomNudgeRequest = None) -> CheckCustomNudgeResponse:
    r"""
    Check if a user should be served a particular custom nudge.

    Args:
      request (CheckCustomNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckCustomNudgeRequest()

    return self._client.call("users.NudgeService", "CheckCustomNudge", request, CheckCustomNudgeResponse)

  def get_nudge_config(self, request: GetNudgeConfigRequest = None) -> GetNudgeConfigResponse:
    r"""
    Args:
      request (GetNudgeConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNudgeConfigRequest()

    return self._client.call("users.NudgeService", "GetNudgeConfig", request, GetNudgeConfigResponse)

  def add_nudge(self, request: AddNudgeRequest = None) -> AddNudgeResponse:
    r"""
    Args:
      request (AddNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddNudgeRequest()

    return self._client.call("users.NudgeService", "AddNudge", request, AddNudgeResponse)

  def test_big_query_nudge(self, request: TestBigQueryNudgeRequest = None) -> TestBigQueryNudgeResponse:
    r"""
    Used to test the connection to bigquery and the query/view

    Args:
      request (TestBigQueryNudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TestBigQueryNudgeRequest()

    return self._client.call("users.NudgeService", "TestBigQueryNudge", request, TestBigQueryNudgeResponse)
