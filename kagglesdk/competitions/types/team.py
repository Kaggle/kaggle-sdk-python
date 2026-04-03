from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

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

TeamUpInfo._fields = [
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("teamLeader", "team_leader", "_team_leader", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("intro", "intro", "_intro", str, None, PredefinedSerializer(), optional=True),
]

