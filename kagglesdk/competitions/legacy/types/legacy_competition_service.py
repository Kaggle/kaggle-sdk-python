import enum
from kagglesdk.competitions.types.competition_enums import CompetitionDatabundleType
from kagglesdk.datasets.types.dataset_service import CompetitionDatabundleVersion
from kagglesdk.kaggle_object import *
from typing import Optional, List

class CompetitionTeamSortBy(enum.Enum):
  RANK = 0
  PUBLIC_SCORE_ASC = 1
  PUBLIC_SCORE_DESC = 2
  PRIVATE_SCORE_ASC = 3
  PRIVATE_SCORE_DESC = 4

class TeamType(enum.Enum):
  TEAM_TYPE_UNSPECIFIED = 0
  TEAM_TYPE_RANKED = 1
  TEAM_TYPE_UNRANKED = 2

class CompetitionTeamInfoDto(KaggleObject):
  r"""
  Attributes:
    id (int)
    rank (int)
    name (str)
    entries (int)
    public_score (str)
    download_team_model_url (str)
    private_score (str)
    is_hidden (bool)
      Unfortunately this uses the CreatedAfterDeadline hack, but we should clean
      up with the team state refactor
    benchmark_model_version_id (int)
      Benchmark Model Version ID that is linked to a team for game arena.
  """

  def __init__(self):
    self._id = 0
    self._rank = None
    self._name = None
    self._entries = 0
    self._public_score = None
    self._download_team_model_url = None
    self._private_score = None
    self._is_hidden = False
    self._benchmark_model_version_id = None
    self._freeze()

  @property
  def id(self) -> int:
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
  def rank(self) -> int:
    return self._rank or 0

  @rank.setter
  def rank(self, rank: Optional[int]):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def entries(self) -> int:
    return self._entries

  @entries.setter
  def entries(self, entries: int):
    if entries is None:
      del self.entries
      return
    if not isinstance(entries, int):
      raise TypeError('entries must be of type int')
    self._entries = entries

  @property
  def public_score(self) -> str:
    return self._public_score or ""

  @public_score.setter
  def public_score(self, public_score: Optional[str]):
    if public_score is None:
      del self.public_score
      return
    if not isinstance(public_score, str):
      raise TypeError('public_score must be of type str')
    self._public_score = public_score

  @property
  def download_team_model_url(self) -> str:
    return self._download_team_model_url or ""

  @download_team_model_url.setter
  def download_team_model_url(self, download_team_model_url: Optional[str]):
    if download_team_model_url is None:
      del self.download_team_model_url
      return
    if not isinstance(download_team_model_url, str):
      raise TypeError('download_team_model_url must be of type str')
    self._download_team_model_url = download_team_model_url

  @property
  def private_score(self) -> str:
    return self._private_score or ""

  @private_score.setter
  def private_score(self, private_score: Optional[str]):
    if private_score is None:
      del self.private_score
      return
    if not isinstance(private_score, str):
      raise TypeError('private_score must be of type str')
    self._private_score = private_score

  @property
  def is_hidden(self) -> bool:
    r"""
    Unfortunately this uses the CreatedAfterDeadline hack, but we should clean
    up with the team state refactor
    """
    return self._is_hidden

  @is_hidden.setter
  def is_hidden(self, is_hidden: bool):
    if is_hidden is None:
      del self.is_hidden
      return
    if not isinstance(is_hidden, bool):
      raise TypeError('is_hidden must be of type bool')
    self._is_hidden = is_hidden

  @property
  def benchmark_model_version_id(self) -> int:
    """Benchmark Model Version ID that is linked to a team for game arena."""
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id


class GetCompetitionDatabundleVersionsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_databundle_type (CompetitionDatabundleType)
  """

  def __init__(self):
    self._competition_id = 0
    self._competition_databundle_type = CompetitionDatabundleType.COMPETITION_DATABUNDLE_TYPE_UNSPECIFIED
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
  def competition_databundle_type(self) -> 'CompetitionDatabundleType':
    return self._competition_databundle_type

  @competition_databundle_type.setter
  def competition_databundle_type(self, competition_databundle_type: 'CompetitionDatabundleType'):
    if competition_databundle_type is None:
      del self.competition_databundle_type
      return
    if not isinstance(competition_databundle_type, CompetitionDatabundleType):
      raise TypeError('competition_databundle_type must be of type CompetitionDatabundleType')
    self._competition_databundle_type = competition_databundle_type


class GetCompetitionDatabundleVersionsResponse(KaggleObject):
  r"""
  Attributes:
    databundle_versions (CompetitionDatabundleVersion)
  """

  def __init__(self):
    self._databundle_versions = []
    self._freeze()

  @property
  def databundle_versions(self) -> Optional[List[Optional['CompetitionDatabundleVersion']]]:
    return self._databundle_versions

  @databundle_versions.setter
  def databundle_versions(self, databundle_versions: Optional[List[Optional['CompetitionDatabundleVersion']]]):
    if databundle_versions is None:
      del self.databundle_versions
      return
    if not isinstance(databundle_versions, list):
      raise TypeError('databundle_versions must be of type list')
    if not all([isinstance(t, CompetitionDatabundleVersion) for t in databundle_versions]):
      raise TypeError('databundle_versions must contain only items of type CompetitionDatabundleVersion')
    self._databundle_versions = databundle_versions


class LegacyListTeamsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    sort_by (CompetitionTeamSortBy)
    filter (str)
    team_type (TeamType)
    page (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._sort_by = CompetitionTeamSortBy.RANK
    self._filter = None
    self._team_type = None
    self._page = None
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
  def sort_by(self) -> 'CompetitionTeamSortBy':
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'CompetitionTeamSortBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, CompetitionTeamSortBy):
      raise TypeError('sort_by must be of type CompetitionTeamSortBy')
    self._sort_by = sort_by

  @property
  def filter(self) -> str:
    return self._filter or ""

  @filter.setter
  def filter(self, filter: Optional[str]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, str):
      raise TypeError('filter must be of type str')
    self._filter = filter

  @property
  def team_type(self) -> 'TeamType':
    return self._team_type or TeamType.TEAM_TYPE_UNSPECIFIED

  @team_type.setter
  def team_type(self, team_type: Optional['TeamType']):
    if team_type is None:
      del self.team_type
      return
    if not isinstance(team_type, TeamType):
      raise TypeError('team_type must be of type TeamType')
    self._team_type = team_type

  @property
  def page(self) -> int:
    return self._page or 0

  @page.setter
  def page(self, page: Optional[int]):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page


class LegacyListTeamsResponse(KaggleObject):
  r"""
  Attributes:
    teams_list (CompetitionTeamInfoDto)
    has_more_data (bool)
    total_teams (int)
    total_submissions (int)
  """

  def __init__(self):
    self._teams_list = []
    self._has_more_data = False
    self._total_teams = 0
    self._total_submissions = 0
    self._freeze()

  @property
  def teams_list(self) -> Optional[List[Optional['CompetitionTeamInfoDto']]]:
    return self._teams_list

  @teams_list.setter
  def teams_list(self, teams_list: Optional[List[Optional['CompetitionTeamInfoDto']]]):
    if teams_list is None:
      del self.teams_list
      return
    if not isinstance(teams_list, list):
      raise TypeError('teams_list must be of type list')
    if not all([isinstance(t, CompetitionTeamInfoDto) for t in teams_list]):
      raise TypeError('teams_list must contain only items of type CompetitionTeamInfoDto')
    self._teams_list = teams_list

  @property
  def has_more_data(self) -> bool:
    return self._has_more_data

  @has_more_data.setter
  def has_more_data(self, has_more_data: bool):
    if has_more_data is None:
      del self.has_more_data
      return
    if not isinstance(has_more_data, bool):
      raise TypeError('has_more_data must be of type bool')
    self._has_more_data = has_more_data

  @property
  def total_teams(self) -> int:
    return self._total_teams

  @total_teams.setter
  def total_teams(self, total_teams: int):
    if total_teams is None:
      del self.total_teams
      return
    if not isinstance(total_teams, int):
      raise TypeError('total_teams must be of type int')
    self._total_teams = total_teams

  @property
  def total_submissions(self) -> int:
    return self._total_submissions

  @total_submissions.setter
  def total_submissions(self, total_submissions: int):
    if total_submissions is None:
      del self.total_submissions
      return
    if not isinstance(total_submissions, int):
      raise TypeError('total_submissions must be of type int')
    self._total_submissions = total_submissions


CompetitionTeamInfoDto._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("entries", "entries", "_entries", int, 0, PredefinedSerializer()),
  FieldMetadata("publicScore", "public_score", "_public_score", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("downloadTeamModelUrl", "download_team_model_url", "_download_team_model_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateScore", "private_score", "_private_score", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isHidden", "is_hidden", "_is_hidden", bool, False, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
]

GetCompetitionDatabundleVersionsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionDatabundleType", "competition_databundle_type", "_competition_databundle_type", CompetitionDatabundleType, CompetitionDatabundleType.COMPETITION_DATABUNDLE_TYPE_UNSPECIFIED, EnumSerializer()),
]

GetCompetitionDatabundleVersionsResponse._fields = [
  FieldMetadata("databundleVersions", "databundle_versions", "_databundle_versions", CompetitionDatabundleVersion, [], ListSerializer(KaggleObjectSerializer())),
]

LegacyListTeamsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sortBy", "sort_by", "_sort_by", CompetitionTeamSortBy, CompetitionTeamSortBy.RANK, EnumSerializer()),
  FieldMetadata("filter", "filter", "_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamType", "team_type", "_team_type", TeamType, None, EnumSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
]

LegacyListTeamsResponse._fields = [
  FieldMetadata("teamsList", "teams_list", "_teams_list", CompetitionTeamInfoDto, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("hasMoreData", "has_more_data", "_has_more_data", bool, False, PredefinedSerializer()),
  FieldMetadata("totalTeams", "total_teams", "_total_teams", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSubmissions", "total_submissions", "_total_submissions", int, 0, PredefinedSerializer()),
]

