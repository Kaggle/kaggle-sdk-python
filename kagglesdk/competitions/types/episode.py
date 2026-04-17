import enum

class EpisodeAgentState(enum.Enum):
  EPISODE_AGENT_STATE_UNSPECIFIED = 0
  EPISODE_AGENT_STATE_PENDING = 1
  """The Episode has not yet completed."""
  EPISODE_AGENT_STATE_COMPLETE = 2
  """The Agent completed the Episode."""
  EPISODE_AGENT_STATE_ERROR_EVALUATION = 3
  """The Agent threw an Exception during evaluation, or similar."""
  EPISODE_AGENT_STATE_ERROR_INVALID_ACTION = 4
  """The Agent returned an invalid action and was disqualified."""
  EPISODE_AGENT_STATE_ERROR_TIMEOUT = 5
  """The Agent did not return its action in the required time."""
  EPISODE_AGENT_STATE_ERROR_ON_EPISODE = 6
  """The Episode failed for unexpected reasons."""

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

