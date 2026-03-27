from kagglesdk.competitions.types.team import Team, TeamFile
from kagglesdk.competitions.types.team_service import AcceptTeamMergeRequest, BatchGetUserTeamsRequest, BatchGetUserTeamsResponse, CreateTeamFileRequest, CreateTeamFileResponse, CreateTeamsRequest, CreateTeamsResponse, DownloadTeamFileRequest, DownloadTeamFileResponse, GetTeamFileRequest, GetTeamRequest, GetTeamUpForUsersRequest, GetTeamUpForUsersResponse, InvalidateOrphanedTeamsRequest, InvalidateOrphanedTeamsResponse, ListTeamMergeRequestsRequest, ListTeamMergeRequestsResponse, ListTeamsByUserRequest, ListTeamsByUserResponse, RejectTeamMergeRequest, RequestTeamMergeRequest, SearchTeamsRequest, SearchTeamsResponse, SetTeamWriteUpRequest, UpdateTeamRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class TeamClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def accept_team_merge(self, request: AcceptTeamMergeRequest = None):
    r"""
    Args:
      request (AcceptTeamMergeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AcceptTeamMergeRequest()

    self._client.call("competitions.TeamService", "AcceptTeamMerge", request, None)

  def create_teams(self, request: CreateTeamsRequest = None) -> CreateTeamsResponse:
    r"""
    Args:
      request (CreateTeamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTeamsRequest()

    return self._client.call("competitions.TeamService", "CreateTeams", request, CreateTeamsResponse)

  def create_team_file(self, request: CreateTeamFileRequest = None) -> CreateTeamFileResponse:
    r"""
    Args:
      request (CreateTeamFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTeamFileRequest()

    return self._client.call("competitions.TeamService", "CreateTeamFile", request, CreateTeamFileResponse)

  def download_team_file(self, request: DownloadTeamFileRequest = None) -> DownloadTeamFileResponse:
    r"""
    TODO(b/204171009): Use HTTP Get and redirect once file downloads are
    supported by frontend clients

    Args:
      request (DownloadTeamFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DownloadTeamFileRequest()

    return self._client.call("competitions.TeamService", "DownloadTeamFile", request, DownloadTeamFileResponse)

  def get_team_file(self, request: GetTeamFileRequest = None) -> TeamFile:
    r"""
    Args:
      request (GetTeamFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTeamFileRequest()

    return self._client.call("competitions.TeamService", "GetTeamFile", request, TeamFile)

  def get_team(self, request: GetTeamRequest = None) -> Team:
    r"""
    Args:
      request (GetTeamRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTeamRequest()

    return self._client.call("competitions.TeamService", "GetTeam", request, Team)

  def get_team_up_for_users(self, request: GetTeamUpForUsersRequest = None) -> GetTeamUpForUsersResponse:
    r"""
    Not all provided user_ids are guaranteed to be returned in the response,
    since not all users are in a team.

    Args:
      request (GetTeamUpForUsersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTeamUpForUsersRequest()

    return self._client.call("competitions.TeamService", "GetTeamUpForUsers", request, GetTeamUpForUsersResponse)

  def list_team_merge_requests(self, request: ListTeamMergeRequestsRequest = None) -> ListTeamMergeRequestsResponse:
    r"""
    Args:
      request (ListTeamMergeRequestsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListTeamMergeRequestsRequest()

    return self._client.call("competitions.TeamService", "ListTeamMergeRequests", request, ListTeamMergeRequestsResponse)

  def list_teams_by_user(self, request: ListTeamsByUserRequest = None) -> ListTeamsByUserResponse:
    r"""
    Args:
      request (ListTeamsByUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListTeamsByUserRequest()

    return self._client.call("competitions.TeamService", "ListTeamsByUser", request, ListTeamsByUserResponse)

  def batch_get_user_teams(self, request: BatchGetUserTeamsRequest = None) -> BatchGetUserTeamsResponse:
    r"""
    Args:
      request (BatchGetUserTeamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchGetUserTeamsRequest()

    return self._client.call("competitions.TeamService", "BatchGetUserTeams", request, BatchGetUserTeamsResponse)

  def reject_team_merge(self, request: RejectTeamMergeRequest = None):
    r"""
    Args:
      request (RejectTeamMergeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RejectTeamMergeRequest()

    self._client.call("competitions.TeamService", "RejectTeamMerge", request, None)

  def request_team_merge(self, request: RequestTeamMergeRequest = None):
    r"""
    Args:
      request (RequestTeamMergeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RequestTeamMergeRequest()

    self._client.call("competitions.TeamService", "RequestTeamMerge", request, None)

  def search_teams(self, request: SearchTeamsRequest = None) -> SearchTeamsResponse:
    r"""
    Searches TeamName by a prefix, and returns up to 100 matching teams ordered
    by length.

    Args:
      request (SearchTeamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchTeamsRequest()

    return self._client.call("competitions.TeamService", "SearchTeams", request, SearchTeamsResponse)

  def update_team(self, request: UpdateTeamRequest = None) -> Team:
    r"""
    Args:
      request (UpdateTeamRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateTeamRequest()

    return self._client.call("competitions.TeamService", "UpdateTeam", request, Team)

  def set_team_write_up(self, request: SetTeamWriteUpRequest = None) -> Team:
    r"""
    TODO(aip.dev/134): (-- api-linter: core::0134::synonyms=disabled --)

    Args:
      request (SetTeamWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetTeamWriteUpRequest()

    return self._client.call("competitions.TeamService", "SetTeamWriteUp", request, Team)

  def invalidate_orphaned_teams(self, request: InvalidateOrphanedTeamsRequest = None) -> InvalidateOrphanedTeamsResponse:
    r"""
    Admin handler to call to aid in competition finalization

    Args:
      request (InvalidateOrphanedTeamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateOrphanedTeamsRequest()

    return self._client.call("competitions.TeamService", "InvalidateOrphanedTeams", request, InvalidateOrphanedTeamsResponse)
