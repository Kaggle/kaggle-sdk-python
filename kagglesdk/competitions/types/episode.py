from datetime import datetime
import enum
from kagglesdk.competitions.types.submission import Submission
from kagglesdk.kaggle_object import *
from typing import Optional, List

class EpisodeState(enum.Enum):
  EPISODE_STATE_UNSPECIFIED = 0
  CREATED = 1
  COMPLETED = 2
  ERRORED = 3
  NEVER_STARTED = 4

class EpisodeType(enum.Enum):
  """Controls whether score is written and where"""
  EPISODE_TYPE_UNSPECIFIED = 0
  EPISODE_TYPE_PUBLIC = 1
  EPISODE_TYPE_PRIVATE = 2
  """This is deprecated / was never supported."""
  EPISODE_TYPE_EXHIBITION = 3
  EPISODE_TYPE_VALIDATION = 4

class Episode(KaggleObject):
  r"""
  An episode is an individual run of a simulation with a set of agents

  Attributes:
    id (int)
    create_time (datetime)
      For our purposes, create_time is the same as start_time
    end_time (datetime)
    state (EpisodeState)
    type (EpisodeType)
    agents (EpisodeAgent)
  """

  def __init__(self):
    self._id = 0
    self._create_time = None
    self._end_time = None
    self._state = EpisodeState.EPISODE_STATE_UNSPECIFIED
    self._type = EpisodeType.EPISODE_TYPE_UNSPECIFIED
    self._agents = []
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
  def create_time(self) -> datetime:
    """For our purposes, create_time is the same as start_time"""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def end_time(self) -> datetime:
    return self._end_time

  @end_time.setter
  def end_time(self, end_time: datetime):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time

  @property
  def state(self) -> 'EpisodeState':
    return self._state

  @state.setter
  def state(self, state: 'EpisodeState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, EpisodeState):
      raise TypeError('state must be of type EpisodeState')
    self._state = state

  @property
  def type(self) -> 'EpisodeType':
    return self._type

  @type.setter
  def type(self, type: 'EpisodeType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, EpisodeType):
      raise TypeError('type must be of type EpisodeType')
    self._type = type

  @property
  def agents(self) -> Optional[List[Optional['EpisodeAgent']]]:
    return self._agents

  @agents.setter
  def agents(self, agents: Optional[List[Optional['EpisodeAgent']]]):
    if agents is None:
      del self.agents
      return
    if not isinstance(agents, list):
      raise TypeError('agents must be of type list')
    if not all([isinstance(t, EpisodeAgent) for t in agents]):
      raise TypeError('agents must contain only items of type EpisodeAgent')
    self._agents = agents


class EpisodeAgent(KaggleObject):
  r"""
  An episode agent represents a single competition submission participating in
  this episode

  Attributes:
    id (int)
    submission_id (int)
    reward (float)
    index (int)
    initial_score (float)
      Score and Confidence of Submission at the time the Episode completed,
      before updates were applied (if applicable).
    updated_score (float)
      Updated Submission Score and Confidence, if applicable.
    submission (Submission)
  """

  def __init__(self):
    self._id = 0
    self._submission_id = 0
    self._reward = None
    self._index = 0
    self._initial_score = None
    self._updated_score = None
    self._submission = None
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
  def submission_id(self) -> int:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: int):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def reward(self) -> float:
    return self._reward or 0.0

  @reward.setter
  def reward(self, reward: Optional[float]):
    if reward is None:
      del self.reward
      return
    if not isinstance(reward, float):
      raise TypeError('reward must be of type float')
    self._reward = reward

  @property
  def index(self) -> int:
    return self._index

  @index.setter
  def index(self, index: int):
    if index is None:
      del self.index
      return
    if not isinstance(index, int):
      raise TypeError('index must be of type int')
    self._index = index

  @property
  def initial_score(self) -> float:
    r"""
    Score and Confidence of Submission at the time the Episode completed,
    before updates were applied (if applicable).
    """
    return self._initial_score or 0.0

  @initial_score.setter
  def initial_score(self, initial_score: Optional[float]):
    if initial_score is None:
      del self.initial_score
      return
    if not isinstance(initial_score, float):
      raise TypeError('initial_score must be of type float')
    self._initial_score = initial_score

  @property
  def updated_score(self) -> float:
    """Updated Submission Score and Confidence, if applicable."""
    return self._updated_score or 0.0

  @updated_score.setter
  def updated_score(self, updated_score: Optional[float]):
    if updated_score is None:
      del self.updated_score
      return
    if not isinstance(updated_score, float):
      raise TypeError('updated_score must be of type float')
    self._updated_score = updated_score

  @property
  def submission(self) -> Optional['Submission']:
    return self._submission

  @submission.setter
  def submission(self, submission: Optional['Submission']):
    if submission is None:
      del self.submission
      return
    if not isinstance(submission, Submission):
      raise TypeError('submission must be of type Submission')
    self._submission = submission


Episode._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("state", "state", "_state", EpisodeState, EpisodeState.EPISODE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", EpisodeType, EpisodeType.EPISODE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("agents", "agents", "_agents", EpisodeAgent, [], ListSerializer(KaggleObjectSerializer())),
]

EpisodeAgent._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reward", "reward", "_reward", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("index", "index", "_index", int, 0, PredefinedSerializer()),
  FieldMetadata("initialScore", "initial_score", "_initial_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("updatedScore", "updated_score", "_updated_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submission", "submission", "_submission", Submission, None, KaggleObjectSerializer()),
]

