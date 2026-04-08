from kagglesdk.kaggle_object import *
from typing import Optional

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


BatchScheduleBenchmarkModelVersionResult._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runScheduled", "run_scheduled", "_run_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("runSkippedReason", "run_skipped_reason", "_run_skipped_reason", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
]

