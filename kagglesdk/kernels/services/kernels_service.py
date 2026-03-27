from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.kernels.types.kernels_service import AcceptKernelCompetitionRulesRequest, AddKernelCategoryRequest, CancelKernelSessionRequest, CheckNewerColabVersionRequest, CheckNewerColabVersionResponse, CheckNewerGithubVersionRequest, CheckNewerGithubVersionResponse, ClearPinnedKernelSessionRequest, CommitAndRunRequest, CommitAndRunResponse, CompleteQuickSessionRequest, CompleteQuickSessionResponse, ComputeKernelDiffRequest, ComputeKernelDiffResponse, CreateKernelSessionRequest, CreateKernelSessionResponse, CreateKernelUpvoteRequest, CreateKernelUpvoteResponse, CreateKernelWithSettingsRequest, CreateKernelWithSettingsResponse, CreateUserResourceReferenceViewRequest, DefaultSessionSettings, DeleteKernelRequest, DeleteKernelUpvoteRequest, DeleteScheduledKernelSessionRequest, DeleteScheduledKernelSessionResponse, DockerImageVersionDetailsList, ExportKernelSessionForColabRequest, ExportKernelSessionForColabResponse, FetchAllColabContentRequest, FetchColabContentRequest, FetchExternalKernelContentRequest, FetchGitHubContentRequest, FetchGitHubContentResponse, GetAcceleratorQuotaStatisticsRequest, GetAcceleratorQuotaStatisticsResponse, GetColabUserInfoRequest, GetColabUserInfoResponse, GetCompetitionsPaneInfoRequest, GetCompetitionsPaneInfoResponse, GetDefaultSessionSettingsRequest, GetDeletedKernelRequest, GetDeletedKernelResponse, GetFirebaseAuthTokenRequest, GetFirebaseAuthTokenResponse, GetFirebaseConfigRequest, GetFirebaseConfigResponse, GetKernelCategoryIdsRequest, GetKernelGitHubSettingsRequest, GetKernelGitHubSettingsResponse, GetKernelIdByUrlRequest, GetKernelIdByUrlResponse, GetKernelLandingPageRequest, GetKernelLandingPageResponse, GetKernelRequest, GetKernelSessionDataSourcesRequest, GetKernelSessionDataSourcesResponse, GetKernelSessionLogRequest, GetKernelSessionModelSourcesRequest, GetKernelSessionModelSourcesResponse, GetKernelSessionResourceReferencesRequest, GetKernelSessionResourceReferencesResponse, GetKernelSessionSourceRequest, GetKernelStatusRequest, GetKernelStatusResponse, GetKernelVersionRequest, GetKernelVersionResponse, GetOrCreateKernelSessionRequest, GetOrCreateKernelSessionResponse, GetPackageRequirementsUpdateUrlRequest, GetPackageRequirementsUpdateUrlResponse, GetPackageRequirementsViewUrlRequest, GetPackageRequirementsViewUrlResponse, GetResourceReferenceByIdRequest, GetResourceReferenceRequest, GetScheduledKernelSessionRequest, GetScheduledKernelSessionResponse, GetUserKernelAchievementsRequest, GetUserKernelAchievementsResponse, HasAcceptedKernelCompetitionRulesRequest, HasAcceptedKernelCompetitionRulesResponse, Kernel, KernelCategoryIdList, KernelSessionList, KernelVersionList, ListColabFilesRequest, ListColabFilesResponse, ListDockerImagesRequest, ListGithubRepositoriesRequest, ListGithubRepositoriesResponse, ListGithubRepositoryBranchesRequest, ListGithubRepositoryBranchesResponse, ListGithubRepositoryFilesRequest, ListGithubRepositoryFilesResponse, ListKernelIdsResponse, ListKernelSessionOutputFilesHierarchicalRequest, ListKernelSessionOutputFilesHierarchicalResponse, ListKernelSessionOutputRequest, ListKernelSessionOutputResponse, ListKernelSessionsRequest, ListKernelVersionsRequest, PushToGithubRequest, PushToGithubResponse, RemoveKernelCategoryRequest, RunEpisodeRequest, RunEpisodeResponse, ScheduledKernelSession, ScheduleKernelImportsRequest, ScheduleKernelSessionRequest, SearchKernelCollaboratorsRequest, SearchKernelCollaboratorsResponse, SearchKernelIdsResponse, SyncHuggingFaceModelResourceReferenceMetadataRequest, UpdateDataSourceVersionsRequest, UpdateDataSourceVersionsResponse, UpdateDefaultSessionSettingsRequest, UpdateDependencyManagerPrivacyRequest, UpdateDockerImageVersionRequest, UpdateDockerPinningTypeRequest, UpdateKernelCategoriesRequest, UpdateKernelCategoriesResponse, UpdateKernelDraftRequest, UpdateKernelDraftResponse, UpdateKernelOutputToDatasetRequest, UpdateKernelOutputToModelRequest, UpdateKernelPersistenceRequest, UpdateKernelPersistenceResponse, UpdateKernelPrivacyRequest, UpdateKernelPrivacyResponse, UpdateKernelSessionKeepaliveRequest, UpdateKernelSessionRequest, UpdateKernelSessionResponse, UpdateKernelsPrivacyRequest, UpdateKernelTitleRequest, UpdateKernelTitleResponse, UpdateKernelVersionNameRequest, UpdateKernelViewCountRequest, UpdatePinnedKernelSessionRequest, UpdateResourceReferenceRequest, UpdateUserKernelFirestoreAuthRequest, UpdateUserKernelFirestoreAuthResponse, UploadKernelSessionOutputRequest
from kagglesdk.kernels.types.kernels_types import CreateKernelPinRequest, CreateKernelPinResponse, DeleteKernelPinRequest, DeleteKernelPinResponse, GetKernelListDetailsRequest, KernelList, ListKernelIdsRequest, ListKernelPinsRequest, ListKernelPinsResponse, ListKernelsRequest, ListResourceReferencesByIdsRequest, ListResourceReferencesRequest, ListResourceReferencesResponse, ResourceReference, ResourceReferencesList, SearchKernelIdsRequest

class KernelsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def accept_kernel_competition_rules(self, request: AcceptKernelCompetitionRulesRequest = None):
    r"""
    Args:
      request (AcceptKernelCompetitionRulesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AcceptKernelCompetitionRulesRequest()

    self._client.call("kernels.KernelsService", "AcceptKernelCompetitionRules", request, None)

  def add_kernel_category(self, request: AddKernelCategoryRequest = None):
    r"""
    Args:
      request (AddKernelCategoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddKernelCategoryRequest()

    self._client.call("kernels.KernelsService", "AddKernelCategory", request, None)

  def cancel_kernel_session(self, request: CancelKernelSessionRequest = None):
    r"""
    Args:
      request (CancelKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CancelKernelSessionRequest()

    self._client.call("kernels.KernelsService", "CancelKernelSession", request, None)

  def clear_pinned_kernel_session(self, request: ClearPinnedKernelSessionRequest = None):
    r"""
    Args:
      request (ClearPinnedKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ClearPinnedKernelSessionRequest()

    self._client.call("kernels.KernelsService", "ClearPinnedKernelSession", request, None)

  def complete_quick_session(self, request: CompleteQuickSessionRequest = None) -> CompleteQuickSessionResponse:
    r"""
    Args:
      request (CompleteQuickSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CompleteQuickSessionRequest()

    return self._client.call("kernels.KernelsService", "CompleteQuickSession", request, CompleteQuickSessionResponse)

  def compute_kernel_diff(self, request: ComputeKernelDiffRequest = None) -> ComputeKernelDiffResponse:
    r"""
    Args:
      request (ComputeKernelDiffRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ComputeKernelDiffRequest()

    return self._client.call("kernels.KernelsService", "ComputeKernelDiff", request, ComputeKernelDiffResponse)

  def create_kernel_session(self, request: CreateKernelSessionRequest = None) -> CreateKernelSessionResponse:
    r"""
    Args:
      request (CreateKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "CreateKernelSession", request, CreateKernelSessionResponse)

  def create_kernel_upvote(self, request: CreateKernelUpvoteRequest = None) -> CreateKernelUpvoteResponse:
    r"""
    Args:
      request (CreateKernelUpvoteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKernelUpvoteRequest()

    return self._client.call("kernels.KernelsService", "CreateKernelUpvote", request, CreateKernelUpvoteResponse)

  def create_kernel_with_settings(self, request: CreateKernelWithSettingsRequest = None) -> CreateKernelWithSettingsResponse:
    r"""
    Args:
      request (CreateKernelWithSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKernelWithSettingsRequest()

    return self._client.call("kernels.KernelsService", "CreateKernelWithSettings", request, CreateKernelWithSettingsResponse)

  def delete_kernel(self, request: DeleteKernelRequest = None):
    r"""
    Args:
      request (DeleteKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteKernelRequest()

    self._client.call("kernels.KernelsService", "DeleteKernel", request, None)

  def delete_kernel_upvote(self, request: DeleteKernelUpvoteRequest = None):
    r"""
    Args:
      request (DeleteKernelUpvoteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteKernelUpvoteRequest()

    self._client.call("kernels.KernelsService", "DeleteKernelUpvote", request, None)

  def fetch_colab_content(self, request: FetchColabContentRequest = None) -> FileDownload:
    r"""
    Args:
      request (FetchColabContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FetchColabContentRequest()

    return self._client.call("kernels.KernelsService", "FetchColabContent", request, FileDownload)

  def fetch_external_kernel_content(self, request: FetchExternalKernelContentRequest = None) -> FileDownload:
    r"""
    Args:
      request (FetchExternalKernelContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FetchExternalKernelContentRequest()

    return self._client.call("kernels.KernelsService", "FetchExternalKernelContent", request, FileDownload)

  def fetch_git_hub_content(self, request: FetchGitHubContentRequest = None) -> FetchGitHubContentResponse:
    r"""
    Args:
      request (FetchGitHubContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FetchGitHubContentRequest()

    return self._client.call("kernels.KernelsService", "FetchGitHubContent", request, FetchGitHubContentResponse)

  def get_accelerator_quota_statistics(self, request: GetAcceleratorQuotaStatisticsRequest = None) -> GetAcceleratorQuotaStatisticsResponse:
    r"""
    Args:
      request (GetAcceleratorQuotaStatisticsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAcceleratorQuotaStatisticsRequest()

    return self._client.call("kernels.KernelsService", "GetAcceleratorQuotaStatistics", request, GetAcceleratorQuotaStatisticsResponse)

  def get_competitions_pane_info(self, request: GetCompetitionsPaneInfoRequest = None) -> GetCompetitionsPaneInfoResponse:
    r"""
    Args:
      request (GetCompetitionsPaneInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionsPaneInfoRequest()

    return self._client.call("kernels.KernelsService", "GetCompetitionsPaneInfo", request, GetCompetitionsPaneInfoResponse)

  def get_default_session_settings(self, request: GetDefaultSessionSettingsRequest = None) -> DefaultSessionSettings:
    r"""
    Args:
      request (GetDefaultSessionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDefaultSessionSettingsRequest()

    return self._client.call("kernels.KernelsService", "GetDefaultSessionSettings", request, DefaultSessionSettings)

  def get_deleted_kernel(self, request: GetDeletedKernelRequest = None) -> GetDeletedKernelResponse:
    r"""
    Args:
      request (GetDeletedKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDeletedKernelRequest()

    return self._client.call("kernels.KernelsService", "GetDeletedKernel", request, GetDeletedKernelResponse)

  def get_firebase_auth_token(self, request: GetFirebaseAuthTokenRequest = None) -> GetFirebaseAuthTokenResponse:
    r"""
    Args:
      request (GetFirebaseAuthTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetFirebaseAuthTokenRequest()

    return self._client.call("kernels.KernelsService", "GetFirebaseAuthToken", request, GetFirebaseAuthTokenResponse)

  def get_firebase_config(self, request: GetFirebaseConfigRequest = None) -> GetFirebaseConfigResponse:
    r"""
    Args:
      request (GetFirebaseConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetFirebaseConfigRequest()

    return self._client.call("kernels.KernelsService", "GetFirebaseConfig", request, GetFirebaseConfigResponse)

  def get_kernel(self, request: GetKernelRequest = None) -> Kernel:
    r"""
    Args:
      request (GetKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelRequest()

    return self._client.call("kernels.KernelsService", "GetKernel", request, Kernel)

  def get_kernel_id_by_url(self, request: GetKernelIdByUrlRequest = None) -> GetKernelIdByUrlResponse:
    r"""
    Args:
      request (GetKernelIdByUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelIdByUrlRequest()

    return self._client.call("kernels.KernelsService", "GetKernelIdByUrl", request, GetKernelIdByUrlResponse)

  def get_kernel_category_ids(self, request: GetKernelCategoryIdsRequest = None) -> KernelCategoryIdList:
    r"""
    Args:
      request (GetKernelCategoryIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelCategoryIdsRequest()

    return self._client.call("kernels.KernelsService", "GetKernelCategoryIds", request, KernelCategoryIdList)

  def get_kernel_git_hub_settings(self, request: GetKernelGitHubSettingsRequest = None) -> GetKernelGitHubSettingsResponse:
    r"""
    Args:
      request (GetKernelGitHubSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelGitHubSettingsRequest()

    return self._client.call("kernels.KernelsService", "GetKernelGitHubSettings", request, GetKernelGitHubSettingsResponse)

  def get_kernel_landing_page(self, request: GetKernelLandingPageRequest = None) -> GetKernelLandingPageResponse:
    r"""
    Args:
      request (GetKernelLandingPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelLandingPageRequest()

    return self._client.call("kernels.KernelsService", "GetKernelLandingPage", request, GetKernelLandingPageResponse)

  def get_kernel_list_details(self, request: GetKernelListDetailsRequest = None) -> KernelList:
    r"""
    Args:
      request (GetKernelListDetailsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelListDetailsRequest()

    return self._client.call("kernels.KernelsService", "GetKernelListDetails", request, KernelList)

  def get_kernel_session_log(self, request: GetKernelSessionLogRequest = None) -> FileDownload:
    r"""
    Args:
      request (GetKernelSessionLogRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelSessionLogRequest()

    return self._client.call("kernels.KernelsService", "GetKernelSessionLog", request, FileDownload)

  def get_kernel_session_source(self, request: GetKernelSessionSourceRequest = None) -> FileDownload:
    r"""
    Args:
      request (GetKernelSessionSourceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelSessionSourceRequest()

    return self._client.call("kernels.KernelsService", "GetKernelSessionSource", request, FileDownload)

  def get_kernel_status(self, request: GetKernelStatusRequest = None) -> GetKernelStatusResponse:
    r"""
    Args:
      request (GetKernelStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelStatusRequest()

    return self._client.call("kernels.KernelsService", "GetKernelStatus", request, GetKernelStatusResponse)

  def get_kernel_version(self, request: GetKernelVersionRequest = None) -> GetKernelVersionResponse:
    r"""
    Args:
      request (GetKernelVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelVersionRequest()

    return self._client.call("kernels.KernelsService", "GetKernelVersion", request, GetKernelVersionResponse)

  def get_or_create_kernel_session(self, request: GetOrCreateKernelSessionRequest = None) -> GetOrCreateKernelSessionResponse:
    r"""
    Args:
      request (GetOrCreateKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOrCreateKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "GetOrCreateKernelSession", request, GetOrCreateKernelSessionResponse)

  def get_user_kernel_achievements(self, request: GetUserKernelAchievementsRequest = None) -> GetUserKernelAchievementsResponse:
    r"""
    Args:
      request (GetUserKernelAchievementsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserKernelAchievementsRequest()

    return self._client.call("kernels.KernelsService", "GetUserKernelAchievements", request, GetUserKernelAchievementsResponse)

  def has_accepted_kernel_competition_rules(self, request: HasAcceptedKernelCompetitionRulesRequest = None) -> HasAcceptedKernelCompetitionRulesResponse:
    r"""
    Args:
      request (HasAcceptedKernelCompetitionRulesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = HasAcceptedKernelCompetitionRulesRequest()

    return self._client.call("kernels.KernelsService", "HasAcceptedKernelCompetitionRules", request, HasAcceptedKernelCompetitionRulesResponse)

  def list_colab_files(self, request: ListColabFilesRequest = None) -> ListColabFilesResponse:
    r"""
    Args:
      request (ListColabFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListColabFilesRequest()

    return self._client.call("kernels.KernelsService", "ListColabFiles", request, ListColabFilesResponse)

  def get_colab_user_info(self, request: GetColabUserInfoRequest = None) -> GetColabUserInfoResponse:
    r"""
    Args:
      request (GetColabUserInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetColabUserInfoRequest()

    return self._client.call("kernels.KernelsService", "GetColabUserInfo", request, GetColabUserInfoResponse)

  def list_docker_images(self, request: ListDockerImagesRequest = None) -> DockerImageVersionDetailsList:
    r"""
    Args:
      request (ListDockerImagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListDockerImagesRequest()

    return self._client.call("kernels.KernelsService", "ListDockerImages", request, DockerImageVersionDetailsList)

  def list_github_repositories(self, request: ListGithubRepositoriesRequest = None) -> ListGithubRepositoriesResponse:
    r"""
    Args:
      request (ListGithubRepositoriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListGithubRepositoriesRequest()

    return self._client.call("kernels.KernelsService", "ListGithubRepositories", request, ListGithubRepositoriesResponse)

  def list_github_repository_branches(self, request: ListGithubRepositoryBranchesRequest = None) -> ListGithubRepositoryBranchesResponse:
    r"""
    Args:
      request (ListGithubRepositoryBranchesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListGithubRepositoryBranchesRequest()

    return self._client.call("kernels.KernelsService", "ListGithubRepositoryBranches", request, ListGithubRepositoryBranchesResponse)

  def list_github_repository_files(self, request: ListGithubRepositoryFilesRequest = None) -> ListGithubRepositoryFilesResponse:
    r"""
    Args:
      request (ListGithubRepositoryFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListGithubRepositoryFilesRequest()

    return self._client.call("kernels.KernelsService", "ListGithubRepositoryFiles", request, ListGithubRepositoryFilesResponse)

  def list_kernels(self, request: ListKernelsRequest = None) -> KernelList:
    r"""
    Args:
      request (ListKernelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelsRequest()

    return self._client.call("kernels.KernelsService", "ListKernels", request, KernelList)

  def list_kernel_ids(self, request: ListKernelIdsRequest = None) -> ListKernelIdsResponse:
    r"""
    Args:
      request (ListKernelIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelIdsRequest()

    return self._client.call("kernels.KernelsService", "ListKernelIds", request, ListKernelIdsResponse)

  def list_kernel_session_output(self, request: ListKernelSessionOutputRequest = None) -> ListKernelSessionOutputResponse:
    r"""
    Args:
      request (ListKernelSessionOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelSessionOutputRequest()

    return self._client.call("kernels.KernelsService", "ListKernelSessionOutput", request, ListKernelSessionOutputResponse)

  def list_kernel_sessions(self, request: ListKernelSessionsRequest = None) -> KernelSessionList:
    r"""
    Args:
      request (ListKernelSessionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelSessionsRequest()

    return self._client.call("kernels.KernelsService", "ListKernelSessions", request, KernelSessionList)

  def list_kernel_versions(self, request: ListKernelVersionsRequest = None) -> KernelVersionList:
    r"""
    Args:
      request (ListKernelVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelVersionsRequest()

    return self._client.call("kernels.KernelsService", "ListKernelVersions", request, KernelVersionList)

  def remove_kernel_category(self, request: RemoveKernelCategoryRequest = None):
    r"""
    Args:
      request (RemoveKernelCategoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveKernelCategoryRequest()

    self._client.call("kernels.KernelsService", "RemoveKernelCategory", request, None)

  def run_episode(self, request: RunEpisodeRequest = None) -> RunEpisodeResponse:
    r"""
    Args:
      request (RunEpisodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RunEpisodeRequest()

    return self._client.call("kernels.KernelsService", "RunEpisode", request, RunEpisodeResponse)

  def search_kernel_ids(self, request: SearchKernelIdsRequest = None) -> SearchKernelIdsResponse:
    r"""
    Args:
      request (SearchKernelIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchKernelIdsRequest()

    return self._client.call("kernels.KernelsService", "SearchKernelIds", request, SearchKernelIdsResponse)

  def search_kernel_collaborators(self, request: SearchKernelCollaboratorsRequest = None) -> SearchKernelCollaboratorsResponse:
    r"""
    Args:
      request (SearchKernelCollaboratorsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchKernelCollaboratorsRequest()

    return self._client.call("kernels.KernelsService", "SearchKernelCollaborators", request, SearchKernelCollaboratorsResponse)

  def update_data_source_versions(self, request: UpdateDataSourceVersionsRequest = None) -> UpdateDataSourceVersionsResponse:
    r"""
    Args:
      request (UpdateDataSourceVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDataSourceVersionsRequest()

    return self._client.call("kernels.KernelsService", "UpdateDataSourceVersions", request, UpdateDataSourceVersionsResponse)

  def update_default_session_settings(self, request: UpdateDefaultSessionSettingsRequest = None):
    r"""
    Args:
      request (UpdateDefaultSessionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDefaultSessionSettingsRequest()

    self._client.call("kernels.KernelsService", "UpdateDefaultSessionSettings", request, None)

  def update_docker_image_version(self, request: UpdateDockerImageVersionRequest = None):
    r"""
    Args:
      request (UpdateDockerImageVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDockerImageVersionRequest()

    self._client.call("kernels.KernelsService", "UpdateDockerImageVersion", request, None)

  def update_docker_pinning_type(self, request: UpdateDockerPinningTypeRequest = None):
    r"""
    Args:
      request (UpdateDockerPinningTypeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDockerPinningTypeRequest()

    self._client.call("kernels.KernelsService", "UpdateDockerPinningType", request, None)

  def update_kernel_categories(self, request: UpdateKernelCategoriesRequest = None) -> UpdateKernelCategoriesResponse:
    r"""
    Args:
      request (UpdateKernelCategoriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelCategoriesRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelCategories", request, UpdateKernelCategoriesResponse)

  def update_kernel_privacy(self, request: UpdateKernelPrivacyRequest = None) -> UpdateKernelPrivacyResponse:
    r"""
    Args:
      request (UpdateKernelPrivacyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelPrivacyRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelPrivacy", request, UpdateKernelPrivacyResponse)

  def update_kernel_session(self, request: UpdateKernelSessionRequest = None) -> UpdateKernelSessionResponse:
    r"""
    Args:
      request (UpdateKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelSession", request, UpdateKernelSessionResponse)

  def update_kernel_session_keepalive(self, request: UpdateKernelSessionKeepaliveRequest = None):
    r"""
    Args:
      request (UpdateKernelSessionKeepaliveRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelSessionKeepaliveRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelSessionKeepalive", request, None)

  def update_kernel_title(self, request: UpdateKernelTitleRequest = None) -> UpdateKernelTitleResponse:
    r"""
    Args:
      request (UpdateKernelTitleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelTitleRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelTitle", request, UpdateKernelTitleResponse)

  def update_kernel_persistence(self, request: UpdateKernelPersistenceRequest = None) -> UpdateKernelPersistenceResponse:
    r"""
    Args:
      request (UpdateKernelPersistenceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelPersistenceRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelPersistence", request, UpdateKernelPersistenceResponse)

  def update_kernel_version_name(self, request: UpdateKernelVersionNameRequest = None):
    r"""
    Args:
      request (UpdateKernelVersionNameRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelVersionNameRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelVersionName", request, None)

  def update_kernel_output_to_dataset(self, request: UpdateKernelOutputToDatasetRequest = None):
    r"""
    Args:
      request (UpdateKernelOutputToDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelOutputToDatasetRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelOutputToDataset", request, None)

  def update_kernel_output_to_model(self, request: UpdateKernelOutputToModelRequest = None):
    r"""
    Args:
      request (UpdateKernelOutputToModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelOutputToModelRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelOutputToModel", request, None)

  def update_kernels_privacy(self, request: UpdateKernelsPrivacyRequest = None):
    r"""
    This handler currently only allows admins to make a set of kernels private.
    In the future, it could be extended to allow users to make their own
    kernels public.

    Args:
      request (UpdateKernelsPrivacyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelsPrivacyRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelsPrivacy", request, None)

  def update_pinned_kernel_session(self, request: UpdatePinnedKernelSessionRequest = None):
    r"""
    Args:
      request (UpdatePinnedKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdatePinnedKernelSessionRequest()

    self._client.call("kernels.KernelsService", "UpdatePinnedKernelSession", request, None)

  def update_user_kernel_firestore_auth(self, request: UpdateUserKernelFirestoreAuthRequest = None) -> UpdateUserKernelFirestoreAuthResponse:
    r"""
    Args:
      request (UpdateUserKernelFirestoreAuthRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserKernelFirestoreAuthRequest()

    return self._client.call("kernels.KernelsService", "UpdateUserKernelFirestoreAuth", request, UpdateUserKernelFirestoreAuthResponse)

  def upload_kernel_session_output(self, request: UploadKernelSessionOutputRequest = None):
    r"""
    Args:
      request (UploadKernelSessionOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UploadKernelSessionOutputRequest()

    self._client.call("kernels.KernelsService", "UploadKernelSessionOutput", request, None)

  def update_kernel_view_count(self, request: UpdateKernelViewCountRequest = None):
    r"""
    Args:
      request (UpdateKernelViewCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelViewCountRequest()

    self._client.call("kernels.KernelsService", "UpdateKernelViewCount", request, None)

  def schedule_kernel_session(self, request: ScheduleKernelSessionRequest = None) -> ScheduledKernelSession:
    r"""
    Args:
      request (ScheduleKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ScheduleKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "ScheduleKernelSession", request, ScheduledKernelSession)

  def get_scheduled_kernel_session(self, request: GetScheduledKernelSessionRequest = None) -> GetScheduledKernelSessionResponse:
    r"""
    Args:
      request (GetScheduledKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetScheduledKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "GetScheduledKernelSession", request, GetScheduledKernelSessionResponse)

  def delete_scheduled_kernel_session(self, request: DeleteScheduledKernelSessionRequest = None) -> DeleteScheduledKernelSessionResponse:
    r"""
    Args:
      request (DeleteScheduledKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteScheduledKernelSessionRequest()

    return self._client.call("kernels.KernelsService", "DeleteScheduledKernelSession", request, DeleteScheduledKernelSessionResponse)

  def get_kernel_session_data_sources(self, request: GetKernelSessionDataSourcesRequest = None) -> GetKernelSessionDataSourcesResponse:
    r"""
    Args:
      request (GetKernelSessionDataSourcesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelSessionDataSourcesRequest()

    return self._client.call("kernels.KernelsService", "GetKernelSessionDataSources", request, GetKernelSessionDataSourcesResponse)

  def get_kernel_session_model_sources(self, request: GetKernelSessionModelSourcesRequest = None) -> GetKernelSessionModelSourcesResponse:
    r"""
    Args:
      request (GetKernelSessionModelSourcesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelSessionModelSourcesRequest()

    return self._client.call("kernels.KernelsService", "GetKernelSessionModelSources", request, GetKernelSessionModelSourcesResponse)

  def get_kernel_session_resource_references(self, request: GetKernelSessionResourceReferencesRequest = None) -> GetKernelSessionResourceReferencesResponse:
    r"""
    Args:
      request (GetKernelSessionResourceReferencesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelSessionResourceReferencesRequest()

    return self._client.call("kernels.KernelsService", "GetKernelSessionResourceReferences", request, GetKernelSessionResourceReferencesResponse)

  def list_kernel_session_output_files_hierarchical(self, request: ListKernelSessionOutputFilesHierarchicalRequest = None) -> ListKernelSessionOutputFilesHierarchicalResponse:
    r"""
    Args:
      request (ListKernelSessionOutputFilesHierarchicalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelSessionOutputFilesHierarchicalRequest()

    return self._client.call("kernels.KernelsService", "ListKernelSessionOutputFilesHierarchical", request, ListKernelSessionOutputFilesHierarchicalResponse)

  def update_kernel_draft(self, request: UpdateKernelDraftRequest = None) -> UpdateKernelDraftResponse:
    r"""
    Args:
      request (UpdateKernelDraftRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateKernelDraftRequest()

    return self._client.call("kernels.KernelsService", "UpdateKernelDraft", request, UpdateKernelDraftResponse)

  def commit_and_run(self, request: CommitAndRunRequest = None) -> CommitAndRunResponse:
    r"""
    Args:
      request (CommitAndRunRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CommitAndRunRequest()

    return self._client.call("kernels.KernelsService", "CommitAndRun", request, CommitAndRunResponse)

  def create_kernel_pin(self, request: CreateKernelPinRequest = None) -> CreateKernelPinResponse:
    r"""
    Args:
      request (CreateKernelPinRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKernelPinRequest()

    return self._client.call("kernels.KernelsService", "CreateKernelPin", request, CreateKernelPinResponse)

  def delete_kernel_pin(self, request: DeleteKernelPinRequest = None) -> DeleteKernelPinResponse:
    r"""
    Args:
      request (DeleteKernelPinRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteKernelPinRequest()

    return self._client.call("kernels.KernelsService", "DeleteKernelPin", request, DeleteKernelPinResponse)

  def list_kernel_pins(self, request: ListKernelPinsRequest = None) -> ListKernelPinsResponse:
    r"""
    Args:
      request (ListKernelPinsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelPinsRequest()

    return self._client.call("kernels.KernelsService", "ListKernelPins", request, ListKernelPinsResponse)

  def export_kernel_session_for_colab(self, request: ExportKernelSessionForColabRequest = None) -> ExportKernelSessionForColabResponse:
    r"""
    Args:
      request (ExportKernelSessionForColabRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExportKernelSessionForColabRequest()

    return self._client.call("kernels.KernelsService", "ExportKernelSessionForColab", request, ExportKernelSessionForColabResponse)

  def push_to_github(self, request: PushToGithubRequest = None) -> PushToGithubResponse:
    r"""
    Args:
      request (PushToGithubRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PushToGithubRequest()

    return self._client.call("kernels.KernelsService", "PushToGithub", request, PushToGithubResponse)

  def check_newer_github_version(self, request: CheckNewerGithubVersionRequest = None) -> CheckNewerGithubVersionResponse:
    r"""
    Args:
      request (CheckNewerGithubVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckNewerGithubVersionRequest()

    return self._client.call("kernels.KernelsService", "CheckNewerGithubVersion", request, CheckNewerGithubVersionResponse)

  def get_package_requirements_update_url(self, request: GetPackageRequirementsUpdateUrlRequest = None) -> GetPackageRequirementsUpdateUrlResponse:
    r"""
    Args:
      request (GetPackageRequirementsUpdateUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPackageRequirementsUpdateUrlRequest()

    return self._client.call("kernels.KernelsService", "GetPackageRequirementsUpdateUrl", request, GetPackageRequirementsUpdateUrlResponse)

  def get_package_requirements_view_url(self, request: GetPackageRequirementsViewUrlRequest = None) -> GetPackageRequirementsViewUrlResponse:
    r"""
    Args:
      request (GetPackageRequirementsViewUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPackageRequirementsViewUrlRequest()

    return self._client.call("kernels.KernelsService", "GetPackageRequirementsViewUrl", request, GetPackageRequirementsViewUrlResponse)

  def schedule_kernel_imports(self, request: ScheduleKernelImportsRequest = None):
    r"""
    Args:
      request (ScheduleKernelImportsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ScheduleKernelImportsRequest()

    self._client.call("kernels.KernelsService", "ScheduleKernelImports", request, None)

  def fetch_all_colab_content(self, request: FetchAllColabContentRequest = None):
    r"""
    Args:
      request (FetchAllColabContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FetchAllColabContentRequest()

    self._client.call("kernels.KernelsService", "FetchAllColabContent", request, None)

  def check_newer_colab_version(self, request: CheckNewerColabVersionRequest = None) -> CheckNewerColabVersionResponse:
    r"""
    Args:
      request (CheckNewerColabVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckNewerColabVersionRequest()

    return self._client.call("kernels.KernelsService", "CheckNewerColabVersion", request, CheckNewerColabVersionResponse)

  def update_dependency_manager_privacy(self, request: UpdateDependencyManagerPrivacyRequest = None):
    r"""
    Args:
      request (UpdateDependencyManagerPrivacyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDependencyManagerPrivacyRequest()

    self._client.call("kernels.KernelsService", "UpdateDependencyManagerPrivacy", request, None)

  def sync_hugging_face_model_resource_reference_metadata(self, request: SyncHuggingFaceModelResourceReferenceMetadataRequest = None) -> ResourceReference:
    r"""
    Args:
      request (SyncHuggingFaceModelResourceReferenceMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SyncHuggingFaceModelResourceReferenceMetadataRequest()

    return self._client.call("kernels.KernelsService", "SyncHuggingFaceModelResourceReferenceMetadata", request, ResourceReference)

  def get_resource_reference(self, request: GetResourceReferenceRequest = None) -> ResourceReference:
    r"""
    Args:
      request (GetResourceReferenceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetResourceReferenceRequest()

    return self._client.call("kernels.KernelsService", "GetResourceReference", request, ResourceReference)

  def get_resource_reference_by_id(self, request: GetResourceReferenceByIdRequest = None) -> ResourceReference:
    r"""
    Args:
      request (GetResourceReferenceByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetResourceReferenceByIdRequest()

    return self._client.call("kernels.KernelsService", "GetResourceReferenceById", request, ResourceReference)

  def create_user_resource_reference_view(self, request: CreateUserResourceReferenceViewRequest = None):
    r"""
    Args:
      request (CreateUserResourceReferenceViewRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserResourceReferenceViewRequest()

    self._client.call("kernels.KernelsService", "CreateUserResourceReferenceView", request, None)

  def update_resource_reference(self, request: UpdateResourceReferenceRequest = None) -> ResourceReference:
    r"""
    Args:
      request (UpdateResourceReferenceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateResourceReferenceRequest()

    return self._client.call("kernels.KernelsService", "UpdateResourceReference", request, ResourceReference)

  def list_resource_references(self, request: ListResourceReferencesRequest = None) -> ListResourceReferencesResponse:
    r"""
    Args:
      request (ListResourceReferencesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListResourceReferencesRequest()

    return self._client.call("kernels.KernelsService", "ListResourceReferences", request, ListResourceReferencesResponse)

  def list_resource_references_by_ids(self, request: ListResourceReferencesByIdsRequest = None) -> ResourceReferencesList:
    r"""
    Args:
      request (ListResourceReferencesByIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListResourceReferencesByIdsRequest()

    return self._client.call("kernels.KernelsService", "ListResourceReferencesByIds", request, ResourceReferencesList)
