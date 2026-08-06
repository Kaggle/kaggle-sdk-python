from kagglesdk.kaggle_object import *
from typing import List, Optional

class ListBenchmarkVersionAgentMappingsFilter(KaggleObject):
  r"""
  Attributes:
    parent_benchmark_version_ids (int)
      If set, only return mappings whose parent BenchmarkVersionId is in this
      list.
    child_agent_ids (int)
      If set, only return mappings whose child AgentId is in this list.
  """

  def __init__(self):
    self._parent_benchmark_version_ids = []
    self._child_agent_ids = []
    self._freeze()

  @property
  def parent_benchmark_version_ids(self) -> Optional[List[int]]:
    r"""
    If set, only return mappings whose parent BenchmarkVersionId is in this
    list.
    """
    return self._parent_benchmark_version_ids

  @parent_benchmark_version_ids.setter
  def parent_benchmark_version_ids(self, parent_benchmark_version_ids: Optional[List[int]]):
    if parent_benchmark_version_ids is None:
      del self.parent_benchmark_version_ids
      return
    if not isinstance(parent_benchmark_version_ids, list):
      raise TypeError('parent_benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in parent_benchmark_version_ids]):
      raise TypeError('parent_benchmark_version_ids must contain only items of type int')
    self._parent_benchmark_version_ids = parent_benchmark_version_ids

  @property
  def child_agent_ids(self) -> Optional[List[int]]:
    """If set, only return mappings whose child AgentId is in this list."""
    return self._child_agent_ids

  @child_agent_ids.setter
  def child_agent_ids(self, child_agent_ids: Optional[List[int]]):
    if child_agent_ids is None:
      del self.child_agent_ids
      return
    if not isinstance(child_agent_ids, list):
      raise TypeError('child_agent_ids must be of type list')
    if not all([isinstance(t, int) for t in child_agent_ids]):
      raise TypeError('child_agent_ids must contain only items of type int')
    self._child_agent_ids = child_agent_ids


ListBenchmarkVersionAgentMappingsFilter._fields = [
  FieldMetadata("parentBenchmarkVersionIds", "parent_benchmark_version_ids", "_parent_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("childAgentIds", "child_agent_ids", "_child_agent_ids", int, [], ListSerializer(PredefinedSerializer())),
]

