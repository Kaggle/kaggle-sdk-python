from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ModelProxyQuotaRefillPeriod
from typing import Optional, List

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


class ApiGetModelProxyQuotasRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/models/proxy/quota'
    return path.format_map(self.to_field_map(self))


class ApiGetModelProxyQuotasResponse(KaggleObject):
  r"""
  Attributes:
    quota_balances (ApiModelProxyQuotaBalance)
  """

  def __init__(self):
    self._quota_balances = []
    self._freeze()

  @property
  def quota_balances(self) -> Optional[List[Optional['ApiModelProxyQuotaBalance']]]:
    return self._quota_balances

  @quota_balances.setter
  def quota_balances(self, quota_balances: Optional[List[Optional['ApiModelProxyQuotaBalance']]]):
    if quota_balances is None:
      del self.quota_balances
      return
    if not isinstance(quota_balances, list):
      raise TypeError('quota_balances must be of type list')
    if not all([isinstance(t, ApiModelProxyQuotaBalance) for t in quota_balances]):
      raise TypeError('quota_balances must contain only items of type ApiModelProxyQuotaBalance')
    self._quota_balances = quota_balances

  @property
  def quotaBalances(self):
    return self.quota_balances


class ApiModelProxyQuotaBalance(KaggleObject):
  r"""
  Attributes:
    quota_used (float)
      How much quota was used in the time period (e.g. daily), in USD.
    total_quota_allowed (float)
      Upper limit of allowed quota in the time period (e.g. daily), in USD.
    refill_period (ModelProxyQuotaRefillPeriod)
      The time period this quota is refilled over (daily or monthly).
    refill_time (datetime)
      The time when the quota will next be refilled.
  """

  def __init__(self):
    self._quota_used = 0.0
    self._total_quota_allowed = 0.0
    self._refill_period = ModelProxyQuotaRefillPeriod.REFILL_PERIOD_UNSPECIFIED
    self._refill_time = None
    self._freeze()

  @property
  def quota_used(self) -> float:
    """How much quota was used in the time period (e.g. daily), in USD."""
    return self._quota_used

  @quota_used.setter
  def quota_used(self, quota_used: float):
    if quota_used is None:
      del self.quota_used
      return
    if not isinstance(quota_used, float):
      raise TypeError('quota_used must be of type float')
    self._quota_used = quota_used

  @property
  def total_quota_allowed(self) -> float:
    """Upper limit of allowed quota in the time period (e.g. daily), in USD."""
    return self._total_quota_allowed

  @total_quota_allowed.setter
  def total_quota_allowed(self, total_quota_allowed: float):
    if total_quota_allowed is None:
      del self.total_quota_allowed
      return
    if not isinstance(total_quota_allowed, float):
      raise TypeError('total_quota_allowed must be of type float')
    self._total_quota_allowed = total_quota_allowed

  @property
  def refill_period(self) -> 'ModelProxyQuotaRefillPeriod':
    """The time period this quota is refilled over (daily or monthly)."""
    return self._refill_period

  @refill_period.setter
  def refill_period(self, refill_period: 'ModelProxyQuotaRefillPeriod'):
    if refill_period is None:
      del self.refill_period
      return
    if not isinstance(refill_period, ModelProxyQuotaRefillPeriod):
      raise TypeError('refill_period must be of type ModelProxyQuotaRefillPeriod')
    self._refill_period = refill_period

  @property
  def refill_time(self) -> datetime:
    """The time when the quota will next be refilled."""
    return self._refill_time or None

  @refill_time.setter
  def refill_time(self, refill_time: Optional[datetime]):
    if refill_time is None:
      del self.refill_time
      return
    if not isinstance(refill_time, datetime):
      raise TypeError('refill_time must be of type datetime')
    self._refill_time = refill_time


ApiCreateDefaultModelProxyTokenRequest._fields = []

ApiCreateDefaultModelProxyTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("baseUri", "base_uri", "_base_uri", str, "", PredefinedSerializer()),
  FieldMetadata("expiryTime", "expiry_time", "_expiry_time", datetime, None, DateTimeSerializer()),
]

ApiGetModelProxyQuotasRequest._fields = []

ApiGetModelProxyQuotasResponse._fields = [
  FieldMetadata("quotaBalances", "quota_balances", "_quota_balances", ApiModelProxyQuotaBalance, [], ListSerializer(KaggleObjectSerializer())),
]

ApiModelProxyQuotaBalance._fields = [
  FieldMetadata("quotaUsed", "quota_used", "_quota_used", float, 0.0, PredefinedSerializer()),
  FieldMetadata("totalQuotaAllowed", "total_quota_allowed", "_total_quota_allowed", float, 0.0, PredefinedSerializer()),
  FieldMetadata("refillPeriod", "refill_period", "_refill_period", ModelProxyQuotaRefillPeriod, ModelProxyQuotaRefillPeriod.REFILL_PERIOD_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("refillTime", "refill_time", "_refill_time", datetime, None, DateTimeSerializer(), optional=True),
]

