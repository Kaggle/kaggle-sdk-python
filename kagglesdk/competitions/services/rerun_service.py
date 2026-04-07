from kagglesdk.competitions.types.rerun_service import CancelBulkRerunRequest, InitiateBulkRerunRequest, InitiateBulkRerunResponse, ListBulkRerunsRequest, ListBulkRerunsResponse, PublishBulkRerunRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class RerunClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def cancel_bulk_rerun(self, request: CancelBulkRerunRequest = None):
    r"""
    Bulk Reruns

    Args:
      request (CancelBulkRerunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CancelBulkRerunRequest()

    self._client.call("competitions.RerunService", "CancelBulkRerun", request, None)

  def initiate_bulk_rerun(self, request: InitiateBulkRerunRequest = None) -> InitiateBulkRerunResponse:
    r"""
    Args:
      request (InitiateBulkRerunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InitiateBulkRerunRequest()

    return self._client.call("competitions.RerunService", "InitiateBulkRerun", request, InitiateBulkRerunResponse)

  def list_bulk_reruns(self, request: ListBulkRerunsRequest = None) -> ListBulkRerunsResponse:
    r"""
    Args:
      request (ListBulkRerunsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBulkRerunsRequest()

    return self._client.call("competitions.RerunService", "ListBulkReruns", request, ListBulkRerunsResponse)

  def publish_bulk_rerun(self, request: PublishBulkRerunRequest = None):
    r"""
    Args:
      request (PublishBulkRerunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PublishBulkRerunRequest()

    self._client.call("competitions.RerunService", "PublishBulkRerun", request, None)
