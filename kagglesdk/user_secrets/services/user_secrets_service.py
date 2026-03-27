from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.user_secrets.types.user_secrets_service import AddSecretKernelAttachmentRequest, CheckGoogleGroupsAccessRequest, CheckGoogleGroupsAccessResponse, DeleteSecretKernelAttachmentRequest, DeleteUserSecretRequest, DeleteUserSecretResponse, ExchangeGcloudAuthorizationCodeRequest, GetColabAccessInfoRequest, GetColabAccessInfoResponse, GetDriveAccessInfoRequest, GetDriveAccessInfoResponse, GetGitHubAccessInfoRequest, GetGitHubAccessInfoResponse, GetHuggingFaceAccessInfoRequest, GetHuggingFaceAccessInfoResponse, GetUserSecretByLabelRequest, GetUserSecretResponse, ListKernelSecretsMetadataRequest, ListKernelSecretsMetadataResponse, ListKernelsWithSecretRequest, ListKernelsWithSecretResponse, ListUserSecretsMetadataRequest, ListUserSecretsMetadataResponse, UpsertCustomUserSecretRequest, UserSecretKernelAttachmentMetadata, UserSecretMetadata

class UserSecretsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def add_secret_kernel_attachment(self, request: AddSecretKernelAttachmentRequest = None) -> UserSecretKernelAttachmentMetadata:
    r"""
    Args:
      request (AddSecretKernelAttachmentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddSecretKernelAttachmentRequest()

    return self._client.call("user_secrets.UserSecretsService", "AddSecretKernelAttachment", request, UserSecretKernelAttachmentMetadata)

  def delete_secret_kernel_attachment(self, request: DeleteSecretKernelAttachmentRequest = None):
    r"""
    Args:
      request (DeleteSecretKernelAttachmentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteSecretKernelAttachmentRequest()

    self._client.call("user_secrets.UserSecretsService", "DeleteSecretKernelAttachment", request, None)

  def delete_user_secret(self, request: DeleteUserSecretRequest = None) -> DeleteUserSecretResponse:
    r"""
    Args:
      request (DeleteUserSecretRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteUserSecretRequest()

    return self._client.call("user_secrets.UserSecretsService", "DeleteUserSecret", request, DeleteUserSecretResponse)

  def exchange_gcloud_authorization_code(self, request: ExchangeGcloudAuthorizationCodeRequest = None) -> UserSecretMetadata:
    r"""
    Args:
      request (ExchangeGcloudAuthorizationCodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExchangeGcloudAuthorizationCodeRequest()

    return self._client.call("user_secrets.UserSecretsService", "ExchangeGcloudAuthorizationCode", request, UserSecretMetadata)

  def get_drive_access_info(self, request: GetDriveAccessInfoRequest = None) -> GetDriveAccessInfoResponse:
    r"""
    Args:
      request (GetDriveAccessInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDriveAccessInfoRequest()

    return self._client.call("user_secrets.UserSecretsService", "GetDriveAccessInfo", request, GetDriveAccessInfoResponse)

  def get_colab_access_info(self, request: GetColabAccessInfoRequest = None) -> GetColabAccessInfoResponse:
    r"""
    Args:
      request (GetColabAccessInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetColabAccessInfoRequest()

    return self._client.call("user_secrets.UserSecretsService", "GetColabAccessInfo", request, GetColabAccessInfoResponse)

  def get_git_hub_access_info(self, request: GetGitHubAccessInfoRequest = None) -> GetGitHubAccessInfoResponse:
    r"""
    Args:
      request (GetGitHubAccessInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetGitHubAccessInfoRequest()

    return self._client.call("user_secrets.UserSecretsService", "GetGitHubAccessInfo", request, GetGitHubAccessInfoResponse)

  def get_hugging_face_access_info(self, request: GetHuggingFaceAccessInfoRequest = None) -> GetHuggingFaceAccessInfoResponse:
    r"""
    Args:
      request (GetHuggingFaceAccessInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHuggingFaceAccessInfoRequest()

    return self._client.call("user_secrets.UserSecretsService", "GetHuggingFaceAccessInfo", request, GetHuggingFaceAccessInfoResponse)

  def check_google_groups_access(self, request: CheckGoogleGroupsAccessRequest = None) -> CheckGoogleGroupsAccessResponse:
    r"""
    Args:
      request (CheckGoogleGroupsAccessRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckGoogleGroupsAccessRequest()

    return self._client.call("user_secrets.UserSecretsService", "CheckGoogleGroupsAccess", request, CheckGoogleGroupsAccessResponse)

  def get_user_secret_by_label(self, request: GetUserSecretByLabelRequest = None) -> GetUserSecretResponse:
    r"""
    Args:
      request (GetUserSecretByLabelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserSecretByLabelRequest()

    return self._client.call("user_secrets.UserSecretsService", "GetUserSecretByLabel", request, GetUserSecretResponse)

  def list_kernel_secrets_metadata(self, request: ListKernelSecretsMetadataRequest = None) -> ListKernelSecretsMetadataResponse:
    r"""
    Args:
      request (ListKernelSecretsMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelSecretsMetadataRequest()

    return self._client.call("user_secrets.UserSecretsService", "ListKernelSecretsMetadata", request, ListKernelSecretsMetadataResponse)

  def list_kernels_with_secret(self, request: ListKernelsWithSecretRequest = None) -> ListKernelsWithSecretResponse:
    r"""
    Args:
      request (ListKernelsWithSecretRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListKernelsWithSecretRequest()

    return self._client.call("user_secrets.UserSecretsService", "ListKernelsWithSecret", request, ListKernelsWithSecretResponse)

  def list_user_secrets_metadata(self, request: ListUserSecretsMetadataRequest = None) -> ListUserSecretsMetadataResponse:
    r"""
    Args:
      request (ListUserSecretsMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserSecretsMetadataRequest()

    return self._client.call("user_secrets.UserSecretsService", "ListUserSecretsMetadata", request, ListUserSecretsMetadataResponse)

  def upsert_custom_user_secret(self, request: UpsertCustomUserSecretRequest = None) -> UserSecretMetadata:
    r"""
    Args:
      request (UpsertCustomUserSecretRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpsertCustomUserSecretRequest()

    return self._client.call("user_secrets.UserSecretsService", "UpsertCustomUserSecret", request, UserSecretMetadata)
