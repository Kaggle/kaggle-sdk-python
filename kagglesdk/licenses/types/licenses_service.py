from kagglesdk.kaggle_object import *
from typing import Optional

class ConsentToUserLicenseAgreementRequest(KaggleObject):
  r"""
  Attributes:
    license_id (int)
      License to set/update user ConsentTime on. User consent to send the license
      agreement to a 3rd-party for review is derived from the existence of the
      ConsentTime field in the UserLicenseAgreements table.
    current_kaggle_user (bool)
      Consent to the license using the currently logged-in Kaggle user.
    verify_token (str)
      Consent to the license using a token from a logged-out (non-Kaggle user)
      flow.
    consent (bool)
      Explicitly affirm consent of the license_id.
    first_name (str)
      First (i.e. given) name of the consenting user.
    last_name (str)
      Last (i.e. family) name of the consenting user.
    opt_in_email_updates (bool)
      Explicitly opt in to email updates related to the licensed subject/item.
    license_revision_number (int)
      If applicable, the revision number of the license the user is interacting
      with.
  """

  def __init__(self):
    self._license_id = 0
    self._current_kaggle_user = None
    self._verify_token = None
    self._consent = None
    self._first_name = None
    self._last_name = None
    self._opt_in_email_updates = None
    self._license_revision_number = None
    self._freeze()

  @property
  def license_id(self) -> int:
    r"""
    License to set/update user ConsentTime on. User consent to send the license
    agreement to a 3rd-party for review is derived from the existence of the
    ConsentTime field in the UserLicenseAgreements table.
    """
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def current_kaggle_user(self) -> bool:
    """Consent to the license using the currently logged-in Kaggle user."""
    return self._current_kaggle_user or False

  @current_kaggle_user.setter
  def current_kaggle_user(self, current_kaggle_user: bool):
    if current_kaggle_user is None:
      del self.current_kaggle_user
      return
    if not isinstance(current_kaggle_user, bool):
      raise TypeError('current_kaggle_user must be of type bool')
    del self.verify_token
    self._current_kaggle_user = current_kaggle_user

  @property
  def verify_token(self) -> str:
    r"""
    Consent to the license using a token from a logged-out (non-Kaggle user)
    flow.
    """
    return self._verify_token or ""

  @verify_token.setter
  def verify_token(self, verify_token: str):
    if verify_token is None:
      del self.verify_token
      return
    if not isinstance(verify_token, str):
      raise TypeError('verify_token must be of type str')
    del self.current_kaggle_user
    self._verify_token = verify_token

  @property
  def consent(self) -> bool:
    """Explicitly affirm consent of the license_id."""
    return self._consent or False

  @consent.setter
  def consent(self, consent: Optional[bool]):
    if consent is None:
      del self.consent
      return
    if not isinstance(consent, bool):
      raise TypeError('consent must be of type bool')
    self._consent = consent

  @property
  def first_name(self) -> str:
    """First (i.e. given) name of the consenting user."""
    return self._first_name or ""

  @first_name.setter
  def first_name(self, first_name: Optional[str]):
    if first_name is None:
      del self.first_name
      return
    if not isinstance(first_name, str):
      raise TypeError('first_name must be of type str')
    self._first_name = first_name

  @property
  def last_name(self) -> str:
    """Last (i.e. family) name of the consenting user."""
    return self._last_name or ""

  @last_name.setter
  def last_name(self, last_name: Optional[str]):
    if last_name is None:
      del self.last_name
      return
    if not isinstance(last_name, str):
      raise TypeError('last_name must be of type str')
    self._last_name = last_name

  @property
  def opt_in_email_updates(self) -> bool:
    """Explicitly opt in to email updates related to the licensed subject/item."""
    return self._opt_in_email_updates or False

  @opt_in_email_updates.setter
  def opt_in_email_updates(self, opt_in_email_updates: Optional[bool]):
    if opt_in_email_updates is None:
      del self.opt_in_email_updates
      return
    if not isinstance(opt_in_email_updates, bool):
      raise TypeError('opt_in_email_updates must be of type bool')
    self._opt_in_email_updates = opt_in_email_updates

  @property
  def license_revision_number(self) -> int:
    r"""
    If applicable, the revision number of the license the user is interacting
    with.
    """
    return self._license_revision_number or 0

  @license_revision_number.setter
  def license_revision_number(self, license_revision_number: Optional[int]):
    if license_revision_number is None:
      del self.license_revision_number
      return
    if not isinstance(license_revision_number, int):
      raise TypeError('license_revision_number must be of type int')
    self._license_revision_number = license_revision_number


class GetLicenseConsentFormInfoRequest(KaggleObject):
  r"""
  Attributes:
    license_id (int)
    current_kaggle_user (bool)
    verify_token (str)
  """

  def __init__(self):
    self._license_id = 0
    self._current_kaggle_user = None
    self._verify_token = None
    self._freeze()

  @property
  def license_id(self) -> int:
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def current_kaggle_user(self) -> bool:
    return self._current_kaggle_user or False

  @current_kaggle_user.setter
  def current_kaggle_user(self, current_kaggle_user: bool):
    if current_kaggle_user is None:
      del self.current_kaggle_user
      return
    if not isinstance(current_kaggle_user, bool):
      raise TypeError('current_kaggle_user must be of type bool')
    del self.verify_token
    self._current_kaggle_user = current_kaggle_user

  @property
  def verify_token(self) -> str:
    return self._verify_token or ""

  @verify_token.setter
  def verify_token(self, verify_token: str):
    if verify_token is None:
      del self.verify_token
      return
    if not isinstance(verify_token, str):
      raise TypeError('verify_token must be of type str')
    del self.current_kaggle_user
    self._verify_token = verify_token


class StartLicenseConsentFormEmailVerificationRequest(KaggleObject):
  r"""
  Attributes:
    license_id (int)
    email (str)
    captcha_token (str)
    model_id (int)
    return_url (str)
      Optional return URL for redirecting after consenting. Must be a
      local/relative URL.
  """

  def __init__(self):
    self._license_id = 0
    self._email = ""
    self._captcha_token = ""
    self._model_id = None
    self._return_url = ""
    self._freeze()

  @property
  def license_id(self) -> int:
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def email(self) -> str:
    return self._email

  @email.setter
  def email(self, email: str):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email

  @property
  def captcha_token(self) -> str:
    return self._captcha_token

  @captcha_token.setter
  def captcha_token(self, captcha_token: str):
    if captcha_token is None:
      del self.captcha_token
      return
    if not isinstance(captcha_token, str):
      raise TypeError('captcha_token must be of type str')
    self._captcha_token = captcha_token

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def return_url(self) -> str:
    r"""
    Optional return URL for redirecting after consenting. Must be a
    local/relative URL.
    """
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


ConsentToUserLicenseAgreementRequest._fields = [
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentKaggleUser", "current_kaggle_user", "_current_kaggle_user", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verifyToken", "verify_token", "_verify_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("consent", "consent", "_consent", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("firstName", "first_name", "_first_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastName", "last_name", "_last_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("optInEmailUpdates", "opt_in_email_updates", "_opt_in_email_updates", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseRevisionNumber", "license_revision_number", "_license_revision_number", int, None, PredefinedSerializer(), optional=True),
]

GetLicenseConsentFormInfoRequest._fields = [
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentKaggleUser", "current_kaggle_user", "_current_kaggle_user", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verifyToken", "verify_token", "_verify_token", str, None, PredefinedSerializer(), optional=True),
]

StartLicenseConsentFormEmailVerificationRequest._fields = [
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("captchaToken", "captcha_token", "_captcha_token", str, "", PredefinedSerializer()),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
]

