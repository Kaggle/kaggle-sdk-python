from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_enums import ListBenchmarkTasksOrderBy, ValidateSaveBenchmarkTaskValidationResult
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkTask, BenchmarkTaskVersion, BenchmarkTaskVersionMapping, ListBenchmarkTasksFilter, TaskIdentifier
from kagglesdk.kaggle_object import *
from typing import Optional, List

class AddBenchmarkTaskTagRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
    tag_id (int)
  """

  def __init__(self):
    self._task_identifier = None
    self._tag_id = 0
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier

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


class BatchDeleteBenchmarkTaskVersionsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_version_ids (int)
      The benchmark task versions to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, to
      maintain RemoveTime consistency across tables in the DB.
  """

  def __init__(self):
    self._benchmark_task_version_ids = []
    self._is_user_delete = False
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_task_version_ids(self) -> Optional[List[int]]:
    """The benchmark task versions to delete."""
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
    Optional remove timestamp if handler is called from a parent handler, to
    maintain RemoveTime consistency across tables in the DB.
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


class CreateBenchmarkTaskFromKernelSessionRequest(KaggleObject):
  r"""
  Attributes:
    source_kernel_session_id (int)
      The kernel session to use as the source for creating the benchmark task.
  """

  def __init__(self):
    self._source_kernel_session_id = 0
    self._freeze()

  @property
  def source_kernel_session_id(self) -> int:
    """The kernel session to use as the source for creating the benchmark task."""
    return self._source_kernel_session_id

  @source_kernel_session_id.setter
  def source_kernel_session_id(self, source_kernel_session_id: int):
    if source_kernel_session_id is None:
      del self.source_kernel_session_id
      return
    if not isinstance(source_kernel_session_id, int):
      raise TypeError('source_kernel_session_id must be of type int')
    self._source_kernel_session_id = source_kernel_session_id


class CreateBenchmarkTaskFromPromptRequest(KaggleObject):
  r"""
  Attributes:
    task_description (str)
    assertion_description (str)
  """

  def __init__(self):
    self._task_description = ""
    self._assertion_description = ""
    self._freeze()

  @property
  def task_description(self) -> str:
    return self._task_description

  @task_description.setter
  def task_description(self, task_description: str):
    if task_description is None:
      del self.task_description
      return
    if not isinstance(task_description, str):
      raise TypeError('task_description must be of type str')
    self._task_description = task_description

  @property
  def assertion_description(self) -> str:
    return self._assertion_description

  @assertion_description.setter
  def assertion_description(self, assertion_description: str):
    if assertion_description is None:
      del self.assertion_description
      return
    if not isinstance(assertion_description, str):
      raise TypeError('assertion_description must be of type str')
    self._assertion_description = assertion_description


class CreateBenchmarkTaskFromPromptResponse(KaggleObject):
  r"""
  Attributes:
    kernel_url (str)
  """

  def __init__(self):
    self._kernel_url = ""
    self._freeze()

  @property
  def kernel_url(self) -> str:
    return self._kernel_url

  @kernel_url.setter
  def kernel_url(self, kernel_url: str):
    if kernel_url is None:
      del self.kernel_url
      return
    if not isinstance(kernel_url, str):
      raise TypeError('kernel_url must be of type str')
    self._kernel_url = kernel_url


class CreateBenchmarkTaskVersionMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (BenchmarkTaskVersionMapping)
      The benchmark task version mapping to create.
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['BenchmarkTaskVersionMapping']]]:
    """The benchmark task version mapping to create."""
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['BenchmarkTaskVersionMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersionMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type BenchmarkTaskVersionMapping')
    self._mappings = mappings


class CreateBenchmarkTaskVersionMappingsResponse(KaggleObject):
  r"""
  Attributes:
    mappings (BenchmarkTaskVersionMapping)
      Newly created task version mappings.
  """

  def __init__(self):
    self._mappings = []
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['BenchmarkTaskVersionMapping']]]:
    """Newly created task version mappings."""
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['BenchmarkTaskVersionMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersionMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type BenchmarkTaskVersionMapping')
    self._mappings = mappings


class DeleteBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_id (int)
      The benchmark task to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, to
      maintain RemoveTime consistency across tables in the DB.
    notes (str)
      Optional notes for content state change logs.
  """

  def __init__(self):
    self._benchmark_task_id = 0
    self._is_user_delete = False
    self._remove_time = None
    self._notes = None
    self._freeze()

  @property
  def benchmark_task_id(self) -> int:
    """The benchmark task to delete."""
    return self._benchmark_task_id

  @benchmark_task_id.setter
  def benchmark_task_id(self, benchmark_task_id: int):
    if benchmark_task_id is None:
      del self.benchmark_task_id
      return
    if not isinstance(benchmark_task_id, int):
      raise TypeError('benchmark_task_id must be of type int')
    self._benchmark_task_id = benchmark_task_id

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
    Optional remove timestamp if handler is called from a parent handler, to
    maintain RemoveTime consistency across tables in the DB.
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


class DeleteBenchmarkTaskVersionMappingsRequest(KaggleObject):
  r"""
  Attributes:
    mappings (BenchmarkTaskVersionMapping)
      Mappings to delete, only the ParentTaskVersionId and ChildTaskVersionId
      fields are used.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
  """

  def __init__(self):
    self._mappings = []
    self._is_user_delete = False
    self._freeze()

  @property
  def mappings(self) -> Optional[List[Optional['BenchmarkTaskVersionMapping']]]:
    r"""
    Mappings to delete, only the ParentTaskVersionId and ChildTaskVersionId
    fields are used.
    """
    return self._mappings

  @mappings.setter
  def mappings(self, mappings: Optional[List[Optional['BenchmarkTaskVersionMapping']]]):
    if mappings is None:
      del self.mappings
      return
    if not isinstance(mappings, list):
      raise TypeError('mappings must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersionMapping) for t in mappings]):
      raise TypeError('mappings must contain only items of type BenchmarkTaskVersionMapping')
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


class DeleteBenchmarkTaskVersionMappingsResponse(KaggleObject):
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


class DeleteBenchmarkTaskVersionRequest(KaggleObject):
  r"""
  TODO(b/469460130): Delete the task if the version we're deleting is the last
  version.

  Attributes:
    benchmark_task_version_id (int)
      The benchmark task version to delete.
    is_user_delete (bool)
      Whether the delete is from a user or for moderation.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler, to
      maintain RemoveTime consistency across tables in the DB.
  """

  def __init__(self):
    self._benchmark_task_version_id = 0
    self._is_user_delete = False
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    """The benchmark task version to delete."""
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
    Optional remove timestamp if handler is called from a parent handler, to
    maintain RemoveTime consistency across tables in the DB.
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


class GetBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
      Unique identifier of the benchmark task to get
    read_mask (FieldMask)
      If the read mask is unset, we will default to all fields (per
      https://google.aip.dev/157)
  """

  def __init__(self):
    self._task_identifier = None
    self._read_mask = None
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    """Unique identifier of the benchmark task to get"""
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier

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


class GetBenchmarkTasksByIdRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_ids (int)
  """

  def __init__(self):
    self._benchmark_task_ids = []
    self._freeze()

  @property
  def benchmark_task_ids(self) -> Optional[List[int]]:
    return self._benchmark_task_ids

  @benchmark_task_ids.setter
  def benchmark_task_ids(self, benchmark_task_ids: Optional[List[int]]):
    if benchmark_task_ids is None:
      del self.benchmark_task_ids
      return
    if not isinstance(benchmark_task_ids, list):
      raise TypeError('benchmark_task_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_task_ids]):
      raise TypeError('benchmark_task_ids must contain only items of type int')
    self._benchmark_task_ids = benchmark_task_ids


class GetBenchmarkTasksByIdResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_tasks (BenchmarkTask)
  """

  def __init__(self):
    self._benchmark_tasks = []
    self._freeze()

  @property
  def benchmark_tasks(self) -> Optional[List[Optional['BenchmarkTask']]]:
    return self._benchmark_tasks

  @benchmark_tasks.setter
  def benchmark_tasks(self, benchmark_tasks: Optional[List[Optional['BenchmarkTask']]]):
    if benchmark_tasks is None:
      del self.benchmark_tasks
      return
    if not isinstance(benchmark_tasks, list):
      raise TypeError('benchmark_tasks must be of type list')
    if not all([isinstance(t, BenchmarkTask) for t in benchmark_tasks]):
      raise TypeError('benchmark_tasks must contain only items of type BenchmarkTask')
    self._benchmark_tasks = benchmark_tasks


class GetTaskRecommendationsRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
      Unique identifier of the benchmark task to get recommendations for
    max_recommendations (int)
  """

  def __init__(self):
    self._task_identifier = None
    self._max_recommendations = 0
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    """Unique identifier of the benchmark task to get recommendations for"""
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier

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


class GetTaskRecommendationsResponse(KaggleObject):
  r"""
  Attributes:
    task_recommendations (BenchmarkTask)
  """

  def __init__(self):
    self._task_recommendations = []
    self._freeze()

  @property
  def task_recommendations(self) -> Optional[List[Optional['BenchmarkTask']]]:
    return self._task_recommendations

  @task_recommendations.setter
  def task_recommendations(self, task_recommendations: Optional[List[Optional['BenchmarkTask']]]):
    if task_recommendations is None:
      del self.task_recommendations
      return
    if not isinstance(task_recommendations, list):
      raise TypeError('task_recommendations must be of type list')
    if not all([isinstance(t, BenchmarkTask) for t in task_recommendations]):
      raise TypeError('task_recommendations must contain only items of type BenchmarkTask')
    self._task_recommendations = task_recommendations


class GetUserBenchmarkTaskCountsRequest(KaggleObject):
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


class GetUserBenchmarkTaskCountsResponse(KaggleObject):
  r"""
  Attributes:
    benchmark_task_count (int)
      Number of public tasks made by this user
    total_benchmark_task_votes (int)
      The total score for this user's public tasks
  """

  def __init__(self):
    self._benchmark_task_count = 0
    self._total_benchmark_task_votes = 0
    self._freeze()

  @property
  def benchmark_task_count(self) -> int:
    """Number of public tasks made by this user"""
    return self._benchmark_task_count

  @benchmark_task_count.setter
  def benchmark_task_count(self, benchmark_task_count: int):
    if benchmark_task_count is None:
      del self.benchmark_task_count
      return
    if not isinstance(benchmark_task_count, int):
      raise TypeError('benchmark_task_count must be of type int')
    self._benchmark_task_count = benchmark_task_count

  @property
  def total_benchmark_task_votes(self) -> int:
    """The total score for this user's public tasks"""
    return self._total_benchmark_task_votes

  @total_benchmark_task_votes.setter
  def total_benchmark_task_votes(self, total_benchmark_task_votes: int):
    if total_benchmark_task_votes is None:
      del self.total_benchmark_task_votes
      return
    if not isinstance(total_benchmark_task_votes, int):
      raise TypeError('total_benchmark_task_votes must be of type int')
    self._total_benchmark_task_votes = total_benchmark_task_votes


class IncrementBenchmarkTaskViewCountRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
  """

  def __init__(self):
    self._task_identifier = None
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier


class ListBenchmarkTasksRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    filter (ListBenchmarkTasksFilter)
    order_by (ListBenchmarkTasksOrderBy)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._filter = None
    self._order_by = ListBenchmarkTasksOrderBy.LIST_BENCHMARK_TASKS_ORDER_BY_UNSPECIFIED
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
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def filter(self) -> Optional['ListBenchmarkTasksFilter']:
    return self._filter or None

  @filter.setter
  def filter(self, filter: Optional[Optional['ListBenchmarkTasksFilter']]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarkTasksFilter):
      raise TypeError('filter must be of type ListBenchmarkTasksFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListBenchmarkTasksOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListBenchmarkTasksOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListBenchmarkTasksOrderBy):
      raise TypeError('order_by must be of type ListBenchmarkTasksOrderBy')
    self._order_by = order_by

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


class ListBenchmarkTasksResponse(KaggleObject):
  r"""
  Attributes:
    tasks (BenchmarkTask)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._tasks = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['BenchmarkTask']]]:
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['BenchmarkTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, BenchmarkTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type BenchmarkTask')
    self._tasks = tasks

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

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


class ListBenchmarkTaskVersionsFilter(KaggleObject):
  r"""
  Attributes:
    benchmark_task_id (int)
  """

  def __init__(self):
    self._benchmark_task_id = None
    self._freeze()

  @property
  def benchmark_task_id(self) -> int:
    return self._benchmark_task_id or 0

  @benchmark_task_id.setter
  def benchmark_task_id(self, benchmark_task_id: Optional[int]):
    if benchmark_task_id is None:
      del self.benchmark_task_id
      return
    if not isinstance(benchmark_task_id, int):
      raise TypeError('benchmark_task_id must be of type int')
    self._benchmark_task_id = benchmark_task_id


class ListBenchmarkTaskVersionsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    filter (ListBenchmarkTaskVersionsFilter)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._filter = None
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
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def filter(self) -> Optional['ListBenchmarkTaskVersionsFilter']:
    return self._filter or None

  @filter.setter
  def filter(self, filter: Optional[Optional['ListBenchmarkTaskVersionsFilter']]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListBenchmarkTaskVersionsFilter):
      raise TypeError('filter must be of type ListBenchmarkTaskVersionsFilter')
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


class ListBenchmarkTaskVersionsResponse(KaggleObject):
  r"""
  Attributes:
    task_versions (BenchmarkTaskVersion)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._task_versions = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def task_versions(self) -> Optional[List[Optional['BenchmarkTaskVersion']]]:
    return self._task_versions

  @task_versions.setter
  def task_versions(self, task_versions: Optional[List[Optional['BenchmarkTaskVersion']]]):
    if task_versions is None:
      del self.task_versions
      return
    if not isinstance(task_versions, list):
      raise TypeError('task_versions must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersion) for t in task_versions]):
      raise TypeError('task_versions must contain only items of type BenchmarkTaskVersion')
    self._task_versions = task_versions

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

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


class RemoveBenchmarkTaskTagRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
    tag_id (int)
  """

  def __init__(self):
    self._task_identifier = None
    self._tag_id = 0
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier

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


class RestoreBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_id (int)
      The benchmark task to restore.
    notes (str)
      Notes or reason for restoring the benchmark task (for content state logs).
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler. Will
      be used to restore related entities that were removed at the specific time
      of the parent.
  """

  def __init__(self):
    self._benchmark_task_id = 0
    self._notes = ""
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_task_id(self) -> int:
    """The benchmark task to restore."""
    return self._benchmark_task_id

  @benchmark_task_id.setter
  def benchmark_task_id(self, benchmark_task_id: int):
    if benchmark_task_id is None:
      del self.benchmark_task_id
      return
    if not isinstance(benchmark_task_id, int):
      raise TypeError('benchmark_task_id must be of type int')
    self._benchmark_task_id = benchmark_task_id

  @property
  def notes(self) -> str:
    """Notes or reason for restoring the benchmark task (for content state logs)."""
    return self._notes

  @notes.setter
  def notes(self, notes: str):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes

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


class RestoreBenchmarkTaskVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_version_id (int)
      The benchmark task version to restore.
    remove_time (datetime)
      Optional remove timestamp if handler is called from a parent handler. Will
      be used to restore related entities that were removed at the specific time
      of the parent.
  """

  def __init__(self):
    self._benchmark_task_version_id = 0
    self._remove_time = None
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    """The benchmark task version to restore."""
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


class UpdateBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task (BenchmarkTask)
    update_mask (FieldMask)
      Field mask for fields to update.
  """

  def __init__(self):
    self._benchmark_task = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark_task(self) -> Optional['BenchmarkTask']:
    return self._benchmark_task

  @benchmark_task.setter
  def benchmark_task(self, benchmark_task: Optional['BenchmarkTask']):
    if benchmark_task is None:
      del self.benchmark_task
      return
    if not isinstance(benchmark_task, BenchmarkTask):
      raise TypeError('benchmark_task must be of type BenchmarkTask')
    self._benchmark_task = benchmark_task

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


class UpdateBenchmarkTaskTagsRequest(KaggleObject):
  r"""
  Attributes:
    task_identifier (TaskIdentifier)
    tag_ids (int)
      The new set of tags to use (adding or removing as necessary)
  """

  def __init__(self):
    self._task_identifier = None
    self._tag_ids = []
    self._freeze()

  @property
  def task_identifier(self) -> Optional['TaskIdentifier']:
    return self._task_identifier

  @task_identifier.setter
  def task_identifier(self, task_identifier: Optional['TaskIdentifier']):
    if task_identifier is None:
      del self.task_identifier
      return
    if not isinstance(task_identifier, TaskIdentifier):
      raise TypeError('task_identifier must be of type TaskIdentifier')
    self._task_identifier = task_identifier

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The new set of tags to use (adding or removing as necessary)"""
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids


class UpdateBenchmarkTaskVersionRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_version (BenchmarkTaskVersion)
    update_mask (FieldMask)
      Field mask for fields to update.
  """

  def __init__(self):
    self._benchmark_task_version = None
    self._update_mask = None
    self._freeze()

  @property
  def benchmark_task_version(self) -> Optional['BenchmarkTaskVersion']:
    return self._benchmark_task_version

  @benchmark_task_version.setter
  def benchmark_task_version(self, benchmark_task_version: Optional['BenchmarkTaskVersion']):
    if benchmark_task_version is None:
      del self.benchmark_task_version
      return
    if not isinstance(benchmark_task_version, BenchmarkTaskVersion):
      raise TypeError('benchmark_task_version must be of type BenchmarkTaskVersion')
    self._benchmark_task_version = benchmark_task_version

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


class ValidateSaveBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    source_kernel_id (int)
    task_name (str)
    task_description (str)
  """

  def __init__(self):
    self._source_kernel_id = 0
    self._task_name = ""
    self._task_description = ""
    self._freeze()

  @property
  def source_kernel_id(self) -> int:
    return self._source_kernel_id

  @source_kernel_id.setter
  def source_kernel_id(self, source_kernel_id: int):
    if source_kernel_id is None:
      del self.source_kernel_id
      return
    if not isinstance(source_kernel_id, int):
      raise TypeError('source_kernel_id must be of type int')
    self._source_kernel_id = source_kernel_id

  @property
  def task_name(self) -> str:
    return self._task_name

  @task_name.setter
  def task_name(self, task_name: str):
    if task_name is None:
      del self.task_name
      return
    if not isinstance(task_name, str):
      raise TypeError('task_name must be of type str')
    self._task_name = task_name

  @property
  def task_description(self) -> str:
    return self._task_description

  @task_description.setter
  def task_description(self, task_description: str):
    if task_description is None:
      del self.task_description
      return
    if not isinstance(task_description, str):
      raise TypeError('task_description must be of type str')
    self._task_description = task_description


class ValidateSaveBenchmarkTaskResponse(KaggleObject):
  r"""
  Attributes:
    validation_result (ValidateSaveBenchmarkTaskValidationResult)
    conflicting_kernel_id (int)
  """

  def __init__(self):
    self._validation_result = ValidateSaveBenchmarkTaskValidationResult.VALIDATION_RESULT_UNDEFINED
    self._conflicting_kernel_id = None
    self._freeze()

  @property
  def validation_result(self) -> 'ValidateSaveBenchmarkTaskValidationResult':
    return self._validation_result

  @validation_result.setter
  def validation_result(self, validation_result: 'ValidateSaveBenchmarkTaskValidationResult'):
    if validation_result is None:
      del self.validation_result
      return
    if not isinstance(validation_result, ValidateSaveBenchmarkTaskValidationResult):
      raise TypeError('validation_result must be of type ValidateSaveBenchmarkTaskValidationResult')
    self._validation_result = validation_result

  @property
  def conflicting_kernel_id(self) -> int:
    return self._conflicting_kernel_id or 0

  @conflicting_kernel_id.setter
  def conflicting_kernel_id(self, conflicting_kernel_id: Optional[int]):
    if conflicting_kernel_id is None:
      del self.conflicting_kernel_id
      return
    if not isinstance(conflicting_kernel_id, int):
      raise TypeError('conflicting_kernel_id must be of type int')
    self._conflicting_kernel_id = conflicting_kernel_id


AddBenchmarkTaskTagRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

BatchDeleteBenchmarkTaskVersionsRequest._fields = [
  FieldMetadata("benchmarkTaskVersionIds", "benchmark_task_version_ids", "_benchmark_task_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

CreateBenchmarkTaskFromKernelSessionRequest._fields = [
  FieldMetadata("sourceKernelSessionId", "source_kernel_session_id", "_source_kernel_session_id", int, 0, PredefinedSerializer()),
]

CreateBenchmarkTaskFromPromptRequest._fields = [
  FieldMetadata("taskDescription", "task_description", "_task_description", str, "", PredefinedSerializer()),
  FieldMetadata("assertionDescription", "assertion_description", "_assertion_description", str, "", PredefinedSerializer()),
]

CreateBenchmarkTaskFromPromptResponse._fields = [
  FieldMetadata("kernelUrl", "kernel_url", "_kernel_url", str, "", PredefinedSerializer()),
]

CreateBenchmarkTaskVersionMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", BenchmarkTaskVersionMapping, [], ListSerializer(KaggleObjectSerializer())),
]

CreateBenchmarkTaskVersionMappingsResponse._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", BenchmarkTaskVersionMapping, [], ListSerializer(KaggleObjectSerializer())),
]

DeleteBenchmarkTaskRequest._fields = [
  FieldMetadata("benchmarkTaskId", "benchmark_task_id", "_benchmark_task_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
]

DeleteBenchmarkTaskVersionMappingsRequest._fields = [
  FieldMetadata("mappings", "mappings", "_mappings", BenchmarkTaskVersionMapping, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
]

DeleteBenchmarkTaskVersionMappingsResponse._fields = [
  FieldMetadata("deletedMappingsCount", "deleted_mappings_count", "_deleted_mappings_count", int, 0, PredefinedSerializer()),
]

DeleteBenchmarkTaskVersionRequest._fields = [
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isUserDelete", "is_user_delete", "_is_user_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

GetBenchmarkTaskRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetBenchmarkTasksByIdRequest._fields = [
  FieldMetadata("benchmarkTaskIds", "benchmark_task_ids", "_benchmark_task_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetBenchmarkTasksByIdResponse._fields = [
  FieldMetadata("benchmarkTasks", "benchmark_tasks", "_benchmark_tasks", BenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
]

GetTaskRecommendationsRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("maxRecommendations", "max_recommendations", "_max_recommendations", int, 0, PredefinedSerializer()),
]

GetTaskRecommendationsResponse._fields = [
  FieldMetadata("taskRecommendations", "task_recommendations", "_task_recommendations", BenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
]

GetUserBenchmarkTaskCountsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserBenchmarkTaskCountsResponse._fields = [
  FieldMetadata("benchmarkTaskCount", "benchmark_task_count", "_benchmark_task_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBenchmarkTaskVotes", "total_benchmark_task_votes", "_total_benchmark_task_votes", int, 0, PredefinedSerializer()),
]

IncrementBenchmarkTaskViewCountRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
]

ListBenchmarkTasksRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListBenchmarkTasksFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("orderBy", "order_by", "_order_by", ListBenchmarkTasksOrderBy, ListBenchmarkTasksOrderBy.LIST_BENCHMARK_TASKS_ORDER_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListBenchmarkTasksResponse._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", BenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListBenchmarkTaskVersionsFilter._fields = [
  FieldMetadata("benchmarkTaskId", "benchmark_task_id", "_benchmark_task_id", int, None, PredefinedSerializer(), optional=True),
]

ListBenchmarkTaskVersionsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListBenchmarkTaskVersionsFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListBenchmarkTaskVersionsResponse._fields = [
  FieldMetadata("taskVersions", "task_versions", "_task_versions", BenchmarkTaskVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

RemoveBenchmarkTaskTagRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

RestoreBenchmarkTaskRequest._fields = [
  FieldMetadata("benchmarkTaskId", "benchmark_task_id", "_benchmark_task_id", int, 0, PredefinedSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, "", PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

RestoreBenchmarkTaskVersionRequest._fields = [
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
]

UpdateBenchmarkTaskRequest._fields = [
  FieldMetadata("benchmarkTask", "benchmark_task", "_benchmark_task", BenchmarkTask, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateBenchmarkTaskTagsRequest._fields = [
  FieldMetadata("taskIdentifier", "task_identifier", "_task_identifier", TaskIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

UpdateBenchmarkTaskVersionRequest._fields = [
  FieldMetadata("benchmarkTaskVersion", "benchmark_task_version", "_benchmark_task_version", BenchmarkTaskVersion, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

ValidateSaveBenchmarkTaskRequest._fields = [
  FieldMetadata("sourceKernelId", "source_kernel_id", "_source_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("taskName", "task_name", "_task_name", str, "", PredefinedSerializer()),
  FieldMetadata("taskDescription", "task_description", "_task_description", str, "", PredefinedSerializer()),
]

ValidateSaveBenchmarkTaskResponse._fields = [
  FieldMetadata("validationResult", "validation_result", "_validation_result", ValidateSaveBenchmarkTaskValidationResult, ValidateSaveBenchmarkTaskValidationResult.VALIDATION_RESULT_UNDEFINED, EnumSerializer()),
  FieldMetadata("conflictingKernelId", "conflicting_kernel_id", "_conflicting_kernel_id", int, None, PredefinedSerializer(), optional=True),
]

