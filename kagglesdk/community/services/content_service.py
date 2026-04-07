from kagglesdk.community.types.content_service import BatchDeleteItemsRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class ContentClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def batch_delete_items(self, request: BatchDeleteItemsRequest = None):
    r"""
    Deletes a batch of content owned by the current user with the given IDs

    Args:
      request (BatchDeleteItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteItemsRequest()

    self._client.call("community.ContentService", "BatchDeleteItems", request, None)
