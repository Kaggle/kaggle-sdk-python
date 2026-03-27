from datetime import datetime
import enum
from kagglesdk.blobs.types.blob_file import BlobFile
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class TeamMergeRequestState(enum.Enum):
  TEAM_MERGE_REQUEST_STATE_UNSPECIFIED = 0
  REQUESTED = 1
  ACCEPTED = 2
  REJECTED = 3
  DEACTIVATED = 4

class SubmissionLimitInfo(KaggleObject):
  r"""
  Stats about a Team's submissions that count towards daily and global limits,
  and how many submissions they are currently allowed. Implicitly tied to one
  Team, and should only be surfaced to members of that Team for privacy
  reasons.

  Attributes:
    num_today (int)
      Number of valid submissions submitted after the beginning of today UTC.
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    num_total (int)
      Number of valid submissions ever.
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    num_allowed_now (int)
      Number of submissions allowed for the rest of today UTC.
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    limited_by_total (bool)
      Whether num_allowed_now was limited by num_total rather than num_today.
      Very rare, should only occur on the same day that two Teams merge and they
      barely fit under the num_total limit to be a valid merge. In that case, it
      may cause user confusion, so we may want to highlight it in the UI somehow.
  """

  def __init__(self):
    self._num_today = 0
    self._num_total = 0
    self._num_allowed_now = 0
    self._limited_by_total = False
    self._freeze()

  @property
  def num_today(self) -> int:
    r"""
    Number of valid submissions submitted after the beginning of today UTC.
    TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    """
    return self._num_today

  @num_today.setter
  def num_today(self, num_today: int):
    if num_today is None:
      del self.num_today
      return
    if not isinstance(num_today, int):
      raise TypeError('num_today must be of type int')
    self._num_today = num_today

  @property
  def num_total(self) -> int:
    r"""
    Number of valid submissions ever.
    TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    """
    return self._num_total

  @num_total.setter
  def num_total(self, num_total: int):
    if num_total is None:
      del self.num_total
      return
    if not isinstance(num_total, int):
      raise TypeError('num_total must be of type int')
    self._num_total = num_total

  @property
  def num_allowed_now(self) -> int:
    r"""
    Number of submissions allowed for the rest of today UTC.
    TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    """
    return self._num_allowed_now

  @num_allowed_now.setter
  def num_allowed_now(self, num_allowed_now: int):
    if num_allowed_now is None:
      del self.num_allowed_now
      return
    if not isinstance(num_allowed_now, int):
      raise TypeError('num_allowed_now must be of type int')
    self._num_allowed_now = num_allowed_now

  @property
  def limited_by_total(self) -> bool:
    r"""
    Whether num_allowed_now was limited by num_total rather than num_today.
    Very rare, should only occur on the same day that two Teams merge and they
    barely fit under the num_total limit to be a valid merge. In that case, it
    may cause user confusion, so we may want to highlight it in the UI somehow.
    """
    return self._limited_by_total

  @limited_by_total.setter
  def limited_by_total(self, limited_by_total: bool):
    if limited_by_total is None:
      del self.limited_by_total
      return
    if not isinstance(limited_by_total, bool):
      raise TypeError('limited_by_total must be of type bool')
    self._limited_by_total = limited_by_total


class Team(KaggleObject):
  r"""
  Attributes:
    id (int)
    team_name (str)
    competition_id (int)
      The ID of the competition that the team is entered in.
    team_leader_id (int)
      The userId of the team leader. Can be referenced with team_members to
      determine the user name.
    medal (int)
      The current medal placement of this team.  If comp is finalized, uses
      the stored value representing final private leaderboard rank; otherwise
      uses current public leaderboard rank.  Value corresponds with
      Users.Medal.
    submission_count (int)
      The number of leaderboard-valid submissions that this team has made
      (submissions made before deadline with status Complete). This may differ
      from counts related to submission limits, eg Pending submissions count
      towards limits but not the leaderboard.
    last_submission_date (datetime)
      The date of this team's latest submission.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    public_leaderboard_submission_id (int)
      This will be kept up-to-date while comp is ongoing, if the Team has
      valid submissions.
    public_leaderboard_score_formatted (str)
      This will be kept up-to-date while comp is ongoing.
      This is intended to be a dupe of PublicLeaderboardSubmission.PublicScore
      which is not ideal, but improves performance of GetLeaderboard.
    public_leaderboard_rank (int)
      This will be written when the comp is finalized and LB is 'locked'.
    private_leaderboard_submission_id (int)
      This will be written when the comp is finalized and LB is 'locked'.
    private_leaderboard_score_formatted (str)
      This will be written when the comp is finalized and LB is 'locked'.
      This is intended to be a dupe of PrivateLeaderboardSubmission.PrivateScore
      which is not ideal, but improves performance of GetLeaderboard.
    private_leaderboard_rank (int)
      This will be written when the comp is finalized and LB is 'locked'.
    team_up_enabled (bool)
      Whether this team has indicated that they are open to teaming up.
    team_up_intro (str)
      If this team opted into team up, their optional intro message for
      prospective teammates on the leaderboard.
    write_up_forum_topic_id (int)
      ForumTopic of the team's solution writeup, if set.
    benchmark_model_version_id (int)
      Linked benchmark model version, if set.
    team_members (UserAvatar)
      The list of users on the team.
  """

  def __init__(self):
    self._id = 0
    self._team_name = ""
    self._competition_id = 0
    self._team_leader_id = None
    self._medal = None
    self._submission_count = None
    self._last_submission_date = None
    self._public_leaderboard_submission_id = None
    self._public_leaderboard_score_formatted = None
    self._public_leaderboard_rank = None
    self._private_leaderboard_submission_id = None
    self._private_leaderboard_score_formatted = None
    self._private_leaderboard_rank = None
    self._team_up_enabled = False
    self._team_up_intro = None
    self._write_up_forum_topic_id = None
    self._benchmark_model_version_id = None
    self._team_members = []
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
  def competition_id(self) -> int:
    """The ID of the competition that the team is entered in."""
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
  def team_leader_id(self) -> int:
    r"""
    The userId of the team leader. Can be referenced with team_members to
    determine the user name.
    """
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
  def medal(self) -> int:
    r"""
    The current medal placement of this team.  If comp is finalized, uses
    the stored value representing final private leaderboard rank; otherwise
    uses current public leaderboard rank.  Value corresponds with
    Users.Medal.
    """
    return self._medal or 0

  @medal.setter
  def medal(self, medal: Optional[int]):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, int):
      raise TypeError('medal must be of type int')
    self._medal = medal

  @property
  def submission_count(self) -> int:
    r"""
    The number of leaderboard-valid submissions that this team has made
    (submissions made before deadline with status Complete). This may differ
    from counts related to submission limits, eg Pending submissions count
    towards limits but not the leaderboard.
    """
    return self._submission_count or 0

  @submission_count.setter
  def submission_count(self, submission_count: Optional[int]):
    if submission_count is None:
      del self.submission_count
      return
    if not isinstance(submission_count, int):
      raise TypeError('submission_count must be of type int')
    self._submission_count = submission_count

  @property
  def last_submission_date(self) -> datetime:
    r"""
    The date of this team's latest submission.
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
  def public_leaderboard_submission_id(self) -> int:
    r"""
    This will be kept up-to-date while comp is ongoing, if the Team has
    valid submissions.
    """
    return self._public_leaderboard_submission_id or 0

  @public_leaderboard_submission_id.setter
  def public_leaderboard_submission_id(self, public_leaderboard_submission_id: Optional[int]):
    if public_leaderboard_submission_id is None:
      del self.public_leaderboard_submission_id
      return
    if not isinstance(public_leaderboard_submission_id, int):
      raise TypeError('public_leaderboard_submission_id must be of type int')
    self._public_leaderboard_submission_id = public_leaderboard_submission_id

  @property
  def public_leaderboard_score_formatted(self) -> str:
    r"""
    This will be kept up-to-date while comp is ongoing.
    This is intended to be a dupe of PublicLeaderboardSubmission.PublicScore
    which is not ideal, but improves performance of GetLeaderboard.
    """
    return self._public_leaderboard_score_formatted or ""

  @public_leaderboard_score_formatted.setter
  def public_leaderboard_score_formatted(self, public_leaderboard_score_formatted: Optional[str]):
    if public_leaderboard_score_formatted is None:
      del self.public_leaderboard_score_formatted
      return
    if not isinstance(public_leaderboard_score_formatted, str):
      raise TypeError('public_leaderboard_score_formatted must be of type str')
    self._public_leaderboard_score_formatted = public_leaderboard_score_formatted

  @property
  def public_leaderboard_rank(self) -> int:
    """This will be written when the comp is finalized and LB is 'locked'."""
    return self._public_leaderboard_rank or 0

  @public_leaderboard_rank.setter
  def public_leaderboard_rank(self, public_leaderboard_rank: Optional[int]):
    if public_leaderboard_rank is None:
      del self.public_leaderboard_rank
      return
    if not isinstance(public_leaderboard_rank, int):
      raise TypeError('public_leaderboard_rank must be of type int')
    self._public_leaderboard_rank = public_leaderboard_rank

  @property
  def private_leaderboard_submission_id(self) -> int:
    """This will be written when the comp is finalized and LB is 'locked'."""
    return self._private_leaderboard_submission_id or 0

  @private_leaderboard_submission_id.setter
  def private_leaderboard_submission_id(self, private_leaderboard_submission_id: Optional[int]):
    if private_leaderboard_submission_id is None:
      del self.private_leaderboard_submission_id
      return
    if not isinstance(private_leaderboard_submission_id, int):
      raise TypeError('private_leaderboard_submission_id must be of type int')
    self._private_leaderboard_submission_id = private_leaderboard_submission_id

  @property
  def private_leaderboard_score_formatted(self) -> str:
    r"""
    This will be written when the comp is finalized and LB is 'locked'.
    This is intended to be a dupe of PrivateLeaderboardSubmission.PrivateScore
    which is not ideal, but improves performance of GetLeaderboard.
    """
    return self._private_leaderboard_score_formatted or ""

  @private_leaderboard_score_formatted.setter
  def private_leaderboard_score_formatted(self, private_leaderboard_score_formatted: Optional[str]):
    if private_leaderboard_score_formatted is None:
      del self.private_leaderboard_score_formatted
      return
    if not isinstance(private_leaderboard_score_formatted, str):
      raise TypeError('private_leaderboard_score_formatted must be of type str')
    self._private_leaderboard_score_formatted = private_leaderboard_score_formatted

  @property
  def private_leaderboard_rank(self) -> int:
    """This will be written when the comp is finalized and LB is 'locked'."""
    return self._private_leaderboard_rank or 0

  @private_leaderboard_rank.setter
  def private_leaderboard_rank(self, private_leaderboard_rank: Optional[int]):
    if private_leaderboard_rank is None:
      del self.private_leaderboard_rank
      return
    if not isinstance(private_leaderboard_rank, int):
      raise TypeError('private_leaderboard_rank must be of type int')
    self._private_leaderboard_rank = private_leaderboard_rank

  @property
  def team_up_enabled(self) -> bool:
    """Whether this team has indicated that they are open to teaming up."""
    return self._team_up_enabled

  @team_up_enabled.setter
  def team_up_enabled(self, team_up_enabled: bool):
    if team_up_enabled is None:
      del self.team_up_enabled
      return
    if not isinstance(team_up_enabled, bool):
      raise TypeError('team_up_enabled must be of type bool')
    self._team_up_enabled = team_up_enabled

  @property
  def team_up_intro(self) -> str:
    r"""
    If this team opted into team up, their optional intro message for
    prospective teammates on the leaderboard.
    """
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
  def write_up_forum_topic_id(self) -> int:
    """ForumTopic of the team's solution writeup, if set."""
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
  def benchmark_model_version_id(self) -> int:
    """Linked benchmark model version, if set."""
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

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


class TeamFile(KaggleObject):
  r"""
  Attributes:
    blob_file (BlobFile)
  """

  def __init__(self):
    self._blob_file = None
    self._freeze()

  @property
  def blob_file(self) -> Optional['BlobFile']:
    return self._blob_file

  @blob_file.setter
  def blob_file(self, blob_file: Optional['BlobFile']):
    if blob_file is None:
      del self.blob_file
      return
    if not isinstance(blob_file, BlobFile):
      raise TypeError('blob_file must be of type BlobFile')
    self._blob_file = blob_file


class TeamMergeRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    child_team_id (int)
    parent_team_id (int)
    state (TeamMergeRequestState)
    date_initiated (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    date_updated (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    child_team (Team)
    parent_team (Team)
  """

  def __init__(self):
    self._id = 0
    self._child_team_id = 0
    self._parent_team_id = 0
    self._state = TeamMergeRequestState.TEAM_MERGE_REQUEST_STATE_UNSPECIFIED
    self._date_initiated = None
    self._date_updated = None
    self._child_team = None
    self._parent_team = None
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
  def state(self) -> 'TeamMergeRequestState':
    return self._state

  @state.setter
  def state(self, state: 'TeamMergeRequestState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, TeamMergeRequestState):
      raise TypeError('state must be of type TeamMergeRequestState')
    self._state = state

  @property
  def date_initiated(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_initiated

  @date_initiated.setter
  def date_initiated(self, date_initiated: datetime):
    if date_initiated is None:
      del self.date_initiated
      return
    if not isinstance(date_initiated, datetime):
      raise TypeError('date_initiated must be of type datetime')
    self._date_initiated = date_initiated

  @property
  def date_updated(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_updated

  @date_updated.setter
  def date_updated(self, date_updated: datetime):
    if date_updated is None:
      del self.date_updated
      return
    if not isinstance(date_updated, datetime):
      raise TypeError('date_updated must be of type datetime')
    self._date_updated = date_updated

  @property
  def child_team(self) -> Optional['Team']:
    return self._child_team

  @child_team.setter
  def child_team(self, child_team: Optional['Team']):
    if child_team is None:
      del self.child_team
      return
    if not isinstance(child_team, Team):
      raise TypeError('child_team must be of type Team')
    self._child_team = child_team

  @property
  def parent_team(self) -> Optional['Team']:
    return self._parent_team

  @parent_team.setter
  def parent_team(self, parent_team: Optional['Team']):
    if parent_team is None:
      del self.parent_team
      return
    if not isinstance(parent_team, Team):
      raise TypeError('parent_team must be of type Team')
    self._parent_team = parent_team


class TeamUpInfo(KaggleObject):
  r"""
  Attributes:
    enabled (bool)
    team_leader (UserAvatar)
    intro (str)
  """

  def __init__(self):
    self._enabled = False
    self._team_leader = None
    self._intro = None
    self._freeze()

  @property
  def enabled(self) -> bool:
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled

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

  @property
  def intro(self) -> str:
    return self._intro or ""

  @intro.setter
  def intro(self, intro: Optional[str]):
    if intro is None:
      del self.intro
      return
    if not isinstance(intro, str):
      raise TypeError('intro must be of type str')
    self._intro = intro


SubmissionLimitInfo._fields = [
  FieldMetadata("numToday", "num_today", "_num_today", int, 0, PredefinedSerializer()),
  FieldMetadata("numTotal", "num_total", "_num_total", int, 0, PredefinedSerializer()),
  FieldMetadata("numAllowedNow", "num_allowed_now", "_num_allowed_now", int, 0, PredefinedSerializer()),
  FieldMetadata("limitedByTotal", "limited_by_total", "_limited_by_total", bool, False, PredefinedSerializer()),
]

Team._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, "", PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamLeaderId", "team_leader_id", "_team_leader_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionCount", "submission_count", "_submission_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastSubmissionDate", "last_submission_date", "_last_submission_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("publicLeaderboardSubmissionId", "public_leaderboard_submission_id", "_public_leaderboard_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publicLeaderboardScoreFormatted", "public_leaderboard_score_formatted", "_public_leaderboard_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publicLeaderboardRank", "public_leaderboard_rank", "_public_leaderboard_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateLeaderboardSubmissionId", "private_leaderboard_submission_id", "_private_leaderboard_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateLeaderboardScoreFormatted", "private_leaderboard_score_formatted", "_private_leaderboard_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateLeaderboardRank", "private_leaderboard_rank", "_private_leaderboard_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamUpEnabled", "team_up_enabled", "_team_up_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("teamUpIntro", "team_up_intro", "_team_up_intro", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("writeUpForumTopicId", "write_up_forum_topic_id", "_write_up_forum_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamMembers", "team_members", "_team_members", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
]

TeamFile._fields = [
  FieldMetadata("blobFile", "blob_file", "_blob_file", BlobFile, None, KaggleObjectSerializer()),
]

TeamMergeRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childTeamId", "child_team_id", "_child_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentTeamId", "parent_team_id", "_parent_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", TeamMergeRequestState, TeamMergeRequestState.TEAM_MERGE_REQUEST_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dateInitiated", "date_initiated", "_date_initiated", datetime, None, DateTimeSerializer()),
  FieldMetadata("dateUpdated", "date_updated", "_date_updated", datetime, None, DateTimeSerializer()),
  FieldMetadata("childTeam", "child_team", "_child_team", Team, None, KaggleObjectSerializer()),
  FieldMetadata("parentTeam", "parent_team", "_parent_team", Team, None, KaggleObjectSerializer()),
]

TeamUpInfo._fields = [
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("teamLeader", "team_leader", "_team_leader", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("intro", "intro", "_intro", str, None, PredefinedSerializer(), optional=True),
]

