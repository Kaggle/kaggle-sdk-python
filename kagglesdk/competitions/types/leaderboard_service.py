from datetime import datetime
import enum
from kagglesdk.competitions.types.team import Team, TeamUpInfo
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List, Dict

class LeaderboardMode(enum.Enum):
  LEADERBOARD_MODE_DEFAULT = 0
  r"""
  Default indicates to decide between Weak or Strong based on the
  competition's current state.
  For read operations like GetLeaderboard and GetRanksForUsers, Strong is
  used if the competition is completed, private LB is visible, and
  Strong LB has been written; otherwise Weak is used.
  RecalculateLeaderboard will do the full Strong LB generation (in addition
  to Weak) if the comp is completed, otherwise Weak.
  TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)
  """
  LEADERBOARD_MODE_WEAK = 1
  r"""
  Weak Leaderboard means it only uses localized caching of the best public
  submission per team, stored in the Teams.PublicLeaderboard[SubmissionId,
  Score, Date] fields (note -Rank is not used).
  These fields should be kept current synchronously as the comp
  progresses, along with Teams' SubmissionCount and LastSubmissionDate
  fields.
  GetLeaderboard in Weak mode will use the cached data to efficiently get
  the public LB.  The private LB, which should only be available to admins
  while Weak is the default, will require a more expensive full calculation.
  RecalculateLeaderboard in Weak mode will recalculate the Team-localized
  cached data described above, although ideally those fields are kept in
  sync already.
  """
  LEADERBOARD_MODE_STRONG = 2
  r"""
  Strong Leaderboard caches full information about both public and private
  LBs within the Teams table, including competition-wide Ranks.
  These fields are only written by RecalculateLeaderboard, which can be
  invoked manually by admins, or by a forthcoming ScheduledHandler which
  looks for Competitions which have ended but haven't calculated their
  Strong Leaderboard.
  We track whether a Competition has calculated its Strong Leaderboard via
  Competitions.LeaderboardCacheDate field.
  GetLeaderboard in Strong mode will be able to get Public and Private LBs
  efficiently for all users.
  """

class GetLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition to get the leaderboard for.
    leaderboard_mode (LeaderboardMode)
      Must be admin to set to non-default value.
      Determines which level of LB caching to draw data from.
  """

  def __init__(self):
    self._competition_id = 0
    self._leaderboard_mode = LeaderboardMode.LEADERBOARD_MODE_DEFAULT
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition to get the leaderboard for."""
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
  def leaderboard_mode(self) -> 'LeaderboardMode':
    r"""
    Must be admin to set to non-default value.
    Determines which level of LB caching to draw data from.
    """
    return self._leaderboard_mode

  @leaderboard_mode.setter
  def leaderboard_mode(self, leaderboard_mode: 'LeaderboardMode'):
    if leaderboard_mode is None:
      del self.leaderboard_mode
      return
    if not isinstance(leaderboard_mode, LeaderboardMode):
      raise TypeError('leaderboard_mode must be of type LeaderboardMode')
    self._leaderboard_mode = leaderboard_mode


class GetLeaderboardResponse(KaggleObject):
  r"""
  Attributes:
    public_leaderboard (LeaderboardEntry)
      List of all entries on the leaderboard, including benchmark teams.
      Sorted by rank-order; benchmark teams are in their correct location per
      score, though their rank is 0 since they are not a real team.
    private_leaderboard (LeaderboardEntry)
      Same as above, but for Private LB, provided the Current User can view the
      Private LB. If not, this will be empty.
    teams (LeaderboardTeam)
      The unordered list of Leaderboard teams.  This should be treated as a
      dictionary into which each LeaderboardEntry above can lookup using TeamId
      to get more detailed information, such as TeamName and TeamMembers.
  """

  def __init__(self):
    self._public_leaderboard = []
    self._private_leaderboard = []
    self._teams = []
    self._freeze()

  @property
  def public_leaderboard(self) -> Optional[List[Optional['LeaderboardEntry']]]:
    r"""
    List of all entries on the leaderboard, including benchmark teams.
    Sorted by rank-order; benchmark teams are in their correct location per
    score, though their rank is 0 since they are not a real team.
    """
    return self._public_leaderboard

  @public_leaderboard.setter
  def public_leaderboard(self, public_leaderboard: Optional[List[Optional['LeaderboardEntry']]]):
    if public_leaderboard is None:
      del self.public_leaderboard
      return
    if not isinstance(public_leaderboard, list):
      raise TypeError('public_leaderboard must be of type list')
    if not all([isinstance(t, LeaderboardEntry) for t in public_leaderboard]):
      raise TypeError('public_leaderboard must contain only items of type LeaderboardEntry')
    self._public_leaderboard = public_leaderboard

  @property
  def private_leaderboard(self) -> Optional[List[Optional['LeaderboardEntry']]]:
    r"""
    Same as above, but for Private LB, provided the Current User can view the
    Private LB. If not, this will be empty.
    """
    return self._private_leaderboard

  @private_leaderboard.setter
  def private_leaderboard(self, private_leaderboard: Optional[List[Optional['LeaderboardEntry']]]):
    if private_leaderboard is None:
      del self.private_leaderboard
      return
    if not isinstance(private_leaderboard, list):
      raise TypeError('private_leaderboard must be of type list')
    if not all([isinstance(t, LeaderboardEntry) for t in private_leaderboard]):
      raise TypeError('private_leaderboard must contain only items of type LeaderboardEntry')
    self._private_leaderboard = private_leaderboard

  @property
  def teams(self) -> Optional[List[Optional['LeaderboardTeam']]]:
    r"""
    The unordered list of Leaderboard teams.  This should be treated as a
    dictionary into which each LeaderboardEntry above can lookup using TeamId
    to get more detailed information, such as TeamName and TeamMembers.
    """
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['LeaderboardTeam']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, LeaderboardTeam) for t in teams]):
      raise TypeError('teams must contain only items of type LeaderboardTeam')
    self._teams = teams


class GetRanksForUsersRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition to get the leaderboard for.
    user_ids (int)
      The userIds to lookup Ranks for.
  """

  def __init__(self):
    self._competition_id = 0
    self._user_ids = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition to get the leaderboard for."""
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
    """The userIds to lookup Ranks for."""
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


class GetRanksForUsersResponse(KaggleObject):
  r"""
  Attributes:
    user_ranks (int)
      Maps userId to rank.  If a provided userId is missing here, it means
      they didn't have a Team on the current main (public vs private)
      Leaderboard.
  """

  def __init__(self):
    self._user_ranks = {}
    self._freeze()

  @property
  def user_ranks(self) -> Optional[Dict[int, int]]:
    r"""
    Maps userId to rank.  If a provided userId is missing here, it means
    they didn't have a Team on the current main (public vs private)
    Leaderboard.
    """
    return self._user_ranks

  @user_ranks.setter
  def user_ranks(self, user_ranks: Optional[Dict[int, int]]):
    if user_ranks is None:
      del self.user_ranks
      return
    if not isinstance(user_ranks, dict):
      raise TypeError('user_ranks must be of type dict')
    if not all([isinstance(v, int) for k, v in user_ranks]):
      raise TypeError('user_ranks must contain only items of type int')
    self._user_ranks = user_ranks


class LeaderboardEntry(KaggleObject):
  r"""
  Attributes:
    team_id (int)
      The Id of the team who made the entry.
    submission_id (int)
      The Id of the Team's Submission representing this entry.
    rank (int)
      The rank of the entry. Should only be 0 for benchmark teams.
    display_score (str)
      The score for this entry, possibly truncated.
    medal (Medal)
      The medal for this entry and the leaderboard it's on.  If the competition
      is finalized, we'll use the true Team.Medal values on the final LB (public
      LB if comp has no private LB, otherwise private).  Otherwise, we estimate
      the medal given current standings and Team Count.
    in_the_money (bool)
      Whether this entry qualifies as a prize recipient by being in the top N
      teams where N is Competition.NumPrizes (though also subject to other flags)
      Set for both Public and Private LBs.
    rank_delta (int)
      The delta between the private and public leaderboard rank for the private
      leaderboard Currently calculated by the client - but maybe calculated by
      the service in the future. (public rank - private rank)
    solution_write_up_url (str)
      The URL of the Solution WriteUp.
  """

  def __init__(self):
    self._team_id = 0
    self._submission_id = 0
    self._rank = 0
    self._display_score = ""
    self._medal = Medal.MEDAL_UNSPECIFIED
    self._in_the_money = False
    self._rank_delta = 0
    self._solution_write_up_url = ""
    self._freeze()

  @property
  def team_id(self) -> int:
    """The Id of the team who made the entry."""
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
  def submission_id(self) -> int:
    """The Id of the Team's Submission representing this entry."""
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: int):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def rank(self) -> int:
    """The rank of the entry. Should only be 0 for benchmark teams."""
    return self._rank

  @rank.setter
  def rank(self, rank: int):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

  @property
  def display_score(self) -> str:
    """The score for this entry, possibly truncated."""
    return self._display_score

  @display_score.setter
  def display_score(self, display_score: str):
    if display_score is None:
      del self.display_score
      return
    if not isinstance(display_score, str):
      raise TypeError('display_score must be of type str')
    self._display_score = display_score

  @property
  def medal(self) -> 'Medal':
    r"""
    The medal for this entry and the leaderboard it's on.  If the competition
    is finalized, we'll use the true Team.Medal values on the final LB (public
    LB if comp has no private LB, otherwise private).  Otherwise, we estimate
    the medal given current standings and Team Count.
    """
    return self._medal

  @medal.setter
  def medal(self, medal: 'Medal'):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def in_the_money(self) -> bool:
    r"""
    Whether this entry qualifies as a prize recipient by being in the top N
    teams where N is Competition.NumPrizes (though also subject to other flags)
    Set for both Public and Private LBs.
    """
    return self._in_the_money

  @in_the_money.setter
  def in_the_money(self, in_the_money: bool):
    if in_the_money is None:
      del self.in_the_money
      return
    if not isinstance(in_the_money, bool):
      raise TypeError('in_the_money must be of type bool')
    self._in_the_money = in_the_money

  @property
  def rank_delta(self) -> int:
    r"""
    The delta between the private and public leaderboard rank for the private
    leaderboard Currently calculated by the client - but maybe calculated by
    the service in the future. (public rank - private rank)
    """
    return self._rank_delta

  @rank_delta.setter
  def rank_delta(self, rank_delta: int):
    if rank_delta is None:
      del self.rank_delta
      return
    if not isinstance(rank_delta, int):
      raise TypeError('rank_delta must be of type int')
    self._rank_delta = rank_delta

  @property
  def solution_write_up_url(self) -> str:
    """The URL of the Solution WriteUp."""
    return self._solution_write_up_url

  @solution_write_up_url.setter
  def solution_write_up_url(self, solution_write_up_url: str):
    if solution_write_up_url is None:
      del self.solution_write_up_url
      return
    if not isinstance(solution_write_up_url, str):
      raise TypeError('solution_write_up_url must be of type str')
    self._solution_write_up_url = solution_write_up_url


class LeaderboardTeam(KaggleObject):
  r"""
  Subset of Team object to limit return object size, as well as allowing us
  to read from covering indexes for optimal DB performance.

  Attributes:
    team_id (int)
    team_name (str)
    is_benchmark (bool)
    submission_count (int)
    last_submission_date (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    team_up_info (TeamUpInfo)
      TeamUp and WriteUp related fields
      Team Up is only available on the weak leaderboard, and team leader ID is
      only needed by Team Up, so it will be unset on the strong leaderboard.
    write_up_forum_topic_id (int)
    team_members (UserAvatar)
      The list of users on the team.
    solution_write_up_url (str)
  """

  def __init__(self):
    self._team_id = 0
    self._team_name = ""
    self._is_benchmark = False
    self._submission_count = 0
    self._last_submission_date = None
    self._team_up_info = None
    self._write_up_forum_topic_id = None
    self._team_members = []
    self._solution_write_up_url = None
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
  def is_benchmark(self) -> bool:
    return self._is_benchmark

  @is_benchmark.setter
  def is_benchmark(self, is_benchmark: bool):
    if is_benchmark is None:
      del self.is_benchmark
      return
    if not isinstance(is_benchmark, bool):
      raise TypeError('is_benchmark must be of type bool')
    self._is_benchmark = is_benchmark

  @property
  def submission_count(self) -> int:
    return self._submission_count

  @submission_count.setter
  def submission_count(self, submission_count: int):
    if submission_count is None:
      del self.submission_count
      return
    if not isinstance(submission_count, int):
      raise TypeError('submission_count must be of type int')
    self._submission_count = submission_count

  @property
  def last_submission_date(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._last_submission_date

  @last_submission_date.setter
  def last_submission_date(self, last_submission_date: datetime):
    if last_submission_date is None:
      del self.last_submission_date
      return
    if not isinstance(last_submission_date, datetime):
      raise TypeError('last_submission_date must be of type datetime')
    self._last_submission_date = last_submission_date

  @property
  def team_up_info(self) -> Optional['TeamUpInfo']:
    r"""
    TeamUp and WriteUp related fields
    Team Up is only available on the weak leaderboard, and team leader ID is
    only needed by Team Up, so it will be unset on the strong leaderboard.
    """
    return self._team_up_info

  @team_up_info.setter
  def team_up_info(self, team_up_info: Optional['TeamUpInfo']):
    if team_up_info is None:
      del self.team_up_info
      return
    if not isinstance(team_up_info, TeamUpInfo):
      raise TypeError('team_up_info must be of type TeamUpInfo')
    self._team_up_info = team_up_info

  @property
  def write_up_forum_topic_id(self) -> int:
    return self._write_up_forum_topic_id or 0

  @write_up_forum_topic_id.setter
  def write_up_forum_topic_id(self, write_up_forum_topic_id: Optional[int]):
    if write_up_forum_topic_id is None:
      del self.write_up_forum_topic_id
      return
    if not isinstance(write_up_forum_topic_id, int):
      raise TypeError('write_up_forum_topic_id must be of type int')
    self._write_up_forum_topic_id = write_up_forum_topic_id

  @property
  def solution_write_up_url(self) -> str:
    return self._solution_write_up_url or ""

  @solution_write_up_url.setter
  def solution_write_up_url(self, solution_write_up_url: Optional[str]):
    if solution_write_up_url is None:
      del self.solution_write_up_url
      return
    if not isinstance(solution_write_up_url, str):
      raise TypeError('solution_write_up_url must be of type str')
    self._solution_write_up_url = solution_write_up_url

  @property
  def team_members(self) -> Optional[List[Optional['UserAvatar']]]:
    """The list of users on the team."""
    return self._team_members

  @team_members.setter
  def team_members(self, team_members: Optional[List[Optional['UserAvatar']]]):
    if team_members is None:
      del self.team_members
      return
    if not isinstance(team_members, list):
      raise TypeError('team_members must be of type list')
    if not all([isinstance(t, UserAvatar) for t in team_members]):
      raise TypeError('team_members must contain only items of type UserAvatar')
    self._team_members = team_members


class LegacyRecalculateLeaderboardRequest(KaggleObject):
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


class LegacyRecalculateLeaderboardResponse(KaggleObject):
  r"""
  Attributes:
    rows_affected (int)
      Number of database rows affected by the leaderboard update.
  """

  def __init__(self):
    self._rows_affected = 0
    self._freeze()

  @property
  def rows_affected(self) -> int:
    """Number of database rows affected by the leaderboard update."""
    return self._rows_affected

  @rows_affected.setter
  def rows_affected(self, rows_affected: int):
    if rows_affected is None:
      del self.rows_affected
      return
    if not isinstance(rows_affected, int):
      raise TypeError('rows_affected must be of type int')
    self._rows_affected = rows_affected


class RecalculateLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    leaderboard_mode (LeaderboardMode)
      If STRONG is provided (or chosen as Default, which is possible even if the
      competition hasn't calculated a Strong LB yet), we will also recalculate
      the Weak LB cached fields.
    dry_run (bool)
      If true, we won't persist changes, but still return updated_teams.
      TODO(aip.dev/142): (-- api-linter: core::0163::synonyms=disabled --)
  """

  def __init__(self):
    self._competition_id = 0
    self._leaderboard_mode = LeaderboardMode.LEADERBOARD_MODE_DEFAULT
    self._dry_run = False
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
  def leaderboard_mode(self) -> 'LeaderboardMode':
    r"""
    If STRONG is provided (or chosen as Default, which is possible even if the
    competition hasn't calculated a Strong LB yet), we will also recalculate
    the Weak LB cached fields.
    """
    return self._leaderboard_mode

  @leaderboard_mode.setter
  def leaderboard_mode(self, leaderboard_mode: 'LeaderboardMode'):
    if leaderboard_mode is None:
      del self.leaderboard_mode
      return
    if not isinstance(leaderboard_mode, LeaderboardMode):
      raise TypeError('leaderboard_mode must be of type LeaderboardMode')
    self._leaderboard_mode = leaderboard_mode

  @property
  def dry_run(self) -> bool:
    r"""
    If true, we won't persist changes, but still return updated_teams.
    TODO(aip.dev/142): (-- api-linter: core::0163::synonyms=disabled --)
    """
    return self._dry_run

  @dry_run.setter
  def dry_run(self, dry_run: bool):
    if dry_run is None:
      del self.dry_run
      return
    if not isinstance(dry_run, bool):
      raise TypeError('dry_run must be of type bool')
    self._dry_run = dry_run


class RecalculateLeaderboardResponse(KaggleObject):
  r"""
  Attributes:
    weak_updated_teams (Team)
      Teams whose Weak LB cached fields had an update.
    strong_updated_teams (Team)
      Teams whose Strong LB cached fields had an update.
  """

  def __init__(self):
    self._weak_updated_teams = []
    self._strong_updated_teams = []
    self._freeze()

  @property
  def weak_updated_teams(self) -> Optional[List[Optional['Team']]]:
    """Teams whose Weak LB cached fields had an update."""
    return self._weak_updated_teams

  @weak_updated_teams.setter
  def weak_updated_teams(self, weak_updated_teams: Optional[List[Optional['Team']]]):
    if weak_updated_teams is None:
      del self.weak_updated_teams
      return
    if not isinstance(weak_updated_teams, list):
      raise TypeError('weak_updated_teams must be of type list')
    if not all([isinstance(t, Team) for t in weak_updated_teams]):
      raise TypeError('weak_updated_teams must contain only items of type Team')
    self._weak_updated_teams = weak_updated_teams

  @property
  def strong_updated_teams(self) -> Optional[List[Optional['Team']]]:
    """Teams whose Strong LB cached fields had an update."""
    return self._strong_updated_teams

  @strong_updated_teams.setter
  def strong_updated_teams(self, strong_updated_teams: Optional[List[Optional['Team']]]):
    if strong_updated_teams is None:
      del self.strong_updated_teams
      return
    if not isinstance(strong_updated_teams, list):
      raise TypeError('strong_updated_teams must be of type list')
    if not all([isinstance(t, Team) for t in strong_updated_teams]):
      raise TypeError('strong_updated_teams must contain only items of type Team')
    self._strong_updated_teams = strong_updated_teams


GetLeaderboardRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("leaderboardMode", "leaderboard_mode", "_leaderboard_mode", LeaderboardMode, LeaderboardMode.LEADERBOARD_MODE_DEFAULT, EnumSerializer()),
]

GetLeaderboardResponse._fields = [
  FieldMetadata("publicLeaderboard", "public_leaderboard", "_public_leaderboard", LeaderboardEntry, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("privateLeaderboard", "private_leaderboard", "_private_leaderboard", LeaderboardEntry, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teams", "teams", "_teams", LeaderboardTeam, [], ListSerializer(KaggleObjectSerializer())),
]

GetRanksForUsersRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetRanksForUsersResponse._fields = [
  FieldMetadata("userRanks", "user_ranks", "_user_ranks", int, {}, MapSerializer(PredefinedSerializer())),
]

LeaderboardEntry._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, 0, PredefinedSerializer()),
  FieldMetadata("displayScore", "display_score", "_display_score", str, "", PredefinedSerializer()),
  FieldMetadata("medal", "medal", "_medal", Medal, Medal.MEDAL_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("inTheMoney", "in_the_money", "_in_the_money", bool, False, PredefinedSerializer()),
  FieldMetadata("rankDelta", "rank_delta", "_rank_delta", int, 0, PredefinedSerializer()),
  FieldMetadata("solutionWriteUpUrl", "solution_write_up_url", "_solution_write_up_url", str, "", PredefinedSerializer()),
]

LeaderboardTeam._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, "", PredefinedSerializer()),
  FieldMetadata("isBenchmark", "is_benchmark", "_is_benchmark", bool, False, PredefinedSerializer()),
  FieldMetadata("submissionCount", "submission_count", "_submission_count", int, 0, PredefinedSerializer()),
  FieldMetadata("lastSubmissionDate", "last_submission_date", "_last_submission_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamUpInfo", "team_up_info", "_team_up_info", TeamUpInfo, None, KaggleObjectSerializer()),
  FieldMetadata("writeUpForumTopicId", "write_up_forum_topic_id", "_write_up_forum_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamMembers", "team_members", "_team_members", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("solutionWriteUpUrl", "solution_write_up_url", "_solution_write_up_url", str, None, PredefinedSerializer(), optional=True),
]

LegacyRecalculateLeaderboardRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

LegacyRecalculateLeaderboardResponse._fields = [
  FieldMetadata("rowsAffected", "rows_affected", "_rows_affected", int, 0, PredefinedSerializer()),
]

RecalculateLeaderboardRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("leaderboardMode", "leaderboard_mode", "_leaderboard_mode", LeaderboardMode, LeaderboardMode.LEADERBOARD_MODE_DEFAULT, EnumSerializer()),
  FieldMetadata("dryRun", "dry_run", "_dry_run", bool, False, PredefinedSerializer()),
]

RecalculateLeaderboardResponse._fields = [
  FieldMetadata("weakUpdatedTeams", "weak_updated_teams", "_weak_updated_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("strongUpdatedTeams", "strong_updated_teams", "_strong_updated_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
]

