import enum
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user import User
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import List, Optional

class VoteType(enum.Enum):
  """Type/direction of a vote."""
  VOTE_TYPE_UNSPECIFIED = 0
  UPVOTE = 1
  """Casts an approval/positive vote."""
  DELETE_VOTE = 2
  """Removes a previous vote."""

class LegacyVoteButtonModel(KaggleObject):
  r"""
  TODO(b/217729131): Merge these legacy ones with the above.

  Attributes:
    total_votes (int)
    medal_votes (int)
    has_already_voted_up (bool)
    has_already_voted_down (bool)
    can_upvote (bool)
    can_downvote (bool)
    voters (SimpleUserDto)
    current_user_info (SimpleUserDto)
    show_voters (bool)
    always_show_voters (bool)
    kernel_id (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    dataset_id (int)
    forum_message_id (int)
  """

  def __init__(self):
    self._total_votes = 0
    self._medal_votes = 0
    self._has_already_voted_up = False
    self._has_already_voted_down = False
    self._can_upvote = False
    self._can_downvote = False
    self._voters = []
    self._current_user_info = None
    self._show_voters = False
    self._always_show_voters = False
    self._kernel_id = None
    self._dataset_id = None
    self._forum_message_id = None
    self._freeze()

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def medal_votes(self) -> int:
    return self._medal_votes

  @medal_votes.setter
  def medal_votes(self, medal_votes: int):
    if medal_votes is None:
      del self.medal_votes
      return
    if not isinstance(medal_votes, int):
      raise TypeError('medal_votes must be of type int')
    self._medal_votes = medal_votes

  @property
  def has_already_voted_up(self) -> bool:
    return self._has_already_voted_up

  @has_already_voted_up.setter
  def has_already_voted_up(self, has_already_voted_up: bool):
    if has_already_voted_up is None:
      del self.has_already_voted_up
      return
    if not isinstance(has_already_voted_up, bool):
      raise TypeError('has_already_voted_up must be of type bool')
    self._has_already_voted_up = has_already_voted_up

  @property
  def has_already_voted_down(self) -> bool:
    return self._has_already_voted_down

  @has_already_voted_down.setter
  def has_already_voted_down(self, has_already_voted_down: bool):
    if has_already_voted_down is None:
      del self.has_already_voted_down
      return
    if not isinstance(has_already_voted_down, bool):
      raise TypeError('has_already_voted_down must be of type bool')
    self._has_already_voted_down = has_already_voted_down

  @property
  def can_upvote(self) -> bool:
    return self._can_upvote

  @can_upvote.setter
  def can_upvote(self, can_upvote: bool):
    if can_upvote is None:
      del self.can_upvote
      return
    if not isinstance(can_upvote, bool):
      raise TypeError('can_upvote must be of type bool')
    self._can_upvote = can_upvote

  @property
  def can_downvote(self) -> bool:
    return self._can_downvote

  @can_downvote.setter
  def can_downvote(self, can_downvote: bool):
    if can_downvote is None:
      del self.can_downvote
      return
    if not isinstance(can_downvote, bool):
      raise TypeError('can_downvote must be of type bool')
    self._can_downvote = can_downvote

  @property
  def voters(self) -> Optional[List[Optional['SimpleUserDto']]]:
    return self._voters

  @voters.setter
  def voters(self, voters: Optional[List[Optional['SimpleUserDto']]]):
    if voters is None:
      del self.voters
      return
    if not isinstance(voters, list):
      raise TypeError('voters must be of type list')
    if not all([isinstance(t, SimpleUserDto) for t in voters]):
      raise TypeError('voters must contain only items of type SimpleUserDto')
    self._voters = voters

  @property
  def current_user_info(self) -> Optional['SimpleUserDto']:
    return self._current_user_info

  @current_user_info.setter
  def current_user_info(self, current_user_info: Optional['SimpleUserDto']):
    if current_user_info is None:
      del self.current_user_info
      return
    if not isinstance(current_user_info, SimpleUserDto):
      raise TypeError('current_user_info must be of type SimpleUserDto')
    self._current_user_info = current_user_info

  @property
  def show_voters(self) -> bool:
    return self._show_voters

  @show_voters.setter
  def show_voters(self, show_voters: bool):
    if show_voters is None:
      del self.show_voters
      return
    if not isinstance(show_voters, bool):
      raise TypeError('show_voters must be of type bool')
    self._show_voters = show_voters

  @property
  def always_show_voters(self) -> bool:
    return self._always_show_voters

  @always_show_voters.setter
  def always_show_voters(self, always_show_voters: bool):
    if always_show_voters is None:
      del self.always_show_voters
      return
    if not isinstance(always_show_voters, bool):
      raise TypeError('always_show_voters must be of type bool')
    self._always_show_voters = always_show_voters

  @property
  def kernel_id(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._kernel_id or None

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or None

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id or None

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: Optional[int]):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id


class SimpleUserDto(KaggleObject):
  r"""
  This class is only used by pre-KM upvote button.

  Attributes:
    avatar_thumbnail_url (str)
    display_name (str)
    profile_url (str)
    tier (UserAchievementTier)
    tier_int (int)
    user_id (int)
    user_name (str)
  """

  def __init__(self):
    self._avatar_thumbnail_url = None
    self._display_name = None
    self._profile_url = None
    self._tier = UserAchievementTier.NOVICE
    self._tier_int = 0
    self._user_id = 0
    self._user_name = None
    self._freeze()

  @property
  def avatar_thumbnail_url(self) -> str:
    return self._avatar_thumbnail_url or None

  @avatar_thumbnail_url.setter
  def avatar_thumbnail_url(self, avatar_thumbnail_url: Optional[str]):
    if avatar_thumbnail_url is None:
      del self.avatar_thumbnail_url
      return
    if not isinstance(avatar_thumbnail_url, str):
      raise TypeError('avatar_thumbnail_url must be of type str')
    self._avatar_thumbnail_url = avatar_thumbnail_url

  @property
  def display_name(self) -> str:
    return self._display_name or None

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def profile_url(self) -> str:
    return self._profile_url or None

  @profile_url.setter
  def profile_url(self, profile_url: Optional[str]):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

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
  def tier_int(self) -> int:
    return self._tier_int

  @tier_int.setter
  def tier_int(self, tier_int: int):
    if tier_int is None:
      del self.tier_int
      return
    if not isinstance(tier_int, int):
      raise TypeError('tier_int must be of type int')
    self._tier_int = tier_int

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
  def user_name(self) -> str:
    return self._user_name or None

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class VoteButton(KaggleObject):
  r"""
  Attributes:
    total_votes (int)
    medal_votes (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    has_already_voted_up (bool)
    has_already_voted_down (bool)
    can_upvote (bool)
    can_downvote (bool)
    voters (User)
    current_user_info (User)
    show_voters (bool)
    always_show_voters (bool)
    kernel_id (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    dataset_id (int)
    forum_message_id (int)
  """

  def __init__(self):
    self._total_votes = 0
    self._medal_votes = None
    self._has_already_voted_up = False
    self._has_already_voted_down = False
    self._can_upvote = False
    self._can_downvote = False
    self._voters = []
    self._current_user_info = None
    self._show_voters = False
    self._always_show_voters = False
    self._kernel_id = None
    self._dataset_id = None
    self._forum_message_id = None
    self._freeze()

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def medal_votes(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._medal_votes or None

  @medal_votes.setter
  def medal_votes(self, medal_votes: Optional[int]):
    if medal_votes is None:
      del self.medal_votes
      return
    if not isinstance(medal_votes, int):
      raise TypeError('medal_votes must be of type int')
    self._medal_votes = medal_votes

  @property
  def has_already_voted_up(self) -> bool:
    return self._has_already_voted_up

  @has_already_voted_up.setter
  def has_already_voted_up(self, has_already_voted_up: bool):
    if has_already_voted_up is None:
      del self.has_already_voted_up
      return
    if not isinstance(has_already_voted_up, bool):
      raise TypeError('has_already_voted_up must be of type bool')
    self._has_already_voted_up = has_already_voted_up

  @property
  def has_already_voted_down(self) -> bool:
    return self._has_already_voted_down

  @has_already_voted_down.setter
  def has_already_voted_down(self, has_already_voted_down: bool):
    if has_already_voted_down is None:
      del self.has_already_voted_down
      return
    if not isinstance(has_already_voted_down, bool):
      raise TypeError('has_already_voted_down must be of type bool')
    self._has_already_voted_down = has_already_voted_down

  @property
  def can_upvote(self) -> bool:
    return self._can_upvote

  @can_upvote.setter
  def can_upvote(self, can_upvote: bool):
    if can_upvote is None:
      del self.can_upvote
      return
    if not isinstance(can_upvote, bool):
      raise TypeError('can_upvote must be of type bool')
    self._can_upvote = can_upvote

  @property
  def can_downvote(self) -> bool:
    return self._can_downvote

  @can_downvote.setter
  def can_downvote(self, can_downvote: bool):
    if can_downvote is None:
      del self.can_downvote
      return
    if not isinstance(can_downvote, bool):
      raise TypeError('can_downvote must be of type bool')
    self._can_downvote = can_downvote

  @property
  def voters(self) -> Optional[List[Optional['User']]]:
    return self._voters

  @voters.setter
  def voters(self, voters: Optional[List[Optional['User']]]):
    if voters is None:
      del self.voters
      return
    if not isinstance(voters, list):
      raise TypeError('voters must be of type list')
    if not all([isinstance(t, User) for t in voters]):
      raise TypeError('voters must contain only items of type User')
    self._voters = voters

  @property
  def current_user_info(self) -> Optional['User']:
    return self._current_user_info

  @current_user_info.setter
  def current_user_info(self, current_user_info: Optional['User']):
    if current_user_info is None:
      del self.current_user_info
      return
    if not isinstance(current_user_info, User):
      raise TypeError('current_user_info must be of type User')
    self._current_user_info = current_user_info

  @property
  def show_voters(self) -> bool:
    return self._show_voters

  @show_voters.setter
  def show_voters(self, show_voters: bool):
    if show_voters is None:
      del self.show_voters
      return
    if not isinstance(show_voters, bool):
      raise TypeError('show_voters must be of type bool')
    self._show_voters = show_voters

  @property
  def always_show_voters(self) -> bool:
    return self._always_show_voters

  @always_show_voters.setter
  def always_show_voters(self, always_show_voters: bool):
    if always_show_voters is None:
      del self.always_show_voters
      return
    if not isinstance(always_show_voters, bool):
      raise TypeError('always_show_voters must be of type bool')
    self._always_show_voters = always_show_voters

  @property
  def kernel_id(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._kernel_id or None

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or None

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id or None

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: Optional[int]):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id


LegacyVoteButtonModel._fields = [
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("medalVotes", "medal_votes", "_medal_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("hasAlreadyVotedUp", "has_already_voted_up", "_has_already_voted_up", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAlreadyVotedDown", "has_already_voted_down", "_has_already_voted_down", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpvote", "can_upvote", "_can_upvote", bool, False, PredefinedSerializer()),
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("voters", "voters", "_voters", SimpleUserDto, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("currentUserInfo", "current_user_info", "_current_user_info", SimpleUserDto, None, KaggleObjectSerializer()),
  FieldMetadata("showVoters", "show_voters", "_show_voters", bool, False, PredefinedSerializer()),
  FieldMetadata("alwaysShowVoters", "always_show_voters", "_always_show_voters", bool, False, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, None, PredefinedSerializer(), optional=True),
]

SimpleUserDto._fields = [
  FieldMetadata("avatarThumbnailUrl", "avatar_thumbnail_url", "_avatar_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("tierInt", "tier_int", "_tier_int", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
]

VoteButton._fields = [
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("medalVotes", "medal_votes", "_medal_votes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasAlreadyVotedUp", "has_already_voted_up", "_has_already_voted_up", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAlreadyVotedDown", "has_already_voted_down", "_has_already_voted_down", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpvote", "can_upvote", "_can_upvote", bool, False, PredefinedSerializer()),
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("voters", "voters", "_voters", User, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("currentUserInfo", "current_user_info", "_current_user_info", User, None, KaggleObjectSerializer()),
  FieldMetadata("showVoters", "show_voters", "_show_voters", bool, False, PredefinedSerializer()),
  FieldMetadata("alwaysShowVoters", "always_show_voters", "_always_show_voters", bool, False, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, None, PredefinedSerializer(), optional=True),
]

