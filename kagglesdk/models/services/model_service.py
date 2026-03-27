from kagglesdk.common.types.common_types import DiskUsageLimits
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_service import AddModelTagRequest, CopyModelInstanceVersionRequest, CreateGatingAgreementRequest, CreateGatingUserConsentRequest, CreateModelDoiRequest, CreateModelDoiResponse, CreateModelInstanceRequest, CreateModelInstanceVersionRequest, CreateModelRequest, DeleteModelInstanceRequest, DeleteModelInstanceResponse, DeleteModelInstanceVersionRequest, DeleteModelInstanceVersionResponse, DeleteModelRequest, DeleteModelResponse, GetDeletedModelRequest, GetDeletedModelResponse, GetGatingUserConsentsRequest, GetGatingUserConsentsResponse, GetKernelOutputModelInstanceRequest, GetModelByIdRequest, GetModelGatingRequest, GetModelInstanceHistoryRequest, GetModelInstanceHistoryResponse, GetModelInstanceRequest, GetModelInstanceUploaderConfigRequest, GetModelInstanceVersionKernelUsageRequest, GetModelInstanceVersionKernelUsageResponse, GetModelLimitsRequest, GetModelRequest, GetUserGatingConsentDataRequest, GetUserGatingConsentDataResponse, GetUserModelCountsRequest, GetUserModelCountsResponse, IncrementModelViewCountRequest, ListCompetitionModelInstancesRequest, ListCompetitionModelInstancesResponse, ListModelCompetitionsRequest, ListModelCompetitionsResponse, ListModelInstancesByIdsRequest, ListModelInstancesRequest, ListModelInstancesResponse, ListModelInstanceVersionsRequest, ListModelLicenseGroupsRequest, ListModelLicenseGroupsResponse, ListModelsRequest, ListModelsResponse, ListOwnersRequest, ListOwnersResponse, ListSampleTasksRequest, ListSampleTasksResponse, ModelUploaderConfig, PinModelInstanceToCompetitionRequest, PreviewGatingAgreementContentRequest, RefreshRemoteModelInstanceRequest, RemoveModelTagRequest, ReviewGatingUserConsentRequest, UnpinModelInstanceFromCompetitionRequest, UpdateModelGatingRequest, UpdateModelInstanceRequest, UpdateModelOwnerRequest, UpdateModelOwnerResponse, UpdateModelRequest, VoteOnModelRequest
from kagglesdk.models.types.model_types import GatingAgreement, GatingAgreementContent, GatingUserConsent, KernelOutputModelInstanceReference, Model, ModelGating, ModelInstance, ModelInstanceVersionList

class ModelClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_model(self, request: CreateModelRequest = None) -> Model:
    r"""
    Args:
      request (CreateModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateModelRequest()

    return self._client.call("models.ModelService", "CreateModel", request, Model)

  def update_model(self, request: UpdateModelRequest = None) -> Model:
    r"""
    Args:
      request (UpdateModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateModelRequest()

    return self._client.call("models.ModelService", "UpdateModel", request, Model)

  def get_model(self, request: GetModelRequest = None) -> Model:
    r"""
    Args:
      request (GetModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelRequest()

    return self._client.call("models.ModelService", "GetModel", request, Model)

  def get_model_by_id(self, request: GetModelByIdRequest = None) -> Model:
    r"""
    Args:
      request (GetModelByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelByIdRequest()

    return self._client.call("models.ModelService", "GetModelById", request, Model)

  def get_deleted_model(self, request: GetDeletedModelRequest = None) -> GetDeletedModelResponse:
    r"""
    Args:
      request (GetDeletedModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDeletedModelRequest()

    return self._client.call("models.ModelService", "GetDeletedModel", request, GetDeletedModelResponse)

  def delete_model(self, request: DeleteModelRequest = None) -> DeleteModelResponse:
    r"""
    Args:
      request (DeleteModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteModelRequest()

    return self._client.call("models.ModelService", "DeleteModel", request, DeleteModelResponse)

  def list_model_instances_by_ids(self, request: ListModelInstancesByIdsRequest = None) -> ListModelInstancesResponse:
    r"""
    Args:
      request (ListModelInstancesByIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelInstancesByIdsRequest()

    return self._client.call("models.ModelService", "ListModelInstancesByIds", request, ListModelInstancesResponse)

  def list_model_instances(self, request: ListModelInstancesRequest = None) -> ListModelInstancesResponse:
    r"""
    Args:
      request (ListModelInstancesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelInstancesRequest()

    return self._client.call("models.ModelService", "ListModelInstances", request, ListModelInstancesResponse)

  def list_model_instance_versions(self, request: ListModelInstanceVersionsRequest = None) -> ModelInstanceVersionList:
    r"""
    Args:
      request (ListModelInstanceVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelInstanceVersionsRequest()

    return self._client.call("models.ModelService", "ListModelInstanceVersions", request, ModelInstanceVersionList)

  def get_model_instance(self, request: GetModelInstanceRequest = None) -> ModelInstance:
    r"""
    Args:
      request (GetModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelInstanceRequest()

    return self._client.call("models.ModelService", "GetModelInstance", request, ModelInstance)

  def get_model_instance_version_kernel_usage(self, request: GetModelInstanceVersionKernelUsageRequest = None) -> GetModelInstanceVersionKernelUsageResponse:
    r"""
    Args:
      request (GetModelInstanceVersionKernelUsageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelInstanceVersionKernelUsageRequest()

    return self._client.call("models.ModelService", "GetModelInstanceVersionKernelUsage", request, GetModelInstanceVersionKernelUsageResponse)

  def vote_on_model(self, request: VoteOnModelRequest = None):
    r"""
    Args:
      request (VoteOnModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VoteOnModelRequest()

    self._client.call("models.ModelService", "VoteOnModel", request, None)

  def list_models(self, request: ListModelsRequest = None) -> ListModelsResponse:
    r"""
    Args:
      request (ListModelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelsRequest()

    return self._client.call("models.ModelService", "ListModels", request, ListModelsResponse)

  def add_model_tag(self, request: AddModelTagRequest = None):
    r"""
    Args:
      request (AddModelTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddModelTagRequest()

    self._client.call("models.ModelService", "AddModelTag", request, None)

  def remove_model_tag(self, request: RemoveModelTagRequest = None):
    r"""
    Args:
      request (RemoveModelTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveModelTagRequest()

    self._client.call("models.ModelService", "RemoveModelTag", request, None)

  def create_model_instance(self, request: CreateModelInstanceRequest = None) -> ModelInstance:
    r"""
    Args:
      request (CreateModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateModelInstanceRequest()

    return self._client.call("models.ModelService", "CreateModelInstance", request, ModelInstance)

  def delete_model_instance(self, request: DeleteModelInstanceRequest = None) -> DeleteModelInstanceResponse:
    r"""
    Args:
      request (DeleteModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteModelInstanceRequest()

    return self._client.call("models.ModelService", "DeleteModelInstance", request, DeleteModelInstanceResponse)

  def create_model_instance_version(self, request: CreateModelInstanceVersionRequest = None) -> ModelInstance:
    r"""
    Args:
      request (CreateModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateModelInstanceVersionRequest()

    return self._client.call("models.ModelService", "CreateModelInstanceVersion", request, ModelInstance)

  def copy_model_instance_version(self, request: CopyModelInstanceVersionRequest = None) -> ModelInstance:
    r"""
    Args:
      request (CopyModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CopyModelInstanceVersionRequest()

    return self._client.call("models.ModelService", "CopyModelInstanceVersion", request, ModelInstance)

  def delete_model_instance_version(self, request: DeleteModelInstanceVersionRequest = None) -> DeleteModelInstanceVersionResponse:
    r"""
    Args:
      request (DeleteModelInstanceVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteModelInstanceVersionRequest()

    return self._client.call("models.ModelService", "DeleteModelInstanceVersion", request, DeleteModelInstanceVersionResponse)

  def update_model_instance(self, request: UpdateModelInstanceRequest = None) -> ModelInstance:
    r"""
    This RPC is used for updating a model instance metadata (e.g overview,
    usage, etc.). To upload new files for this instance, use the
    CreateModelInstanceVersion RPC above.

    Args:
      request (UpdateModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateModelInstanceRequest()

    return self._client.call("models.ModelService", "UpdateModelInstance", request, ModelInstance)

  def create_model_doi(self, request: CreateModelDoiRequest = None) -> CreateModelDoiResponse:
    r"""
    Args:
      request (CreateModelDoiRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateModelDoiRequest()

    return self._client.call("models.ModelService", "CreateModelDoi", request, CreateModelDoiResponse)

  def get_model_instance_history(self, request: GetModelInstanceHistoryRequest = None) -> GetModelInstanceHistoryResponse:
    r"""
    Args:
      request (GetModelInstanceHistoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelInstanceHistoryRequest()

    return self._client.call("models.ModelService", "GetModelInstanceHistory", request, GetModelInstanceHistoryResponse)

  def list_owners(self, request: ListOwnersRequest = None) -> ListOwnersResponse:
    r"""
    Args:
      request (ListOwnersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListOwnersRequest()

    return self._client.call("models.ModelService", "ListOwners", request, ListOwnersResponse)

  def get_model_limits(self, request: GetModelLimitsRequest = None) -> DiskUsageLimits:
    r"""
    Args:
      request (GetModelLimitsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelLimitsRequest()

    return self._client.call("models.ModelService", "GetModelLimits", request, DiskUsageLimits)

  def increment_model_view_count(self, request: IncrementModelViewCountRequest = None):
    r"""
    Args:
      request (IncrementModelViewCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = IncrementModelViewCountRequest()

    self._client.call("models.ModelService", "IncrementModelViewCount", request, None)

  def update_model_owner(self, request: UpdateModelOwnerRequest = None) -> UpdateModelOwnerResponse:
    r"""
    Args:
      request (UpdateModelOwnerRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateModelOwnerRequest()

    return self._client.call("models.ModelService", "UpdateModelOwner", request, UpdateModelOwnerResponse)

  def list_sample_tasks(self, request: ListSampleTasksRequest = None) -> ListSampleTasksResponse:
    r"""
    Args:
      request (ListSampleTasksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSampleTasksRequest()

    return self._client.call("models.ModelService", "ListSampleTasks", request, ListSampleTasksResponse)

  def pin_model_instance_to_competition(self, request: PinModelInstanceToCompetitionRequest = None):
    r"""
    Args:
      request (PinModelInstanceToCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PinModelInstanceToCompetitionRequest()

    self._client.call("models.ModelService", "PinModelInstanceToCompetition", request, None)

  def unpin_model_instance_from_competition(self, request: UnpinModelInstanceFromCompetitionRequest = None):
    r"""
    Args:
      request (UnpinModelInstanceFromCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnpinModelInstanceFromCompetitionRequest()

    self._client.call("models.ModelService", "UnpinModelInstanceFromCompetition", request, None)

  def list_competition_model_instances(self, request: ListCompetitionModelInstancesRequest = None) -> ListCompetitionModelInstancesResponse:
    r"""
    Args:
      request (ListCompetitionModelInstancesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCompetitionModelInstancesRequest()

    return self._client.call("models.ModelService", "ListCompetitionModelInstances", request, ListCompetitionModelInstancesResponse)

  def get_model_instance_uploader_config(self, request: GetModelInstanceUploaderConfigRequest = None) -> ModelUploaderConfig:
    r"""
    Args:
      request (GetModelInstanceUploaderConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelInstanceUploaderConfigRequest()

    return self._client.call("models.ModelService", "GetModelInstanceUploaderConfig", request, ModelUploaderConfig)

  def get_user_model_counts(self, request: GetUserModelCountsRequest = None) -> GetUserModelCountsResponse:
    r"""
    Args:
      request (GetUserModelCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserModelCountsRequest()

    return self._client.call("models.ModelService", "GetUserModelCounts", request, GetUserModelCountsResponse)

  def refresh_remote_model_instance(self, request: RefreshRemoteModelInstanceRequest = None) -> ModelInstance:
    r"""
    Args:
      request (RefreshRemoteModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RefreshRemoteModelInstanceRequest()

    return self._client.call("models.ModelService", "RefreshRemoteModelInstance", request, ModelInstance)

  def list_model_competitions(self, request: ListModelCompetitionsRequest = None) -> ListModelCompetitionsResponse:
    r"""
    Args:
      request (ListModelCompetitionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelCompetitionsRequest()

    return self._client.call("models.ModelService", "ListModelCompetitions", request, ListModelCompetitionsResponse)

  def list_model_license_groups(self, request: ListModelLicenseGroupsRequest = None) -> ListModelLicenseGroupsResponse:
    r"""
    Args:
      request (ListModelLicenseGroupsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelLicenseGroupsRequest()

    return self._client.call("models.ModelService", "ListModelLicenseGroups", request, ListModelLicenseGroupsResponse)

  def preview_gating_agreement_content(self, request: PreviewGatingAgreementContentRequest = None) -> GatingAgreementContent:
    r"""
    Model gating handlers.

    Args:
      request (PreviewGatingAgreementContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PreviewGatingAgreementContentRequest()

    return self._client.call("models.ModelService", "PreviewGatingAgreementContent", request, GatingAgreementContent)

  def create_gating_agreement(self, request: CreateGatingAgreementRequest = None) -> GatingAgreement:
    r"""
    Args:
      request (CreateGatingAgreementRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateGatingAgreementRequest()

    return self._client.call("models.ModelService", "CreateGatingAgreement", request, GatingAgreement)

  def create_gating_user_consent(self, request: CreateGatingUserConsentRequest = None) -> GatingUserConsent:
    r"""
    Args:
      request (CreateGatingUserConsentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateGatingUserConsentRequest()

    return self._client.call("models.ModelService", "CreateGatingUserConsent", request, GatingUserConsent)

  def get_gating_user_consents(self, request: GetGatingUserConsentsRequest = None) -> GetGatingUserConsentsResponse:
    r"""
    Args:
      request (GetGatingUserConsentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetGatingUserConsentsRequest()

    return self._client.call("models.ModelService", "GetGatingUserConsents", request, GetGatingUserConsentsResponse)

  def get_user_gating_consent_data(self, request: GetUserGatingConsentDataRequest = None) -> GetUserGatingConsentDataResponse:
    r"""
    Args:
      request (GetUserGatingConsentDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserGatingConsentDataRequest()

    return self._client.call("models.ModelService", "GetUserGatingConsentData", request, GetUserGatingConsentDataResponse)

  def review_gating_user_consent(self, request: ReviewGatingUserConsentRequest = None) -> GatingUserConsent:
    r"""
    Args:
      request (ReviewGatingUserConsentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReviewGatingUserConsentRequest()

    return self._client.call("models.ModelService", "ReviewGatingUserConsent", request, GatingUserConsent)

  def get_model_gating(self, request: GetModelGatingRequest = None) -> ModelGating:
    r"""
    Args:
      request (GetModelGatingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelGatingRequest()

    return self._client.call("models.ModelService", "GetModelGating", request, ModelGating)

  def update_model_gating(self, request: UpdateModelGatingRequest = None) -> ModelGating:
    r"""
    Args:
      request (UpdateModelGatingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateModelGatingRequest()

    return self._client.call("models.ModelService", "UpdateModelGating", request, ModelGating)

  def get_kernel_output_model_instance(self, request: GetKernelOutputModelInstanceRequest = None) -> KernelOutputModelInstanceReference:
    r"""
    Args:
      request (GetKernelOutputModelInstanceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelOutputModelInstanceRequest()

    return self._client.call("models.ModelService", "GetKernelOutputModelInstance", request, KernelOutputModelInstanceReference)
