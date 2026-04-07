from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.legacy_users_service import AccountDto, EmailSignInRequest, EmailSignInResponse, LegacyChangePasswordRequest, LegacyDeleteUserLoginRequest, LegacyGetAccountRequest, LegacyUpdateAccountEmailAddressRequest

class LegacyUsersClient(object):
  r"""
  These RPCs are implemented in Kaggle.Services.Legacy due to dependency
  issues:
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def email_sign_in(self, request: EmailSignInRequest = None) -> EmailSignInResponse:
    r"""
    Args:
      request (EmailSignInRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = EmailSignInRequest()

    return self._client.call("users.LegacyUsersService", "EmailSignIn", request, EmailSignInResponse)

  def legacy_change_password(self, request: LegacyChangePasswordRequest = None):
    r"""
    Args:
      request (LegacyChangePasswordRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyChangePasswordRequest()

    self._client.call("users.LegacyUsersService", "LegacyChangePassword", request, None)

  def legacy_delete_user_login(self, request: LegacyDeleteUserLoginRequest = None):
    r"""
    Args:
      request (LegacyDeleteUserLoginRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyDeleteUserLoginRequest()

    self._client.call("users.LegacyUsersService", "LegacyDeleteUserLogin", request, None)

  def legacy_get_account(self, request: LegacyGetAccountRequest = None) -> AccountDto:
    r"""
    Args:
      request (LegacyGetAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyGetAccountRequest()

    return self._client.call("users.LegacyUsersService", "LegacyGetAccount", request, AccountDto)

  def legacy_update_account_email_address(self, request: LegacyUpdateAccountEmailAddressRequest = None):
    r"""
    Args:
      request (LegacyUpdateAccountEmailAddressRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LegacyUpdateAccountEmailAddressRequest()

    self._client.call("users.LegacyUsersService", "LegacyUpdateAccountEmailAddress", request, None)
