from kagglesdk.content_discovery.types.content_discovery_service import RunContentDiscoveryAgentRequest, RunContentDiscoveryAgentResponse, SearchWithMcpRequest, SearchWithMcpResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class ContentDiscoveryClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def run_content_discovery_agent(self, request: RunContentDiscoveryAgentRequest = None) -> RunContentDiscoveryAgentResponse:
    r"""
    Args:
      request (RunContentDiscoveryAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RunContentDiscoveryAgentRequest()

    return self._client.call("content_discovery.ContentDiscoveryService", "RunContentDiscoveryAgent", request, RunContentDiscoveryAgentResponse)

  def search_with_mcp(self, request: SearchWithMcpRequest = None) -> SearchWithMcpResponse:
    r"""
    Args:
      request (SearchWithMcpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchWithMcpRequest()

    return self._client.call("content_discovery.ContentDiscoveryService", "SearchWithMcp", request, SearchWithMcpResponse)
