from kagglesdk.benchmarks.types.benchmark_task_service import AddBenchmarkTaskTagRequest, BatchDeleteBenchmarkTaskVersionsRequest, CreateBenchmarkTaskFromKernelSessionRequest, CreateBenchmarkTaskFromPromptRequest, CreateBenchmarkTaskFromPromptResponse, CreateBenchmarkTaskVersionMappingsRequest, CreateBenchmarkTaskVersionMappingsResponse, DeleteBenchmarkTaskRequest, DeleteBenchmarkTaskVersionMappingsRequest, DeleteBenchmarkTaskVersionMappingsResponse, DeleteBenchmarkTaskVersionRequest, GetBenchmarkTaskRequest, GetTaskRecommendationsRequest, GetTaskRecommendationsResponse, GetUserBenchmarkTaskCountsRequest, GetUserBenchmarkTaskCountsResponse, IncrementBenchmarkTaskViewCountRequest, ListBenchmarkTasksRequest, ListBenchmarkTasksResponse, ListBenchmarkTaskVersionsRequest, ListBenchmarkTaskVersionsResponse, RemoveBenchmarkTaskTagRequest, RestoreBenchmarkTaskRequest, RestoreBenchmarkTaskVersionRequest, UpdateBenchmarkTaskRequest, UpdateBenchmarkTaskTagsRequest, UpdateBenchmarkTaskVersionRequest, ValidateSaveBenchmarkTaskRequest, ValidateSaveBenchmarkTaskResponse
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkTask, BenchmarkTaskVersion
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkTaskClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_task_from_kernel_session(self, request: CreateBenchmarkTaskFromKernelSessionRequest = None) -> BenchmarkTask:
    r"""
    Args:
      request (CreateBenchmarkTaskFromKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkTaskFromKernelSessionRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "CreateBenchmarkTaskFromKernelSession", request, BenchmarkTask)

  def validate_save_benchmark_task(self, request: ValidateSaveBenchmarkTaskRequest = None) -> ValidateSaveBenchmarkTaskResponse:
    r"""
    CreateBenchmarkTask happens at the end of a (long) kernel save,
    this is a pre-save validator to improve the chance the save is successful.

    Args:
      request (ValidateSaveBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ValidateSaveBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "ValidateSaveBenchmarkTask", request, ValidateSaveBenchmarkTaskResponse)

  def get_benchmark_task(self, request: GetBenchmarkTaskRequest = None) -> BenchmarkTask:
    r"""
    Args:
      request (GetBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "GetBenchmarkTask", request, BenchmarkTask)

  def list_benchmark_tasks(self, request: ListBenchmarkTasksRequest = None) -> ListBenchmarkTasksResponse:
    r"""
    Args:
      request (ListBenchmarkTasksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkTasksRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "ListBenchmarkTasks", request, ListBenchmarkTasksResponse)

  def list_benchmark_task_versions(self, request: ListBenchmarkTaskVersionsRequest = None) -> ListBenchmarkTaskVersionsResponse:
    r"""
    Args:
      request (ListBenchmarkTaskVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkTaskVersionsRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "ListBenchmarkTaskVersions", request, ListBenchmarkTaskVersionsResponse)

  def update_benchmark_task(self, request: UpdateBenchmarkTaskRequest = None) -> BenchmarkTask:
    r"""
    Args:
      request (UpdateBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "UpdateBenchmarkTask", request, BenchmarkTask)

  def update_benchmark_task_version(self, request: UpdateBenchmarkTaskVersionRequest = None) -> BenchmarkTaskVersion:
    r"""
    TODO(bml): Define authz and business logic.

    Args:
      request (UpdateBenchmarkTaskVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkTaskVersionRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "UpdateBenchmarkTaskVersion", request, BenchmarkTaskVersion)

  def delete_benchmark_task(self, request: DeleteBenchmarkTaskRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkTaskRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "DeleteBenchmarkTask", request, None)

  def delete_benchmark_task_version(self, request: DeleteBenchmarkTaskVersionRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkTaskVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkTaskVersionRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "DeleteBenchmarkTaskVersion", request, None)

  def batch_delete_benchmark_task_versions(self, request: BatchDeleteBenchmarkTaskVersionsRequest = None):
    r"""
    Args:
      request (BatchDeleteBenchmarkTaskVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteBenchmarkTaskVersionsRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "BatchDeleteBenchmarkTaskVersions", request, None)

  def create_benchmark_task_version_mappings(self, request: CreateBenchmarkTaskVersionMappingsRequest = None) -> CreateBenchmarkTaskVersionMappingsResponse:
    r"""
    Args:
      request (CreateBenchmarkTaskVersionMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkTaskVersionMappingsRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "CreateBenchmarkTaskVersionMappings", request, CreateBenchmarkTaskVersionMappingsResponse)

  def delete_benchmark_task_version_mappings(self, request: DeleteBenchmarkTaskVersionMappingsRequest = None) -> DeleteBenchmarkTaskVersionMappingsResponse:
    r"""
    Args:
      request (DeleteBenchmarkTaskVersionMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkTaskVersionMappingsRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "DeleteBenchmarkTaskVersionMappings", request, DeleteBenchmarkTaskVersionMappingsResponse)

  def create_benchmark_task_from_prompt(self, request: CreateBenchmarkTaskFromPromptRequest = None) -> CreateBenchmarkTaskFromPromptResponse:
    r"""
    Args:
      request (CreateBenchmarkTaskFromPromptRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkTaskFromPromptRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "CreateBenchmarkTaskFromPrompt", request, CreateBenchmarkTaskFromPromptResponse)

  def get_task_recommendations(self, request: GetTaskRecommendationsRequest = None) -> GetTaskRecommendationsResponse:
    r"""
    Args:
      request (GetTaskRecommendationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTaskRecommendationsRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "GetTaskRecommendations", request, GetTaskRecommendationsResponse)

  def add_benchmark_task_tag(self, request: AddBenchmarkTaskTagRequest = None):
    r"""
    Args:
      request (AddBenchmarkTaskTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddBenchmarkTaskTagRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "AddBenchmarkTaskTag", request, None)

  def remove_benchmark_task_tag(self, request: RemoveBenchmarkTaskTagRequest = None):
    r"""
    Args:
      request (RemoveBenchmarkTaskTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveBenchmarkTaskTagRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "RemoveBenchmarkTaskTag", request, None)

  def update_benchmark_task_tags(self, request: UpdateBenchmarkTaskTagsRequest = None):
    r"""
    Args:
      request (UpdateBenchmarkTaskTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkTaskTagsRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "UpdateBenchmarkTaskTags", request, None)

  def restore_benchmark_task(self, request: RestoreBenchmarkTaskRequest = None):
    r"""
    Restore a moderated benchmark task, such as after a successful user appeal.
    Note: Also restores on moderated task versions. If you want to restore just
    one specific task version, call RestoreBenchmarkTaskVersion instead.

    Args:
      request (RestoreBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RestoreBenchmarkTaskRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "RestoreBenchmarkTask", request, None)

  def restore_benchmark_task_version(self, request: RestoreBenchmarkTaskVersionRequest = None):
    r"""
    Restore a moderated benchmark task version and associated task runs, ex:
    after a successful user appeal.

    Args:
      request (RestoreBenchmarkTaskVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RestoreBenchmarkTaskVersionRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "RestoreBenchmarkTaskVersion", request, None)

  def get_user_benchmark_task_counts(self, request: GetUserBenchmarkTaskCountsRequest = None) -> GetUserBenchmarkTaskCountsResponse:
    r"""
    Args:
      request (GetUserBenchmarkTaskCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserBenchmarkTaskCountsRequest()

    return self._client.call("benchmarks.BenchmarkTaskService", "GetUserBenchmarkTaskCounts", request, GetUserBenchmarkTaskCountsResponse)

  def increment_benchmark_task_view_count(self, request: IncrementBenchmarkTaskViewCountRequest = None):
    r"""
    Args:
      request (IncrementBenchmarkTaskViewCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = IncrementBenchmarkTaskViewCountRequest()

    self._client.call("benchmarks.BenchmarkTaskService", "IncrementBenchmarkTaskViewCount", request, None)
