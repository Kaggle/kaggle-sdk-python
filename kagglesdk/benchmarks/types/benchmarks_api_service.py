from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkModel, BenchmarkResult
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ApiBenchmarkLeaderboard(KaggleObject):
  r"""
  Attributes:
    rows (ApiBenchmarkLeaderboard.LeaderboardRow)
  """

  class LeaderboardRow(KaggleObject):
    r"""
    Attributes:
      model_version_name (str)
      model_version_slug (str)
      task_results (ApiBenchmarkLeaderboard.TaskResult)
    """

    def __init__(self):
      self._model_version_name = ""
      self._model_version_slug = ""
      self._task_results = []
      self._freeze()

    @property
    def model_version_name(self) -> str:
      return self._model_version_name

    @model_version_name.setter
    def model_version_name(self, model_version_name: str):
      if model_version_name is None:
        del self.model_version_name
        return
      if not isinstance(model_version_name, str):
        raise TypeError('model_version_name must be of type str')
      self._model_version_name = model_version_name

    @property
    def model_version_slug(self) -> str:
      return self._model_version_slug

    @model_version_slug.setter
    def model_version_slug(self, model_version_slug: str):
      if model_version_slug is None:
        del self.model_version_slug
        return
      if not isinstance(model_version_slug, str):
        raise TypeError('model_version_slug must be of type str')
      self._model_version_slug = model_version_slug

    @property
    def task_results(self) -> Optional[List[Optional['ApiBenchmarkLeaderboard.TaskResult']]]:
      return self._task_results

    @task_results.setter
    def task_results(self, task_results: Optional[List[Optional['ApiBenchmarkLeaderboard.TaskResult']]]):
      if task_results is None:
        del self.task_results
        return
      if not isinstance(task_results, list):
        raise TypeError('task_results must be of type list')
      if not all([isinstance(t, ApiBenchmarkLeaderboard.TaskResult) for t in task_results]):
        raise TypeError('task_results must contain only items of type ApiBenchmarkLeaderboard.TaskResult')
      self._task_results = task_results


  class TaskResult(KaggleObject):
    r"""
    Attributes:
      benchmark_task_name (str)
      benchmark_task_slug (str)
      task_version (int)
      result (BenchmarkResult)
    """

    def __init__(self):
      self._benchmark_task_name = ""
      self._benchmark_task_slug = ""
      self._task_version = 0
      self._result = None
      self._freeze()

    @property
    def benchmark_task_name(self) -> str:
      return self._benchmark_task_name

    @benchmark_task_name.setter
    def benchmark_task_name(self, benchmark_task_name: str):
      if benchmark_task_name is None:
        del self.benchmark_task_name
        return
      if not isinstance(benchmark_task_name, str):
        raise TypeError('benchmark_task_name must be of type str')
      self._benchmark_task_name = benchmark_task_name

    @property
    def benchmark_task_slug(self) -> str:
      return self._benchmark_task_slug

    @benchmark_task_slug.setter
    def benchmark_task_slug(self, benchmark_task_slug: str):
      if benchmark_task_slug is None:
        del self.benchmark_task_slug
        return
      if not isinstance(benchmark_task_slug, str):
        raise TypeError('benchmark_task_slug must be of type str')
      self._benchmark_task_slug = benchmark_task_slug

    @property
    def task_version(self) -> int:
      return self._task_version

    @task_version.setter
    def task_version(self, task_version: int):
      if task_version is None:
        del self.task_version
        return
      if not isinstance(task_version, int):
        raise TypeError('task_version must be of type int')
      self._task_version = task_version

    @property
    def result(self) -> Optional['BenchmarkResult']:
      return self._result

    @result.setter
    def result(self, result: Optional['BenchmarkResult']):
      if result is None:
        del self.result
        return
      if not isinstance(result, BenchmarkResult):
        raise TypeError('result must be of type BenchmarkResult')
      self._result = result


  def __init__(self):
    self._rows = []
    self._freeze()

  @property
  def rows(self) -> Optional[List[Optional['ApiBenchmarkLeaderboard.LeaderboardRow']]]:
    return self._rows

  @rows.setter
  def rows(self, rows: Optional[List[Optional['ApiBenchmarkLeaderboard.LeaderboardRow']]]):
    if rows is None:
      del self.rows
      return
    if not isinstance(rows, list):
      raise TypeError('rows must be of type list')
    if not all([isinstance(t, ApiBenchmarkLeaderboard.LeaderboardRow) for t in rows]):
      raise TypeError('rows must contain only items of type ApiBenchmarkLeaderboard.LeaderboardRow')
    self._rows = rows


class ApiGetBenchmarkLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    benchmark_slug (str)
    version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._benchmark_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    return self._benchmark_slug

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: str):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug

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

  def endpoint(self):
    if self.version_number:
      path = '/api/v1/benchmarks/{owner_slug}/{benchmark_slug}/versions/{version_number}/leaderboard'
    else:
      path = '/api/v1/benchmarks/{owner_slug}/{benchmark_slug}/leaderboard'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/{owner_slug}/{benchmark_slug}/leaderboard'


class ApiListBenchmarkModelsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = ""
    self._read_mask = None
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

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

  def endpoint(self):
    path = '/api/v1/benchmarks/models'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkModelsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_models (BenchmarkModel)
      NOTE: This reuses the internal BenchmarkModel directly. If BenchmarkModel
      ever gets fields that shouldn't be public, introduce a dedicated API type.
    next_page_token (str)
  """

  def __init__(self):
    self._benchmark_models = []
    self._next_page_token = None
    self._freeze()

  @property
  def benchmark_models(self) -> Optional[List[Optional['BenchmarkModel']]]:
    r"""
    NOTE: This reuses the internal BenchmarkModel directly. If BenchmarkModel
    ever gets fields that shouldn't be public, introduce a dedicated API type.
    """
    return self._benchmark_models

  @benchmark_models.setter
  def benchmark_models(self, benchmark_models: Optional[List[Optional['BenchmarkModel']]]):
    if benchmark_models is None:
      del self.benchmark_models
      return
    if not isinstance(benchmark_models, list):
      raise TypeError('benchmark_models must be of type list')
    if not all([isinstance(t, BenchmarkModel) for t in benchmark_models]):
      raise TypeError('benchmark_models must contain only items of type BenchmarkModel')
    self._benchmark_models = benchmark_models

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

  @property
  def benchmarkModels(self):
    return self.benchmark_models

  @property
  def nextPageToken(self):
    return self.next_page_token


ApiBenchmarkLeaderboard.LeaderboardRow._fields = [
  FieldMetadata("modelVersionName", "model_version_name", "_model_version_name", str, "", PredefinedSerializer()),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("taskResults", "task_results", "_task_results", ApiBenchmarkLeaderboard.TaskResult, [], ListSerializer(KaggleObjectSerializer())),
]

ApiBenchmarkLeaderboard.TaskResult._fields = [
  FieldMetadata("benchmarkTaskName", "benchmark_task_name", "_benchmark_task_name", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkTaskSlug", "benchmark_task_slug", "_benchmark_task_slug", str, "", PredefinedSerializer()),
  FieldMetadata("taskVersion", "task_version", "_task_version", int, 0, PredefinedSerializer()),
  FieldMetadata("result", "result", "_result", BenchmarkResult, None, KaggleObjectSerializer()),
]

ApiBenchmarkLeaderboard._fields = [
  FieldMetadata("rows", "rows", "_rows", ApiBenchmarkLeaderboard.LeaderboardRow, [], ListSerializer(KaggleObjectSerializer())),
]

ApiGetBenchmarkLeaderboardRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiListBenchmarkModelsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ApiListBenchmarkModelsResponse._fields = [
  FieldMetadata("benchmarkModels", "benchmark_models", "_benchmark_models", BenchmarkModel, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

