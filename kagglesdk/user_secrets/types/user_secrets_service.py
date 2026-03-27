import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class UserSecretProviderType(enum.Enum):
  r"""
  UserSecretProviderType values correspond to UserSecretProviderTypes.Id column
  in the db.
  """
  USER_SECRET_PROVIDER_TYPE_UNSPECIFIED = 0
  GOOGLE = 1
  USER = 2
  GITHUB = 3
  DISCORD = 4
  GOOGLE_DRIVE = 5
  GOOGLE_COLAB = 6
  HUGGING_FACE = 7

class UserSecretTargetType(enum.Enum):
  r"""
  UserSecretTargetType values correspond to UserSecretTargetTypes.Id column in
  the db.
  """
  USER_SECRET_TARGET_TYPE_UNSPECIFIED = 0
  BIGQUERY = 1
  GCS = 2
  CLOUD_AI = 3
  AUTO_ML = 4
  """Left AutoMl temporarily for transition (in this order)"""
  DRIVE = 5
  CLOUD_IDENTITY = 8
  """Google groups syncing."""
  COLAB = 9

class UserSecretType(enum.Enum):
  """UserSecretType values correspond to UserSecretType.Id column in the db."""
  USER_SECRET_TYPE_UNSPECIFIED = 0
  REFRESH_TOKEN = 1
  CUSTOM = 2
  ACCESS_TOKEN = 3

class AddSecretKernelAttachmentRequest(KaggleObject):
  r"""
  Adds the association between user secret and a kernel for the logged in user.

  Attributes:
    secret_id (int)
    kernel_id (int)
  """

  def __init__(self):
    self._secret_id = 0
    self._kernel_id = 0
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class CheckGoogleGroupsAccessRequest(KaggleObject):
  r"""
  Attributes:
    test_refresh_token (bool)
  """

  def __init__(self):
    self._test_refresh_token = None
    self._freeze()

  @property
  def test_refresh_token(self) -> bool:
    return self._test_refresh_token or False

  @test_refresh_token.setter
  def test_refresh_token(self, test_refresh_token: Optional[bool]):
    if test_refresh_token is None:
      del self.test_refresh_token
      return
    if not isinstance(test_refresh_token, bool):
      raise TypeError('test_refresh_token must be of type bool')
    self._test_refresh_token = test_refresh_token


class CheckGoogleGroupsAccessResponse(KaggleObject):
  r"""
  Attributes:
    is_successful (bool)
  """

  def __init__(self):
    self._is_successful = False
    self._freeze()

  @property
  def is_successful(self) -> bool:
    return self._is_successful

  @is_successful.setter
  def is_successful(self, is_successful: bool):
    if is_successful is None:
      del self.is_successful
      return
    if not isinstance(is_successful, bool):
      raise TypeError('is_successful must be of type bool')
    self._is_successful = is_successful


class DeleteSecretKernelAttachmentRequest(KaggleObject):
  r"""
  Request to delete a kernel/secret attachment for current user.

  Attributes:
    attachment_id (int)
  """

  def __init__(self):
    self._attachment_id = 0
    self._freeze()

  @property
  def attachment_id(self) -> int:
    return self._attachment_id

  @attachment_id.setter
  def attachment_id(self, attachment_id: int):
    if attachment_id is None:
      del self.attachment_id
      return
    if not isinstance(attachment_id, int):
      raise TypeError('attachment_id must be of type int')
    self._attachment_id = attachment_id


class DeleteUserSecretRequest(KaggleObject):
  r"""
  Request to delete a user secret and kernel attachments for current user.

  Attributes:
    secret_id (int)
  """

  def __init__(self):
    self._secret_id = 0
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id


class DeleteUserSecretResponse(KaggleObject):
  r"""
  Attributes:
    was_attached (bool)
    secret_id (int)
  """

  def __init__(self):
    self._was_attached = False
    self._secret_id = 0
    self._freeze()

  @property
  def was_attached(self) -> bool:
    return self._was_attached

  @was_attached.setter
  def was_attached(self, was_attached: bool):
    if was_attached is None:
      del self.was_attached
      return
    if not isinstance(was_attached, bool):
      raise TypeError('was_attached must be of type bool')
    self._was_attached = was_attached

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id


class ExchangeGcloudAuthorizationCodeRequest(KaggleObject):
  r"""
  Attributes:
    authorization_code (str)
  """

  def __init__(self):
    self._authorization_code = None
    self._freeze()

  @property
  def authorization_code(self) -> str:
    return self._authorization_code or ""

  @authorization_code.setter
  def authorization_code(self, authorization_code: Optional[str]):
    if authorization_code is None:
      del self.authorization_code
      return
    if not isinstance(authorization_code, str):
      raise TypeError('authorization_code must be of type str')
    self._authorization_code = authorization_code


class GetColabAccessInfoRequest(KaggleObject):
  r"""
  Attributes:
    test_refresh_token (bool)
  """

  def __init__(self):
    self._test_refresh_token = None
    self._freeze()

  @property
  def test_refresh_token(self) -> bool:
    return self._test_refresh_token or False

  @test_refresh_token.setter
  def test_refresh_token(self, test_refresh_token: Optional[bool]):
    if test_refresh_token is None:
      del self.test_refresh_token
      return
    if not isinstance(test_refresh_token, bool):
      raise TypeError('test_refresh_token must be of type bool')
    self._test_refresh_token = test_refresh_token


class GetColabAccessInfoResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    secret_label (str)
    secret_type (UserSecretType)
    secret_provider (UserSecretProviderType)
    user_email (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._secret_label = None
    self._secret_type = UserSecretType.USER_SECRET_TYPE_UNSPECIFIED
    self._secret_provider = UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED
    self._user_email = None
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def secret_label(self) -> str:
    return self._secret_label or ""

  @secret_label.setter
  def secret_label(self, secret_label: Optional[str]):
    if secret_label is None:
      del self.secret_label
      return
    if not isinstance(secret_label, str):
      raise TypeError('secret_label must be of type str')
    self._secret_label = secret_label

  @property
  def secret_type(self) -> 'UserSecretType':
    return self._secret_type

  @secret_type.setter
  def secret_type(self, secret_type: 'UserSecretType'):
    if secret_type is None:
      del self.secret_type
      return
    if not isinstance(secret_type, UserSecretType):
      raise TypeError('secret_type must be of type UserSecretType')
    self._secret_type = secret_type

  @property
  def secret_provider(self) -> 'UserSecretProviderType':
    return self._secret_provider

  @secret_provider.setter
  def secret_provider(self, secret_provider: 'UserSecretProviderType'):
    if secret_provider is None:
      del self.secret_provider
      return
    if not isinstance(secret_provider, UserSecretProviderType):
      raise TypeError('secret_provider must be of type UserSecretProviderType')
    self._secret_provider = secret_provider

  @property
  def user_email(self) -> str:
    return self._user_email or ""

  @user_email.setter
  def user_email(self, user_email: Optional[str]):
    if user_email is None:
      del self.user_email
      return
    if not isinstance(user_email, str):
      raise TypeError('user_email must be of type str')
    self._user_email = user_email


class GetDriveAccessInfoRequest(KaggleObject):
  r"""
  Attributes:
    test_refresh_token (bool)
  """

  def __init__(self):
    self._test_refresh_token = None
    self._freeze()

  @property
  def test_refresh_token(self) -> bool:
    return self._test_refresh_token or False

  @test_refresh_token.setter
  def test_refresh_token(self, test_refresh_token: Optional[bool]):
    if test_refresh_token is None:
      del self.test_refresh_token
      return
    if not isinstance(test_refresh_token, bool):
      raise TypeError('test_refresh_token must be of type bool')
    self._test_refresh_token = test_refresh_token


class GetDriveAccessInfoResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    secret_label (str)
    secret_type (UserSecretType)
    secret_provider (UserSecretProviderType)
    user_display_name (str)
    user_profile_image (str)
    user_email (str)
    scopes (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._secret_label = None
    self._secret_type = UserSecretType.USER_SECRET_TYPE_UNSPECIFIED
    self._secret_provider = UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED
    self._user_display_name = None
    self._user_profile_image = None
    self._user_email = None
    self._scopes = []
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def secret_label(self) -> str:
    return self._secret_label or ""

  @secret_label.setter
  def secret_label(self, secret_label: Optional[str]):
    if secret_label is None:
      del self.secret_label
      return
    if not isinstance(secret_label, str):
      raise TypeError('secret_label must be of type str')
    self._secret_label = secret_label

  @property
  def secret_type(self) -> 'UserSecretType':
    return self._secret_type

  @secret_type.setter
  def secret_type(self, secret_type: 'UserSecretType'):
    if secret_type is None:
      del self.secret_type
      return
    if not isinstance(secret_type, UserSecretType):
      raise TypeError('secret_type must be of type UserSecretType')
    self._secret_type = secret_type

  @property
  def secret_provider(self) -> 'UserSecretProviderType':
    return self._secret_provider

  @secret_provider.setter
  def secret_provider(self, secret_provider: 'UserSecretProviderType'):
    if secret_provider is None:
      del self.secret_provider
      return
    if not isinstance(secret_provider, UserSecretProviderType):
      raise TypeError('secret_provider must be of type UserSecretProviderType')
    self._secret_provider = secret_provider

  @property
  def user_display_name(self) -> str:
    return self._user_display_name or ""

  @user_display_name.setter
  def user_display_name(self, user_display_name: Optional[str]):
    if user_display_name is None:
      del self.user_display_name
      return
    if not isinstance(user_display_name, str):
      raise TypeError('user_display_name must be of type str')
    self._user_display_name = user_display_name

  @property
  def user_profile_image(self) -> str:
    return self._user_profile_image or ""

  @user_profile_image.setter
  def user_profile_image(self, user_profile_image: Optional[str]):
    if user_profile_image is None:
      del self.user_profile_image
      return
    if not isinstance(user_profile_image, str):
      raise TypeError('user_profile_image must be of type str')
    self._user_profile_image = user_profile_image

  @property
  def user_email(self) -> str:
    return self._user_email or ""

  @user_email.setter
  def user_email(self, user_email: Optional[str]):
    if user_email is None:
      del self.user_email
      return
    if not isinstance(user_email, str):
      raise TypeError('user_email must be of type str')
    self._user_email = user_email

  @property
  def scopes(self) -> Optional[List[str]]:
    return self._scopes

  @scopes.setter
  def scopes(self, scopes: Optional[List[str]]):
    if scopes is None:
      del self.scopes
      return
    if not isinstance(scopes, list):
      raise TypeError('scopes must be of type list')
    if not all([isinstance(t, str) for t in scopes]):
      raise TypeError('scopes must contain only items of type str')
    self._scopes = scopes


class GetGitHubAccessInfoRequest(KaggleObject):
  r"""
  """

  pass

class GetGitHubAccessInfoResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    login (str)
      The user's associated GitHub account's login.
    email (str)
    avatar_url (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._login = None
    self._email = None
    self._avatar_url = None
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def login(self) -> str:
    """The user's associated GitHub account's login."""
    return self._login or ""

  @login.setter
  def login(self, login: Optional[str]):
    if login is None:
      del self.login
      return
    if not isinstance(login, str):
      raise TypeError('login must be of type str')
    self._login = login

  @property
  def email(self) -> str:
    return self._email or ""

  @email.setter
  def email(self, email: Optional[str]):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email

  @property
  def avatar_url(self) -> str:
    return self._avatar_url or ""

  @avatar_url.setter
  def avatar_url(self, avatar_url: Optional[str]):
    if avatar_url is None:
      del self.avatar_url
      return
    if not isinstance(avatar_url, str):
      raise TypeError('avatar_url must be of type str')
    self._avatar_url = avatar_url


class GetHuggingFaceAccessInfoRequest(KaggleObject):
  r"""
  """

  pass

class GetHuggingFaceAccessInfoResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    has_access (bool)
    user_display_name (str)
    user_email (str)
    user_profile_image (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._has_access = None
    self._user_display_name = ""
    self._user_email = ""
    self._user_profile_image = ""
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def has_access(self) -> bool:
    return self._has_access or False

  @has_access.setter
  def has_access(self, has_access: Optional[bool]):
    if has_access is None:
      del self.has_access
      return
    if not isinstance(has_access, bool):
      raise TypeError('has_access must be of type bool')
    self._has_access = has_access

  @property
  def user_display_name(self) -> str:
    return self._user_display_name

  @user_display_name.setter
  def user_display_name(self, user_display_name: str):
    if user_display_name is None:
      del self.user_display_name
      return
    if not isinstance(user_display_name, str):
      raise TypeError('user_display_name must be of type str')
    self._user_display_name = user_display_name

  @property
  def user_email(self) -> str:
    return self._user_email

  @user_email.setter
  def user_email(self, user_email: str):
    if user_email is None:
      del self.user_email
      return
    if not isinstance(user_email, str):
      raise TypeError('user_email must be of type str')
    self._user_email = user_email

  @property
  def user_profile_image(self) -> str:
    return self._user_profile_image

  @user_profile_image.setter
  def user_profile_image(self, user_profile_image: str):
    if user_profile_image is None:
      del self.user_profile_image
      return
    if not isinstance(user_profile_image, str):
      raise TypeError('user_profile_image must be of type str')
    self._user_profile_image = user_profile_image


class GetUserSecretByLabelRequest(KaggleObject):
  r"""
  Requests user secret with given Label for the current user.

  Attributes:
    label (str)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
  """

  def __init__(self):
    self._label = None
    self._freeze()

  @property
  def label(self) -> str:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._label or None

  @label.setter
  def label(self, label: Optional[str]):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label


class GetUserSecretResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    secret (str)
    expires_in_seconds (int)
    secret_type (UserSecretType)
    secret_provider (UserSecretProviderType)
    secret_targets (UserSecretTargetType)
    scopes (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._secret = None
    self._expires_in_seconds = 0
    self._secret_type = UserSecretType.USER_SECRET_TYPE_UNSPECIFIED
    self._secret_provider = UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED
    self._secret_targets = []
    self._scopes = []
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def secret(self) -> str:
    return self._secret or ""

  @secret.setter
  def secret(self, secret: Optional[str]):
    if secret is None:
      del self.secret
      return
    if not isinstance(secret, str):
      raise TypeError('secret must be of type str')
    self._secret = secret

  @property
  def expires_in_seconds(self) -> int:
    return self._expires_in_seconds

  @expires_in_seconds.setter
  def expires_in_seconds(self, expires_in_seconds: int):
    if expires_in_seconds is None:
      del self.expires_in_seconds
      return
    if not isinstance(expires_in_seconds, int):
      raise TypeError('expires_in_seconds must be of type int')
    self._expires_in_seconds = expires_in_seconds

  @property
  def secret_type(self) -> 'UserSecretType':
    return self._secret_type

  @secret_type.setter
  def secret_type(self, secret_type: 'UserSecretType'):
    if secret_type is None:
      del self.secret_type
      return
    if not isinstance(secret_type, UserSecretType):
      raise TypeError('secret_type must be of type UserSecretType')
    self._secret_type = secret_type

  @property
  def secret_provider(self) -> 'UserSecretProviderType':
    return self._secret_provider

  @secret_provider.setter
  def secret_provider(self, secret_provider: 'UserSecretProviderType'):
    if secret_provider is None:
      del self.secret_provider
      return
    if not isinstance(secret_provider, UserSecretProviderType):
      raise TypeError('secret_provider must be of type UserSecretProviderType')
    self._secret_provider = secret_provider

  @property
  def secret_targets(self) -> Optional[List['UserSecretTargetType']]:
    return self._secret_targets

  @secret_targets.setter
  def secret_targets(self, secret_targets: Optional[List['UserSecretTargetType']]):
    if secret_targets is None:
      del self.secret_targets
      return
    if not isinstance(secret_targets, list):
      raise TypeError('secret_targets must be of type list')
    if not all([isinstance(t, UserSecretTargetType) for t in secret_targets]):
      raise TypeError('secret_targets must contain only items of type UserSecretTargetType')
    self._secret_targets = secret_targets

  @property
  def scopes(self) -> Optional[List[str]]:
    return self._scopes

  @scopes.setter
  def scopes(self, scopes: Optional[List[str]]):
    if scopes is None:
      del self.scopes
      return
    if not isinstance(scopes, list):
      raise TypeError('scopes must be of type list')
    if not all([isinstance(t, str) for t in scopes]):
      raise TypeError('scopes must contain only items of type str')
    self._scopes = scopes


class ListKernelSecretsMetadataRequest(KaggleObject):
  r"""
  Requests a list of secrets' metadata for the currently logged in user, and a
  kernel id.

  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class ListKernelSecretsMetadataResponse(KaggleObject):
  r"""
  Attributes:
    kernel_secrets_metadata (UserSecretKernelAttachmentMetadata)
  """

  def __init__(self):
    self._kernel_secrets_metadata = []
    self._freeze()

  @property
  def kernel_secrets_metadata(self) -> Optional[List[Optional['UserSecretKernelAttachmentMetadata']]]:
    return self._kernel_secrets_metadata

  @kernel_secrets_metadata.setter
  def kernel_secrets_metadata(self, kernel_secrets_metadata: Optional[List[Optional['UserSecretKernelAttachmentMetadata']]]):
    if kernel_secrets_metadata is None:
      del self.kernel_secrets_metadata
      return
    if not isinstance(kernel_secrets_metadata, list):
      raise TypeError('kernel_secrets_metadata must be of type list')
    if not all([isinstance(t, UserSecretKernelAttachmentMetadata) for t in kernel_secrets_metadata]):
      raise TypeError('kernel_secrets_metadata must contain only items of type UserSecretKernelAttachmentMetadata')
    self._kernel_secrets_metadata = kernel_secrets_metadata


class ListKernelsWithSecretRequest(KaggleObject):
  r"""
  Request to retrieve kernel ids associated with a particular secret id and
  currently logged in user.

  Attributes:
    secret_id (int)
  """

  def __init__(self):
    self._secret_id = 0
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id


class ListKernelsWithSecretResponse(KaggleObject):
  r"""
  Attributes:
    kernels_with_secret (int)
  """

  def __init__(self):
    self._kernels_with_secret = []
    self._freeze()

  @property
  def kernels_with_secret(self) -> Optional[List[int]]:
    return self._kernels_with_secret

  @kernels_with_secret.setter
  def kernels_with_secret(self, kernels_with_secret: Optional[List[int]]):
    if kernels_with_secret is None:
      del self.kernels_with_secret
      return
    if not isinstance(kernels_with_secret, list):
      raise TypeError('kernels_with_secret must be of type list')
    if not all([isinstance(t, int) for t in kernels_with_secret]):
      raise TypeError('kernels_with_secret must contain only items of type int')
    self._kernels_with_secret = kernels_with_secret


class ListUserSecretsMetadataRequest(KaggleObject):
  r"""
  Requests secret metadata for the logged in user.

  Attributes:
    target (UserSecretTargetType)
      The request is always for the current user, so we don't pass user id.
      Exactly one of these parameters must be provided.
    provider (UserSecretProviderType)
  """

  def __init__(self):
    self._target = None
    self._provider = None
    self._freeze()

  @property
  def target(self) -> 'UserSecretTargetType':
    r"""
    The request is always for the current user, so we don't pass user id.
    Exactly one of these parameters must be provided.
    """
    return self._target or UserSecretTargetType.USER_SECRET_TARGET_TYPE_UNSPECIFIED

  @target.setter
  def target(self, target: Optional['UserSecretTargetType']):
    if target is None:
      del self.target
      return
    if not isinstance(target, UserSecretTargetType):
      raise TypeError('target must be of type UserSecretTargetType')
    self._target = target

  @property
  def provider(self) -> 'UserSecretProviderType':
    return self._provider or UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED

  @provider.setter
  def provider(self, provider: Optional['UserSecretProviderType']):
    if provider is None:
      del self.provider
      return
    if not isinstance(provider, UserSecretProviderType):
      raise TypeError('provider must be of type UserSecretProviderType')
    self._provider = provider


class ListUserSecretsMetadataResponse(KaggleObject):
  r"""
  Attributes:
    user_secrets_metadata (UserSecretMetadata)
  """

  def __init__(self):
    self._user_secrets_metadata = []
    self._freeze()

  @property
  def user_secrets_metadata(self) -> Optional[List[Optional['UserSecretMetadata']]]:
    return self._user_secrets_metadata

  @user_secrets_metadata.setter
  def user_secrets_metadata(self, user_secrets_metadata: Optional[List[Optional['UserSecretMetadata']]]):
    if user_secrets_metadata is None:
      del self.user_secrets_metadata
      return
    if not isinstance(user_secrets_metadata, list):
      raise TypeError('user_secrets_metadata must be of type list')
    if not all([isinstance(t, UserSecretMetadata) for t in user_secrets_metadata]):
      raise TypeError('user_secrets_metadata must contain only items of type UserSecretMetadata')
    self._user_secrets_metadata = user_secrets_metadata


class UpsertCustomUserSecretRequest(KaggleObject):
  r"""
  Attributes:
    secret (str)
      The request is always for the current user,
      so we don't pass user id.
    secret_label (str)
  """

  def __init__(self):
    self._secret = None
    self._secret_label = None
    self._freeze()

  @property
  def secret(self) -> str:
    r"""
    The request is always for the current user,
    so we don't pass user id.
    """
    return self._secret or ""

  @secret.setter
  def secret(self, secret: Optional[str]):
    if secret is None:
      del self.secret
      return
    if not isinstance(secret, str):
      raise TypeError('secret must be of type str')
    self._secret = secret

  @property
  def secret_label(self) -> str:
    return self._secret_label or ""

  @secret_label.setter
  def secret_label(self, secret_label: Optional[str]):
    if secret_label is None:
      del self.secret_label
      return
    if not isinstance(secret_label, str):
      raise TypeError('secret_label must be of type str')
    self._secret_label = secret_label


class UserSecretKernelAttachmentMetadata(KaggleObject):
  r"""
  Attributes:
    attachment_id (int)
    secret_id (int)
    secret_type (UserSecretType)
    secret_provider (UserSecretProviderType)
    secret_targets (UserSecretTargetType)
  """

  def __init__(self):
    self._attachment_id = 0
    self._secret_id = 0
    self._secret_type = UserSecretType.USER_SECRET_TYPE_UNSPECIFIED
    self._secret_provider = UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED
    self._secret_targets = []
    self._freeze()

  @property
  def attachment_id(self) -> int:
    return self._attachment_id

  @attachment_id.setter
  def attachment_id(self, attachment_id: int):
    if attachment_id is None:
      del self.attachment_id
      return
    if not isinstance(attachment_id, int):
      raise TypeError('attachment_id must be of type int')
    self._attachment_id = attachment_id

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def secret_type(self) -> 'UserSecretType':
    return self._secret_type

  @secret_type.setter
  def secret_type(self, secret_type: 'UserSecretType'):
    if secret_type is None:
      del self.secret_type
      return
    if not isinstance(secret_type, UserSecretType):
      raise TypeError('secret_type must be of type UserSecretType')
    self._secret_type = secret_type

  @property
  def secret_provider(self) -> 'UserSecretProviderType':
    return self._secret_provider

  @secret_provider.setter
  def secret_provider(self, secret_provider: 'UserSecretProviderType'):
    if secret_provider is None:
      del self.secret_provider
      return
    if not isinstance(secret_provider, UserSecretProviderType):
      raise TypeError('secret_provider must be of type UserSecretProviderType')
    self._secret_provider = secret_provider

  @property
  def secret_targets(self) -> Optional[List['UserSecretTargetType']]:
    return self._secret_targets

  @secret_targets.setter
  def secret_targets(self, secret_targets: Optional[List['UserSecretTargetType']]):
    if secret_targets is None:
      del self.secret_targets
      return
    if not isinstance(secret_targets, list):
      raise TypeError('secret_targets must be of type list')
    if not all([isinstance(t, UserSecretTargetType) for t in secret_targets]):
      raise TypeError('secret_targets must contain only items of type UserSecretTargetType')
    self._secret_targets = secret_targets


class UserSecretMetadata(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
    secret_label (str)
    secret_type (UserSecretType)
    secret_provider (UserSecretProviderType)
    secret_targets (UserSecretTargetType)
    open_id_connect_subject (str)
    user_display_name (str)
    user_profile_image (str)
    user_email (str)
    scopes (str)
  """

  def __init__(self):
    self._secret_id = 0
    self._secret_label = None
    self._secret_type = UserSecretType.USER_SECRET_TYPE_UNSPECIFIED
    self._secret_provider = UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED
    self._secret_targets = []
    self._open_id_connect_subject = None
    self._user_display_name = None
    self._user_profile_image = None
    self._user_email = None
    self._scopes = []
    self._freeze()

  @property
  def secret_id(self) -> int:
    return self._secret_id

  @secret_id.setter
  def secret_id(self, secret_id: int):
    if secret_id is None:
      del self.secret_id
      return
    if not isinstance(secret_id, int):
      raise TypeError('secret_id must be of type int')
    self._secret_id = secret_id

  @property
  def secret_label(self) -> str:
    return self._secret_label or ""

  @secret_label.setter
  def secret_label(self, secret_label: Optional[str]):
    if secret_label is None:
      del self.secret_label
      return
    if not isinstance(secret_label, str):
      raise TypeError('secret_label must be of type str')
    self._secret_label = secret_label

  @property
  def secret_type(self) -> 'UserSecretType':
    return self._secret_type

  @secret_type.setter
  def secret_type(self, secret_type: 'UserSecretType'):
    if secret_type is None:
      del self.secret_type
      return
    if not isinstance(secret_type, UserSecretType):
      raise TypeError('secret_type must be of type UserSecretType')
    self._secret_type = secret_type

  @property
  def secret_provider(self) -> 'UserSecretProviderType':
    return self._secret_provider

  @secret_provider.setter
  def secret_provider(self, secret_provider: 'UserSecretProviderType'):
    if secret_provider is None:
      del self.secret_provider
      return
    if not isinstance(secret_provider, UserSecretProviderType):
      raise TypeError('secret_provider must be of type UserSecretProviderType')
    self._secret_provider = secret_provider

  @property
  def secret_targets(self) -> Optional[List['UserSecretTargetType']]:
    return self._secret_targets

  @secret_targets.setter
  def secret_targets(self, secret_targets: Optional[List['UserSecretTargetType']]):
    if secret_targets is None:
      del self.secret_targets
      return
    if not isinstance(secret_targets, list):
      raise TypeError('secret_targets must be of type list')
    if not all([isinstance(t, UserSecretTargetType) for t in secret_targets]):
      raise TypeError('secret_targets must contain only items of type UserSecretTargetType')
    self._secret_targets = secret_targets

  @property
  def open_id_connect_subject(self) -> str:
    return self._open_id_connect_subject or ""

  @open_id_connect_subject.setter
  def open_id_connect_subject(self, open_id_connect_subject: Optional[str]):
    if open_id_connect_subject is None:
      del self.open_id_connect_subject
      return
    if not isinstance(open_id_connect_subject, str):
      raise TypeError('open_id_connect_subject must be of type str')
    self._open_id_connect_subject = open_id_connect_subject

  @property
  def user_display_name(self) -> str:
    return self._user_display_name or ""

  @user_display_name.setter
  def user_display_name(self, user_display_name: Optional[str]):
    if user_display_name is None:
      del self.user_display_name
      return
    if not isinstance(user_display_name, str):
      raise TypeError('user_display_name must be of type str')
    self._user_display_name = user_display_name

  @property
  def user_profile_image(self) -> str:
    return self._user_profile_image or ""

  @user_profile_image.setter
  def user_profile_image(self, user_profile_image: Optional[str]):
    if user_profile_image is None:
      del self.user_profile_image
      return
    if not isinstance(user_profile_image, str):
      raise TypeError('user_profile_image must be of type str')
    self._user_profile_image = user_profile_image

  @property
  def user_email(self) -> str:
    return self._user_email or ""

  @user_email.setter
  def user_email(self, user_email: Optional[str]):
    if user_email is None:
      del self.user_email
      return
    if not isinstance(user_email, str):
      raise TypeError('user_email must be of type str')
    self._user_email = user_email

  @property
  def scopes(self) -> Optional[List[str]]:
    return self._scopes

  @scopes.setter
  def scopes(self, scopes: Optional[List[str]]):
    if scopes is None:
      del self.scopes
      return
    if not isinstance(scopes, list):
      raise TypeError('scopes must be of type list')
    if not all([isinstance(t, str) for t in scopes]):
      raise TypeError('scopes must contain only items of type str')
    self._scopes = scopes


AddSecretKernelAttachmentRequest._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

CheckGoogleGroupsAccessRequest._fields = [
  FieldMetadata("testRefreshToken", "test_refresh_token", "_test_refresh_token", bool, None, PredefinedSerializer(), optional=True),
]

CheckGoogleGroupsAccessResponse._fields = [
  FieldMetadata("isSuccessful", "is_successful", "_is_successful", bool, False, PredefinedSerializer()),
]

DeleteSecretKernelAttachmentRequest._fields = [
  FieldMetadata("attachmentId", "attachment_id", "_attachment_id", int, 0, PredefinedSerializer()),
]

DeleteUserSecretRequest._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
]

DeleteUserSecretResponse._fields = [
  FieldMetadata("wasAttached", "was_attached", "_was_attached", bool, False, PredefinedSerializer()),
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
]

ExchangeGcloudAuthorizationCodeRequest._fields = [
  FieldMetadata("authorizationCode", "authorization_code", "_authorization_code", str, None, PredefinedSerializer(), optional=True),
]

GetColabAccessInfoRequest._fields = [
  FieldMetadata("testRefreshToken", "test_refresh_token", "_test_refresh_token", bool, None, PredefinedSerializer(), optional=True),
]

GetColabAccessInfoResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secretLabel", "secret_label", "_secret_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secretType", "secret_type", "_secret_type", UserSecretType, UserSecretType.USER_SECRET_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretProvider", "secret_provider", "_secret_provider", UserSecretProviderType, UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userEmail", "user_email", "_user_email", str, None, PredefinedSerializer(), optional=True),
]

GetDriveAccessInfoRequest._fields = [
  FieldMetadata("testRefreshToken", "test_refresh_token", "_test_refresh_token", bool, None, PredefinedSerializer(), optional=True),
]

GetDriveAccessInfoResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secretLabel", "secret_label", "_secret_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secretType", "secret_type", "_secret_type", UserSecretType, UserSecretType.USER_SECRET_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretProvider", "secret_provider", "_secret_provider", UserSecretProviderType, UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userProfileImage", "user_profile_image", "_user_profile_image", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userEmail", "user_email", "_user_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scopes", "scopes", "_scopes", str, [], ListSerializer(PredefinedSerializer())),
]

GetGitHubAccessInfoRequest._fields = []

GetGitHubAccessInfoResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("login", "login", "_login", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("avatarUrl", "avatar_url", "_avatar_url", str, None, PredefinedSerializer(), optional=True),
]

GetHuggingFaceAccessInfoRequest._fields = []

GetHuggingFaceAccessInfoResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hasAccess", "has_access", "_has_access", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("userEmail", "user_email", "_user_email", str, "", PredefinedSerializer()),
  FieldMetadata("userProfileImage", "user_profile_image", "_user_profile_image", str, "", PredefinedSerializer()),
]

GetUserSecretByLabelRequest._fields = [
  FieldMetadata("label", "label", "_label", str, None, PredefinedSerializer(), optional=True),
]

GetUserSecretResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secret", "secret", "_secret", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("expiresInSeconds", "expires_in_seconds", "_expires_in_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("secretType", "secret_type", "_secret_type", UserSecretType, UserSecretType.USER_SECRET_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretProvider", "secret_provider", "_secret_provider", UserSecretProviderType, UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretTargets", "secret_targets", "_secret_targets", UserSecretTargetType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("scopes", "scopes", "_scopes", str, [], ListSerializer(PredefinedSerializer())),
]

ListKernelSecretsMetadataRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

ListKernelSecretsMetadataResponse._fields = [
  FieldMetadata("kernelSecretsMetadata", "kernel_secrets_metadata", "_kernel_secrets_metadata", UserSecretKernelAttachmentMetadata, [], ListSerializer(KaggleObjectSerializer())),
]

ListKernelsWithSecretRequest._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
]

ListKernelsWithSecretResponse._fields = [
  FieldMetadata("kernelsWithSecret", "kernels_with_secret", "_kernels_with_secret", int, [], ListSerializer(PredefinedSerializer())),
]

ListUserSecretsMetadataRequest._fields = [
  FieldMetadata("target", "target", "_target", UserSecretTargetType, None, EnumSerializer(), optional=True),
  FieldMetadata("provider", "provider", "_provider", UserSecretProviderType, None, EnumSerializer(), optional=True),
]

ListUserSecretsMetadataResponse._fields = [
  FieldMetadata("userSecretsMetadata", "user_secrets_metadata", "_user_secrets_metadata", UserSecretMetadata, [], ListSerializer(KaggleObjectSerializer())),
]

UpsertCustomUserSecretRequest._fields = [
  FieldMetadata("secret", "secret", "_secret", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secretLabel", "secret_label", "_secret_label", str, None, PredefinedSerializer(), optional=True),
]

UserSecretKernelAttachmentMetadata._fields = [
  FieldMetadata("attachmentId", "attachment_id", "_attachment_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secretType", "secret_type", "_secret_type", UserSecretType, UserSecretType.USER_SECRET_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretProvider", "secret_provider", "_secret_provider", UserSecretProviderType, UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretTargets", "secret_targets", "_secret_targets", UserSecretTargetType, [], ListSerializer(EnumSerializer())),
]

UserSecretMetadata._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("secretLabel", "secret_label", "_secret_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secretType", "secret_type", "_secret_type", UserSecretType, UserSecretType.USER_SECRET_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretProvider", "secret_provider", "_secret_provider", UserSecretProviderType, UserSecretProviderType.USER_SECRET_PROVIDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("secretTargets", "secret_targets", "_secret_targets", UserSecretTargetType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("openIdConnectSubject", "open_id_connect_subject", "_open_id_connect_subject", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userProfileImage", "user_profile_image", "_user_profile_image", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userEmail", "user_email", "_user_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scopes", "scopes", "_scopes", str, [], ListSerializer(PredefinedSerializer())),
]

