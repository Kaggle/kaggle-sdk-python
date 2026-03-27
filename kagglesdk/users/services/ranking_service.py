from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.ranking_service import GetUserMedalCountsRequest, GetUserMedalCountsResponse, GetUserRankingHistoryRequest, GetUserRankingsCountsRequest, GetUserRankingsCountsResponse, GetUserRankingsV2Request, GetUserRankingsV2Response, UserRankingHistory

class RankingClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_user_ranking_history(self, request: GetUserRankingHistoryRequest = None) -> UserRankingHistory:
    r"""
    Returns the history of a user's ranking, including daily rank and tier
    achievements for each progression category.

    Args:
      request (GetUserRankingHistoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserRankingHistoryRequest()

    return self._client.call("users.RankingService", "GetUserRankingHistory", request, UserRankingHistory)

  def get_user_medal_counts(self, request: GetUserMedalCountsRequest = None) -> GetUserMedalCountsResponse:
    r"""
    Returns a medal achievements summary for a user.

    Args:
      request (GetUserMedalCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserMedalCountsRequest()

    return self._client.call("users.RankingService", "GetUserMedalCounts", request, GetUserMedalCountsResponse)

  def get_user_rankings_v2(self, request: GetUserRankingsV2Request = None) -> GetUserRankingsV2Response:
    r"""
    Returns the user leaderboard for the v2 rankings page. Note: This could be
    renamed to GetUserRankings when the legacy endpoint is removed.

    Args:
      request (GetUserRankingsV2Request):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserRankingsV2Request()

    return self._client.call("users.RankingService", "GetUserRankingsV2", request, GetUserRankingsV2Response)

  def get_user_rankings_counts(self, request: GetUserRankingsCountsRequest = None) -> GetUserRankingsCountsResponse:
    r"""
    Returns user counts for all progression types in v2 rankings page.

    Args:
      request (GetUserRankingsCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserRankingsCountsRequest()

    return self._client.call("users.RankingService", "GetUserRankingsCounts", request, GetUserRankingsCountsResponse)
