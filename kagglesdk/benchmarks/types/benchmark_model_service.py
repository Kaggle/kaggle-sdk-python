from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkModel, BenchmarkModelVersion
from kagglesdk.kaggle_object import *
from typing import Optional, List, Dict

class CreateBenchmarkModelRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model (BenchmarkModel)
      The benchmark model to create.
  """

  def __init__(self):
    self._benchmark_model = None
    self._freeze()

  @property
  def benchmark_model(self) -> Optional['BenchmarkModel']:
    """The benchmark model to create."""
    return self._benchmark_model

  @benchmark_model.setter
  def benchmark_model(self, benchmark_model: Optional['BenchmarkModel']):
    if benchmark_model is None:
      del self.benchmark_model
      return
    if not isinstance(benchmark_model, BenchmarkModel):
      raise TypeError('benchmark_model must be of type BenchmarkModel')
    self._benchmark_model = benchmark_model


class CreateBenchmarkModelVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version (BenchmarkModelVersion)
      The benchmark model version to create.
  """

  def __init__(self):
    self._benchmark_model_version = None
    self._freeze()

  @property
  def benchmark_model_version(self) -> Optional['BenchmarkModelVersion']:
    """The benchmark model version to create."""
    return self._benchmark_model_version

  @benchmark_model_version.setter
  def benchmark_model_version(self, benchmark_model_version: Optional['BenchmarkModelVersion']):
    if benchmark_model_version is None:
      del self.benchmark_model_version
      return
    if not isinstance(benchmark_model_version, BenchmarkModelVersion):
      raise TypeError('benchmark_model_version must be of type BenchmarkModelVersion')
    self._benchmark_model_version = benchmark_model_version


class DeleteBenchmarkModelRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model_id (int)
      Id of the resource to be deleted.
    is_user_delete (bool)
      If false, the deletion is treated as done by an admin.
  """

  def __init__(self):
    self._benchmark_model_id = 0
    self._is_user_delete = False
    self._freeze()

  @property
  def benchmark_model_id(self) -> int:
    """Id of the resource to be deleted."""
    return self._benchmark_model_id

  @benchmark_model_id.setter
  def benchmark_model_id(self, benchmark_model_id: int):
    if benchmark_model_id is None:
      del self.benchmark_model_id
      return
    if not isinstance(benchmark_model_id, int):
      raise TypeError('benchmark_model_id must be of type int')
    self._benchmark_model_id = benchmark_model_id

  @property
  def is_user_delete(self) -> bool:
    """If false, the deletion is treated as done by an admin."""
    return self._is_user_delete

  @is_user_delete.setter
  def is_user_delete(self, is_user_delete: bool):
    if is_user_delete is None:
      del self.is_user_delete
      return
    if not isinstance(is_user_delete, bool):
      raise TypeError('is_user_delete must be of type bool')
    self._is_user_delete = is_user_delete


class DeleteBenchmarkModelVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version_id (int)
      Id of the resource to be deleted.
    is_user_delete (bool)
      If false, the deletion is treated as done by an admin.
  """

  def __init__(self):
    self._benchmark_model_version_id = 0
    self._is_user_delete = False
    self._freeze()

  @property
  def benchmark_model_version_id(self) -> int:
    """Id of the resource to be deleted."""
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def is_user_delete(self) -> bool:
    """If false, the deletion is treated as done by an admin."""
    return self._is_user_delete

  @is_user_delete.setter
  def is_user_delete(self, is_user_delete: bool):
    if is_user_delete is None:
      del self.is_user_delete
      return
    if not isinstance(is_user_delete, bool):
      raise TypeError('is_user_delete must be of type bool')
    self._is_user_delete = is_user_delete


class GetBenchmarkModelThumbnailsRequest(KaggleObject):
  r"""
  Attributes:
    model_proxy_slugs (str)
      Model proxy slugs to resolve (e.g. 'google/gemini-2.5-flash').
  """

  def __init__(self):
    self._model_proxy_slugs = []
    self._freeze()

  @property
  def model_proxy_slugs(self) -> Optional[List[str]]:
    """Model proxy slugs to resolve (e.g. 'google/gemini-2.5-flash')."""
    return self._model_proxy_slugs

  @model_proxy_slugs.setter
  def model_proxy_slugs(self, model_proxy_slugs: Optional[List[str]]):
    if model_proxy_slugs is None:
      del self.model_proxy_slugs
      return
    if not isinstance(model_proxy_slugs, list):
      raise TypeError('model_proxy_slugs must be of type list')
    if not all([isinstance(t, str) for t in model_proxy_slugs]):
      raise TypeError('model_proxy_slugs must contain only items of type str')
    self._model_proxy_slugs = model_proxy_slugs


class GetBenchmarkModelThumbnailsResponse(KaggleObject):
  r"""
  Attributes:
    thumbnails (str)
      Map of model proxy slug to the organization's thumbnail image URL.
  """

  def __init__(self):
    self._thumbnails = {}
    self._freeze()

  @property
  def thumbnails(self) -> Optional[Dict[str, str]]:
    """Map of model proxy slug to the organization's thumbnail image URL."""
    return self._thumbnails

  @thumbnails.setter
  def thumbnails(self, thumbnails: Optional[Dict[str, str]]):
    if thumbnails is None:
      del self.thumbnails
      return
    if not isinstance(thumbnails, dict):
      raise TypeError('thumbnails must be of type dict')
    if not all([isinstance(v, str) for k, v in thumbnails]):
      raise TypeError('thumbnails must contain only items of type str')
    self._thumbnails = thumbnails


class ListBenchmarkModelsFilter(KaggleObject):
  r"""
  Attributes:
    model_ids (int)
    model_version_ids (int)
    proxy_supported (bool)
  """

  def __init__(self):
    self._model_ids = []
    self._model_version_ids = []
    self._proxy_supported = None
    self._freeze()

  @property
  def model_ids(self) -> Optional[List[int]]:
    return self._model_ids

  @model_ids.setter
  def model_ids(self, model_ids: Optional[List[int]]):
    if model_ids is None:
      del self.model_ids
      return
    if not isinstance(model_ids, list):
      raise TypeError('model_ids must be of type list')
    if not all([isinstance(t, int) for t in model_ids]):
      raise TypeError('model_ids must contain only items of type int')
    self._model_ids = model_ids

  @property
  def model_version_ids(self) -> Optional[List[int]]:
    return self._model_version_ids

  @model_version_ids.setter
  def model_version_ids(self, model_version_ids: Optional[List[int]]):
    if model_version_ids is None:
      del self.model_version_ids
      return
    if not isinstance(model_version_ids, list):
      raise TypeError('model_version_ids must be of type list')
    if not all([isinstance(t, int) for t in model_version_ids]):
      raise TypeError('model_version_ids must contain only items of type int')
    self._model_version_ids = model_version_ids

  @property
  def proxy_supported(self) -> bool:
    return self._proxy_supported or False

  @proxy_supported.setter
  def proxy_supported(self, proxy_supported: Optional[bool]):
    if proxy_supported is None:
      del self.proxy_supported
      return
    if not isinstance(proxy_supported, bool):
      raise TypeError('proxy_supported must be of type bool')
    self._proxy_supported = proxy_supported


class ListBenchmarkModelsRequest(KaggleObject):
  r"""
  TODO(bml): Update list handlers to AIP standards when no longer admin-only.

  Attributes:
    filter (ListBenchmarkModelsFilter)
    read_mask (FieldMask)
    page_size (int)
    page_token (str)
    skip (int)
  """

  def __init__(self):
    self._filter = None
    self._read_mask = None
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._freeze()

  @property
  def filter(self) -> Optional['ListBenchmarkModelsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListBenchmarkModelsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarkModelsFilter):
      raise TypeError('filter must be of type ListBenchmarkModelsFilter')
    self._filter = filter

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

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip


class ListBenchmarkModelsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_models (BenchmarkModel)
    next_page_token (str)
  """

  def __init__(self):
    self._benchmark_models = []
    self._next_page_token = None
    self._freeze()

  @property
  def benchmark_models(self) -> Optional[List[Optional['BenchmarkModel']]]:
    return self._benchmark_models

  @benchmark_models.setter
  def benchmark_models(self, benchmark_models: Optional[List[Optional['BenchmarkModel']]]):
    if benchmark_models is None:
      del self.benchmark_models
      return
    if not isinstance(benchmark_models, list):
      raise TypeError('benchmark_models must be of type list')
    if not all([isinstance(t, BenchmarkModel) for t in benchmark_models]):
      raise TypeError('benchmark_models must contain only items of type BenchmarkModel')
    self._benchmark_models = benchmark_models

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class UpdateBenchmarkModelRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model (BenchmarkModel)
      The benchmark model to update.
    update_mask (FieldMask)
      The list of fields to update.
  """

  def __init__(self):
    self._benchmark_model = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark_model(self) -> Optional['BenchmarkModel']:
    """The benchmark model to update."""
    return self._benchmark_model

  @benchmark_model.setter
  def benchmark_model(self, benchmark_model: Optional['BenchmarkModel']):
    if benchmark_model is None:
      del self.benchmark_model
      return
    if not isinstance(benchmark_model, BenchmarkModel):
      raise TypeError('benchmark_model must be of type BenchmarkModel')
    self._benchmark_model = benchmark_model

  @property
  def update_mask(self) -> FieldMask:
    """The list of fields to update."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateBenchmarkModelVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version (BenchmarkModelVersion)
      The benchmark model to update.
    update_mask (FieldMask)
      The list of fields to update.
  """

  def __init__(self):
    self._benchmark_model_version = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark_model_version(self) -> Optional['BenchmarkModelVersion']:
    """The benchmark model to update."""
    return self._benchmark_model_version

  @benchmark_model_version.setter
  def benchmark_model_version(self, benchmark_model_version: Optional['BenchmarkModelVersion']):
    if benchmark_model_version is None:
      del self.benchmark_model_version
      return
    if not isinstance(benchmark_model_version, BenchmarkModelVersion):
      raise TypeError('benchmark_model_version must be of type BenchmarkModelVersion')
    self._benchmark_model_version = benchmark_model_version

  @property
  def update_mask(self) -> FieldMask:
    """The list of fields to update."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


CreateBenchmarkModelRequest._fields = [
  FieldMetadata("benchmarkModel", "benchmark_model", "_benchmark_model", BenchmarkModel, None, KaggleObjectSerializer()),
]

CreateBenchmarkModelVersionRequest._fields = [
  FieldMetadata("benchmarkModelVersion", "benchmark_model_version", "_benchmark_model_version", BenchmarkModelVersion, None, KaggleObjectSerializer()),
]

DeleteBenchmarkModelRequest._fields = [
  FieldMetadata("benchmarkModelId", "benchmark_model_id", "_benchmark_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
]

DeleteBenchmarkModelVersionRequest._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
]

GetBenchmarkModelThumbnailsRequest._fields = [
  FieldMetadata("modelProxySlugs", "model_proxy_slugs", "_model_proxy_slugs", str, [], ListSerializer(PredefinedSerializer())),
]

GetBenchmarkModelThumbnailsResponse._fields = [
  FieldMetadata("thumbnails", "thumbnails", "_thumbnails", str, {}, MapSerializer(PredefinedSerializer())),
]

ListBenchmarkModelsFilter._fields = [
  FieldMetadata("modelIds", "model_ids", "_model_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("modelVersionIds", "model_version_ids", "_model_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("proxySupported", "proxy_supported", "_proxy_supported", bool, None, PredefinedSerializer(), optional=True),
]

ListBenchmarkModelsRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListBenchmarkModelsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
]

ListBenchmarkModelsResponse._fields = [
  FieldMetadata("benchmarkModels", "benchmark_models", "_benchmark_models", BenchmarkModel, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

UpdateBenchmarkModelRequest._fields = [
  FieldMetadata("benchmarkModel", "benchmark_model", "_benchmark_model", BenchmarkModel, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateBenchmarkModelVersionRequest._fields = [
  FieldMetadata("benchmarkModelVersion", "benchmark_model_version", "_benchmark_model_version", BenchmarkModelVersion, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

