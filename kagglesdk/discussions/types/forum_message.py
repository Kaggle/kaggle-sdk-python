from datetime import datetime
from kagglesdk.abuse.types.abuse_enums import PrivatedModerationStatus
from kagglesdk.competitions.types.team import TeamUpInfo
from kagglesdk.discussions.types.discussions_enums import CommentAuthorType, EmojiReaction
from kagglesdk.discussions.types.feedback_tracking_data import FeedbackTrackingData
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class CommentAttachment(KaggleObject):
  r"""
  Attributes:
    file_type (str)
    id (int)
    name (str)
    total_bytes (int)
    url (str)
    blob_token (str)
  """

  def __init__(self):
    self._file_type = None
    self._id = 0
    self._name = ""
    self._total_bytes = 0
    self._url = None
    self._blob_token = None
    self._freeze()

  @property
  def file_type(self) -> str:
    return self._file_type or ""

  @file_type.setter
  def file_type(self, file_type: Optional[str]):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, str):
      raise TypeError('file_type must be of type str')
    self._file_type = file_type

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
  def total_bytes(self) -> int:
    return self._total_bytes

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

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
  def blob_token(self) -> str:
    return self._blob_token or ""

  @blob_token.setter
  def blob_token(self, blob_token: Optional[str]):
    if blob_token is None:
      del self.blob_token
      return
    if not isinstance(blob_token, str):
      raise TypeError('blob_token must be of type str')
    self._blob_token = blob_token


class CommentForumMessage(KaggleObject):
  r"""
  This is a version of ForumMessage meant for displaying comments

  Attributes:
    id (int)
    post_date (datetime)
    raw_markdown (str)
    content (str)
    replies (CommentForumMessage)
    attachments (CommentAttachment)
    parent (DiscussionItemLink)
    author (UserAvatar)
    author_type (CommentAuthorType)
    votes (CommentVoteButton)
    can_delete (bool)
      Permissions/Display
    is_user_author (bool)
    has_flags (bool)
    is_deleted (bool)
    is_admin_deleted (bool)
    is_flagged (bool)
    is_spammed (bool)
    current_kernel_version (int)
    kernel_version (int)
    competition_ranking (int)
      Rankings
    feedback_tracking_data (FeedbackTrackingData)
    is_pinned (bool)
    is_auto_privated (bool)
    moderation_status (PrivatedModerationStatus)
    is_thank_you (bool)
    is_collapsed (bool)
      True if the comment should be collapsed into its parent (ie 'show X more
      replies'). Used by FE, populated by BE.
    is_partial (bool)
      True if the data is only partially populated. Clients should call
      BatchGetForumMessages if they want more fields. Fields Included: Id,
      IsPinned, IsDeleted, PostDate, IsThankYou, Votes
    reactions (ForumMessageReactionGroup)
      List of reactions to the message, grouped by the reaction type.
    team_up_info (TeamUpInfo)
      Competitions team up info for the comment's author
  """

  def __init__(self):
    self._id = 0
    self._post_date = None
    self._raw_markdown = None
    self._content = ""
    self._replies = []
    self._attachments = []
    self._parent = None
    self._author = None
    self._author_type = CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED
    self._votes = None
    self._can_delete = False
    self._is_user_author = False
    self._has_flags = False
    self._is_deleted = False
    self._is_admin_deleted = False
    self._is_flagged = False
    self._is_spammed = False
    self._current_kernel_version = 0
    self._kernel_version = None
    self._competition_ranking = None
    self._feedback_tracking_data = None
    self._is_pinned = False
    self._is_auto_privated = False
    self._moderation_status = PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED
    self._is_thank_you = None
    self._is_collapsed = False
    self._is_partial = False
    self._reactions = []
    self._team_up_info = None
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
  def raw_markdown(self) -> str:
    return self._raw_markdown or ""

  @raw_markdown.setter
  def raw_markdown(self, raw_markdown: Optional[str]):
    if raw_markdown is None:
      del self.raw_markdown
      return
    if not isinstance(raw_markdown, str):
      raise TypeError('raw_markdown must be of type str')
    self._raw_markdown = raw_markdown

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
  def replies(self) -> Optional[List[Optional['CommentForumMessage']]]:
    return self._replies

  @replies.setter
  def replies(self, replies: Optional[List[Optional['CommentForumMessage']]]):
    if replies is None:
      del self.replies
      return
    if not isinstance(replies, list):
      raise TypeError('replies must be of type list')
    if not all([isinstance(t, CommentForumMessage) for t in replies]):
      raise TypeError('replies must contain only items of type CommentForumMessage')
    self._replies = replies

  @property
  def attachments(self) -> Optional[List[Optional['CommentAttachment']]]:
    return self._attachments

  @attachments.setter
  def attachments(self, attachments: Optional[List[Optional['CommentAttachment']]]):
    if attachments is None:
      del self.attachments
      return
    if not isinstance(attachments, list):
      raise TypeError('attachments must be of type list')
    if not all([isinstance(t, CommentAttachment) for t in attachments]):
      raise TypeError('attachments must contain only items of type CommentAttachment')
    self._attachments = attachments

  @property
  def parent(self) -> Optional['DiscussionItemLink']:
    return self._parent

  @parent.setter
  def parent(self, parent: Optional['DiscussionItemLink']):
    if parent is None:
      del self.parent
      return
    if not isinstance(parent, DiscussionItemLink):
      raise TypeError('parent must be of type DiscussionItemLink')
    self._parent = parent

  @property
  def author(self) -> Optional['UserAvatar']:
    return self._author

  @author.setter
  def author(self, author: Optional['UserAvatar']):
    if author is None:
      del self.author
      return
    if not isinstance(author, UserAvatar):
      raise TypeError('author must be of type UserAvatar')
    self._author = author

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
  def votes(self) -> Optional['CommentVoteButton']:
    return self._votes

  @votes.setter
  def votes(self, votes: Optional['CommentVoteButton']):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, CommentVoteButton):
      raise TypeError('votes must be of type CommentVoteButton')
    self._votes = votes

  @property
  def can_delete(self) -> bool:
    """Permissions/Display"""
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
  def is_user_author(self) -> bool:
    return self._is_user_author

  @is_user_author.setter
  def is_user_author(self, is_user_author: bool):
    if is_user_author is None:
      del self.is_user_author
      return
    if not isinstance(is_user_author, bool):
      raise TypeError('is_user_author must be of type bool')
    self._is_user_author = is_user_author

  @property
  def has_flags(self) -> bool:
    return self._has_flags

  @has_flags.setter
  def has_flags(self, has_flags: bool):
    if has_flags is None:
      del self.has_flags
      return
    if not isinstance(has_flags, bool):
      raise TypeError('has_flags must be of type bool')
    self._has_flags = has_flags

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
  def is_admin_deleted(self) -> bool:
    return self._is_admin_deleted

  @is_admin_deleted.setter
  def is_admin_deleted(self, is_admin_deleted: bool):
    if is_admin_deleted is None:
      del self.is_admin_deleted
      return
    if not isinstance(is_admin_deleted, bool):
      raise TypeError('is_admin_deleted must be of type bool')
    self._is_admin_deleted = is_admin_deleted

  @property
  def is_flagged(self) -> bool:
    return self._is_flagged

  @is_flagged.setter
  def is_flagged(self, is_flagged: bool):
    if is_flagged is None:
      del self.is_flagged
      return
    if not isinstance(is_flagged, bool):
      raise TypeError('is_flagged must be of type bool')
    self._is_flagged = is_flagged

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
  def current_kernel_version(self) -> int:
    return self._current_kernel_version

  @current_kernel_version.setter
  def current_kernel_version(self, current_kernel_version: int):
    if current_kernel_version is None:
      del self.current_kernel_version
      return
    if not isinstance(current_kernel_version, int):
      raise TypeError('current_kernel_version must be of type int')
    self._current_kernel_version = current_kernel_version

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
  def is_thank_you(self) -> bool:
    return self._is_thank_you or False

  @is_thank_you.setter
  def is_thank_you(self, is_thank_you: Optional[bool]):
    if is_thank_you is None:
      del self.is_thank_you
      return
    if not isinstance(is_thank_you, bool):
      raise TypeError('is_thank_you must be of type bool')
    self._is_thank_you = is_thank_you

  @property
  def kernel_version(self) -> int:
    return self._kernel_version or 0

  @kernel_version.setter
  def kernel_version(self, kernel_version: Optional[int]):
    if kernel_version is None:
      del self.kernel_version
      return
    if not isinstance(kernel_version, int):
      raise TypeError('kernel_version must be of type int')
    self._kernel_version = kernel_version

  @property
  def competition_ranking(self) -> int:
    """Rankings"""
    return self._competition_ranking or 0

  @competition_ranking.setter
  def competition_ranking(self, competition_ranking: Optional[int]):
    if competition_ranking is None:
      del self.competition_ranking
      return
    if not isinstance(competition_ranking, int):
      raise TypeError('competition_ranking must be of type int')
    self._competition_ranking = competition_ranking

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

  @property
  def moderation_status(self) -> 'PrivatedModerationStatus':
    return self._moderation_status

  @moderation_status.setter
  def moderation_status(self, moderation_status: 'PrivatedModerationStatus'):
    if moderation_status is None:
      del self.moderation_status
      return
    if not isinstance(moderation_status, PrivatedModerationStatus):
      raise TypeError('moderation_status must be of type PrivatedModerationStatus')
    self._moderation_status = moderation_status

  @property
  def is_collapsed(self) -> bool:
    r"""
    True if the comment should be collapsed into its parent (ie 'show X more
    replies'). Used by FE, populated by BE.
    """
    return self._is_collapsed

  @is_collapsed.setter
  def is_collapsed(self, is_collapsed: bool):
    if is_collapsed is None:
      del self.is_collapsed
      return
    if not isinstance(is_collapsed, bool):
      raise TypeError('is_collapsed must be of type bool')
    self._is_collapsed = is_collapsed

  @property
  def is_partial(self) -> bool:
    r"""
    True if the data is only partially populated. Clients should call
    BatchGetForumMessages if they want more fields. Fields Included: Id,
    IsPinned, IsDeleted, PostDate, IsThankYou, Votes
    """
    return self._is_partial

  @is_partial.setter
  def is_partial(self, is_partial: bool):
    if is_partial is None:
      del self.is_partial
      return
    if not isinstance(is_partial, bool):
      raise TypeError('is_partial must be of type bool')
    self._is_partial = is_partial

  @property
  def reactions(self) -> Optional[List[Optional['ForumMessageReactionGroup']]]:
    """List of reactions to the message, grouped by the reaction type."""
    return self._reactions

  @reactions.setter
  def reactions(self, reactions: Optional[List[Optional['ForumMessageReactionGroup']]]):
    if reactions is None:
      del self.reactions
      return
    if not isinstance(reactions, list):
      raise TypeError('reactions must be of type list')
    if not all([isinstance(t, ForumMessageReactionGroup) for t in reactions]):
      raise TypeError('reactions must contain only items of type ForumMessageReactionGroup')
    self._reactions = reactions

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


class CommentVoteButton(KaggleObject):
  r"""
  Attributes:
    total_votes (int)
      Count of total votes (up+down).
    has_already_voted_up (bool)
    has_already_voted_down (bool)
    can_upvote (bool)
    can_downvote (bool)
    total_upvotes (int)
      Count of upvotes only (note downvotes is missing since it can be
      calculated).
  """

  def __init__(self):
    self._total_votes = 0
    self._has_already_voted_up = False
    self._has_already_voted_down = False
    self._can_upvote = False
    self._can_downvote = False
    self._total_upvotes = 0
    self._freeze()

  @property
  def total_votes(self) -> int:
    """Count of total votes (up+down)."""
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
  def total_upvotes(self) -> int:
    r"""
    Count of upvotes only (note downvotes is missing since it can be
    calculated).
    """
    return self._total_upvotes

  @total_upvotes.setter
  def total_upvotes(self, total_upvotes: int):
    if total_upvotes is None:
      del self.total_upvotes
      return
    if not isinstance(total_upvotes, int):
      raise TypeError('total_upvotes must be of type int')
    self._total_upvotes = total_upvotes

  @property
  def has_already_voted_up(self) -> bool:
    return self._has_already_voted_up

  @has_already_voted_up.setter
  def has_already_voted_up(self, has_already_voted_up: bool):
    if has_already_voted_up is None:
      del self.has_already_voted_up
      return
    if not isinstance(has_already_voted_up, bool):
      raise TypeError('has_already_voted_up must be of type bool')
    self._has_already_voted_up = has_already_voted_up

  @property
  def has_already_voted_down(self) -> bool:
    return self._has_already_voted_down

  @has_already_voted_down.setter
  def has_already_voted_down(self, has_already_voted_down: bool):
    if has_already_voted_down is None:
      del self.has_already_voted_down
      return
    if not isinstance(has_already_voted_down, bool):
      raise TypeError('has_already_voted_down must be of type bool')
    self._has_already_voted_down = has_already_voted_down

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


class DiscussionItemLink(KaggleObject):
  r"""
  Used to store data about a related item which we'll want to link to.
  Eg a message's topic, or a message's script.

  Attributes:
    id (int)
    name (str)
    url (str)
  """

  def __init__(self):
    self._id = 0
    self._name = None
    self._url = None
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


class ForumMessageReactionGroup(KaggleObject):
  r"""
  A particular reaction to a forum message (ie grouped by emoji).

  Attributes:
    emoji (EmojiReaction)
      Which reaction it is
    featured_user_names (str)
      Users who've reacted. May be truncated, but will always include the current
      user if they've reacted.
    user_count (int)
      The total number of users who've reacted (including any not included in
      usernames).
  """

  def __init__(self):
    self._emoji = EmojiReaction.EMOJI_REACTION_UNSPECIFIED
    self._featured_user_names = []
    self._user_count = 0
    self._freeze()

  @property
  def emoji(self) -> 'EmojiReaction':
    """Which reaction it is"""
    return self._emoji

  @emoji.setter
  def emoji(self, emoji: 'EmojiReaction'):
    if emoji is None:
      del self.emoji
      return
    if not isinstance(emoji, EmojiReaction):
      raise TypeError('emoji must be of type EmojiReaction')
    self._emoji = emoji

  @property
  def featured_user_names(self) -> Optional[List[str]]:
    r"""
    Users who've reacted. May be truncated, but will always include the current
    user if they've reacted.
    """
    return self._featured_user_names

  @featured_user_names.setter
  def featured_user_names(self, featured_user_names: Optional[List[str]]):
    if featured_user_names is None:
      del self.featured_user_names
      return
    if not isinstance(featured_user_names, list):
      raise TypeError('featured_user_names must be of type list')
    if not all([isinstance(t, str) for t in featured_user_names]):
      raise TypeError('featured_user_names must contain only items of type str')
    self._featured_user_names = featured_user_names

  @property
  def user_count(self) -> int:
    r"""
    The total number of users who've reacted (including any not included in
    usernames).
    """
    return self._user_count

  @user_count.setter
  def user_count(self, user_count: int):
    if user_count is None:
      del self.user_count
      return
    if not isinstance(user_count, int):
      raise TypeError('user_count must be of type int')
    self._user_count = user_count


CommentAttachment._fields = [
  FieldMetadata("fileType", "file_type", "_file_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("blobToken", "blob_token", "_blob_token", str, None, PredefinedSerializer(), optional=True),
]

CommentForumMessage._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("postDate", "post_date", "_post_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("rawMarkdown", "raw_markdown", "_raw_markdown", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("replies", "replies", "_replies", CommentForumMessage, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("attachments", "attachments", "_attachments", CommentAttachment, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("parent", "parent", "_parent", DiscussionItemLink, None, KaggleObjectSerializer()),
  FieldMetadata("author", "author", "_author", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("authorType", "author_type", "_author_type", CommentAuthorType, CommentAuthorType.COMMENT_AUTHOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("votes", "votes", "_votes", CommentVoteButton, None, KaggleObjectSerializer()),
  FieldMetadata("canDelete", "can_delete", "_can_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("isUserAuthor", "is_user_author", "_is_user_author", bool, False, PredefinedSerializer()),
  FieldMetadata("hasFlags", "has_flags", "_has_flags", bool, False, PredefinedSerializer()),
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("isAdminDeleted", "is_admin_deleted", "_is_admin_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("isFlagged", "is_flagged", "_is_flagged", bool, False, PredefinedSerializer()),
  FieldMetadata("isSpammed", "is_spammed", "_is_spammed", bool, False, PredefinedSerializer()),
  FieldMetadata("currentKernelVersion", "current_kernel_version", "_current_kernel_version", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelVersion", "kernel_version", "_kernel_version", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionRanking", "competition_ranking", "_competition_ranking", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("feedbackTrackingData", "feedback_tracking_data", "_feedback_tracking_data", FeedbackTrackingData, None, KaggleObjectSerializer()),
  FieldMetadata("isPinned", "is_pinned", "_is_pinned", bool, False, PredefinedSerializer()),
  FieldMetadata("isAutoPrivated", "is_auto_privated", "_is_auto_privated", bool, False, PredefinedSerializer()),
  FieldMetadata("moderationStatus", "moderation_status", "_moderation_status", PrivatedModerationStatus, PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isThankYou", "is_thank_you", "_is_thank_you", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isCollapsed", "is_collapsed", "_is_collapsed", bool, False, PredefinedSerializer()),
  FieldMetadata("isPartial", "is_partial", "_is_partial", bool, False, PredefinedSerializer()),
  FieldMetadata("reactions", "reactions", "_reactions", ForumMessageReactionGroup, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teamUpInfo", "team_up_info", "_team_up_info", TeamUpInfo, None, KaggleObjectSerializer()),
]

CommentVoteButton._fields = [
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("hasAlreadyVotedUp", "has_already_voted_up", "_has_already_voted_up", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAlreadyVotedDown", "has_already_voted_down", "_has_already_voted_down", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpvote", "can_upvote", "_can_upvote", bool, False, PredefinedSerializer()),
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("totalUpvotes", "total_upvotes", "_total_upvotes", int, 0, PredefinedSerializer()),
]

DiscussionItemLink._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

ForumMessageReactionGroup._fields = [
  FieldMetadata("emoji", "emoji", "_emoji", EmojiReaction, EmojiReaction.EMOJI_REACTION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("featuredUserNames", "featured_user_names", "_featured_user_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userCount", "user_count", "_user_count", int, 0, PredefinedSerializer()),
]

