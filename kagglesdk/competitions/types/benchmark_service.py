import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkLeaderboardDisplayType
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkVersionModelMapping, UnevenConfidenceInterval
from kagglesdk.kaggle_object import *
from typing import List, Optional, Dict

class RankingMetric(enum.Enum):
  RANKING_METRIC_UNSPECIFIED = 0
  BRADLEY_TERRY = 1
  """Standard Bradley-Terry with MAP regularization and confidence intervals."""
  MM_BRADLEY_TERRY = 2
  r"""
  Bradley-Terry with smoothing-based regularization and OpenSpiel-style
  Elo scaling. Ratings are anchored to a minimum floor instead of a fixed
  base.
  """
  MEAN_REWARD_PER_100 = 3
  r"""
  Bootstrapped mean reward per 100 actions. Each model's score is the
  average reward normalized to a 100-action window, with 95% confidence
  intervals from bootstrap resampling.

  This is mainly a metric specifically for Poker, renamed from Mean BB/100,
  where each episode contains 100 hands.
  """

class CreateBenchmarkFromCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    secondary_columns (SecondaryColumn)
      Optional secondary columns to create as child tasks of the benchmark's
      root task version. Each column becomes a BenchmarkTask with a
      BenchmarkTaskVersionMapping to the root task version.
    name (str)
      The name for the resulting benchmark.
    slug (str)
      The slug for the resulting benchmark.
    main_column_name (str)
      Optional display name for the main column (root task version).
      Defaults to the benchmark name if unspecified.
    main_column_display_type (BenchmarkLeaderboardDisplayType)
      Optional display type for the main column (root task version).
      Defaults to COUNTS if unspecified.
  """

  def __init__(self):
    self._competition_id = 0
    self._secondary_columns = []
    self._name = ""
    self._slug = ""
    self._main_column_name = None
    self._main_column_display_type = None
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
  def secondary_columns(self) -> Optional[List[Optional['SecondaryColumn']]]:
    r"""
    Optional secondary columns to create as child tasks of the benchmark's
    root task version. Each column becomes a BenchmarkTask with a
    BenchmarkTaskVersionMapping to the root task version.
    """
    return self._secondary_columns

  @secondary_columns.setter
  def secondary_columns(self, secondary_columns: Optional[List[Optional['SecondaryColumn']]]):
    if secondary_columns is None:
      del self.secondary_columns
      return
    if not isinstance(secondary_columns, list):
      raise TypeError('secondary_columns must be of type list')
    if not all([isinstance(t, SecondaryColumn) for t in secondary_columns]):
      raise TypeError('secondary_columns must contain only items of type SecondaryColumn')
    self._secondary_columns = secondary_columns

  @property
  def name(self) -> str:
    """The name for the resulting benchmark."""
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
  def slug(self) -> str:
    """The slug for the resulting benchmark."""
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def main_column_name(self) -> str:
    r"""
    Optional display name for the main column (root task version).
    Defaults to the benchmark name if unspecified.
    """
    return self._main_column_name or ""

  @main_column_name.setter
  def main_column_name(self, main_column_name: Optional[str]):
    if main_column_name is None:
      del self.main_column_name
      return
    if not isinstance(main_column_name, str):
      raise TypeError('main_column_name must be of type str')
    self._main_column_name = main_column_name

  @property
  def main_column_display_type(self) -> 'BenchmarkLeaderboardDisplayType':
    r"""
    Optional display type for the main column (root task version).
    Defaults to COUNTS if unspecified.
    """
    return self._main_column_display_type or BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED

  @main_column_display_type.setter
  def main_column_display_type(self, main_column_display_type: Optional['BenchmarkLeaderboardDisplayType']):
    if main_column_display_type is None:
      del self.main_column_display_type
      return
    if not isinstance(main_column_display_type, BenchmarkLeaderboardDisplayType):
      raise TypeError('main_column_display_type must be of type BenchmarkLeaderboardDisplayType')
    self._main_column_display_type = main_column_display_type


class ExportLeaderboardToBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    benchmark_version_id (int)
    reset (bool)
      Whether to clear the set of episodes currently tied to the benchmark
      version
    dry_run (bool)
      Whether to actually update the DB
    ranking_metric (RankingMetric)
      Which ranking algorithm to use for computing Elo ratings
    exclude_elo (bool)
      Whether to skip inserting Elo scores to the benchmark leaderboard.
      Defaults to false (Elo scores are included).
    exclude_cost_and_tokens (bool)
      Whether to skip inserting cost and token usage columns to the
      benchmark leaderboard. Defaults to false (cost and tokens are
      included).
    exclude_episodes (bool)
      Whether to skip updating episode records in the database (i.e. do not
      tie them to the benchmark version). Defaults to false (episodes are
      included).
  """

  def __init__(self):
    self._competition_id = 0
    self._benchmark_version_id = 0
    self._reset = None
    self._dry_run = None
    self._ranking_metric = RankingMetric.RANKING_METRIC_UNSPECIFIED
    self._exclude_elo = None
    self._exclude_cost_and_tokens = None
    self._exclude_episodes = None
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
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def reset(self) -> bool:
    r"""
    Whether to clear the set of episodes currently tied to the benchmark
    version
    """
    return self._reset or False

  @reset.setter
  def reset(self, reset: Optional[bool]):
    if reset is None:
      del self.reset
      return
    if not isinstance(reset, bool):
      raise TypeError('reset must be of type bool')
    self._reset = reset

  @property
  def dry_run(self) -> bool:
    """Whether to actually update the DB"""
    return self._dry_run or False

  @dry_run.setter
  def dry_run(self, dry_run: Optional[bool]):
    if dry_run is None:
      del self.dry_run
      return
    if not isinstance(dry_run, bool):
      raise TypeError('dry_run must be of type bool')
    self._dry_run = dry_run

  @property
  def ranking_metric(self) -> 'RankingMetric':
    """Which ranking algorithm to use for computing Elo ratings"""
    return self._ranking_metric

  @ranking_metric.setter
  def ranking_metric(self, ranking_metric: 'RankingMetric'):
    if ranking_metric is None:
      del self.ranking_metric
      return
    if not isinstance(ranking_metric, RankingMetric):
      raise TypeError('ranking_metric must be of type RankingMetric')
    self._ranking_metric = ranking_metric

  @property
  def exclude_elo(self) -> bool:
    r"""
    Whether to skip inserting Elo scores to the benchmark leaderboard.
    Defaults to false (Elo scores are included).
    """
    return self._exclude_elo or False

  @exclude_elo.setter
  def exclude_elo(self, exclude_elo: Optional[bool]):
    if exclude_elo is None:
      del self.exclude_elo
      return
    if not isinstance(exclude_elo, bool):
      raise TypeError('exclude_elo must be of type bool')
    self._exclude_elo = exclude_elo

  @property
  def exclude_cost_and_tokens(self) -> bool:
    r"""
    Whether to skip inserting cost and token usage columns to the
    benchmark leaderboard. Defaults to false (cost and tokens are
    included).
    """
    return self._exclude_cost_and_tokens or False

  @exclude_cost_and_tokens.setter
  def exclude_cost_and_tokens(self, exclude_cost_and_tokens: Optional[bool]):
    if exclude_cost_and_tokens is None:
      del self.exclude_cost_and_tokens
      return
    if not isinstance(exclude_cost_and_tokens, bool):
      raise TypeError('exclude_cost_and_tokens must be of type bool')
    self._exclude_cost_and_tokens = exclude_cost_and_tokens

  @property
  def exclude_episodes(self) -> bool:
    r"""
    Whether to skip updating episode records in the database (i.e. do not
    tie them to the benchmark version). Defaults to false (episodes are
    included).
    """
    return self._exclude_episodes or False

  @exclude_episodes.setter
  def exclude_episodes(self, exclude_episodes: Optional[bool]):
    if exclude_episodes is None:
      del self.exclude_episodes
      return
    if not isinstance(exclude_episodes, bool):
      raise TypeError('exclude_episodes must be of type bool')
    self._exclude_episodes = exclude_episodes


class ExportLeaderboardToBenchmarkResponse(KaggleObject):
  r"""
  Attributes:
    num_episodes (int)
      How many episodes are now opted-in to the benchmark leaderboard
    model_results (ModelResult)
      Per-model usage and ranking data, keyed by benchmark_model_version_id
  """

  def __init__(self):
    self._num_episodes = 0
    self._model_results = {}
    self._freeze()

  @property
  def num_episodes(self) -> int:
    """How many episodes are now opted-in to the benchmark leaderboard"""
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
  def model_results(self) -> Optional[Dict[int, Optional['ModelResult']]]:
    """Per-model usage and ranking data, keyed by benchmark_model_version_id"""
    return self._model_results

  @model_results.setter
  def model_results(self, model_results: Optional[Dict[int, Optional['ModelResult']]]):
    if model_results is None:
      del self.model_results
      return
    if not isinstance(model_results, dict):
      raise TypeError('model_results must be of type dict')
    if not all([isinstance(v, ModelResult) for k, v in model_results]):
      raise TypeError('model_results must contain only items of type ModelResult')
    self._model_results = model_results


class GetAggregateEloLeaderboardRequest(KaggleObject):
  r"""
  Attributes:
    competition_ids (int)
  """

  def __init__(self):
    self._competition_ids = []
    self._freeze()

  @property
  def competition_ids(self) -> Optional[List[int]]:
    return self._competition_ids

  @competition_ids.setter
  def competition_ids(self, competition_ids: Optional[List[int]]):
    if competition_ids is None:
      del self.competition_ids
      return
    if not isinstance(competition_ids, list):
      raise TypeError('competition_ids must be of type list')
    if not all([isinstance(t, int) for t in competition_ids]):
      raise TypeError('competition_ids must contain only items of type int')
    self._competition_ids = competition_ids


class GetAggregateEloLeaderboardResponse(KaggleObject):
  r"""
  Attributes:
    model_results (ModelResult)
      Per-model unified Elo ranking data, keyed by benchmark_model_version_id
  """

  def __init__(self):
    self._model_results = {}
    self._freeze()

  @property
  def model_results(self) -> Optional[Dict[int, Optional['ModelResult']]]:
    """Per-model unified Elo ranking data, keyed by benchmark_model_version_id"""
    return self._model_results

  @model_results.setter
  def model_results(self, model_results: Optional[Dict[int, Optional['ModelResult']]]):
    if model_results is None:
      del self.model_results
      return
    if not isinstance(model_results, dict):
      raise TypeError('model_results must be of type dict')
    if not all([isinstance(v, ModelResult) for k, v in model_results]):
      raise TypeError('model_results must contain only items of type ModelResult')
    self._model_results = model_results


class GetMappedModelIdsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._competition_id = 0
    self._read_mask = None
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
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetMappedModelIdsResponse(KaggleObject):
  r"""
  Attributes:
    mapped_benchmark_model_ids (GetMappedModelIdsResponse.MappedModelInfo)
    mapped_competition_model_ids_with_submissions (GetMappedModelIdsResponse.MappedModelInfo)
      Benchmark Model Version Ids with a submission score (leaderboard eligible)
    all_mapped_competition_model_ids (GetMappedModelIdsResponse.MappedModelInfo)
      All Benchmark Model Version Ids mapped to competition
  """

  class MappedModelInfo(KaggleObject):
    r"""
    Attributes:
      slug (str)
      model_version_id (int)
    """

    def __init__(self):
      self._slug = ""
      self._model_version_id = 0
      self._freeze()

    @property
    def slug(self) -> str:
      return self._slug

    @slug.setter
    def slug(self, slug: str):
      if slug is None:
        del self.slug
        return
      if not isinstance(slug, str):
        raise TypeError('slug must be of type str')
      self._slug = slug

    @property
    def model_version_id(self) -> int:
      return self._model_version_id

    @model_version_id.setter
    def model_version_id(self, model_version_id: int):
      if model_version_id is None:
        del self.model_version_id
        return
      if not isinstance(model_version_id, int):
        raise TypeError('model_version_id must be of type int')
      self._model_version_id = model_version_id


  def __init__(self):
    self._mapped_benchmark_model_ids = []
    self._mapped_competition_model_ids_with_submissions = []
    self._all_mapped_competition_model_ids = []
    self._freeze()

  @property
  def mapped_benchmark_model_ids(self) -> Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]:
    return self._mapped_benchmark_model_ids

  @mapped_benchmark_model_ids.setter
  def mapped_benchmark_model_ids(self, mapped_benchmark_model_ids: Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]):
    if mapped_benchmark_model_ids is None:
      del self.mapped_benchmark_model_ids
      return
    if not isinstance(mapped_benchmark_model_ids, list):
      raise TypeError('mapped_benchmark_model_ids must be of type list')
    if not all([isinstance(t, GetMappedModelIdsResponse.MappedModelInfo) for t in mapped_benchmark_model_ids]):
      raise TypeError('mapped_benchmark_model_ids must contain only items of type GetMappedModelIdsResponse.MappedModelInfo')
    self._mapped_benchmark_model_ids = mapped_benchmark_model_ids

  @property
  def mapped_competition_model_ids_with_submissions(self) -> Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]:
    """Benchmark Model Version Ids with a submission score (leaderboard eligible)"""
    return self._mapped_competition_model_ids_with_submissions

  @mapped_competition_model_ids_with_submissions.setter
  def mapped_competition_model_ids_with_submissions(self, mapped_competition_model_ids_with_submissions: Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]):
    if mapped_competition_model_ids_with_submissions is None:
      del self.mapped_competition_model_ids_with_submissions
      return
    if not isinstance(mapped_competition_model_ids_with_submissions, list):
      raise TypeError('mapped_competition_model_ids_with_submissions must be of type list')
    if not all([isinstance(t, GetMappedModelIdsResponse.MappedModelInfo) for t in mapped_competition_model_ids_with_submissions]):
      raise TypeError('mapped_competition_model_ids_with_submissions must contain only items of type GetMappedModelIdsResponse.MappedModelInfo')
    self._mapped_competition_model_ids_with_submissions = mapped_competition_model_ids_with_submissions

  @property
  def all_mapped_competition_model_ids(self) -> Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]:
    """All Benchmark Model Version Ids mapped to competition"""
    return self._all_mapped_competition_model_ids

  @all_mapped_competition_model_ids.setter
  def all_mapped_competition_model_ids(self, all_mapped_competition_model_ids: Optional[List[Optional['GetMappedModelIdsResponse.MappedModelInfo']]]):
    if all_mapped_competition_model_ids is None:
      del self.all_mapped_competition_model_ids
      return
    if not isinstance(all_mapped_competition_model_ids, list):
      raise TypeError('all_mapped_competition_model_ids must be of type list')
    if not all([isinstance(t, GetMappedModelIdsResponse.MappedModelInfo) for t in all_mapped_competition_model_ids]):
      raise TypeError('all_mapped_competition_model_ids must contain only items of type GetMappedModelIdsResponse.MappedModelInfo')
    self._all_mapped_competition_model_ids = all_mapped_competition_model_ids


class MapModelsToBenchmarkRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    sync_mappings (bool)
      When set to true, will also remove model mappings in the associated
      benchmark that are not present in the competition
  """

  def __init__(self):
    self._competition_id = 0
    self._sync_mappings = False
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
  def sync_mappings(self) -> bool:
    r"""
    When set to true, will also remove model mappings in the associated
    benchmark that are not present in the competition
    """
    return self._sync_mappings

  @sync_mappings.setter
  def sync_mappings(self, sync_mappings: bool):
    if sync_mappings is None:
      del self.sync_mappings
      return
    if not isinstance(sync_mappings, bool):
      raise TypeError('sync_mappings must be of type bool')
    self._sync_mappings = sync_mappings


class MapModelsToBenchmarkResponse(KaggleObject):
  r"""
  Attributes:
    new_mappings (BenchmarkVersionModelMapping)
    mappings_added (int)
    mappings_removed (int)
  """

  def __init__(self):
    self._new_mappings = []
    self._mappings_added = 0
    self._mappings_removed = 0
    self._freeze()

  @property
  def new_mappings(self) -> Optional[List[Optional['BenchmarkVersionModelMapping']]]:
    return self._new_mappings

  @new_mappings.setter
  def new_mappings(self, new_mappings: Optional[List[Optional['BenchmarkVersionModelMapping']]]):
    if new_mappings is None:
      del self.new_mappings
      return
    if not isinstance(new_mappings, list):
      raise TypeError('new_mappings must be of type list')
    if not all([isinstance(t, BenchmarkVersionModelMapping) for t in new_mappings]):
      raise TypeError('new_mappings must contain only items of type BenchmarkVersionModelMapping')
    self._new_mappings = new_mappings

  @property
  def mappings_added(self) -> int:
    return self._mappings_added

  @mappings_added.setter
  def mappings_added(self, mappings_added: int):
    if mappings_added is None:
      del self.mappings_added
      return
    if not isinstance(mappings_added, int):
      raise TypeError('mappings_added must be of type int')
    self._mappings_added = mappings_added

  @property
  def mappings_removed(self) -> int:
    return self._mappings_removed

  @mappings_removed.setter
  def mappings_removed(self, mappings_removed: int):
    if mappings_removed is None:
      del self.mappings_removed
      return
    if not isinstance(mappings_removed, int):
      raise TypeError('mappings_removed must be of type int')
    self._mappings_removed = mappings_removed


class ModelResult(KaggleObject):
  r"""
  Attributes:
    elo (float)
      Skill rating
    margin (float)
      The +/- 95% confidence interval margin
    uneven_margin (UnevenConfidenceInterval)
    average_output_tokens_per_request (int)
      Token and cost usage
    average_total_cost_cents_per_request (float)
    num_episodes (int)
      Number of episodes this model participated in
    num_games (int)
      Number of distinct games (competitions) this model participated in
  """

  def __init__(self):
    self._elo = None
    self._margin = None
    self._uneven_margin = None
    self._average_output_tokens_per_request = None
    self._average_total_cost_cents_per_request = None
    self._num_episodes = None
    self._num_games = None
    self._freeze()

  @property
  def elo(self) -> float:
    """Skill rating"""
    return self._elo or 0.0

  @elo.setter
  def elo(self, elo: Optional[float]):
    if elo is None:
      del self.elo
      return
    if not isinstance(elo, float):
      raise TypeError('elo must be of type float')
    self._elo = elo

  @property
  def margin(self) -> float:
    """The +/- 95% confidence interval margin"""
    return self._margin or 0.0

  @margin.setter
  def margin(self, margin: float):
    if margin is None:
      del self.margin
      return
    if not isinstance(margin, float):
      raise TypeError('margin must be of type float')
    del self.uneven_margin
    self._margin = margin

  @property
  def uneven_margin(self) -> Optional['UnevenConfidenceInterval']:
    return self._uneven_margin or None

  @uneven_margin.setter
  def uneven_margin(self, uneven_margin: Optional['UnevenConfidenceInterval']):
    if uneven_margin is None:
      del self.uneven_margin
      return
    if not isinstance(uneven_margin, UnevenConfidenceInterval):
      raise TypeError('uneven_margin must be of type UnevenConfidenceInterval')
    del self.margin
    self._uneven_margin = uneven_margin

  @property
  def average_output_tokens_per_request(self) -> int:
    """Token and cost usage"""
    return self._average_output_tokens_per_request or 0

  @average_output_tokens_per_request.setter
  def average_output_tokens_per_request(self, average_output_tokens_per_request: Optional[int]):
    if average_output_tokens_per_request is None:
      del self.average_output_tokens_per_request
      return
    if not isinstance(average_output_tokens_per_request, int):
      raise TypeError('average_output_tokens_per_request must be of type int')
    self._average_output_tokens_per_request = average_output_tokens_per_request

  @property
  def average_total_cost_cents_per_request(self) -> float:
    return self._average_total_cost_cents_per_request or 0.0

  @average_total_cost_cents_per_request.setter
  def average_total_cost_cents_per_request(self, average_total_cost_cents_per_request: Optional[float]):
    if average_total_cost_cents_per_request is None:
      del self.average_total_cost_cents_per_request
      return
    if not isinstance(average_total_cost_cents_per_request, float):
      raise TypeError('average_total_cost_cents_per_request must be of type float')
    self._average_total_cost_cents_per_request = average_total_cost_cents_per_request

  @property
  def num_episodes(self) -> int:
    """Number of episodes this model participated in"""
    return self._num_episodes or 0

  @num_episodes.setter
  def num_episodes(self, num_episodes: Optional[int]):
    if num_episodes is None:
      del self.num_episodes
      return
    if not isinstance(num_episodes, int):
      raise TypeError('num_episodes must be of type int')
    self._num_episodes = num_episodes

  @property
  def num_games(self) -> int:
    """Number of distinct games (competitions) this model participated in"""
    return self._num_games or 0

  @num_games.setter
  def num_games(self, num_games: Optional[int]):
    if num_games is None:
      del self.num_games
      return
    if not isinstance(num_games, int):
      raise TypeError('num_games must be of type int')
    self._num_games = num_games


class SecondaryColumn(KaggleObject):
  r"""
  Defines a secondary column to be added to a benchmark leaderboard.

  Attributes:
    column_name (str)
      The display name for this column on the leaderboard.
    display_type (BenchmarkLeaderboardDisplayType)
      How values in this column should be displayed.
  """

  def __init__(self):
    self._column_name = ""
    self._display_type = BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def column_name(self) -> str:
    """The display name for this column on the leaderboard."""
    return self._column_name

  @column_name.setter
  def column_name(self, column_name: str):
    if column_name is None:
      del self.column_name
      return
    if not isinstance(column_name, str):
      raise TypeError('column_name must be of type str')
    self._column_name = column_name

  @property
  def display_type(self) -> 'BenchmarkLeaderboardDisplayType':
    """How values in this column should be displayed."""
    return self._display_type

  @display_type.setter
  def display_type(self, display_type: 'BenchmarkLeaderboardDisplayType'):
    if display_type is None:
      del self.display_type
      return
    if not isinstance(display_type, BenchmarkLeaderboardDisplayType):
      raise TypeError('display_type must be of type BenchmarkLeaderboardDisplayType')
    self._display_type = display_type


CreateBenchmarkFromCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secondaryColumns", "secondary_columns", "_secondary_columns", SecondaryColumn, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("mainColumnName", "main_column_name", "_main_column_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mainColumnDisplayType", "main_column_display_type", "_main_column_display_type", BenchmarkLeaderboardDisplayType, None, EnumSerializer(), optional=True),
]

ExportLeaderboardToBenchmarkRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reset", "reset", "_reset", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dryRun", "dry_run", "_dry_run", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rankingMetric", "ranking_metric", "_ranking_metric", RankingMetric, RankingMetric.RANKING_METRIC_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("excludeElo", "exclude_elo", "_exclude_elo", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("excludeCostAndTokens", "exclude_cost_and_tokens", "_exclude_cost_and_tokens", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("excludeEpisodes", "exclude_episodes", "_exclude_episodes", bool, None, PredefinedSerializer(), optional=True),
]

ExportLeaderboardToBenchmarkResponse._fields = [
  FieldMetadata("numEpisodes", "num_episodes", "_num_episodes", int, 0, PredefinedSerializer()),
  FieldMetadata("modelResults", "model_results", "_model_results", ModelResult, {}, MapSerializer(KaggleObjectSerializer())),
]

GetAggregateEloLeaderboardRequest._fields = [
  FieldMetadata("competitionIds", "competition_ids", "_competition_ids", int, [], ListSerializer(PredefinedSerializer())),
]

GetAggregateEloLeaderboardResponse._fields = [
  FieldMetadata("modelResults", "model_results", "_model_results", ModelResult, {}, MapSerializer(KaggleObjectSerializer())),
]

GetMappedModelIdsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetMappedModelIdsResponse.MappedModelInfo._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
]

GetMappedModelIdsResponse._fields = [
  FieldMetadata("mappedBenchmarkModelIds", "mapped_benchmark_model_ids", "_mapped_benchmark_model_ids", GetMappedModelIdsResponse.MappedModelInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("mappedCompetitionModelIdsWithSubmissions", "mapped_competition_model_ids_with_submissions", "_mapped_competition_model_ids_with_submissions", GetMappedModelIdsResponse.MappedModelInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("allMappedCompetitionModelIds", "all_mapped_competition_model_ids", "_all_mapped_competition_model_ids", GetMappedModelIdsResponse.MappedModelInfo, [], ListSerializer(KaggleObjectSerializer())),
]

MapModelsToBenchmarkRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("syncMappings", "sync_mappings", "_sync_mappings", bool, False, PredefinedSerializer()),
]

MapModelsToBenchmarkResponse._fields = [
  FieldMetadata("newMappings", "new_mappings", "_new_mappings", BenchmarkVersionModelMapping, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("mappingsAdded", "mappings_added", "_mappings_added", int, 0, PredefinedSerializer()),
  FieldMetadata("mappingsRemoved", "mappings_removed", "_mappings_removed", int, 0, PredefinedSerializer()),
]

ModelResult._fields = [
  FieldMetadata("elo", "elo", "_elo", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("margin", "margin", "_margin", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unevenMargin", "uneven_margin", "_uneven_margin", UnevenConfidenceInterval, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("averageOutputTokensPerRequest", "average_output_tokens_per_request", "_average_output_tokens_per_request", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("averageTotalCostCentsPerRequest", "average_total_cost_cents_per_request", "_average_total_cost_cents_per_request", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numEpisodes", "num_episodes", "_num_episodes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numGames", "num_games", "_num_games", int, None, PredefinedSerializer(), optional=True),
]

SecondaryColumn._fields = [
  FieldMetadata("columnName", "column_name", "_column_name", str, "", PredefinedSerializer()),
  FieldMetadata("displayType", "display_type", "_display_type", BenchmarkLeaderboardDisplayType, BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED, EnumSerializer()),
]

