from kagglesdk.benchmarks.types.benchmark_tasks_api_service import ApiBatchScheduleBenchmarkTaskRunsRequest, ApiBatchScheduleBenchmarkTaskRunsResponse, ApiBenchmarkTask, ApiCreateBenchmarkTaskRequest, ApiDownloadBenchmarkTaskRunOutputRequest, ApiGetBenchmarkTaskQuotaRequest, ApiGetBenchmarkTaskQuotaResponse, ApiGetBenchmarkTaskRequest, ApiGetBenchmarkTaskRunLogsRequest, ApiListBenchmarkTaskRunsRequest, ApiListBenchmarkTaskRunsResponse, ApiListBenchmarkTasksRequest, ApiListBenchmarkTasksResponse, ApiPublishBenchmarkTaskRequest
from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkTasksApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_task(self, request: ApiCreateBenchmarkTaskRequest = None) -> ApiBenchmarkTask:
    r"""
    For the given slug:
     * if it exists: creates a new task version (under the existing task)
     * if it does not exist: creates a new task (and 1st task version)

    Args:
      request (ApiCreateBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "CreateBenchmarkTask", request, ApiBenchmarkTask)

  def batch_schedule_benchmark_task_runs(self, request: ApiBatchScheduleBenchmarkTaskRunsRequest = None) -> ApiBatchScheduleBenchmarkTaskRunsResponse:
    r"""
    Schedules runs for a set of tasks against a set of models.

    Args:
      request (ApiBatchScheduleBenchmarkTaskRunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiBatchScheduleBenchmarkTaskRunsRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "BatchScheduleBenchmarkTaskRuns", request, ApiBatchScheduleBenchmarkTaskRunsResponse)

  def list_benchmark_tasks(self, request: ApiListBenchmarkTasksRequest = None) -> ApiListBenchmarkTasksResponse:
    r"""
    List tasks for the current user.

    Args:
      request (ApiListBenchmarkTasksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkTasksRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "ListBenchmarkTasks", request, ApiListBenchmarkTasksResponse)

  def get_benchmark_task(self, request: ApiGetBenchmarkTaskRequest = None) -> ApiBenchmarkTask:
    r"""
    Get a particular task for a user.

    Args:
      request (ApiGetBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "GetBenchmarkTask", request, ApiBenchmarkTask)

  def list_benchmark_task_runs(self, request: ApiListBenchmarkTaskRunsRequest = None) -> ApiListBenchmarkTaskRunsResponse:
    r"""
    List runs for a particular task.

    Args:
      request (ApiListBenchmarkTaskRunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkTaskRunsRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "ListBenchmarkTaskRuns", request, ApiListBenchmarkTaskRunsResponse)

  def download_benchmark_task_run_output(self, request: ApiDownloadBenchmarkTaskRunOutputRequest = None) -> FileDownload:
    r"""
    Download output files for a completed task run.

    Args:
      request (ApiDownloadBenchmarkTaskRunOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadBenchmarkTaskRunOutputRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "DownloadBenchmarkTaskRunOutput", request, FileDownload)

  def get_benchmark_task_run_logs(self, request: ApiGetBenchmarkTaskRunLogsRequest = None) -> FileDownload:
    r"""
    Get execution logs for a task run.

    While the underlying notebook session is still running, the response is
    a Server-Sent Events stream (Content-Type: text/event-stream). Once the
    session has terminated, the persisted log file is returned as written by
    the worker (Content-Type: application/json). Callers (e.g. the Kaggle
    CLI) should branch on the response Content-Type.

    Args:
      request (ApiGetBenchmarkTaskRunLogsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkTaskRunLogsRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "GetBenchmarkTaskRunLogs", request, FileDownload)

  def get_benchmark_task_quota(self, request: ApiGetBenchmarkTaskQuotaRequest = None) -> ApiGetBenchmarkTaskQuotaResponse:
    r"""
    Return the current user's model proxy quota.

    Args:
      request (ApiGetBenchmarkTaskQuotaRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkTaskQuotaRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "GetBenchmarkTaskQuota", request, ApiGetBenchmarkTaskQuotaResponse)

  def publish_benchmark_task(self, request: ApiPublishBenchmarkTaskRequest = None) -> ApiBenchmarkTask:
    r"""
    Publish a particular task for a user. Optionally publishes the backing
    notebook (`source_kernel_id`) in the same request.

    Args:
      request (ApiPublishBenchmarkTaskRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiPublishBenchmarkTaskRequest()

    return self._client.call("benchmarks.BenchmarkTasksApiService", "PublishBenchmarkTask", request, ApiBenchmarkTask)
