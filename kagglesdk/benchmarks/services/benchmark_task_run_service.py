from kagglesdk.benchmarks.types.benchmark_task_run_service import BatchScheduleBenchmarkTaskRunsRequest, BatchScheduleBenchmarkTaskRunsResponse, CreateBenchmarkTaskRunsRequest, CreateBenchmarkTaskRunsResponse, DeleteBenchmarkTaskRunRequest, GetBenchmarkTaskRunRequest, ListBenchmarkTaskRunsRequest, ListBenchmarkTaskRunsResponse
from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkTaskRunClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_task_runs(self, request: CreateBenchmarkTaskRunsRequest = None) -> CreateBenchmarkTaskRunsResponse:
    r"""
    Args:
      request (CreateBenchmarkTaskRunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkTaskRunsRequest()

    return self._client.call("benchmarks.BenchmarkTaskRunService", "CreateBenchmarkTaskRuns", request, CreateBenchmarkTaskRunsResponse)

  def delete_benchmark_task_run(self, request: DeleteBenchmarkTaskRunRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkTaskRunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkTaskRunRequest()

    self._client.call("benchmarks.BenchmarkTaskRunService", "DeleteBenchmarkTaskRun", request, None)

  def list_benchmark_task_runs(self, request: ListBenchmarkTaskRunsRequest = None) -> ListBenchmarkTaskRunsResponse:
    r"""
    Args:
      request (ListBenchmarkTaskRunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkTaskRunsRequest()

    return self._client.call("benchmarks.BenchmarkTaskRunService", "ListBenchmarkTaskRuns", request, ListBenchmarkTaskRunsResponse)

  def get_benchmark_task_run(self, request: GetBenchmarkTaskRunRequest = None) -> FileDownload:
    r"""
    Args:
      request (GetBenchmarkTaskRunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkTaskRunRequest()

    return self._client.call("benchmarks.BenchmarkTaskRunService", "GetBenchmarkTaskRun", request, FileDownload)

  def batch_schedule_benchmark_task_runs(self, request: BatchScheduleBenchmarkTaskRunsRequest = None) -> BatchScheduleBenchmarkTaskRunsResponse:
    r"""
    Args:
      request (BatchScheduleBenchmarkTaskRunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchScheduleBenchmarkTaskRunsRequest()

    return self._client.call("benchmarks.BenchmarkTaskRunService", "BatchScheduleBenchmarkTaskRuns", request, BatchScheduleBenchmarkTaskRunsResponse)
