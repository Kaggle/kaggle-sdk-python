from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ModelProxyQuotaRefillPeriod
from typing import Optional, List

class GetModelProxyQuotaRequest(KaggleObject):
  r"""
  """

  pass

class GetModelProxyQuotaResponse(KaggleObject):
  r"""
  Attributes:
    daily_quota_used (float)
      How much quota that was used in the time period (daily), in USD.
    total_daily_quota_allowed (float)
      Upper limit of allowed quota in the time period (daily), in USD.
  """

  def __init__(self):
    self._daily_quota_used = 0.0
    self._total_daily_quota_allowed = 0.0
    self._freeze()

  @property
  def daily_quota_used(self) -> float:
    """How much quota that was used in the time period (daily), in USD."""
    return self._daily_quota_used

  @daily_quota_used.setter
  def daily_quota_used(self, daily_quota_used: float):
    if daily_quota_used is None:
      del self.daily_quota_used
      return
    if not isinstance(daily_quota_used, float):
      raise TypeError('daily_quota_used must be of type float')
    self._daily_quota_used = daily_quota_used

  @property
  def total_daily_quota_allowed(self) -> float:
    """Upper limit of allowed quota in the time period (daily), in USD."""
    return self._total_daily_quota_allowed

  @total_daily_quota_allowed.setter
  def total_daily_quota_allowed(self, total_daily_quota_allowed: float):
    if total_daily_quota_allowed is None:
      del self.total_daily_quota_allowed
      return
    if not isinstance(total_daily_quota_allowed, float):
      raise TypeError('total_daily_quota_allowed must be of type float')
    self._total_daily_quota_allowed = total_daily_quota_allowed


class GetModelProxyQuotasRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      Defaults to current user if not given.
  """

  def __init__(self):
    self._user_id = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """Defaults to current user if not given."""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetModelProxyQuotasResponse(KaggleObject):
  r"""
  Attributes:
    quota_balances (QuotaBalance)
  """

  def __init__(self):
    self._quota_balances = []
    self._freeze()

  @property
  def quota_balances(self) -> Optional[List[Optional['QuotaBalance']]]:
    return self._quota_balances

  @quota_balances.setter
  def quota_balances(self, quota_balances: Optional[List[Optional['QuotaBalance']]]):
    if quota_balances is None:
      del self.quota_balances
      return
    if not isinstance(quota_balances, list):
      raise TypeError('quota_balances must be of type list')
    if not all([isinstance(t, QuotaBalance) for t in quota_balances]):
      raise TypeError('quota_balances must contain only items of type QuotaBalance')
    self._quota_balances = quota_balances


class QuotaBalance(KaggleObject):
  r"""
  Attributes:
    quota_used (float)
      How much quota that was used in the time period (e.g. daily), in USD.
    total_quota_allowed (float)
      Upper limit of allowed quota in the time period (e.g. daily), in USD.
    refill_period (ModelProxyQuotaRefillPeriod)
      How often the quota is refilled. Used to identify which time period the
      quota belongs to (daily, monthly, etc.)
    refill_time (datetime)
      The time when the quota will be refilled.
  """

  def __init__(self):
    self._quota_used = 0.0
    self._total_quota_allowed = 0.0
    self._refill_period = ModelProxyQuotaRefillPeriod.REFILL_PERIOD_UNSPECIFIED
    self._refill_time = None
    self._freeze()

  @property
  def quota_used(self) -> float:
    """How much quota that was used in the time period (e.g. daily), in USD."""
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
    r"""
    How often the quota is refilled. Used to identify which time period the
    quota belongs to (daily, monthly, etc.)
    """
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
    """The time when the quota will be refilled."""
    return self._refill_time or None

  @refill_time.setter
  def refill_time(self, refill_time: Optional[datetime]):
    if refill_time is None:
      del self.refill_time
      return
    if not isinstance(refill_time, datetime):
      raise TypeError('refill_time must be of type datetime')
    self._refill_time = refill_time


GetModelProxyQuotaRequest._fields = []

GetModelProxyQuotaResponse._fields = [
  FieldMetadata("dailyQuotaUsed", "daily_quota_used", "_daily_quota_used", float, 0.0, PredefinedSerializer()),
  FieldMetadata("totalDailyQuotaAllowed", "total_daily_quota_allowed", "_total_daily_quota_allowed", float, 0.0, PredefinedSerializer()),
]

GetModelProxyQuotasRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

GetModelProxyQuotasResponse._fields = [
  FieldMetadata("quotaBalances", "quota_balances", "_quota_balances", QuotaBalance, [], ListSerializer(KaggleObjectSerializer())),
]

QuotaBalance._fields = [
  FieldMetadata("quotaUsed", "quota_used", "_quota_used", float, 0.0, PredefinedSerializer()),
  FieldMetadata("totalQuotaAllowed", "total_quota_allowed", "_total_quota_allowed", float, 0.0, PredefinedSerializer()),
  FieldMetadata("refillPeriod", "refill_period", "_refill_period", ModelProxyQuotaRefillPeriod, ModelProxyQuotaRefillPeriod.REFILL_PERIOD_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("refillTime", "refill_time", "_refill_time", datetime, None, DateTimeSerializer(), optional=True),
]

