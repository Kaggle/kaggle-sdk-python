from kagglesdk.benchmarks.types.benchmarks_api_service import ApiBenchmarkLeaderboard, ApiBenchmarkModelVersionConfig, ApiCreateBenchmarkModelVersionConfigRequest, ApiCreateBenchmarkVersionAgentMappingsRequest, ApiCreateBenchmarkVersionAgentMappingsResponse, ApiDeleteBenchmarkVersionAgentMappingsRequest, ApiDeleteBenchmarkVersionAgentMappingsResponse, ApiGetBenchmarkLeaderboardRequest, ApiGetBenchmarkModelVersionConfigRequest, ApiListBenchmarkModelsRequest, ApiListBenchmarkModelsResponse, ApiListBenchmarkModelVersionConfigsRequest, ApiListBenchmarkModelVersionConfigsResponse, ApiListBenchmarkVersionAgentMappingsRequest, ApiListBenchmarkVersionAgentMappingsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarksApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_model_version_config(self, request: ApiCreateBenchmarkModelVersionConfigRequest = None) -> ApiBenchmarkModelVersionConfig:
    r"""
    Create a fully-configured, runnable BenchmarkModelVersion: pins the
    exact sampling/decoding parameters (reasoning effort, etc.) used when
    invoking the parent BenchmarkModelVersion.

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
            'reasoningEffort': 'high'
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

  def create_benchmark_version_agent_mappings(self, request: ApiCreateBenchmarkVersionAgentMappingsRequest = None) -> ApiCreateBenchmarkVersionAgentMappingsResponse:
    r"""
    Map one or more Agents into a BenchmarkVersion, making them participants
    on that version's leaderboard. Requires update access to the parent
    BenchmarkVersion and read access to each Agent. Remapping an agent whose
    mapping was previously soft-deleted revives the existing row.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/versions/agent-mappings/create \
        -H 'Content-Type: application/json' \
        -d '{
          'mappings': [
            {
              'parentBenchmarkVersionId': 1,
              'childAgentId': 1,
              'type': 'BENCHMARK_VERSION_AGENT_MAPPING_TYPE_PRINCIPAL'
            }
          ]
        }'

    Args:
      request (ApiCreateBenchmarkVersionAgentMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateBenchmarkVersionAgentMappingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "CreateBenchmarkVersionAgentMappings", request, ApiCreateBenchmarkVersionAgentMappingsResponse)

  def delete_benchmark_version_agent_mappings(self, request: ApiDeleteBenchmarkVersionAgentMappingsRequest = None) -> ApiDeleteBenchmarkVersionAgentMappingsResponse:
    r"""
    Soft-delete Agent mappings from a BenchmarkVersion, removing those agents
    from the version's leaderboard. Does NOT affect the Agents themselves or
    any BenchmarkRuns they already produced. Requires update access to the
    parent BenchmarkVersion. Uses POST rather than DELETE because the
    mappings to remove are supplied in the body.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/versions/agent-mappings/delete \
        -H 'Content-Type: application/json' \
        -d '{
          'mappings': [
            {
              'parentBenchmarkVersionId': 1,
              'childAgentId': 1
            }
          ]
        }'

    Args:
      request (ApiDeleteBenchmarkVersionAgentMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteBenchmarkVersionAgentMappingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "DeleteBenchmarkVersionAgentMappings", request, ApiDeleteBenchmarkVersionAgentMappingsResponse)

  def list_benchmark_version_agent_mappings(self, request: ApiListBenchmarkVersionAgentMappingsRequest = None) -> ApiListBenchmarkVersionAgentMappingsResponse:
    r"""
    List the Agent mappings of BenchmarkVersions, optionally filtered by
    parent BenchmarkVersion id(s) and/or child Agent id(s). Soft-deleted
    mappings are excluded. Paginated.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -G http://localhost/api/v1/benchmarks/versions/agent-mappings/list \
        --data-urlencode 'filter.parentBenchmarkVersionIds=1' \
        --data-urlencode 'pageSize=20'

    Args:
      request (ApiListBenchmarkVersionAgentMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkVersionAgentMappingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "ListBenchmarkVersionAgentMappings", request, ApiListBenchmarkVersionAgentMappingsResponse)
