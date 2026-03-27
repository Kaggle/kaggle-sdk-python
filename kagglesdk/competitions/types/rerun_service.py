from datetime import datetime
from kagglesdk.competitions.types.rerun_state import RerunStateName
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BulkRerunInfo(KaggleObject):
  r"""
  Attributes:
    id (int)
    date_initiated (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    state_counts (RerunStateCount)
  """

  def __init__(self):
    self._id = 0
    self._date_initiated = None
    self._state_counts = []
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
  def date_initiated(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_initiated

  @date_initiated.setter
  def date_initiated(self, date_initiated: datetime):
    if date_initiated is None:
      del self.date_initiated
      return
    if not isinstance(date_initiated, datetime):
      raise TypeError('date_initiated must be of type datetime')
    self._date_initiated = date_initiated

  @property
  def state_counts(self) -> Optional[List[Optional['RerunStateCount']]]:
    return self._state_counts

  @state_counts.setter
  def state_counts(self, state_counts: Optional[List[Optional['RerunStateCount']]]):
    if state_counts is None:
      del self.state_counts
      return
    if not isinstance(state_counts, list):
      raise TypeError('state_counts must be of type list')
    if not all([isinstance(t, RerunStateCount) for t in state_counts]):
      raise TypeError('state_counts must contain only items of type RerunStateCount')
    self._state_counts = state_counts


class CancelBulkRerunRequest(KaggleObject):
  r"""
  Attributes:
    bulk_rerun_id (int)
  """

  def __init__(self):
    self._bulk_rerun_id = 0
    self._freeze()

  @property
  def bulk_rerun_id(self) -> int:
    return self._bulk_rerun_id

  @bulk_rerun_id.setter
  def bulk_rerun_id(self, bulk_rerun_id: int):
    if bulk_rerun_id is None:
      del self.bulk_rerun_id
      return
    if not isinstance(bulk_rerun_id, int):
      raise TypeError('bulk_rerun_id must be of type int')
    self._bulk_rerun_id = bulk_rerun_id


class InitiateBulkRerunRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    submission_selector (InitiateBulkRerunRequest.RerunSubmissionSelector)
      Object which helps select Submissions.  Each selected Submission yields
      exactly one child Rerun.
    kernel_run_settings (InitiateBulkRerunRequest.KernelRunSettings)
      Object which controls the Kernel Run for each Rerun.
    expected_submission_filename (str)
      Filename to look for in Kernel Run output to send for Submission.  If
      unset, will use existing Submission's filename.
    max_retries (int)
      Max number of times to attempt a Rerun.  Default is 3.
    use_updated_datasources (bool)
      Whether to take latest versions of all datasources or the previous
      versions from the user's Kernel Commit.
  """

  class KernelRunSettings(KaggleObject):
    r"""
    Attributes:
      max_ram_gb (float)
        Currently unused.
      max_disk_gb (float)
        Currently unused.
      max_cpu_runtime_hours (float)
        Currently unused.
      max_gpu_runtime_hours (float)
        Currently unused.
      cpu_worker_pool_name (str)
      p100_worker_pool_name (str)
      t4_worker_pool_name (str)
    """

    def __init__(self):
      self._max_ram_gb = 0.0
      self._max_disk_gb = 0.0
      self._max_cpu_runtime_hours = 0.0
      self._max_gpu_runtime_hours = 0.0
      self._cpu_worker_pool_name = None
      self._p100_worker_pool_name = None
      self._t4_worker_pool_name = None
      self._freeze()

    @property
    def max_ram_gb(self) -> float:
      """Currently unused."""
      return self._max_ram_gb

    @max_ram_gb.setter
    def max_ram_gb(self, max_ram_gb: float):
      if max_ram_gb is None:
        del self.max_ram_gb
        return
      if not isinstance(max_ram_gb, float):
        raise TypeError('max_ram_gb must be of type float')
      self._max_ram_gb = max_ram_gb

    @property
    def max_disk_gb(self) -> float:
      """Currently unused."""
      return self._max_disk_gb

    @max_disk_gb.setter
    def max_disk_gb(self, max_disk_gb: float):
      if max_disk_gb is None:
        del self.max_disk_gb
        return
      if not isinstance(max_disk_gb, float):
        raise TypeError('max_disk_gb must be of type float')
      self._max_disk_gb = max_disk_gb

    @property
    def max_cpu_runtime_hours(self) -> float:
      """Currently unused."""
      return self._max_cpu_runtime_hours

    @max_cpu_runtime_hours.setter
    def max_cpu_runtime_hours(self, max_cpu_runtime_hours: float):
      if max_cpu_runtime_hours is None:
        del self.max_cpu_runtime_hours
        return
      if not isinstance(max_cpu_runtime_hours, float):
        raise TypeError('max_cpu_runtime_hours must be of type float')
      self._max_cpu_runtime_hours = max_cpu_runtime_hours

    @property
    def max_gpu_runtime_hours(self) -> float:
      """Currently unused."""
      return self._max_gpu_runtime_hours

    @max_gpu_runtime_hours.setter
    def max_gpu_runtime_hours(self, max_gpu_runtime_hours: float):
      if max_gpu_runtime_hours is None:
        del self.max_gpu_runtime_hours
        return
      if not isinstance(max_gpu_runtime_hours, float):
        raise TypeError('max_gpu_runtime_hours must be of type float')
      self._max_gpu_runtime_hours = max_gpu_runtime_hours

    @property
    def cpu_worker_pool_name(self) -> str:
      return self._cpu_worker_pool_name or ""

    @cpu_worker_pool_name.setter
    def cpu_worker_pool_name(self, cpu_worker_pool_name: Optional[str]):
      if cpu_worker_pool_name is None:
        del self.cpu_worker_pool_name
        return
      if not isinstance(cpu_worker_pool_name, str):
        raise TypeError('cpu_worker_pool_name must be of type str')
      self._cpu_worker_pool_name = cpu_worker_pool_name

    @property
    def p100_worker_pool_name(self) -> str:
      return self._p100_worker_pool_name or ""

    @p100_worker_pool_name.setter
    def p100_worker_pool_name(self, p100_worker_pool_name: Optional[str]):
      if p100_worker_pool_name is None:
        del self.p100_worker_pool_name
        return
      if not isinstance(p100_worker_pool_name, str):
        raise TypeError('p100_worker_pool_name must be of type str')
      self._p100_worker_pool_name = p100_worker_pool_name

    @property
    def t4_worker_pool_name(self) -> str:
      return self._t4_worker_pool_name or ""

    @t4_worker_pool_name.setter
    def t4_worker_pool_name(self, t4_worker_pool_name: Optional[str]):
      if t4_worker_pool_name is None:
        del self.t4_worker_pool_name
        return
      if not isinstance(t4_worker_pool_name, str):
        raise TypeError('t4_worker_pool_name must be of type str')
      self._t4_worker_pool_name = t4_worker_pool_name


  class RerunSubmissionSelector(KaggleObject):
    r"""
    Attributes:
      max_submissions (int)
        If > 0, we won't select more Submissions than specified here.
      submission_ids (int)
        If set and non-empty, we will only look for Submissions with the given
        Ids.
      auto_select (bool)
        If set, take unselected Submissions with highest Public Score up to
        Competition.NumScoredSubmissions.
    """

    def __init__(self):
      self._max_submissions = 0
      self._submission_ids = []
      self._auto_select = False
      self._freeze()

    @property
    def max_submissions(self) -> int:
      """If > 0, we won't select more Submissions than specified here."""
      return self._max_submissions

    @max_submissions.setter
    def max_submissions(self, max_submissions: int):
      if max_submissions is None:
        del self.max_submissions
        return
      if not isinstance(max_submissions, int):
        raise TypeError('max_submissions must be of type int')
      self._max_submissions = max_submissions

    @property
    def submission_ids(self) -> Optional[List[int]]:
      r"""
      If set and non-empty, we will only look for Submissions with the given
      Ids.
      """
      return self._submission_ids

    @submission_ids.setter
    def submission_ids(self, submission_ids: Optional[List[int]]):
      if submission_ids is None:
        del self.submission_ids
        return
      if not isinstance(submission_ids, list):
        raise TypeError('submission_ids must be of type list')
      if not all([isinstance(t, int) for t in submission_ids]):
        raise TypeError('submission_ids must contain only items of type int')
      self._submission_ids = submission_ids

    @property
    def auto_select(self) -> bool:
      r"""
      If set, take unselected Submissions with highest Public Score up to
      Competition.NumScoredSubmissions.
      """
      return self._auto_select

    @auto_select.setter
    def auto_select(self, auto_select: bool):
      if auto_select is None:
        del self.auto_select
        return
      if not isinstance(auto_select, bool):
        raise TypeError('auto_select must be of type bool')
      self._auto_select = auto_select


  def __init__(self):
    self._competition_id = 0
    self._submission_selector = None
    self._kernel_run_settings = None
    self._expected_submission_filename = ""
    self._max_retries = 0
    self._use_updated_datasources = False
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
  def submission_selector(self) -> Optional['InitiateBulkRerunRequest.RerunSubmissionSelector']:
    r"""
    Object which helps select Submissions.  Each selected Submission yields
    exactly one child Rerun.
    """
    return self._submission_selector

  @submission_selector.setter
  def submission_selector(self, submission_selector: Optional['InitiateBulkRerunRequest.RerunSubmissionSelector']):
    if submission_selector is None:
      del self.submission_selector
      return
    if not isinstance(submission_selector, InitiateBulkRerunRequest.RerunSubmissionSelector):
      raise TypeError('submission_selector must be of type InitiateBulkRerunRequest.RerunSubmissionSelector')
    self._submission_selector = submission_selector

  @property
  def kernel_run_settings(self) -> Optional['InitiateBulkRerunRequest.KernelRunSettings']:
    """Object which controls the Kernel Run for each Rerun."""
    return self._kernel_run_settings

  @kernel_run_settings.setter
  def kernel_run_settings(self, kernel_run_settings: Optional['InitiateBulkRerunRequest.KernelRunSettings']):
    if kernel_run_settings is None:
      del self.kernel_run_settings
      return
    if not isinstance(kernel_run_settings, InitiateBulkRerunRequest.KernelRunSettings):
      raise TypeError('kernel_run_settings must be of type InitiateBulkRerunRequest.KernelRunSettings')
    self._kernel_run_settings = kernel_run_settings

  @property
  def expected_submission_filename(self) -> str:
    r"""
    Filename to look for in Kernel Run output to send for Submission.  If
    unset, will use existing Submission's filename.
    """
    return self._expected_submission_filename

  @expected_submission_filename.setter
  def expected_submission_filename(self, expected_submission_filename: str):
    if expected_submission_filename is None:
      del self.expected_submission_filename
      return
    if not isinstance(expected_submission_filename, str):
      raise TypeError('expected_submission_filename must be of type str')
    self._expected_submission_filename = expected_submission_filename

  @property
  def max_retries(self) -> int:
    """Max number of times to attempt a Rerun.  Default is 3."""
    return self._max_retries

  @max_retries.setter
  def max_retries(self, max_retries: int):
    if max_retries is None:
      del self.max_retries
      return
    if not isinstance(max_retries, int):
      raise TypeError('max_retries must be of type int')
    self._max_retries = max_retries

  @property
  def use_updated_datasources(self) -> bool:
    r"""
    Whether to take latest versions of all datasources or the previous
    versions from the user's Kernel Commit.
    """
    return self._use_updated_datasources

  @use_updated_datasources.setter
  def use_updated_datasources(self, use_updated_datasources: bool):
    if use_updated_datasources is None:
      del self.use_updated_datasources
      return
    if not isinstance(use_updated_datasources, bool):
      raise TypeError('use_updated_datasources must be of type bool')
    self._use_updated_datasources = use_updated_datasources


class InitiateBulkRerunResponse(KaggleObject):
  r"""
  Attributes:
    num_created (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
  """

  def __init__(self):
    self._num_created = 0
    self._freeze()

  @property
  def num_created(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_created

  @num_created.setter
  def num_created(self, num_created: int):
    if num_created is None:
      del self.num_created
      return
    if not isinstance(num_created, int):
      raise TypeError('num_created must be of type int')
    self._num_created = num_created


class ListBulkRerunsRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
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


class ListBulkRerunsResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    bulk_reruns (BulkRerunInfo)
  """

  def __init__(self):
    self._bulk_reruns = []
    self._freeze()

  @property
  def bulk_reruns(self) -> Optional[List[Optional['BulkRerunInfo']]]:
    return self._bulk_reruns

  @bulk_reruns.setter
  def bulk_reruns(self, bulk_reruns: Optional[List[Optional['BulkRerunInfo']]]):
    if bulk_reruns is None:
      del self.bulk_reruns
      return
    if not isinstance(bulk_reruns, list):
      raise TypeError('bulk_reruns must be of type list')
    if not all([isinstance(t, BulkRerunInfo) for t in bulk_reruns]):
      raise TypeError('bulk_reruns must contain only items of type BulkRerunInfo')
    self._bulk_reruns = bulk_reruns


class PublishBulkRerunRequest(KaggleObject):
  r"""
  Attributes:
    bulk_rerun_id (int)
    publish_to_source (bool)
      Whether to publish rerun results directly to the user's source submission
      instead of generating a new submission.
  """

  def __init__(self):
    self._bulk_rerun_id = 0
    self._publish_to_source = False
    self._freeze()

  @property
  def bulk_rerun_id(self) -> int:
    return self._bulk_rerun_id

  @bulk_rerun_id.setter
  def bulk_rerun_id(self, bulk_rerun_id: int):
    if bulk_rerun_id is None:
      del self.bulk_rerun_id
      return
    if not isinstance(bulk_rerun_id, int):
      raise TypeError('bulk_rerun_id must be of type int')
    self._bulk_rerun_id = bulk_rerun_id

  @property
  def publish_to_source(self) -> bool:
    r"""
    Whether to publish rerun results directly to the user's source submission
    instead of generating a new submission.
    """
    return self._publish_to_source

  @publish_to_source.setter
  def publish_to_source(self, publish_to_source: bool):
    if publish_to_source is None:
      del self.publish_to_source
      return
    if not isinstance(publish_to_source, bool):
      raise TypeError('publish_to_source must be of type bool')
    self._publish_to_source = publish_to_source


class RerunStateCount(KaggleObject):
  r"""
  Attributes:
    name (RerunStateName)
    count (int)
  """

  def __init__(self):
    self._name = RerunStateName.RERUN_STATE_NAME_UNSPECIFIED
    self._count = 0
    self._freeze()

  @property
  def name(self) -> 'RerunStateName':
    return self._name

  @name.setter
  def name(self, name: 'RerunStateName'):
    if name is None:
      del self.name
      return
    if not isinstance(name, RerunStateName):
      raise TypeError('name must be of type RerunStateName')
    self._name = name

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


BulkRerunInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dateInitiated", "date_initiated", "_date_initiated", datetime, None, DateTimeSerializer()),
  FieldMetadata("stateCounts", "state_counts", "_state_counts", RerunStateCount, [], ListSerializer(KaggleObjectSerializer())),
]

CancelBulkRerunRequest._fields = [
  FieldMetadata("bulkRerunId", "bulk_rerun_id", "_bulk_rerun_id", int, 0, PredefinedSerializer()),
]

InitiateBulkRerunRequest.KernelRunSettings._fields = [
  FieldMetadata("maxRamGb", "max_ram_gb", "_max_ram_gb", float, 0.0, PredefinedSerializer()),
  FieldMetadata("maxDiskGb", "max_disk_gb", "_max_disk_gb", float, 0.0, PredefinedSerializer()),
  FieldMetadata("maxCpuRuntimeHours", "max_cpu_runtime_hours", "_max_cpu_runtime_hours", float, 0.0, PredefinedSerializer()),
  FieldMetadata("maxGpuRuntimeHours", "max_gpu_runtime_hours", "_max_gpu_runtime_hours", float, 0.0, PredefinedSerializer()),
  FieldMetadata("cpuWorkerPoolName", "cpu_worker_pool_name", "_cpu_worker_pool_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("p100WorkerPoolName", "p100_worker_pool_name", "_p100_worker_pool_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("t4WorkerPoolName", "t4_worker_pool_name", "_t4_worker_pool_name", str, None, PredefinedSerializer(), optional=True),
]

InitiateBulkRerunRequest.RerunSubmissionSelector._fields = [
  FieldMetadata("maxSubmissions", "max_submissions", "_max_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("autoSelect", "auto_select", "_auto_select", bool, False, PredefinedSerializer()),
]

InitiateBulkRerunRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionSelector", "submission_selector", "_submission_selector", InitiateBulkRerunRequest.RerunSubmissionSelector, None, KaggleObjectSerializer()),
  FieldMetadata("kernelRunSettings", "kernel_run_settings", "_kernel_run_settings", InitiateBulkRerunRequest.KernelRunSettings, None, KaggleObjectSerializer()),
  FieldMetadata("expectedSubmissionFilename", "expected_submission_filename", "_expected_submission_filename", str, "", PredefinedSerializer()),
  FieldMetadata("maxRetries", "max_retries", "_max_retries", int, 0, PredefinedSerializer()),
  FieldMetadata("useUpdatedDatasources", "use_updated_datasources", "_use_updated_datasources", bool, False, PredefinedSerializer()),
]

InitiateBulkRerunResponse._fields = [
  FieldMetadata("numCreated", "num_created", "_num_created", int, 0, PredefinedSerializer()),
]

ListBulkRerunsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListBulkRerunsResponse._fields = [
  FieldMetadata("bulkReruns", "bulk_reruns", "_bulk_reruns", BulkRerunInfo, [], ListSerializer(KaggleObjectSerializer())),
]

PublishBulkRerunRequest._fields = [
  FieldMetadata("bulkRerunId", "bulk_rerun_id", "_bulk_rerun_id", int, 0, PredefinedSerializer()),
  FieldMetadata("publishToSource", "publish_to_source", "_publish_to_source", bool, False, PredefinedSerializer()),
]

RerunStateCount._fields = [
  FieldMetadata("name", "name", "_name", RerunStateName, RerunStateName.RERUN_STATE_NAME_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

