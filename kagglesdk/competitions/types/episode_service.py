from kagglesdk.competitions.types.episode import Episode, EpisodeState, EpisodeType
from kagglesdk.competitions.types.submission import Submission
from kagglesdk.competitions.types.team import Team
from kagglesdk.kaggle_object import *
from typing import List, Optional, Dict

class BenchmarkTaskVersionFilter(KaggleObject):
  r"""
  Attributes:
    benchmark_task_version_id (int)
    benchmark_model_version_id (int)
  """

  def __init__(self):
    self._benchmark_task_version_id = 0
    self._benchmark_model_version_id = 0
    self._freeze()

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id


class BulkCancelEpisodesRequest(KaggleObject):
  r"""
  Attributes:
    episode_ids (int)
  """

  def __init__(self):
    self._episode_ids = []
    self._freeze()

  @property
  def episode_ids(self) -> Optional[List[int]]:
    return self._episode_ids

  @episode_ids.setter
  def episode_ids(self, episode_ids: Optional[List[int]]):
    if episode_ids is None:
      del self.episode_ids
      return
    if not isinstance(episode_ids, list):
      raise TypeError('episode_ids must be of type list')
    if not all([isinstance(t, int) for t in episode_ids]):
      raise TypeError('episode_ids must contain only items of type int')
    self._episode_ids = episode_ids


class BulkCreateEpisodeRequest(KaggleObject):
  r"""
  Attributes:
    requests (CreateEpisodeRequest)
  """

  def __init__(self):
    self._requests = []
    self._freeze()

  @property
  def requests(self) -> Optional[List[Optional['CreateEpisodeRequest']]]:
    return self._requests

  @requests.setter
  def requests(self, requests: Optional[List[Optional['CreateEpisodeRequest']]]):
    if requests is None:
      del self.requests
      return
    if not isinstance(requests, list):
      raise TypeError('requests must be of type list')
    if not all([isinstance(t, CreateEpisodeRequest) for t in requests]):
      raise TypeError('requests must contain only items of type CreateEpisodeRequest')
    self._requests = requests


class BulkCreateEpisodeResponse(KaggleObject):
  r"""
  Attributes:
    episodes (Episode)
  """

  def __init__(self):
    self._episodes = []
    self._freeze()

  @property
  def episodes(self) -> Optional[List[Optional['Episode']]]:
    return self._episodes

  @episodes.setter
  def episodes(self, episodes: Optional[List[Optional['Episode']]]):
    if episodes is None:
      del self.episodes
      return
    if not isinstance(episodes, list):
      raise TypeError('episodes must be of type list')
    if not all([isinstance(t, Episode) for t in episodes]):
      raise TypeError('episodes must contain only items of type Episode')
    self._episodes = episodes


class BulkSetEpisodeRewardsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      Filter: only episodes in this competition are considered.
    episode_state (EpisodeState)
      Filter: only episodes in this state are considered.
    dry_run (bool)
      When true (default), matching episodes are counted but SetEpisodeRewards
      is not invoked. When false, SetEpisodeRewards is invoked for each match.
    min_age_hours (int)
      Filter: only episodes created at least this many hours ago are considered.
      Defaults to 0 (no minimum). Use this to exclude episodes that are still
      running (e.g. set to 1+ when targeting CREATED episodes so freshly-started
      ones don't get a premature rewards attempt against missing replays).
    max_episodes (int)
      Maximum number of episodes to update in a single call. Defaults to 1000
      when unspecified or 0, and is hard-capped at 10000 since SetEpisodeRewards
      is invoked sequentially per match. Matching episodes are processed in
      oldest-first order by create time, so re-running the call drains the
      backlog from the oldest end.
  """

  def __init__(self):
    self._competition_id = 0
    self._episode_state = EpisodeState.EPISODE_STATE_UNSPECIFIED
    self._dry_run = False
    self._min_age_hours = 0
    self._max_episodes = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    """Filter: only episodes in this competition are considered."""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def episode_state(self) -> 'EpisodeState':
    """Filter: only episodes in this state are considered."""
    return self._episode_state

  @episode_state.setter
  def episode_state(self, episode_state: 'EpisodeState'):
    if episode_state is None:
      del self.episode_state
      return
    if not isinstance(episode_state, EpisodeState):
      raise TypeError('episode_state must be of type EpisodeState')
    self._episode_state = episode_state

  @property
  def dry_run(self) -> bool:
    r"""
    When true (default), matching episodes are counted but SetEpisodeRewards
    is not invoked. When false, SetEpisodeRewards is invoked for each match.
    """
    return self._dry_run

  @dry_run.setter
  def dry_run(self, dry_run: bool):
    if dry_run is None:
      del self.dry_run
      return
    if not isinstance(dry_run, bool):
      raise TypeError('dry_run must be of type bool')
    self._dry_run = dry_run

  @property
  def min_age_hours(self) -> int:
    r"""
    Filter: only episodes created at least this many hours ago are considered.
    Defaults to 0 (no minimum). Use this to exclude episodes that are still
    running (e.g. set to 1+ when targeting CREATED episodes so freshly-started
    ones don't get a premature rewards attempt against missing replays).
    """
    return self._min_age_hours

  @min_age_hours.setter
  def min_age_hours(self, min_age_hours: int):
    if min_age_hours is None:
      del self.min_age_hours
      return
    if not isinstance(min_age_hours, int):
      raise TypeError('min_age_hours must be of type int')
    self._min_age_hours = min_age_hours

  @property
  def max_episodes(self) -> int:
    r"""
    Maximum number of episodes to update in a single call. Defaults to 1000
    when unspecified or 0, and is hard-capped at 10000 since SetEpisodeRewards
    is invoked sequentially per match. Matching episodes are processed in
    oldest-first order by create time, so re-running the call drains the
    backlog from the oldest end.
    """
    return self._max_episodes

  @max_episodes.setter
  def max_episodes(self, max_episodes: int):
    if max_episodes is None:
      del self.max_episodes
      return
    if not isinstance(max_episodes, int):
      raise TypeError('max_episodes must be of type int')
    self._max_episodes = max_episodes


class BulkSetEpisodeRewardsResponse(KaggleObject):
  r"""
  Attributes:
    episodes_found (int)
      Number of episodes matched by the filter.
    episodes_processed (int)
      Number of episodes for which SetEpisodeRewards was successfully invoked.
      Always 0 when dry_run is true.
  """

  def __init__(self):
    self._episodes_found = 0
    self._episodes_processed = 0
    self._freeze()

  @property
  def episodes_found(self) -> int:
    """Number of episodes matched by the filter."""
    return self._episodes_found

  @episodes_found.setter
  def episodes_found(self, episodes_found: int):
    if episodes_found is None:
      del self.episodes_found
      return
    if not isinstance(episodes_found, int):
      raise TypeError('episodes_found must be of type int')
    self._episodes_found = episodes_found

  @property
  def episodes_processed(self) -> int:
    r"""
    Number of episodes for which SetEpisodeRewards was successfully invoked.
    Always 0 when dry_run is true.
    """
    return self._episodes_processed

  @episodes_processed.setter
  def episodes_processed(self, episodes_processed: int):
    if episodes_processed is None:
      del self.episodes_processed
      return
    if not isinstance(episodes_processed, int):
      raise TypeError('episodes_processed must be of type int')
    self._episodes_processed = episodes_processed


class CancelEpisodeRequest(KaggleObject):
  r"""
  Attributes:
    episode_id (int)
  """

  def __init__(self):
    self._episode_id = 0
    self._freeze()

  @property
  def episode_id(self) -> int:
    return self._episode_id

  @episode_id.setter
  def episode_id(self, episode_id: int):
    if episode_id is None:
      del self.episode_id
      return
    if not isinstance(episode_id, int):
      raise TypeError('episode_id must be of type int')
    self._episode_id = episode_id


class CreateEpisodeRequest(KaggleObject):
  r"""
  Attributes:
    submission_ids (int)
    type (EpisodeType)
    seed (int)
  """

  def __init__(self):
    self._submission_ids = []
    self._type = EpisodeType.EPISODE_TYPE_UNSPECIFIED
    self._seed = 0
    self._freeze()

  @property
  def submission_ids(self) -> Optional[List[int]]:
    return self._submission_ids

  @submission_ids.setter
  def submission_ids(self, submission_ids: Optional[List[int]]):
    if submission_ids is None:
      del self.submission_ids
      return
    if not isinstance(submission_ids, list):
      raise TypeError('submission_ids must be of type list')
    if not all([isinstance(t, int) for t in submission_ids]):
      raise TypeError('submission_ids must contain only items of type int')
    self._submission_ids = submission_ids

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
  def seed(self) -> int:
    return self._seed

  @seed.setter
  def seed(self, seed: int):
    if seed is None:
      del self.seed
      return
    if not isinstance(seed, int):
      raise TypeError('seed must be of type int')
    self._seed = seed


class EpisodeTypeSummary(KaggleObject):
  r"""
  Attributes:
    type (EpisodeType)
    created_last_24h (int)
      Episodes with CreateTime in the last 24h, regardless of current state.
    running_count (int)
      Episodes currently in EpisodeState.Created (running/queued) at any age.
    completed_last_24h (int)
      Episodes with State = Completed and EndTime in the last 24h.
    errored_last_24h (int)
      Episodes with State = Errored and EndTime in the last 24h.
  """

  def __init__(self):
    self._type = EpisodeType.EPISODE_TYPE_UNSPECIFIED
    self._created_last_24h = 0
    self._running_count = 0
    self._completed_last_24h = 0
    self._errored_last_24h = 0
    self._freeze()

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
  def created_last_24h(self) -> int:
    """Episodes with CreateTime in the last 24h, regardless of current state."""
    return self._created_last_24h

  @created_last_24h.setter
  def created_last_24h(self, created_last_24h: int):
    if created_last_24h is None:
      del self.created_last_24h
      return
    if not isinstance(created_last_24h, int):
      raise TypeError('created_last_24h must be of type int')
    self._created_last_24h = created_last_24h

  @property
  def running_count(self) -> int:
    """Episodes currently in EpisodeState.Created (running/queued) at any age."""
    return self._running_count

  @running_count.setter
  def running_count(self, running_count: int):
    if running_count is None:
      del self.running_count
      return
    if not isinstance(running_count, int):
      raise TypeError('running_count must be of type int')
    self._running_count = running_count

  @property
  def completed_last_24h(self) -> int:
    """Episodes with State = Completed and EndTime in the last 24h."""
    return self._completed_last_24h

  @completed_last_24h.setter
  def completed_last_24h(self, completed_last_24h: int):
    if completed_last_24h is None:
      del self.completed_last_24h
      return
    if not isinstance(completed_last_24h, int):
      raise TypeError('completed_last_24h must be of type int')
    self._completed_last_24h = completed_last_24h

  @property
  def errored_last_24h(self) -> int:
    """Episodes with State = Errored and EndTime in the last 24h."""
    return self._errored_last_24h

  @errored_last_24h.setter
  def errored_last_24h(self, errored_last_24h: int):
    if errored_last_24h is None:
      del self.errored_last_24h
      return
    if not isinstance(errored_last_24h, int):
      raise TypeError('errored_last_24h must be of type int')
    self._errored_last_24h = errored_last_24h


class GenerateEpisodesForCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      Must be provided.
    num_episodes (int)
      Maximum number of episodes to create.  Currently we limit this to 100.
    num_agents_per_episode (int)
      Must be set.
    dry_run (bool)
      If set, we won't call BulkCreateEpisode.
  """

  def __init__(self):
    self._competition_id = 0
    self._num_episodes = 0
    self._num_agents_per_episode = 0
    self._dry_run = False
    self._freeze()

  @property
  def competition_id(self) -> int:
    """Must be provided."""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def num_episodes(self) -> int:
    """Maximum number of episodes to create.  Currently we limit this to 100."""
    return self._num_episodes

  @num_episodes.setter
  def num_episodes(self, num_episodes: int):
    if num_episodes is None:
      del self.num_episodes
      return
    if not isinstance(num_episodes, int):
      raise TypeError('num_episodes must be of type int')
    self._num_episodes = num_episodes

  @property
  def num_agents_per_episode(self) -> int:
    """Must be set."""
    return self._num_agents_per_episode

  @num_agents_per_episode.setter
  def num_agents_per_episode(self, num_agents_per_episode: int):
    if num_agents_per_episode is None:
      del self.num_agents_per_episode
      return
    if not isinstance(num_agents_per_episode, int):
      raise TypeError('num_agents_per_episode must be of type int')
    self._num_agents_per_episode = num_agents_per_episode

  @property
  def dry_run(self) -> bool:
    """If set, we won't call BulkCreateEpisode."""
    return self._dry_run

  @dry_run.setter
  def dry_run(self, dry_run: bool):
    if dry_run is None:
      del self.dry_run
      return
    if not isinstance(dry_run, bool):
      raise TypeError('dry_run must be of type bool')
    self._dry_run = dry_run


class GenerateEpisodesForCompetitionResponse(KaggleObject):
  r"""
  Attributes:
    bulk_create_episode_request (BulkCreateEpisodeRequest)
      The BulkCreateEpisodeRequest we generated.
    bulk_create_episode_response (BulkCreateEpisodeResponse)
      The response from calling BulkCreateEpisode, if dry_run was false.
  """

  def __init__(self):
    self._bulk_create_episode_request = None
    self._bulk_create_episode_response = None
    self._freeze()

  @property
  def bulk_create_episode_request(self) -> Optional['BulkCreateEpisodeRequest']:
    """The BulkCreateEpisodeRequest we generated."""
    return self._bulk_create_episode_request

  @bulk_create_episode_request.setter
  def bulk_create_episode_request(self, bulk_create_episode_request: Optional['BulkCreateEpisodeRequest']):
    if bulk_create_episode_request is None:
      del self.bulk_create_episode_request
      return
    if not isinstance(bulk_create_episode_request, BulkCreateEpisodeRequest):
      raise TypeError('bulk_create_episode_request must be of type BulkCreateEpisodeRequest')
    self._bulk_create_episode_request = bulk_create_episode_request

  @property
  def bulk_create_episode_response(self) -> Optional['BulkCreateEpisodeResponse']:
    """The response from calling BulkCreateEpisode, if dry_run was false."""
    return self._bulk_create_episode_response

  @bulk_create_episode_response.setter
  def bulk_create_episode_response(self, bulk_create_episode_response: Optional['BulkCreateEpisodeResponse']):
    if bulk_create_episode_response is None:
      del self.bulk_create_episode_response
      return
    if not isinstance(bulk_create_episode_response, BulkCreateEpisodeResponse):
      raise TypeError('bulk_create_episode_response must be of type BulkCreateEpisodeResponse')
    self._bulk_create_episode_response = bulk_create_episode_response


class GetEpisodeRequest(KaggleObject):
  r"""
  Attributes:
    episode_id (int)
  """

  def __init__(self):
    self._episode_id = 0
    self._freeze()

  @property
  def episode_id(self) -> int:
    return self._episode_id

  @episode_id.setter
  def episode_id(self, episode_id: int):
    if episode_id is None:
      del self.episode_id
      return
    if not isinstance(episode_id, int):
      raise TypeError('episode_id must be of type int')
    self._episode_id = episode_id


class GetEpisodeResponse(KaggleObject):
  r"""
  Attributes:
    episode (Episode)
    teams (Team)
  """

  def __init__(self):
    self._episode = None
    self._teams = []
    self._freeze()

  @property
  def episode(self) -> Optional['Episode']:
    return self._episode

  @episode.setter
  def episode(self, episode: Optional['Episode']):
    if episode is None:
      del self.episode
      return
    if not isinstance(episode, Episode):
      raise TypeError('episode must be of type Episode')
    self._episode = episode

  @property
  def teams(self) -> Optional[List[Optional['Team']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['Team']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, Team) for t in teams]):
      raise TypeError('teams must contain only items of type Team')
    self._teams = teams


class GetEpisodeSummaryRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class GetEpisodeSummaryResponse(KaggleObject):
  r"""
  Attributes:
    type_summaries (EpisodeTypeSummary)
      One entry per EpisodeType with activity in the last 24h or currently
      running. Types with no recent or running episodes are omitted, so a
      never-used type will not appear at all. (A map<EpisodeType, ...> would
      be nicer but proto3 disallows enum-typed map keys.)
    team_episode_counts (TeamEpisodeCount)
  """

  def __init__(self):
    self._type_summaries = []
    self._team_episode_counts = []
    self._freeze()

  @property
  def type_summaries(self) -> Optional[List[Optional['EpisodeTypeSummary']]]:
    r"""
    One entry per EpisodeType with activity in the last 24h or currently
    running. Types with no recent or running episodes are omitted, so a
    never-used type will not appear at all. (A map<EpisodeType, ...> would
    be nicer but proto3 disallows enum-typed map keys.)
    """
    return self._type_summaries

  @type_summaries.setter
  def type_summaries(self, type_summaries: Optional[List[Optional['EpisodeTypeSummary']]]):
    if type_summaries is None:
      del self.type_summaries
      return
    if not isinstance(type_summaries, list):
      raise TypeError('type_summaries must be of type list')
    if not all([isinstance(t, EpisodeTypeSummary) for t in type_summaries]):
      raise TypeError('type_summaries must contain only items of type EpisodeTypeSummary')
    self._type_summaries = type_summaries

  @property
  def team_episode_counts(self) -> Optional[List[Optional['TeamEpisodeCount']]]:
    return self._team_episode_counts

  @team_episode_counts.setter
  def team_episode_counts(self, team_episode_counts: Optional[List[Optional['TeamEpisodeCount']]]):
    if team_episode_counts is None:
      del self.team_episode_counts
      return
    if not isinstance(team_episode_counts, list):
      raise TypeError('team_episode_counts must be of type list')
    if not all([isinstance(t, TeamEpisodeCount) for t in team_episode_counts]):
      raise TypeError('team_episode_counts must contain only items of type TeamEpisodeCount')
    self._team_episode_counts = team_episode_counts


class ListEpisodesFromCompetitionFilters(KaggleObject):
  r"""
  Attributes:
    state (EpisodeState)
    type (EpisodeType)
    team_ids (int)
    episode_ids (int)
  """

  def __init__(self):
    self._state = None
    self._type = None
    self._team_ids = []
    self._episode_ids = []
    self._freeze()

  @property
  def state(self) -> 'EpisodeState':
    return self._state or EpisodeState.EPISODE_STATE_UNSPECIFIED

  @state.setter
  def state(self, state: Optional['EpisodeState']):
    if state is None:
      del self.state
      return
    if not isinstance(state, EpisodeState):
      raise TypeError('state must be of type EpisodeState')
    self._state = state

  @property
  def type(self) -> 'EpisodeType':
    return self._type or EpisodeType.EPISODE_TYPE_UNSPECIFIED

  @type.setter
  def type(self, type: Optional['EpisodeType']):
    if type is None:
      del self.type
      return
    if not isinstance(type, EpisodeType):
      raise TypeError('type must be of type EpisodeType')
    self._type = type

  @property
  def team_ids(self) -> Optional[List[int]]:
    return self._team_ids

  @team_ids.setter
  def team_ids(self, team_ids: Optional[List[int]]):
    if team_ids is None:
      del self.team_ids
      return
    if not isinstance(team_ids, list):
      raise TypeError('team_ids must be of type list')
    if not all([isinstance(t, int) for t in team_ids]):
      raise TypeError('team_ids must contain only items of type int')
    self._team_ids = team_ids

  @property
  def episode_ids(self) -> Optional[List[int]]:
    return self._episode_ids

  @episode_ids.setter
  def episode_ids(self, episode_ids: Optional[List[int]]):
    if episode_ids is None:
      del self.episode_ids
      return
    if not isinstance(episode_ids, list):
      raise TypeError('episode_ids must be of type list')
    if not all([isinstance(t, int) for t in episode_ids]):
      raise TypeError('episode_ids must contain only items of type int')
    self._episode_ids = episode_ids


class ListEpisodesFromCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    page_size (int)
    page_token (str)
    skip (int)
    filters (ListEpisodesFromCompetitionFilters)
      Optional list episodes filters:
      episode type, episode state.
  """

  def __init__(self):
    self._competition_id = 0
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._filters = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

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

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def filters(self) -> Optional['ListEpisodesFromCompetitionFilters']:
    r"""
    Optional list episodes filters:
    episode type, episode state.
    """
    return self._filters

  @filters.setter
  def filters(self, filters: Optional['ListEpisodesFromCompetitionFilters']):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, ListEpisodesFromCompetitionFilters):
      raise TypeError('filters must be of type ListEpisodesFromCompetitionFilters')
    self._filters = filters


class ListEpisodesFromCompetitionResponse(KaggleObject):
  r"""
  Attributes:
    episodes (Episode)
    total_episodes (int)
    total_pages (int)
    next_page_token (str)
    average_episode_duration_ms (float)
      Average duration (in ms) of completed episodes for this competition.
      Used by the frontend to estimate remaining time for active episodes.
    completed_episode_count (int)
      Number of completed episodes used to compute the average duration.
      The frontend uses this to require a minimum sample size before showing
      estimates.
  """

  def __init__(self):
    self._episodes = []
    self._total_episodes = 0
    self._total_pages = 0
    self._next_page_token = None
    self._average_episode_duration_ms = None
    self._completed_episode_count = None
    self._freeze()

  @property
  def episodes(self) -> Optional[List[Optional['Episode']]]:
    return self._episodes

  @episodes.setter
  def episodes(self, episodes: Optional[List[Optional['Episode']]]):
    if episodes is None:
      del self.episodes
      return
    if not isinstance(episodes, list):
      raise TypeError('episodes must be of type list')
    if not all([isinstance(t, Episode) for t in episodes]):
      raise TypeError('episodes must contain only items of type Episode')
    self._episodes = episodes

  @property
  def total_episodes(self) -> int:
    return self._total_episodes

  @total_episodes.setter
  def total_episodes(self, total_episodes: int):
    if total_episodes is None:
      del self.total_episodes
      return
    if not isinstance(total_episodes, int):
      raise TypeError('total_episodes must be of type int')
    self._total_episodes = total_episodes

  @property
  def total_pages(self) -> int:
    return self._total_pages

  @total_pages.setter
  def total_pages(self, total_pages: int):
    if total_pages is None:
      del self.total_pages
      return
    if not isinstance(total_pages, int):
      raise TypeError('total_pages must be of type int')
    self._total_pages = total_pages

  @property
  def next_page_token(self) -> str:
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def average_episode_duration_ms(self) -> float:
    r"""
    Average duration (in ms) of completed episodes for this competition.
    Used by the frontend to estimate remaining time for active episodes.
    """
    return self._average_episode_duration_ms or 0.0

  @average_episode_duration_ms.setter
  def average_episode_duration_ms(self, average_episode_duration_ms: Optional[float]):
    if average_episode_duration_ms is None:
      del self.average_episode_duration_ms
      return
    if not isinstance(average_episode_duration_ms, float):
      raise TypeError('average_episode_duration_ms must be of type float')
    self._average_episode_duration_ms = average_episode_duration_ms

  @property
  def completed_episode_count(self) -> int:
    r"""
    Number of completed episodes used to compute the average duration.
    The frontend uses this to require a minimum sample size before showing
    estimates.
    """
    return self._completed_episode_count or 0

  @completed_episode_count.setter
  def completed_episode_count(self, completed_episode_count: Optional[int]):
    if completed_episode_count is None:
      del self.completed_episode_count
      return
    if not isinstance(completed_episode_count, int):
      raise TypeError('completed_episode_count must be of type int')
    self._completed_episode_count = completed_episode_count


class ListEpisodesRequest(KaggleObject):
  r"""
  Only the first populated ID filter will be used. Exception thrown if none
  are populated.

  Attributes:
    ids (int)
    submission_id (int)
    benchmark_task_version_filter (BenchmarkTaskVersionFilter)
    successful_only (bool)
    include_in_progress (bool)
      When true, episodes still in CREATED state (queued / in-progress) are
      returned alongside completed episodes. Intended for the submission owner's
      own view so they can see which games their submission is currently playing.
  """

  def __init__(self):
    self._ids = []
    self._submission_id = None
    self._benchmark_task_version_filter = None
    self._successful_only = None
    self._include_in_progress = None
    self._freeze()

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids

  @property
  def submission_id(self) -> int:
    return self._submission_id or 0

  @submission_id.setter
  def submission_id(self, submission_id: Optional[int]):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def benchmark_task_version_filter(self) -> Optional['BenchmarkTaskVersionFilter']:
    return self._benchmark_task_version_filter or None

  @benchmark_task_version_filter.setter
  def benchmark_task_version_filter(self, benchmark_task_version_filter: Optional[Optional['BenchmarkTaskVersionFilter']]):
    if benchmark_task_version_filter is None:
      del self.benchmark_task_version_filter
      return
    if not isinstance(benchmark_task_version_filter, BenchmarkTaskVersionFilter):
      raise TypeError('benchmark_task_version_filter must be of type BenchmarkTaskVersionFilter')
    self._benchmark_task_version_filter = benchmark_task_version_filter

  @property
  def successful_only(self) -> bool:
    return self._successful_only or False

  @successful_only.setter
  def successful_only(self, successful_only: Optional[bool]):
    if successful_only is None:
      del self.successful_only
      return
    if not isinstance(successful_only, bool):
      raise TypeError('successful_only must be of type bool')
    self._successful_only = successful_only

  @property
  def include_in_progress(self) -> bool:
    r"""
    When true, episodes still in CREATED state (queued / in-progress) are
    returned alongside completed episodes. Intended for the submission owner's
    own view so they can see which games their submission is currently playing.
    """
    return self._include_in_progress or False

  @include_in_progress.setter
  def include_in_progress(self, include_in_progress: Optional[bool]):
    if include_in_progress is None:
      del self.include_in_progress
      return
    if not isinstance(include_in_progress, bool):
      raise TypeError('include_in_progress must be of type bool')
    self._include_in_progress = include_in_progress


class ListEpisodesResponse(KaggleObject):
  r"""
  Attributes:
    episodes (Episode)
      EpisodeAgents refs populated, each with no refs, instead pulled out below.
    submissions (Submission)
      Distinct Submissions that would've been used for EpisodeAgent.Submission
      in above.  No refs.
    teams (Team)
      Distinct Teams that would've been used for Submission.Team above.  No refs.
  """

  def __init__(self):
    self._episodes = []
    self._submissions = []
    self._teams = []
    self._freeze()

  @property
  def episodes(self) -> Optional[List[Optional['Episode']]]:
    """EpisodeAgents refs populated, each with no refs, instead pulled out below."""
    return self._episodes

  @episodes.setter
  def episodes(self, episodes: Optional[List[Optional['Episode']]]):
    if episodes is None:
      del self.episodes
      return
    if not isinstance(episodes, list):
      raise TypeError('episodes must be of type list')
    if not all([isinstance(t, Episode) for t in episodes]):
      raise TypeError('episodes must contain only items of type Episode')
    self._episodes = episodes

  @property
  def submissions(self) -> Optional[List[Optional['Submission']]]:
    r"""
    Distinct Submissions that would've been used for EpisodeAgent.Submission
    in above.  No refs.
    """
    return self._submissions

  @submissions.setter
  def submissions(self, submissions: Optional[List[Optional['Submission']]]):
    if submissions is None:
      del self.submissions
      return
    if not isinstance(submissions, list):
      raise TypeError('submissions must be of type list')
    if not all([isinstance(t, Submission) for t in submissions]):
      raise TypeError('submissions must contain only items of type Submission')
    self._submissions = submissions

  @property
  def teams(self) -> Optional[List[Optional['Team']]]:
    """Distinct Teams that would've been used for Submission.Team above.  No refs."""
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['Team']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, Team) for t in teams]):
      raise TypeError('teams must contain only items of type Team')
    self._teams = teams


class ListValidationEpisodesRequest(KaggleObject):
  r"""
  Attributes:
    submission_ids (int)
  """

  def __init__(self):
    self._submission_ids = []
    self._freeze()

  @property
  def submission_ids(self) -> Optional[List[int]]:
    return self._submission_ids

  @submission_ids.setter
  def submission_ids(self, submission_ids: Optional[List[int]]):
    if submission_ids is None:
      del self.submission_ids
      return
    if not isinstance(submission_ids, list):
      raise TypeError('submission_ids must be of type list')
    if not all([isinstance(t, int) for t in submission_ids]):
      raise TypeError('submission_ids must contain only items of type int')
    self._submission_ids = submission_ids


class ListValidationEpisodesResponse(KaggleObject):
  r"""
  Attributes:
    submission_validation_episode_map (int)
  """

  def __init__(self):
    self._submission_validation_episode_map = {}
    self._freeze()

  @property
  def submission_validation_episode_map(self) -> Optional[Dict[int, int]]:
    return self._submission_validation_episode_map

  @submission_validation_episode_map.setter
  def submission_validation_episode_map(self, submission_validation_episode_map: Optional[Dict[int, int]]):
    if submission_validation_episode_map is None:
      del self.submission_validation_episode_map
      return
    if not isinstance(submission_validation_episode_map, dict):
      raise TypeError('submission_validation_episode_map must be of type dict')
    if not all([isinstance(v, int) for k, v in submission_validation_episode_map]):
      raise TypeError('submission_validation_episode_map must contain only items of type int')
    self._submission_validation_episode_map = submission_validation_episode_map


class MarkEnvironmentSubmissionValidatedRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
  """

  def __init__(self):
    self._submission_id = 0
    self._freeze()

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


class SetEpisodeErroredRequest(KaggleObject):
  r"""
  This sets Episode.State = EpisodeState.ERRORED

  Attributes:
    episode_id (int)
  """

  def __init__(self):
    self._episode_id = 0
    self._freeze()

  @property
  def episode_id(self) -> int:
    return self._episode_id

  @episode_id.setter
  def episode_id(self, episode_id: int):
    if episode_id is None:
      del self.episode_id
      return
    if not isinstance(episode_id, int):
      raise TypeError('episode_id must be of type int')
    self._episode_id = episode_id


class TeamEpisodeCount(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    episode_state (EpisodeState)
    episode_count (int)
    team_name (str)
  """

  def __init__(self):
    self._team_id = 0
    self._episode_state = EpisodeState.EPISODE_STATE_UNSPECIFIED
    self._episode_count = 0
    self._team_name = ""
    self._freeze()

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def episode_state(self) -> 'EpisodeState':
    return self._episode_state

  @episode_state.setter
  def episode_state(self, episode_state: 'EpisodeState'):
    if episode_state is None:
      del self.episode_state
      return
    if not isinstance(episode_state, EpisodeState):
      raise TypeError('episode_state must be of type EpisodeState')
    self._episode_state = episode_state

  @property
  def episode_count(self) -> int:
    return self._episode_count

  @episode_count.setter
  def episode_count(self, episode_count: int):
    if episode_count is None:
      del self.episode_count
      return
    if not isinstance(episode_count, int):
      raise TypeError('episode_count must be of type int')
    self._episode_count = episode_count

  @property
  def team_name(self) -> str:
    return self._team_name

  @team_name.setter
  def team_name(self, team_name: str):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name


BenchmarkTaskVersionFilter._fields = [
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
]

BulkCancelEpisodesRequest._fields = [
  FieldMetadata("episodeIds", "episode_ids", "_episode_ids", int, [], ListSerializer(PredefinedSerializer())),
]

BulkCreateEpisodeRequest._fields = [
  FieldMetadata("requests", "requests", "_requests", CreateEpisodeRequest, [], ListSerializer(KaggleObjectSerializer())),
]

BulkCreateEpisodeResponse._fields = [
  FieldMetadata("episodes", "episodes", "_episodes", Episode, [], ListSerializer(KaggleObjectSerializer())),
]

BulkSetEpisodeRewardsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("episodeState", "episode_state", "_episode_state", EpisodeState, EpisodeState.EPISODE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dryRun", "dry_run", "_dry_run", bool, False, PredefinedSerializer()),
  FieldMetadata("minAgeHours", "min_age_hours", "_min_age_hours", int, 0, PredefinedSerializer()),
  FieldMetadata("maxEpisodes", "max_episodes", "_max_episodes", int, 0, PredefinedSerializer()),
]

BulkSetEpisodeRewardsResponse._fields = [
  FieldMetadata("episodesFound", "episodes_found", "_episodes_found", int, 0, PredefinedSerializer()),
  FieldMetadata("episodesProcessed", "episodes_processed", "_episodes_processed", int, 0, PredefinedSerializer()),
]

CancelEpisodeRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

CreateEpisodeRequest._fields = [
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("type", "type", "_type", EpisodeType, EpisodeType.EPISODE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("seed", "seed", "_seed", int, 0, PredefinedSerializer()),
]

EpisodeTypeSummary._fields = [
  FieldMetadata("type", "type", "_type", EpisodeType, EpisodeType.EPISODE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("createdLast24h", "created_last_24h", "_created_last_24h", int, 0, PredefinedSerializer()),
  FieldMetadata("runningCount", "running_count", "_running_count", int, 0, PredefinedSerializer()),
  FieldMetadata("completedLast24h", "completed_last_24h", "_completed_last_24h", int, 0, PredefinedSerializer()),
  FieldMetadata("erroredLast24h", "errored_last_24h", "_errored_last_24h", int, 0, PredefinedSerializer()),
]

GenerateEpisodesForCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("numEpisodes", "num_episodes", "_num_episodes", int, 0, PredefinedSerializer()),
  FieldMetadata("numAgentsPerEpisode", "num_agents_per_episode", "_num_agents_per_episode", int, 0, PredefinedSerializer()),
  FieldMetadata("dryRun", "dry_run", "_dry_run", bool, False, PredefinedSerializer()),
]

GenerateEpisodesForCompetitionResponse._fields = [
  FieldMetadata("bulkCreateEpisodeRequest", "bulk_create_episode_request", "_bulk_create_episode_request", BulkCreateEpisodeRequest, None, KaggleObjectSerializer()),
  FieldMetadata("bulkCreateEpisodeResponse", "bulk_create_episode_response", "_bulk_create_episode_response", BulkCreateEpisodeResponse, None, KaggleObjectSerializer()),
]

GetEpisodeRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

GetEpisodeResponse._fields = [
  FieldMetadata("episode", "episode", "_episode", Episode, None, KaggleObjectSerializer()),
  FieldMetadata("teams", "teams", "_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
]

GetEpisodeSummaryRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetEpisodeSummaryResponse._fields = [
  FieldMetadata("typeSummaries", "type_summaries", "_type_summaries", EpisodeTypeSummary, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teamEpisodeCounts", "team_episode_counts", "_team_episode_counts", TeamEpisodeCount, [], ListSerializer(KaggleObjectSerializer())),
]

ListEpisodesFromCompetitionFilters._fields = [
  FieldMetadata("state", "state", "_state", EpisodeState, None, EnumSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", EpisodeType, None, EnumSerializer(), optional=True),
  FieldMetadata("teamIds", "team_ids", "_team_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("episodeIds", "episode_ids", "_episode_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListEpisodesFromCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("filters", "filters", "_filters", ListEpisodesFromCompetitionFilters, None, KaggleObjectSerializer()),
]

ListEpisodesFromCompetitionResponse._fields = [
  FieldMetadata("episodes", "episodes", "_episodes", Episode, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalEpisodes", "total_episodes", "_total_episodes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalPages", "total_pages", "_total_pages", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("averageEpisodeDurationMs", "average_episode_duration_ms", "_average_episode_duration_ms", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("completedEpisodeCount", "completed_episode_count", "_completed_episode_count", int, None, PredefinedSerializer(), optional=True),
]

ListEpisodesRequest._fields = [
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionFilter", "benchmark_task_version_filter", "_benchmark_task_version_filter", BenchmarkTaskVersionFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("successfulOnly", "successful_only", "_successful_only", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includeInProgress", "include_in_progress", "_include_in_progress", bool, None, PredefinedSerializer(), optional=True),
]

ListEpisodesResponse._fields = [
  FieldMetadata("episodes", "episodes", "_episodes", Episode, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("submissions", "submissions", "_submissions", Submission, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teams", "teams", "_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
]

ListValidationEpisodesRequest._fields = [
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListValidationEpisodesResponse._fields = [
  FieldMetadata("submissionValidationEpisodeMap", "submission_validation_episode_map", "_submission_validation_episode_map", int, {}, MapSerializer(PredefinedSerializer())),
]

MarkEnvironmentSubmissionValidatedRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
]

SetEpisodeErroredRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

TeamEpisodeCount._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("episodeState", "episode_state", "_episode_state", EpisodeState, EpisodeState.EPISODE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("episodeCount", "episode_count", "_episode_count", int, 0, PredefinedSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, "", PredefinedSerializer()),
]

