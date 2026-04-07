from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.discussions.types.discussions_enums import CommentListFilter, CommentListSortBy, EmojiReaction, ForumMessageSettings, ForumSettings, ForumTopicSettings, TopicListAuthor, TopicListCategory, TopicListGroup, TopicListMyActivity, TopicListRecency, TopicListSortBy
from kagglesdk.discussions.types.feedback_tracking_data import FeedbackTrackingData
from kagglesdk.discussions.types.forum import Forum
from kagglesdk.discussions.types.forum_message import CommentForumMessage
from kagglesdk.discussions.types.forum_topic import ForumTopic
from kagglesdk.discussions.types.topic_list_item import TopicListItem
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user import User
from typing import List, Optional

class BatchDeleteMessageRequest(KaggleObject):
  r"""
  Attributes:
    message_ids (int)
    reason (str)
  """

  def __init__(self):
    self._message_ids = []
    self._reason = ""
    self._freeze()

  @property
  def message_ids(self) -> Optional[List[int]]:
    return self._message_ids

  @message_ids.setter
  def message_ids(self, message_ids: Optional[List[int]]):
    if message_ids is None:
      del self.message_ids
      return
    if not isinstance(message_ids, list):
      raise TypeError('message_ids must be of type list')
    if not all([isinstance(t, int) for t in message_ids]):
      raise TypeError('message_ids must contain only items of type int')
    self._message_ids = message_ids

  @property
  def reason(self) -> str:
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class BatchGetForumMessagesRequest(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
      The topic containing all the forum messages to be retrieved. Enables a
      singular permissions check.
    message_ids (int)
      The list of forum messages to retrieve. Must all be under the given topic.
    read_mask (FieldMask)
      Which fields to return, or null to return all fields.
  """

  def __init__(self):
    self._topic_id = 0
    self._message_ids = []
    self._read_mask = None
    self._freeze()

  @property
  def topic_id(self) -> int:
    r"""
    The topic containing all the forum messages to be retrieved. Enables a
    singular permissions check.
    """
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
  def message_ids(self) -> Optional[List[int]]:
    """The list of forum messages to retrieve. Must all be under the given topic."""
    return self._message_ids

  @message_ids.setter
  def message_ids(self, message_ids: Optional[List[int]]):
    if message_ids is None:
      del self.message_ids
      return
    if not isinstance(message_ids, list):
      raise TypeError('message_ids must be of type list')
    if not all([isinstance(t, int) for t in message_ids]):
      raise TypeError('message_ids must contain only items of type int')
    self._message_ids = message_ids

  @property
  def read_mask(self) -> FieldMask:
    """Which fields to return, or null to return all fields."""
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class BatchGetForumMessagesResponse(KaggleObject):
  r"""
  Attributes:
    messages (CommentForumMessage)
      The list of messages matching the ids, returned in the same order as in the
      request.
  """

  def __init__(self):
    self._messages = []
    self._freeze()

  @property
  def messages(self) -> Optional[List[Optional['CommentForumMessage']]]:
    r"""
    The list of messages matching the ids, returned in the same order as in the
    request.
    """
    return self._messages

  @messages.setter
  def messages(self, messages: Optional[List[Optional['CommentForumMessage']]]):
    if messages is None:
      del self.messages
      return
    if not isinstance(messages, list):
      raise TypeError('messages must be of type list')
    if not all([isinstance(t, CommentForumMessage) for t in messages]):
      raise TypeError('messages must contain only items of type CommentForumMessage')
    self._messages = messages


class BlobCreationInfo(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque string token used to reference the new BlobFile.
    create_url (str)
      URL to use to start the upload.
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque string token used to reference the new BlobFile."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def create_url(self) -> str:
    """URL to use to start the upload."""
    return self._create_url

  @create_url.setter
  def create_url(self, create_url: str):
    if create_url is None:
      del self.create_url
      return
    if not isinstance(create_url, str):
      raise TypeError('create_url must be of type str')
    self._create_url = create_url


class BlobFileInfo(KaggleObject):
  r"""
  Attributes:
    name (str)
      The name of the file, minus any path segments.
    content_type (str)
      The content type of the file.
    content_length (int)
      The total size (bytes) of the file.
    last_modified_date (datetime)
      The date last modified, used to help determine whether the file has been
      updated since previous uploads.
  """

  def __init__(self):
    self._name = ""
    self._content_type = ""
    self._content_length = 0
    self._last_modified_date = None
    self._freeze()

  @property
  def name(self) -> str:
    """The name of the file, minus any path segments."""
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
  def content_type(self) -> str:
    """The content type of the file."""
    return self._content_type

  @content_type.setter
  def content_type(self, content_type: str):
    if content_type is None:
      del self.content_type
      return
    if not isinstance(content_type, str):
      raise TypeError('content_type must be of type str')
    self._content_type = content_type

  @property
  def content_length(self) -> int:
    """The total size (bytes) of the file."""
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def last_modified_date(self) -> datetime:
    r"""
    The date last modified, used to help determine whether the file has been
    updated since previous uploads.
    """
    return self._last_modified_date

  @last_modified_date.setter
  def last_modified_date(self, last_modified_date: datetime):
    if last_modified_date is None:
      del self.last_modified_date
      return
    if not isinstance(last_modified_date, datetime):
      raise TypeError('last_modified_date must be of type datetime')
    self._last_modified_date = last_modified_date


class CreateAttachmentRequest(KaggleObject):
  r"""
  Attributes:
    blob_file_info (BlobFileInfo)
      The info for the blob file being created.
  """

  def __init__(self):
    self._blob_file_info = None
    self._freeze()

  @property
  def blob_file_info(self) -> Optional['BlobFileInfo']:
    """The info for the blob file being created."""
    return self._blob_file_info

  @blob_file_info.setter
  def blob_file_info(self, blob_file_info: Optional['BlobFileInfo']):
    if blob_file_info is None:
      del self.blob_file_info
      return
    if not isinstance(blob_file_info, BlobFileInfo):
      raise TypeError('blob_file_info must be of type BlobFileInfo')
    self._blob_file_info = blob_file_info


class CreateAttachmentResponse(KaggleObject):
  r"""
  Attributes:
    blob_creation_info (BlobCreationInfo)
      The info used for creating a blob.
  """

  def __init__(self):
    self._blob_creation_info = None
    self._freeze()

  @property
  def blob_creation_info(self) -> Optional['BlobCreationInfo']:
    """The info used for creating a blob."""
    return self._blob_creation_info

  @blob_creation_info.setter
  def blob_creation_info(self, blob_creation_info: Optional['BlobCreationInfo']):
    if blob_creation_info is None:
      del self.blob_creation_info
      return
    if not isinstance(blob_creation_info, BlobCreationInfo):
      raise TypeError('blob_creation_info must be of type BlobCreationInfo')
    self._blob_creation_info = blob_creation_info


class CreateKernelMessageRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
      The kernel ID to create the message on.
    message (Message)
      The message content & blobs.
  """

  def __init__(self):
    self._kernel_id = 0
    self._message = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    """The kernel ID to create the message on."""
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs."""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message


class CreateKernelMessageResponse(KaggleObject):
  r"""
  Attributes:
    message_id (int)
      The created message ID.
    topic_id (int)
      The topic ID associated with the kernel messages.
  """

  def __init__(self):
    self._message_id = 0
    self._topic_id = 0
    self._freeze()

  @property
  def message_id(self) -> int:
    """The created message ID."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def topic_id(self) -> int:
    """The topic ID associated with the kernel messages."""
    return self._topic_id

  @topic_id.setter
  def topic_id(self, topic_id: int):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id


class CreateReplyRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
      The message ID of the parent message being replied to.
    message (Message)
      The message content & blobs.
  """

  def __init__(self):
    self._message_id = 0
    self._message = None
    self._freeze()

  @property
  def message_id(self) -> int:
    """The message ID of the parent message being replied to."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs."""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message


class CreateReplyResponse(KaggleObject):
  r"""
  Attributes:
    message_id (int)
      The created message ID.
  """

  def __init__(self):
    self._message_id = 0
    self._freeze()

  @property
  def message_id(self) -> int:
    """The created message ID."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id


class CreateTopicRequest(KaggleObject):
  r"""
  Attributes:
    forum_id (int)
      The forum ID of the parent forum for the topic being created.
    topic_name (str)
      The name of the topic being created.
    message (Message)
      The message content & blobs.
    tag_ids (int)
      Optional tags to add to the forum topic
  """

  def __init__(self):
    self._forum_id = 0
    self._topic_name = ""
    self._message = None
    self._tag_ids = []
    self._freeze()

  @property
  def forum_id(self) -> int:
    """The forum ID of the parent forum for the topic being created."""
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
  def topic_name(self) -> str:
    """The name of the topic being created."""
    return self._topic_name

  @topic_name.setter
  def topic_name(self, topic_name: str):
    if topic_name is None:
      del self.topic_name
      return
    if not isinstance(topic_name, str):
      raise TypeError('topic_name must be of type str')
    self._topic_name = topic_name

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs."""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """Optional tags to add to the forum topic"""
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids


class CreateTopicResponse(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
      The created topic ID.
    message_id (int)
      The created message ID.
  """

  def __init__(self):
    self._topic_id = 0
    self._message_id = 0
    self._freeze()

  @property
  def topic_id(self) -> int:
    """The created topic ID."""
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
  def message_id(self) -> int:
    """The created message ID."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id


class DeleteAttachmentRequest(KaggleObject):
  r"""
  Attributes:
    attachment_id (int)
      The ForumMessageAttachmentFiles.Id of the file to delete.
  """

  def __init__(self):
    self._attachment_id = 0
    self._freeze()

  @property
  def attachment_id(self) -> int:
    """The ForumMessageAttachmentFiles.Id of the file to delete."""
    return self._attachment_id

  @attachment_id.setter
  def attachment_id(self, attachment_id: int):
    if attachment_id is None:
      del self.attachment_id
      return
    if not isinstance(attachment_id, int):
      raise TypeError('attachment_id must be of type int')
    self._attachment_id = attachment_id


class DeleteMessageRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
    notes (str)
  """

  def __init__(self):
    self._message_id = 0
    self._notes = None
    self._freeze()

  @property
  def message_id(self) -> int:
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def notes(self) -> str:
    return self._notes or ""

  @notes.setter
  def notes(self, notes: Optional[str]):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


class DeleteTopicRequest(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
  """

  def __init__(self):
    self._topic_id = 0
    self._freeze()

  @property
  def topic_id(self) -> int:
    return self._topic_id

  @topic_id.setter
  def topic_id(self, topic_id: int):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id


class GetForumMessagesInTopicRequest(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
    initial_page_size (int)
      How many comments to pre-load. The rest of the comments will be included as
      just ids. Defaults to 30 if not otherwise specified. Pass -1 to load all
      comments.
    new_user_sort (CommentListSortBy)
    filter (CommentListFilter)
    include_first_forum_message (bool)
    starting_comment_id (int)
      If provided, the pre-loaded comments will start from this comment id rather
      than the first in the topic.
  """

  def __init__(self):
    self._topic_id = 0
    self._initial_page_size = None
    self._new_user_sort = CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED
    self._filter = CommentListFilter.ALL
    self._include_first_forum_message = False
    self._starting_comment_id = None
    self._freeze()

  @property
  def topic_id(self) -> int:
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
  def initial_page_size(self) -> int:
    r"""
    How many comments to pre-load. The rest of the comments will be included as
    just ids. Defaults to 30 if not otherwise specified. Pass -1 to load all
    comments.
    """
    return self._initial_page_size or 0

  @initial_page_size.setter
  def initial_page_size(self, initial_page_size: Optional[int]):
    if initial_page_size is None:
      del self.initial_page_size
      return
    if not isinstance(initial_page_size, int):
      raise TypeError('initial_page_size must be of type int')
    self._initial_page_size = initial_page_size

  @property
  def starting_comment_id(self) -> int:
    r"""
    If provided, the pre-loaded comments will start from this comment id rather
    than the first in the topic.
    """
    return self._starting_comment_id or 0

  @starting_comment_id.setter
  def starting_comment_id(self, starting_comment_id: Optional[int]):
    if starting_comment_id is None:
      del self.starting_comment_id
      return
    if not isinstance(starting_comment_id, int):
      raise TypeError('starting_comment_id must be of type int')
    self._starting_comment_id = starting_comment_id

  @property
  def new_user_sort(self) -> 'CommentListSortBy':
    return self._new_user_sort

  @new_user_sort.setter
  def new_user_sort(self, new_user_sort: 'CommentListSortBy'):
    if new_user_sort is None:
      del self.new_user_sort
      return
    if not isinstance(new_user_sort, CommentListSortBy):
      raise TypeError('new_user_sort must be of type CommentListSortBy')
    self._new_user_sort = new_user_sort

  @property
  def filter(self) -> 'CommentListFilter':
    return self._filter

  @filter.setter
  def filter(self, filter: 'CommentListFilter'):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, CommentListFilter):
      raise TypeError('filter must be of type CommentListFilter')
    self._filter = filter

  @property
  def include_first_forum_message(self) -> bool:
    return self._include_first_forum_message

  @include_first_forum_message.setter
  def include_first_forum_message(self, include_first_forum_message: bool):
    if include_first_forum_message is None:
      del self.include_first_forum_message
      return
    if not isinstance(include_first_forum_message, bool):
      raise TypeError('include_first_forum_message must be of type bool')
    self._include_first_forum_message = include_first_forum_message


class GetForumMessagesInTopicResponse(KaggleObject):
  r"""
  Attributes:
    comments (CommentForumMessage)
    comment_sort (CommentListSortBy)
  """

  def __init__(self):
    self._comments = []
    self._comment_sort = CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED
    self._freeze()

  @property
  def comments(self) -> Optional[List[Optional['CommentForumMessage']]]:
    return self._comments

  @comments.setter
  def comments(self, comments: Optional[List[Optional['CommentForumMessage']]]):
    if comments is None:
      del self.comments
      return
    if not isinstance(comments, list):
      raise TypeError('comments must be of type list')
    if not all([isinstance(t, CommentForumMessage) for t in comments]):
      raise TypeError('comments must contain only items of type CommentForumMessage')
    self._comments = comments

  @property
  def comment_sort(self) -> 'CommentListSortBy':
    return self._comment_sort

  @comment_sort.setter
  def comment_sort(self, comment_sort: 'CommentListSortBy'):
    if comment_sort is None:
      del self.comment_sort
      return
    if not isinstance(comment_sort, CommentListSortBy):
      raise TypeError('comment_sort must be of type CommentListSortBy')
    self._comment_sort = comment_sort


class GetForumMessageUpvotesRequest(KaggleObject):
  r"""
  Attributes:
    forum_message_id (int)
      The forum message to retrieve upvote information on.
  """

  def __init__(self):
    self._forum_message_id = 0
    self._freeze()

  @property
  def forum_message_id(self) -> int:
    """The forum message to retrieve upvote information on."""
    return self._forum_message_id

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id


class GetForumMessageUpvotesResponse(KaggleObject):
  r"""
  Attributes:
    upvoters (User)
      The list of users who upvoted this forum message. Note the user object
      isn't fully populated, contains just the fields UpvoteDialog needs
      (ThumbnailUrl, DisplayName, ProfileUrl, Id, PerformanceTier, UserName).
      Long term this should probably return a more appropriate proto, but will
      need a larger rework of the KM Upvote Dialog.
  """

  def __init__(self):
    self._upvoters = []
    self._freeze()

  @property
  def upvoters(self) -> Optional[List[Optional['User']]]:
    r"""
    The list of users who upvoted this forum message. Note the user object
    isn't fully populated, contains just the fields UpvoteDialog needs
    (ThumbnailUrl, DisplayName, ProfileUrl, Id, PerformanceTier, UserName).
    Long term this should probably return a more appropriate proto, but will
    need a larger rework of the KM Upvote Dialog.
    """
    return self._upvoters

  @upvoters.setter
  def upvoters(self, upvoters: Optional[List[Optional['User']]]):
    if upvoters is None:
      del self.upvoters
      return
    if not isinstance(upvoters, list):
      raise TypeError('upvoters must be of type list')
    if not all([isinstance(t, User) for t in upvoters]):
      raise TypeError('upvoters must contain only items of type User')
    self._upvoters = upvoters


class GetForumRequest(KaggleObject):
  r"""
  Attributes:
    forum_id (int)
    forum_slug (str)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._forum_id = None
    self._forum_slug = None
    self._read_mask = None
    self._freeze()

  @property
  def forum_id(self) -> int:
    return self._forum_id or 0

  @forum_id.setter
  def forum_id(self, forum_id: int):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    del self.forum_slug
    self._forum_id = forum_id

  @property
  def forum_slug(self) -> str:
    return self._forum_slug or ""

  @forum_slug.setter
  def forum_slug(self, forum_slug: str):
    if forum_slug is None:
      del self.forum_slug
      return
    if not isinstance(forum_slug, str):
      raise TypeError('forum_slug must be of type str')
    del self.forum_id
    self._forum_slug = forum_slug

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask or None

  @read_mask.setter
  def read_mask(self, read_mask: Optional[FieldMask]):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetForumResponse(KaggleObject):
  r"""
  Attributes:
    forum (Forum)
    topic_sort (TopicListSortBy)
  """

  def __init__(self):
    self._forum = None
    self._topic_sort = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._freeze()

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


class GetForumTopicByIdRequest(KaggleObject):
  r"""
  Attributes:
    forum_topic_id (int)
      TODO: Add authorization once GetForumTopicsByIdRequest has been properly
      migrated, otherwise adding authz here will result in double permissions
      invocations.
    include_comments (bool)
    read_mask (FieldMask)
    initial_page_size (int)
      How many comments to load for the first page. The rest will be just ids and
      can be loaded on demand. Defaults to 30 if not otherwise specified. Pass -1
      to load all comments.
    starting_comment_id (int)
      If provided, the pre-loaded comments will start from this comment id rather
      than the first in the topic.
  """

  def __init__(self):
    self._forum_topic_id = 0
    self._include_comments = False
    self._read_mask = None
    self._initial_page_size = None
    self._starting_comment_id = None
    self._freeze()

  @property
  def forum_topic_id(self) -> int:
    r"""
    TODO: Add authorization once GetForumTopicsByIdRequest has been properly
    migrated, otherwise adding authz here will result in double permissions
    invocations.
    """
    return self._forum_topic_id

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id

  @property
  def include_comments(self) -> bool:
    return self._include_comments

  @include_comments.setter
  def include_comments(self, include_comments: bool):
    if include_comments is None:
      del self.include_comments
      return
    if not isinstance(include_comments, bool):
      raise TypeError('include_comments must be of type bool')
    self._include_comments = include_comments

  @property
  def initial_page_size(self) -> int:
    r"""
    How many comments to load for the first page. The rest will be just ids and
    can be loaded on demand. Defaults to 30 if not otherwise specified. Pass -1
    to load all comments.
    """
    return self._initial_page_size or 0

  @initial_page_size.setter
  def initial_page_size(self, initial_page_size: Optional[int]):
    if initial_page_size is None:
      del self.initial_page_size
      return
    if not isinstance(initial_page_size, int):
      raise TypeError('initial_page_size must be of type int')
    self._initial_page_size = initial_page_size

  @property
  def starting_comment_id(self) -> int:
    r"""
    If provided, the pre-loaded comments will start from this comment id rather
    than the first in the topic.
    """
    return self._starting_comment_id or 0

  @starting_comment_id.setter
  def starting_comment_id(self, starting_comment_id: Optional[int]):
    if starting_comment_id is None:
      del self.starting_comment_id
      return
    if not isinstance(starting_comment_id, int):
      raise TypeError('starting_comment_id must be of type int')
    self._starting_comment_id = starting_comment_id

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetForumTopicByIdResponse(KaggleObject):
  r"""
  Attributes:
    forum_topic (ForumTopic)
  """

  def __init__(self):
    self._forum_topic = None
    self._freeze()

  @property
  def forum_topic(self) -> Optional['ForumTopic']:
    return self._forum_topic

  @forum_topic.setter
  def forum_topic(self, forum_topic: Optional['ForumTopic']):
    if forum_topic is None:
      del self.forum_topic
      return
    if not isinstance(forum_topic, ForumTopic):
      raise TypeError('forum_topic must be of type ForumTopic')
    self._forum_topic = forum_topic


class GetSiteForumsRequest(KaggleObject):
  r"""
  """

  pass

class GetSiteForumsResponse(KaggleObject):
  r"""
  Attributes:
    forums (Forum)
    initial_sort_by (TopicListSortBy)
  """

  def __init__(self):
    self._forums = []
    self._initial_sort_by = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._freeze()

  @property
  def forums(self) -> Optional[List[Optional['Forum']]]:
    return self._forums

  @forums.setter
  def forums(self, forums: Optional[List[Optional['Forum']]]):
    if forums is None:
      del self.forums
      return
    if not isinstance(forums, list):
      raise TypeError('forums must be of type list')
    if not all([isinstance(t, Forum) for t in forums]):
      raise TypeError('forums must contain only items of type Forum')
    self._forums = forums

  @property
  def initial_sort_by(self) -> 'TopicListSortBy':
    return self._initial_sort_by

  @initial_sort_by.setter
  def initial_sort_by(self, initial_sort_by: 'TopicListSortBy'):
    if initial_sort_by is None:
      del self.initial_sort_by
      return
    if not isinstance(initial_sort_by, TopicListSortBy):
      raise TypeError('initial_sort_by must be of type TopicListSortBy')
    self._initial_sort_by = initial_sort_by


class GetTopicListByForumIdRequest(KaggleObject):
  r"""
  Attributes:
    category (TopicListCategory)
    forum_id (int)
    group (TopicListGroup)
    page (int)
    search_query (str)
    sort_by (TopicListSortBy)
    recency (TopicListRecency)
    my_activity (TopicListMyActivity)
    author (TopicListAuthor)
    filter_category_ids (int)
  """

  def __init__(self):
    self._category = TopicListCategory.TOPIC_LIST_CATEGORY_UNSPECIFIED
    self._forum_id = None
    self._group = TopicListGroup.TOPIC_LIST_GROUP_UNSPECIFIED
    self._page = 0
    self._search_query = None
    self._sort_by = TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED
    self._recency = TopicListRecency.TOPIC_LIST_RECENCY_UNSPECIFIED
    self._my_activity = TopicListMyActivity.TOPIC_LIST_MY_ACTIVITY_UNSPECIFIED
    self._author = TopicListAuthor.TOPIC_LIST_AUTHOR_UNSPECIFIED
    self._filter_category_ids = []
    self._freeze()

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

  @property
  def forum_id(self) -> int:
    return self._forum_id or 0

  @forum_id.setter
  def forum_id(self, forum_id: Optional[int]):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

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
  def search_query(self) -> str:
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
  def recency(self) -> 'TopicListRecency':
    return self._recency

  @recency.setter
  def recency(self, recency: 'TopicListRecency'):
    if recency is None:
      del self.recency
      return
    if not isinstance(recency, TopicListRecency):
      raise TypeError('recency must be of type TopicListRecency')
    self._recency = recency

  @property
  def my_activity(self) -> 'TopicListMyActivity':
    return self._my_activity

  @my_activity.setter
  def my_activity(self, my_activity: 'TopicListMyActivity'):
    if my_activity is None:
      del self.my_activity
      return
    if not isinstance(my_activity, TopicListMyActivity):
      raise TypeError('my_activity must be of type TopicListMyActivity')
    self._my_activity = my_activity

  @property
  def author(self) -> 'TopicListAuthor':
    return self._author

  @author.setter
  def author(self, author: 'TopicListAuthor'):
    if author is None:
      del self.author
      return
    if not isinstance(author, TopicListAuthor):
      raise TypeError('author must be of type TopicListAuthor')
    self._author = author

  @property
  def filter_category_ids(self) -> Optional[List[int]]:
    return self._filter_category_ids

  @filter_category_ids.setter
  def filter_category_ids(self, filter_category_ids: Optional[List[int]]):
    if filter_category_ids is None:
      del self.filter_category_ids
      return
    if not isinstance(filter_category_ids, list):
      raise TypeError('filter_category_ids must be of type list')
    if not all([isinstance(t, int) for t in filter_category_ids]):
      raise TypeError('filter_category_ids must contain only items of type int')
    self._filter_category_ids = filter_category_ids


class GetTopicListResponse(KaggleObject):
  r"""
  Attributes:
    topics (TopicListItem)
    count (int)
  """

  def __init__(self):
    self._topics = []
    self._count = 0
    self._freeze()

  @property
  def topics(self) -> Optional[List[Optional['TopicListItem']]]:
    return self._topics

  @topics.setter
  def topics(self, topics: Optional[List[Optional['TopicListItem']]]):
    if topics is None:
      del self.topics
      return
    if not isinstance(topics, list):
      raise TypeError('topics must be of type list')
    if not all([isinstance(t, TopicListItem) for t in topics]):
      raise TypeError('topics must contain only items of type TopicListItem')
    self._topics = topics

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class Message(KaggleObject):
  r"""
  Attributes:
    markdown (str)
      The markdown of the message.
    html (str)
      The HTML of the message.
    blob_file_tokens (str)
      The blob file tokens of the files attached to the message.
  """

  def __init__(self):
    self._markdown = ""
    self._html = ""
    self._blob_file_tokens = []
    self._freeze()

  @property
  def markdown(self) -> str:
    """The markdown of the message."""
    return self._markdown

  @markdown.setter
  def markdown(self, markdown: str):
    if markdown is None:
      del self.markdown
      return
    if not isinstance(markdown, str):
      raise TypeError('markdown must be of type str')
    self._markdown = markdown

  @property
  def html(self) -> str:
    """The HTML of the message."""
    return self._html

  @html.setter
  def html(self, html: str):
    if html is None:
      del self.html
      return
    if not isinstance(html, str):
      raise TypeError('html must be of type str')
    self._html = html

  @property
  def blob_file_tokens(self) -> Optional[List[str]]:
    """The blob file tokens of the files attached to the message."""
    return self._blob_file_tokens

  @blob_file_tokens.setter
  def blob_file_tokens(self, blob_file_tokens: Optional[List[str]]):
    if blob_file_tokens is None:
      del self.blob_file_tokens
      return
    if not isinstance(blob_file_tokens, list):
      raise TypeError('blob_file_tokens must be of type list')
    if not all([isinstance(t, str) for t in blob_file_tokens]):
      raise TypeError('blob_file_tokens must contain only items of type str')
    self._blob_file_tokens = blob_file_tokens


class MessageVote(KaggleObject):
  r"""
  This is implemented as a separate message so that we can authorize on both of
  these fields simultaneously

  Attributes:
    forum_message_id (int)
    score (int)
  """

  def __init__(self):
    self._forum_message_id = 0
    self._score = 0
    self._freeze()

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id

  @property
  def score(self) -> int:
    return self._score

  @score.setter
  def score(self, score: int):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score


class MoveForumTopicToForumRequest(KaggleObject):
  r"""
  Attributes:
    forum_topic_id (int)
    from_forum_id (int)
    to_forum_id (int)
  """

  def __init__(self):
    self._forum_topic_id = 0
    self._from_forum_id = 0
    self._to_forum_id = 0
    self._freeze()

  @property
  def forum_topic_id(self) -> int:
    return self._forum_topic_id

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id

  @property
  def from_forum_id(self) -> int:
    return self._from_forum_id

  @from_forum_id.setter
  def from_forum_id(self, from_forum_id: int):
    if from_forum_id is None:
      del self.from_forum_id
      return
    if not isinstance(from_forum_id, int):
      raise TypeError('from_forum_id must be of type int')
    self._from_forum_id = from_forum_id

  @property
  def to_forum_id(self) -> int:
    return self._to_forum_id

  @to_forum_id.setter
  def to_forum_id(self, to_forum_id: int):
    if to_forum_id is None:
      del self.to_forum_id
      return
    if not isinstance(to_forum_id, int):
      raise TypeError('to_forum_id must be of type int')
    self._to_forum_id = to_forum_id


class PinForumMessageRequest(KaggleObject):
  r"""
  Attributes:
    forum_message_id (int)
    is_pinned (bool)
  """

  def __init__(self):
    self._forum_message_id = 0
    self._is_pinned = False
    self._freeze()

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id

  @property
  def is_pinned(self) -> bool:
    return self._is_pinned

  @is_pinned.setter
  def is_pinned(self, is_pinned: bool):
    if is_pinned is None:
      del self.is_pinned
      return
    if not isinstance(is_pinned, bool):
      raise TypeError('is_pinned must be of type bool')
    self._is_pinned = is_pinned


class ReactToForumMessageRequest(KaggleObject):
  r"""
  Attributes:
    reaction (EmojiReaction)
    forum_message_id (int)
    should_add_reaction (bool)
  """

  def __init__(self):
    self._reaction = EmojiReaction.EMOJI_REACTION_UNSPECIFIED
    self._forum_message_id = 0
    self._should_add_reaction = False
    self._freeze()

  @property
  def reaction(self) -> 'EmojiReaction':
    return self._reaction

  @reaction.setter
  def reaction(self, reaction: 'EmojiReaction'):
    if reaction is None:
      del self.reaction
      return
    if not isinstance(reaction, EmojiReaction):
      raise TypeError('reaction must be of type EmojiReaction')
    self._reaction = reaction

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id

  @property
  def should_add_reaction(self) -> bool:
    return self._should_add_reaction

  @should_add_reaction.setter
  def should_add_reaction(self, should_add_reaction: bool):
    if should_add_reaction is None:
      del self.should_add_reaction
      return
    if not isinstance(should_add_reaction, bool):
      raise TypeError('should_add_reaction must be of type bool')
    self._should_add_reaction = should_add_reaction


class ToggleSpamMessageRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
  """

  def __init__(self):
    self._message_id = 0
    self._freeze()

  @property
  def message_id(self) -> int:
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id


class ToggleSpamMessageResponse(KaggleObject):
  r"""
  Attributes:
    message_url (str)
  """

  def __init__(self):
    self._message_url = ""
    self._freeze()

  @property
  def message_url(self) -> str:
    return self._message_url

  @message_url.setter
  def message_url(self, message_url: str):
    if message_url is None:
      del self.message_url
      return
    if not isinstance(message_url, str):
      raise TypeError('message_url must be of type str')
    self._message_url = message_url


class UpdateFeedbackTrackingDataRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
    feedback_tracking_data (FeedbackTrackingData)
  """

  def __init__(self):
    self._message_id = 0
    self._feedback_tracking_data = None
    self._freeze()

  @property
  def message_id(self) -> int:
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def feedback_tracking_data(self) -> Optional['FeedbackTrackingData']:
    return self._feedback_tracking_data

  @feedback_tracking_data.setter
  def feedback_tracking_data(self, feedback_tracking_data: Optional['FeedbackTrackingData']):
    if feedback_tracking_data is None:
      del self.feedback_tracking_data
      return
    if not isinstance(feedback_tracking_data, FeedbackTrackingData):
      raise TypeError('feedback_tracking_data must be of type FeedbackTrackingData')
    self._feedback_tracking_data = feedback_tracking_data


class UpdateForumMessageSettingsRequest(KaggleObject):
  r"""
  Attributes:
    forum_message_id (int)
    setting_to_toggle (ForumMessageSettings)
  """

  def __init__(self):
    self._forum_message_id = 0
    self._setting_to_toggle = ForumMessageSettings.FORUM_MESSAGE_SETTINGS_UNSPECIFIED
    self._freeze()

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id

  @property
  def setting_to_toggle(self) -> 'ForumMessageSettings':
    return self._setting_to_toggle

  @setting_to_toggle.setter
  def setting_to_toggle(self, setting_to_toggle: 'ForumMessageSettings'):
    if setting_to_toggle is None:
      del self.setting_to_toggle
      return
    if not isinstance(setting_to_toggle, ForumMessageSettings):
      raise TypeError('setting_to_toggle must be of type ForumMessageSettings')
    self._setting_to_toggle = setting_to_toggle


class UpdateForumSettingsRequest(KaggleObject):
  r"""
  Attributes:
    forum_id (int)
    setting_to_toggle (ForumSettings)
  """

  def __init__(self):
    self._forum_id = 0
    self._setting_to_toggle = ForumSettings.FORUM_SETTINGS_IS_READ_ONLY
    self._freeze()

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
  def setting_to_toggle(self) -> 'ForumSettings':
    return self._setting_to_toggle

  @setting_to_toggle.setter
  def setting_to_toggle(self, setting_to_toggle: 'ForumSettings'):
    if setting_to_toggle is None:
      del self.setting_to_toggle
      return
    if not isinstance(setting_to_toggle, ForumSettings):
      raise TypeError('setting_to_toggle must be of type ForumSettings')
    self._setting_to_toggle = setting_to_toggle


class UpdateForumTopicSettingsRequest(KaggleObject):
  r"""
  Attributes:
    forum_topic_id (int)
    setting_to_toggle (ForumTopicSettings)
       Indicates which field should be toggled
  """

  def __init__(self):
    self._forum_topic_id = 0
    self._setting_to_toggle = ForumTopicSettings.FORUM_TOPIC_SETTINGS_IS_READ_ONLY
    self._freeze()

  @property
  def forum_topic_id(self) -> int:
    return self._forum_topic_id

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id

  @property
  def setting_to_toggle(self) -> 'ForumTopicSettings':
    """ Indicates which field should be toggled"""
    return self._setting_to_toggle

  @setting_to_toggle.setter
  def setting_to_toggle(self, setting_to_toggle: 'ForumTopicSettings'):
    if setting_to_toggle is None:
      del self.setting_to_toggle
      return
    if not isinstance(setting_to_toggle, ForumTopicSettings):
      raise TypeError('setting_to_toggle must be of type ForumTopicSettings')
    self._setting_to_toggle = setting_to_toggle


class UpdateIsThankYouStatusRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
      The forum message to update.
    is_thank_you (bool)
      The new status of whether it's a thank you comment.
  """

  def __init__(self):
    self._message_id = 0
    self._is_thank_you = False
    self._freeze()

  @property
  def message_id(self) -> int:
    """The forum message to update."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def is_thank_you(self) -> bool:
    """The new status of whether it's a thank you comment."""
    return self._is_thank_you

  @is_thank_you.setter
  def is_thank_you(self, is_thank_you: bool):
    if is_thank_you is None:
      del self.is_thank_you
      return
    if not isinstance(is_thank_you, bool):
      raise TypeError('is_thank_you must be of type bool')
    self._is_thank_you = is_thank_you


class UpdateManyFeedbackTrackingDataRequest(KaggleObject):
  r"""
  Attributes:
    message_ids (int)
    feedback_tracking_data (FeedbackTrackingData)
  """

  def __init__(self):
    self._message_ids = []
    self._feedback_tracking_data = None
    self._freeze()

  @property
  def message_ids(self) -> Optional[List[int]]:
    return self._message_ids

  @message_ids.setter
  def message_ids(self, message_ids: Optional[List[int]]):
    if message_ids is None:
      del self.message_ids
      return
    if not isinstance(message_ids, list):
      raise TypeError('message_ids must be of type list')
    if not all([isinstance(t, int) for t in message_ids]):
      raise TypeError('message_ids must contain only items of type int')
    self._message_ids = message_ids

  @property
  def feedback_tracking_data(self) -> Optional['FeedbackTrackingData']:
    return self._feedback_tracking_data

  @feedback_tracking_data.setter
  def feedback_tracking_data(self, feedback_tracking_data: Optional['FeedbackTrackingData']):
    if feedback_tracking_data is None:
      del self.feedback_tracking_data
      return
    if not isinstance(feedback_tracking_data, FeedbackTrackingData):
      raise TypeError('feedback_tracking_data must be of type FeedbackTrackingData')
    self._feedback_tracking_data = feedback_tracking_data


class UpdateMessageRequest(KaggleObject):
  r"""
  Attributes:
    message_id (int)
      The message ID of the message being updated.
    message (Message)
      The message content & blobs.
  """

  def __init__(self):
    self._message_id = 0
    self._message = None
    self._freeze()

  @property
  def message_id(self) -> int:
    """The message ID of the message being updated."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs."""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message


class UpdateTopicRequest(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
      The topic ID of the topic being updated.
    topic_name (str)
      The updated name of the topic.
    message (Message)
      The message content & blobs.
    tag_ids (int)
      Optional tags to add to the forum topic
  """

  def __init__(self):
    self._topic_id = 0
    self._topic_name = ""
    self._message = None
    self._tag_ids = []
    self._freeze()

  @property
  def topic_id(self) -> int:
    """The topic ID of the topic being updated."""
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
  def topic_name(self) -> str:
    """The updated name of the topic."""
    return self._topic_name

  @topic_name.setter
  def topic_name(self, topic_name: str):
    if topic_name is None:
      del self.topic_name
      return
    if not isinstance(topic_name, str):
      raise TypeError('topic_name must be of type str')
    self._topic_name = topic_name

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs."""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """Optional tags to add to the forum topic"""
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids


class VoteOnForumMessageRequest(KaggleObject):
  r"""
  Attributes:
    forum_message_vote (MessageVote)
  """

  def __init__(self):
    self._forum_message_vote = None
    self._freeze()

  @property
  def forum_message_vote(self) -> Optional['MessageVote']:
    return self._forum_message_vote

  @forum_message_vote.setter
  def forum_message_vote(self, forum_message_vote: Optional['MessageVote']):
    if forum_message_vote is None:
      del self.forum_message_vote
      return
    if not isinstance(forum_message_vote, MessageVote):
      raise TypeError('forum_message_vote must be of type MessageVote')
    self._forum_message_vote = forum_message_vote


BatchDeleteMessageRequest._fields = [
  FieldMetadata("messageIds", "message_ids", "_message_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
]

BatchGetForumMessagesRequest._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("messageIds", "message_ids", "_message_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

BatchGetForumMessagesResponse._fields = [
  FieldMetadata("messages", "messages", "_messages", CommentForumMessage, [], ListSerializer(KaggleObjectSerializer())),
]

BlobCreationInfo._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
]

BlobFileInfo._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedDate", "last_modified_date", "_last_modified_date", datetime, None, DateTimeSerializer()),
]

CreateAttachmentRequest._fields = [
  FieldMetadata("blobFileInfo", "blob_file_info", "_blob_file_info", BlobFileInfo, None, KaggleObjectSerializer()),
]

CreateAttachmentResponse._fields = [
  FieldMetadata("blobCreationInfo", "blob_creation_info", "_blob_creation_info", BlobCreationInfo, None, KaggleObjectSerializer()),
]

CreateKernelMessageRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
]

CreateKernelMessageResponse._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
]

CreateReplyRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
]

CreateReplyResponse._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
]

CreateTopicRequest._fields = [
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("topicName", "topic_name", "_topic_name", str, "", PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

CreateTopicResponse._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
]

DeleteAttachmentRequest._fields = [
  FieldMetadata("attachmentId", "attachment_id", "_attachment_id", int, 0, PredefinedSerializer()),
]

DeleteMessageRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
]

DeleteTopicRequest._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
]

GetForumMessagesInTopicRequest._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("initialPageSize", "initial_page_size", "_initial_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newUserSort", "new_user_sort", "_new_user_sort", CommentListSortBy, CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("filter", "filter", "_filter", CommentListFilter, CommentListFilter.ALL, EnumSerializer()),
  FieldMetadata("includeFirstForumMessage", "include_first_forum_message", "_include_first_forum_message", bool, False, PredefinedSerializer()),
  FieldMetadata("startingCommentId", "starting_comment_id", "_starting_comment_id", int, None, PredefinedSerializer(), optional=True),
]

GetForumMessagesInTopicResponse._fields = [
  FieldMetadata("comments", "comments", "_comments", CommentForumMessage, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("commentSort", "comment_sort", "_comment_sort", CommentListSortBy, CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
]

GetForumMessageUpvotesRequest._fields = [
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, 0, PredefinedSerializer()),
]

GetForumMessageUpvotesResponse._fields = [
  FieldMetadata("upvoters", "upvoters", "_upvoters", User, [], ListSerializer(KaggleObjectSerializer())),
]

GetForumRequest._fields = [
  FieldMetadata("forumId", "forum_id", "_forum_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumSlug", "forum_slug", "_forum_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer(), optional=True),
]

GetForumResponse._fields = [
  FieldMetadata("forum", "forum", "_forum", Forum, None, KaggleObjectSerializer()),
  FieldMetadata("topicSort", "topic_sort", "_topic_sort", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
]

GetForumTopicByIdRequest._fields = [
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("includeComments", "include_comments", "_include_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("initialPageSize", "initial_page_size", "_initial_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("startingCommentId", "starting_comment_id", "_starting_comment_id", int, None, PredefinedSerializer(), optional=True),
]

GetForumTopicByIdResponse._fields = [
  FieldMetadata("forumTopic", "forum_topic", "_forum_topic", ForumTopic, None, KaggleObjectSerializer()),
]

GetSiteForumsRequest._fields = []

GetSiteForumsResponse._fields = [
  FieldMetadata("forums", "forums", "_forums", Forum, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("initialSortBy", "initial_sort_by", "_initial_sort_by", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
]

GetTopicListByForumIdRequest._fields = [
  FieldMetadata("category", "category", "_category", TopicListCategory, TopicListCategory.TOPIC_LIST_CATEGORY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", TopicListGroup, TopicListGroup.TOPIC_LIST_GROUP_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sortBy", "sort_by", "_sort_by", TopicListSortBy, TopicListSortBy.TOPIC_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("recency", "recency", "_recency", TopicListRecency, TopicListRecency.TOPIC_LIST_RECENCY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("myActivity", "my_activity", "_my_activity", TopicListMyActivity, TopicListMyActivity.TOPIC_LIST_MY_ACTIVITY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("author", "author", "_author", TopicListAuthor, TopicListAuthor.TOPIC_LIST_AUTHOR_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("filterCategoryIds", "filter_category_ids", "_filter_category_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetTopicListResponse._fields = [
  FieldMetadata("topics", "topics", "_topics", TopicListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

Message._fields = [
  FieldMetadata("markdown", "markdown", "_markdown", str, "", PredefinedSerializer()),
  FieldMetadata("html", "html", "_html", str, "", PredefinedSerializer()),
  FieldMetadata("blobFileTokens", "blob_file_tokens", "_blob_file_tokens", str, [], ListSerializer(PredefinedSerializer())),
]

MessageVote._fields = [
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("score", "score", "_score", int, 0, PredefinedSerializer()),
]

MoveForumTopicToForumRequest._fields = [
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fromForumId", "from_forum_id", "_from_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("toForumId", "to_forum_id", "_to_forum_id", int, 0, PredefinedSerializer()),
]

PinForumMessageRequest._fields = [
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isPinned", "is_pinned", "_is_pinned", bool, False, PredefinedSerializer()),
]

ReactToForumMessageRequest._fields = [
  FieldMetadata("reaction", "reaction", "_reaction", EmojiReaction, EmojiReaction.EMOJI_REACTION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("shouldAddReaction", "should_add_reaction", "_should_add_reaction", bool, False, PredefinedSerializer()),
]

ToggleSpamMessageRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
]

ToggleSpamMessageResponse._fields = [
  FieldMetadata("messageUrl", "message_url", "_message_url", str, "", PredefinedSerializer()),
]

UpdateFeedbackTrackingDataRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("feedbackTrackingData", "feedback_tracking_data", "_feedback_tracking_data", FeedbackTrackingData, None, KaggleObjectSerializer()),
]

UpdateForumMessageSettingsRequest._fields = [
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settingToToggle", "setting_to_toggle", "_setting_to_toggle", ForumMessageSettings, ForumMessageSettings.FORUM_MESSAGE_SETTINGS_UNSPECIFIED, EnumSerializer()),
]

UpdateForumSettingsRequest._fields = [
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settingToToggle", "setting_to_toggle", "_setting_to_toggle", ForumSettings, ForumSettings.FORUM_SETTINGS_IS_READ_ONLY, EnumSerializer()),
]

UpdateForumTopicSettingsRequest._fields = [
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settingToToggle", "setting_to_toggle", "_setting_to_toggle", ForumTopicSettings, ForumTopicSettings.FORUM_TOPIC_SETTINGS_IS_READ_ONLY, EnumSerializer()),
]

UpdateIsThankYouStatusRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isThankYou", "is_thank_you", "_is_thank_you", bool, False, PredefinedSerializer()),
]

UpdateManyFeedbackTrackingDataRequest._fields = [
  FieldMetadata("messageIds", "message_ids", "_message_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("feedbackTrackingData", "feedback_tracking_data", "_feedback_tracking_data", FeedbackTrackingData, None, KaggleObjectSerializer()),
]

UpdateMessageRequest._fields = [
  FieldMetadata("messageId", "message_id", "_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
]

UpdateTopicRequest._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("topicName", "topic_name", "_topic_name", str, "", PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

VoteOnForumMessageRequest._fields = [
  FieldMetadata("forumMessageVote", "forum_message_vote", "_forum_message_vote", MessageVote, None, KaggleObjectSerializer()),
]

