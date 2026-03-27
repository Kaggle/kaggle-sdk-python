import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from kagglesdk.notifications.types.notifications_enums import NotificationType
from kagglesdk.notifications.types.notifications_types import Notification, UserNotificationSettings
from typing import Optional, List

class CommandMark(enum.Enum):
  READ = 0
  VIEWED = 1

class NotificationOpenAction(enum.Enum):
  NO_ACTION = 0
  UPVOTE = 1
  DOWNVOTE = 2

class AddTestNotificationRequest(KaggleObject):
  r"""
  Attributes:
    notification_type (NotificationType)
      What notification type do you want for the notification to be added?
      Not all notification types are currently supported
    variant (int)
      for the notification type specified, there are pre-made notifications -
      which one of those do you want? Not all types have variants - simply
      specify 0 for them the invoking user must have permission to the any
      objects (dataset/comp/etc) mentioned in the variant
    send_email (bool)
      By default the notification will be sent to the invoking user as a web
      notification, when send_email is true, it will also be sent as an email to
      the invoking user.
  """

  def __init__(self):
    self._notification_type = NotificationType.NOTIFICATION_TYPE_UNSPECIFIED
    self._variant = 0
    self._send_email = False
    self._freeze()

  @property
  def notification_type(self) -> 'NotificationType':
    r"""
    What notification type do you want for the notification to be added?
    Not all notification types are currently supported
    """
    return self._notification_type

  @notification_type.setter
  def notification_type(self, notification_type: 'NotificationType'):
    if notification_type is None:
      del self.notification_type
      return
    if not isinstance(notification_type, NotificationType):
      raise TypeError('notification_type must be of type NotificationType')
    self._notification_type = notification_type

  @property
  def variant(self) -> int:
    r"""
    for the notification type specified, there are pre-made notifications -
    which one of those do you want? Not all types have variants - simply
    specify 0 for them the invoking user must have permission to the any
    objects (dataset/comp/etc) mentioned in the variant
    """
    return self._variant

  @variant.setter
  def variant(self, variant: int):
    if variant is None:
      del self.variant
      return
    if not isinstance(variant, int):
      raise TypeError('variant must be of type int')
    self._variant = variant

  @property
  def send_email(self) -> bool:
    r"""
    By default the notification will be sent to the invoking user as a web
    notification, when send_email is true, it will also be sent as an email to
    the invoking user.
    """
    return self._send_email

  @send_email.setter
  def send_email(self, send_email: bool):
    if send_email is None:
      del self.send_email
      return
    if not isinstance(send_email, bool):
      raise TypeError('send_email must be of type bool')
    self._send_email = send_email


class AddTestNotificationResponse(KaggleObject):
  r"""
  Attributes:
    notification_id (int)
      id of the notification that was created
    emails_processed_count (int)
      the number of emails that we attempted to send - does not always succeed.
  """

  def __init__(self):
    self._notification_id = 0
    self._emails_processed_count = 0
    self._freeze()

  @property
  def notification_id(self) -> int:
    """id of the notification that was created"""
    return self._notification_id

  @notification_id.setter
  def notification_id(self, notification_id: int):
    if notification_id is None:
      del self.notification_id
      return
    if not isinstance(notification_id, int):
      raise TypeError('notification_id must be of type int')
    self._notification_id = notification_id

  @property
  def emails_processed_count(self) -> int:
    """the number of emails that we attempted to send - does not always succeed."""
    return self._emails_processed_count

  @emails_processed_count.setter
  def emails_processed_count(self, emails_processed_count: int):
    if emails_processed_count is None:
      del self.emails_processed_count
      return
    if not isinstance(emails_processed_count, int):
      raise TypeError('emails_processed_count must be of type int')
    self._emails_processed_count = emails_processed_count


class GetUserNotificationSettingsRequest(KaggleObject):
  r"""
  """

  pass

class GetUserNotificationSettingsResponse(KaggleObject):
  r"""
  Attributes:
    settings (UserNotificationSettings)
      The user's current notification settings.
  """

  def __init__(self):
    self._settings = None
    self._freeze()

  @property
  def settings(self) -> Optional['UserNotificationSettings']:
    """The user's current notification settings."""
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['UserNotificationSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, UserNotificationSettings):
      raise TypeError('settings must be of type UserNotificationSettings')
    self._settings = settings


class GetUserNotificationsRequest(KaggleObject):
  r"""
  Attributes:
    after_notification_id (int)
      Notification Id used for pagination. Will grab the notifications after this
      id
    page_size (int)
      The number of notifications to retrieve, for pagination
    cached_notification_id (int)
      The newest Id that the client has already cached. If there aren't newer
      notifications than this, then the server will skip loading notifications.
      It will still load the unviewed count as that can change.
  """

  def __init__(self):
    self._after_notification_id = None
    self._page_size = 0
    self._cached_notification_id = None
    self._freeze()

  @property
  def after_notification_id(self) -> int:
    r"""
    Notification Id used for pagination. Will grab the notifications after this
    id
    """
    return self._after_notification_id or 0

  @after_notification_id.setter
  def after_notification_id(self, after_notification_id: Optional[int]):
    if after_notification_id is None:
      del self.after_notification_id
      return
    if not isinstance(after_notification_id, int):
      raise TypeError('after_notification_id must be of type int')
    self._after_notification_id = after_notification_id

  @property
  def page_size(self) -> int:
    """The number of notifications to retrieve, for pagination"""
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
  def cached_notification_id(self) -> int:
    r"""
    The newest Id that the client has already cached. If there aren't newer
    notifications than this, then the server will skip loading notifications.
    It will still load the unviewed count as that can change.
    """
    return self._cached_notification_id or 0

  @cached_notification_id.setter
  def cached_notification_id(self, cached_notification_id: Optional[int]):
    if cached_notification_id is None:
      del self.cached_notification_id
      return
    if not isinstance(cached_notification_id, int):
      raise TypeError('cached_notification_id must be of type int')
    self._cached_notification_id = cached_notification_id


class GetUserNotificationsResponse(KaggleObject):
  r"""
  Attributes:
    contains_more (bool)
    enabled (bool)
    count_unviewed (int)
    notifications (Notification)
    newest_notification_id (int)
    cache_is_valid (bool)
  """

  def __init__(self):
    self._contains_more = False
    self._enabled = False
    self._count_unviewed = 0
    self._notifications = []
    self._newest_notification_id = 0
    self._cache_is_valid = False
    self._freeze()

  @property
  def contains_more(self) -> bool:
    return self._contains_more

  @contains_more.setter
  def contains_more(self, contains_more: bool):
    if contains_more is None:
      del self.contains_more
      return
    if not isinstance(contains_more, bool):
      raise TypeError('contains_more must be of type bool')
    self._contains_more = contains_more

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
  def count_unviewed(self) -> int:
    return self._count_unviewed

  @count_unviewed.setter
  def count_unviewed(self, count_unviewed: int):
    if count_unviewed is None:
      del self.count_unviewed
      return
    if not isinstance(count_unviewed, int):
      raise TypeError('count_unviewed must be of type int')
    self._count_unviewed = count_unviewed

  @property
  def notifications(self) -> Optional[List[Optional['Notification']]]:
    return self._notifications

  @notifications.setter
  def notifications(self, notifications: Optional[List[Optional['Notification']]]):
    if notifications is None:
      del self.notifications
      return
    if not isinstance(notifications, list):
      raise TypeError('notifications must be of type list')
    if not all([isinstance(t, Notification) for t in notifications]):
      raise TypeError('notifications must contain only items of type Notification')
    self._notifications = notifications

  @property
  def newest_notification_id(self) -> int:
    return self._newest_notification_id

  @newest_notification_id.setter
  def newest_notification_id(self, newest_notification_id: int):
    if newest_notification_id is None:
      del self.newest_notification_id
      return
    if not isinstance(newest_notification_id, int):
      raise TypeError('newest_notification_id must be of type int')
    self._newest_notification_id = newest_notification_id

  @property
  def cache_is_valid(self) -> bool:
    return self._cache_is_valid

  @cache_is_valid.setter
  def cache_is_valid(self, cache_is_valid: bool):
    if cache_is_valid is None:
      del self.cache_is_valid
      return
    if not isinstance(cache_is_valid, bool):
      raise TypeError('cache_is_valid must be of type bool')
    self._cache_is_valid = cache_is_valid


class MarkAllNotificationsRequest(KaggleObject):
  r"""
  Attributes:
    newest_notification_id (int)
    command_mark (CommandMark)
  """

  def __init__(self):
    self._newest_notification_id = 0
    self._command_mark = CommandMark.READ
    self._freeze()

  @property
  def newest_notification_id(self) -> int:
    return self._newest_notification_id

  @newest_notification_id.setter
  def newest_notification_id(self, newest_notification_id: int):
    if newest_notification_id is None:
      del self.newest_notification_id
      return
    if not isinstance(newest_notification_id, int):
      raise TypeError('newest_notification_id must be of type int')
    self._newest_notification_id = newest_notification_id

  @property
  def command_mark(self) -> 'CommandMark':
    return self._command_mark

  @command_mark.setter
  def command_mark(self, command_mark: 'CommandMark'):
    if command_mark is None:
      del self.command_mark
      return
    if not isinstance(command_mark, CommandMark):
      raise TypeError('command_mark must be of type CommandMark')
    self._command_mark = command_mark


class MarkNotificationsRequest(KaggleObject):
  r"""
  Attributes:
    single_notification_id (int)
      when you want to change a single notification's status, set this field
    newest_notification_id (int)
      setting this field will mark all notification ids <= this id
    mark_viewed (bool)
      set to true when you want the DatedViewed set on the notification
    mark_read (bool)
      set to true when you want the DateRead set on the notification
  """

  def __init__(self):
    self._single_notification_id = None
    self._newest_notification_id = None
    self._mark_viewed = False
    self._mark_read = False
    self._freeze()

  @property
  def single_notification_id(self) -> int:
    """when you want to change a single notification's status, set this field"""
    return self._single_notification_id or 0

  @single_notification_id.setter
  def single_notification_id(self, single_notification_id: int):
    if single_notification_id is None:
      del self.single_notification_id
      return
    if not isinstance(single_notification_id, int):
      raise TypeError('single_notification_id must be of type int')
    del self.newest_notification_id
    self._single_notification_id = single_notification_id

  @property
  def newest_notification_id(self) -> int:
    """setting this field will mark all notification ids <= this id"""
    return self._newest_notification_id or 0

  @newest_notification_id.setter
  def newest_notification_id(self, newest_notification_id: int):
    if newest_notification_id is None:
      del self.newest_notification_id
      return
    if not isinstance(newest_notification_id, int):
      raise TypeError('newest_notification_id must be of type int')
    del self.single_notification_id
    self._newest_notification_id = newest_notification_id

  @property
  def mark_viewed(self) -> bool:
    """set to true when you want the DatedViewed set on the notification"""
    return self._mark_viewed

  @mark_viewed.setter
  def mark_viewed(self, mark_viewed: bool):
    if mark_viewed is None:
      del self.mark_viewed
      return
    if not isinstance(mark_viewed, bool):
      raise TypeError('mark_viewed must be of type bool')
    self._mark_viewed = mark_viewed

  @property
  def mark_read(self) -> bool:
    """set to true when you want the DateRead set on the notification"""
    return self._mark_read

  @mark_read.setter
  def mark_read(self, mark_read: bool):
    if mark_read is None:
      del self.mark_read
      return
    if not isinstance(mark_read, bool):
      raise TypeError('mark_read must be of type bool')
    self._mark_read = mark_read


class OpenNotificationRequest(KaggleObject):
  r"""
  Attributes:
    notification_id (int)
      The id of the notification to open.
    token (str)
      The open token for the notification, this allows the user to act upon a
      notification. Without this token a link may have been generated by a
      malicious user (e.g. to gather upvotes).
    from_email (bool)
      Whether or not this link was opened via email.
    notification_action (NotificationOpenAction)
      The action that should be taken (e.g. upvote).
    target_url (str)
      The target url that the user will end up going to.
  """

  def __init__(self):
    self._notification_id = 0
    self._token = None
    self._from_email = False
    self._notification_action = NotificationOpenAction.NO_ACTION
    self._target_url = None
    self._freeze()

  @property
  def notification_id(self) -> int:
    """The id of the notification to open."""
    return self._notification_id

  @notification_id.setter
  def notification_id(self, notification_id: int):
    if notification_id is None:
      del self.notification_id
      return
    if not isinstance(notification_id, int):
      raise TypeError('notification_id must be of type int')
    self._notification_id = notification_id

  @property
  def token(self) -> str:
    r"""
    The open token for the notification, this allows the user to act upon a
    notification. Without this token a link may have been generated by a
    malicious user (e.g. to gather upvotes).
    """
    return self._token or ""

  @token.setter
  def token(self, token: Optional[str]):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def from_email(self) -> bool:
    """Whether or not this link was opened via email."""
    return self._from_email

  @from_email.setter
  def from_email(self, from_email: bool):
    if from_email is None:
      del self.from_email
      return
    if not isinstance(from_email, bool):
      raise TypeError('from_email must be of type bool')
    self._from_email = from_email

  @property
  def notification_action(self) -> 'NotificationOpenAction':
    """The action that should be taken (e.g. upvote)."""
    return self._notification_action

  @notification_action.setter
  def notification_action(self, notification_action: 'NotificationOpenAction'):
    if notification_action is None:
      del self.notification_action
      return
    if not isinstance(notification_action, NotificationOpenAction):
      raise TypeError('notification_action must be of type NotificationOpenAction')
    self._notification_action = notification_action

  @property
  def target_url(self) -> str:
    """The target url that the user will end up going to."""
    return self._target_url or ""

  @target_url.setter
  def target_url(self, target_url: Optional[str]):
    if target_url is None:
      del self.target_url
      return
    if not isinstance(target_url, str):
      raise TypeError('target_url must be of type str')
    self._target_url = target_url


class SetUserNotificationSettingsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user who's settings are being set. This must be the current user unless
      the current user is an admin.
    settings (UserNotificationSettings)
      The settings to update to.
    update_mask (FieldMask)
      Which fields are being passed in to be set. If you don't pass this, then
      all fields will be updated.
  """

  def __init__(self):
    self._user_id = 0
    self._settings = None
    self._update_mask = None
    self._freeze()

  @property
  def user_id(self) -> int:
    r"""
    The user who's settings are being set. This must be the current user unless
    the current user is an admin.
    """
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
  def settings(self) -> Optional['UserNotificationSettings']:
    """The settings to update to."""
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['UserNotificationSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, UserNotificationSettings):
      raise TypeError('settings must be of type UserNotificationSettings')
    self._settings = settings

  @property
  def update_mask(self) -> FieldMask:
    r"""
    Which fields are being passed in to be set. If you don't pass this, then
    all fields will be updated.
    """
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class TimeTaken(KaggleObject):
  r"""
  Attributes:
    notification_id (int)
      Which notification this timing is for.
    query_time_milliseconds (int)
      How long it took to query for it (find one to process).
    mark_time_milliseconds (int)
      How long it took to mark it as sent (done before processing to prevent race
      conditions).
    load_time_milliseconds (int)
      How long it took to load all the details for it.
    process_time_milliseconds (int)
      How long it took to process the notification (render it etc).
    send_time_milliseconds (int)
      How long it took to queue it to send.
    log_time_milliseconds (int)
      How long it took to log it as being sent (in notification history DB
      table).
    total_time_milliseconds (int)
      How long the entire process took.
  """

  def __init__(self):
    self._notification_id = 0
    self._query_time_milliseconds = None
    self._mark_time_milliseconds = None
    self._load_time_milliseconds = None
    self._process_time_milliseconds = None
    self._send_time_milliseconds = None
    self._log_time_milliseconds = None
    self._total_time_milliseconds = 0
    self._freeze()

  @property
  def notification_id(self) -> int:
    """Which notification this timing is for."""
    return self._notification_id

  @notification_id.setter
  def notification_id(self, notification_id: int):
    if notification_id is None:
      del self.notification_id
      return
    if not isinstance(notification_id, int):
      raise TypeError('notification_id must be of type int')
    self._notification_id = notification_id

  @property
  def query_time_milliseconds(self) -> int:
    """How long it took to query for it (find one to process)."""
    return self._query_time_milliseconds or 0

  @query_time_milliseconds.setter
  def query_time_milliseconds(self, query_time_milliseconds: Optional[int]):
    if query_time_milliseconds is None:
      del self.query_time_milliseconds
      return
    if not isinstance(query_time_milliseconds, int):
      raise TypeError('query_time_milliseconds must be of type int')
    self._query_time_milliseconds = query_time_milliseconds

  @property
  def mark_time_milliseconds(self) -> int:
    r"""
    How long it took to mark it as sent (done before processing to prevent race
    conditions).
    """
    return self._mark_time_milliseconds or 0

  @mark_time_milliseconds.setter
  def mark_time_milliseconds(self, mark_time_milliseconds: Optional[int]):
    if mark_time_milliseconds is None:
      del self.mark_time_milliseconds
      return
    if not isinstance(mark_time_milliseconds, int):
      raise TypeError('mark_time_milliseconds must be of type int')
    self._mark_time_milliseconds = mark_time_milliseconds

  @property
  def load_time_milliseconds(self) -> int:
    """How long it took to load all the details for it."""
    return self._load_time_milliseconds or 0

  @load_time_milliseconds.setter
  def load_time_milliseconds(self, load_time_milliseconds: Optional[int]):
    if load_time_milliseconds is None:
      del self.load_time_milliseconds
      return
    if not isinstance(load_time_milliseconds, int):
      raise TypeError('load_time_milliseconds must be of type int')
    self._load_time_milliseconds = load_time_milliseconds

  @property
  def process_time_milliseconds(self) -> int:
    """How long it took to process the notification (render it etc)."""
    return self._process_time_milliseconds or 0

  @process_time_milliseconds.setter
  def process_time_milliseconds(self, process_time_milliseconds: Optional[int]):
    if process_time_milliseconds is None:
      del self.process_time_milliseconds
      return
    if not isinstance(process_time_milliseconds, int):
      raise TypeError('process_time_milliseconds must be of type int')
    self._process_time_milliseconds = process_time_milliseconds

  @property
  def send_time_milliseconds(self) -> int:
    """How long it took to queue it to send."""
    return self._send_time_milliseconds or 0

  @send_time_milliseconds.setter
  def send_time_milliseconds(self, send_time_milliseconds: Optional[int]):
    if send_time_milliseconds is None:
      del self.send_time_milliseconds
      return
    if not isinstance(send_time_milliseconds, int):
      raise TypeError('send_time_milliseconds must be of type int')
    self._send_time_milliseconds = send_time_milliseconds

  @property
  def log_time_milliseconds(self) -> int:
    r"""
    How long it took to log it as being sent (in notification history DB
    table).
    """
    return self._log_time_milliseconds or 0

  @log_time_milliseconds.setter
  def log_time_milliseconds(self, log_time_milliseconds: Optional[int]):
    if log_time_milliseconds is None:
      del self.log_time_milliseconds
      return
    if not isinstance(log_time_milliseconds, int):
      raise TypeError('log_time_milliseconds must be of type int')
    self._log_time_milliseconds = log_time_milliseconds

  @property
  def total_time_milliseconds(self) -> int:
    """How long the entire process took."""
    return self._total_time_milliseconds

  @total_time_milliseconds.setter
  def total_time_milliseconds(self, total_time_milliseconds: int):
    if total_time_milliseconds is None:
      del self.total_time_milliseconds
      return
    if not isinstance(total_time_milliseconds, int):
      raise TypeError('total_time_milliseconds must be of type int')
    self._total_time_milliseconds = total_time_milliseconds


AddTestNotificationRequest._fields = [
  FieldMetadata("notificationType", "notification_type", "_notification_type", NotificationType, NotificationType.NOTIFICATION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("variant", "variant", "_variant", int, 0, PredefinedSerializer()),
  FieldMetadata("sendEmail", "send_email", "_send_email", bool, False, PredefinedSerializer()),
]

AddTestNotificationResponse._fields = [
  FieldMetadata("notificationId", "notification_id", "_notification_id", int, 0, PredefinedSerializer()),
  FieldMetadata("emailsProcessedCount", "emails_processed_count", "_emails_processed_count", int, 0, PredefinedSerializer()),
]

GetUserNotificationSettingsRequest._fields = []

GetUserNotificationSettingsResponse._fields = [
  FieldMetadata("settings", "settings", "_settings", UserNotificationSettings, None, KaggleObjectSerializer()),
]

GetUserNotificationsRequest._fields = [
  FieldMetadata("afterNotificationId", "after_notification_id", "_after_notification_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("cachedNotificationId", "cached_notification_id", "_cached_notification_id", int, None, PredefinedSerializer(), optional=True),
]

GetUserNotificationsResponse._fields = [
  FieldMetadata("containsMore", "contains_more", "_contains_more", bool, False, PredefinedSerializer()),
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("countUnviewed", "count_unviewed", "_count_unviewed", int, 0, PredefinedSerializer()),
  FieldMetadata("notifications", "notifications", "_notifications", Notification, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("newestNotificationId", "newest_notification_id", "_newest_notification_id", int, 0, PredefinedSerializer()),
  FieldMetadata("cacheIsValid", "cache_is_valid", "_cache_is_valid", bool, False, PredefinedSerializer()),
]

MarkAllNotificationsRequest._fields = [
  FieldMetadata("newestNotificationId", "newest_notification_id", "_newest_notification_id", int, 0, PredefinedSerializer()),
  FieldMetadata("commandMark", "command_mark", "_command_mark", CommandMark, CommandMark.READ, EnumSerializer()),
]

MarkNotificationsRequest._fields = [
  FieldMetadata("singleNotificationId", "single_notification_id", "_single_notification_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newestNotificationId", "newest_notification_id", "_newest_notification_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("markViewed", "mark_viewed", "_mark_viewed", bool, False, PredefinedSerializer()),
  FieldMetadata("markRead", "mark_read", "_mark_read", bool, False, PredefinedSerializer()),
]

OpenNotificationRequest._fields = [
  FieldMetadata("notificationId", "notification_id", "_notification_id", int, 0, PredefinedSerializer()),
  FieldMetadata("token", "token", "_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fromEmail", "from_email", "_from_email", bool, False, PredefinedSerializer()),
  FieldMetadata("notificationAction", "notification_action", "_notification_action", NotificationOpenAction, NotificationOpenAction.NO_ACTION, EnumSerializer()),
  FieldMetadata("targetUrl", "target_url", "_target_url", str, None, PredefinedSerializer(), optional=True),
]

SetUserNotificationSettingsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", UserNotificationSettings, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

TimeTaken._fields = [
  FieldMetadata("notificationId", "notification_id", "_notification_id", int, 0, PredefinedSerializer()),
  FieldMetadata("queryTimeMilliseconds", "query_time_milliseconds", "_query_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("markTimeMilliseconds", "mark_time_milliseconds", "_mark_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("loadTimeMilliseconds", "load_time_milliseconds", "_load_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("processTimeMilliseconds", "process_time_milliseconds", "_process_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sendTimeMilliseconds", "send_time_milliseconds", "_send_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("logTimeMilliseconds", "log_time_milliseconds", "_log_time_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalTimeMilliseconds", "total_time_milliseconds", "_total_time_milliseconds", int, 0, PredefinedSerializer()),
]

