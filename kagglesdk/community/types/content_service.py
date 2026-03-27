from kagglesdk.kaggle_object import *
from typing import List, Optional

class BatchDeleteItemsRequest(KaggleObject):
  r"""
  Attributes:
    item (Item)
      A list of items to delete
  """

  def __init__(self):
    self._item = []
    self._freeze()

  @property
  def item(self) -> Optional[List[Optional['Item']]]:
    """A list of items to delete"""
    return self._item

  @item.setter
  def item(self, item: Optional[List[Optional['Item']]]):
    if item is None:
      del self.item
      return
    if not isinstance(item, list):
      raise TypeError('item must be of type list')
    if not all([isinstance(t, Item) for t in item]):
      raise TypeError('item must contain only items of type Item')
    self._item = item


class Item(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
      The ID of the dataset to delete
    kernel_id (int)
      The ID of the kernel to delete
    model_id (int)
      The ID of the model to delete
  """

  def __init__(self):
    self._dataset_id = None
    self._kernel_id = None
    self._model_id = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    """The ID of the dataset to delete"""
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.kernel_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    """The ID of the kernel to delete"""
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.dataset_id
    del self.model_id
    self._kernel_id = kernel_id

  @property
  def model_id(self) -> int:
    """The ID of the model to delete"""
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    self._model_id = model_id


BatchDeleteItemsRequest._fields = [
  FieldMetadata("item", "item", "_item", Item, [], ListSerializer(KaggleObjectSerializer())),
]

Item._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

