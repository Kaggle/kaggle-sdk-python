from kagglesdk.agents.types.agent_exam_service import ApiCompleteAgentExamSubmissionRequest, ApiCompleteAgentExamSubmissionResponse, ApiCreateAgentExamAgentRequest, ApiCreateAgentExamAgentResponse, ApiCreateAgentExamSubmissionRequest, ApiCreateAgentExamSubmissionResponse, ApiGetAgentExamAgentRequest, ApiGetAgentExamAgentResponse, ApiGetAgentExamInsightsRequest, ApiGetAgentExamInsightsResponse, ApiGetAgentExamSubmissionRequest, ApiGetAgentExamSubmissionResponse, ApiListTopAgentExamAgentsRequest, ApiListTopAgentExamAgentsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AgentExamClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_agent_exam_agent(self, request: ApiCreateAgentExamAgentRequest = None) -> ApiCreateAgentExamAgentResponse:
    r"""
    Args:
      request (ApiCreateAgentExamAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateAgentExamAgentRequest()

    return self._client.call("agents.AgentExamService", "CreateAgentExamAgent", request, ApiCreateAgentExamAgentResponse)

  def get_agent_exam_agent(self, request: ApiGetAgentExamAgentRequest = None) -> ApiGetAgentExamAgentResponse:
    r"""
    Args:
      request (ApiGetAgentExamAgentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetAgentExamAgentRequest()

    return self._client.call("agents.AgentExamService", "GetAgentExamAgent", request, ApiGetAgentExamAgentResponse)

  def create_agent_exam_submission(self, request: ApiCreateAgentExamSubmissionRequest = None) -> ApiCreateAgentExamSubmissionResponse:
    r"""
    Args:
      request (ApiCreateAgentExamSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateAgentExamSubmissionRequest()

    return self._client.call("agents.AgentExamService", "CreateAgentExamSubmission", request, ApiCreateAgentExamSubmissionResponse)

  def complete_agent_exam_submission(self, request: ApiCompleteAgentExamSubmissionRequest = None) -> ApiCompleteAgentExamSubmissionResponse:
    r"""
    Args:
      request (ApiCompleteAgentExamSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCompleteAgentExamSubmissionRequest()

    return self._client.call("agents.AgentExamService", "CompleteAgentExamSubmission", request, ApiCompleteAgentExamSubmissionResponse)

  def get_agent_exam_submission(self, request: ApiGetAgentExamSubmissionRequest = None) -> ApiGetAgentExamSubmissionResponse:
    r"""
    Args:
      request (ApiGetAgentExamSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetAgentExamSubmissionRequest()

    return self._client.call("agents.AgentExamService", "GetAgentExamSubmission", request, ApiGetAgentExamSubmissionResponse)

  def list_top_agent_exam_agents(self, request: ApiListTopAgentExamAgentsRequest = None) -> ApiListTopAgentExamAgentsResponse:
    r"""
    Args:
      request (ApiListTopAgentExamAgentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListTopAgentExamAgentsRequest()

    return self._client.call("agents.AgentExamService", "ListTopAgentExamAgents", request, ApiListTopAgentExamAgentsResponse)

  def get_agent_exam_insights(self, request: ApiGetAgentExamInsightsRequest = None) -> ApiGetAgentExamInsightsResponse:
    r"""
    Args:
      request (ApiGetAgentExamInsightsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetAgentExamInsightsRequest()

    return self._client.call("agents.AgentExamService", "GetAgentExamInsights", request, ApiGetAgentExamInsightsResponse)
