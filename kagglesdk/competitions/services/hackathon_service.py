from kagglesdk.competitions.types.hackathon_service import ExportEnrichedHackathonWriteUpsCsvRequest, ExportEnrichedHackathonWriteUpsCsvResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class HackathonClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def export_enriched_hackathon_write_ups_csv(self, request: ExportEnrichedHackathonWriteUpsCsvRequest = None) -> ExportEnrichedHackathonWriteUpsCsvResponse:
    r"""
    Args:
      request (ExportEnrichedHackathonWriteUpsCsvRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExportEnrichedHackathonWriteUpsCsvRequest()

    return self._client.call("competitions.HackathonService", "ExportEnrichedHackathonWriteUpsCsv", request, ExportEnrichedHackathonWriteUpsCsvResponse)
