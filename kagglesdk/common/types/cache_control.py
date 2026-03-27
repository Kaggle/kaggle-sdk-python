import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class CacheLevel(enum.Enum):
  CACHE_LEVEL_UNSPECIFIED = 0
  CACHE_LEVEL_APP = 1
  """App level cache is cached in the app server (both in-memory and in Redis)."""
  CACHE_LEVEL_CDN = 2
  r"""
  CDN level cache is cached in the Content Delivery Network (CDN) so cached
  responses are served directly from the CDN without going through the app
  server.
  """

class CacheAge(KaggleObject):
  r"""
  Attributes:
    seconds (int)
    minutes (int)
    hours (int)
    days (int)
  """

  def __init__(self):
    self._seconds = None
    self._minutes = None
    self._hours = None
    self._days = None
    self._freeze()

  @property
  def seconds(self) -> int:
    return self._seconds or 0

  @seconds.setter
  def seconds(self, seconds: int):
    if seconds is None:
      del self.seconds
      return
    if not isinstance(seconds, int):
      raise TypeError('seconds must be of type int')
    del self.minutes
    del self.hours
    del self.days
    self._seconds = seconds

  @property
  def minutes(self) -> int:
    return self._minutes or 0

  @minutes.setter
  def minutes(self, minutes: int):
    if minutes is None:
      del self.minutes
      return
    if not isinstance(minutes, int):
      raise TypeError('minutes must be of type int')
    del self.seconds
    del self.hours
    del self.days
    self._minutes = minutes

  @property
  def hours(self) -> int:
    return self._hours or 0

  @hours.setter
  def hours(self, hours: int):
    if hours is None:
      del self.hours
      return
    if not isinstance(hours, int):
      raise TypeError('hours must be of type int')
    del self.seconds
    del self.minutes
    del self.days
    self._hours = hours

  @property
  def days(self) -> int:
    return self._days or 0

  @days.setter
  def days(self, days: int):
    if days is None:
      del self.days
      return
    if not isinstance(days, int):
      raise TypeError('days must be of type int')
    del self.seconds
    del self.minutes
    del self.hours
    self._days = days


class CacheControl(KaggleObject):
  r"""
  Attributes:
    max_age (CacheAge)
      The maximum age of the cache.
    level (CacheLevel)
      The level of the cache. App level cache is cached in the app server, while
      Content Delivery Network (CDN) level cache is cached in the CDN.
  """

  def __init__(self):
    self._max_age = None
    self._level = CacheLevel.CACHE_LEVEL_UNSPECIFIED
    self._freeze()

  @property
  def max_age(self) -> Optional['CacheAge']:
    """The maximum age of the cache."""
    return self._max_age

  @max_age.setter
  def max_age(self, max_age: Optional['CacheAge']):
    if max_age is None:
      del self.max_age
      return
    if not isinstance(max_age, CacheAge):
      raise TypeError('max_age must be of type CacheAge')
    self._max_age = max_age

  @property
  def level(self) -> 'CacheLevel':
    r"""
    The level of the cache. App level cache is cached in the app server, while
    Content Delivery Network (CDN) level cache is cached in the CDN.
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


CacheAge._fields = [
  FieldMetadata("seconds", "seconds", "_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("minutes", "minutes", "_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hours", "hours", "_hours", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("days", "days", "_days", int, None, PredefinedSerializer(), optional=True),
]

CacheControl._fields = [
  FieldMetadata("maxAge", "max_age", "_max_age", CacheAge, None, KaggleObjectSerializer()),
  FieldMetadata("level", "level", "_level", CacheLevel, CacheLevel.CACHE_LEVEL_UNSPECIFIED, EnumSerializer()),
]

