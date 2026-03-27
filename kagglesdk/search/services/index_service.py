from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.search.types.index_service import BatchForceIndexDocumentsRequest

class IndexClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def batch_force_index_documents(self, request: BatchForceIndexDocumentsRequest = None):
    r"""
    Trigger a reindex for a series of documents of a single type (admin/api
    friendly route)

    Args:
      request (BatchForceIndexDocumentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchForceIndexDocumentsRequest()

    self._client.call("search.IndexService", "BatchForceIndexDocuments", request, None)
