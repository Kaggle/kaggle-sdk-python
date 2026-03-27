from kagglesdk.benchmarks.types.benchmark_model_service import CreateBenchmarkModelRequest, CreateBenchmarkModelVersionRequest, DeleteBenchmarkModelRequest, DeleteBenchmarkModelVersionRequest, GetBenchmarkModelThumbnailsRequest, GetBenchmarkModelThumbnailsResponse, ListBenchmarkModelsRequest, ListBenchmarkModelsResponse, UpdateBenchmarkModelRequest, UpdateBenchmarkModelVersionRequest
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkModel, BenchmarkModelVersion
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkModelClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_model(self, request: CreateBenchmarkModelRequest = None) -> BenchmarkModel:
    r"""
    Args:
      request (CreateBenchmarkModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkModelRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "CreateBenchmarkModel", request, BenchmarkModel)

  def create_benchmark_model_version(self, request: CreateBenchmarkModelVersionRequest = None) -> BenchmarkModelVersion:
    r"""
    Args:
      request (CreateBenchmarkModelVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkModelVersionRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "CreateBenchmarkModelVersion", request, BenchmarkModelVersion)

  def update_benchmark_model(self, request: UpdateBenchmarkModelRequest = None) -> BenchmarkModel:
    r"""
    Args:
      request (UpdateBenchmarkModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkModelRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "UpdateBenchmarkModel", request, BenchmarkModel)

  def update_benchmark_model_version(self, request: UpdateBenchmarkModelVersionRequest = None) -> BenchmarkModelVersion:
    r"""
    Args:
      request (UpdateBenchmarkModelVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkModelVersionRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "UpdateBenchmarkModelVersion", request, BenchmarkModelVersion)

  def delete_benchmark_model(self, request: DeleteBenchmarkModelRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkModelRequest()

    self._client.call("benchmarks.BenchmarkModelService", "DeleteBenchmarkModel", request, None)

  def delete_benchmark_model_version(self, request: DeleteBenchmarkModelVersionRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkModelVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkModelVersionRequest()

    self._client.call("benchmarks.BenchmarkModelService", "DeleteBenchmarkModelVersion", request, None)

  def list_benchmark_models(self, request: ListBenchmarkModelsRequest = None) -> ListBenchmarkModelsResponse:
    r"""
    Args:
      request (ListBenchmarkModelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkModelsRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "ListBenchmarkModels", request, ListBenchmarkModelsResponse)

  def get_benchmark_model_thumbnails(self, request: GetBenchmarkModelThumbnailsRequest = None) -> GetBenchmarkModelThumbnailsResponse:
    r"""
    Resolves model proxy slugs (e.g. 'google/gemini-2.5-flash') to their
    organization thumbnail URLs. Used by the task run conversation view to
    display the correct model icon for multi-model (PvP) benchmarks.

    Args:
      request (GetBenchmarkModelThumbnailsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkModelThumbnailsRequest()

    return self._client.call("benchmarks.BenchmarkModelService", "GetBenchmarkModelThumbnails", request, GetBenchmarkModelThumbnailsResponse)
