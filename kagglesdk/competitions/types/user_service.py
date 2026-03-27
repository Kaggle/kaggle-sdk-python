from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from typing import Optional

class AcceptRulesRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class CreateOrUpdateUserEmailShareRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    email_shared (bool)
  """

  def __init__(self):
    self._competition_id = 0
    self._email_shared = False
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def email_shared(self) -> bool:
    return self._email_shared

  @email_shared.setter
  def email_shared(self, email_shared: bool):
    if email_shared is None:
      del self.email_shared
      return
    if not isinstance(email_shared, bool):
      raise TypeError('email_shared must be of type bool')
    self._email_shared = email_shared


class GetUserEmailShareRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class GetUserEmailShareResponse(KaggleObject):
  r"""
  Attributes:
    email_shared (bool)
  """

  def __init__(self):
    self._email_shared = False
    self._freeze()

  @property
  def email_shared(self) -> bool:
    return self._email_shared

  @email_shared.setter
  def email_shared(self, email_shared: bool):
    if email_shared is None:
      del self.email_shared
      return
    if not isinstance(email_shared, bool):
      raise TypeError('email_shared must be of type bool')
    self._email_shared = email_shared


class GetUserRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_name (str)
    read_mask (FieldMask)
      If the read mask is unset, we will default to all fields (per
      https://protobuf.dev/reference/java/api-docs/com/google/protobuf/FieldMask).
      Some fields are always included. See the CompetitionUser message.
  """

  def __init__(self):
    self._competition_id = None
    self._competition_name = None
    self._read_mask = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.competition_name
    self._competition_id = competition_id

  @property
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    del self.competition_id
    self._competition_name = competition_name

  @property
  def read_mask(self) -> FieldMask:
    r"""
    If the read mask is unset, we will default to all fields (per
    https://protobuf.dev/reference/java/api-docs/com/google/protobuf/FieldMask).
    Some fields are always included. See the CompetitionUser message.
    """
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


AcceptRulesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

CreateOrUpdateUserEmailShareRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("emailShared", "email_shared", "_email_shared", bool, False, PredefinedSerializer()),
]

GetUserEmailShareRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetUserEmailShareResponse._fields = [
  FieldMetadata("emailShared", "email_shared", "_email_shared", bool, False, PredefinedSerializer()),
]

GetUserRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

