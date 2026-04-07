from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional

class BadgeState(enum.Enum):
  r"""
  What state the badge is in (ie whether it's shown to users and whether it's
  awarding).
  """
  BADGE_STATE_UNSPECIFIED = 0
  INACTIVE = 1
  """Not shown to users and not awarding."""
  ACTIVE = 2
  """Showing to users and awarding."""
  LEGACY = 3
  """Showing to users but no longer awarding it."""

class BadgeType(enum.Enum):
  """Type of badge (category)."""
  BADGE_TYPE_UNSPECIFIED = 0
  AWARD = 1
  """Highlighted on the profile, a public badge for a big accomplishment."""
  REGULAR = 2
  r"""
  Not highlighted on the profile, a public badge for a regular
  accomplishment.
  """

class Badge(KaggleObject):
  r"""
  Details about a badge that are common to all users.

  Attributes:
    badge_id (int)
      The id of the badge
    name (str)
      The name of the badge.
    description (str)
      A description of the badge and how to earn it.
    image_url (str)
      Link to the image displayed for the badge.
    badge_type (BadgeType)
      Which type of badge this is.
    banner_info (str)
      Text to display in a banner on the badge (e.g. a year).
    custom_field_name (str)
      The name of the custom field
    issued_user_count (int)
      The number of users that have earned this badge.
    rarity_index (int)
      The rarity index of the badge, with 1 being the most rare. This is only
      populated for the top 10% most rare badges.
  """

  def __init__(self):
    self._badge_id = 0
    self._name = ""
    self._description = ""
    self._image_url = ""
    self._badge_type = BadgeType.BADGE_TYPE_UNSPECIFIED
    self._banner_info = ""
    self._custom_field_name = ""
    self._issued_user_count = 0
    self._rarity_index = None
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The id of the badge"""
    return self._badge_id

  @badge_id.setter
  def badge_id(self, badge_id: int):
    if badge_id is None:
      del self.badge_id
      return
    if not isinstance(badge_id, int):
      raise TypeError('badge_id must be of type int')
    self._badge_id = badge_id

  @property
  def name(self) -> str:
    """The name of the badge."""
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
  def description(self) -> str:
    """A description of the badge and how to earn it."""
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def image_url(self) -> str:
    """Link to the image displayed for the badge."""
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
  def badge_type(self) -> 'BadgeType':
    """Which type of badge this is."""
    return self._badge_type

  @badge_type.setter
  def badge_type(self, badge_type: 'BadgeType'):
    if badge_type is None:
      del self.badge_type
      return
    if not isinstance(badge_type, BadgeType):
      raise TypeError('badge_type must be of type BadgeType')
    self._badge_type = badge_type

  @property
  def banner_info(self) -> str:
    """Text to display in a banner on the badge (e.g. a year)."""
    return self._banner_info

  @banner_info.setter
  def banner_info(self, banner_info: str):
    if banner_info is None:
      del self.banner_info
      return
    if not isinstance(banner_info, str):
      raise TypeError('banner_info must be of type str')
    self._banner_info = banner_info

  @property
  def custom_field_name(self) -> str:
    """The name of the custom field"""
    return self._custom_field_name

  @custom_field_name.setter
  def custom_field_name(self, custom_field_name: str):
    if custom_field_name is None:
      del self.custom_field_name
      return
    if not isinstance(custom_field_name, str):
      raise TypeError('custom_field_name must be of type str')
    self._custom_field_name = custom_field_name

  @property
  def issued_user_count(self) -> int:
    """The number of users that have earned this badge."""
    return self._issued_user_count

  @issued_user_count.setter
  def issued_user_count(self, issued_user_count: int):
    if issued_user_count is None:
      del self.issued_user_count
      return
    if not isinstance(issued_user_count, int):
      raise TypeError('issued_user_count must be of type int')
    self._issued_user_count = issued_user_count

  @property
  def rarity_index(self) -> int:
    r"""
    The rarity index of the badge, with 1 being the most rare. This is only
    populated for the top 10% most rare badges.
    """
    return self._rarity_index or 0

  @rarity_index.setter
  def rarity_index(self, rarity_index: Optional[int]):
    if rarity_index is None:
      del self.rarity_index
      return
    if not isinstance(rarity_index, int):
      raise TypeError('rarity_index must be of type int')
    self._rarity_index = rarity_index


class UserBadge(KaggleObject):
  r"""
  The details for a badge for a given user.

  Attributes:
    badge (Badge)
      Information about the badge that was earned.
    is_hidden (bool)
      Whether this badge is currently hidden by the user. If another user called
      this, this will always be false.
    count (int)
      Count of the number of times this was received.
    custom_field_value (str)
      User-visible custom data for this user about this badge (e.g. list of
      links that earned this badge).
    user (UserAvatar)
      The user who received this badge.
    achieved_time (datetime)
      The date and time that the badge was earned.
  """

  def __init__(self):
    self._badge = None
    self._is_hidden = False
    self._count = 0
    self._custom_field_value = ""
    self._user = None
    self._achieved_time = None
    self._freeze()

  @property
  def badge(self) -> Optional['Badge']:
    """Information about the badge that was earned."""
    return self._badge

  @badge.setter
  def badge(self, badge: Optional['Badge']):
    if badge is None:
      del self.badge
      return
    if not isinstance(badge, Badge):
      raise TypeError('badge must be of type Badge')
    self._badge = badge

  @property
  def is_hidden(self) -> bool:
    r"""
    Whether this badge is currently hidden by the user. If another user called
    this, this will always be false.
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
  def count(self) -> int:
    """Count of the number of times this was received."""
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def custom_field_value(self) -> str:
    r"""
    User-visible custom data for this user about this badge (e.g. list of
    links that earned this badge).
    """
    return self._custom_field_value

  @custom_field_value.setter
  def custom_field_value(self, custom_field_value: str):
    if custom_field_value is None:
      del self.custom_field_value
      return
    if not isinstance(custom_field_value, str):
      raise TypeError('custom_field_value must be of type str')
    self._custom_field_value = custom_field_value

  @property
  def user(self) -> Optional['UserAvatar']:
    """The user who received this badge."""
    return self._user

  @user.setter
  def user(self, user: Optional['UserAvatar']):
    if user is None:
      del self.user
      return
    if not isinstance(user, UserAvatar):
      raise TypeError('user must be of type UserAvatar')
    self._user = user

  @property
  def achieved_time(self) -> datetime:
    """The date and time that the badge was earned."""
    return self._achieved_time

  @achieved_time.setter
  def achieved_time(self, achieved_time: datetime):
    if achieved_time is None:
      del self.achieved_time
      return
    if not isinstance(achieved_time, datetime):
      raise TypeError('achieved_time must be of type datetime')
    self._achieved_time = achieved_time


Badge._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("badgeType", "badge_type", "_badge_type", BadgeType, BadgeType.BADGE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("bannerInfo", "banner_info", "_banner_info", str, "", PredefinedSerializer()),
  FieldMetadata("customFieldName", "custom_field_name", "_custom_field_name", str, "", PredefinedSerializer()),
  FieldMetadata("issuedUserCount", "issued_user_count", "_issued_user_count", int, 0, PredefinedSerializer()),
  FieldMetadata("rarityIndex", "rarity_index", "_rarity_index", int, None, PredefinedSerializer(), optional=True),
]

UserBadge._fields = [
  FieldMetadata("badge", "badge", "_badge", Badge, None, KaggleObjectSerializer()),
  FieldMetadata("isHidden", "is_hidden", "_is_hidden", bool, False, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("customFieldValue", "custom_field_value", "_custom_field_value", str, "", PredefinedSerializer()),
  FieldMetadata("user", "user", "_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("achievedTime", "achieved_time", "_achieved_time", datetime, None, DateTimeSerializer()),
]

