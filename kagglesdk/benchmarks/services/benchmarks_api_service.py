from kagglesdk.benchmarks.types.benchmarks_api_service import ApiBenchmarkLeaderboard, ApiBenchmarkModelVersionConfig, ApiCreateBenchmarkModelVersionConfigRequest, ApiGetBenchmarkLeaderboardRequest, ApiGetBenchmarkModelVersionConfigRequest, ApiListBenchmarkModelsRequest, ApiListBenchmarkModelsResponse, ApiListBenchmarkModelVersionConfigsRequest, ApiListBenchmarkModelVersionConfigsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarksApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_model_version_config(self, request: ApiCreateBenchmarkModelVersionConfigRequest = None) -> ApiBenchmarkModelVersionConfig:
    r"""
    Create a fully-configured, runnable BenchmarkModelVersion: pins the
    exact sampling/decoding parameters (temperature, top-p, reasoning effort,
    etc.) used when invoking the parent BenchmarkModelVersion.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST
        http://localhost/api/v1/benchmarks/models/versions/configs/create \
        -H 'Content-Type: application/json' \
        -d '{
          'config': {
            'benchmarkModelVersionId': 1,
            'displayName': 'Claude Opus 4.8 High Reasoning Effort',
            'slug': 'claude-opus-4.8-high-reasoning-effort',
            'reasoningEffort': 'high',
            'temperature': 1.0,
            'topP': 1.0,
            'maxOutputTokens': 8192
          }
        }'

    Args:
      request (ApiCreateBenchmarkModelVersionConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateBenchmarkModelVersionConfigRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "CreateBenchmarkModelVersionConfig", request, ApiBenchmarkModelVersionConfig)

  def get_benchmark_model_version_config(self, request: ApiGetBenchmarkModelVersionConfigRequest = None) -> ApiBenchmarkModelVersionConfig:
    r"""
    Get a BenchmarkModelVersionConfig by id.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        http://localhost/api/v1/benchmarks/models/versions/configs/1

    Args:
      request (ApiGetBenchmarkModelVersionConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkModelVersionConfigRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "GetBenchmarkModelVersionConfig", request, ApiBenchmarkModelVersionConfig)

  def list_benchmark_model_version_configs(self, request: ApiListBenchmarkModelVersionConfigsRequest = None) -> ApiListBenchmarkModelVersionConfigsResponse:
    r"""
    List BenchmarkModelVersionConfigs, optionally filtered by parent
    BenchmarkModelVersion id(s). Paginated.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -G http://localhost/api/v1/benchmarks/models/versions/configs/list \
        --data-urlencode 'benchmarkModelVersionIds=1' \
        --data-urlencode 'pageSize=20'

    Args:
      request (ApiListBenchmarkModelVersionConfigsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkModelVersionConfigsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "ListBenchmarkModelVersionConfigs", request, ApiListBenchmarkModelVersionConfigsResponse)

  def get_benchmark_leaderboard(self, request: ApiGetBenchmarkLeaderboardRequest = None) -> ApiBenchmarkLeaderboard:
    r"""
    Args:
      request (ApiGetBenchmarkLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkLeaderboardRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "GetBenchmarkLeaderboard", request, ApiBenchmarkLeaderboard)

  def list_benchmark_models(self, request: ApiListBenchmarkModelsRequest = None) -> ApiListBenchmarkModelsResponse:
    r"""
    Args:
      request (ApiListBenchmarkModelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkModelsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "ListBenchmarkModels", request, ApiListBenchmarkModelsResponse)
