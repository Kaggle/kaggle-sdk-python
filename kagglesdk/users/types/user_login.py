from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional

class UserLogin(KaggleObject):
  r"""
  Attributes:
    name (str)
    email (str)
    is_disabled (bool)
    linked_date (datetime)
  """

  def __init__(self):
    self._name = None
    self._email = None
    self._is_disabled = False
    self._linked_date = None
    self._freeze()

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def email(self) -> str:
    return self._email or ""

  @email.setter
  def email(self, email: Optional[str]):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email

  @property
  def is_disabled(self) -> bool:
    return self._is_disabled

  @is_disabled.setter
  def is_disabled(self, is_disabled: bool):
    if is_disabled is None:
      del self.is_disabled
      return
    if not isinstance(is_disabled, bool):
      raise TypeError('is_disabled must be of type bool')
    self._is_disabled = is_disabled

  @property
  def linked_date(self) -> datetime:
    return self._linked_date

  @linked_date.setter
  def linked_date(self, linked_date: datetime):
    if linked_date is None:
      del self.linked_date
      return
    if not isinstance(linked_date, datetime):
      raise TypeError('linked_date must be of type datetime')
    self._linked_date = linked_date


UserLogin._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isDisabled", "is_disabled", "_is_disabled", bool, False, PredefinedSerializer()),
  FieldMetadata("linkedDate", "linked_date", "_linked_date", datetime, None, DateTimeSerializer()),
]

