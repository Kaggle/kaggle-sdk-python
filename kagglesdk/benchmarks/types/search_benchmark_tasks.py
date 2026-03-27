from kagglesdk.kaggle_object import *

class SearchBenchmarkTasksDocument(KaggleObject):
  r"""
  Attributes:
    description (str)
    current_version_id (int)
    current_version_number (int)
  """

  def __init__(self):
    self._description = ""
    self._current_version_id = 0
    self._current_version_number = 0
    self._freeze()

  @property
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def current_version_id(self) -> int:
    return self._current_version_id

  @current_version_id.setter
  def current_version_id(self, current_version_id: int):
    if current_version_id is None:
      del self.current_version_id
      return
    if not isinstance(current_version_id, int):
      raise TypeError('current_version_id must be of type int')
    self._current_version_id = current_version_id

  @property
  def current_version_number(self) -> int:
    return self._current_version_number

  @current_version_number.setter
  def current_version_number(self, current_version_number: int):
    if current_version_number is None:
      del self.current_version_number
      return
    if not isinstance(current_version_number, int):
      raise TypeError('current_version_number must be of type int')
    self._current_version_number = current_version_number


SearchBenchmarkTasksDocument._fields = [
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("currentVersionId", "current_version_id", "_current_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentVersionNumber", "current_version_number", "_current_version_number", int, 0, PredefinedSerializer()),
]

