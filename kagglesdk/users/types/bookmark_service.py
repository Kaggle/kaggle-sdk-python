from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BookmarkType(enum.Enum):
  BOOKMARK_TYPE_UNSPECIFIED = 0
  BOOKMARK_TYPE_COMPETITION = 1
  BOOKMARK_TYPE_DATASET = 2
  BOOKMARK_TYPE_FORUM_TOPIC = 3
  BOOKMARK_TYPE_KERNEL = 4
  BOOKMARK_TYPE_MODEL = 5

class Bookmark(KaggleObject):
  r"""
  Attributes:
    bookmark_type (BookmarkType)
      The content type for a given Bookmark
    bookmarked_entity_id (int)
      The ID for the underlying entity, of content type bookmark_type
    title (str)
      Title of the piece of content
    url (str)
      URL linking to the piece of content
    author_slug (str)
      Slug to link to the author user
    thumbnail_url (str)
      URL for the thumbnail of the piece of content
    bookmarked_date (datetime)
      The timestamp for when a bookmark was created
  """

  def __init__(self):
    self._bookmark_type = BookmarkType.BOOKMARK_TYPE_UNSPECIFIED
    self._bookmarked_entity_id = 0
    self._title = None
    self._url = None
    self._author_slug = None
    self._thumbnail_url = None
    self._bookmarked_date = None
    self._freeze()

  @property
  def bookmark_type(self) -> 'BookmarkType':
    """The content type for a given Bookmark"""
    return self._bookmark_type

  @bookmark_type.setter
  def bookmark_type(self, bookmark_type: 'BookmarkType'):
    if bookmark_type is None:
      del self.bookmark_type
      return
    if not isinstance(bookmark_type, BookmarkType):
      raise TypeError('bookmark_type must be of type BookmarkType')
    self._bookmark_type = bookmark_type

  @property
  def bookmarked_entity_id(self) -> int:
    """The ID for the underlying entity, of content type bookmark_type"""
    return self._bookmarked_entity_id

  @bookmarked_entity_id.setter
  def bookmarked_entity_id(self, bookmarked_entity_id: int):
    if bookmarked_entity_id is None:
      del self.bookmarked_entity_id
      return
    if not isinstance(bookmarked_entity_id, int):
      raise TypeError('bookmarked_entity_id must be of type int')
    self._bookmarked_entity_id = bookmarked_entity_id

  @property
  def title(self) -> str:
    """Title of the piece of content"""
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
  def url(self) -> str:
    """URL linking to the piece of content"""
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
  def author_slug(self) -> str:
    """Slug to link to the author user"""
    return self._author_slug or ""

  @author_slug.setter
  def author_slug(self, author_slug: Optional[str]):
    if author_slug is None:
      del self.author_slug
      return
    if not isinstance(author_slug, str):
      raise TypeError('author_slug must be of type str')
    self._author_slug = author_slug

  @property
  def thumbnail_url(self) -> str:
    """URL for the thumbnail of the piece of content"""
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def bookmarked_date(self) -> datetime:
    """The timestamp for when a bookmark was created"""
    return self._bookmarked_date

  @bookmarked_date.setter
  def bookmarked_date(self, bookmarked_date: datetime):
    if bookmarked_date is None:
      del self.bookmarked_date
      return
    if not isinstance(bookmarked_date, datetime):
      raise TypeError('bookmarked_date must be of type datetime')
    self._bookmarked_date = bookmarked_date


class CreateBookmarkRequest(KaggleObject):
  r"""
  Attributes:
    bookmark (Bookmark)
      A Bookmark message describing what Bookmark to create for the current user
  """

  def __init__(self):
    self._bookmark = None
    self._freeze()

  @property
  def bookmark(self) -> Optional['Bookmark']:
    """A Bookmark message describing what Bookmark to create for the current user"""
    return self._bookmark

  @bookmark.setter
  def bookmark(self, bookmark: Optional['Bookmark']):
    if bookmark is None:
      del self.bookmark
      return
    if not isinstance(bookmark, Bookmark):
      raise TypeError('bookmark must be of type Bookmark')
    self._bookmark = bookmark


class CreateBookmarkResponse(KaggleObject):
  r"""
  """

  pass

class DeleteBookmarkRequest(KaggleObject):
  r"""
  Attributes:
    bookmark (Bookmark)
      A Bookmark message describing what Bookmark to delete for the current user
  """

  def __init__(self):
    self._bookmark = None
    self._freeze()

  @property
  def bookmark(self) -> Optional['Bookmark']:
    """A Bookmark message describing what Bookmark to delete for the current user"""
    return self._bookmark

  @bookmark.setter
  def bookmark(self, bookmark: Optional['Bookmark']):
    if bookmark is None:
      del self.bookmark
      return
    if not isinstance(bookmark, Bookmark):
      raise TypeError('bookmark must be of type Bookmark')
    self._bookmark = bookmark


class DeleteBookmarkResponse(KaggleObject):
  r"""
  """

  pass

class ListAllBookmarksRequest(KaggleObject):
  r"""
  Attributes:
    item_count (int)
      The number of bookmarks to return
  """

  def __init__(self):
    self._item_count = 0
    self._freeze()

  @property
  def item_count(self) -> int:
    """The number of bookmarks to return"""
    return self._item_count

  @item_count.setter
  def item_count(self, item_count: int):
    if item_count is None:
      del self.item_count
      return
    if not isinstance(item_count, int):
      raise TypeError('item_count must be of type int')
    self._item_count = item_count


class ListAllBookmarksResponse(KaggleObject):
  r"""
  Attributes:
    bookmarks (Bookmark)
      Bookmark objects for the current user
  """

  def __init__(self):
    self._bookmarks = []
    self._freeze()

  @property
  def bookmarks(self) -> Optional[List[Optional['Bookmark']]]:
    """Bookmark objects for the current user"""
    return self._bookmarks

  @bookmarks.setter
  def bookmarks(self, bookmarks: Optional[List[Optional['Bookmark']]]):
    if bookmarks is None:
      del self.bookmarks
      return
    if not isinstance(bookmarks, list):
      raise TypeError('bookmarks must be of type list')
    if not all([isinstance(t, Bookmark) for t in bookmarks]):
      raise TypeError('bookmarks must contain only items of type Bookmark')
    self._bookmarks = bookmarks


Bookmark._fields = [
  FieldMetadata("bookmarkType", "bookmark_type", "_bookmark_type", BookmarkType, BookmarkType.BOOKMARK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("bookmarkedEntityId", "bookmarked_entity_id", "_bookmarked_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorSlug", "author_slug", "_author_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bookmarkedDate", "bookmarked_date", "_bookmarked_date", datetime, None, DateTimeSerializer()),
]

CreateBookmarkRequest._fields = [
  FieldMetadata("bookmark", "bookmark", "_bookmark", Bookmark, None, KaggleObjectSerializer()),
]

CreateBookmarkResponse._fields = []

DeleteBookmarkRequest._fields = [
  FieldMetadata("bookmark", "bookmark", "_bookmark", Bookmark, None, KaggleObjectSerializer()),
]

DeleteBookmarkResponse._fields = []

ListAllBookmarksRequest._fields = [
  FieldMetadata("itemCount", "item_count", "_item_count", int, 0, PredefinedSerializer()),
]

ListAllBookmarksResponse._fields = [
  FieldMetadata("bookmarks", "bookmarks", "_bookmarks", Bookmark, [], ListSerializer(KaggleObjectSerializer())),
]

