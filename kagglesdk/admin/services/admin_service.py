from kagglesdk.admin.types.admin_service import AddSiteConfigRequest, AdminUser, AutoFormModel, BatchDeleteAccountActivityRequest, BatchDeleteAccountActivityResponse, BulkUpdateEmergencyBannersRequest, CreateIdmecLinkRequest, CreateIdmecLinkResponse, DeleteAllEmergencyBannersRequest, DeleteEmergencyBannerRequest, DeleteSiteConfigRequest, GetAdminUserRequest, GetAllSiteConfigsRequest, GetAllSiteConfigsResponse, GetApiMethodSampleRequestRequest, GetApiMethodSampleRequestResponse, GetAutoFormModelRequest, GetSearchIndexStatusRequest, GetSearchIndexStatusResponse, ListApiMethodsRequest, ListApiMethodsResponse, ListEmergencyBannersRequest, ListEmergencyBannersResponse, RenewIapTokenRequest, RenewIapTokenResponse, ResetSearchIndexesRequest, ResetSearchIndexRequest, UpdateAutoFormModelRequest, UpdateEmergencyBannerRequest, UpdateNonGenieAutoFormModelRequest, UpdateSiteConfigRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AdminClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def add_site_config(self, request: AddSiteConfigRequest = None):
    r"""
    Args:
      request (AddSiteConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddSiteConfigRequest()

    self._client.call("admin.AdminService", "AddSiteConfig", request, None)

  def delete_site_config(self, request: DeleteSiteConfigRequest = None):
    r"""
    Args:
      request (DeleteSiteConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteSiteConfigRequest()

    self._client.call("admin.AdminService", "DeleteSiteConfig", request, None)

  def batch_delete_account_activity(self, request: BatchDeleteAccountActivityRequest = None) -> BatchDeleteAccountActivityResponse:
    r"""
    Deletes activity not directly related to User Generated Content (UGC).
    For context, see b/275816857

    Args:
      request (BatchDeleteAccountActivityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteAccountActivityRequest()

    return self._client.call("admin.AdminService", "BatchDeleteAccountActivity", request, BatchDeleteAccountActivityResponse)

  def get_admin_user(self, request: GetAdminUserRequest = None) -> AdminUser:
    r"""
    Args:
      request (GetAdminUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAdminUserRequest()

    return self._client.call("admin.AdminService", "GetAdminUser", request, AdminUser)

  def get_all_site_configs(self, request: GetAllSiteConfigsRequest = None) -> GetAllSiteConfigsResponse:
    r"""
    Returns all SiteConfigs, sorted by name.
    This RPC will honor C#-defined flags annotated with FlagDefault if a
    DB-specified value is not found (represented by unset Id)

    Args:
      request (GetAllSiteConfigsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAllSiteConfigsRequest()

    return self._client.call("admin.AdminService", "GetAllSiteConfigs", request, GetAllSiteConfigsResponse)

  def list_api_methods(self, request: ListApiMethodsRequest = None) -> ListApiMethodsResponse:
    r"""
    Args:
      request (ListApiMethodsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListApiMethodsRequest()

    return self._client.call("admin.AdminService", "ListApiMethods", request, ListApiMethodsResponse)

  def get_api_method_sample_request(self, request: GetApiMethodSampleRequestRequest = None) -> GetApiMethodSampleRequestResponse:
    r"""
    Args:
      request (GetApiMethodSampleRequestRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetApiMethodSampleRequestRequest()

    return self._client.call("admin.AdminService", "GetApiMethodSampleRequest", request, GetApiMethodSampleRequestResponse)

  def reset_search_indexes(self, request: ResetSearchIndexesRequest = None):
    r"""
    Args:
      request (ResetSearchIndexesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ResetSearchIndexesRequest()

    self._client.call("admin.AdminService", "ResetSearchIndexes", request, None)

  def reset_search_index(self, request: ResetSearchIndexRequest = None):
    r"""
    Args:
      request (ResetSearchIndexRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ResetSearchIndexRequest()

    self._client.call("admin.AdminService", "ResetSearchIndex", request, None)

  def get_search_index_status(self, request: GetSearchIndexStatusRequest = None) -> GetSearchIndexStatusResponse:
    r"""
    Args:
      request (GetSearchIndexStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetSearchIndexStatusRequest()

    return self._client.call("admin.AdminService", "GetSearchIndexStatus", request, GetSearchIndexStatusResponse)

  def update_site_config(self, request: UpdateSiteConfigRequest = None):
    r"""
    Updates an existing non-ops SiteConfig. To update a FlagDefault-specified
    config, use AddSiteConfig.

    Args:
      request (UpdateSiteConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSiteConfigRequest()

    self._client.call("admin.AdminService", "UpdateSiteConfig", request, None)

  def get_auto_form_model(self, request: GetAutoFormModelRequest = None) -> AutoFormModel:
    r"""
    Args:
      request (GetAutoFormModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAutoFormModelRequest()

    return self._client.call("admin.AdminService", "GetAutoFormModel", request, AutoFormModel)

  def update_auto_form_model(self, request: UpdateAutoFormModelRequest = None):
    r"""
    Args:
      request (UpdateAutoFormModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateAutoFormModelRequest()

    self._client.call("admin.AdminService", "UpdateAutoFormModel", request, None)

  def update_non_genie_auto_form_model(self, request: UpdateNonGenieAutoFormModelRequest = None):
    r"""
    Update an auto-form model that doesn't require genie access (ie no user
    data).

    Args:
      request (UpdateNonGenieAutoFormModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateNonGenieAutoFormModelRequest()

    self._client.call("admin.AdminService", "UpdateNonGenieAutoFormModel", request, None)

  def create_idmec_link(self, request: CreateIdmecLinkRequest = None) -> CreateIdmecLinkResponse:
    r"""
    Generate a link that allows anyone with the link to access an IDMEC record.
    This is used in response to a request from legal to access the data we
    stored for a user under the IDMEC jurisdiction.

    Args:
      request (CreateIdmecLinkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateIdmecLinkRequest()

    return self._client.call("admin.AdminService", "CreateIdmecLink", request, CreateIdmecLinkResponse)

  def list_emergency_banners(self, request: ListEmergencyBannersRequest = None) -> ListEmergencyBannersResponse:
    r"""
    Args:
      request (ListEmergencyBannersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListEmergencyBannersRequest()

    return self._client.call("admin.AdminService", "ListEmergencyBanners", request, ListEmergencyBannersResponse)

  def update_emergency_banner(self, request: UpdateEmergencyBannerRequest = None):
    r"""
    Args:
      request (UpdateEmergencyBannerRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateEmergencyBannerRequest()

    self._client.call("admin.AdminService", "UpdateEmergencyBanner", request, None)

  def bulk_update_emergency_banners(self, request: BulkUpdateEmergencyBannersRequest = None):
    r"""
    Args:
      request (BulkUpdateEmergencyBannersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkUpdateEmergencyBannersRequest()

    self._client.call("admin.AdminService", "BulkUpdateEmergencyBanners", request, None)

  def delete_emergency_banner(self, request: DeleteEmergencyBannerRequest = None):
    r"""
    Args:
      request (DeleteEmergencyBannerRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteEmergencyBannerRequest()

    self._client.call("admin.AdminService", "DeleteEmergencyBanner", request, None)

  def delete_all_emergency_banners(self, request: DeleteAllEmergencyBannersRequest = None):
    r"""
    Args:
      request (DeleteAllEmergencyBannersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteAllEmergencyBannersRequest()

    self._client.call("admin.AdminService", "DeleteAllEmergencyBanners", request, None)

  def renew_iap_token(self, request: RenewIapTokenRequest = None) -> RenewIapTokenResponse:
    r"""
    Args:
      request (RenewIapTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RenewIapTokenRequest()

    return self._client.call("admin.AdminService", "RenewIapToken", request, RenewIapTokenResponse)
