from kagglesdk.benchmarks.types.benchmark_types import BenchmarkArenaSettings
from kagglesdk.benchmarks.types.benchmarks_api_service import ApiAddTasksToBenchmarkRequest, ApiAddTasksToBenchmarkResponse, ApiBenchmarkLeaderboard, ApiBenchmarkModelVersionConfig, ApiCreateBenchmarkArenaSettingsRequest, ApiCreateBenchmarkModelVersionConfigRequest, ApiCreateBenchmarkVersionAgentMappingsRequest, ApiCreateBenchmarkVersionAgentMappingsResponse, ApiDeleteBenchmarkVersionAgentMappingsRequest, ApiDeleteBenchmarkVersionAgentMappingsResponse, ApiGetBenchmarkArenaSettingsRequest, ApiGetBenchmarkLeaderboardRequest, ApiGetBenchmarkModelVersionConfigRequest, ApiListBenchmarkArenaCombinationsRequest, ApiListBenchmarkArenaCombinationsResponse, ApiListBenchmarkModelsRequest, ApiListBenchmarkModelsResponse, ApiListBenchmarkModelVersionConfigsRequest, ApiListBenchmarkModelVersionConfigsResponse, ApiListBenchmarkVersionAgentMappingsRequest, ApiListBenchmarkVersionAgentMappingsResponse, ApiRegisterAuxiliaryModelVersionConfigsRequest, ApiRemoveTasksFromBenchmarkRequest, ApiRemoveTasksFromBenchmarkResponse, ApiUnregisterAuxiliaryModelVersionConfigsRequest, ApiUpdateBenchmarkArenaCombinationsRequest, ApiUpdateBenchmarkArenaSettingsRequest
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

  def add_tasks_to_benchmark(self, request: ApiAddTasksToBenchmarkRequest = None) -> ApiAddTasksToBenchmarkResponse:
    r"""
    Map one or more BenchmarkTasks into one of the current user's own
    benchmarks, making them part of that benchmark's task tree and
    leaderboard. Requires update access to the benchmark version and read
    access to each task. Tasks already mapped to the benchmark are skipped and
    echoed back in `skipped_tasks` rather than failing the request, so a
    partially-applied bulk import can be safely re-run.

    Example:
      curl -sSL -u fickleone:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/my-benchmark/tasks/add \
        -H 'Content-Type: application/json' \
        -d '{
          'taskSlugs': [
            {'taskSlug': 'count-letters'},
            {'ownerSlug': 'bob', 'taskSlug': 'sort-list', 'versionNumber': 2}
          ]
        }'

    Args:
      request (ApiAddTasksToBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiAddTasksToBenchmarkRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "AddTasksToBenchmark", request, ApiAddTasksToBenchmarkResponse)

  def remove_tasks_from_benchmark(self, request: ApiRemoveTasksFromBenchmarkRequest = None) -> ApiRemoveTasksFromBenchmarkResponse:
    r"""
    Unmap one or more BenchmarkTasks from one of the current user's own
    benchmarks, removing them from that benchmark's task tree and leaderboard.
    Requires update access to the benchmark version and read access to each
    task. Tasks not currently mapped to the benchmark are skipped and echoed
    back in `skipped_tasks` rather than failing the request, so a
    partially-applied bulk removal can be safely re-run.

    Example:
      curl -sSL -u fickleone:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/my-benchmark/tasks/remove \
        -H 'Content-Type: application/json' \
        -d '{
          'taskSlugs': [
            {'taskSlug': 'count-letters'},
            {'ownerSlug': 'bob', 'taskSlug': 'sort-list', 'versionNumber': 2}
          ]
        }'

    Args:
      request (ApiRemoveTasksFromBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiRemoveTasksFromBenchmarkRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "RemoveTasksFromBenchmark", request, ApiRemoveTasksFromBenchmarkResponse)

  def register_auxiliary_model_version_configs(self, request: ApiRegisterAuxiliaryModelVersionConfigsRequest = None):
    r"""
    Retroactively records auxiliary BenchmarkModelVersionConfigs a task version
    invokes beyond the candidate (e.g. LLM judges), for authors who did not
    declare them at creation time. The task is resolved under the current user;
    configs are addressed by slug. Additive and idempotent: configs already
    registered on the version are skipped.

    Args:
      request (ApiRegisterAuxiliaryModelVersionConfigsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiRegisterAuxiliaryModelVersionConfigsRequest()

    self._client.call("benchmarks.BenchmarksApiService", "RegisterAuxiliaryModelVersionConfigs", request, None)

  def unregister_auxiliary_model_version_configs(self, request: ApiUnregisterAuxiliaryModelVersionConfigsRequest = None):
    r"""
    Removes previously-registered auxiliary BenchmarkModelVersionConfigs from a
    task version. The task is resolved under the current user; configs are
    addressed by slug. Idempotent: configs not currently registered are
    ignored.

    Args:
      request (ApiUnregisterAuxiliaryModelVersionConfigsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUnregisterAuxiliaryModelVersionConfigsRequest()

    self._client.call("benchmarks.BenchmarksApiService", "UnregisterAuxiliaryModelVersionConfigs", request, None)

  def get_benchmark_arena_settings(self, request: ApiGetBenchmarkArenaSettingsRequest = None) -> BenchmarkArenaSettings:
    r"""
    Get a benchmark version's arena settings. Requires update access to the
    benchmark version. Returns NOT_FOUND if the version has no arena.

    Example:
      curl -sSL -u fickleone:local_api_token \
        http://localhost/api/v1/benchmarks/fickleone/my-benchmark/arena/settings

    Args:
      request (ApiGetBenchmarkArenaSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetBenchmarkArenaSettingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "GetBenchmarkArenaSettings", request, BenchmarkArenaSettings)

  def create_benchmark_arena_settings(self, request: ApiCreateBenchmarkArenaSettingsRequest = None) -> BenchmarkArenaSettings:
    r"""
    Create a benchmark version's arena. Requires update access to the
    benchmark version.

    Example:
      curl -sSL -u fickleone:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/fickleone/my-benchmark/arena/settings/create
        \
        -H 'Content-Type: application/json' \
        -d '{
          'settings': {
            'artifactPath': '*.mp4',
            'artifactType': 'BENCHMARK_ARENA_ARTIFACT_TYPE_VIDEO',
            'revealCandidates': true
          }
        }'

    Args:
      request (ApiCreateBenchmarkArenaSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateBenchmarkArenaSettingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "CreateBenchmarkArenaSettings", request, BenchmarkArenaSettings)

  def update_benchmark_arena_settings(self, request: ApiUpdateBenchmarkArenaSettingsRequest = None) -> BenchmarkArenaSettings:
    r"""
    Update a benchmark version's arena settings. Requires update access to the
    benchmark version.

    Example:
      curl -sSL -u fickleone:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/fickleone/my-benchmark/arena/settings/update
        \
        -H 'Content-Type: application/json' \
        -d '{
          'settings': {'votingEnabled': true},
          'updateMask': 'votingEnabled'
        }'

    Args:
      request (ApiUpdateBenchmarkArenaSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateBenchmarkArenaSettingsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "UpdateBenchmarkArenaSettings", request, BenchmarkArenaSettings)

  def list_benchmark_arena_combinations(self, request: ApiListBenchmarkArenaCombinationsRequest = None) -> ApiListBenchmarkArenaCombinationsResponse:
    r"""
    List the (task version, candidate) combinations opted into a benchmark
    version's arena. Requires update access to the benchmark version.

    Example:
      curl -sSL -u fickleone:local_api_token \
        http://localhost/api/v1/benchmarks/fickleone/my-benchmark/arena/combinations

    Args:
      request (ApiListBenchmarkArenaCombinationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkArenaCombinationsRequest()

    return self._client.call("benchmarks.BenchmarksApiService", "ListBenchmarkArenaCombinations", request, ApiListBenchmarkArenaCombinationsResponse)

  def update_benchmark_arena_combinations(self, request: ApiUpdateBenchmarkArenaCombinationsRequest = None):
    r"""
    Opt (task version, candidate) combinations into or out of a benchmark
    version's arena. Requires update access to the benchmark version and read
    access to each candidate added.

    Example:
      curl -sSL -u fickleone:local_api_token \
        -X POST \
        http://localhost/api/v1/benchmarks/fickleone/my-benchmark/arena/combinations/update
        \
        -H 'Content-Type: application/json' \
        -d '{
          'add': [
            {'taskVersionId': 1, 'candidate': {'benchmarkModelVersionId': 2}}
          ]
        }'

    Args:
      request (ApiUpdateBenchmarkArenaCombinationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateBenchmarkArenaCombinationsRequest()

    self._client.call("benchmarks.BenchmarksApiService", "UpdateBenchmarkArenaCombinations", request, None)
