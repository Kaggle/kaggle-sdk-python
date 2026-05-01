from datetime import datetime
from kagglesdk.discussions.types.discussions_enums import TopicListCategory, TopicListGroup, TopicListSortBy
from kagglesdk.kaggle_object import *
from typing import Optional, List

class ApiDiscussionComment(KaggleObject):
  r"""
  A simplified view of a discussion comment for the public API.

  Attributes:
    id (int)
    author_name (str)
    author_url (str)
    post_date (datetime)
    content (str)
    votes (int)
    replies (ApiDiscussionComment)
  """

  def __init__(self):
    self._id = 0
    self._author_name = ""
    self._author_url = ""
    self._post_date = None
    self._content = ""
    self._votes = 0
    self._replies = []
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
  def author_name(self) -> str:
    return self._author_name

  @author_name.setter
  def author_name(self, author_name: str):
    if author_name is None:
      del self.author_name
      return
    if not isinstance(author_name, str):
      raise TypeError('author_name must be of type str')
    self._author_name = author_name

  @property
  def author_url(self) -> str:
    return self._author_url

  @author_url.setter
  def author_url(self, author_url: str):
    if author_url is None:
      del self.author_url
      return
    if not isinstance(author_url, str):
      raise TypeError('author_url must be of type str')
    self._author_url = author_url

  @property
  def post_date(self) -> datetime:
    return self._post_date

  @post_date.setter
  def post_date(self, post_date: datetime):
    if post_date is None:
      del self.post_date
      return
    if not isinstance(post_date, datetime):
      raise TypeError('post_date must be of type datetime')
    self._post_date = post_date

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

  @property
  def votes(self) -> int:
    return self._votes

  @votes.setter
  def votes(self, votes: int):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, int):
      raise TypeError('votes must be of type int')
    self._votes = votes

  @property
  def replies(self) -> Optional[List[Optional['ApiDiscussionComment']]]:
    return self._replies

  @replies.setter
  def replies(self, replies: Optional[List[Optional['ApiDiscussionComment']]]):
    if replies is None:
      del self.replies
      return
    if not isinstance(replies, list):
      raise TypeError('replies must be of type list')
    if not all([isinstance(t, ApiDiscussionComment) for t in replies]):
      raise TypeError('replies must contain only items of type ApiDiscussionComment')
    self._replies = replies


class ApiDiscussionForum(KaggleObject):
  r"""
  A simplified view of a discussion forum for the public API.

  Attributes:
    id (int)
    name (str)
    url (str)
    subtitle (str)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._url = ""
    self._subtitle = ""
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
  def url(self) -> str:
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
  def subtitle(self) -> str:
    return self._subtitle

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle


class ApiDiscussionTopic(KaggleObject):
  r"""
  A simplified view of a discussion topic for the public API.

  Attributes:
    id (int)
    title (str)
    url (str)
    post_date (datetime)
    last_comment_date (datetime)
    author_name (str)
    author_url (str)
    votes (int)
    comment_count (int)
    forum_name (str)
    forum_id (int)
    content (str)
      The content of the first message (the topic body).
  """

  def __init__(self):
    self._id = 0
    self._title = ""
    self._url = ""
    self._post_date = None
    self._last_comment_date = None
    self._author_name = ""
    self._author_url = ""
    self._votes = 0
    self._comment_count = 0
    self._forum_name = ""
    self._forum_id = 0
    self._content = None
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
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def url(self) -> str:
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
  def post_date(self) -> datetime:
    return self._post_date

  @post_date.setter
  def post_date(self, post_date: datetime):
    if post_date is None:
      del self.post_date
      return
    if not isinstance(post_date, datetime):
      raise TypeError('post_date must be of type datetime')
    self._post_date = post_date

  @property
  def last_comment_date(self) -> datetime:
    return self._last_comment_date

  @last_comment_date.setter
  def last_comment_date(self, last_comment_date: datetime):
    if last_comment_date is None:
      del self.last_comment_date
      return
    if not isinstance(last_comment_date, datetime):
      raise TypeError('last_comment_date must be of type datetime')
    self._last_comment_date = last_comment_date

  @property
  def author_name(self) -> str:
    return self._author_name

  @author_name.setter
  def author_name(self, author_name: str):
    if author_name is None:
      del self.author_name
      return
    if not isinstance(author_name, str):
      raise TypeError('author_name must be of type str')
    self._author_name = author_name

  @property
  def author_url(self) -> str:
    return self._author_url

  @author_url.setter
  def author_url(self, author_url: str):
    if author_url is None:
      del self.author_url
      return
    if not isinstance(author_url, str):
      raise TypeError('author_url must be of type str')
    self._author_url = author_url

  @property
  def votes(self) -> int:
    return self._votes

  @votes.setter
  def votes(self, votes: int):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, int):
      raise TypeError('votes must be of type int')
    self._votes = votes

  @property
  def comment_count(self) -> int:
    return self._comment_count

  @comment_count.setter
  def comment_count(self, comment_count: int):
    if comment_count is None:
      del self.comment_count
      return
    if not isinstance(comment_count, int):
      raise TypeError('comment_count must be of type int')
    self._comment_count = comment_count

  @property
  def forum_name(self) -> str:
    return self._forum_name

  @forum_name.setter
  def forum_name(self, forum_name: str):
    if forum_name is None:
      del self.forum_name
      return
    if not isinstance(forum_name, str):
      raise TypeError('forum_name must be of type str')
    self._forum_name = forum_name

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
  def content(self) -> str:
    """The content of the first message (the topic body)."""
    return self._content or ""

  @content.setter
  def content(self, content: Optional[str]):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content


class ApiGetTopicRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      The topic ID to retrieve.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The topic ID to retrieve."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  def endpoint(self):
    path = '/api/v1/discussions/{id}/get'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/discussions/{id}/get'


class ApiGetTopicResponse(KaggleObject):
  r"""
  Attributes:
    topic (ApiDiscussionTopic)
  """

  def __init__(self):
    self._topic = None
    self._freeze()

  @property
  def topic(self) -> Optional['ApiDiscussionTopic']:
    return self._topic

  @topic.setter
  def topic(self, topic: Optional['ApiDiscussionTopic']):
    if topic is None:
      del self.topic
      return
    if not isinstance(topic, ApiDiscussionTopic):
      raise TypeError('topic must be of type ApiDiscussionTopic')
    self._topic = topic


class ApiListCommentsRequest(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
      The topic ID to list comments for.
    page_size (int)
      Page size for results.
    page_token (str)
      Page token used for pagination.
  """

  def __init__(self):
    self._topic_id = 0
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def topic_id(self) -> int:
    """The topic ID to list comments for."""
    return self._topic_id

  @topic_id.setter
  def topic_id(self, topic_id: int):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def page_size(self) -> int:
    """Page size for results."""
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
  def page_token(self) -> str:
    """Page token used for pagination."""
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  def endpoint(self):
    path = '/api/v1/discussions/{topic_id}/comments'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/discussions/{topic_id}/comments'


class ApiListCommentsResponse(KaggleObject):
  r"""
  Attributes:
    comments (ApiDiscussionComment)
    next_page_token (str)
  """

  def __init__(self):
    self._comments = []
    self._next_page_token = ""
    self._freeze()

  @property
  def comments(self) -> Optional[List[Optional['ApiDiscussionComment']]]:
    return self._comments

  @comments.setter
  def comments(self, comments: Optional[List[Optional['ApiDiscussionComment']]]):
    if comments is None:
      del self.comments
      return
    if not isinstance(comments, list):
      raise TypeError('comments must be of type list')
    if not all([isinstance(t, ApiDiscussionComment) for t in comments]):
      raise TypeError('comments must contain only items of type ApiDiscussionComment')
    self._comments = comments

  @property
  def next_page_token(self) -> str:
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
  def nextPageToken(self):
    return self.next_page_token


class ApiListForumsRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/discussions/forums/list'
    return path.format_map(self.to_field_map(self))


class ApiListForumsResponse(KaggleObject):
  r"""
  Attributes:
    forums (ApiDiscussionForum)
  """

  def __init__(self):
    self._forums = []
    self._freeze()

  @property
  def forums(self) -> Optional[List[Optional['ApiDiscussionForum']]]:
    return self._forums

  @forums.setter
  def forums(self, forums: Optional[List[Optional['ApiDiscussionForum']]]):
    if forums is None:
      del self.forums
      return
    if not isinstance(forums, list):
      raise TypeError('forums must be of type list')
    if not all([isinstance(t, ApiDiscussionForum) for t in forums]):
      raise TypeError('forums must contain only items of type ApiDiscussionForum')
    self._forums = forums


class ApiListTopicsRequest(KaggleObject):
  r"""
  Attributes:
    forum_slug (str)
      Optional forum slug to filter topics by (e.g. 'getting-started',
      'product-feedback'). If not specified, returns topics across all forums.
    sort_by (TopicListSortBy)
      Sort order for the results.
    page_size (int)
      Page size for results.
    search_query (str)
      Optional search query to filter topics by.
    category (TopicListCategory)
      Filter by topic category.
    group (TopicListGroup)
      Filter by topic group.
    page_token (str)
      Page token used for pagination.
  """

  def __init__(self):
    self._forum_slug = None
    self._sort_by = None
    self._page_size = None
    self._search_query = None
    self._category = None
    self._group = None
    self._page_token = None
    self._freeze()

  @property
  def forum_slug(self) -> str:
    r"""
    Optional forum slug to filter topics by (e.g. 'getting-started',
    'product-feedback'). If not specified, returns topics across all forums.
    """
    return self._forum_slug or ""

  @forum_slug.setter
  def forum_slug(self, forum_slug: Optional[str]):
    if forum_slug is None:
      del self.forum_slug
      return
    if not isinstance(forum_slug, str):
      raise TypeError('forum_slug must be of type str')
    self._forum_slug = forum_slug

  @property
  def sort_by(self) -> 'TopicListSortBy':
    """Sort order for the results."""
    return self._sort_by or TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED

  @sort_by.setter
  def sort_by(self, sort_by: Optional['TopicListSortBy']):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, TopicListSortBy):
      raise TypeError('sort_by must be of type TopicListSortBy')
    self._sort_by = sort_by

  @property
  def page_size(self) -> int:
    """Page size for results."""
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
  def page_token(self) -> str:
    """Page token used for pagination."""
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
  def search_query(self) -> str:
    """Optional search query to filter topics by."""
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def category(self) -> 'TopicListCategory':
    """Filter by topic category."""
    return self._category or TopicListCategory.TOPIC_LIST_CATEGORY_UNSPECIFIED

  @category.setter
  def category(self, category: Optional['TopicListCategory']):
    if category is None:
      del self.category
      return
    if not isinstance(category, TopicListCategory):
      raise TypeError('category must be of type TopicListCategory')
    self._category = category

  @property
  def group(self) -> 'TopicListGroup':
    """Filter by topic group."""
    return self._group or TopicListGroup.TOPIC_LIST_GROUP_UNSPECIFIED

  @group.setter
  def group(self, group: Optional['TopicListGroup']):
    if group is None:
      del self.group
      return
    if not isinstance(group, TopicListGroup):
      raise TypeError('group must be of type TopicListGroup')
    self._group = group

  def endpoint(self):
    path = '/api/v1/discussions/topics/list'
    return path.format_map(self.to_field_map(self))


class ApiListTopicsResponse(KaggleObject):
  r"""
  Attributes:
    topics (ApiDiscussionTopic)
    total_count (int)
    next_page_token (str)
  """

  def __init__(self):
    self._topics = []
    self._total_count = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def topics(self) -> Optional[List[Optional['ApiDiscussionTopic']]]:
    return self._topics

  @topics.setter
  def topics(self, topics: Optional[List[Optional['ApiDiscussionTopic']]]):
    if topics is None:
      del self.topics
      return
    if not isinstance(topics, list):
      raise TypeError('topics must be of type list')
    if not all([isinstance(t, ApiDiscussionTopic) for t in topics]):
      raise TypeError('topics must contain only items of type ApiDiscussionTopic')
    self._topics = topics

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def next_page_token(self) -> str:
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
  def totalCount(self):
    return self.total_count

  @property
  def nextPageToken(self):
    return self.next_page_token


ApiDiscussionComment._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("authorName", "author_name", "_author_name", str, "", PredefinedSerializer()),
  FieldMetadata("authorUrl", "author_url", "_author_url", str, "", PredefinedSerializer()),
  FieldMetadata("postDate", "post_date", "_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("votes", "votes", "_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("replies", "replies", "_replies", ApiDiscussionComment, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDiscussionForum._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
]

ApiDiscussionTopic._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("postDate", "post_date", "_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastCommentDate", "last_comment_date", "_last_comment_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("authorName", "author_name", "_author_name", str, "", PredefinedSerializer()),
  FieldMetadata("authorUrl", "author_url", "_author_url", str, "", PredefinedSerializer()),
  FieldMetadata("votes", "votes", "_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("commentCount", "comment_count", "_comment_count", int, 0, PredefinedSerializer()),
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("content", "content", "_content", str, None, PredefinedSerializer(), optional=True),
]

ApiGetTopicRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

ApiGetTopicResponse._fields = [
  FieldMetadata("topic", "topic", "_topic", ApiDiscussionTopic, None, KaggleObjectSerializer()),
]

ApiListCommentsRequest._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListCommentsResponse._fields = [
  FieldMetadata("comments", "comments", "_comments", ApiDiscussionComment, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListForumsRequest._fields = []

ApiListForumsResponse._fields = [
  FieldMetadata("forums", "forums", "_forums", ApiDiscussionForum, [], ListSerializer(KaggleObjectSerializer())),
]

ApiListTopicsRequest._fields = [
  FieldMetadata("forumSlug", "forum_slug", "_forum_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", TopicListSortBy, None, EnumSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", TopicListCategory, None, EnumSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", TopicListGroup, None, EnumSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListTopicsResponse._fields = [
  FieldMetadata("topics", "topics", "_topics", ApiDiscussionTopic, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

