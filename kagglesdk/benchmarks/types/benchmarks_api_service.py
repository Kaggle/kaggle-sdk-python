from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkVersionAgentMappingType
from kagglesdk.benchmarks.types.benchmark_service import ListBenchmarkVersionAgentMappingsFilter
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


class ApiBenchmarkModelVersionConfig(KaggleObject):
  r"""
  API equivalent of BenchmarkModelVersionConfig from benchmark_types.proto:
  a fully-configured, runnable BenchmarkModelVersion (which LLM + all its
  sampling parameters).

  Attributes:
    id (int)
      Output-only on create.
    benchmark_model_version_id (int)
      The BenchmarkModelVersion (i.e. the LLM) being configured.
    display_name (str)
      ex: 'Claude Opus 4.8 High Reasoning Effort'.
    slug (str)
      ex: 'claude-opus-4.8-high-reasoning-effort'.
    reasoning_effort (str)
  """

  def __init__(self):
    self._id = 0
    self._benchmark_model_version_id = 0
    self._display_name = ""
    self._slug = ""
    self._reasoning_effort = ""
    self._freeze()

  @property
  def id(self) -> int:
    """Output-only on create."""
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
  def benchmark_model_version_id(self) -> int:
    """The BenchmarkModelVersion (i.e. the LLM) being configured."""
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
  def display_name(self) -> str:
    """ex: 'Claude Opus 4.8 High Reasoning Effort'."""
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
  def slug(self) -> str:
    """ex: 'claude-opus-4.8-high-reasoning-effort'."""
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def reasoning_effort(self) -> str:
    return self._reasoning_effort

  @reasoning_effort.setter
  def reasoning_effort(self, reasoning_effort: str):
    if reasoning_effort is None:
      del self.reasoning_effort
      return
    if not isinstance(reasoning_effort, str):
      raise TypeError('reasoning_effort must be of type str')
    self._reasoning_effort = reasoning_effort


class ApiBenchmarkVersionAgentMapping(KaggleObject):
  r"""
  API equivalent of BenchmarkVersionAgentMapping from benchmark_types.proto.

  Attributes:
    id (int)
      Output-only on create.
    parent_benchmark_version_id (int)
      The parent benchmark version to map to.
    child_agent_id (int)
      The agent to map.
    type (BenchmarkVersionAgentMappingType)
      The mapping type.
  """

  def __init__(self):
    self._id = 0
    self._parent_benchmark_version_id = 0
    self._child_agent_id = 0
    self._type = BenchmarkVersionAgentMappingType.BENCHMARK_VERSION_AGENT_MAPPING_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    """Output-only on create."""
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
  def parent_benchmark_version_id(self) -> int:
    """The parent benchmark version to map to."""
    return self._parent_benchmark_version_id

  @parent_benchmark_version_id.setter
  def parent_benchmark_version_id(self, parent_benchmark_version_id: int):
    if parent_benchmark_version_id is None:
      del self.parent_benchmark_version_id
      return
    if not isinstance(parent_benchmark_version_id, int):
      raise TypeError('parent_benchmark_version_id must be of type int')
    self._parent_benchmark_version_id = parent_benchmark_version_id

  @property
  def child_agent_id(self) -> int:
    """The agent to map."""
    return self._child_agent_id

  @child_agent_id.setter
  def child_agent_id(self, child_agent_id: int):
    if child_agent_id is None:
      del self.child_agent_id
      return
    if not isinstance(child_agent_id, int):
      raise TypeError('child_agent_id must be of type int')
    self._child_agent_id = child_agent_id

  @property
  def type(self) -> 'BenchmarkVersionAgentMappingType':
    """The mapping type."""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkVersionAgentMappingType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkVersionAgentMappingType):
      raise TypeError('type must be of type BenchmarkVersionAgentMappingType')
    self._type = type


class ApiCreateBenchmarkModelVersionConfigRequest(KaggleObject):
  r"""
  Attributes:
    config (ApiBenchmarkModelVersionConfig)
      The config to create.
  """

  def __init__(self):
    self._config = None
    self._freeze()

  @property
  def config(self) -> Optional['ApiBenchmarkModelVersionConfig']:
    """The config to create."""
    return self._config

  @config.setter
  def config(self, config: Optional['ApiBenchmarkModelVersionConfig']):
    if config is None:
      del self.config
      return
    if not isinstance(config, ApiBenchmarkModelVersionConfig):
      raise TypeError('config must be of type ApiBenchmarkModelVersionConfig')
    self._config = config

  def endpoint(self):
    path = '/api/v1/benchmarks/models/versions/configs/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateBenchmarkVersionAgentMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (ApiBenchmarkVersionAgentMapping)
      Mappings to create. Must be non-empty.
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]:
    """Mappings to create. Must be non-empty."""
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, ApiBenchmarkVersionAgentMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type ApiBenchmarkVersionAgentMapping')
    self._mappings = mappings

  def endpoint(self):
    path = '/api/v1/benchmarks/versions/agent-mappings/create'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateBenchmarkVersionAgentMappingsResponse(KaggleObject):
  r"""
  Attributes:
    mappings (ApiBenchmarkVersionAgentMapping)
      The created (or revived) mappings, in request order.
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]:
    """The created (or revived) mappings, in request order."""
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, ApiBenchmarkVersionAgentMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type ApiBenchmarkVersionAgentMapping')
    self._mappings = mappings


class ApiDeleteBenchmarkVersionAgentMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (ApiBenchmarkVersionAgentMapping)
      Mappings to soft-delete, identified by the
      (parent_benchmark_version_id, child_agent_id) pair; other fields are
      ignored. Must be non-empty.
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]:
    r"""
    Mappings to soft-delete, identified by the
    (parent_benchmark_version_id, child_agent_id) pair; other fields are
    ignored. Must be non-empty.
    """
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, ApiBenchmarkVersionAgentMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type ApiBenchmarkVersionAgentMapping')
    self._mappings = mappings

  def endpoint(self):
    path = '/api/v1/benchmarks/versions/agent-mappings/delete'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiDeleteBenchmarkVersionAgentMappingsResponse(KaggleObject):
  r"""
  Attributes:
    deleted_mappings_count (int)
  """

  def __init__(self):
    self._deleted_mappings_count = 0
    self._freeze()

  @property
  def deleted_mappings_count(self) -> int:
    return self._deleted_mappings_count

  @deleted_mappings_count.setter
  def deleted_mappings_count(self, deleted_mappings_count: int):
    if deleted_mappings_count is None:
      del self.deleted_mappings_count
      return
    if not isinstance(deleted_mappings_count, int):
      raise TypeError('deleted_mappings_count must be of type int')
    self._deleted_mappings_count = deleted_mappings_count

  @property
  def deletedMappingsCount(self):
    return self.deleted_mappings_count


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


class ApiGetBenchmarkModelVersionConfigRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the config to fetch.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the config to fetch."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  def endpoint(self):
    path = '/api/v1/benchmarks/models/versions/configs/{id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/models/versions/configs/{id}'


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


class ApiListBenchmarkModelVersionConfigsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version_ids (int)
      If set, only return configs whose parent BenchmarkModelVersionId is in
      this list.
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._benchmark_model_version_ids = []
    self._page_size = 0
    self._page_token = ""
    self._freeze()

  @property
  def benchmark_model_version_ids(self) -> Optional[List[int]]:
    r"""
    If set, only return configs whose parent BenchmarkModelVersionId is in
    this list.
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

  def endpoint(self):
    path = '/api/v1/benchmarks/models/versions/configs/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkModelVersionConfigsResponse(KaggleObject):
  r"""
  Attributes:
    configs (ApiBenchmarkModelVersionConfig)
    next_page_token (str)
  """

  def __init__(self):
    self._configs = []
    self._next_page_token = None
    self._freeze()

  @property
  def configs(self) -> Optional[List[Optional['ApiBenchmarkModelVersionConfig']]]:
    return self._configs

  @configs.setter
  def configs(self, configs: Optional[List[Optional['ApiBenchmarkModelVersionConfig']]]):
    if configs is None:
      del self.configs
      return
    if not isinstance(configs, list):
      raise TypeError('configs must be of type list')
    if not all([isinstance(t, ApiBenchmarkModelVersionConfig) for t in configs]):
      raise TypeError('configs must contain only items of type ApiBenchmarkModelVersionConfig')
    self._configs = configs

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
  def nextPageToken(self):
    return self.next_page_token


class ApiListBenchmarkVersionAgentMappingsRequest(KaggleObject):
  r"""
  Attributes:
    filter (ListBenchmarkVersionAgentMappingsFilter)
    page_size (int)
    page_token (str)
  """

  def __init__(self):
    self._filter = None
    self._page_size = 0
    self._page_token = ""
    self._freeze()

  @property
  def filter(self) -> Optional['ListBenchmarkVersionAgentMappingsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListBenchmarkVersionAgentMappingsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarkVersionAgentMappingsFilter):
      raise TypeError('filter must be of type ListBenchmarkVersionAgentMappingsFilter')
    self._filter = filter

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

  def endpoint(self):
    path = '/api/v1/benchmarks/versions/agent-mappings/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkVersionAgentMappingsResponse(KaggleObject):
  r"""
  Attributes:
    mappings (ApiBenchmarkVersionAgentMapping)
    next_page_token (str)
  """

  def __init__(self):
    self._mappings = []
    self._next_page_token = None
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]:
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['ApiBenchmarkVersionAgentMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, ApiBenchmarkVersionAgentMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type ApiBenchmarkVersionAgentMapping')
    self._mappings = mappings

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

ApiBenchmarkModelVersionConfig._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("reasoningEffort", "reasoning_effort", "_reasoning_effort", str, "", PredefinedSerializer()),
]

ApiBenchmarkVersionAgentMapping._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentBenchmarkVersionId", "parent_benchmark_version_id", "_parent_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childAgentId", "child_agent_id", "_child_agent_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkVersionAgentMappingType, BenchmarkVersionAgentMappingType.BENCHMARK_VERSION_AGENT_MAPPING_TYPE_UNSPECIFIED, EnumSerializer()),
]

ApiCreateBenchmarkModelVersionConfigRequest._fields = [
  FieldMetadata("config", "config", "_config", ApiBenchmarkModelVersionConfig, None, KaggleObjectSerializer()),
]

ApiCreateBenchmarkVersionAgentMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", ApiBenchmarkVersionAgentMapping, [], ListSerializer(KaggleObjectSerializer())),
]

ApiCreateBenchmarkVersionAgentMappingsResponse._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", ApiBenchmarkVersionAgentMapping, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDeleteBenchmarkVersionAgentMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", ApiBenchmarkVersionAgentMapping, [], ListSerializer(KaggleObjectSerializer())),
]

ApiDeleteBenchmarkVersionAgentMappingsResponse._fields = [
  FieldMetadata("deletedMappingsCount", "deleted_mappings_count", "_deleted_mappings_count", int, 0, PredefinedSerializer()),
]

ApiGetBenchmarkLeaderboardRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiGetBenchmarkModelVersionConfigRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
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

ApiListBenchmarkModelVersionConfigsRequest._fields = [
  FieldMetadata("benchmarkModelVersionIds", "benchmark_model_version_ids", "_benchmark_model_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ApiListBenchmarkModelVersionConfigsResponse._fields = [
  FieldMetadata("configs", "configs", "_configs", ApiBenchmarkModelVersionConfig, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ApiListBenchmarkVersionAgentMappingsRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListBenchmarkVersionAgentMappingsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ApiListBenchmarkVersionAgentMappingsResponse._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", ApiBenchmarkVersionAgentMapping, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

