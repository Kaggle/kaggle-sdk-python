from kagglesdk.kaggle_object import *
from typing import Optional

class BackgroundOperation(KaggleObject):
  r"""
  Similar to
  https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto
  Has historically only been used by Competitions but could eventually be made
  into an official (non-Legacy) service.

  Attributes:
    id (str)
    name (str)
    done (bool)
    error (str)
    progress (str)
  """

  def __init__(self):
    self._id = ""
    self._name = ""
    self._done = False
    self._error = None
    self._progress = None
    self._freeze()

  @property
  def id(self) -> str:
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

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

  @property
  def done(self) -> bool:
    return self._done

  @done.setter
  def done(self, done: bool):
    if done is None:
      del self.done
      return
    if not isinstance(done, bool):
      raise TypeError('done must be of type bool')
    self._done = done

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    del self.progress
    self._error = error

  @property
  def progress(self) -> str:
    return self._progress or ""

  @progress.setter
  def progress(self, progress: str):
    if progress is None:
      del self.progress
      return
    if not isinstance(progress, str):
      raise TypeError('progress must be of type str')
    del self.error
    self._progress = progress


BackgroundOperation._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("done", "done", "_done", bool, False, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progress", "progress", "_progress", str, None, PredefinedSerializer(), optional=True),
]

