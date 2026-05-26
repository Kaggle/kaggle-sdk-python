from kagglesdk.discussions.types.writeup_types import ResolvedWriteUpLink
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ApiGetResolvedWriteUpLinksRequest(KaggleObject):
  r"""
  Attributes:
    write_up_id (int)
  """

  def __init__(self):
    self._write_up_id = 0
    self._freeze()

  @property
  def write_up_id(self) -> int:
    return self._write_up_id

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    self._write_up_id = write_up_id

  def endpoint(self):
    path = '/api/v1/writeups/{write_up_id}/resolved-links'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/writeups/{write_up_id}/resolved-links'


class ApiGetResolvedWriteUpLinksResponse(KaggleObject):
  r"""
  Attributes:
    resolved_links (ResolvedWriteUpLink)
  """

  def __init__(self):
    self._resolved_links = []
    self._freeze()

  @property
  def resolved_links(self) -> Optional[List[Optional['ResolvedWriteUpLink']]]:
    return self._resolved_links

  @resolved_links.setter
  def resolved_links(self, resolved_links: Optional[List[Optional['ResolvedWriteUpLink']]]):
    if resolved_links is None:
      del self.resolved_links
      return
    if not isinstance(resolved_links, list):
      raise TypeError('resolved_links must be of type list')
    if not all([isinstance(t, ResolvedWriteUpLink) for t in resolved_links]):
      raise TypeError('resolved_links must contain only items of type ResolvedWriteUpLink')
    self._resolved_links = resolved_links

  @property
  def resolvedLinks(self):
    return self.resolved_links


ApiGetResolvedWriteUpLinksRequest._fields = [
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, 0, PredefinedSerializer()),
]

ApiGetResolvedWriteUpLinksResponse._fields = [
  FieldMetadata("resolvedLinks", "resolved_links", "_resolved_links", ResolvedWriteUpLink, [], ListSerializer(KaggleObjectSerializer())),
]

