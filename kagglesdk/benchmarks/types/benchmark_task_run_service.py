from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkCandidateType
from kagglesdk.kaggle_object import *
from typing import Optional

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
      When the requested benchmark_task_version_id is a child of another task
      version, scheduling is redirected to the parent and this field reports the
      parent's id. Unset when the requested task version was executed directly.
    agent_id (int)
      One of the values provided in
      BatchScheduleBenchmarkTaskRunsRequest.benchmark_agent_ids
    candidate_type (BenchmarkCandidateType)
      Specifies the candidate type that was scheduled (ModelVersion vs. Agent)
  """

  def __init__(self):
    self._benchmark_model_version_id = 0
    self._run_scheduled = False
    self._run_skipped_reason = None
    self._benchmark_task_version_id = 0
    self._parent_task_version_id = None
    self._agent_id = 0
    self._candidate_type = BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED
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
    When the requested benchmark_task_version_id is a child of another task
    version, scheduling is redirected to the parent and this field reports the
    parent's id. Unset when the requested task version was executed directly.
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


BatchScheduleBenchmarkModelVersionResult._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runScheduled", "run_scheduled", "_run_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("runSkippedReason", "run_skipped_reason", "_run_skipped_reason", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentTaskVersionId", "parent_task_version_id", "_parent_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentId", "agent_id", "_agent_id", int, 0, PredefinedSerializer()),
  FieldMetadata("candidateType", "candidate_type", "_candidate_type", BenchmarkCandidateType, BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED, EnumSerializer()),
]

