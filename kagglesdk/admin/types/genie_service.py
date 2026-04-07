from kagglesdk.kaggle_object import *
from kagglesdk.security.types.authentication import DataAccessReason
from typing import Optional

class CreateDelegatedUserAccessTokenRequest(KaggleObject):
  r"""
  Attributes:
    destination_user_id (int)
      The user id that the token should represent.
    data_access_reason (DataAccessReason)
      Reason for delegated access (e.g. support ticket).
      NOTE: This could be passed to Gin in the future.
  """

  def __init__(self):
    self._destination_user_id = 0
    self._data_access_reason = None
    self._freeze()

  @property
  def destination_user_id(self) -> int:
    """The user id that the token should represent."""
    return self._destination_user_id

  @destination_user_id.setter
  def destination_user_id(self, destination_user_id: int):
    if destination_user_id is None:
      del self.destination_user_id
      return
    if not isinstance(destination_user_id, int):
      raise TypeError('destination_user_id must be of type int')
    self._destination_user_id = destination_user_id

  @property
  def data_access_reason(self) -> Optional['DataAccessReason']:
    r"""
    Reason for delegated access (e.g. support ticket).
    NOTE: This could be passed to Gin in the future.
    """
    return self._data_access_reason

  @data_access_reason.setter
  def data_access_reason(self, data_access_reason: Optional['DataAccessReason']):
    if data_access_reason is None:
      del self.data_access_reason
      return
    if not isinstance(data_access_reason, DataAccessReason):
      raise TypeError('data_access_reason must be of type DataAccessReason')
    self._data_access_reason = data_access_reason


class CreateDelegatedUserAccessTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque token that can be used to impersonate another user.
  """

  def __init__(self):
    self._token = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque token that can be used to impersonate another user."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


CreateDelegatedUserAccessTokenRequest._fields = [
  FieldMetadata("destinationUserId", "destination_user_id", "_destination_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dataAccessReason", "data_access_reason", "_data_access_reason", DataAccessReason, None, KaggleObjectSerializer()),
]

CreateDelegatedUserAccessTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

