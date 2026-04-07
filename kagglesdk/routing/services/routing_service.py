from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.routing.types.routing_service import GetPageDataByUrlRequest, GetPageDataByUrlResponse

class RoutingClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_page_data_by_url(self, request: GetPageDataByUrlRequest = None) -> GetPageDataByUrlResponse:
    r"""
    Args:
      request (GetPageDataByUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPageDataByUrlRequest()

    return self._client.call("routing.RoutingService", "GetPageDataByUrl", request, GetPageDataByUrlResponse)
