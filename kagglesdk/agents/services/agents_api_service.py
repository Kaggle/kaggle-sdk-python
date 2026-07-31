from kagglesdk.agents.types.agents_api_service import ApiCreateHarnessRequest, ApiCreateHarnessVersionRequest, ApiGetHarnessRequest, ApiGetHarnessVersionRequest, ApiHarness, ApiHarnessVersion
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
