import enum
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_content_shared import ListSearchContentRangeFilter
from kagglesdk.users.types.progression_service import UserAchievementType
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class SearchUsersOrderBy(enum.Enum):
  SEARCH_USERS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_USERS_ORDER_BY_COMPETITION_RANKING = 1
  """Ordered by current competition ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_KERNEL_RANKING = 2
  """Ordered by current kernel ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_DATASET_RANKING = 3
  """Ordered by current dataset ranking, ascending (best rank first)."""
  SEARCH_USERS_ORDER_BY_DISPLAY_NAME = 4
  """Ordered by display name, alphabetically, ascending."""
  SEARCH_USERS_ORDER_BY_TIER_AND_LEVEL = 5
  r"""
  Ordered by tier and tier levels, descending. Tier levels are awarded
  starting at Grandmaster. The first user returned will have the highest tier
  and level (GM 7x, etc.).
  """
  SEARCH_USERS_ORDER_BY_OLDEST_JOIN_DATE = 6
  """Ordered by user create date, ascending (i.e. oldest account first)."""
  SEARCH_USERS_ORDER_BY_NEWEST_JOIN_DATE = 7
  """Ordered by user create date, descending (i.e. newest account first)."""

class SearchUsersDocument(KaggleObject):
  r"""
  Attributes:
    grandmaster_tier_level (int)
      User's GM tier level. Tier levels are awarded starting at GM. All
      users who are not GM will have a tier level of 0.
    user_location (str)
      User location string, if location sharing is opted-in. In the format:
      'city, region, country'.
    competition_ranking (int)
      *_ranking and *_points fields below may be unset if the user is opted-out
      of progression. Additionally, *_ranking fields may be unset if the user
      doesn't have any points.

      Current ranking for the user in the competition achievement type.
    competition_points (int)
      Current points for the user in the competition achievement type.
    kernel_ranking (int)
      Current ranking for the user in the kernel achievement type.
    kernel_points (int)
      Current points for the user in the kernel achievement type.
    dataset_ranking (int)
      Current ranking for the user in dataset achievement type.
    dataset_points (int)
      Current points for the user in the dataset achievement type.
    occupation_organization_name (str)
      Occupation organization name as indicated on the user's profile.
  """

  def __init__(self):
    self._grandmaster_tier_level = 0
    self._user_location = None
    self._competition_ranking = None
    self._competition_points = None
    self._kernel_ranking = None
    self._kernel_points = None
    self._dataset_ranking = None
    self._dataset_points = None
    self._occupation_organization_name = None
    self._freeze()

  @property
  def grandmaster_tier_level(self) -> int:
    r"""
    User's GM tier level. Tier levels are awarded starting at GM. All
    users who are not GM will have a tier level of 0.
    """
    return self._grandmaster_tier_level

  @grandmaster_tier_level.setter
  def grandmaster_tier_level(self, grandmaster_tier_level: int):
    if grandmaster_tier_level is None:
      del self.grandmaster_tier_level
      return
    if not isinstance(grandmaster_tier_level, int):
      raise TypeError('grandmaster_tier_level must be of type int')
    self._grandmaster_tier_level = grandmaster_tier_level

  @property
  def user_location(self) -> str:
    r"""
    User location string, if location sharing is opted-in. In the format:
    'city, region, country'.
    """
    return self._user_location or ""

  @user_location.setter
  def user_location(self, user_location: Optional[str]):
    if user_location is None:
      del self.user_location
      return
    if not isinstance(user_location, str):
      raise TypeError('user_location must be of type str')
    self._user_location = user_location

  @property
  def occupation_organization_name(self) -> str:
    """Occupation organization name as indicated on the user's profile."""
    return self._occupation_organization_name or ""

  @occupation_organization_name.setter
  def occupation_organization_name(self, occupation_organization_name: Optional[str]):
    if occupation_organization_name is None:
      del self.occupation_organization_name
      return
    if not isinstance(occupation_organization_name, str):
      raise TypeError('occupation_organization_name must be of type str')
    self._occupation_organization_name = occupation_organization_name

  @property
  def competition_ranking(self) -> int:
    r"""
    *_ranking and *_points fields below may be unset if the user is opted-out
    of progression. Additionally, *_ranking fields may be unset if the user
    doesn't have any points.

    Current ranking for the user in the competition achievement type.
    """
    return self._competition_ranking or 0

  @competition_ranking.setter
  def competition_ranking(self, competition_ranking: Optional[int]):
    if competition_ranking is None:
      del self.competition_ranking
      return
    if not isinstance(competition_ranking, int):
      raise TypeError('competition_ranking must be of type int')
    self._competition_ranking = competition_ranking

  @property
  def competition_points(self) -> int:
    """Current points for the user in the competition achievement type."""
    return self._competition_points or 0

  @competition_points.setter
  def competition_points(self, competition_points: Optional[int]):
    if competition_points is None:
      del self.competition_points
      return
    if not isinstance(competition_points, int):
      raise TypeError('competition_points must be of type int')
    self._competition_points = competition_points

  @property
  def kernel_ranking(self) -> int:
    """Current ranking for the user in the kernel achievement type."""
    return self._kernel_ranking or 0

  @kernel_ranking.setter
  def kernel_ranking(self, kernel_ranking: Optional[int]):
    if kernel_ranking is None:
      del self.kernel_ranking
      return
    if not isinstance(kernel_ranking, int):
      raise TypeError('kernel_ranking must be of type int')
    self._kernel_ranking = kernel_ranking

  @property
  def kernel_points(self) -> int:
    """Current points for the user in the kernel achievement type."""
    return self._kernel_points or 0

  @kernel_points.setter
  def kernel_points(self, kernel_points: Optional[int]):
    if kernel_points is None:
      del self.kernel_points
      return
    if not isinstance(kernel_points, int):
      raise TypeError('kernel_points must be of type int')
    self._kernel_points = kernel_points

  @property
  def dataset_ranking(self) -> int:
    """Current ranking for the user in dataset achievement type."""
    return self._dataset_ranking or 0

  @dataset_ranking.setter
  def dataset_ranking(self, dataset_ranking: Optional[int]):
    if dataset_ranking is None:
      del self.dataset_ranking
      return
    if not isinstance(dataset_ranking, int):
      raise TypeError('dataset_ranking must be of type int')
    self._dataset_ranking = dataset_ranking

  @property
  def dataset_points(self) -> int:
    """Current points for the user in the dataset achievement type."""
    return self._dataset_points or 0

  @dataset_points.setter
  def dataset_points(self, dataset_points: Optional[int]):
    if dataset_points is None:
      del self.dataset_points
      return
    if not isinstance(dataset_points, int):
      raise TypeError('dataset_points must be of type int')
    self._dataset_points = dataset_points


class SearchUsersFilters(KaggleObject):
  r"""
  Used by kaggle.search.ListSearchContent for filtering lists of users.

  Attributes:
    user_locations (str)
      Filter to users that have one of the the specified locations. Expects the
      format: 'city, region, country' for each.
    tier (UserAchievementTier)
      Filter to users that have the specified performance tier.
    user_ids (int)
      Filter to users based on the provided user ids.
    require_ranking_for_type (UserAchievementType)
      Filter to users that have points for the specified type.
    occupation_organization_names (str)
      Filter to users that have one of the provided occupation organization names
      indicated on their user profile, i.e. http://screen/3N68JKC4hocxWmn. Note:
      This is *not* the same thing as a Kaggle Organization, such as
      kaggle.com/organizations/google.
    grandmaster_level (ListSearchContentRangeFilter)
      Filter to users that have the specified range of Grandmaster tier level.
  """

  def __init__(self):
    self._user_locations = []
    self._tier = None
    self._user_ids = []
    self._require_ranking_for_type = None
    self._occupation_organization_names = []
    self._grandmaster_level = None
    self._freeze()

  @property
  def user_locations(self) -> Optional[List[str]]:
    r"""
    Filter to users that have one of the the specified locations. Expects the
    format: 'city, region, country' for each.
    """
    return self._user_locations

  @user_locations.setter
  def user_locations(self, user_locations: Optional[List[str]]):
    if user_locations is None:
      del self.user_locations
      return
    if not isinstance(user_locations, list):
      raise TypeError('user_locations must be of type list')
    if not all([isinstance(t, str) for t in user_locations]):
      raise TypeError('user_locations must contain only items of type str')
    self._user_locations = user_locations

  @property
  def tier(self) -> 'UserAchievementTier':
    """Filter to users that have the specified performance tier."""
    return self._tier or UserAchievementTier.NOVICE

  @tier.setter
  def tier(self, tier: Optional['UserAchievementTier']):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, UserAchievementTier):
      raise TypeError('tier must be of type UserAchievementTier')
    self._tier = tier

  @property
  def user_ids(self) -> Optional[List[int]]:
    """Filter to users based on the provided user ids."""
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

  @property
  def require_ranking_for_type(self) -> 'UserAchievementType':
    """Filter to users that have points for the specified type."""
    return self._require_ranking_for_type or UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED

  @require_ranking_for_type.setter
  def require_ranking_for_type(self, require_ranking_for_type: Optional['UserAchievementType']):
    if require_ranking_for_type is None:
      del self.require_ranking_for_type
      return
    if not isinstance(require_ranking_for_type, UserAchievementType):
      raise TypeError('require_ranking_for_type must be of type UserAchievementType')
    self._require_ranking_for_type = require_ranking_for_type

  @property
  def occupation_organization_names(self) -> Optional[List[str]]:
    r"""
    Filter to users that have one of the provided occupation organization names
    indicated on their user profile, i.e. http://screen/3N68JKC4hocxWmn. Note:
    This is *not* the same thing as a Kaggle Organization, such as
    kaggle.com/organizations/google.
    """
    return self._occupation_organization_names

  @occupation_organization_names.setter
  def occupation_organization_names(self, occupation_organization_names: Optional[List[str]]):
    if occupation_organization_names is None:
      del self.occupation_organization_names
      return
    if not isinstance(occupation_organization_names, list):
      raise TypeError('occupation_organization_names must be of type list')
    if not all([isinstance(t, str) for t in occupation_organization_names]):
      raise TypeError('occupation_organization_names must contain only items of type str')
    self._occupation_organization_names = occupation_organization_names

  @property
  def grandmaster_level(self) -> Optional['ListSearchContentRangeFilter']:
    """Filter to users that have the specified range of Grandmaster tier level."""
    return self._grandmaster_level

  @grandmaster_level.setter
  def grandmaster_level(self, grandmaster_level: Optional['ListSearchContentRangeFilter']):
    if grandmaster_level is None:
      del self.grandmaster_level
      return
    if not isinstance(grandmaster_level, ListSearchContentRangeFilter):
      raise TypeError('grandmaster_level must be of type ListSearchContentRangeFilter')
    self._grandmaster_level = grandmaster_level


SearchUsersDocument._fields = [
  FieldMetadata("grandmasterTierLevel", "grandmaster_tier_level", "_grandmaster_tier_level", int, 0, PredefinedSerializer()),
  FieldMetadata("userLocation", "user_location", "_user_location", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionRanking", "competition_ranking", "_competition_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionPoints", "competition_points", "_competition_points", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelRanking", "kernel_ranking", "_kernel_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelPoints", "kernel_points", "_kernel_points", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetRanking", "dataset_ranking", "_dataset_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetPoints", "dataset_points", "_dataset_points", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("occupationOrganizationName", "occupation_organization_name", "_occupation_organization_name", str, None, PredefinedSerializer(), optional=True),
]

SearchUsersFilters._fields = [
  FieldMetadata("userLocations", "user_locations", "_user_locations", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("requireRankingForType", "require_ranking_for_type", "_require_ranking_for_type", UserAchievementType, None, EnumSerializer(), optional=True),
  FieldMetadata("occupationOrganizationNames", "occupation_organization_names", "_occupation_organization_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("grandmasterLevel", "grandmaster_level", "_grandmaster_level", ListSearchContentRangeFilter, None, KaggleObjectSerializer()),
]

