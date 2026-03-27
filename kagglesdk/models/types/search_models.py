import enum
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_content_shared import ListSearchContentRangeFilter
from typing import Optional

class SearchModelsOrderBy(enum.Enum):
  MODELS_SEARCH_ORDER_BY_UNSPECIFIED = 0
  MODELS_SEARCH_ORDER_BY_DOWNLOAD_COUNT = 1
  MODELS_SEARCH_ORDER_BY_NOTEBOOK_COUNT = 2
  MODELS_SEARCH_ORDER_BY_PUBLISH_DATE = 3

class SearchModelsDocument(KaggleObject):
  r"""
  Attributes:
    instance_count (int)
      The total number of instances in the Model
    notebook_count (int)
      The total number of notebooks in the Model
  """

  def __init__(self):
    self._instance_count = 0
    self._notebook_count = 0
    self._freeze()

  @property
  def instance_count(self) -> int:
    """The total number of instances in the Model"""
    return self._instance_count

  @instance_count.setter
  def instance_count(self, instance_count: int):
    if instance_count is None:
      del self.instance_count
      return
    if not isinstance(instance_count, int):
      raise TypeError('instance_count must be of type int')
    self._instance_count = instance_count

  @property
  def notebook_count(self) -> int:
    """The total number of notebooks in the Model"""
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count


class SearchModelsFilters(KaggleObject):
  r"""
  Used by kaggle.search.ListSearchContent for filtering lists on Your Work or
  User Profile

  Attributes:
    size (ListSearchContentRangeFilter)
      The size of the Model used to filter the documents
  """

  def __init__(self):
    self._size = None
    self._freeze()

  @property
  def size(self) -> Optional['ListSearchContentRangeFilter']:
    """The size of the Model used to filter the documents"""
    return self._size

  @size.setter
  def size(self, size: Optional['ListSearchContentRangeFilter']):
    if size is None:
      del self.size
      return
    if not isinstance(size, ListSearchContentRangeFilter):
      raise TypeError('size must be of type ListSearchContentRangeFilter')
    self._size = size


SearchModelsDocument._fields = [
  FieldMetadata("instanceCount", "instance_count", "_instance_count", int, 0, PredefinedSerializer()),
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
]

SearchModelsFilters._fields = [
  FieldMetadata("size", "size", "_size", ListSearchContentRangeFilter, None, KaggleObjectSerializer()),
]

