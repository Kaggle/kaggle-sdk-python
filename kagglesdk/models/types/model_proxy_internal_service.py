from datetime import timedelta
import enum
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ModelBackendState(enum.Enum):
  MODEL_BACKEND_STATE_UNSPECIFIED = 0
  MODEL_BACKEND_STATE_HEALTHY = 1
  MODEL_BACKEND_STATE_UNHEALTHY = 2

class Capabilities(KaggleObject):
  r"""
  What features can this token use?
  Note that features may be enabled by model groups *or* by being set on the
  token.
  NOTE: These are manually copied from modelproxy/auth.proto to prevent
  accidental exposure of hidden ones.

  Attributes:
    unrestricted_image_url (bool)
      Can users use any URL rather than just base64 encoded data URLs?
      This makes it harder to estimate token counts and is more prone to abuse.
    tool_calling (bool)
      Can users use tool/function calling?
      NOTE: This is experimental and only supports Chat Completions right now.
    allow_telemetry (bool)
      Can users use the telemetry API? /telemetry/logs
    allow_models_logs (bool)
      Can users use the logs API? /models/logs/latest
    allow_response_caching (bool)
      Can users use the model response cache?
      TODO(b/452348144): Currently, caching is enabled for all requests when this
      capability is enabled for a token.
    allow_full_model_list (bool)
      Can users list all models, not just the ones they have access to via
      their token groups/model slugs. This also includes extra
      model details such as allowed use groups and if the slug
      is the primary alias for its model.
    allow_model_capacity_info (bool)
      Can users list model capacity info? This is primarily meant for use by
      midtier schedulers.
    allow_request_logging (bool)
      Should users logs be recorded to the request log?
    allow_extended_input_modalities (bool)
      Can users use extended input modalities (e.g. YouTube URLs) in requests?
  """

  def __init__(self):
    self._unrestricted_image_url = False
    self._tool_calling = False
    self._allow_telemetry = False
    self._allow_models_logs = False
    self._allow_response_caching = False
    self._allow_full_model_list = False
    self._allow_model_capacity_info = False
    self._allow_request_logging = False
    self._allow_extended_input_modalities = False
    self._freeze()

  @property
  def unrestricted_image_url(self) -> bool:
    r"""
    Can users use any URL rather than just base64 encoded data URLs?
    This makes it harder to estimate token counts and is more prone to abuse.
    """
    return self._unrestricted_image_url

  @unrestricted_image_url.setter
  def unrestricted_image_url(self, unrestricted_image_url: bool):
    if unrestricted_image_url is None:
      del self.unrestricted_image_url
      return
    if not isinstance(unrestricted_image_url, bool):
      raise TypeError('unrestricted_image_url must be of type bool')
    self._unrestricted_image_url = unrestricted_image_url

  @property
  def tool_calling(self) -> bool:
    r"""
    Can users use tool/function calling?
    NOTE: This is experimental and only supports Chat Completions right now.
    """
    return self._tool_calling

  @tool_calling.setter
  def tool_calling(self, tool_calling: bool):
    if tool_calling is None:
      del self.tool_calling
      return
    if not isinstance(tool_calling, bool):
      raise TypeError('tool_calling must be of type bool')
    self._tool_calling = tool_calling

  @property
  def allow_telemetry(self) -> bool:
    """Can users use the telemetry API? /telemetry/logs"""
    return self._allow_telemetry

  @allow_telemetry.setter
  def allow_telemetry(self, allow_telemetry: bool):
    if allow_telemetry is None:
      del self.allow_telemetry
      return
    if not isinstance(allow_telemetry, bool):
      raise TypeError('allow_telemetry must be of type bool')
    self._allow_telemetry = allow_telemetry

  @property
  def allow_models_logs(self) -> bool:
    """Can users use the logs API? /models/logs/latest"""
    return self._allow_models_logs

  @allow_models_logs.setter
  def allow_models_logs(self, allow_models_logs: bool):
    if allow_models_logs is None:
      del self.allow_models_logs
      return
    if not isinstance(allow_models_logs, bool):
      raise TypeError('allow_models_logs must be of type bool')
    self._allow_models_logs = allow_models_logs

  @property
  def allow_response_caching(self) -> bool:
    r"""
    Can users use the model response cache?
    TODO(b/452348144): Currently, caching is enabled for all requests when this
    capability is enabled for a token.
    """
    return self._allow_response_caching

  @allow_response_caching.setter
  def allow_response_caching(self, allow_response_caching: bool):
    if allow_response_caching is None:
      del self.allow_response_caching
      return
    if not isinstance(allow_response_caching, bool):
      raise TypeError('allow_response_caching must be of type bool')
    self._allow_response_caching = allow_response_caching

  @property
  def allow_full_model_list(self) -> bool:
    r"""
    Can users list all models, not just the ones they have access to via
    their token groups/model slugs. This also includes extra
    model details such as allowed use groups and if the slug
    is the primary alias for its model.
    """
    return self._allow_full_model_list

  @allow_full_model_list.setter
  def allow_full_model_list(self, allow_full_model_list: bool):
    if allow_full_model_list is None:
      del self.allow_full_model_list
      return
    if not isinstance(allow_full_model_list, bool):
      raise TypeError('allow_full_model_list must be of type bool')
    self._allow_full_model_list = allow_full_model_list

  @property
  def allow_model_capacity_info(self) -> bool:
    r"""
    Can users list model capacity info? This is primarily meant for use by
    midtier schedulers.
    """
    return self._allow_model_capacity_info

  @allow_model_capacity_info.setter
  def allow_model_capacity_info(self, allow_model_capacity_info: bool):
    if allow_model_capacity_info is None:
      del self.allow_model_capacity_info
      return
    if not isinstance(allow_model_capacity_info, bool):
      raise TypeError('allow_model_capacity_info must be of type bool')
    self._allow_model_capacity_info = allow_model_capacity_info

  @property
  def allow_request_logging(self) -> bool:
    """Should users logs be recorded to the request log?"""
    return self._allow_request_logging

  @allow_request_logging.setter
  def allow_request_logging(self, allow_request_logging: bool):
    if allow_request_logging is None:
      del self.allow_request_logging
      return
    if not isinstance(allow_request_logging, bool):
      raise TypeError('allow_request_logging must be of type bool')
    self._allow_request_logging = allow_request_logging

  @property
  def allow_extended_input_modalities(self) -> bool:
    """Can users use extended input modalities (e.g. YouTube URLs) in requests?"""
    return self._allow_extended_input_modalities

  @allow_extended_input_modalities.setter
  def allow_extended_input_modalities(self, allow_extended_input_modalities: bool):
    if allow_extended_input_modalities is None:
      del self.allow_extended_input_modalities
      return
    if not isinstance(allow_extended_input_modalities, bool):
      raise TypeError('allow_extended_input_modalities must be of type bool')
    self._allow_extended_input_modalities = allow_extended_input_modalities


class CreateModelProxyTokenRequest(KaggleObject):
  r"""
  Attributes:
    allowed_model_names (str)
      Explicit list of model names (e.g. 'google/gemini-2.0-flash').
    allowed_model_groups (str)
      Preconfigured lists of models that are allowed (e.g. 'kaggle-benchmarks').
    validity_duration (timedelta)
      How long should the token be valid for? That is, its Time-To-Live (TTL).
      The duration should be specified in seconds, for example, '57600s' for 16
      hours.
    quota_infos (QuotaInfo)
      Contains info on max budgets and refill durations for each quota.
      `quotaUsd` is the max budget in USD, and `quotaRefillDuration` is the
      duration after which the quota is refilled.
      Example:
      quota_infos = [
        { 'quota_usd': 10, quota_refill_duration: '57600s'},
      ]
    quota_key (str)
      Key used to enforce quota/billing (e.g.
      'game_arena(chess-input):123456:openai/gpt-5').
      If not specified, it'll be of the form 'kaggle(123456)' or
      'kaggle_admin(123456)'.
    token_prefix (str)
      If specified, the prefix of the generated token to make it clearly
      identifiable. For example, 'game_arena(chess-input)'. If not specified, it
      will be 'kaggle'.
    token_restrictions (TokenRestrictions)
      If specified, restrictions to place upon the token itself.
      If not specified, default restrictions will apply.
    capabilities (Capabilities)
      If specified, grants this token the specified capabilities.
      Capabilities may be granted by the token, or by any model groups that the
      token is allowed to be used in.
      Available capabilities:
      - AllowTelemetry: Set to true to allow telemetry on the requests.
      - AllowModelsLogs: Set to true to allow logging of the models' inputs and
      outputs.
      - AllowRequestLogging: Set to true to allow logging of the requests.
      - AllowResponseCaching: Allow using the model proxy responses cache.
      - AllowExtendedInputModalities: Allow extended input modalities (e.g. YouTube URLs).
  """

  def __init__(self):
    self._allowed_model_names = []
    self._allowed_model_groups = []
    self._validity_duration = None
    self._quota_infos = []
    self._quota_key = ""
    self._token_prefix = ""
    self._token_restrictions = None
    self._capabilities = None
    self._freeze()

  @property
  def allowed_model_names(self) -> Optional[List[str]]:
    """Explicit list of model names (e.g. 'google/gemini-2.0-flash')."""
    return self._allowed_model_names

  @allowed_model_names.setter
  def allowed_model_names(self, allowed_model_names: Optional[List[str]]):
    if allowed_model_names is None:
      del self.allowed_model_names
      return
    if not isinstance(allowed_model_names, list):
      raise TypeError('allowed_model_names must be of type list')
    if not all([isinstance(t, str) for t in allowed_model_names]):
      raise TypeError('allowed_model_names must contain only items of type str')
    self._allowed_model_names = allowed_model_names

  @property
  def allowed_model_groups(self) -> Optional[List[str]]:
    """Preconfigured lists of models that are allowed (e.g. 'kaggle-benchmarks')."""
    return self._allowed_model_groups

  @allowed_model_groups.setter
  def allowed_model_groups(self, allowed_model_groups: Optional[List[str]]):
    if allowed_model_groups is None:
      del self.allowed_model_groups
      return
    if not isinstance(allowed_model_groups, list):
      raise TypeError('allowed_model_groups must be of type list')
    if not all([isinstance(t, str) for t in allowed_model_groups]):
      raise TypeError('allowed_model_groups must contain only items of type str')
    self._allowed_model_groups = allowed_model_groups

  @property
  def validity_duration(self) -> timedelta:
    r"""
    How long should the token be valid for? That is, its Time-To-Live (TTL).
    The duration should be specified in seconds, for example, '57600s' for 16
    hours.
    """
    return self._validity_duration

  @validity_duration.setter
  def validity_duration(self, validity_duration: timedelta):
    if validity_duration is None:
      del self.validity_duration
      return
    if not isinstance(validity_duration, timedelta):
      raise TypeError('validity_duration must be of type timedelta')
    self._validity_duration = validity_duration

  @property
  def quota_infos(self) -> Optional[List[Optional['QuotaInfo']]]:
    r"""
    Contains info on max budgets and refill durations for each quota.
    `quotaUsd` is the max budget in USD, and `quotaRefillDuration` is the
    duration after which the quota is refilled.
    Example:
    quota_infos = [
      { 'quota_usd': 10, quota_refill_duration: '57600s'},
    ]
    """
    return self._quota_infos

  @quota_infos.setter
  def quota_infos(self, quota_infos: Optional[List[Optional['QuotaInfo']]]):
    if quota_infos is None:
      del self.quota_infos
      return
    if not isinstance(quota_infos, list):
      raise TypeError('quota_infos must be of type list')
    if not all([isinstance(t, QuotaInfo) for t in quota_infos]):
      raise TypeError('quota_infos must contain only items of type QuotaInfo')
    self._quota_infos = quota_infos

  @property
  def quota_key(self) -> str:
    r"""
    Key used to enforce quota/billing (e.g.
    'game_arena(chess-input):123456:openai/gpt-5').
    If not specified, it'll be of the form 'kaggle(123456)' or
    'kaggle_admin(123456)'.
    """
    return self._quota_key

  @quota_key.setter
  def quota_key(self, quota_key: str):
    if quota_key is None:
      del self.quota_key
      return
    if not isinstance(quota_key, str):
      raise TypeError('quota_key must be of type str')
    self._quota_key = quota_key

  @property
  def token_prefix(self) -> str:
    r"""
    If specified, the prefix of the generated token to make it clearly
    identifiable. For example, 'game_arena(chess-input)'. If not specified, it
    will be 'kaggle'.
    """
    return self._token_prefix

  @token_prefix.setter
  def token_prefix(self, token_prefix: str):
    if token_prefix is None:
      del self.token_prefix
      return
    if not isinstance(token_prefix, str):
      raise TypeError('token_prefix must be of type str')
    self._token_prefix = token_prefix

  @property
  def token_restrictions(self) -> Optional['TokenRestrictions']:
    r"""
    If specified, restrictions to place upon the token itself.
    If not specified, default restrictions will apply.
    """
    return self._token_restrictions

  @token_restrictions.setter
  def token_restrictions(self, token_restrictions: Optional['TokenRestrictions']):
    if token_restrictions is None:
      del self.token_restrictions
      return
    if not isinstance(token_restrictions, TokenRestrictions):
      raise TypeError('token_restrictions must be of type TokenRestrictions')
    self._token_restrictions = token_restrictions

  @property
  def capabilities(self) -> Optional['Capabilities']:
    r"""
    If specified, grants this token the specified capabilities.
    Capabilities may be granted by the token, or by any model groups that the
    token is allowed to be used in.
    Available capabilities:
    - AllowTelemetry: Set to true to allow telemetry on the requests.
    - AllowModelsLogs: Set to true to allow logging of the models' inputs and
    outputs.
    - AllowRequestLogging: Set to true to allow logging of the requests.
    - AllowResponseCaching: Allow using the model proxy responses cache.
    - AllowExtendedInputModalities: Allow extended input modalities (e.g. YouTube URLs).
    """
    return self._capabilities

  @capabilities.setter
  def capabilities(self, capabilities: Optional['Capabilities']):
    if capabilities is None:
      del self.capabilities
      return
    if not isinstance(capabilities, Capabilities):
      raise TypeError('capabilities must be of type Capabilities')
    self._capabilities = capabilities


class CreateModelProxyTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Model Proxy token/API key
    base_uri (str)
      Base URL for contacting the proxy (e.g. 'https://mp.kaggle.net/models')
  """

  def __init__(self):
    self._token = ""
    self._base_uri = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Model Proxy token/API key"""
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
    """Base URL for contacting the proxy (e.g. 'https://mp.kaggle.net/models')"""
    return self._base_uri

  @base_uri.setter
  def base_uri(self, base_uri: str):
    if base_uri is None:
      del self.base_uri
      return
    if not isinstance(base_uri, str):
      raise TypeError('base_uri must be of type str')
    self._base_uri = base_uri


class ListModelBackendsRequest(KaggleObject):
  r"""
  """

  pass

class ListModelBackendsResponse(KaggleObject):
  r"""
  Attributes:
    model_backends (ModelBackend)
  """

  def __init__(self):
    self._model_backends = []
    self._freeze()

  @property
  def model_backends(self) -> Optional[List[Optional['ModelBackend']]]:
    return self._model_backends

  @model_backends.setter
  def model_backends(self, model_backends: Optional[List[Optional['ModelBackend']]]):
    if model_backends is None:
      del self.model_backends
      return
    if not isinstance(model_backends, list):
      raise TypeError('model_backends must be of type list')
    if not all([isinstance(t, ModelBackend) for t in model_backends]):
      raise TypeError('model_backends must contain only items of type ModelBackend')
    self._model_backends = model_backends


class ModelBackend(KaggleObject):
  r"""
  Attributes:
    slug (str)
      Slug of the model (e.g. 'google/gemini-2.5-pro').
    state (ModelBackendState)
      Current state of the backend.
    average_rpm (float)
      Average number of requests per minute.
    target_rpm (float)
      Current target number of requests per minute.
  """

  def __init__(self):
    self._slug = ""
    self._state = ModelBackendState.MODEL_BACKEND_STATE_UNSPECIFIED
    self._average_rpm = None
    self._target_rpm = None
    self._freeze()

  @property
  def slug(self) -> str:
    """Slug of the model (e.g. 'google/gemini-2.5-pro')."""
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def state(self) -> 'ModelBackendState':
    """Current state of the backend."""
    return self._state

  @state.setter
  def state(self, state: 'ModelBackendState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, ModelBackendState):
      raise TypeError('state must be of type ModelBackendState')
    self._state = state

  @property
  def average_rpm(self) -> float:
    """Average number of requests per minute."""
    return self._average_rpm or 0.0

  @average_rpm.setter
  def average_rpm(self, average_rpm: Optional[float]):
    if average_rpm is None:
      del self.average_rpm
      return
    if not isinstance(average_rpm, float):
      raise TypeError('average_rpm must be of type float')
    self._average_rpm = average_rpm

  @property
  def target_rpm(self) -> float:
    """Current target number of requests per minute."""
    return self._target_rpm or 0.0

  @target_rpm.setter
  def target_rpm(self, target_rpm: Optional[float]):
    if target_rpm is None:
      del self.target_rpm
      return
    if not isinstance(target_rpm, float):
      raise TypeError('target_rpm must be of type float')
    self._target_rpm = target_rpm


class QuotaInfo(KaggleObject):
  r"""
  Attributes:
    quota_refill_duration (timedelta)
      If specified, how long until the quota tracked by the key will be refilled.
      If not specified, it will exactly match the validity_duration.
    quota_usd (float)
      Maximum quota/budget (in US dollars). This is enforced based on the
      quota_key. All tokens with the same quota_usd and quota_key will be
      aggregated together.
  """

  def __init__(self):
    self._quota_refill_duration = None
    self._quota_usd = 0.0
    self._freeze()

  @property
  def quota_refill_duration(self) -> timedelta:
    r"""
    If specified, how long until the quota tracked by the key will be refilled.
    If not specified, it will exactly match the validity_duration.
    """
    return self._quota_refill_duration

  @quota_refill_duration.setter
  def quota_refill_duration(self, quota_refill_duration: timedelta):
    if quota_refill_duration is None:
      del self.quota_refill_duration
      return
    if not isinstance(quota_refill_duration, timedelta):
      raise TypeError('quota_refill_duration must be of type timedelta')
    self._quota_refill_duration = quota_refill_duration

  @property
  def quota_usd(self) -> float:
    r"""
    Maximum quota/budget (in US dollars). This is enforced based on the
    quota_key. All tokens with the same quota_usd and quota_key will be
    aggregated together.
    """
    return self._quota_usd

  @quota_usd.setter
  def quota_usd(self, quota_usd: float):
    if quota_usd is None:
      del self.quota_usd
      return
    if not isinstance(quota_usd, float):
      raise TypeError('quota_usd must be of type float')
    self._quota_usd = quota_usd


class TokenRestrictions(KaggleObject):
  r"""
  Where can the token be used? If multiple are specified, they are treated
  as an AND (all must be true).
  NOTE: These are manually copied from modelproxy/auth.proto to prevent
  accidental exposure of hidden ones.

  Attributes:
    client_ip_address (str)
      Allowed (external) IP address for using the token. This is typically
      the IP address of the virtual machine that is making the call to the proxy.
    country_code (str)
      The country code of the user. This is used to enforce geo restrictions of
      the token (e.g. disallowing image generation in restricted countries).
    max_ips (int)
      If set, the number of distinct IP addresses that are allowed to use the
      token.
  """

  def __init__(self):
    self._client_ip_address = None
    self._country_code = None
    self._max_ips = None
    self._freeze()

  @property
  def client_ip_address(self) -> str:
    r"""
    Allowed (external) IP address for using the token. This is typically
    the IP address of the virtual machine that is making the call to the proxy.
    """
    return self._client_ip_address or ""

  @client_ip_address.setter
  def client_ip_address(self, client_ip_address: Optional[str]):
    if client_ip_address is None:
      del self.client_ip_address
      return
    if not isinstance(client_ip_address, str):
      raise TypeError('client_ip_address must be of type str')
    self._client_ip_address = client_ip_address

  @property
  def country_code(self) -> str:
    r"""
    The country code of the user. This is used to enforce geo restrictions of
    the token (e.g. disallowing image generation in restricted countries).
    """
    return self._country_code or ""

  @country_code.setter
  def country_code(self, country_code: Optional[str]):
    if country_code is None:
      del self.country_code
      return
    if not isinstance(country_code, str):
      raise TypeError('country_code must be of type str')
    self._country_code = country_code

  @property
  def max_ips(self) -> int:
    r"""
    If set, the number of distinct IP addresses that are allowed to use the
    token.
    """
    return self._max_ips or 0

  @max_ips.setter
  def max_ips(self, max_ips: Optional[int]):
    if max_ips is None:
      del self.max_ips
      return
    if not isinstance(max_ips, int):
      raise TypeError('max_ips must be of type int')
    self._max_ips = max_ips


Capabilities._fields = [
  FieldMetadata("unrestrictedImageUrl", "unrestricted_image_url", "_unrestricted_image_url", bool, False, PredefinedSerializer()),
  FieldMetadata("toolCalling", "tool_calling", "_tool_calling", bool, False, PredefinedSerializer()),
  FieldMetadata("allowTelemetry", "allow_telemetry", "_allow_telemetry", bool, False, PredefinedSerializer()),
  FieldMetadata("allowModelsLogs", "allow_models_logs", "_allow_models_logs", bool, False, PredefinedSerializer()),
  FieldMetadata("allowResponseCaching", "allow_response_caching", "_allow_response_caching", bool, False, PredefinedSerializer()),
  FieldMetadata("allowFullModelList", "allow_full_model_list", "_allow_full_model_list", bool, False, PredefinedSerializer()),
  FieldMetadata("allowModelCapacityInfo", "allow_model_capacity_info", "_allow_model_capacity_info", bool, False, PredefinedSerializer()),
  FieldMetadata("allowRequestLogging", "allow_request_logging", "_allow_request_logging", bool, False, PredefinedSerializer()),
  FieldMetadata("allowExtendedInputModalities", "allow_extended_input_modalities", "_allow_extended_input_modalities", bool, False, PredefinedSerializer()),
]

CreateModelProxyTokenRequest._fields = [
  FieldMetadata("allowedModelNames", "allowed_model_names", "_allowed_model_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("allowedModelGroups", "allowed_model_groups", "_allowed_model_groups", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("validityDuration", "validity_duration", "_validity_duration", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("quotaInfos", "quota_infos", "_quota_infos", QuotaInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("quotaKey", "quota_key", "_quota_key", str, "", PredefinedSerializer()),
  FieldMetadata("tokenPrefix", "token_prefix", "_token_prefix", str, "", PredefinedSerializer()),
  FieldMetadata("tokenRestrictions", "token_restrictions", "_token_restrictions", TokenRestrictions, None, KaggleObjectSerializer()),
  FieldMetadata("capabilities", "capabilities", "_capabilities", Capabilities, None, KaggleObjectSerializer()),
]

CreateModelProxyTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("baseUri", "base_uri", "_base_uri", str, "", PredefinedSerializer()),
]

ListModelBackendsRequest._fields = []

ListModelBackendsResponse._fields = [
  FieldMetadata("modelBackends", "model_backends", "_model_backends", ModelBackend, [], ListSerializer(KaggleObjectSerializer())),
]

ModelBackend._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", ModelBackendState, ModelBackendState.MODEL_BACKEND_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("averageRpm", "average_rpm", "_average_rpm", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("targetRpm", "target_rpm", "_target_rpm", float, None, PredefinedSerializer(), optional=True),
]

QuotaInfo._fields = [
  FieldMetadata("quotaRefillDuration", "quota_refill_duration", "_quota_refill_duration", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("quotaUsd", "quota_usd", "_quota_usd", float, 0.0, PredefinedSerializer()),
]

TokenRestrictions._fields = [
  FieldMetadata("clientIpAddress", "client_ip_address", "_client_ip_address", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countryCode", "country_code", "_country_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxIps", "max_ips", "_max_ips", int, None, PredefinedSerializer(), optional=True),
]

