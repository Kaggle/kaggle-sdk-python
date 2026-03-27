from kagglesdk.competitions.legacy.types.legacy_submission_service import GetMostRecentSubmissionStatusRequest, GetMostRecentSubmissionStatusResponse, ListSandboxSubmissionsRequest, ListSandboxSubmissionsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LegacySubmissionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_most_recent_submission_status(self, request: GetMostRecentSubmissionStatusRequest = None) -> GetMostRecentSubmissionStatusResponse:
    r"""
    Gets the status of the current user's most recent submission.

    Args:
      request (GetMostRecentSubmissionStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetMostRecentSubmissionStatusRequest()

    return self._client.call("competitions.legacy.LegacySubmissionService", "GetMostRecentSubmissionStatus", request, GetMostRecentSubmissionStatusResponse)

  def list_sandbox_submissions(self, request: ListSandboxSubmissionsRequest = None) -> ListSandboxSubmissionsResponse:
    r"""
    Args:
      request (ListSandboxSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSandboxSubmissionsRequest()

    return self._client.call("competitions.legacy.LegacySubmissionService", "ListSandboxSubmissions", request, ListSandboxSubmissionsResponse)
