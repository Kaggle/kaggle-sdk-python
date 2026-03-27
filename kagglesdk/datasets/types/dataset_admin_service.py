from kagglesdk.kaggle_object import *
from typing import Optional

class RecreateCroissantRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
    databundle_version_firestore_path (str)
  """

  def __init__(self):
    self._databundle_version_id = None
    self._databundle_version_firestore_path = None
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id or 0

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    del self.databundle_version_firestore_path
    self._databundle_version_id = databundle_version_id

  @property
  def databundle_version_firestore_path(self) -> str:
    return self._databundle_version_firestore_path or ""

  @databundle_version_firestore_path.setter
  def databundle_version_firestore_path(self, databundle_version_firestore_path: str):
    if databundle_version_firestore_path is None:
      del self.databundle_version_firestore_path
      return
    if not isinstance(databundle_version_firestore_path, str):
      raise TypeError('databundle_version_firestore_path must be of type str')
    del self.databundle_version_id
    self._databundle_version_firestore_path = databundle_version_firestore_path


class RecreateCroissantResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
      Status of the request
  """

  def __init__(self):
    self._message = ""
    self._freeze()

  @property
  def message(self) -> str:
    """Status of the request"""
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


class SetDatabundleVersionNotesRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
    version_notes (str)
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._version_notes = None
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

  @property
  def version_notes(self) -> str:
    return self._version_notes or ""

  @version_notes.setter
  def version_notes(self, version_notes: Optional[str]):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes


RecreateCroissantRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("databundleVersionFirestorePath", "databundle_version_firestore_path", "_databundle_version_firestore_path", str, None, PredefinedSerializer(), optional=True),
]

RecreateCroissantResponse._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

SetDatabundleVersionNotesRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, None, PredefinedSerializer(), optional=True),
]

