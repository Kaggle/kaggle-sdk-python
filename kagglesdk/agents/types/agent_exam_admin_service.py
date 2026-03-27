from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import List, Optional

class AgentExamAgentSummary(KaggleObject):
  r"""
  Attributes:
    id (int)
    external_id (str)
    name (str)
    model (str)
    version (str)
    registered_at (datetime)
    submission_count (int)
    api_token_count (int)
    agent_type (str)
  """

  def __init__(self):
    self._id = 0
    self._external_id = ""
    self._name = ""
    self._model = ""
    self._version = ""
    self._registered_at = None
    self._submission_count = 0
    self._api_token_count = 0
    self._agent_type = ""
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def external_id(self) -> str:
    return self._external_id

  @external_id.setter
  def external_id(self, external_id: str):
    if external_id is None:
      del self.external_id
      return
    if not isinstance(external_id, str):
      raise TypeError('external_id must be of type str')
    self._external_id = external_id

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def model(self) -> str:
    return self._model

  @model.setter
  def model(self, model: str):
    if model is None:
      del self.model
      return
    if not isinstance(model, str):
      raise TypeError('model must be of type str')
    self._model = model

  @property
  def version(self) -> str:
    return self._version

  @version.setter
  def version(self, version: str):
    if version is None:
      del self.version
      return
    if not isinstance(version, str):
      raise TypeError('version must be of type str')
    self._version = version

  @property
  def registered_at(self) -> datetime:
    return self._registered_at

  @registered_at.setter
  def registered_at(self, registered_at: datetime):
    if registered_at is None:
      del self.registered_at
      return
    if not isinstance(registered_at, datetime):
      raise TypeError('registered_at must be of type datetime')
    self._registered_at = registered_at

  @property
  def submission_count(self) -> int:
    return self._submission_count

  @submission_count.setter
  def submission_count(self, submission_count: int):
    if submission_count is None:
      del self.submission_count
      return
    if not isinstance(submission_count, int):
      raise TypeError('submission_count must be of type int')
    self._submission_count = submission_count

  @property
  def api_token_count(self) -> int:
    return self._api_token_count

  @api_token_count.setter
  def api_token_count(self, api_token_count: int):
    if api_token_count is None:
      del self.api_token_count
      return
    if not isinstance(api_token_count, int):
      raise TypeError('api_token_count must be of type int')
    self._api_token_count = api_token_count

  @property
  def agent_type(self) -> str:
    return self._agent_type

  @agent_type.setter
  def agent_type(self, agent_type: str):
    if agent_type is None:
      del self.agent_type
      return
    if not isinstance(agent_type, str):
      raise TypeError('agent_type must be of type str')
    self._agent_type = agent_type


class DeleteAgentExamAgentRequest(KaggleObject):
  r"""
  Attributes:
    agent_id (int)
  """

  def __init__(self):
    self._agent_id = 0
    self._freeze()

  @property
  def agent_id(self) -> int:
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: int):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, int):
      raise TypeError('agent_id must be of type int')
    self._agent_id = agent_id


class ListAgentExamAgentsRequest(KaggleObject):
  r"""
  """

  pass

class ListAgentExamAgentsResponse(KaggleObject):
  r"""
  Attributes:
    agents (AgentExamAgentSummary)
  """

  def __init__(self):
    self._agents = []
    self._freeze()

  @property
  def agents(self) -> Optional[List[Optional['AgentExamAgentSummary']]]:
    return self._agents

  @agents.setter
  def agents(self, agents: Optional[List[Optional['AgentExamAgentSummary']]]):
    if agents is None:
      del self.agents
      return
    if not isinstance(agents, list):
      raise TypeError('agents must be of type list')
    if not all([isinstance(t, AgentExamAgentSummary) for t in agents]):
      raise TypeError('agents must contain only items of type AgentExamAgentSummary')
    self._agents = agents


AgentExamAgentSummary._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("externalId", "external_id", "_external_id", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", str, "", PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", str, "", PredefinedSerializer()),
  FieldMetadata("registeredAt", "registered_at", "_registered_at", datetime, None, DateTimeSerializer()),
  FieldMetadata("submissionCount", "submission_count", "_submission_count", int, 0, PredefinedSerializer()),
  FieldMetadata("apiTokenCount", "api_token_count", "_api_token_count", int, 0, PredefinedSerializer()),
  FieldMetadata("agentType", "agent_type", "_agent_type", str, "", PredefinedSerializer()),
]

DeleteAgentExamAgentRequest._fields = [
  FieldMetadata("agentId", "agent_id", "_agent_id", int, 0, PredefinedSerializer()),
]

ListAgentExamAgentsRequest._fields = []

ListAgentExamAgentsResponse._fields = [
  FieldMetadata("agents", "agents", "_agents", AgentExamAgentSummary, [], ListSerializer(KaggleObjectSerializer())),
]

