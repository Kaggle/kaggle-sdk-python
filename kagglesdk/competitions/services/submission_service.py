from kagglesdk.competitions.types.submission import Submission
from kagglesdk.competitions.types.submission_service import CanSubmitRequest, CanSubmitResponse, ClearLeaderboardSubmissionsRequest, ClearLeaderboardSubmissionsResponse, CreateSubmissionRequest, GetSubmissionLimitInfoRequest, GetSubmissionRequest, InvalidateSubmissionsRequest, ListSubmissionsRequest, ListSubmissionsResponse, UpdateSubmissionDescriptionRequest, UpdateSubmissionSelectionRequest, UpdateSubmissionSelectionResponse
from kagglesdk.competitions.types.team import SubmissionLimitInfo
from kagglesdk.kaggle_http_client import KaggleHttpClient

class SubmissionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def can_submit(self, request: CanSubmitRequest = None) -> CanSubmitResponse:
    r"""
    Args:
      request (CanSubmitRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CanSubmitRequest()

    return self._client.call("competitions.SubmissionService", "CanSubmit", request, CanSubmitResponse)

  def create_submission(self, request: CreateSubmissionRequest = None) -> Submission:
    r"""
    Args:
      request (CreateSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateSubmissionRequest()

    return self._client.call("competitions.SubmissionService", "CreateSubmission", request, Submission)

  def get_submission(self, request: GetSubmissionRequest = None) -> Submission:
    r"""
    Args:
      request (GetSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetSubmissionRequest()

    return self._client.call("competitions.SubmissionService", "GetSubmission", request, Submission)

  def list_submissions(self, request: ListSubmissionsRequest = None) -> ListSubmissionsResponse:
    r"""
    Args:
      request (ListSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSubmissionsRequest()

    return self._client.call("competitions.SubmissionService", "ListSubmissions", request, ListSubmissionsResponse)

  def get_submission_limit_info(self, request: GetSubmissionLimitInfoRequest = None) -> SubmissionLimitInfo:
    r"""
    Args:
      request (GetSubmissionLimitInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetSubmissionLimitInfoRequest()

    return self._client.call("competitions.SubmissionService", "GetSubmissionLimitInfo", request, SubmissionLimitInfo)

  def invalidate_submissions(self, request: InvalidateSubmissionsRequest = None):
    r"""
    Used to bulk-invalidate particular submission ids.

    Args:
      request (InvalidateSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateSubmissionsRequest()

    self._client.call("competitions.SubmissionService", "InvalidateSubmissions", request, None)

  def clear_leaderboard_submissions(self, request: ClearLeaderboardSubmissionsRequest = None) -> ClearLeaderboardSubmissionsResponse:
    r"""
    Invalidates the entire leaderboard for a specified Competition.

    Args:
      request (ClearLeaderboardSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ClearLeaderboardSubmissionsRequest()

    return self._client.call("competitions.SubmissionService", "ClearLeaderboardSubmissions", request, ClearLeaderboardSubmissionsResponse)

  def update_submission_description(self, request: UpdateSubmissionDescriptionRequest = None) -> Submission:
    r"""
    Args:
      request (UpdateSubmissionDescriptionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSubmissionDescriptionRequest()

    return self._client.call("competitions.SubmissionService", "UpdateSubmissionDescription", request, Submission)

  def update_submission_selection(self, request: UpdateSubmissionSelectionRequest = None) -> UpdateSubmissionSelectionResponse:
    r"""
    Args:
      request (UpdateSubmissionSelectionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSubmissionSelectionRequest()

    return self._client.call("competitions.SubmissionService", "UpdateSubmissionSelection", request, UpdateSubmissionSelectionResponse)
