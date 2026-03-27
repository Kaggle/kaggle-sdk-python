import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class SchedulingMode(enum.Enum):
  SCHEDULING_MODE_UNSPECIFIED = 0
  SCHEDULING_MODE_DEFAULT = 1
  SCHEDULING_MODE_PAIRWISE = 2
  SCHEDULING_MODE_PRIORITY_MATCHES = 3

class CompetitionSimulationSettings(KaggleObject):
  r"""
  Attributes:
    submission_size_limit_kb (int)
    agent_disk_kb (int)
    agent_ram_kb (int)
    agent_cpu_cores_percent (int)
    mirror_match (bool)
    enable_internet (bool)
    evaluation_algorithm_config_override (str)
    extra_agents (str)
    max_concurrent_active_episodes (int)
    generate_episodes_submission_runs_per_day (int)
    flat_scheduler (bool)
    random_opponent_probability (float)
    priority_submissions (str)
    priority_matches (str)
    scheduling_mode (SchedulingMode)
    pairwise_settings (PairwiseSettings)
    use_model_proxy (bool)
    max_episode_duration_seconds (int)
    random_opponent_sample_with_replacement (bool)
    validation_evaluation_algorithm_config_override (str)
      Override for evaluation algorithm config used for validation episodes.
      If set, this is used instead of evaluation_algorithm_config_override for
      validation.
    max_concurrent_episodes_per_submission (int)
  """

  def __init__(self):
    self._submission_size_limit_kb = 0
    self._agent_disk_kb = 0
    self._agent_ram_kb = 0
    self._agent_cpu_cores_percent = 0
    self._mirror_match = False
    self._enable_internet = False
    self._evaluation_algorithm_config_override = ""
    self._extra_agents = ""
    self._max_concurrent_active_episodes = None
    self._generate_episodes_submission_runs_per_day = None
    self._flat_scheduler = None
    self._random_opponent_probability = None
    self._priority_submissions = None
    self._priority_matches = None
    self._scheduling_mode = None
    self._pairwise_settings = None
    self._use_model_proxy = None
    self._max_episode_duration_seconds = None
    self._random_opponent_sample_with_replacement = False
    self._validation_evaluation_algorithm_config_override = None
    self._max_concurrent_episodes_per_submission = None
    self._freeze()

  @property
  def submission_size_limit_kb(self) -> int:
    return self._submission_size_limit_kb

  @submission_size_limit_kb.setter
  def submission_size_limit_kb(self, submission_size_limit_kb: int):
    if submission_size_limit_kb is None:
      del self.submission_size_limit_kb
      return
    if not isinstance(submission_size_limit_kb, int):
      raise TypeError('submission_size_limit_kb must be of type int')
    self._submission_size_limit_kb = submission_size_limit_kb

  @property
  def agent_disk_kb(self) -> int:
    return self._agent_disk_kb

  @agent_disk_kb.setter
  def agent_disk_kb(self, agent_disk_kb: int):
    if agent_disk_kb is None:
      del self.agent_disk_kb
      return
    if not isinstance(agent_disk_kb, int):
      raise TypeError('agent_disk_kb must be of type int')
    self._agent_disk_kb = agent_disk_kb

  @property
  def agent_ram_kb(self) -> int:
    return self._agent_ram_kb

  @agent_ram_kb.setter
  def agent_ram_kb(self, agent_ram_kb: int):
    if agent_ram_kb is None:
      del self.agent_ram_kb
      return
    if not isinstance(agent_ram_kb, int):
      raise TypeError('agent_ram_kb must be of type int')
    self._agent_ram_kb = agent_ram_kb

  @property
  def agent_cpu_cores_percent(self) -> int:
    return self._agent_cpu_cores_percent

  @agent_cpu_cores_percent.setter
  def agent_cpu_cores_percent(self, agent_cpu_cores_percent: int):
    if agent_cpu_cores_percent is None:
      del self.agent_cpu_cores_percent
      return
    if not isinstance(agent_cpu_cores_percent, int):
      raise TypeError('agent_cpu_cores_percent must be of type int')
    self._agent_cpu_cores_percent = agent_cpu_cores_percent

  @property
  def mirror_match(self) -> bool:
    return self._mirror_match

  @mirror_match.setter
  def mirror_match(self, mirror_match: bool):
    if mirror_match is None:
      del self.mirror_match
      return
    if not isinstance(mirror_match, bool):
      raise TypeError('mirror_match must be of type bool')
    self._mirror_match = mirror_match

  @property
  def enable_internet(self) -> bool:
    return self._enable_internet

  @enable_internet.setter
  def enable_internet(self, enable_internet: bool):
    if enable_internet is None:
      del self.enable_internet
      return
    if not isinstance(enable_internet, bool):
      raise TypeError('enable_internet must be of type bool')
    self._enable_internet = enable_internet

  @property
  def evaluation_algorithm_config_override(self) -> str:
    return self._evaluation_algorithm_config_override

  @evaluation_algorithm_config_override.setter
  def evaluation_algorithm_config_override(self, evaluation_algorithm_config_override: str):
    if evaluation_algorithm_config_override is None:
      del self.evaluation_algorithm_config_override
      return
    if not isinstance(evaluation_algorithm_config_override, str):
      raise TypeError('evaluation_algorithm_config_override must be of type str')
    self._evaluation_algorithm_config_override = evaluation_algorithm_config_override

  @property
  def extra_agents(self) -> str:
    return self._extra_agents

  @extra_agents.setter
  def extra_agents(self, extra_agents: str):
    if extra_agents is None:
      del self.extra_agents
      return
    if not isinstance(extra_agents, str):
      raise TypeError('extra_agents must be of type str')
    self._extra_agents = extra_agents

  @property
  def validation_evaluation_algorithm_config_override(self) -> str:
    r"""
    Override for evaluation algorithm config used for validation episodes.
    If set, this is used instead of evaluation_algorithm_config_override for
    validation.
    """
    return self._validation_evaluation_algorithm_config_override or ""

  @validation_evaluation_algorithm_config_override.setter
  def validation_evaluation_algorithm_config_override(self, validation_evaluation_algorithm_config_override: Optional[str]):
    if validation_evaluation_algorithm_config_override is None:
      del self.validation_evaluation_algorithm_config_override
      return
    if not isinstance(validation_evaluation_algorithm_config_override, str):
      raise TypeError('validation_evaluation_algorithm_config_override must be of type str')
    self._validation_evaluation_algorithm_config_override = validation_evaluation_algorithm_config_override

  @property
  def max_concurrent_active_episodes(self) -> int:
    return self._max_concurrent_active_episodes or 0

  @max_concurrent_active_episodes.setter
  def max_concurrent_active_episodes(self, max_concurrent_active_episodes: Optional[int]):
    if max_concurrent_active_episodes is None:
      del self.max_concurrent_active_episodes
      return
    if not isinstance(max_concurrent_active_episodes, int):
      raise TypeError('max_concurrent_active_episodes must be of type int')
    self._max_concurrent_active_episodes = max_concurrent_active_episodes

  @property
  def generate_episodes_submission_runs_per_day(self) -> int:
    return self._generate_episodes_submission_runs_per_day or 0

  @generate_episodes_submission_runs_per_day.setter
  def generate_episodes_submission_runs_per_day(self, generate_episodes_submission_runs_per_day: Optional[int]):
    if generate_episodes_submission_runs_per_day is None:
      del self.generate_episodes_submission_runs_per_day
      return
    if not isinstance(generate_episodes_submission_runs_per_day, int):
      raise TypeError('generate_episodes_submission_runs_per_day must be of type int')
    self._generate_episodes_submission_runs_per_day = generate_episodes_submission_runs_per_day

  @property
  def flat_scheduler(self) -> bool:
    return self._flat_scheduler or False

  @flat_scheduler.setter
  def flat_scheduler(self, flat_scheduler: Optional[bool]):
    if flat_scheduler is None:
      del self.flat_scheduler
      return
    if not isinstance(flat_scheduler, bool):
      raise TypeError('flat_scheduler must be of type bool')
    self._flat_scheduler = flat_scheduler

  @property
  def random_opponent_probability(self) -> float:
    return self._random_opponent_probability or 0.0

  @random_opponent_probability.setter
  def random_opponent_probability(self, random_opponent_probability: Optional[float]):
    if random_opponent_probability is None:
      del self.random_opponent_probability
      return
    if not isinstance(random_opponent_probability, float):
      raise TypeError('random_opponent_probability must be of type float')
    self._random_opponent_probability = random_opponent_probability

  @property
  def priority_submissions(self) -> str:
    return self._priority_submissions or ""

  @priority_submissions.setter
  def priority_submissions(self, priority_submissions: Optional[str]):
    if priority_submissions is None:
      del self.priority_submissions
      return
    if not isinstance(priority_submissions, str):
      raise TypeError('priority_submissions must be of type str')
    self._priority_submissions = priority_submissions

  @property
  def priority_matches(self) -> str:
    return self._priority_matches or ""

  @priority_matches.setter
  def priority_matches(self, priority_matches: Optional[str]):
    if priority_matches is None:
      del self.priority_matches
      return
    if not isinstance(priority_matches, str):
      raise TypeError('priority_matches must be of type str')
    self._priority_matches = priority_matches

  @property
  def scheduling_mode(self) -> 'SchedulingMode':
    return self._scheduling_mode or SchedulingMode.SCHEDULING_MODE_UNSPECIFIED

  @scheduling_mode.setter
  def scheduling_mode(self, scheduling_mode: Optional['SchedulingMode']):
    if scheduling_mode is None:
      del self.scheduling_mode
      return
    if not isinstance(scheduling_mode, SchedulingMode):
      raise TypeError('scheduling_mode must be of type SchedulingMode')
    self._scheduling_mode = scheduling_mode

  @property
  def pairwise_settings(self) -> Optional['PairwiseSettings']:
    return self._pairwise_settings or None

  @pairwise_settings.setter
  def pairwise_settings(self, pairwise_settings: Optional[Optional['PairwiseSettings']]):
    if pairwise_settings is None:
      del self.pairwise_settings
      return
    if not isinstance(pairwise_settings, PairwiseSettings):
      raise TypeError('pairwise_settings must be of type PairwiseSettings')
    self._pairwise_settings = pairwise_settings

  @property
  def use_model_proxy(self) -> bool:
    return self._use_model_proxy or False

  @use_model_proxy.setter
  def use_model_proxy(self, use_model_proxy: Optional[bool]):
    if use_model_proxy is None:
      del self.use_model_proxy
      return
    if not isinstance(use_model_proxy, bool):
      raise TypeError('use_model_proxy must be of type bool')
    self._use_model_proxy = use_model_proxy

  @property
  def max_episode_duration_seconds(self) -> int:
    return self._max_episode_duration_seconds or 0

  @max_episode_duration_seconds.setter
  def max_episode_duration_seconds(self, max_episode_duration_seconds: Optional[int]):
    if max_episode_duration_seconds is None:
      del self.max_episode_duration_seconds
      return
    if not isinstance(max_episode_duration_seconds, int):
      raise TypeError('max_episode_duration_seconds must be of type int')
    self._max_episode_duration_seconds = max_episode_duration_seconds

  @property
  def random_opponent_sample_with_replacement(self) -> bool:
    return self._random_opponent_sample_with_replacement

  @random_opponent_sample_with_replacement.setter
  def random_opponent_sample_with_replacement(self, random_opponent_sample_with_replacement: bool):
    if random_opponent_sample_with_replacement is None:
      del self.random_opponent_sample_with_replacement
      return
    if not isinstance(random_opponent_sample_with_replacement, bool):
      raise TypeError('random_opponent_sample_with_replacement must be of type bool')
    self._random_opponent_sample_with_replacement = random_opponent_sample_with_replacement

  @property
  def max_concurrent_episodes_per_submission(self) -> int:
    return self._max_concurrent_episodes_per_submission or 0

  @max_concurrent_episodes_per_submission.setter
  def max_concurrent_episodes_per_submission(self, max_concurrent_episodes_per_submission: Optional[int]):
    if max_concurrent_episodes_per_submission is None:
      del self.max_concurrent_episodes_per_submission
      return
    if not isinstance(max_concurrent_episodes_per_submission, int):
      raise TypeError('max_concurrent_episodes_per_submission must be of type int')
    self._max_concurrent_episodes_per_submission = max_concurrent_episodes_per_submission


class PairwiseSettings(KaggleObject):
  r"""
  Attributes:
    pairwise_target (int)
      The number of games to run for each ordered pair.
    seeded (bool)
      If the pairwise matches enforce 0 indexed incrementing seeds for each match
    early_stopping (bool)
      Enable early stopping. When true, pairs with well-established BT orderings
      get reduced game targets. New/uncertain pairs get the full target.
  """

  def __init__(self):
    self._pairwise_target = 0
    self._seeded = None
    self._early_stopping = None
    self._freeze()

  @property
  def pairwise_target(self) -> int:
    """The number of games to run for each ordered pair."""
    return self._pairwise_target

  @pairwise_target.setter
  def pairwise_target(self, pairwise_target: int):
    if pairwise_target is None:
      del self.pairwise_target
      return
    if not isinstance(pairwise_target, int):
      raise TypeError('pairwise_target must be of type int')
    self._pairwise_target = pairwise_target

  @property
  def seeded(self) -> bool:
    """If the pairwise matches enforce 0 indexed incrementing seeds for each match"""
    return self._seeded or False

  @seeded.setter
  def seeded(self, seeded: Optional[bool]):
    if seeded is None:
      del self.seeded
      return
    if not isinstance(seeded, bool):
      raise TypeError('seeded must be of type bool')
    self._seeded = seeded

  @property
  def early_stopping(self) -> bool:
    r"""
    Enable early stopping. When true, pairs with well-established BT orderings
    get reduced game targets. New/uncertain pairs get the full target.
    """
    return self._early_stopping or False

  @early_stopping.setter
  def early_stopping(self, early_stopping: Optional[bool]):
    if early_stopping is None:
      del self.early_stopping
      return
    if not isinstance(early_stopping, bool):
      raise TypeError('early_stopping must be of type bool')
    self._early_stopping = early_stopping


CompetitionSimulationSettings._fields = [
  FieldMetadata("submissionSizeLimitKb", "submission_size_limit_kb", "_submission_size_limit_kb", int, 0, PredefinedSerializer()),
  FieldMetadata("agentDiskKb", "agent_disk_kb", "_agent_disk_kb", int, 0, PredefinedSerializer()),
  FieldMetadata("agentRamKb", "agent_ram_kb", "_agent_ram_kb", int, 0, PredefinedSerializer()),
  FieldMetadata("agentCpuCoresPercent", "agent_cpu_cores_percent", "_agent_cpu_cores_percent", int, 0, PredefinedSerializer()),
  FieldMetadata("mirrorMatch", "mirror_match", "_mirror_match", bool, False, PredefinedSerializer()),
  FieldMetadata("enableInternet", "enable_internet", "_enable_internet", bool, False, PredefinedSerializer()),
  FieldMetadata("evaluationAlgorithmConfigOverride", "evaluation_algorithm_config_override", "_evaluation_algorithm_config_override", str, "", PredefinedSerializer()),
  FieldMetadata("extraAgents", "extra_agents", "_extra_agents", str, "", PredefinedSerializer()),
  FieldMetadata("maxConcurrentActiveEpisodes", "max_concurrent_active_episodes", "_max_concurrent_active_episodes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("generateEpisodesSubmissionRunsPerDay", "generate_episodes_submission_runs_per_day", "_generate_episodes_submission_runs_per_day", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("flatScheduler", "flat_scheduler", "_flat_scheduler", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("randomOpponentProbability", "random_opponent_probability", "_random_opponent_probability", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("prioritySubmissions", "priority_submissions", "_priority_submissions", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("priorityMatches", "priority_matches", "_priority_matches", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("schedulingMode", "scheduling_mode", "_scheduling_mode", SchedulingMode, None, EnumSerializer(), optional=True),
  FieldMetadata("pairwiseSettings", "pairwise_settings", "_pairwise_settings", PairwiseSettings, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("useModelProxy", "use_model_proxy", "_use_model_proxy", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxEpisodeDurationSeconds", "max_episode_duration_seconds", "_max_episode_duration_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("randomOpponentSampleWithReplacement", "random_opponent_sample_with_replacement", "_random_opponent_sample_with_replacement", bool, False, PredefinedSerializer()),
  FieldMetadata("validationEvaluationAlgorithmConfigOverride", "validation_evaluation_algorithm_config_override", "_validation_evaluation_algorithm_config_override", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxConcurrentEpisodesPerSubmission", "max_concurrent_episodes_per_submission", "_max_concurrent_episodes_per_submission", int, None, PredefinedSerializer(), optional=True),
]

PairwiseSettings._fields = [
  FieldMetadata("pairwiseTarget", "pairwise_target", "_pairwise_target", int, 0, PredefinedSerializer()),
  FieldMetadata("seeded", "seeded", "_seeded", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("earlyStopping", "early_stopping", "_early_stopping", bool, None, PredefinedSerializer(), optional=True),
]

