from kagglesdk.kaggle_object import *
from typing import Optional

class Page(KaggleObject):
  r"""
  Representation of a top-level Competition or Benchmark page.
  Note that this does not map directly to the Page database entity,
  as it also includes elements of the Post entity (contents, mime_type).

  Attributes:
    id (int)
      Unique identifier of the Page
    competition_id (int)
      If set, identifier of the containing Competition
    benchmark_version_id (int)
      If set, identifier of the containing Benchmark Version
    name (str)
      The Page name/title
    content (str)
      Contents of the page (to be rendered according to 'mime_type')
    mime_type (str)
      The MIME type of the 'content' field
    is_published (bool)
      Whether the page is publicly visible
    order (int)
      The order of the page within the competition
    post_title (str)
      The title of the post associated with the page
    post_id (int)
      The id of the post associated with the page - used to warn about concurrent
      edits
  """

  def __init__(self):
    self._id = 0
    self._competition_id = None
    self._benchmark_version_id = None
    self._name = ""
    self._content = ""
    self._mime_type = ""
    self._is_published = False
    self._order = None
    self._post_title = None
    self._post_id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """Unique identifier of the Page"""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def competition_id(self) -> int:
    """If set, identifier of the containing Competition"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def benchmark_version_id(self) -> int:
    """If set, identifier of the containing Benchmark Version"""
    return self._benchmark_version_id or 0

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: Optional[int]):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def name(self) -> str:
    """The Page name/title"""
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
  def content(self) -> str:
    """Contents of the page (to be rendered according to 'mime_type')"""
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

  @property
  def mime_type(self) -> str:
    """The MIME type of the 'content' field"""
    return self._mime_type

  @mime_type.setter
  def mime_type(self, mime_type: str):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type

  @property
  def is_published(self) -> bool:
    """Whether the page is publicly visible"""
    return self._is_published

  @is_published.setter
  def is_published(self, is_published: bool):
    if is_published is None:
      del self.is_published
      return
    if not isinstance(is_published, bool):
      raise TypeError('is_published must be of type bool')
    self._is_published = is_published

  @property
  def order(self) -> int:
    """The order of the page within the competition"""
    return self._order or 0

  @order.setter
  def order(self, order: Optional[int]):
    if order is None:
      del self.order
      return
    if not isinstance(order, int):
      raise TypeError('order must be of type int')
    self._order = order

  @property
  def post_title(self) -> str:
    """The title of the post associated with the page"""
    return self._post_title or ""

  @post_title.setter
  def post_title(self, post_title: Optional[str]):
    if post_title is None:
      del self.post_title
      return
    if not isinstance(post_title, str):
      raise TypeError('post_title must be of type str')
    self._post_title = post_title

  @property
  def post_id(self) -> int:
    r"""
    The id of the post associated with the page - used to warn about concurrent
    edits
    """
    return self._post_id

  @post_id.setter
  def post_id(self, post_id: int):
    if post_id is None:
      del self.post_id
      return
    if not isinstance(post_id, int):
      raise TypeError('post_id must be of type int')
    self._post_id = post_id


Page._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, "", PredefinedSerializer()),
  FieldMetadata("isPublished", "is_published", "_is_published", bool, False, PredefinedSerializer()),
  FieldMetadata("order", "order", "_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("postTitle", "post_title", "_post_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("postId", "post_id", "_post_id", int, 0, PredefinedSerializer()),
]

