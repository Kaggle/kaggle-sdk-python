from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from typing import Optional

class CreateFeaturedResourceRequest(KaggleObject):
  r"""
  Attributes:
    featured_resource (FeaturedResource)
  """

  def __init__(self):
    self._featured_resource = None
    self._freeze()

  @property
  def featured_resource(self) -> Optional['FeaturedResource']:
    return self._featured_resource

  @featured_resource.setter
  def featured_resource(self, featured_resource: Optional['FeaturedResource']):
    if featured_resource is None:
      del self.featured_resource
      return
    if not isinstance(featured_resource, FeaturedResource):
      raise TypeError('featured_resource must be of type FeaturedResource')
    self._featured_resource = featured_resource


class DeleteFeaturedResourceRequest(KaggleObject):
  r"""
  Attributes:
    featured_resource_id (int)
    force_delete (bool)
      If we need to delete past featured resources, set this flag.
  """

  def __init__(self):
    self._featured_resource_id = 0
    self._force_delete = None
    self._freeze()

  @property
  def featured_resource_id(self) -> int:
    return self._featured_resource_id

  @featured_resource_id.setter
  def featured_resource_id(self, featured_resource_id: int):
    if featured_resource_id is None:
      del self.featured_resource_id
      return
    if not isinstance(featured_resource_id, int):
      raise TypeError('featured_resource_id must be of type int')
    self._featured_resource_id = featured_resource_id

  @property
  def force_delete(self) -> bool:
    """If we need to delete past featured resources, set this flag."""
    return self._force_delete or False

  @force_delete.setter
  def force_delete(self, force_delete: Optional[bool]):
    if force_delete is None:
      del self.force_delete
      return
    if not isinstance(force_delete, bool):
      raise TypeError('force_delete must be of type bool')
    self._force_delete = force_delete


class FeaturedResource(KaggleObject):
  r"""
  Attributes:
    id (int)
    feature_start_date (datetime)
    feature_end_date (datetime)
    model_id (int)
    dataset_id (int)
  """

  def __init__(self):
    self._id = None
    self._feature_start_date = None
    self._feature_end_date = None
    self._model_id = None
    self._dataset_id = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def feature_start_date(self) -> datetime:
    return self._feature_start_date

  @feature_start_date.setter
  def feature_start_date(self, feature_start_date: datetime):
    if feature_start_date is None:
      del self.feature_start_date
      return
    if not isinstance(feature_start_date, datetime):
      raise TypeError('feature_start_date must be of type datetime')
    self._feature_start_date = feature_start_date

  @property
  def feature_end_date(self) -> datetime:
    return self._feature_end_date

  @feature_end_date.setter
  def feature_end_date(self, feature_end_date: datetime):
    if feature_end_date is None:
      del self.feature_end_date
      return
    if not isinstance(feature_end_date, datetime):
      raise TypeError('feature_end_date must be of type datetime')
    self._feature_end_date = feature_end_date

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.dataset_id
    self._model_id = model_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.model_id
    self._dataset_id = dataset_id


class GetFeaturedResourceRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    dataset_id (int)
  """

  def __init__(self):
    self._model_id = None
    self._dataset_id = None
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.dataset_id
    self._model_id = model_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.model_id
    self._dataset_id = dataset_id


class UpdateFeaturedResourceRequest(KaggleObject):
  r"""
  Attributes:
    featured_resource (FeaturedResource)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._featured_resource = None
    self._update_mask = None
    self._freeze()

  @property
  def featured_resource(self) -> Optional['FeaturedResource']:
    return self._featured_resource

  @featured_resource.setter
  def featured_resource(self, featured_resource: Optional['FeaturedResource']):
    if featured_resource is None:
      del self.featured_resource
      return
    if not isinstance(featured_resource, FeaturedResource):
      raise TypeError('featured_resource must be of type FeaturedResource')
    self._featured_resource = featured_resource

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


CreateFeaturedResourceRequest._fields = [
  FieldMetadata("featuredResource", "featured_resource", "_featured_resource", FeaturedResource, None, KaggleObjectSerializer()),
]

DeleteFeaturedResourceRequest._fields = [
  FieldMetadata("featuredResourceId", "featured_resource_id", "_featured_resource_id", int, 0, PredefinedSerializer()),
  FieldMetadata("forceDelete", "force_delete", "_force_delete", bool, None, PredefinedSerializer(), optional=True),
]

FeaturedResource._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("featureStartDate", "feature_start_date", "_feature_start_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("featureEndDate", "feature_end_date", "_feature_end_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
]

GetFeaturedResourceRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
]

UpdateFeaturedResourceRequest._fields = [
  FieldMetadata("featuredResource", "featured_resource", "_featured_resource", FeaturedResource, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

