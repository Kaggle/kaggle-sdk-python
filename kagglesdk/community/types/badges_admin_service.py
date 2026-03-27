from datetime import datetime, timedelta
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.community.types.badges_service import BadgeRecipient
from kagglesdk.community.types.badges_types import Badge, BadgeState, BadgeType
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class ListBadgeConfigsSortColumn(enum.Enum):
  LIST_BADGE_CONFIGS_SORT_BY_UNSPECIFIED = 0
  CREATE_TIME = 1
  LAST_ISSUED_TIME = 2
  COUNT_ISSUED = 3
  NAME = 4
  SORT_KEY = 5

class BadgeConfig(KaggleObject):
  r"""
  Details about the configuration of a badge

  Attributes:
    badge_details (Badge)
      User-visible details of the badge.
    custom_field_name (str)
      A name/label to use for the custom field value for recipients of this
      badge.
    has_counter (bool)
      Whether this badge has a counter and thus can be assigned to the same user
      multiple times without using different info banners.
    query_config (QueryBadgeConfig)
      If the badge isn't manual, this configures the automatic assignment.
    create_time (datetime)
      When this configuration for this badge was created.
    badge_state (BadgeState)
      What state the badge is in (visibility and awarding)
    issued_count (int)
      @OutputOnly How many times the badge has been given.
    last_issued_time (datetime)
      @OutputOnly The last time the badge was given (if ever).
    sort_key (float)
      A configured value used to sort the badges on a user profile (should be
      between 0 and 1).
  """

  def __init__(self):
    self._badge_details = None
    self._custom_field_name = ""
    self._has_counter = False
    self._query_config = None
    self._create_time = None
    self._badge_state = BadgeState.BADGE_STATE_UNSPECIFIED
    self._issued_count = None
    self._last_issued_time = None
    self._sort_key = 0.0
    self._freeze()

  @property
  def badge_details(self) -> Optional['Badge']:
    """User-visible details of the badge."""
    return self._badge_details

  @badge_details.setter
  def badge_details(self, badge_details: Optional['Badge']):
    if badge_details is None:
      del self.badge_details
      return
    if not isinstance(badge_details, Badge):
      raise TypeError('badge_details must be of type Badge')
    self._badge_details = badge_details

  @property
  def custom_field_name(self) -> str:
    r"""
    A name/label to use for the custom field value for recipients of this
    badge.
    """
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
  def has_counter(self) -> bool:
    r"""
    Whether this badge has a counter and thus can be assigned to the same user
    multiple times without using different info banners.
    """
    return self._has_counter

  @has_counter.setter
  def has_counter(self, has_counter: bool):
    if has_counter is None:
      del self.has_counter
      return
    if not isinstance(has_counter, bool):
      raise TypeError('has_counter must be of type bool')
    self._has_counter = has_counter

  @property
  def query_config(self) -> Optional['QueryBadgeConfig']:
    """If the badge isn't manual, this configures the automatic assignment."""
    return self._query_config or None

  @query_config.setter
  def query_config(self, query_config: Optional[Optional['QueryBadgeConfig']]):
    if query_config is None:
      del self.query_config
      return
    if not isinstance(query_config, QueryBadgeConfig):
      raise TypeError('query_config must be of type QueryBadgeConfig')
    self._query_config = query_config

  @property
  def create_time(self) -> datetime:
    """When this configuration for this badge was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def badge_state(self) -> 'BadgeState':
    """What state the badge is in (visibility and awarding)"""
    return self._badge_state

  @badge_state.setter
  def badge_state(self, badge_state: 'BadgeState'):
    if badge_state is None:
      del self.badge_state
      return
    if not isinstance(badge_state, BadgeState):
      raise TypeError('badge_state must be of type BadgeState')
    self._badge_state = badge_state

  @property
  def sort_key(self) -> float:
    r"""
    A configured value used to sort the badges on a user profile (should be
    between 0 and 1).
    """
    return self._sort_key

  @sort_key.setter
  def sort_key(self, sort_key: float):
    if sort_key is None:
      del self.sort_key
      return
    if not isinstance(sort_key, float):
      raise TypeError('sort_key must be of type float')
    self._sort_key = sort_key

  @property
  def issued_count(self) -> int:
    """@OutputOnly How many times the badge has been given."""
    return self._issued_count or 0

  @issued_count.setter
  def issued_count(self, issued_count: Optional[int]):
    if issued_count is None:
      del self.issued_count
      return
    if not isinstance(issued_count, int):
      raise TypeError('issued_count must be of type int')
    self._issued_count = issued_count

  @property
  def last_issued_time(self) -> datetime:
    """@OutputOnly The last time the badge was given (if ever)."""
    return self._last_issued_time or None

  @last_issued_time.setter
  def last_issued_time(self, last_issued_time: Optional[datetime]):
    if last_issued_time is None:
      del self.last_issued_time
      return
    if not isinstance(last_issued_time, datetime):
      raise TypeError('last_issued_time must be of type datetime')
    self._last_issued_time = last_issued_time


class BadgeRecipientStatus(KaggleObject):
  r"""
  Attributes:
    parsed_user_name (str)
    parsed_additional_details_markdown (str)
    user (UserAvatar)
    existing_additional_details_markdown (str)
  """

  def __init__(self):
    self._parsed_user_name = ""
    self._parsed_additional_details_markdown = ""
    self._user = None
    self._existing_additional_details_markdown = None
    self._freeze()

  @property
  def parsed_user_name(self) -> str:
    return self._parsed_user_name

  @parsed_user_name.setter
  def parsed_user_name(self, parsed_user_name: str):
    if parsed_user_name is None:
      del self.parsed_user_name
      return
    if not isinstance(parsed_user_name, str):
      raise TypeError('parsed_user_name must be of type str')
    self._parsed_user_name = parsed_user_name

  @property
  def parsed_additional_details_markdown(self) -> str:
    return self._parsed_additional_details_markdown

  @parsed_additional_details_markdown.setter
  def parsed_additional_details_markdown(self, parsed_additional_details_markdown: str):
    if parsed_additional_details_markdown is None:
      del self.parsed_additional_details_markdown
      return
    if not isinstance(parsed_additional_details_markdown, str):
      raise TypeError('parsed_additional_details_markdown must be of type str')
    self._parsed_additional_details_markdown = parsed_additional_details_markdown

  @property
  def user(self) -> Optional['UserAvatar']:
    return self._user or None

  @user.setter
  def user(self, user: Optional[Optional['UserAvatar']]):
    if user is None:
      del self.user
      return
    if not isinstance(user, UserAvatar):
      raise TypeError('user must be of type UserAvatar')
    self._user = user

  @property
  def existing_additional_details_markdown(self) -> str:
    return self._existing_additional_details_markdown or ""

  @existing_additional_details_markdown.setter
  def existing_additional_details_markdown(self, existing_additional_details_markdown: Optional[str]):
    if existing_additional_details_markdown is None:
      del self.existing_additional_details_markdown
      return
    if not isinstance(existing_additional_details_markdown, str):
      raise TypeError('existing_additional_details_markdown must be of type str')
    self._existing_additional_details_markdown = existing_additional_details_markdown


class BadgeStats(KaggleObject):
  r"""
  Attributes:
    created_by (UserAvatar)
      The user that created the badge.
    issued_count (int)
      How many times the badge has been given.
    last_issued_time (datetime)
      The last time the badge was given (if ever).
    last_issued_by (UserAvatar)
      Manual only: The last user to issue this badge.
    last_runtime_duration (timedelta)
      Automatic only: How long it took the last run to complete.
    last_runtime_error (str)
      Automatic only: Any errors from the last run.
    issued_user_count (int)
      How many users the badge has been given to.
  """

  def __init__(self):
    self._created_by = None
    self._issued_count = 0
    self._last_issued_time = None
    self._last_issued_by = None
    self._last_runtime_duration = None
    self._last_runtime_error = None
    self._issued_user_count = 0
    self._freeze()

  @property
  def created_by(self) -> Optional['UserAvatar']:
    """The user that created the badge."""
    return self._created_by

  @created_by.setter
  def created_by(self, created_by: Optional['UserAvatar']):
    if created_by is None:
      del self.created_by
      return
    if not isinstance(created_by, UserAvatar):
      raise TypeError('created_by must be of type UserAvatar')
    self._created_by = created_by

  @property
  def issued_count(self) -> int:
    """How many times the badge has been given."""
    return self._issued_count

  @issued_count.setter
  def issued_count(self, issued_count: int):
    if issued_count is None:
      del self.issued_count
      return
    if not isinstance(issued_count, int):
      raise TypeError('issued_count must be of type int')
    self._issued_count = issued_count

  @property
  def issued_user_count(self) -> int:
    """How many users the badge has been given to."""
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
  def last_issued_time(self) -> datetime:
    """The last time the badge was given (if ever)."""
    return self._last_issued_time or None

  @last_issued_time.setter
  def last_issued_time(self, last_issued_time: Optional[datetime]):
    if last_issued_time is None:
      del self.last_issued_time
      return
    if not isinstance(last_issued_time, datetime):
      raise TypeError('last_issued_time must be of type datetime')
    self._last_issued_time = last_issued_time

  @property
  def last_issued_by(self) -> Optional['UserAvatar']:
    """Manual only: The last user to issue this badge."""
    return self._last_issued_by or None

  @last_issued_by.setter
  def last_issued_by(self, last_issued_by: Optional[Optional['UserAvatar']]):
    if last_issued_by is None:
      del self.last_issued_by
      return
    if not isinstance(last_issued_by, UserAvatar):
      raise TypeError('last_issued_by must be of type UserAvatar')
    self._last_issued_by = last_issued_by

  @property
  def last_runtime_duration(self) -> timedelta:
    """Automatic only: How long it took the last run to complete."""
    return self._last_runtime_duration or None

  @last_runtime_duration.setter
  def last_runtime_duration(self, last_runtime_duration: Optional[timedelta]):
    if last_runtime_duration is None:
      del self.last_runtime_duration
      return
    if not isinstance(last_runtime_duration, timedelta):
      raise TypeError('last_runtime_duration must be of type timedelta')
    self._last_runtime_duration = last_runtime_duration

  @property
  def last_runtime_error(self) -> str:
    """Automatic only: Any errors from the last run."""
    return self._last_runtime_error or ""

  @last_runtime_error.setter
  def last_runtime_error(self, last_runtime_error: Optional[str]):
    if last_runtime_error is None:
      del self.last_runtime_error
      return
    if not isinstance(last_runtime_error, str):
      raise TypeError('last_runtime_error must be of type str')
    self._last_runtime_error = last_runtime_error


class BatchCreateBadgeRecipientsRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      Badge these requests are for, each request may omit this field.
    requests (CreateBadgeRecipientRequest)
      A list of user details for awarding the badge.
  """

  def __init__(self):
    self._badge_id = 0
    self._requests = []
    self._freeze()

  @property
  def badge_id(self) -> int:
    """Badge these requests are for, each request may omit this field."""
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
  def requests(self) -> Optional[List[Optional['CreateBadgeRecipientRequest']]]:
    """A list of user details for awarding the badge."""
    return self._requests

  @requests.setter
  def requests(self, requests: Optional[List[Optional['CreateBadgeRecipientRequest']]]):
    if requests is None:
      del self.requests
      return
    if not isinstance(requests, list):
      raise TypeError('requests must be of type list')
    if not all([isinstance(t, CreateBadgeRecipientRequest) for t in requests]):
      raise TypeError('requests must contain only items of type CreateBadgeRecipientRequest')
    self._requests = requests


class BatchCreateBadgeRecipientsResponse(KaggleObject):
  r"""
  Attributes:
    user_badges (BadgeRecipient)
      A list of the badge recipients added. Order matches the request order.
  """

  def __init__(self):
    self._user_badges = []
    self._freeze()

  @property
  def user_badges(self) -> Optional[List[Optional['BadgeRecipient']]]:
    """A list of the badge recipients added. Order matches the request order."""
    return self._user_badges

  @user_badges.setter
  def user_badges(self, user_badges: Optional[List[Optional['BadgeRecipient']]]):
    if user_badges is None:
      del self.user_badges
      return
    if not isinstance(user_badges, list):
      raise TypeError('user_badges must be of type list')
    if not all([isinstance(t, BadgeRecipient) for t in user_badges]):
      raise TypeError('user_badges must contain only items of type BadgeRecipient')
    self._user_badges = user_badges


class BatchDeleteBadgeRecipientsRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to remove.
    user_ids (int)
      A list of users to remove the badge from.
  """

  def __init__(self):
    self._badge_id = 0
    self._user_ids = []
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The badge to remove."""
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
  def user_ids(self) -> Optional[List[int]]:
    """A list of users to remove the badge from."""
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


class CreateBadgeRecipientRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to award.
    badge_recipient (BadgeRecipient)
      All the details for the user
  """

  def __init__(self):
    self._badge_id = 0
    self._badge_recipient = None
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The badge to award."""
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
  def badge_recipient(self) -> Optional['BadgeRecipient']:
    """All the details for the user"""
    return self._badge_recipient

  @badge_recipient.setter
  def badge_recipient(self, badge_recipient: Optional['BadgeRecipient']):
    if badge_recipient is None:
      del self.badge_recipient
      return
    if not isinstance(badge_recipient, BadgeRecipient):
      raise TypeError('badge_recipient must be of type BadgeRecipient')
    self._badge_recipient = badge_recipient


class DeleteBadgeConfigRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The id of the badge to delete all data for.
    badge_name (str)
      The name of the badge, as a confirmation that the right badge is being
      deleted.
  """

  def __init__(self):
    self._badge_id = 0
    self._badge_name = ""
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The id of the badge to delete all data for."""
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
  def badge_name(self) -> str:
    r"""
    The name of the badge, as a confirmation that the right badge is being
    deleted.
    """
    return self._badge_name

  @badge_name.setter
  def badge_name(self, badge_name: str):
    if badge_name is None:
      del self.badge_name
      return
    if not isinstance(badge_name, str):
      raise TypeError('badge_name must be of type str')
    self._badge_name = badge_name


class GetBadgeConfigRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The id of the badge to retrieve.
  """

  def __init__(self):
    self._badge_id = 0
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The id of the badge to retrieve."""
    return self._badge_id

  @badge_id.setter
  def badge_id(self, badge_id: int):
    if badge_id is None:
      del self.badge_id
      return
    if not isinstance(badge_id, int):
      raise TypeError('badge_id must be of type int')
    self._badge_id = badge_id


class GetBadgeRecipientsStatusRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to check for.
    user_list (str)
      A list of users to verify, sent as-is from what the admin enters.
      Uses a CSV parser to separate out each entry, but entries may be either
      rows or columns. This means the following formats are accepted:
      1. A single username
      2. A comma separated list of usernames
      3. One username per line
      4. CSV file
      each username may optionally be followed by any additional markdown data.
  """

  def __init__(self):
    self._badge_id = 0
    self._user_list = ""
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The badge to check for."""
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
  def user_list(self) -> str:
    r"""
    A list of users to verify, sent as-is from what the admin enters.
    Uses a CSV parser to separate out each entry, but entries may be either
    rows or columns. This means the following formats are accepted:
    1. A single username
    2. A comma separated list of usernames
    3. One username per line
    4. CSV file
    each username may optionally be followed by any additional markdown data.
    """
    return self._user_list

  @user_list.setter
  def user_list(self, user_list: str):
    if user_list is None:
      del self.user_list
      return
    if not isinstance(user_list, str):
      raise TypeError('user_list must be of type str')
    self._user_list = user_list


class GetBadgeRecipientsStatusResponse(KaggleObject):
  r"""
  Attributes:
    matched_new_users (BadgeRecipientStatus)
      The list of users that were matched and haven't received the badge yet. The
      additional_details_markdown field will contain any data passed in with the
      user.
    matched_existing_users (BadgeRecipientStatus)
      The list of users that were matched but already have the badge. They can
      only receive it if the badge supports counters.
    unmatched_users (BadgeRecipientStatus)
      The list of users that were not matched, along with the additional data
      specified.
  """

  def __init__(self):
    self._matched_new_users = []
    self._matched_existing_users = []
    self._unmatched_users = []
    self._freeze()

  @property
  def matched_new_users(self) -> Optional[List[Optional['BadgeRecipientStatus']]]:
    r"""
    The list of users that were matched and haven't received the badge yet. The
    additional_details_markdown field will contain any data passed in with the
    user.
    """
    return self._matched_new_users

  @matched_new_users.setter
  def matched_new_users(self, matched_new_users: Optional[List[Optional['BadgeRecipientStatus']]]):
    if matched_new_users is None:
      del self.matched_new_users
      return
    if not isinstance(matched_new_users, list):
      raise TypeError('matched_new_users must be of type list')
    if not all([isinstance(t, BadgeRecipientStatus) for t in matched_new_users]):
      raise TypeError('matched_new_users must contain only items of type BadgeRecipientStatus')
    self._matched_new_users = matched_new_users

  @property
  def matched_existing_users(self) -> Optional[List[Optional['BadgeRecipientStatus']]]:
    r"""
    The list of users that were matched but already have the badge. They can
    only receive it if the badge supports counters.
    """
    return self._matched_existing_users

  @matched_existing_users.setter
  def matched_existing_users(self, matched_existing_users: Optional[List[Optional['BadgeRecipientStatus']]]):
    if matched_existing_users is None:
      del self.matched_existing_users
      return
    if not isinstance(matched_existing_users, list):
      raise TypeError('matched_existing_users must be of type list')
    if not all([isinstance(t, BadgeRecipientStatus) for t in matched_existing_users]):
      raise TypeError('matched_existing_users must contain only items of type BadgeRecipientStatus')
    self._matched_existing_users = matched_existing_users

  @property
  def unmatched_users(self) -> Optional[List[Optional['BadgeRecipientStatus']]]:
    r"""
    The list of users that were not matched, along with the additional data
    specified.
    """
    return self._unmatched_users

  @unmatched_users.setter
  def unmatched_users(self, unmatched_users: Optional[List[Optional['BadgeRecipientStatus']]]):
    if unmatched_users is None:
      del self.unmatched_users
      return
    if not isinstance(unmatched_users, list):
      raise TypeError('unmatched_users must be of type list')
    if not all([isinstance(t, BadgeRecipientStatus) for t in unmatched_users]):
      raise TypeError('unmatched_users must contain only items of type BadgeRecipientStatus')
    self._unmatched_users = unmatched_users


class GetBadgeStatsRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The id of the badge to retrieve stats for.
  """

  def __init__(self):
    self._badge_id = 0
    self._freeze()

  @property
  def badge_id(self) -> int:
    """The id of the badge to retrieve stats for."""
    return self._badge_id

  @badge_id.setter
  def badge_id(self, badge_id: int):
    if badge_id is None:
      del self.badge_id
      return
    if not isinstance(badge_id, int):
      raise TypeError('badge_id must be of type int')
    self._badge_id = badge_id


class ListBadgeConfigsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
      The number of badges to return at once.
    page_token (str)
      Token given from previous call, returns the next page of results.
    sort_by (ListBadgeConfigsSortOptions)
      How to order the results, this is applied before pagination.
    type (BadgeType)
      Optional type to filter the results to only those.
    name_filter (str)
      Optional filter for the name of the badge, searches with StartsWith.
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._sort_by = None
    self._type = None
    self._name_filter = None
    self._freeze()

  @property
  def page_size(self) -> int:
    """The number of badges to return at once."""
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
    """Token given from previous call, returns the next page of results."""
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
  def sort_by(self) -> Optional['ListBadgeConfigsSortOptions']:
    """How to order the results, this is applied before pagination."""
    return self._sort_by or None

  @sort_by.setter
  def sort_by(self, sort_by: Optional[Optional['ListBadgeConfigsSortOptions']]):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, ListBadgeConfigsSortOptions):
      raise TypeError('sort_by must be of type ListBadgeConfigsSortOptions')
    self._sort_by = sort_by

  @property
  def type(self) -> 'BadgeType':
    """Optional type to filter the results to only those."""
    return self._type or BadgeType.BADGE_TYPE_UNSPECIFIED

  @type.setter
  def type(self, type: Optional['BadgeType']):
    if type is None:
      del self.type
      return
    if not isinstance(type, BadgeType):
      raise TypeError('type must be of type BadgeType')
    self._type = type

  @property
  def name_filter(self) -> str:
    """Optional filter for the name of the badge, searches with StartsWith."""
    return self._name_filter or ""

  @name_filter.setter
  def name_filter(self, name_filter: Optional[str]):
    if name_filter is None:
      del self.name_filter
      return
    if not isinstance(name_filter, str):
      raise TypeError('name_filter must be of type str')
    self._name_filter = name_filter


class ListBadgeConfigsResponse(KaggleObject):
  r"""
  Attributes:
    badges (BadgeConfig)
    next_page_token (str)
      Token to retrieve the next page of results.
    total_size (int)
      How many badges in total there are.
  """

  def __init__(self):
    self._badges = []
    self._next_page_token = ""
    self._total_size = 0
    self._freeze()

  @property
  def badges(self) -> Optional[List[Optional['BadgeConfig']]]:
    return self._badges

  @badges.setter
  def badges(self, badges: Optional[List[Optional['BadgeConfig']]]):
    if badges is None:
      del self.badges
      return
    if not isinstance(badges, list):
      raise TypeError('badges must be of type list')
    if not all([isinstance(t, BadgeConfig) for t in badges]):
      raise TypeError('badges must contain only items of type BadgeConfig')
    self._badges = badges

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


class ListBadgeConfigsSortOptions(KaggleObject):
  r"""
  Attributes:
    column (ListBadgeConfigsSortColumn)
      Which column to sort by.
    descending (bool)
      Whether to sort ascending or descending.
  """

  def __init__(self):
    self._column = ListBadgeConfigsSortColumn.LIST_BADGE_CONFIGS_SORT_BY_UNSPECIFIED
    self._descending = False
    self._freeze()

  @property
  def column(self) -> 'ListBadgeConfigsSortColumn':
    """Which column to sort by."""
    return self._column

  @column.setter
  def column(self, column: 'ListBadgeConfigsSortColumn'):
    if column is None:
      del self.column
      return
    if not isinstance(column, ListBadgeConfigsSortColumn):
      raise TypeError('column must be of type ListBadgeConfigsSortColumn')
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


class QueryBadgeConfig(KaggleObject):
  r"""
  Attributes:
    badge_recipients_query_text (str)
      BigQuery SQL query text that defines who should receive badge.
    badge_refresh_query_text (str)
      Optional query to check if the list of recipients needs to be refreshed.
      This allows a badge to be checked more frequently, since it doesn't need
      to do the full comparison.
  """

  def __init__(self):
    self._badge_recipients_query_text = ""
    self._badge_refresh_query_text = None
    self._freeze()

  @property
  def badge_recipients_query_text(self) -> str:
    """BigQuery SQL query text that defines who should receive badge."""
    return self._badge_recipients_query_text

  @badge_recipients_query_text.setter
  def badge_recipients_query_text(self, badge_recipients_query_text: str):
    if badge_recipients_query_text is None:
      del self.badge_recipients_query_text
      return
    if not isinstance(badge_recipients_query_text, str):
      raise TypeError('badge_recipients_query_text must be of type str')
    self._badge_recipients_query_text = badge_recipients_query_text

  @property
  def badge_refresh_query_text(self) -> str:
    r"""
    Optional query to check if the list of recipients needs to be refreshed.
    This allows a badge to be checked more frequently, since it doesn't need
    to do the full comparison.
    """
    return self._badge_refresh_query_text or ""

  @badge_refresh_query_text.setter
  def badge_refresh_query_text(self, badge_refresh_query_text: Optional[str]):
    if badge_refresh_query_text is None:
      del self.badge_refresh_query_text
      return
    if not isinstance(badge_refresh_query_text, str):
      raise TypeError('badge_refresh_query_text must be of type str')
    self._badge_refresh_query_text = badge_refresh_query_text


class SyncBigQueryBadgeRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to sync, will issue this badge to users based on the BigQuery
      configured.
    max_size (int)
      The maximum number to create/update.
    after_user_id (int)
      Skip all users up to and including this user (ordered by id), used to
      continue with the next batch. Default 0.
  """

  def __init__(self):
    self._badge_id = 0
    self._max_size = 0
    self._after_user_id = 0
    self._freeze()

  @property
  def badge_id(self) -> int:
    r"""
    The badge to sync, will issue this badge to users based on the BigQuery
    configured.
    """
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
  def max_size(self) -> int:
    """The maximum number to create/update."""
    return self._max_size

  @max_size.setter
  def max_size(self, max_size: int):
    if max_size is None:
      del self.max_size
      return
    if not isinstance(max_size, int):
      raise TypeError('max_size must be of type int')
    self._max_size = max_size

  @property
  def after_user_id(self) -> int:
    r"""
    Skip all users up to and including this user (ordered by id), used to
    continue with the next batch. Default 0.
    """
    return self._after_user_id

  @after_user_id.setter
  def after_user_id(self, after_user_id: int):
    if after_user_id is None:
      del self.after_user_id
      return
    if not isinstance(after_user_id, int):
      raise TypeError('after_user_id must be of type int')
    self._after_user_id = after_user_id


class SyncBigQueryBadgeResponse(KaggleObject):
  r"""
  Attributes:
    new_users (int)
      The ids of the users that received badges this run.
    updated_users (int)
      The ids of the user that were updated this run.
    ignored_users (int)
      The ids of the users that were returned by BiqQuery but ignored this
      run (because they already exist). This is likely from a delay in mssql2bq
      sync of the UserBadges table.
    error_message (str)
      A message if an error occured. If the error came from BigQuery, this will
      be the message returned by BigQuery.
  """

  def __init__(self):
    self._new_users = []
    self._updated_users = []
    self._ignored_users = []
    self._error_message = ""
    self._freeze()

  @property
  def new_users(self) -> Optional[List[int]]:
    """The ids of the users that received badges this run."""
    return self._new_users

  @new_users.setter
  def new_users(self, new_users: Optional[List[int]]):
    if new_users is None:
      del self.new_users
      return
    if not isinstance(new_users, list):
      raise TypeError('new_users must be of type list')
    if not all([isinstance(t, int) for t in new_users]):
      raise TypeError('new_users must contain only items of type int')
    self._new_users = new_users

  @property
  def updated_users(self) -> Optional[List[int]]:
    """The ids of the user that were updated this run."""
    return self._updated_users

  @updated_users.setter
  def updated_users(self, updated_users: Optional[List[int]]):
    if updated_users is None:
      del self.updated_users
      return
    if not isinstance(updated_users, list):
      raise TypeError('updated_users must be of type list')
    if not all([isinstance(t, int) for t in updated_users]):
      raise TypeError('updated_users must contain only items of type int')
    self._updated_users = updated_users

  @property
  def ignored_users(self) -> Optional[List[int]]:
    r"""
    The ids of the users that were returned by BiqQuery but ignored this
    run (because they already exist). This is likely from a delay in mssql2bq
    sync of the UserBadges table.
    """
    return self._ignored_users

  @ignored_users.setter
  def ignored_users(self, ignored_users: Optional[List[int]]):
    if ignored_users is None:
      del self.ignored_users
      return
    if not isinstance(ignored_users, list):
      raise TypeError('ignored_users must be of type list')
    if not all([isinstance(t, int) for t in ignored_users]):
      raise TypeError('ignored_users must contain only items of type int')
    self._ignored_users = ignored_users

  @property
  def error_message(self) -> str:
    r"""
    A message if an error occured. If the error came from BigQuery, this will
    be the message returned by BigQuery.
    """
    return self._error_message

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class TestBigQueryBadgeRequest(KaggleObject):
  r"""
  Attributes:
    query_text (str)
      The query to test with, same format as what would be saved to the
      Badge.BadgeRecipientsQueryText.
  """

  def __init__(self):
    self._query_text = ""
    self._freeze()

  @property
  def query_text(self) -> str:
    r"""
    The query to test with, same format as what would be saved to the
    Badge.BadgeRecipientsQueryText.
    """
    return self._query_text

  @query_text.setter
  def query_text(self, query_text: str):
    if query_text is None:
      del self.query_text
      return
    if not isinstance(query_text, str):
      raise TypeError('query_text must be of type str')
    self._query_text = query_text


class TestBigQueryBadgeResponse(KaggleObject):
  r"""
  Attributes:
    row_count (int)
      The number of rows returned by the query (ie how many users would receive
      it).
    log_messages (str)
      A list of messages logged by the test.
    error_message (str)
      If an exception was thrown, the details of the exception.
  """

  def __init__(self):
    self._row_count = 0
    self._log_messages = []
    self._error_message = None
    self._freeze()

  @property
  def row_count(self) -> int:
    r"""
    The number of rows returned by the query (ie how many users would receive
    it).
    """
    return self._row_count

  @row_count.setter
  def row_count(self, row_count: int):
    if row_count is None:
      del self.row_count
      return
    if not isinstance(row_count, int):
      raise TypeError('row_count must be of type int')
    self._row_count = row_count

  @property
  def log_messages(self) -> Optional[List[str]]:
    """A list of messages logged by the test."""
    return self._log_messages

  @log_messages.setter
  def log_messages(self, log_messages: Optional[List[str]]):
    if log_messages is None:
      del self.log_messages
      return
    if not isinstance(log_messages, list):
      raise TypeError('log_messages must be of type list')
    if not all([isinstance(t, str) for t in log_messages]):
      raise TypeError('log_messages must contain only items of type str')
    self._log_messages = log_messages

  @property
  def error_message(self) -> str:
    """If an exception was thrown, the details of the exception."""
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class UpdateBadgeConfigRequest(KaggleObject):
  r"""
  Attributes:
    badge_config (BadgeConfig)
      The configuration to update.
    update_mask (FieldMask)
      A mask to selectively update fields.
  """

  def __init__(self):
    self._badge_config = None
    self._update_mask = None
    self._freeze()

  @property
  def badge_config(self) -> Optional['BadgeConfig']:
    """The configuration to update."""
    return self._badge_config

  @badge_config.setter
  def badge_config(self, badge_config: Optional['BadgeConfig']):
    if badge_config is None:
      del self.badge_config
      return
    if not isinstance(badge_config, BadgeConfig):
      raise TypeError('badge_config must be of type BadgeConfig')
    self._badge_config = badge_config

  @property
  def update_mask(self) -> FieldMask:
    """A mask to selectively update fields."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateBadgeRecipientRequest(KaggleObject):
  r"""
  Attributes:
    badge_id (int)
      The badge to update.
    badge_recipient (BadgeRecipient)
      The details to update.
    update_mask (FieldMask)
      A mask to selectively update fields.
  """

  def __init__(self):
    self._badge_id = 0
    self._badge_recipient = None
    self._update_mask = None
    self._freeze()

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
  def badge_recipient(self) -> Optional['BadgeRecipient']:
    """The details to update."""
    return self._badge_recipient

  @badge_recipient.setter
  def badge_recipient(self, badge_recipient: Optional['BadgeRecipient']):
    if badge_recipient is None:
      del self.badge_recipient
      return
    if not isinstance(badge_recipient, BadgeRecipient):
      raise TypeError('badge_recipient must be of type BadgeRecipient')
    self._badge_recipient = badge_recipient

  @property
  def update_mask(self) -> FieldMask:
    """A mask to selectively update fields."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


BadgeConfig._fields = [
  FieldMetadata("badgeDetails", "badge_details", "_badge_details", Badge, None, KaggleObjectSerializer()),
  FieldMetadata("customFieldName", "custom_field_name", "_custom_field_name", str, "", PredefinedSerializer()),
  FieldMetadata("hasCounter", "has_counter", "_has_counter", bool, False, PredefinedSerializer()),
  FieldMetadata("queryConfig", "query_config", "_query_config", QueryBadgeConfig, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("badgeState", "badge_state", "_badge_state", BadgeState, BadgeState.BADGE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("issuedCount", "issued_count", "_issued_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastIssuedTime", "last_issued_time", "_last_issued_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("sortKey", "sort_key", "_sort_key", float, 0.0, PredefinedSerializer()),
]

BadgeRecipientStatus._fields = [
  FieldMetadata("parsedUserName", "parsed_user_name", "_parsed_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("parsedAdditionalDetailsMarkdown", "parsed_additional_details_markdown", "_parsed_additional_details_markdown", str, "", PredefinedSerializer()),
  FieldMetadata("user", "user", "_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("existingAdditionalDetailsMarkdown", "existing_additional_details_markdown", "_existing_additional_details_markdown", str, None, PredefinedSerializer(), optional=True),
]

BadgeStats._fields = [
  FieldMetadata("createdBy", "created_by", "_created_by", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("issuedCount", "issued_count", "_issued_count", int, 0, PredefinedSerializer()),
  FieldMetadata("lastIssuedTime", "last_issued_time", "_last_issued_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("lastIssuedBy", "last_issued_by", "_last_issued_by", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("lastRuntimeDuration", "last_runtime_duration", "_last_runtime_duration", timedelta, None, TimeDeltaSerializer(), optional=True),
  FieldMetadata("lastRuntimeError", "last_runtime_error", "_last_runtime_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("issuedUserCount", "issued_user_count", "_issued_user_count", int, 0, PredefinedSerializer()),
]

BatchCreateBadgeRecipientsRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("requests", "requests", "_requests", CreateBadgeRecipientRequest, [], ListSerializer(KaggleObjectSerializer())),
]

BatchCreateBadgeRecipientsResponse._fields = [
  FieldMetadata("userBadges", "user_badges", "_user_badges", BadgeRecipient, [], ListSerializer(KaggleObjectSerializer())),
]

BatchDeleteBadgeRecipientsRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

CreateBadgeRecipientRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("badgeRecipient", "badge_recipient", "_badge_recipient", BadgeRecipient, None, KaggleObjectSerializer()),
]

DeleteBadgeConfigRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("badgeName", "badge_name", "_badge_name", str, "", PredefinedSerializer()),
]

GetBadgeConfigRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
]

GetBadgeRecipientsStatusRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userList", "user_list", "_user_list", str, "", PredefinedSerializer()),
]

GetBadgeRecipientsStatusResponse._fields = [
  FieldMetadata("matchedNewUsers", "matched_new_users", "_matched_new_users", BadgeRecipientStatus, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("matchedExistingUsers", "matched_existing_users", "_matched_existing_users", BadgeRecipientStatus, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("unmatchedUsers", "unmatched_users", "_unmatched_users", BadgeRecipientStatus, [], ListSerializer(KaggleObjectSerializer())),
]

GetBadgeStatsRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
]

ListBadgeConfigsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", ListBadgeConfigsSortOptions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", BadgeType, None, EnumSerializer(), optional=True),
  FieldMetadata("nameFilter", "name_filter", "_name_filter", str, None, PredefinedSerializer(), optional=True),
]

ListBadgeConfigsResponse._fields = [
  FieldMetadata("badges", "badges", "_badges", BadgeConfig, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

ListBadgeConfigsSortOptions._fields = [
  FieldMetadata("column", "column", "_column", ListBadgeConfigsSortColumn, ListBadgeConfigsSortColumn.LIST_BADGE_CONFIGS_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("descending", "descending", "_descending", bool, False, PredefinedSerializer()),
]

QueryBadgeConfig._fields = [
  FieldMetadata("badgeRecipientsQueryText", "badge_recipients_query_text", "_badge_recipients_query_text", str, "", PredefinedSerializer()),
  FieldMetadata("badgeRefreshQueryText", "badge_refresh_query_text", "_badge_refresh_query_text", str, None, PredefinedSerializer(), optional=True),
]

SyncBigQueryBadgeRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("maxSize", "max_size", "_max_size", int, 0, PredefinedSerializer()),
  FieldMetadata("afterUserId", "after_user_id", "_after_user_id", int, 0, PredefinedSerializer()),
]

SyncBigQueryBadgeResponse._fields = [
  FieldMetadata("newUsers", "new_users", "_new_users", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("updatedUsers", "updated_users", "_updated_users", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("ignoredUsers", "ignored_users", "_ignored_users", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
]

TestBigQueryBadgeRequest._fields = [
  FieldMetadata("queryText", "query_text", "_query_text", str, "", PredefinedSerializer()),
]

TestBigQueryBadgeResponse._fields = [
  FieldMetadata("rowCount", "row_count", "_row_count", int, 0, PredefinedSerializer()),
  FieldMetadata("logMessages", "log_messages", "_log_messages", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

UpdateBadgeConfigRequest._fields = [
  FieldMetadata("badgeConfig", "badge_config", "_badge_config", BadgeConfig, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateBadgeRecipientRequest._fields = [
  FieldMetadata("badgeId", "badge_id", "_badge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("badgeRecipient", "badge_recipient", "_badge_recipient", BadgeRecipient, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

