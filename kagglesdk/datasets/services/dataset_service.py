from kagglesdk.common.types.common_types import DiskUsageLimits
from kagglesdk.datasets.data_viewer.types.dataviewer_service import GetDataViewResponse
from kagglesdk.datasets.types.dataset_service import ActivityPage, AddDatasetCategoriesRequest, AddDatasetCategoriesResponse, CompetitionUploaderConfig, CreateBigQueryDatasetRequest, CreateCompetitionDataFromGcsArchiveRequest, CreateCompetitionDataRequest, CreateCompetitionDataResponse, CreateDatasetHashLinkRequest, CreateDatasetHashLinkResponse, CreateDatasetRequest, CreateDatasetVersionRequest, CreateDoiRequest, CreateDoiResponse, CreateUserDatasetViewRequest, DatabundleVersionCreationStatus, DatasetCreationResponse, DatasetHistory, DatasetList, DatasetMetadata, DatasetUploaderConfig, DeleteDatasetBySlugRequest, DeleteDatasetCategoriesRequest, DeleteDatasetCategoriesResponse, DeleteDatasetHashLinkRequest, DeleteDataViewerCacheEntryExternalRequest, DetectAggregateDuplicateRequest, DetectDuplicateRequest, DuplicationReference, EditDatasetDescriptionRequest, EditDatasetDescriptionResponse, GetCompetitionUploaderConfigRequest, GetDatabundleVersionCreationStatusRequest, GetDatasetActivityRequest, GetDatasetByUrlRequest, GetDatasetByUrlResponse, GetDatasetHistoryRequest, GetDatasetLimitsRequest, GetDatasetMetadataRequest, GetDatasetsByIdRequest, GetDatasetSuggestionsRequest, GetDatasetSuggestionsResponse, GetDatasetUploaderConfigRequest, GetDataViewExternalRequest, GetGithubRepositoryInfoRequest, GetGithubRepositoryInfoResponse, GetHuggingFaceRepositoryInfoRequest, GetHuggingFaceRepositoryInfoResponse, GetKernelOutputDatasetRequest, GetKernelOutputDataViewExternalRequest, GetLandingPageTopicsRequest, GetLandingPageTopicsResponse, GetProfileDatasetStatsRequest, GetProfileDatasetStatsResponse, GetRecentlyViewedDatasetsRequest, GetRemoteUrlFileInfoRequest, GetTopicalDatasetsRequest, GetTopicalDatasetsResponse, ReanalyzeDatabundleVersionRequest, RecreateDatasetArchiveRequest, RecreateDatasetArchiveResponse, RefreshRemoteDatasetRequest, RemoteUrlUploadFile, SearchDatasetsRequest, SearchDatasetsResponse, SoftDeleteDatasetsForOrgRequest, SoftDeleteDatasetsForUserRequest, UpdateDatasetGeneralRequest, UpdateDatasetGeneralResponse, UpdateDatasetMetadataRequest, UpdateDatasetPrivacyRequest, UpdateDatasetRequest, UpdateDatasetResponse, ValidateGcsBucketRequest, ValidateGcsBucketResponse, VoteOnDatasetRequest
from kagglesdk.datasets.types.dataset_types import DatasetUsabilityRating, KernelOutputDatasetReference
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DatasetClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_hugging_face_repository_info(self, request: GetHuggingFaceRepositoryInfoRequest = None) -> GetHuggingFaceRepositoryInfoResponse:
    r"""
    Args:
      request (GetHuggingFaceRepositoryInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHuggingFaceRepositoryInfoRequest()

    return self._client.call("datasets.DatasetService", "GetHuggingFaceRepositoryInfo", request, GetHuggingFaceRepositoryInfoResponse)

  def add_dataset_categories(self, request: AddDatasetCategoriesRequest = None) -> AddDatasetCategoriesResponse:
    r"""
    Args:
      request (AddDatasetCategoriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddDatasetCategoriesRequest()

    return self._client.call("datasets.DatasetService", "AddDatasetCategories", request, AddDatasetCategoriesResponse)

  def delete_dataset_categories(self, request: DeleteDatasetCategoriesRequest = None) -> DeleteDatasetCategoriesResponse:
    r"""
    Args:
      request (DeleteDatasetCategoriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDatasetCategoriesRequest()

    return self._client.call("datasets.DatasetService", "DeleteDatasetCategories", request, DeleteDatasetCategoriesResponse)

  def create_big_query_dataset(self, request: CreateBigQueryDatasetRequest = None) -> DatasetCreationResponse:
    r"""
    Args:
      request (CreateBigQueryDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBigQueryDatasetRequest()

    return self._client.call("datasets.DatasetService", "CreateBigQueryDataset", request, DatasetCreationResponse)

  def create_competition_data(self, request: CreateCompetitionDataRequest = None) -> CreateCompetitionDataResponse:
    r"""
    Args:
      request (CreateCompetitionDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionDataRequest()

    return self._client.call("datasets.DatasetService", "CreateCompetitionData", request, CreateCompetitionDataResponse)

  def create_competition_data_from_gcs_archive(self, request: CreateCompetitionDataFromGcsArchiveRequest = None) -> CreateCompetitionDataResponse:
    r"""
    Args:
      request (CreateCompetitionDataFromGcsArchiveRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionDataFromGcsArchiveRequest()

    return self._client.call("datasets.DatasetService", "CreateCompetitionDataFromGcsArchive", request, CreateCompetitionDataResponse)

  def create_dataset_hash_link(self, request: CreateDatasetHashLinkRequest = None) -> CreateDatasetHashLinkResponse:
    r"""
    Args:
      request (CreateDatasetHashLinkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDatasetHashLinkRequest()

    return self._client.call("datasets.DatasetService", "CreateDatasetHashLink", request, CreateDatasetHashLinkResponse)

  def create_dataset(self, request: CreateDatasetRequest = None) -> DatasetCreationResponse:
    r"""
    Args:
      request (CreateDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDatasetRequest()

    return self._client.call("datasets.DatasetService", "CreateDataset", request, DatasetCreationResponse)

  def create_dataset_version(self, request: CreateDatasetVersionRequest = None) -> DatasetCreationResponse:
    r"""
    Args:
      request (CreateDatasetVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDatasetVersionRequest()

    return self._client.call("datasets.DatasetService", "CreateDatasetVersion", request, DatasetCreationResponse)

  def create_doi(self, request: CreateDoiRequest = None) -> CreateDoiResponse:
    r"""
    Args:
      request (CreateDoiRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDoiRequest()

    return self._client.call("datasets.DatasetService", "CreateDoi", request, CreateDoiResponse)

  def create_user_dataset_view(self, request: CreateUserDatasetViewRequest = None):
    r"""
    Args:
      request (CreateUserDatasetViewRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserDatasetViewRequest()

    self._client.call("datasets.DatasetService", "CreateUserDatasetView", request, None)

  def delete_dataset_by_slug(self, request: DeleteDatasetBySlugRequest = None):
    r"""
    Args:
      request (DeleteDatasetBySlugRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDatasetBySlugRequest()

    self._client.call("datasets.DatasetService", "DeleteDatasetBySlug", request, None)

  def delete_dataset_hash_link(self, request: DeleteDatasetHashLinkRequest = None):
    r"""
    Args:
      request (DeleteDatasetHashLinkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDatasetHashLinkRequest()

    self._client.call("datasets.DatasetService", "DeleteDatasetHashLink", request, None)

  def detect_duplicate(self, request: DetectDuplicateRequest = None) -> DuplicationReference:
    r"""
    Args:
      request (DetectDuplicateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DetectDuplicateRequest()

    return self._client.call("datasets.DatasetService", "DetectDuplicate", request, DuplicationReference)

  def detect_aggregate_duplicate(self, request: DetectAggregateDuplicateRequest = None) -> DuplicationReference:
    r"""
    Args:
      request (DetectAggregateDuplicateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DetectAggregateDuplicateRequest()

    return self._client.call("datasets.DatasetService", "DetectAggregateDuplicate", request, DuplicationReference)

  def edit_dataset_description(self, request: EditDatasetDescriptionRequest = None) -> EditDatasetDescriptionResponse:
    r"""
    Args:
      request (EditDatasetDescriptionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = EditDatasetDescriptionRequest()

    return self._client.call("datasets.DatasetService", "EditDatasetDescription", request, EditDatasetDescriptionResponse)

  def get_competition_uploader_config(self, request: GetCompetitionUploaderConfigRequest = None) -> CompetitionUploaderConfig:
    r"""
    Args:
      request (GetCompetitionUploaderConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionUploaderConfigRequest()

    return self._client.call("datasets.DatasetService", "GetCompetitionUploaderConfig", request, CompetitionUploaderConfig)

  def get_databundle_version_creation_status(self, request: GetDatabundleVersionCreationStatusRequest = None) -> DatabundleVersionCreationStatus:
    r"""
    Args:
      request (GetDatabundleVersionCreationStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleVersionCreationStatusRequest()

    return self._client.call("datasets.DatasetService", "GetDatabundleVersionCreationStatus", request, DatabundleVersionCreationStatus)

  def get_dataset_activity(self, request: GetDatasetActivityRequest = None) -> ActivityPage:
    r"""
    Args:
      request (GetDatasetActivityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetActivityRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetActivity", request, ActivityPage)

  def get_dataset_by_url(self, request: GetDatasetByUrlRequest = None) -> GetDatasetByUrlResponse:
    r"""
    Args:
      request (GetDatasetByUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetByUrlRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetByUrl", request, GetDatasetByUrlResponse)

  def get_dataset_history(self, request: GetDatasetHistoryRequest = None) -> DatasetHistory:
    r"""
    Args:
      request (GetDatasetHistoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetHistoryRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetHistory", request, DatasetHistory)

  def get_dataset_limits(self, request: GetDatasetLimitsRequest = None) -> DiskUsageLimits:
    r"""
    Args:
      request (GetDatasetLimitsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetLimitsRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetLimits", request, DiskUsageLimits)

  def get_dataset_metadata(self, request: GetDatasetMetadataRequest = None) -> DatasetMetadata:
    r"""
    Args:
      request (GetDatasetMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetMetadataRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetMetadata", request, DatasetMetadata)

  def get_datasets_by_id(self, request: GetDatasetsByIdRequest = None) -> DatasetList:
    r"""
    Args:
      request (GetDatasetsByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetsByIdRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetsById", request, DatasetList)

  def get_dataset_suggestions(self, request: GetDatasetSuggestionsRequest = None) -> GetDatasetSuggestionsResponse:
    r"""
    Args:
      request (GetDatasetSuggestionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetSuggestionsRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetSuggestions", request, GetDatasetSuggestionsResponse)

  def get_dataset_uploader_config(self, request: GetDatasetUploaderConfigRequest = None) -> DatasetUploaderConfig:
    r"""
    Args:
      request (GetDatasetUploaderConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetUploaderConfigRequest()

    return self._client.call("datasets.DatasetService", "GetDatasetUploaderConfig", request, DatasetUploaderConfig)

  def get_data_view_external(self, request: GetDataViewExternalRequest = None) -> GetDataViewResponse:
    r"""
    Args:
      request (GetDataViewExternalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDataViewExternalRequest()

    return self._client.call("datasets.DatasetService", "GetDataViewExternal", request, GetDataViewResponse)

  def delete_data_viewer_cache_entry_external(self, request: DeleteDataViewerCacheEntryExternalRequest = None):
    r"""
    Args:
      request (DeleteDataViewerCacheEntryExternalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDataViewerCacheEntryExternalRequest()

    self._client.call("datasets.DatasetService", "DeleteDataViewerCacheEntryExternal", request, None)

  def get_github_repository_info(self, request: GetGithubRepositoryInfoRequest = None) -> GetGithubRepositoryInfoResponse:
    r"""
    Args:
      request (GetGithubRepositoryInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetGithubRepositoryInfoRequest()

    return self._client.call("datasets.DatasetService", "GetGithubRepositoryInfo", request, GetGithubRepositoryInfoResponse)

  def get_kernel_output_dataset(self, request: GetKernelOutputDatasetRequest = None) -> KernelOutputDatasetReference:
    r"""
    Args:
      request (GetKernelOutputDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelOutputDatasetRequest()

    return self._client.call("datasets.DatasetService", "GetKernelOutputDataset", request, KernelOutputDatasetReference)

  def get_kernel_output_data_view_external(self, request: GetKernelOutputDataViewExternalRequest = None) -> GetDataViewResponse:
    r"""
    Args:
      request (GetKernelOutputDataViewExternalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelOutputDataViewExternalRequest()

    return self._client.call("datasets.DatasetService", "GetKernelOutputDataViewExternal", request, GetDataViewResponse)

  def get_landing_page_topics(self, request: GetLandingPageTopicsRequest = None) -> GetLandingPageTopicsResponse:
    r"""
    Args:
      request (GetLandingPageTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLandingPageTopicsRequest()

    return self._client.call("datasets.DatasetService", "GetLandingPageTopics", request, GetLandingPageTopicsResponse)

  def get_recently_viewed_datasets(self, request: GetRecentlyViewedDatasetsRequest = None) -> DatasetList:
    r"""
    Args:
      request (GetRecentlyViewedDatasetsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetRecentlyViewedDatasetsRequest()

    return self._client.call("datasets.DatasetService", "GetRecentlyViewedDatasets", request, DatasetList)

  def get_remote_url_file_info(self, request: GetRemoteUrlFileInfoRequest = None) -> RemoteUrlUploadFile:
    r"""
    Args:
      request (GetRemoteUrlFileInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetRemoteUrlFileInfoRequest()

    return self._client.call("datasets.DatasetService", "GetRemoteUrlFileInfo", request, RemoteUrlUploadFile)

  def get_topical_datasets(self, request: GetTopicalDatasetsRequest = None) -> GetTopicalDatasetsResponse:
    r"""
    Args:
      request (GetTopicalDatasetsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTopicalDatasetsRequest()

    return self._client.call("datasets.DatasetService", "GetTopicalDatasets", request, GetTopicalDatasetsResponse)

  def refresh_remote_dataset(self, request: RefreshRemoteDatasetRequest = None) -> DatasetCreationResponse:
    r"""
    Args:
      request (RefreshRemoteDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RefreshRemoteDatasetRequest()

    return self._client.call("datasets.DatasetService", "RefreshRemoteDataset", request, DatasetCreationResponse)

  def search_datasets(self, request: SearchDatasetsRequest = None) -> SearchDatasetsResponse:
    r"""
    Args:
      request (SearchDatasetsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchDatasetsRequest()

    return self._client.call("datasets.DatasetService", "SearchDatasets", request, SearchDatasetsResponse)

  def soft_delete_datasets_for_org(self, request: SoftDeleteDatasetsForOrgRequest = None):
    r"""
    Args:
      request (SoftDeleteDatasetsForOrgRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SoftDeleteDatasetsForOrgRequest()

    self._client.call("datasets.DatasetService", "SoftDeleteDatasetsForOrg", request, None)

  def soft_delete_datasets_for_user(self, request: SoftDeleteDatasetsForUserRequest = None):
    r"""
    Args:
      request (SoftDeleteDatasetsForUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SoftDeleteDatasetsForUserRequest()

    self._client.call("datasets.DatasetService", "SoftDeleteDatasetsForUser", request, None)

  def update_dataset_general(self, request: UpdateDatasetGeneralRequest = None) -> UpdateDatasetGeneralResponse:
    r"""
    Args:
      request (UpdateDatasetGeneralRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetGeneralRequest()

    return self._client.call("datasets.DatasetService", "UpdateDatasetGeneral", request, UpdateDatasetGeneralResponse)

  def update_dataset_privacy(self, request: UpdateDatasetPrivacyRequest = None):
    r"""
    Args:
      request (UpdateDatasetPrivacyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetPrivacyRequest()

    self._client.call("datasets.DatasetService", "UpdateDatasetPrivacy", request, None)

  def update_dataset(self, request: UpdateDatasetRequest = None) -> UpdateDatasetResponse:
    r"""
    Args:
      request (UpdateDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetRequest()

    return self._client.call("datasets.DatasetService", "UpdateDataset", request, UpdateDatasetResponse)

  def get_profile_dataset_stats(self, request: GetProfileDatasetStatsRequest = None) -> GetProfileDatasetStatsResponse:
    r"""
    retrieve counts of the content that the user has created. This is used for
    display on the User Profile > Dataset tab

    Args:
      request (GetProfileDatasetStatsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetProfileDatasetStatsRequest()

    return self._client.call("datasets.DatasetService", "GetProfileDatasetStats", request, GetProfileDatasetStatsResponse)

  def recreate_dataset_archive(self, request: RecreateDatasetArchiveRequest = None) -> RecreateDatasetArchiveResponse:
    r"""
    Sometime the databundle zipper would fail, this give moderator/host to
    recreate the databundle zip file

    Args:
      request (RecreateDatasetArchiveRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecreateDatasetArchiveRequest()

    return self._client.call("datasets.DatasetService", "RecreateDatasetArchive", request, RecreateDatasetArchiveResponse)

  def reanalyze_databundle_version(self, request: ReanalyzeDatabundleVersionRequest = None):
    r"""
    Used to rerun the analysis of a DatabundleVersion (particularly to backfill
    any parquet data)

    Args:
      request (ReanalyzeDatabundleVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReanalyzeDatabundleVersionRequest()

    self._client.call("datasets.DatasetService", "ReanalyzeDatabundleVersion", request, None)

  def vote_on_dataset(self, request: VoteOnDatasetRequest = None):
    r"""
    Args:
      request (VoteOnDatasetRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VoteOnDatasetRequest()

    self._client.call("datasets.DatasetService", "VoteOnDataset", request, None)

  def update_dataset_metadata(self, request: UpdateDatasetMetadataRequest = None) -> DatasetUsabilityRating:
    r"""
    Args:
      request (UpdateDatasetMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetMetadataRequest()

    return self._client.call("datasets.DatasetService", "UpdateDatasetMetadata", request, DatasetUsabilityRating)

  def validate_gcs_bucket(self, request: ValidateGcsBucketRequest = None) -> ValidateGcsBucketResponse:
    r"""
    Args:
      request (ValidateGcsBucketRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ValidateGcsBucketRequest()

    return self._client.call("datasets.DatasetService", "ValidateGcsBucket", request, ValidateGcsBucketResponse)
