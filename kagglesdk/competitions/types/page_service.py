from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkVersionIdentifier
from kagglesdk.competitions.types.page import Page
from kagglesdk.kaggle_object import *
from typing import Optional, List

class CreatePageRequest(KaggleObject):
  r"""
  Attributes:
    page (Page)
  """

  def __init__(self):
    self._page = None
    self._freeze()

  @property
  def page(self) -> Optional['Page']:
    return self._page

  @page.setter
  def page(self, page: Optional['Page']):
    if page is None:
      del self.page
      return
    if not isinstance(page, Page):
      raise TypeError('page must be of type Page')
    self._page = page


class DeletePageRequest(KaggleObject):
  r"""
  Attributes:
    page_id (int)
  """

  def __init__(self):
    self._page_id = 0
    self._freeze()

  @property
  def page_id(self) -> int:
    return self._page_id

  @page_id.setter
  def page_id(self, page_id: int):
    if page_id is None:
      del self.page_id
      return
    if not isinstance(page_id, int):
      raise TypeError('page_id must be of type int')
    self._page_id = page_id


class GetPageRequest(KaggleObject):
  r"""
  Attributes:
    page (PageByName)
  """

  def __init__(self):
    self._page = None
    self._freeze()

  @property
  def page(self) -> Optional['PageByName']:
    return self._page

  @page.setter
  def page(self, page: Optional['PageByName']):
    if page is None:
      del self.page
      return
    if not isinstance(page, PageByName):
      raise TypeError('page must be of type PageByName')
    self._page = page


class ListPagesRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    competition_id (int)
    benchmark_version_identifier (BenchmarkVersionIdentifier)
  """

  def __init__(self):
    self._competition_id = None
    self._benchmark_version_identifier = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.benchmark_version_identifier
    self._competition_id = competition_id

  @property
  def benchmark_version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    return self._benchmark_version_identifier or None

  @benchmark_version_identifier.setter
  def benchmark_version_identifier(self, benchmark_version_identifier: Optional['BenchmarkVersionIdentifier']):
    if benchmark_version_identifier is None:
      del self.benchmark_version_identifier
      return
    if not isinstance(benchmark_version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('benchmark_version_identifier must be of type BenchmarkVersionIdentifier')
    del self.competition_id
    self._benchmark_version_identifier = benchmark_version_identifier


class ListPagesResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    pages (Page)
  """

  def __init__(self):
    self._pages = []
    self._freeze()

  @property
  def pages(self) -> Optional[List[Optional['Page']]]:
    return self._pages

  @pages.setter
  def pages(self, pages: Optional[List[Optional['Page']]]):
    if pages is None:
      del self.pages
      return
    if not isinstance(pages, list):
      raise TypeError('pages must be of type list')
    if not all([isinstance(t, Page) for t in pages]):
      raise TypeError('pages must contain only items of type Page')
    self._pages = pages


class PageByName(KaggleObject):
  r"""
  Unique identifier of a page by name and competition_id or
  benchmark_version_id.

  Attributes:
    competition_id (int)
    benchmark_version_id (int)
    name (str)
  """

  def __init__(self):
    self._competition_id = None
    self._benchmark_version_id = None
    self._name = ""
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.benchmark_version_id
    self._competition_id = competition_id

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id or 0

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    del self.competition_id
    self._benchmark_version_id = benchmark_version_id

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


class SwapPageOrdersRequest(KaggleObject):
  r"""
  Attributes:
    page_a_id (int)
    page_b_id (int)
  """

  def __init__(self):
    self._page_a_id = 0
    self._page_b_id = 0
    self._freeze()

  @property
  def page_a_id(self) -> int:
    return self._page_a_id

  @page_a_id.setter
  def page_a_id(self, page_a_id: int):
    if page_a_id is None:
      del self.page_a_id
      return
    if not isinstance(page_a_id, int):
      raise TypeError('page_a_id must be of type int')
    self._page_a_id = page_a_id

  @property
  def page_b_id(self) -> int:
    return self._page_b_id

  @page_b_id.setter
  def page_b_id(self, page_b_id: int):
    if page_b_id is None:
      del self.page_b_id
      return
    if not isinstance(page_b_id, int):
      raise TypeError('page_b_id must be of type int')
    self._page_b_id = page_b_id


class UpdatePageRequest(KaggleObject):
  r"""
  Attributes:
    page (Page)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._page = None
    self._update_mask = None
    self._freeze()

  @property
  def page(self) -> Optional['Page']:
    return self._page

  @page.setter
  def page(self, page: Optional['Page']):
    if page is None:
      del self.page
      return
    if not isinstance(page, Page):
      raise TypeError('page must be of type Page')
    self._page = page

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


CreatePageRequest._fields = [
  FieldMetadata("page", "page", "_page", Page, None, KaggleObjectSerializer()),
]

DeletePageRequest._fields = [
  FieldMetadata("pageId", "page_id", "_page_id", int, 0, PredefinedSerializer()),
]

GetPageRequest._fields = [
  FieldMetadata("page", "page", "_page", PageByName, None, KaggleObjectSerializer()),
]

ListPagesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkVersionIdentifier", "benchmark_version_identifier", "_benchmark_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer(), optional=True),
]

ListPagesResponse._fields = [
  FieldMetadata("pages", "pages", "_pages", Page, [], ListSerializer(KaggleObjectSerializer())),
]

PageByName._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

SwapPageOrdersRequest._fields = [
  FieldMetadata("pageAId", "page_a_id", "_page_a_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageBId", "page_b_id", "_page_b_id", int, 0, PredefinedSerializer()),
]

UpdatePageRequest._fields = [
  FieldMetadata("page", "page", "_page", Page, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

