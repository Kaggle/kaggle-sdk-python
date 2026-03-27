from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.notifications.types.notifications_enums import NotificationAggregationOption, NotificationDeliveryType, NotificationRelatedItemType, SubscriptionType
from typing import Optional, List

class MessageObject(KaggleObject):
  r"""
  Attributes:
    key (str)
    text (str)
    url (str)
  """

  def __init__(self):
    self._key = None
    self._text = None
    self._url = None
    self._freeze()

  @property
  def key(self) -> str:
    return self._key or ""

  @key.setter
  def key(self, key: Optional[str]):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def text(self) -> str:
    return self._text or ""

  @text.setter
  def text(self, text: Optional[str]):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

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


class Notification(KaggleObject):
  r"""
  Attributes:
    id (int)
    subscription_type (SubscriptionType)
    related_item_id (int)
    related_item_type (NotificationRelatedItemType)
    is_read (bool)
    is_viewed (bool)
    created_date (datetime)
    image_url (str)
    image_href (str)
    message_format (str)
    message_objects (MessageObject)
    title (str)
    message (str)
    bundle_count (int)
      if non-null, this indicates that the notification represents a bundle of
      notifications the count is the number of notifications in the bundle. Value
      will never be 0 or 1.
    message_preview (str)
      The following fields are only defined for emails or summary/full views
    action_url (str)
    upvote_url (str)
    downvote_url (str)
    vote_count (int)
    medal_url (str)
  """

  def __init__(self):
    self._id = 0
    self._subscription_type = SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE
    self._related_item_id = 0
    self._related_item_type = NotificationRelatedItemType.NOTIFICATION_RELATED_ITEM_TYPE_UNSPECIFIED
    self._is_read = False
    self._is_viewed = False
    self._created_date = None
    self._image_url = None
    self._image_href = None
    self._message_format = None
    self._message_objects = []
    self._title = None
    self._message = None
    self._bundle_count = None
    self._message_preview = None
    self._action_url = None
    self._upvote_url = None
    self._downvote_url = None
    self._vote_count = None
    self._medal_url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def subscription_type(self) -> 'SubscriptionType':
    return self._subscription_type

  @subscription_type.setter
  def subscription_type(self, subscription_type: 'SubscriptionType'):
    if subscription_type is None:
      del self.subscription_type
      return
    if not isinstance(subscription_type, SubscriptionType):
      raise TypeError('subscription_type must be of type SubscriptionType')
    self._subscription_type = subscription_type

  @property
  def related_item_id(self) -> int:
    return self._related_item_id

  @related_item_id.setter
  def related_item_id(self, related_item_id: int):
    if related_item_id is None:
      del self.related_item_id
      return
    if not isinstance(related_item_id, int):
      raise TypeError('related_item_id must be of type int')
    self._related_item_id = related_item_id

  @property
  def related_item_type(self) -> 'NotificationRelatedItemType':
    return self._related_item_type

  @related_item_type.setter
  def related_item_type(self, related_item_type: 'NotificationRelatedItemType'):
    if related_item_type is None:
      del self.related_item_type
      return
    if not isinstance(related_item_type, NotificationRelatedItemType):
      raise TypeError('related_item_type must be of type NotificationRelatedItemType')
    self._related_item_type = related_item_type

  @property
  def is_read(self) -> bool:
    return self._is_read

  @is_read.setter
  def is_read(self, is_read: bool):
    if is_read is None:
      del self.is_read
      return
    if not isinstance(is_read, bool):
      raise TypeError('is_read must be of type bool')
    self._is_read = is_read

  @property
  def is_viewed(self) -> bool:
    return self._is_viewed

  @is_viewed.setter
  def is_viewed(self, is_viewed: bool):
    if is_viewed is None:
      del self.is_viewed
      return
    if not isinstance(is_viewed, bool):
      raise TypeError('is_viewed must be of type bool')
    self._is_viewed = is_viewed

  @property
  def created_date(self) -> datetime:
    return self._created_date

  @created_date.setter
  def created_date(self, created_date: datetime):
    if created_date is None:
      del self.created_date
      return
    if not isinstance(created_date, datetime):
      raise TypeError('created_date must be of type datetime')
    self._created_date = created_date

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
  def image_href(self) -> str:
    return self._image_href or ""

  @image_href.setter
  def image_href(self, image_href: Optional[str]):
    if image_href is None:
      del self.image_href
      return
    if not isinstance(image_href, str):
      raise TypeError('image_href must be of type str')
    self._image_href = image_href

  @property
  def message_format(self) -> str:
    return self._message_format or ""

  @message_format.setter
  def message_format(self, message_format: Optional[str]):
    if message_format is None:
      del self.message_format
      return
    if not isinstance(message_format, str):
      raise TypeError('message_format must be of type str')
    self._message_format = message_format

  @property
  def message_objects(self) -> Optional[List[Optional['MessageObject']]]:
    return self._message_objects

  @message_objects.setter
  def message_objects(self, message_objects: Optional[List[Optional['MessageObject']]]):
    if message_objects is None:
      del self.message_objects
      return
    if not isinstance(message_objects, list):
      raise TypeError('message_objects must be of type list')
    if not all([isinstance(t, MessageObject) for t in message_objects]):
      raise TypeError('message_objects must contain only items of type MessageObject')
    self._message_objects = message_objects

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def message(self) -> str:
    return self._message or ""

  @message.setter
  def message(self, message: Optional[str]):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def bundle_count(self) -> int:
    r"""
    if non-null, this indicates that the notification represents a bundle of
    notifications the count is the number of notifications in the bundle. Value
    will never be 0 or 1.
    """
    return self._bundle_count or 0

  @bundle_count.setter
  def bundle_count(self, bundle_count: Optional[int]):
    if bundle_count is None:
      del self.bundle_count
      return
    if not isinstance(bundle_count, int):
      raise TypeError('bundle_count must be of type int')
    self._bundle_count = bundle_count

  @property
  def message_preview(self) -> str:
    """The following fields are only defined for emails or summary/full views"""
    return self._message_preview or ""

  @message_preview.setter
  def message_preview(self, message_preview: Optional[str]):
    if message_preview is None:
      del self.message_preview
      return
    if not isinstance(message_preview, str):
      raise TypeError('message_preview must be of type str')
    self._message_preview = message_preview

  @property
  def action_url(self) -> str:
    return self._action_url or ""

  @action_url.setter
  def action_url(self, action_url: Optional[str]):
    if action_url is None:
      del self.action_url
      return
    if not isinstance(action_url, str):
      raise TypeError('action_url must be of type str')
    self._action_url = action_url

  @property
  def upvote_url(self) -> str:
    return self._upvote_url or ""

  @upvote_url.setter
  def upvote_url(self, upvote_url: Optional[str]):
    if upvote_url is None:
      del self.upvote_url
      return
    if not isinstance(upvote_url, str):
      raise TypeError('upvote_url must be of type str')
    self._upvote_url = upvote_url

  @property
  def downvote_url(self) -> str:
    return self._downvote_url or ""

  @downvote_url.setter
  def downvote_url(self, downvote_url: Optional[str]):
    if downvote_url is None:
      del self.downvote_url
      return
    if not isinstance(downvote_url, str):
      raise TypeError('downvote_url must be of type str')
    self._downvote_url = downvote_url

  @property
  def vote_count(self) -> int:
    return self._vote_count or 0

  @vote_count.setter
  def vote_count(self, vote_count: Optional[int]):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def medal_url(self) -> str:
    return self._medal_url or ""

  @medal_url.setter
  def medal_url(self, medal_url: Optional[str]):
    if medal_url is None:
      del self.medal_url
      return
    if not isinstance(medal_url, str):
      raise TypeError('medal_url must be of type str')
    self._medal_url = medal_url


class UserNotificationSettings(KaggleObject):
  r"""
  Settings for notifications.

  Attributes:
    enabled (bool)
      Are notifications enabled at all (global setting).
    subscriptions (UserSubscription)
      A list of your current subscriptions, currently not populated (because of a
      performance issue).
    aggregation (NotificationAggregationOption)
      Whether email notifications are aggregated, currently not used.
    user_collaboration_messages (NotificationDeliveryType)
      How to receive collaboration emails from other users. Should only be Email
      or None.
    is_subscribed_to_mailing_list (bool)
      Whether you are subscribed to the mailing list ('News and Tips').
    at_mention_followed_user (NotificationDeliveryType)
      How to receive notifications about @-mentions from users you are following.
    at_mention_regular_user (NotificationDeliveryType)
      How to receive notifications about @-mentions from other users.
    competition_announcements (NotificationDeliveryType)
      How to receive notifications for competition announcements.
    competition_team_updates (NotificationDeliveryType)
      How to receive notifications about updates for your competition team.
    dataset_alerts (NotificationDeliveryType)
      How to receive notifications about your datasets.
    notebook_alerts (NotificationDeliveryType)
      How to receive notifications about your notebooks.
    engaged_topic_comment (NotificationDeliveryType)
      How to receive notifications about topics you've participated in.
    user_new_follower (NotificationDeliveryType)
      How to receive notifications when a user follows you.
    new_topic (NotificationDeliveryType)
      How to receive notifications about new topics in a forum you're following.
    new_tier_achieved_or_medal (NotificationDeliveryType)
      How to receive notifications about new medals you've achieved or tier
      level-ups.
    topic_upvote (NotificationDeliveryType)
      How to receive notifications when one of your topics is upvoted
    topic_comment (NotificationDeliveryType)
      How to receive notifications when a topic you are following is commented on
    organization_alerts (NotificationDeliveryType)
      How to receive notifications about your organizations
    dataset_suggestion_alerts (NotificationDeliveryType)
      How to receive notifications about suggestions you've made on datasets
    group_alerts (NotificationDeliveryType)
      How to receive notifications about groups
    resource_share_alerts (NotificationDeliveryType)
      How to receive notifications when a resource is shared with you
    benchmark_alerts (NotificationDeliveryType)
      How to receive notifications about benchmarks you subscribe to
    benchmark_run_alerts (NotificationDeliveryType)
      How to receive notifications about benchmark runs you own
    new_model_alerts (NotificationDeliveryType)
      How to receive notifications about new models on benchmarks you subscribe
      to
  """

  def __init__(self):
    self._enabled = False
    self._subscriptions = []
    self._aggregation = NotificationAggregationOption.NOTIFICATION_AGGREGATION_OPTION_NO_AGGREGATION
    self._user_collaboration_messages = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._is_subscribed_to_mailing_list = False
    self._at_mention_followed_user = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._at_mention_regular_user = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._competition_announcements = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._competition_team_updates = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._dataset_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._notebook_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._engaged_topic_comment = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._user_new_follower = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._new_topic = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._new_tier_achieved_or_medal = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._topic_upvote = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._topic_comment = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._organization_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._dataset_suggestion_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._group_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._resource_share_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._benchmark_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._benchmark_run_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._new_model_alerts = NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE
    self._freeze()

  @property
  def enabled(self) -> bool:
    """Are notifications enabled at all (global setting)."""
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
  def subscriptions(self) -> Optional[List[Optional['UserSubscription']]]:
    r"""
    A list of your current subscriptions, currently not populated (because of a
    performance issue).
    """
    return self._subscriptions

  @subscriptions.setter
  def subscriptions(self, subscriptions: Optional[List[Optional['UserSubscription']]]):
    if subscriptions is None:
      del self.subscriptions
      return
    if not isinstance(subscriptions, list):
      raise TypeError('subscriptions must be of type list')
    if not all([isinstance(t, UserSubscription) for t in subscriptions]):
      raise TypeError('subscriptions must contain only items of type UserSubscription')
    self._subscriptions = subscriptions

  @property
  def aggregation(self) -> 'NotificationAggregationOption':
    """Whether email notifications are aggregated, currently not used."""
    return self._aggregation

  @aggregation.setter
  def aggregation(self, aggregation: 'NotificationAggregationOption'):
    if aggregation is None:
      del self.aggregation
      return
    if not isinstance(aggregation, NotificationAggregationOption):
      raise TypeError('aggregation must be of type NotificationAggregationOption')
    self._aggregation = aggregation

  @property
  def user_collaboration_messages(self) -> 'NotificationDeliveryType':
    r"""
    How to receive collaboration emails from other users. Should only be Email
    or None.
    """
    return self._user_collaboration_messages

  @user_collaboration_messages.setter
  def user_collaboration_messages(self, user_collaboration_messages: 'NotificationDeliveryType'):
    if user_collaboration_messages is None:
      del self.user_collaboration_messages
      return
    if not isinstance(user_collaboration_messages, NotificationDeliveryType):
      raise TypeError('user_collaboration_messages must be of type NotificationDeliveryType')
    self._user_collaboration_messages = user_collaboration_messages

  @property
  def is_subscribed_to_mailing_list(self) -> bool:
    """Whether you are subscribed to the mailing list ('News and Tips')."""
    return self._is_subscribed_to_mailing_list

  @is_subscribed_to_mailing_list.setter
  def is_subscribed_to_mailing_list(self, is_subscribed_to_mailing_list: bool):
    if is_subscribed_to_mailing_list is None:
      del self.is_subscribed_to_mailing_list
      return
    if not isinstance(is_subscribed_to_mailing_list, bool):
      raise TypeError('is_subscribed_to_mailing_list must be of type bool')
    self._is_subscribed_to_mailing_list = is_subscribed_to_mailing_list

  @property
  def at_mention_followed_user(self) -> 'NotificationDeliveryType':
    """How to receive notifications about @-mentions from users you are following."""
    return self._at_mention_followed_user

  @at_mention_followed_user.setter
  def at_mention_followed_user(self, at_mention_followed_user: 'NotificationDeliveryType'):
    if at_mention_followed_user is None:
      del self.at_mention_followed_user
      return
    if not isinstance(at_mention_followed_user, NotificationDeliveryType):
      raise TypeError('at_mention_followed_user must be of type NotificationDeliveryType')
    self._at_mention_followed_user = at_mention_followed_user

  @property
  def at_mention_regular_user(self) -> 'NotificationDeliveryType':
    """How to receive notifications about @-mentions from other users."""
    return self._at_mention_regular_user

  @at_mention_regular_user.setter
  def at_mention_regular_user(self, at_mention_regular_user: 'NotificationDeliveryType'):
    if at_mention_regular_user is None:
      del self.at_mention_regular_user
      return
    if not isinstance(at_mention_regular_user, NotificationDeliveryType):
      raise TypeError('at_mention_regular_user must be of type NotificationDeliveryType')
    self._at_mention_regular_user = at_mention_regular_user

  @property
  def competition_announcements(self) -> 'NotificationDeliveryType':
    """How to receive notifications for competition announcements."""
    return self._competition_announcements

  @competition_announcements.setter
  def competition_announcements(self, competition_announcements: 'NotificationDeliveryType'):
    if competition_announcements is None:
      del self.competition_announcements
      return
    if not isinstance(competition_announcements, NotificationDeliveryType):
      raise TypeError('competition_announcements must be of type NotificationDeliveryType')
    self._competition_announcements = competition_announcements

  @property
  def competition_team_updates(self) -> 'NotificationDeliveryType':
    """How to receive notifications about updates for your competition team."""
    return self._competition_team_updates

  @competition_team_updates.setter
  def competition_team_updates(self, competition_team_updates: 'NotificationDeliveryType'):
    if competition_team_updates is None:
      del self.competition_team_updates
      return
    if not isinstance(competition_team_updates, NotificationDeliveryType):
      raise TypeError('competition_team_updates must be of type NotificationDeliveryType')
    self._competition_team_updates = competition_team_updates

  @property
  def dataset_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about your datasets."""
    return self._dataset_alerts

  @dataset_alerts.setter
  def dataset_alerts(self, dataset_alerts: 'NotificationDeliveryType'):
    if dataset_alerts is None:
      del self.dataset_alerts
      return
    if not isinstance(dataset_alerts, NotificationDeliveryType):
      raise TypeError('dataset_alerts must be of type NotificationDeliveryType')
    self._dataset_alerts = dataset_alerts

  @property
  def notebook_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about your notebooks."""
    return self._notebook_alerts

  @notebook_alerts.setter
  def notebook_alerts(self, notebook_alerts: 'NotificationDeliveryType'):
    if notebook_alerts is None:
      del self.notebook_alerts
      return
    if not isinstance(notebook_alerts, NotificationDeliveryType):
      raise TypeError('notebook_alerts must be of type NotificationDeliveryType')
    self._notebook_alerts = notebook_alerts

  @property
  def engaged_topic_comment(self) -> 'NotificationDeliveryType':
    """How to receive notifications about topics you've participated in."""
    return self._engaged_topic_comment

  @engaged_topic_comment.setter
  def engaged_topic_comment(self, engaged_topic_comment: 'NotificationDeliveryType'):
    if engaged_topic_comment is None:
      del self.engaged_topic_comment
      return
    if not isinstance(engaged_topic_comment, NotificationDeliveryType):
      raise TypeError('engaged_topic_comment must be of type NotificationDeliveryType')
    self._engaged_topic_comment = engaged_topic_comment

  @property
  def user_new_follower(self) -> 'NotificationDeliveryType':
    """How to receive notifications when a user follows you."""
    return self._user_new_follower

  @user_new_follower.setter
  def user_new_follower(self, user_new_follower: 'NotificationDeliveryType'):
    if user_new_follower is None:
      del self.user_new_follower
      return
    if not isinstance(user_new_follower, NotificationDeliveryType):
      raise TypeError('user_new_follower must be of type NotificationDeliveryType')
    self._user_new_follower = user_new_follower

  @property
  def new_topic(self) -> 'NotificationDeliveryType':
    """How to receive notifications about new topics in a forum you're following."""
    return self._new_topic

  @new_topic.setter
  def new_topic(self, new_topic: 'NotificationDeliveryType'):
    if new_topic is None:
      del self.new_topic
      return
    if not isinstance(new_topic, NotificationDeliveryType):
      raise TypeError('new_topic must be of type NotificationDeliveryType')
    self._new_topic = new_topic

  @property
  def new_tier_achieved_or_medal(self) -> 'NotificationDeliveryType':
    r"""
    How to receive notifications about new medals you've achieved or tier
    level-ups.
    """
    return self._new_tier_achieved_or_medal

  @new_tier_achieved_or_medal.setter
  def new_tier_achieved_or_medal(self, new_tier_achieved_or_medal: 'NotificationDeliveryType'):
    if new_tier_achieved_or_medal is None:
      del self.new_tier_achieved_or_medal
      return
    if not isinstance(new_tier_achieved_or_medal, NotificationDeliveryType):
      raise TypeError('new_tier_achieved_or_medal must be of type NotificationDeliveryType')
    self._new_tier_achieved_or_medal = new_tier_achieved_or_medal

  @property
  def topic_upvote(self) -> 'NotificationDeliveryType':
    """How to receive notifications when one of your topics is upvoted"""
    return self._topic_upvote

  @topic_upvote.setter
  def topic_upvote(self, topic_upvote: 'NotificationDeliveryType'):
    if topic_upvote is None:
      del self.topic_upvote
      return
    if not isinstance(topic_upvote, NotificationDeliveryType):
      raise TypeError('topic_upvote must be of type NotificationDeliveryType')
    self._topic_upvote = topic_upvote

  @property
  def topic_comment(self) -> 'NotificationDeliveryType':
    """How to receive notifications when a topic you are following is commented on"""
    return self._topic_comment

  @topic_comment.setter
  def topic_comment(self, topic_comment: 'NotificationDeliveryType'):
    if topic_comment is None:
      del self.topic_comment
      return
    if not isinstance(topic_comment, NotificationDeliveryType):
      raise TypeError('topic_comment must be of type NotificationDeliveryType')
    self._topic_comment = topic_comment

  @property
  def organization_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about your organizations"""
    return self._organization_alerts

  @organization_alerts.setter
  def organization_alerts(self, organization_alerts: 'NotificationDeliveryType'):
    if organization_alerts is None:
      del self.organization_alerts
      return
    if not isinstance(organization_alerts, NotificationDeliveryType):
      raise TypeError('organization_alerts must be of type NotificationDeliveryType')
    self._organization_alerts = organization_alerts

  @property
  def dataset_suggestion_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about suggestions you've made on datasets"""
    return self._dataset_suggestion_alerts

  @dataset_suggestion_alerts.setter
  def dataset_suggestion_alerts(self, dataset_suggestion_alerts: 'NotificationDeliveryType'):
    if dataset_suggestion_alerts is None:
      del self.dataset_suggestion_alerts
      return
    if not isinstance(dataset_suggestion_alerts, NotificationDeliveryType):
      raise TypeError('dataset_suggestion_alerts must be of type NotificationDeliveryType')
    self._dataset_suggestion_alerts = dataset_suggestion_alerts

  @property
  def group_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about groups"""
    return self._group_alerts

  @group_alerts.setter
  def group_alerts(self, group_alerts: 'NotificationDeliveryType'):
    if group_alerts is None:
      del self.group_alerts
      return
    if not isinstance(group_alerts, NotificationDeliveryType):
      raise TypeError('group_alerts must be of type NotificationDeliveryType')
    self._group_alerts = group_alerts

  @property
  def resource_share_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications when a resource is shared with you"""
    return self._resource_share_alerts

  @resource_share_alerts.setter
  def resource_share_alerts(self, resource_share_alerts: 'NotificationDeliveryType'):
    if resource_share_alerts is None:
      del self.resource_share_alerts
      return
    if not isinstance(resource_share_alerts, NotificationDeliveryType):
      raise TypeError('resource_share_alerts must be of type NotificationDeliveryType')
    self._resource_share_alerts = resource_share_alerts

  @property
  def benchmark_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about benchmarks you subscribe to"""
    return self._benchmark_alerts

  @benchmark_alerts.setter
  def benchmark_alerts(self, benchmark_alerts: 'NotificationDeliveryType'):
    if benchmark_alerts is None:
      del self.benchmark_alerts
      return
    if not isinstance(benchmark_alerts, NotificationDeliveryType):
      raise TypeError('benchmark_alerts must be of type NotificationDeliveryType')
    self._benchmark_alerts = benchmark_alerts

  @property
  def benchmark_run_alerts(self) -> 'NotificationDeliveryType':
    """How to receive notifications about benchmark runs you own"""
    return self._benchmark_run_alerts

  @benchmark_run_alerts.setter
  def benchmark_run_alerts(self, benchmark_run_alerts: 'NotificationDeliveryType'):
    if benchmark_run_alerts is None:
      del self.benchmark_run_alerts
      return
    if not isinstance(benchmark_run_alerts, NotificationDeliveryType):
      raise TypeError('benchmark_run_alerts must be of type NotificationDeliveryType')
    self._benchmark_run_alerts = benchmark_run_alerts

  @property
  def new_model_alerts(self) -> 'NotificationDeliveryType':
    r"""
    How to receive notifications about new models on benchmarks you subscribe
    to
    """
    return self._new_model_alerts

  @new_model_alerts.setter
  def new_model_alerts(self, new_model_alerts: 'NotificationDeliveryType'):
    if new_model_alerts is None:
      del self.new_model_alerts
      return
    if not isinstance(new_model_alerts, NotificationDeliveryType):
      raise TypeError('new_model_alerts must be of type NotificationDeliveryType')
    self._new_model_alerts = new_model_alerts


class UserSubscription(KaggleObject):
  r"""
  Attributes:
    id (int)
    subscription_state_id (int)
    subscription_type (str)
    name (str)
    kernel_name (str)
    notification_count (int)
    last_notification_created_date (datetime)
    link (str)
  """

  def __init__(self):
    self._id = 0
    self._subscription_state_id = 0
    self._subscription_type = ""
    self._name = ""
    self._kernel_name = ""
    self._notification_count = 0
    self._last_notification_created_date = None
    self._link = ""
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def subscription_state_id(self) -> int:
    return self._subscription_state_id

  @subscription_state_id.setter
  def subscription_state_id(self, subscription_state_id: int):
    if subscription_state_id is None:
      del self.subscription_state_id
      return
    if not isinstance(subscription_state_id, int):
      raise TypeError('subscription_state_id must be of type int')
    self._subscription_state_id = subscription_state_id

  @property
  def subscription_type(self) -> str:
    return self._subscription_type

  @subscription_type.setter
  def subscription_type(self, subscription_type: str):
    if subscription_type is None:
      del self.subscription_type
      return
    if not isinstance(subscription_type, str):
      raise TypeError('subscription_type must be of type str')
    self._subscription_type = subscription_type

  @property
  def name(self) -> str:
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
  def kernel_name(self) -> str:
    return self._kernel_name

  @kernel_name.setter
  def kernel_name(self, kernel_name: str):
    if kernel_name is None:
      del self.kernel_name
      return
    if not isinstance(kernel_name, str):
      raise TypeError('kernel_name must be of type str')
    self._kernel_name = kernel_name

  @property
  def notification_count(self) -> int:
    return self._notification_count

  @notification_count.setter
  def notification_count(self, notification_count: int):
    if notification_count is None:
      del self.notification_count
      return
    if not isinstance(notification_count, int):
      raise TypeError('notification_count must be of type int')
    self._notification_count = notification_count

  @property
  def last_notification_created_date(self) -> datetime:
    return self._last_notification_created_date

  @last_notification_created_date.setter
  def last_notification_created_date(self, last_notification_created_date: datetime):
    if last_notification_created_date is None:
      del self.last_notification_created_date
      return
    if not isinstance(last_notification_created_date, datetime):
      raise TypeError('last_notification_created_date must be of type datetime')
    self._last_notification_created_date = last_notification_created_date

  @property
  def link(self) -> str:
    return self._link

  @link.setter
  def link(self, link: str):
    if link is None:
      del self.link
      return
    if not isinstance(link, str):
      raise TypeError('link must be of type str')
    self._link = link


MessageObject._fields = [
  FieldMetadata("key", "key", "_key", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("text", "text", "_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

Notification._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("subscriptionType", "subscription_type", "_subscription_type", SubscriptionType, SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE, EnumSerializer()),
  FieldMetadata("relatedItemId", "related_item_id", "_related_item_id", int, 0, PredefinedSerializer()),
  FieldMetadata("relatedItemType", "related_item_type", "_related_item_type", NotificationRelatedItemType, NotificationRelatedItemType.NOTIFICATION_RELATED_ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isRead", "is_read", "_is_read", bool, False, PredefinedSerializer()),
  FieldMetadata("isViewed", "is_viewed", "_is_viewed", bool, False, PredefinedSerializer()),
  FieldMetadata("createdDate", "created_date", "_created_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageHref", "image_href", "_image_href", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageFormat", "message_format", "_message_format", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageObjects", "message_objects", "_message_objects", MessageObject, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("message", "message", "_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bundleCount", "bundle_count", "_bundle_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messagePreview", "message_preview", "_message_preview", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("actionUrl", "action_url", "_action_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("upvoteUrl", "upvote_url", "_upvote_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("downvoteUrl", "downvote_url", "_downvote_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medalUrl", "medal_url", "_medal_url", str, None, PredefinedSerializer(), optional=True),
]

UserNotificationSettings._fields = [
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("subscriptions", "subscriptions", "_subscriptions", UserSubscription, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("aggregation", "aggregation", "_aggregation", NotificationAggregationOption, NotificationAggregationOption.NOTIFICATION_AGGREGATION_OPTION_NO_AGGREGATION, EnumSerializer()),
  FieldMetadata("userCollaborationMessages", "user_collaboration_messages", "_user_collaboration_messages", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("isSubscribedToMailingList", "is_subscribed_to_mailing_list", "_is_subscribed_to_mailing_list", bool, False, PredefinedSerializer()),
  FieldMetadata("atMentionFollowedUser", "at_mention_followed_user", "_at_mention_followed_user", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("atMentionRegularUser", "at_mention_regular_user", "_at_mention_regular_user", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("competitionAnnouncements", "competition_announcements", "_competition_announcements", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("competitionTeamUpdates", "competition_team_updates", "_competition_team_updates", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("datasetAlerts", "dataset_alerts", "_dataset_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("notebookAlerts", "notebook_alerts", "_notebook_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("engagedTopicComment", "engaged_topic_comment", "_engaged_topic_comment", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("userNewFollower", "user_new_follower", "_user_new_follower", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("newTopic", "new_topic", "_new_topic", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("newTierAchievedOrMedal", "new_tier_achieved_or_medal", "_new_tier_achieved_or_medal", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("topicUpvote", "topic_upvote", "_topic_upvote", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("topicComment", "topic_comment", "_topic_comment", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("organizationAlerts", "organization_alerts", "_organization_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("datasetSuggestionAlerts", "dataset_suggestion_alerts", "_dataset_suggestion_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("groupAlerts", "group_alerts", "_group_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("resourceShareAlerts", "resource_share_alerts", "_resource_share_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("benchmarkAlerts", "benchmark_alerts", "_benchmark_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("benchmarkRunAlerts", "benchmark_run_alerts", "_benchmark_run_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
  FieldMetadata("newModelAlerts", "new_model_alerts", "_new_model_alerts", NotificationDeliveryType, NotificationDeliveryType.NOTIFICATION_DELIVERY_TYPE_NONE, EnumSerializer()),
]

UserSubscription._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("subscriptionStateId", "subscription_state_id", "_subscription_state_id", int, 0, PredefinedSerializer()),
  FieldMetadata("subscriptionType", "subscription_type", "_subscription_type", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("kernelName", "kernel_name", "_kernel_name", str, "", PredefinedSerializer()),
  FieldMetadata("notificationCount", "notification_count", "_notification_count", int, 0, PredefinedSerializer()),
  FieldMetadata("lastNotificationCreatedDate", "last_notification_created_date", "_last_notification_created_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("link", "link", "_link", str, "", PredefinedSerializer()),
]

