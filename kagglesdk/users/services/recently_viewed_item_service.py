from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.recently_viewed_item_service import GetRecentlyViewedItemsRequest, GetRecentlyViewedItemsResponse

class RecentlyViewedClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_recently_viewed_items(self, request: GetRecentlyViewedItemsRequest = None) -> GetRecentlyViewedItemsResponse:
    r"""
    Args:
      request (GetRecentlyViewedItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetRecentlyViewedItemsRequest()

    return self._client.call("users.RecentlyViewedService", "GetRecentlyViewedItems", request, GetRecentlyViewedItemsResponse)
