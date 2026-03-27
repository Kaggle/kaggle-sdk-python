from kagglesdk.competitions.types.leaderboard_service import GetLeaderboardRequest, GetLeaderboardResponse, GetRanksForUsersRequest, GetRanksForUsersResponse, LegacyRecalculateLeaderboardRequest, LegacyRecalculateLeaderboardResponse, RecalculateLeaderboardRequest, RecalculateLeaderboardResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LeaderboardClient(object):
  """Contains methods related to competition leaderboards."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_leaderboard(self, request: GetLeaderboardRequest = None) -> GetLeaderboardResponse:
    r"""
    Gets the leaderboard for the specified competition.

    Args:
      request (GetLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLeaderboardRequest()

    return self._client.call("competitions.LeaderboardService", "GetLeaderboard", request, GetLeaderboardResponse)

  def get_ranks_for_users(self, request: GetRanksForUsersRequest = None) -> GetRanksForUsersResponse:
    r"""
    Given a Competition and set of UserIds, returns each User's Team's Rank.
    Uses the current main Leaderboard:  Public LB if comp is in Weak LB mode
    (~= comp is ongoing), Private LB if comp is in Strong LB mode (and comp
    has Private LB).  See LeaderboardMode enum below.

    Args:
      request (GetRanksForUsersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetRanksForUsersRequest()

    return self._client.call("competitions.LeaderboardService", "GetRanksForUsers", request, GetRanksForUsersResponse)

  def recalculate_leaderboard(self, request: RecalculateLeaderboardRequest = None) -> RecalculateLeaderboardResponse:
    r"""
    Admin-only RPC which recalculates cached LB data stored on Teams rows.
    Can either recalculate only Weak LB fields, or both Weak and Strong.
    NOTE: This is the only way for the Strong LB fields, such as Ranks, to be
    written.
    It is not intended for frequent usage; the Weak LB should be kept up-to-
    date synchronously as the competition progresses.

    Args:
      request (RecalculateLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecalculateLeaderboardRequest()

    return self._client.call("competitions.LeaderboardService", "RecalculateLeaderboard", request, RecalculateLeaderboardResponse)

  def legacy_recalculate_leaderboard(self, request: LegacyRecalculateLeaderboardRequest = None) -> LegacyRecalculateLeaderboardResponse:
    r"""
    Admin-only RPC that uses the legacy recalculate version of the above RPC.
    NOTE: This RPC should be removed once the newer one is fully live.

    Args:
      request (LegacyRecalculateLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyRecalculateLeaderboardRequest()

    return self._client.call("competitions.LeaderboardService", "LegacyRecalculateLeaderboard", request, LegacyRecalculateLeaderboardResponse)
