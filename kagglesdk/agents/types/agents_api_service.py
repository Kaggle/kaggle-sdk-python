from kagglesdk.agents.types.agent_enums import HarnessType
from kagglesdk.agents.types.agent_service import ListAgentsFilter, ListHarnessesFilter
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from typing import Optional, List

class ApiAgent(KaggleObject):
  r"""
  API equivalent of Agent from agent_types.proto.

  Attributes:
    id (int)
      Output-only on create.
    display_name (str)
    slug (str)
    is_public (bool)
    organization_id (int)
    benchmark_model_version_config_id (int)
    harness_version_id (int)
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._is_public = False
    self._organization_id = None
    self._benchmark_model_version_config_id = 0
    self._harness_version_id = 0
    self._organization = None
    self._freeze()

  @property
  def id(self) -> int:
    """Output-only on create."""
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
  def display_name(self) -> str:
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def slug(self) -> str:
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
  def is_public(self) -> bool:
    return self._is_public

  @is_public.setter
  def is_public(self, is_public: bool):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def organization_id(self) -> int:
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: Optional[int]):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def benchmark_model_version_config_id(self) -> int:
    return self._benchmark_model_version_config_id

  @benchmark_model_version_config_id.setter
  def benchmark_model_version_config_id(self, benchmark_model_version_config_id: int):
    if benchmark_model_version_config_id is None:
      del self.benchmark_model_version_config_id
      return
    if not isinstance(benchmark_model_version_config_id, int):
      raise TypeError('benchmark_model_version_config_id must be of type int')
    self._benchmark_model_version_config_id = benchmark_model_version_config_id

  @property
  def harness_version_id(self) -> int:
    return self._harness_version_id

  @harness_version_id.setter
  def harness_version_id(self, harness_version_id: int):
    if harness_version_id is None:
      del self.harness_version_id
      return
    if not isinstance(harness_version_id, int):
      raise TypeError('harness_version_id must be of type int')
    self._harness_version_id = harness_version_id

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization


class ApiCreateAgentRequest(KaggleObject):
  r"""
  Attributes:
    agent (ApiAgent)
  """

  def __init__(self):
    self._agent = None
    self._freeze()

  @property
  def agent(self) -> Optional['ApiAgent']:
    return self._agent

  @agent.setter
  def agent(self, agent: Optional['ApiAgent']):
    if agent is None:
      del self.agent
      return
    if not isinstance(agent, ApiAgent):
      raise TypeError('agent must be of type ApiAgent')
    self._agent = agent

  def endpoint(self):
    path = '/api/v1/agents/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateHarnessRequest(KaggleObject):
  r"""
  Attributes:
    harness (ApiHarness)
      The Harness to create. Must include version.
  """

  def __init__(self):
    self._harness = None
    self._freeze()

  @property
  def harness(self) -> Optional['ApiHarness']:
    """The Harness to create. Must include version."""
    return self._harness

  @harness.setter
  def harness(self, harness: Optional['ApiHarness']):
    if harness is None:
      del self.harness
      return
    if not isinstance(harness, ApiHarness):
      raise TypeError('harness must be of type ApiHarness')
    self._harness = harness

  def endpoint(self):
    path = '/api/v1/agents/harnesses/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateHarnessVersionRequest(KaggleObject):
  r"""
  Attributes:
    harness_version (ApiHarnessVersion)
  """

  def __init__(self):
    self._harness_version = None
    self._freeze()

  @property
  def harness_version(self) -> Optional['ApiHarnessVersion']:
    return self._harness_version

  @harness_version.setter
  def harness_version(self, harness_version: Optional['ApiHarnessVersion']):
    if harness_version is None:
      del self.harness_version
      return
    if not isinstance(harness_version, ApiHarnessVersion):
      raise TypeError('harness_version must be of type ApiHarnessVersion')
    self._harness_version = harness_version

  def endpoint(self):
    path = '/api/v1/agents/harnesses/versions/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiGetAgentRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the Agent to fetch.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the Agent to fetch."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  def endpoint(self):
    path = '/api/v1/agents/{id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/agents/{id}'


class ApiGetHarnessRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the Harness to fetch.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the Harness to fetch."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  def endpoint(self):
    path = '/api/v1/agents/harnesses/{id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/agents/harnesses/{id}'


class ApiGetHarnessVersionRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the HarnessVersion to fetch.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the HarnessVersion to fetch."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  def endpoint(self):
    path = '/api/v1/agents/harnesses/versions/{id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/agents/harnesses/versions/{id}'


class ApiHarborCanonicalHarnessVersion(KaggleObject):
  r"""
  API equivalent of HarborCanonicalHarnessVersion.

  Attributes:
    harbor_slug (str)
    harbor_version_slug (str)
  """

  def __init__(self):
    self._harbor_slug = ""
    self._harbor_version_slug = ""
    self._freeze()

  @property
  def harbor_slug(self) -> str:
    return self._harbor_slug

  @harbor_slug.setter
  def harbor_slug(self, harbor_slug: str):
    if harbor_slug is None:
      del self.harbor_slug
      return
    if not isinstance(harbor_slug, str):
      raise TypeError('harbor_slug must be of type str')
    self._harbor_slug = harbor_slug

  @property
  def harbor_version_slug(self) -> str:
    return self._harbor_version_slug

  @harbor_version_slug.setter
  def harbor_version_slug(self, harbor_version_slug: str):
    if harbor_version_slug is None:
      del self.harbor_version_slug
      return
    if not isinstance(harbor_version_slug, str):
      raise TypeError('harbor_version_slug must be of type str')
    self._harbor_version_slug = harbor_version_slug


class ApiHarness(KaggleObject):
  r"""
  API equivalent of Harness from agent_types.proto.

  Attributes:
    id (int)
      Output-only on create.
    display_name (str)
    slug (str)
    is_public (bool)
    organization_id (int)
    type (HarnessType)
    version (ApiHarnessVersion)
      Required on CreateHarness — a Harness is unusable without a version.
      On read responses this holds the latest / relevant HarnessVersion.
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._is_public = False
    self._organization_id = None
    self._type = HarnessType.HARNESS_TYPE_UNSPECIFIED
    self._version = None
    self._organization = None
    self._freeze()

  @property
  def id(self) -> int:
    """Output-only on create."""
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
  def display_name(self) -> str:
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def slug(self) -> str:
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
  def is_public(self) -> bool:
    return self._is_public

  @is_public.setter
  def is_public(self, is_public: bool):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def organization_id(self) -> int:
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: Optional[int]):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def type(self) -> 'HarnessType':
    return self._type

  @type.setter
  def type(self, type: 'HarnessType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HarnessType):
      raise TypeError('type must be of type HarnessType')
    self._type = type

  @property
  def version(self) -> Optional['ApiHarnessVersion']:
    r"""
    Required on CreateHarness — a Harness is unusable without a version.
    On read responses this holds the latest / relevant HarnessVersion.
    """
    return self._version

  @version.setter
  def version(self, version: Optional['ApiHarnessVersion']):
    if version is None:
      del self.version
      return
    if not isinstance(version, ApiHarnessVersion):
      raise TypeError('version must be of type ApiHarnessVersion')
    self._version = version

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization


class ApiHarnessVersion(KaggleObject):
  r"""
  API equivalent of HarnessVersion from agent_types.proto.

  Attributes:
    id (int)
      Output-only on create.
    display_name (str)
    slug (str)
    is_public (bool)
    harness_id (int)
      Required for standalone CreateHarnessVersion; ignored when nested in
      ApiHarness.version on CreateHarness.
    harbor_canonical (ApiHarborCanonicalHarnessVersion)
    kernel_game_arena (ApiKernelGameArenaHarnessVersion)
    kernel_comps_bench (ApiKernelCompsBenchHarnessVersion)
    organization (OrganizationCard)
      Fields from the parent Harness for convenience. Ignored on create and
      update.
    type (HarnessType)
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._is_public = False
    self._harness_id = 0
    self._harbor_canonical = None
    self._kernel_game_arena = None
    self._kernel_comps_bench = None
    self._organization = None
    self._type = HarnessType.HARNESS_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    """Output-only on create."""
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
  def display_name(self) -> str:
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def slug(self) -> str:
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
  def is_public(self) -> bool:
    return self._is_public

  @is_public.setter
  def is_public(self, is_public: bool):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def harness_id(self) -> int:
    r"""
    Required for standalone CreateHarnessVersion; ignored when nested in
    ApiHarness.version on CreateHarness.
    """
    return self._harness_id

  @harness_id.setter
  def harness_id(self, harness_id: int):
    if harness_id is None:
      del self.harness_id
      return
    if not isinstance(harness_id, int):
      raise TypeError('harness_id must be of type int')
    self._harness_id = harness_id

  @property
  def harbor_canonical(self) -> Optional['ApiHarborCanonicalHarnessVersion']:
    return self._harbor_canonical or None

  @harbor_canonical.setter
  def harbor_canonical(self, harbor_canonical: Optional['ApiHarborCanonicalHarnessVersion']):
    if harbor_canonical is None:
      del self.harbor_canonical
      return
    if not isinstance(harbor_canonical, ApiHarborCanonicalHarnessVersion):
      raise TypeError('harbor_canonical must be of type ApiHarborCanonicalHarnessVersion')
    del self.kernel_game_arena
    del self.kernel_comps_bench
    self._harbor_canonical = harbor_canonical

  @property
  def kernel_game_arena(self) -> Optional['ApiKernelGameArenaHarnessVersion']:
    return self._kernel_game_arena or None

  @kernel_game_arena.setter
  def kernel_game_arena(self, kernel_game_arena: Optional['ApiKernelGameArenaHarnessVersion']):
    if kernel_game_arena is None:
      del self.kernel_game_arena
      return
    if not isinstance(kernel_game_arena, ApiKernelGameArenaHarnessVersion):
      raise TypeError('kernel_game_arena must be of type ApiKernelGameArenaHarnessVersion')
    del self.harbor_canonical
    del self.kernel_comps_bench
    self._kernel_game_arena = kernel_game_arena

  @property
  def kernel_comps_bench(self) -> Optional['ApiKernelCompsBenchHarnessVersion']:
    return self._kernel_comps_bench or None

  @kernel_comps_bench.setter
  def kernel_comps_bench(self, kernel_comps_bench: Optional['ApiKernelCompsBenchHarnessVersion']):
    if kernel_comps_bench is None:
      del self.kernel_comps_bench
      return
    if not isinstance(kernel_comps_bench, ApiKernelCompsBenchHarnessVersion):
      raise TypeError('kernel_comps_bench must be of type ApiKernelCompsBenchHarnessVersion')
    del self.harbor_canonical
    del self.kernel_game_arena
    self._kernel_comps_bench = kernel_comps_bench

  @property
  def organization(self) -> Optional['OrganizationCard']:
    r"""
    Fields from the parent Harness for convenience. Ignored on create and
    update.
    """
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def type(self) -> 'HarnessType':
    return self._type

  @type.setter
  def type(self, type: 'HarnessType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HarnessType):
      raise TypeError('type must be of type HarnessType')
    self._type = type


class ApiKernelCompsBenchHarnessVersion(KaggleObject):
  r"""
  API equivalent of KernelCompsBenchHarnessVersion.

  Attributes:
    kernel_session_id (int)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    return self._kernel_session_id

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id


class ApiKernelGameArenaHarnessVersion(KaggleObject):
  r"""
  API equivalent of KernelGameArenaHarnessVersion.

  Attributes:
    kernel_session_id (int)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    return self._kernel_session_id

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id


class ApiListAgentsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    filter (ListAgentsFilter)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = ""
    self._filter = None
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def filter(self) -> Optional['ListAgentsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListAgentsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListAgentsFilter):
      raise TypeError('filter must be of type ListAgentsFilter')
    self._filter = filter

  def endpoint(self):
    path = '/api/v1/agents'
    return path.format_map(self.to_field_map(self))


class ApiListAgentsResponse(KaggleObject):
  r"""
  Attributes:
    agents (ApiAgent)
    next_page_token (str)
  """

  def __init__(self):
    self._agents = []
    self._next_page_token = None
    self._freeze()

  @property
  def agents(self) -> Optional[List[Optional['ApiAgent']]]:
    return self._agents

  @agents.setter
  def agents(self, agents: Optional[List[Optional['ApiAgent']]]):
    if agents is None:
      del self.agents
      return
    if not isinstance(agents, list):
      raise TypeError('agents must be of type list')
    if not all([isinstance(t, ApiAgent) for t in agents]):
      raise TypeError('agents must contain only items of type ApiAgent')
    self._agents = agents

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiListHarnessesRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    filter (ListHarnessesFilter)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = ""
    self._filter = None
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def filter(self) -> Optional['ListHarnessesFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListHarnessesFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListHarnessesFilter):
      raise TypeError('filter must be of type ListHarnessesFilter')
    self._filter = filter

  def endpoint(self):
    path = '/api/v1/agents/harnesses'
    return path.format_map(self.to_field_map(self))


class ApiListHarnessesResponse(KaggleObject):
  r"""
  Attributes:
    harnesses (ApiHarness)
      One row per HarnessVersion. Each row's outer ApiHarness fields describe
      the parent Harness; ApiHarness.version is the specific version for this
      row.
    next_page_token (str)
  """

  def __init__(self):
    self._harnesses = []
    self._next_page_token = None
    self._freeze()

  @property
  def harnesses(self) -> Optional[List[Optional['ApiHarness']]]:
    r"""
    One row per HarnessVersion. Each row's outer ApiHarness fields describe
    the parent Harness; ApiHarness.version is the specific version for this
    row.
    """
    return self._harnesses

  @harnesses.setter
  def harnesses(self, harnesses: Optional[List[Optional['ApiHarness']]]):
    if harnesses is None:
      del self.harnesses
      return
    if not isinstance(harnesses, list):
      raise TypeError('harnesses must be of type list')
    if not all([isinstance(t, ApiHarness) for t in harnesses]):
      raise TypeError('harnesses must contain only items of type ApiHarness')
    self._harnesses = harnesses

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def nextPageToken(self):
    return self.next_page_token


ApiAgent._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkModelVersionConfigId", "benchmark_model_version_config_id", "_benchmark_model_version_config_id", int, 0, PredefinedSerializer()),
  FieldMetadata("harnessVersionId", "harness_version_id", "_harness_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
]

ApiCreateAgentRequest._fields = [
  FieldMetadata("agent", "agent", "_agent", ApiAgent, None, KaggleObjectSerializer()),
]

ApiCreateHarnessRequest._fields = [
  FieldMetadata("harness", "harness", "_harness", ApiHarness, None, KaggleObjectSerializer()),
]

ApiCreateHarnessVersionRequest._fields = [
  FieldMetadata("harnessVersion", "harness_version", "_harness_version", ApiHarnessVersion, None, KaggleObjectSerializer()),
]

ApiGetAgentRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

ApiGetHarnessRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

ApiGetHarnessVersionRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

ApiHarborCanonicalHarnessVersion._fields = [
  FieldMetadata("harborSlug", "harbor_slug", "_harbor_slug", str, "", PredefinedSerializer()),
  FieldMetadata("harborVersionSlug", "harbor_version_slug", "_harbor_version_slug", str, "", PredefinedSerializer()),
]

ApiHarness._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", HarnessType, HarnessType.HARNESS_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("version", "version", "_version", ApiHarnessVersion, None, KaggleObjectSerializer()),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
]

ApiHarnessVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("harnessId", "harness_id", "_harness_id", int, 0, PredefinedSerializer()),
  FieldMetadata("harborCanonical", "harbor_canonical", "_harbor_canonical", ApiHarborCanonicalHarnessVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelGameArena", "kernel_game_arena", "_kernel_game_arena", ApiKernelGameArenaHarnessVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelCompsBench", "kernel_comps_bench", "_kernel_comps_bench", ApiKernelCompsBenchHarnessVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", HarnessType, HarnessType.HARNESS_TYPE_UNSPECIFIED, EnumSerializer()),
]

ApiKernelCompsBenchHarnessVersion._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

ApiKernelGameArenaHarnessVersion._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

ApiListAgentsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("filter", "filter", "_filter", ListAgentsFilter, None, KaggleObjectSerializer()),
]

ApiListAgentsResponse._fields = [
  FieldMetadata("agents", "agents", "_agents", ApiAgent, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListHarnessesRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("filter", "filter", "_filter", ListHarnessesFilter, None, KaggleObjectSerializer()),
]

ApiListHarnessesResponse._fields = [
  FieldMetadata("harnesses", "harnesses", "_harnesses", ApiHarness, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

