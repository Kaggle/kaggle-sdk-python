from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class CreateTestAccountRequest(KaggleObject):
  r"""
  Attributes:
    username_prefix (str)
      Prefix for the username (e.g., 'e2e-' -> 'e2e-abc123')
    options (TestAccountOptions)
      Options for configuring the test account
    test_run_id (str)
      Unique ID for this test run, used for grouping accounts for bulk cleanup
  """

  def __init__(self):
    self._username_prefix = ""
    self._options = None
    self._test_run_id = ""
    self._freeze()

  @property
  def username_prefix(self) -> str:
    """Prefix for the username (e.g., 'e2e-' -> 'e2e-abc123')"""
    return self._username_prefix

  @username_prefix.setter
  def username_prefix(self, username_prefix: str):
    if username_prefix is None:
      del self.username_prefix
      return
    if not isinstance(username_prefix, str):
      raise TypeError('username_prefix must be of type str')
    self._username_prefix = username_prefix

  @property
  def options(self) -> Optional['TestAccountOptions']:
    """Options for configuring the test account"""
    return self._options

  @options.setter
  def options(self, options: Optional['TestAccountOptions']):
    if options is None:
      del self.options
      return
    if not isinstance(options, TestAccountOptions):
      raise TypeError('options must be of type TestAccountOptions')
    self._options = options

  @property
  def test_run_id(self) -> str:
    """Unique ID for this test run, used for grouping accounts for bulk cleanup"""
    return self._test_run_id

  @test_run_id.setter
  def test_run_id(self, test_run_id: str):
    if test_run_id is None:
      del self.test_run_id
      return
    if not isinstance(test_run_id, str):
      raise TypeError('test_run_id must be of type str')
    self._test_run_id = test_run_id


class CreateTestAccountResponse(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The ID of the created user
    username (str)
      The username of the created account
    password (str)
      The password to use for logging in (auto-generated)
    email (str)
      The email address of the account
  """

  def __init__(self):
    self._user_id = 0
    self._username = ""
    self._password = ""
    self._email = ""
    self._freeze()

  @property
  def user_id(self) -> int:
    """The ID of the created user"""
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
  def username(self) -> str:
    """The username of the created account"""
    return self._username

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def password(self) -> str:
    """The password to use for logging in (auto-generated)"""
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
  def email(self) -> str:
    """The email address of the account"""
    return self._email

  @email.setter
  def email(self, email: str):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email


class DeleteTestAccountRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user ID to delete
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user ID to delete"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class ListTestAccountsRequest(KaggleObject):
  r"""
  Attributes:
    test_run_id (str)
      Optional: filter to accounts from a specific test run
  """

  def __init__(self):
    self._test_run_id = ""
    self._freeze()

  @property
  def test_run_id(self) -> str:
    """Optional: filter to accounts from a specific test run"""
    return self._test_run_id

  @test_run_id.setter
  def test_run_id(self, test_run_id: str):
    if test_run_id is None:
      del self.test_run_id
      return
    if not isinstance(test_run_id, str):
      raise TypeError('test_run_id must be of type str')
    self._test_run_id = test_run_id


class ListTestAccountsResponse(KaggleObject):
  r"""
  Attributes:
    accounts (TestAccountInfo)
  """

  def __init__(self):
    self._accounts = []
    self._freeze()

  @property
  def accounts(self) -> Optional[List[Optional['TestAccountInfo']]]:
    return self._accounts

  @accounts.setter
  def accounts(self, accounts: Optional[List[Optional['TestAccountInfo']]]):
    if accounts is None:
      del self.accounts
      return
    if not isinstance(accounts, list):
      raise TypeError('accounts must be of type list')
    if not all([isinstance(t, TestAccountInfo) for t in accounts]):
      raise TypeError('accounts must contain only items of type TestAccountInfo')
    self._accounts = accounts


class TestAccountInfo(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    username (str)
    test_run_id (str)
    created_at (datetime)
  """

  def __init__(self):
    self._user_id = 0
    self._username = ""
    self._test_run_id = ""
    self._created_at = None
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
  def username(self) -> str:
    return self._username

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def test_run_id(self) -> str:
    return self._test_run_id

  @test_run_id.setter
  def test_run_id(self, test_run_id: str):
    if test_run_id is None:
      del self.test_run_id
      return
    if not isinstance(test_run_id, str):
      raise TypeError('test_run_id must be of type str')
    self._test_run_id = test_run_id

  @property
  def created_at(self) -> datetime:
    return self._created_at

  @created_at.setter
  def created_at(self, created_at: datetime):
    if created_at is None:
      del self.created_at
      return
    if not isinstance(created_at, datetime):
      raise TypeError('created_at must be of type datetime')
    self._created_at = created_at


class TestAccountOptions(KaggleObject):
  r"""
  Attributes:
    phone_verified (bool)
      Whether the account should have phone verification completed
    identity_verified (bool)
      Whether the account should have identity verification completed
    tier (UserAchievementTier)
      The tier level for this account (defaults to Novice if not specified)
  """

  def __init__(self):
    self._phone_verified = False
    self._identity_verified = False
    self._tier = UserAchievementTier.NOVICE
    self._freeze()

  @property
  def phone_verified(self) -> bool:
    """Whether the account should have phone verification completed"""
    return self._phone_verified

  @phone_verified.setter
  def phone_verified(self, phone_verified: bool):
    if phone_verified is None:
      del self.phone_verified
      return
    if not isinstance(phone_verified, bool):
      raise TypeError('phone_verified must be of type bool')
    self._phone_verified = phone_verified

  @property
  def identity_verified(self) -> bool:
    """Whether the account should have identity verification completed"""
    return self._identity_verified

  @identity_verified.setter
  def identity_verified(self, identity_verified: bool):
    if identity_verified is None:
      del self.identity_verified
      return
    if not isinstance(identity_verified, bool):
      raise TypeError('identity_verified must be of type bool')
    self._identity_verified = identity_verified

  @property
  def tier(self) -> 'UserAchievementTier':
    """The tier level for this account (defaults to Novice if not specified)"""
    return self._tier

  @tier.setter
  def tier(self, tier: 'UserAchievementTier'):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, UserAchievementTier):
      raise TypeError('tier must be of type UserAchievementTier')
    self._tier = tier


CreateTestAccountRequest._fields = [
  FieldMetadata("usernamePrefix", "username_prefix", "_username_prefix", str, "", PredefinedSerializer()),
  FieldMetadata("options", "options", "_options", TestAccountOptions, None, KaggleObjectSerializer()),
  FieldMetadata("testRunId", "test_run_id", "_test_run_id", str, "", PredefinedSerializer()),
]

CreateTestAccountResponse._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
  FieldMetadata("password", "password", "_password", str, "", PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
]

DeleteTestAccountRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

ListTestAccountsRequest._fields = [
  FieldMetadata("testRunId", "test_run_id", "_test_run_id", str, "", PredefinedSerializer()),
]

ListTestAccountsResponse._fields = [
  FieldMetadata("accounts", "accounts", "_accounts", TestAccountInfo, [], ListSerializer(KaggleObjectSerializer())),
]

TestAccountInfo._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
  FieldMetadata("testRunId", "test_run_id", "_test_run_id", str, "", PredefinedSerializer()),
  FieldMetadata("createdAt", "created_at", "_created_at", datetime, None, DateTimeSerializer()),
]

TestAccountOptions._fields = [
  FieldMetadata("phoneVerified", "phone_verified", "_phone_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("identityVerified", "identity_verified", "_identity_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("tier", "tier", "_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
]

