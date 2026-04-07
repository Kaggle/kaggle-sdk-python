from kagglesdk.competitions.types.competition_user import CompetitionUser
from kagglesdk.competitions.types.user_service import AcceptRulesRequest, CreateOrUpdateUserEmailShareRequest, GetUserEmailShareRequest, GetUserEmailShareResponse, GetUserRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class UserClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def accept_rules(self, request: AcceptRulesRequest = None):
    r"""
    Logs that the Current User has accepted the rules for the given
    Competition.

    Args:
      request (AcceptRulesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AcceptRulesRequest()

    self._client.call("competitions.UserService", "AcceptRules", request, None)

  def get_user(self, request: GetUserRequest = None) -> CompetitionUser:
    r"""
    Returns information about the calling User in the context of the given
    Competition.

    Args:
      request (GetUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserRequest()

    return self._client.call("competitions.UserService", "GetUser", request, CompetitionUser)

  def get_user_email_share(self, request: GetUserEmailShareRequest = None) -> GetUserEmailShareResponse:
    r"""
    Args:
      request (GetUserEmailShareRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserEmailShareRequest()

    return self._client.call("competitions.UserService", "GetUserEmailShare", request, GetUserEmailShareResponse)

  def create_or_update_user_email_share(self, request: CreateOrUpdateUserEmailShareRequest = None):
    r"""
    Args:
      request (CreateOrUpdateUserEmailShareRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateOrUpdateUserEmailShareRequest()

    self._client.call("competitions.UserService", "CreateOrUpdateUserEmailShare", request, None)
