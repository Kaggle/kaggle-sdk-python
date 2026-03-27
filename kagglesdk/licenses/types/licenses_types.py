from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class LicenseUrlPostConsentAction(enum.Enum):
  LICENSE_URL_POST_CONSENT_ACTION_UNSPECIFIED = 0
  LICENSE_URL_POST_CONSENT_ACTION_EXPLORE = 1
  """Encourage user to explore on our site."""
  LICENSE_URL_POST_CONSENT_ACTION_DOWNLOAD = 2
  """Direct the user to download a resource."""

class LicenseUrlSearchParam(enum.Enum):
  """These are used in handling URLs on the frontend and backend:"""
  LICENSE_URL_SEARCH_PARAM_UNSPECIFIED = 0
  LICENSE_URL_SEARCH_PARAM_KAGGLE_LOGIN = 1
  """Did the user explicitly ask to use their Kaggle login?"""
  LICENSE_URL_SEARCH_PARAM_VERIFY_TOKEN = 2
  """Verification token used in logged-out scenarios."""
  LICENSE_URL_SEARCH_PARAM_POST_CONSENT_ACTION = 3
  """What should we do after the user consents to a license agreement?"""
  LICENSE_URL_SEARCH_PARAM_RETURN_URL = 4
  """Where should we redirect the user when they return?"""

class UserLicenseAgreementStatus(enum.Enum):
  r"""
  This enum tracks the state of a user's agreement with respect to any
  license that requires it. For Llama 2, users will consent and after some
  time, Meta will indicate to us that they're approved.
  """
  USER_LICENSE_AGREEMENT_STATUS_UNSPECIFIED = 0
  """Default, unspecified."""
  USER_LICENSE_AGREEMENT_STATUS_PENDING = 1
  r"""
  Users in this status are waiting for review from the 3rd-party. Users in
  any specified status implicitly have consented to this review. The presence
  of a ConsentTime value in the UserLicenseAgreements table explicitly
  denotes if and when the user consented.
  """
  USER_LICENSE_AGREEMENT_STATUS_ACCEPTED = 2
  """3rd-party has approved the user's license agreement."""
  USER_LICENSE_AGREEMENT_STATUS_REJECTED = 3
  """3rd-party has rejected the user's license agreement."""
  USER_LICENSE_AGREEMENT_STATUS_EXPIRED = 4
  r"""
  Too much time has passed from when the user submitted the consent form and
  the license owner reviewed it
  """

class LicenseConsentFormMethod(enum.Enum):
  LICENSE_CONSENT_FORM_METHOD_UNSPECIFIED = 0
  LICENSE_CONSENT_FORM_METHOD_KAGGLE = 1
  """Logged-in Kaggle use."""
  LICENSE_CONSENT_FORM_METHOD_GOOGLE = 2
  """Google SSO/OAuth."""
  LICENSE_CONSENT_FORM_METHOD_HUGGING_FACE = 3
  """Hugging Face OAuth."""
  LICENSE_CONSENT_FORM_METHOD_EMAIL = 4
  """Verified email."""

class License(KaggleObject):
  r"""
  This proto is a subset of LicenseOption representing the currently selected
  License. It excludes any metadata needed to organize a selection of options
  (like display_sequence, etc.)

  Attributes:
    id (int)
    name (str)
    url (str)
    agreement_required (bool)
      Indicates whether this license requires agreement to its terms (e.g. Llama
      2, other custom license, etc.)
    agreement_status (UserLicenseAgreementStatus)
      Represents the status of the current user's agreement regarding this
      specific license. Only applicable when requires_agreement is true
    consent_time (datetime)
      If applicable, this is the time when the current user consented to the
      license agreement
    current_revision_number (int)
      If applicable, the current license revision number we want users to be
      accepting.
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._url = None
    self._agreement_required = None
    self._agreement_status = None
    self._consent_time = None
    self._current_revision_number = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def agreement_required(self) -> bool:
    r"""
    Indicates whether this license requires agreement to its terms (e.g. Llama
    2, other custom license, etc.)
    """
    return self._agreement_required or False

  @agreement_required.setter
  def agreement_required(self, agreement_required: Optional[bool]):
    if agreement_required is None:
      del self.agreement_required
      return
    if not isinstance(agreement_required, bool):
      raise TypeError('agreement_required must be of type bool')
    self._agreement_required = agreement_required

  @property
  def agreement_status(self) -> 'UserLicenseAgreementStatus':
    r"""
    Represents the status of the current user's agreement regarding this
    specific license. Only applicable when requires_agreement is true
    """
    return self._agreement_status or UserLicenseAgreementStatus.USER_LICENSE_AGREEMENT_STATUS_UNSPECIFIED

  @agreement_status.setter
  def agreement_status(self, agreement_status: Optional['UserLicenseAgreementStatus']):
    if agreement_status is None:
      del self.agreement_status
      return
    if not isinstance(agreement_status, UserLicenseAgreementStatus):
      raise TypeError('agreement_status must be of type UserLicenseAgreementStatus')
    self._agreement_status = agreement_status

  @property
  def consent_time(self) -> datetime:
    r"""
    If applicable, this is the time when the current user consented to the
    license agreement
    """
    return self._consent_time or None

  @consent_time.setter
  def consent_time(self, consent_time: Optional[datetime]):
    if consent_time is None:
      del self.consent_time
      return
    if not isinstance(consent_time, datetime):
      raise TypeError('consent_time must be of type datetime')
    self._consent_time = consent_time

  @property
  def current_revision_number(self) -> int:
    r"""
    If applicable, the current license revision number we want users to be
    accepting.
    """
    return self._current_revision_number or 0

  @current_revision_number.setter
  def current_revision_number(self, current_revision_number: Optional[int]):
    if current_revision_number is None:
      del self.current_revision_number
      return
    if not isinstance(current_revision_number, int):
      raise TypeError('current_revision_number must be of type int')
    self._current_revision_number = current_revision_number


class LicenseConsentFormInfo(KaggleObject):
  r"""
  Attributes:
    consent_method (LicenseConsentFormMethod)
    first_name (str)
    last_name (str)
    verified_email (str)
    consented (bool)
    send_related_emails (bool)
    consent_time (datetime)
    post_consent_uri (str)
  """

  def __init__(self):
    self._consent_method = LicenseConsentFormMethod.LICENSE_CONSENT_FORM_METHOD_UNSPECIFIED
    self._first_name = ""
    self._last_name = ""
    self._verified_email = ""
    self._consented = None
    self._send_related_emails = None
    self._consent_time = None
    self._post_consent_uri = ""
    self._freeze()

  @property
  def consent_method(self) -> 'LicenseConsentFormMethod':
    return self._consent_method

  @consent_method.setter
  def consent_method(self, consent_method: 'LicenseConsentFormMethod'):
    if consent_method is None:
      del self.consent_method
      return
    if not isinstance(consent_method, LicenseConsentFormMethod):
      raise TypeError('consent_method must be of type LicenseConsentFormMethod')
    self._consent_method = consent_method

  @property
  def first_name(self) -> str:
    return self._first_name

  @first_name.setter
  def first_name(self, first_name: str):
    if first_name is None:
      del self.first_name
      return
    if not isinstance(first_name, str):
      raise TypeError('first_name must be of type str')
    self._first_name = first_name

  @property
  def last_name(self) -> str:
    return self._last_name

  @last_name.setter
  def last_name(self, last_name: str):
    if last_name is None:
      del self.last_name
      return
    if not isinstance(last_name, str):
      raise TypeError('last_name must be of type str')
    self._last_name = last_name

  @property
  def verified_email(self) -> str:
    return self._verified_email

  @verified_email.setter
  def verified_email(self, verified_email: str):
    if verified_email is None:
      del self.verified_email
      return
    if not isinstance(verified_email, str):
      raise TypeError('verified_email must be of type str')
    self._verified_email = verified_email

  @property
  def consented(self) -> bool:
    return self._consented or False

  @consented.setter
  def consented(self, consented: Optional[bool]):
    if consented is None:
      del self.consented
      return
    if not isinstance(consented, bool):
      raise TypeError('consented must be of type bool')
    self._consented = consented

  @property
  def send_related_emails(self) -> bool:
    return self._send_related_emails or False

  @send_related_emails.setter
  def send_related_emails(self, send_related_emails: Optional[bool]):
    if send_related_emails is None:
      del self.send_related_emails
      return
    if not isinstance(send_related_emails, bool):
      raise TypeError('send_related_emails must be of type bool')
    self._send_related_emails = send_related_emails

  @property
  def consent_time(self) -> datetime:
    return self._consent_time or None

  @consent_time.setter
  def consent_time(self, consent_time: Optional[datetime]):
    if consent_time is None:
      del self.consent_time
      return
    if not isinstance(consent_time, datetime):
      raise TypeError('consent_time must be of type datetime')
    self._consent_time = consent_time

  @property
  def post_consent_uri(self) -> str:
    return self._post_consent_uri

  @post_consent_uri.setter
  def post_consent_uri(self, post_consent_uri: str):
    if post_consent_uri is None:
      del self.post_consent_uri
      return
    if not isinstance(post_consent_uri, str):
      raise TypeError('post_consent_uri must be of type str')
    self._post_consent_uri = post_consent_uri


class LicenseGroupDto(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    licenses (LicenseOption)
    display_sequence (int)
  """

  def __init__(self):
    self._id = 0
    self._name = None
    self._licenses = []
    self._display_sequence = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def licenses(self) -> Optional[List[Optional['LicenseOption']]]:
    return self._licenses

  @licenses.setter
  def licenses(self, licenses: Optional[List[Optional['LicenseOption']]]):
    if licenses is None:
      del self.licenses
      return
    if not isinstance(licenses, list):
      raise TypeError('licenses must be of type list')
    if not all([isinstance(t, LicenseOption) for t in licenses]):
      raise TypeError('licenses must contain only items of type LicenseOption')
    self._licenses = licenses

  @property
  def display_sequence(self) -> int:
    return self._display_sequence or 0

  @display_sequence.setter
  def display_sequence(self, display_sequence: Optional[int]):
    if display_sequence is None:
      del self.display_sequence
      return
    if not isinstance(display_sequence, int):
      raise TypeError('display_sequence must be of type int')
    self._display_sequence = display_sequence


class LicenseOption(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    description (str)
    url (str)
    display_sequence (int)
    commercial_use (bool)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._description = ""
    self._url = None
    self._display_sequence = None
    self._commercial_use = False
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def display_sequence(self) -> int:
    return self._display_sequence or 0

  @display_sequence.setter
  def display_sequence(self, display_sequence: Optional[int]):
    if display_sequence is None:
      del self.display_sequence
      return
    if not isinstance(display_sequence, int):
      raise TypeError('display_sequence must be of type int')
    self._display_sequence = display_sequence

  @property
  def commercial_use(self) -> bool:
    return self._commercial_use

  @commercial_use.setter
  def commercial_use(self, commercial_use: bool):
    if commercial_use is None:
      del self.commercial_use
      return
    if not isinstance(commercial_use, bool):
      raise TypeError('commercial_use must be of type bool')
    self._commercial_use = commercial_use


License._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agreementRequired", "agreement_required", "_agreement_required", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agreementStatus", "agreement_status", "_agreement_status", UserLicenseAgreementStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("consentTime", "consent_time", "_consent_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("currentRevisionNumber", "current_revision_number", "_current_revision_number", int, None, PredefinedSerializer(), optional=True),
]

LicenseConsentFormInfo._fields = [
  FieldMetadata("consentMethod", "consent_method", "_consent_method", LicenseConsentFormMethod, LicenseConsentFormMethod.LICENSE_CONSENT_FORM_METHOD_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("firstName", "first_name", "_first_name", str, "", PredefinedSerializer()),
  FieldMetadata("lastName", "last_name", "_last_name", str, "", PredefinedSerializer()),
  FieldMetadata("verifiedEmail", "verified_email", "_verified_email", str, "", PredefinedSerializer()),
  FieldMetadata("consented", "consented", "_consented", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sendRelatedEmails", "send_related_emails", "_send_related_emails", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("consentTime", "consent_time", "_consent_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("postConsentUri", "post_consent_uri", "_post_consent_uri", str, "", PredefinedSerializer()),
]

LicenseGroupDto._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenses", "licenses", "_licenses", LicenseOption, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("displaySequence", "display_sequence", "_display_sequence", int, None, PredefinedSerializer(), optional=True),
]

LicenseOption._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displaySequence", "display_sequence", "_display_sequence", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("commercialUse", "commercial_use", "_commercial_use", bool, False, PredefinedSerializer()),
]

