from kagglesdk.competitions.legacy.types.legacy_competition_service import GetCompetitionDatabundleVersionsRequest, GetCompetitionDatabundleVersionsResponse, LegacyListTeamsRequest, LegacyListTeamsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LegacyCompetitionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_competition_databundle_versions(self, request: GetCompetitionDatabundleVersionsRequest = None) -> GetCompetitionDatabundleVersionsResponse:
    r"""
    Args:
      request (GetCompetitionDatabundleVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionDatabundleVersionsRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionService", "GetCompetitionDatabundleVersions", request, GetCompetitionDatabundleVersionsResponse)

  def list_teams(self, request: LegacyListTeamsRequest = None) -> LegacyListTeamsResponse:
    r"""
    Args:
      request (LegacyListTeamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyListTeamsRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionService", "ListTeams", request, LegacyListTeamsResponse)
