from datetime import datetime
import enum
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.community.types.badges_types import UserBadge
from kagglesdk.community.types.organization import Organization
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_service import WriteUpCompetitionInfo
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from kagglesdk.users.types.progression_service import Medal, UserAchievementType
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class ListFollowersUserIdType(enum.Enum):
  LIST_FOLLOWERS_USER_ID_TYPE_UNSPECIFIED = 0
  FROM_USER = 1
  TO_USER = 2

class ProfilePinType(enum.Enum):
  PROFILE_PIN_TYPE_UNSPECIFIED = 0
  PROFILE_PIN_TYPE_COMPETITION = 1
  PROFILE_PIN_TYPE_DATASET = 2
  PROFILE_PIN_TYPE_MODEL = 3
  PROFILE_PIN_TYPE_NOTEBOOK = 4
  PROFILE_PIN_TYPE_LEARN_CERTIFICATE = 5
  PROFILE_PIN_TYPE_WRITE_UP = 6

class ProfileSection(enum.Enum):
  r"""
  Enumerates UI profile sections.
  WARNING: Do not reorder or change enum values!
  These values are persisted in UserProfileAttribute
  (ATTRIBUTE_ID_PROFILE_VISIBILITY_SETTINGS and
  ATTRIBUTE_ID_PROFILE_SECTION_ORDER) and changing them will break existing
  user customizations. Always add new sections at the end with the next
  sequential number.
  """
  PROFILE_SECTION_UNSPECIFIED = 0
  PROFILE_SECTION_ACHIEVEMENTS = 1
  PROFILE_SECTION_PINNED_WORK = 2
  PROFILE_SECTION_ACTIVITY = 3
  PROFILE_SECTION_FOLLOWERS = 4
  PROFILE_SECTION_FOLLOWING = 5
  PROFILE_SECTION_AWARDS = 6
  PROFILE_SECTION_BADGES = 7
  PROFILE_SECTION_FEATURED_WRITE_UPS = 8
  PROFILE_SECTION_BIO = 9

class AchievementSummary(KaggleObject):
  r"""
  Attributes:
    tier (UserAchievementTier)
      The tier for this achievement
    summary_type (UserAchievementType)
      The type of achievement (competitions, datasets, notebooks, discussions)
    total_results (int)
      Total items in this achievement type for the user
    rank_percentage (float)
      The percentage rank of this achievement for the user
    rank_out_of (int)
      The total users ranked in this achievement
    rank_current (int)
      The number rank of this achievement for the user
    rank_highest (int)
      The highest number rank of this achievement for the user
    total_gold_medals (int)
      The total number of gold medals of this achievement for the user
    total_silver_medals (int)
      The total number of silver medals of this achievement for the user
    total_bronze_medals (int)
      The total number of bronze medals of this achievement for the user
    legacy_tier (UserAchievementTier)
      A previous tier they earned before changes in eligibility
  """

  def __init__(self):
    self._tier = UserAchievementTier.NOVICE
    self._summary_type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._total_results = 0
    self._rank_percentage = None
    self._rank_out_of = 0
    self._rank_current = None
    self._rank_highest = None
    self._total_gold_medals = 0
    self._total_silver_medals = 0
    self._total_bronze_medals = 0
    self._legacy_tier = None
    self._freeze()

  @property
  def tier(self) -> 'UserAchievementTier':
    """The tier for this achievement"""
    return self._tier

  @tier.setter
  def tier(self, tier: 'UserAchievementTier'):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, UserAchievementTier):
      raise TypeError('tier must be of type UserAchievementTier')
    self._tier = tier

  @property
  def legacy_tier(self) -> 'UserAchievementTier':
    """A previous tier they earned before changes in eligibility"""
    return self._legacy_tier or UserAchievementTier.NOVICE

  @legacy_tier.setter
  def legacy_tier(self, legacy_tier: Optional['UserAchievementTier']):
    if legacy_tier is None:
      del self.legacy_tier
      return
    if not isinstance(legacy_tier, UserAchievementTier):
      raise TypeError('legacy_tier must be of type UserAchievementTier')
    self._legacy_tier = legacy_tier

  @property
  def summary_type(self) -> 'UserAchievementType':
    """The type of achievement (competitions, datasets, notebooks, discussions)"""
    return self._summary_type

  @summary_type.setter
  def summary_type(self, summary_type: 'UserAchievementType'):
    if summary_type is None:
      del self.summary_type
      return
    if not isinstance(summary_type, UserAchievementType):
      raise TypeError('summary_type must be of type UserAchievementType')
    self._summary_type = summary_type

  @property
  def total_results(self) -> int:
    """Total items in this achievement type for the user"""
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results

  @property
  def rank_percentage(self) -> float:
    """The percentage rank of this achievement for the user"""
    return self._rank_percentage or 0.0

  @rank_percentage.setter
  def rank_percentage(self, rank_percentage: Optional[float]):
    if rank_percentage is None:
      del self.rank_percentage
      return
    if not isinstance(rank_percentage, float):
      raise TypeError('rank_percentage must be of type float')
    self._rank_percentage = rank_percentage

  @property
  def rank_out_of(self) -> int:
    """The total users ranked in this achievement"""
    return self._rank_out_of

  @rank_out_of.setter
  def rank_out_of(self, rank_out_of: int):
    if rank_out_of is None:
      del self.rank_out_of
      return
    if not isinstance(rank_out_of, int):
      raise TypeError('rank_out_of must be of type int')
    self._rank_out_of = rank_out_of

  @property
  def rank_current(self) -> int:
    """The number rank of this achievement for the user"""
    return self._rank_current or 0

  @rank_current.setter
  def rank_current(self, rank_current: Optional[int]):
    if rank_current is None:
      del self.rank_current
      return
    if not isinstance(rank_current, int):
      raise TypeError('rank_current must be of type int')
    self._rank_current = rank_current

  @property
  def rank_highest(self) -> int:
    """The highest number rank of this achievement for the user"""
    return self._rank_highest or 0

  @rank_highest.setter
  def rank_highest(self, rank_highest: Optional[int]):
    if rank_highest is None:
      del self.rank_highest
      return
    if not isinstance(rank_highest, int):
      raise TypeError('rank_highest must be of type int')
    self._rank_highest = rank_highest

  @property
  def total_gold_medals(self) -> int:
    """The total number of gold medals of this achievement for the user"""
    return self._total_gold_medals

  @total_gold_medals.setter
  def total_gold_medals(self, total_gold_medals: int):
    if total_gold_medals is None:
      del self.total_gold_medals
      return
    if not isinstance(total_gold_medals, int):
      raise TypeError('total_gold_medals must be of type int')
    self._total_gold_medals = total_gold_medals

  @property
  def total_silver_medals(self) -> int:
    """The total number of silver medals of this achievement for the user"""
    return self._total_silver_medals

  @total_silver_medals.setter
  def total_silver_medals(self, total_silver_medals: int):
    if total_silver_medals is None:
      del self.total_silver_medals
      return
    if not isinstance(total_silver_medals, int):
      raise TypeError('total_silver_medals must be of type int')
    self._total_silver_medals = total_silver_medals

  @property
  def total_bronze_medals(self) -> int:
    """The total number of bronze medals of this achievement for the user"""
    return self._total_bronze_medals

  @total_bronze_medals.setter
  def total_bronze_medals(self, total_bronze_medals: int):
    if total_bronze_medals is None:
      del self.total_bronze_medals
      return
    if not isinstance(total_bronze_medals, int):
      raise TypeError('total_bronze_medals must be of type int')
    self._total_bronze_medals = total_bronze_medals


class ActivityCalendar(KaggleObject):
  r"""
  Attributes:
    date (datetime)
      This name cannot be changed as react-calendar-heatmap relies on the name of
      this property being 'date'
    total_submissions_count (int)
    total_scripts_count (int)
    total_discussions_count (int)
    total_datasets_count (int)
  """

  def __init__(self):
    self._date = None
    self._total_submissions_count = 0
    self._total_scripts_count = 0
    self._total_discussions_count = 0
    self._total_datasets_count = 0
    self._freeze()

  @property
  def date(self) -> datetime:
    r"""
    This name cannot be changed as react-calendar-heatmap relies on the name of
    this property being 'date'
    """
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

  @property
  def total_submissions_count(self) -> int:
    return self._total_submissions_count

  @total_submissions_count.setter
  def total_submissions_count(self, total_submissions_count: int):
    if total_submissions_count is None:
      del self.total_submissions_count
      return
    if not isinstance(total_submissions_count, int):
      raise TypeError('total_submissions_count must be of type int')
    self._total_submissions_count = total_submissions_count

  @property
  def total_scripts_count(self) -> int:
    return self._total_scripts_count

  @total_scripts_count.setter
  def total_scripts_count(self, total_scripts_count: int):
    if total_scripts_count is None:
      del self.total_scripts_count
      return
    if not isinstance(total_scripts_count, int):
      raise TypeError('total_scripts_count must be of type int')
    self._total_scripts_count = total_scripts_count

  @property
  def total_discussions_count(self) -> int:
    return self._total_discussions_count

  @total_discussions_count.setter
  def total_discussions_count(self, total_discussions_count: int):
    if total_discussions_count is None:
      del self.total_discussions_count
      return
    if not isinstance(total_discussions_count, int):
      raise TypeError('total_discussions_count must be of type int')
    self._total_discussions_count = total_discussions_count

  @property
  def total_datasets_count(self) -> int:
    return self._total_datasets_count

  @total_datasets_count.setter
  def total_datasets_count(self, total_datasets_count: int):
    if total_datasets_count is None:
      del self.total_datasets_count
      return
    if not isinstance(total_datasets_count, int):
      raise TypeError('total_datasets_count must be of type int')
    self._total_datasets_count = total_datasets_count


class CompetitionPin(KaggleObject):
  r"""
  Attributes:
    rank (int)
      The user's rank in this competition
    total_team_count (int)
      The total number of teams in this competition
    is_host (bool)
      Whether the user is a host for this competition
    total_joined_users (int)
      The total number of joined users in this competition
  """

  def __init__(self):
    self._rank = 0
    self._total_team_count = 0
    self._is_host = False
    self._total_joined_users = 0
    self._freeze()

  @property
  def rank(self) -> int:
    """The user's rank in this competition"""
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
  def total_team_count(self) -> int:
    """The total number of teams in this competition"""
    return self._total_team_count

  @total_team_count.setter
  def total_team_count(self, total_team_count: int):
    if total_team_count is None:
      del self.total_team_count
      return
    if not isinstance(total_team_count, int):
      raise TypeError('total_team_count must be of type int')
    self._total_team_count = total_team_count

  @property
  def is_host(self) -> bool:
    """Whether the user is a host for this competition"""
    return self._is_host

  @is_host.setter
  def is_host(self, is_host: bool):
    if is_host is None:
      del self.is_host
      return
    if not isinstance(is_host, bool):
      raise TypeError('is_host must be of type bool')
    self._is_host = is_host

  @property
  def total_joined_users(self) -> int:
    """The total number of joined users in this competition"""
    return self._total_joined_users

  @total_joined_users.setter
  def total_joined_users(self, total_joined_users: int):
    if total_joined_users is None:
      del self.total_joined_users
      return
    if not isinstance(total_joined_users, int):
      raise TypeError('total_joined_users must be of type int')
    self._total_joined_users = total_joined_users


class CreateProfilePinRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    dataset_id (int)
    kernel_id (int)
    model_id (int)
    learn_track_id (int)
      Intentionally no permission checker for this, we will verify the user has
      a LearnCompletion outside of authorization.
    write_up_id (int)
  """

  def __init__(self):
    self._competition_id = None
    self._dataset_id = None
    self._kernel_id = None
    self._model_id = None
    self._learn_track_id = None
    self._write_up_id = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._kernel_id = kernel_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.learn_track_id
    del self.write_up_id
    self._model_id = model_id

  @property
  def learn_track_id(self) -> int:
    r"""
    Intentionally no permission checker for this, we will verify the user has
    a LearnCompletion outside of authorization.
    """
    return self._learn_track_id or 0

  @learn_track_id.setter
  def learn_track_id(self, learn_track_id: int):
    if learn_track_id is None:
      del self.learn_track_id
      return
    if not isinstance(learn_track_id, int):
      raise TypeError('learn_track_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.write_up_id
    self._learn_track_id = learn_track_id

  @property
  def write_up_id(self) -> int:
    return self._write_up_id or 0

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    self._write_up_id = write_up_id


class DeleteProfilePinRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    dataset_id (int)
    kernel_id (int)
    model_id (int)
    learn_track_id (int)
    write_up_id (int)
  """

  def __init__(self):
    self._competition_id = None
    self._dataset_id = None
    self._kernel_id = None
    self._model_id = None
    self._learn_track_id = None
    self._write_up_id = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.model_id
    del self.learn_track_id
    del self.write_up_id
    self._kernel_id = kernel_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.learn_track_id
    del self.write_up_id
    self._model_id = model_id

  @property
  def learn_track_id(self) -> int:
    return self._learn_track_id or 0

  @learn_track_id.setter
  def learn_track_id(self, learn_track_id: int):
    if learn_track_id is None:
      del self.learn_track_id
      return
    if not isinstance(learn_track_id, int):
      raise TypeError('learn_track_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.write_up_id
    self._learn_track_id = learn_track_id

  @property
  def write_up_id(self) -> int:
    return self._write_up_id or 0

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.learn_track_id
    self._write_up_id = write_up_id


class DiscussionCounts(KaggleObject):
  r"""
  Attributes:
    total_discussions_count (int)
    total_topics_count (int)
    total_replies_count (int)
    total_upvotes_count (int)
  """

  def __init__(self):
    self._total_discussions_count = 0
    self._total_topics_count = 0
    self._total_replies_count = 0
    self._total_upvotes_count = 0
    self._freeze()

  @property
  def total_discussions_count(self) -> int:
    return self._total_discussions_count

  @total_discussions_count.setter
  def total_discussions_count(self, total_discussions_count: int):
    if total_discussions_count is None:
      del self.total_discussions_count
      return
    if not isinstance(total_discussions_count, int):
      raise TypeError('total_discussions_count must be of type int')
    self._total_discussions_count = total_discussions_count

  @property
  def total_topics_count(self) -> int:
    return self._total_topics_count

  @total_topics_count.setter
  def total_topics_count(self, total_topics_count: int):
    if total_topics_count is None:
      del self.total_topics_count
      return
    if not isinstance(total_topics_count, int):
      raise TypeError('total_topics_count must be of type int')
    self._total_topics_count = total_topics_count

  @property
  def total_replies_count(self) -> int:
    return self._total_replies_count

  @total_replies_count.setter
  def total_replies_count(self, total_replies_count: int):
    if total_replies_count is None:
      del self.total_replies_count
      return
    if not isinstance(total_replies_count, int):
      raise TypeError('total_replies_count must be of type int')
    self._total_replies_count = total_replies_count

  @property
  def total_upvotes_count(self) -> int:
    return self._total_upvotes_count

  @total_upvotes_count.setter
  def total_upvotes_count(self, total_upvotes_count: int):
    if total_upvotes_count is None:
      del self.total_upvotes_count
      return
    if not isinstance(total_upvotes_count, int):
      raise TypeError('total_upvotes_count must be of type int')
    self._total_upvotes_count = total_upvotes_count


class GetProfilePreviewRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user ID for whom to return a profile preview
    user_name (str)
      The user name for whom to return a profile preview
  """

  def __init__(self):
    self._user_id = None
    self._user_name = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user ID for whom to return a profile preview"""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    del self.user_name
    self._user_id = user_id

  @property
  def user_name(self) -> str:
    """The user name for whom to return a profile preview"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.user_id
    self._user_name = user_name


class GetProfilePreviewResponse(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The requested user's user name
    display_name (str)
      The requested user's display name
    profile_url (str)
      The URL for the requested user's profile
    thumbnail_url (str)
      The URL For the requested user's avatar
    performance_tier (UserAchievementTier)
      The requested user's tier
    country (str)
      The requested user's country
    region (str)
      The requested user's region
    city (str)
      The requested user's city
    occupation (str)
      The requested user's occupation
    can_be_seen (bool)
      Boolean indicating whether the current user can be seen (false is i.e.
      account is deleted or user is banned)
    organization (str)
      The requested user's organization
    pronouns (str)
      The requested user's pronouns
    progression_opt_out (bool)
      Whether or not the requested user has opted out from progression
  """

  def __init__(self):
    self._user_name = ""
    self._display_name = ""
    self._profile_url = ""
    self._thumbnail_url = ""
    self._performance_tier = UserAchievementTier.NOVICE
    self._country = ""
    self._region = ""
    self._city = ""
    self._occupation = ""
    self._can_be_seen = False
    self._organization = ""
    self._pronouns = ""
    self._progression_opt_out = False
    self._freeze()

  @property
  def user_name(self) -> str:
    """The requested user's user name"""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def display_name(self) -> str:
    """The requested user's display name"""
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def profile_url(self) -> str:
    """The URL for the requested user's profile"""
    return self._profile_url

  @profile_url.setter
  def profile_url(self, profile_url: str):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def thumbnail_url(self) -> str:
    """The URL For the requested user's avatar"""
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def performance_tier(self) -> 'UserAchievementTier':
    """The requested user's tier"""
    return self._performance_tier

  @performance_tier.setter
  def performance_tier(self, performance_tier: 'UserAchievementTier'):
    if performance_tier is None:
      del self.performance_tier
      return
    if not isinstance(performance_tier, UserAchievementTier):
      raise TypeError('performance_tier must be of type UserAchievementTier')
    self._performance_tier = performance_tier

  @property
  def country(self) -> str:
    """The requested user's country"""
    return self._country

  @country.setter
  def country(self, country: str):
    if country is None:
      del self.country
      return
    if not isinstance(country, str):
      raise TypeError('country must be of type str')
    self._country = country

  @property
  def region(self) -> str:
    """The requested user's region"""
    return self._region

  @region.setter
  def region(self, region: str):
    if region is None:
      del self.region
      return
    if not isinstance(region, str):
      raise TypeError('region must be of type str')
    self._region = region

  @property
  def city(self) -> str:
    """The requested user's city"""
    return self._city

  @city.setter
  def city(self, city: str):
    if city is None:
      del self.city
      return
    if not isinstance(city, str):
      raise TypeError('city must be of type str')
    self._city = city

  @property
  def occupation(self) -> str:
    """The requested user's occupation"""
    return self._occupation

  @occupation.setter
  def occupation(self, occupation: str):
    if occupation is None:
      del self.occupation
      return
    if not isinstance(occupation, str):
      raise TypeError('occupation must be of type str')
    self._occupation = occupation

  @property
  def can_be_seen(self) -> bool:
    r"""
    Boolean indicating whether the current user can be seen (false is i.e.
    account is deleted or user is banned)
    """
    return self._can_be_seen

  @can_be_seen.setter
  def can_be_seen(self, can_be_seen: bool):
    if can_be_seen is None:
      del self.can_be_seen
      return
    if not isinstance(can_be_seen, bool):
      raise TypeError('can_be_seen must be of type bool')
    self._can_be_seen = can_be_seen

  @property
  def organization(self) -> str:
    """The requested user's organization"""
    return self._organization

  @organization.setter
  def organization(self, organization: str):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, str):
      raise TypeError('organization must be of type str')
    self._organization = organization

  @property
  def pronouns(self) -> str:
    """The requested user's pronouns"""
    return self._pronouns

  @pronouns.setter
  def pronouns(self, pronouns: str):
    if pronouns is None:
      del self.pronouns
      return
    if not isinstance(pronouns, str):
      raise TypeError('pronouns must be of type str')
    self._pronouns = pronouns

  @property
  def progression_opt_out(self) -> bool:
    """Whether or not the requested user has opted out from progression"""
    return self._progression_opt_out

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: bool):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out


class GetProfileRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The username of the user for the profile (from the request URL)
    user_id (int)
      The user Id of the user for the profile (from the request URL)
  """

  def __init__(self):
    self._user_name = None
    self._user_id = None
    self._freeze()

  @property
  def user_name(self) -> str:
    """The username of the user for the profile (from the request URL)"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.user_id
    self._user_name = user_name

  @property
  def user_id(self) -> int:
    """The user Id of the user for the profile (from the request URL)"""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    del self.user_name
    self._user_id = user_id


class GetProfileResponse(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The ID of the user
    display_name (str)
      The display name of the user
    country (str)
      The country of the user
    region (str)
      The region of the user
    city (str)
      The city of the user
    git_hub_user_name (str)
      The GitHub username of the user
    twitter_user_name (str)
      The Twitter of the user
    linked_in_url (str)
      The LinkedIn URL of the user
    website_url (str)
      The website URL the user attached to their profile
    occupation (str)
      The occupation of the user
    organization (str)
      The organization of the user
    bio (str)
      The bio of the user
    user_last_active (datetime)
      The date the user was last active
    user_join_date (datetime)
      The date the user joined Kaggle
    performance_tier (UserAchievementTier)
      The performance tier of the user
    performance_tier_category (UserAchievementType)
      The category of the top performance tier for the user
    user_avatar_url (str)
      The URL of the user's avatar
    can_edit (bool)
      Whether the current user can edit the profile
    achievement_summaries (AchievementSummary)
      Summaries for achievements (for each type)
    total_users_i_follow (int)
      Count of users this user is followed by
    total_users_following_me (int)
      Count of users this user is following
    user_name (str)
      User name
    tagline (str)
      Tagline
    pronouns (str)
      Pronouns
    total_kernels (int)
      Number of public kernels authored by the user
    total_competitions (int)
      Number of public finalized competitions participated in by the user
    total_datasets (int)
      Number of public datasets owned by the user
    total_discussions (int)
      Number of public topics and public comments made by the user
    total_models (int)
      Number of public models owned by the user
    badges (UserBadge)
      Badges to show for this user.
    visibility_settings (ProfileVisibilitySettings)
      Visibility settings.
    total_hosted_competitions (int)
      Number of public competitions user has hosted
    total_active_competitions (int)
      Number of public competitions user is currently participating in
    progression_opt_out (bool)
      Whether or not the user is opted out of progression
    current_user_follows_this_user (bool)
      Whether the current user follows the user for this profile
    location_sharing_opt_out (bool)
      Whether or not the requested user has opted out from sharing their location
    organizations (Organization)
      Organizations the user belongs to
    total_grandmaster_level (int)
      The number of grandmaster levels the user has earned
    total_write_ups (int)
      Number of public writeups owned by this user
    section_order (ProfileSection)
      The order of sections on the About tab of the profile
    total_benchmarks (int)
      The number of public benchmarks owned by this user
    total_benchmark_tasks (int)
      The number of public tasks owned by this user
  """

  def __init__(self):
    self._user_id = 0
    self._display_name = None
    self._country = None
    self._region = None
    self._city = None
    self._git_hub_user_name = None
    self._twitter_user_name = None
    self._linked_in_url = None
    self._website_url = None
    self._occupation = None
    self._organization = None
    self._bio = None
    self._user_last_active = None
    self._user_join_date = None
    self._performance_tier = UserAchievementTier.NOVICE
    self._performance_tier_category = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._user_avatar_url = None
    self._can_edit = False
    self._achievement_summaries = []
    self._total_users_i_follow = 0
    self._total_users_following_me = 0
    self._user_name = None
    self._tagline = None
    self._pronouns = None
    self._total_kernels = 0
    self._total_competitions = 0
    self._total_datasets = 0
    self._total_discussions = 0
    self._total_models = 0
    self._badges = []
    self._visibility_settings = None
    self._total_hosted_competitions = 0
    self._total_active_competitions = 0
    self._progression_opt_out = None
    self._current_user_follows_this_user = False
    self._location_sharing_opt_out = None
    self._organizations = []
    self._total_grandmaster_level = 0
    self._total_write_ups = 0
    self._section_order = []
    self._total_benchmarks = 0
    self._total_benchmark_tasks = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The ID of the user"""
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
  def display_name(self) -> str:
    """The display name of the user"""
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def country(self) -> str:
    """The country of the user"""
    return self._country or ""

  @country.setter
  def country(self, country: Optional[str]):
    if country is None:
      del self.country
      return
    if not isinstance(country, str):
      raise TypeError('country must be of type str')
    self._country = country

  @property
  def region(self) -> str:
    """The region of the user"""
    return self._region or ""

  @region.setter
  def region(self, region: Optional[str]):
    if region is None:
      del self.region
      return
    if not isinstance(region, str):
      raise TypeError('region must be of type str')
    self._region = region

  @property
  def city(self) -> str:
    """The city of the user"""
    return self._city or ""

  @city.setter
  def city(self, city: Optional[str]):
    if city is None:
      del self.city
      return
    if not isinstance(city, str):
      raise TypeError('city must be of type str')
    self._city = city

  @property
  def git_hub_user_name(self) -> str:
    """The GitHub username of the user"""
    return self._git_hub_user_name or ""

  @git_hub_user_name.setter
  def git_hub_user_name(self, git_hub_user_name: Optional[str]):
    if git_hub_user_name is None:
      del self.git_hub_user_name
      return
    if not isinstance(git_hub_user_name, str):
      raise TypeError('git_hub_user_name must be of type str')
    self._git_hub_user_name = git_hub_user_name

  @property
  def twitter_user_name(self) -> str:
    """The Twitter of the user"""
    return self._twitter_user_name or ""

  @twitter_user_name.setter
  def twitter_user_name(self, twitter_user_name: Optional[str]):
    if twitter_user_name is None:
      del self.twitter_user_name
      return
    if not isinstance(twitter_user_name, str):
      raise TypeError('twitter_user_name must be of type str')
    self._twitter_user_name = twitter_user_name

  @property
  def linked_in_url(self) -> str:
    """The LinkedIn URL of the user"""
    return self._linked_in_url or ""

  @linked_in_url.setter
  def linked_in_url(self, linked_in_url: Optional[str]):
    if linked_in_url is None:
      del self.linked_in_url
      return
    if not isinstance(linked_in_url, str):
      raise TypeError('linked_in_url must be of type str')
    self._linked_in_url = linked_in_url

  @property
  def website_url(self) -> str:
    """The website URL the user attached to their profile"""
    return self._website_url or ""

  @website_url.setter
  def website_url(self, website_url: Optional[str]):
    if website_url is None:
      del self.website_url
      return
    if not isinstance(website_url, str):
      raise TypeError('website_url must be of type str')
    self._website_url = website_url

  @property
  def occupation(self) -> str:
    """The occupation of the user"""
    return self._occupation or ""

  @occupation.setter
  def occupation(self, occupation: Optional[str]):
    if occupation is None:
      del self.occupation
      return
    if not isinstance(occupation, str):
      raise TypeError('occupation must be of type str')
    self._occupation = occupation

  @property
  def organization(self) -> str:
    """The organization of the user"""
    return self._organization or ""

  @organization.setter
  def organization(self, organization: Optional[str]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, str):
      raise TypeError('organization must be of type str')
    self._organization = organization

  @property
  def bio(self) -> str:
    """The bio of the user"""
    return self._bio or ""

  @bio.setter
  def bio(self, bio: Optional[str]):
    if bio is None:
      del self.bio
      return
    if not isinstance(bio, str):
      raise TypeError('bio must be of type str')
    self._bio = bio

  @property
  def user_last_active(self) -> datetime:
    """The date the user was last active"""
    return self._user_last_active

  @user_last_active.setter
  def user_last_active(self, user_last_active: datetime):
    if user_last_active is None:
      del self.user_last_active
      return
    if not isinstance(user_last_active, datetime):
      raise TypeError('user_last_active must be of type datetime')
    self._user_last_active = user_last_active

  @property
  def user_join_date(self) -> datetime:
    """The date the user joined Kaggle"""
    return self._user_join_date

  @user_join_date.setter
  def user_join_date(self, user_join_date: datetime):
    if user_join_date is None:
      del self.user_join_date
      return
    if not isinstance(user_join_date, datetime):
      raise TypeError('user_join_date must be of type datetime')
    self._user_join_date = user_join_date

  @property
  def performance_tier(self) -> 'UserAchievementTier':
    """The performance tier of the user"""
    return self._performance_tier

  @performance_tier.setter
  def performance_tier(self, performance_tier: 'UserAchievementTier'):
    if performance_tier is None:
      del self.performance_tier
      return
    if not isinstance(performance_tier, UserAchievementTier):
      raise TypeError('performance_tier must be of type UserAchievementTier')
    self._performance_tier = performance_tier

  @property
  def performance_tier_category(self) -> 'UserAchievementType':
    """The category of the top performance tier for the user"""
    return self._performance_tier_category

  @performance_tier_category.setter
  def performance_tier_category(self, performance_tier_category: 'UserAchievementType'):
    if performance_tier_category is None:
      del self.performance_tier_category
      return
    if not isinstance(performance_tier_category, UserAchievementType):
      raise TypeError('performance_tier_category must be of type UserAchievementType')
    self._performance_tier_category = performance_tier_category

  @property
  def user_avatar_url(self) -> str:
    """The URL of the user's avatar"""
    return self._user_avatar_url or ""

  @user_avatar_url.setter
  def user_avatar_url(self, user_avatar_url: Optional[str]):
    if user_avatar_url is None:
      del self.user_avatar_url
      return
    if not isinstance(user_avatar_url, str):
      raise TypeError('user_avatar_url must be of type str')
    self._user_avatar_url = user_avatar_url

  @property
  def can_edit(self) -> bool:
    """Whether the current user can edit the profile"""
    return self._can_edit

  @can_edit.setter
  def can_edit(self, can_edit: bool):
    if can_edit is None:
      del self.can_edit
      return
    if not isinstance(can_edit, bool):
      raise TypeError('can_edit must be of type bool')
    self._can_edit = can_edit

  @property
  def achievement_summaries(self) -> Optional[List[Optional['AchievementSummary']]]:
    """Summaries for achievements (for each type)"""
    return self._achievement_summaries

  @achievement_summaries.setter
  def achievement_summaries(self, achievement_summaries: Optional[List[Optional['AchievementSummary']]]):
    if achievement_summaries is None:
      del self.achievement_summaries
      return
    if not isinstance(achievement_summaries, list):
      raise TypeError('achievement_summaries must be of type list')
    if not all([isinstance(t, AchievementSummary) for t in achievement_summaries]):
      raise TypeError('achievement_summaries must contain only items of type AchievementSummary')
    self._achievement_summaries = achievement_summaries

  @property
  def total_users_i_follow(self) -> int:
    """Count of users this user is followed by"""
    return self._total_users_i_follow

  @total_users_i_follow.setter
  def total_users_i_follow(self, total_users_i_follow: int):
    if total_users_i_follow is None:
      del self.total_users_i_follow
      return
    if not isinstance(total_users_i_follow, int):
      raise TypeError('total_users_i_follow must be of type int')
    self._total_users_i_follow = total_users_i_follow

  @property
  def total_users_following_me(self) -> int:
    """Count of users this user is following"""
    return self._total_users_following_me

  @total_users_following_me.setter
  def total_users_following_me(self, total_users_following_me: int):
    if total_users_following_me is None:
      del self.total_users_following_me
      return
    if not isinstance(total_users_following_me, int):
      raise TypeError('total_users_following_me must be of type int')
    self._total_users_following_me = total_users_following_me

  @property
  def user_name(self) -> str:
    """User name"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def tagline(self) -> str:
    """Tagline"""
    return self._tagline or ""

  @tagline.setter
  def tagline(self, tagline: Optional[str]):
    if tagline is None:
      del self.tagline
      return
    if not isinstance(tagline, str):
      raise TypeError('tagline must be of type str')
    self._tagline = tagline

  @property
  def pronouns(self) -> str:
    """Pronouns"""
    return self._pronouns or ""

  @pronouns.setter
  def pronouns(self, pronouns: Optional[str]):
    if pronouns is None:
      del self.pronouns
      return
    if not isinstance(pronouns, str):
      raise TypeError('pronouns must be of type str')
    self._pronouns = pronouns

  @property
  def total_kernels(self) -> int:
    """Number of public kernels authored by the user"""
    return self._total_kernels

  @total_kernels.setter
  def total_kernels(self, total_kernels: int):
    if total_kernels is None:
      del self.total_kernels
      return
    if not isinstance(total_kernels, int):
      raise TypeError('total_kernels must be of type int')
    self._total_kernels = total_kernels

  @property
  def total_competitions(self) -> int:
    """Number of public finalized competitions participated in by the user"""
    return self._total_competitions

  @total_competitions.setter
  def total_competitions(self, total_competitions: int):
    if total_competitions is None:
      del self.total_competitions
      return
    if not isinstance(total_competitions, int):
      raise TypeError('total_competitions must be of type int')
    self._total_competitions = total_competitions

  @property
  def total_datasets(self) -> int:
    """Number of public datasets owned by the user"""
    return self._total_datasets

  @total_datasets.setter
  def total_datasets(self, total_datasets: int):
    if total_datasets is None:
      del self.total_datasets
      return
    if not isinstance(total_datasets, int):
      raise TypeError('total_datasets must be of type int')
    self._total_datasets = total_datasets

  @property
  def total_discussions(self) -> int:
    """Number of public topics and public comments made by the user"""
    return self._total_discussions

  @total_discussions.setter
  def total_discussions(self, total_discussions: int):
    if total_discussions is None:
      del self.total_discussions
      return
    if not isinstance(total_discussions, int):
      raise TypeError('total_discussions must be of type int')
    self._total_discussions = total_discussions

  @property
  def total_models(self) -> int:
    """Number of public models owned by the user"""
    return self._total_models

  @total_models.setter
  def total_models(self, total_models: int):
    if total_models is None:
      del self.total_models
      return
    if not isinstance(total_models, int):
      raise TypeError('total_models must be of type int')
    self._total_models = total_models

  @property
  def badges(self) -> Optional[List[Optional['UserBadge']]]:
    """Badges to show for this user."""
    return self._badges

  @badges.setter
  def badges(self, badges: Optional[List[Optional['UserBadge']]]):
    if badges is None:
      del self.badges
      return
    if not isinstance(badges, list):
      raise TypeError('badges must be of type list')
    if not all([isinstance(t, UserBadge) for t in badges]):
      raise TypeError('badges must contain only items of type UserBadge')
    self._badges = badges

  @property
  def visibility_settings(self) -> Optional['ProfileVisibilitySettings']:
    """Visibility settings."""
    return self._visibility_settings

  @visibility_settings.setter
  def visibility_settings(self, visibility_settings: Optional['ProfileVisibilitySettings']):
    if visibility_settings is None:
      del self.visibility_settings
      return
    if not isinstance(visibility_settings, ProfileVisibilitySettings):
      raise TypeError('visibility_settings must be of type ProfileVisibilitySettings')
    self._visibility_settings = visibility_settings

  @property
  def total_hosted_competitions(self) -> int:
    """Number of public competitions user has hosted"""
    return self._total_hosted_competitions

  @total_hosted_competitions.setter
  def total_hosted_competitions(self, total_hosted_competitions: int):
    if total_hosted_competitions is None:
      del self.total_hosted_competitions
      return
    if not isinstance(total_hosted_competitions, int):
      raise TypeError('total_hosted_competitions must be of type int')
    self._total_hosted_competitions = total_hosted_competitions

  @property
  def total_active_competitions(self) -> int:
    """Number of public competitions user is currently participating in"""
    return self._total_active_competitions

  @total_active_competitions.setter
  def total_active_competitions(self, total_active_competitions: int):
    if total_active_competitions is None:
      del self.total_active_competitions
      return
    if not isinstance(total_active_competitions, int):
      raise TypeError('total_active_competitions must be of type int')
    self._total_active_competitions = total_active_competitions

  @property
  def progression_opt_out(self) -> bool:
    """Whether or not the user is opted out of progression"""
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out

  @property
  def current_user_follows_this_user(self) -> bool:
    """Whether the current user follows the user for this profile"""
    return self._current_user_follows_this_user

  @current_user_follows_this_user.setter
  def current_user_follows_this_user(self, current_user_follows_this_user: bool):
    if current_user_follows_this_user is None:
      del self.current_user_follows_this_user
      return
    if not isinstance(current_user_follows_this_user, bool):
      raise TypeError('current_user_follows_this_user must be of type bool')
    self._current_user_follows_this_user = current_user_follows_this_user

  @property
  def location_sharing_opt_out(self) -> bool:
    """Whether or not the requested user has opted out from sharing their location"""
    return self._location_sharing_opt_out or False

  @location_sharing_opt_out.setter
  def location_sharing_opt_out(self, location_sharing_opt_out: Optional[bool]):
    if location_sharing_opt_out is None:
      del self.location_sharing_opt_out
      return
    if not isinstance(location_sharing_opt_out, bool):
      raise TypeError('location_sharing_opt_out must be of type bool')
    self._location_sharing_opt_out = location_sharing_opt_out

  @property
  def organizations(self) -> Optional[List[Optional['Organization']]]:
    """Organizations the user belongs to"""
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[List[Optional['Organization']]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, list):
      raise TypeError('organizations must be of type list')
    if not all([isinstance(t, Organization) for t in organizations]):
      raise TypeError('organizations must contain only items of type Organization')
    self._organizations = organizations

  @property
  def total_grandmaster_level(self) -> int:
    """The number of grandmaster levels the user has earned"""
    return self._total_grandmaster_level

  @total_grandmaster_level.setter
  def total_grandmaster_level(self, total_grandmaster_level: int):
    if total_grandmaster_level is None:
      del self.total_grandmaster_level
      return
    if not isinstance(total_grandmaster_level, int):
      raise TypeError('total_grandmaster_level must be of type int')
    self._total_grandmaster_level = total_grandmaster_level

  @property
  def total_write_ups(self) -> int:
    """Number of public writeups owned by this user"""
    return self._total_write_ups

  @total_write_ups.setter
  def total_write_ups(self, total_write_ups: int):
    if total_write_ups is None:
      del self.total_write_ups
      return
    if not isinstance(total_write_ups, int):
      raise TypeError('total_write_ups must be of type int')
    self._total_write_ups = total_write_ups

  @property
  def section_order(self) -> Optional[List['ProfileSection']]:
    """The order of sections on the About tab of the profile"""
    return self._section_order

  @section_order.setter
  def section_order(self, section_order: Optional[List['ProfileSection']]):
    if section_order is None:
      del self.section_order
      return
    if not isinstance(section_order, list):
      raise TypeError('section_order must be of type list')
    if not all([isinstance(t, ProfileSection) for t in section_order]):
      raise TypeError('section_order must contain only items of type ProfileSection')
    self._section_order = section_order

  @property
  def total_benchmarks(self) -> int:
    """The number of public benchmarks owned by this user"""
    return self._total_benchmarks

  @total_benchmarks.setter
  def total_benchmarks(self, total_benchmarks: int):
    if total_benchmarks is None:
      del self.total_benchmarks
      return
    if not isinstance(total_benchmarks, int):
      raise TypeError('total_benchmarks must be of type int')
    self._total_benchmarks = total_benchmarks

  @property
  def total_benchmark_tasks(self) -> int:
    """The number of public tasks owned by this user"""
    return self._total_benchmark_tasks

  @total_benchmark_tasks.setter
  def total_benchmark_tasks(self, total_benchmark_tasks: int):
    if total_benchmark_tasks is None:
      del self.total_benchmark_tasks
      return
    if not isinstance(total_benchmark_tasks, int):
      raise TypeError('total_benchmark_tasks must be of type int')
    self._total_benchmark_tasks = total_benchmark_tasks


class GetUserActivityRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class GetUserActivityResponse(KaggleObject):
  r"""
  Attributes:
    activities (ActivityCalendar)
  """

  def __init__(self):
    self._activities = []
    self._freeze()

  @property
  def activities(self) -> Optional[List[Optional['ActivityCalendar']]]:
    return self._activities

  @activities.setter
  def activities(self, activities: Optional[List[Optional['ActivityCalendar']]]):
    if activities is None:
      del self.activities
      return
    if not isinstance(activities, list):
      raise TypeError('activities must be of type list')
    if not all([isinstance(t, ActivityCalendar) for t in activities]):
      raise TypeError('activities must contain only items of type ActivityCalendar')
    self._activities = activities


class GetUserDiscussionCountsRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class GetUserWriteUpCountsRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The username of the user for WriteUps stats (from the request URL)
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    """The username of the user for WriteUps stats (from the request URL)"""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class ListFollowersRequest(KaggleObject):
  r"""
  Attributes:
    user_id_type (ListFollowersUserIdType)
      Whether the user_id value is the from_user or to_user
    user_id (int)
      List users that this user_id follows
    skip (int)
      The number of rows to skip (for pagination)
    page_size (int)
      The total users per page
    page_token (str)
      The token used for paging
  """

  def __init__(self):
    self._user_id_type = ListFollowersUserIdType.LIST_FOLLOWERS_USER_ID_TYPE_UNSPECIFIED
    self._user_id = 0
    self._skip = None
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def user_id_type(self) -> 'ListFollowersUserIdType':
    """Whether the user_id value is the from_user or to_user"""
    return self._user_id_type

  @user_id_type.setter
  def user_id_type(self, user_id_type: 'ListFollowersUserIdType'):
    if user_id_type is None:
      del self.user_id_type
      return
    if not isinstance(user_id_type, ListFollowersUserIdType):
      raise TypeError('user_id_type must be of type ListFollowersUserIdType')
    self._user_id_type = user_id_type

  @property
  def user_id(self) -> int:
    """List users that this user_id follows"""
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
  def skip(self) -> int:
    """The number of rows to skip (for pagination)"""
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def page_size(self) -> int:
    """The total users per page"""
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    """The token used for paging"""
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListFollowersResponse(KaggleObject):
  r"""
  Attributes:
    followers (UserAvatar)
      The paginated list of followers
    total_followers (int)
      The total number of followers
    next_page_token (str)
      The token for fetching the next page
  """

  def __init__(self):
    self._followers = []
    self._total_followers = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def followers(self) -> Optional[List[Optional['UserAvatar']]]:
    """The paginated list of followers"""
    return self._followers

  @followers.setter
  def followers(self, followers: Optional[List[Optional['UserAvatar']]]):
    if followers is None:
      del self.followers
      return
    if not isinstance(followers, list):
      raise TypeError('followers must be of type list')
    if not all([isinstance(t, UserAvatar) for t in followers]):
      raise TypeError('followers must contain only items of type UserAvatar')
    self._followers = followers

  @property
  def total_followers(self) -> int:
    """The total number of followers"""
    return self._total_followers

  @total_followers.setter
  def total_followers(self, total_followers: int):
    if total_followers is None:
      del self.total_followers
      return
    if not isinstance(total_followers, int):
      raise TypeError('total_followers must be of type int')
    self._total_followers = total_followers

  @property
  def next_page_token(self) -> str:
    """The token for fetching the next page"""
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ListProfilePinsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user whose pins should be fetched
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user whose pins should be fetched"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class ListProfilePinsResponse(KaggleObject):
  r"""
  Attributes:
    profile_pins (ProfilePin)
      Pins on this user's profile, in order
  """

  def __init__(self):
    self._profile_pins = []
    self._freeze()

  @property
  def profile_pins(self) -> Optional[List[Optional['ProfilePin']]]:
    """Pins on this user's profile, in order"""
    return self._profile_pins

  @profile_pins.setter
  def profile_pins(self, profile_pins: Optional[List[Optional['ProfilePin']]]):
    if profile_pins is None:
      del self.profile_pins
      return
    if not isinstance(profile_pins, list):
      raise TypeError('profile_pins must be of type list')
    if not all([isinstance(t, ProfilePin) for t in profile_pins]):
      raise TypeError('profile_pins must contain only items of type ProfilePin')
    self._profile_pins = profile_pins


class ModelPin(KaggleObject):
  r"""
  Attributes:
    download_count (int)
      The number of downloads on this model
  """

  def __init__(self):
    self._download_count = 0
    self._freeze()

  @property
  def download_count(self) -> int:
    """The number of downloads on this model"""
    return self._download_count

  @download_count.setter
  def download_count(self, download_count: int):
    if download_count is None:
      del self.download_count
      return
    if not isinstance(download_count, int):
      raise TypeError('download_count must be of type int')
    self._download_count = download_count


class ProfilePin(KaggleObject):
  r"""
  Attributes:
    type (ProfilePinType)
      The type of content this profile pin corresponds with
    date (datetime)
      The date to display on this profile pin, i.e. created date, completed
      date, etc.
    upvote_count (int)
      The number of upvotes for this content, if applicable
    medal (Medal)
      The medal assigned to this content, if applicable
    name (str)
      The name for this piece of content
    url (str)
      The URL for this piece of content
    thumbnail_url (str)
      The URL for a thumbnail for this piece of content, if applicable
    entity_id (int)
      The ID for the piece of content this pin represents
    owner_user (UserAvatar)
    owner_organization (OrganizationCard)
    competition (CompetitionPin)
    model (ModelPin)
    collaborators (UserAvatar)
    write_up (WriteUpPin)
  """

  def __init__(self):
    self._type = ProfilePinType.PROFILE_PIN_TYPE_UNSPECIFIED
    self._date = None
    self._upvote_count = None
    self._medal = None
    self._name = ""
    self._url = ""
    self._thumbnail_url = None
    self._entity_id = 0
    self._owner_user = None
    self._owner_organization = None
    self._competition = None
    self._model = None
    self._collaborators = []
    self._write_up = None
    self._freeze()

  @property
  def type(self) -> 'ProfilePinType':
    """The type of content this profile pin corresponds with"""
    return self._type

  @type.setter
  def type(self, type: 'ProfilePinType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ProfilePinType):
      raise TypeError('type must be of type ProfilePinType')
    self._type = type

  @property
  def date(self) -> datetime:
    r"""
    The date to display on this profile pin, i.e. created date, completed
    date, etc.
    """
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

  @property
  def upvote_count(self) -> int:
    """The number of upvotes for this content, if applicable"""
    return self._upvote_count or 0

  @upvote_count.setter
  def upvote_count(self, upvote_count: Optional[int]):
    if upvote_count is None:
      del self.upvote_count
      return
    if not isinstance(upvote_count, int):
      raise TypeError('upvote_count must be of type int')
    self._upvote_count = upvote_count

  @property
  def medal(self) -> 'Medal':
    """The medal assigned to this content, if applicable"""
    return self._medal or Medal.MEDAL_UNSPECIFIED

  @medal.setter
  def medal(self, medal: Optional['Medal']):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def name(self) -> str:
    """The name for this piece of content"""
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
  def url(self) -> str:
    """The URL for this piece of content"""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def thumbnail_url(self) -> str:
    """The URL for a thumbnail for this piece of content, if applicable"""
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def entity_id(self) -> int:
    """The ID for the piece of content this pin represents"""
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: int):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, int):
      raise TypeError('entity_id must be of type int')
    self._entity_id = entity_id

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional['UserAvatar']):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    del self.owner_organization
    self._owner_user = owner_user

  @property
  def owner_organization(self) -> Optional['OrganizationCard']:
    return self._owner_organization or None

  @owner_organization.setter
  def owner_organization(self, owner_organization: Optional['OrganizationCard']):
    if owner_organization is None:
      del self.owner_organization
      return
    if not isinstance(owner_organization, OrganizationCard):
      raise TypeError('owner_organization must be of type OrganizationCard')
    del self.owner_user
    self._owner_organization = owner_organization

  @property
  def competition(self) -> Optional['CompetitionPin']:
    return self._competition or None

  @competition.setter
  def competition(self, competition: Optional['CompetitionPin']):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, CompetitionPin):
      raise TypeError('competition must be of type CompetitionPin')
    del self.model
    del self.write_up
    self._competition = competition

  @property
  def model(self) -> Optional['ModelPin']:
    return self._model or None

  @model.setter
  def model(self, model: Optional['ModelPin']):
    if model is None:
      del self.model
      return
    if not isinstance(model, ModelPin):
      raise TypeError('model must be of type ModelPin')
    del self.competition
    del self.write_up
    self._model = model

  @property
  def write_up(self) -> Optional['WriteUpPin']:
    return self._write_up or None

  @write_up.setter
  def write_up(self, write_up: Optional['WriteUpPin']):
    if write_up is None:
      del self.write_up
      return
    if not isinstance(write_up, WriteUpPin):
      raise TypeError('write_up must be of type WriteUpPin')
    del self.competition
    del self.model
    self._write_up = write_up

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['UserAvatar']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, UserAvatar) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type UserAvatar')
    self._collaborators = collaborators


class ProfileVisibilitySettings(KaggleObject):
  r"""
  Attributes:
    hidden_sections (ProfileSection)
      Profile sections that should be hidden in the UI.
    hidden_achievement_types (UserAchievementType)
      Profile progression cards that should be hidden in the UI.
    hidden_badge_ids (int)
      IDs of badges that should be hidden in the UI.
  """

  def __init__(self):
    self._hidden_sections = []
    self._hidden_achievement_types = []
    self._hidden_badge_ids = []
    self._freeze()

  @property
  def hidden_sections(self) -> Optional[List['ProfileSection']]:
    """Profile sections that should be hidden in the UI."""
    return self._hidden_sections

  @hidden_sections.setter
  def hidden_sections(self, hidden_sections: Optional[List['ProfileSection']]):
    if hidden_sections is None:
      del self.hidden_sections
      return
    if not isinstance(hidden_sections, list):
      raise TypeError('hidden_sections must be of type list')
    if not all([isinstance(t, ProfileSection) for t in hidden_sections]):
      raise TypeError('hidden_sections must contain only items of type ProfileSection')
    self._hidden_sections = hidden_sections

  @property
  def hidden_achievement_types(self) -> Optional[List['UserAchievementType']]:
    """Profile progression cards that should be hidden in the UI."""
    return self._hidden_achievement_types

  @hidden_achievement_types.setter
  def hidden_achievement_types(self, hidden_achievement_types: Optional[List['UserAchievementType']]):
    if hidden_achievement_types is None:
      del self.hidden_achievement_types
      return
    if not isinstance(hidden_achievement_types, list):
      raise TypeError('hidden_achievement_types must be of type list')
    if not all([isinstance(t, UserAchievementType) for t in hidden_achievement_types]):
      raise TypeError('hidden_achievement_types must contain only items of type UserAchievementType')
    self._hidden_achievement_types = hidden_achievement_types

  @property
  def hidden_badge_ids(self) -> Optional[List[int]]:
    """IDs of badges that should be hidden in the UI."""
    return self._hidden_badge_ids

  @hidden_badge_ids.setter
  def hidden_badge_ids(self, hidden_badge_ids: Optional[List[int]]):
    if hidden_badge_ids is None:
      del self.hidden_badge_ids
      return
    if not isinstance(hidden_badge_ids, list):
      raise TypeError('hidden_badge_ids must be of type list')
    if not all([isinstance(t, int) for t in hidden_badge_ids]):
      raise TypeError('hidden_badge_ids must contain only items of type int')
    self._hidden_badge_ids = hidden_badge_ids


class UpdateBioRequest(KaggleObject):
  r"""
  Attributes:
    bio (str)
      The new bio to be saved.
    user_id (int)
      The user this bio is for, usually the current user.
  """

  def __init__(self):
    self._bio = ""
    self._user_id = 0
    self._freeze()

  @property
  def bio(self) -> str:
    """The new bio to be saved."""
    return self._bio

  @bio.setter
  def bio(self, bio: str):
    if bio is None:
      del self.bio
      return
    if not isinstance(bio, str):
      raise TypeError('bio must be of type str')
    self._bio = bio

  @property
  def user_id(self) -> int:
    """The user this bio is for, usually the current user."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class UpdateBioResponse(KaggleObject):
  r"""
  """

  pass

class UpdateCompetitionProfileVisibilityRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    hidden (bool)
  """

  def __init__(self):
    self._competition_id = 0
    self._hidden = False
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
  def hidden(self) -> bool:
    return self._hidden

  @hidden.setter
  def hidden(self, hidden: bool):
    if hidden is None:
      del self.hidden
      return
    if not isinstance(hidden, bool):
      raise TypeError('hidden must be of type bool')
    self._hidden = hidden


class UpdateProfileImageRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The Id of the user to update the profile image.
    profile_image (CroppedImageUpload)
      The profile image along with a cropping rectangle.
  """

  def __init__(self):
    self._user_id = 0
    self._profile_image = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The Id of the user to update the profile image."""
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
  def profile_image(self) -> Optional['CroppedImageUpload']:
    """The profile image along with a cropping rectangle."""
    return self._profile_image

  @profile_image.setter
  def profile_image(self, profile_image: Optional['CroppedImageUpload']):
    if profile_image is None:
      del self.profile_image
      return
    if not isinstance(profile_image, CroppedImageUpload):
      raise TypeError('profile_image must be of type CroppedImageUpload')
    self._profile_image = profile_image


class UpdateProfileImageResponse(KaggleObject):
  r"""
  Attributes:
    image_url (str)
      URL for the primary profile image.
    thumbnail_url (str)
      URL for the smaller/thumbnail image.
  """

  def __init__(self):
    self._image_url = ""
    self._thumbnail_url = ""
    self._freeze()

  @property
  def image_url(self) -> str:
    """URL for the primary profile image."""
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def thumbnail_url(self) -> str:
    """URL for the smaller/thumbnail image."""
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url


class UpdateProfileRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The Id of the user being updated
    display_name (str)
      The user's display name
    git_hub_user_name (str)
      The user's username in github
    twitter_user_name (str)
      The user's username on twitter
    linked_in_url (str)
      A url corresponding to the user's linked in page
    city (str)
      City the user lives in
    region (str)
      Region the user lives in (state, province etc)
    country (str)
      Country the user lives in
    occupation (str)
      User's current occupation
    organization (str)
      Organization user currently works for
    website (str)
      A link to the user's website
    user_name (str)
      The username of the user being updated
    tagline (str)
      Tagline
    pronouns (str)
      Pronouns
    progression_opt_out (bool)
      Whether or not the user is opted out of progression
    location_sharing_opt_out (bool)
      Whether or not the requested user has opted out from sharing their location
  """

  def __init__(self):
    self._user_id = None
    self._display_name = None
    self._git_hub_user_name = None
    self._twitter_user_name = None
    self._linked_in_url = None
    self._city = None
    self._region = None
    self._country = None
    self._occupation = None
    self._organization = None
    self._website = None
    self._user_name = None
    self._tagline = None
    self._pronouns = None
    self._progression_opt_out = None
    self._location_sharing_opt_out = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The Id of the user being updated"""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    del self.user_name
    self._user_id = user_id

  @property
  def user_name(self) -> str:
    """The username of the user being updated"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.user_id
    self._user_name = user_name

  @property
  def display_name(self) -> str:
    """The user's display name"""
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def git_hub_user_name(self) -> str:
    """The user's username in github"""
    return self._git_hub_user_name or ""

  @git_hub_user_name.setter
  def git_hub_user_name(self, git_hub_user_name: Optional[str]):
    if git_hub_user_name is None:
      del self.git_hub_user_name
      return
    if not isinstance(git_hub_user_name, str):
      raise TypeError('git_hub_user_name must be of type str')
    self._git_hub_user_name = git_hub_user_name

  @property
  def twitter_user_name(self) -> str:
    """The user's username on twitter"""
    return self._twitter_user_name or ""

  @twitter_user_name.setter
  def twitter_user_name(self, twitter_user_name: Optional[str]):
    if twitter_user_name is None:
      del self.twitter_user_name
      return
    if not isinstance(twitter_user_name, str):
      raise TypeError('twitter_user_name must be of type str')
    self._twitter_user_name = twitter_user_name

  @property
  def linked_in_url(self) -> str:
    """A url corresponding to the user's linked in page"""
    return self._linked_in_url or ""

  @linked_in_url.setter
  def linked_in_url(self, linked_in_url: Optional[str]):
    if linked_in_url is None:
      del self.linked_in_url
      return
    if not isinstance(linked_in_url, str):
      raise TypeError('linked_in_url must be of type str')
    self._linked_in_url = linked_in_url

  @property
  def city(self) -> str:
    """City the user lives in"""
    return self._city or ""

  @city.setter
  def city(self, city: Optional[str]):
    if city is None:
      del self.city
      return
    if not isinstance(city, str):
      raise TypeError('city must be of type str')
    self._city = city

  @property
  def region(self) -> str:
    """Region the user lives in (state, province etc)"""
    return self._region or ""

  @region.setter
  def region(self, region: Optional[str]):
    if region is None:
      del self.region
      return
    if not isinstance(region, str):
      raise TypeError('region must be of type str')
    self._region = region

  @property
  def country(self) -> str:
    """Country the user lives in"""
    return self._country or ""

  @country.setter
  def country(self, country: Optional[str]):
    if country is None:
      del self.country
      return
    if not isinstance(country, str):
      raise TypeError('country must be of type str')
    self._country = country

  @property
  def occupation(self) -> str:
    """User's current occupation"""
    return self._occupation or ""

  @occupation.setter
  def occupation(self, occupation: Optional[str]):
    if occupation is None:
      del self.occupation
      return
    if not isinstance(occupation, str):
      raise TypeError('occupation must be of type str')
    self._occupation = occupation

  @property
  def organization(self) -> str:
    """Organization user currently works for"""
    return self._organization or ""

  @organization.setter
  def organization(self, organization: Optional[str]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, str):
      raise TypeError('organization must be of type str')
    self._organization = organization

  @property
  def website(self) -> str:
    """A link to the user's website"""
    return self._website or ""

  @website.setter
  def website(self, website: Optional[str]):
    if website is None:
      del self.website
      return
    if not isinstance(website, str):
      raise TypeError('website must be of type str')
    self._website = website

  @property
  def tagline(self) -> str:
    """Tagline"""
    return self._tagline or ""

  @tagline.setter
  def tagline(self, tagline: Optional[str]):
    if tagline is None:
      del self.tagline
      return
    if not isinstance(tagline, str):
      raise TypeError('tagline must be of type str')
    self._tagline = tagline

  @property
  def pronouns(self) -> str:
    """Pronouns"""
    return self._pronouns or ""

  @pronouns.setter
  def pronouns(self, pronouns: Optional[str]):
    if pronouns is None:
      del self.pronouns
      return
    if not isinstance(pronouns, str):
      raise TypeError('pronouns must be of type str')
    self._pronouns = pronouns

  @property
  def progression_opt_out(self) -> bool:
    """Whether or not the user is opted out of progression"""
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out

  @property
  def location_sharing_opt_out(self) -> bool:
    """Whether or not the requested user has opted out from sharing their location"""
    return self._location_sharing_opt_out or False

  @location_sharing_opt_out.setter
  def location_sharing_opt_out(self, location_sharing_opt_out: Optional[bool]):
    if location_sharing_opt_out is None:
      del self.location_sharing_opt_out
      return
    if not isinstance(location_sharing_opt_out, bool):
      raise TypeError('location_sharing_opt_out must be of type bool')
    self._location_sharing_opt_out = location_sharing_opt_out


class UpdateProfileResponse(KaggleObject):
  r"""
  Attributes:
    was_successful (bool)
    error_message (str)
    parsed_twitter_user_name (str)
    parsed_git_hub_user_name (str)
    parsed_linked_in_url (str)
    parsed_website (str)
    display_name (str)
  """

  def __init__(self):
    self._was_successful = False
    self._error_message = None
    self._parsed_twitter_user_name = None
    self._parsed_git_hub_user_name = None
    self._parsed_linked_in_url = None
    self._parsed_website = None
    self._display_name = None
    self._freeze()

  @property
  def was_successful(self) -> bool:
    return self._was_successful

  @was_successful.setter
  def was_successful(self, was_successful: bool):
    if was_successful is None:
      del self.was_successful
      return
    if not isinstance(was_successful, bool):
      raise TypeError('was_successful must be of type bool')
    self._was_successful = was_successful

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def parsed_twitter_user_name(self) -> str:
    return self._parsed_twitter_user_name or ""

  @parsed_twitter_user_name.setter
  def parsed_twitter_user_name(self, parsed_twitter_user_name: Optional[str]):
    if parsed_twitter_user_name is None:
      del self.parsed_twitter_user_name
      return
    if not isinstance(parsed_twitter_user_name, str):
      raise TypeError('parsed_twitter_user_name must be of type str')
    self._parsed_twitter_user_name = parsed_twitter_user_name

  @property
  def parsed_git_hub_user_name(self) -> str:
    return self._parsed_git_hub_user_name or ""

  @parsed_git_hub_user_name.setter
  def parsed_git_hub_user_name(self, parsed_git_hub_user_name: Optional[str]):
    if parsed_git_hub_user_name is None:
      del self.parsed_git_hub_user_name
      return
    if not isinstance(parsed_git_hub_user_name, str):
      raise TypeError('parsed_git_hub_user_name must be of type str')
    self._parsed_git_hub_user_name = parsed_git_hub_user_name

  @property
  def parsed_linked_in_url(self) -> str:
    return self._parsed_linked_in_url or ""

  @parsed_linked_in_url.setter
  def parsed_linked_in_url(self, parsed_linked_in_url: Optional[str]):
    if parsed_linked_in_url is None:
      del self.parsed_linked_in_url
      return
    if not isinstance(parsed_linked_in_url, str):
      raise TypeError('parsed_linked_in_url must be of type str')
    self._parsed_linked_in_url = parsed_linked_in_url

  @property
  def parsed_website(self) -> str:
    return self._parsed_website or ""

  @parsed_website.setter
  def parsed_website(self, parsed_website: Optional[str]):
    if parsed_website is None:
      del self.parsed_website
      return
    if not isinstance(parsed_website, str):
      raise TypeError('parsed_website must be of type str')
    self._parsed_website = parsed_website

  @property
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name


class UpdateProfileSectionOrderRequest(KaggleObject):
  r"""
  Attributes:
    section_order (ProfileSection)
      New section order for the About tab.
  """

  def __init__(self):
    self._section_order = []
    self._freeze()

  @property
  def section_order(self) -> Optional[List['ProfileSection']]:
    """New section order for the About tab."""
    return self._section_order

  @section_order.setter
  def section_order(self, section_order: Optional[List['ProfileSection']]):
    if section_order is None:
      del self.section_order
      return
    if not isinstance(section_order, list):
      raise TypeError('section_order must be of type list')
    if not all([isinstance(t, ProfileSection) for t in section_order]):
      raise TypeError('section_order must contain only items of type ProfileSection')
    self._section_order = section_order


class UpdateProfileVisibilityRequest(KaggleObject):
  r"""
  Attributes:
    visibility_settings (ProfileVisibilitySettings)
      New profile visibility settings.
  """

  def __init__(self):
    self._visibility_settings = None
    self._freeze()

  @property
  def visibility_settings(self) -> Optional['ProfileVisibilitySettings']:
    """New profile visibility settings."""
    return self._visibility_settings

  @visibility_settings.setter
  def visibility_settings(self, visibility_settings: Optional['ProfileVisibilitySettings']):
    if visibility_settings is None:
      del self.visibility_settings
      return
    if not isinstance(visibility_settings, ProfileVisibilitySettings):
      raise TypeError('visibility_settings must be of type ProfileVisibilitySettings')
    self._visibility_settings = visibility_settings


class WriteUpCounts(KaggleObject):
  r"""
  Attributes:
    competition_solution_write_ups_count (int)
      Number of Competition Solution WriteUps authored by the user
    hackathon_write_ups_count (int)
      Number of Hackathon WriteUps authored by the user
    knowledge_write_ups_count (int)
      Number of Knowledge WriteUps authored by the user
    personal_project_write_ups_count (int)
      Number of Personal Project WriteUps authored by the user
    total_comments_count (int)
      Number of all comments left on all user's WriteUps
  """

  def __init__(self):
    self._competition_solution_write_ups_count = 0
    self._hackathon_write_ups_count = 0
    self._knowledge_write_ups_count = 0
    self._personal_project_write_ups_count = 0
    self._total_comments_count = 0
    self._freeze()

  @property
  def competition_solution_write_ups_count(self) -> int:
    """Number of Competition Solution WriteUps authored by the user"""
    return self._competition_solution_write_ups_count

  @competition_solution_write_ups_count.setter
  def competition_solution_write_ups_count(self, competition_solution_write_ups_count: int):
    if competition_solution_write_ups_count is None:
      del self.competition_solution_write_ups_count
      return
    if not isinstance(competition_solution_write_ups_count, int):
      raise TypeError('competition_solution_write_ups_count must be of type int')
    self._competition_solution_write_ups_count = competition_solution_write_ups_count

  @property
  def hackathon_write_ups_count(self) -> int:
    """Number of Hackathon WriteUps authored by the user"""
    return self._hackathon_write_ups_count

  @hackathon_write_ups_count.setter
  def hackathon_write_ups_count(self, hackathon_write_ups_count: int):
    if hackathon_write_ups_count is None:
      del self.hackathon_write_ups_count
      return
    if not isinstance(hackathon_write_ups_count, int):
      raise TypeError('hackathon_write_ups_count must be of type int')
    self._hackathon_write_ups_count = hackathon_write_ups_count

  @property
  def knowledge_write_ups_count(self) -> int:
    """Number of Knowledge WriteUps authored by the user"""
    return self._knowledge_write_ups_count

  @knowledge_write_ups_count.setter
  def knowledge_write_ups_count(self, knowledge_write_ups_count: int):
    if knowledge_write_ups_count is None:
      del self.knowledge_write_ups_count
      return
    if not isinstance(knowledge_write_ups_count, int):
      raise TypeError('knowledge_write_ups_count must be of type int')
    self._knowledge_write_ups_count = knowledge_write_ups_count

  @property
  def personal_project_write_ups_count(self) -> int:
    """Number of Personal Project WriteUps authored by the user"""
    return self._personal_project_write_ups_count

  @personal_project_write_ups_count.setter
  def personal_project_write_ups_count(self, personal_project_write_ups_count: int):
    if personal_project_write_ups_count is None:
      del self.personal_project_write_ups_count
      return
    if not isinstance(personal_project_write_ups_count, int):
      raise TypeError('personal_project_write_ups_count must be of type int')
    self._personal_project_write_ups_count = personal_project_write_ups_count

  @property
  def total_comments_count(self) -> int:
    """Number of all comments left on all user's WriteUps"""
    return self._total_comments_count

  @total_comments_count.setter
  def total_comments_count(self, total_comments_count: int):
    if total_comments_count is None:
      del self.total_comments_count
      return
    if not isinstance(total_comments_count, int):
      raise TypeError('total_comments_count must be of type int')
    self._total_comments_count = total_comments_count


class WriteUpPin(KaggleObject):
  r"""
  Attributes:
    message_stripped (str)
      Stripped message content for the preview
    type (WriteUpType)
      Type of WriteUp used for different contexts (i.e. competition vs hackathon
      WriteUp)
    tags (Tag)
      List of tags connected to the WriteUp
    collaborators (UserAvatar)
      List of WriteUp collaborators
    competition_info (WriteUpCompetitionInfo)
      Competition metadata associated with WriteUp
    team_name (str)
      Name of the team that owns the WriteUp
    forum_topic_id (int)
      Id of the ForumTopic
  """

  def __init__(self):
    self._message_stripped = ""
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._tags = []
    self._collaborators = []
    self._competition_info = None
    self._team_name = None
    self._forum_topic_id = 0
    self._freeze()

  @property
  def message_stripped(self) -> str:
    """Stripped message content for the preview"""
    return self._message_stripped

  @message_stripped.setter
  def message_stripped(self, message_stripped: str):
    if message_stripped is None:
      del self.message_stripped
      return
    if not isinstance(message_stripped, str):
      raise TypeError('message_stripped must be of type str')
    self._message_stripped = message_stripped

  @property
  def type(self) -> 'WriteUpType':
    r"""
    Type of WriteUp used for different contexts (i.e. competition vs hackathon
    WriteUp)
    """
    return self._type

  @type.setter
  def type(self, type: 'WriteUpType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, WriteUpType):
      raise TypeError('type must be of type WriteUpType')
    self._type = type

  @property
  def tags(self) -> Optional[List[Optional['Tag']]]:
    """List of tags connected to the WriteUp"""
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['Tag']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, Tag) for t in tags]):
      raise TypeError('tags must contain only items of type Tag')
    self._tags = tags

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of WriteUp collaborators"""
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['UserAvatar']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, UserAvatar) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type UserAvatar')
    self._collaborators = collaborators

  @property
  def competition_info(self) -> Optional['WriteUpCompetitionInfo']:
    """Competition metadata associated with WriteUp"""
    return self._competition_info or None

  @competition_info.setter
  def competition_info(self, competition_info: Optional[Optional['WriteUpCompetitionInfo']]):
    if competition_info is None:
      del self.competition_info
      return
    if not isinstance(competition_info, WriteUpCompetitionInfo):
      raise TypeError('competition_info must be of type WriteUpCompetitionInfo')
    self._competition_info = competition_info

  @property
  def team_name(self) -> str:
    """Name of the team that owns the WriteUp"""
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
  def forum_topic_id(self) -> int:
    """Id of the ForumTopic"""
    return self._forum_topic_id

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id


AchievementSummary._fields = [
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("summaryType", "summary_type", "_summary_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("rankPercentage", "rank_percentage", "_rank_percentage", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rankOutOf", "rank_out_of", "_rank_out_of", int, 0, PredefinedSerializer()),
  FieldMetadata("rankCurrent", "rank_current", "_rank_current", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rankHighest", "rank_highest", "_rank_highest", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalGoldMedals", "total_gold_medals", "_total_gold_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSilverMedals", "total_silver_medals", "_total_silver_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBronzeMedals", "total_bronze_medals", "_total_bronze_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("legacyTier", "legacy_tier", "_legacy_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
]

ActivityCalendar._fields = [
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("totalSubmissionsCount", "total_submissions_count", "_total_submissions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalScriptsCount", "total_scripts_count", "_total_scripts_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDiscussionsCount", "total_discussions_count", "_total_discussions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDatasetsCount", "total_datasets_count", "_total_datasets_count", int, 0, PredefinedSerializer()),
]

CompetitionPin._fields = [
  FieldMetadata("rank", "rank", "_rank", int, 0, PredefinedSerializer()),
  FieldMetadata("totalTeamCount", "total_team_count", "_total_team_count", int, 0, PredefinedSerializer()),
  FieldMetadata("isHost", "is_host", "_is_host", bool, False, PredefinedSerializer()),
  FieldMetadata("totalJoinedUsers", "total_joined_users", "_total_joined_users", int, 0, PredefinedSerializer()),
]

CreateProfilePinRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("learnTrackId", "learn_track_id", "_learn_track_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, None, PredefinedSerializer(), optional=True),
]

DeleteProfilePinRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("learnTrackId", "learn_track_id", "_learn_track_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, None, PredefinedSerializer(), optional=True),
]

DiscussionCounts._fields = [
  FieldMetadata("totalDiscussionsCount", "total_discussions_count", "_total_discussions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalTopicsCount", "total_topics_count", "_total_topics_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalRepliesCount", "total_replies_count", "_total_replies_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalUpvotesCount", "total_upvotes_count", "_total_upvotes_count", int, 0, PredefinedSerializer()),
]

GetProfilePreviewRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
]

GetProfilePreviewResponse._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("performanceTier", "performance_tier", "_performance_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("country", "country", "_country", str, "", PredefinedSerializer()),
  FieldMetadata("region", "region", "_region", str, "", PredefinedSerializer()),
  FieldMetadata("city", "city", "_city", str, "", PredefinedSerializer()),
  FieldMetadata("occupation", "occupation", "_occupation", str, "", PredefinedSerializer()),
  FieldMetadata("canBeSeen", "can_be_seen", "_can_be_seen", bool, False, PredefinedSerializer()),
  FieldMetadata("organization", "organization", "_organization", str, "", PredefinedSerializer()),
  FieldMetadata("pronouns", "pronouns", "_pronouns", str, "", PredefinedSerializer()),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, False, PredefinedSerializer()),
]

GetProfileRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

GetProfileResponse._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("country", "country", "_country", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("region", "region", "_region", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("city", "city", "_city", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gitHubUserName", "git_hub_user_name", "_git_hub_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("twitterUserName", "twitter_user_name", "_twitter_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("linkedInUrl", "linked_in_url", "_linked_in_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("websiteUrl", "website_url", "_website_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("occupation", "occupation", "_occupation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bio", "bio", "_bio", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userLastActive", "user_last_active", "_user_last_active", datetime, None, DateTimeSerializer()),
  FieldMetadata("userJoinDate", "user_join_date", "_user_join_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("performanceTier", "performance_tier", "_performance_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("performanceTierCategory", "performance_tier_category", "_performance_tier_category", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userAvatarUrl", "user_avatar_url", "_user_avatar_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canEdit", "can_edit", "_can_edit", bool, False, PredefinedSerializer()),
  FieldMetadata("achievementSummaries", "achievement_summaries", "_achievement_summaries", AchievementSummary, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalUsersIFollow", "total_users_i_follow", "_total_users_i_follow", int, 0, PredefinedSerializer()),
  FieldMetadata("totalUsersFollowingMe", "total_users_following_me", "_total_users_following_me", int, 0, PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tagline", "tagline", "_tagline", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pronouns", "pronouns", "_pronouns", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalKernels", "total_kernels", "_total_kernels", int, 0, PredefinedSerializer()),
  FieldMetadata("totalCompetitions", "total_competitions", "_total_competitions", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDatasets", "total_datasets", "_total_datasets", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDiscussions", "total_discussions", "_total_discussions", int, 0, PredefinedSerializer()),
  FieldMetadata("totalModels", "total_models", "_total_models", int, 0, PredefinedSerializer()),
  FieldMetadata("badges", "badges", "_badges", UserBadge, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("visibilitySettings", "visibility_settings", "_visibility_settings", ProfileVisibilitySettings, None, KaggleObjectSerializer()),
  FieldMetadata("totalHostedCompetitions", "total_hosted_competitions", "_total_hosted_competitions", int, 0, PredefinedSerializer()),
  FieldMetadata("totalActiveCompetitions", "total_active_competitions", "_total_active_competitions", int, 0, PredefinedSerializer()),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("currentUserFollowsThisUser", "current_user_follows_this_user", "_current_user_follows_this_user", bool, False, PredefinedSerializer()),
  FieldMetadata("locationSharingOptOut", "location_sharing_opt_out", "_location_sharing_opt_out", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizations", "organizations", "_organizations", Organization, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalGrandmasterLevel", "total_grandmaster_level", "_total_grandmaster_level", int, 0, PredefinedSerializer()),
  FieldMetadata("totalWriteUps", "total_write_ups", "_total_write_ups", int, 0, PredefinedSerializer()),
  FieldMetadata("sectionOrder", "section_order", "_section_order", ProfileSection, [], ListSerializer(EnumSerializer())),
  FieldMetadata("totalBenchmarks", "total_benchmarks", "_total_benchmarks", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBenchmarkTasks", "total_benchmark_tasks", "_total_benchmark_tasks", int, 0, PredefinedSerializer()),
]

GetUserActivityRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

GetUserActivityResponse._fields = [
  FieldMetadata("activities", "activities", "_activities", ActivityCalendar, [], ListSerializer(KaggleObjectSerializer())),
]

GetUserDiscussionCountsRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

GetUserWriteUpCountsRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

ListFollowersRequest._fields = [
  FieldMetadata("userIdType", "user_id_type", "_user_id_type", ListFollowersUserIdType, ListFollowersUserIdType.LIST_FOLLOWERS_USER_ID_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListFollowersResponse._fields = [
  FieldMetadata("followers", "followers", "_followers", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalFollowers", "total_followers", "_total_followers", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListProfilePinsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

ListProfilePinsResponse._fields = [
  FieldMetadata("profilePins", "profile_pins", "_profile_pins", ProfilePin, [], ListSerializer(KaggleObjectSerializer())),
]

ModelPin._fields = [
  FieldMetadata("downloadCount", "download_count", "_download_count", int, 0, PredefinedSerializer()),
]

ProfilePin._fields = [
  FieldMetadata("type", "type", "_type", ProfilePinType, ProfilePinType.PROFILE_PIN_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("upvoteCount", "upvote_count", "_upvote_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", Medal, None, EnumSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("ownerOrganization", "owner_organization", "_owner_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competition", "competition", "_competition", CompetitionPin, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("model", "model", "_model", ModelPin, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("writeUp", "write_up", "_write_up", WriteUpPin, None, KaggleObjectSerializer(), optional=True),
]

ProfileVisibilitySettings._fields = [
  FieldMetadata("hiddenSections", "hidden_sections", "_hidden_sections", ProfileSection, [], ListSerializer(EnumSerializer())),
  FieldMetadata("hiddenAchievementTypes", "hidden_achievement_types", "_hidden_achievement_types", UserAchievementType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("hiddenBadgeIds", "hidden_badge_ids", "_hidden_badge_ids", int, [], ListSerializer(PredefinedSerializer())),
]

UpdateBioRequest._fields = [
  FieldMetadata("bio", "bio", "_bio", str, "", PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UpdateBioResponse._fields = []

UpdateCompetitionProfileVisibilityRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hidden", "hidden", "_hidden", bool, False, PredefinedSerializer()),
]

UpdateProfileImageRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("profileImage", "profile_image", "_profile_image", CroppedImageUpload, None, KaggleObjectSerializer()),
]

UpdateProfileImageResponse._fields = [
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
]

UpdateProfileRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gitHubUserName", "git_hub_user_name", "_git_hub_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("twitterUserName", "twitter_user_name", "_twitter_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("linkedInUrl", "linked_in_url", "_linked_in_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("city", "city", "_city", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("region", "region", "_region", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("country", "country", "_country", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("occupation", "occupation", "_occupation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("website", "website", "_website", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tagline", "tagline", "_tagline", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pronouns", "pronouns", "_pronouns", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("locationSharingOptOut", "location_sharing_opt_out", "_location_sharing_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

UpdateProfileResponse._fields = [
  FieldMetadata("wasSuccessful", "was_successful", "_was_successful", bool, False, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parsedTwitterUserName", "parsed_twitter_user_name", "_parsed_twitter_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parsedGitHubUserName", "parsed_git_hub_user_name", "_parsed_git_hub_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parsedLinkedInUrl", "parsed_linked_in_url", "_parsed_linked_in_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parsedWebsite", "parsed_website", "_parsed_website", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
]

UpdateProfileSectionOrderRequest._fields = [
  FieldMetadata("sectionOrder", "section_order", "_section_order", ProfileSection, [], ListSerializer(EnumSerializer())),
]

UpdateProfileVisibilityRequest._fields = [
  FieldMetadata("visibilitySettings", "visibility_settings", "_visibility_settings", ProfileVisibilitySettings, None, KaggleObjectSerializer()),
]

WriteUpCounts._fields = [
  FieldMetadata("competitionSolutionWriteUpsCount", "competition_solution_write_ups_count", "_competition_solution_write_ups_count", int, 0, PredefinedSerializer()),
  FieldMetadata("hackathonWriteUpsCount", "hackathon_write_ups_count", "_hackathon_write_ups_count", int, 0, PredefinedSerializer()),
  FieldMetadata("knowledgeWriteUpsCount", "knowledge_write_ups_count", "_knowledge_write_ups_count", int, 0, PredefinedSerializer()),
  FieldMetadata("personalProjectWriteUpsCount", "personal_project_write_ups_count", "_personal_project_write_ups_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalCommentsCount", "total_comments_count", "_total_comments_count", int, 0, PredefinedSerializer()),
]

WriteUpPin._fields = [
  FieldMetadata("messageStripped", "message_stripped", "_message_stripped", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("competitionInfo", "competition_info", "_competition_info", WriteUpCompetitionInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
]

