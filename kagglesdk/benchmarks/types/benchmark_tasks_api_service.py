from datetime import datetime
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkTaskRunState, BenchmarkTaskVersionCreationState
from kagglesdk.benchmarks.types.benchmark_task_run_service import BatchScheduleBenchmarkModelVersionResult
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ApiBatchScheduleBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    task_slugs (ApiBenchmarkTaskSlug)
    model_version_slugs (str)
  """

  def __init__(self):
    self._task_slugs = []
    self._model_version_slugs = []
    self._freeze()

  @property
  def task_slugs(self) -> Optional[List[Optional['ApiBenchmarkTaskSlug']]]:
    return self._task_slugs

  @task_slugs.setter
  def task_slugs(self, task_slugs: Optional[List[Optional['ApiBenchmarkTaskSlug']]]):
    if task_slugs is None:
      del self.task_slugs
      return
    if not isinstance(task_slugs, list):
      raise TypeError('task_slugs must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskSlug) for t in task_slugs]):
      raise TypeError('task_slugs must contain only items of type ApiBenchmarkTaskSlug')
    self._task_slugs = task_slugs

  @property
  def model_version_slugs(self) -> Optional[List[str]]:
    return self._model_version_slugs

  @model_version_slugs.setter
  def model_version_slugs(self, model_version_slugs: Optional[List[str]]):
    if model_version_slugs is None:
      del self.model_version_slugs
      return
    if not isinstance(model_version_slugs, list):
      raise TypeError('model_version_slugs must be of type list')
    if not all([isinstance(t, str) for t in model_version_slugs]):
      raise TypeError('model_version_slugs must contain only items of type str')
    self._model_version_slugs = model_version_slugs

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/schedule'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiBatchScheduleBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    results (BatchScheduleBenchmarkModelVersionResult)
  """

  def __init__(self):
    self._results = []
    self._freeze()

  @property
  def results(self) -> Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]:
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, BatchScheduleBenchmarkModelVersionResult) for t in results]):
      raise TypeError('results must contain only items of type BatchScheduleBenchmarkModelVersionResult')
    self._results = results


class ApiBenchmarkTask(KaggleObject):
  r"""
  API equivalent of the BenchmarkTask + BenchmarkTaskVersion from
  benchmark_types.proto.

  Attributes:
    slug (ApiBenchmarkTaskSlug)
      Identifier for the task (+version)
    url (str)
      URL to the created task (or new task version)
    error (str)
      Optional error string.
    creation_state (BenchmarkTaskVersionCreationState)
      Creation state, for now this is essentially the state of the first
      underlying kernel session (SourceKernelSessionId).
    create_time (datetime)
      When this task version was created.
  """

  def __init__(self):
    self._slug = None
    self._url = ""
    self._error = None
    self._creation_state = BenchmarkTaskVersionCreationState.BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED
    self._create_time = None
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    """Identifier for the task (+version)"""
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def url(self) -> str:
    """URL to the created task (or new task version)"""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def error(self) -> str:
    """Optional error string."""
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def creation_state(self) -> 'BenchmarkTaskVersionCreationState':
    r"""
    Creation state, for now this is essentially the state of the first
    underlying kernel session (SourceKernelSessionId).
    """
    return self._creation_state

  @creation_state.setter
  def creation_state(self, creation_state: 'BenchmarkTaskVersionCreationState'):
    if creation_state is None:
      del self.creation_state
      return
    if not isinstance(creation_state, BenchmarkTaskVersionCreationState):
      raise TypeError('creation_state must be of type BenchmarkTaskVersionCreationState')
    self._creation_state = creation_state

  @property
  def create_time(self) -> datetime:
    """When this task version was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time


class ApiBenchmarkTaskRun(KaggleObject):
  r"""
  API equivalent of the BenchmarkTaskRun from benchmark_types.proto.

  Attributes:
    task_slug (ApiBenchmarkTaskSlug)
      Task that was invoked.
    model_version_slug (str)
      Model candidate against the task.
    id (int)
      Run identifier.
    state (BenchmarkTaskRunState)
      State of the run
    start_time (datetime)
      Start time of the run
    end_time (datetime)
      End time of the run
    error_message (str)
      Error message if the run failed
  """

  def __init__(self):
    self._task_slug = None
    self._model_version_slug = ""
    self._id = 0
    self._state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._start_time = None
    self._end_time = None
    self._error_message = None
    self._freeze()

  @property
  def task_slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    """Task that was invoked."""
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: Optional['ApiBenchmarkTaskSlug']):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, ApiBenchmarkTaskSlug):
      raise TypeError('task_slug must be of type ApiBenchmarkTaskSlug')
    self._task_slug = task_slug

  @property
  def model_version_slug(self) -> str:
    """Model candidate against the task."""
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
  def id(self) -> int:
    """Run identifier."""
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
  def state(self) -> 'BenchmarkTaskRunState':
    """State of the run"""
    return self._state

  @state.setter
  def state(self, state: 'BenchmarkTaskRunState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, BenchmarkTaskRunState):
      raise TypeError('state must be of type BenchmarkTaskRunState')
    self._state = state

  @property
  def start_time(self) -> datetime:
    """Start time of the run"""
    return self._start_time or None

  @start_time.setter
  def start_time(self, start_time: Optional[datetime]):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    """End time of the run"""
    return self._end_time or None

  @end_time.setter
  def end_time(self, end_time: Optional[datetime]):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time

  @property
  def error_message(self) -> str:
    """Error message if the run failed"""
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class ApiBenchmarkTaskSlug(KaggleObject):
  r"""
  This is an identifier, equivalent of a task version ID

  Attributes:
    owner_slug (str)
      The owner slug
      If omitted: use the current user's slug
    task_slug (str)
      The task slug
    version_number (int)
      Version number
      If omitted: use the latest version
  """

  def __init__(self):
    self._owner_slug = None
    self._task_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    r"""
    The owner slug
    If omitted: use the current user's slug
    """
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: Optional[str]):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def task_slug(self) -> str:
    """The task slug"""
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: str):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, str):
      raise TypeError('task_slug must be of type str')
    self._task_slug = task_slug

  @property
  def version_number(self) -> int:
    r"""
    Version number
    If omitted: use the latest version
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class ApiCreateBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (str)
      The slug for the task without the user's namespace. (ex: my-task instead of
      username/my-task). This should match the slug in the kaggle-benchmarks
      decorator in the code.
    text (str)
      The task's (or task version's) source code
  """

  def __init__(self):
    self._slug = ""
    self._text = ""
    self._freeze()

  @property
  def slug(self) -> str:
    r"""
    The slug for the task without the user's namespace. (ex: my-task instead of
    username/my-task). This should match the slug in the kaggle-benchmarks
    decorator in the code.
    """
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
  def text(self) -> str:
    """The task's (or task version's) source code"""
    return self._text

  @text.setter
  def text(self, text: str):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/push'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiDownloadBenchmarkTaskRunOutputRequest(KaggleObject):
  r"""
  Attributes:
    run_id (int)
  """

  def __init__(self):
    self._run_id = 0
    self._freeze()

  @property
  def run_id(self) -> int:
    return self._run_id

  @run_id.setter
  def run_id(self, run_id: int):
    if run_id is None:
      del self.run_id
      return
    if not isinstance(run_id, int):
      raise TypeError('run_id must be of type int')
    self._run_id = run_id

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/{run_id}/output'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/tasks/runs/{run_id}/output'


class ApiGetBenchmarkTaskQuotaRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/quota'
    return path.format_map(self.to_field_map(self))


class ApiGetBenchmarkTaskQuotaResponse(KaggleObject):
  r"""
  Attributes:
    daily_quota_used (float)
      How much quota that was used in the time period (daily), in USD.
    total_daily_quota_allowed (float)
      Upper limit of allowed quota in the time period (daily), in USD.
  """

  def __init__(self):
    self._daily_quota_used = 0.0
    self._total_daily_quota_allowed = 0.0
    self._freeze()

  @property
  def daily_quota_used(self) -> float:
    """How much quota that was used in the time period (daily), in USD."""
    return self._daily_quota_used

  @daily_quota_used.setter
  def daily_quota_used(self, daily_quota_used: float):
    if daily_quota_used is None:
      del self.daily_quota_used
      return
    if not isinstance(daily_quota_used, float):
      raise TypeError('daily_quota_used must be of type float')
    self._daily_quota_used = daily_quota_used

  @property
  def total_daily_quota_allowed(self) -> float:
    """Upper limit of allowed quota in the time period (daily), in USD."""
    return self._total_daily_quota_allowed

  @total_daily_quota_allowed.setter
  def total_daily_quota_allowed(self, total_daily_quota_allowed: float):
    if total_daily_quota_allowed is None:
      del self.total_daily_quota_allowed
      return
    if not isinstance(total_daily_quota_allowed, float):
      raise TypeError('total_daily_quota_allowed must be of type float')
    self._total_daily_quota_allowed = total_daily_quota_allowed

  @property
  def dailyQuotaUsed(self):
    return self.daily_quota_used

  @property
  def totalDailyQuotaAllowed(self):
    return self.total_daily_quota_allowed


class ApiGetBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (ApiBenchmarkTaskSlug)
  """

  def __init__(self):
    self._slug = None
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/{slug.task_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/tasks/{slug.task_slug}'


class ApiListBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    task_slug (ApiBenchmarkTaskSlug)
    model_version_slugs (str)
    page_size (int)
    page_token (str)
    skip (int)
  """

  def __init__(self):
    self._task_slug = None
    self._model_version_slugs = []
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._freeze()

  @property
  def task_slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: Optional['ApiBenchmarkTaskSlug']):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, ApiBenchmarkTaskSlug):
      raise TypeError('task_slug must be of type ApiBenchmarkTaskSlug')
    self._task_slug = task_slug

  @property
  def model_version_slugs(self) -> Optional[List[str]]:
    return self._model_version_slugs

  @model_version_slugs.setter
  def model_version_slugs(self, model_version_slugs: Optional[List[str]]):
    if model_version_slugs is None:
      del self.model_version_slugs
      return
    if not isinstance(model_version_slugs, list):
      raise TypeError('model_version_slugs must be of type list')
    if not all([isinstance(t, str) for t in model_version_slugs]):
      raise TypeError('model_version_slugs must contain only items of type str')
    self._model_version_slugs = model_version_slugs

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

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    runs (ApiBenchmarkTaskRun)
    total_results (int)
    next_page_token (str)
  """

  def __init__(self):
    self._runs = []
    self._total_results = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def runs(self) -> Optional[List[Optional['ApiBenchmarkTaskRun']]]:
    return self._runs

  @runs.setter
  def runs(self, runs: Optional[List[Optional['ApiBenchmarkTaskRun']]]):
    if runs is None:
      del self.runs
      return
    if not isinstance(runs, list):
      raise TypeError('runs must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskRun) for t in runs]):
      raise TypeError('runs must contain only items of type ApiBenchmarkTaskRun')
    self._runs = runs

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
  def totalResults(self):
    return self.total_results

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiListBenchmarkTasksRequest(KaggleObject):
  r"""
  Attributes:
    status_filter (str)
      Filter by task creation status (e.g. 'created', 'error').
    regex_filter (str)
      Filter task slugs by regular expression.
  """

  def __init__(self):
    self._status_filter = None
    self._regex_filter = None
    self._freeze()

  @property
  def status_filter(self) -> str:
    """Filter by task creation status (e.g. 'created', 'error')."""
    return self._status_filter or ""

  @status_filter.setter
  def status_filter(self, status_filter: Optional[str]):
    if status_filter is None:
      del self.status_filter
      return
    if not isinstance(status_filter, str):
      raise TypeError('status_filter must be of type str')
    self._status_filter = status_filter

  @property
  def regex_filter(self) -> str:
    """Filter task slugs by regular expression."""
    return self._regex_filter or ""

  @regex_filter.setter
  def regex_filter(self, regex_filter: Optional[str]):
    if regex_filter is None:
      del self.regex_filter
      return
    if not isinstance(regex_filter, str):
      raise TypeError('regex_filter must be of type str')
    self._regex_filter = regex_filter

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkTasksResponse(KaggleObject):
  r"""
  Attributes:
    tasks (ApiBenchmarkTask)
  """

  def __init__(self):
    self._tasks = []
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['ApiBenchmarkTask']]]:
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['ApiBenchmarkTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, ApiBenchmarkTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type ApiBenchmarkTask')
    self._tasks = tasks


ApiBatchScheduleBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("taskSlugs", "task_slugs", "_task_slugs", ApiBenchmarkTaskSlug, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelVersionSlugs", "model_version_slugs", "_model_version_slugs", str, [], ListSerializer(PredefinedSerializer())),
]

ApiBatchScheduleBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("results", "results", "_results", BatchScheduleBenchmarkModelVersionResult, [], ListSerializer(KaggleObjectSerializer())),
]

ApiBenchmarkTask._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationState", "creation_state", "_creation_state", BenchmarkTaskVersionCreationState, BenchmarkTaskVersionCreationState.BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
]

ApiBenchmarkTaskRun._fields = [
  FieldMetadata("taskSlug", "task_slug", "_task_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

ApiBenchmarkTaskSlug._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("taskSlug", "task_slug", "_task_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiCreateBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("text", "text", "_text", str, "", PredefinedSerializer()),
]

ApiDownloadBenchmarkTaskRunOutputRequest._fields = [
  FieldMetadata("runId", "run_id", "_run_id", int, 0, PredefinedSerializer()),
]

ApiGetBenchmarkTaskQuotaRequest._fields = []

ApiGetBenchmarkTaskQuotaResponse._fields = [
  FieldMetadata("dailyQuotaUsed", "daily_quota_used", "_daily_quota_used", float, 0.0, PredefinedSerializer()),
  FieldMetadata("totalDailyQuotaAllowed", "total_daily_quota_allowed", "_total_daily_quota_allowed", float, 0.0, PredefinedSerializer()),
]

ApiGetBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
]

ApiListBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("taskSlug", "task_slug", "_task_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionSlugs", "model_version_slugs", "_model_version_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
]

ApiListBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("runs", "runs", "_runs", ApiBenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListBenchmarkTasksRequest._fields = [
  FieldMetadata("statusFilter", "status_filter", "_status_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regexFilter", "regex_filter", "_regex_filter", str, None, PredefinedSerializer(), optional=True),
]

ApiListBenchmarkTasksResponse._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", ApiBenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
]

