from kagglesdk.competitions.types.team import Team, TeamMergeRequest, TeamUpInfo
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import List, Optional, Dict

class AcceptTeamMergeRequest(KaggleObject):
  r"""
  Attributes:
    merge_request_id (int)
  """

  def __init__(self):
    self._merge_request_id = 0
    self._freeze()

  @property
  def merge_request_id(self) -> int:
    return self._merge_request_id

  @merge_request_id.setter
  def merge_request_id(self, merge_request_id: int):
    if merge_request_id is None:
      del self.merge_request_id
      return
    if not isinstance(merge_request_id, int):
      raise TypeError('merge_request_id must be of type int')
    self._merge_request_id = merge_request_id


class BatchGetUserTeamsRequest(KaggleObject):
  r"""
  Request the associated team in a specific competition for a list of users.

  Attributes:
    competition_id (int)
      Only retrieve users who have joined this competition.
    user_ids (int)
      The length of of user_ids is limited to 100.
  """

  def __init__(self):
    self._competition_id = 0
    self._user_ids = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    """Only retrieve users who have joined this competition."""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The length of of user_ids is limited to 100."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids


class BatchGetUserTeamsResponse(KaggleObject):
  r"""
  Only one competition_id is requested, therefore, only one team is returned
  for each user_id.

  Attributes:
    user_results (BatchGetUserTeamsResponse.UserResult)
      Returns all users requested in the same order.
  """

  class UserResult(KaggleObject):
    r"""
    Attributes:
      user_id (int)
        Corresponds to the user_id in the request.
      team (Team)
        Only set if the user_id has joined the requested competition.
    """

    def __init__(self):
      self._user_id = 0
      self._team = None
      self._freeze()

    @property
    def user_id(self) -> int:
      """Corresponds to the user_id in the request."""
      return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
      if user_id is None:
        del self.user_id
        return
      if not isinstance(user_id, int):
        raise TypeError('user_id must be of type int')
      self._user_id = user_id

    @property
    def team(self) -> Optional['Team']:
      """Only set if the user_id has joined the requested competition."""
      return self._team

    @team.setter
    def team(self, team: Optional['Team']):
      if team is None:
        del self.team
        return
      if not isinstance(team, Team):
        raise TypeError('team must be of type Team')
      self._team = team


  def __init__(self):
    self._user_results = []
    self._freeze()

  @property
  def user_results(self) -> Optional[List[Optional['BatchGetUserTeamsResponse.UserResult']]]:
    """Returns all users requested in the same order."""
    return self._user_results

  @user_results.setter
  def user_results(self, user_results: Optional[List[Optional['BatchGetUserTeamsResponse.UserResult']]]):
    if user_results is None:
      del self.user_results
      return
    if not isinstance(user_results, list):
      raise TypeError('user_results must be of type list')
    if not all([isinstance(t, BatchGetUserTeamsResponse.UserResult) for t in user_results]):
      raise TypeError('user_results must contain only items of type BatchGetUserTeamsResponse.UserResult')
    self._user_results = user_results


class BenchmarkModelVersionId(KaggleObject):
  r"""
  Attributes:
    id (int)
  """

  def __init__(self):
    self._id = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class CreateTeamFileRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    blob_token (str)
  """

  def __init__(self):
    self._team_id = 0
    self._blob_token = ""
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def blob_token(self) -> str:
    return self._blob_token

  @blob_token.setter
  def blob_token(self, blob_token: str):
    if blob_token is None:
      del self.blob_token
      return
    if not isinstance(blob_token, str):
      raise TypeError('blob_token must be of type str')
    self._blob_token = blob_token


class CreateTeamFileResponse(KaggleObject):
  r"""
  Attributes:
    file_name (str)
    size_bytes (int)
      Length of the file in bytes.
  """

  def __init__(self):
    self._file_name = ""
    self._size_bytes = 0
    self._freeze()

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def size_bytes(self) -> int:
    """Length of the file in bytes."""
    return self._size_bytes

  @size_bytes.setter
  def size_bytes(self, size_bytes: int):
    if size_bytes is None:
      del self.size_bytes
      return
    if not isinstance(size_bytes, int):
      raise TypeError('size_bytes must be of type int')
    self._size_bytes = size_bytes


class CreateTeamsInfo(KaggleObject):
  r"""
  Attributes:
    id (int)
      Team Id is ignored on request, and populated on response.
    name (str)
    leader_id (int)
    member_ids (int)
    benchmark_model_version_id (int)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._leader_id = 0
    self._member_ids = []
    self._benchmark_model_version_id = None
    self._freeze()

  @property
  def id(self) -> int:
    """Team Id is ignored on request, and populated on response."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def leader_id(self) -> int:
    return self._leader_id

  @leader_id.setter
  def leader_id(self, leader_id: int):
    if leader_id is None:
      del self.leader_id
      return
    if not isinstance(leader_id, int):
      raise TypeError('leader_id must be of type int')
    self._leader_id = leader_id

  @property
  def member_ids(self) -> Optional[List[int]]:
    return self._member_ids

  @member_ids.setter
  def member_ids(self, member_ids: Optional[List[int]]):
    if member_ids is None:
      del self.member_ids
      return
    if not isinstance(member_ids, list):
      raise TypeError('member_ids must be of type list')
    if not all([isinstance(t, int) for t in member_ids]):
      raise TypeError('member_ids must contain only items of type int')
    self._member_ids = member_ids

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id


class CreateTeamsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    teams (CreateTeamsInfo)
  """

  def __init__(self):
    self._competition_id = 0
    self._teams = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def teams(self) -> Optional[List[Optional['CreateTeamsInfo']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['CreateTeamsInfo']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, CreateTeamsInfo) for t in teams]):
      raise TypeError('teams must contain only items of type CreateTeamsInfo')
    self._teams = teams


class CreateTeamsResponse(KaggleObject):
  r"""
  Attributes:
    teams (CreateTeamsInfo)
  """

  def __init__(self):
    self._teams = []
    self._freeze()

  @property
  def teams(self) -> Optional[List[Optional['CreateTeamsInfo']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['CreateTeamsInfo']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, CreateTeamsInfo) for t in teams]):
      raise TypeError('teams must contain only items of type CreateTeamsInfo')
    self._teams = teams


class DownloadTeamFileRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
  """

  def __init__(self):
    self._team_id = 0
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id


class DownloadTeamFileResponse(KaggleObject):
  r"""
  Attributes:
    download_url (str)
  """

  def __init__(self):
    self._download_url = ""
    self._freeze()

  @property
  def download_url(self) -> str:
    return self._download_url

  @download_url.setter
  def download_url(self, download_url: str):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url


class GetTeamFileRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
  """

  def __init__(self):
    self._team_id = 0
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id


class GetTeamRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
  """

  def __init__(self):
    self._team_id = 0
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id


class GetTeamUpForUsersRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    user_ids (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._user_ids = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def user_ids(self) -> Optional[List[int]]:
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids


class GetTeamUpForUsersResponse(KaggleObject):
  r"""
  Attributes:
    team_up_state (TeamUpInfo)
      Map for userId (int32 key) to associate TeamUpInfo
  """

  def __init__(self):
    self._team_up_state = {}
    self._freeze()

  @property
  def team_up_state(self) -> Optional[Dict[int, Optional['TeamUpInfo']]]:
    """Map for userId (int32 key) to associate TeamUpInfo"""
    return self._team_up_state

  @team_up_state.setter
  def team_up_state(self, team_up_state: Optional[Dict[int, Optional['TeamUpInfo']]]):
    if team_up_state is None:
      del self.team_up_state
      return
    if not isinstance(team_up_state, dict):
      raise TypeError('team_up_state must be of type dict')
    if not all([isinstance(v, TeamUpInfo) for k, v in team_up_state]):
      raise TypeError('team_up_state must contain only items of type TeamUpInfo')
    self._team_up_state = team_up_state


class InvalidateOrphanedTeamsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class InvalidateOrphanedTeamsResponse(KaggleObject):
  r"""
  Attributes:
    num_invalidated (int)
  """

  def __init__(self):
    self._num_invalidated = 0
    self._freeze()

  @property
  def num_invalidated(self) -> int:
    return self._num_invalidated

  @num_invalidated.setter
  def num_invalidated(self, num_invalidated: int):
    if num_invalidated is None:
      del self.num_invalidated
      return
    if not isinstance(num_invalidated, int):
      raise TypeError('num_invalidated must be of type int')
    self._num_invalidated = num_invalidated


class ListTeamMergeRequestsRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    team_id (int)
  """

  def __init__(self):
    self._team_id = 0
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id


class ListTeamMergeRequestsResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    inbound (TeamMergeRequest)
      TODO(aip.dev/158): (-- api-linter:
      core::0158::response-plural-first-field=disabled --)
    outbound (TeamMergeRequest)
  """

  def __init__(self):
    self._inbound = []
    self._outbound = []
    self._freeze()

  @property
  def inbound(self) -> Optional[List[Optional['TeamMergeRequest']]]:
    r"""
    TODO(aip.dev/158): (-- api-linter:
    core::0158::response-plural-first-field=disabled --)
    """
    return self._inbound

  @inbound.setter
  def inbound(self, inbound: Optional[List[Optional['TeamMergeRequest']]]):
    if inbound is None:
      del self.inbound
      return
    if not isinstance(inbound, list):
      raise TypeError('inbound must be of type list')
    if not all([isinstance(t, TeamMergeRequest) for t in inbound]):
      raise TypeError('inbound must contain only items of type TeamMergeRequest')
    self._inbound = inbound

  @property
  def outbound(self) -> Optional[List[Optional['TeamMergeRequest']]]:
    return self._outbound

  @outbound.setter
  def outbound(self, outbound: Optional[List[Optional['TeamMergeRequest']]]):
    if outbound is None:
      del self.outbound
      return
    if not isinstance(outbound, list):
      raise TypeError('outbound must be of type list')
    if not all([isinstance(t, TeamMergeRequest) for t in outbound]):
      raise TypeError('outbound must contain only items of type TeamMergeRequest')
    self._outbound = outbound


class ListTeamsByUserRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class ListTeamsByUserResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    teams (Team)
  """

  def __init__(self):
    self._teams = []
    self._freeze()

  @property
  def teams(self) -> Optional[List[Optional['Team']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['Team']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, Team) for t in teams]):
      raise TypeError('teams must contain only items of type Team')
    self._teams = teams


class RejectTeamMergeRequest(KaggleObject):
  r"""
  Attributes:
    merge_request_id (int)
  """

  def __init__(self):
    self._merge_request_id = 0
    self._freeze()

  @property
  def merge_request_id(self) -> int:
    return self._merge_request_id

  @merge_request_id.setter
  def merge_request_id(self, merge_request_id: int):
    if merge_request_id is None:
      del self.merge_request_id
      return
    if not isinstance(merge_request_id, int):
      raise TypeError('merge_request_id must be of type int')
    self._merge_request_id = merge_request_id


class RequestTeamMergeRequest(KaggleObject):
  r"""
  Attributes:
    parent_team_id (int)
    child_team_id (int)
  """

  def __init__(self):
    self._parent_team_id = 0
    self._child_team_id = 0
    self._freeze()

  @property
  def parent_team_id(self) -> int:
    return self._parent_team_id

  @parent_team_id.setter
  def parent_team_id(self, parent_team_id: int):
    if parent_team_id is None:
      del self.parent_team_id
      return
    if not isinstance(parent_team_id, int):
      raise TypeError('parent_team_id must be of type int')
    self._parent_team_id = parent_team_id

  @property
  def child_team_id(self) -> int:
    return self._child_team_id

  @child_team_id.setter
  def child_team_id(self, child_team_id: int):
    if child_team_id is None:
      del self.child_team_id
      return
    if not isinstance(child_team_id, int):
      raise TypeError('child_team_id must be of type int')
    self._child_team_id = child_team_id


class SearchTeamsRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    competition_id (int)
    team_name_prefix (str)
      Checks for team names beginning with this value.
    take (int)
      Max number of teams to return
  """

  def __init__(self):
    self._competition_id = 0
    self._team_name_prefix = ""
    self._take = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def team_name_prefix(self) -> str:
    """Checks for team names beginning with this value."""
    return self._team_name_prefix

  @team_name_prefix.setter
  def team_name_prefix(self, team_name_prefix: str):
    if team_name_prefix is None:
      del self.team_name_prefix
      return
    if not isinstance(team_name_prefix, str):
      raise TypeError('team_name_prefix must be of type str')
    self._team_name_prefix = team_name_prefix

  @property
  def take(self) -> int:
    """Max number of teams to return"""
    return self._take or 0

  @take.setter
  def take(self, take: Optional[int]):
    if take is None:
      del self.take
      return
    if not isinstance(take, int):
      raise TypeError('take must be of type int')
    self._take = take


class SearchTeamsResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    teams (SearchTeamsResponse.FoundTeam)
    teams_detailed (Team)
  """

  class FoundTeam(KaggleObject):
    r"""
    Attributes:
      team_id (int)
      team_name (str)
      team_leader (UserAvatar)
    """

    def __init__(self):
      self._team_id = 0
      self._team_name = ""
      self._team_leader = None
      self._freeze()

    @property
    def team_id(self) -> int:
      return self._team_id

    @team_id.setter
    def team_id(self, team_id: int):
      if team_id is None:
        del self.team_id
        return
      if not isinstance(team_id, int):
        raise TypeError('team_id must be of type int')
      self._team_id = team_id

    @property
    def team_name(self) -> str:
      return self._team_name

    @team_name.setter
    def team_name(self, team_name: str):
      if team_name is None:
        del self.team_name
        return
      if not isinstance(team_name, str):
        raise TypeError('team_name must be of type str')
      self._team_name = team_name

    @property
    def team_leader(self) -> Optional['UserAvatar']:
      return self._team_leader

    @team_leader.setter
    def team_leader(self, team_leader: Optional['UserAvatar']):
      if team_leader is None:
        del self.team_leader
        return
      if not isinstance(team_leader, UserAvatar):
        raise TypeError('team_leader must be of type UserAvatar')
      self._team_leader = team_leader


  def __init__(self):
    self._teams = []
    self._teams_detailed = []
    self._freeze()

  @property
  def teams(self) -> Optional[List[Optional['SearchTeamsResponse.FoundTeam']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['SearchTeamsResponse.FoundTeam']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, SearchTeamsResponse.FoundTeam) for t in teams]):
      raise TypeError('teams must contain only items of type SearchTeamsResponse.FoundTeam')
    self._teams = teams

  @property
  def teams_detailed(self) -> Optional[List[Optional['Team']]]:
    return self._teams_detailed

  @teams_detailed.setter
  def teams_detailed(self, teams_detailed: Optional[List[Optional['Team']]]):
    if teams_detailed is None:
      del self.teams_detailed
      return
    if not isinstance(teams_detailed, list):
      raise TypeError('teams_detailed must be of type list')
    if not all([isinstance(t, Team) for t in teams_detailed]):
      raise TypeError('teams_detailed must contain only items of type Team')
    self._teams_detailed = teams_detailed


class SetTeamWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
      Intentionally allowing non-leaders to update to support the New Topic
      checkbox feature
    forum_topic_id (int)
      Unset to clear the field
  """

  def __init__(self):
    self._team_id = 0
    self._forum_topic_id = None
    self._freeze()

  @property
  def team_id(self) -> int:
    r"""
    Intentionally allowing non-leaders to update to support the New Topic
    checkbox feature
    """
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def forum_topic_id(self) -> int:
    """Unset to clear the field"""
    return self._forum_topic_id or 0

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: Optional[int]):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id


class UpdateTeamRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    team_name (str)
    team_leader_id (int)
    team_up_enabled (bool)
    team_up_intro (str)
    write_up_url (str)
      URL linking to a Kaggle discussion post, subject to validation.
    benchmark_model_version_id (BenchmarkModelVersionId)
      Admin only. Links the team to a benchmark model version for game arena.
  """

  def __init__(self):
    self._team_id = 0
    self._team_name = None
    self._team_leader_id = None
    self._team_up_enabled = None
    self._team_up_intro = None
    self._write_up_url = None
    self._benchmark_model_version_id = None
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def team_name(self) -> str:
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: Optional[str]):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name

  @property
  def team_leader_id(self) -> int:
    return self._team_leader_id or 0

  @team_leader_id.setter
  def team_leader_id(self, team_leader_id: Optional[int]):
    if team_leader_id is None:
      del self.team_leader_id
      return
    if not isinstance(team_leader_id, int):
      raise TypeError('team_leader_id must be of type int')
    self._team_leader_id = team_leader_id

  @property
  def team_up_enabled(self) -> bool:
    return self._team_up_enabled or False

  @team_up_enabled.setter
  def team_up_enabled(self, team_up_enabled: Optional[bool]):
    if team_up_enabled is None:
      del self.team_up_enabled
      return
    if not isinstance(team_up_enabled, bool):
      raise TypeError('team_up_enabled must be of type bool')
    self._team_up_enabled = team_up_enabled

  @property
  def team_up_intro(self) -> str:
    return self._team_up_intro or ""

  @team_up_intro.setter
  def team_up_intro(self, team_up_intro: Optional[str]):
    if team_up_intro is None:
      del self.team_up_intro
      return
    if not isinstance(team_up_intro, str):
      raise TypeError('team_up_intro must be of type str')
    self._team_up_intro = team_up_intro

  @property
  def write_up_url(self) -> str:
    """URL linking to a Kaggle discussion post, subject to validation."""
    return self._write_up_url or ""

  @write_up_url.setter
  def write_up_url(self, write_up_url: Optional[str]):
    if write_up_url is None:
      del self.write_up_url
      return
    if not isinstance(write_up_url, str):
      raise TypeError('write_up_url must be of type str')
    self._write_up_url = write_up_url

  @property
  def benchmark_model_version_id(self) -> Optional['BenchmarkModelVersionId']:
    """Admin only. Links the team to a benchmark model version for game arena."""
    return self._benchmark_model_version_id or None

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[Optional['BenchmarkModelVersionId']]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, BenchmarkModelVersionId):
      raise TypeError('benchmark_model_version_id must be of type BenchmarkModelVersionId')
    self._benchmark_model_version_id = benchmark_model_version_id


AcceptTeamMergeRequest._fields = [
  FieldMetadata("mergeRequestId", "merge_request_id", "_merge_request_id", int, 0, PredefinedSerializer()),
]

BatchGetUserTeamsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BatchGetUserTeamsResponse.UserResult._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("team", "team", "_team", Team, None, KaggleObjectSerializer()),
]

BatchGetUserTeamsResponse._fields = [
  FieldMetadata("userResults", "user_results", "_user_results", BatchGetUserTeamsResponse.UserResult, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkModelVersionId._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
]

CreateTeamFileRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("blobToken", "blob_token", "_blob_token", str, "", PredefinedSerializer()),
]

CreateTeamFileResponse._fields = [
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("sizeBytes", "size_bytes", "_size_bytes", int, 0, PredefinedSerializer()),
]

CreateTeamsInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("leaderId", "leader_id", "_leader_id", int, 0, PredefinedSerializer()),
  FieldMetadata("memberIds", "member_ids", "_member_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
]

CreateTeamsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teams", "teams", "_teams", CreateTeamsInfo, [], ListSerializer(KaggleObjectSerializer())),
]

CreateTeamsResponse._fields = [
  FieldMetadata("teams", "teams", "_teams", CreateTeamsInfo, [], ListSerializer(KaggleObjectSerializer())),
]

DownloadTeamFileRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
]

DownloadTeamFileResponse._fields = [
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, "", PredefinedSerializer()),
]

GetTeamFileRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
]

GetTeamRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
]

GetTeamUpForUsersRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetTeamUpForUsersResponse._fields = [
  FieldMetadata("teamUpState", "team_up_state", "_team_up_state", TeamUpInfo, {}, MapSerializer(KaggleObjectSerializer())),
]

InvalidateOrphanedTeamsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

InvalidateOrphanedTeamsResponse._fields = [
  FieldMetadata("numInvalidated", "num_invalidated", "_num_invalidated", int, 0, PredefinedSerializer()),
]

ListTeamMergeRequestsRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
]

ListTeamMergeRequestsResponse._fields = [
  FieldMetadata("inbound", "inbound", "_inbound", TeamMergeRequest, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("outbound", "outbound", "_outbound", TeamMergeRequest, [], ListSerializer(KaggleObjectSerializer())),
]

ListTeamsByUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

ListTeamsByUserResponse._fields = [
  FieldMetadata("teams", "teams", "_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
]

RejectTeamMergeRequest._fields = [
  FieldMetadata("mergeRequestId", "merge_request_id", "_merge_request_id", int, 0, PredefinedSerializer()),
]

RequestTeamMergeRequest._fields = [
  FieldMetadata("parentTeamId", "parent_team_id", "_parent_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childTeamId", "child_team_id", "_child_team_id", int, 0, PredefinedSerializer()),
]

SearchTeamsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamNamePrefix", "team_name_prefix", "_team_name_prefix", str, "", PredefinedSerializer()),
  FieldMetadata("take", "take", "_take", int, None, PredefinedSerializer(), optional=True),
]

SearchTeamsResponse.FoundTeam._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, "", PredefinedSerializer()),
  FieldMetadata("teamLeader", "team_leader", "_team_leader", UserAvatar, None, KaggleObjectSerializer()),
]

SearchTeamsResponse._fields = [
  FieldMetadata("teams", "teams", "_teams", SearchTeamsResponse.FoundTeam, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teamsDetailed", "teams_detailed", "_teams_detailed", Team, [], ListSerializer(KaggleObjectSerializer())),
]

SetTeamWriteUpRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, None, PredefinedSerializer(), optional=True),
]

UpdateTeamRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamLeaderId", "team_leader_id", "_team_leader_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamUpEnabled", "team_up_enabled", "_team_up_enabled", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamUpIntro", "team_up_intro", "_team_up_intro", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("writeUpUrl", "write_up_url", "_write_up_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", BenchmarkModelVersionId, None, KaggleObjectSerializer(), optional=True),
]

