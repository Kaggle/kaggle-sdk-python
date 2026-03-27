from kagglesdk.admin.types.rate_limit import RateLimit, RateLimitStatus
from kagglesdk.kaggle_object import *
from typing import List, Optional

class BatchResetRateLimitStatusesRequest(KaggleObject):
  r"""
  Attributes:
    keys (str)
      The Redis keys of the rate limits to reset.
  """

  def __init__(self):
    self._keys = []
    self._freeze()

  @property
  def keys(self) -> Optional[List[str]]:
    """The Redis keys of the rate limits to reset."""
    return self._keys

  @keys.setter
  def keys(self, keys: Optional[List[str]]):
    if keys is None:
      del self.keys
      return
    if not isinstance(keys, list):
      raise TypeError('keys must be of type list')
    if not all([isinstance(t, str) for t in keys]):
      raise TypeError('keys must contain only items of type str')
    self._keys = keys


class BatchResetRateLimitStatusesResponse(KaggleObject):
  r"""
  Attributes:
    reset_count (int)
  """

  def __init__(self):
    self._reset_count = 0
    self._freeze()

  @property
  def reset_count(self) -> int:
    return self._reset_count

  @reset_count.setter
  def reset_count(self, reset_count: int):
    if reset_count is None:
      del self.reset_count
      return
    if not isinstance(reset_count, int):
      raise TypeError('reset_count must be of type int')
    self._reset_count = reset_count


class ListRateLimitsRequest(KaggleObject):
  r"""
  """

  pass

class ListRateLimitsResponse(KaggleObject):
  r"""
  Attributes:
    rate_limits (RateLimit)
  """

  def __init__(self):
    self._rate_limits = []
    self._freeze()

  @property
  def rate_limits(self) -> Optional[List[Optional['RateLimit']]]:
    return self._rate_limits

  @rate_limits.setter
  def rate_limits(self, rate_limits: Optional[List[Optional['RateLimit']]]):
    if rate_limits is None:
      del self.rate_limits
      return
    if not isinstance(rate_limits, list):
      raise TypeError('rate_limits must be of type list')
    if not all([isinstance(t, RateLimit) for t in rate_limits]):
      raise TypeError('rate_limits must contain only items of type RateLimit')
    self._rate_limits = rate_limits


class ListRateLimitStatusesRequest(KaggleObject):
  r"""
  Attributes:
    redis_key_pattern (str)
      Optional filter/pattern passed directly to Redis (for efficient key
      searching)
    key_regex (str)
      Optional regex to use on the rate limit (Redis) key names.
    only_exceeded (bool)
      Should the response only include rate limits that have been
      exceeded/tripped?
    order_by (str)
      Optional fields to order by (e.g. 'key, tokens_count desc').
  """

  def __init__(self):
    self._redis_key_pattern = ""
    self._key_regex = ""
    self._only_exceeded = False
    self._order_by = ""
    self._freeze()

  @property
  def redis_key_pattern(self) -> str:
    r"""
    Optional filter/pattern passed directly to Redis (for efficient key
    searching)
    """
    return self._redis_key_pattern

  @redis_key_pattern.setter
  def redis_key_pattern(self, redis_key_pattern: str):
    if redis_key_pattern is None:
      del self.redis_key_pattern
      return
    if not isinstance(redis_key_pattern, str):
      raise TypeError('redis_key_pattern must be of type str')
    self._redis_key_pattern = redis_key_pattern

  @property
  def key_regex(self) -> str:
    """Optional regex to use on the rate limit (Redis) key names."""
    return self._key_regex

  @key_regex.setter
  def key_regex(self, key_regex: str):
    if key_regex is None:
      del self.key_regex
      return
    if not isinstance(key_regex, str):
      raise TypeError('key_regex must be of type str')
    self._key_regex = key_regex

  @property
  def only_exceeded(self) -> bool:
    r"""
    Should the response only include rate limits that have been
    exceeded/tripped?
    """
    return self._only_exceeded

  @only_exceeded.setter
  def only_exceeded(self, only_exceeded: bool):
    if only_exceeded is None:
      del self.only_exceeded
      return
    if not isinstance(only_exceeded, bool):
      raise TypeError('only_exceeded must be of type bool')
    self._only_exceeded = only_exceeded

  @property
  def order_by(self) -> str:
    """Optional fields to order by (e.g. 'key, tokens_count desc')."""
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: str):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, str):
      raise TypeError('order_by must be of type str')
    self._order_by = order_by


class ListRateLimitStatusesResponse(KaggleObject):
  r"""
  Attributes:
    filters_match_count (int)
      Number of rate limits that matched the filters (but irrespective of
      'only_exceeded').
    rate_limit_statuses (RateLimitStatus)
      All rate limits that match the filters and 'only_exceeded'
      Optionally ordered by 'order_by'.
    server_time_string (str)
      Time that the request was processed. All expiration times should be after
      this date. Not using Timestamp until JSON serialization issue is resolved:
      google.protobuf.Timestamp server_time = 2;
  """

  def __init__(self):
    self._filters_match_count = 0
    self._rate_limit_statuses = []
    self._server_time_string = ""
    self._freeze()

  @property
  def filters_match_count(self) -> int:
    r"""
    Number of rate limits that matched the filters (but irrespective of
    'only_exceeded').
    """
    return self._filters_match_count

  @filters_match_count.setter
  def filters_match_count(self, filters_match_count: int):
    if filters_match_count is None:
      del self.filters_match_count
      return
    if not isinstance(filters_match_count, int):
      raise TypeError('filters_match_count must be of type int')
    self._filters_match_count = filters_match_count

  @property
  def server_time_string(self) -> str:
    r"""
    Time that the request was processed. All expiration times should be after
    this date. Not using Timestamp until JSON serialization issue is resolved:
    google.protobuf.Timestamp server_time = 2;
    """
    return self._server_time_string

  @server_time_string.setter
  def server_time_string(self, server_time_string: str):
    if server_time_string is None:
      del self.server_time_string
      return
    if not isinstance(server_time_string, str):
      raise TypeError('server_time_string must be of type str')
    self._server_time_string = server_time_string

  @property
  def rate_limit_statuses(self) -> Optional[List[Optional['RateLimitStatus']]]:
    r"""
    All rate limits that match the filters and 'only_exceeded'
    Optionally ordered by 'order_by'.
    """
    return self._rate_limit_statuses

  @rate_limit_statuses.setter
  def rate_limit_statuses(self, rate_limit_statuses: Optional[List[Optional['RateLimitStatus']]]):
    if rate_limit_statuses is None:
      del self.rate_limit_statuses
      return
    if not isinstance(rate_limit_statuses, list):
      raise TypeError('rate_limit_statuses must be of type list')
    if not all([isinstance(t, RateLimitStatus) for t in rate_limit_statuses]):
      raise TypeError('rate_limit_statuses must contain only items of type RateLimitStatus')
    self._rate_limit_statuses = rate_limit_statuses


BatchResetRateLimitStatusesRequest._fields = [
  FieldMetadata("keys", "keys", "_keys", str, [], ListSerializer(PredefinedSerializer())),
]

BatchResetRateLimitStatusesResponse._fields = [
  FieldMetadata("resetCount", "reset_count", "_reset_count", int, 0, PredefinedSerializer()),
]

ListRateLimitsRequest._fields = []

ListRateLimitsResponse._fields = [
  FieldMetadata("rateLimits", "rate_limits", "_rate_limits", RateLimit, [], ListSerializer(KaggleObjectSerializer())),
]

ListRateLimitStatusesRequest._fields = [
  FieldMetadata("redisKeyPattern", "redis_key_pattern", "_redis_key_pattern", str, "", PredefinedSerializer()),
  FieldMetadata("keyRegex", "key_regex", "_key_regex", str, "", PredefinedSerializer()),
  FieldMetadata("onlyExceeded", "only_exceeded", "_only_exceeded", bool, False, PredefinedSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", str, "", PredefinedSerializer()),
]

ListRateLimitStatusesResponse._fields = [
  FieldMetadata("filtersMatchCount", "filters_match_count", "_filters_match_count", int, 0, PredefinedSerializer()),
  FieldMetadata("rateLimitStatuses", "rate_limit_statuses", "_rate_limit_statuses", RateLimitStatus, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("serverTimeString", "server_time_string", "_server_time_string", str, "", PredefinedSerializer()),
]

