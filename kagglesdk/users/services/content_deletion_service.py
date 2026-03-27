from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.content_deletion_service import BatchDeleteItemsRequest

class ContentDeletionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def batch_delete_items(self, request: BatchDeleteItemsRequest = None):
    r"""
    Deletes the content matching the provided IDs

    Args:
      request (BatchDeleteItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteItemsRequest()

    self._client.call("users.ContentDeletionService", "BatchDeleteItems", request, None)
