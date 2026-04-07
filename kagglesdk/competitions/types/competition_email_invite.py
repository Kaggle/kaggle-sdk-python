from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional

class CompetitionEmailInvite(KaggleObject):
  r"""
  Attributes:
    id (int)
    creation_time (datetime)
    email_address (str)
  """

  def __init__(self):
    self._id = 0
    self._creation_time = None
    self._email_address = ""
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
  def creation_time(self) -> datetime:
    return self._creation_time

  @creation_time.setter
  def creation_time(self, creation_time: datetime):
    if creation_time is None:
      del self.creation_time
      return
    if not isinstance(creation_time, datetime):
      raise TypeError('creation_time must be of type datetime')
    self._creation_time = creation_time

  @property
  def email_address(self) -> str:
    return self._email_address

  @email_address.setter
  def email_address(self, email_address: str):
    if email_address is None:
      del self.email_address
      return
    if not isinstance(email_address, str):
      raise TypeError('email_address must be of type str')
    self._email_address = email_address


CompetitionEmailInvite._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("creationTime", "creation_time", "_creation_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("emailAddress", "email_address", "_email_address", str, "", PredefinedSerializer()),
]

