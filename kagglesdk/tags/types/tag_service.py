from kagglesdk.kaggle_object import *
from typing import Optional

class Tag(KaggleObject):
  r"""
  Attributes:
    id (int)
      The unique identifier for a tag
    name (str)
      The name of a tag
    full_path (str)
      The complete path for a tag, showing its ancestors, separated by >
    listing_url (str)
      The URL to link to an appropriate listing for the tag, e.g. datasets
      listing filtered by tag
    description (str)
      The description for a given tag
    dataset_count (int)
      The count of datasets tagged with a given tag
    competition_count (int)
      The count of competitions tagged with a given tag
    notebook_count (int)
      The count of notebooks tagged with a given tag
    tag_url (str)
      The URL to link directly to a given tag
    display_name (str)
      The display name for a given tag
    google_material_icon (str)
      Google Material Icon (previously FontAwesomeIcon)
    model_count (int)
      The count of models tagged with a given tag
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._full_path = ""
    self._listing_url = ""
    self._description = None
    self._dataset_count = 0
    self._competition_count = 0
    self._notebook_count = 0
    self._tag_url = ""
    self._display_name = ""
    self._google_material_icon = ""
    self._model_count = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The unique identifier for a tag"""
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
    """The name of a tag"""
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
    """The complete path for a tag, showing its ancestors, separated by >"""
    return self._full_path

  @full_path.setter
  def full_path(self, full_path: str):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def listing_url(self) -> str:
    r"""
    The URL to link to an appropriate listing for the tag, e.g. datasets
    listing filtered by tag
    """
    return self._listing_url

  @listing_url.setter
  def listing_url(self, listing_url: str):
    if listing_url is None:
      del self.listing_url
      return
    if not isinstance(listing_url, str):
      raise TypeError('listing_url must be of type str')
    self._listing_url = listing_url

  @property
  def description(self) -> str:
    """The description for a given tag"""
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
    """The count of datasets tagged with a given tag"""
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
    """The count of competitions tagged with a given tag"""
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
  def notebook_count(self) -> int:
    """The count of notebooks tagged with a given tag"""
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count

  @property
  def model_count(self) -> int:
    """The count of models tagged with a given tag"""
    return self._model_count

  @model_count.setter
  def model_count(self, model_count: int):
    if model_count is None:
      del self.model_count
      return
    if not isinstance(model_count, int):
      raise TypeError('model_count must be of type int')
    self._model_count = model_count

  @property
  def tag_url(self) -> str:
    """The URL to link directly to a given tag"""
    return self._tag_url

  @tag_url.setter
  def tag_url(self, tag_url: str):
    if tag_url is None:
      del self.tag_url
      return
    if not isinstance(tag_url, str):
      raise TypeError('tag_url must be of type str')
    self._tag_url = tag_url

  @property
  def display_name(self) -> str:
    """The display name for a given tag"""
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def google_material_icon(self) -> str:
    """Google Material Icon (previously FontAwesomeIcon)"""
    return self._google_material_icon

  @google_material_icon.setter
  def google_material_icon(self, google_material_icon: str):
    if google_material_icon is None:
      del self.google_material_icon
      return
    if not isinstance(google_material_icon, str):
      raise TypeError('google_material_icon must be of type str')
    self._google_material_icon = google_material_icon


Tag._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("fullPath", "full_path", "_full_path", str, "", PredefinedSerializer()),
  FieldMetadata("listingUrl", "listing_url", "_listing_url", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
  FieldMetadata("tagUrl", "tag_url", "_tag_url", str, "", PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("googleMaterialIcon", "google_material_icon", "_google_material_icon", str, "", PredefinedSerializer()),
  FieldMetadata("modelCount", "model_count", "_model_count", int, 0, PredefinedSerializer()),
]

