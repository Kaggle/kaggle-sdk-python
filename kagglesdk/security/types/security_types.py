from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.security.types.authentication import AuthorizationScope
from typing import Optional, List

class KaggleResourceType(enum.Enum):
  r"""
  Types of Kaggle resources on which permissions can be defined. Each entry in
  this proto must correspond to a permission block in the Permission enum in
  'permissions.proto'. For example COMPETITIONS_GET permission
  applies to resource of type COMPETITIONS and thus has value of 300 because
  COMPETITIONS_X permissions block start at 3000. The formula
  ValueOfFirstCanonicalPermission / 10. (COMPETITIONS_GET = 3001) / 10 =>
  (COMPETITIONS = 300).
  Please see the documentation of the Permission enum to understand permission
  blocks better.
  """
  KAGGLE_RESOURCE_TYPE_UNSPECIFIED = 0
  KAGGLE_RESOURCE_TYPE_WILDCARD_ALL = -1
  KAGGLE_RESOURCE_TYPE_USERS = 100
  """---------- Shared ----------"""
  KAGGLE_RESOURCE_TYPE_USER_ATTRIBUTES = 102
  KAGGLE_RESOURCE_TYPE_ATTRIBUTES = 104
  KAGGLE_RESOURCE_TYPE_ACCESS_TOKENS = 106
  KAGGLE_RESOURCE_TYPE_API_TOKENS = 108
  KAGGLE_RESOURCE_TYPE_SYNCHRONIZED_GROUPS = 110
  KAGGLE_RESOURCE_TYPE_BLOBS = 112
  KAGGLE_RESOURCE_TYPE_LICENSES = 114
  KAGGLE_RESOURCE_TYPE_LICENSE_USER_AGREEMENTS = 116
  KAGGLE_RESOURCE_TYPE_SEARCH_PROXY = 118
  KAGGLE_RESOURCE_TYPE_SECRETS = 120
  KAGGLE_RESOURCE_TYPE_SECRET_ATTACHMENTS = 122
  KAGGLE_RESOURCE_TYPE_TAGS = 124
  KAGGLE_RESOURCE_TYPE_RESOURCES = 130
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUPS = 132
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUP_INVITES = 134
  KAGGLE_RESOURCE_TYPE_USER_MANAGED_GROUP_MEMBERSHIPS = 136
  KAGGLE_RESOURCE_TYPE_OAUTH_CLIENTS = 138
  KAGGLE_RESOURCE_TYPE_RESOURCE_ACCESS_GROUPS = 140
  KAGGLE_RESOURCE_TYPE_OPERATIONS = 142
  KAGGLE_RESOURCE_TYPE_AGENT_EXAMS = 144
  KAGGLE_RESOURCE_TYPE_FORUMS = 200
  """---------- Community ----------"""
  KAGGLE_RESOURCE_TYPE_FORUM_TOPICS = 202
  KAGGLE_RESOURCE_TYPE_FORUM_MESSAGES = 204
  KAGGLE_RESOURCE_TYPE_FORUM_MESSAGE_ATTACHMENTS = 208
  KAGGLE_RESOURCE_TYPE_BADGES = 210
  KAGGLE_RESOURCE_TYPE_USER_BADGES = 212
  KAGGLE_RESOURCE_TYPE_BOOKMARKS = 214
  KAGGLE_RESOURCE_TYPE_COLLECTIONS = 216
  KAGGLE_RESOURCE_TYPE_NUDGES = 218
  KAGGLE_RESOURCE_TYPE_ORGANIZATIONS = 220
  KAGGLE_RESOURCE_TYPE_ORGANIZATION_MEMBERS = 224
  KAGGLE_RESOURCE_TYPE_SUGGESTED_ITEMS = 226
  KAGGLE_RESOURCE_TYPE_WRITE_UPS = 228
  KAGGLE_RESOURCE_TYPE_VOTES = 230
  KAGGLE_RESOURCE_TYPE_OPEN_GRAPH_IMAGE_METADATUM = 232
  KAGGLE_RESOURCE_TYPE_COMPETITIONS = 300
  """---------- Competitions ----------"""
  KAGGLE_RESOURCE_TYPE_COMPETITION_LEADERBOARDS = 304
  KAGGLE_RESOURCE_TYPE_EPISODES = 306
  KAGGLE_RESOURCE_TYPE_EPISODE_AGENTS = 308
  KAGGLE_RESOURCE_TYPE_EVALUATION_ALGORITHMS = 310
  KAGGLE_RESOURCE_TYPE_HOST_SEGMENTS = 312
  KAGGLE_RESOURCE_TYPE_PAGES = 314
  KAGGLE_RESOURCE_TYPE_SUBMISSIONS = 316
  KAGGLE_RESOURCE_TYPE_SUBMISSION_RESCORES = 318
  KAGGLE_RESOURCE_TYPE_TEAMS = 320
  KAGGLE_RESOURCE_TYPE_TEAM_MERGE_REQUESTS = 322
  KAGGLE_RESOURCE_TYPE_HACKATHON_WRITE_UPS = 324
  KAGGLE_RESOURCE_TYPE_COMPETITION_METRIC_VERSIONS = 326
  KAGGLE_RESOURCE_TYPE_DATASETS = 400
  """---------- Datasets ----------"""
  KAGGLE_RESOURCE_TYPE_DATASET_VERSIONS = 404
  KAGGLE_RESOURCE_TYPE_DATASET_SUGGESTION_BUNDLES = 406
  KAGGLE_RESOURCE_TYPE_DATABUNDLES = 408
  KAGGLE_RESOURCE_TYPE_DATABUNDLE_VERSIONS = 410
  KAGGLE_RESOURCE_TYPE_DATA_VIEWS = 412
  KAGGLE_RESOURCE_TYPE_KERNELS = 500
  """---------- Kernels ----------"""
  KAGGLE_RESOURCE_TYPE_KERNEL_SESSIONS = 504
  KAGGLE_RESOURCE_TYPE_KERNEL_SNIPPETS = 508
  KAGGLE_RESOURCE_TYPE_KERNEL_SOURCE_REFERENCES = 510
  KAGGLE_RESOURCE_TYPE_KERNEL_VERSIONS = 512
  KAGGLE_RESOURCE_TYPE_RESOURCE_REFERENCES = 520
  KAGGLE_RESOURCE_TYPE_MODELS = 600
  """---------- Models ----------"""
  KAGGLE_RESOURCE_TYPE_MODEL_INSTANCES = 608
  KAGGLE_RESOURCE_TYPE_MODEL_INSTANCE_VERSIONS = 610
  KAGGLE_RESOURCE_TYPE_MODEL_VERSIONS = 612
  KAGGLE_RESOURCE_TYPE_GATING_AGREEMENTS = 614
  KAGGLE_RESOURCE_TYPE_GATING_AGREEMENTS_USER_CONSENTS = 616
  KAGGLE_RESOURCE_TYPE_MODEL_PROXY = 620
  KAGGLE_RESOURCE_TYPE_BENCHMARKS = 700
  """---------- Benchmarks ----------"""
  KAGGLE_RESOURCE_TYPE_BENCHMARK_VERSIONS = 704
  KAGGLE_RESOURCE_TYPE_BENCHMARK_MODELS = 706
  KAGGLE_RESOURCE_TYPE_BENCHMARK_MODEL_VERSIONS = 708
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASKS = 710
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASK_VERSIONS = 712
  KAGGLE_RESOURCE_TYPE_BENCHMARK_TASK_RUNS = 714
  KAGGLE_RESOURCE_TYPE_COURSE_TRACKS = 800
  """---------- Courses ----------"""
  KAGGLE_RESOURCE_TYPE_COURSE_LESSONS = 802
  KAGGLE_RESOURCE_TYPE_COURSE_TUTORIALS = 804

class ApiTokenStatus(enum.Enum):
  API_TOKEN_STATUS_UNSPECIFIED = 0
  ACTIVE = 1
  EXPIRED = 2

class ApiTokenType(enum.Enum):
  """Type of an ApiToken."""
  API_TOKEN_TYPE_UNSPECIFIED = 0
  UNRESTRICTED_ACCESS_TOKEN = 1
  r"""
  Unrestricted API tokens that are used to access Kaggle ApiV1 endpoints
  (https://github.com/Kaggle/kaggle-cli). These grant access to all ApiV1
  endpoints ('/api/v1/...') without any restriction and they never expire
  (unless explicitly expired by the user through the
  https://www.kaggle.com/settings interface).
  """
  REFRESH_TOKEN = 2
  r"""
  Modern scoped API refresh tokens that are used to generate short-lived
  scoped access tokens to provide granular access to Kaggle. These let us
  create tokens that can be used, for example, to only allow 'submission
  to a certain competition'.
  """
  ACCESS_TOKEN = 3
  r"""
  Modern scoped API access tokens that are not associated with a refresh
  token to provide granular access to Kaggle.
  """

class ApiToken(KaggleObject):
  r"""
  Represents an access or refresh token stored in the database.

  Attributes:
    id (int)
      Id of the token.
    type (ApiTokenType)
      Type of the token: UnrestrictedAccessToken or RefreshToken.
    name (str)
      User-assigned descriptive name.
    redacted_value (str)
      Last 8 characters of the token to make it easier for users to identity it.
    create_time (datetime)
      Time this token was created.
    last_use_time (datetime)
      Approximate last time this token was used to access Kaggle.
    oauth_client (OAuthClient)
      OAuth application that has generated this token on behalf of the token
      owner.
    authorization_scopes (AuthorizationScope)
      Set of scopes to restrict a refresh token.
    user_id (int)
      Id of the user that this tokens belongs to.
    status (ApiTokenStatus)
      Status of the token (active or expired).
  """

  def __init__(self):
    self._id = 0
    self._type = ApiTokenType.API_TOKEN_TYPE_UNSPECIFIED
    self._name = None
    self._redacted_value = None
    self._create_time = None
    self._last_use_time = None
    self._oauth_client = None
    self._authorization_scopes = []
    self._user_id = 0
    self._status = ApiTokenStatus.API_TOKEN_STATUS_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the token."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def type(self) -> 'ApiTokenType':
    """Type of the token: UnrestrictedAccessToken or RefreshToken."""
    return self._type

  @type.setter
  def type(self, type: 'ApiTokenType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ApiTokenType):
      raise TypeError('type must be of type ApiTokenType')
    self._type = type

  @property
  def name(self) -> str:
    """User-assigned descriptive name."""
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def redacted_value(self) -> str:
    """Last 8 characters of the token to make it easier for users to identity it."""
    return self._redacted_value or ""

  @redacted_value.setter
  def redacted_value(self, redacted_value: Optional[str]):
    if redacted_value is None:
      del self.redacted_value
      return
    if not isinstance(redacted_value, str):
      raise TypeError('redacted_value must be of type str')
    self._redacted_value = redacted_value

  @property
  def create_time(self) -> datetime:
    """Time this token was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def last_use_time(self) -> datetime:
    """Approximate last time this token was used to access Kaggle."""
    return self._last_use_time or None

  @last_use_time.setter
  def last_use_time(self, last_use_time: Optional[datetime]):
    if last_use_time is None:
      del self.last_use_time
      return
    if not isinstance(last_use_time, datetime):
      raise TypeError('last_use_time must be of type datetime')
    self._last_use_time = last_use_time

  @property
  def oauth_client(self) -> Optional['OAuthClient']:
    r"""
    OAuth application that has generated this token on behalf of the token
    owner.
    """
    return self._oauth_client or None

  @oauth_client.setter
  def oauth_client(self, oauth_client: Optional[Optional['OAuthClient']]):
    if oauth_client is None:
      del self.oauth_client
      return
    if not isinstance(oauth_client, OAuthClient):
      raise TypeError('oauth_client must be of type OAuthClient')
    self._oauth_client = oauth_client

  @property
  def authorization_scopes(self) -> Optional[List[Optional['AuthorizationScope']]]:
    """Set of scopes to restrict a refresh token."""
    return self._authorization_scopes

  @authorization_scopes.setter
  def authorization_scopes(self, authorization_scopes: Optional[List[Optional['AuthorizationScope']]]):
    if authorization_scopes is None:
      del self.authorization_scopes
      return
    if not isinstance(authorization_scopes, list):
      raise TypeError('authorization_scopes must be of type list')
    if not all([isinstance(t, AuthorizationScope) for t in authorization_scopes]):
      raise TypeError('authorization_scopes must contain only items of type AuthorizationScope')
    self._authorization_scopes = authorization_scopes

  @property
  def user_id(self) -> int:
    """Id of the user that this tokens belongs to."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def status(self) -> 'ApiTokenStatus':
    """Status of the token (active or expired)."""
    return self._status

  @status.setter
  def status(self, status: 'ApiTokenStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, ApiTokenStatus):
      raise TypeError('status must be of type ApiTokenStatus')
    self._status = status


class KaggleResourceId(KaggleObject):
  r"""
  Attributes:
    type (KaggleResourceType)
    id (int)
    hash_link (str)
  """

  def __init__(self):
    self._type = KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED
    self._id = 0
    self._hash_link = None
    self._freeze()

  @property
  def type(self) -> 'KaggleResourceType':
    return self._type

  @type.setter
  def type(self, type: 'KaggleResourceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, KaggleResourceType):
      raise TypeError('type must be of type KaggleResourceType')
    self._type = type

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


class OAuthClient(KaggleObject):
  r"""
  Attributes:
    id (int)
      Database-generated immutable unique id that is used to update or delete
      this client.
    organization_slug (str)
      Slug of the organization that this OAuth client associated to. Caller must
      have owner rights to the organization to be able to see/create/delete an
      organization-backed client.
    client_id (str)
      OAuth client_id. When creating a new client, this must be set if the
      client is not an organization-backed one (i.e., a public client like
      'kagglesdk' or 'kagglehub'). For organization-backed clients, this is set
      automatically to 'org:<slug>'.
    client_name (str)
      OAuth client_name. Similar to client_id, this must be set if the client is
      not an organization-backed (i.e., a public client like 'kagglesdk' or
      'kagglehub'). It will be automatically set to organization name otherwise.
    allowed_authorization_scopes (AuthorizationScope)
      Authorization scopes that the client can use. Must be set.
    allowed_redirect_uris (str)
      List of redirect URIs that are allowed as callback for this OAuth client.
    enabled (bool)
      Whether this application is enabled or not.
  """

  def __init__(self):
    self._id = 0
    self._organization_slug = None
    self._client_id = None
    self._client_name = None
    self._allowed_authorization_scopes = []
    self._allowed_redirect_uris = []
    self._enabled = False
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    Database-generated immutable unique id that is used to update or delete
    this client.
    """
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def organization_slug(self) -> str:
    r"""
    Slug of the organization that this OAuth client associated to. Caller must
    have owner rights to the organization to be able to see/create/delete an
    organization-backed client.
    """
    return self._organization_slug or ""

  @organization_slug.setter
  def organization_slug(self, organization_slug: Optional[str]):
    if organization_slug is None:
      del self.organization_slug
      return
    if not isinstance(organization_slug, str):
      raise TypeError('organization_slug must be of type str')
    self._organization_slug = organization_slug

  @property
  def client_id(self) -> str:
    r"""
    OAuth client_id. When creating a new client, this must be set if the
    client is not an organization-backed one (i.e., a public client like
    'kagglesdk' or 'kagglehub'). For organization-backed clients, this is set
    automatically to 'org:<slug>'.
    """
    return self._client_id or ""

  @client_id.setter
  def client_id(self, client_id: Optional[str]):
    if client_id is None:
      del self.client_id
      return
    if not isinstance(client_id, str):
      raise TypeError('client_id must be of type str')
    self._client_id = client_id

  @property
  def client_name(self) -> str:
    r"""
    OAuth client_name. Similar to client_id, this must be set if the client is
    not an organization-backed (i.e., a public client like 'kagglesdk' or
    'kagglehub'). It will be automatically set to organization name otherwise.
    """
    return self._client_name or ""

  @client_name.setter
  def client_name(self, client_name: Optional[str]):
    if client_name is None:
      del self.client_name
      return
    if not isinstance(client_name, str):
      raise TypeError('client_name must be of type str')
    self._client_name = client_name

  @property
  def allowed_authorization_scopes(self) -> Optional[List[Optional['AuthorizationScope']]]:
    """Authorization scopes that the client can use. Must be set."""
    return self._allowed_authorization_scopes

  @allowed_authorization_scopes.setter
  def allowed_authorization_scopes(self, allowed_authorization_scopes: Optional[List[Optional['AuthorizationScope']]]):
    if allowed_authorization_scopes is None:
      del self.allowed_authorization_scopes
      return
    if not isinstance(allowed_authorization_scopes, list):
      raise TypeError('allowed_authorization_scopes must be of type list')
    if not all([isinstance(t, AuthorizationScope) for t in allowed_authorization_scopes]):
      raise TypeError('allowed_authorization_scopes must contain only items of type AuthorizationScope')
    self._allowed_authorization_scopes = allowed_authorization_scopes

  @property
  def allowed_redirect_uris(self) -> Optional[List[str]]:
    """List of redirect URIs that are allowed as callback for this OAuth client."""
    return self._allowed_redirect_uris

  @allowed_redirect_uris.setter
  def allowed_redirect_uris(self, allowed_redirect_uris: Optional[List[str]]):
    if allowed_redirect_uris is None:
      del self.allowed_redirect_uris
      return
    if not isinstance(allowed_redirect_uris, list):
      raise TypeError('allowed_redirect_uris must be of type list')
    if not all([isinstance(t, str) for t in allowed_redirect_uris]):
      raise TypeError('allowed_redirect_uris must contain only items of type str')
    self._allowed_redirect_uris = allowed_redirect_uris

  @property
  def enabled(self) -> bool:
    """Whether this application is enabled or not."""
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled


ApiToken._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", ApiTokenType, ApiTokenType.API_TOKEN_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("redactedValue", "redacted_value", "_redacted_value", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastUseTime", "last_use_time", "_last_use_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("oauthClient", "oauth_client", "_oauth_client", OAuthClient, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authorizationScopes", "authorization_scopes", "_authorization_scopes", AuthorizationScope, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", ApiTokenStatus, ApiTokenStatus.API_TOKEN_STATUS_UNSPECIFIED, EnumSerializer()),
]

KaggleResourceId._fields = [
  FieldMetadata("type", "type", "_type", KaggleResourceType, KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

OAuthClient._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("organizationSlug", "organization_slug", "_organization_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("clientId", "client_id", "_client_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("clientName", "client_name", "_client_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("allowedAuthorizationScopes", "allowed_authorization_scopes", "_allowed_authorization_scopes", AuthorizationScope, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("allowedRedirectUris", "allowed_redirect_uris", "_allowed_redirect_uris", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
]

