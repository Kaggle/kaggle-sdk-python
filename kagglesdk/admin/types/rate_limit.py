from kagglesdk.kaggle_object import *
from typing import List, Optional

class RateLimit(KaggleObject):
  r"""
  Attributes:
    name (str)
      The name of the limit (e.g. 'CompetitionApiRequest').
    scopes (RateLimitScope)
      All of the scopes that apply for the rate limit.
  """

  def __init__(self):
    self._name = ""
    self._scopes = []
    self._freeze()

  @property
  def name(self) -> str:
    """The name of the limit (e.g. 'CompetitionApiRequest')."""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def scopes(self) -> Optional[List[Optional['RateLimitScope']]]:
    """All of the scopes that apply for the rate limit."""
    return self._scopes

  @scopes.setter
  def scopes(self, scopes: Optional[List[Optional['RateLimitScope']]]):
    if scopes is None:
      del self.scopes
      return
    if not isinstance(scopes, list):
      raise TypeError('scopes must be of type list')
    if not all([isinstance(t, RateLimitScope) for t in scopes]):
      raise TypeError('scopes must contain only items of type RateLimitScope')
    self._scopes = scopes


class RateLimitFillRate(KaggleObject):
  r"""
  Attributes:
    per (str)
      Time period to fill completely (e.g. 'minute', 'hour')
    initial_token_count (float)
  """

  def __init__(self):
    self._per = ""
    self._initial_token_count = 0.0
    self._freeze()

  @property
  def per(self) -> str:
    """Time period to fill completely (e.g. 'minute', 'hour')"""
    return self._per

  @per.setter
  def per(self, per: str):
    if per is None:
      del self.per
      return
    if not isinstance(per, str):
      raise TypeError('per must be of type str')
    self._per = per

  @property
  def initial_token_count(self) -> float:
    return self._initial_token_count

  @initial_token_count.setter
  def initial_token_count(self, initial_token_count: float):
    if initial_token_count is None:
      del self.initial_token_count
      return
    if not isinstance(initial_token_count, float):
      raise TypeError('initial_token_count must be of type float')
    self._initial_token_count = initial_token_count


class RateLimitScope(KaggleObject):
  r"""
  Attributes:
    scope (str)
      The scope of the rate limit (e.g. 'user', 'all')
    fill_rates (RateLimitFillRate)
  """

  def __init__(self):
    self._scope = ""
    self._fill_rates = []
    self._freeze()

  @property
  def scope(self) -> str:
    """The scope of the rate limit (e.g. 'user', 'all')"""
    return self._scope

  @scope.setter
  def scope(self, scope: str):
    if scope is None:
      del self.scope
      return
    if not isinstance(scope, str):
      raise TypeError('scope must be of type str')
    self._scope = scope

  @property
  def fill_rates(self) -> Optional[List[Optional['RateLimitFillRate']]]:
    return self._fill_rates

  @fill_rates.setter
  def fill_rates(self, fill_rates: Optional[List[Optional['RateLimitFillRate']]]):
    if fill_rates is None:
      del self.fill_rates
      return
    if not isinstance(fill_rates, list):
      raise TypeError('fill_rates must be of type list')
    if not all([isinstance(t, RateLimitFillRate) for t in fill_rates]):
      raise TypeError('fill_rates must contain only items of type RateLimitFillRate')
    self._fill_rates = fill_rates


class RateLimitStatus(KaggleObject):
  r"""
  Attributes:
    key (str)
    tokens_count (float)
    blocks_count (int)
    initial_tokens_count (float)
    update_time_string (str)
      Not using Timestamp until JSON serialization issue is resolved:
      See
      https://kaggle.slack.com/archives/CEDHFMV6D/p1570810506045800?thread_ts=1570810037.045200&cid=CEDHFMV6D
      google.protobuf.Timestamp update_time = 2;
    expiration_time_string (str)
      google.protobuf.Timestamp expiration_time = 3;
  """

  def __init__(self):
    self._key = ""
    self._tokens_count = 0.0
    self._blocks_count = 0
    self._initial_tokens_count = 0.0
    self._update_time_string = ""
    self._expiration_time_string = ""
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def update_time_string(self) -> str:
    r"""
    Not using Timestamp until JSON serialization issue is resolved:
    See
    https://kaggle.slack.com/archives/CEDHFMV6D/p1570810506045800?thread_ts=1570810037.045200&cid=CEDHFMV6D
    google.protobuf.Timestamp update_time = 2;
    """
    return self._update_time_string

  @update_time_string.setter
  def update_time_string(self, update_time_string: str):
    if update_time_string is None:
      del self.update_time_string
      return
    if not isinstance(update_time_string, str):
      raise TypeError('update_time_string must be of type str')
    self._update_time_string = update_time_string

  @property
  def expiration_time_string(self) -> str:
    """google.protobuf.Timestamp expiration_time = 3;"""
    return self._expiration_time_string

  @expiration_time_string.setter
  def expiration_time_string(self, expiration_time_string: str):
    if expiration_time_string is None:
      del self.expiration_time_string
      return
    if not isinstance(expiration_time_string, str):
      raise TypeError('expiration_time_string must be of type str')
    self._expiration_time_string = expiration_time_string

  @property
  def tokens_count(self) -> float:
    return self._tokens_count

  @tokens_count.setter
  def tokens_count(self, tokens_count: float):
    if tokens_count is None:
      del self.tokens_count
      return
    if not isinstance(tokens_count, float):
      raise TypeError('tokens_count must be of type float')
    self._tokens_count = tokens_count

  @property
  def blocks_count(self) -> int:
    return self._blocks_count

  @blocks_count.setter
  def blocks_count(self, blocks_count: int):
    if blocks_count is None:
      del self.blocks_count
      return
    if not isinstance(blocks_count, int):
      raise TypeError('blocks_count must be of type int')
    self._blocks_count = blocks_count

  @property
  def initial_tokens_count(self) -> float:
    return self._initial_tokens_count

  @initial_tokens_count.setter
  def initial_tokens_count(self, initial_tokens_count: float):
    if initial_tokens_count is None:
      del self.initial_tokens_count
      return
    if not isinstance(initial_tokens_count, float):
      raise TypeError('initial_tokens_count must be of type float')
    self._initial_tokens_count = initial_tokens_count


RateLimit._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("scopes", "scopes", "_scopes", RateLimitScope, [], ListSerializer(KaggleObjectSerializer())),
]

RateLimitFillRate._fields = [
  FieldMetadata("per", "per", "_per", str, "", PredefinedSerializer()),
  FieldMetadata("initialTokenCount", "initial_token_count", "_initial_token_count", float, 0.0, PredefinedSerializer()),
]

RateLimitScope._fields = [
  FieldMetadata("scope", "scope", "_scope", str, "", PredefinedSerializer()),
  FieldMetadata("fillRates", "fill_rates", "_fill_rates", RateLimitFillRate, [], ListSerializer(KaggleObjectSerializer())),
]

RateLimitStatus._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("tokensCount", "tokens_count", "_tokens_count", float, 0.0, PredefinedSerializer()),
  FieldMetadata("blocksCount", "blocks_count", "_blocks_count", int, 0, PredefinedSerializer()),
  FieldMetadata("initialTokensCount", "initial_tokens_count", "_initial_tokens_count", float, 0.0, PredefinedSerializer()),
  FieldMetadata("updateTimeString", "update_time_string", "_update_time_string", str, "", PredefinedSerializer()),
  FieldMetadata("expirationTimeString", "expiration_time_string", "_expiration_time_string", str, "", PredefinedSerializer()),
]

