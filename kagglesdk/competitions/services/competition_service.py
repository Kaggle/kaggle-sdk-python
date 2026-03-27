from kagglesdk.competitions.types.competition import Competition
from kagglesdk.competitions.types.competition_service import CheckCompetitionsAccessRequest, CheckCompetitionsAccessResponse, CompetitionCertificate, GetCompetitionCertificateRequest, GetCompetitionCertificateUploadUrlRequest, GetCompetitionCertificateUploadUrlResponse, GetCompetitionCitationRequest, GetCompetitionCitationResponse, GetCompetitionDatabundleVersionRequest, GetCompetitionDatabundleVersionResponse, GetCompetitionRequest, GetProfileUserStatsRequest, GetProfileUserStatsResponse, HasCompetitionEmailInviteRequest, HasCompetitionEmailInviteResponse, ListCompetitionsRequest, ListCompetitionsResponse, PromptWriteUpsRequest, PromptWriteUpsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class CompetitionClient(object):
  """Contains methods related to competitions."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_competition(self, request: GetCompetitionRequest = None, competition_id: int = None, competition_name: str = None) -> Competition:
    r"""
    Gets information about the requested competition.

    Args:
      request (GetCompetitionRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      competition_id (int)
        This corresponds to the ``competition_id`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
      competition_name (str)
        This corresponds to the ``competition_name`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([competition_id, competition_name])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = GetCompetitionRequest()
      if competition_id is not None:
        request.competition_id = competition_id
      if competition_name is not None:
        request.competition_name = competition_name

    return self._client.call("competitions.CompetitionService", "GetCompetition", request, Competition)

  def list_competitions(self, request: ListCompetitionsRequest = None) -> ListCompetitionsResponse:
    r"""
    Lists the competitions according the query and sorting parameters
    specified. Also includes information about the current user's team for each
    competition.

    Args:
      request (ListCompetitionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCompetitionsRequest()

    return self._client.call("competitions.CompetitionService", "ListCompetitions", request, ListCompetitionsResponse)

  def get_competition_databundle_version(self, request: GetCompetitionDatabundleVersionRequest = None) -> GetCompetitionDatabundleVersionResponse:
    r"""
    Args:
      request (GetCompetitionDatabundleVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionDatabundleVersionRequest()

    return self._client.call("competitions.CompetitionService", "GetCompetitionDatabundleVersion", request, GetCompetitionDatabundleVersionResponse)

  def has_competition_email_invite(self, request: HasCompetitionEmailInviteRequest = None) -> HasCompetitionEmailInviteResponse:
    r"""
    Args:
      request (HasCompetitionEmailInviteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = HasCompetitionEmailInviteRequest()

    return self._client.call("competitions.CompetitionService", "HasCompetitionEmailInvite", request, HasCompetitionEmailInviteResponse)

  def check_competitions_access(self, request: CheckCompetitionsAccessRequest = None) -> CheckCompetitionsAccessResponse:
    r"""
    Args:
      request (CheckCompetitionsAccessRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckCompetitionsAccessRequest()

    return self._client.call("competitions.CompetitionService", "CheckCompetitionsAccess", request, CheckCompetitionsAccessResponse)

  def get_profile_user_stats(self, request: GetProfileUserStatsRequest = None) -> GetProfileUserStatsResponse:
    r"""
    Returns data used to create the 'Competitions Summary' on a user profile's
    Competitions tab

    Args:
      request (GetProfileUserStatsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetProfileUserStatsRequest()

    return self._client.call("competitions.CompetitionService", "GetProfileUserStats", request, GetProfileUserStatsResponse)

  def get_competition_certificate(self, request: GetCompetitionCertificateRequest = None) -> CompetitionCertificate:
    r"""
    Args:
      request (GetCompetitionCertificateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionCertificateRequest()

    return self._client.call("competitions.CompetitionService", "GetCompetitionCertificate", request, CompetitionCertificate)

  def get_competition_citation(self, request: GetCompetitionCitationRequest = None) -> GetCompetitionCitationResponse:
    r"""
    Args:
      request (GetCompetitionCitationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionCitationRequest()

    return self._client.call("competitions.CompetitionService", "GetCompetitionCitation", request, GetCompetitionCitationResponse)

  def get_competition_certificate_upload_url(self, request: GetCompetitionCertificateUploadUrlRequest = None) -> GetCompetitionCertificateUploadUrlResponse:
    r"""
    Args:
      request (GetCompetitionCertificateUploadUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionCertificateUploadUrlRequest()

    return self._client.call("competitions.CompetitionService", "GetCompetitionCertificateUploadUrl", request, GetCompetitionCertificateUploadUrlResponse)

  def prompt_write_ups(self, request: PromptWriteUpsRequest = None) -> PromptWriteUpsResponse:
    r"""
    Admin-only hackathon API: b/362267345

    Args:
      request (PromptWriteUpsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PromptWriteUpsRequest()

    return self._client.call("competitions.CompetitionService", "PromptWriteUps", request, PromptWriteUpsResponse)
