import enum
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_content_service import ListSearchContentAggregation
from typing import List, Optional

class ListCollectionsOrderBy(enum.Enum):
  LIST_COLLECTIONS_ORDER_BY_UNSPECIFIED = 0
  LIST_COLLECTIONS_ORDER_BY_RECENTLY_CREATED_COLLECTION = 3
  LIST_COLLECTIONS_ORDER_BY_LAST_OPENED_COLLECTION = 2

class AccessCollectionItemRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition ID of the item
    dataset_id (int)
      The dataset ID of the item
    kernel_id (int)
      The kernel ID of the item
    forum_topic_id (int)
      The forum topic ID of the item
    forum_message_id (int)
      The forum message ID of the item
    model_id (int)
      The model ID of the item
  """

  def __init__(self):
    self._competition_id = None
    self._dataset_id = None
    self._kernel_id = None
    self._forum_topic_id = None
    self._forum_message_id = None
    self._model_id = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition ID of the item"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.forum_topic_id
    del self.forum_message_id
    del self.model_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    """The dataset ID of the item"""
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.kernel_id
    del self.forum_topic_id
    del self.forum_message_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    """The kernel ID of the item"""
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.forum_topic_id
    del self.forum_message_id
    del self.model_id
    self._kernel_id = kernel_id

  @property
  def forum_topic_id(self) -> int:
    """The forum topic ID of the item"""
    return self._forum_topic_id or 0

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.forum_message_id
    del self.model_id
    self._forum_topic_id = forum_topic_id

  @property
  def forum_message_id(self) -> int:
    """The forum message ID of the item"""
    return self._forum_message_id or 0

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.forum_topic_id
    del self.model_id
    self._forum_message_id = forum_message_id

  @property
  def model_id(self) -> int:
    """The model ID of the item"""
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    del self.kernel_id
    del self.forum_topic_id
    del self.forum_message_id
    self._model_id = model_id


class Collection(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection
    name (str)
      The name of the collection
    item_count (int)
      The total items contained in the collection
    is_auto_generated (bool)
      Whether the collection is auto-generated
    aggregations (ListSearchContentAggregation)
      The total items contained in the collection, grouped by document type
  """

  def __init__(self):
    self._collection_id = 0
    self._name = ""
    self._item_count = 0
    self._is_auto_generated = False
    self._aggregations = []
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id

  @property
  def name(self) -> str:
    """The name of the collection"""
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
  def item_count(self) -> int:
    """The total items contained in the collection"""
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
  def is_auto_generated(self) -> bool:
    """Whether the collection is auto-generated"""
    return self._is_auto_generated

  @is_auto_generated.setter
  def is_auto_generated(self, is_auto_generated: bool):
    if is_auto_generated is None:
      del self.is_auto_generated
      return
    if not isinstance(is_auto_generated, bool):
      raise TypeError('is_auto_generated must be of type bool')
    self._is_auto_generated = is_auto_generated

  @property
  def aggregations(self) -> Optional[List[Optional['ListSearchContentAggregation']]]:
    """The total items contained in the collection, grouped by document type"""
    return self._aggregations

  @aggregations.setter
  def aggregations(self, aggregations: Optional[List[Optional['ListSearchContentAggregation']]]):
    if aggregations is None:
      del self.aggregations
      return
    if not isinstance(aggregations, list):
      raise TypeError('aggregations must be of type list')
    if not all([isinstance(t, ListSearchContentAggregation) for t in aggregations]):
      raise TypeError('aggregations must contain only items of type ListSearchContentAggregation')
    self._aggregations = aggregations


class CreateCollectionItemsRequest(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection to add the items to
    items (AccessCollectionItemRequest)
      All of the items contained in the collection
  """

  def __init__(self):
    self._collection_id = 0
    self._items = []
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection to add the items to"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id

  @property
  def items(self) -> Optional[List[Optional['AccessCollectionItemRequest']]]:
    """All of the items contained in the collection"""
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['AccessCollectionItemRequest']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, AccessCollectionItemRequest) for t in items]):
      raise TypeError('items must contain only items of type AccessCollectionItemRequest')
    self._items = items


class CreateCollectionRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
      The name of the collection
    competition_id (int)
      The ID of the competition for auto-generated competitions
  """

  def __init__(self):
    self._name = None
    self._competition_id = None
    self._freeze()

  @property
  def name(self) -> str:
    """The name of the collection"""
    return self._name or ""

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    del self.competition_id
    self._name = name

  @property
  def competition_id(self) -> int:
    """The ID of the competition for auto-generated competitions"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.name
    self._competition_id = competition_id


class CreateCollectionResponse(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection
  """

  def __init__(self):
    self._collection_id = 0
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id


class DeleteCollectionItemsRequest(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection containing the items to delete
    items (AccessCollectionItemRequest)
      The list of IDs to delete from the collection
  """

  def __init__(self):
    self._collection_id = 0
    self._items = []
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection containing the items to delete"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id

  @property
  def items(self) -> Optional[List[Optional['AccessCollectionItemRequest']]]:
    """The list of IDs to delete from the collection"""
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['AccessCollectionItemRequest']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, AccessCollectionItemRequest) for t in items]):
      raise TypeError('items must contain only items of type AccessCollectionItemRequest')
    self._items = items


class DeleteCollectionRequest(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection to delete
  """

  def __init__(self):
    self._collection_id = 0
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection to delete"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id


class ListCollectionsRequest(KaggleObject):
  r"""
  Attributes:
    name_filter (str)
      The name of the collection to filter the results by
    item_filter (AccessCollectionItemRequest)
      All of the items contained in the collection
    omit_counts (bool)
      Whether to omit (potentially expensive) counts when listing Collections
    order_by (ListCollectionsOrderBy)
      The sort used when listing Collections
  """

  def __init__(self):
    self._name_filter = None
    self._item_filter = None
    self._omit_counts = None
    self._order_by = None
    self._freeze()

  @property
  def name_filter(self) -> str:
    """The name of the collection to filter the results by"""
    return self._name_filter or ""

  @name_filter.setter
  def name_filter(self, name_filter: Optional[str]):
    if name_filter is None:
      del self.name_filter
      return
    if not isinstance(name_filter, str):
      raise TypeError('name_filter must be of type str')
    self._name_filter = name_filter

  @property
  def item_filter(self) -> Optional['AccessCollectionItemRequest']:
    """All of the items contained in the collection"""
    return self._item_filter or None

  @item_filter.setter
  def item_filter(self, item_filter: Optional[Optional['AccessCollectionItemRequest']]):
    if item_filter is None:
      del self.item_filter
      return
    if not isinstance(item_filter, AccessCollectionItemRequest):
      raise TypeError('item_filter must be of type AccessCollectionItemRequest')
    self._item_filter = item_filter

  @property
  def omit_counts(self) -> bool:
    """Whether to omit (potentially expensive) counts when listing Collections"""
    return self._omit_counts or False

  @omit_counts.setter
  def omit_counts(self, omit_counts: Optional[bool]):
    if omit_counts is None:
      del self.omit_counts
      return
    if not isinstance(omit_counts, bool):
      raise TypeError('omit_counts must be of type bool')
    self._omit_counts = omit_counts

  @property
  def order_by(self) -> 'ListCollectionsOrderBy':
    """The sort used when listing Collections"""
    return self._order_by or ListCollectionsOrderBy.LIST_COLLECTIONS_ORDER_BY_UNSPECIFIED

  @order_by.setter
  def order_by(self, order_by: Optional['ListCollectionsOrderBy']):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListCollectionsOrderBy):
      raise TypeError('order_by must be of type ListCollectionsOrderBy')
    self._order_by = order_by


class ListCollectionsResponse(KaggleObject):
  r"""
  Attributes:
    collections (Collection)
      The list of collections created by the current user
  """

  def __init__(self):
    self._collections = []
    self._freeze()

  @property
  def collections(self) -> Optional[List[Optional['Collection']]]:
    """The list of collections created by the current user"""
    return self._collections

  @collections.setter
  def collections(self, collections: Optional[List[Optional['Collection']]]):
    if collections is None:
      del self.collections
      return
    if not isinstance(collections, list):
      raise TypeError('collections must be of type list')
    if not all([isinstance(t, Collection) for t in collections]):
      raise TypeError('collections must contain only items of type Collection')
    self._collections = collections


class UpdateCollectionRequest(KaggleObject):
  r"""
  Attributes:
    collection_id (int)
      The ID of the collection
    name (str)
      The updated name of the collection
  """

  def __init__(self):
    self._collection_id = 0
    self._name = ""
    self._freeze()

  @property
  def collection_id(self) -> int:
    """The ID of the collection"""
    return self._collection_id

  @collection_id.setter
  def collection_id(self, collection_id: int):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id

  @property
  def name(self) -> str:
    """The updated name of the collection"""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


AccessCollectionItemRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

Collection._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("itemCount", "item_count", "_item_count", int, 0, PredefinedSerializer()),
  FieldMetadata("isAutoGenerated", "is_auto_generated", "_is_auto_generated", bool, False, PredefinedSerializer()),
  FieldMetadata("aggregations", "aggregations", "_aggregations", ListSearchContentAggregation, [], ListSerializer(KaggleObjectSerializer())),
]

CreateCollectionItemsRequest._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
  FieldMetadata("items", "items", "_items", AccessCollectionItemRequest, [], ListSerializer(KaggleObjectSerializer())),
]

CreateCollectionRequest._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
]

CreateCollectionResponse._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
]

DeleteCollectionItemsRequest._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
  FieldMetadata("items", "items", "_items", AccessCollectionItemRequest, [], ListSerializer(KaggleObjectSerializer())),
]

DeleteCollectionRequest._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
]

ListCollectionsRequest._fields = [
  FieldMetadata("nameFilter", "name_filter", "_name_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("itemFilter", "item_filter", "_item_filter", AccessCollectionItemRequest, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("omitCounts", "omit_counts", "_omit_counts", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("orderBy", "order_by", "_order_by", ListCollectionsOrderBy, None, EnumSerializer(), optional=True),
]

ListCollectionsResponse._fields = [
  FieldMetadata("collections", "collections", "_collections", Collection, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateCollectionRequest._fields = [
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

