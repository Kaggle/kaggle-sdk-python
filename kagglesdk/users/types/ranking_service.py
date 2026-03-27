from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.progression_service import UserAchievementType
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import List, Optional

class UserRankingHistoryType(enum.Enum):
  USER_RANKING_HISTORY_TYPE_UNSPECIFIED = 0
  BEST_RANKING = 1
  r"""
  By default, we use the best of computed or recorded rankings for
  each point in time. This is the same as the prod behavior.
  """
  COMPUTED_RANKINGS_ONLY = 2
  """Only use computed rankings from UserRankingHistory table."""
  RECORDED_RANKINGS_ONLY = 3
  r"""
  Only use recorded rankings from UserRankingRecordedHistory table.
  Note: To make the implementation simpler, we still use the list of dates
  populated in UserRankingHistory. So if a date is missing in
  UserRankingRecordedHistory, it will appear as a 0. This shouldn't happen
  in practice, and it's a bug in our data if we see it.
  """

class GetUserMedalCountsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User id to fetch user achievement medal counts.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """User id to fetch user achievement medal counts."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserMedalCountsResponse(KaggleObject):
  r"""
  Attributes:
    medal_counts (MedalCount)
  """

  def __init__(self):
    self._medal_counts = []
    self._freeze()

  @property
  def medal_counts(self) -> Optional[List[Optional['MedalCount']]]:
    return self._medal_counts

  @medal_counts.setter
  def medal_counts(self, medal_counts: Optional[List[Optional['MedalCount']]]):
    if medal_counts is None:
      del self.medal_counts
      return
    if not isinstance(medal_counts, list):
      raise TypeError('medal_counts must be of type list')
    if not all([isinstance(t, MedalCount) for t in medal_counts]):
      raise TypeError('medal_counts must contain only items of type MedalCount')
    self._medal_counts = medal_counts


class GetUserRankingHistoryRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User id to fetch detailed ranking history.
    admin_only_history_type (UserRankingHistoryType)
      Admin-only request option to set the specific type of ranking history to
      render. This is useful for debugging, because by default we use the best of
      computed and recorded rankings, which masks issues in one of the sources.
  """

  def __init__(self):
    self._user_id = 0
    self._admin_only_history_type = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """User id to fetch detailed ranking history."""
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
  def admin_only_history_type(self) -> 'UserRankingHistoryType':
    r"""
    Admin-only request option to set the specific type of ranking history to
    render. This is useful for debugging, because by default we use the best of
    computed and recorded rankings, which masks issues in one of the sources.
    """
    return self._admin_only_history_type or UserRankingHistoryType.USER_RANKING_HISTORY_TYPE_UNSPECIFIED

  @admin_only_history_type.setter
  def admin_only_history_type(self, admin_only_history_type: Optional['UserRankingHistoryType']):
    if admin_only_history_type is None:
      del self.admin_only_history_type
      return
    if not isinstance(admin_only_history_type, UserRankingHistoryType):
      raise TypeError('admin_only_history_type must be of type UserRankingHistoryType')
    self._admin_only_history_type = admin_only_history_type


class GetUserRankingsCountsRequest(KaggleObject):
  r"""
  """

  pass

class GetUserRankingsCountsResponse(KaggleObject):
  r"""
  Attributes:
    counts (UserAchievementLeaderboardCounts)
  """

  def __init__(self):
    self._counts = []
    self._freeze()

  @property
  def counts(self) -> Optional[List[Optional['UserAchievementLeaderboardCounts']]]:
    return self._counts

  @counts.setter
  def counts(self, counts: Optional[List[Optional['UserAchievementLeaderboardCounts']]]):
    if counts is None:
      del self.counts
      return
    if not isinstance(counts, list):
      raise TypeError('counts must be of type list')
    if not all([isinstance(t, UserAchievementLeaderboardCounts) for t in counts]):
      raise TypeError('counts must contain only items of type UserAchievementLeaderboardCounts')
    self._counts = counts


class GetUserRankingsV2Request(KaggleObject):
  r"""
  Attributes:
    type (UserAchievementType)
      The achievement type to obtain the user rankings for.
    filters (UserRankingsFilters)
      Optional user rankings filters, e.g. query string, user profile
      organization, user location.
    page_token (str)
      Page token for paging (see aip.dev/158)
    page_size (int)
      Number of documents per page to return
    skip (int)
      How many results to skip
    skip_for_caching (int)
      TODO(b/430080319):A hack used for page caching, to avoid reading the
      same relative skip from a page token.
  """

  def __init__(self):
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._filters = None
    self._page_token = ""
    self._page_size = None
    self._skip = 0
    self._skip_for_caching = 0
    self._freeze()

  @property
  def type(self) -> 'UserAchievementType':
    """The achievement type to obtain the user rankings for."""
    return self._type

  @type.setter
  def type(self, type: 'UserAchievementType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, UserAchievementType):
      raise TypeError('type must be of type UserAchievementType')
    self._type = type

  @property
  def filters(self) -> Optional['UserRankingsFilters']:
    r"""
    Optional user rankings filters, e.g. query string, user profile
    organization, user location.
    """
    return self._filters

  @filters.setter
  def filters(self, filters: Optional['UserRankingsFilters']):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, UserRankingsFilters):
      raise TypeError('filters must be of type UserRankingsFilters')
    self._filters = filters

  @property
  def page_token(self) -> str:
    """Page token for paging (see aip.dev/158)"""
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def page_size(self) -> int:
    """Number of documents per page to return"""
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
  def skip(self) -> int:
    """How many results to skip"""
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def skip_for_caching(self) -> int:
    r"""
    TODO(b/430080319):A hack used for page caching, to avoid reading the
    same relative skip from a page token.
    """
    return self._skip_for_caching

  @skip_for_caching.setter
  def skip_for_caching(self, skip_for_caching: int):
    if skip_for_caching is None:
      del self.skip_for_caching
      return
    if not isinstance(skip_for_caching, int):
      raise TypeError('skip_for_caching must be of type int')
    self._skip_for_caching = skip_for_caching


class GetUserRankingsV2Response(KaggleObject):
  r"""
  Attributes:
    current_user_ranking (LeaderboardsListItem)
      The current user ranking for the requested user achievement type. May be
      null if the current user isn't eligible for a ranking, or for the current
      set of filters in the request.
    user_rankings (LeaderboardsListItem)
      The user rankings for the requested user achievement type.
    next_page_token (str)
      The token to request the next page of user_rankings.
    total_user_rankings (int)
      The total number of user rankings matching any filters.
  """

  def __init__(self):
    self._current_user_ranking = None
    self._user_rankings = []
    self._next_page_token = ""
    self._total_user_rankings = 0
    self._freeze()

  @property
  def current_user_ranking(self) -> Optional['LeaderboardsListItem']:
    r"""
    The current user ranking for the requested user achievement type. May be
    null if the current user isn't eligible for a ranking, or for the current
    set of filters in the request.
    """
    return self._current_user_ranking or None

  @current_user_ranking.setter
  def current_user_ranking(self, current_user_ranking: Optional[Optional['LeaderboardsListItem']]):
    if current_user_ranking is None:
      del self.current_user_ranking
      return
    if not isinstance(current_user_ranking, LeaderboardsListItem):
      raise TypeError('current_user_ranking must be of type LeaderboardsListItem')
    self._current_user_ranking = current_user_ranking

  @property
  def user_rankings(self) -> Optional[List[Optional['LeaderboardsListItem']]]:
    """The user rankings for the requested user achievement type."""
    return self._user_rankings

  @user_rankings.setter
  def user_rankings(self, user_rankings: Optional[List[Optional['LeaderboardsListItem']]]):
    if user_rankings is None:
      del self.user_rankings
      return
    if not isinstance(user_rankings, list):
      raise TypeError('user_rankings must be of type list')
    if not all([isinstance(t, LeaderboardsListItem) for t in user_rankings]):
      raise TypeError('user_rankings must contain only items of type LeaderboardsListItem')
    self._user_rankings = user_rankings

  @property
  def next_page_token(self) -> str:
    """The token to request the next page of user_rankings."""
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def total_user_rankings(self) -> int:
    """The total number of user rankings matching any filters."""
    return self._total_user_rankings

  @total_user_rankings.setter
  def total_user_rankings(self, total_user_rankings: int):
    if total_user_rankings is None:
      del self.total_user_rankings
      return
    if not isinstance(total_user_rankings, int):
      raise TypeError('total_user_rankings must be of type int')
    self._total_user_rankings = total_user_rankings


class LeaderboardCounts(KaggleObject):
  r"""
  Attributes:
    tier (UserAchievementTier)
    count (int)
  """

  def __init__(self):
    self._tier = UserAchievementTier.NOVICE
    self._count = 0
    self._freeze()

  @property
  def tier(self) -> 'UserAchievementTier':
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
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class LeaderboardsListItem(KaggleObject):
  r"""
  Attributes:
    current_ranking (int)
    display_name (str)
    thumbnail_url (str)
    user_id (int)
    user_url (str)
    tier (UserAchievementTier)
    points (float)
    join_time (datetime)
    total_gold_medals (int)
    total_silver_medals (int)
    total_bronze_medals (int)
    tier_for_achievement_type (UserAchievementTier)
  """

  def __init__(self):
    self._current_ranking = None
    self._display_name = None
    self._thumbnail_url = None
    self._user_id = 0
    self._user_url = None
    self._tier = UserAchievementTier.NOVICE
    self._points = 0.0
    self._join_time = None
    self._total_gold_medals = 0
    self._total_silver_medals = 0
    self._total_bronze_medals = 0
    self._tier_for_achievement_type = UserAchievementTier.NOVICE
    self._freeze()

  @property
  def current_ranking(self) -> int:
    return self._current_ranking or 0

  @current_ranking.setter
  def current_ranking(self, current_ranking: Optional[int]):
    if current_ranking is None:
      del self.current_ranking
      return
    if not isinstance(current_ranking, int):
      raise TypeError('current_ranking must be of type int')
    self._current_ranking = current_ranking

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

  @property
  def thumbnail_url(self) -> str:
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

  @property
  def user_url(self) -> str:
    return self._user_url or ""

  @user_url.setter
  def user_url(self, user_url: Optional[str]):
    if user_url is None:
      del self.user_url
      return
    if not isinstance(user_url, str):
      raise TypeError('user_url must be of type str')
    self._user_url = user_url

  @property
  def tier(self) -> 'UserAchievementTier':
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
  def points(self) -> float:
    return self._points

  @points.setter
  def points(self, points: float):
    if points is None:
      del self.points
      return
    if not isinstance(points, float):
      raise TypeError('points must be of type float')
    self._points = points

  @property
  def join_time(self) -> datetime:
    return self._join_time

  @join_time.setter
  def join_time(self, join_time: datetime):
    if join_time is None:
      del self.join_time
      return
    if not isinstance(join_time, datetime):
      raise TypeError('join_time must be of type datetime')
    self._join_time = join_time

  @property
  def total_gold_medals(self) -> int:
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
    return self._total_bronze_medals

  @total_bronze_medals.setter
  def total_bronze_medals(self, total_bronze_medals: int):
    if total_bronze_medals is None:
      del self.total_bronze_medals
      return
    if not isinstance(total_bronze_medals, int):
      raise TypeError('total_bronze_medals must be of type int')
    self._total_bronze_medals = total_bronze_medals

  @property
  def tier_for_achievement_type(self) -> 'UserAchievementTier':
    return self._tier_for_achievement_type

  @tier_for_achievement_type.setter
  def tier_for_achievement_type(self, tier_for_achievement_type: 'UserAchievementTier'):
    if tier_for_achievement_type is None:
      del self.tier_for_achievement_type
      return
    if not isinstance(tier_for_achievement_type, UserAchievementTier):
      raise TypeError('tier_for_achievement_type must be of type UserAchievementTier')
    self._tier_for_achievement_type = tier_for_achievement_type


class MedalCount(KaggleObject):
  r"""
  Attributes:
    type (UserAchievementType)
    total_gold_medals (int)
    total_silver_medals (int)
    total_bronze_medals (int)
  """

  def __init__(self):
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._total_gold_medals = 0
    self._total_silver_medals = 0
    self._total_bronze_medals = 0
    self._freeze()

  @property
  def type(self) -> 'UserAchievementType':
    return self._type

  @type.setter
  def type(self, type: 'UserAchievementType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, UserAchievementType):
      raise TypeError('type must be of type UserAchievementType')
    self._type = type

  @property
  def total_gold_medals(self) -> int:
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
    return self._total_bronze_medals

  @total_bronze_medals.setter
  def total_bronze_medals(self, total_bronze_medals: int):
    if total_bronze_medals is None:
      del self.total_bronze_medals
      return
    if not isinstance(total_bronze_medals, int):
      raise TypeError('total_bronze_medals must be of type int')
    self._total_bronze_medals = total_bronze_medals


class RankingPosition(KaggleObject):
  r"""
  Rankings for a specific achievement time checkpoint.
  Structure of this proto is optimized for it's usage in the FE / rendering.

  Attributes:
    achievement_time (datetime)
    competitions_ranking (int)
      User ranking for competitions.
    datasets_ranking (int)
      User ranking for datasets.
    kernels_ranking (int)
      User ranking for notebooks.
  """

  def __init__(self):
    self._achievement_time = None
    self._competitions_ranking = None
    self._datasets_ranking = None
    self._kernels_ranking = None
    self._freeze()

  @property
  def achievement_time(self) -> datetime:
    return self._achievement_time

  @achievement_time.setter
  def achievement_time(self, achievement_time: datetime):
    if achievement_time is None:
      del self.achievement_time
      return
    if not isinstance(achievement_time, datetime):
      raise TypeError('achievement_time must be of type datetime')
    self._achievement_time = achievement_time

  @property
  def competitions_ranking(self) -> int:
    """User ranking for competitions."""
    return self._competitions_ranking or 0

  @competitions_ranking.setter
  def competitions_ranking(self, competitions_ranking: Optional[int]):
    if competitions_ranking is None:
      del self.competitions_ranking
      return
    if not isinstance(competitions_ranking, int):
      raise TypeError('competitions_ranking must be of type int')
    self._competitions_ranking = competitions_ranking

  @property
  def datasets_ranking(self) -> int:
    """User ranking for datasets."""
    return self._datasets_ranking or 0

  @datasets_ranking.setter
  def datasets_ranking(self, datasets_ranking: Optional[int]):
    if datasets_ranking is None:
      del self.datasets_ranking
      return
    if not isinstance(datasets_ranking, int):
      raise TypeError('datasets_ranking must be of type int')
    self._datasets_ranking = datasets_ranking

  @property
  def kernels_ranking(self) -> int:
    """User ranking for notebooks."""
    return self._kernels_ranking or 0

  @kernels_ranking.setter
  def kernels_ranking(self, kernels_ranking: Optional[int]):
    if kernels_ranking is None:
      del self.kernels_ranking
      return
    if not isinstance(kernels_ranking, int):
      raise TypeError('kernels_ranking must be of type int')
    self._kernels_ranking = kernels_ranking


class TierAchievement(KaggleObject):
  r"""
  Attributes:
    tier (UserAchievementTier)
    type (UserAchievementType)
    current_level (int)
      Provided if the tier is GM, with the user's current (not historic) GM+
      level for this progression type. Competitions 3x GM would be 3, datasets GM
      would be 1, and non-GM tiers would have this field unset.
    achievement_time (datetime)
  """

  def __init__(self):
    self._tier = UserAchievementTier.NOVICE
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._current_level = None
    self._achievement_time = None
    self._freeze()

  @property
  def tier(self) -> 'UserAchievementTier':
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
  def type(self) -> 'UserAchievementType':
    return self._type

  @type.setter
  def type(self, type: 'UserAchievementType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, UserAchievementType):
      raise TypeError('type must be of type UserAchievementType')
    self._type = type

  @property
  def current_level(self) -> int:
    r"""
    Provided if the tier is GM, with the user's current (not historic) GM+
    level for this progression type. Competitions 3x GM would be 3, datasets GM
    would be 1, and non-GM tiers would have this field unset.
    """
    return self._current_level or 0

  @current_level.setter
  def current_level(self, current_level: Optional[int]):
    if current_level is None:
      del self.current_level
      return
    if not isinstance(current_level, int):
      raise TypeError('current_level must be of type int')
    self._current_level = current_level

  @property
  def achievement_time(self) -> datetime:
    return self._achievement_time

  @achievement_time.setter
  def achievement_time(self, achievement_time: datetime):
    if achievement_time is None:
      del self.achievement_time
      return
    if not isinstance(achievement_time, datetime):
      raise TypeError('achievement_time must be of type datetime')
    self._achievement_time = achievement_time


class UserAchievementLeaderboardCounts(KaggleObject):
  r"""
  Attributes:
    type (UserAchievementType)
      The achievement type the user ranking counts are for.
    counts (LeaderboardCounts)
      The user counts for each tier of the requested user achievement type.
  """

  def __init__(self):
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._counts = []
    self._freeze()

  @property
  def type(self) -> 'UserAchievementType':
    """The achievement type the user ranking counts are for."""
    return self._type

  @type.setter
  def type(self, type: 'UserAchievementType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, UserAchievementType):
      raise TypeError('type must be of type UserAchievementType')
    self._type = type

  @property
  def counts(self) -> Optional[List[Optional['LeaderboardCounts']]]:
    """The user counts for each tier of the requested user achievement type."""
    return self._counts

  @counts.setter
  def counts(self, counts: Optional[List[Optional['LeaderboardCounts']]]):
    if counts is None:
      del self.counts
      return
    if not isinstance(counts, list):
      raise TypeError('counts must be of type list')
    if not all([isinstance(t, LeaderboardCounts) for t in counts]):
      raise TypeError('counts must contain only items of type LeaderboardCounts')
    self._counts = counts


class UserRankingHistory(KaggleObject):
  r"""
  Attributes:
    ranking_positions (RankingPosition)
      History of the user's ranks sorted by time, ascending. There should be at
      most one ranking position per ranking checkpoint date.
    tier_achievements (TierAchievement)
      History of all tiers achieved, sorted by time, ascending.
    total_grandmaster_level (int)
      Sum of GM levels for the user. Ex: If a user is a grandmaster in all
      three progression types, and 'over-levels' in Competitions by 2 levels (3x
      Competitions GM), they are a 5x GM, and this field will be 5.
  """

  def __init__(self):
    self._ranking_positions = []
    self._tier_achievements = []
    self._total_grandmaster_level = 0
    self._freeze()

  @property
  def ranking_positions(self) -> Optional[List[Optional['RankingPosition']]]:
    r"""
    History of the user's ranks sorted by time, ascending. There should be at
    most one ranking position per ranking checkpoint date.
    """
    return self._ranking_positions

  @ranking_positions.setter
  def ranking_positions(self, ranking_positions: Optional[List[Optional['RankingPosition']]]):
    if ranking_positions is None:
      del self.ranking_positions
      return
    if not isinstance(ranking_positions, list):
      raise TypeError('ranking_positions must be of type list')
    if not all([isinstance(t, RankingPosition) for t in ranking_positions]):
      raise TypeError('ranking_positions must contain only items of type RankingPosition')
    self._ranking_positions = ranking_positions

  @property
  def tier_achievements(self) -> Optional[List[Optional['TierAchievement']]]:
    """History of all tiers achieved, sorted by time, ascending."""
    return self._tier_achievements

  @tier_achievements.setter
  def tier_achievements(self, tier_achievements: Optional[List[Optional['TierAchievement']]]):
    if tier_achievements is None:
      del self.tier_achievements
      return
    if not isinstance(tier_achievements, list):
      raise TypeError('tier_achievements must be of type list')
    if not all([isinstance(t, TierAchievement) for t in tier_achievements]):
      raise TypeError('tier_achievements must contain only items of type TierAchievement')
    self._tier_achievements = tier_achievements

  @property
  def total_grandmaster_level(self) -> int:
    r"""
    Sum of GM levels for the user. Ex: If a user is a grandmaster in all
    three progression types, and 'over-levels' in Competitions by 2 levels (3x
    Competitions GM), they are a 5x GM, and this field will be 5.
    """
    return self._total_grandmaster_level

  @total_grandmaster_level.setter
  def total_grandmaster_level(self, total_grandmaster_level: int):
    if total_grandmaster_level is None:
      del self.total_grandmaster_level
      return
    if not isinstance(total_grandmaster_level, int):
      raise TypeError('total_grandmaster_level must be of type int')
    self._total_grandmaster_level = total_grandmaster_level


class UserRankingsFilters(KaggleObject):
  r"""
  Attributes:
    query (str)
      A string query to apply as a filter on usernames.
    occupation_organization_names (str)
      When provided, only users that have one of the indicated occupation
      organization name on their user profile will be eligible, i.e.
      http://screen/3N68JKC4hocxWmn. Note: This is *not* the same thing as a
      Kaggle Organization, such as kaggle.com/organizations/google.
    user_locations (str)
      When provided, only users that have one of the specified locations on
      their user profile, and are location sharing opted-in, will be returned.
      Expects the format: 'city, region, country'.
  """

  def __init__(self):
    self._query = None
    self._occupation_organization_names = []
    self._user_locations = []
    self._freeze()

  @property
  def query(self) -> str:
    """A string query to apply as a filter on usernames."""
    return self._query or ""

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def occupation_organization_names(self) -> Optional[List[str]]:
    r"""
    When provided, only users that have one of the indicated occupation
    organization name on their user profile will be eligible, i.e.
    http://screen/3N68JKC4hocxWmn. Note: This is *not* the same thing as a
    Kaggle Organization, such as kaggle.com/organizations/google.
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
  def user_locations(self) -> Optional[List[str]]:
    r"""
    When provided, only users that have one of the specified locations on
    their user profile, and are location sharing opted-in, will be returned.
    Expects the format: 'city, region, country'.
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


GetUserMedalCountsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserMedalCountsResponse._fields = [
  FieldMetadata("medalCounts", "medal_counts", "_medal_counts", MedalCount, [], ListSerializer(KaggleObjectSerializer())),
]

GetUserRankingHistoryRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("adminOnlyHistoryType", "admin_only_history_type", "_admin_only_history_type", UserRankingHistoryType, None, EnumSerializer(), optional=True),
]

GetUserRankingsCountsRequest._fields = []

GetUserRankingsCountsResponse._fields = [
  FieldMetadata("counts", "counts", "_counts", UserAchievementLeaderboardCounts, [], ListSerializer(KaggleObjectSerializer())),
]

GetUserRankingsV2Request._fields = [
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("filters", "filters", "_filters", UserRankingsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("skipForCaching", "skip_for_caching", "_skip_for_caching", int, 0, PredefinedSerializer()),
]

GetUserRankingsV2Response._fields = [
  FieldMetadata("currentUserRanking", "current_user_ranking", "_current_user_ranking", LeaderboardsListItem, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userRankings", "user_rankings", "_user_rankings", LeaderboardsListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalUserRankings", "total_user_rankings", "_total_user_rankings", int, 0, PredefinedSerializer()),
]

LeaderboardCounts._fields = [
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

LeaderboardsListItem._fields = [
  FieldMetadata("currentRanking", "current_ranking", "_current_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userUrl", "user_url", "_user_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("points", "points", "_points", float, 0.0, PredefinedSerializer()),
  FieldMetadata("joinTime", "join_time", "_join_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("totalGoldMedals", "total_gold_medals", "_total_gold_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSilverMedals", "total_silver_medals", "_total_silver_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBronzeMedals", "total_bronze_medals", "_total_bronze_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("tierForAchievementType", "tier_for_achievement_type", "_tier_for_achievement_type", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
]

MedalCount._fields = [
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("totalGoldMedals", "total_gold_medals", "_total_gold_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSilverMedals", "total_silver_medals", "_total_silver_medals", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBronzeMedals", "total_bronze_medals", "_total_bronze_medals", int, 0, PredefinedSerializer()),
]

RankingPosition._fields = [
  FieldMetadata("achievementTime", "achievement_time", "_achievement_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("competitionsRanking", "competitions_ranking", "_competitions_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetsRanking", "datasets_ranking", "_datasets_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelsRanking", "kernels_ranking", "_kernels_ranking", int, None, PredefinedSerializer(), optional=True),
]

TierAchievement._fields = [
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("currentLevel", "current_level", "_current_level", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("achievementTime", "achievement_time", "_achievement_time", datetime, None, DateTimeSerializer()),
]

UserAchievementLeaderboardCounts._fields = [
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("counts", "counts", "_counts", LeaderboardCounts, [], ListSerializer(KaggleObjectSerializer())),
]

UserRankingHistory._fields = [
  FieldMetadata("rankingPositions", "ranking_positions", "_ranking_positions", RankingPosition, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tierAchievements", "tier_achievements", "_tier_achievements", TierAchievement, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalGrandmasterLevel", "total_grandmaster_level", "_total_grandmaster_level", int, 0, PredefinedSerializer()),
]

UserRankingsFilters._fields = [
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("occupationOrganizationNames", "occupation_organization_names", "_occupation_organization_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userLocations", "user_locations", "_user_locations", str, [], ListSerializer(PredefinedSerializer())),
]

