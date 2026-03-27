from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.moderation_service import ApproveAppealRequest, ForceUpdateContentStatesRequest, GetEntityForModerationRequest, GetEntityForModerationResponse, IssueUserPenaltyRequest, ListAppealReasonsRequest, ListAppealReasonsResponse, ListPenaltySourcesRequest, ListPenaltySourcesResponse, ListUserModerationHistoryRequest, ListUserModerationHistoryResponse, SetUserAppealVerdictRequest, UnbanUsersRequest, UnbanUsersResponse

class ModerationClient(object):
  """Admin-only moderation service."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def issue_user_penalty(self, request: IssueUserPenaltyRequest = None):
    r"""
    Args:
      request (IssueUserPenaltyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = IssueUserPenaltyRequest()

    self._client.call("users.ModerationService", "IssueUserPenalty", request, None)

  def list_user_moderation_history(self, request: ListUserModerationHistoryRequest = None) -> ListUserModerationHistoryResponse:
    r"""
    Args:
      request (ListUserModerationHistoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserModerationHistoryRequest()

    return self._client.call("users.ModerationService", "ListUserModerationHistory", request, ListUserModerationHistoryResponse)

  def list_appeal_reasons(self, request: ListAppealReasonsRequest = None) -> ListAppealReasonsResponse:
    r"""
    Args:
      request (ListAppealReasonsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListAppealReasonsRequest()

    return self._client.call("users.ModerationService", "ListAppealReasons", request, ListAppealReasonsResponse)

  def list_penalty_sources(self, request: ListPenaltySourcesRequest = None) -> ListPenaltySourcesResponse:
    r"""
    Args:
      request (ListPenaltySourcesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListPenaltySourcesRequest()

    return self._client.call("users.ModerationService", "ListPenaltySources", request, ListPenaltySourcesResponse)

  def approve_appeal(self, request: ApproveAppealRequest = None):
    r"""
    Args:
      request (ApproveAppealRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApproveAppealRequest()

    self._client.call("users.ModerationService", "ApproveAppeal", request, None)

  def unban_users(self, request: UnbanUsersRequest = None) -> UnbanUsersResponse:
    r"""
    Args:
      request (UnbanUsersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnbanUsersRequest()

    return self._client.call("users.ModerationService", "UnbanUsers", request, UnbanUsersResponse)

  def get_entity_for_moderation(self, request: GetEntityForModerationRequest = None) -> GetEntityForModerationResponse:
    r"""
    Verifies an entity was created by the requested user, and gets the
    title + creation date for the entity.
    NOTE: This is a fairly dangerous route, as it bypasses the normal authz
    configured for getting the entity. This route should only be
    used by moderation (manual/auto).

    Args:
      request (GetEntityForModerationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetEntityForModerationRequest()

    return self._client.call("users.ModerationService", "GetEntityForModeration", request, GetEntityForModerationResponse)

  def set_user_appeal_verdict(self, request: SetUserAppealVerdictRequest = None):
    r"""
    Args:
      request (SetUserAppealVerdictRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetUserAppealVerdictRequest()

    self._client.call("users.ModerationService", "SetUserAppealVerdict", request, None)

  def force_update_content_states(self, request: ForceUpdateContentStatesRequest = None):
    r"""
    Updates a list of same-type entities to a target content state.
    WARNING: Does not do any content state validation. Meant to be a
    convenience for SQL migrations used in moderation requests.

    Args:
      request (ForceUpdateContentStatesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ForceUpdateContentStatesRequest()

    self._client.call("users.ModerationService", "ForceUpdateContentStates", request, None)
