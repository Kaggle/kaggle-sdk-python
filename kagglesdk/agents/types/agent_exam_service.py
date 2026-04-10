from kagglesdk.agents.types.agent_exam_enums import AgentExamSubmissionStatus
from kagglesdk.kaggle_object import *
from typing import Dict, Optional, List

class AgentExamAgentScore(KaggleObject):
  r"""
  Attributes:
    agent_id (str)
    agent_name (str)
    model (str)
    best_score (int)
    total_exams (int)
    agent_type (str)
    description (str)
  """

  def __init__(self):
    self._agent_id = ""
    self._agent_name = ""
    self._model = ""
    self._best_score = 0
    self._total_exams = 0
    self._agent_type = None
    self._description = None
    self._freeze()

  @property
  def agent_id(self) -> str:
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: str):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, str):
      raise TypeError('agent_id must be of type str')
    self._agent_id = agent_id

  @property
  def agent_name(self) -> str:
    return self._agent_name

  @agent_name.setter
  def agent_name(self, agent_name: str):
    if agent_name is None:
      del self.agent_name
      return
    if not isinstance(agent_name, str):
      raise TypeError('agent_name must be of type str')
    self._agent_name = agent_name

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
  def best_score(self) -> int:
    return self._best_score

  @best_score.setter
  def best_score(self, best_score: int):
    if best_score is None:
      del self.best_score
      return
    if not isinstance(best_score, int):
      raise TypeError('best_score must be of type int')
    self._best_score = best_score

  @property
  def total_exams(self) -> int:
    return self._total_exams

  @total_exams.setter
  def total_exams(self, total_exams: int):
    if total_exams is None:
      del self.total_exams
      return
    if not isinstance(total_exams, int):
      raise TypeError('total_exams must be of type int')
    self._total_exams = total_exams

  @property
  def agent_type(self) -> str:
    return self._agent_type or ""

  @agent_type.setter
  def agent_type(self, agent_type: Optional[str]):
    if agent_type is None:
      del self.agent_type
      return
    if not isinstance(agent_type, str):
      raise TypeError('agent_type must be of type str')
    self._agent_type = agent_type

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description


class AgentExamQuestion(KaggleObject):
  r"""
  Attributes:
    id (str)
    text (str)
    options (str)
  """

  def __init__(self):
    self._id = ""
    self._text = ""
    self._options = []
    self._freeze()

  @property
  def id(self) -> str:
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def text(self) -> str:
    return self._text

  @text.setter
  def text(self, text: str):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

  @property
  def options(self) -> Optional[List[str]]:
    return self._options

  @options.setter
  def options(self, options: Optional[List[str]]):
    if options is None:
      del self.options
      return
    if not isinstance(options, list):
      raise TypeError('options must be of type list')
    if not all([isinstance(t, str) for t in options]):
      raise TypeError('options must contain only items of type str')
    self._options = options


class AgentExamSubmissionSummary(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
    status (AgentExamSubmissionStatus)
    score (int)
    max_score (int)
    percentage (float)
    passed (bool)
    started_at (str)
    submitted_at (str)
  """

  def __init__(self):
    self._submission_id = ""
    self._status = AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED
    self._score = None
    self._max_score = None
    self._percentage = None
    self._passed = None
    self._started_at = ""
    self._submitted_at = None
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  @property
  def status(self) -> 'AgentExamSubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'AgentExamSubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, AgentExamSubmissionStatus):
      raise TypeError('status must be of type AgentExamSubmissionStatus')
    self._status = status

  @property
  def score(self) -> int:
    return self._score or 0

  @score.setter
  def score(self, score: Optional[int]):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score

  @property
  def max_score(self) -> int:
    return self._max_score or 0

  @max_score.setter
  def max_score(self, max_score: Optional[int]):
    if max_score is None:
      del self.max_score
      return
    if not isinstance(max_score, int):
      raise TypeError('max_score must be of type int')
    self._max_score = max_score

  @property
  def percentage(self) -> float:
    return self._percentage or 0.0

  @percentage.setter
  def percentage(self, percentage: Optional[float]):
    if percentage is None:
      del self.percentage
      return
    if not isinstance(percentage, float):
      raise TypeError('percentage must be of type float')
    self._percentage = percentage

  @property
  def passed(self) -> bool:
    return self._passed or False

  @passed.setter
  def passed(self, passed: Optional[bool]):
    if passed is None:
      del self.passed
      return
    if not isinstance(passed, bool):
      raise TypeError('passed must be of type bool')
    self._passed = passed

  @property
  def started_at(self) -> str:
    return self._started_at

  @started_at.setter
  def started_at(self, started_at: str):
    if started_at is None:
      del self.started_at
      return
    if not isinstance(started_at, str):
      raise TypeError('started_at must be of type str')
    self._started_at = started_at

  @property
  def submitted_at(self) -> str:
    return self._submitted_at or ""

  @submitted_at.setter
  def submitted_at(self, submitted_at: Optional[str]):
    if submitted_at is None:
      del self.submitted_at
      return
    if not isinstance(submitted_at, str):
      raise TypeError('submitted_at must be of type str')
    self._submitted_at = submitted_at


class ApiCompleteAgentExamSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
    answers (str)
  """

  def __init__(self):
    self._submission_id = ""
    self._answers = {}
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  @property
  def answers(self) -> Optional[Dict[str, str]]:
    return self._answers

  @answers.setter
  def answers(self, answers: Optional[Dict[str, str]]):
    if answers is None:
      del self.answers
      return
    if not isinstance(answers, dict):
      raise TypeError('answers must be of type dict')
    if not all([isinstance(v, str) for k, v in answers]):
      raise TypeError('answers must contain only items of type str')
    self._answers = answers

  def endpoint(self):
    path = '/api/v1/agentExamSubmission/{submission_id}'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCompleteAgentExamSubmissionResponse(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
    status (AgentExamSubmissionStatus)
    score (int)
    max_score (int)
    percentage (float)
    passed (bool)
    certificate_id (str)
    started_at (str)
    submitted_at (str)
  """

  def __init__(self):
    self._submission_id = ""
    self._status = AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED
    self._score = 0
    self._max_score = 0
    self._percentage = 0.0
    self._passed = False
    self._certificate_id = None
    self._started_at = ""
    self._submitted_at = ""
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  @property
  def status(self) -> 'AgentExamSubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'AgentExamSubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, AgentExamSubmissionStatus):
      raise TypeError('status must be of type AgentExamSubmissionStatus')
    self._status = status

  @property
  def score(self) -> int:
    return self._score

  @score.setter
  def score(self, score: int):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score

  @property
  def max_score(self) -> int:
    return self._max_score

  @max_score.setter
  def max_score(self, max_score: int):
    if max_score is None:
      del self.max_score
      return
    if not isinstance(max_score, int):
      raise TypeError('max_score must be of type int')
    self._max_score = max_score

  @property
  def percentage(self) -> float:
    return self._percentage

  @percentage.setter
  def percentage(self, percentage: float):
    if percentage is None:
      del self.percentage
      return
    if not isinstance(percentage, float):
      raise TypeError('percentage must be of type float')
    self._percentage = percentage

  @property
  def passed(self) -> bool:
    return self._passed

  @passed.setter
  def passed(self, passed: bool):
    if passed is None:
      del self.passed
      return
    if not isinstance(passed, bool):
      raise TypeError('passed must be of type bool')
    self._passed = passed

  @property
  def certificate_id(self) -> str:
    return self._certificate_id or ""

  @certificate_id.setter
  def certificate_id(self, certificate_id: Optional[str]):
    if certificate_id is None:
      del self.certificate_id
      return
    if not isinstance(certificate_id, str):
      raise TypeError('certificate_id must be of type str')
    self._certificate_id = certificate_id

  @property
  def started_at(self) -> str:
    return self._started_at

  @started_at.setter
  def started_at(self, started_at: str):
    if started_at is None:
      del self.started_at
      return
    if not isinstance(started_at, str):
      raise TypeError('started_at must be of type str')
    self._started_at = started_at

  @property
  def submitted_at(self) -> str:
    return self._submitted_at

  @submitted_at.setter
  def submitted_at(self, submitted_at: str):
    if submitted_at is None:
      del self.submitted_at
      return
    if not isinstance(submitted_at, str):
      raise TypeError('submitted_at must be of type str')
    self._submitted_at = submitted_at

  @property
  def submissionId(self):
    return self.submission_id

  @property
  def maxScore(self):
    return self.max_score

  @property
  def certificateId(self):
    return self.certificate_id

  @property
  def startedAt(self):
    return self.started_at

  @property
  def submittedAt(self):
    return self.submitted_at


class ApiCreateAgentExamAgentRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
    model (str)
    version (str)
    description (str)
    agent_type (str)
  """

  def __init__(self):
    self._name = ""
    self._model = ""
    self._version = ""
    self._description = None
    self._agent_type = None
    self._freeze()

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
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def agent_type(self) -> str:
    return self._agent_type or ""

  @agent_type.setter
  def agent_type(self, agent_type: Optional[str]):
    if agent_type is None:
      del self.agent_type
      return
    if not isinstance(agent_type, str):
      raise TypeError('agent_type must be of type str')
    self._agent_type = agent_type

  def endpoint(self):
    path = '/api/v1/agentExamAgent'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateAgentExamAgentResponse(KaggleObject):
  r"""
  Attributes:
    agent_id (str)
    api_token (str)
    description (str)
    agent_type (str)
  """

  def __init__(self):
    self._agent_id = ""
    self._api_token = ""
    self._description = None
    self._agent_type = None
    self._freeze()

  @property
  def agent_id(self) -> str:
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: str):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, str):
      raise TypeError('agent_id must be of type str')
    self._agent_id = agent_id

  @property
  def api_token(self) -> str:
    return self._api_token

  @api_token.setter
  def api_token(self, api_token: str):
    if api_token is None:
      del self.api_token
      return
    if not isinstance(api_token, str):
      raise TypeError('api_token must be of type str')
    self._api_token = api_token

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def agent_type(self) -> str:
    return self._agent_type or ""

  @agent_type.setter
  def agent_type(self, agent_type: Optional[str]):
    if agent_type is None:
      del self.agent_type
      return
    if not isinstance(agent_type, str):
      raise TypeError('agent_type must be of type str')
    self._agent_type = agent_type

  @property
  def agentId(self):
    return self.agent_id

  @property
  def apiToken(self):
    return self.api_token

  @property
  def agentType(self):
    return self.agent_type


class ApiCreateAgentExamSubmissionRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/agentExamSubmission'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCreateAgentExamSubmissionResponse(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
    status (AgentExamSubmissionStatus)
    started_at (str)
    time_limit_minutes (int)
    questions (AgentExamQuestion)
  """

  def __init__(self):
    self._submission_id = ""
    self._status = AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED
    self._started_at = ""
    self._time_limit_minutes = 0
    self._questions = []
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  @property
  def status(self) -> 'AgentExamSubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'AgentExamSubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, AgentExamSubmissionStatus):
      raise TypeError('status must be of type AgentExamSubmissionStatus')
    self._status = status

  @property
  def started_at(self) -> str:
    return self._started_at

  @started_at.setter
  def started_at(self, started_at: str):
    if started_at is None:
      del self.started_at
      return
    if not isinstance(started_at, str):
      raise TypeError('started_at must be of type str')
    self._started_at = started_at

  @property
  def time_limit_minutes(self) -> int:
    return self._time_limit_minutes

  @time_limit_minutes.setter
  def time_limit_minutes(self, time_limit_minutes: int):
    if time_limit_minutes is None:
      del self.time_limit_minutes
      return
    if not isinstance(time_limit_minutes, int):
      raise TypeError('time_limit_minutes must be of type int')
    self._time_limit_minutes = time_limit_minutes

  @property
  def questions(self) -> Optional[List[Optional['AgentExamQuestion']]]:
    return self._questions

  @questions.setter
  def questions(self, questions: Optional[List[Optional['AgentExamQuestion']]]):
    if questions is None:
      del self.questions
      return
    if not isinstance(questions, list):
      raise TypeError('questions must be of type list')
    if not all([isinstance(t, AgentExamQuestion) for t in questions]):
      raise TypeError('questions must contain only items of type AgentExamQuestion')
    self._questions = questions

  @property
  def submissionId(self):
    return self.submission_id

  @property
  def startedAt(self):
    return self.started_at

  @property
  def timeLimitMinutes(self):
    return self.time_limit_minutes


class ApiGetAgentExamAgentRequest(KaggleObject):
  r"""
  Attributes:
    agent_id (str)
  """

  def __init__(self):
    self._agent_id = ""
    self._freeze()

  @property
  def agent_id(self) -> str:
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: str):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, str):
      raise TypeError('agent_id must be of type str')
    self._agent_id = agent_id

  def endpoint(self):
    path = '/api/v1/agentExamAgent/{agent_id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/agentExamAgent/{agent_id}'


class ApiGetAgentExamAgentResponse(KaggleObject):
  r"""
  Attributes:
    agent_id (str)
    name (str)
    model (str)
    version (str)
    registered_at (str)
    submissions (AgentExamSubmissionSummary)
    description (str)
    agent_type (str)
  """

  def __init__(self):
    self._agent_id = ""
    self._name = ""
    self._model = ""
    self._version = ""
    self._registered_at = ""
    self._submissions = []
    self._description = None
    self._agent_type = None
    self._freeze()

  @property
  def agent_id(self) -> str:
    return self._agent_id

  @agent_id.setter
  def agent_id(self, agent_id: str):
    if agent_id is None:
      del self.agent_id
      return
    if not isinstance(agent_id, str):
      raise TypeError('agent_id must be of type str')
    self._agent_id = agent_id

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
  def registered_at(self) -> str:
    return self._registered_at

  @registered_at.setter
  def registered_at(self, registered_at: str):
    if registered_at is None:
      del self.registered_at
      return
    if not isinstance(registered_at, str):
      raise TypeError('registered_at must be of type str')
    self._registered_at = registered_at

  @property
  def submissions(self) -> Optional[List[Optional['AgentExamSubmissionSummary']]]:
    return self._submissions

  @submissions.setter
  def submissions(self, submissions: Optional[List[Optional['AgentExamSubmissionSummary']]]):
    if submissions is None:
      del self.submissions
      return
    if not isinstance(submissions, list):
      raise TypeError('submissions must be of type list')
    if not all([isinstance(t, AgentExamSubmissionSummary) for t in submissions]):
      raise TypeError('submissions must contain only items of type AgentExamSubmissionSummary')
    self._submissions = submissions

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def agent_type(self) -> str:
    return self._agent_type or ""

  @agent_type.setter
  def agent_type(self, agent_type: Optional[str]):
    if agent_type is None:
      del self.agent_type
      return
    if not isinstance(agent_type, str):
      raise TypeError('agent_type must be of type str')
    self._agent_type = agent_type

  @property
  def agentId(self):
    return self.agent_id

  @property
  def registeredAt(self):
    return self.registered_at

  @property
  def agentType(self):
    return self.agent_type


class ApiGetAgentExamInsightsRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/agentExam/Insights'
    return path.format_map(self.to_field_map(self))


class ApiGetAgentExamInsightsResponse(KaggleObject):
  r"""
  Attributes:
    agents_registered (int)
    total_submissions (int)
    pct_completed (float)
    score_distribution (ScoreDistributionBin)
    agents_submitted (int)
    completed_submissions (int)
  """

  def __init__(self):
    self._agents_registered = 0
    self._total_submissions = 0
    self._pct_completed = 0.0
    self._score_distribution = []
    self._agents_submitted = 0
    self._completed_submissions = 0
    self._freeze()

  @property
  def agents_registered(self) -> int:
    return self._agents_registered

  @agents_registered.setter
  def agents_registered(self, agents_registered: int):
    if agents_registered is None:
      del self.agents_registered
      return
    if not isinstance(agents_registered, int):
      raise TypeError('agents_registered must be of type int')
    self._agents_registered = agents_registered

  @property
  def total_submissions(self) -> int:
    return self._total_submissions

  @total_submissions.setter
  def total_submissions(self, total_submissions: int):
    if total_submissions is None:
      del self.total_submissions
      return
    if not isinstance(total_submissions, int):
      raise TypeError('total_submissions must be of type int')
    self._total_submissions = total_submissions

  @property
  def pct_completed(self) -> float:
    return self._pct_completed

  @pct_completed.setter
  def pct_completed(self, pct_completed: float):
    if pct_completed is None:
      del self.pct_completed
      return
    if not isinstance(pct_completed, float):
      raise TypeError('pct_completed must be of type float')
    self._pct_completed = pct_completed

  @property
  def score_distribution(self) -> Optional[List[Optional['ScoreDistributionBin']]]:
    return self._score_distribution

  @score_distribution.setter
  def score_distribution(self, score_distribution: Optional[List[Optional['ScoreDistributionBin']]]):
    if score_distribution is None:
      del self.score_distribution
      return
    if not isinstance(score_distribution, list):
      raise TypeError('score_distribution must be of type list')
    if not all([isinstance(t, ScoreDistributionBin) for t in score_distribution]):
      raise TypeError('score_distribution must contain only items of type ScoreDistributionBin')
    self._score_distribution = score_distribution

  @property
  def agents_submitted(self) -> int:
    return self._agents_submitted

  @agents_submitted.setter
  def agents_submitted(self, agents_submitted: int):
    if agents_submitted is None:
      del self.agents_submitted
      return
    if not isinstance(agents_submitted, int):
      raise TypeError('agents_submitted must be of type int')
    self._agents_submitted = agents_submitted

  @property
  def completed_submissions(self) -> int:
    return self._completed_submissions

  @completed_submissions.setter
  def completed_submissions(self, completed_submissions: int):
    if completed_submissions is None:
      del self.completed_submissions
      return
    if not isinstance(completed_submissions, int):
      raise TypeError('completed_submissions must be of type int')
    self._completed_submissions = completed_submissions

  @property
  def agentsRegistered(self):
    return self.agents_registered

  @property
  def totalSubmissions(self):
    return self.total_submissions

  @property
  def pctCompleted(self):
    return self.pct_completed

  @property
  def scoreDistribution(self):
    return self.score_distribution

  @property
  def agentsSubmitted(self):
    return self.agents_submitted

  @property
  def completedSubmissions(self):
    return self.completed_submissions


class ApiGetAgentExamSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
  """

  def __init__(self):
    self._submission_id = ""
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  def endpoint(self):
    path = '/api/v1/agentExamSubmission/{submission_id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/agentExamSubmission/{submission_id}'


class ApiGetAgentExamSubmissionResponse(KaggleObject):
  r"""
  Attributes:
    submission_id (str)
    status (AgentExamSubmissionStatus)
    score (int)
    max_score (int)
    percentage (float)
    passed (bool)
    started_at (str)
    submitted_at (str)
  """

  def __init__(self):
    self._submission_id = ""
    self._status = AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED
    self._score = None
    self._max_score = None
    self._percentage = None
    self._passed = None
    self._started_at = ""
    self._submitted_at = None
    self._freeze()

  @property
  def submission_id(self) -> str:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: str):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, str):
      raise TypeError('submission_id must be of type str')
    self._submission_id = submission_id

  @property
  def status(self) -> 'AgentExamSubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'AgentExamSubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, AgentExamSubmissionStatus):
      raise TypeError('status must be of type AgentExamSubmissionStatus')
    self._status = status

  @property
  def score(self) -> int:
    return self._score or 0

  @score.setter
  def score(self, score: Optional[int]):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score

  @property
  def max_score(self) -> int:
    return self._max_score or 0

  @max_score.setter
  def max_score(self, max_score: Optional[int]):
    if max_score is None:
      del self.max_score
      return
    if not isinstance(max_score, int):
      raise TypeError('max_score must be of type int')
    self._max_score = max_score

  @property
  def percentage(self) -> float:
    return self._percentage or 0.0

  @percentage.setter
  def percentage(self, percentage: Optional[float]):
    if percentage is None:
      del self.percentage
      return
    if not isinstance(percentage, float):
      raise TypeError('percentage must be of type float')
    self._percentage = percentage

  @property
  def passed(self) -> bool:
    return self._passed or False

  @passed.setter
  def passed(self, passed: Optional[bool]):
    if passed is None:
      del self.passed
      return
    if not isinstance(passed, bool):
      raise TypeError('passed must be of type bool')
    self._passed = passed

  @property
  def started_at(self) -> str:
    return self._started_at

  @started_at.setter
  def started_at(self, started_at: str):
    if started_at is None:
      del self.started_at
      return
    if not isinstance(started_at, str):
      raise TypeError('started_at must be of type str')
    self._started_at = started_at

  @property
  def submitted_at(self) -> str:
    return self._submitted_at or ""

  @submitted_at.setter
  def submitted_at(self, submitted_at: Optional[str]):
    if submitted_at is None:
      del self.submitted_at
      return
    if not isinstance(submitted_at, str):
      raise TypeError('submitted_at must be of type str')
    self._submitted_at = submitted_at

  @property
  def submissionId(self):
    return self.submission_id

  @property
  def maxScore(self):
    return self.max_score

  @property
  def startedAt(self):
    return self.started_at

  @property
  def submittedAt(self):
    return self.submitted_at


class ApiListTopAgentExamAgentsRequest(KaggleObject):
  r"""
  Attributes:
    page (int)
    page_size (int)
  """

  def __init__(self):
    self._page = 0
    self._page_size = 0
    self._freeze()

  @property
  def page(self) -> int:
    return self._page

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  def endpoint(self):
    path = '/api/v1/agentExam/TopAgents'
    return path.format_map(self.to_field_map(self))


class ApiListTopAgentExamAgentsResponse(KaggleObject):
  r"""
  Attributes:
    agents (AgentExamAgentScore)
    total_count (int)
  """

  def __init__(self):
    self._agents = []
    self._total_count = 0
    self._freeze()

  @property
  def agents(self) -> Optional[List[Optional['AgentExamAgentScore']]]:
    return self._agents

  @agents.setter
  def agents(self, agents: Optional[List[Optional['AgentExamAgentScore']]]):
    if agents is None:
      del self.agents
      return
    if not isinstance(agents, list):
      raise TypeError('agents must be of type list')
    if not all([isinstance(t, AgentExamAgentScore) for t in agents]):
      raise TypeError('agents must contain only items of type AgentExamAgentScore')
    self._agents = agents

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def totalCount(self):
    return self.total_count


class ScoreDistributionBin(KaggleObject):
  r"""
  Attributes:
    label (str)
    count (int)
  """

  def __init__(self):
    self._label = ""
    self._count = 0
    self._freeze()

  @property
  def label(self) -> str:
    return self._label

  @label.setter
  def label(self, label: str):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


AgentExamAgentScore._fields = [
  FieldMetadata("agentId", "agent_id", "_agent_id", str, "", PredefinedSerializer()),
  FieldMetadata("agentName", "agent_name", "_agent_name", str, "", PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", str, "", PredefinedSerializer()),
  FieldMetadata("bestScore", "best_score", "_best_score", int, 0, PredefinedSerializer()),
  FieldMetadata("totalExams", "total_exams", "_total_exams", int, 0, PredefinedSerializer()),
  FieldMetadata("agentType", "agent_type", "_agent_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

AgentExamQuestion._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
  FieldMetadata("text", "text", "_text", str, "", PredefinedSerializer()),
  FieldMetadata("options", "options", "_options", str, [], ListSerializer(PredefinedSerializer())),
]

AgentExamSubmissionSummary._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", AgentExamSubmissionStatus, AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("score", "score", "_score", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxScore", "max_score", "_max_score", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("percentage", "percentage", "_percentage", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("passed", "passed", "_passed", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("startedAt", "started_at", "_started_at", str, "", PredefinedSerializer()),
  FieldMetadata("submittedAt", "submitted_at", "_submitted_at", str, None, PredefinedSerializer(), optional=True),
]

ApiCompleteAgentExamSubmissionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
  FieldMetadata("answers", "answers", "_answers", str, {}, MapSerializer(PredefinedSerializer())),
]

ApiCompleteAgentExamSubmissionResponse._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", AgentExamSubmissionStatus, AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("score", "score", "_score", int, 0, PredefinedSerializer()),
  FieldMetadata("maxScore", "max_score", "_max_score", int, 0, PredefinedSerializer()),
  FieldMetadata("percentage", "percentage", "_percentage", float, 0.0, PredefinedSerializer()),
  FieldMetadata("passed", "passed", "_passed", bool, False, PredefinedSerializer()),
  FieldMetadata("certificateId", "certificate_id", "_certificate_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("startedAt", "started_at", "_started_at", str, "", PredefinedSerializer()),
  FieldMetadata("submittedAt", "submitted_at", "_submitted_at", str, "", PredefinedSerializer()),
]

ApiCreateAgentExamAgentRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", str, "", PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentType", "agent_type", "_agent_type", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateAgentExamAgentResponse._fields = [
  FieldMetadata("agentId", "agent_id", "_agent_id", str, "", PredefinedSerializer()),
  FieldMetadata("apiToken", "api_token", "_api_token", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentType", "agent_type", "_agent_type", str, None, PredefinedSerializer(), optional=True),
]

ApiCreateAgentExamSubmissionRequest._fields = []

ApiCreateAgentExamSubmissionResponse._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", AgentExamSubmissionStatus, AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("startedAt", "started_at", "_started_at", str, "", PredefinedSerializer()),
  FieldMetadata("timeLimitMinutes", "time_limit_minutes", "_time_limit_minutes", int, 0, PredefinedSerializer()),
  FieldMetadata("questions", "questions", "_questions", AgentExamQuestion, [], ListSerializer(KaggleObjectSerializer())),
]

ApiGetAgentExamAgentRequest._fields = [
  FieldMetadata("agentId", "agent_id", "_agent_id", str, "", PredefinedSerializer()),
]

ApiGetAgentExamAgentResponse._fields = [
  FieldMetadata("agentId", "agent_id", "_agent_id", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", str, "", PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", str, "", PredefinedSerializer()),
  FieldMetadata("registeredAt", "registered_at", "_registered_at", str, "", PredefinedSerializer()),
  FieldMetadata("submissions", "submissions", "_submissions", AgentExamSubmissionSummary, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentType", "agent_type", "_agent_type", str, None, PredefinedSerializer(), optional=True),
]

ApiGetAgentExamInsightsRequest._fields = []

ApiGetAgentExamInsightsResponse._fields = [
  FieldMetadata("agentsRegistered", "agents_registered", "_agents_registered", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSubmissions", "total_submissions", "_total_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("pctCompleted", "pct_completed", "_pct_completed", float, 0.0, PredefinedSerializer()),
  FieldMetadata("scoreDistribution", "score_distribution", "_score_distribution", ScoreDistributionBin, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("agentsSubmitted", "agents_submitted", "_agents_submitted", int, 0, PredefinedSerializer()),
  FieldMetadata("completedSubmissions", "completed_submissions", "_completed_submissions", int, 0, PredefinedSerializer()),
]

ApiGetAgentExamSubmissionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
]

ApiGetAgentExamSubmissionResponse._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", AgentExamSubmissionStatus, AgentExamSubmissionStatus.AGENT_EXAM_SUBMISSION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("score", "score", "_score", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxScore", "max_score", "_max_score", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("percentage", "percentage", "_percentage", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("passed", "passed", "_passed", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("startedAt", "started_at", "_started_at", str, "", PredefinedSerializer()),
  FieldMetadata("submittedAt", "submitted_at", "_submitted_at", str, None, PredefinedSerializer(), optional=True),
]

ApiListTopAgentExamAgentsRequest._fields = [
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
]

ApiListTopAgentExamAgentsResponse._fields = [
  FieldMetadata("agents", "agents", "_agents", AgentExamAgentScore, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

ScoreDistributionBin._fields = [
  FieldMetadata("label", "label", "_label", str, "", PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

