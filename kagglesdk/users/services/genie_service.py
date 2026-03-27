from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.genie_service import BulkSetKaggleXRoleRequest, BulkVerifyPhoneRequest, CreateKaggleAccountRequest, GetNewPasswordRequest, GetNewPasswordResponse, GetUserIdByUsernameOrEmailRequest, GetUserIdByUsernameOrEmailResponse, GetUserStatusLogsRequest, GetUserStatusLogsResponse, GrantSiteAdminRequest, RevokeSiteAdminRequest, UnverifyPhoneRequest

class GenieClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def bulk_verify_phone(self, request: BulkVerifyPhoneRequest = None):
    r"""
    Verify a group of phone numbers.

    Args:
      request (BulkVerifyPhoneRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkVerifyPhoneRequest()

    self._client.call("users.GenieService", "BulkVerifyPhone", request, None)

  def unverify_phone(self, request: UnverifyPhoneRequest = None):
    r"""
    Unverify a user's phone number, forcing them to reverify.

    Args:
      request (UnverifyPhoneRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnverifyPhoneRequest()

    self._client.call("users.GenieService", "UnverifyPhone", request, None)

  def grant_site_admin(self, request: GrantSiteAdminRequest = None):
    r"""
    Grant the selected user admin privileges on kaggle.

    Args:
      request (GrantSiteAdminRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GrantSiteAdminRequest()

    self._client.call("users.GenieService", "GrantSiteAdmin", request, None)

  def revoke_site_admin(self, request: RevokeSiteAdminRequest = None):
    r"""
    Remove the admin privileges for a user.

    Args:
      request (RevokeSiteAdminRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RevokeSiteAdminRequest()

    self._client.call("users.GenieService", "RevokeSiteAdmin", request, None)

  def get_new_password(self, request: GetNewPasswordRequest = None) -> GetNewPasswordResponse:
    r"""
    Get a new randomly generated password.

    Args:
      request (GetNewPasswordRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNewPasswordRequest()

    return self._client.call("users.GenieService", "GetNewPassword", request, GetNewPasswordResponse)

  def create_kaggle_account(self, request: CreateKaggleAccountRequest = None):
    r"""
    Force-create a Kaggle login (username+password login).

    Args:
      request (CreateKaggleAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKaggleAccountRequest()

    self._client.call("users.GenieService", "CreateKaggleAccount", request, None)

  def get_user_status_logs(self, request: GetUserStatusLogsRequest = None) -> GetUserStatusLogsResponse:
    r"""
    Get the user status logs for a user.

    Args:
      request (GetUserStatusLogsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserStatusLogsRequest()

    return self._client.call("users.GenieService", "GetUserStatusLogs", request, GetUserStatusLogsResponse)

  def get_user_id_by_username_or_email(self, request: GetUserIdByUsernameOrEmailRequest = None) -> GetUserIdByUsernameOrEmailResponse:
    r"""
    Fetches a user ID by a given username or email. Prioritizes username
    matches.

    Args:
      request (GetUserIdByUsernameOrEmailRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserIdByUsernameOrEmailRequest()

    return self._client.call("users.GenieService", "GetUserIdByUsernameOrEmail", request, GetUserIdByUsernameOrEmailResponse)

  def bulk_set_kaggle_xrole(self, request: BulkSetKaggleXRoleRequest = None):
    r"""
    Set the KaggleX mentor/mentee role for a group of users.

    Args:
      request (BulkSetKaggleXRoleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkSetKaggleXRoleRequest()

    self._client.call("users.GenieService", "BulkSetKaggleXRole", request, None)
