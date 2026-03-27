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


class GetEpisodeReplayRequest(KaggleObject):
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


class ListEpisodesFromCompetitionFilters(KaggleObject):
  r"""
  Attributes:
    state (EpisodeState)
    type (EpisodeType)
    team_ids (int)
  """

  def __init__(self):
    self._state = None
    self._type = None
    self._team_ids = []
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
  """

  def __init__(self):
    self._episodes = []
    self._total_episodes = 0
    self._total_pages = 0
    self._next_page_token = None
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


class ListEpisodesRequest(KaggleObject):
  r"""
  Only the first populated ID filter will be used. Exception thrown if none
  are populated.

  Attributes:
    ids (int)
    submission_id (int)
    benchmark_task_version_filter (BenchmarkTaskVersionFilter)
    successful_only (bool)
  """

  def __init__(self):
    self._ids = []
    self._submission_id = None
    self._benchmark_task_version_filter = None
    self._successful_only = None
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

CancelEpisodeRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

CreateEpisodeRequest._fields = [
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("type", "type", "_type", EpisodeType, EpisodeType.EPISODE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("seed", "seed", "_seed", int, 0, PredefinedSerializer()),
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

GetEpisodeReplayRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

GetEpisodeRequest._fields = [
  FieldMetadata("episodeId", "episode_id", "_episode_id", int, 0, PredefinedSerializer()),
]

GetEpisodeResponse._fields = [
  FieldMetadata("episode", "episode", "_episode", Episode, None, KaggleObjectSerializer()),
  FieldMetadata("teams", "teams", "_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
]

ListEpisodesFromCompetitionFilters._fields = [
  FieldMetadata("state", "state", "_state", EpisodeState, None, EnumSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", EpisodeType, None, EnumSerializer(), optional=True),
  FieldMetadata("teamIds", "team_ids", "_team_ids", int, [], ListSerializer(PredefinedSerializer())),
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
]

ListEpisodesRequest._fields = [
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionFilter", "benchmark_task_version_filter", "_benchmark_task_version_filter", BenchmarkTaskVersionFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("successfulOnly", "successful_only", "_successful_only", bool, None, PredefinedSerializer(), optional=True),
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

