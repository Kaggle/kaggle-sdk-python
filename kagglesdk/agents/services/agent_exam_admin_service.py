from kagglesdk.agents.types.agent_exam_admin_service import DeleteAgentExamAgentRequest, ListAgentExamAgentsRequest, ListAgentExamAgentsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AgentExamAdminClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_agent_exam_agents(self, request: ListAgentExamAgentsRequest = None) -> ListAgentExamAgentsResponse:
    r"""
    Args:
      request (ListAgentExamAgentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListAgentExamAgentsRequest()

    return self._client.call("agents.AgentExamAdminService", "ListAgentExamAgents", request, ListAgentExamAgentsResponse)

  def delete_agent_exam_agent(self, request: DeleteAgentExamAgentRequest = None):
    r"""
    Args:
      request (DeleteAgentExamAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteAgentExamAgentRequest()

    self._client.call("agents.AgentExamAdminService", "DeleteAgentExamAgent", request, None)
