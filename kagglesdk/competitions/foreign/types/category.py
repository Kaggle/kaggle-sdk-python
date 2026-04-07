from kagglesdk.kaggle_object import *
from typing import Optional

class Category(KaggleObject):
  r"""
  Subset of the full Category object with seemingly everything needed for now.
  Also known as Tag.

  Attributes:
    id (int)
    name (str)
      The name of the category.
    full_path (str)
      The category's full path.
    description (str)
      A description of the category.
    dataset_count (int)
      The number of datasets tagged with this category.
    competition_count (int)
      The number of competitions tagged with this category.
    script_count (int)
      The number of kernels tagged with this category.
    slug (str)
      The name of the category, as it appears in the URL.
    display_name (str)
      The display name of the category.
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._full_path = None
    self._description = None
    self._dataset_count = 0
    self._competition_count = 0
    self._script_count = 0
    self._slug = ""
    self._display_name = None
    self._freeze()

  @property
  def id(self) -> int:
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
  def name(self) -> str:
    """The name of the category."""
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
  def full_path(self) -> str:
    """The category's full path."""
    return self._full_path or ""

  @full_path.setter
  def full_path(self, full_path: Optional[str]):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def description(self) -> str:
    """A description of the category."""
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def dataset_count(self) -> int:
    """The number of datasets tagged with this category."""
    return self._dataset_count

  @dataset_count.setter
  def dataset_count(self, dataset_count: int):
    if dataset_count is None:
      del self.dataset_count
      return
    if not isinstance(dataset_count, int):
      raise TypeError('dataset_count must be of type int')
    self._dataset_count = dataset_count

  @property
  def competition_count(self) -> int:
    """The number of competitions tagged with this category."""
    return self._competition_count

  @competition_count.setter
  def competition_count(self, competition_count: int):
    if competition_count is None:
      del self.competition_count
      return
    if not isinstance(competition_count, int):
      raise TypeError('competition_count must be of type int')
    self._competition_count = competition_count

  @property
  def script_count(self) -> int:
    """The number of kernels tagged with this category."""
    return self._script_count

  @script_count.setter
  def script_count(self, script_count: int):
    if script_count is None:
      del self.script_count
      return
    if not isinstance(script_count, int):
      raise TypeError('script_count must be of type int')
    self._script_count = script_count

  @property
  def slug(self) -> str:
    """The name of the category, as it appears in the URL."""
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def display_name(self) -> str:
    """The display name of the category."""
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name


Category._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("fullPath", "full_path", "_full_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptCount", "script_count", "_script_count", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
]

