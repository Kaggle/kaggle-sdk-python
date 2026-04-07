from datetime import datetime, timedelta
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.competitions.types.episode import EpisodeType
from kagglesdk.competitions.types.evaluation_algorithm import EnvironmentRenderType
from kagglesdk.datasets.databundles.types.databundle_types import DataSource, Directory, File
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import AcceleratorType, ColabNotebookSource, ColabSubscriptionTier, ColabVariant, DockerImagePinningType, DockerImageVersionDisabledReason, DockerImageVersionType, EditorType, ImportType, KernelSessionPackageState, KernelVersionPinningType, KernelVersionType, KernelWorkerStatus, Language, LegacyDataSourceType, ListColabSortType, PersistenceMode, ResourceReferenceType
from kagglesdk.kernels.types.kernels_events import KernelSessionInfo
from kagglesdk.kernels.types.kernels_types import CreationSource, DataSourceReference, KernelListItem, KernelSessionOutputFile, ListKernelIdsRequest, ResourceReference, ResourceReferenceIdentifier
from kagglesdk.models.types.model_enums import ModelFramework
from kagglesdk.tags.types.tag_service import TagList
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.user import User
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class ScheduleFrequencyType(enum.Enum):
  """How often to execute the notebook."""
  SCHEDULE_FREQUENCY_UNSPECIFIED = 0
  DAILY = 1
  WEEKLY = 2
  MONTHLY = 3

class ScheduleTriggerType(enum.Enum):
  """What triggers the schedule to be run."""
  SCHEDULE_TRIGGER_TYPE_UNSPECIFIED = 0
  SCHEDULED_TIME = 1
  DATASOURCE_UPDATE = 2

class AcceleratorSelection(enum.Enum):
  """Accelerator selection for the default session settings."""
  ACCELERATOR_UNSPECIFIED = 0
  GPU_ONCE = 1
  GPU_ALWAYS = 2
  TPU_ONCE = 3

class AcceleratorQuotaStatistics(KaggleObject):
  r"""
  Attributes:
    has_ever_run (bool)
    minimum_time_allowed (timedelta)
    time_reserved (timedelta)
    time_used (timedelta)
    total_time_allowed (timedelta)
    is_pay_to_scale_enabled (bool)
  """

  def __init__(self):
    self._has_ever_run = False
    self._minimum_time_allowed = None
    self._time_reserved = None
    self._time_used = None
    self._total_time_allowed = None
    self._is_pay_to_scale_enabled = False
    self._freeze()

  @property
  def has_ever_run(self) -> bool:
    return self._has_ever_run

  @has_ever_run.setter
  def has_ever_run(self, has_ever_run: bool):
    if has_ever_run is None:
      del self.has_ever_run
      return
    if not isinstance(has_ever_run, bool):
      raise TypeError('has_ever_run must be of type bool')
    self._has_ever_run = has_ever_run

  @property
  def minimum_time_allowed(self) -> timedelta:
    return self._minimum_time_allowed

  @minimum_time_allowed.setter
  def minimum_time_allowed(self, minimum_time_allowed: timedelta):
    if minimum_time_allowed is None:
      del self.minimum_time_allowed
      return
    if not isinstance(minimum_time_allowed, timedelta):
      raise TypeError('minimum_time_allowed must be of type timedelta')
    self._minimum_time_allowed = minimum_time_allowed

  @property
  def time_reserved(self) -> timedelta:
    return self._time_reserved

  @time_reserved.setter
  def time_reserved(self, time_reserved: timedelta):
    if time_reserved is None:
      del self.time_reserved
      return
    if not isinstance(time_reserved, timedelta):
      raise TypeError('time_reserved must be of type timedelta')
    self._time_reserved = time_reserved

  @property
  def time_used(self) -> timedelta:
    return self._time_used

  @time_used.setter
  def time_used(self, time_used: timedelta):
    if time_used is None:
      del self.time_used
      return
    if not isinstance(time_used, timedelta):
      raise TypeError('time_used must be of type timedelta')
    self._time_used = time_used

  @property
  def total_time_allowed(self) -> timedelta:
    return self._total_time_allowed

  @total_time_allowed.setter
  def total_time_allowed(self, total_time_allowed: timedelta):
    if total_time_allowed is None:
      del self.total_time_allowed
      return
    if not isinstance(total_time_allowed, timedelta):
      raise TypeError('total_time_allowed must be of type timedelta')
    self._total_time_allowed = total_time_allowed

  @property
  def is_pay_to_scale_enabled(self) -> bool:
    return self._is_pay_to_scale_enabled

  @is_pay_to_scale_enabled.setter
  def is_pay_to_scale_enabled(self, is_pay_to_scale_enabled: bool):
    if is_pay_to_scale_enabled is None:
      del self.is_pay_to_scale_enabled
      return
    if not isinstance(is_pay_to_scale_enabled, bool):
      raise TypeError('is_pay_to_scale_enabled must be of type bool')
    self._is_pay_to_scale_enabled = is_pay_to_scale_enabled


class AcceptKernelCompetitionRulesRequest(KaggleObject):
  r"""
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


class AddKernelCategoryRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    category_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._category_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def category_id(self) -> int:
    return self._category_id

  @category_id.setter
  def category_id(self, category_id: int):
    if category_id is None:
      del self.category_id
      return
    if not isinstance(category_id, int):
      raise TypeError('category_id must be of type int')
    self._category_id = category_id


class AgentEntry(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
    team_name (str)
  """

  def __init__(self):
    self._submission_id = 0
    self._team_name = None
    self._freeze()

  @property
  def submission_id(self) -> int:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: int):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def team_name(self) -> str:
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: Optional[str]):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name


class CancelKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    suppress_active_events (bool)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._suppress_active_events = None
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

  @property
  def suppress_active_events(self) -> bool:
    return self._suppress_active_events or False

  @suppress_active_events.setter
  def suppress_active_events(self, suppress_active_events: Optional[bool]):
    if suppress_active_events is None:
      del self.suppress_active_events
      return
    if not isinstance(suppress_active_events, bool):
      raise TypeError('suppress_active_events must be of type bool')
    self._suppress_active_events = suppress_active_events


class CheckNewerColabVersionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class CheckNewerColabVersionResponse(KaggleObject):
  r"""
  Attributes:
    has_newer_version (bool)
    last_modified_time (datetime)
  """

  def __init__(self):
    self._has_newer_version = False
    self._last_modified_time = None
    self._freeze()

  @property
  def has_newer_version(self) -> bool:
    return self._has_newer_version

  @has_newer_version.setter
  def has_newer_version(self, has_newer_version: bool):
    if has_newer_version is None:
      del self.has_newer_version
      return
    if not isinstance(has_newer_version, bool):
      raise TypeError('has_newer_version must be of type bool')
    self._has_newer_version = has_newer_version

  @property
  def last_modified_time(self) -> datetime:
    return self._last_modified_time or None

  @last_modified_time.setter
  def last_modified_time(self, last_modified_time: Optional[datetime]):
    if last_modified_time is None:
      del self.last_modified_time
      return
    if not isinstance(last_modified_time, datetime):
      raise TypeError('last_modified_time must be of type datetime')
    self._last_modified_time = last_modified_time


class CheckNewerGithubVersionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class CheckNewerGithubVersionResponse(KaggleObject):
  r"""
  Attributes:
    has_newer_version (bool)
  """

  def __init__(self):
    self._has_newer_version = False
    self._freeze()

  @property
  def has_newer_version(self) -> bool:
    return self._has_newer_version

  @has_newer_version.setter
  def has_newer_version(self, has_newer_version: bool):
    if has_newer_version is None:
      del self.has_newer_version
      return
    if not isinstance(has_newer_version, bool):
      raise TypeError('has_newer_version must be of type bool')
    self._has_newer_version = has_newer_version


class ClearPinnedKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class ColabSpec(KaggleObject):
  r"""
  Attributes:
    drive_id (str)
    is_public (bool)
    last_pull_time (datetime)
    last_ignore_nudge_time (datetime)
    default_save_version_type (KernelVersionType)
    file_name (str)
  """

  def __init__(self):
    self._drive_id = ""
    self._is_public = False
    self._last_pull_time = None
    self._last_ignore_nudge_time = None
    self._default_save_version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._file_name = None
    self._freeze()

  @property
  def drive_id(self) -> str:
    return self._drive_id

  @drive_id.setter
  def drive_id(self, drive_id: str):
    if drive_id is None:
      del self.drive_id
      return
    if not isinstance(drive_id, str):
      raise TypeError('drive_id must be of type str')
    self._drive_id = drive_id

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
  def last_pull_time(self) -> datetime:
    return self._last_pull_time

  @last_pull_time.setter
  def last_pull_time(self, last_pull_time: datetime):
    if last_pull_time is None:
      del self.last_pull_time
      return
    if not isinstance(last_pull_time, datetime):
      raise TypeError('last_pull_time must be of type datetime')
    self._last_pull_time = last_pull_time

  @property
  def last_ignore_nudge_time(self) -> datetime:
    return self._last_ignore_nudge_time or None

  @last_ignore_nudge_time.setter
  def last_ignore_nudge_time(self, last_ignore_nudge_time: Optional[datetime]):
    if last_ignore_nudge_time is None:
      del self.last_ignore_nudge_time
      return
    if not isinstance(last_ignore_nudge_time, datetime):
      raise TypeError('last_ignore_nudge_time must be of type datetime')
    self._last_ignore_nudge_time = last_ignore_nudge_time

  @property
  def default_save_version_type(self) -> 'KernelVersionType':
    return self._default_save_version_type

  @default_save_version_type.setter
  def default_save_version_type(self, default_save_version_type: 'KernelVersionType'):
    if default_save_version_type is None:
      del self.default_save_version_type
      return
    if not isinstance(default_save_version_type, KernelVersionType):
      raise TypeError('default_save_version_type must be of type KernelVersionType')
    self._default_save_version_type = default_save_version_type

  @property
  def file_name(self) -> str:
    return self._file_name or ""

  @file_name.setter
  def file_name(self, file_name: Optional[str]):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name


class CollaboratorItem(KaggleObject):
  r"""
  Attributes:
    author_user_name (str)
    author_display_name (str)
    thumbnail_image_url (str)
    score (float)
    author_tier (UserAchievementTier)
    database_id (int)
    url (str)
    progression_opt_out (bool)
      True if the user is opted out of the progression system.
  """

  def __init__(self):
    self._author_user_name = ""
    self._author_display_name = ""
    self._thumbnail_image_url = ""
    self._score = 0.0
    self._author_tier = None
    self._database_id = 0
    self._url = ""
    self._progression_opt_out = None
    self._freeze()

  @property
  def author_user_name(self) -> str:
    return self._author_user_name

  @author_user_name.setter
  def author_user_name(self, author_user_name: str):
    if author_user_name is None:
      del self.author_user_name
      return
    if not isinstance(author_user_name, str):
      raise TypeError('author_user_name must be of type str')
    self._author_user_name = author_user_name

  @property
  def author_display_name(self) -> str:
    return self._author_display_name

  @author_display_name.setter
  def author_display_name(self, author_display_name: str):
    if author_display_name is None:
      del self.author_display_name
      return
    if not isinstance(author_display_name, str):
      raise TypeError('author_display_name must be of type str')
    self._author_display_name = author_display_name

  @property
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: str):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

  @property
  def score(self) -> float:
    return self._score

  @score.setter
  def score(self, score: float):
    if score is None:
      del self.score
      return
    if not isinstance(score, float):
      raise TypeError('score must be of type float')
    self._score = score

  @property
  def author_tier(self) -> 'UserAchievementTier':
    return self._author_tier or UserAchievementTier.NOVICE

  @author_tier.setter
  def author_tier(self, author_tier: Optional['UserAchievementTier']):
    if author_tier is None:
      del self.author_tier
      return
    if not isinstance(author_tier, UserAchievementTier):
      raise TypeError('author_tier must be of type UserAchievementTier')
    self._author_tier = author_tier

  @property
  def database_id(self) -> int:
    return self._database_id

  @database_id.setter
  def database_id(self, database_id: int):
    if database_id is None:
      del self.database_id
      return
    if not isinstance(database_id, int):
      raise TypeError('database_id must be of type int')
    self._database_id = database_id

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def progression_opt_out(self) -> bool:
    """True if the user is opted out of the progression system."""
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out


class CommitAndRunRequest(KaggleObject):
  r"""
  Attributes:
    data_sources (DataSourceReference)
    fork_parent_script_version_id (int)
    is_language_template (bool)
    new_text (str)
    new_title (str)
    script_id (int)
    script_language_name (str)
    docker_image_version_id (int)
    editor_type (EditorType)
    docker_image_tag (str)
    worker_pool_name (str)
    sequence (int)
    compute (ComputeState)
    kernel_version_id (int)
    version_name (str)
    version_type (KernelVersionType)
    submission_requested_details (SubmissionRequestedDetails)
    executed_by_schedule_id (int)
    github_save_request (GitHubSaveRequest)
    is_import (bool)
    external_source_data (ExternalSourceData)
    github_spec (GithubSpec)
    colab_spec (ColabSpec)
    from_kernel_import_worker (bool)
    priority (int)
      Sets the execution priority of this KernelSession request when queued,
      lower is better (10 will get run before 100). Only used if in the
      KERNELS_ALLOW_SET_PRIORITY flag, otherwise ignored.
    is_one_time_accelerator (bool)
      By default, the accelerator will be used for this session and all future
      sessions. If is_one_time_accelerator is true, the accelerator will only be
      used for this session.
    benchmark_task_version_id (int)
      If set, the session will be created with a BenchmarkTaskVersionScaffold
      creation source using this ID. Requires the PersonalBenchmark tag.
  """

  def __init__(self):
    self._data_sources = []
    self._fork_parent_script_version_id = None
    self._is_language_template = None
    self._new_text = None
    self._new_title = None
    self._script_id = 0
    self._script_language_name = None
    self._docker_image_version_id = None
    self._editor_type = None
    self._docker_image_tag = None
    self._worker_pool_name = None
    self._sequence = None
    self._compute = None
    self._kernel_version_id = None
    self._version_name = None
    self._version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._submission_requested_details = None
    self._executed_by_schedule_id = None
    self._github_save_request = None
    self._is_import = None
    self._external_source_data = None
    self._github_spec = None
    self._colab_spec = None
    self._from_kernel_import_worker = None
    self._priority = None
    self._is_one_time_accelerator = None
    self._benchmark_task_version_id = None
    self._freeze()

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def fork_parent_script_version_id(self) -> int:
    return self._fork_parent_script_version_id or 0

  @fork_parent_script_version_id.setter
  def fork_parent_script_version_id(self, fork_parent_script_version_id: Optional[int]):
    if fork_parent_script_version_id is None:
      del self.fork_parent_script_version_id
      return
    if not isinstance(fork_parent_script_version_id, int):
      raise TypeError('fork_parent_script_version_id must be of type int')
    self._fork_parent_script_version_id = fork_parent_script_version_id

  @property
  def is_language_template(self) -> bool:
    return self._is_language_template or False

  @is_language_template.setter
  def is_language_template(self, is_language_template: Optional[bool]):
    if is_language_template is None:
      del self.is_language_template
      return
    if not isinstance(is_language_template, bool):
      raise TypeError('is_language_template must be of type bool')
    self._is_language_template = is_language_template

  @property
  def new_text(self) -> str:
    return self._new_text or ""

  @new_text.setter
  def new_text(self, new_text: Optional[str]):
    if new_text is None:
      del self.new_text
      return
    if not isinstance(new_text, str):
      raise TypeError('new_text must be of type str')
    self._new_text = new_text

  @property
  def new_title(self) -> str:
    return self._new_title or ""

  @new_title.setter
  def new_title(self, new_title: Optional[str]):
    if new_title is None:
      del self.new_title
      return
    if not isinstance(new_title, str):
      raise TypeError('new_title must be of type str')
    self._new_title = new_title

  @property
  def script_id(self) -> int:
    return self._script_id

  @script_id.setter
  def script_id(self, script_id: int):
    if script_id is None:
      del self.script_id
      return
    if not isinstance(script_id, int):
      raise TypeError('script_id must be of type int')
    self._script_id = script_id

  @property
  def script_language_name(self) -> str:
    return self._script_language_name or ""

  @script_language_name.setter
  def script_language_name(self, script_language_name: Optional[str]):
    if script_language_name is None:
      del self.script_language_name
      return
    if not isinstance(script_language_name, str):
      raise TypeError('script_language_name must be of type str')
    self._script_language_name = script_language_name

  @property
  def docker_image_version_id(self) -> int:
    return self._docker_image_version_id or 0

  @docker_image_version_id.setter
  def docker_image_version_id(self, docker_image_version_id: Optional[int]):
    if docker_image_version_id is None:
      del self.docker_image_version_id
      return
    if not isinstance(docker_image_version_id, int):
      raise TypeError('docker_image_version_id must be of type int')
    self._docker_image_version_id = docker_image_version_id

  @property
  def editor_type(self) -> 'EditorType':
    return self._editor_type or EditorType.EDITOR_TYPE_UNSPECIFIED

  @editor_type.setter
  def editor_type(self, editor_type: Optional['EditorType']):
    if editor_type is None:
      del self.editor_type
      return
    if not isinstance(editor_type, EditorType):
      raise TypeError('editor_type must be of type EditorType')
    self._editor_type = editor_type

  @property
  def docker_image_tag(self) -> str:
    return self._docker_image_tag or ""

  @docker_image_tag.setter
  def docker_image_tag(self, docker_image_tag: Optional[str]):
    if docker_image_tag is None:
      del self.docker_image_tag
      return
    if not isinstance(docker_image_tag, str):
      raise TypeError('docker_image_tag must be of type str')
    self._docker_image_tag = docker_image_tag

  @property
  def worker_pool_name(self) -> str:
    return self._worker_pool_name or ""

  @worker_pool_name.setter
  def worker_pool_name(self, worker_pool_name: Optional[str]):
    if worker_pool_name is None:
      del self.worker_pool_name
      return
    if not isinstance(worker_pool_name, str):
      raise TypeError('worker_pool_name must be of type str')
    self._worker_pool_name = worker_pool_name

  @property
  def sequence(self) -> int:
    return self._sequence or 0

  @sequence.setter
  def sequence(self, sequence: Optional[int]):
    if sequence is None:
      del self.sequence
      return
    if not isinstance(sequence, int):
      raise TypeError('sequence must be of type int')
    self._sequence = sequence

  @property
  def compute(self) -> Optional['ComputeState']:
    return self._compute

  @compute.setter
  def compute(self, compute: Optional['ComputeState']):
    if compute is None:
      del self.compute
      return
    if not isinstance(compute, ComputeState):
      raise TypeError('compute must be of type ComputeState')
    self._compute = compute

  @property
  def kernel_version_id(self) -> int:
    return self._kernel_version_id or 0

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: Optional[int]):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def version_name(self) -> str:
    return self._version_name or ""

  @version_name.setter
  def version_name(self, version_name: Optional[str]):
    if version_name is None:
      del self.version_name
      return
    if not isinstance(version_name, str):
      raise TypeError('version_name must be of type str')
    self._version_name = version_name

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type

  @version_type.setter
  def version_type(self, version_type: 'KernelVersionType'):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type

  @property
  def submission_requested_details(self) -> Optional['SubmissionRequestedDetails']:
    return self._submission_requested_details

  @submission_requested_details.setter
  def submission_requested_details(self, submission_requested_details: Optional['SubmissionRequestedDetails']):
    if submission_requested_details is None:
      del self.submission_requested_details
      return
    if not isinstance(submission_requested_details, SubmissionRequestedDetails):
      raise TypeError('submission_requested_details must be of type SubmissionRequestedDetails')
    self._submission_requested_details = submission_requested_details

  @property
  def executed_by_schedule_id(self) -> int:
    return self._executed_by_schedule_id or 0

  @executed_by_schedule_id.setter
  def executed_by_schedule_id(self, executed_by_schedule_id: Optional[int]):
    if executed_by_schedule_id is None:
      del self.executed_by_schedule_id
      return
    if not isinstance(executed_by_schedule_id, int):
      raise TypeError('executed_by_schedule_id must be of type int')
    self._executed_by_schedule_id = executed_by_schedule_id

  @property
  def github_save_request(self) -> Optional['GitHubSaveRequest']:
    return self._github_save_request

  @github_save_request.setter
  def github_save_request(self, github_save_request: Optional['GitHubSaveRequest']):
    if github_save_request is None:
      del self.github_save_request
      return
    if not isinstance(github_save_request, GitHubSaveRequest):
      raise TypeError('github_save_request must be of type GitHubSaveRequest')
    self._github_save_request = github_save_request

  @property
  def is_import(self) -> bool:
    return self._is_import or False

  @is_import.setter
  def is_import(self, is_import: Optional[bool]):
    if is_import is None:
      del self.is_import
      return
    if not isinstance(is_import, bool):
      raise TypeError('is_import must be of type bool')
    self._is_import = is_import

  @property
  def external_source_data(self) -> Optional['ExternalSourceData']:
    return self._external_source_data or None

  @external_source_data.setter
  def external_source_data(self, external_source_data: Optional[Optional['ExternalSourceData']]):
    if external_source_data is None:
      del self.external_source_data
      return
    if not isinstance(external_source_data, ExternalSourceData):
      raise TypeError('external_source_data must be of type ExternalSourceData')
    self._external_source_data = external_source_data

  @property
  def github_spec(self) -> Optional['GithubSpec']:
    return self._github_spec or None

  @github_spec.setter
  def github_spec(self, github_spec: Optional[Optional['GithubSpec']]):
    if github_spec is None:
      del self.github_spec
      return
    if not isinstance(github_spec, GithubSpec):
      raise TypeError('github_spec must be of type GithubSpec')
    self._github_spec = github_spec

  @property
  def colab_spec(self) -> Optional['ColabSpec']:
    return self._colab_spec or None

  @colab_spec.setter
  def colab_spec(self, colab_spec: Optional[Optional['ColabSpec']]):
    if colab_spec is None:
      del self.colab_spec
      return
    if not isinstance(colab_spec, ColabSpec):
      raise TypeError('colab_spec must be of type ColabSpec')
    self._colab_spec = colab_spec

  @property
  def from_kernel_import_worker(self) -> bool:
    return self._from_kernel_import_worker or False

  @from_kernel_import_worker.setter
  def from_kernel_import_worker(self, from_kernel_import_worker: Optional[bool]):
    if from_kernel_import_worker is None:
      del self.from_kernel_import_worker
      return
    if not isinstance(from_kernel_import_worker, bool):
      raise TypeError('from_kernel_import_worker must be of type bool')
    self._from_kernel_import_worker = from_kernel_import_worker

  @property
  def priority(self) -> int:
    r"""
    Sets the execution priority of this KernelSession request when queued,
    lower is better (10 will get run before 100). Only used if in the
    KERNELS_ALLOW_SET_PRIORITY flag, otherwise ignored.
    """
    return self._priority or 0

  @priority.setter
  def priority(self, priority: Optional[int]):
    if priority is None:
      del self.priority
      return
    if not isinstance(priority, int):
      raise TypeError('priority must be of type int')
    self._priority = priority

  @property
  def is_one_time_accelerator(self) -> bool:
    r"""
    By default, the accelerator will be used for this session and all future
    sessions. If is_one_time_accelerator is true, the accelerator will only be
    used for this session.
    """
    return self._is_one_time_accelerator or False

  @is_one_time_accelerator.setter
  def is_one_time_accelerator(self, is_one_time_accelerator: Optional[bool]):
    if is_one_time_accelerator is None:
      del self.is_one_time_accelerator
      return
    if not isinstance(is_one_time_accelerator, bool):
      raise TypeError('is_one_time_accelerator must be of type bool')
    self._is_one_time_accelerator = is_one_time_accelerator

  @property
  def benchmark_task_version_id(self) -> int:
    r"""
    If set, the session will be created with a BenchmarkTaskVersionScaffold
    creation source using this ID. Requires the PersonalBenchmark tag.
    """
    return self._benchmark_task_version_id or 0

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: Optional[int]):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id


class CommitAndRunResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
    submit_redirect_url (str)
      [Deprecated] - no callers require this.
      optional string new_url = 2;
    sequence (int)
    parent_kernel_version_id (int)
    diff (KernelDiff)
    kernel_id (int)
    kernel_version_id (int)
    kernel_run_id (int)
    version_number (int)
    status (KernelWorkerStatus)
    blob_upload_url (str)
  """

  def __init__(self):
    self._message = None
    self._submit_redirect_url = None
    self._sequence = None
    self._parent_kernel_version_id = None
    self._diff = None
    self._kernel_id = 0
    self._kernel_version_id = 0
    self._kernel_run_id = 0
    self._version_number = None
    self._status = KernelWorkerStatus.QUEUED
    self._blob_upload_url = None
    self._freeze()

  @property
  def message(self) -> str:
    return self._message or ""

  @message.setter
  def message(self, message: Optional[str]):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def submit_redirect_url(self) -> str:
    r"""
    [Deprecated] - no callers require this.
    optional string new_url = 2;
    """
    return self._submit_redirect_url or ""

  @submit_redirect_url.setter
  def submit_redirect_url(self, submit_redirect_url: Optional[str]):
    if submit_redirect_url is None:
      del self.submit_redirect_url
      return
    if not isinstance(submit_redirect_url, str):
      raise TypeError('submit_redirect_url must be of type str')
    self._submit_redirect_url = submit_redirect_url

  @property
  def sequence(self) -> int:
    return self._sequence or 0

  @sequence.setter
  def sequence(self, sequence: Optional[int]):
    if sequence is None:
      del self.sequence
      return
    if not isinstance(sequence, int):
      raise TypeError('sequence must be of type int')
    self._sequence = sequence

  @property
  def parent_kernel_version_id(self) -> int:
    return self._parent_kernel_version_id or 0

  @parent_kernel_version_id.setter
  def parent_kernel_version_id(self, parent_kernel_version_id: Optional[int]):
    if parent_kernel_version_id is None:
      del self.parent_kernel_version_id
      return
    if not isinstance(parent_kernel_version_id, int):
      raise TypeError('parent_kernel_version_id must be of type int')
    self._parent_kernel_version_id = parent_kernel_version_id

  @property
  def diff(self) -> Optional['KernelDiff']:
    return self._diff

  @diff.setter
  def diff(self, diff: Optional['KernelDiff']):
    if diff is None:
      del self.diff
      return
    if not isinstance(diff, KernelDiff):
      raise TypeError('diff must be of type KernelDiff')
    self._diff = diff

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def kernel_version_id(self) -> int:
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def kernel_run_id(self) -> int:
    return self._kernel_run_id

  @kernel_run_id.setter
  def kernel_run_id(self, kernel_run_id: int):
    if kernel_run_id is None:
      del self.kernel_run_id
      return
    if not isinstance(kernel_run_id, int):
      raise TypeError('kernel_run_id must be of type int')
    self._kernel_run_id = kernel_run_id

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def status(self) -> 'KernelWorkerStatus':
    return self._status

  @status.setter
  def status(self, status: 'KernelWorkerStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, KernelWorkerStatus):
      raise TypeError('status must be of type KernelWorkerStatus')
    self._status = status

  @property
  def blob_upload_url(self) -> str:
    return self._blob_upload_url or ""

  @blob_upload_url.setter
  def blob_upload_url(self, blob_upload_url: Optional[str]):
    if blob_upload_url is None:
      del self.blob_upload_url
      return
    if not isinstance(blob_upload_url, str):
      raise TypeError('blob_upload_url must be of type str')
    self._blob_upload_url = blob_upload_url


class CompleteQuickSessionRequest(KaggleObject):
  r"""
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


class CompleteQuickSessionResponse(KaggleObject):
  r"""
  Attributes:
    error_message (str)
  """

  def __init__(self):
    self._error_message = None
    self._freeze()

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class ComputeConstraintState(KaggleObject):
  r"""
  Attributes:
    session_timeout_seconds (int)
    max_cpu_cores (int)
    max_storage_bytes (int)
    max_memory_bytes (int)
    disallow_internet (bool)
  """

  def __init__(self):
    self._session_timeout_seconds = None
    self._max_cpu_cores = None
    self._max_storage_bytes = None
    self._max_memory_bytes = None
    self._disallow_internet = None
    self._freeze()

  @property
  def session_timeout_seconds(self) -> int:
    return self._session_timeout_seconds or 0

  @session_timeout_seconds.setter
  def session_timeout_seconds(self, session_timeout_seconds: Optional[int]):
    if session_timeout_seconds is None:
      del self.session_timeout_seconds
      return
    if not isinstance(session_timeout_seconds, int):
      raise TypeError('session_timeout_seconds must be of type int')
    self._session_timeout_seconds = session_timeout_seconds

  @property
  def max_cpu_cores(self) -> int:
    return self._max_cpu_cores or 0

  @max_cpu_cores.setter
  def max_cpu_cores(self, max_cpu_cores: Optional[int]):
    if max_cpu_cores is None:
      del self.max_cpu_cores
      return
    if not isinstance(max_cpu_cores, int):
      raise TypeError('max_cpu_cores must be of type int')
    self._max_cpu_cores = max_cpu_cores

  @property
  def max_storage_bytes(self) -> int:
    return self._max_storage_bytes or 0

  @max_storage_bytes.setter
  def max_storage_bytes(self, max_storage_bytes: Optional[int]):
    if max_storage_bytes is None:
      del self.max_storage_bytes
      return
    if not isinstance(max_storage_bytes, int):
      raise TypeError('max_storage_bytes must be of type int')
    self._max_storage_bytes = max_storage_bytes

  @property
  def max_memory_bytes(self) -> int:
    return self._max_memory_bytes or 0

  @max_memory_bytes.setter
  def max_memory_bytes(self, max_memory_bytes: Optional[int]):
    if max_memory_bytes is None:
      del self.max_memory_bytes
      return
    if not isinstance(max_memory_bytes, int):
      raise TypeError('max_memory_bytes must be of type int')
    self._max_memory_bytes = max_memory_bytes

  @property
  def disallow_internet(self) -> bool:
    return self._disallow_internet or False

  @disallow_internet.setter
  def disallow_internet(self, disallow_internet: Optional[bool]):
    if disallow_internet is None:
      del self.disallow_internet
      return
    if not isinstance(disallow_internet, bool):
      raise TypeError('disallow_internet must be of type bool')
    self._disallow_internet = disallow_internet


class ComputeInternetState(KaggleObject):
  r"""
  Attributes:
    is_enabled (bool)
  """

  def __init__(self):
    self._is_enabled = False
    self._freeze()

  @property
  def is_enabled(self) -> bool:
    return self._is_enabled

  @is_enabled.setter
  def is_enabled(self, is_enabled: bool):
    if is_enabled is None:
      del self.is_enabled
      return
    if not isinstance(is_enabled, bool):
      raise TypeError('is_enabled must be of type bool')
    self._is_enabled = is_enabled


class ComputeKernelDiffRequest(KaggleObject):
  r"""
  Attributes:
    left_session_id (int)
    right_session_id (int)
    include_contents (bool)
  """

  def __init__(self):
    self._left_session_id = 0
    self._right_session_id = 0
    self._include_contents = False
    self._freeze()

  @property
  def left_session_id(self) -> int:
    return self._left_session_id

  @left_session_id.setter
  def left_session_id(self, left_session_id: int):
    if left_session_id is None:
      del self.left_session_id
      return
    if not isinstance(left_session_id, int):
      raise TypeError('left_session_id must be of type int')
    self._left_session_id = left_session_id

  @property
  def right_session_id(self) -> int:
    return self._right_session_id

  @right_session_id.setter
  def right_session_id(self, right_session_id: int):
    if right_session_id is None:
      del self.right_session_id
      return
    if not isinstance(right_session_id, int):
      raise TypeError('right_session_id must be of type int')
    self._right_session_id = right_session_id

  @property
  def include_contents(self) -> bool:
    return self._include_contents

  @include_contents.setter
  def include_contents(self, include_contents: bool):
    if include_contents is None:
      del self.include_contents
      return
    if not isinstance(include_contents, bool):
      raise TypeError('include_contents must be of type bool')
    self._include_contents = include_contents


class ComputeKernelDiffResponse(KaggleObject):
  r"""
  Attributes:
    diff (KernelDiff)
    left_content (str)
    right_content (str)
  """

  def __init__(self):
    self._diff = None
    self._left_content = None
    self._right_content = None
    self._freeze()

  @property
  def diff(self) -> Optional['KernelDiff']:
    return self._diff

  @diff.setter
  def diff(self, diff: Optional['KernelDiff']):
    if diff is None:
      del self.diff
      return
    if not isinstance(diff, KernelDiff):
      raise TypeError('diff must be of type KernelDiff')
    self._diff = diff

  @property
  def left_content(self) -> str:
    return self._left_content or ""

  @left_content.setter
  def left_content(self, left_content: Optional[str]):
    if left_content is None:
      del self.left_content
      return
    if not isinstance(left_content, str):
      raise TypeError('left_content must be of type str')
    self._left_content = left_content

  @property
  def right_content(self) -> str:
    return self._right_content or ""

  @right_content.setter
  def right_content(self, right_content: Optional[str]):
    if right_content is None:
      del self.right_content
      return
    if not isinstance(right_content, str):
      raise TypeError('right_content must be of type str')
    self._right_content = right_content


class ComputeState(KaggleObject):
  r"""
  Attributes:
    accelerator (AcceleratorType)
    internet (ComputeInternetState)
    constraints (ComputeConstraintState)
    intranet (bool)
  """

  def __init__(self):
    self._accelerator = AcceleratorType.ACCELERATOR_TYPE_NONE
    self._internet = None
    self._constraints = None
    self._intranet = None
    self._freeze()

  @property
  def accelerator(self) -> 'AcceleratorType':
    return self._accelerator

  @accelerator.setter
  def accelerator(self, accelerator: 'AcceleratorType'):
    if accelerator is None:
      del self.accelerator
      return
    if not isinstance(accelerator, AcceleratorType):
      raise TypeError('accelerator must be of type AcceleratorType')
    self._accelerator = accelerator

  @property
  def internet(self) -> Optional['ComputeInternetState']:
    return self._internet

  @internet.setter
  def internet(self, internet: Optional['ComputeInternetState']):
    if internet is None:
      del self.internet
      return
    if not isinstance(internet, ComputeInternetState):
      raise TypeError('internet must be of type ComputeInternetState')
    self._internet = internet

  @property
  def constraints(self) -> Optional['ComputeConstraintState']:
    return self._constraints

  @constraints.setter
  def constraints(self, constraints: Optional['ComputeConstraintState']):
    if constraints is None:
      del self.constraints
      return
    if not isinstance(constraints, ComputeConstraintState):
      raise TypeError('constraints must be of type ComputeConstraintState')
    self._constraints = constraints

  @property
  def intranet(self) -> bool:
    return self._intranet or False

  @intranet.setter
  def intranet(self, intranet: Optional[bool]):
    if intranet is None:
      del self.intranet
      return
    if not isinstance(intranet, bool):
      raise TypeError('intranet must be of type bool')
    self._intranet = intranet


class CreateKernelParameters(KaggleObject):
  r"""
  Attributes:
    title (str)
    language_id (int)
    docker_image_version_id (int)
    compute (ComputeState)
    data_sources (DataSourceReference)
    tag_ids (int)
  """

  def __init__(self):
    self._title = None
    self._language_id = 0
    self._docker_image_version_id = None
    self._compute = None
    self._data_sources = []
    self._tag_ids = []
    self._freeze()

  @property
  def title(self) -> str:
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
  def language_id(self) -> int:
    return self._language_id

  @language_id.setter
  def language_id(self, language_id: int):
    if language_id is None:
      del self.language_id
      return
    if not isinstance(language_id, int):
      raise TypeError('language_id must be of type int')
    self._language_id = language_id

  @property
  def docker_image_version_id(self) -> int:
    return self._docker_image_version_id or 0

  @docker_image_version_id.setter
  def docker_image_version_id(self, docker_image_version_id: Optional[int]):
    if docker_image_version_id is None:
      del self.docker_image_version_id
      return
    if not isinstance(docker_image_version_id, int):
      raise TypeError('docker_image_version_id must be of type int')
    self._docker_image_version_id = docker_image_version_id

  @property
  def compute(self) -> Optional['ComputeState']:
    return self._compute

  @compute.setter
  def compute(self, compute: Optional['ComputeState']):
    if compute is None:
      del self.compute
      return
    if not isinstance(compute, ComputeState):
      raise TypeError('compute must be of type ComputeState')
    self._compute = compute

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def tag_ids(self) -> Optional[List[int]]:
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids


class CreateKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    version_type (KernelVersionType)
    docker_image_tag (str)
    worker_pool_name (str)
    immediately_cancel_session (bool)
    executed_by_schedule_id (int)
    kernel_version_id (int)
      These properties are only set for batch runs.
    diff (KernelDiff)
    fork_parent_diff (KernelDiff)
    submission_requested_details (SubmissionRequestedDetails)
    use_given_data_source_version_ids (bool)
      This is a hack to support two different use cases for CreateKernelSession:
      The normal (typically interactive) use case of starting up a new session
      using the latest [Comp|Dataset|Kernel] Version for each data source, and
      the reproducibility use case (right now, specifically for Competition
      Reruns) where we need to use the same Versions for each data source as the
      original KernelSession used.

      Setting this flag to `true` will bypass the default behavior of querying
      the latest Versions for each data source and instead use the VersionIds
      which are already provided in the `DataSources` field above.

      A future version of this API should handle this more cleanly, for example
      by acting as if this flag was always set to true and requiring callers to
      fetch VersionIds according to their needs.
    parameters (CreateKernelParameters)
    github_save_request (GitHubSaveRequest)
    environment_variables (EnvironmentVariable)
    creation_source (CreationSource)
    stagger_start (timedelta)
    aliases (str)
    extra_mounts (ExtraMountSettings)
    priority (int)
      Sets the execution priority of this KernelSession request when queued,
      lower is better (10 will get run before 100). Only used if current user is
      admin or bot, or in the KERNELS_ALLOW_SET_PRIORITY flag, otherwise ignored.
    allow_container_reset (bool)
      If true, this container allows being reset via the reset signal mechanism.
      Only supported for child containers.
  """

  def __init__(self):
    self._kernel_id = 0
    self._version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._docker_image_tag = None
    self._worker_pool_name = None
    self._immediately_cancel_session = False
    self._executed_by_schedule_id = None
    self._kernel_version_id = None
    self._diff = None
    self._fork_parent_diff = None
    self._submission_requested_details = None
    self._use_given_data_source_version_ids = False
    self._parameters = None
    self._github_save_request = None
    self._environment_variables = []
    self._creation_source = None
    self._stagger_start = None
    self._aliases = []
    self._extra_mounts = []
    self._priority = None
    self._allow_container_reset = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type

  @version_type.setter
  def version_type(self, version_type: 'KernelVersionType'):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type

  @property
  def docker_image_tag(self) -> str:
    return self._docker_image_tag or ""

  @docker_image_tag.setter
  def docker_image_tag(self, docker_image_tag: Optional[str]):
    if docker_image_tag is None:
      del self.docker_image_tag
      return
    if not isinstance(docker_image_tag, str):
      raise TypeError('docker_image_tag must be of type str')
    self._docker_image_tag = docker_image_tag

  @property
  def worker_pool_name(self) -> str:
    return self._worker_pool_name or ""

  @worker_pool_name.setter
  def worker_pool_name(self, worker_pool_name: Optional[str]):
    if worker_pool_name is None:
      del self.worker_pool_name
      return
    if not isinstance(worker_pool_name, str):
      raise TypeError('worker_pool_name must be of type str')
    self._worker_pool_name = worker_pool_name

  @property
  def immediately_cancel_session(self) -> bool:
    return self._immediately_cancel_session

  @immediately_cancel_session.setter
  def immediately_cancel_session(self, immediately_cancel_session: bool):
    if immediately_cancel_session is None:
      del self.immediately_cancel_session
      return
    if not isinstance(immediately_cancel_session, bool):
      raise TypeError('immediately_cancel_session must be of type bool')
    self._immediately_cancel_session = immediately_cancel_session

  @property
  def executed_by_schedule_id(self) -> int:
    return self._executed_by_schedule_id or 0

  @executed_by_schedule_id.setter
  def executed_by_schedule_id(self, executed_by_schedule_id: Optional[int]):
    if executed_by_schedule_id is None:
      del self.executed_by_schedule_id
      return
    if not isinstance(executed_by_schedule_id, int):
      raise TypeError('executed_by_schedule_id must be of type int')
    self._executed_by_schedule_id = executed_by_schedule_id

  @property
  def kernel_version_id(self) -> int:
    """These properties are only set for batch runs."""
    return self._kernel_version_id or 0

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: Optional[int]):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def diff(self) -> Optional['KernelDiff']:
    return self._diff

  @diff.setter
  def diff(self, diff: Optional['KernelDiff']):
    if diff is None:
      del self.diff
      return
    if not isinstance(diff, KernelDiff):
      raise TypeError('diff must be of type KernelDiff')
    self._diff = diff

  @property
  def fork_parent_diff(self) -> Optional['KernelDiff']:
    return self._fork_parent_diff

  @fork_parent_diff.setter
  def fork_parent_diff(self, fork_parent_diff: Optional['KernelDiff']):
    if fork_parent_diff is None:
      del self.fork_parent_diff
      return
    if not isinstance(fork_parent_diff, KernelDiff):
      raise TypeError('fork_parent_diff must be of type KernelDiff')
    self._fork_parent_diff = fork_parent_diff

  @property
  def submission_requested_details(self) -> Optional['SubmissionRequestedDetails']:
    return self._submission_requested_details

  @submission_requested_details.setter
  def submission_requested_details(self, submission_requested_details: Optional['SubmissionRequestedDetails']):
    if submission_requested_details is None:
      del self.submission_requested_details
      return
    if not isinstance(submission_requested_details, SubmissionRequestedDetails):
      raise TypeError('submission_requested_details must be of type SubmissionRequestedDetails')
    self._submission_requested_details = submission_requested_details

  @property
  def use_given_data_source_version_ids(self) -> bool:
    r"""
    This is a hack to support two different use cases for CreateKernelSession:
    The normal (typically interactive) use case of starting up a new session
    using the latest [Comp|Dataset|Kernel] Version for each data source, and
    the reproducibility use case (right now, specifically for Competition
    Reruns) where we need to use the same Versions for each data source as the
    original KernelSession used.

    Setting this flag to `true` will bypass the default behavior of querying
    the latest Versions for each data source and instead use the VersionIds
    which are already provided in the `DataSources` field above.

    A future version of this API should handle this more cleanly, for example
    by acting as if this flag was always set to true and requiring callers to
    fetch VersionIds according to their needs.
    """
    return self._use_given_data_source_version_ids

  @use_given_data_source_version_ids.setter
  def use_given_data_source_version_ids(self, use_given_data_source_version_ids: bool):
    if use_given_data_source_version_ids is None:
      del self.use_given_data_source_version_ids
      return
    if not isinstance(use_given_data_source_version_ids, bool):
      raise TypeError('use_given_data_source_version_ids must be of type bool')
    self._use_given_data_source_version_ids = use_given_data_source_version_ids

  @property
  def parameters(self) -> Optional['CreateKernelParameters']:
    return self._parameters

  @parameters.setter
  def parameters(self, parameters: Optional['CreateKernelParameters']):
    if parameters is None:
      del self.parameters
      return
    if not isinstance(parameters, CreateKernelParameters):
      raise TypeError('parameters must be of type CreateKernelParameters')
    self._parameters = parameters

  @property
  def github_save_request(self) -> Optional['GitHubSaveRequest']:
    return self._github_save_request

  @github_save_request.setter
  def github_save_request(self, github_save_request: Optional['GitHubSaveRequest']):
    if github_save_request is None:
      del self.github_save_request
      return
    if not isinstance(github_save_request, GitHubSaveRequest):
      raise TypeError('github_save_request must be of type GitHubSaveRequest')
    self._github_save_request = github_save_request

  @property
  def environment_variables(self) -> Optional[List[Optional['EnvironmentVariable']]]:
    return self._environment_variables

  @environment_variables.setter
  def environment_variables(self, environment_variables: Optional[List[Optional['EnvironmentVariable']]]):
    if environment_variables is None:
      del self.environment_variables
      return
    if not isinstance(environment_variables, list):
      raise TypeError('environment_variables must be of type list')
    if not all([isinstance(t, EnvironmentVariable) for t in environment_variables]):
      raise TypeError('environment_variables must contain only items of type EnvironmentVariable')
    self._environment_variables = environment_variables

  @property
  def creation_source(self) -> Optional['CreationSource']:
    return self._creation_source or None

  @creation_source.setter
  def creation_source(self, creation_source: Optional[Optional['CreationSource']]):
    if creation_source is None:
      del self.creation_source
      return
    if not isinstance(creation_source, CreationSource):
      raise TypeError('creation_source must be of type CreationSource')
    self._creation_source = creation_source

  @property
  def stagger_start(self) -> timedelta:
    return self._stagger_start

  @stagger_start.setter
  def stagger_start(self, stagger_start: timedelta):
    if stagger_start is None:
      del self.stagger_start
      return
    if not isinstance(stagger_start, timedelta):
      raise TypeError('stagger_start must be of type timedelta')
    self._stagger_start = stagger_start

  @property
  def aliases(self) -> Optional[List[str]]:
    return self._aliases

  @aliases.setter
  def aliases(self, aliases: Optional[List[str]]):
    if aliases is None:
      del self.aliases
      return
    if not isinstance(aliases, list):
      raise TypeError('aliases must be of type list')
    if not all([isinstance(t, str) for t in aliases]):
      raise TypeError('aliases must contain only items of type str')
    self._aliases = aliases

  @property
  def extra_mounts(self) -> Optional[List[Optional['ExtraMountSettings']]]:
    return self._extra_mounts

  @extra_mounts.setter
  def extra_mounts(self, extra_mounts: Optional[List[Optional['ExtraMountSettings']]]):
    if extra_mounts is None:
      del self.extra_mounts
      return
    if not isinstance(extra_mounts, list):
      raise TypeError('extra_mounts must be of type list')
    if not all([isinstance(t, ExtraMountSettings) for t in extra_mounts]):
      raise TypeError('extra_mounts must contain only items of type ExtraMountSettings')
    self._extra_mounts = extra_mounts

  @property
  def priority(self) -> int:
    r"""
    Sets the execution priority of this KernelSession request when queued,
    lower is better (10 will get run before 100). Only used if current user is
    admin or bot, or in the KERNELS_ALLOW_SET_PRIORITY flag, otherwise ignored.
    """
    return self._priority or 0

  @priority.setter
  def priority(self, priority: Optional[int]):
    if priority is None:
      del self.priority
      return
    if not isinstance(priority, int):
      raise TypeError('priority must be of type int')
    self._priority = priority

  @property
  def allow_container_reset(self) -> bool:
    r"""
    If true, this container allows being reset via the reset signal mechanism.
    Only supported for child containers.
    """
    return self._allow_container_reset or False

  @allow_container_reset.setter
  def allow_container_reset(self, allow_container_reset: Optional[bool]):
    if allow_container_reset is None:
      del self.allow_container_reset
      return
    if not isinstance(allow_container_reset, bool):
      raise TypeError('allow_container_reset must be of type bool')
    self._allow_container_reset = allow_container_reset


class CreateKernelSessionResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
    error (str)
    show_parent_fork_secret_warning (bool)
    accelerator_changed (AcceleratorType)
      Set iff the AcceleratorType used by this Session doesn't match the
      requested AcceleratorType. It returns the actually used AcceleratorType.
  """

  def __init__(self):
    self._id = 0
    self._error = None
    self._show_parent_fork_secret_warning = False
    self._accelerator_changed = None
    self._freeze()

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
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def show_parent_fork_secret_warning(self) -> bool:
    return self._show_parent_fork_secret_warning

  @show_parent_fork_secret_warning.setter
  def show_parent_fork_secret_warning(self, show_parent_fork_secret_warning: bool):
    if show_parent_fork_secret_warning is None:
      del self.show_parent_fork_secret_warning
      return
    if not isinstance(show_parent_fork_secret_warning, bool):
      raise TypeError('show_parent_fork_secret_warning must be of type bool')
    self._show_parent_fork_secret_warning = show_parent_fork_secret_warning

  @property
  def accelerator_changed(self) -> 'AcceleratorType':
    r"""
    Set iff the AcceleratorType used by this Session doesn't match the
    requested AcceleratorType. It returns the actually used AcceleratorType.
    """
    return self._accelerator_changed or AcceleratorType.ACCELERATOR_TYPE_NONE

  @accelerator_changed.setter
  def accelerator_changed(self, accelerator_changed: Optional['AcceleratorType']):
    if accelerator_changed is None:
      del self.accelerator_changed
      return
    if not isinstance(accelerator_changed, AcceleratorType):
      raise TypeError('accelerator_changed must be of type AcceleratorType')
    self._accelerator_changed = accelerator_changed


class CreateKernelUpvoteRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class CreateKernelUpvoteResponse(KaggleObject):
  r"""
  Attributes:
    vote_id (int)
    is_self_vote (bool)
  """

  def __init__(self):
    self._vote_id = 0
    self._is_self_vote = False
    self._freeze()

  @property
  def vote_id(self) -> int:
    return self._vote_id

  @vote_id.setter
  def vote_id(self, vote_id: int):
    if vote_id is None:
      del self.vote_id
      return
    if not isinstance(vote_id, int):
      raise TypeError('vote_id must be of type int')
    self._vote_id = vote_id

  @property
  def is_self_vote(self) -> bool:
    return self._is_self_vote

  @is_self_vote.setter
  def is_self_vote(self, is_self_vote: bool):
    if is_self_vote is None:
      del self.is_self_vote
      return
    if not isinstance(is_self_vote, bool):
      raise TypeError('is_self_vote must be of type bool')
    self._is_self_vote = is_self_vote


class CreateKernelWithSettingsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_language_id (int)
    source_type (EditorType)
    accelerator (AcceleratorType)
    source_url (str)
      URL to fetch for initial content.
    enable_internet (bool)
    fork_parent_script_version_id (int)
    competition_id (int)
      Create a kernel using this competition's data.
    dataset_version_id (int)
      Create a kernel with this dataset.
    kernel_output_version_id (int)
      Use the output of a kernel as an input data source.
    docker_image_pinning_type (DockerImagePinningType)
    model_id (int)
    model_instance_version_id (int)
    import_source (CreateKernelWithSettingsRequest.ImportSource)
  """

  class ImportSource(KaggleObject):
    r"""
    Attributes:
      import_type (ImportType)
      source_data (str)
        For Colab: the driveId, for GitHub: the rawUrl, for an external source:
        the url, for File: the content of the file.
      version_type (KernelVersionType)
      file_name (str)
      accelerator_selection (AcceleratorSelection)
    """

    def __init__(self):
      self._import_type = None
      self._source_data = None
      self._version_type = None
      self._file_name = None
      self._accelerator_selection = None
      self._freeze()

    @property
    def import_type(self) -> 'ImportType':
      return self._import_type or ImportType.UNSPECIFIED

    @import_type.setter
    def import_type(self, import_type: Optional['ImportType']):
      if import_type is None:
        del self.import_type
        return
      if not isinstance(import_type, ImportType):
        raise TypeError('import_type must be of type ImportType')
      self._import_type = import_type

    @property
    def source_data(self) -> str:
      r"""
      For Colab: the driveId, for GitHub: the rawUrl, for an external source:
      the url, for File: the content of the file.
      """
      return self._source_data or ""

    @source_data.setter
    def source_data(self, source_data: Optional[str]):
      if source_data is None:
        del self.source_data
        return
      if not isinstance(source_data, str):
        raise TypeError('source_data must be of type str')
      self._source_data = source_data

    @property
    def version_type(self) -> 'KernelVersionType':
      return self._version_type or KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED

    @version_type.setter
    def version_type(self, version_type: Optional['KernelVersionType']):
      if version_type is None:
        del self.version_type
        return
      if not isinstance(version_type, KernelVersionType):
        raise TypeError('version_type must be of type KernelVersionType')
      self._version_type = version_type

    @property
    def file_name(self) -> str:
      return self._file_name or ""

    @file_name.setter
    def file_name(self, file_name: Optional[str]):
      if file_name is None:
        del self.file_name
        return
      if not isinstance(file_name, str):
        raise TypeError('file_name must be of type str')
      self._file_name = file_name

    @property
    def accelerator_selection(self) -> 'AcceleratorSelection':
      return self._accelerator_selection or AcceleratorSelection.ACCELERATOR_UNSPECIFIED

    @accelerator_selection.setter
    def accelerator_selection(self, accelerator_selection: Optional['AcceleratorSelection']):
      if accelerator_selection is None:
        del self.accelerator_selection
        return
      if not isinstance(accelerator_selection, AcceleratorSelection):
        raise TypeError('accelerator_selection must be of type AcceleratorSelection')
      self._accelerator_selection = accelerator_selection


  def __init__(self):
    self._kernel_language_id = 0
    self._source_type = EditorType.EDITOR_TYPE_UNSPECIFIED
    self._accelerator = AcceleratorType.ACCELERATOR_TYPE_NONE
    self._source_url = None
    self._enable_internet = None
    self._fork_parent_script_version_id = None
    self._competition_id = None
    self._dataset_version_id = None
    self._kernel_output_version_id = None
    self._docker_image_pinning_type = None
    self._model_id = None
    self._model_instance_version_id = None
    self._import_source = None
    self._freeze()

  @property
  def kernel_language_id(self) -> int:
    return self._kernel_language_id

  @kernel_language_id.setter
  def kernel_language_id(self, kernel_language_id: int):
    if kernel_language_id is None:
      del self.kernel_language_id
      return
    if not isinstance(kernel_language_id, int):
      raise TypeError('kernel_language_id must be of type int')
    self._kernel_language_id = kernel_language_id

  @property
  def source_type(self) -> 'EditorType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'EditorType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, EditorType):
      raise TypeError('source_type must be of type EditorType')
    self._source_type = source_type

  @property
  def accelerator(self) -> 'AcceleratorType':
    return self._accelerator

  @accelerator.setter
  def accelerator(self, accelerator: 'AcceleratorType'):
    if accelerator is None:
      del self.accelerator
      return
    if not isinstance(accelerator, AcceleratorType):
      raise TypeError('accelerator must be of type AcceleratorType')
    self._accelerator = accelerator

  @property
  def source_url(self) -> str:
    """URL to fetch for initial content."""
    return self._source_url or ""

  @source_url.setter
  def source_url(self, source_url: Optional[str]):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    self._source_url = source_url

  @property
  def enable_internet(self) -> bool:
    return self._enable_internet or False

  @enable_internet.setter
  def enable_internet(self, enable_internet: Optional[bool]):
    if enable_internet is None:
      del self.enable_internet
      return
    if not isinstance(enable_internet, bool):
      raise TypeError('enable_internet must be of type bool')
    self._enable_internet = enable_internet

  @property
  def fork_parent_script_version_id(self) -> int:
    return self._fork_parent_script_version_id or 0

  @fork_parent_script_version_id.setter
  def fork_parent_script_version_id(self, fork_parent_script_version_id: Optional[int]):
    if fork_parent_script_version_id is None:
      del self.fork_parent_script_version_id
      return
    if not isinstance(fork_parent_script_version_id, int):
      raise TypeError('fork_parent_script_version_id must be of type int')
    self._fork_parent_script_version_id = fork_parent_script_version_id

  @property
  def competition_id(self) -> int:
    """Create a kernel using this competition's data."""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def dataset_version_id(self) -> int:
    """Create a kernel with this dataset."""
    return self._dataset_version_id or 0

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: Optional[int]):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id

  @property
  def kernel_output_version_id(self) -> int:
    """Use the output of a kernel as an input data source."""
    return self._kernel_output_version_id or 0

  @kernel_output_version_id.setter
  def kernel_output_version_id(self, kernel_output_version_id: Optional[int]):
    if kernel_output_version_id is None:
      del self.kernel_output_version_id
      return
    if not isinstance(kernel_output_version_id, int):
      raise TypeError('kernel_output_version_id must be of type int')
    self._kernel_output_version_id = kernel_output_version_id

  @property
  def docker_image_pinning_type(self) -> 'DockerImagePinningType':
    return self._docker_image_pinning_type or DockerImagePinningType.DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED

  @docker_image_pinning_type.setter
  def docker_image_pinning_type(self, docker_image_pinning_type: Optional['DockerImagePinningType']):
    if docker_image_pinning_type is None:
      del self.docker_image_pinning_type
      return
    if not isinstance(docker_image_pinning_type, DockerImagePinningType):
      raise TypeError('docker_image_pinning_type must be of type DockerImagePinningType')
    self._docker_image_pinning_type = docker_image_pinning_type

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: Optional[int]):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id or 0

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: Optional[int]):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    self._model_instance_version_id = model_instance_version_id

  @property
  def import_source(self) -> Optional['CreateKernelWithSettingsRequest.ImportSource']:
    return self._import_source or None

  @import_source.setter
  def import_source(self, import_source: Optional[Optional['CreateKernelWithSettingsRequest.ImportSource']]):
    if import_source is None:
      del self.import_source
      return
    if not isinstance(import_source, CreateKernelWithSettingsRequest.ImportSource):
      raise TypeError('import_source must be of type CreateKernelWithSettingsRequest.ImportSource')
    self._import_source = import_source


class CreateKernelWithSettingsResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
    current_url_slug (str)
  """

  def __init__(self):
    self._id = 0
    self._current_url_slug = None
    self._freeze()

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
  def current_url_slug(self) -> str:
    return self._current_url_slug or ""

  @current_url_slug.setter
  def current_url_slug(self, current_url_slug: Optional[str]):
    if current_url_slug is None:
      del self.current_url_slug
      return
    if not isinstance(current_url_slug, str):
      raise TypeError('current_url_slug must be of type str')
    self._current_url_slug = current_url_slug


class CreateUserResourceReferenceViewRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
  """

  def __init__(self):
    self._id = 0
    self._freeze()

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


class DailySubmissionInfo(KaggleObject):
  r"""
  Attributes:
    submission_count (int)
    submission_limit (int)
  """

  def __init__(self):
    self._submission_count = 0
    self._submission_limit = None
    self._freeze()

  @property
  def submission_count(self) -> int:
    return self._submission_count

  @submission_count.setter
  def submission_count(self, submission_count: int):
    if submission_count is None:
      del self.submission_count
      return
    if not isinstance(submission_count, int):
      raise TypeError('submission_count must be of type int')
    self._submission_count = submission_count

  @property
  def submission_limit(self) -> int:
    return self._submission_limit or 0

  @submission_limit.setter
  def submission_limit(self, submission_limit: Optional[int]):
    if submission_limit is None:
      del self.submission_limit
      return
    if not isinstance(submission_limit, int):
      raise TypeError('submission_limit must be of type int')
    self._submission_limit = submission_limit


class DataSourceVersion(KaggleObject):
  r"""
  Version of a data source attached to a kernel session. Data source can be
  either a dataset, competition dataset or output of another kernel. Depending
  on the type of the dataset, meanings of the fields in this model change.

  Attributes:
    id (int)
      For datasets, this is the databundle version id.
      For competition datasets, this is the databundle version id.
      For kernel output files, this is the kernel session id.
    number (int)
      For datasets, this is the databundle version number.
      For competition datasets, this is the databundle version number.
      For kernel output files, this is the kernel session version number.
    slug (str)
      Mount slug for the data source.
  """

  def __init__(self):
    self._id = None
    self._number = None
    self._slug = None
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    For datasets, this is the databundle version id.
    For competition datasets, this is the databundle version id.
    For kernel output files, this is the kernel session id.
    """
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def number(self) -> int:
    r"""
    For datasets, this is the databundle version number.
    For competition datasets, this is the databundle version number.
    For kernel output files, this is the kernel session version number.
    """
    return self._number or 0

  @number.setter
  def number(self, number: Optional[int]):
    if number is None:
      del self.number
      return
    if not isinstance(number, int):
      raise TypeError('number must be of type int')
    self._number = number

  @property
  def slug(self) -> str:
    """Mount slug for the data source."""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug


class DefaultSessionSettings(KaggleObject):
  r"""
  Attributes:
    save_quick_version_output_files (bool)
    batch_session_default_accelerator (AcceleratorType)
    link_to_github (bool)
    github_spec (GithubSpec)
    colab_spec (ColabSpec)
  """

  def __init__(self):
    self._save_quick_version_output_files = None
    self._batch_session_default_accelerator = None
    self._link_to_github = None
    self._github_spec = None
    self._colab_spec = None
    self._freeze()

  @property
  def save_quick_version_output_files(self) -> bool:
    return self._save_quick_version_output_files or False

  @save_quick_version_output_files.setter
  def save_quick_version_output_files(self, save_quick_version_output_files: Optional[bool]):
    if save_quick_version_output_files is None:
      del self.save_quick_version_output_files
      return
    if not isinstance(save_quick_version_output_files, bool):
      raise TypeError('save_quick_version_output_files must be of type bool')
    self._save_quick_version_output_files = save_quick_version_output_files

  @property
  def batch_session_default_accelerator(self) -> 'AcceleratorType':
    return self._batch_session_default_accelerator or AcceleratorType.ACCELERATOR_TYPE_NONE

  @batch_session_default_accelerator.setter
  def batch_session_default_accelerator(self, batch_session_default_accelerator: Optional['AcceleratorType']):
    if batch_session_default_accelerator is None:
      del self.batch_session_default_accelerator
      return
    if not isinstance(batch_session_default_accelerator, AcceleratorType):
      raise TypeError('batch_session_default_accelerator must be of type AcceleratorType')
    self._batch_session_default_accelerator = batch_session_default_accelerator

  @property
  def link_to_github(self) -> bool:
    return self._link_to_github or False

  @link_to_github.setter
  def link_to_github(self, link_to_github: Optional[bool]):
    if link_to_github is None:
      del self.link_to_github
      return
    if not isinstance(link_to_github, bool):
      raise TypeError('link_to_github must be of type bool')
    self._link_to_github = link_to_github

  @property
  def github_spec(self) -> Optional['GithubSpec']:
    return self._github_spec or None

  @github_spec.setter
  def github_spec(self, github_spec: Optional[Optional['GithubSpec']]):
    if github_spec is None:
      del self.github_spec
      return
    if not isinstance(github_spec, GithubSpec):
      raise TypeError('github_spec must be of type GithubSpec')
    self._github_spec = github_spec

  @property
  def colab_spec(self) -> Optional['ColabSpec']:
    return self._colab_spec or None

  @colab_spec.setter
  def colab_spec(self, colab_spec: Optional[Optional['ColabSpec']]):
    if colab_spec is None:
      del self.colab_spec
      return
    if not isinstance(colab_spec, ColabSpec):
      raise TypeError('colab_spec must be of type ColabSpec')
    self._colab_spec = colab_spec


class DeleteKernelRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class DeleteKernelUpvoteRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class DeleteScheduledKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      ID of the scheduling.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """ID of the scheduling."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class DeleteScheduledKernelSessionResponse(KaggleObject):
  r"""
  """

  pass

class DockerImageVersionDetails(KaggleObject):
  r"""
  Attributes:
    id (int)
    type (DockerImageVersionType)
    disabled_reason (DockerImageVersionDisabledReason)
    date_created (datetime)
  """

  def __init__(self):
    self._id = None
    self._type = DockerImageVersionType.DOCKER_IMAGE_VERSION_TYPE_LATEST
    self._disabled_reason = DockerImageVersionDisabledReason.DOCKER_IMAGE_VERSION_DISABLED_REASON_UNSPECIFIED
    self._date_created = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def type(self) -> 'DockerImageVersionType':
    return self._type

  @type.setter
  def type(self, type: 'DockerImageVersionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DockerImageVersionType):
      raise TypeError('type must be of type DockerImageVersionType')
    self._type = type

  @property
  def disabled_reason(self) -> 'DockerImageVersionDisabledReason':
    return self._disabled_reason

  @disabled_reason.setter
  def disabled_reason(self, disabled_reason: 'DockerImageVersionDisabledReason'):
    if disabled_reason is None:
      del self.disabled_reason
      return
    if not isinstance(disabled_reason, DockerImageVersionDisabledReason):
      raise TypeError('disabled_reason must be of type DockerImageVersionDisabledReason')
    self._disabled_reason = disabled_reason

  @property
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created


class DockerImageVersionDetailsList(KaggleObject):
  r"""
  Attributes:
    images (DockerImageVersionDetails)
    selected_version_type (DockerImageVersionType)
    selected_version_id (int)
      Set only if SelectedVersionType == Custom.
  """

  def __init__(self):
    self._images = []
    self._selected_version_type = DockerImageVersionType.DOCKER_IMAGE_VERSION_TYPE_LATEST
    self._selected_version_id = None
    self._freeze()

  @property
  def images(self) -> Optional[List[Optional['DockerImageVersionDetails']]]:
    return self._images

  @images.setter
  def images(self, images: Optional[List[Optional['DockerImageVersionDetails']]]):
    if images is None:
      del self.images
      return
    if not isinstance(images, list):
      raise TypeError('images must be of type list')
    if not all([isinstance(t, DockerImageVersionDetails) for t in images]):
      raise TypeError('images must contain only items of type DockerImageVersionDetails')
    self._images = images

  @property
  def selected_version_type(self) -> 'DockerImageVersionType':
    return self._selected_version_type

  @selected_version_type.setter
  def selected_version_type(self, selected_version_type: 'DockerImageVersionType'):
    if selected_version_type is None:
      del self.selected_version_type
      return
    if not isinstance(selected_version_type, DockerImageVersionType):
      raise TypeError('selected_version_type must be of type DockerImageVersionType')
    self._selected_version_type = selected_version_type

  @property
  def selected_version_id(self) -> int:
    """Set only if SelectedVersionType == Custom."""
    return self._selected_version_id or 0

  @selected_version_id.setter
  def selected_version_id(self, selected_version_id: Optional[int]):
    if selected_version_id is None:
      del self.selected_version_id
      return
    if not isinstance(selected_version_id, int):
      raise TypeError('selected_version_id must be of type int')
    self._selected_version_id = selected_version_id


class EligibleAccelerator(KaggleObject):
  r"""
  Attributes:
    variant (ColabVariant)
    models (str)
  """

  def __init__(self):
    self._variant = ColabVariant.VARIANT_UNSPECIFIED
    self._models = []
    self._freeze()

  @property
  def variant(self) -> 'ColabVariant':
    return self._variant

  @variant.setter
  def variant(self, variant: 'ColabVariant'):
    if variant is None:
      del self.variant
      return
    if not isinstance(variant, ColabVariant):
      raise TypeError('variant must be of type ColabVariant')
    self._variant = variant

  @property
  def models(self) -> Optional[List[str]]:
    return self._models

  @models.setter
  def models(self, models: Optional[List[str]]):
    if models is None:
      del self.models
      return
    if not isinstance(models, list):
      raise TypeError('models must be of type list')
    if not all([isinstance(t, str) for t in models]):
      raise TypeError('models must contain only items of type str')
    self._models = models


class EnvironmentVariable(KaggleObject):
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


class ExportKernelSessionForColabRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    use_draft (bool)
    colab_notebook_source (ColabNotebookSource)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._use_draft = False
    self._colab_notebook_source = None
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

  @property
  def use_draft(self) -> bool:
    return self._use_draft

  @use_draft.setter
  def use_draft(self, use_draft: bool):
    if use_draft is None:
      del self.use_draft
      return
    if not isinstance(use_draft, bool):
      raise TypeError('use_draft must be of type bool')
    self._use_draft = use_draft

  @property
  def colab_notebook_source(self) -> 'ColabNotebookSource':
    return self._colab_notebook_source or ColabNotebookSource.COLAB_NOTEBOOK_SOURCE_UNSPECIFIED

  @colab_notebook_source.setter
  def colab_notebook_source(self, colab_notebook_source: Optional['ColabNotebookSource']):
    if colab_notebook_source is None:
      del self.colab_notebook_source
      return
    if not isinstance(colab_notebook_source, ColabNotebookSource):
      raise TypeError('colab_notebook_source must be of type ColabNotebookSource')
    self._colab_notebook_source = colab_notebook_source


class ExportKernelSessionForColabResponse(KaggleObject):
  r"""
  Attributes:
    warnings (str)
    colab_url (str)
  """

  def __init__(self):
    self._warnings = []
    self._colab_url = None
    self._freeze()

  @property
  def warnings(self) -> Optional[List[str]]:
    return self._warnings

  @warnings.setter
  def warnings(self, warnings: Optional[List[str]]):
    if warnings is None:
      del self.warnings
      return
    if not isinstance(warnings, list):
      raise TypeError('warnings must be of type list')
    if not all([isinstance(t, str) for t in warnings]):
      raise TypeError('warnings must contain only items of type str')
    self._warnings = warnings

  @property
  def colab_url(self) -> str:
    return self._colab_url or ""

  @colab_url.setter
  def colab_url(self, colab_url: Optional[str]):
    if colab_url is None:
      del self.colab_url
      return
    if not isinstance(colab_url, str):
      raise TypeError('colab_url must be of type str')
    self._colab_url = colab_url


class ExternalSourceData(KaggleObject):
  r"""
  Attributes:
    source_description (str)
      This is typically a url, but may also indicate that a file was uploaded.
    is_public (bool)
      The source is private for private github repos as well as file uploads.
  """

  def __init__(self):
    self._source_description = ""
    self._is_public = False
    self._freeze()

  @property
  def source_description(self) -> str:
    """This is typically a url, but may also indicate that a file was uploaded."""
    return self._source_description

  @source_description.setter
  def source_description(self, source_description: str):
    if source_description is None:
      del self.source_description
      return
    if not isinstance(source_description, str):
      raise TypeError('source_description must be of type str')
    self._source_description = source_description

  @property
  def is_public(self) -> bool:
    """The source is private for private github repos as well as file uploads."""
    return self._is_public

  @is_public.setter
  def is_public(self, is_public: bool):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public


class ExtraMountSettings(KaggleObject):
  r"""
  Attributes:
    dir (str)
    shared_volume_name (str)
    propagation (str)
    reset_signal (bool)
      If true, adds a MountData entry with reset_signal=true to this mount.
  """

  def __init__(self):
    self._dir = ""
    self._shared_volume_name = None
    self._propagation = None
    self._reset_signal = False
    self._freeze()

  @property
  def dir(self) -> str:
    return self._dir

  @dir.setter
  def dir(self, dir: str):
    if dir is None:
      del self.dir
      return
    if not isinstance(dir, str):
      raise TypeError('dir must be of type str')
    self._dir = dir

  @property
  def shared_volume_name(self) -> str:
    return self._shared_volume_name or ""

  @shared_volume_name.setter
  def shared_volume_name(self, shared_volume_name: Optional[str]):
    if shared_volume_name is None:
      del self.shared_volume_name
      return
    if not isinstance(shared_volume_name, str):
      raise TypeError('shared_volume_name must be of type str')
    self._shared_volume_name = shared_volume_name

  @property
  def propagation(self) -> str:
    return self._propagation or ""

  @propagation.setter
  def propagation(self, propagation: Optional[str]):
    if propagation is None:
      del self.propagation
      return
    if not isinstance(propagation, str):
      raise TypeError('propagation must be of type str')
    self._propagation = propagation

  @property
  def reset_signal(self) -> bool:
    """If true, adds a MountData entry with reset_signal=true to this mount."""
    return self._reset_signal

  @reset_signal.setter
  def reset_signal(self, reset_signal: bool):
    if reset_signal is None:
      del self.reset_signal
      return
    if not isinstance(reset_signal, bool):
      raise TypeError('reset_signal must be of type bool')
    self._reset_signal = reset_signal


class FetchAllColabContentRequest(KaggleObject):
  r"""
  Attributes:
    external_source_user_id (str)
    external_source_avatar_url (str)
  """

  def __init__(self):
    self._external_source_user_id = ""
    self._external_source_avatar_url = ""
    self._freeze()

  @property
  def external_source_user_id(self) -> str:
    return self._external_source_user_id

  @external_source_user_id.setter
  def external_source_user_id(self, external_source_user_id: str):
    if external_source_user_id is None:
      del self.external_source_user_id
      return
    if not isinstance(external_source_user_id, str):
      raise TypeError('external_source_user_id must be of type str')
    self._external_source_user_id = external_source_user_id

  @property
  def external_source_avatar_url(self) -> str:
    return self._external_source_avatar_url

  @external_source_avatar_url.setter
  def external_source_avatar_url(self, external_source_avatar_url: str):
    if external_source_avatar_url is None:
      del self.external_source_avatar_url
      return
    if not isinstance(external_source_avatar_url, str):
      raise TypeError('external_source_avatar_url must be of type str')
    self._external_source_avatar_url = external_source_avatar_url


class FetchColabContentRequest(KaggleObject):
  r"""
  Attributes:
    drive_id (str)
      Id associated with colab file in drive.
    kernel_id (int)
  """

  def __init__(self):
    self._drive_id = ""
    self._kernel_id = 0
    self._freeze()

  @property
  def drive_id(self) -> str:
    """Id associated with colab file in drive."""
    return self._drive_id

  @drive_id.setter
  def drive_id(self, drive_id: str):
    if drive_id is None:
      del self.drive_id
      return
    if not isinstance(drive_id, str):
      raise TypeError('drive_id must be of type str')
    self._drive_id = drive_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class FetchDriveContentResponse(KaggleObject):
  r"""
  Attributes:
    is_public (bool)
    mime_type (str)
    file_extension (str)
    file_name (str)
  """

  def __init__(self):
    self._is_public = False
    self._mime_type = ""
    self._file_extension = ""
    self._file_name = None
    self._freeze()

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
  def mime_type(self) -> str:
    return self._mime_type

  @mime_type.setter
  def mime_type(self, mime_type: str):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type

  @property
  def file_extension(self) -> str:
    return self._file_extension

  @file_extension.setter
  def file_extension(self, file_extension: str):
    if file_extension is None:
      del self.file_extension
      return
    if not isinstance(file_extension, str):
      raise TypeError('file_extension must be of type str')
    self._file_extension = file_extension

  @property
  def file_name(self) -> str:
    return self._file_name or ""

  @file_name.setter
  def file_name(self, file_name: Optional[str]):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name


class FetchExternalKernelContentRequest(KaggleObject):
  r"""
  Attributes:
    source_url (str)
  """

  def __init__(self):
    self._source_url = None
    self._freeze()

  @property
  def source_url(self) -> str:
    return self._source_url or ""

  @source_url.setter
  def source_url(self, source_url: Optional[str]):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    self._source_url = source_url


class FetchGitHubContentRequest(KaggleObject):
  r"""
  Attributes:
    owner (str)
      The owner of the repo. e.g. 'Kaggle'.
    repo (str)
      The name of the repo. e.g. 'docker-python'.
    path (str)
      The path of the file. e.g. 'README.md', 'directory/foo.txt' relative to the
      root of the repo.
    ref (str)
      The name of the commit/branch/tag
    kernel_id (int)
      Should be defined if reading Github Spec Information.
  """

  def __init__(self):
    self._owner = None
    self._repo = None
    self._path = None
    self._ref = None
    self._kernel_id = None
    self._freeze()

  @property
  def owner(self) -> str:
    """The owner of the repo. e.g. 'Kaggle'."""
    return self._owner or ""

  @owner.setter
  def owner(self, owner: Optional[str]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def repo(self) -> str:
    """The name of the repo. e.g. 'docker-python'."""
    return self._repo or ""

  @repo.setter
  def repo(self, repo: Optional[str]):
    if repo is None:
      del self.repo
      return
    if not isinstance(repo, str):
      raise TypeError('repo must be of type str')
    self._repo = repo

  @property
  def path(self) -> str:
    r"""
    The path of the file. e.g. 'README.md', 'directory/foo.txt' relative to the
    root of the repo.
    """
    return self._path or ""

  @path.setter
  def path(self, path: Optional[str]):
    if path is None:
      del self.path
      return
    if not isinstance(path, str):
      raise TypeError('path must be of type str')
    self._path = path

  @property
  def ref(self) -> str:
    """The name of the commit/branch/tag"""
    return self._ref or ""

  @ref.setter
  def ref(self, ref: Optional[str]):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def kernel_id(self) -> int:
    """Should be defined if reading Github Spec Information."""
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class FetchGitHubContentResponse(KaggleObject):
  r"""
  Attributes:
    content (str)
    is_public (bool)
    github_spec (GithubSpec)
  """

  def __init__(self):
    self._content = ""
    self._is_public = False
    self._github_spec = None
    self._freeze()

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

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
  def github_spec(self) -> Optional['GithubSpec']:
    return self._github_spec

  @github_spec.setter
  def github_spec(self, github_spec: Optional['GithubSpec']):
    if github_spec is None:
      del self.github_spec
      return
    if not isinstance(github_spec, GithubSpec):
      raise TypeError('github_spec must be of type GithubSpec')
    self._github_spec = github_spec


class GetAcceleratorQuotaStatisticsRequest(KaggleObject):
  r"""
  """

  pass

class GetAcceleratorQuotaStatisticsResponse(KaggleObject):
  r"""
  Attributes:
    quota_refresh_time (datetime)
    kernels_max_size_in_mb (int)
    tpu_quota (AcceleratorQuotaStatistics)
    gpu_quota (AcceleratorQuotaStatistics)
  """

  def __init__(self):
    self._quota_refresh_time = None
    self._kernels_max_size_in_mb = 0
    self._tpu_quota = None
    self._gpu_quota = None
    self._freeze()

  @property
  def quota_refresh_time(self) -> datetime:
    return self._quota_refresh_time

  @quota_refresh_time.setter
  def quota_refresh_time(self, quota_refresh_time: datetime):
    if quota_refresh_time is None:
      del self.quota_refresh_time
      return
    if not isinstance(quota_refresh_time, datetime):
      raise TypeError('quota_refresh_time must be of type datetime')
    self._quota_refresh_time = quota_refresh_time

  @property
  def kernels_max_size_in_mb(self) -> int:
    return self._kernels_max_size_in_mb

  @kernels_max_size_in_mb.setter
  def kernels_max_size_in_mb(self, kernels_max_size_in_mb: int):
    if kernels_max_size_in_mb is None:
      del self.kernels_max_size_in_mb
      return
    if not isinstance(kernels_max_size_in_mb, int):
      raise TypeError('kernels_max_size_in_mb must be of type int')
    self._kernels_max_size_in_mb = kernels_max_size_in_mb

  @property
  def tpu_quota(self) -> Optional['AcceleratorQuotaStatistics']:
    return self._tpu_quota

  @tpu_quota.setter
  def tpu_quota(self, tpu_quota: Optional['AcceleratorQuotaStatistics']):
    if tpu_quota is None:
      del self.tpu_quota
      return
    if not isinstance(tpu_quota, AcceleratorQuotaStatistics):
      raise TypeError('tpu_quota must be of type AcceleratorQuotaStatistics')
    self._tpu_quota = tpu_quota

  @property
  def gpu_quota(self) -> Optional['AcceleratorQuotaStatistics']:
    return self._gpu_quota

  @gpu_quota.setter
  def gpu_quota(self, gpu_quota: Optional['AcceleratorQuotaStatistics']):
    if gpu_quota is None:
      del self.gpu_quota
      return
    if not isinstance(gpu_quota, AcceleratorQuotaStatistics):
      raise TypeError('gpu_quota must be of type AcceleratorQuotaStatistics')
    self._gpu_quota = gpu_quota


class GetColabUserInfoRequest(KaggleObject):
  r"""
  """

  pass

class GetColabUserInfoResponse(KaggleObject):
  r"""
  Attributes:
    subscription_tier (ColabSubscriptionTier)
    paid_compute_units_balance (float)
    eligible_accelerators (EligibleAccelerator)
  """

  def __init__(self):
    self._subscription_tier = ColabSubscriptionTier.SUBSCRIPTION_TIER_UNSPECIFIED
    self._paid_compute_units_balance = 0.0
    self._eligible_accelerators = []
    self._freeze()

  @property
  def subscription_tier(self) -> 'ColabSubscriptionTier':
    return self._subscription_tier

  @subscription_tier.setter
  def subscription_tier(self, subscription_tier: 'ColabSubscriptionTier'):
    if subscription_tier is None:
      del self.subscription_tier
      return
    if not isinstance(subscription_tier, ColabSubscriptionTier):
      raise TypeError('subscription_tier must be of type ColabSubscriptionTier')
    self._subscription_tier = subscription_tier

  @property
  def paid_compute_units_balance(self) -> float:
    return self._paid_compute_units_balance

  @paid_compute_units_balance.setter
  def paid_compute_units_balance(self, paid_compute_units_balance: float):
    if paid_compute_units_balance is None:
      del self.paid_compute_units_balance
      return
    if not isinstance(paid_compute_units_balance, float):
      raise TypeError('paid_compute_units_balance must be of type float')
    self._paid_compute_units_balance = paid_compute_units_balance

  @property
  def eligible_accelerators(self) -> Optional[List[Optional['EligibleAccelerator']]]:
    return self._eligible_accelerators

  @eligible_accelerators.setter
  def eligible_accelerators(self, eligible_accelerators: Optional[List[Optional['EligibleAccelerator']]]):
    if eligible_accelerators is None:
      del self.eligible_accelerators
      return
    if not isinstance(eligible_accelerators, list):
      raise TypeError('eligible_accelerators must be of type list')
    if not all([isinstance(t, EligibleAccelerator) for t in eligible_accelerators]):
      raise TypeError('eligible_accelerators must contain only items of type EligibleAccelerator')
    self._eligible_accelerators = eligible_accelerators


class GetCompetitionsPaneInfoRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    competition_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._competition_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class GetCompetitionsPaneInfoResponse(KaggleObject):
  r"""
  Attributes:
    best_kernel_session_score (KernelSessionScore)
    latest_kernel_session_score (KernelSessionScore)
    daily_submission_info (DailySubmissionInfo)
  """

  def __init__(self):
    self._best_kernel_session_score = None
    self._latest_kernel_session_score = None
    self._daily_submission_info = None
    self._freeze()

  @property
  def best_kernel_session_score(self) -> Optional['KernelSessionScore']:
    return self._best_kernel_session_score

  @best_kernel_session_score.setter
  def best_kernel_session_score(self, best_kernel_session_score: Optional['KernelSessionScore']):
    if best_kernel_session_score is None:
      del self.best_kernel_session_score
      return
    if not isinstance(best_kernel_session_score, KernelSessionScore):
      raise TypeError('best_kernel_session_score must be of type KernelSessionScore')
    self._best_kernel_session_score = best_kernel_session_score

  @property
  def latest_kernel_session_score(self) -> Optional['KernelSessionScore']:
    return self._latest_kernel_session_score

  @latest_kernel_session_score.setter
  def latest_kernel_session_score(self, latest_kernel_session_score: Optional['KernelSessionScore']):
    if latest_kernel_session_score is None:
      del self.latest_kernel_session_score
      return
    if not isinstance(latest_kernel_session_score, KernelSessionScore):
      raise TypeError('latest_kernel_session_score must be of type KernelSessionScore')
    self._latest_kernel_session_score = latest_kernel_session_score

  @property
  def daily_submission_info(self) -> Optional['DailySubmissionInfo']:
    return self._daily_submission_info

  @daily_submission_info.setter
  def daily_submission_info(self, daily_submission_info: Optional['DailySubmissionInfo']):
    if daily_submission_info is None:
      del self.daily_submission_info
      return
    if not isinstance(daily_submission_info, DailySubmissionInfo):
      raise TypeError('daily_submission_info must be of type DailySubmissionInfo')
    self._daily_submission_info = daily_submission_info


class GetDefaultSessionSettingsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetDeletedKernelRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetDeletedKernelResponse(KaggleObject):
  r"""
  Attributes:
    default_datasource_image_url (str)
    default_user_image_url (str)
    deleted_kernel_url (str)
    topic_id (int)
    comment_count (int)
    user_can_downvote_comments (bool)
  """

  def __init__(self):
    self._default_datasource_image_url = None
    self._default_user_image_url = None
    self._deleted_kernel_url = None
    self._topic_id = None
    self._comment_count = 0
    self._user_can_downvote_comments = False
    self._freeze()

  @property
  def default_datasource_image_url(self) -> str:
    return self._default_datasource_image_url or ""

  @default_datasource_image_url.setter
  def default_datasource_image_url(self, default_datasource_image_url: Optional[str]):
    if default_datasource_image_url is None:
      del self.default_datasource_image_url
      return
    if not isinstance(default_datasource_image_url, str):
      raise TypeError('default_datasource_image_url must be of type str')
    self._default_datasource_image_url = default_datasource_image_url

  @property
  def default_user_image_url(self) -> str:
    return self._default_user_image_url or ""

  @default_user_image_url.setter
  def default_user_image_url(self, default_user_image_url: Optional[str]):
    if default_user_image_url is None:
      del self.default_user_image_url
      return
    if not isinstance(default_user_image_url, str):
      raise TypeError('default_user_image_url must be of type str')
    self._default_user_image_url = default_user_image_url

  @property
  def deleted_kernel_url(self) -> str:
    return self._deleted_kernel_url or ""

  @deleted_kernel_url.setter
  def deleted_kernel_url(self, deleted_kernel_url: Optional[str]):
    if deleted_kernel_url is None:
      del self.deleted_kernel_url
      return
    if not isinstance(deleted_kernel_url, str):
      raise TypeError('deleted_kernel_url must be of type str')
    self._deleted_kernel_url = deleted_kernel_url

  @property
  def topic_id(self) -> int:
    return self._topic_id or 0

  @topic_id.setter
  def topic_id(self, topic_id: Optional[int]):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def comment_count(self) -> int:
    return self._comment_count

  @comment_count.setter
  def comment_count(self, comment_count: int):
    if comment_count is None:
      del self.comment_count
      return
    if not isinstance(comment_count, int):
      raise TypeError('comment_count must be of type int')
    self._comment_count = comment_count

  @property
  def user_can_downvote_comments(self) -> bool:
    return self._user_can_downvote_comments

  @user_can_downvote_comments.setter
  def user_can_downvote_comments(self, user_can_downvote_comments: bool):
    if user_can_downvote_comments is None:
      del self.user_can_downvote_comments
      return
    if not isinstance(user_can_downvote_comments, bool):
      raise TypeError('user_can_downvote_comments must be of type bool')
    self._user_can_downvote_comments = user_can_downvote_comments


class GetFirebaseAuthTokenRequest(KaggleObject):
  r"""
  """

  pass

class GetFirebaseAuthTokenResponse(KaggleObject):
  r"""
  Attributes:
    auth_token (str)
  """

  def __init__(self):
    self._auth_token = ""
    self._freeze()

  @property
  def auth_token(self) -> str:
    return self._auth_token

  @auth_token.setter
  def auth_token(self, auth_token: str):
    if auth_token is None:
      del self.auth_token
      return
    if not isinstance(auth_token, str):
      raise TypeError('auth_token must be of type str')
    self._auth_token = auth_token


class GetFirebaseConfigRequest(KaggleObject):
  r"""
  """

  pass

class GetFirebaseConfigResponse(KaggleObject):
  r"""
  Attributes:
    api_key (str)
    auth_domain (str)
    database_url (str)
    project_id (str)
    storage_bucket (str)
    messaging_sender_id (str)
    app_id (str)
    proxy_domain (str)
  """

  def __init__(self):
    self._api_key = ""
    self._auth_domain = ""
    self._database_url = ""
    self._project_id = ""
    self._storage_bucket = ""
    self._messaging_sender_id = ""
    self._app_id = ""
    self._proxy_domain = ""
    self._freeze()

  @property
  def api_key(self) -> str:
    return self._api_key

  @api_key.setter
  def api_key(self, api_key: str):
    if api_key is None:
      del self.api_key
      return
    if not isinstance(api_key, str):
      raise TypeError('api_key must be of type str')
    self._api_key = api_key

  @property
  def auth_domain(self) -> str:
    return self._auth_domain

  @auth_domain.setter
  def auth_domain(self, auth_domain: str):
    if auth_domain is None:
      del self.auth_domain
      return
    if not isinstance(auth_domain, str):
      raise TypeError('auth_domain must be of type str')
    self._auth_domain = auth_domain

  @property
  def database_url(self) -> str:
    return self._database_url

  @database_url.setter
  def database_url(self, database_url: str):
    if database_url is None:
      del self.database_url
      return
    if not isinstance(database_url, str):
      raise TypeError('database_url must be of type str')
    self._database_url = database_url

  @property
  def project_id(self) -> str:
    return self._project_id

  @project_id.setter
  def project_id(self, project_id: str):
    if project_id is None:
      del self.project_id
      return
    if not isinstance(project_id, str):
      raise TypeError('project_id must be of type str')
    self._project_id = project_id

  @property
  def storage_bucket(self) -> str:
    return self._storage_bucket

  @storage_bucket.setter
  def storage_bucket(self, storage_bucket: str):
    if storage_bucket is None:
      del self.storage_bucket
      return
    if not isinstance(storage_bucket, str):
      raise TypeError('storage_bucket must be of type str')
    self._storage_bucket = storage_bucket

  @property
  def messaging_sender_id(self) -> str:
    return self._messaging_sender_id

  @messaging_sender_id.setter
  def messaging_sender_id(self, messaging_sender_id: str):
    if messaging_sender_id is None:
      del self.messaging_sender_id
      return
    if not isinstance(messaging_sender_id, str):
      raise TypeError('messaging_sender_id must be of type str')
    self._messaging_sender_id = messaging_sender_id

  @property
  def app_id(self) -> str:
    return self._app_id

  @app_id.setter
  def app_id(self, app_id: str):
    if app_id is None:
      del self.app_id
      return
    if not isinstance(app_id, str):
      raise TypeError('app_id must be of type str')
    self._app_id = app_id

  @property
  def proxy_domain(self) -> str:
    return self._proxy_domain

  @proxy_domain.setter
  def proxy_domain(self, proxy_domain: str):
    if proxy_domain is None:
      del self.proxy_domain
      return
    if not isinstance(proxy_domain, str):
      raise TypeError('proxy_domain must be of type str')
    self._proxy_domain = proxy_domain


class GetKernelCategoryIdsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetKernelEmbedResponse(KaggleObject):
  r"""
  Attributes:
    ipynb_content (str)
    rendered_output_url (str)
    viewer_url (str)
  """

  def __init__(self):
    self._ipynb_content = None
    self._rendered_output_url = None
    self._viewer_url = ""
    self._freeze()

  @property
  def ipynb_content(self) -> str:
    return self._ipynb_content or ""

  @ipynb_content.setter
  def ipynb_content(self, ipynb_content: Optional[str]):
    if ipynb_content is None:
      del self.ipynb_content
      return
    if not isinstance(ipynb_content, str):
      raise TypeError('ipynb_content must be of type str')
    self._ipynb_content = ipynb_content

  @property
  def rendered_output_url(self) -> str:
    return self._rendered_output_url or ""

  @rendered_output_url.setter
  def rendered_output_url(self, rendered_output_url: Optional[str]):
    if rendered_output_url is None:
      del self.rendered_output_url
      return
    if not isinstance(rendered_output_url, str):
      raise TypeError('rendered_output_url must be of type str')
    self._rendered_output_url = rendered_output_url

  @property
  def viewer_url(self) -> str:
    return self._viewer_url

  @viewer_url.setter
  def viewer_url(self, viewer_url: str):
    if viewer_url is None:
      del self.viewer_url
      return
    if not isinstance(viewer_url, str):
      raise TypeError('viewer_url must be of type str')
    self._viewer_url = viewer_url


class GetKernelGitHubSettingsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetKernelGitHubSettingsResponse(KaggleObject):
  r"""
  Attributes:
    github_login (str)
    repositories (GithubRepositoryInfo)
    branches (GithubBranchInfo)
    last_settings (GitHubSaveRequest)
  """

  def __init__(self):
    self._github_login = ""
    self._repositories = []
    self._branches = []
    self._last_settings = None
    self._freeze()

  @property
  def github_login(self) -> str:
    return self._github_login

  @github_login.setter
  def github_login(self, github_login: str):
    if github_login is None:
      del self.github_login
      return
    if not isinstance(github_login, str):
      raise TypeError('github_login must be of type str')
    self._github_login = github_login

  @property
  def repositories(self) -> Optional[List[Optional['GithubRepositoryInfo']]]:
    return self._repositories

  @repositories.setter
  def repositories(self, repositories: Optional[List[Optional['GithubRepositoryInfo']]]):
    if repositories is None:
      del self.repositories
      return
    if not isinstance(repositories, list):
      raise TypeError('repositories must be of type list')
    if not all([isinstance(t, GithubRepositoryInfo) for t in repositories]):
      raise TypeError('repositories must contain only items of type GithubRepositoryInfo')
    self._repositories = repositories

  @property
  def branches(self) -> Optional[List[Optional['GithubBranchInfo']]]:
    return self._branches

  @branches.setter
  def branches(self, branches: Optional[List[Optional['GithubBranchInfo']]]):
    if branches is None:
      del self.branches
      return
    if not isinstance(branches, list):
      raise TypeError('branches must be of type list')
    if not all([isinstance(t, GithubBranchInfo) for t in branches]):
      raise TypeError('branches must contain only items of type GithubBranchInfo')
    self._branches = branches

  @property
  def last_settings(self) -> Optional['GitHubSaveRequest']:
    return self._last_settings

  @last_settings.setter
  def last_settings(self, last_settings: Optional['GitHubSaveRequest']):
    if last_settings is None:
      del self.last_settings
      return
    if not isinstance(last_settings, GitHubSaveRequest):
      raise TypeError('last_settings must be of type GitHubSaveRequest')
    self._last_settings = last_settings


class GetKernelIdByUrlRequest(KaggleObject):
  r"""
  Attributes:
    url (str)
      Expects a notebook viewer URL, ex:
      https://www.kaggle.com/code/alexisbcook/titanic-tutorial?scriptVersionId=123456
  """

  def __init__(self):
    self._url = ""
    self._freeze()

  @property
  def url(self) -> str:
    r"""
    Expects a notebook viewer URL, ex:
    https://www.kaggle.com/code/alexisbcook/titanic-tutorial?scriptVersionId=123456
    """
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class GetKernelIdByUrlResponse(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetKernelLandingPageRequest(KaggleObject):
  r"""
  """

  pass

class GetKernelLandingPageResponse(KaggleObject):
  r"""
  Attributes:
    shelves (KernelShelf)
    total_public_kernels (int)
  """

  def __init__(self):
    self._shelves = []
    self._total_public_kernels = 0
    self._freeze()

  @property
  def shelves(self) -> Optional[List[Optional['KernelShelf']]]:
    return self._shelves

  @shelves.setter
  def shelves(self, shelves: Optional[List[Optional['KernelShelf']]]):
    if shelves is None:
      del self.shelves
      return
    if not isinstance(shelves, list):
      raise TypeError('shelves must be of type list')
    if not all([isinstance(t, KernelShelf) for t in shelves]):
      raise TypeError('shelves must contain only items of type KernelShelf')
    self._shelves = shelves

  @property
  def total_public_kernels(self) -> int:
    return self._total_public_kernels

  @total_public_kernels.setter
  def total_public_kernels(self, total_public_kernels: int):
    if total_public_kernels is None:
      del self.total_public_kernels
      return
    if not isinstance(total_public_kernels, int):
      raise TypeError('total_public_kernels must be of type int')
    self._total_public_kernels = total_public_kernels


class GetKernelRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    username (str)
      TODO: Switch to just `kernel_id` after making sure they are unused.
    slug (str)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._kernel_id = None
    self._username = None
    self._slug = None
    self._read_mask = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def username(self) -> str:
    """TODO: Switch to just `kernel_id` after making sure they are unused."""
    return self._username or ""

  @username.setter
  def username(self, username: Optional[str]):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetKernelSessionDataSourcesRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    include_output_files (bool)
    hierarchical_output_files (bool)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._include_output_files = False
    self._hierarchical_output_files = False
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

  @property
  def include_output_files(self) -> bool:
    return self._include_output_files

  @include_output_files.setter
  def include_output_files(self, include_output_files: bool):
    if include_output_files is None:
      del self.include_output_files
      return
    if not isinstance(include_output_files, bool):
      raise TypeError('include_output_files must be of type bool')
    self._include_output_files = include_output_files

  @property
  def hierarchical_output_files(self) -> bool:
    return self._hierarchical_output_files

  @hierarchical_output_files.setter
  def hierarchical_output_files(self, hierarchical_output_files: bool):
    if hierarchical_output_files is None:
      del self.hierarchical_output_files
      return
    if not isinstance(hierarchical_output_files, bool):
      raise TypeError('hierarchical_output_files must be of type bool')
    self._hierarchical_output_files = hierarchical_output_files


class GetKernelSessionDataSourcesResponse(KaggleObject):
  r"""
  Attributes:
    data_sources (DataSource)
  """

  def __init__(self):
    self._data_sources = []
    self._freeze()

  @property
  def data_sources(self) -> Optional[List[Optional['DataSource']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSource']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSource) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSource')
    self._data_sources = data_sources


class GetKernelSessionLogRequest(KaggleObject):
  r"""
  Attributes:
    session_id (int)
  """

  def __init__(self):
    self._session_id = 0
    self._freeze()

  @property
  def session_id(self) -> int:
    return self._session_id

  @session_id.setter
  def session_id(self, session_id: int):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id


class GetKernelSessionModelSourcesRequest(KaggleObject):
  r"""
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


class GetKernelSessionModelSourcesResponse(KaggleObject):
  r"""
  Attributes:
    model_sources (ModelSource)
  """

  def __init__(self):
    self._model_sources = []
    self._freeze()

  @property
  def model_sources(self) -> Optional[List[Optional['ModelSource']]]:
    return self._model_sources

  @model_sources.setter
  def model_sources(self, model_sources: Optional[List[Optional['ModelSource']]]):
    if model_sources is None:
      del self.model_sources
      return
    if not isinstance(model_sources, list):
      raise TypeError('model_sources must be of type list')
    if not all([isinstance(t, ModelSource) for t in model_sources]):
      raise TypeError('model_sources must contain only items of type ModelSource')
    self._model_sources = model_sources


class GetKernelSessionResourceReferencesRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    read_mask (FieldMask)
    resource_reference_type_filter (ResourceReferenceType)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._read_mask = None
    self._resource_reference_type_filter = None
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

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask

  @property
  def resource_reference_type_filter(self) -> 'ResourceReferenceType':
    return self._resource_reference_type_filter or ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED

  @resource_reference_type_filter.setter
  def resource_reference_type_filter(self, resource_reference_type_filter: Optional['ResourceReferenceType']):
    if resource_reference_type_filter is None:
      del self.resource_reference_type_filter
      return
    if not isinstance(resource_reference_type_filter, ResourceReferenceType):
      raise TypeError('resource_reference_type_filter must be of type ResourceReferenceType')
    self._resource_reference_type_filter = resource_reference_type_filter


class GetKernelSessionResourceReferencesResponse(KaggleObject):
  r"""
  Attributes:
    resource_references (ResourceReference)
  """

  def __init__(self):
    self._resource_references = []
    self._freeze()

  @property
  def resource_references(self) -> Optional[List[Optional['ResourceReference']]]:
    return self._resource_references

  @resource_references.setter
  def resource_references(self, resource_references: Optional[List[Optional['ResourceReference']]]):
    if resource_references is None:
      del self.resource_references
      return
    if not isinstance(resource_references, list):
      raise TypeError('resource_references must be of type list')
    if not all([isinstance(t, ResourceReference) for t in resource_references]):
      raise TypeError('resource_references must contain only items of type ResourceReference')
    self._resource_references = resource_references


class GetKernelSessionSourceRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    include_output_if_available (bool)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._include_output_if_available = False
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

  @property
  def include_output_if_available(self) -> bool:
    return self._include_output_if_available

  @include_output_if_available.setter
  def include_output_if_available(self, include_output_if_available: bool):
    if include_output_if_available is None:
      del self.include_output_if_available
      return
    if not isinstance(include_output_if_available, bool):
      raise TypeError('include_output_if_available must be of type bool')
    self._include_output_if_available = include_output_if_available


class GetKernelStatusRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    existing_status (KernelWorkerStatus)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._existing_status = None
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

  @property
  def existing_status(self) -> 'KernelWorkerStatus':
    return self._existing_status or KernelWorkerStatus.QUEUED

  @existing_status.setter
  def existing_status(self, existing_status: Optional['KernelWorkerStatus']):
    if existing_status is None:
      del self.existing_status
      return
    if not isinstance(existing_status, KernelWorkerStatus):
      raise TypeError('existing_status must be of type KernelWorkerStatus')
    self._existing_status = existing_status


class GetKernelStatusResponse(KaggleObject):
  r"""
  Attributes:
    status (KernelWorkerStatus)
  """

  def __init__(self):
    self._status = KernelWorkerStatus.QUEUED
    self._freeze()

  @property
  def status(self) -> 'KernelWorkerStatus':
    return self._status

  @status.setter
  def status(self, status: 'KernelWorkerStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, KernelWorkerStatus):
      raise TypeError('status must be of type KernelWorkerStatus')
    self._status = status


class GetKernelVersionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    get_data_sources (bool)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._get_data_sources = None
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

  @property
  def get_data_sources(self) -> bool:
    return self._get_data_sources or False

  @get_data_sources.setter
  def get_data_sources(self, get_data_sources: Optional[bool]):
    if get_data_sources is None:
      del self.get_data_sources
      return
    if not isinstance(get_data_sources, bool):
      raise TypeError('get_data_sources must be of type bool')
    self._get_data_sources = get_data_sources


class GetKernelVersionResponse(KaggleObject):
  r"""
  Attributes:
    kernel_version_and_run (KernelVersionAndRun)
  """

  def __init__(self):
    self._kernel_version_and_run = None
    self._freeze()

  @property
  def kernel_version_and_run(self) -> Optional['KernelVersionAndRun']:
    return self._kernel_version_and_run

  @kernel_version_and_run.setter
  def kernel_version_and_run(self, kernel_version_and_run: Optional['KernelVersionAndRun']):
    if kernel_version_and_run is None:
      del self.kernel_version_and_run
      return
    if not isinstance(kernel_version_and_run, KernelVersionAndRun):
      raise TypeError('kernel_version_and_run must be of type KernelVersionAndRun')
    self._kernel_version_and_run = kernel_version_and_run


class GetOrCreateKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    use_new_scope (bool)
      Determines if a new Container scope will be used.
      If it is false, a new scope is not created, and all operations are tracked
      together. This is required in order to have the KernelSession created
      within a transaction. If it is true, or null, a new scope will be created.
      This is useful when you require separate scopes, like for parallel
      processing.
  """

  def __init__(self):
    self._kernel_id = 0
    self._use_new_scope = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def use_new_scope(self) -> bool:
    r"""
    Determines if a new Container scope will be used.
    If it is false, a new scope is not created, and all operations are tracked
    together. This is required in order to have the KernelSession created
    within a transaction. If it is true, or null, a new scope will be created.
    This is useful when you require separate scopes, like for parallel
    processing.
    """
    return self._use_new_scope or False

  @use_new_scope.setter
  def use_new_scope(self, use_new_scope: Optional[bool]):
    if use_new_scope is None:
      del self.use_new_scope
      return
    if not isinstance(use_new_scope, bool):
      raise TypeError('use_new_scope must be of type bool')
    self._use_new_scope = use_new_scope


class GetOrCreateKernelSessionResponse(KaggleObject):
  r"""
  Attributes:
    draft (KernelDraft)
    session_id (int)
    session_timeout_seconds (int)
    session_creation_failure_message (str)
    has_more_recent_collaborator_version (bool)
    session_status (KernelWorkerStatus)
    enable_lsp (bool)
    verification_redirect_url (str)
      If set, the frontend should redirect the user to this URL for verification
      (phone or identity) before allowing access to the notebook editor.
  """

  def __init__(self):
    self._draft = None
    self._session_id = None
    self._session_timeout_seconds = 0
    self._session_creation_failure_message = None
    self._has_more_recent_collaborator_version = False
    self._session_status = None
    self._enable_lsp = None
    self._verification_redirect_url = None
    self._freeze()

  @property
  def draft(self) -> Optional['KernelDraft']:
    return self._draft

  @draft.setter
  def draft(self, draft: Optional['KernelDraft']):
    if draft is None:
      del self.draft
      return
    if not isinstance(draft, KernelDraft):
      raise TypeError('draft must be of type KernelDraft')
    self._draft = draft

  @property
  def session_id(self) -> int:
    return self._session_id or 0

  @session_id.setter
  def session_id(self, session_id: Optional[int]):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id

  @property
  def session_timeout_seconds(self) -> int:
    return self._session_timeout_seconds

  @session_timeout_seconds.setter
  def session_timeout_seconds(self, session_timeout_seconds: int):
    if session_timeout_seconds is None:
      del self.session_timeout_seconds
      return
    if not isinstance(session_timeout_seconds, int):
      raise TypeError('session_timeout_seconds must be of type int')
    self._session_timeout_seconds = session_timeout_seconds

  @property
  def session_creation_failure_message(self) -> str:
    return self._session_creation_failure_message or ""

  @session_creation_failure_message.setter
  def session_creation_failure_message(self, session_creation_failure_message: Optional[str]):
    if session_creation_failure_message is None:
      del self.session_creation_failure_message
      return
    if not isinstance(session_creation_failure_message, str):
      raise TypeError('session_creation_failure_message must be of type str')
    self._session_creation_failure_message = session_creation_failure_message

  @property
  def has_more_recent_collaborator_version(self) -> bool:
    return self._has_more_recent_collaborator_version

  @has_more_recent_collaborator_version.setter
  def has_more_recent_collaborator_version(self, has_more_recent_collaborator_version: bool):
    if has_more_recent_collaborator_version is None:
      del self.has_more_recent_collaborator_version
      return
    if not isinstance(has_more_recent_collaborator_version, bool):
      raise TypeError('has_more_recent_collaborator_version must be of type bool')
    self._has_more_recent_collaborator_version = has_more_recent_collaborator_version

  @property
  def session_status(self) -> 'KernelWorkerStatus':
    return self._session_status or KernelWorkerStatus.QUEUED

  @session_status.setter
  def session_status(self, session_status: Optional['KernelWorkerStatus']):
    if session_status is None:
      del self.session_status
      return
    if not isinstance(session_status, KernelWorkerStatus):
      raise TypeError('session_status must be of type KernelWorkerStatus')
    self._session_status = session_status

  @property
  def enable_lsp(self) -> bool:
    return self._enable_lsp or False

  @enable_lsp.setter
  def enable_lsp(self, enable_lsp: Optional[bool]):
    if enable_lsp is None:
      del self.enable_lsp
      return
    if not isinstance(enable_lsp, bool):
      raise TypeError('enable_lsp must be of type bool')
    self._enable_lsp = enable_lsp

  @property
  def verification_redirect_url(self) -> str:
    r"""
    If set, the frontend should redirect the user to this URL for verification
    (phone or identity) before allowing access to the notebook editor.
    """
    return self._verification_redirect_url or ""

  @verification_redirect_url.setter
  def verification_redirect_url(self, verification_redirect_url: Optional[str]):
    if verification_redirect_url is None:
      del self.verification_redirect_url
      return
    if not isinstance(verification_redirect_url, str):
      raise TypeError('verification_redirect_url must be of type str')
    self._verification_redirect_url = verification_redirect_url


class GetPackageRequirementsUpdateUrlRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    content_length (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._content_length = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length


class GetPackageRequirementsUpdateUrlResponse(KaggleObject):
  r"""
  Attributes:
    signed_url (str)
  """

  def __init__(self):
    self._signed_url = ""
    self._freeze()

  @property
  def signed_url(self) -> str:
    return self._signed_url

  @signed_url.setter
  def signed_url(self, signed_url: str):
    if signed_url is None:
      del self.signed_url
      return
    if not isinstance(signed_url, str):
      raise TypeError('signed_url must be of type str')
    self._signed_url = signed_url


class GetPackageRequirementsViewUrlRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetPackageRequirementsViewUrlResponse(KaggleObject):
  r"""
  Attributes:
    signed_url (str)
  """

  def __init__(self):
    self._signed_url = None
    self._freeze()

  @property
  def signed_url(self) -> str:
    return self._signed_url or ""

  @signed_url.setter
  def signed_url(self, signed_url: Optional[str]):
    if signed_url is None:
      del self.signed_url
      return
    if not isinstance(signed_url, str):
      raise TypeError('signed_url must be of type str')
    self._signed_url = signed_url


class GetResourceReferenceByIdRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._id = 0
    self._read_mask = None
    self._freeze()

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
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetResourceReferenceRequest(KaggleObject):
  r"""
  Attributes:
    identifier (ResourceReferenceIdentifier)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._identifier = None
    self._read_mask = None
    self._freeze()

  @property
  def identifier(self) -> Optional['ResourceReferenceIdentifier']:
    return self._identifier

  @identifier.setter
  def identifier(self, identifier: Optional['ResourceReferenceIdentifier']):
    if identifier is None:
      del self.identifier
      return
    if not isinstance(identifier, ResourceReferenceIdentifier):
      raise TypeError('identifier must be of type ResourceReferenceIdentifier')
    self._identifier = identifier

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetScheduledKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetScheduledKernelSessionResponse(KaggleObject):
  r"""
  Attributes:
    session (ScheduledKernelSession)
  """

  def __init__(self):
    self._session = None
    self._freeze()

  @property
  def session(self) -> Optional['ScheduledKernelSession']:
    return self._session

  @session.setter
  def session(self, session: Optional['ScheduledKernelSession']):
    if session is None:
      del self.session
      return
    if not isinstance(session, ScheduledKernelSession):
      raise TypeError('session must be of type ScheduledKernelSession')
    self._session = session


class GetUserKernelAchievementsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    kernel_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._kernel_id = None
    self._freeze()

  @property
  def user_id(self) -> int:
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
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetUserKernelAchievementsResponse(KaggleObject):
  r"""
  Attributes:
    total_upvotes (int)
    total_kernels (int)
    total_forks (int)
    weekly_forks (int)
  """

  def __init__(self):
    self._total_upvotes = 0
    self._total_kernels = 0
    self._total_forks = 0
    self._weekly_forks = 0
    self._freeze()

  @property
  def total_upvotes(self) -> int:
    return self._total_upvotes

  @total_upvotes.setter
  def total_upvotes(self, total_upvotes: int):
    if total_upvotes is None:
      del self.total_upvotes
      return
    if not isinstance(total_upvotes, int):
      raise TypeError('total_upvotes must be of type int')
    self._total_upvotes = total_upvotes

  @property
  def total_kernels(self) -> int:
    return self._total_kernels

  @total_kernels.setter
  def total_kernels(self, total_kernels: int):
    if total_kernels is None:
      del self.total_kernels
      return
    if not isinstance(total_kernels, int):
      raise TypeError('total_kernels must be of type int')
    self._total_kernels = total_kernels

  @property
  def total_forks(self) -> int:
    return self._total_forks

  @total_forks.setter
  def total_forks(self, total_forks: int):
    if total_forks is None:
      del self.total_forks
      return
    if not isinstance(total_forks, int):
      raise TypeError('total_forks must be of type int')
    self._total_forks = total_forks

  @property
  def weekly_forks(self) -> int:
    return self._weekly_forks

  @weekly_forks.setter
  def weekly_forks(self, weekly_forks: int):
    if weekly_forks is None:
      del self.weekly_forks
      return
    if not isinstance(weekly_forks, int):
      raise TypeError('weekly_forks must be of type int')
    self._weekly_forks = weekly_forks


class GithubBranchInfo(KaggleObject):
  r"""
  Attributes:
    name (str)
      The name of the branch. e.g. 'master'.
  """

  def __init__(self):
    self._name = ""
    self._freeze()

  @property
  def name(self) -> str:
    """The name of the branch. e.g. 'master'."""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


class GithubFileInfo(KaggleObject):
  r"""
  Attributes:
    owner (str)
      The owner of the repo. e.g. 'Kaggle'.
    repo (str)
      The name of the repo. e.g. 'docker-python'.
    path (str)
      The path of the file. e.g. 'README.md', 'directory/foo.txt' relative to the
      root of the repo.
    ref (str)
      The name of the commit/branch/tag
    raw_url (str)
      The URL pointing to the raw file. e.g.
      'https://raw.githubusercontent.com/Kaggle/docker-python/master/Dockerfile'.
    size (int)
      The size of the file in binary (ex: 1024 bytes = 1 KB)
  """

  def __init__(self):
    self._owner = ""
    self._repo = ""
    self._path = ""
    self._ref = ""
    self._raw_url = ""
    self._size = None
    self._freeze()

  @property
  def owner(self) -> str:
    """The owner of the repo. e.g. 'Kaggle'."""
    return self._owner

  @owner.setter
  def owner(self, owner: str):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def repo(self) -> str:
    """The name of the repo. e.g. 'docker-python'."""
    return self._repo

  @repo.setter
  def repo(self, repo: str):
    if repo is None:
      del self.repo
      return
    if not isinstance(repo, str):
      raise TypeError('repo must be of type str')
    self._repo = repo

  @property
  def path(self) -> str:
    r"""
    The path of the file. e.g. 'README.md', 'directory/foo.txt' relative to the
    root of the repo.
    """
    return self._path

  @path.setter
  def path(self, path: str):
    if path is None:
      del self.path
      return
    if not isinstance(path, str):
      raise TypeError('path must be of type str')
    self._path = path

  @property
  def ref(self) -> str:
    """The name of the commit/branch/tag"""
    return self._ref

  @ref.setter
  def ref(self, ref: str):
    if ref is None:
      del self.ref
      return
    if not isinstance(ref, str):
      raise TypeError('ref must be of type str')
    self._ref = ref

  @property
  def raw_url(self) -> str:
    r"""
    The URL pointing to the raw file. e.g.
    'https://raw.githubusercontent.com/Kaggle/docker-python/master/Dockerfile'.
    """
    return self._raw_url

  @raw_url.setter
  def raw_url(self, raw_url: str):
    if raw_url is None:
      del self.raw_url
      return
    if not isinstance(raw_url, str):
      raise TypeError('raw_url must be of type str')
    self._raw_url = raw_url

  @property
  def size(self) -> int:
    """The size of the file in binary (ex: 1024 bytes = 1 KB)"""
    return self._size or 0

  @size.setter
  def size(self, size: Optional[int]):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size


class GithubRepositoryInfo(KaggleObject):
  r"""
  Attributes:
    owner (str)
      The owner of the repo. e.g. 'Kaggle'.
    name (str)
      The name of the repo. e.g. 'docker-python'.
    default_branch (str)
      The default branch of the repo. e.g. 'master'.
  """

  def __init__(self):
    self._owner = ""
    self._name = ""
    self._default_branch = ""
    self._freeze()

  @property
  def owner(self) -> str:
    """The owner of the repo. e.g. 'Kaggle'."""
    return self._owner

  @owner.setter
  def owner(self, owner: str):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def name(self) -> str:
    """The name of the repo. e.g. 'docker-python'."""
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
  def default_branch(self) -> str:
    """The default branch of the repo. e.g. 'master'."""
    return self._default_branch

  @default_branch.setter
  def default_branch(self, default_branch: str):
    if default_branch is None:
      del self.default_branch
      return
    if not isinstance(default_branch, str):
      raise TypeError('default_branch must be of type str')
    self._default_branch = default_branch


class GitHubSaveRequest(KaggleObject):
  r"""
  Attributes:
    repository_owner (str)
    repository_name (str)
    branch (str)
    file_name (str)
    commit_message (str)
    include_kaggle_badge (bool)
  """

  def __init__(self):
    self._repository_owner = ""
    self._repository_name = ""
    self._branch = ""
    self._file_name = ""
    self._commit_message = ""
    self._include_kaggle_badge = False
    self._freeze()

  @property
  def repository_owner(self) -> str:
    return self._repository_owner

  @repository_owner.setter
  def repository_owner(self, repository_owner: str):
    if repository_owner is None:
      del self.repository_owner
      return
    if not isinstance(repository_owner, str):
      raise TypeError('repository_owner must be of type str')
    self._repository_owner = repository_owner

  @property
  def repository_name(self) -> str:
    return self._repository_name

  @repository_name.setter
  def repository_name(self, repository_name: str):
    if repository_name is None:
      del self.repository_name
      return
    if not isinstance(repository_name, str):
      raise TypeError('repository_name must be of type str')
    self._repository_name = repository_name

  @property
  def branch(self) -> str:
    return self._branch

  @branch.setter
  def branch(self, branch: str):
    if branch is None:
      del self.branch
      return
    if not isinstance(branch, str):
      raise TypeError('branch must be of type str')
    self._branch = branch

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def commit_message(self) -> str:
    return self._commit_message

  @commit_message.setter
  def commit_message(self, commit_message: str):
    if commit_message is None:
      del self.commit_message
      return
    if not isinstance(commit_message, str):
      raise TypeError('commit_message must be of type str')
    self._commit_message = commit_message

  @property
  def include_kaggle_badge(self) -> bool:
    return self._include_kaggle_badge

  @include_kaggle_badge.setter
  def include_kaggle_badge(self, include_kaggle_badge: bool):
    if include_kaggle_badge is None:
      del self.include_kaggle_badge
      return
    if not isinstance(include_kaggle_badge, bool):
      raise TypeError('include_kaggle_badge must be of type bool')
    self._include_kaggle_badge = include_kaggle_badge


class GithubSpec(KaggleObject):
  r"""
  Attributes:
    file_info (GithubSpec.FileInfo)
    last_push (GithubSpec.CommitInfo)
    last_pull (GithubSpec.CommitInfo)
    last_ignore_nudge_time (datetime)
  """

  class CommitInfo(KaggleObject):
    r"""
    Attributes:
      sha (str)
      time (datetime)
    """

    def __init__(self):
      self._sha = None
      self._time = None
      self._freeze()

    @property
    def sha(self) -> str:
      return self._sha or ""

    @sha.setter
    def sha(self, sha: Optional[str]):
      if sha is None:
        del self.sha
        return
      if not isinstance(sha, str):
        raise TypeError('sha must be of type str')
      self._sha = sha

    @property
    def time(self) -> datetime:
      return self._time or None

    @time.setter
    def time(self, time: Optional[datetime]):
      if time is None:
        del self.time
        return
      if not isinstance(time, datetime):
        raise TypeError('time must be of type datetime')
      self._time = time


  class FileInfo(KaggleObject):
    r"""
    Attributes:
      repo_owner (str)
      repo_name (str)
      branch (str)
      file_name (str)
    """

    def __init__(self):
      self._repo_owner = ""
      self._repo_name = ""
      self._branch = ""
      self._file_name = ""
      self._freeze()

    @property
    def repo_owner(self) -> str:
      return self._repo_owner

    @repo_owner.setter
    def repo_owner(self, repo_owner: str):
      if repo_owner is None:
        del self.repo_owner
        return
      if not isinstance(repo_owner, str):
        raise TypeError('repo_owner must be of type str')
      self._repo_owner = repo_owner

    @property
    def repo_name(self) -> str:
      return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name: str):
      if repo_name is None:
        del self.repo_name
        return
      if not isinstance(repo_name, str):
        raise TypeError('repo_name must be of type str')
      self._repo_name = repo_name

    @property
    def branch(self) -> str:
      return self._branch

    @branch.setter
    def branch(self, branch: str):
      if branch is None:
        del self.branch
        return
      if not isinstance(branch, str):
        raise TypeError('branch must be of type str')
      self._branch = branch

    @property
    def file_name(self) -> str:
      return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
      if file_name is None:
        del self.file_name
        return
      if not isinstance(file_name, str):
        raise TypeError('file_name must be of type str')
      self._file_name = file_name


  def __init__(self):
    self._file_info = None
    self._last_push = None
    self._last_pull = None
    self._last_ignore_nudge_time = None
    self._freeze()

  @property
  def file_info(self) -> Optional['GithubSpec.FileInfo']:
    return self._file_info

  @file_info.setter
  def file_info(self, file_info: Optional['GithubSpec.FileInfo']):
    if file_info is None:
      del self.file_info
      return
    if not isinstance(file_info, GithubSpec.FileInfo):
      raise TypeError('file_info must be of type GithubSpec.FileInfo')
    self._file_info = file_info

  @property
  def last_push(self) -> Optional['GithubSpec.CommitInfo']:
    return self._last_push or None

  @last_push.setter
  def last_push(self, last_push: Optional[Optional['GithubSpec.CommitInfo']]):
    if last_push is None:
      del self.last_push
      return
    if not isinstance(last_push, GithubSpec.CommitInfo):
      raise TypeError('last_push must be of type GithubSpec.CommitInfo')
    self._last_push = last_push

  @property
  def last_pull(self) -> Optional['GithubSpec.CommitInfo']:
    return self._last_pull or None

  @last_pull.setter
  def last_pull(self, last_pull: Optional[Optional['GithubSpec.CommitInfo']]):
    if last_pull is None:
      del self.last_pull
      return
    if not isinstance(last_pull, GithubSpec.CommitInfo):
      raise TypeError('last_pull must be of type GithubSpec.CommitInfo')
    self._last_pull = last_pull

  @property
  def last_ignore_nudge_time(self) -> datetime:
    return self._last_ignore_nudge_time or None

  @last_ignore_nudge_time.setter
  def last_ignore_nudge_time(self, last_ignore_nudge_time: Optional[datetime]):
    if last_ignore_nudge_time is None:
      del self.last_ignore_nudge_time
      return
    if not isinstance(last_ignore_nudge_time, datetime):
      raise TypeError('last_ignore_nudge_time must be of type datetime')
    self._last_ignore_nudge_time = last_ignore_nudge_time


class HasAcceptedKernelCompetitionRulesRequest(KaggleObject):
  r"""
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


class HasAcceptedKernelCompetitionRulesResponse(KaggleObject):
  r"""
  Attributes:
    competitions_requiring_acceptance (KernelCompetition)
  """

  def __init__(self):
    self._competitions_requiring_acceptance = []
    self._freeze()

  @property
  def competitions_requiring_acceptance(self) -> Optional[List[Optional['KernelCompetition']]]:
    return self._competitions_requiring_acceptance

  @competitions_requiring_acceptance.setter
  def competitions_requiring_acceptance(self, competitions_requiring_acceptance: Optional[List[Optional['KernelCompetition']]]):
    if competitions_requiring_acceptance is None:
      del self.competitions_requiring_acceptance
      return
    if not isinstance(competitions_requiring_acceptance, list):
      raise TypeError('competitions_requiring_acceptance must be of type list')
    if not all([isinstance(t, KernelCompetition) for t in competitions_requiring_acceptance]):
      raise TypeError('competitions_requiring_acceptance must contain only items of type KernelCompetition')
    self._competitions_requiring_acceptance = competitions_requiring_acceptance


class Kernel(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
    fork_parent (KernelForkInfo)
    current_run_id (int)
    most_recent_run_id (int)
    url (str)
    tags (Tag)
    comment_count (int)
    upvote_count (int)
    view_count (int)
    fork_count (int)
    best_public_score (float)
    author (User)
    is_private (bool)
    updated_time (datetime)
    self_link (str)
    pinned_docker_image_version_id (int)
    docker_image_pinning_type (DockerImagePinningType)
    original_docker_image_id (int)
    is_language_template (bool)
    medal (Medal)
    topic_id (int)
    slug (str)
    pinned_session_id (int)
    disable_comments (bool)
    has_linked_submission (bool)
      Whether or not any child KernelSession was used to make a successful
      Competition Submission
    current_user_has_bookmarked (bool)
      Whether or not the current user has bookmarked this notebook
    date_output_to_dataset_enabled (datetime)
    can_toggle_visibility (bool)
    persistence (PersistenceMode)
    private_competition_id (int)
    date_output_to_model_enabled (datetime)
  """

  def __init__(self):
    self._id = 0
    self._title = None
    self._fork_parent = None
    self._current_run_id = None
    self._most_recent_run_id = None
    self._url = None
    self._tags = []
    self._comment_count = 0
    self._upvote_count = 0
    self._view_count = 0
    self._fork_count = 0
    self._best_public_score = None
    self._author = None
    self._is_private = False
    self._updated_time = None
    self._self_link = None
    self._pinned_docker_image_version_id = None
    self._docker_image_pinning_type = DockerImagePinningType.DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED
    self._original_docker_image_id = None
    self._is_language_template = False
    self._medal = Medal.MEDAL_UNSPECIFIED
    self._topic_id = None
    self._slug = None
    self._pinned_session_id = None
    self._disable_comments = False
    self._has_linked_submission = False
    self._current_user_has_bookmarked = False
    self._date_output_to_dataset_enabled = None
    self._can_toggle_visibility = False
    self._persistence = PersistenceMode.PERSISTENCE_MODE_UNSPECIFIED
    self._private_competition_id = None
    self._date_output_to_model_enabled = None
    self._freeze()

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
  def title(self) -> str:
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
  def fork_parent(self) -> Optional['KernelForkInfo']:
    return self._fork_parent

  @fork_parent.setter
  def fork_parent(self, fork_parent: Optional['KernelForkInfo']):
    if fork_parent is None:
      del self.fork_parent
      return
    if not isinstance(fork_parent, KernelForkInfo):
      raise TypeError('fork_parent must be of type KernelForkInfo')
    self._fork_parent = fork_parent

  @property
  def current_run_id(self) -> int:
    return self._current_run_id or 0

  @current_run_id.setter
  def current_run_id(self, current_run_id: Optional[int]):
    if current_run_id is None:
      del self.current_run_id
      return
    if not isinstance(current_run_id, int):
      raise TypeError('current_run_id must be of type int')
    self._current_run_id = current_run_id

  @property
  def most_recent_run_id(self) -> int:
    return self._most_recent_run_id or 0

  @most_recent_run_id.setter
  def most_recent_run_id(self, most_recent_run_id: Optional[int]):
    if most_recent_run_id is None:
      del self.most_recent_run_id
      return
    if not isinstance(most_recent_run_id, int):
      raise TypeError('most_recent_run_id must be of type int')
    self._most_recent_run_id = most_recent_run_id

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def tags(self) -> Optional[List[Optional['Tag']]]:
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['Tag']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, Tag) for t in tags]):
      raise TypeError('tags must contain only items of type Tag')
    self._tags = tags

  @property
  def comment_count(self) -> int:
    return self._comment_count

  @comment_count.setter
  def comment_count(self, comment_count: int):
    if comment_count is None:
      del self.comment_count
      return
    if not isinstance(comment_count, int):
      raise TypeError('comment_count must be of type int')
    self._comment_count = comment_count

  @property
  def upvote_count(self) -> int:
    return self._upvote_count

  @upvote_count.setter
  def upvote_count(self, upvote_count: int):
    if upvote_count is None:
      del self.upvote_count
      return
    if not isinstance(upvote_count, int):
      raise TypeError('upvote_count must be of type int')
    self._upvote_count = upvote_count

  @property
  def view_count(self) -> int:
    return self._view_count

  @view_count.setter
  def view_count(self, view_count: int):
    if view_count is None:
      del self.view_count
      return
    if not isinstance(view_count, int):
      raise TypeError('view_count must be of type int')
    self._view_count = view_count

  @property
  def fork_count(self) -> int:
    return self._fork_count

  @fork_count.setter
  def fork_count(self, fork_count: int):
    if fork_count is None:
      del self.fork_count
      return
    if not isinstance(fork_count, int):
      raise TypeError('fork_count must be of type int')
    self._fork_count = fork_count

  @property
  def best_public_score(self) -> float:
    return self._best_public_score or 0.0

  @best_public_score.setter
  def best_public_score(self, best_public_score: Optional[float]):
    if best_public_score is None:
      del self.best_public_score
      return
    if not isinstance(best_public_score, float):
      raise TypeError('best_public_score must be of type float')
    self._best_public_score = best_public_score

  @property
  def author(self) -> Optional['User']:
    return self._author

  @author.setter
  def author(self, author: Optional['User']):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def updated_time(self) -> datetime:
    return self._updated_time

  @updated_time.setter
  def updated_time(self, updated_time: datetime):
    if updated_time is None:
      del self.updated_time
      return
    if not isinstance(updated_time, datetime):
      raise TypeError('updated_time must be of type datetime')
    self._updated_time = updated_time

  @property
  def self_link(self) -> str:
    return self._self_link or ""

  @self_link.setter
  def self_link(self, self_link: Optional[str]):
    if self_link is None:
      del self.self_link
      return
    if not isinstance(self_link, str):
      raise TypeError('self_link must be of type str')
    self._self_link = self_link

  @property
  def pinned_docker_image_version_id(self) -> int:
    return self._pinned_docker_image_version_id or 0

  @pinned_docker_image_version_id.setter
  def pinned_docker_image_version_id(self, pinned_docker_image_version_id: Optional[int]):
    if pinned_docker_image_version_id is None:
      del self.pinned_docker_image_version_id
      return
    if not isinstance(pinned_docker_image_version_id, int):
      raise TypeError('pinned_docker_image_version_id must be of type int')
    self._pinned_docker_image_version_id = pinned_docker_image_version_id

  @property
  def docker_image_pinning_type(self) -> 'DockerImagePinningType':
    return self._docker_image_pinning_type

  @docker_image_pinning_type.setter
  def docker_image_pinning_type(self, docker_image_pinning_type: 'DockerImagePinningType'):
    if docker_image_pinning_type is None:
      del self.docker_image_pinning_type
      return
    if not isinstance(docker_image_pinning_type, DockerImagePinningType):
      raise TypeError('docker_image_pinning_type must be of type DockerImagePinningType')
    self._docker_image_pinning_type = docker_image_pinning_type

  @property
  def original_docker_image_id(self) -> int:
    return self._original_docker_image_id or 0

  @original_docker_image_id.setter
  def original_docker_image_id(self, original_docker_image_id: Optional[int]):
    if original_docker_image_id is None:
      del self.original_docker_image_id
      return
    if not isinstance(original_docker_image_id, int):
      raise TypeError('original_docker_image_id must be of type int')
    self._original_docker_image_id = original_docker_image_id

  @property
  def is_language_template(self) -> bool:
    return self._is_language_template

  @is_language_template.setter
  def is_language_template(self, is_language_template: bool):
    if is_language_template is None:
      del self.is_language_template
      return
    if not isinstance(is_language_template, bool):
      raise TypeError('is_language_template must be of type bool')
    self._is_language_template = is_language_template

  @property
  def medal(self) -> 'Medal':
    return self._medal

  @medal.setter
  def medal(self, medal: 'Medal'):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def topic_id(self) -> int:
    return self._topic_id or 0

  @topic_id.setter
  def topic_id(self, topic_id: Optional[int]):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def pinned_session_id(self) -> int:
    return self._pinned_session_id or 0

  @pinned_session_id.setter
  def pinned_session_id(self, pinned_session_id: Optional[int]):
    if pinned_session_id is None:
      del self.pinned_session_id
      return
    if not isinstance(pinned_session_id, int):
      raise TypeError('pinned_session_id must be of type int')
    self._pinned_session_id = pinned_session_id

  @property
  def disable_comments(self) -> bool:
    return self._disable_comments

  @disable_comments.setter
  def disable_comments(self, disable_comments: bool):
    if disable_comments is None:
      del self.disable_comments
      return
    if not isinstance(disable_comments, bool):
      raise TypeError('disable_comments must be of type bool')
    self._disable_comments = disable_comments

  @property
  def has_linked_submission(self) -> bool:
    r"""
    Whether or not any child KernelSession was used to make a successful
    Competition Submission
    """
    return self._has_linked_submission

  @has_linked_submission.setter
  def has_linked_submission(self, has_linked_submission: bool):
    if has_linked_submission is None:
      del self.has_linked_submission
      return
    if not isinstance(has_linked_submission, bool):
      raise TypeError('has_linked_submission must be of type bool')
    self._has_linked_submission = has_linked_submission

  @property
  def current_user_has_bookmarked(self) -> bool:
    """Whether or not the current user has bookmarked this notebook"""
    return self._current_user_has_bookmarked

  @current_user_has_bookmarked.setter
  def current_user_has_bookmarked(self, current_user_has_bookmarked: bool):
    if current_user_has_bookmarked is None:
      del self.current_user_has_bookmarked
      return
    if not isinstance(current_user_has_bookmarked, bool):
      raise TypeError('current_user_has_bookmarked must be of type bool')
    self._current_user_has_bookmarked = current_user_has_bookmarked

  @property
  def date_output_to_dataset_enabled(self) -> datetime:
    return self._date_output_to_dataset_enabled

  @date_output_to_dataset_enabled.setter
  def date_output_to_dataset_enabled(self, date_output_to_dataset_enabled: datetime):
    if date_output_to_dataset_enabled is None:
      del self.date_output_to_dataset_enabled
      return
    if not isinstance(date_output_to_dataset_enabled, datetime):
      raise TypeError('date_output_to_dataset_enabled must be of type datetime')
    self._date_output_to_dataset_enabled = date_output_to_dataset_enabled

  @property
  def can_toggle_visibility(self) -> bool:
    return self._can_toggle_visibility

  @can_toggle_visibility.setter
  def can_toggle_visibility(self, can_toggle_visibility: bool):
    if can_toggle_visibility is None:
      del self.can_toggle_visibility
      return
    if not isinstance(can_toggle_visibility, bool):
      raise TypeError('can_toggle_visibility must be of type bool')
    self._can_toggle_visibility = can_toggle_visibility

  @property
  def persistence(self) -> 'PersistenceMode':
    return self._persistence

  @persistence.setter
  def persistence(self, persistence: 'PersistenceMode'):
    if persistence is None:
      del self.persistence
      return
    if not isinstance(persistence, PersistenceMode):
      raise TypeError('persistence must be of type PersistenceMode')
    self._persistence = persistence

  @property
  def private_competition_id(self) -> int:
    return self._private_competition_id or 0

  @private_competition_id.setter
  def private_competition_id(self, private_competition_id: Optional[int]):
    if private_competition_id is None:
      del self.private_competition_id
      return
    if not isinstance(private_competition_id, int):
      raise TypeError('private_competition_id must be of type int')
    self._private_competition_id = private_competition_id

  @property
  def date_output_to_model_enabled(self) -> datetime:
    return self._date_output_to_model_enabled

  @date_output_to_model_enabled.setter
  def date_output_to_model_enabled(self, date_output_to_model_enabled: datetime):
    if date_output_to_model_enabled is None:
      del self.date_output_to_model_enabled
      return
    if not isinstance(date_output_to_model_enabled, datetime):
      raise TypeError('date_output_to_model_enabled must be of type datetime')
    self._date_output_to_model_enabled = date_output_to_model_enabled


class KernelBlob(KaggleObject):
  r"""
  Attributes:
    id (int)
    settings (KernelBlobSettings)
    source (str)
    date_created (datetime)
    source_url (str)
    settings_schema_version (int)
  """

  def __init__(self):
    self._id = 0
    self._settings = None
    self._source = None
    self._date_created = None
    self._source_url = None
    self._settings_schema_version = None
    self._freeze()

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
  def settings(self) -> Optional['KernelBlobSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['KernelBlobSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, KernelBlobSettings):
      raise TypeError('settings must be of type KernelBlobSettings')
    self._settings = settings

  @property
  def source(self) -> str:
    return self._source or ""

  @source.setter
  def source(self, source: Optional[str]):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source

  @property
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created

  @property
  def source_url(self) -> str:
    return self._source_url or ""

  @source_url.setter
  def source_url(self, source_url: Optional[str]):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    self._source_url = source_url

  @property
  def settings_schema_version(self) -> int:
    return self._settings_schema_version or 0

  @settings_schema_version.setter
  def settings_schema_version(self, settings_schema_version: Optional[int]):
    if settings_schema_version is None:
      del self.settings_schema_version
      return
    if not isinstance(settings_schema_version, int):
      raise TypeError('settings_schema_version must be of type int')
    self._settings_schema_version = settings_schema_version


class KernelBlobSettings(KaggleObject):
  r"""
  Important: This message is serialized to database as Json so be extra careful
  while making any changes.

  Attributes:
    docker_image_version_id (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    data_sources (DataSourceReference)
    source_type (EditorType)
    language (Language)
    accelerator (AcceleratorType)
    is_internet_enabled (bool)
    is_gpu_enabled (bool)
      This property is deprecated and only used for backwards compatibility. Use
      Accelerator instead.
      TODO(vimota) Remove this once sufficient time has passed that there are no
      reruns using the old property.
  """

  def __init__(self):
    self._docker_image_version_id = None
    self._data_sources = []
    self._source_type = EditorType.EDITOR_TYPE_UNSPECIFIED
    self._language = Language.LANGUAGE_UNSPECIFIED
    self._accelerator = AcceleratorType.ACCELERATOR_TYPE_NONE
    self._is_internet_enabled = False
    self._is_gpu_enabled = False
    self._freeze()

  @property
  def docker_image_version_id(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._docker_image_version_id or None

  @docker_image_version_id.setter
  def docker_image_version_id(self, docker_image_version_id: Optional[int]):
    if docker_image_version_id is None:
      del self.docker_image_version_id
      return
    if not isinstance(docker_image_version_id, int):
      raise TypeError('docker_image_version_id must be of type int')
    self._docker_image_version_id = docker_image_version_id

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def source_type(self) -> 'EditorType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'EditorType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, EditorType):
      raise TypeError('source_type must be of type EditorType')
    self._source_type = source_type

  @property
  def language(self) -> 'Language':
    return self._language

  @language.setter
  def language(self, language: 'Language'):
    if language is None:
      del self.language
      return
    if not isinstance(language, Language):
      raise TypeError('language must be of type Language')
    self._language = language

  @property
  def accelerator(self) -> 'AcceleratorType':
    return self._accelerator

  @accelerator.setter
  def accelerator(self, accelerator: 'AcceleratorType'):
    if accelerator is None:
      del self.accelerator
      return
    if not isinstance(accelerator, AcceleratorType):
      raise TypeError('accelerator must be of type AcceleratorType')
    self._accelerator = accelerator

  @property
  def is_internet_enabled(self) -> bool:
    return self._is_internet_enabled

  @is_internet_enabled.setter
  def is_internet_enabled(self, is_internet_enabled: bool):
    if is_internet_enabled is None:
      del self.is_internet_enabled
      return
    if not isinstance(is_internet_enabled, bool):
      raise TypeError('is_internet_enabled must be of type bool')
    self._is_internet_enabled = is_internet_enabled

  @property
  def is_gpu_enabled(self) -> bool:
    r"""
    This property is deprecated and only used for backwards compatibility. Use
    Accelerator instead.
    TODO(vimota) Remove this once sufficient time has passed that there are no
    reruns using the old property.
    """
    return self._is_gpu_enabled

  @is_gpu_enabled.setter
  def is_gpu_enabled(self, is_gpu_enabled: bool):
    if is_gpu_enabled is None:
      del self.is_gpu_enabled
      return
    if not isinstance(is_gpu_enabled, bool):
      raise TypeError('is_gpu_enabled must be of type bool')
    self._is_gpu_enabled = is_gpu_enabled


class KernelCategoryIdList(KaggleObject):
  r"""
  Attributes:
    total_count (int)
      This is the total number of categories that match the specified filters,
      even though 'category_ids' below will contain only a single page of
      results.
    category_ids (int)
  """

  def __init__(self):
    self._total_count = None
    self._category_ids = []
    self._freeze()

  @property
  def total_count(self) -> int:
    r"""
    This is the total number of categories that match the specified filters,
    even though 'category_ids' below will contain only a single page of
    results.
    """
    return self._total_count or 0

  @total_count.setter
  def total_count(self, total_count: Optional[int]):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def category_ids(self) -> Optional[List[int]]:
    return self._category_ids

  @category_ids.setter
  def category_ids(self, category_ids: Optional[List[int]]):
    if category_ids is None:
      del self.category_ids
      return
    if not isinstance(category_ids, list):
      raise TypeError('category_ids must be of type list')
    if not all([isinstance(t, int) for t in category_ids]):
      raise TypeError('category_ids must contain only items of type int')
    self._category_ids = category_ids


class KernelCompetition(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    title (str)
    rules_url (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._title = ""
    self._rules_url = ""
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def rules_url(self) -> str:
    return self._rules_url

  @rules_url.setter
  def rules_url(self, rules_url: str):
    if rules_url is None:
      del self.rules_url
      return
    if not isinstance(rules_url, str):
      raise TypeError('rules_url must be of type str')
    self._rules_url = rules_url


class KernelDataSourceListItemDto(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    source_type (LegacyDataSourceType)
    source_id (int)
    description (str)
    site_name (str)
    thumbnail_url (str)
    title (str)
    is_private (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._source_type = LegacyDataSourceType.LEGACY_DATA_SOURCE_TYPE_DATASET
    self._source_id = 0
    self._description = None
    self._site_name = None
    self._thumbnail_url = None
    self._title = None
    self._is_private = False
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def source_type(self) -> 'LegacyDataSourceType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'LegacyDataSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, LegacyDataSourceType):
      raise TypeError('source_type must be of type LegacyDataSourceType')
    self._source_type = source_type

  @property
  def source_id(self) -> int:
    return self._source_id

  @source_id.setter
  def source_id(self, source_id: int):
    if source_id is None:
      del self.source_id
      return
    if not isinstance(source_id, int):
      raise TypeError('source_id must be of type int')
    self._source_id = source_id

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
  def site_name(self) -> str:
    return self._site_name or ""

  @site_name.setter
  def site_name(self, site_name: Optional[str]):
    if site_name is None:
      del self.site_name
      return
    if not isinstance(site_name, str):
      raise TypeError('site_name must be of type str')
    self._site_name = site_name

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def title(self) -> str:
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
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private


class KernelDiff(KaggleObject):
  r"""
  Attributes:
    lines_inserted (int)
    lines_deleted (int)
    lines_changed (int)
    lines_unchanged (int)
    new_total_lines (int)
  """

  def __init__(self):
    self._lines_inserted = 0
    self._lines_deleted = 0
    self._lines_changed = 0
    self._lines_unchanged = 0
    self._new_total_lines = 0
    self._freeze()

  @property
  def lines_inserted(self) -> int:
    return self._lines_inserted

  @lines_inserted.setter
  def lines_inserted(self, lines_inserted: int):
    if lines_inserted is None:
      del self.lines_inserted
      return
    if not isinstance(lines_inserted, int):
      raise TypeError('lines_inserted must be of type int')
    self._lines_inserted = lines_inserted

  @property
  def lines_deleted(self) -> int:
    return self._lines_deleted

  @lines_deleted.setter
  def lines_deleted(self, lines_deleted: int):
    if lines_deleted is None:
      del self.lines_deleted
      return
    if not isinstance(lines_deleted, int):
      raise TypeError('lines_deleted must be of type int')
    self._lines_deleted = lines_deleted

  @property
  def lines_changed(self) -> int:
    return self._lines_changed

  @lines_changed.setter
  def lines_changed(self, lines_changed: int):
    if lines_changed is None:
      del self.lines_changed
      return
    if not isinstance(lines_changed, int):
      raise TypeError('lines_changed must be of type int')
    self._lines_changed = lines_changed

  @property
  def lines_unchanged(self) -> int:
    return self._lines_unchanged

  @lines_unchanged.setter
  def lines_unchanged(self, lines_unchanged: int):
    if lines_unchanged is None:
      del self.lines_unchanged
      return
    if not isinstance(lines_unchanged, int):
      raise TypeError('lines_unchanged must be of type int')
    self._lines_unchanged = lines_unchanged

  @property
  def new_total_lines(self) -> int:
    return self._new_total_lines

  @new_total_lines.setter
  def new_total_lines(self, new_total_lines: int):
    if new_total_lines is None:
      del self.new_total_lines
      return
    if not isinstance(new_total_lines, int):
      raise TypeError('new_total_lines must be of type int')
    self._new_total_lines = new_total_lines


class KernelDraft(KaggleObject):
  r"""
  Attributes:
    sequence (int)
    kernel_version_id (int)
    parent_kernel_version_id (int)
    blob (KernelBlob)
    has_more_recent_collaborator_version (bool)
  """

  def __init__(self):
    self._sequence = 0
    self._kernel_version_id = 0
    self._parent_kernel_version_id = None
    self._blob = None
    self._has_more_recent_collaborator_version = False
    self._freeze()

  @property
  def sequence(self) -> int:
    return self._sequence

  @sequence.setter
  def sequence(self, sequence: int):
    if sequence is None:
      del self.sequence
      return
    if not isinstance(sequence, int):
      raise TypeError('sequence must be of type int')
    self._sequence = sequence

  @property
  def kernel_version_id(self) -> int:
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def parent_kernel_version_id(self) -> int:
    return self._parent_kernel_version_id or 0

  @parent_kernel_version_id.setter
  def parent_kernel_version_id(self, parent_kernel_version_id: Optional[int]):
    if parent_kernel_version_id is None:
      del self.parent_kernel_version_id
      return
    if not isinstance(parent_kernel_version_id, int):
      raise TypeError('parent_kernel_version_id must be of type int')
    self._parent_kernel_version_id = parent_kernel_version_id

  @property
  def blob(self) -> Optional['KernelBlob']:
    return self._blob

  @blob.setter
  def blob(self, blob: Optional['KernelBlob']):
    if blob is None:
      del self.blob
      return
    if not isinstance(blob, KernelBlob):
      raise TypeError('blob must be of type KernelBlob')
    self._blob = blob

  @property
  def has_more_recent_collaborator_version(self) -> bool:
    return self._has_more_recent_collaborator_version

  @has_more_recent_collaborator_version.setter
  def has_more_recent_collaborator_version(self, has_more_recent_collaborator_version: bool):
    if has_more_recent_collaborator_version is None:
      del self.has_more_recent_collaborator_version
      return
    if not isinstance(has_more_recent_collaborator_version, bool):
      raise TypeError('has_more_recent_collaborator_version must be of type bool')
    self._has_more_recent_collaborator_version = has_more_recent_collaborator_version


class KernelForkInfo(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    run_id (int)
    url (str)
    title (str)
    author (User)
    diff (KernelDiff)
    is_redacted (bool)
    date_created (datetime)
    worker_status (KernelWorkerStatus)
    isolator_results (str)
    language_id (int)
    version_type (KernelVersionType)
    is_private (bool)
    is_fork (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._run_id = 0
    self._url = None
    self._title = None
    self._author = None
    self._diff = None
    self._is_redacted = False
    self._date_created = None
    self._worker_status = KernelWorkerStatus.QUEUED
    self._isolator_results = None
    self._language_id = None
    self._version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._is_private = False
    self._is_fork = False
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def run_id(self) -> int:
    return self._run_id

  @run_id.setter
  def run_id(self, run_id: int):
    if run_id is None:
      del self.run_id
      return
    if not isinstance(run_id, int):
      raise TypeError('run_id must be of type int')
    self._run_id = run_id

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def title(self) -> str:
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
  def author(self) -> Optional['User']:
    return self._author

  @author.setter
  def author(self, author: Optional['User']):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author

  @property
  def diff(self) -> Optional['KernelDiff']:
    return self._diff

  @diff.setter
  def diff(self, diff: Optional['KernelDiff']):
    if diff is None:
      del self.diff
      return
    if not isinstance(diff, KernelDiff):
      raise TypeError('diff must be of type KernelDiff')
    self._diff = diff

  @property
  def is_redacted(self) -> bool:
    return self._is_redacted

  @is_redacted.setter
  def is_redacted(self, is_redacted: bool):
    if is_redacted is None:
      del self.is_redacted
      return
    if not isinstance(is_redacted, bool):
      raise TypeError('is_redacted must be of type bool')
    self._is_redacted = is_redacted

  @property
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created

  @property
  def worker_status(self) -> 'KernelWorkerStatus':
    return self._worker_status

  @worker_status.setter
  def worker_status(self, worker_status: 'KernelWorkerStatus'):
    if worker_status is None:
      del self.worker_status
      return
    if not isinstance(worker_status, KernelWorkerStatus):
      raise TypeError('worker_status must be of type KernelWorkerStatus')
    self._worker_status = worker_status

  @property
  def isolator_results(self) -> str:
    return self._isolator_results or ""

  @isolator_results.setter
  def isolator_results(self, isolator_results: Optional[str]):
    if isolator_results is None:
      del self.isolator_results
      return
    if not isinstance(isolator_results, str):
      raise TypeError('isolator_results must be of type str')
    self._isolator_results = isolator_results

  @property
  def language_id(self) -> int:
    return self._language_id or 0

  @language_id.setter
  def language_id(self, language_id: Optional[int]):
    if language_id is None:
      del self.language_id
      return
    if not isinstance(language_id, int):
      raise TypeError('language_id must be of type int')
    self._language_id = language_id

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type

  @version_type.setter
  def version_type(self, version_type: 'KernelVersionType'):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def is_fork(self) -> bool:
    return self._is_fork

  @is_fork.setter
  def is_fork(self, is_fork: bool):
    if is_fork is None:
      del self.is_fork
      return
    if not isinstance(is_fork, bool):
      raise TypeError('is_fork must be of type bool')
    self._is_fork = is_fork


class KernelImport(KaggleObject):
  r"""
  Attributes:
    id (str)
    user_id (int)
      This is set on the backend.
    import_type (ImportType)
    source_data (str)
      For Colab: the driveId, for GitHub: the rawUrl, for an external source:
      the url, for File: the content of the selected file.
    file_name (str)
    external_source_user_id (str)
    external_source_avatar_url (str)
    version_type (KernelVersionType)
    accelerator (AcceleratorType)
    is_phone_verified (bool)
    accelerator_selection (AcceleratorSelection)
  """

  def __init__(self):
    self._id = ""
    self._user_id = None
    self._import_type = ImportType.UNSPECIFIED
    self._source_data = ""
    self._file_name = ""
    self._external_source_user_id = None
    self._external_source_avatar_url = None
    self._version_type = None
    self._accelerator = None
    self._is_phone_verified = None
    self._accelerator_selection = None
    self._freeze()

  @property
  def id(self) -> str:
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def user_id(self) -> int:
    """This is set on the backend."""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def import_type(self) -> 'ImportType':
    return self._import_type

  @import_type.setter
  def import_type(self, import_type: 'ImportType'):
    if import_type is None:
      del self.import_type
      return
    if not isinstance(import_type, ImportType):
      raise TypeError('import_type must be of type ImportType')
    self._import_type = import_type

  @property
  def source_data(self) -> str:
    r"""
    For Colab: the driveId, for GitHub: the rawUrl, for an external source:
    the url, for File: the content of the selected file.
    """
    return self._source_data

  @source_data.setter
  def source_data(self, source_data: str):
    if source_data is None:
      del self.source_data
      return
    if not isinstance(source_data, str):
      raise TypeError('source_data must be of type str')
    self._source_data = source_data

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

  @property
  def external_source_user_id(self) -> str:
    return self._external_source_user_id or ""

  @external_source_user_id.setter
  def external_source_user_id(self, external_source_user_id: Optional[str]):
    if external_source_user_id is None:
      del self.external_source_user_id
      return
    if not isinstance(external_source_user_id, str):
      raise TypeError('external_source_user_id must be of type str')
    self._external_source_user_id = external_source_user_id

  @property
  def external_source_avatar_url(self) -> str:
    return self._external_source_avatar_url or ""

  @external_source_avatar_url.setter
  def external_source_avatar_url(self, external_source_avatar_url: Optional[str]):
    if external_source_avatar_url is None:
      del self.external_source_avatar_url
      return
    if not isinstance(external_source_avatar_url, str):
      raise TypeError('external_source_avatar_url must be of type str')
    self._external_source_avatar_url = external_source_avatar_url

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type or KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED

  @version_type.setter
  def version_type(self, version_type: Optional['KernelVersionType']):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type

  @property
  def accelerator(self) -> 'AcceleratorType':
    return self._accelerator or AcceleratorType.ACCELERATOR_TYPE_NONE

  @accelerator.setter
  def accelerator(self, accelerator: Optional['AcceleratorType']):
    if accelerator is None:
      del self.accelerator
      return
    if not isinstance(accelerator, AcceleratorType):
      raise TypeError('accelerator must be of type AcceleratorType')
    self._accelerator = accelerator

  @property
  def is_phone_verified(self) -> bool:
    return self._is_phone_verified or False

  @is_phone_verified.setter
  def is_phone_verified(self, is_phone_verified: Optional[bool]):
    if is_phone_verified is None:
      del self.is_phone_verified
      return
    if not isinstance(is_phone_verified, bool):
      raise TypeError('is_phone_verified must be of type bool')
    self._is_phone_verified = is_phone_verified

  @property
  def accelerator_selection(self) -> 'AcceleratorSelection':
    return self._accelerator_selection or AcceleratorSelection.ACCELERATOR_UNSPECIFIED

  @accelerator_selection.setter
  def accelerator_selection(self, accelerator_selection: Optional['AcceleratorSelection']):
    if accelerator_selection is None:
      del self.accelerator_selection
      return
    if not isinstance(accelerator_selection, AcceleratorSelection):
      raise TypeError('accelerator_selection must be of type AcceleratorSelection')
    self._accelerator_selection = accelerator_selection


class KernelRun(KaggleObject):
  r"""
  Attributes:
    id (int)
    kernel_id (int)
    status (KernelWorkerStatus)
    kernel_version_type (KernelVersionType)
    source_type (EditorType)
    language (Language)
    title (str)
    date_created (datetime)
    date_evaluated (datetime)
    date_cancelled (datetime)
    worker_container_port (int)
    worker_uptime_seconds (int)
    worker_ip_address (str)
    worker_ip_address_external (str)
    script_language_id (int)
      TODO(bergam): Remove these once we're no longer using them in
      ScriptsController.EditScript.
    script_language_name (str)
    rendered_output_url (str)
    commit (KernelBlob)
    resources (KernelSessionResources)
    isolator_results (str)
    run_info (KernelSessionInfo)
    docker_image_version_id (int)
    used_custom_docker_image (bool)
    data_sources (DataSourceReference)
      This is the list of DataSources used by the KernelSession as pulled from
      the KernelSession[Competition|Dataset|Script]Sources tables.  Note that
      there is an alternative list within Commit.Settings which may differ.  The
      results here hopefully more accurately represent which versions were used
      by the KernelSession, whereas Commit.Settings better reflects what the
      caller had requested.
    use_new_kernels_backend (bool)
    is_gpu_enabled (bool)
    is_tpu_enabled (bool)
    accelerator_type (AcceleratorType)
    is_internet_enabled (bool)
    executed_by_schedule_id (int)
    next_scheduled_session_date (datetime)
    is_kernel_scheduled (bool)
    github_url (str)
      This is set if the executed kernel was uploaded to a public GitHub repo.
    author_user_id (int)
    kernel_version_number (int)
    kernel_session_package_state (KernelSessionPackageState)
    benchmark_model_version_id (int)
      If this session was run as a Benchmark Task, this is the Model Version
      that was used as the candidate LLM
    author (User)
      The executor of the session (not strictly always the same as the owner of
      the KernelVersion).
  """

  def __init__(self):
    self._id = 0
    self._kernel_id = 0
    self._status = KernelWorkerStatus.QUEUED
    self._kernel_version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._source_type = EditorType.EDITOR_TYPE_UNSPECIFIED
    self._language = Language.LANGUAGE_UNSPECIFIED
    self._title = None
    self._date_created = None
    self._date_evaluated = None
    self._date_cancelled = None
    self._worker_container_port = None
    self._worker_uptime_seconds = None
    self._worker_ip_address = None
    self._worker_ip_address_external = None
    self._script_language_id = 0
    self._script_language_name = None
    self._rendered_output_url = None
    self._commit = None
    self._resources = None
    self._isolator_results = None
    self._run_info = None
    self._docker_image_version_id = None
    self._used_custom_docker_image = False
    self._data_sources = []
    self._use_new_kernels_backend = None
    self._is_gpu_enabled = False
    self._is_tpu_enabled = False
    self._accelerator_type = AcceleratorType.ACCELERATOR_TYPE_NONE
    self._is_internet_enabled = False
    self._executed_by_schedule_id = None
    self._next_scheduled_session_date = None
    self._is_kernel_scheduled = False
    self._github_url = None
    self._author_user_id = None
    self._kernel_version_number = None
    self._kernel_session_package_state = None
    self._benchmark_model_version_id = None
    self._author = None
    self._freeze()

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
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def status(self) -> 'KernelWorkerStatus':
    return self._status

  @status.setter
  def status(self, status: 'KernelWorkerStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, KernelWorkerStatus):
      raise TypeError('status must be of type KernelWorkerStatus')
    self._status = status

  @property
  def kernel_version_type(self) -> 'KernelVersionType':
    return self._kernel_version_type

  @kernel_version_type.setter
  def kernel_version_type(self, kernel_version_type: 'KernelVersionType'):
    if kernel_version_type is None:
      del self.kernel_version_type
      return
    if not isinstance(kernel_version_type, KernelVersionType):
      raise TypeError('kernel_version_type must be of type KernelVersionType')
    self._kernel_version_type = kernel_version_type

  @property
  def source_type(self) -> 'EditorType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'EditorType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, EditorType):
      raise TypeError('source_type must be of type EditorType')
    self._source_type = source_type

  @property
  def language(self) -> 'Language':
    return self._language

  @language.setter
  def language(self, language: 'Language'):
    if language is None:
      del self.language
      return
    if not isinstance(language, Language):
      raise TypeError('language must be of type Language')
    self._language = language

  @property
  def title(self) -> str:
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
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created

  @property
  def date_evaluated(self) -> datetime:
    return self._date_evaluated

  @date_evaluated.setter
  def date_evaluated(self, date_evaluated: datetime):
    if date_evaluated is None:
      del self.date_evaluated
      return
    if not isinstance(date_evaluated, datetime):
      raise TypeError('date_evaluated must be of type datetime')
    self._date_evaluated = date_evaluated

  @property
  def date_cancelled(self) -> datetime:
    return self._date_cancelled

  @date_cancelled.setter
  def date_cancelled(self, date_cancelled: datetime):
    if date_cancelled is None:
      del self.date_cancelled
      return
    if not isinstance(date_cancelled, datetime):
      raise TypeError('date_cancelled must be of type datetime')
    self._date_cancelled = date_cancelled

  @property
  def worker_container_port(self) -> int:
    return self._worker_container_port or 0

  @worker_container_port.setter
  def worker_container_port(self, worker_container_port: Optional[int]):
    if worker_container_port is None:
      del self.worker_container_port
      return
    if not isinstance(worker_container_port, int):
      raise TypeError('worker_container_port must be of type int')
    self._worker_container_port = worker_container_port

  @property
  def worker_uptime_seconds(self) -> int:
    return self._worker_uptime_seconds or 0

  @worker_uptime_seconds.setter
  def worker_uptime_seconds(self, worker_uptime_seconds: Optional[int]):
    if worker_uptime_seconds is None:
      del self.worker_uptime_seconds
      return
    if not isinstance(worker_uptime_seconds, int):
      raise TypeError('worker_uptime_seconds must be of type int')
    self._worker_uptime_seconds = worker_uptime_seconds

  @property
  def worker_ip_address(self) -> str:
    return self._worker_ip_address or ""

  @worker_ip_address.setter
  def worker_ip_address(self, worker_ip_address: Optional[str]):
    if worker_ip_address is None:
      del self.worker_ip_address
      return
    if not isinstance(worker_ip_address, str):
      raise TypeError('worker_ip_address must be of type str')
    self._worker_ip_address = worker_ip_address

  @property
  def worker_ip_address_external(self) -> str:
    return self._worker_ip_address_external or ""

  @worker_ip_address_external.setter
  def worker_ip_address_external(self, worker_ip_address_external: Optional[str]):
    if worker_ip_address_external is None:
      del self.worker_ip_address_external
      return
    if not isinstance(worker_ip_address_external, str):
      raise TypeError('worker_ip_address_external must be of type str')
    self._worker_ip_address_external = worker_ip_address_external

  @property
  def script_language_id(self) -> int:
    r"""
    TODO(bergam): Remove these once we're no longer using them in
    ScriptsController.EditScript.
    """
    return self._script_language_id

  @script_language_id.setter
  def script_language_id(self, script_language_id: int):
    if script_language_id is None:
      del self.script_language_id
      return
    if not isinstance(script_language_id, int):
      raise TypeError('script_language_id must be of type int')
    self._script_language_id = script_language_id

  @property
  def script_language_name(self) -> str:
    return self._script_language_name or ""

  @script_language_name.setter
  def script_language_name(self, script_language_name: Optional[str]):
    if script_language_name is None:
      del self.script_language_name
      return
    if not isinstance(script_language_name, str):
      raise TypeError('script_language_name must be of type str')
    self._script_language_name = script_language_name

  @property
  def rendered_output_url(self) -> str:
    return self._rendered_output_url or ""

  @rendered_output_url.setter
  def rendered_output_url(self, rendered_output_url: Optional[str]):
    if rendered_output_url is None:
      del self.rendered_output_url
      return
    if not isinstance(rendered_output_url, str):
      raise TypeError('rendered_output_url must be of type str')
    self._rendered_output_url = rendered_output_url

  @property
  def commit(self) -> Optional['KernelBlob']:
    return self._commit

  @commit.setter
  def commit(self, commit: Optional['KernelBlob']):
    if commit is None:
      del self.commit
      return
    if not isinstance(commit, KernelBlob):
      raise TypeError('commit must be of type KernelBlob')
    self._commit = commit

  @property
  def resources(self) -> Optional['KernelSessionResources']:
    return self._resources

  @resources.setter
  def resources(self, resources: Optional['KernelSessionResources']):
    if resources is None:
      del self.resources
      return
    if not isinstance(resources, KernelSessionResources):
      raise TypeError('resources must be of type KernelSessionResources')
    self._resources = resources

  @property
  def isolator_results(self) -> str:
    return self._isolator_results or ""

  @isolator_results.setter
  def isolator_results(self, isolator_results: Optional[str]):
    if isolator_results is None:
      del self.isolator_results
      return
    if not isinstance(isolator_results, str):
      raise TypeError('isolator_results must be of type str')
    self._isolator_results = isolator_results

  @property
  def run_info(self) -> Optional['KernelSessionInfo']:
    return self._run_info

  @run_info.setter
  def run_info(self, run_info: Optional['KernelSessionInfo']):
    if run_info is None:
      del self.run_info
      return
    if not isinstance(run_info, KernelSessionInfo):
      raise TypeError('run_info must be of type KernelSessionInfo')
    self._run_info = run_info

  @property
  def docker_image_version_id(self) -> int:
    return self._docker_image_version_id or 0

  @docker_image_version_id.setter
  def docker_image_version_id(self, docker_image_version_id: Optional[int]):
    if docker_image_version_id is None:
      del self.docker_image_version_id
      return
    if not isinstance(docker_image_version_id, int):
      raise TypeError('docker_image_version_id must be of type int')
    self._docker_image_version_id = docker_image_version_id

  @property
  def used_custom_docker_image(self) -> bool:
    return self._used_custom_docker_image

  @used_custom_docker_image.setter
  def used_custom_docker_image(self, used_custom_docker_image: bool):
    if used_custom_docker_image is None:
      del self.used_custom_docker_image
      return
    if not isinstance(used_custom_docker_image, bool):
      raise TypeError('used_custom_docker_image must be of type bool')
    self._used_custom_docker_image = used_custom_docker_image

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    r"""
    This is the list of DataSources used by the KernelSession as pulled from
    the KernelSession[Competition|Dataset|Script]Sources tables.  Note that
    there is an alternative list within Commit.Settings which may differ.  The
    results here hopefully more accurately represent which versions were used
    by the KernelSession, whereas Commit.Settings better reflects what the
    caller had requested.
    """
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def use_new_kernels_backend(self) -> bool:
    return self._use_new_kernels_backend or False

  @use_new_kernels_backend.setter
  def use_new_kernels_backend(self, use_new_kernels_backend: Optional[bool]):
    if use_new_kernels_backend is None:
      del self.use_new_kernels_backend
      return
    if not isinstance(use_new_kernels_backend, bool):
      raise TypeError('use_new_kernels_backend must be of type bool')
    self._use_new_kernels_backend = use_new_kernels_backend

  @property
  def is_gpu_enabled(self) -> bool:
    return self._is_gpu_enabled

  @is_gpu_enabled.setter
  def is_gpu_enabled(self, is_gpu_enabled: bool):
    if is_gpu_enabled is None:
      del self.is_gpu_enabled
      return
    if not isinstance(is_gpu_enabled, bool):
      raise TypeError('is_gpu_enabled must be of type bool')
    self._is_gpu_enabled = is_gpu_enabled

  @property
  def is_tpu_enabled(self) -> bool:
    return self._is_tpu_enabled

  @is_tpu_enabled.setter
  def is_tpu_enabled(self, is_tpu_enabled: bool):
    if is_tpu_enabled is None:
      del self.is_tpu_enabled
      return
    if not isinstance(is_tpu_enabled, bool):
      raise TypeError('is_tpu_enabled must be of type bool')
    self._is_tpu_enabled = is_tpu_enabled

  @property
  def accelerator_type(self) -> 'AcceleratorType':
    return self._accelerator_type

  @accelerator_type.setter
  def accelerator_type(self, accelerator_type: 'AcceleratorType'):
    if accelerator_type is None:
      del self.accelerator_type
      return
    if not isinstance(accelerator_type, AcceleratorType):
      raise TypeError('accelerator_type must be of type AcceleratorType')
    self._accelerator_type = accelerator_type

  @property
  def is_internet_enabled(self) -> bool:
    return self._is_internet_enabled

  @is_internet_enabled.setter
  def is_internet_enabled(self, is_internet_enabled: bool):
    if is_internet_enabled is None:
      del self.is_internet_enabled
      return
    if not isinstance(is_internet_enabled, bool):
      raise TypeError('is_internet_enabled must be of type bool')
    self._is_internet_enabled = is_internet_enabled

  @property
  def executed_by_schedule_id(self) -> int:
    return self._executed_by_schedule_id or 0

  @executed_by_schedule_id.setter
  def executed_by_schedule_id(self, executed_by_schedule_id: Optional[int]):
    if executed_by_schedule_id is None:
      del self.executed_by_schedule_id
      return
    if not isinstance(executed_by_schedule_id, int):
      raise TypeError('executed_by_schedule_id must be of type int')
    self._executed_by_schedule_id = executed_by_schedule_id

  @property
  def next_scheduled_session_date(self) -> datetime:
    return self._next_scheduled_session_date

  @next_scheduled_session_date.setter
  def next_scheduled_session_date(self, next_scheduled_session_date: datetime):
    if next_scheduled_session_date is None:
      del self.next_scheduled_session_date
      return
    if not isinstance(next_scheduled_session_date, datetime):
      raise TypeError('next_scheduled_session_date must be of type datetime')
    self._next_scheduled_session_date = next_scheduled_session_date

  @property
  def is_kernel_scheduled(self) -> bool:
    return self._is_kernel_scheduled

  @is_kernel_scheduled.setter
  def is_kernel_scheduled(self, is_kernel_scheduled: bool):
    if is_kernel_scheduled is None:
      del self.is_kernel_scheduled
      return
    if not isinstance(is_kernel_scheduled, bool):
      raise TypeError('is_kernel_scheduled must be of type bool')
    self._is_kernel_scheduled = is_kernel_scheduled

  @property
  def github_url(self) -> str:
    """This is set if the executed kernel was uploaded to a public GitHub repo."""
    return self._github_url or ""

  @github_url.setter
  def github_url(self, github_url: Optional[str]):
    if github_url is None:
      del self.github_url
      return
    if not isinstance(github_url, str):
      raise TypeError('github_url must be of type str')
    self._github_url = github_url

  @property
  def author_user_id(self) -> int:
    return self._author_user_id or 0

  @author_user_id.setter
  def author_user_id(self, author_user_id: Optional[int]):
    if author_user_id is None:
      del self.author_user_id
      return
    if not isinstance(author_user_id, int):
      raise TypeError('author_user_id must be of type int')
    self._author_user_id = author_user_id

  @property
  def kernel_version_number(self) -> int:
    return self._kernel_version_number or 0

  @kernel_version_number.setter
  def kernel_version_number(self, kernel_version_number: Optional[int]):
    if kernel_version_number is None:
      del self.kernel_version_number
      return
    if not isinstance(kernel_version_number, int):
      raise TypeError('kernel_version_number must be of type int')
    self._kernel_version_number = kernel_version_number

  @property
  def kernel_session_package_state(self) -> 'KernelSessionPackageState':
    return self._kernel_session_package_state or KernelSessionPackageState.PACKAGE_NOT_DETECTED

  @kernel_session_package_state.setter
  def kernel_session_package_state(self, kernel_session_package_state: Optional['KernelSessionPackageState']):
    if kernel_session_package_state is None:
      del self.kernel_session_package_state
      return
    if not isinstance(kernel_session_package_state, KernelSessionPackageState):
      raise TypeError('kernel_session_package_state must be of type KernelSessionPackageState')
    self._kernel_session_package_state = kernel_session_package_state

  @property
  def benchmark_model_version_id(self) -> int:
    r"""
    If this session was run as a Benchmark Task, this is the Model Version
    that was used as the candidate LLM
    """
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def author(self) -> Optional['User']:
    r"""
    The executor of the session (not strictly always the same as the owner of
    the KernelVersion).
    """
    return self._author or None

  @author.setter
  def author(self, author: Optional[Optional['User']]):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author


class KernelSession(KaggleObject):
  r"""
  Represents a flattening of Kernel Version / Kernel Run entities for a running
  session. Primarily used in client.

  Attributes:
    kernel_id (int)
    kernel_run_id (int)
    type (KernelVersionType)
    source_type (EditorType)
    title (str)
    date_created (datetime)
    language_name (str)
    accelerator (AcceleratorType)
    is_internet_enabled (bool)
    version_number (int)
    version_name (str)
  """

  def __init__(self):
    self._kernel_id = 0
    self._kernel_run_id = 0
    self._type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._source_type = EditorType.EDITOR_TYPE_UNSPECIFIED
    self._title = None
    self._date_created = None
    self._language_name = None
    self._accelerator = AcceleratorType.ACCELERATOR_TYPE_NONE
    self._is_internet_enabled = False
    self._version_number = None
    self._version_name = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def kernel_run_id(self) -> int:
    return self._kernel_run_id

  @kernel_run_id.setter
  def kernel_run_id(self, kernel_run_id: int):
    if kernel_run_id is None:
      del self.kernel_run_id
      return
    if not isinstance(kernel_run_id, int):
      raise TypeError('kernel_run_id must be of type int')
    self._kernel_run_id = kernel_run_id

  @property
  def type(self) -> 'KernelVersionType':
    return self._type

  @type.setter
  def type(self, type: 'KernelVersionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, KernelVersionType):
      raise TypeError('type must be of type KernelVersionType')
    self._type = type

  @property
  def source_type(self) -> 'EditorType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'EditorType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, EditorType):
      raise TypeError('source_type must be of type EditorType')
    self._source_type = source_type

  @property
  def title(self) -> str:
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
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created

  @property
  def language_name(self) -> str:
    return self._language_name or ""

  @language_name.setter
  def language_name(self, language_name: Optional[str]):
    if language_name is None:
      del self.language_name
      return
    if not isinstance(language_name, str):
      raise TypeError('language_name must be of type str')
    self._language_name = language_name

  @property
  def accelerator(self) -> 'AcceleratorType':
    return self._accelerator

  @accelerator.setter
  def accelerator(self, accelerator: 'AcceleratorType'):
    if accelerator is None:
      del self.accelerator
      return
    if not isinstance(accelerator, AcceleratorType):
      raise TypeError('accelerator must be of type AcceleratorType')
    self._accelerator = accelerator

  @property
  def is_internet_enabled(self) -> bool:
    return self._is_internet_enabled

  @is_internet_enabled.setter
  def is_internet_enabled(self, is_internet_enabled: bool):
    if is_internet_enabled is None:
      del self.is_internet_enabled
      return
    if not isinstance(is_internet_enabled, bool):
      raise TypeError('is_internet_enabled must be of type bool')
    self._is_internet_enabled = is_internet_enabled

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def version_name(self) -> str:
    return self._version_name or ""

  @version_name.setter
  def version_name(self, version_name: Optional[str]):
    if version_name is None:
      del self.version_name
      return
    if not isinstance(version_name, str):
      raise TypeError('version_name must be of type str')
    self._version_name = version_name


class KernelSessionList(KaggleObject):
  r"""
  A list of running kernel sessions that are currently counting against user
  quota.

  Attributes:
    total_count (int)
    quota_limits (KernelSessionQuotaLimits)
    sessions (KernelSession)
  """

  def __init__(self):
    self._total_count = 0
    self._quota_limits = None
    self._sessions = []
    self._freeze()

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def quota_limits(self) -> Optional['KernelSessionQuotaLimits']:
    return self._quota_limits

  @quota_limits.setter
  def quota_limits(self, quota_limits: Optional['KernelSessionQuotaLimits']):
    if quota_limits is None:
      del self.quota_limits
      return
    if not isinstance(quota_limits, KernelSessionQuotaLimits):
      raise TypeError('quota_limits must be of type KernelSessionQuotaLimits')
    self._quota_limits = quota_limits

  @property
  def sessions(self) -> Optional[List[Optional['KernelSession']]]:
    return self._sessions

  @sessions.setter
  def sessions(self, sessions: Optional[List[Optional['KernelSession']]]):
    if sessions is None:
      del self.sessions
      return
    if not isinstance(sessions, list):
      raise TypeError('sessions must be of type list')
    if not all([isinstance(t, KernelSession) for t in sessions]):
      raise TypeError('sessions must contain only items of type KernelSession')
    self._sessions = sessions


class KernelSessionQuotaLimits(KaggleObject):
  r"""
  Represents the maximum Kernel session quota limits for the current user.

  Attributes:
    gpu_interactive (int)
    gpu_batch (int)
    cpu_interactive (int)
    cpu_batch (int)
    tpu_interactive (int)
    tpu_batch (int)
  """

  def __init__(self):
    self._gpu_interactive = 0
    self._gpu_batch = 0
    self._cpu_interactive = 0
    self._cpu_batch = 0
    self._tpu_interactive = 0
    self._tpu_batch = 0
    self._freeze()

  @property
  def gpu_interactive(self) -> int:
    return self._gpu_interactive

  @gpu_interactive.setter
  def gpu_interactive(self, gpu_interactive: int):
    if gpu_interactive is None:
      del self.gpu_interactive
      return
    if not isinstance(gpu_interactive, int):
      raise TypeError('gpu_interactive must be of type int')
    self._gpu_interactive = gpu_interactive

  @property
  def gpu_batch(self) -> int:
    return self._gpu_batch

  @gpu_batch.setter
  def gpu_batch(self, gpu_batch: int):
    if gpu_batch is None:
      del self.gpu_batch
      return
    if not isinstance(gpu_batch, int):
      raise TypeError('gpu_batch must be of type int')
    self._gpu_batch = gpu_batch

  @property
  def cpu_interactive(self) -> int:
    return self._cpu_interactive

  @cpu_interactive.setter
  def cpu_interactive(self, cpu_interactive: int):
    if cpu_interactive is None:
      del self.cpu_interactive
      return
    if not isinstance(cpu_interactive, int):
      raise TypeError('cpu_interactive must be of type int')
    self._cpu_interactive = cpu_interactive

  @property
  def cpu_batch(self) -> int:
    return self._cpu_batch

  @cpu_batch.setter
  def cpu_batch(self, cpu_batch: int):
    if cpu_batch is None:
      del self.cpu_batch
      return
    if not isinstance(cpu_batch, int):
      raise TypeError('cpu_batch must be of type int')
    self._cpu_batch = cpu_batch

  @property
  def tpu_interactive(self) -> int:
    return self._tpu_interactive

  @tpu_interactive.setter
  def tpu_interactive(self, tpu_interactive: int):
    if tpu_interactive is None:
      del self.tpu_interactive
      return
    if not isinstance(tpu_interactive, int):
      raise TypeError('tpu_interactive must be of type int')
    self._tpu_interactive = tpu_interactive

  @property
  def tpu_batch(self) -> int:
    return self._tpu_batch

  @tpu_batch.setter
  def tpu_batch(self, tpu_batch: int):
    if tpu_batch is None:
      del self.tpu_batch
      return
    if not isinstance(tpu_batch, int):
      raise TypeError('tpu_batch must be of type int')
    self._tpu_batch = tpu_batch


class KernelSessionResources(KaggleObject):
  r"""
  Describes resource limits for kernel requests.

  Attributes:
    storage_bytes (int)
    memory_bytes (int)
    cpu_cores (int)
    session_timeout_seconds (int)
    idle_timeout_seconds (int)
    network (str)
      For enabling or disabling internet access. Should be 'external' or
      'no-external'.
  """

  def __init__(self):
    self._storage_bytes = 0
    self._memory_bytes = 0
    self._cpu_cores = 0
    self._session_timeout_seconds = 0
    self._idle_timeout_seconds = 0
    self._network = None
    self._freeze()

  @property
  def storage_bytes(self) -> int:
    return self._storage_bytes

  @storage_bytes.setter
  def storage_bytes(self, storage_bytes: int):
    if storage_bytes is None:
      del self.storage_bytes
      return
    if not isinstance(storage_bytes, int):
      raise TypeError('storage_bytes must be of type int')
    self._storage_bytes = storage_bytes

  @property
  def memory_bytes(self) -> int:
    return self._memory_bytes

  @memory_bytes.setter
  def memory_bytes(self, memory_bytes: int):
    if memory_bytes is None:
      del self.memory_bytes
      return
    if not isinstance(memory_bytes, int):
      raise TypeError('memory_bytes must be of type int')
    self._memory_bytes = memory_bytes

  @property
  def cpu_cores(self) -> int:
    return self._cpu_cores

  @cpu_cores.setter
  def cpu_cores(self, cpu_cores: int):
    if cpu_cores is None:
      del self.cpu_cores
      return
    if not isinstance(cpu_cores, int):
      raise TypeError('cpu_cores must be of type int')
    self._cpu_cores = cpu_cores

  @property
  def session_timeout_seconds(self) -> int:
    return self._session_timeout_seconds

  @session_timeout_seconds.setter
  def session_timeout_seconds(self, session_timeout_seconds: int):
    if session_timeout_seconds is None:
      del self.session_timeout_seconds
      return
    if not isinstance(session_timeout_seconds, int):
      raise TypeError('session_timeout_seconds must be of type int')
    self._session_timeout_seconds = session_timeout_seconds

  @property
  def idle_timeout_seconds(self) -> int:
    return self._idle_timeout_seconds

  @idle_timeout_seconds.setter
  def idle_timeout_seconds(self, idle_timeout_seconds: int):
    if idle_timeout_seconds is None:
      del self.idle_timeout_seconds
      return
    if not isinstance(idle_timeout_seconds, int):
      raise TypeError('idle_timeout_seconds must be of type int')
    self._idle_timeout_seconds = idle_timeout_seconds

  @property
  def network(self) -> str:
    r"""
    For enabling or disabling internet access. Should be 'external' or
    'no-external'.
    """
    return self._network or ""

  @network.setter
  def network(self, network: Optional[str]):
    if network is None:
      del self.network
      return
    if not isinstance(network, str):
      raise TypeError('network must be of type str')
    self._network = network


class KernelSessionScore(KaggleObject):
  r"""
  Attributes:
    score_formatted (str)
    kernel_version_name (str)
    kernel_version_number (int)
    kernel_session_url (str)
  """

  def __init__(self):
    self._score_formatted = None
    self._kernel_version_name = None
    self._kernel_version_number = 0
    self._kernel_session_url = ""
    self._freeze()

  @property
  def score_formatted(self) -> str:
    return self._score_formatted or ""

  @score_formatted.setter
  def score_formatted(self, score_formatted: Optional[str]):
    if score_formatted is None:
      del self.score_formatted
      return
    if not isinstance(score_formatted, str):
      raise TypeError('score_formatted must be of type str')
    self._score_formatted = score_formatted

  @property
  def kernel_version_name(self) -> str:
    return self._kernel_version_name or ""

  @kernel_version_name.setter
  def kernel_version_name(self, kernel_version_name: Optional[str]):
    if kernel_version_name is None:
      del self.kernel_version_name
      return
    if not isinstance(kernel_version_name, str):
      raise TypeError('kernel_version_name must be of type str')
    self._kernel_version_name = kernel_version_name

  @property
  def kernel_version_number(self) -> int:
    return self._kernel_version_number

  @kernel_version_number.setter
  def kernel_version_number(self, kernel_version_number: int):
    if kernel_version_number is None:
      del self.kernel_version_number
      return
    if not isinstance(kernel_version_number, int):
      raise TypeError('kernel_version_number must be of type int')
    self._kernel_version_number = kernel_version_number

  @property
  def kernel_session_url(self) -> str:
    return self._kernel_session_url

  @kernel_session_url.setter
  def kernel_session_url(self, kernel_session_url: str):
    if kernel_session_url is None:
      del self.kernel_session_url
      return
    if not isinstance(kernel_session_url, str):
      raise TypeError('kernel_session_url must be of type str')
    self._kernel_session_url = kernel_session_url


class KernelShelf(KaggleObject):
  r"""
  Attributes:
    kernels (KernelListItem)
    label (str)
    total_kernels (int)
    more_kernels_request (ListKernelIdsRequest)
  """

  def __init__(self):
    self._kernels = []
    self._label = None
    self._total_kernels = 0
    self._more_kernels_request = None
    self._freeze()

  @property
  def kernels(self) -> Optional[List[Optional['KernelListItem']]]:
    return self._kernels

  @kernels.setter
  def kernels(self, kernels: Optional[List[Optional['KernelListItem']]]):
    if kernels is None:
      del self.kernels
      return
    if not isinstance(kernels, list):
      raise TypeError('kernels must be of type list')
    if not all([isinstance(t, KernelListItem) for t in kernels]):
      raise TypeError('kernels must contain only items of type KernelListItem')
    self._kernels = kernels

  @property
  def label(self) -> str:
    return self._label or ""

  @label.setter
  def label(self, label: Optional[str]):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label

  @property
  def total_kernels(self) -> int:
    return self._total_kernels

  @total_kernels.setter
  def total_kernels(self, total_kernels: int):
    if total_kernels is None:
      del self.total_kernels
      return
    if not isinstance(total_kernels, int):
      raise TypeError('total_kernels must be of type int')
    self._total_kernels = total_kernels

  @property
  def more_kernels_request(self) -> Optional['ListKernelIdsRequest']:
    return self._more_kernels_request

  @more_kernels_request.setter
  def more_kernels_request(self, more_kernels_request: Optional['ListKernelIdsRequest']):
    if more_kernels_request is None:
      del self.more_kernels_request
      return
    if not isinstance(more_kernels_request, ListKernelIdsRequest):
      raise TypeError('more_kernels_request must be of type ListKernelIdsRequest')
    self._more_kernels_request = more_kernels_request


class KernelVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
    version_number (int)
    lines_total (int)
    lines_inserted (int)
    lines_deleted (int)
    pinning_type (KernelVersionPinningType)
    version_name (str)
    version_type (KernelVersionType)
  """

  def __init__(self):
    self._id = 0
    self._version_number = 0
    self._lines_total = 0
    self._lines_inserted = 0
    self._lines_deleted = 0
    self._pinning_type = KernelVersionPinningType.UNPINNED
    self._version_name = None
    self._version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
    self._freeze()

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
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def lines_total(self) -> int:
    return self._lines_total

  @lines_total.setter
  def lines_total(self, lines_total: int):
    if lines_total is None:
      del self.lines_total
      return
    if not isinstance(lines_total, int):
      raise TypeError('lines_total must be of type int')
    self._lines_total = lines_total

  @property
  def lines_inserted(self) -> int:
    return self._lines_inserted

  @lines_inserted.setter
  def lines_inserted(self, lines_inserted: int):
    if lines_inserted is None:
      del self.lines_inserted
      return
    if not isinstance(lines_inserted, int):
      raise TypeError('lines_inserted must be of type int')
    self._lines_inserted = lines_inserted

  @property
  def lines_deleted(self) -> int:
    return self._lines_deleted

  @lines_deleted.setter
  def lines_deleted(self, lines_deleted: int):
    if lines_deleted is None:
      del self.lines_deleted
      return
    if not isinstance(lines_deleted, int):
      raise TypeError('lines_deleted must be of type int')
    self._lines_deleted = lines_deleted

  @property
  def pinning_type(self) -> 'KernelVersionPinningType':
    return self._pinning_type

  @pinning_type.setter
  def pinning_type(self, pinning_type: 'KernelVersionPinningType'):
    if pinning_type is None:
      del self.pinning_type
      return
    if not isinstance(pinning_type, KernelVersionPinningType):
      raise TypeError('pinning_type must be of type KernelVersionPinningType')
    self._pinning_type = pinning_type

  @property
  def version_name(self) -> str:
    return self._version_name or ""

  @version_name.setter
  def version_name(self, version_name: Optional[str]):
    if version_name is None:
      del self.version_name
      return
    if not isinstance(version_name, str):
      raise TypeError('version_name must be of type str')
    self._version_name = version_name

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type

  @version_type.setter
  def version_type(self, version_type: 'KernelVersionType'):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type


class KernelVersionAndRun(KaggleObject):
  r"""
  Attributes:
    author (User)
    version (KernelVersion)
    run (KernelRun)
    blob (KernelBlob)
    is_fork_parent (bool)
    current_url_slug (str)
    kernel_author_user_name (str)
    viewer_url (str)
  """

  def __init__(self):
    self._author = None
    self._version = None
    self._run = None
    self._blob = None
    self._is_fork_parent = False
    self._current_url_slug = None
    self._kernel_author_user_name = None
    self._viewer_url = ""
    self._freeze()

  @property
  def author(self) -> Optional['User']:
    return self._author

  @author.setter
  def author(self, author: Optional['User']):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author

  @property
  def version(self) -> Optional['KernelVersion']:
    return self._version

  @version.setter
  def version(self, version: Optional['KernelVersion']):
    if version is None:
      del self.version
      return
    if not isinstance(version, KernelVersion):
      raise TypeError('version must be of type KernelVersion')
    self._version = version

  @property
  def run(self) -> Optional['KernelRun']:
    return self._run

  @run.setter
  def run(self, run: Optional['KernelRun']):
    if run is None:
      del self.run
      return
    if not isinstance(run, KernelRun):
      raise TypeError('run must be of type KernelRun')
    self._run = run

  @property
  def blob(self) -> Optional['KernelBlob']:
    return self._blob

  @blob.setter
  def blob(self, blob: Optional['KernelBlob']):
    if blob is None:
      del self.blob
      return
    if not isinstance(blob, KernelBlob):
      raise TypeError('blob must be of type KernelBlob')
    self._blob = blob

  @property
  def is_fork_parent(self) -> bool:
    return self._is_fork_parent

  @is_fork_parent.setter
  def is_fork_parent(self, is_fork_parent: bool):
    if is_fork_parent is None:
      del self.is_fork_parent
      return
    if not isinstance(is_fork_parent, bool):
      raise TypeError('is_fork_parent must be of type bool')
    self._is_fork_parent = is_fork_parent

  @property
  def current_url_slug(self) -> str:
    return self._current_url_slug or ""

  @current_url_slug.setter
  def current_url_slug(self, current_url_slug: Optional[str]):
    if current_url_slug is None:
      del self.current_url_slug
      return
    if not isinstance(current_url_slug, str):
      raise TypeError('current_url_slug must be of type str')
    self._current_url_slug = current_url_slug

  @property
  def kernel_author_user_name(self) -> str:
    return self._kernel_author_user_name or ""

  @kernel_author_user_name.setter
  def kernel_author_user_name(self, kernel_author_user_name: Optional[str]):
    if kernel_author_user_name is None:
      del self.kernel_author_user_name
      return
    if not isinstance(kernel_author_user_name, str):
      raise TypeError('kernel_author_user_name must be of type str')
    self._kernel_author_user_name = kernel_author_user_name

  @property
  def viewer_url(self) -> str:
    return self._viewer_url

  @viewer_url.setter
  def viewer_url(self, viewer_url: str):
    if viewer_url is None:
      del self.viewer_url
      return
    if not isinstance(viewer_url, str):
      raise TypeError('viewer_url must be of type str')
    self._viewer_url = viewer_url


class KernelVersionList(KaggleObject):
  r"""
  NOTE: This model only works until we move away from the 1:1 relationship for
  Version:Run.

  Attributes:
    items (KernelVersionAndRun)
  """

  def __init__(self):
    self._items = []
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['KernelVersionAndRun']]]:
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['KernelVersionAndRun']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, KernelVersionAndRun) for t in items]):
      raise TypeError('items must contain only items of type KernelVersionAndRun')
    self._items = items


class ListColabFilesRequest(KaggleObject):
  r"""
  Attributes:
    search_query (str)
    order_by (ListColabSortType)
    order_by_ascending (bool)
    limit_to_owned_by_me (bool)
    is_test_request (bool)
  """

  def __init__(self):
    self._search_query = None
    self._order_by = None
    self._order_by_ascending = None
    self._limit_to_owned_by_me = False
    self._is_test_request = None
    self._freeze()

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def order_by(self) -> 'ListColabSortType':
    return self._order_by or ListColabSortType.NAME

  @order_by.setter
  def order_by(self, order_by: Optional['ListColabSortType']):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListColabSortType):
      raise TypeError('order_by must be of type ListColabSortType')
    self._order_by = order_by

  @property
  def order_by_ascending(self) -> bool:
    return self._order_by_ascending or False

  @order_by_ascending.setter
  def order_by_ascending(self, order_by_ascending: Optional[bool]):
    if order_by_ascending is None:
      del self.order_by_ascending
      return
    if not isinstance(order_by_ascending, bool):
      raise TypeError('order_by_ascending must be of type bool')
    self._order_by_ascending = order_by_ascending

  @property
  def limit_to_owned_by_me(self) -> bool:
    return self._limit_to_owned_by_me

  @limit_to_owned_by_me.setter
  def limit_to_owned_by_me(self, limit_to_owned_by_me: bool):
    if limit_to_owned_by_me is None:
      del self.limit_to_owned_by_me
      return
    if not isinstance(limit_to_owned_by_me, bool):
      raise TypeError('limit_to_owned_by_me must be of type bool')
    self._limit_to_owned_by_me = limit_to_owned_by_me

  @property
  def is_test_request(self) -> bool:
    return self._is_test_request or False

  @is_test_request.setter
  def is_test_request(self, is_test_request: Optional[bool]):
    if is_test_request is None:
      del self.is_test_request
      return
    if not isinstance(is_test_request, bool):
      raise TypeError('is_test_request must be of type bool')
    self._is_test_request = is_test_request


class ListColabFilesResponse(KaggleObject):
  r"""
  Attributes:
    files (ListColabFilesResponse.ColabFileInfo)
  """

  class ColabFileInfo(KaggleObject):
    r"""
    Attributes:
      drive_id (str)
      title (str)
      owners (ListColabFilesResponse.DriveOwner)
      owned_by_me (bool)
      thumbnail_link (str)
      created_time (str)
      last_activity_time (str)
        Defaults to viewedByMeTime, but if user has access to a file and it has
        not been opened createdTime is used instead.
      size (int)
        The size of the file in binary (ex: 1024 bytes = 1 KB)
    """

    def __init__(self):
      self._drive_id = ""
      self._title = ""
      self._owners = []
      self._owned_by_me = False
      self._thumbnail_link = None
      self._created_time = ""
      self._last_activity_time = ""
      self._size = 0
      self._freeze()

    @property
    def drive_id(self) -> str:
      return self._drive_id

    @drive_id.setter
    def drive_id(self, drive_id: str):
      if drive_id is None:
        del self.drive_id
        return
      if not isinstance(drive_id, str):
        raise TypeError('drive_id must be of type str')
      self._drive_id = drive_id

    @property
    def title(self) -> str:
      return self._title

    @title.setter
    def title(self, title: str):
      if title is None:
        del self.title
        return
      if not isinstance(title, str):
        raise TypeError('title must be of type str')
      self._title = title

    @property
    def owners(self) -> Optional[List[Optional['ListColabFilesResponse.DriveOwner']]]:
      return self._owners

    @owners.setter
    def owners(self, owners: Optional[List[Optional['ListColabFilesResponse.DriveOwner']]]):
      if owners is None:
        del self.owners
        return
      if not isinstance(owners, list):
        raise TypeError('owners must be of type list')
      if not all([isinstance(t, ListColabFilesResponse.DriveOwner) for t in owners]):
        raise TypeError('owners must contain only items of type ListColabFilesResponse.DriveOwner')
      self._owners = owners

    @property
    def owned_by_me(self) -> bool:
      return self._owned_by_me

    @owned_by_me.setter
    def owned_by_me(self, owned_by_me: bool):
      if owned_by_me is None:
        del self.owned_by_me
        return
      if not isinstance(owned_by_me, bool):
        raise TypeError('owned_by_me must be of type bool')
      self._owned_by_me = owned_by_me

    @property
    def thumbnail_link(self) -> str:
      return self._thumbnail_link or ""

    @thumbnail_link.setter
    def thumbnail_link(self, thumbnail_link: Optional[str]):
      if thumbnail_link is None:
        del self.thumbnail_link
        return
      if not isinstance(thumbnail_link, str):
        raise TypeError('thumbnail_link must be of type str')
      self._thumbnail_link = thumbnail_link

    @property
    def created_time(self) -> str:
      return self._created_time

    @created_time.setter
    def created_time(self, created_time: str):
      if created_time is None:
        del self.created_time
        return
      if not isinstance(created_time, str):
        raise TypeError('created_time must be of type str')
      self._created_time = created_time

    @property
    def last_activity_time(self) -> str:
      r"""
      Defaults to viewedByMeTime, but if user has access to a file and it has
      not been opened createdTime is used instead.
      """
      return self._last_activity_time

    @last_activity_time.setter
    def last_activity_time(self, last_activity_time: str):
      if last_activity_time is None:
        del self.last_activity_time
        return
      if not isinstance(last_activity_time, str):
        raise TypeError('last_activity_time must be of type str')
      self._last_activity_time = last_activity_time

    @property
    def size(self) -> int:
      """The size of the file in binary (ex: 1024 bytes = 1 KB)"""
      return self._size

    @size.setter
    def size(self, size: int):
      if size is None:
        del self.size
        return
      if not isinstance(size, int):
        raise TypeError('size must be of type int')
      self._size = size


  class DriveOwner(KaggleObject):
    r"""
    Attributes:
      display_name (str)
      thumbnail_url (str)
    """

    def __init__(self):
      self._display_name = ""
      self._thumbnail_url = None
      self._freeze()

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
    def thumbnail_url(self) -> str:
      return self._thumbnail_url or ""

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url: Optional[str]):
      if thumbnail_url is None:
        del self.thumbnail_url
        return
      if not isinstance(thumbnail_url, str):
        raise TypeError('thumbnail_url must be of type str')
      self._thumbnail_url = thumbnail_url


  def __init__(self):
    self._files = []
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['ListColabFilesResponse.ColabFileInfo']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['ListColabFilesResponse.ColabFileInfo']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, ListColabFilesResponse.ColabFileInfo) for t in files]):
      raise TypeError('files must contain only items of type ListColabFilesResponse.ColabFileInfo')
    self._files = files


class ListDockerImagesRequest(KaggleObject):
  r"""
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


class ListGithubRepositoriesRequest(KaggleObject):
  r"""
  Attributes:
    query (str)
      Free form search query term.
    page (int)
      Page index, starts at 0.
    per_page (int)
      Results to include per page.
    include_private (bool)
      Include private results.
      If the user doesn't have a GitHub OAuth access token, only public results
      are returned.
  """

  def __init__(self):
    self._query = None
    self._page = None
    self._per_page = None
    self._include_private = False
    self._freeze()

  @property
  def query(self) -> str:
    """Free form search query term."""
    return self._query or ""

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def page(self) -> int:
    """Page index, starts at 0."""
    return self._page or 0

  @page.setter
  def page(self, page: Optional[int]):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def per_page(self) -> int:
    """Results to include per page."""
    return self._per_page or 0

  @per_page.setter
  def per_page(self, per_page: Optional[int]):
    if per_page is None:
      del self.per_page
      return
    if not isinstance(per_page, int):
      raise TypeError('per_page must be of type int')
    self._per_page = per_page

  @property
  def include_private(self) -> bool:
    r"""
    Include private results.
    If the user doesn't have a GitHub OAuth access token, only public results
    are returned.
    """
    return self._include_private

  @include_private.setter
  def include_private(self, include_private: bool):
    if include_private is None:
      del self.include_private
      return
    if not isinstance(include_private, bool):
      raise TypeError('include_private must be of type bool')
    self._include_private = include_private


class ListGithubRepositoriesResponse(KaggleObject):
  r"""
  Attributes:
    repositories (GithubRepositoryInfo)
  """

  def __init__(self):
    self._repositories = []
    self._freeze()

  @property
  def repositories(self) -> Optional[List[Optional['GithubRepositoryInfo']]]:
    return self._repositories

  @repositories.setter
  def repositories(self, repositories: Optional[List[Optional['GithubRepositoryInfo']]]):
    if repositories is None:
      del self.repositories
      return
    if not isinstance(repositories, list):
      raise TypeError('repositories must be of type list')
    if not all([isinstance(t, GithubRepositoryInfo) for t in repositories]):
      raise TypeError('repositories must contain only items of type GithubRepositoryInfo')
    self._repositories = repositories


class ListGithubRepositoryBranchesRequest(KaggleObject):
  r"""
  Attributes:
    owner (str)
      The owner of the repo. e.g. 'Kaggle'.
    name (str)
      The name of the repo. e.g. 'docker-python'.
    include_private (bool)
      Include private results.
      If the user doesn't have a GitHub OAuth access token, only public results
      are returned.
  """

  def __init__(self):
    self._owner = ""
    self._name = ""
    self._include_private = False
    self._freeze()

  @property
  def owner(self) -> str:
    """The owner of the repo. e.g. 'Kaggle'."""
    return self._owner

  @owner.setter
  def owner(self, owner: str):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def name(self) -> str:
    """The name of the repo. e.g. 'docker-python'."""
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
  def include_private(self) -> bool:
    r"""
    Include private results.
    If the user doesn't have a GitHub OAuth access token, only public results
    are returned.
    """
    return self._include_private

  @include_private.setter
  def include_private(self, include_private: bool):
    if include_private is None:
      del self.include_private
      return
    if not isinstance(include_private, bool):
      raise TypeError('include_private must be of type bool')
    self._include_private = include_private


class ListGithubRepositoryBranchesResponse(KaggleObject):
  r"""
  Attributes:
    branches (GithubBranchInfo)
  """

  def __init__(self):
    self._branches = []
    self._freeze()

  @property
  def branches(self) -> Optional[List[Optional['GithubBranchInfo']]]:
    return self._branches

  @branches.setter
  def branches(self, branches: Optional[List[Optional['GithubBranchInfo']]]):
    if branches is None:
      del self.branches
      return
    if not isinstance(branches, list):
      raise TypeError('branches must be of type list')
    if not all([isinstance(t, GithubBranchInfo) for t in branches]):
      raise TypeError('branches must contain only items of type GithubBranchInfo')
    self._branches = branches


class ListGithubRepositoryFilesRequest(KaggleObject):
  r"""
  Attributes:
    owner (str)
      The owner of the repo. e.g. 'Kaggle'.
    name (str)
      The name of the repo. e.g. 'docker-python'.
    branch (str)
      The name of the branch. e.g. 'master'.
    file_extension_filter (str)
      Extensions (including the period '.') to filter by. If empty, return all
      files.
    include_private (bool)
      Include private results.
      If the user doesn't have a GitHub OAuth access token, only public results
      are returned.
  """

  def __init__(self):
    self._owner = None
    self._name = None
    self._branch = None
    self._file_extension_filter = []
    self._include_private = False
    self._freeze()

  @property
  def owner(self) -> str:
    """The owner of the repo. e.g. 'Kaggle'."""
    return self._owner or ""

  @owner.setter
  def owner(self, owner: Optional[str]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, str):
      raise TypeError('owner must be of type str')
    self._owner = owner

  @property
  def name(self) -> str:
    """The name of the repo. e.g. 'docker-python'."""
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
  def branch(self) -> str:
    """The name of the branch. e.g. 'master'."""
    return self._branch or ""

  @branch.setter
  def branch(self, branch: Optional[str]):
    if branch is None:
      del self.branch
      return
    if not isinstance(branch, str):
      raise TypeError('branch must be of type str')
    self._branch = branch

  @property
  def file_extension_filter(self) -> Optional[List[str]]:
    r"""
    Extensions (including the period '.') to filter by. If empty, return all
    files.
    """
    return self._file_extension_filter

  @file_extension_filter.setter
  def file_extension_filter(self, file_extension_filter: Optional[List[str]]):
    if file_extension_filter is None:
      del self.file_extension_filter
      return
    if not isinstance(file_extension_filter, list):
      raise TypeError('file_extension_filter must be of type list')
    if not all([isinstance(t, str) for t in file_extension_filter]):
      raise TypeError('file_extension_filter must contain only items of type str')
    self._file_extension_filter = file_extension_filter

  @property
  def include_private(self) -> bool:
    r"""
    Include private results.
    If the user doesn't have a GitHub OAuth access token, only public results
    are returned.
    """
    return self._include_private

  @include_private.setter
  def include_private(self, include_private: bool):
    if include_private is None:
      del self.include_private
      return
    if not isinstance(include_private, bool):
      raise TypeError('include_private must be of type bool')
    self._include_private = include_private


class ListGithubRepositoryFilesResponse(KaggleObject):
  r"""
  Attributes:
    files (GithubFileInfo)
  """

  def __init__(self):
    self._files = []
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['GithubFileInfo']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['GithubFileInfo']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, GithubFileInfo) for t in files]):
      raise TypeError('files must contain only items of type GithubFileInfo')
    self._files = files


class ListKernelIdsResponse(KaggleObject):
  r"""
  Attributes:
    kernel_ids (int)
  """

  def __init__(self):
    self._kernel_ids = []
    self._freeze()

  @property
  def kernel_ids(self) -> Optional[List[int]]:
    return self._kernel_ids

  @kernel_ids.setter
  def kernel_ids(self, kernel_ids: Optional[List[int]]):
    if kernel_ids is None:
      del self.kernel_ids
      return
    if not isinstance(kernel_ids, list):
      raise TypeError('kernel_ids must be of type list')
    if not all([isinstance(t, int) for t in kernel_ids]):
      raise TypeError('kernel_ids must contain only items of type int')
    self._kernel_ids = kernel_ids


class ListKernelSessionOutputFilesHierarchicalRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    relative_path (str)
    offset (str)
    max_results (int)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._relative_path = None
    self._offset = None
    self._max_results = 0
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

  @property
  def relative_path(self) -> str:
    return self._relative_path or ""

  @relative_path.setter
  def relative_path(self, relative_path: Optional[str]):
    if relative_path is None:
      del self.relative_path
      return
    if not isinstance(relative_path, str):
      raise TypeError('relative_path must be of type str')
    self._relative_path = relative_path

  @property
  def offset(self) -> str:
    return self._offset or ""

  @offset.setter
  def offset(self, offset: Optional[str]):
    if offset is None:
      del self.offset
      return
    if not isinstance(offset, str):
      raise TypeError('offset must be of type str')
    self._offset = offset

  @property
  def max_results(self) -> int:
    return self._max_results

  @max_results.setter
  def max_results(self, max_results: int):
    if max_results is None:
      del self.max_results
      return
    if not isinstance(max_results, int):
      raise TypeError('max_results must be of type int')
    self._max_results = max_results


class ListKernelSessionOutputFilesHierarchicalResponse(KaggleObject):
  r"""
  Attributes:
    directories (Directory)
    files (File)
    next_page_token (str)
  """

  def __init__(self):
    self._directories = []
    self._files = []
    self._next_page_token = None
    self._freeze()

  @property
  def directories(self) -> Optional[List[Optional['Directory']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['Directory']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, Directory) for t in directories]):
      raise TypeError('directories must contain only items of type Directory')
    self._directories = directories

  @property
  def files(self) -> Optional[List[Optional['File']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['File']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, File) for t in files]):
      raise TypeError('files must contain only items of type File')
    self._files = files

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


class ListKernelSessionOutputRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    page_size (int)
    page_token (str)
    file_path (str)
      If specified, only return files matching this path exactly
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._page_size = None
    self._page_token = None
    self._file_path = None
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

  @property
  def page_size(self) -> int:
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def file_path(self) -> str:
    """If specified, only return files matching this path exactly"""
    return self._file_path or ""

  @file_path.setter
  def file_path(self, file_path: Optional[str]):
    if file_path is None:
      del self.file_path
      return
    if not isinstance(file_path, str):
      raise TypeError('file_path must be of type str')
    self._file_path = file_path


class ListKernelSessionOutputResponse(KaggleObject):
  r"""
  Attributes:
    items (KernelSessionOutputFile)
    next_page_token (str)
  """

  def __init__(self):
    self._items = []
    self._next_page_token = None
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['KernelSessionOutputFile']]]:
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['KernelSessionOutputFile']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, KernelSessionOutputFile) for t in items]):
      raise TypeError('items must contain only items of type KernelSessionOutputFile')
    self._items = items

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


class ListKernelSessionsRequest(KaggleObject):
  r"""
  """

  pass

class ListKernelVersionsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    sort_option (ListKernelVersionsRequest.SortOption)
    page_size (int)
    read_mask (FieldMask)
  """

  class SortOption(enum.Enum):
    SORT_OPTION_UNSPECIFIED = 0
    VERSION_ID = 1
    VERSION_DATE_UPDATED = 2

  def __init__(self):
    self._kernel_id = 0
    self._sort_option = self.SortOption.SORT_OPTION_UNSPECIFIED
    self._page_size = None
    self._read_mask = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def sort_option(self) -> 'ListKernelVersionsRequest.SortOption':
    return self._sort_option

  @sort_option.setter
  def sort_option(self, sort_option: 'ListKernelVersionsRequest.SortOption'):
    if sort_option is None:
      del self.sort_option
      return
    if not isinstance(sort_option, ListKernelVersionsRequest.SortOption):
      raise TypeError('sort_option must be of type ListKernelVersionsRequest.SortOption')
    self._sort_option = sort_option

  @property
  def page_size(self) -> int:
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ModelSource(KaggleObject):
  r"""
  Attributes:
    current_user_upvoted (bool)
    model_id (int)
    model_instance_framework (ModelFramework)
    model_instance_version_id (int)
    model_instance_version_url (str)
    model_instance_version_number (int)
    model_owner_image_url (str)
    model_owner_name (str)
    model_subtitle (str)
    model_tags (TagList)
    model_title (str)
    vote_count (int)
    model_instance_variation_slug (str)
    is_organization_owned (bool)
    notebook_count (int)
  """

  def __init__(self):
    self._current_user_upvoted = False
    self._model_id = 0
    self._model_instance_framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._model_instance_version_id = 0
    self._model_instance_version_url = ""
    self._model_instance_version_number = None
    self._model_owner_image_url = ""
    self._model_owner_name = ""
    self._model_subtitle = ""
    self._model_tags = None
    self._model_title = ""
    self._vote_count = 0
    self._model_instance_variation_slug = ""
    self._is_organization_owned = False
    self._notebook_count = 0
    self._freeze()

  @property
  def current_user_upvoted(self) -> bool:
    return self._current_user_upvoted

  @current_user_upvoted.setter
  def current_user_upvoted(self, current_user_upvoted: bool):
    if current_user_upvoted is None:
      del self.current_user_upvoted
      return
    if not isinstance(current_user_upvoted, bool):
      raise TypeError('current_user_upvoted must be of type bool')
    self._current_user_upvoted = current_user_upvoted

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def model_instance_framework(self) -> 'ModelFramework':
    return self._model_instance_framework

  @model_instance_framework.setter
  def model_instance_framework(self, model_instance_framework: 'ModelFramework'):
    if model_instance_framework is None:
      del self.model_instance_framework
      return
    if not isinstance(model_instance_framework, ModelFramework):
      raise TypeError('model_instance_framework must be of type ModelFramework')
    self._model_instance_framework = model_instance_framework

  @property
  def model_instance_variation_slug(self) -> str:
    return self._model_instance_variation_slug

  @model_instance_variation_slug.setter
  def model_instance_variation_slug(self, model_instance_variation_slug: str):
    if model_instance_variation_slug is None:
      del self.model_instance_variation_slug
      return
    if not isinstance(model_instance_variation_slug, str):
      raise TypeError('model_instance_variation_slug must be of type str')
    self._model_instance_variation_slug = model_instance_variation_slug

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: int):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    self._model_instance_version_id = model_instance_version_id

  @property
  def model_instance_version_url(self) -> str:
    return self._model_instance_version_url

  @model_instance_version_url.setter
  def model_instance_version_url(self, model_instance_version_url: str):
    if model_instance_version_url is None:
      del self.model_instance_version_url
      return
    if not isinstance(model_instance_version_url, str):
      raise TypeError('model_instance_version_url must be of type str')
    self._model_instance_version_url = model_instance_version_url

  @property
  def model_instance_version_number(self) -> int:
    return self._model_instance_version_number or 0

  @model_instance_version_number.setter
  def model_instance_version_number(self, model_instance_version_number: Optional[int]):
    if model_instance_version_number is None:
      del self.model_instance_version_number
      return
    if not isinstance(model_instance_version_number, int):
      raise TypeError('model_instance_version_number must be of type int')
    self._model_instance_version_number = model_instance_version_number

  @property
  def model_owner_image_url(self) -> str:
    return self._model_owner_image_url

  @model_owner_image_url.setter
  def model_owner_image_url(self, model_owner_image_url: str):
    if model_owner_image_url is None:
      del self.model_owner_image_url
      return
    if not isinstance(model_owner_image_url, str):
      raise TypeError('model_owner_image_url must be of type str')
    self._model_owner_image_url = model_owner_image_url

  @property
  def model_owner_name(self) -> str:
    return self._model_owner_name

  @model_owner_name.setter
  def model_owner_name(self, model_owner_name: str):
    if model_owner_name is None:
      del self.model_owner_name
      return
    if not isinstance(model_owner_name, str):
      raise TypeError('model_owner_name must be of type str')
    self._model_owner_name = model_owner_name

  @property
  def model_subtitle(self) -> str:
    return self._model_subtitle

  @model_subtitle.setter
  def model_subtitle(self, model_subtitle: str):
    if model_subtitle is None:
      del self.model_subtitle
      return
    if not isinstance(model_subtitle, str):
      raise TypeError('model_subtitle must be of type str')
    self._model_subtitle = model_subtitle

  @property
  def model_tags(self) -> Optional['TagList']:
    return self._model_tags

  @model_tags.setter
  def model_tags(self, model_tags: Optional['TagList']):
    if model_tags is None:
      del self.model_tags
      return
    if not isinstance(model_tags, TagList):
      raise TypeError('model_tags must be of type TagList')
    self._model_tags = model_tags

  @property
  def model_title(self) -> str:
    return self._model_title

  @model_title.setter
  def model_title(self, model_title: str):
    if model_title is None:
      del self.model_title
      return
    if not isinstance(model_title, str):
      raise TypeError('model_title must be of type str')
    self._model_title = model_title

  @property
  def vote_count(self) -> int:
    return self._vote_count

  @vote_count.setter
  def vote_count(self, vote_count: int):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def is_organization_owned(self) -> bool:
    return self._is_organization_owned

  @is_organization_owned.setter
  def is_organization_owned(self, is_organization_owned: bool):
    if is_organization_owned is None:
      del self.is_organization_owned
      return
    if not isinstance(is_organization_owned, bool):
      raise TypeError('is_organization_owned must be of type bool')
    self._is_organization_owned = is_organization_owned

  @property
  def notebook_count(self) -> int:
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count


class PushToGithubRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    save_request (GitHubSaveRequest)
    source (str)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._save_request = None
    self._source = None
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

  @property
  def save_request(self) -> Optional['GitHubSaveRequest']:
    return self._save_request

  @save_request.setter
  def save_request(self, save_request: Optional['GitHubSaveRequest']):
    if save_request is None:
      del self.save_request
      return
    if not isinstance(save_request, GitHubSaveRequest):
      raise TypeError('save_request must be of type GitHubSaveRequest')
    self._save_request = save_request

  @property
  def source(self) -> str:
    return self._source or ""

  @source.setter
  def source(self, source: Optional[str]):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source


class PushToGithubResponse(KaggleObject):
  r"""
  Attributes:
    spec (GithubSpec)
  """

  def __init__(self):
    self._spec = None
    self._freeze()

  @property
  def spec(self) -> Optional['GithubSpec']:
    return self._spec or None

  @spec.setter
  def spec(self, spec: Optional[Optional['GithubSpec']]):
    if spec is None:
      del self.spec
      return
    if not isinstance(spec, GithubSpec):
      raise TypeError('spec must be of type GithubSpec')
    self._spec = spec


class RemoveKernelCategoryRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    category_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._category_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def category_id(self) -> int:
    return self._category_id

  @category_id.setter
  def category_id(self, category_id: int):
    if category_id is None:
      del self.category_id
      return
    if not isinstance(category_id, int):
      raise TypeError('category_id must be of type int')
    self._category_id = category_id


class RunEpisodeRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    episode_id (int)
    environment (str)
    episode_type (EpisodeType)
    agents (AgentEntry)
    configuration (str)
    render_type (EnvironmentRenderType)
    docker_image_name_override (str)
    pool_name_override (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._episode_id = 0
    self._environment = None
    self._episode_type = EpisodeType.EPISODE_TYPE_UNSPECIFIED
    self._agents = []
    self._configuration = None
    self._render_type = EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED
    self._docker_image_name_override = None
    self._pool_name_override = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def episode_id(self) -> int:
    return self._episode_id

  @episode_id.setter
  def episode_id(self, episode_id: int):
    if episode_id is None:
      del self.episode_id
      return
    if not isinstance(episode_id, int):
      raise TypeError('episode_id must be of type int')
    self._episode_id = episode_id

  @property
  def environment(self) -> str:
    return self._environment or ""

  @environment.setter
  def environment(self, environment: Optional[str]):
    if environment is None:
      del self.environment
      return
    if not isinstance(environment, str):
      raise TypeError('environment must be of type str')
    self._environment = environment

  @property
  def episode_type(self) -> 'EpisodeType':
    return self._episode_type

  @episode_type.setter
  def episode_type(self, episode_type: 'EpisodeType'):
    if episode_type is None:
      del self.episode_type
      return
    if not isinstance(episode_type, EpisodeType):
      raise TypeError('episode_type must be of type EpisodeType')
    self._episode_type = episode_type

  @property
  def agents(self) -> Optional[List[Optional['AgentEntry']]]:
    return self._agents

  @agents.setter
  def agents(self, agents: Optional[List[Optional['AgentEntry']]]):
    if agents is None:
      del self.agents
      return
    if not isinstance(agents, list):
      raise TypeError('agents must be of type list')
    if not all([isinstance(t, AgentEntry) for t in agents]):
      raise TypeError('agents must contain only items of type AgentEntry')
    self._agents = agents

  @property
  def configuration(self) -> str:
    return self._configuration or ""

  @configuration.setter
  def configuration(self, configuration: Optional[str]):
    if configuration is None:
      del self.configuration
      return
    if not isinstance(configuration, str):
      raise TypeError('configuration must be of type str')
    self._configuration = configuration

  @property
  def render_type(self) -> 'EnvironmentRenderType':
    return self._render_type

  @render_type.setter
  def render_type(self, render_type: 'EnvironmentRenderType'):
    if render_type is None:
      del self.render_type
      return
    if not isinstance(render_type, EnvironmentRenderType):
      raise TypeError('render_type must be of type EnvironmentRenderType')
    self._render_type = render_type

  @property
  def docker_image_name_override(self) -> str:
    return self._docker_image_name_override or ""

  @docker_image_name_override.setter
  def docker_image_name_override(self, docker_image_name_override: Optional[str]):
    if docker_image_name_override is None:
      del self.docker_image_name_override
      return
    if not isinstance(docker_image_name_override, str):
      raise TypeError('docker_image_name_override must be of type str')
    self._docker_image_name_override = docker_image_name_override

  @property
  def pool_name_override(self) -> str:
    return self._pool_name_override or ""

  @pool_name_override.setter
  def pool_name_override(self, pool_name_override: Optional[str]):
    if pool_name_override is None:
      del self.pool_name_override
      return
    if not isinstance(pool_name_override, str):
      raise TypeError('pool_name_override must be of type str')
    self._pool_name_override = pool_name_override


class RunEpisodeResponse(KaggleObject):
  r"""
  Attributes:
    episode (str)
  """

  def __init__(self):
    self._episode = None
    self._freeze()

  @property
  def episode(self) -> str:
    return self._episode or ""

  @episode.setter
  def episode(self, episode: Optional[str]):
    if episode is None:
      del self.episode
      return
    if not isinstance(episode, str):
      raise TypeError('episode must be of type str')
    self._episode = episode


class ScheduledKernelSession(KaggleObject):
  r"""
  Attributes:
    id (int)
      ID of the scheduling.
    kernel_id (int)
      ID of the kernel which is being scheduled.
    creation_date (datetime)
      Timestamp of the creation of the scheduling.
    start_date (datetime)
      Timestamp after which the first scheduled run will be triggered.
    frequency (ScheduleFrequencyType)
      How often to execute the notebook.
      SCHEDULED_TIME only.
    iterations (int)
      Number of times this schedule should be repeated.
      SCHEDULED_TIME only.
    iteration (int)
      Number of times this schedule has been run already.
    trigger (ScheduleTriggerType)
      Determines what triggers this kernel to be run.
    last_session_date (datetime)
      Timestamp when this schedule was last executed.
  """

  def __init__(self):
    self._id = 0
    self._kernel_id = 0
    self._creation_date = None
    self._start_date = None
    self._frequency = ScheduleFrequencyType.SCHEDULE_FREQUENCY_UNSPECIFIED
    self._iterations = 0
    self._iteration = 0
    self._trigger = ScheduleTriggerType.SCHEDULE_TRIGGER_TYPE_UNSPECIFIED
    self._last_session_date = None
    self._freeze()

  @property
  def id(self) -> int:
    """ID of the scheduling."""
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
  def kernel_id(self) -> int:
    """ID of the kernel which is being scheduled."""
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def creation_date(self) -> datetime:
    """Timestamp of the creation of the scheduling."""
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date

  @property
  def start_date(self) -> datetime:
    """Timestamp after which the first scheduled run will be triggered."""
    return self._start_date

  @start_date.setter
  def start_date(self, start_date: datetime):
    if start_date is None:
      del self.start_date
      return
    if not isinstance(start_date, datetime):
      raise TypeError('start_date must be of type datetime')
    self._start_date = start_date

  @property
  def last_session_date(self) -> datetime:
    """Timestamp when this schedule was last executed."""
    return self._last_session_date

  @last_session_date.setter
  def last_session_date(self, last_session_date: datetime):
    if last_session_date is None:
      del self.last_session_date
      return
    if not isinstance(last_session_date, datetime):
      raise TypeError('last_session_date must be of type datetime')
    self._last_session_date = last_session_date

  @property
  def frequency(self) -> 'ScheduleFrequencyType':
    r"""
    How often to execute the notebook.
    SCHEDULED_TIME only.
    """
    return self._frequency

  @frequency.setter
  def frequency(self, frequency: 'ScheduleFrequencyType'):
    if frequency is None:
      del self.frequency
      return
    if not isinstance(frequency, ScheduleFrequencyType):
      raise TypeError('frequency must be of type ScheduleFrequencyType')
    self._frequency = frequency

  @property
  def iterations(self) -> int:
    r"""
    Number of times this schedule should be repeated.
    SCHEDULED_TIME only.
    """
    return self._iterations

  @iterations.setter
  def iterations(self, iterations: int):
    if iterations is None:
      del self.iterations
      return
    if not isinstance(iterations, int):
      raise TypeError('iterations must be of type int')
    self._iterations = iterations

  @property
  def iteration(self) -> int:
    """Number of times this schedule has been run already."""
    return self._iteration

  @iteration.setter
  def iteration(self, iteration: int):
    if iteration is None:
      del self.iteration
      return
    if not isinstance(iteration, int):
      raise TypeError('iteration must be of type int')
    self._iteration = iteration

  @property
  def trigger(self) -> 'ScheduleTriggerType':
    """Determines what triggers this kernel to be run."""
    return self._trigger

  @trigger.setter
  def trigger(self, trigger: 'ScheduleTriggerType'):
    if trigger is None:
      del self.trigger
      return
    if not isinstance(trigger, ScheduleTriggerType):
      raise TypeError('trigger must be of type ScheduleTriggerType')
    self._trigger = trigger


class ScheduleKernelImportsRequest(KaggleObject):
  r"""
  Attributes:
    imports (KernelImport)
  """

  def __init__(self):
    self._imports = []
    self._freeze()

  @property
  def imports(self) -> Optional[List[Optional['KernelImport']]]:
    return self._imports

  @imports.setter
  def imports(self, imports: Optional[List[Optional['KernelImport']]]):
    if imports is None:
      del self.imports
      return
    if not isinstance(imports, list):
      raise TypeError('imports must be of type list')
    if not all([isinstance(t, KernelImport) for t in imports]):
      raise TypeError('imports must contain only items of type KernelImport')
    self._imports = imports


class ScheduleKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
      ID of the kernel which is being scheduled.
    frequency (ScheduleFrequencyType)
      How often to execute the notebook.
      SCHEDULED_TIME only.
    start_date (datetime)
      Timestamp after which the first scheduled run will be triggered.
    iterations (int)
      Number of times this schedule should be repeated.
      SCHEDULED_TIME only.
    trigger (ScheduleTriggerType)
      Determines what triggers this kernel to be run.
  """

  def __init__(self):
    self._kernel_id = 0
    self._frequency = ScheduleFrequencyType.SCHEDULE_FREQUENCY_UNSPECIFIED
    self._start_date = None
    self._iterations = 0
    self._trigger = ScheduleTriggerType.SCHEDULE_TRIGGER_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def kernel_id(self) -> int:
    """ID of the kernel which is being scheduled."""
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def trigger(self) -> 'ScheduleTriggerType':
    """Determines what triggers this kernel to be run."""
    return self._trigger

  @trigger.setter
  def trigger(self, trigger: 'ScheduleTriggerType'):
    if trigger is None:
      del self.trigger
      return
    if not isinstance(trigger, ScheduleTriggerType):
      raise TypeError('trigger must be of type ScheduleTriggerType')
    self._trigger = trigger

  @property
  def frequency(self) -> 'ScheduleFrequencyType':
    r"""
    How often to execute the notebook.
    SCHEDULED_TIME only.
    """
    return self._frequency

  @frequency.setter
  def frequency(self, frequency: 'ScheduleFrequencyType'):
    if frequency is None:
      del self.frequency
      return
    if not isinstance(frequency, ScheduleFrequencyType):
      raise TypeError('frequency must be of type ScheduleFrequencyType')
    self._frequency = frequency

  @property
  def start_date(self) -> datetime:
    """Timestamp after which the first scheduled run will be triggered."""
    return self._start_date

  @start_date.setter
  def start_date(self, start_date: datetime):
    if start_date is None:
      del self.start_date
      return
    if not isinstance(start_date, datetime):
      raise TypeError('start_date must be of type datetime')
    self._start_date = start_date

  @property
  def iterations(self) -> int:
    r"""
    Number of times this schedule should be repeated.
    SCHEDULED_TIME only.
    """
    return self._iterations

  @iterations.setter
  def iterations(self, iterations: int):
    if iterations is None:
      del self.iterations
      return
    if not isinstance(iterations, int):
      raise TypeError('iterations must be of type int')
    self._iterations = iterations


class SearchKernelCollaboratorsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    search (str)
    page (int)
    show_private (bool)
    results_per_page (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._search = ""
    self._page = 0
    self._show_private = False
    self._results_per_page = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def search(self) -> str:
    return self._search

  @search.setter
  def search(self, search: str):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

  @property
  def page(self) -> int:
    return self._page

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def show_private(self) -> bool:
    return self._show_private

  @show_private.setter
  def show_private(self, show_private: bool):
    if show_private is None:
      del self.show_private
      return
    if not isinstance(show_private, bool):
      raise TypeError('show_private must be of type bool')
    self._show_private = show_private

  @property
  def results_per_page(self) -> int:
    return self._results_per_page

  @results_per_page.setter
  def results_per_page(self, results_per_page: int):
    if results_per_page is None:
      del self.results_per_page
      return
    if not isinstance(results_per_page, int):
      raise TypeError('results_per_page must be of type int')
    self._results_per_page = results_per_page


class SearchKernelCollaboratorsResponse(KaggleObject):
  r"""
  Attributes:
    results (CollaboratorItem)
  """

  def __init__(self):
    self._results = []
    self._freeze()

  @property
  def results(self) -> Optional[List[Optional['CollaboratorItem']]]:
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['CollaboratorItem']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, CollaboratorItem) for t in results]):
      raise TypeError('results must contain only items of type CollaboratorItem')
    self._results = results


class SearchKernelIdsResponse(KaggleObject):
  r"""
  Attributes:
    kernel_ids (int)
  """

  def __init__(self):
    self._kernel_ids = []
    self._freeze()

  @property
  def kernel_ids(self) -> Optional[List[int]]:
    return self._kernel_ids

  @kernel_ids.setter
  def kernel_ids(self, kernel_ids: Optional[List[int]]):
    if kernel_ids is None:
      del self.kernel_ids
      return
    if not isinstance(kernel_ids, list):
      raise TypeError('kernel_ids must be of type list')
    if not all([isinstance(t, int) for t in kernel_ids]):
      raise TypeError('kernel_ids must contain only items of type int')
    self._kernel_ids = kernel_ids


class SnippetData(KaggleObject):
  r"""
  Attributes:
    title (str)
    tags (str)
    content (str)
    language_name (str)
    is_private (bool)
  """

  def __init__(self):
    self._title = None
    self._tags = None
    self._content = None
    self._language_name = None
    self._is_private = False
    self._freeze()

  @property
  def title(self) -> str:
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
  def tags(self) -> str:
    return self._tags or ""

  @tags.setter
  def tags(self, tags: Optional[str]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, str):
      raise TypeError('tags must be of type str')
    self._tags = tags

  @property
  def content(self) -> str:
    return self._content or ""

  @content.setter
  def content(self, content: Optional[str]):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

  @property
  def language_name(self) -> str:
    return self._language_name or ""

  @language_name.setter
  def language_name(self, language_name: Optional[str]):
    if language_name is None:
      del self.language_name
      return
    if not isinstance(language_name, str):
      raise TypeError('language_name must be of type str')
    self._language_name = language_name

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private


class SubmissionRequestedDetails(KaggleObject):
  r"""
  The list of file names which are checked in order for a valid submission
  file. This field requires a list as simulation competitions allow multiple
  different file names. Important: This message is serialized to database in
  KernelSession.SubmissionRequestedDetails column as Json so be extra careful
  while making any changes.

  Attributes:
    file_names (str)
    description (str)
  """

  def __init__(self):
    self._file_names = []
    self._description = None
    self._freeze()

  @property
  def file_names(self) -> Optional[List[str]]:
    return self._file_names

  @file_names.setter
  def file_names(self, file_names: Optional[List[str]]):
    if file_names is None:
      del self.file_names
      return
    if not isinstance(file_names, list):
      raise TypeError('file_names must be of type list')
    if not all([isinstance(t, str) for t in file_names]):
      raise TypeError('file_names must contain only items of type str')
    self._file_names = file_names

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


class SyncHuggingFaceModelResourceReferenceMetadataRequest(KaggleObject):
  r"""
  Attributes:
    owner_identifier (str)
    resource_identifier (str)
    allow_missing (bool)
  """

  def __init__(self):
    self._owner_identifier = ""
    self._resource_identifier = ""
    self._allow_missing = False
    self._freeze()

  @property
  def owner_identifier(self) -> str:
    return self._owner_identifier

  @owner_identifier.setter
  def owner_identifier(self, owner_identifier: str):
    if owner_identifier is None:
      del self.owner_identifier
      return
    if not isinstance(owner_identifier, str):
      raise TypeError('owner_identifier must be of type str')
    self._owner_identifier = owner_identifier

  @property
  def resource_identifier(self) -> str:
    return self._resource_identifier

  @resource_identifier.setter
  def resource_identifier(self, resource_identifier: str):
    if resource_identifier is None:
      del self.resource_identifier
      return
    if not isinstance(resource_identifier, str):
      raise TypeError('resource_identifier must be of type str')
    self._resource_identifier = resource_identifier

  @property
  def allow_missing(self) -> bool:
    return self._allow_missing

  @allow_missing.setter
  def allow_missing(self, allow_missing: bool):
    if allow_missing is None:
      del self.allow_missing
      return
    if not isinstance(allow_missing, bool):
      raise TypeError('allow_missing must be of type bool')
    self._allow_missing = allow_missing


class Tag(KaggleObject):
  r"""
  Attributes:
    name (str)
    slug (str)
    url (str)
  """

  def __init__(self):
    self._name = None
    self._slug = None
    self._url = None
    self._freeze()

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
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class UpdateDataSourceResult(KaggleObject):
  r"""
  Attributes:
    reference (DataSourceReference)
      Data source reference passed to UpdateDataSourcesRequest.
    mounted_version (DataSourceVersion)
      The version that was mounted to the kernel before calling
      UpdateDataSources.
    new_version (DataSourceVersion)
      The new/latest version to which the data source is upgraded.
  """

  def __init__(self):
    self._reference = None
    self._mounted_version = None
    self._new_version = None
    self._freeze()

  @property
  def reference(self) -> Optional['DataSourceReference']:
    """Data source reference passed to UpdateDataSourcesRequest."""
    return self._reference

  @reference.setter
  def reference(self, reference: Optional['DataSourceReference']):
    if reference is None:
      del self.reference
      return
    if not isinstance(reference, DataSourceReference):
      raise TypeError('reference must be of type DataSourceReference')
    self._reference = reference

  @property
  def mounted_version(self) -> Optional['DataSourceVersion']:
    r"""
    The version that was mounted to the kernel before calling
    UpdateDataSources.
    """
    return self._mounted_version

  @mounted_version.setter
  def mounted_version(self, mounted_version: Optional['DataSourceVersion']):
    if mounted_version is None:
      del self.mounted_version
      return
    if not isinstance(mounted_version, DataSourceVersion):
      raise TypeError('mounted_version must be of type DataSourceVersion')
    self._mounted_version = mounted_version

  @property
  def new_version(self) -> Optional['DataSourceVersion']:
    """The new/latest version to which the data source is upgraded."""
    return self._new_version

  @new_version.setter
  def new_version(self, new_version: Optional['DataSourceVersion']):
    if new_version is None:
      del self.new_version
      return
    if not isinstance(new_version, DataSourceVersion):
      raise TypeError('new_version must be of type DataSourceVersion')
    self._new_version = new_version


class UpdateDataSourceVersionsRequest(KaggleObject):
  r"""
  Attributes:
    session_id (int)
    data_sources (DataSourceReference)
    dry_run (bool)
  """

  def __init__(self):
    self._session_id = 0
    self._data_sources = []
    self._dry_run = False
    self._freeze()

  @property
  def session_id(self) -> int:
    return self._session_id

  @session_id.setter
  def session_id(self, session_id: int):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def dry_run(self) -> bool:
    return self._dry_run

  @dry_run.setter
  def dry_run(self, dry_run: bool):
    if dry_run is None:
      del self.dry_run
      return
    if not isinstance(dry_run, bool):
      raise TypeError('dry_run must be of type bool')
    self._dry_run = dry_run


class UpdateDataSourceVersionsResponse(KaggleObject):
  r"""
  Attributes:
    results (UpdateDataSourceResult)
    any_changes (bool)
  """

  def __init__(self):
    self._results = []
    self._any_changes = False
    self._freeze()

  @property
  def results(self) -> Optional[List[Optional['UpdateDataSourceResult']]]:
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['UpdateDataSourceResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, UpdateDataSourceResult) for t in results]):
      raise TypeError('results must contain only items of type UpdateDataSourceResult')
    self._results = results

  @property
  def any_changes(self) -> bool:
    return self._any_changes

  @any_changes.setter
  def any_changes(self, any_changes: bool):
    if any_changes is None:
      del self.any_changes
      return
    if not isinstance(any_changes, bool):
      raise TypeError('any_changes must be of type bool')
    self._any_changes = any_changes


class UpdateDefaultSessionSettingsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    settings (DefaultSessionSettings)
    delete_sync_spec (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._settings = None
    self._delete_sync_spec = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def settings(self) -> Optional['DefaultSessionSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['DefaultSessionSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, DefaultSessionSettings):
      raise TypeError('settings must be of type DefaultSessionSettings')
    self._settings = settings

  @property
  def delete_sync_spec(self) -> bool:
    return self._delete_sync_spec or False

  @delete_sync_spec.setter
  def delete_sync_spec(self, delete_sync_spec: Optional[bool]):
    if delete_sync_spec is None:
      del self.delete_sync_spec
      return
    if not isinstance(delete_sync_spec, bool):
      raise TypeError('delete_sync_spec must be of type bool')
    self._delete_sync_spec = delete_sync_spec


class UpdateDependencyManagerPrivacyRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
      Kernel Id of the Parent Kernel.
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    """Kernel Id of the Parent Kernel."""
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class UpdateDockerImageVersionRequest(KaggleObject):
  r"""
  Attributes:
    script_id (int)
    docker_image_version_id (int)
  """

  def __init__(self):
    self._script_id = 0
    self._docker_image_version_id = None
    self._freeze()

  @property
  def script_id(self) -> int:
    return self._script_id

  @script_id.setter
  def script_id(self, script_id: int):
    if script_id is None:
      del self.script_id
      return
    if not isinstance(script_id, int):
      raise TypeError('script_id must be of type int')
    self._script_id = script_id

  @property
  def docker_image_version_id(self) -> int:
    return self._docker_image_version_id or 0

  @docker_image_version_id.setter
  def docker_image_version_id(self, docker_image_version_id: Optional[int]):
    if docker_image_version_id is None:
      del self.docker_image_version_id
      return
    if not isinstance(docker_image_version_id, int):
      raise TypeError('docker_image_version_id must be of type int')
    self._docker_image_version_id = docker_image_version_id


class UpdateDockerPinningTypeRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    docker_image_pinning_type (DockerImagePinningType)
  """

  def __init__(self):
    self._kernel_id = 0
    self._docker_image_pinning_type = DockerImagePinningType.DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def docker_image_pinning_type(self) -> 'DockerImagePinningType':
    return self._docker_image_pinning_type

  @docker_image_pinning_type.setter
  def docker_image_pinning_type(self, docker_image_pinning_type: 'DockerImagePinningType'):
    if docker_image_pinning_type is None:
      del self.docker_image_pinning_type
      return
    if not isinstance(docker_image_pinning_type, DockerImagePinningType):
      raise TypeError('docker_image_pinning_type must be of type DockerImagePinningType')
    self._docker_image_pinning_type = docker_image_pinning_type


class UpdateKernelCategoriesRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    category_ids (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._category_ids = []
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def category_ids(self) -> Optional[List[int]]:
    return self._category_ids

  @category_ids.setter
  def category_ids(self, category_ids: Optional[List[int]]):
    if category_ids is None:
      del self.category_ids
      return
    if not isinstance(category_ids, list):
      raise TypeError('category_ids must be of type list')
    if not all([isinstance(t, int) for t in category_ids]):
      raise TypeError('category_ids must contain only items of type int')
    self._category_ids = category_ids


class UpdateKernelCategoriesResponse(KaggleObject):
  r"""
  Attributes:
    category_ids (int)
  """

  def __init__(self):
    self._category_ids = []
    self._freeze()

  @property
  def category_ids(self) -> Optional[List[int]]:
    return self._category_ids

  @category_ids.setter
  def category_ids(self, category_ids: Optional[List[int]]):
    if category_ids is None:
      del self.category_ids
      return
    if not isinstance(category_ids, list):
      raise TypeError('category_ids must be of type list')
    if not all([isinstance(t, int) for t in category_ids]):
      raise TypeError('category_ids must contain only items of type int')
    self._category_ids = category_ids


class UpdateKernelDraftRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    sequence (int)
    parent_kernel_version_id (int)
    settings (KernelBlobSettings)
    source (str)
    external_source_data (ExternalSourceData)
    source_token (str)
      Optional: Read the source in from a GCS uploaded blob instead of passing
      directly. If set, ignores the passed source.
    github_spec (GithubSpec)
    update_mask (FieldMask)
    colab_spec (ColabSpec)
  """

  def __init__(self):
    self._kernel_id = 0
    self._sequence = 0
    self._parent_kernel_version_id = None
    self._settings = None
    self._source = None
    self._external_source_data = None
    self._source_token = None
    self._github_spec = None
    self._update_mask = None
    self._colab_spec = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def sequence(self) -> int:
    return self._sequence

  @sequence.setter
  def sequence(self, sequence: int):
    if sequence is None:
      del self.sequence
      return
    if not isinstance(sequence, int):
      raise TypeError('sequence must be of type int')
    self._sequence = sequence

  @property
  def parent_kernel_version_id(self) -> int:
    return self._parent_kernel_version_id or 0

  @parent_kernel_version_id.setter
  def parent_kernel_version_id(self, parent_kernel_version_id: Optional[int]):
    if parent_kernel_version_id is None:
      del self.parent_kernel_version_id
      return
    if not isinstance(parent_kernel_version_id, int):
      raise TypeError('parent_kernel_version_id must be of type int')
    self._parent_kernel_version_id = parent_kernel_version_id

  @property
  def settings(self) -> Optional['KernelBlobSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['KernelBlobSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, KernelBlobSettings):
      raise TypeError('settings must be of type KernelBlobSettings')
    self._settings = settings

  @property
  def source(self) -> str:
    return self._source or ""

  @source.setter
  def source(self, source: Optional[str]):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source

  @property
  def source_token(self) -> str:
    r"""
    Optional: Read the source in from a GCS uploaded blob instead of passing
    directly. If set, ignores the passed source.
    """
    return self._source_token or ""

  @source_token.setter
  def source_token(self, source_token: Optional[str]):
    if source_token is None:
      del self.source_token
      return
    if not isinstance(source_token, str):
      raise TypeError('source_token must be of type str')
    self._source_token = source_token

  @property
  def external_source_data(self) -> Optional['ExternalSourceData']:
    return self._external_source_data

  @external_source_data.setter
  def external_source_data(self, external_source_data: Optional['ExternalSourceData']):
    if external_source_data is None:
      del self.external_source_data
      return
    if not isinstance(external_source_data, ExternalSourceData):
      raise TypeError('external_source_data must be of type ExternalSourceData')
    self._external_source_data = external_source_data

  @property
  def github_spec(self) -> Optional['GithubSpec']:
    return self._github_spec or None

  @github_spec.setter
  def github_spec(self, github_spec: Optional[Optional['GithubSpec']]):
    if github_spec is None:
      del self.github_spec
      return
    if not isinstance(github_spec, GithubSpec):
      raise TypeError('github_spec must be of type GithubSpec')
    self._github_spec = github_spec

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask

  @property
  def colab_spec(self) -> Optional['ColabSpec']:
    return self._colab_spec or None

  @colab_spec.setter
  def colab_spec(self, colab_spec: Optional[Optional['ColabSpec']]):
    if colab_spec is None:
      del self.colab_spec
      return
    if not isinstance(colab_spec, ColabSpec):
      raise TypeError('colab_spec must be of type ColabSpec')
    self._colab_spec = colab_spec


class UpdateKernelDraftResponse(KaggleObject):
  r"""
  Attributes:
    sequence (int)
    kernel_version_id (int)
    new_settings (KernelBlobSettings)
  """

  def __init__(self):
    self._sequence = 0
    self._kernel_version_id = 0
    self._new_settings = None
    self._freeze()

  @property
  def sequence(self) -> int:
    return self._sequence

  @sequence.setter
  def sequence(self, sequence: int):
    if sequence is None:
      del self.sequence
      return
    if not isinstance(sequence, int):
      raise TypeError('sequence must be of type int')
    self._sequence = sequence

  @property
  def kernel_version_id(self) -> int:
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def new_settings(self) -> Optional['KernelBlobSettings']:
    return self._new_settings or None

  @new_settings.setter
  def new_settings(self, new_settings: Optional[Optional['KernelBlobSettings']]):
    if new_settings is None:
      del self.new_settings
      return
    if not isinstance(new_settings, KernelBlobSettings):
      raise TypeError('new_settings must be of type KernelBlobSettings')
    self._new_settings = new_settings


class UpdateKernelOutputToDatasetRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    enabled (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._enabled = False
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def enabled(self) -> bool:
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled


class UpdateKernelOutputToModelRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    enabled (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._enabled = False
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def enabled(self) -> bool:
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled


class UpdateKernelPersistenceRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    persistence (PersistenceMode)
  """

  def __init__(self):
    self._kernel_id = 0
    self._persistence = PersistenceMode.PERSISTENCE_MODE_UNSPECIFIED
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def persistence(self) -> 'PersistenceMode':
    return self._persistence

  @persistence.setter
  def persistence(self, persistence: 'PersistenceMode'):
    if persistence is None:
      del self.persistence
      return
    if not isinstance(persistence, PersistenceMode):
      raise TypeError('persistence must be of type PersistenceMode')
    self._persistence = persistence


class UpdateKernelPersistenceResponse(KaggleObject):
  r"""
  """

  pass

class UpdateKernelPrivacyRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    disable_comments (bool)
    is_private (bool)
  """

  def __init__(self):
    self._kernel_id = 0
    self._disable_comments = None
    self._is_private = False
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def disable_comments(self) -> bool:
    return self._disable_comments or False

  @disable_comments.setter
  def disable_comments(self, disable_comments: Optional[bool]):
    if disable_comments is None:
      del self.disable_comments
      return
    if not isinstance(disable_comments, bool):
      raise TypeError('disable_comments must be of type bool')
    self._disable_comments = disable_comments

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private


class UpdateKernelPrivacyResponse(KaggleObject):
  r"""
  Attributes:
    can_toggle_visibility (bool)
  """

  def __init__(self):
    self._can_toggle_visibility = False
    self._freeze()

  @property
  def can_toggle_visibility(self) -> bool:
    return self._can_toggle_visibility

  @can_toggle_visibility.setter
  def can_toggle_visibility(self, can_toggle_visibility: bool):
    if can_toggle_visibility is None:
      del self.can_toggle_visibility
      return
    if not isinstance(can_toggle_visibility, bool):
      raise TypeError('can_toggle_visibility must be of type bool')
    self._can_toggle_visibility = can_toggle_visibility


class UpdateKernelSessionKeepaliveRequest(KaggleObject):
  r"""
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


class UpdateKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    is_internet_enabled (bool)
    data_sources (DataSourceReference)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._is_internet_enabled = False
    self._data_sources = []
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

  @property
  def is_internet_enabled(self) -> bool:
    return self._is_internet_enabled

  @is_internet_enabled.setter
  def is_internet_enabled(self, is_internet_enabled: bool):
    if is_internet_enabled is None:
      del self.is_internet_enabled
      return
    if not isinstance(is_internet_enabled, bool):
      raise TypeError('is_internet_enabled must be of type bool')
    self._is_internet_enabled = is_internet_enabled

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources


class UpdateKernelSessionResponse(KaggleObject):
  r"""
  Attributes:
    restart_required (bool)
    data_sources (DataSourceReference)
  """

  def __init__(self):
    self._restart_required = False
    self._data_sources = []
    self._freeze()

  @property
  def restart_required(self) -> bool:
    return self._restart_required

  @restart_required.setter
  def restart_required(self, restart_required: bool):
    if restart_required is None:
      del self.restart_required
      return
    if not isinstance(restart_required, bool):
      raise TypeError('restart_required must be of type bool')
    self._restart_required = restart_required

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources


class UpdateKernelsPrivacyRequest(KaggleObject):
  r"""
  Attributes:
    kernel_ids (int)
    is_public (bool)
      Note: this is is_public whereas UpdateKernelPrivacyRequest uses is_private.
      This is because the APIs have different defaults by design: this handler to
      make things private and the other to make them public.
  """

  def __init__(self):
    self._kernel_ids = []
    self._is_public = None
    self._freeze()

  @property
  def kernel_ids(self) -> Optional[List[int]]:
    return self._kernel_ids

  @kernel_ids.setter
  def kernel_ids(self, kernel_ids: Optional[List[int]]):
    if kernel_ids is None:
      del self.kernel_ids
      return
    if not isinstance(kernel_ids, list):
      raise TypeError('kernel_ids must be of type list')
    if not all([isinstance(t, int) for t in kernel_ids]):
      raise TypeError('kernel_ids must contain only items of type int')
    self._kernel_ids = kernel_ids

  @property
  def is_public(self) -> bool:
    r"""
    Note: this is is_public whereas UpdateKernelPrivacyRequest uses is_private.
    This is because the APIs have different defaults by design: this handler to
    make things private and the other to make them public.
    """
    return self._is_public or False

  @is_public.setter
  def is_public(self, is_public: Optional[bool]):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public


class UpdateKernelTitleRequest(KaggleObject):
  r"""
  Command handler request to update a Kernel title. Returns an error if title
  change is not valid.

  Attributes:
    new_title (str)
    script_version_id (int)
    from_kernel_import_worker (bool)
  """

  def __init__(self):
    self._new_title = None
    self._script_version_id = 0
    self._from_kernel_import_worker = None
    self._freeze()

  @property
  def new_title(self) -> str:
    return self._new_title or ""

  @new_title.setter
  def new_title(self, new_title: Optional[str]):
    if new_title is None:
      del self.new_title
      return
    if not isinstance(new_title, str):
      raise TypeError('new_title must be of type str')
    self._new_title = new_title

  @property
  def script_version_id(self) -> int:
    return self._script_version_id

  @script_version_id.setter
  def script_version_id(self, script_version_id: int):
    if script_version_id is None:
      del self.script_version_id
      return
    if not isinstance(script_version_id, int):
      raise TypeError('script_version_id must be of type int')
    self._script_version_id = script_version_id

  @property
  def from_kernel_import_worker(self) -> bool:
    return self._from_kernel_import_worker or False

  @from_kernel_import_worker.setter
  def from_kernel_import_worker(self, from_kernel_import_worker: Optional[bool]):
    if from_kernel_import_worker is None:
      del self.from_kernel_import_worker
      return
    if not isinstance(from_kernel_import_worker, bool):
      raise TypeError('from_kernel_import_worker must be of type bool')
    self._from_kernel_import_worker = from_kernel_import_worker


class UpdateKernelTitleResponse(KaggleObject):
  r"""
  Attributes:
    error_message (str)
    username (str)
    slug (str)
    new_url (str)
    new_title (str)
  """

  def __init__(self):
    self._error_message = None
    self._username = None
    self._slug = None
    self._new_url = None
    self._new_title = None
    self._freeze()

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def username(self) -> str:
    return self._username or ""

  @username.setter
  def username(self, username: Optional[str]):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def new_url(self) -> str:
    return self._new_url or ""

  @new_url.setter
  def new_url(self, new_url: Optional[str]):
    if new_url is None:
      del self.new_url
      return
    if not isinstance(new_url, str):
      raise TypeError('new_url must be of type str')
    self._new_url = new_url

  @property
  def new_title(self) -> str:
    return self._new_title or ""

  @new_title.setter
  def new_title(self, new_title: Optional[str]):
    if new_title is None:
      del self.new_title
      return
    if not isinstance(new_title, str):
      raise TypeError('new_title must be of type str')
    self._new_title = new_title


class UpdateKernelVersionNameRequest(KaggleObject):
  r"""
  Attributes:
    version_id (int)
    new_name (str)
  """

  def __init__(self):
    self._version_id = 0
    self._new_name = None
    self._freeze()

  @property
  def version_id(self) -> int:
    return self._version_id

  @version_id.setter
  def version_id(self, version_id: int):
    if version_id is None:
      del self.version_id
      return
    if not isinstance(version_id, int):
      raise TypeError('version_id must be of type int')
    self._version_id = version_id

  @property
  def new_name(self) -> str:
    return self._new_name or ""

  @new_name.setter
  def new_name(self, new_name: Optional[str]):
    if new_name is None:
      del self.new_name
      return
    if not isinstance(new_name, str):
      raise TypeError('new_name must be of type str')
    self._new_name = new_name


class UpdateKernelViewCountRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class UpdatePinnedKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    session_id (int)
    pinning_type (KernelVersionPinningType)
  """

  def __init__(self):
    self._session_id = 0
    self._pinning_type = KernelVersionPinningType.UNPINNED
    self._freeze()

  @property
  def session_id(self) -> int:
    return self._session_id

  @session_id.setter
  def session_id(self, session_id: int):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id

  @property
  def pinning_type(self) -> 'KernelVersionPinningType':
    return self._pinning_type

  @pinning_type.setter
  def pinning_type(self, pinning_type: 'KernelVersionPinningType'):
    if pinning_type is None:
      del self.pinning_type
      return
    if not isinstance(pinning_type, KernelVersionPinningType):
      raise TypeError('pinning_type must be of type KernelVersionPinningType')
    self._pinning_type = pinning_type


class UpdateResourceReferenceRequest(KaggleObject):
  r"""
  Attributes:
    resource_reference (ResourceReference)
      The group's `id` field is used to identify the group to update.
    update_mask (FieldMask)
  """

  def __init__(self):
    self._resource_reference = None
    self._update_mask = None
    self._freeze()

  @property
  def resource_reference(self) -> Optional['ResourceReference']:
    """The group's `id` field is used to identify the group to update."""
    return self._resource_reference

  @resource_reference.setter
  def resource_reference(self, resource_reference: Optional['ResourceReference']):
    if resource_reference is None:
      del self.resource_reference
      return
    if not isinstance(resource_reference, ResourceReference):
      raise TypeError('resource_reference must be of type ResourceReference')
    self._resource_reference = resource_reference

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateUserKernelFirestoreAuthRequest(KaggleObject):
  r"""
  Attributes:
    kernel_run_id (int)
    firebase_id_token (str)
  """

  def __init__(self):
    self._kernel_run_id = 0
    self._firebase_id_token = None
    self._freeze()

  @property
  def kernel_run_id(self) -> int:
    return self._kernel_run_id

  @kernel_run_id.setter
  def kernel_run_id(self, kernel_run_id: int):
    if kernel_run_id is None:
      del self.kernel_run_id
      return
    if not isinstance(kernel_run_id, int):
      raise TypeError('kernel_run_id must be of type int')
    self._kernel_run_id = kernel_run_id

  @property
  def firebase_id_token(self) -> str:
    return self._firebase_id_token or ""

  @firebase_id_token.setter
  def firebase_id_token(self, firebase_id_token: Optional[str]):
    if firebase_id_token is None:
      del self.firebase_id_token
      return
    if not isinstance(firebase_id_token, str):
      raise TypeError('firebase_id_token must be of type str')
    self._firebase_id_token = firebase_id_token


class UpdateUserKernelFirestoreAuthResponse(KaggleObject):
  r"""
  Attributes:
    session_id (str)
  """

  def __init__(self):
    self._session_id = None
    self._freeze()

  @property
  def session_id(self) -> str:
    return self._session_id or ""

  @session_id.setter
  def session_id(self, session_id: Optional[str]):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, str):
      raise TypeError('session_id must be of type str')
    self._session_id = session_id


class UploadKernelSessionOutputRequest(KaggleObject):
  r"""
  Attributes:
    interactive_session_id (int)
    batch_session_id (int)
  """

  def __init__(self):
    self._interactive_session_id = 0
    self._batch_session_id = 0
    self._freeze()

  @property
  def interactive_session_id(self) -> int:
    return self._interactive_session_id

  @interactive_session_id.setter
  def interactive_session_id(self, interactive_session_id: int):
    if interactive_session_id is None:
      del self.interactive_session_id
      return
    if not isinstance(interactive_session_id, int):
      raise TypeError('interactive_session_id must be of type int')
    self._interactive_session_id = interactive_session_id

  @property
  def batch_session_id(self) -> int:
    return self._batch_session_id

  @batch_session_id.setter
  def batch_session_id(self, batch_session_id: int):
    if batch_session_id is None:
      del self.batch_session_id
      return
    if not isinstance(batch_session_id, int):
      raise TypeError('batch_session_id must be of type int')
    self._batch_session_id = batch_session_id


AcceleratorQuotaStatistics._fields = [
  FieldMetadata("hasEverRun", "has_ever_run", "_has_ever_run", bool, False, PredefinedSerializer()),
  FieldMetadata("minimumTimeAllowed", "minimum_time_allowed", "_minimum_time_allowed", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("timeReserved", "time_reserved", "_time_reserved", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("timeUsed", "time_used", "_time_used", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("totalTimeAllowed", "total_time_allowed", "_total_time_allowed", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("isPayToScaleEnabled", "is_pay_to_scale_enabled", "_is_pay_to_scale_enabled", bool, False, PredefinedSerializer()),
]

AcceptKernelCompetitionRulesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

AddKernelCategoryRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("categoryId", "category_id", "_category_id", int, 0, PredefinedSerializer()),
]

AgentEntry._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
]

CancelKernelSessionRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("suppressActiveEvents", "suppress_active_events", "_suppress_active_events", bool, None, PredefinedSerializer(), optional=True),
]

CheckNewerColabVersionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

CheckNewerColabVersionResponse._fields = [
  FieldMetadata("hasNewerVersion", "has_newer_version", "_has_newer_version", bool, False, PredefinedSerializer()),
  FieldMetadata("lastModifiedTime", "last_modified_time", "_last_modified_time", datetime, None, DateTimeSerializer(), optional=True),
]

CheckNewerGithubVersionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

CheckNewerGithubVersionResponse._fields = [
  FieldMetadata("hasNewerVersion", "has_newer_version", "_has_newer_version", bool, False, PredefinedSerializer()),
]

ClearPinnedKernelSessionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

ColabSpec._fields = [
  FieldMetadata("driveId", "drive_id", "_drive_id", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("lastPullTime", "last_pull_time", "_last_pull_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastIgnoreNudgeTime", "last_ignore_nudge_time", "_last_ignore_nudge_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("defaultSaveVersionType", "default_save_version_type", "_default_save_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
]

CollaboratorItem._fields = [
  FieldMetadata("authorUserName", "author_user_name", "_author_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("authorDisplayName", "author_display_name", "_author_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("score", "score", "_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("authorTier", "author_tier", "_author_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
  FieldMetadata("databaseId", "database_id", "_database_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

CommitAndRunRequest._fields = [
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("forkParentScriptVersionId", "fork_parent_script_version_id", "_fork_parent_script_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLanguageTemplate", "is_language_template", "_is_language_template", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newText", "new_text", "_new_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newTitle", "new_title", "_new_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scriptId", "script_id", "_script_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptLanguageName", "script_language_name", "_script_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageVersionId", "docker_image_version_id", "_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("editorType", "editor_type", "_editor_type", EditorType, None, EnumSerializer(), optional=True),
  FieldMetadata("dockerImageTag", "docker_image_tag", "_docker_image_tag", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("workerPoolName", "worker_pool_name", "_worker_pool_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sequence", "sequence", "_sequence", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("compute", "compute", "_compute", ComputeState, None, KaggleObjectSerializer()),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionName", "version_name", "_version_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("submissionRequestedDetails", "submission_requested_details", "_submission_requested_details", SubmissionRequestedDetails, None, KaggleObjectSerializer()),
  FieldMetadata("executedByScheduleId", "executed_by_schedule_id", "_executed_by_schedule_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("githubSaveRequest", "github_save_request", "_github_save_request", GitHubSaveRequest, None, KaggleObjectSerializer()),
  FieldMetadata("isImport", "is_import", "_is_import", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalSourceData", "external_source_data", "_external_source_data", ExternalSourceData, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("githubSpec", "github_spec", "_github_spec", GithubSpec, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("colabSpec", "colab_spec", "_colab_spec", ColabSpec, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("fromKernelImportWorker", "from_kernel_import_worker", "_from_kernel_import_worker", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("priority", "priority", "_priority", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isOneTimeAccelerator", "is_one_time_accelerator", "_is_one_time_accelerator", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, None, PredefinedSerializer(), optional=True),
]

CommitAndRunResponse._fields = [
  FieldMetadata("message", "message", "_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submitRedirectUrl", "submit_redirect_url", "_submit_redirect_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sequence", "sequence", "_sequence", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentKernelVersionId", "parent_kernel_version_id", "_parent_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("diff", "diff", "_diff", KernelDiff, None, KaggleObjectSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelRunId", "kernel_run_id", "_kernel_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("status", "status", "_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("blobUploadUrl", "blob_upload_url", "_blob_upload_url", str, None, PredefinedSerializer(), optional=True),
]

CompleteQuickSessionRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

CompleteQuickSessionResponse._fields = [
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

ComputeConstraintState._fields = [
  FieldMetadata("sessionTimeoutSeconds", "session_timeout_seconds", "_session_timeout_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxCpuCores", "max_cpu_cores", "_max_cpu_cores", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxStorageBytes", "max_storage_bytes", "_max_storage_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxMemoryBytes", "max_memory_bytes", "_max_memory_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disallowInternet", "disallow_internet", "_disallow_internet", bool, None, PredefinedSerializer(), optional=True),
]

ComputeInternetState._fields = [
  FieldMetadata("isEnabled", "is_enabled", "_is_enabled", bool, False, PredefinedSerializer()),
]

ComputeKernelDiffRequest._fields = [
  FieldMetadata("leftSessionId", "left_session_id", "_left_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rightSessionId", "right_session_id", "_right_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("includeContents", "include_contents", "_include_contents", bool, False, PredefinedSerializer()),
]

ComputeKernelDiffResponse._fields = [
  FieldMetadata("diff", "diff", "_diff", KernelDiff, None, KaggleObjectSerializer()),
  FieldMetadata("leftContent", "left_content", "_left_content", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rightContent", "right_content", "_right_content", str, None, PredefinedSerializer(), optional=True),
]

ComputeState._fields = [
  FieldMetadata("accelerator", "accelerator", "_accelerator", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("internet", "internet", "_internet", ComputeInternetState, None, KaggleObjectSerializer()),
  FieldMetadata("constraints", "constraints", "_constraints", ComputeConstraintState, None, KaggleObjectSerializer()),
  FieldMetadata("intranet", "intranet", "_intranet", bool, None, PredefinedSerializer(), optional=True),
]

CreateKernelParameters._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("languageId", "language_id", "_language_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dockerImageVersionId", "docker_image_version_id", "_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("compute", "compute", "_compute", ComputeState, None, KaggleObjectSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

CreateKernelSessionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dockerImageTag", "docker_image_tag", "_docker_image_tag", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("workerPoolName", "worker_pool_name", "_worker_pool_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("immediatelyCancelSession", "immediately_cancel_session", "_immediately_cancel_session", bool, False, PredefinedSerializer()),
  FieldMetadata("executedByScheduleId", "executed_by_schedule_id", "_executed_by_schedule_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("diff", "diff", "_diff", KernelDiff, None, KaggleObjectSerializer()),
  FieldMetadata("forkParentDiff", "fork_parent_diff", "_fork_parent_diff", KernelDiff, None, KaggleObjectSerializer()),
  FieldMetadata("submissionRequestedDetails", "submission_requested_details", "_submission_requested_details", SubmissionRequestedDetails, None, KaggleObjectSerializer()),
  FieldMetadata("useGivenDataSourceVersionIds", "use_given_data_source_version_ids", "_use_given_data_source_version_ids", bool, False, PredefinedSerializer()),
  FieldMetadata("parameters", "parameters", "_parameters", CreateKernelParameters, None, KaggleObjectSerializer()),
  FieldMetadata("githubSaveRequest", "github_save_request", "_github_save_request", GitHubSaveRequest, None, KaggleObjectSerializer()),
  FieldMetadata("environmentVariables", "environment_variables", "_environment_variables", EnvironmentVariable, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("creationSource", "creation_source", "_creation_source", CreationSource, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("staggerStart", "stagger_start", "_stagger_start", timedelta, None, TimeDeltaSerializer()),
  FieldMetadata("aliases", "aliases", "_aliases", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("extraMounts", "extra_mounts", "_extra_mounts", ExtraMountSettings, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("priority", "priority", "_priority", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("allowContainerReset", "allow_container_reset", "_allow_container_reset", bool, None, PredefinedSerializer(), optional=True),
]

CreateKernelSessionResponse._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("showParentForkSecretWarning", "show_parent_fork_secret_warning", "_show_parent_fork_secret_warning", bool, False, PredefinedSerializer()),
  FieldMetadata("acceleratorChanged", "accelerator_changed", "_accelerator_changed", AcceleratorType, None, EnumSerializer(), optional=True),
]

CreateKernelUpvoteRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

CreateKernelUpvoteResponse._fields = [
  FieldMetadata("voteId", "vote_id", "_vote_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isSelfVote", "is_self_vote", "_is_self_vote", bool, False, PredefinedSerializer()),
]

CreateKernelWithSettingsRequest.ImportSource._fields = [
  FieldMetadata("importType", "import_type", "_import_type", ImportType, None, EnumSerializer(), optional=True),
  FieldMetadata("sourceData", "source_data", "_source_data", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, None, EnumSerializer(), optional=True),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("acceleratorSelection", "accelerator_selection", "_accelerator_selection", AcceleratorSelection, None, EnumSerializer(), optional=True),
]

CreateKernelWithSettingsRequest._fields = [
  FieldMetadata("kernelLanguageId", "kernel_language_id", "_kernel_language_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceType", "source_type", "_source_type", EditorType, EditorType.EDITOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("accelerator", "accelerator", "_accelerator", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableInternet", "enable_internet", "_enable_internet", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forkParentScriptVersionId", "fork_parent_script_version_id", "_fork_parent_script_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelOutputVersionId", "kernel_output_version_id", "_kernel_output_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImagePinningType", "docker_image_pinning_type", "_docker_image_pinning_type", DockerImagePinningType, None, EnumSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("importSource", "import_source", "_import_source", CreateKernelWithSettingsRequest.ImportSource, None, KaggleObjectSerializer(), optional=True),
]

CreateKernelWithSettingsResponse._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentUrlSlug", "current_url_slug", "_current_url_slug", str, None, PredefinedSerializer(), optional=True),
]

CreateUserResourceReferenceViewRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DailySubmissionInfo._fields = [
  FieldMetadata("submissionCount", "submission_count", "_submission_count", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionLimit", "submission_limit", "_submission_limit", int, None, PredefinedSerializer(), optional=True),
]

DataSourceVersion._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("number", "number", "_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
]

DefaultSessionSettings._fields = [
  FieldMetadata("saveQuickVersionOutputFiles", "save_quick_version_output_files", "_save_quick_version_output_files", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("batchSessionDefaultAccelerator", "batch_session_default_accelerator", "_batch_session_default_accelerator", AcceleratorType, None, EnumSerializer(), optional=True),
  FieldMetadata("linkToGithub", "link_to_github", "_link_to_github", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("githubSpec", "github_spec", "_github_spec", GithubSpec, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("colabSpec", "colab_spec", "_colab_spec", ColabSpec, None, KaggleObjectSerializer(), optional=True),
]

DeleteKernelRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

DeleteKernelUpvoteRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

DeleteScheduledKernelSessionRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DeleteScheduledKernelSessionResponse._fields = []

DockerImageVersionDetails._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", DockerImageVersionType, DockerImageVersionType.DOCKER_IMAGE_VERSION_TYPE_LATEST, EnumSerializer()),
  FieldMetadata("disabledReason", "disabled_reason", "_disabled_reason", DockerImageVersionDisabledReason, DockerImageVersionDisabledReason.DOCKER_IMAGE_VERSION_DISABLED_REASON_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
]

DockerImageVersionDetailsList._fields = [
  FieldMetadata("images", "images", "_images", DockerImageVersionDetails, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("selectedVersionType", "selected_version_type", "_selected_version_type", DockerImageVersionType, DockerImageVersionType.DOCKER_IMAGE_VERSION_TYPE_LATEST, EnumSerializer()),
  FieldMetadata("selectedVersionId", "selected_version_id", "_selected_version_id", int, None, PredefinedSerializer(), optional=True),
]

EligibleAccelerator._fields = [
  FieldMetadata("variant", "variant", "_variant", ColabVariant, ColabVariant.VARIANT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("models", "models", "_models", str, [], ListSerializer(PredefinedSerializer())),
]

EnvironmentVariable._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

ExportKernelSessionForColabRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("useDraft", "use_draft", "_use_draft", bool, False, PredefinedSerializer()),
  FieldMetadata("colabNotebookSource", "colab_notebook_source", "_colab_notebook_source", ColabNotebookSource, None, EnumSerializer(), optional=True),
]

ExportKernelSessionForColabResponse._fields = [
  FieldMetadata("warnings", "warnings", "_warnings", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("colabUrl", "colab_url", "_colab_url", str, None, PredefinedSerializer(), optional=True),
]

ExternalSourceData._fields = [
  FieldMetadata("sourceDescription", "source_description", "_source_description", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
]

ExtraMountSettings._fields = [
  FieldMetadata("dir", "dir", "_dir", str, "", PredefinedSerializer()),
  FieldMetadata("sharedVolumeName", "shared_volume_name", "_shared_volume_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("propagation", "propagation", "_propagation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resetSignal", "reset_signal", "_reset_signal", bool, False, PredefinedSerializer()),
]

FetchAllColabContentRequest._fields = [
  FieldMetadata("externalSourceUserId", "external_source_user_id", "_external_source_user_id", str, "", PredefinedSerializer()),
  FieldMetadata("externalSourceAvatarUrl", "external_source_avatar_url", "_external_source_avatar_url", str, "", PredefinedSerializer()),
]

FetchColabContentRequest._fields = [
  FieldMetadata("driveId", "drive_id", "_drive_id", str, "", PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

FetchDriveContentResponse._fields = [
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, "", PredefinedSerializer()),
  FieldMetadata("fileExtension", "file_extension", "_file_extension", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
]

FetchExternalKernelContentRequest._fields = [
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, None, PredefinedSerializer(), optional=True),
]

FetchGitHubContentRequest._fields = [
  FieldMetadata("owner", "owner", "_owner", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("repo", "repo", "_repo", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("path", "path", "_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ref", "ref", "_ref", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
]

FetchGitHubContentResponse._fields = [
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("githubSpec", "github_spec", "_github_spec", GithubSpec, None, KaggleObjectSerializer()),
]

GetAcceleratorQuotaStatisticsRequest._fields = []

GetAcceleratorQuotaStatisticsResponse._fields = [
  FieldMetadata("quotaRefreshTime", "quota_refresh_time", "_quota_refresh_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("kernelsMaxSizeInMb", "kernels_max_size_in_mb", "_kernels_max_size_in_mb", int, 0, PredefinedSerializer()),
  FieldMetadata("tpuQuota", "tpu_quota", "_tpu_quota", AcceleratorQuotaStatistics, None, KaggleObjectSerializer()),
  FieldMetadata("gpuQuota", "gpu_quota", "_gpu_quota", AcceleratorQuotaStatistics, None, KaggleObjectSerializer()),
]

GetColabUserInfoRequest._fields = []

GetColabUserInfoResponse._fields = [
  FieldMetadata("subscriptionTier", "subscription_tier", "_subscription_tier", ColabSubscriptionTier, ColabSubscriptionTier.SUBSCRIPTION_TIER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("paidComputeUnitsBalance", "paid_compute_units_balance", "_paid_compute_units_balance", float, 0.0, PredefinedSerializer()),
  FieldMetadata("eligibleAccelerators", "eligible_accelerators", "_eligible_accelerators", EligibleAccelerator, [], ListSerializer(KaggleObjectSerializer())),
]

GetCompetitionsPaneInfoRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetCompetitionsPaneInfoResponse._fields = [
  FieldMetadata("bestKernelSessionScore", "best_kernel_session_score", "_best_kernel_session_score", KernelSessionScore, None, KaggleObjectSerializer()),
  FieldMetadata("latestKernelSessionScore", "latest_kernel_session_score", "_latest_kernel_session_score", KernelSessionScore, None, KaggleObjectSerializer()),
  FieldMetadata("dailySubmissionInfo", "daily_submission_info", "_daily_submission_info", DailySubmissionInfo, None, KaggleObjectSerializer()),
]

GetDefaultSessionSettingsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetDeletedKernelRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetDeletedKernelResponse._fields = [
  FieldMetadata("defaultDatasourceImageUrl", "default_datasource_image_url", "_default_datasource_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultUserImageUrl", "default_user_image_url", "_default_user_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("deletedKernelUrl", "deleted_kernel_url", "_deleted_kernel_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("commentCount", "comment_count", "_comment_count", int, 0, PredefinedSerializer()),
  FieldMetadata("userCanDownvoteComments", "user_can_downvote_comments", "_user_can_downvote_comments", bool, False, PredefinedSerializer()),
]

GetFirebaseAuthTokenRequest._fields = []

GetFirebaseAuthTokenResponse._fields = [
  FieldMetadata("authToken", "auth_token", "_auth_token", str, "", PredefinedSerializer()),
]

GetFirebaseConfigRequest._fields = []

GetFirebaseConfigResponse._fields = [
  FieldMetadata("apiKey", "api_key", "_api_key", str, "", PredefinedSerializer()),
  FieldMetadata("authDomain", "auth_domain", "_auth_domain", str, "", PredefinedSerializer()),
  FieldMetadata("databaseUrl", "database_url", "_database_url", str, "", PredefinedSerializer()),
  FieldMetadata("projectId", "project_id", "_project_id", str, "", PredefinedSerializer()),
  FieldMetadata("storageBucket", "storage_bucket", "_storage_bucket", str, "", PredefinedSerializer()),
  FieldMetadata("messagingSenderId", "messaging_sender_id", "_messaging_sender_id", str, "", PredefinedSerializer()),
  FieldMetadata("appId", "app_id", "_app_id", str, "", PredefinedSerializer()),
  FieldMetadata("proxyDomain", "proxy_domain", "_proxy_domain", str, "", PredefinedSerializer()),
]

GetKernelCategoryIdsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetKernelEmbedResponse._fields = [
  FieldMetadata("ipynbContent", "ipynb_content", "_ipynb_content", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("renderedOutputUrl", "rendered_output_url", "_rendered_output_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("viewerUrl", "viewer_url", "_viewer_url", str, "", PredefinedSerializer()),
]

GetKernelGitHubSettingsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetKernelGitHubSettingsResponse._fields = [
  FieldMetadata("githubLogin", "github_login", "_github_login", str, "", PredefinedSerializer()),
  FieldMetadata("repositories", "repositories", "_repositories", GithubRepositoryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("branches", "branches", "_branches", GithubBranchInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("lastSettings", "last_settings", "_last_settings", GitHubSaveRequest, None, KaggleObjectSerializer()),
]

GetKernelIdByUrlRequest._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

GetKernelIdByUrlResponse._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetKernelLandingPageRequest._fields = []

GetKernelLandingPageResponse._fields = [
  FieldMetadata("shelves", "shelves", "_shelves", KernelShelf, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalPublicKernels", "total_public_kernels", "_total_public_kernels", int, 0, PredefinedSerializer()),
]

GetKernelRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetKernelSessionDataSourcesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("includeOutputFiles", "include_output_files", "_include_output_files", bool, False, PredefinedSerializer()),
  FieldMetadata("hierarchicalOutputFiles", "hierarchical_output_files", "_hierarchical_output_files", bool, False, PredefinedSerializer()),
]

GetKernelSessionDataSourcesResponse._fields = [
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSource, [], ListSerializer(KaggleObjectSerializer())),
]

GetKernelSessionLogRequest._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, 0, PredefinedSerializer()),
]

GetKernelSessionModelSourcesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

GetKernelSessionModelSourcesResponse._fields = [
  FieldMetadata("modelSources", "model_sources", "_model_sources", ModelSource, [], ListSerializer(KaggleObjectSerializer())),
]

GetKernelSessionResourceReferencesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("resourceReferenceTypeFilter", "resource_reference_type_filter", "_resource_reference_type_filter", ResourceReferenceType, None, EnumSerializer(), optional=True),
]

GetKernelSessionResourceReferencesResponse._fields = [
  FieldMetadata("resourceReferences", "resource_references", "_resource_references", ResourceReference, [], ListSerializer(KaggleObjectSerializer())),
]

GetKernelSessionSourceRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("includeOutputIfAvailable", "include_output_if_available", "_include_output_if_available", bool, False, PredefinedSerializer()),
]

GetKernelStatusRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("existingStatus", "existing_status", "_existing_status", KernelWorkerStatus, None, EnumSerializer(), optional=True),
]

GetKernelStatusResponse._fields = [
  FieldMetadata("status", "status", "_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
]

GetKernelVersionRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("getDataSources", "get_data_sources", "_get_data_sources", bool, None, PredefinedSerializer(), optional=True),
]

GetKernelVersionResponse._fields = [
  FieldMetadata("kernelVersionAndRun", "kernel_version_and_run", "_kernel_version_and_run", KernelVersionAndRun, None, KaggleObjectSerializer()),
]

GetOrCreateKernelSessionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("useNewScope", "use_new_scope", "_use_new_scope", bool, None, PredefinedSerializer(), optional=True),
]

GetOrCreateKernelSessionResponse._fields = [
  FieldMetadata("draft", "draft", "_draft", KernelDraft, None, KaggleObjectSerializer()),
  FieldMetadata("sessionId", "session_id", "_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sessionTimeoutSeconds", "session_timeout_seconds", "_session_timeout_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("sessionCreationFailureMessage", "session_creation_failure_message", "_session_creation_failure_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasMoreRecentCollaboratorVersion", "has_more_recent_collaborator_version", "_has_more_recent_collaborator_version", bool, False, PredefinedSerializer()),
  FieldMetadata("sessionStatus", "session_status", "_session_status", KernelWorkerStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("enableLsp", "enable_lsp", "_enable_lsp", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verificationRedirectUrl", "verification_redirect_url", "_verification_redirect_url", str, None, PredefinedSerializer(), optional=True),
]

GetPackageRequirementsUpdateUrlRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
]

GetPackageRequirementsUpdateUrlResponse._fields = [
  FieldMetadata("signedUrl", "signed_url", "_signed_url", str, "", PredefinedSerializer()),
]

GetPackageRequirementsViewUrlRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetPackageRequirementsViewUrlResponse._fields = [
  FieldMetadata("signedUrl", "signed_url", "_signed_url", str, None, PredefinedSerializer(), optional=True),
]

GetResourceReferenceByIdRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetResourceReferenceRequest._fields = [
  FieldMetadata("identifier", "identifier", "_identifier", ResourceReferenceIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetScheduledKernelSessionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetScheduledKernelSessionResponse._fields = [
  FieldMetadata("session", "session", "_session", ScheduledKernelSession, None, KaggleObjectSerializer()),
]

GetUserKernelAchievementsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
]

GetUserKernelAchievementsResponse._fields = [
  FieldMetadata("totalUpvotes", "total_upvotes", "_total_upvotes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalKernels", "total_kernels", "_total_kernels", int, 0, PredefinedSerializer()),
  FieldMetadata("totalForks", "total_forks", "_total_forks", int, 0, PredefinedSerializer()),
  FieldMetadata("weeklyForks", "weekly_forks", "_weekly_forks", int, 0, PredefinedSerializer()),
]

GithubBranchInfo._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

GithubFileInfo._fields = [
  FieldMetadata("owner", "owner", "_owner", str, "", PredefinedSerializer()),
  FieldMetadata("repo", "repo", "_repo", str, "", PredefinedSerializer()),
  FieldMetadata("path", "path", "_path", str, "", PredefinedSerializer()),
  FieldMetadata("ref", "ref", "_ref", str, "", PredefinedSerializer()),
  FieldMetadata("rawUrl", "raw_url", "_raw_url", str, "", PredefinedSerializer()),
  FieldMetadata("size", "size", "_size", int, None, PredefinedSerializer(), optional=True),
]

GithubRepositoryInfo._fields = [
  FieldMetadata("owner", "owner", "_owner", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("defaultBranch", "default_branch", "_default_branch", str, "", PredefinedSerializer()),
]

GitHubSaveRequest._fields = [
  FieldMetadata("repositoryOwner", "repository_owner", "_repository_owner", str, "", PredefinedSerializer()),
  FieldMetadata("repositoryName", "repository_name", "_repository_name", str, "", PredefinedSerializer()),
  FieldMetadata("branch", "branch", "_branch", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("commitMessage", "commit_message", "_commit_message", str, "", PredefinedSerializer()),
  FieldMetadata("includeKaggleBadge", "include_kaggle_badge", "_include_kaggle_badge", bool, False, PredefinedSerializer()),
]

GithubSpec.CommitInfo._fields = [
  FieldMetadata("sha", "sha", "_sha", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("time", "time", "_time", datetime, None, DateTimeSerializer(), optional=True),
]

GithubSpec.FileInfo._fields = [
  FieldMetadata("repoOwner", "repo_owner", "_repo_owner", str, "", PredefinedSerializer()),
  FieldMetadata("repoName", "repo_name", "_repo_name", str, "", PredefinedSerializer()),
  FieldMetadata("branch", "branch", "_branch", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
]

GithubSpec._fields = [
  FieldMetadata("fileInfo", "file_info", "_file_info", GithubSpec.FileInfo, None, KaggleObjectSerializer()),
  FieldMetadata("lastPush", "last_push", "_last_push", GithubSpec.CommitInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("lastPull", "last_pull", "_last_pull", GithubSpec.CommitInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("lastIgnoreNudgeTime", "last_ignore_nudge_time", "_last_ignore_nudge_time", datetime, None, DateTimeSerializer(), optional=True),
]

HasAcceptedKernelCompetitionRulesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

HasAcceptedKernelCompetitionRulesResponse._fields = [
  FieldMetadata("competitionsRequiringAcceptance", "competitions_requiring_acceptance", "_competitions_requiring_acceptance", KernelCompetition, [], ListSerializer(KaggleObjectSerializer())),
]

Kernel._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forkParent", "fork_parent", "_fork_parent", KernelForkInfo, None, KaggleObjectSerializer()),
  FieldMetadata("currentRunId", "current_run_id", "_current_run_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mostRecentRunId", "most_recent_run_id", "_most_recent_run_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("commentCount", "comment_count", "_comment_count", int, 0, PredefinedSerializer()),
  FieldMetadata("upvoteCount", "upvote_count", "_upvote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("viewCount", "view_count", "_view_count", int, 0, PredefinedSerializer()),
  FieldMetadata("forkCount", "fork_count", "_fork_count", int, 0, PredefinedSerializer()),
  FieldMetadata("bestPublicScore", "best_public_score", "_best_public_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("updatedTime", "updated_time", "_updated_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("selfLink", "self_link", "_self_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pinnedDockerImageVersionId", "pinned_docker_image_version_id", "_pinned_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImagePinningType", "docker_image_pinning_type", "_docker_image_pinning_type", DockerImagePinningType, DockerImagePinningType.DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("originalDockerImageId", "original_docker_image_id", "_original_docker_image_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLanguageTemplate", "is_language_template", "_is_language_template", bool, False, PredefinedSerializer()),
  FieldMetadata("medal", "medal", "_medal", Medal, Medal.MEDAL_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pinnedSessionId", "pinned_session_id", "_pinned_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableComments", "disable_comments", "_disable_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("hasLinkedSubmission", "has_linked_submission", "_has_linked_submission", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserHasBookmarked", "current_user_has_bookmarked", "_current_user_has_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("dateOutputToDatasetEnabled", "date_output_to_dataset_enabled", "_date_output_to_dataset_enabled", datetime, None, DateTimeSerializer()),
  FieldMetadata("canToggleVisibility", "can_toggle_visibility", "_can_toggle_visibility", bool, False, PredefinedSerializer()),
  FieldMetadata("persistence", "persistence", "_persistence", PersistenceMode, PersistenceMode.PERSISTENCE_MODE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("privateCompetitionId", "private_competition_id", "_private_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateOutputToModelEnabled", "date_output_to_model_enabled", "_date_output_to_model_enabled", datetime, None, DateTimeSerializer()),
]

KernelBlob._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", KernelBlobSettings, None, KaggleObjectSerializer()),
  FieldMetadata("source", "source", "_source", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("settingsSchemaVersion", "settings_schema_version", "_settings_schema_version", int, None, PredefinedSerializer(), optional=True),
]

KernelBlobSettings._fields = [
  FieldMetadata("dockerImageVersionId", "docker_image_version_id", "_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("sourceType", "source_type", "_source_type", EditorType, EditorType.EDITOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("language", "language", "_language", Language, Language.LANGUAGE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("accelerator", "accelerator", "_accelerator", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("isInternetEnabled", "is_internet_enabled", "_is_internet_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("isGpuEnabled", "is_gpu_enabled", "_is_gpu_enabled", bool, False, PredefinedSerializer()),
]

KernelCategoryIdList._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", int, [], ListSerializer(PredefinedSerializer())),
]

KernelCompetition._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("rulesUrl", "rules_url", "_rules_url", str, "", PredefinedSerializer()),
]

KernelDataSourceListItemDto._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceType", "source_type", "_source_type", LegacyDataSourceType, LegacyDataSourceType.LEGACY_DATA_SOURCE_TYPE_DATASET, EnumSerializer()),
  FieldMetadata("sourceId", "source_id", "_source_id", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("siteName", "site_name", "_site_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
]

KernelDiff._fields = [
  FieldMetadata("linesInserted", "lines_inserted", "_lines_inserted", int, 0, PredefinedSerializer()),
  FieldMetadata("linesDeleted", "lines_deleted", "_lines_deleted", int, 0, PredefinedSerializer()),
  FieldMetadata("linesChanged", "lines_changed", "_lines_changed", int, 0, PredefinedSerializer()),
  FieldMetadata("linesUnchanged", "lines_unchanged", "_lines_unchanged", int, 0, PredefinedSerializer()),
  FieldMetadata("newTotalLines", "new_total_lines", "_new_total_lines", int, 0, PredefinedSerializer()),
]

KernelDraft._fields = [
  FieldMetadata("sequence", "sequence", "_sequence", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentKernelVersionId", "parent_kernel_version_id", "_parent_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("blob", "blob", "_blob", KernelBlob, None, KaggleObjectSerializer()),
  FieldMetadata("hasMoreRecentCollaboratorVersion", "has_more_recent_collaborator_version", "_has_more_recent_collaborator_version", bool, False, PredefinedSerializer()),
]

KernelForkInfo._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runId", "run_id", "_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer()),
  FieldMetadata("diff", "diff", "_diff", KernelDiff, None, KaggleObjectSerializer()),
  FieldMetadata("isRedacted", "is_redacted", "_is_redacted", bool, False, PredefinedSerializer()),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("workerStatus", "worker_status", "_worker_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("isolatorResults", "isolator_results", "_isolator_results", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("languageId", "language_id", "_language_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("isFork", "is_fork", "_is_fork", bool, False, PredefinedSerializer()),
]

KernelImport._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("importType", "import_type", "_import_type", ImportType, ImportType.UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sourceData", "source_data", "_source_data", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("externalSourceUserId", "external_source_user_id", "_external_source_user_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalSourceAvatarUrl", "external_source_avatar_url", "_external_source_avatar_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, None, EnumSerializer(), optional=True),
  FieldMetadata("accelerator", "accelerator", "_accelerator", AcceleratorType, None, EnumSerializer(), optional=True),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("acceleratorSelection", "accelerator_selection", "_accelerator_selection", AcceleratorSelection, None, EnumSerializer(), optional=True),
]

KernelRun._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("kernelVersionType", "kernel_version_type", "_kernel_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sourceType", "source_type", "_source_type", EditorType, EditorType.EDITOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("language", "language", "_language", Language, Language.LANGUAGE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("dateEvaluated", "date_evaluated", "_date_evaluated", datetime, None, DateTimeSerializer()),
  FieldMetadata("dateCancelled", "date_cancelled", "_date_cancelled", datetime, None, DateTimeSerializer()),
  FieldMetadata("workerContainerPort", "worker_container_port", "_worker_container_port", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("workerUptimeSeconds", "worker_uptime_seconds", "_worker_uptime_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("workerIpAddress", "worker_ip_address", "_worker_ip_address", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("workerIpAddressExternal", "worker_ip_address_external", "_worker_ip_address_external", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scriptLanguageId", "script_language_id", "_script_language_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptLanguageName", "script_language_name", "_script_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("renderedOutputUrl", "rendered_output_url", "_rendered_output_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("commit", "commit", "_commit", KernelBlob, None, KaggleObjectSerializer()),
  FieldMetadata("resources", "resources", "_resources", KernelSessionResources, None, KaggleObjectSerializer()),
  FieldMetadata("isolatorResults", "isolator_results", "_isolator_results", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("runInfo", "run_info", "_run_info", KernelSessionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("dockerImageVersionId", "docker_image_version_id", "_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("usedCustomDockerImage", "used_custom_docker_image", "_used_custom_docker_image", bool, False, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("useNewKernelsBackend", "use_new_kernels_backend", "_use_new_kernels_backend", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isGpuEnabled", "is_gpu_enabled", "_is_gpu_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("isTpuEnabled", "is_tpu_enabled", "_is_tpu_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("acceleratorType", "accelerator_type", "_accelerator_type", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("isInternetEnabled", "is_internet_enabled", "_is_internet_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("executedByScheduleId", "executed_by_schedule_id", "_executed_by_schedule_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("nextScheduledSessionDate", "next_scheduled_session_date", "_next_scheduled_session_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("isKernelScheduled", "is_kernel_scheduled", "_is_kernel_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("githubUrl", "github_url", "_github_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorUserId", "author_user_id", "_author_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelVersionNumber", "kernel_version_number", "_kernel_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelSessionPackageState", "kernel_session_package_state", "_kernel_session_package_state", KernelSessionPackageState, None, EnumSerializer(), optional=True),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer(), optional=True),
]

KernelSession._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelRunId", "kernel_run_id", "_kernel_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sourceType", "source_type", "_source_type", EditorType, EditorType.EDITOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("languageName", "language_name", "_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("accelerator", "accelerator", "_accelerator", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("isInternetEnabled", "is_internet_enabled", "_is_internet_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionName", "version_name", "_version_name", str, None, PredefinedSerializer(), optional=True),
]

KernelSessionList._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
  FieldMetadata("quotaLimits", "quota_limits", "_quota_limits", KernelSessionQuotaLimits, None, KaggleObjectSerializer()),
  FieldMetadata("sessions", "sessions", "_sessions", KernelSession, [], ListSerializer(KaggleObjectSerializer())),
]

KernelSessionQuotaLimits._fields = [
  FieldMetadata("gpuInteractive", "gpu_interactive", "_gpu_interactive", int, 0, PredefinedSerializer()),
  FieldMetadata("gpuBatch", "gpu_batch", "_gpu_batch", int, 0, PredefinedSerializer()),
  FieldMetadata("cpuInteractive", "cpu_interactive", "_cpu_interactive", int, 0, PredefinedSerializer()),
  FieldMetadata("cpuBatch", "cpu_batch", "_cpu_batch", int, 0, PredefinedSerializer()),
  FieldMetadata("tpuInteractive", "tpu_interactive", "_tpu_interactive", int, 0, PredefinedSerializer()),
  FieldMetadata("tpuBatch", "tpu_batch", "_tpu_batch", int, 0, PredefinedSerializer()),
]

KernelSessionResources._fields = [
  FieldMetadata("storageBytes", "storage_bytes", "_storage_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("memoryBytes", "memory_bytes", "_memory_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("cpuCores", "cpu_cores", "_cpu_cores", int, 0, PredefinedSerializer()),
  FieldMetadata("sessionTimeoutSeconds", "session_timeout_seconds", "_session_timeout_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("idleTimeoutSeconds", "idle_timeout_seconds", "_idle_timeout_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("network", "network", "_network", str, None, PredefinedSerializer(), optional=True),
]

KernelSessionScore._fields = [
  FieldMetadata("scoreFormatted", "score_formatted", "_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelVersionName", "kernel_version_name", "_kernel_version_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelVersionNumber", "kernel_version_number", "_kernel_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelSessionUrl", "kernel_session_url", "_kernel_session_url", str, "", PredefinedSerializer()),
]

KernelShelf._fields = [
  FieldMetadata("kernels", "kernels", "_kernels", KernelListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("label", "label", "_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalKernels", "total_kernels", "_total_kernels", int, 0, PredefinedSerializer()),
  FieldMetadata("moreKernelsRequest", "more_kernels_request", "_more_kernels_request", ListKernelIdsRequest, None, KaggleObjectSerializer()),
]

KernelVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("linesTotal", "lines_total", "_lines_total", int, 0, PredefinedSerializer()),
  FieldMetadata("linesInserted", "lines_inserted", "_lines_inserted", int, 0, PredefinedSerializer()),
  FieldMetadata("linesDeleted", "lines_deleted", "_lines_deleted", int, 0, PredefinedSerializer()),
  FieldMetadata("pinningType", "pinning_type", "_pinning_type", KernelVersionPinningType, KernelVersionPinningType.UNPINNED, EnumSerializer()),
  FieldMetadata("versionName", "version_name", "_version_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
]

KernelVersionAndRun._fields = [
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer()),
  FieldMetadata("version", "version", "_version", KernelVersion, None, KaggleObjectSerializer()),
  FieldMetadata("run", "run", "_run", KernelRun, None, KaggleObjectSerializer()),
  FieldMetadata("blob", "blob", "_blob", KernelBlob, None, KaggleObjectSerializer()),
  FieldMetadata("isForkParent", "is_fork_parent", "_is_fork_parent", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUrlSlug", "current_url_slug", "_current_url_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelAuthorUserName", "kernel_author_user_name", "_kernel_author_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("viewerUrl", "viewer_url", "_viewer_url", str, "", PredefinedSerializer()),
]

KernelVersionList._fields = [
  FieldMetadata("items", "items", "_items", KernelVersionAndRun, [], ListSerializer(KaggleObjectSerializer())),
]

ListColabFilesRequest._fields = [
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("orderBy", "order_by", "_order_by", ListColabSortType, None, EnumSerializer(), optional=True),
  FieldMetadata("orderByAscending", "order_by_ascending", "_order_by_ascending", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("limitToOwnedByMe", "limit_to_owned_by_me", "_limit_to_owned_by_me", bool, False, PredefinedSerializer()),
  FieldMetadata("isTestRequest", "is_test_request", "_is_test_request", bool, None, PredefinedSerializer(), optional=True),
]

ListColabFilesResponse.ColabFileInfo._fields = [
  FieldMetadata("driveId", "drive_id", "_drive_id", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("owners", "owners", "_owners", ListColabFilesResponse.DriveOwner, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("ownedByMe", "owned_by_me", "_owned_by_me", bool, False, PredefinedSerializer()),
  FieldMetadata("thumbnailLink", "thumbnail_link", "_thumbnail_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createdTime", "created_time", "_created_time", str, "", PredefinedSerializer()),
  FieldMetadata("lastActivityTime", "last_activity_time", "_last_activity_time", str, "", PredefinedSerializer()),
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
]

ListColabFilesResponse.DriveOwner._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
]

ListColabFilesResponse._fields = [
  FieldMetadata("files", "files", "_files", ListColabFilesResponse.ColabFileInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ListDockerImagesRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

ListGithubRepositoriesRequest._fields = [
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("perPage", "per_page", "_per_page", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includePrivate", "include_private", "_include_private", bool, False, PredefinedSerializer()),
]

ListGithubRepositoriesResponse._fields = [
  FieldMetadata("repositories", "repositories", "_repositories", GithubRepositoryInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ListGithubRepositoryBranchesRequest._fields = [
  FieldMetadata("owner", "owner", "_owner", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("includePrivate", "include_private", "_include_private", bool, False, PredefinedSerializer()),
]

ListGithubRepositoryBranchesResponse._fields = [
  FieldMetadata("branches", "branches", "_branches", GithubBranchInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ListGithubRepositoryFilesRequest._fields = [
  FieldMetadata("owner", "owner", "_owner", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("branch", "branch", "_branch", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileExtensionFilter", "file_extension_filter", "_file_extension_filter", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("includePrivate", "include_private", "_include_private", bool, False, PredefinedSerializer()),
]

ListGithubRepositoryFilesResponse._fields = [
  FieldMetadata("files", "files", "_files", GithubFileInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ListKernelIdsResponse._fields = [
  FieldMetadata("kernelIds", "kernel_ids", "_kernel_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListKernelSessionOutputFilesHierarchicalRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("relativePath", "relative_path", "_relative_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("offset", "offset", "_offset", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxResults", "max_results", "_max_results", int, 0, PredefinedSerializer()),
]

ListKernelSessionOutputFilesHierarchicalResponse._fields = [
  FieldMetadata("directories", "directories", "_directories", Directory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("files", "files", "_files", File, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListKernelSessionOutputRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filePath", "file_path", "_file_path", str, None, PredefinedSerializer(), optional=True),
]

ListKernelSessionOutputResponse._fields = [
  FieldMetadata("items", "items", "_items", KernelSessionOutputFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListKernelSessionsRequest._fields = []

ListKernelVersionsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sortOption", "sort_option", "_sort_option", ListKernelVersionsRequest.SortOption, ListKernelVersionsRequest.SortOption.SORT_OPTION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ModelSource._fields = [
  FieldMetadata("currentUserUpvoted", "current_user_upvoted", "_current_user_upvoted", bool, False, PredefinedSerializer()),
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceFramework", "model_instance_framework", "_model_instance_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceVersionUrl", "model_instance_version_url", "_model_instance_version_url", str, "", PredefinedSerializer()),
  FieldMetadata("modelInstanceVersionNumber", "model_instance_version_number", "_model_instance_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelOwnerImageUrl", "model_owner_image_url", "_model_owner_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("modelOwnerName", "model_owner_name", "_model_owner_name", str, "", PredefinedSerializer()),
  FieldMetadata("modelSubtitle", "model_subtitle", "_model_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("modelTags", "model_tags", "_model_tags", TagList, None, KaggleObjectSerializer()),
  FieldMetadata("modelTitle", "model_title", "_model_title", str, "", PredefinedSerializer()),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceVariationSlug", "model_instance_variation_slug", "_model_instance_variation_slug", str, "", PredefinedSerializer()),
  FieldMetadata("isOrganizationOwned", "is_organization_owned", "_is_organization_owned", bool, False, PredefinedSerializer()),
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
]

PushToGithubRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("saveRequest", "save_request", "_save_request", GitHubSaveRequest, None, KaggleObjectSerializer()),
  FieldMetadata("source", "source", "_source", str, None, PredefinedSerializer(), optional=True),
]

PushToGithubResponse._fields = [
  FieldMetadata("spec", "spec", "_spec", GithubSpec, None, KaggleObjectSerializer(), optional=True),
]

RemoveKernelCategoryRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("categoryId", "category_id", "_category_id", int, 0, PredefinedSerializer()),
]

RunEpisodeRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
  FieldMetadata("environment", "environment", "_environment", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("episodeType", "episode_type", "_episode_type", EpisodeType, EpisodeType.EPISODE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("agents", "agents", "_agents", AgentEntry, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("configuration", "configuration", "_configuration", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("renderType", "render_type", "_render_type", EnvironmentRenderType, EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dockerImageNameOverride", "docker_image_name_override", "_docker_image_name_override", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("poolNameOverride", "pool_name_override", "_pool_name_override", str, None, PredefinedSerializer(), optional=True),
]

RunEpisodeResponse._fields = [
  FieldMetadata("episode", "episode", "_episode", str, None, PredefinedSerializer(), optional=True),
]

ScheduledKernelSession._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("startDate", "start_date", "_start_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("frequency", "frequency", "_frequency", ScheduleFrequencyType, ScheduleFrequencyType.SCHEDULE_FREQUENCY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("iterations", "iterations", "_iterations", int, 0, PredefinedSerializer()),
  FieldMetadata("iteration", "iteration", "_iteration", int, 0, PredefinedSerializer()),
  FieldMetadata("trigger", "trigger", "_trigger", ScheduleTriggerType, ScheduleTriggerType.SCHEDULE_TRIGGER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastSessionDate", "last_session_date", "_last_session_date", datetime, None, DateTimeSerializer()),
]

ScheduleKernelImportsRequest._fields = [
  FieldMetadata("imports", "imports", "_imports", KernelImport, [], ListSerializer(KaggleObjectSerializer())),
]

ScheduleKernelSessionRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("frequency", "frequency", "_frequency", ScheduleFrequencyType, ScheduleFrequencyType.SCHEDULE_FREQUENCY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("startDate", "start_date", "_start_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("iterations", "iterations", "_iterations", int, 0, PredefinedSerializer()),
  FieldMetadata("trigger", "trigger", "_trigger", ScheduleTriggerType, ScheduleTriggerType.SCHEDULE_TRIGGER_TYPE_UNSPECIFIED, EnumSerializer()),
]

SearchKernelCollaboratorsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("search", "search", "_search", str, "", PredefinedSerializer()),
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("showPrivate", "show_private", "_show_private", bool, False, PredefinedSerializer()),
  FieldMetadata("resultsPerPage", "results_per_page", "_results_per_page", int, 0, PredefinedSerializer()),
]

SearchKernelCollaboratorsResponse._fields = [
  FieldMetadata("results", "results", "_results", CollaboratorItem, [], ListSerializer(KaggleObjectSerializer())),
]

SearchKernelIdsResponse._fields = [
  FieldMetadata("kernelIds", "kernel_ids", "_kernel_ids", int, [], ListSerializer(PredefinedSerializer())),
]

SnippetData._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("content", "content", "_content", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("languageName", "language_name", "_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
]

SubmissionRequestedDetails._fields = [
  FieldMetadata("fileNames", "file_names", "_file_names", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

SyncHuggingFaceModelResourceReferenceMetadataRequest._fields = [
  FieldMetadata("ownerIdentifier", "owner_identifier", "_owner_identifier", str, "", PredefinedSerializer()),
  FieldMetadata("resourceIdentifier", "resource_identifier", "_resource_identifier", str, "", PredefinedSerializer()),
  FieldMetadata("allowMissing", "allow_missing", "_allow_missing", bool, False, PredefinedSerializer()),
]

Tag._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

UpdateDataSourceResult._fields = [
  FieldMetadata("reference", "reference", "_reference", DataSourceReference, None, KaggleObjectSerializer()),
  FieldMetadata("mountedVersion", "mounted_version", "_mounted_version", DataSourceVersion, None, KaggleObjectSerializer()),
  FieldMetadata("newVersion", "new_version", "_new_version", DataSourceVersion, None, KaggleObjectSerializer()),
]

UpdateDataSourceVersionsRequest._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("dryRun", "dry_run", "_dry_run", bool, False, PredefinedSerializer()),
]

UpdateDataSourceVersionsResponse._fields = [
  FieldMetadata("results", "results", "_results", UpdateDataSourceResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("anyChanges", "any_changes", "_any_changes", bool, False, PredefinedSerializer()),
]

UpdateDefaultSessionSettingsRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", DefaultSessionSettings, None, KaggleObjectSerializer()),
  FieldMetadata("deleteSyncSpec", "delete_sync_spec", "_delete_sync_spec", bool, None, PredefinedSerializer(), optional=True),
]

UpdateDependencyManagerPrivacyRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

UpdateDockerImageVersionRequest._fields = [
  FieldMetadata("scriptId", "script_id", "_script_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dockerImageVersionId", "docker_image_version_id", "_docker_image_version_id", int, None, PredefinedSerializer(), optional=True),
]

UpdateDockerPinningTypeRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dockerImagePinningType", "docker_image_pinning_type", "_docker_image_pinning_type", DockerImagePinningType, DockerImagePinningType.DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED, EnumSerializer()),
]

UpdateKernelCategoriesRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("categoryIds", "category_ids", "_category_ids", int, [], ListSerializer(PredefinedSerializer())),
]

UpdateKernelCategoriesResponse._fields = [
  FieldMetadata("categoryIds", "category_ids", "_category_ids", int, [], ListSerializer(PredefinedSerializer())),
]

UpdateKernelDraftRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sequence", "sequence", "_sequence", int, 0, PredefinedSerializer()),
  FieldMetadata("parentKernelVersionId", "parent_kernel_version_id", "_parent_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("settings", "settings", "_settings", KernelBlobSettings, None, KaggleObjectSerializer()),
  FieldMetadata("source", "source", "_source", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalSourceData", "external_source_data", "_external_source_data", ExternalSourceData, None, KaggleObjectSerializer()),
  FieldMetadata("sourceToken", "source_token", "_source_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("githubSpec", "github_spec", "_github_spec", GithubSpec, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("colabSpec", "colab_spec", "_colab_spec", ColabSpec, None, KaggleObjectSerializer(), optional=True),
]

UpdateKernelDraftResponse._fields = [
  FieldMetadata("sequence", "sequence", "_sequence", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("newSettings", "new_settings", "_new_settings", KernelBlobSettings, None, KaggleObjectSerializer(), optional=True),
]

UpdateKernelOutputToDatasetRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
]

UpdateKernelOutputToModelRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
]

UpdateKernelPersistenceRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("persistence", "persistence", "_persistence", PersistenceMode, PersistenceMode.PERSISTENCE_MODE_UNSPECIFIED, EnumSerializer()),
]

UpdateKernelPersistenceResponse._fields = []

UpdateKernelPrivacyRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("disableComments", "disable_comments", "_disable_comments", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
]

UpdateKernelPrivacyResponse._fields = [
  FieldMetadata("canToggleVisibility", "can_toggle_visibility", "_can_toggle_visibility", bool, False, PredefinedSerializer()),
]

UpdateKernelSessionKeepaliveRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

UpdateKernelSessionRequest._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isInternetEnabled", "is_internet_enabled", "_is_internet_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateKernelSessionResponse._fields = [
  FieldMetadata("restartRequired", "restart_required", "_restart_required", bool, False, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateKernelsPrivacyRequest._fields = [
  FieldMetadata("kernelIds", "kernel_ids", "_kernel_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, None, PredefinedSerializer(), optional=True),
]

UpdateKernelTitleRequest._fields = [
  FieldMetadata("newTitle", "new_title", "_new_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scriptVersionId", "script_version_id", "_script_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fromKernelImportWorker", "from_kernel_import_worker", "_from_kernel_import_worker", bool, None, PredefinedSerializer(), optional=True),
]

UpdateKernelTitleResponse._fields = [
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newUrl", "new_url", "_new_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newTitle", "new_title", "_new_title", str, None, PredefinedSerializer(), optional=True),
]

UpdateKernelVersionNameRequest._fields = [
  FieldMetadata("versionId", "version_id", "_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("newName", "new_name", "_new_name", str, None, PredefinedSerializer(), optional=True),
]

UpdateKernelViewCountRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

UpdatePinnedKernelSessionRequest._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pinningType", "pinning_type", "_pinning_type", KernelVersionPinningType, KernelVersionPinningType.UNPINNED, EnumSerializer()),
]

UpdateResourceReferenceRequest._fields = [
  FieldMetadata("resourceReference", "resource_reference", "_resource_reference", ResourceReference, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateUserKernelFirestoreAuthRequest._fields = [
  FieldMetadata("kernelRunId", "kernel_run_id", "_kernel_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("firebaseIdToken", "firebase_id_token", "_firebase_id_token", str, None, PredefinedSerializer(), optional=True),
]

UpdateUserKernelFirestoreAuthResponse._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", str, None, PredefinedSerializer(), optional=True),
]

UploadKernelSessionOutputRequest._fields = [
  FieldMetadata("interactiveSessionId", "interactive_session_id", "_interactive_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("batchSessionId", "batch_session_id", "_batch_session_id", int, 0, PredefinedSerializer()),
]

