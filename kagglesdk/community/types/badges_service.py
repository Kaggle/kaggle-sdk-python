from datetime import datetime
import enum
from kagglesdk.community.types.badges_types import Badge, BadgeType, UserBadge
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class ListBadgeRecipientsSortColumn(enum.Enum):
  LIST_BADGE_RECIPIENTS_SORT_BY_UNSPECIFIED = 0
  USER_NAME = 1
  USER_DISPLAY_NAME = 2
  CUSTOM_FIELD_VALUE = 3
  USER_ID = 4
  RECEIVED_TIME = 5

class BadgeListItem(KaggleObject):
  r"""
  Attributes:
    badge (Badge)
      Details about a badge.
  """

  def __init__(self):
    self._badge = None
    self._freeze()

  @property
  def badge(self) -> Optional['Badge']:
    """Details about a badge."""
    return self._badge

  @badge.setter
  def badge(self, badge: Optional['Badge']):
    if badge is None:
      del self.badge
      return
    if not isinstance(badge, Badge):
      raise TypeError('badge must be of type Badge')
    self._badge = badge


class BadgeRecipient(KaggleObject):
  r"""
  Attributes:
    user (UserAvatar)
      The user who received this badge.
    additional_details_markdown (str)
      User-visible additional data for this user about this badge (e.g. list of
      links that earned this badge).
    count (int)
      The number of times this badge was received by this user.
    issued_time (datetime)
      The time the badge was given to the user.
  """

  def __init__(self):
    self._user = None
    self._additional_details_markdown = ""
    self._count = 0
    self._issued_time = None
    self._freeze()

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
  def additional_details_markdown(self) -> str:
    r"""
    User-visible additional data for this user about this badge (e.g. list of
    links that earned this badge).
    """
    return self._additional_details_markdown

  @additional_details_markdown.setter
  def additional_details_markdown(self, additional_details_markdown: str):
    if additional_details_markdown is None:
      del self.additional_details_markdown
      return
    if not isinstance(additional_details_markdown, str):
      raise TypeError('additional_details_markdown must be of type str')
    self._additional_details_markdown = additional_details_markdown

  @property
  def count(self) -> int:
    """The number of times this badge was received by this user."""
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
  def issued_time(self) -> datetime:
    """The time the badge was given to the user."""
    return self._issued_time

  @issued_time.setter
  def issued_time(self, issued_time: datetime):
    if issued_time is None:
      del self.issued_time
      return
    if not isinstance(issued_time, datetime):
      raise TypeError('issued_time must be of type datetime')
    self._issued_time = issued_time


class GetBadgeRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to retrieve information for.
  """

  def __init__(self):
    self._badge_id = 0
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The badge to retrieve information for."""
    return self._badge_id

  @badge_id.setter
  def badge_id(self, badge_id: int):
    if badge_id is None:
      del self.badge_id
      return
    if not isinstance(badge_id, int):
      raise TypeError('badge_id must be of type int')
    self._badge_id = badge_id


class GetUserBadgeRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The user to get the badge for.
    badge_id (int)
      The badge to get.
  """

  def __init__(self):
    self._user_name = ""
    self._badge_id = 0
    self._freeze()

  @property
  def user_name(self) -> str:
    """The user to get the badge for."""
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
  def badge_id(self) -> int:
    """The badge to get."""
    return self._badge_id

  @badge_id.setter
  def badge_id(self, badge_id: int):
    if badge_id is None:
      del self.badge_id
      return
    if not isinstance(badge_id, int):
      raise TypeError('badge_id must be of type int')
    self._badge_id = badge_id


class ListBadgeRecipientsRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      Retrieve the list of users who received this badge.
    page_size (int)
      The number of users to return at once
    page_token (str)
      Optional token given from previous call, returns the next page of results.
    sort_by (ListBadgeRecipientsSortOptions)
      How to order the results, this is applied before pagination.
    user_name_filter (str)
      Optional filter to filter recipients by username, searches by prefix
    display_name_filter (str)
      Optional filter to filter recipients by display name, searches by prefix
    skip (int)
      How many results to skip
    admin_enforce_can_be_seen (bool)
      Optional admin-only filter to enforce that users can be seen. Used for the
      rankings page.
  """

  def __init__(self):
    self._badge_id = 0
    self._page_size = 0
    self._page_token = None
    self._sort_by = None
    self._user_name_filter = None
    self._display_name_filter = None
    self._skip = 0
    self._admin_enforce_can_be_seen = None
    self._freeze()

  @property
  def badge_id(self) -> int:
    """Retrieve the list of users who received this badge."""
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
  def page_size(self) -> int:
    """The number of users to return at once"""
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    """Optional token given from previous call, returns the next page of results."""
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def sort_by(self) -> Optional['ListBadgeRecipientsSortOptions']:
    """How to order the results, this is applied before pagination."""
    return self._sort_by or None

  @sort_by.setter
  def sort_by(self, sort_by: Optional[Optional['ListBadgeRecipientsSortOptions']]):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, ListBadgeRecipientsSortOptions):
      raise TypeError('sort_by must be of type ListBadgeRecipientsSortOptions')
    self._sort_by = sort_by

  @property
  def user_name_filter(self) -> str:
    """Optional filter to filter recipients by username, searches by prefix"""
    return self._user_name_filter or ""

  @user_name_filter.setter
  def user_name_filter(self, user_name_filter: Optional[str]):
    if user_name_filter is None:
      del self.user_name_filter
      return
    if not isinstance(user_name_filter, str):
      raise TypeError('user_name_filter must be of type str')
    self._user_name_filter = user_name_filter

  @property
  def display_name_filter(self) -> str:
    """Optional filter to filter recipients by display name, searches by prefix"""
    return self._display_name_filter or ""

  @display_name_filter.setter
  def display_name_filter(self, display_name_filter: Optional[str]):
    if display_name_filter is None:
      del self.display_name_filter
      return
    if not isinstance(display_name_filter, str):
      raise TypeError('display_name_filter must be of type str')
    self._display_name_filter = display_name_filter

  @property
  def admin_enforce_can_be_seen(self) -> bool:
    r"""
    Optional admin-only filter to enforce that users can be seen. Used for the
    rankings page.
    """
    return self._admin_enforce_can_be_seen or False

  @admin_enforce_can_be_seen.setter
  def admin_enforce_can_be_seen(self, admin_enforce_can_be_seen: Optional[bool]):
    if admin_enforce_can_be_seen is None:
      del self.admin_enforce_can_be_seen
      return
    if not isinstance(admin_enforce_can_be_seen, bool):
      raise TypeError('admin_enforce_can_be_seen must be of type bool')
    self._admin_enforce_can_be_seen = admin_enforce_can_be_seen

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


class ListBadgeRecipientsResponse(KaggleObject):
  r"""
  Attributes:
    badge_recipients (BadgeRecipient)
      List of users who received the badge.
    next_page_token (str)
      Token to retrieve the next page of results.
    total_size (int)
      How many badges in total there are.
  """

  def __init__(self):
    self._badge_recipients = []
    self._next_page_token = ""
    self._total_size = 0
    self._freeze()

  @property
  def badge_recipients(self) -> Optional[List[Optional['BadgeRecipient']]]:
    """List of users who received the badge."""
    return self._badge_recipients

  @badge_recipients.setter
  def badge_recipients(self, badge_recipients: Optional[List[Optional['BadgeRecipient']]]):
    if badge_recipients is None:
      del self.badge_recipients
      return
    if not isinstance(badge_recipients, list):
      raise TypeError('badge_recipients must be of type list')
    if not all([isinstance(t, BadgeRecipient) for t in badge_recipients]):
      raise TypeError('badge_recipients must contain only items of type BadgeRecipient')
    self._badge_recipients = badge_recipients

  @property
  def next_page_token(self) -> str:
    """Token to retrieve the next page of results."""
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
  def total_size(self) -> int:
    """How many badges in total there are."""
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size


class ListBadgeRecipientsSortOptions(KaggleObject):
  r"""
  Attributes:
    column (ListBadgeRecipientsSortColumn)
      Which column to sort by.
    descending (bool)
      Whether to sort ascending or descending.
  """

  def __init__(self):
    self._column = ListBadgeRecipientsSortColumn.LIST_BADGE_RECIPIENTS_SORT_BY_UNSPECIFIED
    self._descending = False
    self._freeze()

  @property
  def column(self) -> 'ListBadgeRecipientsSortColumn':
    """Which column to sort by."""
    return self._column

  @column.setter
  def column(self, column: 'ListBadgeRecipientsSortColumn'):
    if column is None:
      del self.column
      return
    if not isinstance(column, ListBadgeRecipientsSortColumn):
      raise TypeError('column must be of type ListBadgeRecipientsSortColumn')
    self._column = column

  @property
  def descending(self) -> bool:
    """Whether to sort ascending or descending."""
    return self._descending

  @descending.setter
  def descending(self, descending: bool):
    if descending is None:
      del self.descending
      return
    if not isinstance(descending, bool):
      raise TypeError('descending must be of type bool')
    self._descending = descending


class ListBadgesRequest(KaggleObject):
  r"""
  Attributes:
    type (BadgeType)
      List badges of the given type.
  """

  def __init__(self):
    self._type = None
    self._freeze()

  @property
  def type(self) -> 'BadgeType':
    """List badges of the given type."""
    return self._type or BadgeType.BADGE_TYPE_UNSPECIFIED

  @type.setter
  def type(self, type: Optional['BadgeType']):
    if type is None:
      del self.type
      return
    if not isinstance(type, BadgeType):
      raise TypeError('type must be of type BadgeType')
    self._type = type


class ListBadgesResponse(KaggleObject):
  r"""
  Attributes:
    items (BadgeListItem)
      Metadata to render a badge list item.
  """

  def __init__(self):
    self._items = []
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['BadgeListItem']]]:
    """Metadata to render a badge list item."""
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['BadgeListItem']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, BadgeListItem) for t in items]):
      raise TypeError('items must contain only items of type BadgeListItem')
    self._items = items


class ListUserBadgesRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user to fetch badges for.
    badge_type (BadgeType)
      If given, list only badges of the given type
    include_hidden (bool)
      Set to true to include hidden badges in the result, only works if the
      current user is being viewed.
  """

  def __init__(self):
    self._user_id = 0
    self._badge_type = None
    self._include_hidden = False
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user to fetch badges for."""
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
  def badge_type(self) -> 'BadgeType':
    """If given, list only badges of the given type"""
    return self._badge_type or BadgeType.BADGE_TYPE_UNSPECIFIED

  @badge_type.setter
  def badge_type(self, badge_type: Optional['BadgeType']):
    if badge_type is None:
      del self.badge_type
      return
    if not isinstance(badge_type, BadgeType):
      raise TypeError('badge_type must be of type BadgeType')
    self._badge_type = badge_type

  @property
  def include_hidden(self) -> bool:
    r"""
    Set to true to include hidden badges in the result, only works if the
    current user is being viewed.
    """
    return self._include_hidden

  @include_hidden.setter
  def include_hidden(self, include_hidden: bool):
    if include_hidden is None:
      del self.include_hidden
      return
    if not isinstance(include_hidden, bool):
      raise TypeError('include_hidden must be of type bool')
    self._include_hidden = include_hidden


class ListUserBadgesResponse(KaggleObject):
  r"""
  Attributes:
    badges (UserBadge)
      The list of badges that user has earned, in display order.
  """

  def __init__(self):
    self._badges = []
    self._freeze()

  @property
  def badges(self) -> Optional[List[Optional['UserBadge']]]:
    """The list of badges that user has earned, in display order."""
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


class UpdateUserBadgeRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user who’s badge is being updated.
    badge_id (int)
      The badge to update.
    is_hidden (bool)
      Whether to hide this badge.
  """

  def __init__(self):
    self._user_id = 0
    self._badge_id = 0
    self._is_hidden = False
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user who’s badge is being updated."""
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
  def badge_id(self) -> int:
    """The badge to update."""
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
  def is_hidden(self) -> bool:
    """Whether to hide this badge."""
    return self._is_hidden

  @is_hidden.setter
  def is_hidden(self, is_hidden: bool):
    if is_hidden is None:
      del self.is_hidden
      return
    if not isinstance(is_hidden, bool):
      raise TypeError('is_hidden must be of type bool')
    self._is_hidden = is_hidden


BadgeListItem._fields = [
  FieldMetadata("badge", "badge", "_badge", Badge, None, KaggleObjectSerializer()),
]

BadgeRecipient._fields = [
  FieldMetadata("user", "user", "_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("additionalDetailsMarkdown", "additional_details_markdown", "_additional_details_markdown", str, "", PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("issuedTime", "issued_time", "_issued_time", datetime, None, DateTimeSerializer()),
]

GetBadgeRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
]

GetUserBadgeRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
]

ListBadgeRecipientsRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", ListBadgeRecipientsSortOptions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userNameFilter", "user_name_filter", "_user_name_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayNameFilter", "display_name_filter", "_display_name_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("adminEnforceCanBeSeen", "admin_enforce_can_be_seen", "_admin_enforce_can_be_seen", bool, None, PredefinedSerializer(), optional=True),
]

ListBadgeRecipientsResponse._fields = [
  FieldMetadata("badgeRecipients", "badge_recipients", "_badge_recipients", BadgeRecipient, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

ListBadgeRecipientsSortOptions._fields = [
  FieldMetadata("column", "column", "_column", ListBadgeRecipientsSortColumn, ListBadgeRecipientsSortColumn.LIST_BADGE_RECIPIENTS_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("descending", "descending", "_descending", bool, False, PredefinedSerializer()),
]

ListBadgesRequest._fields = [
  FieldMetadata("type", "type", "_type", BadgeType, None, EnumSerializer(), optional=True),
]

ListBadgesResponse._fields = [
  FieldMetadata("items", "items", "_items", BadgeListItem, [], ListSerializer(KaggleObjectSerializer())),
]

ListUserBadgesRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("badgeType", "badge_type", "_badge_type", BadgeType, None, EnumSerializer(), optional=True),
  FieldMetadata("includeHidden", "include_hidden", "_include_hidden", bool, False, PredefinedSerializer()),
]

ListUserBadgesResponse._fields = [
  FieldMetadata("badges", "badges", "_badges", UserBadge, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateUserBadgeRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isHidden", "is_hidden", "_is_hidden", bool, False, PredefinedSerializer()),
]

