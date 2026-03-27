from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkTaskRun, BenchmarkVersionIdentifier, TaskIdentifier
from kagglesdk.kaggle_object import *
from typing import List, Optional

class BatchScheduleBenchmarkModelVersionResult(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_versions
    run_scheduled (bool)
      Whether the run was scheduled for the provided (benchmark_task_version,
      benchmark_model_version) pair
    run_skipped_reason (str)
      If run_scheduled was false, the reason the provided
      (benchmark_task_version, benchmark_model_version) pair was skipped
    benchmark_task_version_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_versions
  """

  def __init__(self):
    self._benchmark_model_version_id = 0
    self._run_scheduled = False
    self._run_skipped_reason = None
    self._benchmark_task_version_id = 0
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    r"""
    One of the values provided in
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_versions
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
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_versions
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
  def run_scheduled(self) -> bool:
    r"""
    Whether the run was scheduled for the provided (benchmark_task_version,
    benchmark_model_version) pair
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
  def run_skipped_reason(self) -> str:
    r"""
    If run_scheduled was false, the reason the provided
    (benchmark_task_version, benchmark_model_version) pair was skipped
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


class BatchScheduleBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  This request is for manually specifying a task version you want run against
  a set of model versions irrespective of any benchmark. Later, either in this
  handler or with a separate one, we can support providing a benchmark version,
  which has a predefined mapping of which model versions should be run. That
  would effectively replace the benchmark_model_versions field.

  Attributes:
    benchmark_task_version_ids (int)
      The versions of the tasks to run. Because the runs manifest as new
      sessions of the notebook, the requester should have update authz on
      the task version's source kernel session. Can only have one task if
      there is more than one model.
    benchmark_model_version_ids (int)
      Which model version(s) to run the task(s) against. Only
      BenchmarkModelVersions with AllowModelProxy=1 will have runs scheduled. All
      others will be skipped with a stated reason. Can only have one model if
      there is more than one task.
  """

  def __init__(self):
    self._benchmark_task_version_ids = []
    self._benchmark_model_version_ids = []
    self._freeze()

  @property
  def benchmark_task_version_ids(self) -> Optional[List[int]]:
    r"""
    The versions of the tasks to run. Because the runs manifest as new
    sessions of the notebook, the requester should have update authz on
    the task version's source kernel session. Can only have one task if
    there is more than one model.
    """
    return self._benchmark_task_version_ids

  @benchmark_task_version_ids.setter
  def benchmark_task_version_ids(self, benchmark_task_version_ids: Optional[List[int]]):
    if benchmark_task_version_ids is None:
      del self.benchmark_task_version_ids
      return
    if not isinstance(benchmark_task_version_ids, list):
      raise TypeError('benchmark_task_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_task_version_ids]):
      raise TypeError('benchmark_task_version_ids must contain only items of type int')
    self._benchmark_task_version_ids = benchmark_task_version_ids

  @property
  def benchmark_model_version_ids(self) -> Optional[List[int]]:
    r"""
    Which model version(s) to run the task(s) against. Only
    BenchmarkModelVersions with AllowModelProxy=1 will have runs scheduled. All
    others will be skipped with a stated reason. Can only have one model if
    there is more than one task.
    """
    return self._benchmark_model_version_ids

  @benchmark_model_version_ids.setter
  def benchmark_model_version_ids(self, benchmark_model_version_ids: Optional[List[int]]):
    if benchmark_model_version_ids is None:
      del self.benchmark_model_version_ids
      return
    if not isinstance(benchmark_model_version_ids, list):
      raise TypeError('benchmark_model_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_model_version_ids]):
      raise TypeError('benchmark_model_version_ids must contain only items of type int')
    self._benchmark_model_version_ids = benchmark_model_version_ids


class BatchScheduleBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    results (BatchScheduleBenchmarkModelVersionResult)
      Results to indicate which (task, model) pairs were successfully scheduled.
      There should be a BatchScheduleBenchmarkModelVersionResult for every
      (task,model) pair in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_versions and
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_versions.
  """

  def __init__(self):
    self._results = []
    self._freeze()

  @property
  def results(self) -> Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]:
    r"""
    Results to indicate which (task, model) pairs were successfully scheduled.
    There should be a BatchScheduleBenchmarkModelVersionResult for every
    (task,model) pair in
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_task_versions and
    BatchScheduleBenchmarkTaskRunsRequest.benchmark_model_versions.
    """
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, BatchScheduleBenchmarkModelVersionResult) for t in results]):
      raise TypeError('results must contain only items of type BatchScheduleBenchmarkModelVersionResult')
    self._results = results


class CreateBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_runs (BenchmarkTaskRun)
      The benchmark task runs to create.
  """

  def __init__(self):
    self._benchmark_task_runs = []
    self._freeze()

  @property
  def benchmark_task_runs(self) -> Optional[List[Optional['BenchmarkTaskRun']]]:
    """The benchmark task runs to create."""
    return self._benchmark_task_runs

  @benchmark_task_runs.setter
  def benchmark_task_runs(self, benchmark_task_runs: Optional[List[Optional['BenchmarkTaskRun']]]):
    if benchmark_task_runs is None:
      del self.benchmark_task_runs
      return
    if not isinstance(benchmark_task_runs, list):
      raise TypeError('benchmark_task_runs must be of type list')
    if not all([isinstance(t, BenchmarkTaskRun) for t in benchmark_task_runs]):
      raise TypeError('benchmark_task_runs must contain only items of type BenchmarkTaskRun')
    self._benchmark_task_runs = benchmark_task_runs


class CreateBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_task_runs (BenchmarkTaskRun)
      The created benchmark task runs.
  """

  def __init__(self):
    self._benchmark_task_runs = []
    self._freeze()

  @property
  def benchmark_task_runs(self) -> Optional[List[Optional['BenchmarkTaskRun']]]:
    """The created benchmark task runs."""
    return self._benchmark_task_runs

  @benchmark_task_runs.setter
  def benchmark_task_runs(self, benchmark_task_runs: Optional[List[Optional['BenchmarkTaskRun']]]):
    if benchmark_task_runs is None:
      del self.benchmark_task_runs
      return
    if not isinstance(benchmark_task_runs, list):
      raise TypeError('benchmark_task_runs must be of type list')
    if not all([isinstance(t, BenchmarkTaskRun) for t in benchmark_task_runs]):
      raise TypeError('benchmark_task_runs must contain only items of type BenchmarkTaskRun')
    self._benchmark_task_runs = benchmark_task_runs


class DeleteBenchmarkTaskRunRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_run_id (int)
      The benchmark task run to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
  """

  def __init__(self):
    self._benchmark_task_run_id = 0
    self._is_user_delete = False
    self._freeze()

  @property
  def benchmark_task_run_id(self) -> int:
    """The benchmark task run to delete."""
    return self._benchmark_task_run_id

  @benchmark_task_run_id.setter
  def benchmark_task_run_id(self, benchmark_task_run_id: int):
    if benchmark_task_run_id is None:
      del self.benchmark_task_run_id
      return
    if not isinstance(benchmark_task_run_id, int):
      raise TypeError('benchmark_task_run_id must be of type int')
    self._benchmark_task_run_id = benchmark_task_run_id

  @property
  def is_user_delete(self) -> bool:
    """Whether the delete is from a user or for moderation."""
    return self._is_user_delete

  @is_user_delete.setter
  def is_user_delete(self, is_user_delete: bool):
    if is_user_delete is None:
      del self.is_user_delete
      return
    if not isinstance(is_user_delete, bool):
      raise TypeError('is_user_delete must be of type bool')
    self._is_user_delete = is_user_delete


class GetBenchmarkTaskRunRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_run_id (int)
  """

  def __init__(self):
    self._benchmark_task_run_id = 0
    self._freeze()

  @property
  def benchmark_task_run_id(self) -> int:
    return self._benchmark_task_run_id

  @benchmark_task_run_id.setter
  def benchmark_task_run_id(self, benchmark_task_run_id: int):
    if benchmark_task_run_id is None:
      del self.benchmark_task_run_id
      return
    if not isinstance(benchmark_task_run_id, int):
      raise TypeError('benchmark_task_run_id must be of type int')
    self._benchmark_task_run_id = benchmark_task_run_id


class ListBenchmarkTaskRunsFilter(KaggleObject):
  r"""
  Attributes:
    benchmark_version_identifier (BenchmarkVersionIdentifier)
      When filtering by a BenchmarkVersion, only the runs that pertain to the
      associated BenchmarkVersionModelMappings will be returned. This is
      especially useful/important for loading BenchmarkVersion-level pages.
    task_identifier (TaskIdentifier)
      When filtering by a Task, any results associated with the TaskVersion are
      returned (regardless of relationship with a Benchmark or any
      BenchmarkVersionModelMappings). This is especially useful/important for
      loading Task Detail pages.
    task_run_ids (int)
      When filtering by Task Run Ids, only the runs that with the specified ids
      will be returned.
  """

  def __init__(self):
    self._benchmark_version_identifier = None
    self._task_identifier = None
    self._task_run_ids = []
    self._freeze()

  @property
  def benchmark_version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    r"""
    When filtering by a BenchmarkVersion, only the runs that pertain to the
    associated BenchmarkVersionModelMappings will be returned. This is
    especially useful/important for loading BenchmarkVersion-level pages.
    """
    return self._benchmark_version_identifier or None

  @benchmark_version_identifier.setter
  def benchmark_version_identifier(self, benchmark_version_identifier: Optional['BenchmarkVersionIdentifier']):
    if benchmark_version_identifier is None:
      del self.benchmark_version_identifier
      return
    if not isinstance(benchmark_version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('benchmark_version_identifier must be of type BenchmarkVersionIdentifier')
    del self.task_identifier
    self._benchmark_version_identifier = benchmark_version_identifier

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    r"""
    When filtering by a Task, any results associated with the TaskVersion are
    returned (regardless of relationship with a Benchmark or any
    BenchmarkVersionModelMappings). This is especially useful/important for
    loading Task Detail pages.
    """
    return self._task_identifier or None

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    del self.benchmark_version_identifier
    self._task_identifier = task_identifier

  @property
  def task_run_ids(self) -> Optional[List[int]]:
    r"""
    When filtering by Task Run Ids, only the runs that with the specified ids
    will be returned.
    """
    return self._task_run_ids

  @task_run_ids.setter
  def task_run_ids(self, task_run_ids: Optional[List[int]]):
    if task_run_ids is None:
      del self.task_run_ids
      return
    if not isinstance(task_run_ids, list):
      raise TypeError('task_run_ids must be of type list')
    if not all([isinstance(t, int) for t in task_run_ids]):
      raise TypeError('task_run_ids must contain only items of type int')
    self._task_run_ids = task_run_ids


class ListBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  This handler only returns the most recent run for any (TaskVersion,
  ModelVersion) pair. If we need to be able to fetch the full history of
  runs, we can implement another field in ListBenchmarkTaskRunsFilter to toggle
  this behavior.

  Attributes:
    filter (ListBenchmarkTaskRunsFilter)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._filter = None
    self._read_mask = None
    self._freeze()

  @property
  def filter(self) -> Optional['ListBenchmarkTaskRunsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListBenchmarkTaskRunsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarkTaskRunsFilter):
      raise TypeError('filter must be of type ListBenchmarkTaskRunsFilter')
    self._filter = filter

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


class ListBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_task_runs (BenchmarkTaskRun)
    total_results (int)
  """

  def __init__(self):
    self._benchmark_task_runs = []
    self._total_results = 0
    self._freeze()

  @property
  def benchmark_task_runs(self) -> Optional[List[Optional['BenchmarkTaskRun']]]:
    return self._benchmark_task_runs

  @benchmark_task_runs.setter
  def benchmark_task_runs(self, benchmark_task_runs: Optional[List[Optional['BenchmarkTaskRun']]]):
    if benchmark_task_runs is None:
      del self.benchmark_task_runs
      return
    if not isinstance(benchmark_task_runs, list):
      raise TypeError('benchmark_task_runs must be of type list')
    if not all([isinstance(t, BenchmarkTaskRun) for t in benchmark_task_runs]):
      raise TypeError('benchmark_task_runs must contain only items of type BenchmarkTaskRun')
    self._benchmark_task_runs = benchmark_task_runs

  @property
  def total_results(self) -> int:
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results


BatchScheduleBenchmarkModelVersionResult._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runScheduled", "run_scheduled", "_run_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("runSkippedReason", "run_skipped_reason", "_run_skipped_reason", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
]

BatchScheduleBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("benchmarkTaskVersionIds", "benchmark_task_version_ids", "_benchmark_task_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("benchmarkModelVersionIds", "benchmark_model_version_ids", "_benchmark_model_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BatchScheduleBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("results", "results", "_results", BatchScheduleBenchmarkModelVersionResult, [], ListSerializer(KaggleObjectSerializer())),
]

CreateBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("benchmarkTaskRuns", "benchmark_task_runs", "_benchmark_task_runs", BenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
]

CreateBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("benchmarkTaskRuns", "benchmark_task_runs", "_benchmark_task_runs", BenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
]

DeleteBenchmarkTaskRunRequest._fields = [
  FieldMetadata("benchmarkTaskRunId", "benchmark_task_run_id", "_benchmark_task_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
]

GetBenchmarkTaskRunRequest._fields = [
  FieldMetadata("benchmarkTaskRunId", "benchmark_task_run_id", "_benchmark_task_run_id", int, 0, PredefinedSerializer()),
]

ListBenchmarkTaskRunsFilter._fields = [
  FieldMetadata("benchmarkVersionIdentifier", "benchmark_version_identifier", "_benchmark_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("taskRunIds", "task_run_ids", "_task_run_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListBenchmarkTaskRunsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("benchmarkTaskRuns", "benchmark_task_runs", "_benchmark_task_runs", BenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
]

