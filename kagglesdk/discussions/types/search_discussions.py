import enum
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_service import WriteUpItemInfo
from typing import Optional, List

class SearchDiscussionsDocumentType(enum.Enum):
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_COMMENT = 1
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_TOPIC = 2
  SEARCH_DISCUSSIONS_DOCUMENT_TYPE_WRITE_UP = 3

class SearchDiscussionsOrderBy(enum.Enum):
  SEARCH_DISCUSSIONS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_ORDER_BY_LAST_TOPIC_COMMENT_DATE = 1

class SearchDiscussionsSourceType(enum.Enum):
  SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_SOURCE_TYPE_COMPETITION = 1
  SEARCH_DISCUSSIONS_SOURCE_TYPE_DATASET = 2
  SEARCH_DISCUSSIONS_SOURCE_TYPE_KERNEL = 4
  SEARCH_DISCUSSIONS_SOURCE_TYPE_SITE_FORUM = 5
  SEARCH_DISCUSSIONS_SOURCE_TYPE_COMPETITION_SOLUTION = 6
  SEARCH_DISCUSSIONS_SOURCE_TYPE_MODEL = 7
  SEARCH_DISCUSSIONS_SOURCE_TYPE_WRITE_UP = 8
  SEARCH_DISCUSSIONS_SOURCE_TYPE_LEARN_TRACK = 9
  SEARCH_DISCUSSIONS_SOURCE_TYPE_BENCHMARK = 10
  SEARCH_DISCUSSIONS_SOURCE_TYPE_BENCHMARK_TASK = 11

class SearchDiscussionsTopicType(enum.Enum):
  SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED = 0
  SEARCH_DISCUSSIONS_TOPIC_TYPE_TOPICS = 1
  SEARCH_DISCUSSIONS_TOPIC_TYPE_WRITE_UPS = 2

class WriteUpInclusionType(enum.Enum):
  WRITE_UP_INCLUSION_TYPE_UNSPECIFIED = 0
  WRITE_UP_INCLUSION_TYPE_EXCLUDE = 1
  r"""
  Only ForumTopics will be included, while
  WriteUps will be excluded
  """
  WRITE_UP_INCLUSION_TYPE_INCLUDE = 2
  """WriteUps and ForumTopics will be included"""
  WRITE_UP_INCLUSION_TYPE_ONLY = 3
  r"""
  Only WriteUps will be included, while
  ForumTopics will be excluded
  """

class SearchDiscussionsDocument(KaggleObject):
  r"""
  Attributes:
    new_comment_url (str)
    message_stripped (str)
      The message of the topic/comment, stripped of HTML (at time of index)
    message_markdown (str)
      The markdown for the message of the topic/comment
    forum_name (str)
      The name of the parent forum
    forum_url (str)
      The URL for the parent forum
    source_type (SearchDiscussionsSourceType)
      The source type of the comment
    topic_type (SearchDiscussionsTopicType)
      The type of topic returned
    type (SearchDiscussionsDocumentType)
      The type of document returned
    write_up_metadata (WriteUpItemInfo)
      If the document is a WriteUp, extra WriteUp-specific data
      is provided
  """

  def __init__(self):
    self._new_comment_url = None
    self._message_stripped = ""
    self._message_markdown = None
    self._forum_name = ""
    self._forum_url = None
    self._source_type = SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED
    self._topic_type = SearchDiscussionsTopicType.SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED
    self._type = SearchDiscussionsDocumentType.SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED
    self._write_up_metadata = None
    self._freeze()

  @property
  def new_comment_url(self) -> str:
    return self._new_comment_url or ""

  @new_comment_url.setter
  def new_comment_url(self, new_comment_url: Optional[str]):
    if new_comment_url is None:
      del self.new_comment_url
      return
    if not isinstance(new_comment_url, str):
      raise TypeError('new_comment_url must be of type str')
    self._new_comment_url = new_comment_url

  @property
  def message_stripped(self) -> str:
    """The message of the topic/comment, stripped of HTML (at time of index)"""
    return self._message_stripped

  @message_stripped.setter
  def message_stripped(self, message_stripped: str):
    if message_stripped is None:
      del self.message_stripped
      return
    if not isinstance(message_stripped, str):
      raise TypeError('message_stripped must be of type str')
    self._message_stripped = message_stripped

  @property
  def message_markdown(self) -> str:
    """The markdown for the message of the topic/comment"""
    return self._message_markdown or ""

  @message_markdown.setter
  def message_markdown(self, message_markdown: Optional[str]):
    if message_markdown is None:
      del self.message_markdown
      return
    if not isinstance(message_markdown, str):
      raise TypeError('message_markdown must be of type str')
    self._message_markdown = message_markdown

  @property
  def forum_name(self) -> str:
    """The name of the parent forum"""
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
  def forum_url(self) -> str:
    """The URL for the parent forum"""
    return self._forum_url or ""

  @forum_url.setter
  def forum_url(self, forum_url: Optional[str]):
    if forum_url is None:
      del self.forum_url
      return
    if not isinstance(forum_url, str):
      raise TypeError('forum_url must be of type str')
    self._forum_url = forum_url

  @property
  def source_type(self) -> 'SearchDiscussionsSourceType':
    """The source type of the comment"""
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'SearchDiscussionsSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, SearchDiscussionsSourceType):
      raise TypeError('source_type must be of type SearchDiscussionsSourceType')
    self._source_type = source_type

  @property
  def topic_type(self) -> 'SearchDiscussionsTopicType':
    """The type of topic returned"""
    return self._topic_type

  @topic_type.setter
  def topic_type(self, topic_type: 'SearchDiscussionsTopicType'):
    if topic_type is None:
      del self.topic_type
      return
    if not isinstance(topic_type, SearchDiscussionsTopicType):
      raise TypeError('topic_type must be of type SearchDiscussionsTopicType')
    self._topic_type = topic_type

  @property
  def type(self) -> 'SearchDiscussionsDocumentType':
    """The type of document returned"""
    return self._type

  @type.setter
  def type(self, type: 'SearchDiscussionsDocumentType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, SearchDiscussionsDocumentType):
      raise TypeError('type must be of type SearchDiscussionsDocumentType')
    self._type = type

  @property
  def write_up_metadata(self) -> Optional['WriteUpItemInfo']:
    r"""
    If the document is a WriteUp, extra WriteUp-specific data
    is provided
    """
    return self._write_up_metadata or None

  @write_up_metadata.setter
  def write_up_metadata(self, write_up_metadata: Optional[Optional['WriteUpItemInfo']]):
    if write_up_metadata is None:
      del self.write_up_metadata
      return
    if not isinstance(write_up_metadata, WriteUpItemInfo):
      raise TypeError('write_up_metadata must be of type WriteUpItemInfo')
    self._write_up_metadata = write_up_metadata


class SearchDiscussionsFilters(KaggleObject):
  r"""
  Attributes:
    source_type (SearchDiscussionsSourceType)
      The discussion source type used to filter the documents
    only_new_comments (bool)
      Show only topics with new comments
    write_up_inclusion_type (WriteUpInclusionType)
      Determines whether or not WriteUps should be included
    write_up_types (WriteUpType)
      Filters on WriteUp type
    hackathon_track_ids (int)
      The hackathon track ids
  """

  def __init__(self):
    self._source_type = SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED
    self._only_new_comments = False
    self._write_up_inclusion_type = WriteUpInclusionType.WRITE_UP_INCLUSION_TYPE_UNSPECIFIED
    self._write_up_types = []
    self._hackathon_track_ids = []
    self._freeze()

  @property
  def source_type(self) -> 'SearchDiscussionsSourceType':
    """The discussion source type used to filter the documents"""
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'SearchDiscussionsSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, SearchDiscussionsSourceType):
      raise TypeError('source_type must be of type SearchDiscussionsSourceType')
    self._source_type = source_type

  @property
  def only_new_comments(self) -> bool:
    """Show only topics with new comments"""
    return self._only_new_comments

  @only_new_comments.setter
  def only_new_comments(self, only_new_comments: bool):
    if only_new_comments is None:
      del self.only_new_comments
      return
    if not isinstance(only_new_comments, bool):
      raise TypeError('only_new_comments must be of type bool')
    self._only_new_comments = only_new_comments

  @property
  def write_up_inclusion_type(self) -> 'WriteUpInclusionType':
    """Determines whether or not WriteUps should be included"""
    return self._write_up_inclusion_type

  @write_up_inclusion_type.setter
  def write_up_inclusion_type(self, write_up_inclusion_type: 'WriteUpInclusionType'):
    if write_up_inclusion_type is None:
      del self.write_up_inclusion_type
      return
    if not isinstance(write_up_inclusion_type, WriteUpInclusionType):
      raise TypeError('write_up_inclusion_type must be of type WriteUpInclusionType')
    self._write_up_inclusion_type = write_up_inclusion_type

  @property
  def write_up_types(self) -> Optional[List['WriteUpType']]:
    """Filters on WriteUp type"""
    return self._write_up_types

  @write_up_types.setter
  def write_up_types(self, write_up_types: Optional[List['WriteUpType']]):
    if write_up_types is None:
      del self.write_up_types
      return
    if not isinstance(write_up_types, list):
      raise TypeError('write_up_types must be of type list')
    if not all([isinstance(t, WriteUpType) for t in write_up_types]):
      raise TypeError('write_up_types must contain only items of type WriteUpType')
    self._write_up_types = write_up_types

  @property
  def hackathon_track_ids(self) -> Optional[List[int]]:
    """The hackathon track ids"""
    return self._hackathon_track_ids

  @hackathon_track_ids.setter
  def hackathon_track_ids(self, hackathon_track_ids: Optional[List[int]]):
    if hackathon_track_ids is None:
      del self.hackathon_track_ids
      return
    if not isinstance(hackathon_track_ids, list):
      raise TypeError('hackathon_track_ids must be of type list')
    if not all([isinstance(t, int) for t in hackathon_track_ids]):
      raise TypeError('hackathon_track_ids must contain only items of type int')
    self._hackathon_track_ids = hackathon_track_ids


SearchDiscussionsDocument._fields = [
  FieldMetadata("newCommentUrl", "new_comment_url", "_new_comment_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageStripped", "message_stripped", "_message_stripped", str, "", PredefinedSerializer()),
  FieldMetadata("messageMarkdown", "message_markdown", "_message_markdown", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("forumUrl", "forum_url", "_forum_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceType", "source_type", "_source_type", SearchDiscussionsSourceType, SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("topicType", "topic_type", "_topic_type", SearchDiscussionsTopicType, SearchDiscussionsTopicType.SEARCH_DISCUSSIONS_TOPIC_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", SearchDiscussionsDocumentType, SearchDiscussionsDocumentType.SEARCH_DISCUSSIONS_DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("writeUpMetadata", "write_up_metadata", "_write_up_metadata", WriteUpItemInfo, None, KaggleObjectSerializer(), optional=True),
]

SearchDiscussionsFilters._fields = [
  FieldMetadata("sourceType", "source_type", "_source_type", SearchDiscussionsSourceType, SearchDiscussionsSourceType.SEARCH_DISCUSSIONS_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("onlyNewComments", "only_new_comments", "_only_new_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("writeUpInclusionType", "write_up_inclusion_type", "_write_up_inclusion_type", WriteUpInclusionType, WriteUpInclusionType.WRITE_UP_INCLUSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("writeUpTypes", "write_up_types", "_write_up_types", WriteUpType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
]

