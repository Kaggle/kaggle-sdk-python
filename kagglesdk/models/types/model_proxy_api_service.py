from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional

class ApiCreateDefaultModelProxyTokenRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/models/proxy/token'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateDefaultModelProxyTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Model Proxy token/API key to use for inference requests.
    base_uri (str)
      Base URL for the proxy (usually 'https://mp-staging.kaggle.net/models').
    expiry_time (datetime)
      When the token expires.
  """

  def __init__(self):
    self._token = ""
    self._base_uri = ""
    self._expiry_time = None
    self._freeze()

  @property
  def token(self) -> str:
    """Model Proxy token/API key to use for inference requests."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def base_uri(self) -> str:
    """Base URL for the proxy (usually 'https://mp-staging.kaggle.net/models')."""
    return self._base_uri

  @base_uri.setter
  def base_uri(self, base_uri: str):
    if base_uri is None:
      del self.base_uri
      return
    if not isinstance(base_uri, str):
      raise TypeError('base_uri must be of type str')
    self._base_uri = base_uri

  @property
  def expiry_time(self) -> datetime:
    """When the token expires."""
    return self._expiry_time

  @expiry_time.setter
  def expiry_time(self, expiry_time: datetime):
    if expiry_time is None:
      del self.expiry_time
      return
    if not isinstance(expiry_time, datetime):
      raise TypeError('expiry_time must be of type datetime')
    self._expiry_time = expiry_time

  @property
  def baseUri(self):
    return self.base_uri

  @property
  def expiryTime(self):
    return self.expiry_time


ApiCreateDefaultModelProxyTokenRequest._fields = []

ApiCreateDefaultModelProxyTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("baseUri", "base_uri", "_base_uri", str, "", PredefinedSerializer()),
  FieldMetadata("expiryTime", "expiry_time", "_expiry_time", datetime, None, DateTimeSerializer()),
]

