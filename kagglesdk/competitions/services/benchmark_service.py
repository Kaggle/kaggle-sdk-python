from kagglesdk.benchmarks.types.benchmark_types import Benchmark
from kagglesdk.competitions.types.benchmark_service import CreateBenchmarkFromCompetitionRequest, ExportLeaderboardToBenchmarkRequest, ExportLeaderboardToBenchmarkResponse, GetAggregateEloLeaderboardRequest, GetAggregateEloLeaderboardResponse, GetMappedModelIdsRequest, GetMappedModelIdsResponse, MapModelsToBenchmarkRequest, MapModelsToBenchmarkResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkClient(object):
  """Competitions RPCs which manage a Competition's relationship with a Benchmark."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_benchmark_from_competition(self, request: CreateBenchmarkFromCompetitionRequest = None) -> Benchmark:
    r"""
    Converts a simulation competition into a benchmark with the basic
    settings pre-defined.

    Args:
      request (CreateBenchmarkFromCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkFromCompetitionRequest()

    return self._client.call("competitions.BenchmarkService", "CreateBenchmarkFromCompetition", request, Benchmark)

  def map_models_to_benchmark(self, request: MapModelsToBenchmarkRequest = None) -> MapModelsToBenchmarkResponse:
    r"""
    Args:
      request (MapModelsToBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MapModelsToBenchmarkRequest()

    return self._client.call("competitions.BenchmarkService", "MapModelsToBenchmark", request, MapModelsToBenchmarkResponse)

  def get_mapped_model_ids(self, request: GetMappedModelIdsRequest = None) -> GetMappedModelIdsResponse:
    r"""
    Args:
      request (GetMappedModelIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetMappedModelIdsRequest()

    return self._client.call("competitions.BenchmarkService", "GetMappedModelIds", request, GetMappedModelIdsResponse)

  def export_leaderboard_to_benchmark(self, request: ExportLeaderboardToBenchmarkRequest = None) -> ExportLeaderboardToBenchmarkResponse:
    r"""
    Supports a 'one-click checkout' to convert
    a simulation competition to a benchmark leaderboard.
    Given the current competition state, determines which episodes to include
    and gets model rankings + usage details.

    Args:
      request (ExportLeaderboardToBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExportLeaderboardToBenchmarkRequest()

    return self._client.call("competitions.BenchmarkService", "ExportLeaderboardToBenchmark", request, ExportLeaderboardToBenchmarkResponse)

  def get_aggregate_elo_leaderboard(self, request: GetAggregateEloLeaderboardRequest = None) -> GetAggregateEloLeaderboardResponse:
    r"""
    Computes a unified Elo leaderboard across multiple simulation competitions
    using game-balanced Bradley-Terry aggregation.

    Args:
      request (GetAggregateEloLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAggregateEloLeaderboardRequest()

    return self._client.call("competitions.BenchmarkService", "GetAggregateEloLeaderboard", request, GetAggregateEloLeaderboardResponse)
