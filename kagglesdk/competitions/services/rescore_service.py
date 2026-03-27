from kagglesdk.competitions.types.rescore_service import CancelBulkRescoreRequest, CancelBulkRescoreResponse, InitiateBulkRescoreRequest, InitiateBulkRescoreResponse, ListBulkRescoresRequest, ListBulkRescoresResponse, RescoreSubmissionRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class RescoreClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def initiate_bulk_rescore(self, request: InitiateBulkRescoreRequest = None) -> InitiateBulkRescoreResponse:
    r"""
    Args:
      request (InitiateBulkRescoreRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InitiateBulkRescoreRequest()

    return self._client.call("competitions.RescoreService", "InitiateBulkRescore", request, InitiateBulkRescoreResponse)

  def list_bulk_rescores(self, request: ListBulkRescoresRequest = None) -> ListBulkRescoresResponse:
    r"""
    Args:
      request (ListBulkRescoresRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBulkRescoresRequest()

    return self._client.call("competitions.RescoreService", "ListBulkRescores", request, ListBulkRescoresResponse)

  def cancel_bulk_rescore(self, request: CancelBulkRescoreRequest = None) -> CancelBulkRescoreResponse:
    r"""
    Args:
      request (CancelBulkRescoreRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CancelBulkRescoreRequest()

    return self._client.call("competitions.RescoreService", "CancelBulkRescore", request, CancelBulkRescoreResponse)

  def rescore_submission(self, request: RescoreSubmissionRequest = None):
    r"""
    Endpoint for synchronous, one-off Rescores of a single Submission
    Visible to competition hosts, admins (ignoring field permissions), and
    system accounts (ignoring field permissions)

    Args:
      request (RescoreSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RescoreSubmissionRequest()

    self._client.call("competitions.RescoreService", "RescoreSubmission", request, None)
