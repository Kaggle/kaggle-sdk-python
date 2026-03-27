from datetime import datetime
import enum
from kagglesdk.competitions.types.competition import RewardTypeId
from kagglesdk.competitions.types.competition_enums import HostSegment
from kagglesdk.kaggle_object import *
from typing import Optional

class SearchCompetitionsOrderBy(enum.Enum):
  SEARCH_COMPETITIONS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_COMPETITIONS_ORDER_BY_DEADLINE = 1
  SEARCH_COMPETITIONS_ORDER_BY_PRIZE_VALUE = 2
  SEARCH_COMPETITIONS_ORDER_BY_TEAM_RANK = 3
  SEARCH_COMPETITIONS_ORDER_BY_LAST_SUBMISSION_DATE = 4

class SearchCompetitionsProfileVisibility(enum.Enum):
  SEARCH_COMPETITIONS_PROFILE_VISIBILITY_ANY = 0
  SEARCH_COMPETITIONS_PROFILE_VISIBILITY_VISIBLE = 1
  SEARCH_COMPETITIONS_PROFILE_VISIBILITY_HIDDEN = 2

class SearchCompetitionsRole(enum.Enum):
  SEARCH_COMPETITIONS_ROLE_ANY = 0
  SEARCH_COMPETITIONS_ROLE_HOST = 1
  SEARCH_COMPETITIONS_ROLE_PARTICIPANT = 2
  SEARCH_COMPETITIONS_ROLE_PARTICIPANT_ONLY = 3
  """Excludes competitions user hosted, even if they are also a participant"""
  SEARCH_COMPETITIONS_ROLE_JUDGE = 4

class SearchCompetitionsStatus(enum.Enum):
  SEARCH_COMPETITIONS_STATUS_ANY = 0
  SEARCH_COMPETITIONS_STATUS_ACTIVE = 1
  SEARCH_COMPETITIONS_STATUS_COMPLETE = 2
  SEARCH_COMPETITIONS_STATUS_UNLAUNCHED = 3

class SearchCompetitionsDocument(KaggleObject):
  r"""
  Attributes:
    host_segment (HostSegment)
      The host segment of the Competition
    deadline (datetime)
      The deadline of the Competition
    team_count (int)
      The total number of teams participating in the Competition
    team_rank (int)
      The rank of the current user's team on the Competition
    is_environment_evaluation (bool)
      Whether the Competition has an environment evaluation
    prize_type (RewardTypeId)
      The prize/award type of the Competition
    prize_value (float)
      The prize/award value of the Competition
    is_launched (bool)
      Whether the competition has launched (even if it's ended)
    owner_user_has_joined (bool)
      Whether the owner user (profile user, then current user) has joined the
      competition
    is_limited_participation (bool)
      Whether the competition is a limited participation competition
    only_allow_kernel_submissions (bool)
      Whether only kernel submissions are allowed
    participant_user_id (int)
      Used to generate competition certificate link
    is_current_user_host (bool)
      Whether current user is host for this competition
    is_hidden_on_profile (bool)
      Whether the competition is hidden on user's profile
  """

  def __init__(self):
    self._host_segment = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._deadline = None
    self._team_count = 0
    self._team_rank = None
    self._is_environment_evaluation = False
    self._prize_type = RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED
    self._prize_value = None
    self._is_launched = False
    self._owner_user_has_joined = False
    self._is_limited_participation = False
    self._only_allow_kernel_submissions = False
    self._participant_user_id = 0
    self._is_current_user_host = False
    self._is_hidden_on_profile = False
    self._freeze()

  @property
  def host_segment(self) -> 'HostSegment':
    """The host segment of the Competition"""
    return self._host_segment

  @host_segment.setter
  def host_segment(self, host_segment: 'HostSegment'):
    if host_segment is None:
      del self.host_segment
      return
    if not isinstance(host_segment, HostSegment):
      raise TypeError('host_segment must be of type HostSegment')
    self._host_segment = host_segment

  @property
  def deadline(self) -> datetime:
    """The deadline of the Competition"""
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline

  @property
  def team_count(self) -> int:
    """The total number of teams participating in the Competition"""
    return self._team_count

  @team_count.setter
  def team_count(self, team_count: int):
    if team_count is None:
      del self.team_count
      return
    if not isinstance(team_count, int):
      raise TypeError('team_count must be of type int')
    self._team_count = team_count

  @property
  def team_rank(self) -> int:
    """The rank of the current user's team on the Competition"""
    return self._team_rank or 0

  @team_rank.setter
  def team_rank(self, team_rank: Optional[int]):
    if team_rank is None:
      del self.team_rank
      return
    if not isinstance(team_rank, int):
      raise TypeError('team_rank must be of type int')
    self._team_rank = team_rank

  @property
  def is_environment_evaluation(self) -> bool:
    """Whether the Competition has an environment evaluation"""
    return self._is_environment_evaluation

  @is_environment_evaluation.setter
  def is_environment_evaluation(self, is_environment_evaluation: bool):
    if is_environment_evaluation is None:
      del self.is_environment_evaluation
      return
    if not isinstance(is_environment_evaluation, bool):
      raise TypeError('is_environment_evaluation must be of type bool')
    self._is_environment_evaluation = is_environment_evaluation

  @property
  def prize_type(self) -> 'RewardTypeId':
    """The prize/award type of the Competition"""
    return self._prize_type

  @prize_type.setter
  def prize_type(self, prize_type: 'RewardTypeId'):
    if prize_type is None:
      del self.prize_type
      return
    if not isinstance(prize_type, RewardTypeId):
      raise TypeError('prize_type must be of type RewardTypeId')
    self._prize_type = prize_type

  @property
  def prize_value(self) -> float:
    """The prize/award value of the Competition"""
    return self._prize_value or 0.0

  @prize_value.setter
  def prize_value(self, prize_value: Optional[float]):
    if prize_value is None:
      del self.prize_value
      return
    if not isinstance(prize_value, float):
      raise TypeError('prize_value must be of type float')
    self._prize_value = prize_value

  @property
  def is_launched(self) -> bool:
    """Whether the competition has launched (even if it's ended)"""
    return self._is_launched

  @is_launched.setter
  def is_launched(self, is_launched: bool):
    if is_launched is None:
      del self.is_launched
      return
    if not isinstance(is_launched, bool):
      raise TypeError('is_launched must be of type bool')
    self._is_launched = is_launched

  @property
  def owner_user_has_joined(self) -> bool:
    r"""
    Whether the owner user (profile user, then current user) has joined the
    competition
    """
    return self._owner_user_has_joined

  @owner_user_has_joined.setter
  def owner_user_has_joined(self, owner_user_has_joined: bool):
    if owner_user_has_joined is None:
      del self.owner_user_has_joined
      return
    if not isinstance(owner_user_has_joined, bool):
      raise TypeError('owner_user_has_joined must be of type bool')
    self._owner_user_has_joined = owner_user_has_joined

  @property
  def is_limited_participation(self) -> bool:
    """Whether the competition is a limited participation competition"""
    return self._is_limited_participation

  @is_limited_participation.setter
  def is_limited_participation(self, is_limited_participation: bool):
    if is_limited_participation is None:
      del self.is_limited_participation
      return
    if not isinstance(is_limited_participation, bool):
      raise TypeError('is_limited_participation must be of type bool')
    self._is_limited_participation = is_limited_participation

  @property
  def only_allow_kernel_submissions(self) -> bool:
    """Whether only kernel submissions are allowed"""
    return self._only_allow_kernel_submissions

  @only_allow_kernel_submissions.setter
  def only_allow_kernel_submissions(self, only_allow_kernel_submissions: bool):
    if only_allow_kernel_submissions is None:
      del self.only_allow_kernel_submissions
      return
    if not isinstance(only_allow_kernel_submissions, bool):
      raise TypeError('only_allow_kernel_submissions must be of type bool')
    self._only_allow_kernel_submissions = only_allow_kernel_submissions

  @property
  def participant_user_id(self) -> int:
    """Used to generate competition certificate link"""
    return self._participant_user_id

  @participant_user_id.setter
  def participant_user_id(self, participant_user_id: int):
    if participant_user_id is None:
      del self.participant_user_id
      return
    if not isinstance(participant_user_id, int):
      raise TypeError('participant_user_id must be of type int')
    self._participant_user_id = participant_user_id

  @property
  def is_current_user_host(self) -> bool:
    """Whether current user is host for this competition"""
    return self._is_current_user_host

  @is_current_user_host.setter
  def is_current_user_host(self, is_current_user_host: bool):
    if is_current_user_host is None:
      del self.is_current_user_host
      return
    if not isinstance(is_current_user_host, bool):
      raise TypeError('is_current_user_host must be of type bool')
    self._is_current_user_host = is_current_user_host

  @property
  def is_hidden_on_profile(self) -> bool:
    """Whether the competition is hidden on user's profile"""
    return self._is_hidden_on_profile

  @is_hidden_on_profile.setter
  def is_hidden_on_profile(self, is_hidden_on_profile: bool):
    if is_hidden_on_profile is None:
      del self.is_hidden_on_profile
      return
    if not isinstance(is_hidden_on_profile, bool):
      raise TypeError('is_hidden_on_profile must be of type bool')
    self._is_hidden_on_profile = is_hidden_on_profile


class SearchCompetitionsFilters(KaggleObject):
  r"""
  Attributes:
    role (SearchCompetitionsRole)
      The Competition role used to filter the documents
    status (SearchCompetitionsStatus)
      The Competition status used to filter the documents
    profile_visibility (SearchCompetitionsProfileVisibility)
      Competition visibility status on user profile
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._role = SearchCompetitionsRole.SEARCH_COMPETITIONS_ROLE_ANY
    self._status = SearchCompetitionsStatus.SEARCH_COMPETITIONS_STATUS_ANY
    self._profile_visibility = SearchCompetitionsProfileVisibility.SEARCH_COMPETITIONS_PROFILE_VISIBILITY_ANY
    self._earned_medal = None
    self._freeze()

  @property
  def role(self) -> 'SearchCompetitionsRole':
    """The Competition role used to filter the documents"""
    return self._role

  @role.setter
  def role(self, role: 'SearchCompetitionsRole'):
    if role is None:
      del self.role
      return
    if not isinstance(role, SearchCompetitionsRole):
      raise TypeError('role must be of type SearchCompetitionsRole')
    self._role = role

  @property
  def status(self) -> 'SearchCompetitionsStatus':
    """The Competition status used to filter the documents"""
    return self._status

  @status.setter
  def status(self, status: 'SearchCompetitionsStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, SearchCompetitionsStatus):
      raise TypeError('status must be of type SearchCompetitionsStatus')
    self._status = status

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal

  @property
  def profile_visibility(self) -> 'SearchCompetitionsProfileVisibility':
    """Competition visibility status on user profile"""
    return self._profile_visibility

  @profile_visibility.setter
  def profile_visibility(self, profile_visibility: 'SearchCompetitionsProfileVisibility'):
    if profile_visibility is None:
      del self.profile_visibility
      return
    if not isinstance(profile_visibility, SearchCompetitionsProfileVisibility):
      raise TypeError('profile_visibility must be of type SearchCompetitionsProfileVisibility')
    self._profile_visibility = profile_visibility


SearchCompetitionsDocument._fields = [
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamCount", "team_count", "_team_count", int, 0, PredefinedSerializer()),
  FieldMetadata("teamRank", "team_rank", "_team_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isEnvironmentEvaluation", "is_environment_evaluation", "_is_environment_evaluation", bool, False, PredefinedSerializer()),
  FieldMetadata("prizeType", "prize_type", "_prize_type", RewardTypeId, RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("prizeValue", "prize_value", "_prize_value", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLaunched", "is_launched", "_is_launched", bool, False, PredefinedSerializer()),
  FieldMetadata("ownerUserHasJoined", "owner_user_has_joined", "_owner_user_has_joined", bool, False, PredefinedSerializer()),
  FieldMetadata("isLimitedParticipation", "is_limited_participation", "_is_limited_participation", bool, False, PredefinedSerializer()),
  FieldMetadata("onlyAllowKernelSubmissions", "only_allow_kernel_submissions", "_only_allow_kernel_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("participantUserId", "participant_user_id", "_participant_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isCurrentUserHost", "is_current_user_host", "_is_current_user_host", bool, False, PredefinedSerializer()),
  FieldMetadata("isHiddenOnProfile", "is_hidden_on_profile", "_is_hidden_on_profile", bool, False, PredefinedSerializer()),
]

SearchCompetitionsFilters._fields = [
  FieldMetadata("role", "role", "_role", SearchCompetitionsRole, SearchCompetitionsRole.SEARCH_COMPETITIONS_ROLE_ANY, EnumSerializer()),
  FieldMetadata("status", "status", "_status", SearchCompetitionsStatus, SearchCompetitionsStatus.SEARCH_COMPETITIONS_STATUS_ANY, EnumSerializer()),
  FieldMetadata("profileVisibility", "profile_visibility", "_profile_visibility", SearchCompetitionsProfileVisibility, SearchCompetitionsProfileVisibility.SEARCH_COMPETITIONS_PROFILE_VISIBILITY_ANY, EnumSerializer()),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

