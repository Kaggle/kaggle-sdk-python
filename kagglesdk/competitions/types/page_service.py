from kagglesdk.competitions.types.page import Page
from kagglesdk.kaggle_object import *
from typing import List, Optional

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


ListPagesResponse._fields = [
  FieldMetadata("pages", "pages", "_pages", Page, [], ListSerializer(KaggleObjectSerializer())),
]

