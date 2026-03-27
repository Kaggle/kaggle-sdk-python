from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.account_service import BatchSoftDeleteAccountsRequest, BatchSoftDeleteAccountsResponse, ContactSupportRequest, DeleteCurrentAccountRequest, ExpireApiTokenRequest, ExpireApiTokensRequest, GenerateAnalyticsTokenRequest, GenerateAnalyticsTokenResponse, GenerateApiTokenRequest, GenerateApiTokenResponse, GetBuildInfoRequest, GetBuildInfoResponse, GetPhoneVerificationStatusRequest, GetPhoneVerificationStatusResponse, GetSupportPhoneNumbersRequest, GetSupportPhoneNumbersResponse, ListApiTokensRequest, ListApiTokensResponse, ListCurrentUserModerationHistoryRequest, ListCurrentUserModerationHistoryResponse, ListSupportRequestsRequest, ListSupportRequestsResponse, NewEmailRegistrationUserRequest, NewEmailRegistrationUserResponse, RegistrationValidationRequest, RegistrationValidationResponse, ReportContentRequest, ResendVerificationEmailRequest, ResetPasswordRequest, ResetPasswordResponse, SignOutRequest, SoftDeleteAccountRequest, SoftDeleteAccountResponse, StartMigrateSsoRequest, StartMigrateSsoResponse, StartPhoneVerificationRequest, StartPhoneVerificationResponse, StartResetPasswordRequest, TakeoutUserRequest, TakeoutUserResponse, ValidateResetPasswordCodeRequest, ValidateResetPasswordCodeResponse, VerifyAccountEmailRequest, VerifyAccountEmailResponse, VerifyPhoneRequest

class AccountClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def verify_account_email(self, request: VerifyAccountEmailRequest = None) -> VerifyAccountEmailResponse:
    r"""
    Attempt to verify an account from an emailed verification code.

    Args:
      request (VerifyAccountEmailRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VerifyAccountEmailRequest()

    return self._client.call("users.AccountService", "VerifyAccountEmail", request, VerifyAccountEmailResponse)

  def sign_out(self, request: SignOutRequest = None):
    r"""
    Sign the current user out.

    Args:
      request (SignOutRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SignOutRequest()

    self._client.call("users.AccountService", "SignOut", request, None)

  def new_email_registration_user(self, request: NewEmailRegistrationUserRequest = None) -> NewEmailRegistrationUserResponse:
    r"""
    Registers the user via email.

    Args:
      request (NewEmailRegistrationUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = NewEmailRegistrationUserRequest()

    return self._client.call("users.AccountService", "NewEmailRegistrationUser", request, NewEmailRegistrationUserResponse)

  def registration_validation(self, request: RegistrationValidationRequest = None) -> RegistrationValidationResponse:
    r"""
    Validates registration values and returns any applicable errors.

    Args:
      request (RegistrationValidationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RegistrationValidationRequest()

    return self._client.call("users.AccountService", "RegistrationValidation", request, RegistrationValidationResponse)

  def start_phone_verification(self, request: StartPhoneVerificationRequest = None) -> StartPhoneVerificationResponse:
    r"""
    Creates and starts the phone verification process.

    Args:
      request (StartPhoneVerificationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartPhoneVerificationRequest()

    return self._client.call("users.AccountService", "StartPhoneVerification", request, StartPhoneVerificationResponse)

  def get_phone_verification_status(self, request: GetPhoneVerificationStatusRequest = None) -> GetPhoneVerificationStatusResponse:
    r"""
    Args:
      request (GetPhoneVerificationStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPhoneVerificationStatusRequest()

    return self._client.call("users.AccountService", "GetPhoneVerificationStatus", request, GetPhoneVerificationStatusResponse)

  def contact_support(self, request: ContactSupportRequest = None):
    r"""
    Args:
      request (ContactSupportRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ContactSupportRequest()

    self._client.call("users.AccountService", "ContactSupport", request, None)

  def get_support_phone_numbers(self, request: GetSupportPhoneNumbersRequest = None) -> GetSupportPhoneNumbersResponse:
    r"""
    Args:
      request (GetSupportPhoneNumbersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetSupportPhoneNumbersRequest()

    return self._client.call("users.AccountService", "GetSupportPhoneNumbers", request, GetSupportPhoneNumbersResponse)

  def list_support_requests(self, request: ListSupportRequestsRequest = None) -> ListSupportRequestsResponse:
    r"""
    Args:
      request (ListSupportRequestsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSupportRequestsRequest()

    return self._client.call("users.AccountService", "ListSupportRequests", request, ListSupportRequestsResponse)

  def list_api_tokens(self, request: ListApiTokensRequest = None) -> ListApiTokensResponse:
    r"""
    Args:
      request (ListApiTokensRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListApiTokensRequest()

    return self._client.call("users.AccountService", "ListApiTokens", request, ListApiTokensResponse)

  def generate_api_token(self, request: GenerateApiTokenRequest = None) -> GenerateApiTokenResponse:
    r"""
    Args:
      request (GenerateApiTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GenerateApiTokenRequest()

    return self._client.call("users.AccountService", "GenerateApiToken", request, GenerateApiTokenResponse)

  def expire_api_token(self, request: ExpireApiTokenRequest = None):
    r"""
    Args:
      request (ExpireApiTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExpireApiTokenRequest()

    self._client.call("users.AccountService", "ExpireApiToken", request, None)

  def expire_api_tokens(self, request: ExpireApiTokensRequest = None):
    r"""
    Args:
      request (ExpireApiTokensRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ExpireApiTokensRequest()

    self._client.call("users.AccountService", "ExpireApiTokens", request, None)

  def delete_current_account(self, request: DeleteCurrentAccountRequest = None) -> SoftDeleteAccountResponse:
    r"""
    Delete the current user's account (put into soft-delete, for later hard
    delete).

    Args:
      request (DeleteCurrentAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCurrentAccountRequest()

    return self._client.call("users.AccountService", "DeleteCurrentAccount", request, SoftDeleteAccountResponse)

  def soft_delete_account(self, request: SoftDeleteAccountRequest = None) -> SoftDeleteAccountResponse:
    r"""
    Delete the requested user's account (put into soft-delete, for late hard
    delete).

    Args:
      request (SoftDeleteAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SoftDeleteAccountRequest()

    return self._client.call("users.AccountService", "SoftDeleteAccount", request, SoftDeleteAccountResponse)

  def batch_soft_delete_accounts(self, request: BatchSoftDeleteAccountsRequest = None) -> BatchSoftDeleteAccountsResponse:
    r"""
    Delete a collection of users (soft-delete, then mark for later hard
    delete). This request is idempotent, so it can be called repeatedly if some
    users encounter errors, or it takes too long to process.

    Args:
      request (BatchSoftDeleteAccountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchSoftDeleteAccountsRequest()

    return self._client.call("users.AccountService", "BatchSoftDeleteAccounts", request, BatchSoftDeleteAccountsResponse)

  def generate_analytics_token(self, request: GenerateAnalyticsTokenRequest = None) -> GenerateAnalyticsTokenResponse:
    r"""
    Args:
      request (GenerateAnalyticsTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GenerateAnalyticsTokenRequest()

    return self._client.call("users.AccountService", "GenerateAnalyticsToken", request, GenerateAnalyticsTokenResponse)

  def start_reset_password(self, request: StartResetPasswordRequest = None):
    r"""
    Request a reset password code be sent to the given email. No direct
    response to prevent leaking email existence.

    Args:
      request (StartResetPasswordRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartResetPasswordRequest()

    self._client.call("users.AccountService", "StartResetPassword", request, None)

  def validate_reset_password_code(self, request: ValidateResetPasswordCodeRequest = None) -> ValidateResetPasswordCodeResponse:
    r"""
    Validate a given password code, and get the user Id for it if valid.

    Args:
      request (ValidateResetPasswordCodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ValidateResetPasswordCodeRequest()

    return self._client.call("users.AccountService", "ValidateResetPasswordCode", request, ValidateResetPasswordCodeResponse)

  def reset_password(self, request: ResetPasswordRequest = None) -> ResetPasswordResponse:
    r"""
    Given a valid password reset code, reset the password of the user to the
    given password and log them in.

    Args:
      request (ResetPasswordRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ResetPasswordRequest()

    return self._client.call("users.AccountService", "ResetPassword", request, ResetPasswordResponse)

  def resend_verification_email(self, request: ResendVerificationEmailRequest = None):
    r"""
    Args:
      request (ResendVerificationEmailRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ResendVerificationEmailRequest()

    self._client.call("users.AccountService", "ResendVerificationEmail", request, None)

  def start_migrate_sso(self, request: StartMigrateSsoRequest = None) -> StartMigrateSsoResponse:
    r"""
    Args:
      request (StartMigrateSsoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartMigrateSsoRequest()

    return self._client.call("users.AccountService", "StartMigrateSso", request, StartMigrateSsoResponse)

  def verify_phone(self, request: VerifyPhoneRequest = None):
    r"""
    Args:
      request (VerifyPhoneRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VerifyPhoneRequest()

    self._client.call("users.AccountService", "VerifyPhone", request, None)

  def takeout_user(self, request: TakeoutUserRequest = None) -> TakeoutUserResponse:
    r"""
    Performs user takeout, putting a user's data into the appropriate bucket.

    Args:
      request (TakeoutUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TakeoutUserRequest()

    return self._client.call("users.AccountService", "TakeoutUser", request, TakeoutUserResponse)

  def get_build_info(self, request: GetBuildInfoRequest = None) -> GetBuildInfoResponse:
    r"""
    Args:
      request (GetBuildInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBuildInfoRequest()

    return self._client.call("users.AccountService", "GetBuildInfo", request, GetBuildInfoResponse)

  def report_content(self, request: ReportContentRequest = None):
    r"""
    Report content for abuse, queuing it for the moderation team via Zendesk

    Args:
      request (ReportContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReportContentRequest()

    self._client.call("users.AccountService", "ReportContent", request, None)

  def list_current_user_moderation_history(self, request: ListCurrentUserModerationHistoryRequest = None) -> ListCurrentUserModerationHistoryResponse:
    r"""
    List all user-visible penalties & data for the current user

    Args:
      request (ListCurrentUserModerationHistoryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCurrentUserModerationHistoryRequest()

    return self._client.call("users.AccountService", "ListCurrentUserModerationHistory", request, ListCurrentUserModerationHistoryResponse)
