from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.licenses.types.licenses_service import ConsentToUserLicenseAgreementRequest, GetLicenseConsentFormInfoRequest, StartLicenseConsentFormEmailVerificationRequest
from kagglesdk.licenses.types.licenses_types import LicenseConsentFormInfo

class LicensesClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def consent_to_user_license_agreement(self, request: ConsentToUserLicenseAgreementRequest = None):
    r"""
    Args:
      request (ConsentToUserLicenseAgreementRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ConsentToUserLicenseAgreementRequest()

    self._client.call("licenses.LicensesService", "ConsentToUserLicenseAgreement", request, None)

  def get_license_consent_form_info(self, request: GetLicenseConsentFormInfoRequest = None) -> LicenseConsentFormInfo:
    r"""
    Args:
      request (GetLicenseConsentFormInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLicenseConsentFormInfoRequest()

    return self._client.call("licenses.LicensesService", "GetLicenseConsentFormInfo", request, LicenseConsentFormInfo)

  def start_license_consent_form_email_verification(self, request: StartLicenseConsentFormEmailVerificationRequest = None):
    r"""
    Args:
      request (StartLicenseConsentFormEmailVerificationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartLicenseConsentFormEmailVerificationRequest()

    self._client.call("licenses.LicensesService", "StartLicenseConsentFormEmailVerification", request, None)
