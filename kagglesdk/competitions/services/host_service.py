from kagglesdk.competitions.types.competition_types import DatabundleBasicInfo, PrivacySettings
from kagglesdk.competitions.types.host_service import AddHostUserRequest, ClaimCompetitionSyntheticCopyRequest, ClaimCompetitionSyntheticCopyResponse, CreateCompetitionEmailInvitesRequest, CreateCompetitionEmailInvitesResponse, CreateCompetitionRequest, CreateCompetitionResponse, CreateCompetitionSampleSubmissionRequest, CreateCompetitionSolutionRequest, DeleteCompetitionEmailInviteRequest, DeleteCompetitionRequest, DeleteCompetitionResponse, DeleteSolutionFilesRequest, GetCompetitionSimulationSettingsRequest, GetDatabundleBasicInfoRequest, GetPrivacySettingsRequest, LaunchCompetitionRequest, ListCompetitionEmailInvitesRequest, ListCompetitionEmailInvitesResponse, ListCompetitionLicensesRequest, ListCompetitionLicensesResponse, ListHostUsersRequest, ListHostUsersResponse, RegenerateShareTokenRequest, RemoveHostUserRequest, SetCompetitionCitationAuthorsRequest, SetCompetitionMetricRequest, SetCompetitionMetricResponse, SetEvaluationMetricParametersRequest, ToggleBenchmarkSubmissionRequest, UpdateCompetitionSettingsRequest, UpdateCompetitionSettingsResponse, UpdateCompetitionSimulationSettingsRequest, UpdateCurrentCompetitionMetricVersionRequest, UpdateCurrentCompetitionMetricVersionResponse, UpdateImagesRequest, UpdateImagesResponse, UpdateSandboxSubmissionNameRequest, UpdateTeamsVisibilityRequest
from kagglesdk.competitions.types.simulations import CompetitionSimulationSettings
from kagglesdk.kaggle_http_client import KaggleHttpClient

class HostClient(object):
  """Contains methods related to hosting competitions."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_competition(self, request: CreateCompetitionRequest = None) -> CreateCompetitionResponse:
    r"""
    Creates a new (unlaunched) competition.
    (-- aip.dev/not-precedent: Returning Competition wrapped in a Response --)

    Args:
      request (CreateCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionRequest()

    return self._client.call("competitions.HostService", "CreateCompetition", request, CreateCompetitionResponse)

  def delete_competition(self, request: DeleteCompetitionRequest = None) -> DeleteCompetitionResponse:
    r"""
    Args:
      request (DeleteCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCompetitionRequest()

    return self._client.call("competitions.HostService", "DeleteCompetition", request, DeleteCompetitionResponse)

  def list_competition_licenses(self, request: ListCompetitionLicensesRequest = None) -> ListCompetitionLicensesResponse:
    r"""
    These RPCs support various tabs on the host wizard:

    Args:
      request (ListCompetitionLicensesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCompetitionLicensesRequest()

    return self._client.call("competitions.HostService", "ListCompetitionLicenses", request, ListCompetitionLicensesResponse)

  def get_privacy_settings(self, request: GetPrivacySettingsRequest = None) -> PrivacySettings:
    r"""
    'Privacy' tab:

    Args:
      request (GetPrivacySettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPrivacySettingsRequest()

    return self._client.call("competitions.HostService", "GetPrivacySettings", request, PrivacySettings)

  def list_competition_email_invites(self, request: ListCompetitionEmailInvitesRequest = None) -> ListCompetitionEmailInvitesResponse:
    r"""
    Args:
      request (ListCompetitionEmailInvitesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCompetitionEmailInvitesRequest()

    return self._client.call("competitions.HostService", "ListCompetitionEmailInvites", request, ListCompetitionEmailInvitesResponse)

  def delete_competition_email_invite(self, request: DeleteCompetitionEmailInviteRequest = None):
    r"""
    Args:
      request (DeleteCompetitionEmailInviteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCompetitionEmailInviteRequest()

    self._client.call("competitions.HostService", "DeleteCompetitionEmailInvite", request, None)

  def create_competition_email_invite(self, request: CreateCompetitionEmailInvitesRequest = None) -> CreateCompetitionEmailInvitesResponse:
    r"""
    TODO(aip.dev/133): (-- api-linter:
    core::0133::request-message-name=disabled --)

    Args:
      request (CreateCompetitionEmailInvitesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionEmailInvitesRequest()

    return self._client.call("competitions.HostService", "CreateCompetitionEmailInvite", request, CreateCompetitionEmailInvitesResponse)

  def create_competition_sample_submission(self, request: CreateCompetitionSampleSubmissionRequest = None):
    r"""
    Evaluation tab

    Args:
      request (CreateCompetitionSampleSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionSampleSubmissionRequest()

    self._client.call("competitions.HostService", "CreateCompetitionSampleSubmission", request, None)

  def create_competition_solution(self, request: CreateCompetitionSolutionRequest = None):
    r"""
    Args:
      request (CreateCompetitionSolutionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionSolutionRequest()

    self._client.call("competitions.HostService", "CreateCompetitionSolution", request, None)

  def toggle_benchmark_submission(self, request: ToggleBenchmarkSubmissionRequest = None):
    r"""
    Args:
      request (ToggleBenchmarkSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ToggleBenchmarkSubmissionRequest()

    self._client.call("competitions.HostService", "ToggleBenchmarkSubmission", request, None)

  def update_sandbox_submission_name(self, request: UpdateSandboxSubmissionNameRequest = None):
    r"""
    Args:
      request (UpdateSandboxSubmissionNameRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSandboxSubmissionNameRequest()

    self._client.call("competitions.HostService", "UpdateSandboxSubmissionName", request, None)

  def delete_solution_files(self, request: DeleteSolutionFilesRequest = None):
    r"""
    Args:
      request (DeleteSolutionFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteSolutionFilesRequest()

    self._client.call("competitions.HostService", "DeleteSolutionFiles", request, None)

  def regenerate_share_token(self, request: RegenerateShareTokenRequest = None) -> PrivacySettings:
    r"""
    This keeps existing UI behavior, but it could be refactored into the
    UpdatePrivacySettings RPC above with a convention like setting it to
    'regenerate' would cause it to be regenerated.

    Args:
      request (RegenerateShareTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RegenerateShareTokenRequest()

    return self._client.call("competitions.HostService", "RegenerateShareToken", request, PrivacySettings)

  def set_competition_metric(self, request: SetCompetitionMetricRequest = None) -> SetCompetitionMetricResponse:
    r"""
    TODO(aip.dev/134): (-- api-linter: core::0134::synonyms=disabled --)

    Args:
      request (SetCompetitionMetricRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetCompetitionMetricRequest()

    return self._client.call("competitions.HostService", "SetCompetitionMetric", request, SetCompetitionMetricResponse)

  def update_current_competition_metric_version(self, request: UpdateCurrentCompetitionMetricVersionRequest = None) -> UpdateCurrentCompetitionMetricVersionResponse:
    r"""
    Args:
      request (UpdateCurrentCompetitionMetricVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCurrentCompetitionMetricVersionRequest()

    return self._client.call("competitions.HostService", "UpdateCurrentCompetitionMetricVersion", request, UpdateCurrentCompetitionMetricVersionResponse)

  def claim_competition_synthetic_copy(self, request: ClaimCompetitionSyntheticCopyRequest = None) -> ClaimCompetitionSyntheticCopyResponse:
    r"""
    Allows claiming a copy of the specified base competition with unique
    synthetic data (if available)
    go/kaggle-competition-datasets-on-demand

    Args:
      request (ClaimCompetitionSyntheticCopyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ClaimCompetitionSyntheticCopyRequest()

    return self._client.call("competitions.HostService", "ClaimCompetitionSyntheticCopy", request, ClaimCompetitionSyntheticCopyResponse)

  def get_databundle_basic_info(self, request: GetDatabundleBasicInfoRequest = None) -> DatabundleBasicInfo:
    r"""
    For each file in the competition's public databundle, returns file names,
    sizes, and dimensions. Also returns total size and whether any directories
    exist.

    Args:
      request (GetDatabundleBasicInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleBasicInfoRequest()

    return self._client.call("competitions.HostService", "GetDatabundleBasicInfo", request, DatabundleBasicInfo)

  def set_competition_citation_authors(self, request: SetCompetitionCitationAuthorsRequest = None):
    r"""
    Args:
      request (SetCompetitionCitationAuthorsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetCompetitionCitationAuthorsRequest()

    self._client.call("competitions.HostService", "SetCompetitionCitationAuthors", request, None)

  def add_host_user(self, request: AddHostUserRequest = None):
    r"""
    Args:
      request (AddHostUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddHostUserRequest()

    self._client.call("competitions.HostService", "AddHostUser", request, None)

  def remove_host_user(self, request: RemoveHostUserRequest = None):
    r"""
    Args:
      request (RemoveHostUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveHostUserRequest()

    self._client.call("competitions.HostService", "RemoveHostUser", request, None)

  def list_host_users(self, request: ListHostUsersRequest = None) -> ListHostUsersResponse:
    r"""
    Args:
      request (ListHostUsersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListHostUsersRequest()

    return self._client.call("competitions.HostService", "ListHostUsers", request, ListHostUsersResponse)

  def update_images(self, request: UpdateImagesRequest = None) -> UpdateImagesResponse:
    r"""
    Updates the header and/or thumbnail images associated with the competition.

    Args:
      request (UpdateImagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateImagesRequest()

    return self._client.call("competitions.HostService", "UpdateImages", request, UpdateImagesResponse)

  def update_competition_settings(self, request: UpdateCompetitionSettingsRequest = None) -> UpdateCompetitionSettingsResponse:
    r"""
    Args:
      request (UpdateCompetitionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionSettingsRequest()

    return self._client.call("competitions.HostService", "UpdateCompetitionSettings", request, UpdateCompetitionSettingsResponse)

  def update_competition_simulation_settings(self, request: UpdateCompetitionSimulationSettingsRequest = None) -> CompetitionSimulationSettings:
    r"""
    Args:
      request (UpdateCompetitionSimulationSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionSimulationSettingsRequest()

    return self._client.call("competitions.HostService", "UpdateCompetitionSimulationSettings", request, CompetitionSimulationSettings)

  def get_competition_simulation_settings(self, request: GetCompetitionSimulationSettingsRequest = None) -> CompetitionSimulationSettings:
    r"""
    Args:
      request (GetCompetitionSimulationSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionSimulationSettingsRequest()

    return self._client.call("competitions.HostService", "GetCompetitionSimulationSettings", request, CompetitionSimulationSettings)

  def update_teams_visibility(self, request: UpdateTeamsVisibilityRequest = None):
    r"""
    Args:
      request (UpdateTeamsVisibilityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateTeamsVisibilityRequest()

    self._client.call("competitions.HostService", "UpdateTeamsVisibility", request, None)

  def launch_competition(self, request: LaunchCompetitionRequest = None):
    r"""
    Launch the competition (or set it to be launched in the future) so that it
    becomes visible to participants.

    Args:
      request (LaunchCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LaunchCompetitionRequest()

    self._client.call("competitions.HostService", "LaunchCompetition", request, None)

  def set_evaluation_metric_parameters(self, request: SetEvaluationMetricParametersRequest = None):
    r"""
    Args:
      request (SetEvaluationMetricParametersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetEvaluationMetricParametersRequest()

    self._client.call("competitions.HostService", "SetEvaluationMetricParameters", request, None)
