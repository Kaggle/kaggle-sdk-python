from kagglesdk.kaggle_object import *

class GetBackgroundOperationRequest(KaggleObject):
  r"""
  Attributes:
    id (str)
  """

  def __init__(self):
    self._id = ""
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


class WaitBackgroundOperationRequest(KaggleObject):
  r"""
  Attributes:
    id (str)
  """

  def __init__(self):
    self._id = ""
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


GetBackgroundOperationRequest._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
]

WaitBackgroundOperationRequest._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
]

