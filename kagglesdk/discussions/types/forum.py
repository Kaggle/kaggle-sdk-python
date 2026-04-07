from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.notifications.types.notifications_enums import SubscribeState
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class Forum(KaggleObject):
  r"""
  Attributes:
    allow_attachments (bool)
    current_user_can_downvote (bool)
    current_user_tier (UserAchievementTier)
    id (int)
    image_url (str)
    is_private (bool)
    last_post_date (datetime)
    last_post_url (str)
    name (str)
    subscription_state (SubscribeState)
    subtitle (str)
    url (str)
    has_unread_topics (bool)
    recent_authors (UserAvatar)
    last_post_user (UserAvatar)
    global_notifications_enabled (bool)
    current_user_can_create_topics (bool)
  """

  def __init__(self):
    self._allow_attachments = False
    self._current_user_can_downvote = False
    self._current_user_tier = UserAchievementTier.NOVICE
    self._id = None
    self._image_url = None
    self._is_private = False
    self._last_post_date = None
    self._last_post_url = None
    self._name = None
    self._subscription_state = SubscribeState.INVALID
    self._subtitle = None
    self._url = None
    self._has_unread_topics = False
    self._recent_authors = []
    self._last_post_user = None
    self._global_notifications_enabled = False
    self._current_user_can_create_topics = False
    self._freeze()

  @property
  def allow_attachments(self) -> bool:
    return self._allow_attachments

  @allow_attachments.setter
  def allow_attachments(self, allow_attachments: bool):
    if allow_attachments is None:
      del self.allow_attachments
      return
    if not isinstance(allow_attachments, bool):
      raise TypeError('allow_attachments must be of type bool')
    self._allow_attachments = allow_attachments

  @property
  def current_user_can_downvote(self) -> bool:
    return self._current_user_can_downvote

  @current_user_can_downvote.setter
  def current_user_can_downvote(self, current_user_can_downvote: bool):
    if current_user_can_downvote is None:
      del self.current_user_can_downvote
      return
    if not isinstance(current_user_can_downvote, bool):
      raise TypeError('current_user_can_downvote must be of type bool')
    self._current_user_can_downvote = current_user_can_downvote

  @property
  def current_user_tier(self) -> 'UserAchievementTier':
    return self._current_user_tier

  @current_user_tier.setter
  def current_user_tier(self, current_user_tier: 'UserAchievementTier'):
    if current_user_tier is None:
      del self.current_user_tier
      return
    if not isinstance(current_user_tier, UserAchievementTier):
      raise TypeError('current_user_tier must be of type UserAchievementTier')
    self._current_user_tier = current_user_tier

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def last_post_date(self) -> datetime:
    return self._last_post_date

  @last_post_date.setter
  def last_post_date(self, last_post_date: datetime):
    if last_post_date is None:
      del self.last_post_date
      return
    if not isinstance(last_post_date, datetime):
      raise TypeError('last_post_date must be of type datetime')
    self._last_post_date = last_post_date

  @property
  def last_post_url(self) -> str:
    return self._last_post_url or ""

  @last_post_url.setter
  def last_post_url(self, last_post_url: Optional[str]):
    if last_post_url is None:
      del self.last_post_url
      return
    if not isinstance(last_post_url, str):
      raise TypeError('last_post_url must be of type str')
    self._last_post_url = last_post_url

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def subscription_state(self) -> 'SubscribeState':
    return self._subscription_state

  @subscription_state.setter
  def subscription_state(self, subscription_state: 'SubscribeState'):
    if subscription_state is None:
      del self.subscription_state
      return
    if not isinstance(subscription_state, SubscribeState):
      raise TypeError('subscription_state must be of type SubscribeState')
    self._subscription_state = subscription_state

  @property
  def global_notifications_enabled(self) -> bool:
    return self._global_notifications_enabled

  @global_notifications_enabled.setter
  def global_notifications_enabled(self, global_notifications_enabled: bool):
    if global_notifications_enabled is None:
      del self.global_notifications_enabled
      return
    if not isinstance(global_notifications_enabled, bool):
      raise TypeError('global_notifications_enabled must be of type bool')
    self._global_notifications_enabled = global_notifications_enabled

  @property
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def has_unread_topics(self) -> bool:
    return self._has_unread_topics

  @has_unread_topics.setter
  def has_unread_topics(self, has_unread_topics: bool):
    if has_unread_topics is None:
      del self.has_unread_topics
      return
    if not isinstance(has_unread_topics, bool):
      raise TypeError('has_unread_topics must be of type bool')
    self._has_unread_topics = has_unread_topics

  @property
  def recent_authors(self) -> Optional[List[Optional['UserAvatar']]]:
    return self._recent_authors

  @recent_authors.setter
  def recent_authors(self, recent_authors: Optional[List[Optional['UserAvatar']]]):
    if recent_authors is None:
      del self.recent_authors
      return
    if not isinstance(recent_authors, list):
      raise TypeError('recent_authors must be of type list')
    if not all([isinstance(t, UserAvatar) for t in recent_authors]):
      raise TypeError('recent_authors must contain only items of type UserAvatar')
    self._recent_authors = recent_authors

  @property
  def last_post_user(self) -> Optional['UserAvatar']:
    return self._last_post_user

  @last_post_user.setter
  def last_post_user(self, last_post_user: Optional['UserAvatar']):
    if last_post_user is None:
      del self.last_post_user
      return
    if not isinstance(last_post_user, UserAvatar):
      raise TypeError('last_post_user must be of type UserAvatar')
    self._last_post_user = last_post_user

  @property
  def current_user_can_create_topics(self) -> bool:
    return self._current_user_can_create_topics

  @current_user_can_create_topics.setter
  def current_user_can_create_topics(self, current_user_can_create_topics: bool):
    if current_user_can_create_topics is None:
      del self.current_user_can_create_topics
      return
    if not isinstance(current_user_can_create_topics, bool):
      raise TypeError('current_user_can_create_topics must be of type bool')
    self._current_user_can_create_topics = current_user_can_create_topics


Forum._fields = [
  FieldMetadata("allowAttachments", "allow_attachments", "_allow_attachments", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserCanDownvote", "current_user_can_downvote", "_current_user_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserTier", "current_user_tier", "_current_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("lastPostDate", "last_post_date", "_last_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastPostUrl", "last_post_url", "_last_post_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subscriptionState", "subscription_state", "_subscription_state", SubscribeState, SubscribeState.INVALID, EnumSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasUnreadTopics", "has_unread_topics", "_has_unread_topics", bool, False, PredefinedSerializer()),
  FieldMetadata("recentAuthors", "recent_authors", "_recent_authors", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("lastPostUser", "last_post_user", "_last_post_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("globalNotificationsEnabled", "global_notifications_enabled", "_global_notifications_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserCanCreateTopics", "current_user_can_create_topics", "_current_user_can_create_topics", bool, False, PredefinedSerializer()),
]

