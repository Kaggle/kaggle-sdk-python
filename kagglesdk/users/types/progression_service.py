import enum
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import List, Optional

class Medal(enum.Enum):
  MEDAL_UNSPECIFIED = 0
  GOLD = 1
  SILVER = 2
  BRONZE = 3

class UserAchievementType(enum.Enum):
  USER_ACHIEVEMENT_TYPE_UNSPECIFIED = 0
  USER_ACHIEVEMENT_TYPE_COMPETITIONS = 1
  USER_ACHIEVEMENT_TYPE_NOTEBOOKS = 2
  USER_ACHIEVEMENT_TYPE_DISCUSSION = 3
  USER_ACHIEVEMENT_TYPE_DATASETS = 4

class UpdateRankingsAndPointsVariant(enum.Enum):
  UPDATE_RANKINGS_AND_POINTS_VARIANT_UNSPECIFIED = 0
  UPDATE_RANKINGS_AND_POINTS_V2016 = 1
  r"""
  Runs update leaderboard and points sproc with the ruleset established in
  2016 on older vote tables, using vote date based point decay.
  """
  UPDATE_RANKINGS_AND_POINTS_V2025_EXPERIMENT = 2
  r"""
  Runs update leaderboard and points sproc with the ruleset established in
  2025 on unified vote tables, using content created date based point decay.
  This is the experimental version that writes to
  UserAchievementsExperimental.
  """
  UPDATE_RANKINGS_AND_POINTS_V2025_PROD = 3
  r"""
  Runs update leaderboard and points sproc with the ruleset established in
  2025 on unified vote tables, using content created date based point decay.
  This is the prod version that writes to UserAchievements.
  """

class AchievementTypeRanking(KaggleObject):
  r"""
  Attributes:
    type (UserAchievementType)
      The progression type for the ranking
    ranking (int)
      The ranking for this user for the corresponding progression type
    rank_out_of (int)
      The total users ranked in this achievement
    highest_rank (int)
      The highest rank this user has held
    current_points (int)
      The current number of points this user has
    tier (UserAchievementTier)
      The current tier of the user for the achievement type.
    highest_points (int)
      The highest number of points this user has had for this progression type.
  """

  def __init__(self):
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._ranking = 0
    self._rank_out_of = 0
    self._highest_rank = 0
    self._current_points = 0
    self._tier = UserAchievementTier.NOVICE
    self._highest_points = 0
    self._freeze()

  @property
  def type(self) -> 'UserAchievementType':
    """The progression type for the ranking"""
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
  def tier(self) -> 'UserAchievementTier':
    """The current tier of the user for the achievement type."""
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
  def ranking(self) -> int:
    """The ranking for this user for the corresponding progression type"""
    return self._ranking

  @ranking.setter
  def ranking(self, ranking: int):
    if ranking is None:
      del self.ranking
      return
    if not isinstance(ranking, int):
      raise TypeError('ranking must be of type int')
    self._ranking = ranking

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
  def highest_rank(self) -> int:
    """The highest rank this user has held"""
    return self._highest_rank

  @highest_rank.setter
  def highest_rank(self, highest_rank: int):
    if highest_rank is None:
      del self.highest_rank
      return
    if not isinstance(highest_rank, int):
      raise TypeError('highest_rank must be of type int')
    self._highest_rank = highest_rank

  @property
  def current_points(self) -> int:
    """The current number of points this user has"""
    return self._current_points

  @current_points.setter
  def current_points(self, current_points: int):
    if current_points is None:
      del self.current_points
      return
    if not isinstance(current_points, int):
      raise TypeError('current_points must be of type int')
    self._current_points = current_points

  @property
  def highest_points(self) -> int:
    """The highest number of points this user has had for this progression type."""
    return self._highest_points

  @highest_points.setter
  def highest_points(self, highest_points: int):
    if highest_points is None:
      del self.highest_points
      return
    if not isinstance(highest_points, int):
      raise TypeError('highest_points must be of type int')
    self._highest_points = highest_points


class BatchSetUsersToRecalcRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      The list of user ids to set progression tier to recalc.
  """

  def __init__(self):
    self._user_ids = []
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The list of user ids to set progression tier to recalc."""
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


class BatchSetUsersToRecalcResponse(KaggleObject):
  r"""
  Attributes:
    updated_count (int)
      Number of users affected. This can be lower than requested, if user ids are
      not valid.
  """

  def __init__(self):
    self._updated_count = 0
    self._freeze()

  @property
  def updated_count(self) -> int:
    r"""
    Number of users affected. This can be lower than requested, if user ids are
    not valid.
    """
    return self._updated_count

  @updated_count.setter
  def updated_count(self, updated_count: int):
    if updated_count is None:
      del self.updated_count
      return
    if not isinstance(updated_count, int):
      raise TypeError('updated_count must be of type int')
    self._updated_count = updated_count


class BatchUpdateUserAchievementsRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      The list of user ids to update user achievements for.
  """

  def __init__(self):
    self._user_ids = []
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The list of user ids to update user achievements for."""
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


class BatchUpdateUserAchievementsResponse(KaggleObject):
  r"""
  Attributes:
    updated_count (int)
      Number of users affected. This can be lower than requested, if user ids are
      not valid.
    tiers_changed_count (int)
      The count of overall tiers that changed for the set of users updated.
  """

  def __init__(self):
    self._updated_count = 0
    self._tiers_changed_count = 0
    self._freeze()

  @property
  def updated_count(self) -> int:
    r"""
    Number of users affected. This can be lower than requested, if user ids are
    not valid.
    """
    return self._updated_count

  @updated_count.setter
  def updated_count(self, updated_count: int):
    if updated_count is None:
      del self.updated_count
      return
    if not isinstance(updated_count, int):
      raise TypeError('updated_count must be of type int')
    self._updated_count = updated_count

  @property
  def tiers_changed_count(self) -> int:
    """The count of overall tiers that changed for the set of users updated."""
    return self._tiers_changed_count

  @tiers_changed_count.setter
  def tiers_changed_count(self, tiers_changed_count: int):
    if tiers_changed_count is None:
      del self.tiers_changed_count
      return
    if not isinstance(tiers_changed_count, int):
      raise TypeError('tiers_changed_count must be of type int')
    self._tiers_changed_count = tiers_changed_count


class GetCurrentUserProgressionRequest(KaggleObject):
  r"""
  """

  pass

class GetCurrentUserProgressionResponse(KaggleObject):
  r"""
  Attributes:
    tier_requirement_groups (TierRequirementGroup)
      Sets of requirements for each progression type for the user. A group
      consists of all requirements for a given type (Competitions, Kernels, etc.)
      and tier (Expert, Master, etc.). A group can have multiple requirements,
      where a single requirement may be '3 Gold Competition Medals'.
    achievement_type_rankings (AchievementTypeRanking)
      The user's ranking and current tier for each progression type
    is_opted_out (bool)
      Whether or not the user is opted out from progression.
  """

  def __init__(self):
    self._tier_requirement_groups = []
    self._achievement_type_rankings = []
    self._is_opted_out = False
    self._freeze()

  @property
  def tier_requirement_groups(self) -> Optional[List[Optional['TierRequirementGroup']]]:
    r"""
    Sets of requirements for each progression type for the user. A group
    consists of all requirements for a given type (Competitions, Kernels, etc.)
    and tier (Expert, Master, etc.). A group can have multiple requirements,
    where a single requirement may be '3 Gold Competition Medals'.
    """
    return self._tier_requirement_groups

  @tier_requirement_groups.setter
  def tier_requirement_groups(self, tier_requirement_groups: Optional[List[Optional['TierRequirementGroup']]]):
    if tier_requirement_groups is None:
      del self.tier_requirement_groups
      return
    if not isinstance(tier_requirement_groups, list):
      raise TypeError('tier_requirement_groups must be of type list')
    if not all([isinstance(t, TierRequirementGroup) for t in tier_requirement_groups]):
      raise TypeError('tier_requirement_groups must contain only items of type TierRequirementGroup')
    self._tier_requirement_groups = tier_requirement_groups

  @property
  def achievement_type_rankings(self) -> Optional[List[Optional['AchievementTypeRanking']]]:
    """The user's ranking and current tier for each progression type"""
    return self._achievement_type_rankings

  @achievement_type_rankings.setter
  def achievement_type_rankings(self, achievement_type_rankings: Optional[List[Optional['AchievementTypeRanking']]]):
    if achievement_type_rankings is None:
      del self.achievement_type_rankings
      return
    if not isinstance(achievement_type_rankings, list):
      raise TypeError('achievement_type_rankings must be of type list')
    if not all([isinstance(t, AchievementTypeRanking) for t in achievement_type_rankings]):
      raise TypeError('achievement_type_rankings must contain only items of type AchievementTypeRanking')
    self._achievement_type_rankings = achievement_type_rankings

  @property
  def is_opted_out(self) -> bool:
    """Whether or not the user is opted out from progression."""
    return self._is_opted_out

  @is_opted_out.setter
  def is_opted_out(self, is_opted_out: bool):
    if is_opted_out is None:
      del self.is_opted_out
      return
    if not isinstance(is_opted_out, bool):
      raise TypeError('is_opted_out must be of type bool')
    self._is_opted_out = is_opted_out


class MedalCeremonySettings(KaggleObject):
  r"""
  Attributes:
    update_rankings_and_points_variant (UpdateRankingsAndPointsVariant)
      Specifies the rankings and points script (i.e. leaderboard updates) to use.
    medals_from_run (str)
      If provided, uses the given run identifier as the source of truth for
      current medals, rather than live tables. Can use a prefix for this, will
      match the latest unique run identifier that starts with this.
      This can be used to run the medal ceremony experiment 'multiple times'.
      Only valid with the use_unified_vote_table is also being used.
  """

  def __init__(self):
    self._update_rankings_and_points_variant = UpdateRankingsAndPointsVariant.UPDATE_RANKINGS_AND_POINTS_VARIANT_UNSPECIFIED
    self._medals_from_run = None
    self._freeze()

  @property
  def update_rankings_and_points_variant(self) -> 'UpdateRankingsAndPointsVariant':
    """Specifies the rankings and points script (i.e. leaderboard updates) to use."""
    return self._update_rankings_and_points_variant

  @update_rankings_and_points_variant.setter
  def update_rankings_and_points_variant(self, update_rankings_and_points_variant: 'UpdateRankingsAndPointsVariant'):
    if update_rankings_and_points_variant is None:
      del self.update_rankings_and_points_variant
      return
    if not isinstance(update_rankings_and_points_variant, UpdateRankingsAndPointsVariant):
      raise TypeError('update_rankings_and_points_variant must be of type UpdateRankingsAndPointsVariant')
    self._update_rankings_and_points_variant = update_rankings_and_points_variant

  @property
  def medals_from_run(self) -> str:
    r"""
    If provided, uses the given run identifier as the source of truth for
    current medals, rather than live tables. Can use a prefix for this, will
    match the latest unique run identifier that starts with this.
    This can be used to run the medal ceremony experiment 'multiple times'.
    Only valid with the use_unified_vote_table is also being used.
    """
    return self._medals_from_run or ""

  @medals_from_run.setter
  def medals_from_run(self, medals_from_run: Optional[str]):
    if medals_from_run is None:
      del self.medals_from_run
      return
    if not isinstance(medals_from_run, str):
      raise TypeError('medals_from_run must be of type str')
    self._medals_from_run = medals_from_run


class PerformMedalCeremonyExperimentRequest(KaggleObject):
  r"""
  Attributes:
    run_identifier (str)
      A key to use to identify this run
    settings (MedalCeremonySettings)
  """

  def __init__(self):
    self._run_identifier = ""
    self._settings = None
    self._freeze()

  @property
  def run_identifier(self) -> str:
    """A key to use to identify this run"""
    return self._run_identifier

  @run_identifier.setter
  def run_identifier(self, run_identifier: str):
    if run_identifier is None:
      del self.run_identifier
      return
    if not isinstance(run_identifier, str):
      raise TypeError('run_identifier must be of type str')
    self._run_identifier = run_identifier

  @property
  def settings(self) -> Optional['MedalCeremonySettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['MedalCeremonySettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, MedalCeremonySettings):
      raise TypeError('settings must be of type MedalCeremonySettings')
    self._settings = settings


class PerformMedalCeremonyExperimentResponse(KaggleObject):
  r"""
  Attributes:
    count_medal_changes (int)
      How many medal tier entries were added (how many medals would change)
    count_tier_changes (int)
      How many user tier entries were added (how many user tiers would change)
  """

  def __init__(self):
    self._count_medal_changes = 0
    self._count_tier_changes = 0
    self._freeze()

  @property
  def count_medal_changes(self) -> int:
    """How many medal tier entries were added (how many medals would change)"""
    return self._count_medal_changes

  @count_medal_changes.setter
  def count_medal_changes(self, count_medal_changes: int):
    if count_medal_changes is None:
      del self.count_medal_changes
      return
    if not isinstance(count_medal_changes, int):
      raise TypeError('count_medal_changes must be of type int')
    self._count_medal_changes = count_medal_changes

  @property
  def count_tier_changes(self) -> int:
    """How many user tier entries were added (how many user tiers would change)"""
    return self._count_tier_changes

  @count_tier_changes.setter
  def count_tier_changes(self, count_tier_changes: int):
    if count_tier_changes is None:
      del self.count_tier_changes
      return
    if not isinstance(count_tier_changes, int):
      raise TypeError('count_tier_changes must be of type int')
    self._count_tier_changes = count_tier_changes


class TierRequirement(KaggleObject):
  r"""
  Attributes:
    label (str)
      The copy shown to the user for the requirement
    url (str)
      The call-to-action URL for the requirement
    number_required (int)
      The total number required to satisfy the requirement
    number_met (int)
      The current number of the requirement completed by the user
    level (int)
      If applicable, the tier level represented by this requirement (2 for 2x,
      etc). As of 2025 Q2 this is only supported for the Competitions GM tier.
  """

  def __init__(self):
    self._label = ""
    self._url = ""
    self._number_required = 0
    self._number_met = 0
    self._level = None
    self._freeze()

  @property
  def label(self) -> str:
    """The copy shown to the user for the requirement"""
    return self._label

  @label.setter
  def label(self, label: str):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label

  @property
  def url(self) -> str:
    """The call-to-action URL for the requirement"""
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
  def number_required(self) -> int:
    """The total number required to satisfy the requirement"""
    return self._number_required

  @number_required.setter
  def number_required(self, number_required: int):
    if number_required is None:
      del self.number_required
      return
    if not isinstance(number_required, int):
      raise TypeError('number_required must be of type int')
    self._number_required = number_required

  @property
  def number_met(self) -> int:
    """The current number of the requirement completed by the user"""
    return self._number_met

  @number_met.setter
  def number_met(self, number_met: int):
    if number_met is None:
      del self.number_met
      return
    if not isinstance(number_met, int):
      raise TypeError('number_met must be of type int')
    self._number_met = number_met

  @property
  def level(self) -> int:
    r"""
    If applicable, the tier level represented by this requirement (2 for 2x,
    etc). As of 2025 Q2 this is only supported for the Competitions GM tier.
    """
    return self._level or 0

  @level.setter
  def level(self, level: Optional[int]):
    if level is None:
      del self.level
      return
    if not isinstance(level, int):
      raise TypeError('level must be of type int')
    self._level = level


class TierRequirementGroup(KaggleObject):
  r"""
  Attributes:
    tier (UserAchievementTier)
      The progression tier for the set of requirements
    type (UserAchievementType)
      The progression type for the set of requirements
    is_complete (bool)
      Whether the full set of requirements is complete
    is_in_progress (bool)
      Whether this progression type/tier is the current in-progress tier
    requirements (TierRequirement)
      The set of requirements for the type/tier
    level (int)
      If applicable, the obtained level for this tier (2 for 2x, etc). As of
      2025 Q2 this is only supported for the Competitions GM tier. This is an
      absolute value, where 1 is 1x, i.e. user has only met basic GM
      requirements.
    next_level_requirements (TierRequirement)
      The set of requirements for the next level of the type/tier. As of 2025 Q2
      this is only supported for the Competitions GM tier.
  """

  def __init__(self):
    self._tier = UserAchievementTier.NOVICE
    self._type = UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED
    self._is_complete = False
    self._is_in_progress = False
    self._requirements = []
    self._level = None
    self._next_level_requirements = []
    self._freeze()

  @property
  def tier(self) -> 'UserAchievementTier':
    """The progression tier for the set of requirements"""
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
    """The progression type for the set of requirements"""
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
  def is_complete(self) -> bool:
    """Whether the full set of requirements is complete"""
    return self._is_complete

  @is_complete.setter
  def is_complete(self, is_complete: bool):
    if is_complete is None:
      del self.is_complete
      return
    if not isinstance(is_complete, bool):
      raise TypeError('is_complete must be of type bool')
    self._is_complete = is_complete

  @property
  def is_in_progress(self) -> bool:
    """Whether this progression type/tier is the current in-progress tier"""
    return self._is_in_progress

  @is_in_progress.setter
  def is_in_progress(self, is_in_progress: bool):
    if is_in_progress is None:
      del self.is_in_progress
      return
    if not isinstance(is_in_progress, bool):
      raise TypeError('is_in_progress must be of type bool')
    self._is_in_progress = is_in_progress

  @property
  def requirements(self) -> Optional[List[Optional['TierRequirement']]]:
    """The set of requirements for the type/tier"""
    return self._requirements

  @requirements.setter
  def requirements(self, requirements: Optional[List[Optional['TierRequirement']]]):
    if requirements is None:
      del self.requirements
      return
    if not isinstance(requirements, list):
      raise TypeError('requirements must be of type list')
    if not all([isinstance(t, TierRequirement) for t in requirements]):
      raise TypeError('requirements must contain only items of type TierRequirement')
    self._requirements = requirements

  @property
  def level(self) -> int:
    r"""
    If applicable, the obtained level for this tier (2 for 2x, etc). As of
    2025 Q2 this is only supported for the Competitions GM tier. This is an
    absolute value, where 1 is 1x, i.e. user has only met basic GM
    requirements.
    """
    return self._level or 0

  @level.setter
  def level(self, level: Optional[int]):
    if level is None:
      del self.level
      return
    if not isinstance(level, int):
      raise TypeError('level must be of type int')
    self._level = level

  @property
  def next_level_requirements(self) -> Optional[List[Optional['TierRequirement']]]:
    r"""
    The set of requirements for the next level of the type/tier. As of 2025 Q2
    this is only supported for the Competitions GM tier.
    """
    return self._next_level_requirements

  @next_level_requirements.setter
  def next_level_requirements(self, next_level_requirements: Optional[List[Optional['TierRequirement']]]):
    if next_level_requirements is None:
      del self.next_level_requirements
      return
    if not isinstance(next_level_requirements, list):
      raise TypeError('next_level_requirements must be of type list')
    if not all([isinstance(t, TierRequirement) for t in next_level_requirements]):
      raise TypeError('next_level_requirements must contain only items of type TierRequirement')
    self._next_level_requirements = next_level_requirements


class UpdateUserAchievementsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The UserId of the user whose progression data should be synced
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The UserId of the user whose progression data should be synced"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class UpdateUserAchievementsResponse(KaggleObject):
  r"""
  Attributes:
    tier_changed (bool)
      Whether the user's overall tier changed as a result of the update
    new_tier (UserAchievementTier)
      The new tier for the user (or current tier, if unchanged)
  """

  def __init__(self):
    self._tier_changed = False
    self._new_tier = UserAchievementTier.NOVICE
    self._freeze()

  @property
  def tier_changed(self) -> bool:
    """Whether the user's overall tier changed as a result of the update"""
    return self._tier_changed

  @tier_changed.setter
  def tier_changed(self, tier_changed: bool):
    if tier_changed is None:
      del self.tier_changed
      return
    if not isinstance(tier_changed, bool):
      raise TypeError('tier_changed must be of type bool')
    self._tier_changed = tier_changed

  @property
  def new_tier(self) -> 'UserAchievementTier':
    """The new tier for the user (or current tier, if unchanged)"""
    return self._new_tier

  @new_tier.setter
  def new_tier(self, new_tier: 'UserAchievementTier'):
    if new_tier is None:
      del self.new_tier
      return
    if not isinstance(new_tier, UserAchievementTier):
      raise TypeError('new_tier must be of type UserAchievementTier')
    self._new_tier = new_tier


AchievementTypeRanking._fields = [
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ranking", "ranking", "_ranking", int, 0, PredefinedSerializer()),
  FieldMetadata("rankOutOf", "rank_out_of", "_rank_out_of", int, 0, PredefinedSerializer()),
  FieldMetadata("highestRank", "highest_rank", "_highest_rank", int, 0, PredefinedSerializer()),
  FieldMetadata("currentPoints", "current_points", "_current_points", int, 0, PredefinedSerializer()),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("highestPoints", "highest_points", "_highest_points", int, 0, PredefinedSerializer()),
]

BatchSetUsersToRecalcRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BatchSetUsersToRecalcResponse._fields = [
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
]

BatchUpdateUserAchievementsRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BatchUpdateUserAchievementsResponse._fields = [
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
  FieldMetadata("tiersChangedCount", "tiers_changed_count", "_tiers_changed_count", int, 0, PredefinedSerializer()),
]

GetCurrentUserProgressionRequest._fields = []

GetCurrentUserProgressionResponse._fields = [
  FieldMetadata("tierRequirementGroups", "tier_requirement_groups", "_tier_requirement_groups", TierRequirementGroup, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("achievementTypeRankings", "achievement_type_rankings", "_achievement_type_rankings", AchievementTypeRanking, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("isOptedOut", "is_opted_out", "_is_opted_out", bool, False, PredefinedSerializer()),
]

MedalCeremonySettings._fields = [
  FieldMetadata("updateRankingsAndPointsVariant", "update_rankings_and_points_variant", "_update_rankings_and_points_variant", UpdateRankingsAndPointsVariant, UpdateRankingsAndPointsVariant.UPDATE_RANKINGS_AND_POINTS_VARIANT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("medalsFromRun", "medals_from_run", "_medals_from_run", str, None, PredefinedSerializer(), optional=True),
]

PerformMedalCeremonyExperimentRequest._fields = [
  FieldMetadata("runIdentifier", "run_identifier", "_run_identifier", str, "", PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", MedalCeremonySettings, None, KaggleObjectSerializer()),
]

PerformMedalCeremonyExperimentResponse._fields = [
  FieldMetadata("countMedalChanges", "count_medal_changes", "_count_medal_changes", int, 0, PredefinedSerializer()),
  FieldMetadata("countTierChanges", "count_tier_changes", "_count_tier_changes", int, 0, PredefinedSerializer()),
]

TierRequirement._fields = [
  FieldMetadata("label", "label", "_label", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("numberRequired", "number_required", "_number_required", int, 0, PredefinedSerializer()),
  FieldMetadata("numberMet", "number_met", "_number_met", int, 0, PredefinedSerializer()),
  FieldMetadata("level", "level", "_level", int, None, PredefinedSerializer(), optional=True),
]

TierRequirementGroup._fields = [
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("type", "type", "_type", UserAchievementType, UserAchievementType.USER_ACHIEVEMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isComplete", "is_complete", "_is_complete", bool, False, PredefinedSerializer()),
  FieldMetadata("isInProgress", "is_in_progress", "_is_in_progress", bool, False, PredefinedSerializer()),
  FieldMetadata("requirements", "requirements", "_requirements", TierRequirement, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("level", "level", "_level", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("nextLevelRequirements", "next_level_requirements", "_next_level_requirements", TierRequirement, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateUserAchievementsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UpdateUserAchievementsResponse._fields = [
  FieldMetadata("tierChanged", "tier_changed", "_tier_changed", bool, False, PredefinedSerializer()),
  FieldMetadata("newTier", "new_tier", "_new_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
]

