from kagglesdk.kaggle_object import *
from typing import List, Optional

class ListAgentsFilter(KaggleObject):
  r"""
  Attributes:
    agent_ids (int)
      Restrict to Agents with the given ids.
    benchmark_model_version_config_ids (int)
      Restrict to Agents whose BenchmarkModelVersionConfig has the given ids.
    harness_version_ids (int)
      Restrict to Agents whose HarnessVersion has the given ids.
  """

  def __init__(self):
    self._agent_ids = []
    self._benchmark_model_version_config_ids = []
    self._harness_version_ids = []
    self._freeze()

  @property
  def agent_ids(self) -> Optional[List[int]]:
    """Restrict to Agents with the given ids."""
    return self._agent_ids

  @agent_ids.setter
  def agent_ids(self, agent_ids: Optional[List[int]]):
    if agent_ids is None:
      del self.agent_ids
      return
    if not isinstance(agent_ids, list):
      raise TypeError('agent_ids must be of type list')
    if not all([isinstance(t, int) for t in agent_ids]):
      raise TypeError('agent_ids must contain only items of type int')
    self._agent_ids = agent_ids

  @property
  def benchmark_model_version_config_ids(self) -> Optional[List[int]]:
    """Restrict to Agents whose BenchmarkModelVersionConfig has the given ids."""
    return self._benchmark_model_version_config_ids

  @benchmark_model_version_config_ids.setter
  def benchmark_model_version_config_ids(self, benchmark_model_version_config_ids: Optional[List[int]]):
    if benchmark_model_version_config_ids is None:
      del self.benchmark_model_version_config_ids
      return
    if not isinstance(benchmark_model_version_config_ids, list):
      raise TypeError('benchmark_model_version_config_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_model_version_config_ids]):
      raise TypeError('benchmark_model_version_config_ids must contain only items of type int')
    self._benchmark_model_version_config_ids = benchmark_model_version_config_ids

  @property
  def harness_version_ids(self) -> Optional[List[int]]:
    """Restrict to Agents whose HarnessVersion has the given ids."""
    return self._harness_version_ids

  @harness_version_ids.setter
  def harness_version_ids(self, harness_version_ids: Optional[List[int]]):
    if harness_version_ids is None:
      del self.harness_version_ids
      return
    if not isinstance(harness_version_ids, list):
      raise TypeError('harness_version_ids must be of type list')
    if not all([isinstance(t, int) for t in harness_version_ids]):
      raise TypeError('harness_version_ids must contain only items of type int')
    self._harness_version_ids = harness_version_ids


class ListHarnessesFilter(KaggleObject):
  r"""
  Attributes:
    harness_ids (int)
      Restrict to Harnesses with the given ids.
    latest_version_per_harness_only (bool)
      If true, collapse to a single row per Harness carrying only its latest
      (highest-id) HarnessVersion. Useful for selectors that only need the
      current version per Harness.
  """

  def __init__(self):
    self._harness_ids = []
    self._latest_version_per_harness_only = None
    self._freeze()

  @property
  def harness_ids(self) -> Optional[List[int]]:
    """Restrict to Harnesses with the given ids."""
    return self._harness_ids

  @harness_ids.setter
  def harness_ids(self, harness_ids: Optional[List[int]]):
    if harness_ids is None:
      del self.harness_ids
      return
    if not isinstance(harness_ids, list):
      raise TypeError('harness_ids must be of type list')
    if not all([isinstance(t, int) for t in harness_ids]):
      raise TypeError('harness_ids must contain only items of type int')
    self._harness_ids = harness_ids

  @property
  def latest_version_per_harness_only(self) -> bool:
    r"""
    If true, collapse to a single row per Harness carrying only its latest
    (highest-id) HarnessVersion. Useful for selectors that only need the
    current version per Harness.
    """
    return self._latest_version_per_harness_only or False

  @latest_version_per_harness_only.setter
  def latest_version_per_harness_only(self, latest_version_per_harness_only: Optional[bool]):
    if latest_version_per_harness_only is None:
      del self.latest_version_per_harness_only
      return
    if not isinstance(latest_version_per_harness_only, bool):
      raise TypeError('latest_version_per_harness_only must be of type bool')
    self._latest_version_per_harness_only = latest_version_per_harness_only


ListAgentsFilter._fields = [
  FieldMetadata("agentIds", "agent_ids", "_agent_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("benchmarkModelVersionConfigIds", "benchmark_model_version_config_ids", "_benchmark_model_version_config_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("harnessVersionIds", "harness_version_ids", "_harness_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListHarnessesFilter._fields = [
  FieldMetadata("harnessIds", "harness_ids", "_harness_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("latestVersionPerHarnessOnly", "latest_version_per_harness_only", "_latest_version_per_harness_only", bool, None, PredefinedSerializer(), optional=True),
]

