from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.verification_service import GetUserVerificationRequest, GetUserVerificationResponse, GetVerificationStatusRequest, GetVerificationStatusResponse, InvalidateUserVerificationInquiriesRequest, ListPhoneVerificationsRequest, ListPhoneVerificationsResponse, ListUserVerificationInquiriesRequest, ListUserVerificationInquiriesResponse, ManuallyVerifyUserRequest, RedactUserVerificationInquiriesRequest

class VerificationClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_verification_status(self, request: GetVerificationStatusRequest = None) -> GetVerificationStatusResponse:
    r"""
    Args:
      request (GetVerificationStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetVerificationStatusRequest()

    return self._client.call("users.VerificationService", "GetVerificationStatus", request, GetVerificationStatusResponse)

  def redact_user_verification_inquiries(self, request: RedactUserVerificationInquiriesRequest = None):
    r"""
    Redacts the user's PII from Persona and un-verifies them.
    Can be called by a user if they wish to remove their data. Also called when
    we hard delete an account.

    Args:
      request (RedactUserVerificationInquiriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RedactUserVerificationInquiriesRequest()

    self._client.call("users.VerificationService", "RedactUserVerificationInquiries", request, None)

  def manually_verify_user(self, request: ManuallyVerifyUserRequest = None):
    r"""
    Bypasses Persona to verify a user

    Args:
      request (ManuallyVerifyUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ManuallyVerifyUserRequest()

    self._client.call("users.VerificationService", "ManuallyVerifyUser", request, None)

  def invalidate_user_verification_inquiries(self, request: InvalidateUserVerificationInquiriesRequest = None):
    r"""
    Invalidates all existing inquiries for a user to require re-verification

    Args:
      request (InvalidateUserVerificationInquiriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateUserVerificationInquiriesRequest()

    self._client.call("users.VerificationService", "InvalidateUserVerificationInquiries", request, None)

  def get_user_verification(self, request: GetUserVerificationRequest = None) -> GetUserVerificationResponse:
    r"""
    Admin-only endpoint to return user verification info for showing in Genie.
    If you'd like to use this in handler logic, use GetUserVerificationHelper.

    Args:
      request (GetUserVerificationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserVerificationRequest()

    return self._client.call("users.VerificationService", "GetUserVerification", request, GetUserVerificationResponse)

  def list_user_verification_inquiries(self, request: ListUserVerificationInquiriesRequest = None) -> ListUserVerificationInquiriesResponse:
    r"""
    Args:
      request (ListUserVerificationInquiriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserVerificationInquiriesRequest()

    return self._client.call("users.VerificationService", "ListUserVerificationInquiries", request, ListUserVerificationInquiriesResponse)

  def list_phone_verifications(self, request: ListPhoneVerificationsRequest = None) -> ListPhoneVerificationsResponse:
    r"""
    Args:
      request (ListPhoneVerificationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListPhoneVerificationsRequest()

    return self._client.call("users.VerificationService", "ListPhoneVerifications", request, ListPhoneVerificationsResponse)
