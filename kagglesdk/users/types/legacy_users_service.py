from kagglesdk.common.types.common_types import DiskUsageLimits
from kagglesdk.kaggle_object import *
from typing import Optional, List

class AccountDto(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    user_name (str)
    email_address (str)
    edited_email_address (str)
    verify_account_url (str)
    is_sms_verified (bool)
    is_subscribed_to_mailing_list (bool)
    logins (UserLoginDto)
    can_see_api (bool)
    dataset_limits (DiskUsageLimits)
    model_limits (DiskUsageLimits)
    can_redact_persona_account (bool)
  """

  def __init__(self):
    self._user_id = 0
    self._user_name = ""
    self._email_address = ""
    self._edited_email_address = None
    self._verify_account_url = ""
    self._is_sms_verified = False
    self._is_subscribed_to_mailing_list = False
    self._logins = []
    self._can_see_api = False
    self._dataset_limits = None
    self._model_limits = None
    self._can_redact_persona_account = False
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def email_address(self) -> str:
    return self._email_address

  @email_address.setter
  def email_address(self, email_address: str):
    if email_address is None:
      del self.email_address
      return
    if not isinstance(email_address, str):
      raise TypeError('email_address must be of type str')
    self._email_address = email_address

  @property
  def edited_email_address(self) -> str:
    return self._edited_email_address or ""

  @edited_email_address.setter
  def edited_email_address(self, edited_email_address: Optional[str]):
    if edited_email_address is None:
      del self.edited_email_address
      return
    if not isinstance(edited_email_address, str):
      raise TypeError('edited_email_address must be of type str')
    self._edited_email_address = edited_email_address

  @property
  def verify_account_url(self) -> str:
    return self._verify_account_url

  @verify_account_url.setter
  def verify_account_url(self, verify_account_url: str):
    if verify_account_url is None:
      del self.verify_account_url
      return
    if not isinstance(verify_account_url, str):
      raise TypeError('verify_account_url must be of type str')
    self._verify_account_url = verify_account_url

  @property
  def is_sms_verified(self) -> bool:
    return self._is_sms_verified

  @is_sms_verified.setter
  def is_sms_verified(self, is_sms_verified: bool):
    if is_sms_verified is None:
      del self.is_sms_verified
      return
    if not isinstance(is_sms_verified, bool):
      raise TypeError('is_sms_verified must be of type bool')
    self._is_sms_verified = is_sms_verified

  @property
  def is_subscribed_to_mailing_list(self) -> bool:
    return self._is_subscribed_to_mailing_list

  @is_subscribed_to_mailing_list.setter
  def is_subscribed_to_mailing_list(self, is_subscribed_to_mailing_list: bool):
    if is_subscribed_to_mailing_list is None:
      del self.is_subscribed_to_mailing_list
      return
    if not isinstance(is_subscribed_to_mailing_list, bool):
      raise TypeError('is_subscribed_to_mailing_list must be of type bool')
    self._is_subscribed_to_mailing_list = is_subscribed_to_mailing_list

  @property
  def logins(self) -> Optional[List[Optional['UserLoginDto']]]:
    return self._logins

  @logins.setter
  def logins(self, logins: Optional[List[Optional['UserLoginDto']]]):
    if logins is None:
      del self.logins
      return
    if not isinstance(logins, list):
      raise TypeError('logins must be of type list')
    if not all([isinstance(t, UserLoginDto) for t in logins]):
      raise TypeError('logins must contain only items of type UserLoginDto')
    self._logins = logins

  @property
  def can_see_api(self) -> bool:
    return self._can_see_api

  @can_see_api.setter
  def can_see_api(self, can_see_api: bool):
    if can_see_api is None:
      del self.can_see_api
      return
    if not isinstance(can_see_api, bool):
      raise TypeError('can_see_api must be of type bool')
    self._can_see_api = can_see_api

  @property
  def dataset_limits(self) -> Optional['DiskUsageLimits']:
    return self._dataset_limits

  @dataset_limits.setter
  def dataset_limits(self, dataset_limits: Optional['DiskUsageLimits']):
    if dataset_limits is None:
      del self.dataset_limits
      return
    if not isinstance(dataset_limits, DiskUsageLimits):
      raise TypeError('dataset_limits must be of type DiskUsageLimits')
    self._dataset_limits = dataset_limits

  @property
  def model_limits(self) -> Optional['DiskUsageLimits']:
    return self._model_limits

  @model_limits.setter
  def model_limits(self, model_limits: Optional['DiskUsageLimits']):
    if model_limits is None:
      del self.model_limits
      return
    if not isinstance(model_limits, DiskUsageLimits):
      raise TypeError('model_limits must be of type DiskUsageLimits')
    self._model_limits = model_limits

  @property
  def can_redact_persona_account(self) -> bool:
    return self._can_redact_persona_account

  @can_redact_persona_account.setter
  def can_redact_persona_account(self, can_redact_persona_account: bool):
    if can_redact_persona_account is None:
      del self.can_redact_persona_account
      return
    if not isinstance(can_redact_persona_account, bool):
      raise TypeError('can_redact_persona_account must be of type bool')
    self._can_redact_persona_account = can_redact_persona_account


class EmailSignInRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
    password (str)
    return_url (str)
  """

  def __init__(self):
    self._email = ""
    self._password = ""
    self._return_url = ""
    self._freeze()

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
  def password(self) -> str:
    return self._password

  @password.setter
  def password(self, password: str):
    if password is None:
      del self.password
      return
    if not isinstance(password, str):
      raise TypeError('password must be of type str')
    self._password = password

  @property
  def return_url(self) -> str:
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class EmailSignInResponse(KaggleObject):
  r"""
  Attributes:
    redirect_url (str)
      Where the user should be redirect to. Note this is a quirk of a refactor
      from a form submit to client request. Further refactoring should remove
      then need for this legacy call altogether, calling usersClient.signin
      directly.
  """

  def __init__(self):
    self._redirect_url = ""
    self._freeze()

  @property
  def redirect_url(self) -> str:
    r"""
    Where the user should be redirect to. Note this is a quirk of a refactor
    from a form submit to client request. Further refactoring should remove
    then need for this legacy call altogether, calling usersClient.signin
    directly.
    """
    return self._redirect_url

  @redirect_url.setter
  def redirect_url(self, redirect_url: str):
    if redirect_url is None:
      del self.redirect_url
      return
    if not isinstance(redirect_url, str):
      raise TypeError('redirect_url must be of type str')
    self._redirect_url = redirect_url


class LegacyChangePasswordRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    current_password (str)
    new_password (str)
  """

  def __init__(self):
    self._user_name = ""
    self._current_password = ""
    self._new_password = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def current_password(self) -> str:
    return self._current_password

  @current_password.setter
  def current_password(self, current_password: str):
    if current_password is None:
      del self.current_password
      return
    if not isinstance(current_password, str):
      raise TypeError('current_password must be of type str')
    self._current_password = current_password

  @property
  def new_password(self) -> str:
    return self._new_password

  @new_password.setter
  def new_password(self, new_password: str):
    if new_password is None:
      del self.new_password
      return
    if not isinstance(new_password, str):
      raise TypeError('new_password must be of type str')
    self._new_password = new_password


class LegacyDeleteUserLoginRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    user_login_id (int)
  """

  def __init__(self):
    self._user_name = ""
    self._user_login_id = 0
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def user_login_id(self) -> int:
    return self._user_login_id

  @user_login_id.setter
  def user_login_id(self, user_login_id: int):
    if user_login_id is None:
      del self.user_login_id
      return
    if not isinstance(user_login_id, int):
      raise TypeError('user_login_id must be of type int')
    self._user_login_id = user_login_id


class LegacyGetAccountRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class LegacyUpdateAccountEmailAddressRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    email_address (str)
  """

  def __init__(self):
    self._user_name = ""
    self._email_address = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def email_address(self) -> str:
    return self._email_address

  @email_address.setter
  def email_address(self, email_address: str):
    if email_address is None:
      del self.email_address
      return
    if not isinstance(email_address, str):
      raise TypeError('email_address must be of type str')
    self._email_address = email_address


class UserLoginDto(KaggleObject):
  r"""
  Attributes:
    login_id (int)
    login_identifier (str)
    email_from_provider (str)
    login_provider_id (int)
    login_provider_name (str)
  """

  def __init__(self):
    self._login_id = 0
    self._login_identifier = None
    self._email_from_provider = None
    self._login_provider_id = 0
    self._login_provider_name = ""
    self._freeze()

  @property
  def login_id(self) -> int:
    return self._login_id

  @login_id.setter
  def login_id(self, login_id: int):
    if login_id is None:
      del self.login_id
      return
    if not isinstance(login_id, int):
      raise TypeError('login_id must be of type int')
    self._login_id = login_id

  @property
  def login_identifier(self) -> str:
    return self._login_identifier or ""

  @login_identifier.setter
  def login_identifier(self, login_identifier: Optional[str]):
    if login_identifier is None:
      del self.login_identifier
      return
    if not isinstance(login_identifier, str):
      raise TypeError('login_identifier must be of type str')
    self._login_identifier = login_identifier

  @property
  def email_from_provider(self) -> str:
    return self._email_from_provider or ""

  @email_from_provider.setter
  def email_from_provider(self, email_from_provider: Optional[str]):
    if email_from_provider is None:
      del self.email_from_provider
      return
    if not isinstance(email_from_provider, str):
      raise TypeError('email_from_provider must be of type str')
    self._email_from_provider = email_from_provider

  @property
  def login_provider_id(self) -> int:
    return self._login_provider_id

  @login_provider_id.setter
  def login_provider_id(self, login_provider_id: int):
    if login_provider_id is None:
      del self.login_provider_id
      return
    if not isinstance(login_provider_id, int):
      raise TypeError('login_provider_id must be of type int')
    self._login_provider_id = login_provider_id

  @property
  def login_provider_name(self) -> str:
    return self._login_provider_name

  @login_provider_name.setter
  def login_provider_name(self, login_provider_name: str):
    if login_provider_name is None:
      del self.login_provider_name
      return
    if not isinstance(login_provider_name, str):
      raise TypeError('login_provider_name must be of type str')
    self._login_provider_name = login_provider_name


AccountDto._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("emailAddress", "email_address", "_email_address", str, "", PredefinedSerializer()),
  FieldMetadata("editedEmailAddress", "edited_email_address", "_edited_email_address", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verifyAccountUrl", "verify_account_url", "_verify_account_url", str, "", PredefinedSerializer()),
  FieldMetadata("isSmsVerified", "is_sms_verified", "_is_sms_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("isSubscribedToMailingList", "is_subscribed_to_mailing_list", "_is_subscribed_to_mailing_list", bool, False, PredefinedSerializer()),
  FieldMetadata("logins", "logins", "_logins", UserLoginDto, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("canSeeApi", "can_see_api", "_can_see_api", bool, False, PredefinedSerializer()),
  FieldMetadata("datasetLimits", "dataset_limits", "_dataset_limits", DiskUsageLimits, None, KaggleObjectSerializer()),
  FieldMetadata("modelLimits", "model_limits", "_model_limits", DiskUsageLimits, None, KaggleObjectSerializer()),
  FieldMetadata("canRedactPersonaAccount", "can_redact_persona_account", "_can_redact_persona_account", bool, False, PredefinedSerializer()),
]

EmailSignInRequest._fields = [
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("password", "password", "_password", str, "", PredefinedSerializer()),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
]

EmailSignInResponse._fields = [
  FieldMetadata("redirectUrl", "redirect_url", "_redirect_url", str, "", PredefinedSerializer()),
]

LegacyChangePasswordRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("currentPassword", "current_password", "_current_password", str, "", PredefinedSerializer()),
  FieldMetadata("newPassword", "new_password", "_new_password", str, "", PredefinedSerializer()),
]

LegacyDeleteUserLoginRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("userLoginId", "user_login_id", "_user_login_id", int, 0, PredefinedSerializer()),
]

LegacyGetAccountRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

LegacyUpdateAccountEmailAddressRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("emailAddress", "email_address", "_email_address", str, "", PredefinedSerializer()),
]

UserLoginDto._fields = [
  FieldMetadata("loginId", "login_id", "_login_id", int, 0, PredefinedSerializer()),
  FieldMetadata("loginIdentifier", "login_identifier", "_login_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("emailFromProvider", "email_from_provider", "_email_from_provider", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("loginProviderId", "login_provider_id", "_login_provider_id", int, 0, PredefinedSerializer()),
  FieldMetadata("loginProviderName", "login_provider_name", "_login_provider_name", str, "", PredefinedSerializer()),
]

