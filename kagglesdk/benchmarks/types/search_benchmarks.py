from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkType
from kagglesdk.kaggle_object import *
from typing import Optional

class SearchBenchmarksDocument(KaggleObject):
  r"""
  Attributes:
    type (BenchmarkType)
    current_published_version_number (int)
    current_draft_version_number (int)
    current_published_version_description (str)
    current_draft_version_description (str)
    current_published_version_name (str)
    current_draft_version_name (str)
    current_published_version_task_count (int)
      Number of tasks associated with the current published version (via task version mappings)
    current_published_version_model_count (int)
      Number of models associated with the current published version (via model version mappings)
    current_published_version_benchmark_count (int)
      Number of child benchmarks in the current published version (only populated for suite type benchmarks)
  """

  def __init__(self):
    self._type = BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED
    self._current_published_version_number = 0
    self._current_draft_version_number = 0
    self._current_published_version_description = ""
    self._current_draft_version_description = ""
    self._current_published_version_name = ""
    self._current_draft_version_name = ""
    self._current_published_version_task_count = 0
    self._current_published_version_model_count = 0
    self._current_published_version_benchmark_count = 0
    self._freeze()

  @property
  def type(self) -> 'BenchmarkType':
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkType):
      raise TypeError('type must be of type BenchmarkType')
    self._type = type

  @property
  def current_published_version_number(self) -> int:
    return self._current_published_version_number

  @current_published_version_number.setter
  def current_published_version_number(self, current_published_version_number: int):
    if current_published_version_number is None:
      del self.current_published_version_number
      return
    if not isinstance(current_published_version_number, int):
      raise TypeError('current_published_version_number must be of type int')
    self._current_published_version_number = current_published_version_number

  @property
  def current_draft_version_number(self) -> int:
    return self._current_draft_version_number

  @current_draft_version_number.setter
  def current_draft_version_number(self, current_draft_version_number: int):
    if current_draft_version_number is None:
      del self.current_draft_version_number
      return
    if not isinstance(current_draft_version_number, int):
      raise TypeError('current_draft_version_number must be of type int')
    self._current_draft_version_number = current_draft_version_number

  @property
  def current_published_version_description(self) -> str:
    return self._current_published_version_description

  @current_published_version_description.setter
  def current_published_version_description(self, current_published_version_description: str):
    if current_published_version_description is None:
      del self.current_published_version_description
      return
    if not isinstance(current_published_version_description, str):
      raise TypeError('current_published_version_description must be of type str')
    self._current_published_version_description = current_published_version_description

  @property
  def current_draft_version_description(self) -> str:
    return self._current_draft_version_description

  @current_draft_version_description.setter
  def current_draft_version_description(self, current_draft_version_description: str):
    if current_draft_version_description is None:
      del self.current_draft_version_description
      return
    if not isinstance(current_draft_version_description, str):
      raise TypeError('current_draft_version_description must be of type str')
    self._current_draft_version_description = current_draft_version_description

  @property
  def current_published_version_name(self) -> str:
    return self._current_published_version_name

  @current_published_version_name.setter
  def current_published_version_name(self, current_published_version_name: str):
    if current_published_version_name is None:
      del self.current_published_version_name
      return
    if not isinstance(current_published_version_name, str):
      raise TypeError('current_published_version_name must be of type str')
    self._current_published_version_name = current_published_version_name

  @property
  def current_draft_version_name(self) -> str:
    return self._current_draft_version_name

  @current_draft_version_name.setter
  def current_draft_version_name(self, current_draft_version_name: str):
    if current_draft_version_name is None:
      del self.current_draft_version_name
      return
    if not isinstance(current_draft_version_name, str):
      raise TypeError('current_draft_version_name must be of type str')
    self._current_draft_version_name = current_draft_version_name

  @property
  def current_published_version_task_count(self) -> int:
    """Number of tasks associated with the current published version (via task version mappings)"""
    return self._current_published_version_task_count

  @current_published_version_task_count.setter
  def current_published_version_task_count(self, current_published_version_task_count: int):
    if current_published_version_task_count is None:
      del self.current_published_version_task_count
      return
    if not isinstance(current_published_version_task_count, int):
      raise TypeError('current_published_version_task_count must be of type int')
    self._current_published_version_task_count = current_published_version_task_count

  @property
  def current_published_version_model_count(self) -> int:
    """Number of models associated with the current published version (via model version mappings)"""
    return self._current_published_version_model_count

  @current_published_version_model_count.setter
  def current_published_version_model_count(self, current_published_version_model_count: int):
    if current_published_version_model_count is None:
      del self.current_published_version_model_count
      return
    if not isinstance(current_published_version_model_count, int):
      raise TypeError('current_published_version_model_count must be of type int')
    self._current_published_version_model_count = current_published_version_model_count

  @property
  def current_published_version_benchmark_count(self) -> int:
    """Number of child benchmarks in the current published version (only populated for suite type benchmarks)"""
    return self._current_published_version_benchmark_count

  @current_published_version_benchmark_count.setter
  def current_published_version_benchmark_count(self, current_published_version_benchmark_count: int):
    if current_published_version_benchmark_count is None:
      del self.current_published_version_benchmark_count
      return
    if not isinstance(current_published_version_benchmark_count, int):
      raise TypeError('current_published_version_benchmark_count must be of type int')
    self._current_published_version_benchmark_count = current_published_version_benchmark_count


SearchBenchmarksDocument._fields = [
  FieldMetadata("type", "type", "_type", BenchmarkType, BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("currentPublishedVersionNumber", "current_published_version_number", "_current_published_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("currentDraftVersionNumber", "current_draft_version_number", "_current_draft_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("currentPublishedVersionDescription", "current_published_version_description", "_current_published_version_description", str, "", PredefinedSerializer()),
  FieldMetadata("currentDraftVersionDescription", "current_draft_version_description", "_current_draft_version_description", str, "", PredefinedSerializer()),
  FieldMetadata("currentPublishedVersionName", "current_published_version_name", "_current_published_version_name", str, "", PredefinedSerializer()),
  FieldMetadata("currentDraftVersionName", "current_draft_version_name", "_current_draft_version_name", str, "", PredefinedSerializer()),
  FieldMetadata("currentPublishedVersionTaskCount", "current_published_version_task_count", "_current_published_version_task_count", int, 0, PredefinedSerializer()),
  FieldMetadata("currentPublishedVersionModelCount", "current_published_version_model_count", "_current_published_version_model_count", int, 0, PredefinedSerializer()),
  FieldMetadata("currentPublishedVersionBenchmarkCount", "current_published_version_benchmark_count", "_current_published_version_benchmark_count", int, 0, PredefinedSerializer()),
]

