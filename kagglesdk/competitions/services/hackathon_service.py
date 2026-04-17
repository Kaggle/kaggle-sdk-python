from kagglesdk.competitions.types.hackathon_service import ListHackathonTracksRequest, ListHackathonTracksResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class HackathonClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_hackathon_tracks(self, request: ListHackathonTracksRequest = None) -> ListHackathonTracksResponse:
    r"""
    Args:
      request (ListHackathonTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListHackathonTracksRequest()

    return self._client.call("competitions.HackathonService", "ListHackathonTracks", request, ListHackathonTracksResponse)
