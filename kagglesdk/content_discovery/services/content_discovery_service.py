from kagglesdk.content_discovery.types.content_discovery_service import RunContentDiscoveryAgentRequest, RunContentDiscoveryAgentResponse
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
