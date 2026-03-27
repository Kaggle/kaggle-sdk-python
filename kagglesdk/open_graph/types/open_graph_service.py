from kagglesdk.kaggle_object import *
from kagglesdk.open_graph.types.open_graph_types import OpenGraphImageMetadata, OpenGraphResource, OpenGraphResourceType
from typing import List, Optional

class BatchGetOpenGraphImageMetadataRequest(KaggleObject):
  r"""
  Attributes:
    open_graph_resources (OpenGraphResource)
  """

  def __init__(self):
    self._open_graph_resources = []
    self._freeze()

  @property
  def open_graph_resources(self) -> Optional[List[Optional['OpenGraphResource']]]:
    return self._open_graph_resources

  @open_graph_resources.setter
  def open_graph_resources(self, open_graph_resources: Optional[List[Optional['OpenGraphResource']]]):
    if open_graph_resources is None:
      del self.open_graph_resources
      return
    if not isinstance(open_graph_resources, list):
      raise TypeError('open_graph_resources must be of type list')
    if not all([isinstance(t, OpenGraphResource) for t in open_graph_resources]):
      raise TypeError('open_graph_resources must contain only items of type OpenGraphResource')
    self._open_graph_resources = open_graph_resources


class BatchGetOpenGraphImageMetadataResponse(KaggleObject):
  r"""
  Attributes:
    metadata (OpenGraphImageMetadata)
  """

  def __init__(self):
    self._metadata = []
    self._freeze()

  @property
  def metadata(self) -> Optional[List[Optional['OpenGraphImageMetadata']]]:
    return self._metadata

  @metadata.setter
  def metadata(self, metadata: Optional[List[Optional['OpenGraphImageMetadata']]]):
    if metadata is None:
      del self.metadata
      return
    if not isinstance(metadata, list):
      raise TypeError('metadata must be of type list')
    if not all([isinstance(t, OpenGraphImageMetadata) for t in metadata]):
      raise TypeError('metadata must contain only items of type OpenGraphImageMetadata')
    self._metadata = metadata


class GetLatestOpenGraphImageMetadataRequest(KaggleObject):
  r"""
  Attributes:
    open_graph_resource_type (OpenGraphResourceType)
    entity_id (int)
    entity_version_id (int)
  """

  def __init__(self):
    self._open_graph_resource_type = OpenGraphResourceType.UNSPECIFIED
    self._entity_id = 0
    self._entity_version_id = None
    self._freeze()

  @property
  def open_graph_resource_type(self) -> 'OpenGraphResourceType':
    return self._open_graph_resource_type

  @open_graph_resource_type.setter
  def open_graph_resource_type(self, open_graph_resource_type: 'OpenGraphResourceType'):
    if open_graph_resource_type is None:
      del self.open_graph_resource_type
      return
    if not isinstance(open_graph_resource_type, OpenGraphResourceType):
      raise TypeError('open_graph_resource_type must be of type OpenGraphResourceType')
    self._open_graph_resource_type = open_graph_resource_type

  @property
  def entity_id(self) -> int:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: int):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, int):
      raise TypeError('entity_id must be of type int')
    self._entity_id = entity_id

  @property
  def entity_version_id(self) -> int:
    return self._entity_version_id or 0

  @entity_version_id.setter
  def entity_version_id(self, entity_version_id: Optional[int]):
    if entity_version_id is None:
      del self.entity_version_id
      return
    if not isinstance(entity_version_id, int):
      raise TypeError('entity_version_id must be of type int')
    self._entity_version_id = entity_version_id


class GetLatestOpenGraphImageMetadataResponse(KaggleObject):
  r"""
  Attributes:
    url (str)
  """

  def __init__(self):
    self._url = None
    self._freeze()

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


class OpenGraph(KaggleObject):
  r"""
  """

  pass

BatchGetOpenGraphImageMetadataRequest._fields = [
  FieldMetadata("openGraphResources", "open_graph_resources", "_open_graph_resources", OpenGraphResource, [], ListSerializer(KaggleObjectSerializer())),
]

BatchGetOpenGraphImageMetadataResponse._fields = [
  FieldMetadata("metadata", "metadata", "_metadata", OpenGraphImageMetadata, [], ListSerializer(KaggleObjectSerializer())),
]

GetLatestOpenGraphImageMetadataRequest._fields = [
  FieldMetadata("openGraphResourceType", "open_graph_resource_type", "_open_graph_resource_type", OpenGraphResourceType, OpenGraphResourceType.UNSPECIFIED, EnumSerializer()),
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityVersionId", "entity_version_id", "_entity_version_id", int, None, PredefinedSerializer(), optional=True),
]

GetLatestOpenGraphImageMetadataResponse._fields = [
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

OpenGraph._fields = []

