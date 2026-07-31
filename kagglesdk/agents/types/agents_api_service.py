from kagglesdk.agents.types.agent_enums import HarnessType
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from typing import Optional

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


ApiCreateHarnessRequest._fields = [
  FieldMetadata("harness", "harness", "_harness", ApiHarness, None, KaggleObjectSerializer()),
]

ApiCreateHarnessVersionRequest._fields = [
  FieldMetadata("harnessVersion", "harness_version", "_harness_version", ApiHarnessVersion, None, KaggleObjectSerializer()),
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

