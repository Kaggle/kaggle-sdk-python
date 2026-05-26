from kagglesdk.competitions.types.hackathon_api_service import ApiExportHackathonWriteUpsCsvRequest, ApiExportHackathonWriteUpsCsvResponse, ApiGetHackathonOverviewRequest, ApiGetHackathonOverviewResponse, ApiGetHackathonWriteUpRequest, ApiListHackathonTracksRequest, ApiListHackathonTracksResponse, ApiListHackathonWriteUpsRequest, ApiListHackathonWriteUpsResponse
from kagglesdk.competitions.types.hackathons import HackathonWriteUp
from kagglesdk.kaggle_http_client import KaggleHttpClient

class HackathonApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_hackathon_write_up(self, request: ApiGetHackathonWriteUpRequest = None) -> HackathonWriteUp:
    r"""
    Args:
      request (ApiGetHackathonWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetHackathonWriteUpRequest()

    return self._client.call("competitions.HackathonApiService", "GetHackathonWriteUp", request, HackathonWriteUp)

  def list_hackathon_write_ups(self, request: ApiListHackathonWriteUpsRequest = None) -> ApiListHackathonWriteUpsResponse:
    r"""
    Args:
      request (ApiListHackathonWriteUpsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListHackathonWriteUpsRequest()

    return self._client.call("competitions.HackathonApiService", "ListHackathonWriteUps", request, ApiListHackathonWriteUpsResponse)

  def list_hackathon_tracks(self, request: ApiListHackathonTracksRequest = None) -> ApiListHackathonTracksResponse:
    r"""
    Args:
      request (ApiListHackathonTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListHackathonTracksRequest()

    return self._client.call("competitions.HackathonApiService", "ListHackathonTracks", request, ApiListHackathonTracksResponse)

  def export_hackathon_write_ups_csv(self, request: ApiExportHackathonWriteUpsCsvRequest = None) -> ApiExportHackathonWriteUpsCsvResponse:
    r"""
    Exports a CSV with the data from all submitted writeups after the
    hackathon has closed. Returns plain CSV text for use by AI agents via MCP.

    Args:
      request (ApiExportHackathonWriteUpsCsvRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiExportHackathonWriteUpsCsvRequest()

    return self._client.call("competitions.HackathonApiService", "ExportHackathonWriteUpsCsv", request, ApiExportHackathonWriteUpsCsvResponse)

  def get_hackathon_overview(self, request: ApiGetHackathonOverviewRequest = None) -> ApiGetHackathonOverviewResponse:
    r"""
    Args:
      request (ApiGetHackathonOverviewRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetHackathonOverviewRequest()

    return self._client.call("competitions.HackathonApiService", "GetHackathonOverview", request, ApiGetHackathonOverviewResponse)
