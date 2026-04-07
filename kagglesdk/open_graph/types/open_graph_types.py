from datetime import datetime
import enum
from kagglesdk.benchmarks.types.benchmark_types import Benchmark, BenchmarkLeaderboard, BenchmarkVersion, UnifiedBenchmarkLeaderboard
from kagglesdk.kaggle_object import *
from typing import Optional

class OpenGraphResourceType(enum.Enum):
  UNSPECIFIED = 0
  RESEARCH_BENCHMARKS = 1
  """Individual and Suite Benchmarks"""
  PERSONAL_BENCHMARKS = 2
  """Personal Benchmarks"""
  GAME_ARENA_BENCHMARKS = 3
  """Game Arena Benchmarks"""

class BenchmarkLeaderboardMetadata(KaggleObject):
  r"""
  Attributes:
    benchmark (Benchmark)
      Benchmark
    benchmark_leaderboard (UnifiedBenchmarkLeaderboard)
      Benchmark leaderboard data
  """

  def __init__(self):
    self._benchmark = None
    self._benchmark_leaderboard = None
    self._freeze()

  @property
  def benchmark(self) -> Optional['Benchmark']:
    """Benchmark"""
    return self._benchmark

  @benchmark.setter
  def benchmark(self, benchmark: Optional['Benchmark']):
    if benchmark is None:
      del self.benchmark
      return
    if not isinstance(benchmark, Benchmark):
      raise TypeError('benchmark must be of type Benchmark')
    self._benchmark = benchmark

  @property
  def benchmark_leaderboard(self) -> Optional['UnifiedBenchmarkLeaderboard']:
    """Benchmark leaderboard data"""
    return self._benchmark_leaderboard

  @benchmark_leaderboard.setter
  def benchmark_leaderboard(self, benchmark_leaderboard: Optional['UnifiedBenchmarkLeaderboard']):
    if benchmark_leaderboard is None:
      del self.benchmark_leaderboard
      return
    if not isinstance(benchmark_leaderboard, UnifiedBenchmarkLeaderboard):
      raise TypeError('benchmark_leaderboard must be of type UnifiedBenchmarkLeaderboard')
    self._benchmark_leaderboard = benchmark_leaderboard


class OpenGraphImageMetadata(KaggleObject):
  r"""
  Attributes:
    id (int)
    open_graph_resource_type (OpenGraphResourceType)
      Type of OpenGraph resource used to determine the screenshot style
    benchmark_id (int)
      Id of specific benchmark used to populate the screenshot
    benchmark_version_id (int)
      Id of specific benchmark version used to populate the screenshot
    url (str)
      GCS Url of the OpenGraph image
    create_time (datetime)
      Time when a new resource entity was created
    update_time (datetime)
      Time when an existing resource entity was updated
    research_benchmark_leaderboard_metadata (ResearchBenchmarkLeaderboardMetadata)
      TODO(b/455897477): Remove this field and prefer using the generic
      benchmark_leaderboard for all types of benchmarks Data used to render the
      Research Benchmark OpenGraph image
    benchmark_leaderboard_metadata (BenchmarkLeaderboardMetadata)
      Data used to render Benchmark OpenGraph image
    delete_time (datetime)
      Time when an existing resource entity was deleted
  """

  def __init__(self):
    self._id = 0
    self._open_graph_resource_type = OpenGraphResourceType.UNSPECIFIED
    self._benchmark_id = None
    self._benchmark_version_id = None
    self._url = None
    self._create_time = None
    self._update_time = None
    self._research_benchmark_leaderboard_metadata = None
    self._benchmark_leaderboard_metadata = None
    self._delete_time = None
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
  def open_graph_resource_type(self) -> 'OpenGraphResourceType':
    """Type of OpenGraph resource used to determine the screenshot style"""
    return self._open_graph_resource_type

  @open_graph_resource_type.setter
  def open_graph_resource_type(self, open_graph_resource_type: 'OpenGraphResourceType'):
    if open_graph_resource_type is None:
      del self.open_graph_resource_type
      return
    if not isinstance(open_graph_resource_type, OpenGraphResourceType):
      raise TypeError('open_graph_resource_type must be of type OpenGraphResourceType')
    self._open_graph_resource_type = open_graph_resource_type

  @property
  def benchmark_id(self) -> int:
    """Id of specific benchmark used to populate the screenshot"""
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
  def benchmark_version_id(self) -> int:
    """Id of specific benchmark version used to populate the screenshot"""
    return self._benchmark_version_id or 0

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: Optional[int]):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def url(self) -> str:
    """GCS Url of the OpenGraph image"""
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def create_time(self) -> datetime:
    """Time when a new resource entity was created"""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def update_time(self) -> datetime:
    """Time when an existing resource entity was updated"""
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def delete_time(self) -> datetime:
    """Time when an existing resource entity was deleted"""
    return self._delete_time

  @delete_time.setter
  def delete_time(self, delete_time: datetime):
    if delete_time is None:
      del self.delete_time
      return
    if not isinstance(delete_time, datetime):
      raise TypeError('delete_time must be of type datetime')
    self._delete_time = delete_time

  @property
  def research_benchmark_leaderboard_metadata(self) -> Optional['ResearchBenchmarkLeaderboardMetadata']:
    r"""
    TODO(b/455897477): Remove this field and prefer using the generic
    benchmark_leaderboard for all types of benchmarks Data used to render the
    Research Benchmark OpenGraph image
    """
    return self._research_benchmark_leaderboard_metadata or None

  @research_benchmark_leaderboard_metadata.setter
  def research_benchmark_leaderboard_metadata(self, research_benchmark_leaderboard_metadata: Optional[Optional['ResearchBenchmarkLeaderboardMetadata']]):
    if research_benchmark_leaderboard_metadata is None:
      del self.research_benchmark_leaderboard_metadata
      return
    if not isinstance(research_benchmark_leaderboard_metadata, ResearchBenchmarkLeaderboardMetadata):
      raise TypeError('research_benchmark_leaderboard_metadata must be of type ResearchBenchmarkLeaderboardMetadata')
    self._research_benchmark_leaderboard_metadata = research_benchmark_leaderboard_metadata

  @property
  def benchmark_leaderboard_metadata(self) -> Optional['BenchmarkLeaderboardMetadata']:
    """Data used to render Benchmark OpenGraph image"""
    return self._benchmark_leaderboard_metadata or None

  @benchmark_leaderboard_metadata.setter
  def benchmark_leaderboard_metadata(self, benchmark_leaderboard_metadata: Optional[Optional['BenchmarkLeaderboardMetadata']]):
    if benchmark_leaderboard_metadata is None:
      del self.benchmark_leaderboard_metadata
      return
    if not isinstance(benchmark_leaderboard_metadata, BenchmarkLeaderboardMetadata):
      raise TypeError('benchmark_leaderboard_metadata must be of type BenchmarkLeaderboardMetadata')
    self._benchmark_leaderboard_metadata = benchmark_leaderboard_metadata


class OpenGraphResource(KaggleObject):
  r"""
  Attributes:
    open_graph_resource_type (OpenGraphResourceType)
    entity_id (int)
    entity_version_id (int)
  """

  def __init__(self):
    self._open_graph_resource_type = OpenGraphResourceType.UNSPECIFIED
    self._entity_id = 0
    self._entity_version_id = None
    self._freeze()

  @property
  def open_graph_resource_type(self) -> 'OpenGraphResourceType':
    return self._open_graph_resource_type

  @open_graph_resource_type.setter
  def open_graph_resource_type(self, open_graph_resource_type: 'OpenGraphResourceType'):
    if open_graph_resource_type is None:
      del self.open_graph_resource_type
      return
    if not isinstance(open_graph_resource_type, OpenGraphResourceType):
      raise TypeError('open_graph_resource_type must be of type OpenGraphResourceType')
    self._open_graph_resource_type = open_graph_resource_type

  @property
  def entity_id(self) -> int:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: int):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, int):
      raise TypeError('entity_id must be of type int')
    self._entity_id = entity_id

  @property
  def entity_version_id(self) -> int:
    return self._entity_version_id or 0

  @entity_version_id.setter
  def entity_version_id(self, entity_version_id: Optional[int]):
    if entity_version_id is None:
      del self.entity_version_id
      return
    if not isinstance(entity_version_id, int):
      raise TypeError('entity_version_id must be of type int')
    self._entity_version_id = entity_version_id


class ResearchBenchmarkLeaderboardMetadata(KaggleObject):
  r"""
  TODO(bml): Tidy representations so that both use the unified leaderboard

  Attributes:
    benchmark_version (BenchmarkVersion)
      Benchmark version
    benchmark_leaderboard (BenchmarkLeaderboard)
      [deprecated] Research benchmark leaderboard
    unified_benchmark_leaderboard (UnifiedBenchmarkLeaderboard)
      New research benchmark leaderboard
  """

  def __init__(self):
    self._benchmark_version = None
    self._benchmark_leaderboard = None
    self._unified_benchmark_leaderboard = None
    self._freeze()

  @property
  def benchmark_version(self) -> Optional['BenchmarkVersion']:
    """Benchmark version"""
    return self._benchmark_version

  @benchmark_version.setter
  def benchmark_version(self, benchmark_version: Optional['BenchmarkVersion']):
    if benchmark_version is None:
      del self.benchmark_version
      return
    if not isinstance(benchmark_version, BenchmarkVersion):
      raise TypeError('benchmark_version must be of type BenchmarkVersion')
    self._benchmark_version = benchmark_version

  @property
  def benchmark_leaderboard(self) -> Optional['BenchmarkLeaderboard']:
    """[deprecated] Research benchmark leaderboard"""
    return self._benchmark_leaderboard

  @benchmark_leaderboard.setter
  def benchmark_leaderboard(self, benchmark_leaderboard: Optional['BenchmarkLeaderboard']):
    if benchmark_leaderboard is None:
      del self.benchmark_leaderboard
      return
    if not isinstance(benchmark_leaderboard, BenchmarkLeaderboard):
      raise TypeError('benchmark_leaderboard must be of type BenchmarkLeaderboard')
    self._benchmark_leaderboard = benchmark_leaderboard

  @property
  def unified_benchmark_leaderboard(self) -> Optional['UnifiedBenchmarkLeaderboard']:
    """New research benchmark leaderboard"""
    return self._unified_benchmark_leaderboard

  @unified_benchmark_leaderboard.setter
  def unified_benchmark_leaderboard(self, unified_benchmark_leaderboard: Optional['UnifiedBenchmarkLeaderboard']):
    if unified_benchmark_leaderboard is None:
      del self.unified_benchmark_leaderboard
      return
    if not isinstance(unified_benchmark_leaderboard, UnifiedBenchmarkLeaderboard):
      raise TypeError('unified_benchmark_leaderboard must be of type UnifiedBenchmarkLeaderboard')
    self._unified_benchmark_leaderboard = unified_benchmark_leaderboard


BenchmarkLeaderboardMetadata._fields = [
  FieldMetadata("benchmark", "benchmark", "_benchmark", Benchmark, None, KaggleObjectSerializer()),
  FieldMetadata("benchmarkLeaderboard", "benchmark_leaderboard", "_benchmark_leaderboard", UnifiedBenchmarkLeaderboard, None, KaggleObjectSerializer()),
]

OpenGraphImageMetadata._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("openGraphResourceType", "open_graph_resource_type", "_open_graph_resource_type", OpenGraphResourceType, OpenGraphResourceType.UNSPECIFIED, EnumSerializer()),
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("researchBenchmarkLeaderboardMetadata", "research_benchmark_leaderboard_metadata", "_research_benchmark_leaderboard_metadata", ResearchBenchmarkLeaderboardMetadata, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkLeaderboardMetadata", "benchmark_leaderboard_metadata", "_benchmark_leaderboard_metadata", BenchmarkLeaderboardMetadata, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("deleteTime", "delete_time", "_delete_time", datetime, None, DateTimeSerializer()),
]

OpenGraphResource._fields = [
  FieldMetadata("openGraphResourceType", "open_graph_resource_type", "_open_graph_resource_type", OpenGraphResourceType, OpenGraphResourceType.UNSPECIFIED, EnumSerializer()),
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityVersionId", "entity_version_id", "_entity_version_id", int, None, PredefinedSerializer(), optional=True),
]

ResearchBenchmarkLeaderboardMetadata._fields = [
  FieldMetadata("benchmarkVersion", "benchmark_version", "_benchmark_version", BenchmarkVersion, None, KaggleObjectSerializer()),
  FieldMetadata("benchmarkLeaderboard", "benchmark_leaderboard", "_benchmark_leaderboard", BenchmarkLeaderboard, None, KaggleObjectSerializer()),
  FieldMetadata("unifiedBenchmarkLeaderboard", "unified_benchmark_leaderboard", "_unified_benchmark_leaderboard", UnifiedBenchmarkLeaderboard, None, KaggleObjectSerializer()),
]

