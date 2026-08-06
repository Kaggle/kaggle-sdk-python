from kagglesdk.agents.types.agents_api_service import ApiAgent, ApiCreateAgentRequest, ApiCreateHarnessRequest, ApiCreateHarnessVersionRequest, ApiGetAgentRequest, ApiGetHarnessRequest, ApiGetHarnessVersionRequest, ApiHarness, ApiHarnessVersion, ApiListAgentsRequest, ApiListAgentsResponse, ApiListHarnessesRequest, ApiListHarnessesResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AgentsApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_harness(self, request: ApiCreateHarnessRequest = None) -> ApiHarness:
    r"""
    Create a Harness together with its (required) first HarnessVersion.
    Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST http://localhost/api/v1/agents/harnesses/create \
        -H 'Content-Type: application/json' \
        -d '{
          'harness': {
            'displayName': 'Claude Code',
            'slug': 'claude-code',
            'isPublic': false,
            'type': 'HARNESS_TYPE_HARBOR_CANONICAL',
            'version': {
              'displayName': 'Claude Code v2.1.216',
              'slug': 'claude-code-2.1.216',
              'isPublic': false,
              'harborCanonical': {
                'harborSlug': 'claude-code',
                'harborVersionSlug': '2.1.216'
              }
            }
          }
        }'

    Args:
      request (ApiCreateHarnessRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateHarnessRequest()

    return self._client.call("agents.AgentsApiService", "CreateHarness", request, ApiHarness)

  def get_harness(self, request: ApiGetHarnessRequest = None) -> ApiHarness:
    r"""
    Get a Harness by id. Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        http://localhost/api/v1/agents/harnesses/1

    Args:
      request (ApiGetHarnessRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetHarnessRequest()

    return self._client.call("agents.AgentsApiService", "GetHarness", request, ApiHarness)

  def create_harness_version(self, request: ApiCreateHarnessVersionRequest = None) -> ApiHarnessVersion:
    r"""
    Create an additional HarnessVersion under an existing Harness.
    Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST http://localhost/api/v1/agents/harnesses/versions/create \
        -H 'Content-Type: application/json' \
        -d '{
          'harnessVersion': {
            'harnessId': 1,
            'displayName': 'Claude Code v2.1.217',
            'slug': 'claude-code-2.1.217',
            'isPublic': false,
            'harborCanonical': {
              'harborSlug': 'claude-code',
              'harborVersionSlug': '2.1.217'
            }
          }
        }'

    Args:
      request (ApiCreateHarnessVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateHarnessVersionRequest()

    return self._client.call("agents.AgentsApiService", "CreateHarnessVersion", request, ApiHarnessVersion)

  def get_harness_version(self, request: ApiGetHarnessVersionRequest = None) -> ApiHarnessVersion:
    r"""
    Get a HarnessVersion by id. Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        http://localhost/api/v1/agents/harnesses/versions/1

    Args:
      request (ApiGetHarnessVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetHarnessVersionRequest()

    return self._client.call("agents.AgentsApiService", "GetHarnessVersion", request, ApiHarnessVersion)

  def list_harnesses(self, request: ApiListHarnessesRequest = None) -> ApiListHarnessesResponse:
    r"""
    List Harnesses. Returns one row per HarnessVersion visible to the caller
    (a Harness with N versions appears N times, each row with version
    populated for that version). Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token -G \
        http://localhost/api/v1/agents/harnesses \
        --data-urlencode 'pageSize=50'

    Args:
      request (ApiListHarnessesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListHarnessesRequest()

    return self._client.call("agents.AgentsApiService", "ListHarnesses", request, ApiListHarnessesResponse)

  def create_agent(self, request: ApiCreateAgentRequest = None) -> ApiAgent:
    r"""
    Create an Agent (pairing of BenchmarkModelVersionConfig + HarnessVersion).
    Admin-only, plus the caller must be able to read the referenced
    BenchmarkModelVersionConfig and HarnessVersion.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        -X POST http://localhost/api/v1/agents/create \
        -H 'Content-Type: application/json' \
        -d '{
          'agent': {
            'displayName': 'Claude Code v2.1.216 (Claude Opus 4.8 high)',
            'slug': 'claude-code-2.1.216-opus-4.8-high',
            'isPublic': false,
            'benchmarkModelVersionConfigId': 1,
            'harnessVersionId': 1
          }
        }'

    Args:
      request (ApiCreateAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateAgentRequest()

    return self._client.call("agents.AgentsApiService", "CreateAgent", request, ApiAgent)

  def get_agent(self, request: ApiGetAgentRequest = None) -> ApiAgent:
    r"""
    Get an Agent by id. Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token \
        http://localhost/api/v1/agents/1

    Args:
      request (ApiGetAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetAgentRequest()

    return self._client.call("agents.AgentsApiService", "GetAgent", request, ApiAgent)

  def list_agents(self, request: ApiListAgentsRequest = None) -> ApiListAgentsResponse:
    r"""
    List Agents visible to the caller. Admin-only.

    Example:
      curl -sSL -u andrewmingwang:local_api_token -G \
        http://localhost/api/v1/agents \
        --data-urlencode 'pageSize=50'

    Args:
      request (ApiListAgentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListAgentsRequest()

    return self._client.call("agents.AgentsApiService", "ListAgents", request, ApiListAgentsResponse)
