from kagglesdk.common.types.cache_control import CacheControl, CacheLevel
from kagglesdk.kaggle_object import *
from typing import Optional, List

class InvalidateCacheRequest(KaggleObject):
  r"""
  Attributes:
    method_name (str)
      Full method name to specify which handler's cache will be evicted.
      Example: 'benchmarks.BenchmarksService/GetBenchmarkLeaderboard'.
    level (CacheLevel)
      What CacheLevel to invalidate. If not specified, request will be evicted
      from all caches (app, cdn).
    request_json (str)
      Json-serialized request to invalidate. If not specified, or set to empty
      string or empty json, all cached data of the method/handler will be
      evicted.
  """

  def __init__(self):
    self._method_name = ""
    self._level = CacheLevel.CACHE_LEVEL_UNSPECIFIED
    self._request_json = None
    self._freeze()

  @property
  def method_name(self) -> str:
    r"""
    Full method name to specify which handler's cache will be evicted.
    Example: 'benchmarks.BenchmarksService/GetBenchmarkLeaderboard'.
    """
    return self._method_name

  @method_name.setter
  def method_name(self, method_name: str):
    if method_name is None:
      del self.method_name
      return
    if not isinstance(method_name, str):
      raise TypeError('method_name must be of type str')
    self._method_name = method_name

  @property
  def level(self) -> 'CacheLevel':
    r"""
    What CacheLevel to invalidate. If not specified, request will be evicted
    from all caches (app, cdn).
    """
    return self._level

  @level.setter
  def level(self, level: 'CacheLevel'):
    if level is None:
      del self.level
      return
    if not isinstance(level, CacheLevel):
      raise TypeError('level must be of type CacheLevel')
    self._level = level

  @property
  def request_json(self) -> str:
    r"""
    Json-serialized request to invalidate. If not specified, or set to empty
    string or empty json, all cached data of the method/handler will be
    evicted.
    """
    return self._request_json or ""

  @request_json.setter
  def request_json(self, request_json: Optional[str]):
    if request_json is None:
      del self.request_json
      return
    if not isinstance(request_json, str):
      raise TypeError('request_json must be of type str')
    self._request_json = request_json


class InvalidateCacheResponse(KaggleObject):
  r"""
  Attributes:
    cache_control (CacheControl)
      CacheControl annotations for the requested method (for debugging purposes).
    message (str)
  """

  def __init__(self):
    self._cache_control = []
    self._message = ""
    self._freeze()

  @property
  def cache_control(self) -> Optional[List[Optional['CacheControl']]]:
    """CacheControl annotations for the requested method (for debugging purposes)."""
    return self._cache_control

  @cache_control.setter
  def cache_control(self, cache_control: Optional[List[Optional['CacheControl']]]):
    if cache_control is None:
      del self.cache_control
      return
    if not isinstance(cache_control, list):
      raise TypeError('cache_control must be of type list')
    if not all([isinstance(t, CacheControl) for t in cache_control]):
      raise TypeError('cache_control must contain only items of type CacheControl')
    self._cache_control = cache_control

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


InvalidateCacheRequest._fields = [
  FieldMetadata("methodName", "method_name", "_method_name", str, "", PredefinedSerializer()),
  FieldMetadata("level", "level", "_level", CacheLevel, CacheLevel.CACHE_LEVEL_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("requestJson", "request_json", "_request_json", str, None, PredefinedSerializer(), optional=True),
]

InvalidateCacheResponse._fields = [
  FieldMetadata("cacheControl", "cache_control", "_cache_control", CacheControl, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

