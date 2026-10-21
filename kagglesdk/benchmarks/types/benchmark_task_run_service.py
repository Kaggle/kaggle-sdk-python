from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkCandidateType, BenchmarkTaskRunState
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkSchedulerSettings
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BatchScheduleBenchmarkModelVersionResult(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_version_ids
    run_scheduled (bool)
      Whether the run was scheduled for the provided (TaskVersion, Candidate)
      pair.
    run_skipped_reason (str)
      If run_scheduled was false, the reason the (TaskVersion, Candidate) pair
      was skipped
    benchmark_task_version_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_version_ids
    parent_task_version_id (int)
      If the request task version was a leaf, this field indicates the parent
      task version that should be executed instead.
    agent_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_agent_ids
    candidate_type (BenchmarkCandidateType)
      Specifies the candidate type that was scheduled (ModelVersion vs. Agent)
    benchmark_model_version_config_id (int)
      The BenchmarkModelVersionConfig the run was scheduled against, resolved
      from benchmark_model_version_id plus the request's reasoning_effort. Unset
      when the request named no reasoning effort.
      TODO(bml): eventually deprecate benchmark_model_version_id in favor of
      this field, since the config identifies the model version too.
    run_id (int)
      The id of the BenchmarkRun that was scheduled. Set only when run_scheduled
      is true.
  """

  def __init__(self):
    self._benchmark_model_version_id = 0
    self._run_scheduled = False
    self._run_skipped_reason = None
    self._benchmark_task_version_id = 0
    self._parent_task_version_id = None
    self._agent_id = 0
    self._candidate_type = BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED
    self._benchmark_model_version_config_id = None
    self._run_id = None
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    r"""
    One of the values provided in
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_version_ids
    """
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id

  @property
  def benchmark_model_version_id(self) -> int:
    r"""
    One of the values provided in
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_version_ids
    """
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def agent_id(self) -> int:
    r"""
    One of the values provided in
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_agent_ids
    """
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: int):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, int):
      raise TypeError('agent_id must be of type int')
    self._agent_id = agent_id

  @property
  def benchmark_model_version_config_id(self) -> int:
    r"""
    The BenchmarkModelVersionConfig the run was scheduled against, resolved
    from benchmark_model_version_id plus the request's reasoning_effort. Unset
    when the request named no reasoning effort.
    TODO(bml): eventually deprecate benchmark_model_version_id in favor of
    this field, since the config identifies the model version too.
    """
    return self._benchmark_model_version_config_id or 0

  @benchmark_model_version_config_id.setter
  def benchmark_model_version_config_id(self, benchmark_model_version_config_id: Optional[int]):
    if benchmark_model_version_config_id is None:
      del self.benchmark_model_version_config_id
      return
    if not isinstance(benchmark_model_version_config_id, int):
      raise TypeError('benchmark_model_version_config_id must be of type int')
    self._benchmark_model_version_config_id = benchmark_model_version_config_id

  @property
  def candidate_type(self) -> 'BenchmarkCandidateType':
    """Specifies the candidate type that was scheduled (ModelVersion vs. Agent)"""
    return self._candidate_type

  @candidate_type.setter
  def candidate_type(self, candidate_type: 'BenchmarkCandidateType'):
    if candidate_type is None:
      del self.candidate_type
      return
    if not isinstance(candidate_type, BenchmarkCandidateType):
      raise TypeError('candidate_type must be of type BenchmarkCandidateType')
    self._candidate_type = candidate_type

  @property
  def run_scheduled(self) -> bool:
    r"""
    Whether the run was scheduled for the provided (TaskVersion, Candidate)
    pair.
    """
    return self._run_scheduled

  @run_scheduled.setter
  def run_scheduled(self, run_scheduled: bool):
    if run_scheduled is None:
      del self.run_scheduled
      return
    if not isinstance(run_scheduled, bool):
      raise TypeError('run_scheduled must be of type bool')
    self._run_scheduled = run_scheduled

  @property
  def run_id(self) -> int:
    r"""
    The id of the BenchmarkRun that was scheduled. Set only when run_scheduled
    is true.
    """
    return self._run_id or 0

  @run_id.setter
  def run_id(self, run_id: Optional[int]):
    if run_id is None:
      del self.run_id
      return
    if not isinstance(run_id, int):
      raise TypeError('run_id must be of type int')
    self._run_id = run_id

  @property
  def run_skipped_reason(self) -> str:
    r"""
    If run_scheduled was false, the reason the (TaskVersion, Candidate) pair
    was skipped
    """
    return self._run_skipped_reason or ""

  @run_skipped_reason.setter
  def run_skipped_reason(self, run_skipped_reason: Optional[str]):
    if run_skipped_reason is None:
      del self.run_skipped_reason
      return
    if not isinstance(run_skipped_reason, str):
      raise TypeError('run_skipped_reason must be of type str')
    self._run_skipped_reason = run_skipped_reason

  @property
  def parent_task_version_id(self) -> int:
    r"""
    If the request task version was a leaf, this field indicates the parent
    task version that should be executed instead.
    """
    return self._parent_task_version_id or 0

  @parent_task_version_id.setter
  def parent_task_version_id(self, parent_task_version_id: Optional[int]):
    if parent_task_version_id is None:
      del self.parent_task_version_id
      return
    if not isinstance(parent_task_version_id, int):
      raise TypeError('parent_task_version_id must be of type int')
    self._parent_task_version_id = parent_task_version_id


class BenchmarkSchedulerBenchmarkStats(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
      Unset for the row grouping runs of unmapped tasks, and for the withheld
      row below.
    benchmark_name (str)
    withheld (bool)
      Groups runs on benchmarks the caller can't read, so their counts still add
      up without disclosing which benchmarks they are.
    queued_count (int)
    running_count (int)
    recent_state_counts (BenchmarkSchedulerStateCount)
  """

  def __init__(self):
    self._benchmark_id = None
    self._benchmark_name = ""
    self._withheld = False
    self._queued_count = 0
    self._running_count = 0
    self._recent_state_counts = []
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    r"""
    Unset for the row grouping runs of unmapped tasks, and for the withheld
    row below.
    """
    return self._benchmark_id or 0

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: Optional[int]):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def benchmark_name(self) -> str:
    return self._benchmark_name

  @benchmark_name.setter
  def benchmark_name(self, benchmark_name: str):
    if benchmark_name is None:
      del self.benchmark_name
      return
    if not isinstance(benchmark_name, str):
      raise TypeError('benchmark_name must be of type str')
    self._benchmark_name = benchmark_name

  @property
  def withheld(self) -> bool:
    r"""
    Groups runs on benchmarks the caller can't read, so their counts still add
    up without disclosing which benchmarks they are.
    """
    return self._withheld

  @withheld.setter
  def withheld(self, withheld: bool):
    if withheld is None:
      del self.withheld
      return
    if not isinstance(withheld, bool):
      raise TypeError('withheld must be of type bool')
    self._withheld = withheld

  @property
  def queued_count(self) -> int:
    return self._queued_count

  @queued_count.setter
  def queued_count(self, queued_count: int):
    if queued_count is None:
      del self.queued_count
      return
    if not isinstance(queued_count, int):
      raise TypeError('queued_count must be of type int')
    self._queued_count = queued_count

  @property
  def running_count(self) -> int:
    return self._running_count

  @running_count.setter
  def running_count(self, running_count: int):
    if running_count is None:
      del self.running_count
      return
    if not isinstance(running_count, int):
      raise TypeError('running_count must be of type int')
    self._running_count = running_count

  @property
  def recent_state_counts(self) -> Optional[List[Optional['BenchmarkSchedulerStateCount']]]:
    return self._recent_state_counts

  @recent_state_counts.setter
  def recent_state_counts(self, recent_state_counts: Optional[List[Optional['BenchmarkSchedulerStateCount']]]):
    if recent_state_counts is None:
      del self.recent_state_counts
      return
    if not isinstance(recent_state_counts, list):
      raise TypeError('recent_state_counts must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerStateCount) for t in recent_state_counts]):
      raise TypeError('recent_state_counts must contain only items of type BenchmarkSchedulerStateCount')
    self._recent_state_counts = recent_state_counts


class BenchmarkSchedulerModelVersionStats(KaggleObject):
  r"""
  Agent runs count under their backing model version, which is the identity
  the per-candidate cap and Model Proxy capacity are tracked against.

  Attributes:
    benchmark_model_version_id (int)
    queued_count (int)
    running_count (int)
    recent_state_counts (BenchmarkSchedulerStateCount)
      Same 24-hour window as the fleet-wide recent_state_counts, so one failing
      candidate can be told apart from a fleet-wide problem.
  """

  def __init__(self):
    self._benchmark_model_version_id = 0
    self._queued_count = 0
    self._running_count = 0
    self._recent_state_counts = []
    self._freeze()

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def queued_count(self) -> int:
    return self._queued_count

  @queued_count.setter
  def queued_count(self, queued_count: int):
    if queued_count is None:
      del self.queued_count
      return
    if not isinstance(queued_count, int):
      raise TypeError('queued_count must be of type int')
    self._queued_count = queued_count

  @property
  def running_count(self) -> int:
    return self._running_count

  @running_count.setter
  def running_count(self, running_count: int):
    if running_count is None:
      del self.running_count
      return
    if not isinstance(running_count, int):
      raise TypeError('running_count must be of type int')
    self._running_count = running_count

  @property
  def recent_state_counts(self) -> Optional[List[Optional['BenchmarkSchedulerStateCount']]]:
    r"""
    Same 24-hour window as the fleet-wide recent_state_counts, so one failing
    candidate can be told apart from a fleet-wide problem.
    """
    return self._recent_state_counts

  @recent_state_counts.setter
  def recent_state_counts(self, recent_state_counts: Optional[List[Optional['BenchmarkSchedulerStateCount']]]):
    if recent_state_counts is None:
      del self.recent_state_counts
      return
    if not isinstance(recent_state_counts, list):
      raise TypeError('recent_state_counts must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerStateCount) for t in recent_state_counts]):
      raise TypeError('recent_state_counts must contain only items of type BenchmarkSchedulerStateCount')
    self._recent_state_counts = recent_state_counts


class BenchmarkSchedulerStateCount(KaggleObject):
  r"""
  Attributes:
    state (BenchmarkTaskRunState)
    count (int)
  """

  def __init__(self):
    self._state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._count = 0
    self._freeze()

  @property
  def state(self) -> 'BenchmarkTaskRunState':
    return self._state

  @state.setter
  def state(self, state: 'BenchmarkTaskRunState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, BenchmarkTaskRunState):
      raise TypeError('state must be of type BenchmarkTaskRunState')
    self._state = state

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


class GetBenchmarkSchedulerStatusResponse(KaggleObject):
  r"""
  Point-in-time readout of the scheduler. Under FLEET, every count covers only
  runs the scheduler enqueued (non-null EnqueueTime): that scope reports on the
  drain, and synchronously started runs are work it never saw and cannot
  influence. SELF counts the caller's runs however they were started, since the
  surfaces they schedule through start runs synchronously. Counts always
  exclude removed runs and leaf runs of a multi-metric parent, which share the
  parent's session.

  Attributes:
    state_counts (BenchmarkSchedulerStateCount)
      Queue depth per live state (Queued, Running, ScorePending); a state with
      no runs is omitted. Not a map because proto3 forbids enum keys.
    recent_state_counts (BenchmarkSchedulerStateCount)
      Completed / Errored counts for runs that ended in the last 24 hours.
      Excludes cancellations, which are stamped Errored and removed.
    model_version_stats (BenchmarkSchedulerModelVersionStats)
      One entry per model version with live work or a recent outcome, ordered
      by running count descending, then id ascending so ties stay stable.
    settings (BenchmarkSchedulerSettings)
      The settings these counts were measured against. The caps are enforced over
      the enqueued-only population, so headroom is their difference from the
      FLEET counts; under SELF the counts cover a wider population than the caps
      govern. Readable by any caller of this RPC, writes stay admin-only.
    benchmark_stats (BenchmarkSchedulerBenchmarkStats)
      The same counts as model_version_stats, grouped by the run's benchmark
      instead, with the same inclusion rule and order.
  """

  def __init__(self):
    self._state_counts = []
    self._recent_state_counts = []
    self._model_version_stats = []
    self._settings = None
    self._benchmark_stats = []
    self._freeze()

  @property
  def state_counts(self) -> Optional[List[Optional['BenchmarkSchedulerStateCount']]]:
    r"""
    Queue depth per live state (Queued, Running, ScorePending); a state with
    no runs is omitted. Not a map because proto3 forbids enum keys.
    """
    return self._state_counts

  @state_counts.setter
  def state_counts(self, state_counts: Optional[List[Optional['BenchmarkSchedulerStateCount']]]):
    if state_counts is None:
      del self.state_counts
      return
    if not isinstance(state_counts, list):
      raise TypeError('state_counts must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerStateCount) for t in state_counts]):
      raise TypeError('state_counts must contain only items of type BenchmarkSchedulerStateCount')
    self._state_counts = state_counts

  @property
  def recent_state_counts(self) -> Optional[List[Optional['BenchmarkSchedulerStateCount']]]:
    r"""
    Completed / Errored counts for runs that ended in the last 24 hours.
    Excludes cancellations, which are stamped Errored and removed.
    """
    return self._recent_state_counts

  @recent_state_counts.setter
  def recent_state_counts(self, recent_state_counts: Optional[List[Optional['BenchmarkSchedulerStateCount']]]):
    if recent_state_counts is None:
      del self.recent_state_counts
      return
    if not isinstance(recent_state_counts, list):
      raise TypeError('recent_state_counts must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerStateCount) for t in recent_state_counts]):
      raise TypeError('recent_state_counts must contain only items of type BenchmarkSchedulerStateCount')
    self._recent_state_counts = recent_state_counts

  @property
  def model_version_stats(self) -> Optional[List[Optional['BenchmarkSchedulerModelVersionStats']]]:
    r"""
    One entry per model version with live work or a recent outcome, ordered
    by running count descending, then id ascending so ties stay stable.
    """
    return self._model_version_stats

  @model_version_stats.setter
  def model_version_stats(self, model_version_stats: Optional[List[Optional['BenchmarkSchedulerModelVersionStats']]]):
    if model_version_stats is None:
      del self.model_version_stats
      return
    if not isinstance(model_version_stats, list):
      raise TypeError('model_version_stats must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerModelVersionStats) for t in model_version_stats]):
      raise TypeError('model_version_stats must contain only items of type BenchmarkSchedulerModelVersionStats')
    self._model_version_stats = model_version_stats

  @property
  def settings(self) -> Optional['BenchmarkSchedulerSettings']:
    r"""
    The settings these counts were measured against. The caps are enforced over
    the enqueued-only population, so headroom is their difference from the
    FLEET counts; under SELF the counts cover a wider population than the caps
    govern. Readable by any caller of this RPC, writes stay admin-only.
    """
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['BenchmarkSchedulerSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, BenchmarkSchedulerSettings):
      raise TypeError('settings must be of type BenchmarkSchedulerSettings')
    self._settings = settings

  @property
  def benchmark_stats(self) -> Optional[List[Optional['BenchmarkSchedulerBenchmarkStats']]]:
    r"""
    The same counts as model_version_stats, grouped by the run's benchmark
    instead, with the same inclusion rule and order.
    """
    return self._benchmark_stats

  @benchmark_stats.setter
  def benchmark_stats(self, benchmark_stats: Optional[List[Optional['BenchmarkSchedulerBenchmarkStats']]]):
    if benchmark_stats is None:
      del self.benchmark_stats
      return
    if not isinstance(benchmark_stats, list):
      raise TypeError('benchmark_stats must be of type list')
    if not all([isinstance(t, BenchmarkSchedulerBenchmarkStats) for t in benchmark_stats]):
      raise TypeError('benchmark_stats must contain only items of type BenchmarkSchedulerBenchmarkStats')
    self._benchmark_stats = benchmark_stats

  @property
  def stateCounts(self):
    return self.state_counts

  @property
  def recentStateCounts(self):
    return self.recent_state_counts

  @property
  def modelVersionStats(self):
    return self.model_version_stats

  @property
  def benchmarkStats(self):
    return self.benchmark_stats


BatchScheduleBenchmarkModelVersionResult._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runScheduled", "run_scheduled", "_run_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("runSkippedReason", "run_skipped_reason", "_run_skipped_reason", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentTaskVersionId", "parent_task_version_id", "_parent_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentId", "agent_id", "_agent_id", int, 0, PredefinedSerializer()),
  FieldMetadata("candidateType", "candidate_type", "_candidate_type", BenchmarkCandidateType, BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("benchmarkModelVersionConfigId", "benchmark_model_version_config_id", "_benchmark_model_version_config_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("runId", "run_id", "_run_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkSchedulerBenchmarkStats._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkName", "benchmark_name", "_benchmark_name", str, "", PredefinedSerializer()),
  FieldMetadata("withheld", "withheld", "_withheld", bool, False, PredefinedSerializer()),
  FieldMetadata("queuedCount", "queued_count", "_queued_count", int, 0, PredefinedSerializer()),
  FieldMetadata("runningCount", "running_count", "_running_count", int, 0, PredefinedSerializer()),
  FieldMetadata("recentStateCounts", "recent_state_counts", "_recent_state_counts", BenchmarkSchedulerStateCount, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkSchedulerModelVersionStats._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("queuedCount", "queued_count", "_queued_count", int, 0, PredefinedSerializer()),
  FieldMetadata("runningCount", "running_count", "_running_count", int, 0, PredefinedSerializer()),
  FieldMetadata("recentStateCounts", "recent_state_counts", "_recent_state_counts", BenchmarkSchedulerStateCount, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkSchedulerStateCount._fields = [
  FieldMetadata("state", "state", "_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

GetBenchmarkSchedulerStatusResponse._fields = [
  FieldMetadata("stateCounts", "state_counts", "_state_counts", BenchmarkSchedulerStateCount, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("recentStateCounts", "recent_state_counts", "_recent_state_counts", BenchmarkSchedulerStateCount, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelVersionStats", "model_version_stats", "_model_version_stats", BenchmarkSchedulerModelVersionStats, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("settings", "settings", "_settings", BenchmarkSchedulerSettings, None, KaggleObjectSerializer()),
  FieldMetadata("benchmarkStats", "benchmark_stats", "_benchmark_stats", BenchmarkSchedulerBenchmarkStats, [], ListSerializer(KaggleObjectSerializer())),
]

