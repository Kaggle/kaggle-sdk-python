from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_enums import ListBenchmarksOrderBy
from kagglesdk.benchmarks.types.benchmark_types import Benchmark, BenchmarkBracket, BenchmarkIdentifier, BenchmarkModelVersion, BenchmarkTaskVersion, BenchmarkVersion, BenchmarkVersionIdentifier, BenchmarkVersionModelMapping, GameArenaStreams, ListBenchmarksFilter, SampleTask
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from typing import List, Optional

class AddBenchmarkTagRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
    tag_id (int)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._tag_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def tag_id(self) -> int:
    return self._tag_id

  @tag_id.setter
  def tag_id(self, tag_id: int):
    if tag_id is None:
      del self.tag_id
      return
    if not isinstance(tag_id, int):
      raise TypeError('tag_id must be of type int')
    self._tag_id = tag_id


class AddTaskToBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
      Only supports benchmark of type 'Personal'.
    benchmark_task_version_id (int)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._benchmark_task_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """Only supports benchmark of type 'Personal'."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id


class BatchDeleteBenchmarkVersionsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_ids (int)
      The benchmark versions to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, keeps
      remove time consistent across db
  """

  def __init__(self):
    self._benchmark_version_ids = []
    self._is_user_delete = False
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_version_ids(self) -> Optional[List[int]]:
    """The benchmark versions to delete."""
    return self._benchmark_version_ids

  @benchmark_version_ids.setter
  def benchmark_version_ids(self, benchmark_version_ids: Optional[List[int]]):
    if benchmark_version_ids is None:
      del self.benchmark_version_ids
      return
    if not isinstance(benchmark_version_ids, list):
      raise TypeError('benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_version_ids]):
      raise TypeError('benchmark_version_ids must contain only items of type int')
    self._benchmark_version_ids = benchmark_version_ids

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

  @property
  def remove_time(self) -> datetime:
    r"""
    Optional remove timestamp if handler is called from a parent handler, keeps
    remove time consistent across db
    """
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time


class BenchmarkActivityResponse(KaggleObject):
  r"""
  Attributes:
    total_views (int)
    total_downloads (int)
    total_comments (int)
    total_models (int)
  """

  def __init__(self):
    self._total_views = 0
    self._total_downloads = 0
    self._total_comments = 0
    self._total_models = 0
    self._freeze()

  @property
  def total_views(self) -> int:
    return self._total_views

  @total_views.setter
  def total_views(self, total_views: int):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

  @property
  def total_downloads(self) -> int:
    return self._total_downloads

  @total_downloads.setter
  def total_downloads(self, total_downloads: int):
    if total_downloads is None:
      del self.total_downloads
      return
    if not isinstance(total_downloads, int):
      raise TypeError('total_downloads must be of type int')
    self._total_downloads = total_downloads

  @property
  def total_comments(self) -> int:
    return self._total_comments

  @total_comments.setter
  def total_comments(self, total_comments: int):
    if total_comments is None:
      del self.total_comments
      return
    if not isinstance(total_comments, int):
      raise TypeError('total_comments must be of type int')
    self._total_comments = total_comments

  @property
  def total_models(self) -> int:
    return self._total_models

  @total_models.setter
  def total_models(self, total_models: int):
    if total_models is None:
      del self.total_models
      return
    if not isinstance(total_models, int):
      raise TypeError('total_models must be of type int')
    self._total_models = total_models


class BulkAddBenchmarkReadCollaboratorsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_ids (int)
      Benchmarks to add read collaborators to.
    user_ids (int)
      Users to add as read collaborators.
  """

  def __init__(self):
    self._benchmark_ids = []
    self._user_ids = []
    self._freeze()

  @property
  def benchmark_ids(self) -> Optional[List[int]]:
    """Benchmarks to add read collaborators to."""
    return self._benchmark_ids

  @benchmark_ids.setter
  def benchmark_ids(self, benchmark_ids: Optional[List[int]]):
    if benchmark_ids is None:
      del self.benchmark_ids
      return
    if not isinstance(benchmark_ids, list):
      raise TypeError('benchmark_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_ids]):
      raise TypeError('benchmark_ids must contain only items of type int')
    self._benchmark_ids = benchmark_ids

  @property
  def user_ids(self) -> Optional[List[int]]:
    """Users to add as read collaborators."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids


class BulkAddBenchmarkReadCollaboratorsResponse(KaggleObject):
  r"""
  Attributes:
    count (int)
      Total read collaborator permissions added.
  """

  def __init__(self):
    self._count = 0
    self._freeze()

  @property
  def count(self) -> int:
    """Total read collaborator permissions added."""
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class BulkCreateBenchmarksRequest(KaggleObject):
  r"""
  Attributes:
    benchmarks (Benchmark)
      The benchmarks to create.
  """

  def __init__(self):
    self._benchmarks = []
    self._freeze()

  @property
  def benchmarks(self) -> Optional[List[Optional['Benchmark']]]:
    """The benchmarks to create."""
    return self._benchmarks

  @benchmarks.setter
  def benchmarks(self, benchmarks: Optional[List[Optional['Benchmark']]]):
    if benchmarks is None:
      del self.benchmarks
      return
    if not isinstance(benchmarks, list):
      raise TypeError('benchmarks must be of type list')
    if not all([isinstance(t, Benchmark) for t in benchmarks]):
      raise TypeError('benchmarks must contain only items of type Benchmark')
    self._benchmarks = benchmarks


class BulkCreateBenchmarksResponse(KaggleObject):
  r"""
  Attributes:
    benchmarks (Benchmark)
      The newly created benchmarks.
  """

  def __init__(self):
    self._benchmarks = []
    self._freeze()

  @property
  def benchmarks(self) -> Optional[List[Optional['Benchmark']]]:
    """The newly created benchmarks."""
    return self._benchmarks

  @benchmarks.setter
  def benchmarks(self, benchmarks: Optional[List[Optional['Benchmark']]]):
    if benchmarks is None:
      del self.benchmarks
      return
    if not isinstance(benchmarks, list):
      raise TypeError('benchmarks must be of type list')
    if not all([isinstance(t, Benchmark) for t in benchmarks]):
      raise TypeError('benchmarks must contain only items of type Benchmark')
    self._benchmarks = benchmarks


class BulkRemoveBenchmarkReadCollaboratorsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_ids (int)
      Benchmarks to remove read collaborators from.
    user_ids (int)
      Users to remove as read collaborators.
  """

  def __init__(self):
    self._benchmark_ids = []
    self._user_ids = []
    self._freeze()

  @property
  def benchmark_ids(self) -> Optional[List[int]]:
    """Benchmarks to remove read collaborators from."""
    return self._benchmark_ids

  @benchmark_ids.setter
  def benchmark_ids(self, benchmark_ids: Optional[List[int]]):
    if benchmark_ids is None:
      del self.benchmark_ids
      return
    if not isinstance(benchmark_ids, list):
      raise TypeError('benchmark_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_ids]):
      raise TypeError('benchmark_ids must contain only items of type int')
    self._benchmark_ids = benchmark_ids

  @property
  def user_ids(self) -> Optional[List[int]]:
    """Users to remove as read collaborators."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids


class BulkRemoveBenchmarkReadCollaboratorsResponse(KaggleObject):
  r"""
  Attributes:
    count (int)
      Total read collaborator permissions removed.
  """

  def __init__(self):
    self._count = 0
    self._freeze()

  @property
  def count(self) -> int:
    """Total read collaborator permissions removed."""
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class CreateBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark (Benchmark)
      The benchmark to create.
  """

  def __init__(self):
    self._benchmark = None
    self._freeze()

  @property
  def benchmark(self) -> Optional['Benchmark']:
    """The benchmark to create."""
    return self._benchmark

  @benchmark.setter
  def benchmark(self, benchmark: Optional['Benchmark']):
    if benchmark is None:
      del self.benchmark
      return
    if not isinstance(benchmark, Benchmark):
      raise TypeError('benchmark must be of type Benchmark')
    self._benchmark = benchmark


class CreateBenchmarkVersionDoiRequest(KaggleObject):
  r"""
  Request to create a DOI (DataCite's Digital Object Identifier,
  https://support.datacite.org/docs/api-create-dois) for the specified
  benchmark version.

  Attributes:
    benchmark_version_id (int)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id


class CreateBenchmarkVersionDoiResponse(KaggleObject):
  r"""
  Attributes:
    doi (str)
  """

  def __init__(self):
    self._doi = ""
    self._freeze()

  @property
  def doi(self) -> str:
    return self._doi

  @doi.setter
  def doi(self, doi: str):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi


class CreateBenchmarkVersionModelMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (BenchmarkVersionModelMapping)
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['BenchmarkVersionModelMapping']]]:
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['BenchmarkVersionModelMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, BenchmarkVersionModelMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type BenchmarkVersionModelMapping')
    self._mappings = mappings


class CreateBenchmarkVersionModelMappingsResponse(KaggleObject):
  r"""
  Attributes:
    new_mappings (BenchmarkVersionModelMapping)
  """

  def __init__(self):
    self._new_mappings = []
    self._freeze()

  @property
  def new_mappings(self) -> Optional[List[Optional['BenchmarkVersionModelMapping']]]:
    return self._new_mappings

  @new_mappings.setter
  def new_mappings(self, new_mappings: Optional[List[Optional['BenchmarkVersionModelMapping']]]):
    if new_mappings is None:
      del self.new_mappings
      return
    if not isinstance(new_mappings, list):
      raise TypeError('new_mappings must be of type list')
    if not all([isinstance(t, BenchmarkVersionModelMapping) for t in new_mappings]):
      raise TypeError('new_mappings must contain only items of type BenchmarkVersionModelMapping')
    self._new_mappings = new_mappings


class CreateBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version (BenchmarkVersion)
      The benchmark version to create.
  """

  def __init__(self):
    self._benchmark_version = None
    self._freeze()

  @property
  def benchmark_version(self) -> Optional['BenchmarkVersion']:
    """The benchmark version to create."""
    return self._benchmark_version

  @benchmark_version.setter
  def benchmark_version(self, benchmark_version: Optional['BenchmarkVersion']):
    if benchmark_version is None:
      del self.benchmark_version
      return
    if not isinstance(benchmark_version, BenchmarkVersion):
      raise TypeError('benchmark_version must be of type BenchmarkVersion')
    self._benchmark_version = benchmark_version


class DeleteBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
      The benchmark to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    notes (str)
      Optional notes for content state change logs.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, keeps
      remove time consistent across db
  """

  def __init__(self):
    self._benchmark_id = 0
    self._is_user_delete = False
    self._notes = None
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    """The benchmark to delete."""
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

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

  @property
  def notes(self) -> str:
    """Optional notes for content state change logs."""
    return self._notes or ""

  @notes.setter
  def notes(self, notes: Optional[str]):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes

  @property
  def remove_time(self) -> datetime:
    r"""
    Optional remove timestamp if handler is called from a parent handler, keeps
    remove time consistent across db
    """
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time


class DeleteBenchmarkVersionModelMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (BenchmarkVersionModelMapping)
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
  """

  def __init__(self):
    self._mappings = []
    self._is_user_delete = False
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['BenchmarkVersionModelMapping']]]:
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['BenchmarkVersionModelMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, BenchmarkVersionModelMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type BenchmarkVersionModelMapping')
    self._mappings = mappings

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


class DeleteBenchmarkVersionModelMappingsResponse(KaggleObject):
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


class DeleteBenchmarkVersionRequest(KaggleObject):
  r"""
  TODO(b/469460130): Delete the benchmark if the version we're deleting is the
  last version.

  Attributes:
    benchmark_version_id (int)
      The benchmark version to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, keeps
      remove time consistent across db
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._is_user_delete = False
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """The benchmark version to delete."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

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

  @property
  def remove_time(self) -> datetime:
    r"""
    Optional remove timestamp if handler is called from a parent handler, keeps
    remove time consistent across db
    """
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time


class DownloadBenchmarkLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_ids (int)
  """

  def __init__(self):
    self._benchmark_version_ids = []
    self._freeze()

  @property
  def benchmark_version_ids(self) -> Optional[List[int]]:
    return self._benchmark_version_ids

  @benchmark_version_ids.setter
  def benchmark_version_ids(self, benchmark_version_ids: Optional[List[int]]):
    if benchmark_version_ids is None:
      del self.benchmark_version_ids
      return
    if not isinstance(benchmark_version_ids, list):
      raise TypeError('benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_version_ids]):
      raise TypeError('benchmark_version_ids must contain only items of type int')
    self._benchmark_version_ids = benchmark_version_ids


class GetBenchmarkActivityRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id


class GetBenchmarkLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    version_identifier (BenchmarkVersionIdentifier)
      The benchmark version to fetch the leaderboard for
    take (int)
      If specified, only return the top N rows
      TODO(bml): Implement proper pagination
  """

  def __init__(self):
    self._version_identifier = None
    self._take = None
    self._freeze()

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    """The benchmark version to fetch the leaderboard for"""
    return self._version_identifier

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional['BenchmarkVersionIdentifier']):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier

  @property
  def take(self) -> int:
    r"""
    If specified, only return the top N rows
    TODO(bml): Implement proper pagination
    """
    return self._take or 0

  @take.setter
  def take(self, take: Optional[int]):
    if take is None:
      del self.take
      return
    if not isinstance(take, int):
      raise TypeError('take must be of type int')
    self._take = take


class GetBenchmarkRecommendationsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_identifier (BenchmarkIdentifier)
      Unique identifier of the benchmark to get recommendations for
    max_recommendations (int)
  """

  def __init__(self):
    self._benchmark_identifier = None
    self._max_recommendations = 0
    self._freeze()

  @property
  def benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    """Unique identifier of the benchmark to get recommendations for"""
    return self._benchmark_identifier

  @benchmark_identifier.setter
  def benchmark_identifier(self, benchmark_identifier: Optional['BenchmarkIdentifier']):
    if benchmark_identifier is None:
      del self.benchmark_identifier
      return
    if not isinstance(benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('benchmark_identifier must be of type BenchmarkIdentifier')
    self._benchmark_identifier = benchmark_identifier

  @property
  def max_recommendations(self) -> int:
    return self._max_recommendations

  @max_recommendations.setter
  def max_recommendations(self, max_recommendations: int):
    if max_recommendations is None:
      del self.max_recommendations
      return
    if not isinstance(max_recommendations, int):
      raise TypeError('max_recommendations must be of type int')
    self._max_recommendations = max_recommendations


class GetBenchmarkRecommendationsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_recommendations (Benchmark)
  """

  def __init__(self):
    self._benchmark_recommendations = []
    self._freeze()

  @property
  def benchmark_recommendations(self) -> Optional[List[Optional['Benchmark']]]:
    return self._benchmark_recommendations

  @benchmark_recommendations.setter
  def benchmark_recommendations(self, benchmark_recommendations: Optional[List[Optional['Benchmark']]]):
    if benchmark_recommendations is None:
      del self.benchmark_recommendations
      return
    if not isinstance(benchmark_recommendations, list):
      raise TypeError('benchmark_recommendations must be of type list')
    if not all([isinstance(t, Benchmark) for t in benchmark_recommendations]):
      raise TypeError('benchmark_recommendations must contain only items of type Benchmark')
    self._benchmark_recommendations = benchmark_recommendations


class GetBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_identifier (BenchmarkIdentifier)
      Unique identifier of the benchmark to get
    version_identifier (BenchmarkVersionIdentifier)
      Unique identifier for the contained benchmark version. If no
      identifier is specified, the latest published version (ordered by version
      number) is fetched. If no published versions exist, NULL is returned.
    read_mask (FieldMask)
      If the read mask is unset, we will default to all fields (per
      https://google.aip.dev/157)
  """

  def __init__(self):
    self._benchmark_identifier = None
    self._version_identifier = None
    self._read_mask = None
    self._freeze()

  @property
  def benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    """Unique identifier of the benchmark to get"""
    return self._benchmark_identifier

  @benchmark_identifier.setter
  def benchmark_identifier(self, benchmark_identifier: Optional['BenchmarkIdentifier']):
    if benchmark_identifier is None:
      del self.benchmark_identifier
      return
    if not isinstance(benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('benchmark_identifier must be of type BenchmarkIdentifier')
    self._benchmark_identifier = benchmark_identifier

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    r"""
    Unique identifier for the contained benchmark version. If no
    identifier is specified, the latest published version (ordered by version
    number) is fetched. If no published versions exist, NULL is returned.
    """
    return self._version_identifier or None

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional[Optional['BenchmarkVersionIdentifier']]):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier

  @property
  def read_mask(self) -> FieldMask:
    r"""
    If the read mask is unset, we will default to all fields (per
    https://google.aip.dev/157)
    """
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetBenchmarkVersionBracketRequest(KaggleObject):
  r"""
  Attributes:
    version_identifier (BenchmarkVersionIdentifier)
  """

  def __init__(self):
    self._version_identifier = None
    self._freeze()

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    return self._version_identifier

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional['BenchmarkVersionIdentifier']):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier


class GetBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    version_identifier (BenchmarkVersionIdentifier)
    read_mask (FieldMask)
      If the read mask is unset, we will default to all fields (per
      https://google.aip.dev/157)
  """

  def __init__(self):
    self._version_identifier = None
    self._read_mask = None
    self._freeze()

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    return self._version_identifier

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional['BenchmarkVersionIdentifier']):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier

  @property
  def read_mask(self) -> FieldMask:
    r"""
    If the read mask is unset, we will default to all fields (per
    https://google.aip.dev/157)
    """
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetGameArenaStreamsRequest(KaggleObject):
  r"""
  """

  pass

class GetParentBenchmarkVersionIdsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_version_id (int)
      The child/personal task version ID to look up benchmark versions for.
  """

  def __init__(self):
    self._benchmark_task_version_id = 0
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    """The child/personal task version ID to look up benchmark versions for."""
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id


class GetParentBenchmarkVersionIdsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_version_ids (int)
      The benchmark version IDs whose root task version is a parent of the
      given task version in the BenchmarkTaskVersionMappings table.
  """

  def __init__(self):
    self._benchmark_version_ids = []
    self._freeze()

  @property
  def benchmark_version_ids(self) -> Optional[List[int]]:
    r"""
    The benchmark version IDs whose root task version is a parent of the
    given task version in the BenchmarkTaskVersionMappings table.
    """
    return self._benchmark_version_ids

  @benchmark_version_ids.setter
  def benchmark_version_ids(self, benchmark_version_ids: Optional[List[int]]):
    if benchmark_version_ids is None:
      del self.benchmark_version_ids
      return
    if not isinstance(benchmark_version_ids, list):
      raise TypeError('benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_version_ids]):
      raise TypeError('benchmark_version_ids must contain only items of type int')
    self._benchmark_version_ids = benchmark_version_ids


class GetUnifiedBenchmarkLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    version_identifier (BenchmarkVersionIdentifier)
      The benchmark version to fetch the leaderboard for
    take_task_version_headers (int)
      How many task version headers to return. If not specified, all headers are
      returned.

      By default, sorted by the task version priority.
    take_model_version_headers (int)
      How many model version headers to return. If not specified, all headers are
      returned.

      By default, sorted by model version performance on the highest priority
      task version.
  """

  def __init__(self):
    self._version_identifier = None
    self._take_task_version_headers = None
    self._take_model_version_headers = None
    self._freeze()

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    """The benchmark version to fetch the leaderboard for"""
    return self._version_identifier

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional['BenchmarkVersionIdentifier']):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier

  @property
  def take_task_version_headers(self) -> int:
    r"""
    How many task version headers to return. If not specified, all headers are
    returned.

    By default, sorted by the task version priority.
    """
    return self._take_task_version_headers or 0

  @take_task_version_headers.setter
  def take_task_version_headers(self, take_task_version_headers: Optional[int]):
    if take_task_version_headers is None:
      del self.take_task_version_headers
      return
    if not isinstance(take_task_version_headers, int):
      raise TypeError('take_task_version_headers must be of type int')
    self._take_task_version_headers = take_task_version_headers

  @property
  def take_model_version_headers(self) -> int:
    r"""
    How many model version headers to return. If not specified, all headers are
    returned.

    By default, sorted by model version performance on the highest priority
    task version.
    """
    return self._take_model_version_headers or 0

  @take_model_version_headers.setter
  def take_model_version_headers(self, take_model_version_headers: Optional[int]):
    if take_model_version_headers is None:
      del self.take_model_version_headers
      return
    if not isinstance(take_model_version_headers, int):
      raise TypeError('take_model_version_headers must be of type int')
    self._take_model_version_headers = take_model_version_headers


class GetUserBenchmarkCountsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserBenchmarkCountsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_count (int)
      Number of public benchmarks made by this user
    total_benchmark_votes (int)
      The total score for this user's public benchmarks
  """

  def __init__(self):
    self._benchmark_count = 0
    self._total_benchmark_votes = 0
    self._freeze()

  @property
  def benchmark_count(self) -> int:
    """Number of public benchmarks made by this user"""
    return self._benchmark_count

  @benchmark_count.setter
  def benchmark_count(self, benchmark_count: int):
    if benchmark_count is None:
      del self.benchmark_count
      return
    if not isinstance(benchmark_count, int):
      raise TypeError('benchmark_count must be of type int')
    self._benchmark_count = benchmark_count

  @property
  def total_benchmark_votes(self) -> int:
    """The total score for this user's public benchmarks"""
    return self._total_benchmark_votes

  @total_benchmark_votes.setter
  def total_benchmark_votes(self, total_benchmark_votes: int):
    if total_benchmark_votes is None:
      del self.total_benchmark_votes
      return
    if not isinstance(total_benchmark_votes, int):
      raise TypeError('total_benchmark_votes must be of type int')
    self._total_benchmark_votes = total_benchmark_votes


class IncrementBenchmarkViewCountRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id


class ListBenchmarkSampleTasksRequest(KaggleObject):
  r"""
  """

  pass

class ListBenchmarkSampleTasksResponse(KaggleObject):
  r"""
  Attributes:
    tasks (SampleTask)
  """

  def __init__(self):
    self._tasks = []
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['SampleTask']]]:
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['SampleTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, SampleTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type SampleTask')
    self._tasks = tasks


class ListBenchmarksRequest(KaggleObject):
  r"""
  TODO(bml): Update list handlers to AIP standards when no longer admin-only.

  Attributes:
    filter (ListBenchmarksFilter)
      add filter and order by
    order_by (ListBenchmarksOrderBy)
    page_size (int)
      The maximum number of benchmarks to return.
    page_token (str)
    skip (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._filter = None
    self._order_by = ListBenchmarksOrderBy.LIST_BENCHMARKS_ORDER_BY_UNSPECIFIED
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._read_mask = None
    self._freeze()

  @property
  def filter(self) -> Optional['ListBenchmarksFilter']:
    """add filter and order by"""
    return self._filter or None

  @filter.setter
  def filter(self, filter: Optional[Optional['ListBenchmarksFilter']]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarksFilter):
      raise TypeError('filter must be of type ListBenchmarksFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListBenchmarksOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListBenchmarksOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListBenchmarksOrderBy):
      raise TypeError('order_by must be of type ListBenchmarksOrderBy')
    self._order_by = order_by

  @property
  def page_size(self) -> int:
    """The maximum number of benchmarks to return."""
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
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

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


class ListBenchmarksResponse(KaggleObject):
  r"""
  Attributes:
    benchmarks (Benchmark)
    next_page_token (str)
    total_results (int)
  """

  def __init__(self):
    self._benchmarks = []
    self._next_page_token = ""
    self._total_results = 0
    self._freeze()

  @property
  def benchmarks(self) -> Optional[List[Optional['Benchmark']]]:
    return self._benchmarks

  @benchmarks.setter
  def benchmarks(self, benchmarks: Optional[List[Optional['Benchmark']]]):
    if benchmarks is None:
      del self.benchmarks
      return
    if not isinstance(benchmarks, list):
      raise TypeError('benchmarks must be of type list')
    if not all([isinstance(t, Benchmark) for t in benchmarks]):
      raise TypeError('benchmarks must contain only items of type Benchmark')
    self._benchmarks = benchmarks

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

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


class ListBenchmarkVersionMappingsRequest(KaggleObject):
  r"""
  TODO(bml): migrate the request and response to be AIP compliant.

  Attributes:
    version_identifier (BenchmarkVersionIdentifier)
       The benchmark version to list mappings for.
    read_mask (FieldMask)
      If the read mask is unset, we will default to all fields (per
      https://google.aip.dev/157)
  """

  def __init__(self):
    self._version_identifier = None
    self._read_mask = None
    self._freeze()

  @property
  def version_identifier(self) -> Optional['BenchmarkVersionIdentifier']:
    """ The benchmark version to list mappings for."""
    return self._version_identifier

  @version_identifier.setter
  def version_identifier(self, version_identifier: Optional['BenchmarkVersionIdentifier']):
    if version_identifier is None:
      del self.version_identifier
      return
    if not isinstance(version_identifier, BenchmarkVersionIdentifier):
      raise TypeError('version_identifier must be of type BenchmarkVersionIdentifier')
    self._version_identifier = version_identifier

  @property
  def read_mask(self) -> FieldMask:
    r"""
    If the read mask is unset, we will default to all fields (per
    https://google.aip.dev/157)
    """
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListBenchmarkVersionMappingsResponse(KaggleObject):
  r"""
  Attributes:
    child_benchmark_versions (BenchmarkVersion)
      Child benchmark versions of the requested benchmark version.
      Ex: for SciCode, a child benchmark version is SciCode Main Standard
    parent_benchmark_versions (BenchmarkVersion)
      Parent benchmark versions of the requested benchmark version.
      Ex: for SciCode Main Standard, a parent benchmark version is SciCode
    benchmark_model_versions (BenchmarkModelVersion)
      Model versions mapped to the benchmark version
      Ex: for SiCode, a mapped model version is Gemini-2.0-Flash-001
    child_task_versions (BenchmarkTaskVersion)
      Child task versions of the requested benchmark version.
      Ex: for FACTS Grounding, a child task version is the FACTS Grounding Public
      Score task version
    parent_task_versions (BenchmarkTaskVersion)
      Parent task versions of the requested benchmark version.
      Ex: for FACTS Grounding Public Score, a parent task version is the FACTS
      Grounding 'root task version'
  """

  def __init__(self):
    self._child_benchmark_versions = []
    self._parent_benchmark_versions = []
    self._benchmark_model_versions = []
    self._child_task_versions = []
    self._parent_task_versions = []
    self._freeze()

  @property
  def child_benchmark_versions(self) -> Optional[List[Optional['BenchmarkVersion']]]:
    r"""
    Child benchmark versions of the requested benchmark version.
    Ex: for SciCode, a child benchmark version is SciCode Main Standard
    """
    return self._child_benchmark_versions

  @child_benchmark_versions.setter
  def child_benchmark_versions(self, child_benchmark_versions: Optional[List[Optional['BenchmarkVersion']]]):
    if child_benchmark_versions is None:
      del self.child_benchmark_versions
      return
    if not isinstance(child_benchmark_versions, list):
      raise TypeError('child_benchmark_versions must be of type list')
    if not all([isinstance(t, BenchmarkVersion) for t in child_benchmark_versions]):
      raise TypeError('child_benchmark_versions must contain only items of type BenchmarkVersion')
    self._child_benchmark_versions = child_benchmark_versions

  @property
  def parent_benchmark_versions(self) -> Optional[List[Optional['BenchmarkVersion']]]:
    r"""
    Parent benchmark versions of the requested benchmark version.
    Ex: for SciCode Main Standard, a parent benchmark version is SciCode
    """
    return self._parent_benchmark_versions

  @parent_benchmark_versions.setter
  def parent_benchmark_versions(self, parent_benchmark_versions: Optional[List[Optional['BenchmarkVersion']]]):
    if parent_benchmark_versions is None:
      del self.parent_benchmark_versions
      return
    if not isinstance(parent_benchmark_versions, list):
      raise TypeError('parent_benchmark_versions must be of type list')
    if not all([isinstance(t, BenchmarkVersion) for t in parent_benchmark_versions]):
      raise TypeError('parent_benchmark_versions must contain only items of type BenchmarkVersion')
    self._parent_benchmark_versions = parent_benchmark_versions

  @property
  def benchmark_model_versions(self) -> Optional[List[Optional['BenchmarkModelVersion']]]:
    r"""
    Model versions mapped to the benchmark version
    Ex: for SiCode, a mapped model version is Gemini-2.0-Flash-001
    """
    return self._benchmark_model_versions

  @benchmark_model_versions.setter
  def benchmark_model_versions(self, benchmark_model_versions: Optional[List[Optional['BenchmarkModelVersion']]]):
    if benchmark_model_versions is None:
      del self.benchmark_model_versions
      return
    if not isinstance(benchmark_model_versions, list):
      raise TypeError('benchmark_model_versions must be of type list')
    if not all([isinstance(t, BenchmarkModelVersion) for t in benchmark_model_versions]):
      raise TypeError('benchmark_model_versions must contain only items of type BenchmarkModelVersion')
    self._benchmark_model_versions = benchmark_model_versions

  @property
  def child_task_versions(self) -> Optional[List[Optional['BenchmarkTaskVersion']]]:
    r"""
    Child task versions of the requested benchmark version.
    Ex: for FACTS Grounding, a child task version is the FACTS Grounding Public
    Score task version
    """
    return self._child_task_versions

  @child_task_versions.setter
  def child_task_versions(self, child_task_versions: Optional[List[Optional['BenchmarkTaskVersion']]]):
    if child_task_versions is None:
      del self.child_task_versions
      return
    if not isinstance(child_task_versions, list):
      raise TypeError('child_task_versions must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersion) for t in child_task_versions]):
      raise TypeError('child_task_versions must contain only items of type BenchmarkTaskVersion')
    self._child_task_versions = child_task_versions

  @property
  def parent_task_versions(self) -> Optional[List[Optional['BenchmarkTaskVersion']]]:
    r"""
    Parent task versions of the requested benchmark version.
    Ex: for FACTS Grounding Public Score, a parent task version is the FACTS
    Grounding 'root task version'
    """
    return self._parent_task_versions

  @parent_task_versions.setter
  def parent_task_versions(self, parent_task_versions: Optional[List[Optional['BenchmarkTaskVersion']]]):
    if parent_task_versions is None:
      del self.parent_task_versions
      return
    if not isinstance(parent_task_versions, list):
      raise TypeError('parent_task_versions must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersion) for t in parent_task_versions]):
      raise TypeError('parent_task_versions must contain only items of type BenchmarkTaskVersion')
    self._parent_task_versions = parent_task_versions


class ListBenchmarkVersionsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
      The benchmark to list versions for.
  """

  def __init__(self):
    self._benchmark_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    """The benchmark to list versions for."""
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id


class ListBenchmarkVersionsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_versions (BenchmarkVersion)
      The list of benchmark versions that are visible to the user.
      If the user can view drafts, this includes draft versions.
      Otherwise, only published versions are returned.
  """

  def __init__(self):
    self._benchmark_versions = []
    self._freeze()

  @property
  def benchmark_versions(self) -> Optional[List[Optional['BenchmarkVersion']]]:
    r"""
    The list of benchmark versions that are visible to the user.
    If the user can view drafts, this includes draft versions.
    Otherwise, only published versions are returned.
    """
    return self._benchmark_versions

  @benchmark_versions.setter
  def benchmark_versions(self, benchmark_versions: Optional[List[Optional['BenchmarkVersion']]]):
    if benchmark_versions is None:
      del self.benchmark_versions
      return
    if not isinstance(benchmark_versions, list):
      raise TypeError('benchmark_versions must be of type list')
    if not all([isinstance(t, BenchmarkVersion) for t in benchmark_versions]):
      raise TypeError('benchmark_versions must contain only items of type BenchmarkVersion')
    self._benchmark_versions = benchmark_versions


class ListOrganizationsRequest(KaggleObject):
  r"""
  """

  pass

class ListOrganizationsResponse(KaggleObject):
  r"""
  Attributes:
    organizations (OrganizationCard)
  """

  def __init__(self):
    self._organizations = []
    self._freeze()

  @property
  def organizations(self) -> Optional[List[Optional['OrganizationCard']]]:
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[List[Optional['OrganizationCard']]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, list):
      raise TypeError('organizations must be of type list')
    if not all([isinstance(t, OrganizationCard) for t in organizations]):
      raise TypeError('organizations must contain only items of type OrganizationCard')
    self._organizations = organizations


class PublishBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
    skip_task_publish (bool)
      Whether or not to also publish the root Task. Not publishing the root Task
      will hide the leaderboard.
  """

  def __init__(self):
    self._benchmark_id = 0
    self._skip_task_publish = None
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def skip_task_publish(self) -> bool:
    r"""
    Whether or not to also publish the root Task. Not publishing the root Task
    will hide the leaderboard.
    """
    return self._skip_task_publish or False

  @skip_task_publish.setter
  def skip_task_publish(self, skip_task_publish: Optional[bool]):
    if skip_task_publish is None:
      del self.skip_task_publish
      return
    if not isinstance(skip_task_publish, bool):
      raise TypeError('skip_task_publish must be of type bool')
    self._skip_task_publish = skip_task_publish


class PublishBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
    skip_task_publish (bool)
      Whether or not to also publish the root Task for the benchmark.
      Not publishing the root Task will hide the leaderboard.
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._skip_task_publish = None
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def skip_task_publish(self) -> bool:
    r"""
    Whether or not to also publish the root Task for the benchmark.
    Not publishing the root Task will hide the leaderboard.
    """
    return self._skip_task_publish or False

  @skip_task_publish.setter
  def skip_task_publish(self, skip_task_publish: Optional[bool]):
    if skip_task_publish is None:
      del self.skip_task_publish
      return
    if not isinstance(skip_task_publish, bool):
      raise TypeError('skip_task_publish must be of type bool')
    self._skip_task_publish = skip_task_publish


class RemoveBenchmarkTagRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
    tag_id (int)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._tag_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def tag_id(self) -> int:
    return self._tag_id

  @tag_id.setter
  def tag_id(self, tag_id: int):
    if tag_id is None:
      del self.tag_id
      return
    if not isinstance(tag_id, int):
      raise TypeError('tag_id must be of type int')
    self._tag_id = tag_id


class RemoveTaskFromBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
      Only supports benchmark of type 'Personal'.
    benchmark_task_version_id (int)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._benchmark_task_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """Only supports benchmark of type 'Personal'."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id


class RestoreBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
      The benchmark to restore.
    notes (str)
      Notes or reason for restoring the benchmark (for content state logs).
  """

  def __init__(self):
    self._benchmark_id = 0
    self._notes = ""
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    """The benchmark to restore."""
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def notes(self) -> str:
    """Notes or reason for restoring the benchmark (for content state logs)."""
    return self._notes

  @notes.setter
  def notes(self, notes: str):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


class RestoreBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
      The benchmark version to restore.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler. Will
      be used to restore related entities that were removed at the specific time
      of the parent.
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """The benchmark version to restore."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def remove_time(self) -> datetime:
    r"""
    Optional remove timestamp if handler is called from a parent handler. Will
    be used to restore related entities that were removed at the specific time
    of the parent.
    """
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time


class UnpublishBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id


class UnpublishBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id


class UpdateBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    benchmark (Benchmark)
      The benchmark to update.
    update_mask (FieldMask)
      Field mask for fields to update.
  """

  def __init__(self):
    self._benchmark = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark(self) -> Optional['Benchmark']:
    """The benchmark to update."""
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
  def update_mask(self) -> FieldMask:
    """Field mask for fields to update."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateBenchmarkVersionBracketRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
    bracket (BenchmarkBracket)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._bracket = None
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def bracket(self) -> Optional['BenchmarkBracket']:
    return self._bracket

  @bracket.setter
  def bracket(self, bracket: Optional['BenchmarkBracket']):
    if bracket is None:
      del self.bracket
      return
    if not isinstance(bracket, BenchmarkBracket):
      raise TypeError('bracket must be of type BenchmarkBracket')
    self._bracket = bracket


class UpdateBenchmarkVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version (BenchmarkVersion)
      The benchmark version to update.
    update_mask (FieldMask)
      Field mask for fields to update.
  """

  def __init__(self):
    self._benchmark_version = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark_version(self) -> Optional['BenchmarkVersion']:
    """The benchmark version to update."""
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
  def update_mask(self) -> FieldMask:
    """Field mask for fields to update."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateGameArenaStreamsRequest(KaggleObject):
  r"""
  Attributes:
    streams (GameArenaStreams)
  """

  def __init__(self):
    self._streams = None
    self._freeze()

  @property
  def streams(self) -> Optional['GameArenaStreams']:
    return self._streams

  @streams.setter
  def streams(self, streams: Optional['GameArenaStreams']):
    if streams is None:
      del self.streams
      return
    if not isinstance(streams, GameArenaStreams):
      raise TypeError('streams must be of type GameArenaStreams')
    self._streams = streams


AddBenchmarkTagRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

AddTaskToBenchmarkRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
]

BatchDeleteBenchmarkVersionsRequest._fields = [
  FieldMetadata("benchmarkVersionIds", "benchmark_version_ids", "_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

BenchmarkActivityResponse._fields = [
  FieldMetadata("totalViews", "total_views", "_total_views", int, 0, PredefinedSerializer()),
  FieldMetadata("totalDownloads", "total_downloads", "_total_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("totalComments", "total_comments", "_total_comments", int, 0, PredefinedSerializer()),
  FieldMetadata("totalModels", "total_models", "_total_models", int, 0, PredefinedSerializer()),
]

BulkAddBenchmarkReadCollaboratorsRequest._fields = [
  FieldMetadata("benchmarkIds", "benchmark_ids", "_benchmark_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BulkAddBenchmarkReadCollaboratorsResponse._fields = [
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

BulkCreateBenchmarksRequest._fields = [
  FieldMetadata("benchmarks", "benchmarks", "_benchmarks", Benchmark, [], ListSerializer(KaggleObjectSerializer())),
]

BulkCreateBenchmarksResponse._fields = [
  FieldMetadata("benchmarks", "benchmarks", "_benchmarks", Benchmark, [], ListSerializer(KaggleObjectSerializer())),
]

BulkRemoveBenchmarkReadCollaboratorsRequest._fields = [
  FieldMetadata("benchmarkIds", "benchmark_ids", "_benchmark_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BulkRemoveBenchmarkReadCollaboratorsResponse._fields = [
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

CreateBenchmarkRequest._fields = [
  FieldMetadata("benchmark", "benchmark", "_benchmark", Benchmark, None, KaggleObjectSerializer()),
]

CreateBenchmarkVersionDoiRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
]

CreateBenchmarkVersionDoiResponse._fields = [
  FieldMetadata("doi", "doi", "_doi", str, "", PredefinedSerializer()),
]

CreateBenchmarkVersionModelMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", BenchmarkVersionModelMapping, [], ListSerializer(KaggleObjectSerializer())),
]

CreateBenchmarkVersionModelMappingsResponse._fields = [
  FieldMetadata("newMappings", "new_mappings", "_new_mappings", BenchmarkVersionModelMapping, [], ListSerializer(KaggleObjectSerializer())),
]

CreateBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersion", "benchmark_version", "_benchmark_version", BenchmarkVersion, None, KaggleObjectSerializer()),
]

DeleteBenchmarkRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

DeleteBenchmarkVersionModelMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", BenchmarkVersionModelMapping, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
]

DeleteBenchmarkVersionModelMappingsResponse._fields = [
  FieldMetadata("deletedMappingsCount", "deleted_mappings_count", "_deleted_mappings_count", int, 0, PredefinedSerializer()),
]

DeleteBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

DownloadBenchmarkLeaderboardRequest._fields = [
  FieldMetadata("benchmarkVersionIds", "benchmark_version_ids", "_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetBenchmarkActivityRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
]

GetBenchmarkLeaderboardRequest._fields = [
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("take", "take", "_take", int, None, PredefinedSerializer(), optional=True),
]

GetBenchmarkRecommendationsRequest._fields = [
  FieldMetadata("benchmarkIdentifier", "benchmark_identifier", "_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("maxRecommendations", "max_recommendations", "_max_recommendations", int, 0, PredefinedSerializer()),
]

GetBenchmarkRecommendationsResponse._fields = [
  FieldMetadata("benchmarkRecommendations", "benchmark_recommendations", "_benchmark_recommendations", Benchmark, [], ListSerializer(KaggleObjectSerializer())),
]

GetBenchmarkRequest._fields = [
  FieldMetadata("benchmarkIdentifier", "benchmark_identifier", "_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetBenchmarkVersionBracketRequest._fields = [
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer()),
]

GetBenchmarkVersionRequest._fields = [
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetGameArenaStreamsRequest._fields = []

GetParentBenchmarkVersionIdsRequest._fields = [
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
]

GetParentBenchmarkVersionIdsResponse._fields = [
  FieldMetadata("benchmarkVersionIds", "benchmark_version_ids", "_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetUnifiedBenchmarkLeaderboardRequest._fields = [
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("takeTaskVersionHeaders", "take_task_version_headers", "_take_task_version_headers", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("takeModelVersionHeaders", "take_model_version_headers", "_take_model_version_headers", int, None, PredefinedSerializer(), optional=True),
]

GetUserBenchmarkCountsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserBenchmarkCountsResponse._fields = [
  FieldMetadata("benchmarkCount", "benchmark_count", "_benchmark_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBenchmarkVotes", "total_benchmark_votes", "_total_benchmark_votes", int, 0, PredefinedSerializer()),
]

IncrementBenchmarkViewCountRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
]

ListBenchmarkSampleTasksRequest._fields = []

ListBenchmarkSampleTasksResponse._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", SampleTask, [], ListSerializer(KaggleObjectSerializer())),
]

ListBenchmarksRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListBenchmarksFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("orderBy", "order_by", "_order_by", ListBenchmarksOrderBy, ListBenchmarksOrderBy.LIST_BENCHMARKS_ORDER_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListBenchmarksResponse._fields = [
  FieldMetadata("benchmarks", "benchmarks", "_benchmarks", Benchmark, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
]

ListBenchmarkVersionMappingsRequest._fields = [
  FieldMetadata("versionIdentifier", "version_identifier", "_version_identifier", BenchmarkVersionIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListBenchmarkVersionMappingsResponse._fields = [
  FieldMetadata("childBenchmarkVersions", "child_benchmark_versions", "_child_benchmark_versions", BenchmarkVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("parentBenchmarkVersions", "parent_benchmark_versions", "_parent_benchmark_versions", BenchmarkVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("benchmarkModelVersions", "benchmark_model_versions", "_benchmark_model_versions", BenchmarkModelVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("childTaskVersions", "child_task_versions", "_child_task_versions", BenchmarkTaskVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("parentTaskVersions", "parent_task_versions", "_parent_task_versions", BenchmarkTaskVersion, [], ListSerializer(KaggleObjectSerializer())),
]

ListBenchmarkVersionsRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
]

ListBenchmarkVersionsResponse._fields = [
  FieldMetadata("benchmarkVersions", "benchmark_versions", "_benchmark_versions", BenchmarkVersion, [], ListSerializer(KaggleObjectSerializer())),
]

ListOrganizationsRequest._fields = []

ListOrganizationsResponse._fields = [
  FieldMetadata("organizations", "organizations", "_organizations", OrganizationCard, [], ListSerializer(KaggleObjectSerializer())),
]

PublishBenchmarkRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("skipTaskPublish", "skip_task_publish", "_skip_task_publish", bool, None, PredefinedSerializer(), optional=True),
]

PublishBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("skipTaskPublish", "skip_task_publish", "_skip_task_publish", bool, None, PredefinedSerializer(), optional=True),
]

RemoveBenchmarkTagRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

RemoveTaskFromBenchmarkRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
]

RestoreBenchmarkRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, "", PredefinedSerializer()),
]

RestoreBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

UnpublishBenchmarkRequest._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
]

UnpublishBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
]

UpdateBenchmarkRequest._fields = [
  FieldMetadata("benchmark", "benchmark", "_benchmark", Benchmark, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateBenchmarkVersionBracketRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("bracket", "bracket", "_bracket", BenchmarkBracket, None, KaggleObjectSerializer()),
]

UpdateBenchmarkVersionRequest._fields = [
  FieldMetadata("benchmarkVersion", "benchmark_version", "_benchmark_version", BenchmarkVersion, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateGameArenaStreamsRequest._fields = [
  FieldMetadata("streams", "streams", "_streams", GameArenaStreams, None, KaggleObjectSerializer()),
]

