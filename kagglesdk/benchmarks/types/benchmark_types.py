from datetime import datetime
import enum
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkArenaArtifactType, BenchmarkGalleryCardSize, BenchmarkModelImportanceLevel, Modality
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from typing import Optional, List

class BenchmarkTaskValidationStage(enum.Enum):
  r"""
  A stage run against a new task version before it is marked completed. Saved
  to the DB. Do not modify existing values.
  """
  BENCHMARK_TASK_VALIDATION_STAGE_UNSPECIFIED = 0
  BENCHMARK_TASK_VALIDATION_STAGE_NOP = 1
  r"""
  Harbor's nop agent, which takes no action. Passes when no attempt earns a
  reward, catching tasks whose tests pass on an untouched environment.
  """
  BENCHMARK_TASK_VALIDATION_STAGE_ORACLE = 2
  r"""
  Harbor's oracle agent, which runs the task's solution script. Passes when
  every attempt earns a reward of 1.
  """
  BENCHMARK_TASK_VALIDATION_STAGE_DEFAULT_CANDIDATE = 3
  """The task version's default candidate. Passes when its run completes."""

class HarborMetricType(enum.Enum):
  r"""
  Canonical metric reducers shipped by Harbor (minus uv-script), used to
  resolve a task version's N attempts into aggregate values (e.g. for pass@K
  scoring). Saved to the DB. Do not modify existing values.
  """
  HARBOR_METRIC_TYPE_UNSPECIFIED = 0
  HARBOR_METRIC_TYPE_SUM = 1
  HARBOR_METRIC_TYPE_MIN = 2
  HARBOR_METRIC_TYPE_MAX = 3
  HARBOR_METRIC_TYPE_MEAN = 4

class BenchmarkArenaCombination(KaggleObject):
  r"""
  A (task version, candidate) combination opted into a benchmark version's
  arena. The candidate matches the task version's candidate type.

  Attributes:
    task_version_id (int)
    candidate (BenchmarkCandidate)
      reasoning_effort is not supported; pass the config instead.
  """

  def __init__(self):
    self._task_version_id = 0
    self._candidate = None
    self._freeze()

  @property
  def task_version_id(self) -> int:
    return self._task_version_id

  @task_version_id.setter
  def task_version_id(self, task_version_id: int):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def candidate(self) -> Optional['BenchmarkCandidate']:
    """reasoning_effort is not supported; pass the config instead."""
    return self._candidate

  @candidate.setter
  def candidate(self, candidate: Optional['BenchmarkCandidate']):
    if candidate is None:
      del self.candidate
      return
    if not isinstance(candidate, BenchmarkCandidate):
      raise TypeError('candidate must be of type BenchmarkCandidate')
    self._candidate = candidate


class BenchmarkArenaSettings(KaggleObject):
  r"""
  Human-vote arena over a benchmark version's task run artifacts.

  Attributes:
    artifact_path (str)
      Glob, relative to a run's session output root, selecting the artifact,
      e.g. '*.mp4'.
    artifact_type (BenchmarkArenaArtifactType)
    reveal_candidates (bool)
      Show candidate names after a vote. Off keeps voting fully blind.
    voting_enabled (bool)
      Kill switches for the arena's public surfaces. Off when the arena is
      created.
    gallery_enabled (bool)
    arena_task_version_id (int)
      The task version the arena's overall Elo is written to, shown as a
      leaderboard column. Created once the arena has votes to rank.
    gallery_card_size (BenchmarkGalleryCardSize)
    expand_artifacts (bool)
      Clicking an artifact opens it full size, rather than voting for it in the
      arena. HTML artifacts always do; this extends it to every type, for outputs
      too detailed to judge at card size.
  """

  def __init__(self):
    self._artifact_path = ""
    self._artifact_type = BenchmarkArenaArtifactType.BENCHMARK_ARENA_ARTIFACT_TYPE_UNSPECIFIED
    self._reveal_candidates = False
    self._voting_enabled = False
    self._gallery_enabled = False
    self._arena_task_version_id = None
    self._gallery_card_size = BenchmarkGalleryCardSize.BENCHMARK_GALLERY_CARD_SIZE_UNSPECIFIED
    self._expand_artifacts = False
    self._freeze()

  @property
  def artifact_path(self) -> str:
    r"""
    Glob, relative to a run's session output root, selecting the artifact,
    e.g. '*.mp4'.
    """
    return self._artifact_path

  @artifact_path.setter
  def artifact_path(self, artifact_path: str):
    if artifact_path is None:
      del self.artifact_path
      return
    if not isinstance(artifact_path, str):
      raise TypeError('artifact_path must be of type str')
    self._artifact_path = artifact_path

  @property
  def artifact_type(self) -> 'BenchmarkArenaArtifactType':
    return self._artifact_type

  @artifact_type.setter
  def artifact_type(self, artifact_type: 'BenchmarkArenaArtifactType'):
    if artifact_type is None:
      del self.artifact_type
      return
    if not isinstance(artifact_type, BenchmarkArenaArtifactType):
      raise TypeError('artifact_type must be of type BenchmarkArenaArtifactType')
    self._artifact_type = artifact_type

  @property
  def reveal_candidates(self) -> bool:
    """Show candidate names after a vote. Off keeps voting fully blind."""
    return self._reveal_candidates

  @reveal_candidates.setter
  def reveal_candidates(self, reveal_candidates: bool):
    if reveal_candidates is None:
      del self.reveal_candidates
      return
    if not isinstance(reveal_candidates, bool):
      raise TypeError('reveal_candidates must be of type bool')
    self._reveal_candidates = reveal_candidates

  @property
  def voting_enabled(self) -> bool:
    r"""
    Kill switches for the arena's public surfaces. Off when the arena is
    created.
    """
    return self._voting_enabled

  @voting_enabled.setter
  def voting_enabled(self, voting_enabled: bool):
    if voting_enabled is None:
      del self.voting_enabled
      return
    if not isinstance(voting_enabled, bool):
      raise TypeError('voting_enabled must be of type bool')
    self._voting_enabled = voting_enabled

  @property
  def gallery_enabled(self) -> bool:
    return self._gallery_enabled

  @gallery_enabled.setter
  def gallery_enabled(self, gallery_enabled: bool):
    if gallery_enabled is None:
      del self.gallery_enabled
      return
    if not isinstance(gallery_enabled, bool):
      raise TypeError('gallery_enabled must be of type bool')
    self._gallery_enabled = gallery_enabled

  @property
  def arena_task_version_id(self) -> int:
    r"""
    The task version the arena's overall Elo is written to, shown as a
    leaderboard column. Created once the arena has votes to rank.
    """
    return self._arena_task_version_id or 0

  @arena_task_version_id.setter
  def arena_task_version_id(self, arena_task_version_id: Optional[int]):
    if arena_task_version_id is None:
      del self.arena_task_version_id
      return
    if not isinstance(arena_task_version_id, int):
      raise TypeError('arena_task_version_id must be of type int')
    self._arena_task_version_id = arena_task_version_id

  @property
  def gallery_card_size(self) -> 'BenchmarkGalleryCardSize':
    return self._gallery_card_size

  @gallery_card_size.setter
  def gallery_card_size(self, gallery_card_size: 'BenchmarkGalleryCardSize'):
    if gallery_card_size is None:
      del self.gallery_card_size
      return
    if not isinstance(gallery_card_size, BenchmarkGalleryCardSize):
      raise TypeError('gallery_card_size must be of type BenchmarkGalleryCardSize')
    self._gallery_card_size = gallery_card_size

  @property
  def expand_artifacts(self) -> bool:
    r"""
    Clicking an artifact opens it full size, rather than voting for it in the
    arena. HTML artifacts always do; this extends it to every type, for outputs
    too detailed to judge at card size.
    """
    return self._expand_artifacts

  @expand_artifacts.setter
  def expand_artifacts(self, expand_artifacts: bool):
    if expand_artifacts is None:
      del self.expand_artifacts
      return
    if not isinstance(expand_artifacts, bool):
      raise TypeError('expand_artifacts must be of type bool')
    self._expand_artifacts = expand_artifacts


class BenchmarkCandidate(KaggleObject):
  r"""
  One contestant to run a benchmark against. A config can be named either by
  its id or as its model version plus reasoning_effort, because the public API
  knows an effort string while the admin UI already holds config ids.

  Attributes:
    benchmark_model_version_id (int)
      The model version to run against.
    agent_id (int)
      The agent to run against. Agents are backed by a BenchmarkModelVersion.
    reasoning_effort (str)
      Reasoning effort to evaluate the model version at (e.g. 'high'), resolved
      to the model version's config at that effort; no such config is rejected.
      Only valid alongside benchmark_model_version_id, since an agent and a
      config each already pin their own.
    benchmark_model_version_config_id (int)
      The config to run against, which pins its own model version and effort.
  """

  def __init__(self):
    self._benchmark_model_version_id = None
    self._agent_id = None
    self._reasoning_effort = None
    self._benchmark_model_version_config_id = None
    self._freeze()

  @property
  def benchmark_model_version_id(self) -> int:
    """The model version to run against."""
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    del self.agent_id
    del self.benchmark_model_version_config_id
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def agent_id(self) -> int:
    """The agent to run against. Agents are backed by a BenchmarkModelVersion."""
    return self._agent_id or 0

  @agent_id.setter
  def agent_id(self, agent_id: int):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, int):
      raise TypeError('agent_id must be of type int')
    del self.benchmark_model_version_id
    del self.benchmark_model_version_config_id
    self._agent_id = agent_id

  @property
  def benchmark_model_version_config_id(self) -> int:
    """The config to run against, which pins its own model version and effort."""
    return self._benchmark_model_version_config_id or 0

  @benchmark_model_version_config_id.setter
  def benchmark_model_version_config_id(self, benchmark_model_version_config_id: int):
    if benchmark_model_version_config_id is None:
      del self.benchmark_model_version_config_id
      return
    if not isinstance(benchmark_model_version_config_id, int):
      raise TypeError('benchmark_model_version_config_id must be of type int')
    del self.benchmark_model_version_id
    del self.agent_id
    self._benchmark_model_version_config_id = benchmark_model_version_config_id

  @property
  def reasoning_effort(self) -> str:
    r"""
    Reasoning effort to evaluate the model version at (e.g. 'high'), resolved
    to the model version's config at that effort; no such config is rejected.
    Only valid alongside benchmark_model_version_id, since an agent and a
    config each already pin their own.
    """
    return self._reasoning_effort or ""

  @reasoning_effort.setter
  def reasoning_effort(self, reasoning_effort: Optional[str]):
    if reasoning_effort is None:
      del self.reasoning_effort
      return
    if not isinstance(reasoning_effort, str):
      raise TypeError('reasoning_effort must be of type str')
    self._reasoning_effort = reasoning_effort


class BenchmarkModel(KaggleObject):
  r"""
  Attributes:
    id (int)
      This benchmark model's id.
    display_name (str)
      The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'
    slug (str)
      The slug of the model (plus variation). ex: 'gemini-1.5-pro'
    organization_id (int)
      The organization that published the model.
    owner_user_id (int)
      The user that owns / created this model.
      Filled automatically while creating, can be updated later.
    license_id (int)
      The license for this model.
    default_version_id (int)
      The default version to use for this model.
      Filled automatically while creating, can be updated later.
    version (BenchmarkModelVersion)
      The version associated with this benchmark model.
      * CREATE : first version to be created with the parent benchmark model.
      * GET    : specified version or default if none was specified.
      * UPDATE : unused (use UpdateBenchmarkModelVersion).
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
    license (License)
      The associated License. Ignored on create and update.
    published (bool)
      Whether the benchmark model is published (iff ContentStateId == PUBLISHED).
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._organization_id = None
    self._owner_user_id = None
    self._license_id = 0
    self._default_version_id = None
    self._version = None
    self._organization = None
    self._license = None
    self._published = False
    self._freeze()

  @property
  def id(self) -> int:
    """This benchmark model's id."""
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
    """The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'"""
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
    """The slug of the model (plus variation). ex: 'gemini-1.5-pro'"""
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
  def organization_id(self) -> int:
    """The organization that published the model."""
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
  def owner_user_id(self) -> int:
    r"""
    The user that owns / created this model.
    Filled automatically while creating, can be updated later.
    """
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def license_id(self) -> int:
    """The license for this model."""
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def default_version_id(self) -> int:
    r"""
    The default version to use for this model.
    Filled automatically while creating, can be updated later.
    """
    return self._default_version_id or 0

  @default_version_id.setter
  def default_version_id(self, default_version_id: Optional[int]):
    if default_version_id is None:
      del self.default_version_id
      return
    if not isinstance(default_version_id, int):
      raise TypeError('default_version_id must be of type int')
    self._default_version_id = default_version_id

  @property
  def version(self) -> Optional['BenchmarkModelVersion']:
    r"""
    The version associated with this benchmark model.
    * CREATE : first version to be created with the parent benchmark model.
    * GET    : specified version or default if none was specified.
    * UPDATE : unused (use UpdateBenchmarkModelVersion).
    """
    return self._version or None

  @version.setter
  def version(self, version: Optional[Optional['BenchmarkModelVersion']]):
    if version is None:
      del self.version
      return
    if not isinstance(version, BenchmarkModelVersion):
      raise TypeError('version must be of type BenchmarkModelVersion')
    self._version = version

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization

  @organization.setter
  def organization(self, organization: Optional['OrganizationCard']):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def license(self) -> Optional['License']:
    """The associated License. Ignored on create and update."""
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def published(self) -> bool:
    """Whether the benchmark model is published (iff ContentStateId == PUBLISHED)."""
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published


class BenchmarkModelVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the benchmark model version.
    benchmark_model_id (int)
      The id of the parent benchmark model.
    slug (str)
      The slug of the model version. ex: 'gemini-1.5-pro-001'
      Required for CREATE, can be updated later.
    external_url (str)
      An external link to a resource explaining the model version. ex: blog post,
      aistudio, etc.
    knowledge_cutoff (datetime)
      A cutoff date for training data for the model.
    is_default (bool)
      Whether this BenchmarkModelVersion is the default for the parent
      BenchmarkModel.
    published (bool)
      Whether the model version is published (iff ContentStateId == PUBLISHED and
      parent benchmark model has ContentStateId == PUBLISHED).
    allow_model_proxy (bool)
      Whether this BenchmarkModelVersion is supported by model proxy.
    model_proxy_slug (str)
      The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
      Only set when `allow_model_proxy` is true.
    display_name (str)
    description (str)
    organization (OrganizationCard)
      Fields from the model for convenience
    name (str)
    license (License)
    importance_level (BenchmarkModelImportanceLevel)
      Whether this model version is run on Kaggle-maintained benchmarks
    input_modalities (Modality)
      Input modalities supported by this model version.
    output_modalities (Modality)
      Output modalities supported by this model version.
    deprecation_time (datetime)
      Timestamp when this model version was deprecated. A future value indicates
      a scheduled deprecation. Null/unset means not deprecated.
    benchmark_model_slug (str)
      The slug of the parent benchmark model. ex: 'gemini-1.5-pro'. Distinct from
      `slug` above, which identifies the version.
    supports_reasoning_effort (bool)
      Whether the model takes a reasoning effort. Its configs must pin one
      unless this is false. Unset reads as true.
    release_date (datetime)
      When the vendor released this model version. Distinct from the row's
      CreateTime (Kaggle onboarding), which lags by weeks to months for
      third-party and open-weight models. Unset when unknown.
  """

  def __init__(self):
    self._id = 0
    self._benchmark_model_id = 0
    self._slug = ""
    self._external_url = None
    self._knowledge_cutoff = None
    self._is_default = False
    self._published = False
    self._allow_model_proxy = False
    self._model_proxy_slug = None
    self._display_name = None
    self._description = None
    self._organization = None
    self._name = None
    self._license = None
    self._importance_level = None
    self._input_modalities = []
    self._output_modalities = []
    self._deprecation_time = None
    self._benchmark_model_slug = None
    self._supports_reasoning_effort = None
    self._release_date = None
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the benchmark model version."""
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
  def benchmark_model_id(self) -> int:
    """The id of the parent benchmark model."""
    return self._benchmark_model_id

  @benchmark_model_id.setter
  def benchmark_model_id(self, benchmark_model_id: int):
    if benchmark_model_id is None:
      del self.benchmark_model_id
      return
    if not isinstance(benchmark_model_id, int):
      raise TypeError('benchmark_model_id must be of type int')
    self._benchmark_model_id = benchmark_model_id

  @property
  def slug(self) -> str:
    r"""
    The slug of the model version. ex: 'gemini-1.5-pro-001'
    Required for CREATE, can be updated later.
    """
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
  def external_url(self) -> str:
    r"""
    An external link to a resource explaining the model version. ex: blog post,
    aistudio, etc.
    """
    return self._external_url or ""

  @external_url.setter
  def external_url(self, external_url: Optional[str]):
    if external_url is None:
      del self.external_url
      return
    if not isinstance(external_url, str):
      raise TypeError('external_url must be of type str')
    self._external_url = external_url

  @property
  def knowledge_cutoff(self) -> datetime:
    """A cutoff date for training data for the model."""
    return self._knowledge_cutoff or None

  @knowledge_cutoff.setter
  def knowledge_cutoff(self, knowledge_cutoff: Optional[datetime]):
    if knowledge_cutoff is None:
      del self.knowledge_cutoff
      return
    if not isinstance(knowledge_cutoff, datetime):
      raise TypeError('knowledge_cutoff must be of type datetime')
    self._knowledge_cutoff = knowledge_cutoff

  @property
  def is_default(self) -> bool:
    r"""
    Whether this BenchmarkModelVersion is the default for the parent
    BenchmarkModel.
    """
    return self._is_default

  @is_default.setter
  def is_default(self, is_default: bool):
    if is_default is None:
      del self.is_default
      return
    if not isinstance(is_default, bool):
      raise TypeError('is_default must be of type bool')
    self._is_default = is_default

  @property
  def published(self) -> bool:
    r"""
    Whether the model version is published (iff ContentStateId == PUBLISHED and
    parent benchmark model has ContentStateId == PUBLISHED).
    """
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def allow_model_proxy(self) -> bool:
    """Whether this BenchmarkModelVersion is supported by model proxy."""
    return self._allow_model_proxy

  @allow_model_proxy.setter
  def allow_model_proxy(self, allow_model_proxy: bool):
    if allow_model_proxy is None:
      del self.allow_model_proxy
      return
    if not isinstance(allow_model_proxy, bool):
      raise TypeError('allow_model_proxy must be of type bool')
    self._allow_model_proxy = allow_model_proxy

  @property
  def model_proxy_slug(self) -> str:
    r"""
    The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
    Only set when `allow_model_proxy` is true.
    """
    return self._model_proxy_slug or ""

  @model_proxy_slug.setter
  def model_proxy_slug(self, model_proxy_slug: Optional[str]):
    if model_proxy_slug is None:
      del self.model_proxy_slug
      return
    if not isinstance(model_proxy_slug, str):
      raise TypeError('model_proxy_slug must be of type str')
    self._model_proxy_slug = model_proxy_slug

  @property
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def name(self) -> str:
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
  def organization(self) -> Optional['OrganizationCard']:
    """Fields from the model for convenience"""
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
  def license(self) -> Optional['License']:
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def importance_level(self) -> 'BenchmarkModelImportanceLevel':
    """Whether this model version is run on Kaggle-maintained benchmarks"""
    return self._importance_level or BenchmarkModelImportanceLevel.BENCHMARK_MODEL_IMPORTANCE_LEVEL_UNSPECIFIED

  @importance_level.setter
  def importance_level(self, importance_level: Optional['BenchmarkModelImportanceLevel']):
    if importance_level is None:
      del self.importance_level
      return
    if not isinstance(importance_level, BenchmarkModelImportanceLevel):
      raise TypeError('importance_level must be of type BenchmarkModelImportanceLevel')
    self._importance_level = importance_level

  @property
  def input_modalities(self) -> Optional[List['Modality']]:
    """Input modalities supported by this model version."""
    return self._input_modalities

  @input_modalities.setter
  def input_modalities(self, input_modalities: Optional[List['Modality']]):
    if input_modalities is None:
      del self.input_modalities
      return
    if not isinstance(input_modalities, list):
      raise TypeError('input_modalities must be of type list')
    if not all([isinstance(t, Modality) for t in input_modalities]):
      raise TypeError('input_modalities must contain only items of type Modality')
    self._input_modalities = input_modalities

  @property
  def output_modalities(self) -> Optional[List['Modality']]:
    """Output modalities supported by this model version."""
    return self._output_modalities

  @output_modalities.setter
  def output_modalities(self, output_modalities: Optional[List['Modality']]):
    if output_modalities is None:
      del self.output_modalities
      return
    if not isinstance(output_modalities, list):
      raise TypeError('output_modalities must be of type list')
    if not all([isinstance(t, Modality) for t in output_modalities]):
      raise TypeError('output_modalities must contain only items of type Modality')
    self._output_modalities = output_modalities

  @property
  def deprecation_time(self) -> datetime:
    r"""
    Timestamp when this model version was deprecated. A future value indicates
    a scheduled deprecation. Null/unset means not deprecated.
    """
    return self._deprecation_time or None

  @deprecation_time.setter
  def deprecation_time(self, deprecation_time: Optional[datetime]):
    if deprecation_time is None:
      del self.deprecation_time
      return
    if not isinstance(deprecation_time, datetime):
      raise TypeError('deprecation_time must be of type datetime')
    self._deprecation_time = deprecation_time

  @property
  def benchmark_model_slug(self) -> str:
    r"""
    The slug of the parent benchmark model. ex: 'gemini-1.5-pro'. Distinct from
    `slug` above, which identifies the version.
    """
    return self._benchmark_model_slug or ""

  @benchmark_model_slug.setter
  def benchmark_model_slug(self, benchmark_model_slug: Optional[str]):
    if benchmark_model_slug is None:
      del self.benchmark_model_slug
      return
    if not isinstance(benchmark_model_slug, str):
      raise TypeError('benchmark_model_slug must be of type str')
    self._benchmark_model_slug = benchmark_model_slug

  @property
  def supports_reasoning_effort(self) -> bool:
    r"""
    Whether the model takes a reasoning effort. Its configs must pin one
    unless this is false. Unset reads as true.
    """
    return self._supports_reasoning_effort or False

  @supports_reasoning_effort.setter
  def supports_reasoning_effort(self, supports_reasoning_effort: Optional[bool]):
    if supports_reasoning_effort is None:
      del self.supports_reasoning_effort
      return
    if not isinstance(supports_reasoning_effort, bool):
      raise TypeError('supports_reasoning_effort must be of type bool')
    self._supports_reasoning_effort = supports_reasoning_effort

  @property
  def release_date(self) -> datetime:
    r"""
    When the vendor released this model version. Distinct from the row's
    CreateTime (Kaggle onboarding), which lags by weeks to months for
    third-party and open-weight models. Unset when unknown.
    """
    return self._release_date or None

  @release_date.setter
  def release_date(self, release_date: Optional[datetime]):
    if release_date is None:
      del self.release_date
      return
    if not isinstance(release_date, datetime):
      raise TypeError('release_date must be of type datetime')
    self._release_date = release_date


class BenchmarkResult(KaggleObject):
  r"""
  TODO(bml): Integrate this proto with personal benchmarks trials.
  Represents the outcome of a benchmark run. All fields are immutable.

  Attributes:
    numeric_result (NumericResult)
    boolean_result (bool)
    custom_additional_results (CustomResult)
      Generic additional results. These are rendered generically on the frontend:
    numeric_result_private (NumericResult)
      Numeric result on the private set of the benchmark version.
    numeric_result_public (NumericResult)
      Numeric result on the public set of the benchmark version.
    evaluation_date (datetime)
      The date on which evaluation was performed.
    task_version_id (int)
      Convenience fields for this result (for the frontend):
  """

  def __init__(self):
    self._numeric_result = None
    self._boolean_result = None
    self._custom_additional_results = []
    self._numeric_result_private = None
    self._numeric_result_public = None
    self._evaluation_date = None
    self._task_version_id = None
    self._freeze()

  @property
  def task_version_id(self) -> int:
    """Convenience fields for this result (for the frontend):"""
    return self._task_version_id or 0

  @task_version_id.setter
  def task_version_id(self, task_version_id: Optional[int]):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def numeric_result(self) -> Optional['NumericResult']:
    return self._numeric_result or None

  @numeric_result.setter
  def numeric_result(self, numeric_result: Optional['NumericResult']):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, NumericResult):
      raise TypeError('numeric_result must be of type NumericResult')
    del self.boolean_result
    self._numeric_result = numeric_result

  @property
  def boolean_result(self) -> bool:
    return self._boolean_result or False

  @boolean_result.setter
  def boolean_result(self, boolean_result: bool):
    if boolean_result is None:
      del self.boolean_result
      return
    if not isinstance(boolean_result, bool):
      raise TypeError('boolean_result must be of type bool')
    del self.numeric_result
    self._boolean_result = boolean_result

  @property
  def custom_additional_results(self) -> Optional[List[Optional['CustomResult']]]:
    """Generic additional results. These are rendered generically on the frontend:"""
    return self._custom_additional_results

  @custom_additional_results.setter
  def custom_additional_results(self, custom_additional_results: Optional[List[Optional['CustomResult']]]):
    if custom_additional_results is None:
      del self.custom_additional_results
      return
    if not isinstance(custom_additional_results, list):
      raise TypeError('custom_additional_results must be of type list')
    if not all([isinstance(t, CustomResult) for t in custom_additional_results]):
      raise TypeError('custom_additional_results must contain only items of type CustomResult')
    self._custom_additional_results = custom_additional_results

  @property
  def numeric_result_private(self) -> Optional['NumericResult']:
    """Numeric result on the private set of the benchmark version."""
    return self._numeric_result_private or None

  @numeric_result_private.setter
  def numeric_result_private(self, numeric_result_private: Optional[Optional['NumericResult']]):
    if numeric_result_private is None:
      del self.numeric_result_private
      return
    if not isinstance(numeric_result_private, NumericResult):
      raise TypeError('numeric_result_private must be of type NumericResult')
    self._numeric_result_private = numeric_result_private

  @property
  def numeric_result_public(self) -> Optional['NumericResult']:
    """Numeric result on the public set of the benchmark version."""
    return self._numeric_result_public or None

  @numeric_result_public.setter
  def numeric_result_public(self, numeric_result_public: Optional[Optional['NumericResult']]):
    if numeric_result_public is None:
      del self.numeric_result_public
      return
    if not isinstance(numeric_result_public, NumericResult):
      raise TypeError('numeric_result_public must be of type NumericResult')
    self._numeric_result_public = numeric_result_public

  @property
  def evaluation_date(self) -> datetime:
    """The date on which evaluation was performed."""
    return self._evaluation_date or None

  @evaluation_date.setter
  def evaluation_date(self, evaluation_date: Optional[datetime]):
    if evaluation_date is None:
      del self.evaluation_date
      return
    if not isinstance(evaluation_date, datetime):
      raise TypeError('evaluation_date must be of type datetime')
    self._evaluation_date = evaluation_date


class BenchmarkSchedulerSettings(KaggleObject):
  r"""
  Global settings for the benchmark task-run scheduler, stored in a single
  row (Id = 1). The concurrency caps count Running runs that went through the
  queue; synchronously started runs don't count.

  Attributes:
    enabled (bool)
      Kill switch. When false, the drain dispatches nothing and runs stay Queued.
    max_concurrency (int)
      Fleet-wide cap on Running runs. Unset = unbounded.
    max_concurrency_per_candidate_model (int)
      Cap on Running runs per candidate model version. Unset = unbounded.
    max_kickoffs_per_tick (int)
      Max runs one drain tick may dispatch. Unset = unbounded, though Model
      Proxy's batch limit also applies when reservations are enabled.
    dispatch_concurrency (int)
      How many dispatches a tick runs concurrently. Unset = the drain's default;
      values below 1 are treated as 1.
    pool_batch_size (int)
      How many Queued runs a tick fetches to consider. Unset = the drain's
      default; values below 1 are treated as 1.
    stale_queued_ttl_hours (int)
      How long a run may sit Queued before the stale-GC cron errors it out,
      measured from its enqueue time. Unset = skip the Queued sweep entirely.
    stale_running_ttl_hours (int)
      How long a run may sit Running before the stale-GC cron cancels its session
      and errors it out, measured from its start time. Set this above the longest
      legitimate task phase timeout or the sweep will kill healthy long-running
      work. Unset = skip the Running sweep entirely.
    reservations_enabled (bool)
      Whether the drain reserves Model Proxy capacity before starting each run.
    max_retries (int)
      How many cron-driven re-queues a task version + candidate may accumulate,
      not counting the original attempt. It does not bound the drain's in-place
      requeue of a transient dispatch failure, which leaves the count alone.
      Unset, or 0, disables retries entirely -- this is the retry kill-switch.
    retry_cooldown_minutes (int)
      How long a failed run must sit before the retry cron will re-queue it,
      measured from its end time. Unset = no cooldown, so a failure is eligible
      on the next tick.
    max_retries_per_tick (int)
      Upper bound on how many runs a single retry tick may re-queue. Like
      dispatch_concurrency, unset is not 'unbounded' but 'use the cron's
      built-in default'.
    screening_enabled (bool)
      Whether the drain asks Model Proxy which models have capacity before
      admitting runs. Turn off during a screening outage, which otherwise defers
      every run. Optional because it defaults to on, so a client that omits it
      doesn't disable it.
    global_min_model_proxy_priority (float)
      Minimum priority value sent to Model Proxy for every run. 0.0 is most
      urgent, so this caps how urgent a run can be. Unset = no floor.
  """

  def __init__(self):
    self._enabled = False
    self._max_concurrency = None
    self._max_concurrency_per_candidate_model = None
    self._max_kickoffs_per_tick = None
    self._dispatch_concurrency = None
    self._pool_batch_size = None
    self._stale_queued_ttl_hours = None
    self._stale_running_ttl_hours = None
    self._reservations_enabled = False
    self._max_retries = None
    self._retry_cooldown_minutes = None
    self._max_retries_per_tick = None
    self._screening_enabled = None
    self._global_min_model_proxy_priority = None
    self._freeze()

  @property
  def enabled(self) -> bool:
    """Kill switch. When false, the drain dispatches nothing and runs stay Queued."""
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled

  @property
  def max_concurrency(self) -> int:
    """Fleet-wide cap on Running runs. Unset = unbounded."""
    return self._max_concurrency or 0

  @max_concurrency.setter
  def max_concurrency(self, max_concurrency: Optional[int]):
    if max_concurrency is None:
      del self.max_concurrency
      return
    if not isinstance(max_concurrency, int):
      raise TypeError('max_concurrency must be of type int')
    self._max_concurrency = max_concurrency

  @property
  def max_concurrency_per_candidate_model(self) -> int:
    """Cap on Running runs per candidate model version. Unset = unbounded."""
    return self._max_concurrency_per_candidate_model or 0

  @max_concurrency_per_candidate_model.setter
  def max_concurrency_per_candidate_model(self, max_concurrency_per_candidate_model: Optional[int]):
    if max_concurrency_per_candidate_model is None:
      del self.max_concurrency_per_candidate_model
      return
    if not isinstance(max_concurrency_per_candidate_model, int):
      raise TypeError('max_concurrency_per_candidate_model must be of type int')
    self._max_concurrency_per_candidate_model = max_concurrency_per_candidate_model

  @property
  def max_kickoffs_per_tick(self) -> int:
    r"""
    Max runs one drain tick may dispatch. Unset = unbounded, though Model
    Proxy's batch limit also applies when reservations are enabled.
    """
    return self._max_kickoffs_per_tick or 0

  @max_kickoffs_per_tick.setter
  def max_kickoffs_per_tick(self, max_kickoffs_per_tick: Optional[int]):
    if max_kickoffs_per_tick is None:
      del self.max_kickoffs_per_tick
      return
    if not isinstance(max_kickoffs_per_tick, int):
      raise TypeError('max_kickoffs_per_tick must be of type int')
    self._max_kickoffs_per_tick = max_kickoffs_per_tick

  @property
  def dispatch_concurrency(self) -> int:
    r"""
    How many dispatches a tick runs concurrently. Unset = the drain's default;
    values below 1 are treated as 1.
    """
    return self._dispatch_concurrency or 0

  @dispatch_concurrency.setter
  def dispatch_concurrency(self, dispatch_concurrency: Optional[int]):
    if dispatch_concurrency is None:
      del self.dispatch_concurrency
      return
    if not isinstance(dispatch_concurrency, int):
      raise TypeError('dispatch_concurrency must be of type int')
    self._dispatch_concurrency = dispatch_concurrency

  @property
  def pool_batch_size(self) -> int:
    r"""
    How many Queued runs a tick fetches to consider. Unset = the drain's
    default; values below 1 are treated as 1.
    """
    return self._pool_batch_size or 0

  @pool_batch_size.setter
  def pool_batch_size(self, pool_batch_size: Optional[int]):
    if pool_batch_size is None:
      del self.pool_batch_size
      return
    if not isinstance(pool_batch_size, int):
      raise TypeError('pool_batch_size must be of type int')
    self._pool_batch_size = pool_batch_size

  @property
  def stale_queued_ttl_hours(self) -> int:
    r"""
    How long a run may sit Queued before the stale-GC cron errors it out,
    measured from its enqueue time. Unset = skip the Queued sweep entirely.
    """
    return self._stale_queued_ttl_hours or 0

  @stale_queued_ttl_hours.setter
  def stale_queued_ttl_hours(self, stale_queued_ttl_hours: Optional[int]):
    if stale_queued_ttl_hours is None:
      del self.stale_queued_ttl_hours
      return
    if not isinstance(stale_queued_ttl_hours, int):
      raise TypeError('stale_queued_ttl_hours must be of type int')
    self._stale_queued_ttl_hours = stale_queued_ttl_hours

  @property
  def stale_running_ttl_hours(self) -> int:
    r"""
    How long a run may sit Running before the stale-GC cron cancels its session
    and errors it out, measured from its start time. Set this above the longest
    legitimate task phase timeout or the sweep will kill healthy long-running
    work. Unset = skip the Running sweep entirely.
    """
    return self._stale_running_ttl_hours or 0

  @stale_running_ttl_hours.setter
  def stale_running_ttl_hours(self, stale_running_ttl_hours: Optional[int]):
    if stale_running_ttl_hours is None:
      del self.stale_running_ttl_hours
      return
    if not isinstance(stale_running_ttl_hours, int):
      raise TypeError('stale_running_ttl_hours must be of type int')
    self._stale_running_ttl_hours = stale_running_ttl_hours

  @property
  def reservations_enabled(self) -> bool:
    """Whether the drain reserves Model Proxy capacity before starting each run."""
    return self._reservations_enabled

  @reservations_enabled.setter
  def reservations_enabled(self, reservations_enabled: bool):
    if reservations_enabled is None:
      del self.reservations_enabled
      return
    if not isinstance(reservations_enabled, bool):
      raise TypeError('reservations_enabled must be of type bool')
    self._reservations_enabled = reservations_enabled

  @property
  def max_retries(self) -> int:
    r"""
    How many cron-driven re-queues a task version + candidate may accumulate,
    not counting the original attempt. It does not bound the drain's in-place
    requeue of a transient dispatch failure, which leaves the count alone.
    Unset, or 0, disables retries entirely -- this is the retry kill-switch.
    """
    return self._max_retries or 0

  @max_retries.setter
  def max_retries(self, max_retries: Optional[int]):
    if max_retries is None:
      del self.max_retries
      return
    if not isinstance(max_retries, int):
      raise TypeError('max_retries must be of type int')
    self._max_retries = max_retries

  @property
  def retry_cooldown_minutes(self) -> int:
    r"""
    How long a failed run must sit before the retry cron will re-queue it,
    measured from its end time. Unset = no cooldown, so a failure is eligible
    on the next tick.
    """
    return self._retry_cooldown_minutes or 0

  @retry_cooldown_minutes.setter
  def retry_cooldown_minutes(self, retry_cooldown_minutes: Optional[int]):
    if retry_cooldown_minutes is None:
      del self.retry_cooldown_minutes
      return
    if not isinstance(retry_cooldown_minutes, int):
      raise TypeError('retry_cooldown_minutes must be of type int')
    self._retry_cooldown_minutes = retry_cooldown_minutes

  @property
  def max_retries_per_tick(self) -> int:
    r"""
    Upper bound on how many runs a single retry tick may re-queue. Like
    dispatch_concurrency, unset is not 'unbounded' but 'use the cron's
    built-in default'.
    """
    return self._max_retries_per_tick or 0

  @max_retries_per_tick.setter
  def max_retries_per_tick(self, max_retries_per_tick: Optional[int]):
    if max_retries_per_tick is None:
      del self.max_retries_per_tick
      return
    if not isinstance(max_retries_per_tick, int):
      raise TypeError('max_retries_per_tick must be of type int')
    self._max_retries_per_tick = max_retries_per_tick

  @property
  def screening_enabled(self) -> bool:
    r"""
    Whether the drain asks Model Proxy which models have capacity before
    admitting runs. Turn off during a screening outage, which otherwise defers
    every run. Optional because it defaults to on, so a client that omits it
    doesn't disable it.
    """
    return self._screening_enabled or False

  @screening_enabled.setter
  def screening_enabled(self, screening_enabled: Optional[bool]):
    if screening_enabled is None:
      del self.screening_enabled
      return
    if not isinstance(screening_enabled, bool):
      raise TypeError('screening_enabled must be of type bool')
    self._screening_enabled = screening_enabled

  @property
  def global_min_model_proxy_priority(self) -> float:
    r"""
    Minimum priority value sent to Model Proxy for every run. 0.0 is most
    urgent, so this caps how urgent a run can be. Unset = no floor.
    """
    return self._global_min_model_proxy_priority or 0.0

  @global_min_model_proxy_priority.setter
  def global_min_model_proxy_priority(self, global_min_model_proxy_priority: Optional[float]):
    if global_min_model_proxy_priority is None:
      del self.global_min_model_proxy_priority
      return
    if not isinstance(global_min_model_proxy_priority, float):
      raise TypeError('global_min_model_proxy_priority must be of type float')
    self._global_min_model_proxy_priority = global_min_model_proxy_priority


class BenchmarkTaskDefinition(KaggleObject):
  r"""
  Attributes:
    notebook (BenchmarkTaskNotebookDefinition)
    docker_image (BenchmarkTaskDockerImageDefinition)
    harbor_kaggle_datasets (BenchmarkTaskKaggleDatasetsDefinition)
  """

  def __init__(self):
    self._notebook = None
    self._docker_image = None
    self._harbor_kaggle_datasets = None
    self._freeze()

  @property
  def notebook(self) -> Optional['BenchmarkTaskNotebookDefinition']:
    return self._notebook or None

  @notebook.setter
  def notebook(self, notebook: Optional['BenchmarkTaskNotebookDefinition']):
    if notebook is None:
      del self.notebook
      return
    if not isinstance(notebook, BenchmarkTaskNotebookDefinition):
      raise TypeError('notebook must be of type BenchmarkTaskNotebookDefinition')
    del self.docker_image
    del self.harbor_kaggle_datasets
    self._notebook = notebook

  @property
  def docker_image(self) -> Optional['BenchmarkTaskDockerImageDefinition']:
    return self._docker_image or None

  @docker_image.setter
  def docker_image(self, docker_image: Optional['BenchmarkTaskDockerImageDefinition']):
    if docker_image is None:
      del self.docker_image
      return
    if not isinstance(docker_image, BenchmarkTaskDockerImageDefinition):
      raise TypeError('docker_image must be of type BenchmarkTaskDockerImageDefinition')
    del self.notebook
    del self.harbor_kaggle_datasets
    self._docker_image = docker_image

  @property
  def harbor_kaggle_datasets(self) -> Optional['BenchmarkTaskKaggleDatasetsDefinition']:
    return self._harbor_kaggle_datasets or None

  @harbor_kaggle_datasets.setter
  def harbor_kaggle_datasets(self, harbor_kaggle_datasets: Optional['BenchmarkTaskKaggleDatasetsDefinition']):
    if harbor_kaggle_datasets is None:
      del self.harbor_kaggle_datasets
      return
    if not isinstance(harbor_kaggle_datasets, BenchmarkTaskKaggleDatasetsDefinition):
      raise TypeError('harbor_kaggle_datasets must be of type BenchmarkTaskKaggleDatasetsDefinition')
    del self.notebook
    del self.docker_image
    self._harbor_kaggle_datasets = harbor_kaggle_datasets


class BenchmarkTaskDockerImageDefinition(KaggleObject):
  r"""
  User-supplied Docker image task definition.

  Attributes:
    docker_image_url (str)
      Required. Full image ref (e.g. gcr.io/project/image:tag).
    description (str)
      Required on new tasks; ignored on version bumps (existing description
      carries over). Task description.
    title (str)
      Optional. Display name for the task. Defaults to the slug when omitted.
      Ignored on version bumps.
    env_variables (EnvVariable)
      Optional. Environment variables set on the container.
    secrets (UserSecret)
      Optional. Create/update UserSecrets inline before running.
    nested_virtualization_required (bool)
      Optional. Run the container with nested virtualization enabled — set
      when the image needs to launch VMs (e.g. QEMU/KVM guests) inside its
      sandbox. Ignored unless the caller has the
      BENCHMARKS_ALLOW_NESTED_VIRTUALIZATION feature flag.
    default_model_version_slug (str)
      Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default').
    default_agent_slug (str)
      Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high').
    auxiliary_model_version_config_slugs (str)
      Optional. Canonical BenchmarkModelVersionConfig.slugs the task invokes
      beyond the candidate (e.g. LLM judges), recorded so the scheduler can
      account for their model-proxy demand. Slugs rather than ids because this
      type is the public API input shape; the BenchmarkTasksApi handler resolves
      them to the internal auxiliary_model_version_config_ids.
    default_model_version_config_slug (str)
      Canonical BenchmarkModelVersionConfig.slug (e.g.
      'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
      the reasoning effort.
  """

  def __init__(self):
    self._docker_image_url = ""
    self._description = None
    self._title = None
    self._env_variables = []
    self._secrets = []
    self._nested_virtualization_required = False
    self._default_model_version_slug = None
    self._default_agent_slug = None
    self._auxiliary_model_version_config_slugs = []
    self._default_model_version_config_slug = None
    self._freeze()

  @property
  def docker_image_url(self) -> str:
    """Required. Full image ref (e.g. gcr.io/project/image:tag)."""
    return self._docker_image_url

  @docker_image_url.setter
  def docker_image_url(self, docker_image_url: str):
    if docker_image_url is None:
      del self.docker_image_url
      return
    if not isinstance(docker_image_url, str):
      raise TypeError('docker_image_url must be of type str')
    self._docker_image_url = docker_image_url

  @property
  def description(self) -> str:
    r"""
    Required on new tasks; ignored on version bumps (existing description
    carries over). Task description.
    """
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def title(self) -> str:
    r"""
    Optional. Display name for the task. Defaults to the slug when omitted.
    Ignored on version bumps.
    """
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def env_variables(self) -> Optional[List[Optional['EnvVariable']]]:
    """Optional. Environment variables set on the container."""
    return self._env_variables

  @env_variables.setter
  def env_variables(self, env_variables: Optional[List[Optional['EnvVariable']]]):
    if env_variables is None:
      del self.env_variables
      return
    if not isinstance(env_variables, list):
      raise TypeError('env_variables must be of type list')
    if not all([isinstance(t, EnvVariable) for t in env_variables]):
      raise TypeError('env_variables must contain only items of type EnvVariable')
    self._env_variables = env_variables

  @property
  def secrets(self) -> Optional[List[Optional['UserSecret']]]:
    """Optional. Create/update UserSecrets inline before running."""
    return self._secrets

  @secrets.setter
  def secrets(self, secrets: Optional[List[Optional['UserSecret']]]):
    if secrets is None:
      del self.secrets
      return
    if not isinstance(secrets, list):
      raise TypeError('secrets must be of type list')
    if not all([isinstance(t, UserSecret) for t in secrets]):
      raise TypeError('secrets must contain only items of type UserSecret')
    self._secrets = secrets

  @property
  def nested_virtualization_required(self) -> bool:
    r"""
    Optional. Run the container with nested virtualization enabled — set
    when the image needs to launch VMs (e.g. QEMU/KVM guests) inside its
    sandbox. Ignored unless the caller has the
    BENCHMARKS_ALLOW_NESTED_VIRTUALIZATION feature flag.
    """
    return self._nested_virtualization_required

  @nested_virtualization_required.setter
  def nested_virtualization_required(self, nested_virtualization_required: bool):
    if nested_virtualization_required is None:
      del self.nested_virtualization_required
      return
    if not isinstance(nested_virtualization_required, bool):
      raise TypeError('nested_virtualization_required must be of type bool')
    self._nested_virtualization_required = nested_virtualization_required

  @property
  def default_model_version_slug(self) -> str:
    """Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default')."""
    return self._default_model_version_slug or ""

  @default_model_version_slug.setter
  def default_model_version_slug(self, default_model_version_slug: str):
    if default_model_version_slug is None:
      del self.default_model_version_slug
      return
    if not isinstance(default_model_version_slug, str):
      raise TypeError('default_model_version_slug must be of type str')
    del self.default_agent_slug
    del self.default_model_version_config_slug
    self._default_model_version_slug = default_model_version_slug

  @property
  def default_agent_slug(self) -> str:
    """Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high')."""
    return self._default_agent_slug or ""

  @default_agent_slug.setter
  def default_agent_slug(self, default_agent_slug: str):
    if default_agent_slug is None:
      del self.default_agent_slug
      return
    if not isinstance(default_agent_slug, str):
      raise TypeError('default_agent_slug must be of type str')
    del self.default_model_version_slug
    del self.default_model_version_config_slug
    self._default_agent_slug = default_agent_slug

  @property
  def default_model_version_config_slug(self) -> str:
    r"""
    Canonical BenchmarkModelVersionConfig.slug (e.g.
    'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
    the reasoning effort.
    """
    return self._default_model_version_config_slug or ""

  @default_model_version_config_slug.setter
  def default_model_version_config_slug(self, default_model_version_config_slug: str):
    if default_model_version_config_slug is None:
      del self.default_model_version_config_slug
      return
    if not isinstance(default_model_version_config_slug, str):
      raise TypeError('default_model_version_config_slug must be of type str')
    del self.default_model_version_slug
    del self.default_agent_slug
    self._default_model_version_config_slug = default_model_version_config_slug

  @property
  def auxiliary_model_version_config_slugs(self) -> Optional[List[str]]:
    r"""
    Optional. Canonical BenchmarkModelVersionConfig.slugs the task invokes
    beyond the candidate (e.g. LLM judges), recorded so the scheduler can
    account for their model-proxy demand. Slugs rather than ids because this
    type is the public API input shape; the BenchmarkTasksApi handler resolves
    them to the internal auxiliary_model_version_config_ids.
    """
    return self._auxiliary_model_version_config_slugs

  @auxiliary_model_version_config_slugs.setter
  def auxiliary_model_version_config_slugs(self, auxiliary_model_version_config_slugs: Optional[List[str]]):
    if auxiliary_model_version_config_slugs is None:
      del self.auxiliary_model_version_config_slugs
      return
    if not isinstance(auxiliary_model_version_config_slugs, list):
      raise TypeError('auxiliary_model_version_config_slugs must be of type list')
    if not all([isinstance(t, str) for t in auxiliary_model_version_config_slugs]):
      raise TypeError('auxiliary_model_version_config_slugs must contain only items of type str')
    self._auxiliary_model_version_config_slugs = auxiliary_model_version_config_slugs


class BenchmarkTaskKaggleDatasetsDefinition(KaggleObject):
  r"""
  Task definition and asset mounts for a Harbor task whose definition and data
  live in mounted Kaggle datasets instead of a git clone. Dataset references
  are pinned to an immutable version for reproducibility.

  Attributes:
    definition_source (DefinitionSource)
    mounts (DatasetMount)
    env_variables (EnvVariable)
      Optional. Environment variables to expose to the Harbor session container.
      Keys the executor injects itself — the task-definition path, the agent
      pin, and the model-proxy variables — are rejected with InvalidArgument.
    secrets (UserSecret)
      Optional. Create/update UserSecrets inline before running.
    override_harness_version_slug (str)
      HarnessVersion.slug (e.g. 'claude-code-2.1.216'). Slug rather than id
      because this type is the public API input shape; the BenchmarkTasksApi
      handler resolves it to the internal override_harness_version_id.
    default_model_version_slug (str)
      Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default').
      Requires override_harness_version: without one the task evaluates
      agents, so pick the model via default_agent_slug instead.
    default_agent_slug (str)
      Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high').
    override_harness_version_custom_slug (str)
      Passed directly to the Harbor run command's --agent flag.
    auxiliary_model_version_config_slugs (str)
      Optional. Canonical BenchmarkModelVersionConfig.slugs the task invokes
      beyond the candidate (e.g. LLM judges), recorded so the scheduler can
      account for their model-proxy demand. Slugs rather than ids because this
      type is the public API input shape; the BenchmarkTasksApi handler resolves
      them to the internal auxiliary_model_version_config_ids.
    nested_virtualization_required (bool)
      Optional. Run the Harbor executor container with nested virtualization
      enabled — set when the task needs to launch VMs (e.g. QEMU/KVM guests)
      inside its sandbox. Ignored unless the caller has the
      BENCHMARKS_ALLOW_NESTED_VIRTUALIZATION feature flag.
    n_attempts (int)
      Optional. How many times the task is run per invocation, mapped to the
      Harbor run's n_attempts (used to compute metrics like pass@K). Defaults to
      1 when omitted.
    metrics (HarborMetricType)
      Optional. Canonical Harbor metrics the task version declares to reduce its
      attempts into aggregate values, supplied to Harbor's JobConfig.Metrics when
      the task is invoked. Duplicates are collapsed. When omitted, Harbor
      defaults to mean.
    session_concurrency (int)
      Optional. Maximum number of the task version's attempts run concurrently
      across VMs when n_attempts > 1. Defaults to 1 (serial) when omitted.
      Rejected with PERMISSION_DENIED unless the caller has the
      BENCHMARKS_ATTEMPTS_ACROSS_VMS feature flag.
    default_model_version_config_slug (str)
      Canonical BenchmarkModelVersionConfig.slug (e.g.
      'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
      the reasoning effort. Requires override_harness_version.
  """

  def __init__(self):
    self._definition_source = None
    self._mounts = []
    self._env_variables = []
    self._secrets = []
    self._override_harness_version_slug = None
    self._default_model_version_slug = None
    self._default_agent_slug = None
    self._override_harness_version_custom_slug = None
    self._auxiliary_model_version_config_slugs = []
    self._nested_virtualization_required = False
    self._n_attempts = None
    self._metrics = []
    self._session_concurrency = None
    self._default_model_version_config_slug = None
    self._freeze()

  @property
  def definition_source(self) -> Optional['DefinitionSource']:
    return self._definition_source

  @definition_source.setter
  def definition_source(self, definition_source: Optional['DefinitionSource']):
    if definition_source is None:
      del self.definition_source
      return
    if not isinstance(definition_source, DefinitionSource):
      raise TypeError('definition_source must be of type DefinitionSource')
    self._definition_source = definition_source

  @property
  def mounts(self) -> Optional[List[Optional['DatasetMount']]]:
    return self._mounts

  @mounts.setter
  def mounts(self, mounts: Optional[List[Optional['DatasetMount']]]):
    if mounts is None:
      del self.mounts
      return
    if not isinstance(mounts, list):
      raise TypeError('mounts must be of type list')
    if not all([isinstance(t, DatasetMount) for t in mounts]):
      raise TypeError('mounts must contain only items of type DatasetMount')
    self._mounts = mounts

  @property
  def env_variables(self) -> Optional[List[Optional['EnvVariable']]]:
    r"""
    Optional. Environment variables to expose to the Harbor session container.
    Keys the executor injects itself — the task-definition path, the agent
    pin, and the model-proxy variables — are rejected with InvalidArgument.
    """
    return self._env_variables

  @env_variables.setter
  def env_variables(self, env_variables: Optional[List[Optional['EnvVariable']]]):
    if env_variables is None:
      del self.env_variables
      return
    if not isinstance(env_variables, list):
      raise TypeError('env_variables must be of type list')
    if not all([isinstance(t, EnvVariable) for t in env_variables]):
      raise TypeError('env_variables must contain only items of type EnvVariable')
    self._env_variables = env_variables

  @property
  def secrets(self) -> Optional[List[Optional['UserSecret']]]:
    """Optional. Create/update UserSecrets inline before running."""
    return self._secrets

  @secrets.setter
  def secrets(self, secrets: Optional[List[Optional['UserSecret']]]):
    if secrets is None:
      del self.secrets
      return
    if not isinstance(secrets, list):
      raise TypeError('secrets must be of type list')
    if not all([isinstance(t, UserSecret) for t in secrets]):
      raise TypeError('secrets must contain only items of type UserSecret')
    self._secrets = secrets

  @property
  def override_harness_version_slug(self) -> str:
    r"""
    HarnessVersion.slug (e.g. 'claude-code-2.1.216'). Slug rather than id
    because this type is the public API input shape; the BenchmarkTasksApi
    handler resolves it to the internal override_harness_version_id.
    """
    return self._override_harness_version_slug or ""

  @override_harness_version_slug.setter
  def override_harness_version_slug(self, override_harness_version_slug: str):
    if override_harness_version_slug is None:
      del self.override_harness_version_slug
      return
    if not isinstance(override_harness_version_slug, str):
      raise TypeError('override_harness_version_slug must be of type str')
    del self.override_harness_version_custom_slug
    self._override_harness_version_slug = override_harness_version_slug

  @property
  def override_harness_version_custom_slug(self) -> str:
    """Passed directly to the Harbor run command's --agent flag."""
    return self._override_harness_version_custom_slug or ""

  @override_harness_version_custom_slug.setter
  def override_harness_version_custom_slug(self, override_harness_version_custom_slug: str):
    if override_harness_version_custom_slug is None:
      del self.override_harness_version_custom_slug
      return
    if not isinstance(override_harness_version_custom_slug, str):
      raise TypeError('override_harness_version_custom_slug must be of type str')
    del self.override_harness_version_slug
    self._override_harness_version_custom_slug = override_harness_version_custom_slug

  @property
  def default_model_version_slug(self) -> str:
    r"""
    Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default').
    Requires override_harness_version: without one the task evaluates
    agents, so pick the model via default_agent_slug instead.
    """
    return self._default_model_version_slug or ""

  @default_model_version_slug.setter
  def default_model_version_slug(self, default_model_version_slug: str):
    if default_model_version_slug is None:
      del self.default_model_version_slug
      return
    if not isinstance(default_model_version_slug, str):
      raise TypeError('default_model_version_slug must be of type str')
    del self.default_agent_slug
    del self.default_model_version_config_slug
    self._default_model_version_slug = default_model_version_slug

  @property
  def default_agent_slug(self) -> str:
    """Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high')."""
    return self._default_agent_slug or ""

  @default_agent_slug.setter
  def default_agent_slug(self, default_agent_slug: str):
    if default_agent_slug is None:
      del self.default_agent_slug
      return
    if not isinstance(default_agent_slug, str):
      raise TypeError('default_agent_slug must be of type str')
    del self.default_model_version_slug
    del self.default_model_version_config_slug
    self._default_agent_slug = default_agent_slug

  @property
  def default_model_version_config_slug(self) -> str:
    r"""
    Canonical BenchmarkModelVersionConfig.slug (e.g.
    'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
    the reasoning effort. Requires override_harness_version.
    """
    return self._default_model_version_config_slug or ""

  @default_model_version_config_slug.setter
  def default_model_version_config_slug(self, default_model_version_config_slug: str):
    if default_model_version_config_slug is None:
      del self.default_model_version_config_slug
      return
    if not isinstance(default_model_version_config_slug, str):
      raise TypeError('default_model_version_config_slug must be of type str')
    del self.default_model_version_slug
    del self.default_agent_slug
    self._default_model_version_config_slug = default_model_version_config_slug

  @property
  def auxiliary_model_version_config_slugs(self) -> Optional[List[str]]:
    r"""
    Optional. Canonical BenchmarkModelVersionConfig.slugs the task invokes
    beyond the candidate (e.g. LLM judges), recorded so the scheduler can
    account for their model-proxy demand. Slugs rather than ids because this
    type is the public API input shape; the BenchmarkTasksApi handler resolves
    them to the internal auxiliary_model_version_config_ids.
    """
    return self._auxiliary_model_version_config_slugs

  @auxiliary_model_version_config_slugs.setter
  def auxiliary_model_version_config_slugs(self, auxiliary_model_version_config_slugs: Optional[List[str]]):
    if auxiliary_model_version_config_slugs is None:
      del self.auxiliary_model_version_config_slugs
      return
    if not isinstance(auxiliary_model_version_config_slugs, list):
      raise TypeError('auxiliary_model_version_config_slugs must be of type list')
    if not all([isinstance(t, str) for t in auxiliary_model_version_config_slugs]):
      raise TypeError('auxiliary_model_version_config_slugs must contain only items of type str')
    self._auxiliary_model_version_config_slugs = auxiliary_model_version_config_slugs

  @property
  def nested_virtualization_required(self) -> bool:
    r"""
    Optional. Run the Harbor executor container with nested virtualization
    enabled — set when the task needs to launch VMs (e.g. QEMU/KVM guests)
    inside its sandbox. Ignored unless the caller has the
    BENCHMARKS_ALLOW_NESTED_VIRTUALIZATION feature flag.
    """
    return self._nested_virtualization_required

  @nested_virtualization_required.setter
  def nested_virtualization_required(self, nested_virtualization_required: bool):
    if nested_virtualization_required is None:
      del self.nested_virtualization_required
      return
    if not isinstance(nested_virtualization_required, bool):
      raise TypeError('nested_virtualization_required must be of type bool')
    self._nested_virtualization_required = nested_virtualization_required

  @property
  def n_attempts(self) -> int:
    r"""
    Optional. How many times the task is run per invocation, mapped to the
    Harbor run's n_attempts (used to compute metrics like pass@K). Defaults to
    1 when omitted.
    """
    return self._n_attempts or 0

  @n_attempts.setter
  def n_attempts(self, n_attempts: Optional[int]):
    if n_attempts is None:
      del self.n_attempts
      return
    if not isinstance(n_attempts, int):
      raise TypeError('n_attempts must be of type int')
    self._n_attempts = n_attempts

  @property
  def metrics(self) -> Optional[List['HarborMetricType']]:
    r"""
    Optional. Canonical Harbor metrics the task version declares to reduce its
    attempts into aggregate values, supplied to Harbor's JobConfig.Metrics when
    the task is invoked. Duplicates are collapsed. When omitted, Harbor
    defaults to mean.
    """
    return self._metrics

  @metrics.setter
  def metrics(self, metrics: Optional[List['HarborMetricType']]):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, list):
      raise TypeError('metrics must be of type list')
    if not all([isinstance(t, HarborMetricType) for t in metrics]):
      raise TypeError('metrics must contain only items of type HarborMetricType')
    self._metrics = metrics

  @property
  def session_concurrency(self) -> int:
    r"""
    Optional. Maximum number of the task version's attempts run concurrently
    across VMs when n_attempts > 1. Defaults to 1 (serial) when omitted.
    Rejected with PERMISSION_DENIED unless the caller has the
    BENCHMARKS_ATTEMPTS_ACROSS_VMS feature flag.
    """
    return self._session_concurrency or 0

  @session_concurrency.setter
  def session_concurrency(self, session_concurrency: Optional[int]):
    if session_concurrency is None:
      del self.session_concurrency
      return
    if not isinstance(session_concurrency, int):
      raise TypeError('session_concurrency must be of type int')
    self._session_concurrency = session_concurrency


class BenchmarkTaskNotebookDefinition(KaggleObject):
  r"""
  TODO(bml): Get parity with text + options fields in the create request proto

  """

  pass

class BenchmarkTaskOptions(KaggleObject):
  r"""
  Options persisted on a BenchmarkTaskVersion. Currently only carries
  data-source attachments; more fields (model/competition/kernel sources,
  compute knobs) will be added incrementally, so field numbers 2-20 are
  reserved. Defined here (rather than under the API surface) because the
  type is shared between the SDK read shape and the public API proto.

  Attributes:
    dataset_data_sources (str)
      Dataset data sources attached to the underlying notebook. Each entry is
      '{owner}/{dataset-slug}'. The latest published version of the dataset is
      attached; pinning to a specific version ('owner/dataset/versions/N') is
      not yet supported.
  """

  def __init__(self):
    self._dataset_data_sources = []
    self._freeze()

  @property
  def dataset_data_sources(self) -> Optional[List[str]]:
    r"""
    Dataset data sources attached to the underlying notebook. Each entry is
    '{owner}/{dataset-slug}'. The latest published version of the dataset is
    attached; pinning to a specific version ('owner/dataset/versions/N') is
    not yet supported.
    """
    return self._dataset_data_sources

  @dataset_data_sources.setter
  def dataset_data_sources(self, dataset_data_sources: Optional[List[str]]):
    if dataset_data_sources is None:
      del self.dataset_data_sources
      return
    if not isinstance(dataset_data_sources, list):
      raise TypeError('dataset_data_sources must be of type list')
    if not all([isinstance(t, str) for t in dataset_data_sources]):
      raise TypeError('dataset_data_sources must contain only items of type str')
    self._dataset_data_sources = dataset_data_sources


class CustomResult(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (str)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
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
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class DatasetMount(KaggleObject):
  r"""
  A Kaggle dataset mounted as an asset for a Harbor task, pinned to an
  immutable version for reproducibility.

  Attributes:
    dataset_version_slug (str)
      'owner/slug/versions/N' — the version segment is REQUIRED for
      reproducibility. Requests without an explicit version are rejected.
    mount_path (str)
      Absolute path inside the container where the dataset is mounted. Callers
      pick this so tasks can locate their data anywhere. Unique across the
      mount list; must not shadow the task-definition mount.
  """

  def __init__(self):
    self._dataset_version_slug = ""
    self._mount_path = ""
    self._freeze()

  @property
  def dataset_version_slug(self) -> str:
    r"""
    'owner/slug/versions/N' — the version segment is REQUIRED for
    reproducibility. Requests without an explicit version are rejected.
    """
    return self._dataset_version_slug

  @dataset_version_slug.setter
  def dataset_version_slug(self, dataset_version_slug: str):
    if dataset_version_slug is None:
      del self.dataset_version_slug
      return
    if not isinstance(dataset_version_slug, str):
      raise TypeError('dataset_version_slug must be of type str')
    self._dataset_version_slug = dataset_version_slug

  @property
  def mount_path(self) -> str:
    r"""
    Absolute path inside the container where the dataset is mounted. Callers
    pick this so tasks can locate their data anywhere. Unique across the
    mount list; must not shadow the task-definition mount.
    """
    return self._mount_path

  @mount_path.setter
  def mount_path(self, mount_path: str):
    if mount_path is None:
      del self.mount_path
      return
    if not isinstance(mount_path, str):
      raise TypeError('mount_path must be of type str')
    self._mount_path = mount_path


class DefinitionSource(KaggleObject):
  r"""
  Task-definition dataset for a Harbor task whose definition lives in a mounted
  Kaggle dataset. Pinned to an immutable version for reproducibility.

  Attributes:
    dataset_version_slug (str)
      'owner/slug/versions/N' — the version segment is REQUIRED for
      reproducibility. Requests without an explicit version are rejected.
    sub_path (str)
      Sub-directory within the dataset containing task.toml. Empty means the
      dataset root.
  """

  def __init__(self):
    self._dataset_version_slug = ""
    self._sub_path = ""
    self._freeze()

  @property
  def dataset_version_slug(self) -> str:
    r"""
    'owner/slug/versions/N' — the version segment is REQUIRED for
    reproducibility. Requests without an explicit version are rejected.
    """
    return self._dataset_version_slug

  @dataset_version_slug.setter
  def dataset_version_slug(self, dataset_version_slug: str):
    if dataset_version_slug is None:
      del self.dataset_version_slug
      return
    if not isinstance(dataset_version_slug, str):
      raise TypeError('dataset_version_slug must be of type str')
    self._dataset_version_slug = dataset_version_slug

  @property
  def sub_path(self) -> str:
    r"""
    Sub-directory within the dataset containing task.toml. Empty means the
    dataset root.
    """
    return self._sub_path

  @sub_path.setter
  def sub_path(self, sub_path: str):
    if sub_path is None:
      del self.sub_path
      return
    if not isinstance(sub_path, str):
      raise TypeError('sub_path must be of type str')
    self._sub_path = sub_path


class EnvVariable(KaggleObject):
  r"""
  Environment variable on a container-backed BenchmarkTask.

    - `key`: variable name (e.g. `API_BASE_URL`).
    - `value`: literal value, OR (when `is_secret_name` is true) a secret
      name.
    - `is_secret_name`: when true, the system resolves `value` at runtime
      against the running user's UserSecrets and injects the resolved
      secret.

  Attributes:
    key (str)
    value (str)
    is_secret_name (bool)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
    self._is_secret_name = False
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
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

  @property
  def is_secret_name(self) -> bool:
    return self._is_secret_name

  @is_secret_name.setter
  def is_secret_name(self, is_secret_name: bool):
    if is_secret_name is None:
      del self.is_secret_name
      return
    if not isinstance(is_secret_name, bool):
      raise TypeError('is_secret_name must be of type bool')
    self._is_secret_name = is_secret_name


class NumericResult(KaggleObject):
  r"""
  Attributes:
    value (float)
      The largest double marks an Elo with no finite value, for a model that has
      never lost or tied (see BenchmarksConstants.UndefeatedScore).
    confidence_interval (float)
      Note, while we call this the 'confidence interval' - the value we store
      here is actually the 'confidence radius', it should always be displayed
      as a +- value.
    uneven_confidence_interval (UnevenConfidenceInterval)
      For asymmetric confidence intervals in which the +/- values differ
      If set, prioritized over confidence_interval (if both are set)
    standard_deviation (float)
      Sample standard deviation across the attempts this result pooled. Kept
      alongside confidence_interval rather than derived from it: the interval is
      a radius already scaled by a critical value, so recovering the spread would
      mean knowing which multiplier produced it. Aggregations that combine
      children into a single interval need the spread itself.
  """

  def __init__(self):
    self._value = 0.0
    self._confidence_interval = None
    self._uneven_confidence_interval = None
    self._standard_deviation = None
    self._freeze()

  @property
  def value(self) -> float:
    r"""
    The largest double marks an Elo with no finite value, for a model that has
    never lost or tied (see BenchmarksConstants.UndefeatedScore).
    """
    return self._value

  @value.setter
  def value(self, value: float):
    if value is None:
      del self.value
      return
    if not isinstance(value, float):
      raise TypeError('value must be of type float')
    self._value = value

  @property
  def confidence_interval(self) -> float:
    r"""
    Note, while we call this the 'confidence interval' - the value we store
    here is actually the 'confidence radius', it should always be displayed
    as a +- value.
    """
    return self._confidence_interval or 0.0

  @confidence_interval.setter
  def confidence_interval(self, confidence_interval: Optional[float]):
    if confidence_interval is None:
      del self.confidence_interval
      return
    if not isinstance(confidence_interval, float):
      raise TypeError('confidence_interval must be of type float')
    self._confidence_interval = confidence_interval

  @property
  def uneven_confidence_interval(self) -> Optional['UnevenConfidenceInterval']:
    r"""
    For asymmetric confidence intervals in which the +/- values differ
    If set, prioritized over confidence_interval (if both are set)
    """
    return self._uneven_confidence_interval or None

  @uneven_confidence_interval.setter
  def uneven_confidence_interval(self, uneven_confidence_interval: Optional[Optional['UnevenConfidenceInterval']]):
    if uneven_confidence_interval is None:
      del self.uneven_confidence_interval
      return
    if not isinstance(uneven_confidence_interval, UnevenConfidenceInterval):
      raise TypeError('uneven_confidence_interval must be of type UnevenConfidenceInterval')
    self._uneven_confidence_interval = uneven_confidence_interval

  @property
  def standard_deviation(self) -> float:
    r"""
    Sample standard deviation across the attempts this result pooled. Kept
    alongside confidence_interval rather than derived from it: the interval is
    a radius already scaled by a critical value, so recovering the spread would
    mean knowing which multiplier produced it. Aggregations that combine
    children into a single interval need the spread itself.
    """
    return self._standard_deviation or 0.0

  @standard_deviation.setter
  def standard_deviation(self, standard_deviation: Optional[float]):
    if standard_deviation is None:
      del self.standard_deviation
      return
    if not isinstance(standard_deviation, float):
      raise TypeError('standard_deviation must be of type float')
    self._standard_deviation = standard_deviation


class UnevenConfidenceInterval(KaggleObject):
  r"""
  Attributes:
    plus (float)
    minus (float)
  """

  def __init__(self):
    self._plus = 0.0
    self._minus = 0.0
    self._freeze()

  @property
  def plus(self) -> float:
    return self._plus

  @plus.setter
  def plus(self, plus: float):
    if plus is None:
      del self.plus
      return
    if not isinstance(plus, float):
      raise TypeError('plus must be of type float')
    self._plus = plus

  @property
  def minus(self) -> float:
    return self._minus

  @minus.setter
  def minus(self, minus: float):
    if minus is None:
      del self.minus
      return
    if not isinstance(minus, float):
      raise TypeError('minus must be of type float')
    self._minus = minus


class UserSecret(KaggleObject):
  r"""
  UserSecret to create/update on the caller's account before running a
  container-backed BenchmarkTask.

    - `name`: secret label (matched against existing UserSecrets by Label).
    - `value`: plaintext secret value.
    - `override_existing`: when true, replace any existing secret with the
      same name. When false, fail with AlreadyExists on a name collision.

  Attributes:
    name (str)
    value (str)
    override_existing (bool)
  """

  def __init__(self):
    self._name = ""
    self._value = ""
    self._override_existing = False
    self._freeze()

  @property
  def name(self) -> str:
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
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

  @property
  def override_existing(self) -> bool:
    return self._override_existing

  @override_existing.setter
  def override_existing(self, override_existing: bool):
    if override_existing is None:
      del self.override_existing
      return
    if not isinstance(override_existing, bool):
      raise TypeError('override_existing must be of type bool')
    self._override_existing = override_existing


BenchmarkArenaCombination._fields = [
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("candidate", "candidate", "_candidate", BenchmarkCandidate, None, KaggleObjectSerializer()),
]

BenchmarkArenaSettings._fields = [
  FieldMetadata("artifactPath", "artifact_path", "_artifact_path", str, "", PredefinedSerializer()),
  FieldMetadata("artifactType", "artifact_type", "_artifact_type", BenchmarkArenaArtifactType, BenchmarkArenaArtifactType.BENCHMARK_ARENA_ARTIFACT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("revealCandidates", "reveal_candidates", "_reveal_candidates", bool, False, PredefinedSerializer()),
  FieldMetadata("votingEnabled", "voting_enabled", "_voting_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("galleryEnabled", "gallery_enabled", "_gallery_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("arenaTaskVersionId", "arena_task_version_id", "_arena_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("galleryCardSize", "gallery_card_size", "_gallery_card_size", BenchmarkGalleryCardSize, BenchmarkGalleryCardSize.BENCHMARK_GALLERY_CARD_SIZE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("expandArtifacts", "expand_artifacts", "_expand_artifacts", bool, False, PredefinedSerializer()),
]

BenchmarkCandidate._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentId", "agent_id", "_agent_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reasoningEffort", "reasoning_effort", "_reasoning_effort", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkModelVersionConfigId", "benchmark_model_version_config_id", "_benchmark_model_version_config_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkModel._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("defaultVersionId", "default_version_id", "_default_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("version", "version", "_version", BenchmarkModelVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
]

BenchmarkModelVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelId", "benchmark_model_id", "_benchmark_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("knowledgeCutoff", "knowledge_cutoff", "_knowledge_cutoff", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("isDefault", "is_default", "_is_default", bool, False, PredefinedSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
  FieldMetadata("allowModelProxy", "allow_model_proxy", "_allow_model_proxy", bool, False, PredefinedSerializer()),
  FieldMetadata("modelProxySlug", "model_proxy_slug", "_model_proxy_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("importanceLevel", "importance_level", "_importance_level", BenchmarkModelImportanceLevel, None, EnumSerializer(), optional=True),
  FieldMetadata("inputModalities", "input_modalities", "_input_modalities", Modality, [], ListSerializer(EnumSerializer())),
  FieldMetadata("outputModalities", "output_modalities", "_output_modalities", Modality, [], ListSerializer(EnumSerializer())),
  FieldMetadata("deprecationTime", "deprecation_time", "_deprecation_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("benchmarkModelSlug", "benchmark_model_slug", "_benchmark_model_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("supportsReasoningEffort", "supports_reasoning_effort", "_supports_reasoning_effort", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("releaseDate", "release_date", "_release_date", datetime, None, DateTimeSerializer(), optional=True),
]

BenchmarkResult._fields = [
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("customAdditionalResults", "custom_additional_results", "_custom_additional_results", CustomResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numericResultPrivate", "numeric_result_private", "_numeric_result_private", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericResultPublic", "numeric_result_public", "_numeric_result_public", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("evaluationDate", "evaluation_date", "_evaluation_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkSchedulerSettings._fields = [
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("maxConcurrency", "max_concurrency", "_max_concurrency", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxConcurrencyPerCandidateModel", "max_concurrency_per_candidate_model", "_max_concurrency_per_candidate_model", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxKickoffsPerTick", "max_kickoffs_per_tick", "_max_kickoffs_per_tick", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dispatchConcurrency", "dispatch_concurrency", "_dispatch_concurrency", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("poolBatchSize", "pool_batch_size", "_pool_batch_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("staleQueuedTtlHours", "stale_queued_ttl_hours", "_stale_queued_ttl_hours", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("staleRunningTtlHours", "stale_running_ttl_hours", "_stale_running_ttl_hours", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reservationsEnabled", "reservations_enabled", "_reservations_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("maxRetries", "max_retries", "_max_retries", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("retryCooldownMinutes", "retry_cooldown_minutes", "_retry_cooldown_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxRetriesPerTick", "max_retries_per_tick", "_max_retries_per_tick", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("screeningEnabled", "screening_enabled", "_screening_enabled", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("globalMinModelProxyPriority", "global_min_model_proxy_priority", "_global_min_model_proxy_priority", float, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskDefinition._fields = [
  FieldMetadata("notebook", "notebook", "_notebook", BenchmarkTaskNotebookDefinition, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("dockerImage", "docker_image", "_docker_image", BenchmarkTaskDockerImageDefinition, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("harborKaggleDatasets", "harbor_kaggle_datasets", "_harbor_kaggle_datasets", BenchmarkTaskKaggleDatasetsDefinition, None, KaggleObjectSerializer(), optional=True),
]

BenchmarkTaskDockerImageDefinition._fields = [
  FieldMetadata("dockerImageUrl", "docker_image_url", "_docker_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("envVariables", "env_variables", "_env_variables", EnvVariable, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("secrets", "secrets", "_secrets", UserSecret, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nestedVirtualizationRequired", "nested_virtualization_required", "_nested_virtualization_required", bool, False, PredefinedSerializer()),
  FieldMetadata("defaultModelVersionSlug", "default_model_version_slug", "_default_model_version_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultAgentSlug", "default_agent_slug", "_default_agent_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("auxiliaryModelVersionConfigSlugs", "auxiliary_model_version_config_slugs", "_auxiliary_model_version_config_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("defaultModelVersionConfigSlug", "default_model_version_config_slug", "_default_model_version_config_slug", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskKaggleDatasetsDefinition._fields = [
  FieldMetadata("definitionSource", "definition_source", "_definition_source", DefinitionSource, None, KaggleObjectSerializer()),
  FieldMetadata("mounts", "mounts", "_mounts", DatasetMount, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("envVariables", "env_variables", "_env_variables", EnvVariable, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("secrets", "secrets", "_secrets", UserSecret, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("overrideHarnessVersionSlug", "override_harness_version_slug", "_override_harness_version_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultModelVersionSlug", "default_model_version_slug", "_default_model_version_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultAgentSlug", "default_agent_slug", "_default_agent_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("overrideHarnessVersionCustomSlug", "override_harness_version_custom_slug", "_override_harness_version_custom_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("auxiliaryModelVersionConfigSlugs", "auxiliary_model_version_config_slugs", "_auxiliary_model_version_config_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("nestedVirtualizationRequired", "nested_virtualization_required", "_nested_virtualization_required", bool, False, PredefinedSerializer()),
  FieldMetadata("nAttempts", "n_attempts", "_n_attempts", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("metrics", "metrics", "_metrics", HarborMetricType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("sessionConcurrency", "session_concurrency", "_session_concurrency", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultModelVersionConfigSlug", "default_model_version_config_slug", "_default_model_version_config_slug", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskNotebookDefinition._fields = []

BenchmarkTaskOptions._fields = [
  FieldMetadata("datasetDataSources", "dataset_data_sources", "_dataset_data_sources", str, [], ListSerializer(PredefinedSerializer())),
]

CustomResult._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

DatasetMount._fields = [
  FieldMetadata("datasetVersionSlug", "dataset_version_slug", "_dataset_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("mountPath", "mount_path", "_mount_path", str, "", PredefinedSerializer()),
]

DefinitionSource._fields = [
  FieldMetadata("datasetVersionSlug", "dataset_version_slug", "_dataset_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("subPath", "sub_path", "_sub_path", str, "", PredefinedSerializer()),
]

EnvVariable._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
  FieldMetadata("isSecretName", "is_secret_name", "_is_secret_name", bool, False, PredefinedSerializer()),
]

NumericResult._fields = [
  FieldMetadata("value", "value", "_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("confidenceInterval", "confidence_interval", "_confidence_interval", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unevenConfidenceInterval", "uneven_confidence_interval", "_uneven_confidence_interval", UnevenConfidenceInterval, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("standardDeviation", "standard_deviation", "_standard_deviation", float, None, PredefinedSerializer(), optional=True),
]

UnevenConfidenceInterval._fields = [
  FieldMetadata("plus", "plus", "_plus", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minus", "minus", "_minus", float, 0.0, PredefinedSerializer()),
]

UserSecret._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
  FieldMetadata("overrideExisting", "override_existing", "_override_existing", bool, False, PredefinedSerializer()),
]

