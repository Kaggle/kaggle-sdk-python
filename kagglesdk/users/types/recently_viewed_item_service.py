from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class RecentlyViewedItemType(enum.Enum):
  RECENTLY_VIEWED_ITEM_TYPE_UNSPECIFIED = 0
  COMPETITION = 1
  DATASET = 2
  KERNEL = 4
  TOPIC = 5
  COURSE = 6
  FORUM = 7
  CMS_PAGE = 8
  MODEL = 9
  COLLECTION = 10
  BENCHMARK = 11
  BENCHMARK_TASK = 12

class ReturnedItemsType(enum.Enum):
  RETURNED_ITEMS_TYPE_UNSPECIFIED = 0
  EDITED = 1
  VIEWED = 2
  ALL = 3
  ALL_TYPE_AND_IDS_ONLY = 4

class GetRecentlyViewedItemsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    item_count (int)
    returned_type (ReturnedItemsType)
    item_type_filter (RecentlyViewedItemType)
  """

  def __init__(self):
    self._user_id = 0
    self._item_count = 0
    self._returned_type = ReturnedItemsType.RETURNED_ITEMS_TYPE_UNSPECIFIED
    self._item_type_filter = None
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def item_count(self) -> int:
    return self._item_count

  @item_count.setter
  def item_count(self, item_count: int):
    if item_count is None:
      del self.item_count
      return
    if not isinstance(item_count, int):
      raise TypeError('item_count must be of type int')
    self._item_count = item_count

  @property
  def returned_type(self) -> 'ReturnedItemsType':
    return self._returned_type

  @returned_type.setter
  def returned_type(self, returned_type: 'ReturnedItemsType'):
    if returned_type is None:
      del self.returned_type
      return
    if not isinstance(returned_type, ReturnedItemsType):
      raise TypeError('returned_type must be of type ReturnedItemsType')
    self._returned_type = returned_type

  @property
  def item_type_filter(self) -> 'RecentlyViewedItemType':
    return self._item_type_filter or RecentlyViewedItemType.RECENTLY_VIEWED_ITEM_TYPE_UNSPECIFIED

  @item_type_filter.setter
  def item_type_filter(self, item_type_filter: Optional['RecentlyViewedItemType']):
    if item_type_filter is None:
      del self.item_type_filter
      return
    if not isinstance(item_type_filter, RecentlyViewedItemType):
      raise TypeError('item_type_filter must be of type RecentlyViewedItemType')
    self._item_type_filter = item_type_filter


class GetRecentlyViewedItemsResponse(KaggleObject):
  r"""
  Attributes:
    recently_viewed_items (RecentlyViewedItem)
  """

  def __init__(self):
    self._recently_viewed_items = []
    self._freeze()

  @property
  def recently_viewed_items(self) -> Optional[List[Optional['RecentlyViewedItem']]]:
    return self._recently_viewed_items

  @recently_viewed_items.setter
  def recently_viewed_items(self, recently_viewed_items: Optional[List[Optional['RecentlyViewedItem']]]):
    if recently_viewed_items is None:
      del self.recently_viewed_items
      return
    if not isinstance(recently_viewed_items, list):
      raise TypeError('recently_viewed_items must be of type list')
    if not all([isinstance(t, RecentlyViewedItem) for t in recently_viewed_items]):
      raise TypeError('recently_viewed_items must contain only items of type RecentlyViewedItem')
    self._recently_viewed_items = recently_viewed_items


class RecentlyViewedItem(KaggleObject):
  r"""
  Attributes:
    title (str)
    url (str)
    item_type (RecentlyViewedItemType)
    author_slug (str)
    most_recent_view (datetime)
    thumbnail_url (str)
    id (int)
  """

  def __init__(self):
    self._title = ""
    self._url = ""
    self._item_type = RecentlyViewedItemType.RECENTLY_VIEWED_ITEM_TYPE_UNSPECIFIED
    self._author_slug = ""
    self._most_recent_view = None
    self._thumbnail_url = ""
    self._id = 0
    self._freeze()

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
  def item_type(self) -> 'RecentlyViewedItemType':
    return self._item_type

  @item_type.setter
  def item_type(self, item_type: 'RecentlyViewedItemType'):
    if item_type is None:
      del self.item_type
      return
    if not isinstance(item_type, RecentlyViewedItemType):
      raise TypeError('item_type must be of type RecentlyViewedItemType')
    self._item_type = item_type

  @property
  def author_slug(self) -> str:
    return self._author_slug

  @author_slug.setter
  def author_slug(self, author_slug: str):
    if author_slug is None:
      del self.author_slug
      return
    if not isinstance(author_slug, str):
      raise TypeError('author_slug must be of type str')
    self._author_slug = author_slug

  @property
  def most_recent_view(self) -> datetime:
    return self._most_recent_view

  @most_recent_view.setter
  def most_recent_view(self, most_recent_view: datetime):
    if most_recent_view is None:
      del self.most_recent_view
      return
    if not isinstance(most_recent_view, datetime):
      raise TypeError('most_recent_view must be of type datetime')
    self._most_recent_view = most_recent_view

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

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


GetRecentlyViewedItemsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("itemCount", "item_count", "_item_count", int, 0, PredefinedSerializer()),
  FieldMetadata("returnedType", "returned_type", "_returned_type", ReturnedItemsType, ReturnedItemsType.RETURNED_ITEMS_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("itemTypeFilter", "item_type_filter", "_item_type_filter", RecentlyViewedItemType, None, EnumSerializer(), optional=True),
]

GetRecentlyViewedItemsResponse._fields = [
  FieldMetadata("recentlyViewedItems", "recently_viewed_items", "_recently_viewed_items", RecentlyViewedItem, [], ListSerializer(KaggleObjectSerializer())),
]

RecentlyViewedItem._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("itemType", "item_type", "_item_type", RecentlyViewedItemType, RecentlyViewedItemType.RECENTLY_VIEWED_ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("authorSlug", "author_slug", "_author_slug", str, "", PredefinedSerializer()),
  FieldMetadata("mostRecentView", "most_recent_view", "_most_recent_view", datetime, None, DateTimeSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

