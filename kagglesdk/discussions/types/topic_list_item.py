from datetime import datetime
from kagglesdk.competitions.types.team import TeamUpInfo
from kagglesdk.discussions.types.discussions_enums import CommentAuthorType
from kagglesdk.kaggle_object import *
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class TopicListItem(KaggleObject):
  r"""
  Attributes:
    author_user (UserAvatar)
    author_type (CommentAuthorType)
    comment_count (int)
    current_user_vote (int)
    can_upvote (bool)
    can_downvote (bool)
    first_forum_message_id (int)
    has_admin_response (bool)
    id (int)
    is_sticky (bool)
    last_commenter_type (CommentAuthorType)
    last_commenter_name (str)
    last_commenter_url (str)
    last_comment_post_date (datetime)
    last_view_date (datetime)
    parent_name (str)
    parent_url (str)
    post_date (datetime)
    tags (Tag)
    title (str)
    topic_url (str)
    votes (int)
    is_bookmarked (bool)
    oldest_unread_comment_url (str)
    team_up_info (TeamUpInfo)
      Competitions team up info for the comment's author
    is_write_up (bool)
    is_admin_triage_flagged (bool)
      Flagged by automated systems for admin triage. See: b/372020273
  """

  def __init__(self):
    self._author_user = None
    self._author_type = CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED
    self._comment_count = 0
    self._current_user_vote = 0
    self._can_upvote = False
    self._can_downvote = False
    self._first_forum_message_id = 0
    self._has_admin_response = False
    self._id = 0
    self._is_sticky = False
    self._last_commenter_type = CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED
    self._last_commenter_name = ""
    self._last_commenter_url = ""
    self._last_comment_post_date = None
    self._last_view_date = None
    self._parent_name = None
    self._parent_url = None
    self._post_date = None
    self._tags = []
    self._title = ""
    self._topic_url = ""
    self._votes = 0
    self._is_bookmarked = False
    self._oldest_unread_comment_url = None
    self._team_up_info = None
    self._is_write_up = False
    self._is_admin_triage_flagged = False
    self._freeze()

  @property
  def author_user(self) -> Optional['UserAvatar']:
    return self._author_user

  @author_user.setter
  def author_user(self, author_user: Optional['UserAvatar']):
    if author_user is None:
      del self.author_user
      return
    if not isinstance(author_user, UserAvatar):
      raise TypeError('author_user must be of type UserAvatar')
    self._author_user = author_user

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
  def current_user_vote(self) -> int:
    return self._current_user_vote

  @current_user_vote.setter
  def current_user_vote(self, current_user_vote: int):
    if current_user_vote is None:
      del self.current_user_vote
      return
    if not isinstance(current_user_vote, int):
      raise TypeError('current_user_vote must be of type int')
    self._current_user_vote = current_user_vote

  @property
  def can_upvote(self) -> bool:
    return self._can_upvote

  @can_upvote.setter
  def can_upvote(self, can_upvote: bool):
    if can_upvote is None:
      del self.can_upvote
      return
    if not isinstance(can_upvote, bool):
      raise TypeError('can_upvote must be of type bool')
    self._can_upvote = can_upvote

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
  def first_forum_message_id(self) -> int:
    return self._first_forum_message_id

  @first_forum_message_id.setter
  def first_forum_message_id(self, first_forum_message_id: int):
    if first_forum_message_id is None:
      del self.first_forum_message_id
      return
    if not isinstance(first_forum_message_id, int):
      raise TypeError('first_forum_message_id must be of type int')
    self._first_forum_message_id = first_forum_message_id

  @property
  def has_admin_response(self) -> bool:
    return self._has_admin_response

  @has_admin_response.setter
  def has_admin_response(self, has_admin_response: bool):
    if has_admin_response is None:
      del self.has_admin_response
      return
    if not isinstance(has_admin_response, bool):
      raise TypeError('has_admin_response must be of type bool')
    self._has_admin_response = has_admin_response

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
  def is_sticky(self) -> bool:
    return self._is_sticky

  @is_sticky.setter
  def is_sticky(self, is_sticky: bool):
    if is_sticky is None:
      del self.is_sticky
      return
    if not isinstance(is_sticky, bool):
      raise TypeError('is_sticky must be of type bool')
    self._is_sticky = is_sticky

  @property
  def last_commenter_type(self) -> 'CommentAuthorType':
    return self._last_commenter_type

  @last_commenter_type.setter
  def last_commenter_type(self, last_commenter_type: 'CommentAuthorType'):
    if last_commenter_type is None:
      del self.last_commenter_type
      return
    if not isinstance(last_commenter_type, CommentAuthorType):
      raise TypeError('last_commenter_type must be of type CommentAuthorType')
    self._last_commenter_type = last_commenter_type

  @property
  def last_commenter_name(self) -> str:
    return self._last_commenter_name

  @last_commenter_name.setter
  def last_commenter_name(self, last_commenter_name: str):
    if last_commenter_name is None:
      del self.last_commenter_name
      return
    if not isinstance(last_commenter_name, str):
      raise TypeError('last_commenter_name must be of type str')
    self._last_commenter_name = last_commenter_name

  @property
  def last_commenter_url(self) -> str:
    return self._last_commenter_url

  @last_commenter_url.setter
  def last_commenter_url(self, last_commenter_url: str):
    if last_commenter_url is None:
      del self.last_commenter_url
      return
    if not isinstance(last_commenter_url, str):
      raise TypeError('last_commenter_url must be of type str')
    self._last_commenter_url = last_commenter_url

  @property
  def last_comment_post_date(self) -> datetime:
    return self._last_comment_post_date

  @last_comment_post_date.setter
  def last_comment_post_date(self, last_comment_post_date: datetime):
    if last_comment_post_date is None:
      del self.last_comment_post_date
      return
    if not isinstance(last_comment_post_date, datetime):
      raise TypeError('last_comment_post_date must be of type datetime')
    self._last_comment_post_date = last_comment_post_date

  @property
  def last_view_date(self) -> datetime:
    return self._last_view_date

  @last_view_date.setter
  def last_view_date(self, last_view_date: datetime):
    if last_view_date is None:
      del self.last_view_date
      return
    if not isinstance(last_view_date, datetime):
      raise TypeError('last_view_date must be of type datetime')
    self._last_view_date = last_view_date

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
  def topic_url(self) -> str:
    return self._topic_url

  @topic_url.setter
  def topic_url(self, topic_url: str):
    if topic_url is None:
      del self.topic_url
      return
    if not isinstance(topic_url, str):
      raise TypeError('topic_url must be of type str')
    self._topic_url = topic_url

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
  def oldest_unread_comment_url(self) -> str:
    return self._oldest_unread_comment_url or ""

  @oldest_unread_comment_url.setter
  def oldest_unread_comment_url(self, oldest_unread_comment_url: Optional[str]):
    if oldest_unread_comment_url is None:
      del self.oldest_unread_comment_url
      return
    if not isinstance(oldest_unread_comment_url, str):
      raise TypeError('oldest_unread_comment_url must be of type str')
    self._oldest_unread_comment_url = oldest_unread_comment_url

  @property
  def team_up_info(self) -> Optional['TeamUpInfo']:
    """Competitions team up info for the comment's author"""
    return self._team_up_info

  @team_up_info.setter
  def team_up_info(self, team_up_info: Optional['TeamUpInfo']):
    if team_up_info is None:
      del self.team_up_info
      return
    if not isinstance(team_up_info, TeamUpInfo):
      raise TypeError('team_up_info must be of type TeamUpInfo')
    self._team_up_info = team_up_info

  @property
  def is_write_up(self) -> bool:
    return self._is_write_up

  @is_write_up.setter
  def is_write_up(self, is_write_up: bool):
    if is_write_up is None:
      del self.is_write_up
      return
    if not isinstance(is_write_up, bool):
      raise TypeError('is_write_up must be of type bool')
    self._is_write_up = is_write_up

  @property
  def is_admin_triage_flagged(self) -> bool:
    """Flagged by automated systems for admin triage. See: b/372020273"""
    return self._is_admin_triage_flagged

  @is_admin_triage_flagged.setter
  def is_admin_triage_flagged(self, is_admin_triage_flagged: bool):
    if is_admin_triage_flagged is None:
      del self.is_admin_triage_flagged
      return
    if not isinstance(is_admin_triage_flagged, bool):
      raise TypeError('is_admin_triage_flagged must be of type bool')
    self._is_admin_triage_flagged = is_admin_triage_flagged


TopicListItem._fields = [
  FieldMetadata("authorUser", "author_user", "_author_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("authorType", "author_type", "_author_type", CommentAuthorType, CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("commentCount", "comment_count", "_comment_count", int, 0, PredefinedSerializer()),
  FieldMetadata("currentUserVote", "current_user_vote", "_current_user_vote", int, 0, PredefinedSerializer()),
  FieldMetadata("canUpvote", "can_upvote", "_can_upvote", bool, False, PredefinedSerializer()),
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("firstForumMessageId", "first_forum_message_id", "_first_forum_message_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hasAdminResponse", "has_admin_response", "_has_admin_response", bool, False, PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isSticky", "is_sticky", "_is_sticky", bool, False, PredefinedSerializer()),
  FieldMetadata("lastCommenterType", "last_commenter_type", "_last_commenter_type", CommentAuthorType, CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastCommenterName", "last_commenter_name", "_last_commenter_name", str, "", PredefinedSerializer()),
  FieldMetadata("lastCommenterUrl", "last_commenter_url", "_last_commenter_url", str, "", PredefinedSerializer()),
  FieldMetadata("lastCommentPostDate", "last_comment_post_date", "_last_comment_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastViewDate", "last_view_date", "_last_view_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("parentName", "parent_name", "_parent_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentUrl", "parent_url", "_parent_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("postDate", "post_date", "_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("topicUrl", "topic_url", "_topic_url", str, "", PredefinedSerializer()),
  FieldMetadata("votes", "votes", "_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("isBookmarked", "is_bookmarked", "_is_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("oldestUnreadCommentUrl", "oldest_unread_comment_url", "_oldest_unread_comment_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamUpInfo", "team_up_info", "_team_up_info", TeamUpInfo, None, KaggleObjectSerializer()),
  FieldMetadata("isWriteUp", "is_write_up", "_is_write_up", bool, False, PredefinedSerializer()),
  FieldMetadata("isAdminTriageFlagged", "is_admin_triage_flagged", "_is_admin_triage_flagged", bool, False, PredefinedSerializer()),
]

