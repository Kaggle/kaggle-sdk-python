from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_admin_service import AddModelImplementationRequest, AddModelVersionLinkRequest, DeleteModelImplementationRequest, DeleteModelVersionLinkRequest, GetTfHubRedirectRequest, GetTfHubRedirectResponse, RecreateModelInstanceVersionArchiveRequest, RecreateModelInstanceVersionArchiveResponse, ResetModelInstancesVersionsRequest, ResetModelInstancesVersionsResponse, SetTfHubRedirectRequest, SetTfHubRedirectResponse, UpdateModelSlugRequest, UpdateModelSlugResponse

class ModelAdminClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def recreate_model_instance_version_archive(self, request: RecreateModelInstanceVersionArchiveRequest = None) -> RecreateModelInstanceVersionArchiveResponse:
    r"""
    Args:
      request (RecreateModelInstanceVersionArchiveRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecreateModelInstanceVersionArchiveRequest()

    return self._client.call("models.ModelAdminService", "RecreateModelInstanceVersionArchive", request, RecreateModelInstanceVersionArchiveResponse)

  def update_model_slug(self, request: UpdateModelSlugRequest = None) -> UpdateModelSlugResponse:
    r"""
    Args:
      request (UpdateModelSlugRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateModelSlugRequest()

    return self._client.call("models.ModelAdminService", "UpdateModelSlug", request, UpdateModelSlugResponse)

  def get_tf_hub_redirect(self, request: GetTfHubRedirectRequest = None) -> GetTfHubRedirectResponse:
    r"""
    Args:
      request (GetTfHubRedirectRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTfHubRedirectRequest()

    return self._client.call("models.ModelAdminService", "GetTfHubRedirect", request, GetTfHubRedirectResponse)

  def set_tf_hub_redirect(self, request: SetTfHubRedirectRequest = None) -> SetTfHubRedirectResponse:
    r"""
    Args:
      request (SetTfHubRedirectRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetTfHubRedirectRequest()

    return self._client.call("models.ModelAdminService", "SetTfHubRedirect", request, SetTfHubRedirectResponse)

  def reset_model_instances_versions(self, request: ResetModelInstancesVersionsRequest = None) -> ResetModelInstancesVersionsResponse:
    r"""
    Args:
      request (ResetModelInstancesVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ResetModelInstancesVersionsRequest()

    return self._client.call("models.ModelAdminService", "ResetModelInstancesVersions", request, ResetModelInstancesVersionsResponse)

  def add_model_implementation(self, request: AddModelImplementationRequest = None):
    r"""
    Args:
      request (AddModelImplementationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddModelImplementationRequest()

    self._client.call("models.ModelAdminService", "AddModelImplementation", request, None)

  def delete_model_implementation(self, request: DeleteModelImplementationRequest = None):
    r"""
    Args:
      request (DeleteModelImplementationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteModelImplementationRequest()

    self._client.call("models.ModelAdminService", "DeleteModelImplementation", request, None)

  def add_model_version_link(self, request: AddModelVersionLinkRequest = None):
    r"""
    Args:
      request (AddModelVersionLinkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddModelVersionLinkRequest()

    self._client.call("models.ModelAdminService", "AddModelVersionLink", request, None)

  def delete_model_version_link(self, request: DeleteModelVersionLinkRequest = None):
    r"""
    Args:
      request (DeleteModelVersionLinkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteModelVersionLinkRequest()

    self._client.call("models.ModelAdminService", "DeleteModelVersionLink", request, None)
