from kagglesdk.discussions.types.discussions_enums import CommentAuthorType, TopicListCategory, TopicListGroup, TopicListSortBy
from kagglesdk.discussions.types.forum import Forum
from kagglesdk.discussions.types.forum_topic import ForumTopic
from kagglesdk.kaggle_object import *
from kagglesdk.notifications.types.notifications_enums import SubscribeState
from kagglesdk.users.types.user import User
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class Discussion(KaggleObject):
  r"""
  Attributes:
    current_user (User)
    site_forums (Forum)
    topic_sort (TopicListSortBy)
  """

  def __init__(self):
    self._current_user = None
    self._site_forums = []
    self._topic_sort = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._freeze()

  @property
  def current_user(self) -> Optional['User']:
    return self._current_user

  @current_user.setter
  def current_user(self, current_user: Optional['User']):
    if current_user is None:
      del self.current_user
      return
    if not isinstance(current_user, User):
      raise TypeError('current_user must be of type User')
    self._current_user = current_user

  @property
  def site_forums(self) -> Optional[List[Optional['Forum']]]:
    return self._site_forums

  @site_forums.setter
  def site_forums(self, site_forums: Optional[List[Optional['Forum']]]):
    if site_forums is None:
      del self.site_forums
      return
    if not isinstance(site_forums, list):
      raise TypeError('site_forums must be of type list')
    if not all([isinstance(t, Forum) for t in site_forums]):
      raise TypeError('site_forums must contain only items of type Forum')
    self._site_forums = site_forums

  @property
  def topic_sort(self) -> 'TopicListSortBy':
    return self._topic_sort

  @topic_sort.setter
  def topic_sort(self, topic_sort: 'TopicListSortBy'):
    if topic_sort is None:
      del self.topic_sort
      return
    if not isinstance(topic_sort, TopicListSortBy):
      raise TypeError('topic_sort must be of type TopicListSortBy')
    self._topic_sort = topic_sort


class DiscussionForum(KaggleObject):
  r"""
  Attributes:
    current_user (User)
    site_forums (Forum)
    topic_sort (TopicListSortBy)
    forum (Forum)
  """

  def __init__(self):
    self._current_user = None
    self._site_forums = []
    self._topic_sort = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._forum = None
    self._freeze()

  @property
  def current_user(self) -> Optional['User']:
    return self._current_user

  @current_user.setter
  def current_user(self, current_user: Optional['User']):
    if current_user is None:
      del self.current_user
      return
    if not isinstance(current_user, User):
      raise TypeError('current_user must be of type User')
    self._current_user = current_user

  @property
  def site_forums(self) -> Optional[List[Optional['Forum']]]:
    return self._site_forums

  @site_forums.setter
  def site_forums(self, site_forums: Optional[List[Optional['Forum']]]):
    if site_forums is None:
      del self.site_forums
      return
    if not isinstance(site_forums, list):
      raise TypeError('site_forums must be of type list')
    if not all([isinstance(t, Forum) for t in site_forums]):
      raise TypeError('site_forums must contain only items of type Forum')
    self._site_forums = site_forums

  @property
  def topic_sort(self) -> 'TopicListSortBy':
    return self._topic_sort

  @topic_sort.setter
  def topic_sort(self, topic_sort: 'TopicListSortBy'):
    if topic_sort is None:
      del self.topic_sort
      return
    if not isinstance(topic_sort, TopicListSortBy):
      raise TypeError('topic_sort must be of type TopicListSortBy')
    self._topic_sort = topic_sort

  @property
  def forum(self) -> Optional['Forum']:
    return self._forum

  @forum.setter
  def forum(self, forum: Optional['Forum']):
    if forum is None:
      del self.forum
      return
    if not isinstance(forum, Forum):
      raise TypeError('forum must be of type Forum')
    self._forum = forum


class DiscussionParamValues(KaggleObject):
  r"""
  Attributes:
    page (int)
    search (str)
    group (TopicListGroup)
    sort_by (TopicListSortBy)
    category (TopicListCategory)
  """

  def __init__(self):
    self._page = 0
    self._search = None
    self._group = TopicListGroup.TOPIC_LIST_GROUP_UNSPECIFIED
    self._sort_by = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._category = TopicListCategory.TOPIC_LIST_CATEGORY_UNSPECIFIED
    self._freeze()

  @property
  def page(self) -> int:
    return self._page

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def search(self) -> str:
    return self._search or ""

  @search.setter
  def search(self, search: Optional[str]):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

  @property
  def group(self) -> 'TopicListGroup':
    return self._group

  @group.setter
  def group(self, group: 'TopicListGroup'):
    if group is None:
      del self.group
      return
    if not isinstance(group, TopicListGroup):
      raise TypeError('group must be of type TopicListGroup')
    self._group = group

  @property
  def sort_by(self) -> 'TopicListSortBy':
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'TopicListSortBy'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, TopicListSortBy):
      raise TypeError('sort_by must be of type TopicListSortBy')
    self._sort_by = sort_by

  @property
  def category(self) -> 'TopicListCategory':
    return self._category

  @category.setter
  def category(self, category: 'TopicListCategory'):
    if category is None:
      del self.category
      return
    if not isinstance(category, TopicListCategory):
      raise TypeError('category must be of type TopicListCategory')
    self._category = category


class DiscussionTopic(KaggleObject):
  r"""
  Attributes:
    current_user (User)
    site_forums (Forum)
    topic_sort (TopicListSortBy)
    topic (ForumTopic)
  """

  def __init__(self):
    self._current_user = None
    self._site_forums = []
    self._topic_sort = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._topic = None
    self._freeze()

  @property
  def current_user(self) -> Optional['User']:
    return self._current_user

  @current_user.setter
  def current_user(self, current_user: Optional['User']):
    if current_user is None:
      del self.current_user
      return
    if not isinstance(current_user, User):
      raise TypeError('current_user must be of type User')
    self._current_user = current_user

  @property
  def site_forums(self) -> Optional[List[Optional['Forum']]]:
    return self._site_forums

  @site_forums.setter
  def site_forums(self, site_forums: Optional[List[Optional['Forum']]]):
    if site_forums is None:
      del self.site_forums
      return
    if not isinstance(site_forums, list):
      raise TypeError('site_forums must be of type list')
    if not all([isinstance(t, Forum) for t in site_forums]):
      raise TypeError('site_forums must contain only items of type Forum')
    self._site_forums = site_forums

  @property
  def topic_sort(self) -> 'TopicListSortBy':
    return self._topic_sort

  @topic_sort.setter
  def topic_sort(self, topic_sort: 'TopicListSortBy'):
    if topic_sort is None:
      del self.topic_sort
      return
    if not isinstance(topic_sort, TopicListSortBy):
      raise TypeError('topic_sort must be of type TopicListSortBy')
    self._topic_sort = topic_sort

  @property
  def topic(self) -> Optional['ForumTopic']:
    return self._topic

  @topic.setter
  def topic(self, topic: Optional['ForumTopic']):
    if topic is None:
      del self.topic
      return
    if not isinstance(topic, ForumTopic):
      raise TypeError('topic must be of type ForumTopic')
    self._topic = topic


class NewTopicDto(KaggleObject):
  r"""
  Attributes:
    allow_attachments (bool)
    author_tier (UserAchievementTier)
    author_type (CommentAuthorType)
    forum_id (int)
    parent_name (str)
    parent_url (str)
    is_private (bool)
    write_up_team_id (int)
      If set, show a checkbox allowing user to set the new topic as their team's
      write-up.
  """

  def __init__(self):
    self._allow_attachments = False
    self._author_tier = UserAchievementTier.NOVICE
    self._author_type = CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED
    self._forum_id = 0
    self._parent_name = None
    self._parent_url = None
    self._is_private = False
    self._write_up_team_id = None
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
  def author_tier(self) -> 'UserAchievementTier':
    return self._author_tier

  @author_tier.setter
  def author_tier(self, author_tier: 'UserAchievementTier'):
    if author_tier is None:
      del self.author_tier
      return
    if not isinstance(author_tier, UserAchievementTier):
      raise TypeError('author_tier must be of type UserAchievementTier')
    self._author_tier = author_tier

  @property
  def author_type(self) -> 'CommentAuthorType':
    return self._author_type

  @author_type.setter
  def author_type(self, author_type: 'CommentAuthorType'):
    if author_type is None:
      del self.author_type
      return
    if not isinstance(author_type, CommentAuthorType):
      raise TypeError('author_type must be of type CommentAuthorType')
    self._author_type = author_type

  @property
  def forum_id(self) -> int:
    return self._forum_id

  @forum_id.setter
  def forum_id(self, forum_id: int):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

  @property
  def parent_name(self) -> str:
    return self._parent_name or ""

  @parent_name.setter
  def parent_name(self, parent_name: Optional[str]):
    if parent_name is None:
      del self.parent_name
      return
    if not isinstance(parent_name, str):
      raise TypeError('parent_name must be of type str')
    self._parent_name = parent_name

  @property
  def parent_url(self) -> str:
    return self._parent_url or ""

  @parent_url.setter
  def parent_url(self, parent_url: Optional[str]):
    if parent_url is None:
      del self.parent_url
      return
    if not isinstance(parent_url, str):
      raise TypeError('parent_url must be of type str')
    self._parent_url = parent_url

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
  def write_up_team_id(self) -> int:
    r"""
    If set, show a checkbox allowing user to set the new topic as their team's
    write-up.
    """
    return self._write_up_team_id or 0

  @write_up_team_id.setter
  def write_up_team_id(self, write_up_team_id: Optional[int]):
    if write_up_team_id is None:
      del self.write_up_team_id
      return
    if not isinstance(write_up_team_id, int):
      raise TypeError('write_up_team_id must be of type int')
    self._write_up_team_id = write_up_team_id


class TopicListDto(KaggleObject):
  r"""
  Attributes:
    can_downvote (bool)
    data_url (str)
    id (int)
    show_subscribe_button (bool)
    subscription (SubscribeState)
    param_values (DiscussionParamValues)
  """

  def __init__(self):
    self._can_downvote = False
    self._data_url = None
    self._id = None
    self._show_subscribe_button = False
    self._subscription = SubscribeState.INVALID
    self._param_values = None
    self._freeze()

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
  def data_url(self) -> str:
    return self._data_url or ""

  @data_url.setter
  def data_url(self, data_url: Optional[str]):
    if data_url is None:
      del self.data_url
      return
    if not isinstance(data_url, str):
      raise TypeError('data_url must be of type str')
    self._data_url = data_url

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
  def show_subscribe_button(self) -> bool:
    return self._show_subscribe_button

  @show_subscribe_button.setter
  def show_subscribe_button(self, show_subscribe_button: bool):
    if show_subscribe_button is None:
      del self.show_subscribe_button
      return
    if not isinstance(show_subscribe_button, bool):
      raise TypeError('show_subscribe_button must be of type bool')
    self._show_subscribe_button = show_subscribe_button

  @property
  def subscription(self) -> 'SubscribeState':
    return self._subscription

  @subscription.setter
  def subscription(self, subscription: 'SubscribeState'):
    if subscription is None:
      del self.subscription
      return
    if not isinstance(subscription, SubscribeState):
      raise TypeError('subscription must be of type SubscribeState')
    self._subscription = subscription

  @property
  def param_values(self) -> Optional['DiscussionParamValues']:
    return self._param_values

  @param_values.setter
  def param_values(self, param_values: Optional['DiscussionParamValues']):
    if param_values is None:
      del self.param_values
      return
    if not isinstance(param_values, DiscussionParamValues):
      raise TypeError('param_values must be of type DiscussionParamValues')
    self._param_values = param_values


Discussion._fields = [
  FieldMetadata("currentUser", "current_user", "_current_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("siteForums", "site_forums", "_site_forums", Forum, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("topicSort", "topic_sort", "_topic_sort", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
]

DiscussionForum._fields = [
  FieldMetadata("currentUser", "current_user", "_current_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("siteForums", "site_forums", "_site_forums", Forum, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("topicSort", "topic_sort", "_topic_sort", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("forum", "forum", "_forum", Forum, None, KaggleObjectSerializer()),
]

DiscussionParamValues._fields = [
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", TopicListGroup, TopicListGroup.TOPIC_LIST_GROUP_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sortBy", "sort_by", "_sort_by", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("category", "category", "_category", TopicListCategory, TopicListCategory.TOPIC_LIST_CATEGORY_UNSPECIFIED, EnumSerializer()),
]

DiscussionTopic._fields = [
  FieldMetadata("currentUser", "current_user", "_current_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("siteForums", "site_forums", "_site_forums", Forum, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("topicSort", "topic_sort", "_topic_sort", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("topic", "topic", "_topic", ForumTopic, None, KaggleObjectSerializer()),
]

NewTopicDto._fields = [
  FieldMetadata("allowAttachments", "allow_attachments", "_allow_attachments", bool, False, PredefinedSerializer()),
  FieldMetadata("authorTier", "author_tier", "_author_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("authorType", "author_type", "_author_type", CommentAuthorType, CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentName", "parent_name", "_parent_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentUrl", "parent_url", "_parent_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("writeUpTeamId", "write_up_team_id", "_write_up_team_id", int, None, PredefinedSerializer(), optional=True),
]

TopicListDto._fields = [
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("dataUrl", "data_url", "_data_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("showSubscribeButton", "show_subscribe_button", "_show_subscribe_button", bool, False, PredefinedSerializer()),
  FieldMetadata("subscription", "subscription", "_subscription", SubscribeState, SubscribeState.INVALID, EnumSerializer()),
  FieldMetadata("paramValues", "param_values", "_param_values", DiscussionParamValues, None, KaggleObjectSerializer()),
]

