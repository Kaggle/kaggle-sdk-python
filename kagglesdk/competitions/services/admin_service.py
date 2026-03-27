from kagglesdk.competitions.types.admin_service import InvalidateCompetitionSyntheticCopiesRequest, InvalidateCompetitionSyntheticCopiesResponse, RecreateCompetitionDatabundleArchiveRequest, RecreateCompetitionDatabundleArchiveResponse, SetCompetitionDeadlineNowRequest, SetCompetitionDeadlineNowResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AdminClient(object):
  r"""
  Competitions RPCs which only site admins can invoke. RPCs in other services
  may also be admin-only, this service is more of a catch-all for RPCs that
  don't have a more appropriate service home.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def set_competition_deadline_now(self, request: SetCompetitionDeadlineNowRequest = None) -> SetCompetitionDeadlineNowResponse:
    r"""
    Sets the competition deadline to now (ending the competition immediately).
    Requestor must be Admin.
    TODO(aip.dev/134): (-- api-linter: core::0134::synonyms=disabled --)

    Args:
      request (SetCompetitionDeadlineNowRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetCompetitionDeadlineNowRequest()

    return self._client.call("competitions.AdminService", "SetCompetitionDeadlineNow", request, SetCompetitionDeadlineNowResponse)

  def recreate_competition_databundle_archive(self, request: RecreateCompetitionDatabundleArchiveRequest = None) -> RecreateCompetitionDatabundleArchiveResponse:
    r"""
    Re-publishes the message to create the archive for the Competition's
    current databundle version

    Args:
      request (RecreateCompetitionDatabundleArchiveRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecreateCompetitionDatabundleArchiveRequest()

    return self._client.call("competitions.AdminService", "RecreateCompetitionDatabundleArchive", request, RecreateCompetitionDatabundleArchiveResponse)

  def invalidate_competition_synthetic_copies(self, request: InvalidateCompetitionSyntheticCopiesRequest = None) -> InvalidateCompetitionSyntheticCopiesResponse:
    r"""
    Invalidates all synthetic copies for a given generative template
    competition. Can be used if a change is made to the template's generator
    Notebook and we only want users to claim new copies.

    Args:
      request (InvalidateCompetitionSyntheticCopiesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateCompetitionSyntheticCopiesRequest()

    return self._client.call("competitions.AdminService", "InvalidateCompetitionSyntheticCopies", request, InvalidateCompetitionSyntheticCopiesResponse)
