from kagglesdk.admin.types.codelab_service import CreateStardewItemRequest, ListStardewItemsRequest, ListStardewItemsResponse, RemoveStardewItemRequest, StardewItem
from kagglesdk.kaggle_http_client import KaggleHttpClient

class CodelabClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_stardew_items(self, request: ListStardewItemsRequest = None) -> ListStardewItemsResponse:
    r"""
    Args:
      request (ListStardewItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListStardewItemsRequest()

    return self._client.call("admin.CodelabService", "ListStardewItems", request, ListStardewItemsResponse)

  def create_stardew_item(self, request: CreateStardewItemRequest = None) -> StardewItem:
    r"""
    Args:
      request (CreateStardewItemRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateStardewItemRequest()

    return self._client.call("admin.CodelabService", "CreateStardewItem", request, StardewItem)

  def remove_stardew_item(self, request: RemoveStardewItemRequest = None) -> StardewItem:
    r"""
    Args:
      request (RemoveStardewItemRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveStardewItemRequest()

    return self._client.call("admin.CodelabService", "RemoveStardewItem", request, StardewItem)
