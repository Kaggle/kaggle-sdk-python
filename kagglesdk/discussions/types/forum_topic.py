from datetime import datetime
from kagglesdk.discussions.types.discussions_enums import CommentListSortBy
from kagglesdk.discussions.types.forum_message import CommentForumMessage
from kagglesdk.discussions.types.writeup_types import WriteUp
from kagglesdk.kaggle_object import *
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class ForumTopic(KaggleObject):
  r"""
  Attributes:
    allow_attachments (bool)
    author_id (int)
    author_thumbnail_name (str)
    author_user_display_name (str)
    author_user_name (str)
    can_delete (bool)
    comments (CommentForumMessage)
    comment_sort (CommentListSortBy)
    first_message (CommentForumMessage)
    first_message_id (int)
    forum_id (int)
    forum_name (str)
    id (int)
    is_deleted (bool)
    is_deleted_legacy (bool)
    is_followed (bool)
    is_locked (bool)
    is_spammed (bool)
    is_stickied (bool)
    name (str)
    parent_name (str)
    parent_url (str)
    post_date (datetime)
    tags (Tag)
    total_votes (int)
    url (str)
    is_bookmarked (bool)
    is_private (bool)
    is_auto_privated (bool)
    total_messages (int)
    author_performance_tier (UserAchievementTier)
    is_global_notifications_enabled (bool)
    current_user_can_reply (bool)
    write_up (WriteUp)
    author_progression_opt_out (bool)
  """

  def __init__(self):
    self._allow_attachments = False
    self._author_id = None
    self._author_thumbnail_name = None
    self._author_user_display_name = None
    self._author_user_name = None
    self._can_delete = False
    self._comments = []
    self._comment_sort = CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED
    self._first_message = None
    self._first_message_id = None
    self._forum_id = 0
    self._forum_name = ""
    self._id = 0
    self._is_deleted = False
    self._is_deleted_legacy = False
    self._is_followed = False
    self._is_locked = False
    self._is_spammed = False
    self._is_stickied = False
    self._name = ""
    self._parent_name = None
    self._parent_url = None
    self._post_date = None
    self._tags = []
    self._total_votes = 0
    self._url = ""
    self._is_bookmarked = False
    self._is_private = False
    self._is_auto_privated = False
    self._total_messages = 0
    self._author_performance_tier = UserAchievementTier.NOVICE
    self._is_global_notifications_enabled = False
    self._current_user_can_reply = False
    self._write_up = None
    self._author_progression_opt_out = None
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
  def author_id(self) -> int:
    return self._author_id or 0

  @author_id.setter
  def author_id(self, author_id: Optional[int]):
    if author_id is None:
      del self.author_id
      return
    if not isinstance(author_id, int):
      raise TypeError('author_id must be of type int')
    self._author_id = author_id

  @property
  def author_thumbnail_name(self) -> str:
    return self._author_thumbnail_name or ""

  @author_thumbnail_name.setter
  def author_thumbnail_name(self, author_thumbnail_name: Optional[str]):
    if author_thumbnail_name is None:
      del self.author_thumbnail_name
      return
    if not isinstance(author_thumbnail_name, str):
      raise TypeError('author_thumbnail_name must be of type str')
    self._author_thumbnail_name = author_thumbnail_name

  @property
  def author_user_display_name(self) -> str:
    return self._author_user_display_name or ""

  @author_user_display_name.setter
  def author_user_display_name(self, author_user_display_name: Optional[str]):
    if author_user_display_name is None:
      del self.author_user_display_name
      return
    if not isinstance(author_user_display_name, str):
      raise TypeError('author_user_display_name must be of type str')
    self._author_user_display_name = author_user_display_name

  @property
  def author_user_name(self) -> str:
    return self._author_user_name or ""

  @author_user_name.setter
  def author_user_name(self, author_user_name: Optional[str]):
    if author_user_name is None:
      del self.author_user_name
      return
    if not isinstance(author_user_name, str):
      raise TypeError('author_user_name must be of type str')
    self._author_user_name = author_user_name

  @property
  def author_performance_tier(self) -> 'UserAchievementTier':
    return self._author_performance_tier

  @author_performance_tier.setter
  def author_performance_tier(self, author_performance_tier: 'UserAchievementTier'):
    if author_performance_tier is None:
      del self.author_performance_tier
      return
    if not isinstance(author_performance_tier, UserAchievementTier):
      raise TypeError('author_performance_tier must be of type UserAchievementTier')
    self._author_performance_tier = author_performance_tier

  @property
  def author_progression_opt_out(self) -> bool:
    return self._author_progression_opt_out or False

  @author_progression_opt_out.setter
  def author_progression_opt_out(self, author_progression_opt_out: Optional[bool]):
    if author_progression_opt_out is None:
      del self.author_progression_opt_out
      return
    if not isinstance(author_progression_opt_out, bool):
      raise TypeError('author_progression_opt_out must be of type bool')
    self._author_progression_opt_out = author_progression_opt_out

  @property
  def can_delete(self) -> bool:
    return self._can_delete

  @can_delete.setter
  def can_delete(self, can_delete: bool):
    if can_delete is None:
      del self.can_delete
      return
    if not isinstance(can_delete, bool):
      raise TypeError('can_delete must be of type bool')
    self._can_delete = can_delete

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

  @property
  def first_message(self) -> Optional['CommentForumMessage']:
    return self._first_message

  @first_message.setter
  def first_message(self, first_message: Optional['CommentForumMessage']):
    if first_message is None:
      del self.first_message
      return
    if not isinstance(first_message, CommentForumMessage):
      raise TypeError('first_message must be of type CommentForumMessage')
    self._first_message = first_message

  @property
  def first_message_id(self) -> int:
    return self._first_message_id or 0

  @first_message_id.setter
  def first_message_id(self, first_message_id: Optional[int]):
    if first_message_id is None:
      del self.first_message_id
      return
    if not isinstance(first_message_id, int):
      raise TypeError('first_message_id must be of type int')
    self._first_message_id = first_message_id

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
  def is_deleted(self) -> bool:
    return self._is_deleted

  @is_deleted.setter
  def is_deleted(self, is_deleted: bool):
    if is_deleted is None:
      del self.is_deleted
      return
    if not isinstance(is_deleted, bool):
      raise TypeError('is_deleted must be of type bool')
    self._is_deleted = is_deleted

  @property
  def is_deleted_legacy(self) -> bool:
    return self._is_deleted_legacy

  @is_deleted_legacy.setter
  def is_deleted_legacy(self, is_deleted_legacy: bool):
    if is_deleted_legacy is None:
      del self.is_deleted_legacy
      return
    if not isinstance(is_deleted_legacy, bool):
      raise TypeError('is_deleted_legacy must be of type bool')
    self._is_deleted_legacy = is_deleted_legacy

  @property
  def is_followed(self) -> bool:
    return self._is_followed

  @is_followed.setter
  def is_followed(self, is_followed: bool):
    if is_followed is None:
      del self.is_followed
      return
    if not isinstance(is_followed, bool):
      raise TypeError('is_followed must be of type bool')
    self._is_followed = is_followed

  @property
  def is_global_notifications_enabled(self) -> bool:
    return self._is_global_notifications_enabled

  @is_global_notifications_enabled.setter
  def is_global_notifications_enabled(self, is_global_notifications_enabled: bool):
    if is_global_notifications_enabled is None:
      del self.is_global_notifications_enabled
      return
    if not isinstance(is_global_notifications_enabled, bool):
      raise TypeError('is_global_notifications_enabled must be of type bool')
    self._is_global_notifications_enabled = is_global_notifications_enabled

  @property
  def is_locked(self) -> bool:
    return self._is_locked

  @is_locked.setter
  def is_locked(self, is_locked: bool):
    if is_locked is None:
      del self.is_locked
      return
    if not isinstance(is_locked, bool):
      raise TypeError('is_locked must be of type bool')
    self._is_locked = is_locked

  @property
  def is_spammed(self) -> bool:
    return self._is_spammed

  @is_spammed.setter
  def is_spammed(self, is_spammed: bool):
    if is_spammed is None:
      del self.is_spammed
      return
    if not isinstance(is_spammed, bool):
      raise TypeError('is_spammed must be of type bool')
    self._is_spammed = is_spammed

  @property
  def is_stickied(self) -> bool:
    return self._is_stickied

  @is_stickied.setter
  def is_stickied(self, is_stickied: bool):
    if is_stickied is None:
      del self.is_stickied
      return
    if not isinstance(is_stickied, bool):
      raise TypeError('is_stickied must be of type bool')
    self._is_stickied = is_stickied

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
  def tags(self) -> Optional[List[Optional['Tag']]]:
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['Tag']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, Tag) for t in tags]):
      raise TypeError('tags must contain only items of type Tag')
    self._tags = tags

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

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
  def is_bookmarked(self) -> bool:
    return self._is_bookmarked

  @is_bookmarked.setter
  def is_bookmarked(self, is_bookmarked: bool):
    if is_bookmarked is None:
      del self.is_bookmarked
      return
    if not isinstance(is_bookmarked, bool):
      raise TypeError('is_bookmarked must be of type bool')
    self._is_bookmarked = is_bookmarked

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
  def is_auto_privated(self) -> bool:
    return self._is_auto_privated

  @is_auto_privated.setter
  def is_auto_privated(self, is_auto_privated: bool):
    if is_auto_privated is None:
      del self.is_auto_privated
      return
    if not isinstance(is_auto_privated, bool):
      raise TypeError('is_auto_privated must be of type bool')
    self._is_auto_privated = is_auto_privated

  @property
  def total_messages(self) -> int:
    return self._total_messages

  @total_messages.setter
  def total_messages(self, total_messages: int):
    if total_messages is None:
      del self.total_messages
      return
    if not isinstance(total_messages, int):
      raise TypeError('total_messages must be of type int')
    self._total_messages = total_messages

  @property
  def current_user_can_reply(self) -> bool:
    return self._current_user_can_reply

  @current_user_can_reply.setter
  def current_user_can_reply(self, current_user_can_reply: bool):
    if current_user_can_reply is None:
      del self.current_user_can_reply
      return
    if not isinstance(current_user_can_reply, bool):
      raise TypeError('current_user_can_reply must be of type bool')
    self._current_user_can_reply = current_user_can_reply

  @property
  def write_up(self) -> Optional['WriteUp']:
    return self._write_up or None

  @write_up.setter
  def write_up(self, write_up: Optional[Optional['WriteUp']]):
    if write_up is None:
      del self.write_up
      return
    if not isinstance(write_up, WriteUp):
      raise TypeError('write_up must be of type WriteUp')
    self._write_up = write_up


ForumTopic._fields = [
  FieldMetadata("allowAttachments", "allow_attachments", "_allow_attachments", bool, False, PredefinedSerializer()),
  FieldMetadata("authorId", "author_id", "_author_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorThumbnailName", "author_thumbnail_name", "_author_thumbnail_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorUserDisplayName", "author_user_display_name", "_author_user_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorUserName", "author_user_name", "_author_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canDelete", "can_delete", "_can_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("comments", "comments", "_comments", CommentForumMessage, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("commentSort", "comment_sort", "_comment_sort", CommentListSortBy, CommentListSortBy.COMMENT_LIST_SORT_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("firstMessage", "first_message", "_first_message", CommentForumMessage, None, KaggleObjectSerializer()),
  FieldMetadata("firstMessageId", "first_message_id", "_first_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("isDeletedLegacy", "is_deleted_legacy", "_is_deleted_legacy", bool, False, PredefinedSerializer()),
  FieldMetadata("isFollowed", "is_followed", "_is_followed", bool, False, PredefinedSerializer()),
  FieldMetadata("isLocked", "is_locked", "_is_locked", bool, False, PredefinedSerializer()),
  FieldMetadata("isSpammed", "is_spammed", "_is_spammed", bool, False, PredefinedSerializer()),
  FieldMetadata("isStickied", "is_stickied", "_is_stickied", bool, False, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("parentName", "parent_name", "_parent_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentUrl", "parent_url", "_parent_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("postDate", "post_date", "_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("isBookmarked", "is_bookmarked", "_is_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("isAutoPrivated", "is_auto_privated", "_is_auto_privated", bool, False, PredefinedSerializer()),
  FieldMetadata("totalMessages", "total_messages", "_total_messages", int, 0, PredefinedSerializer()),
  FieldMetadata("authorPerformanceTier", "author_performance_tier", "_author_performance_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("isGlobalNotificationsEnabled", "is_global_notifications_enabled", "_is_global_notifications_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserCanReply", "current_user_can_reply", "_current_user_can_reply", bool, False, PredefinedSerializer()),
  FieldMetadata("writeUp", "write_up", "_write_up", WriteUp, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authorProgressionOptOut", "author_progression_opt_out", "_author_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

