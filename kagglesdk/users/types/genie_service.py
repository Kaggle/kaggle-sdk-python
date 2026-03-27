from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import KaggleXRole
from typing import List, Optional

class BulkSetKaggleXRoleRequest(KaggleObject):
  r"""
  Attributes:
    usernames (str)
      Usernames of the users who's status is being set.
    role (KaggleXRole)
      The role to set these users as.
  """

  def __init__(self):
    self._usernames = []
    self._role = KaggleXRole.KAGGLE_X_ROLE_UNSPECIFIED
    self._freeze()

  @property
  def usernames(self) -> Optional[List[str]]:
    """Usernames of the users who's status is being set."""
    return self._usernames

  @usernames.setter
  def usernames(self, usernames: Optional[List[str]]):
    if usernames is None:
      del self.usernames
      return
    if not isinstance(usernames, list):
      raise TypeError('usernames must be of type list')
    if not all([isinstance(t, str) for t in usernames]):
      raise TypeError('usernames must contain only items of type str')
    self._usernames = usernames

  @property
  def role(self) -> 'KaggleXRole':
    """The role to set these users as."""
    return self._role

  @role.setter
  def role(self, role: 'KaggleXRole'):
    if role is None:
      del self.role
      return
    if not isinstance(role, KaggleXRole):
      raise TypeError('role must be of type KaggleXRole')
    self._role = role


class BulkVerifyPhoneRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      List of user ids to verify.
    phone_numbers (str)
      List of corresponding phone numbers to verify.
      Counts need to match, each user_id corresponds to one phone_numer.
    force_verify (bool)
      Whether to verify the phone numbers without checking for users already
      using those phone numbers.
  """

  def __init__(self):
    self._user_ids = []
    self._phone_numbers = []
    self._force_verify = False
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    """List of user ids to verify."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids

  @property
  def phone_numbers(self) -> Optional[List[str]]:
    r"""
    List of corresponding phone numbers to verify.
    Counts need to match, each user_id corresponds to one phone_numer.
    """
    return self._phone_numbers

  @phone_numbers.setter
  def phone_numbers(self, phone_numbers: Optional[List[str]]):
    if phone_numbers is None:
      del self.phone_numbers
      return
    if not isinstance(phone_numbers, list):
      raise TypeError('phone_numbers must be of type list')
    if not all([isinstance(t, str) for t in phone_numbers]):
      raise TypeError('phone_numbers must contain only items of type str')
    self._phone_numbers = phone_numbers

  @property
  def force_verify(self) -> bool:
    r"""
    Whether to verify the phone numbers without checking for users already
    using those phone numbers.
    """
    return self._force_verify

  @force_verify.setter
  def force_verify(self, force_verify: bool):
    if force_verify is None:
      del self.force_verify
      return
    if not isinstance(force_verify, bool):
      raise TypeError('force_verify must be of type bool')
    self._force_verify = force_verify


class CreateKaggleAccountRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User who will be getting a kaggle login.
    password (str)
      Password to use for that kaggle login.
  """

  def __init__(self):
    self._user_id = 0
    self._password = ""
    self._freeze()

  @property
  def user_id(self) -> int:
    """User who will be getting a kaggle login."""
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
  def password(self) -> str:
    """Password to use for that kaggle login."""
    return self._password

  @password.setter
  def password(self, password: str):
    if password is None:
      del self.password
      return
    if not isinstance(password, str):
      raise TypeError('password must be of type str')
    self._password = password


class GetNewPasswordRequest(KaggleObject):
  r"""
  """

  pass

class GetNewPasswordResponse(KaggleObject):
  r"""
  Attributes:
    new_password (str)
      The randomly generated new password.
  """

  def __init__(self):
    self._new_password = ""
    self._freeze()

  @property
  def new_password(self) -> str:
    """The randomly generated new password."""
    return self._new_password

  @new_password.setter
  def new_password(self, new_password: str):
    if new_password is None:
      del self.new_password
      return
    if not isinstance(new_password, str):
      raise TypeError('new_password must be of type str')
    self._new_password = new_password


class GetUserIdByUsernameOrEmailRequest(KaggleObject):
  r"""
  Attributes:
    username (str)
    email (str)
  """

  def __init__(self):
    self._username = ""
    self._email = ""
    self._freeze()

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


class GetUserIdByUsernameOrEmailResponse(KaggleObject):
  r"""
  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = 0
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


class GetUserStatusLogsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User to get status logs of.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """User to get status logs of."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserStatusLogsResponse(KaggleObject):
  r"""
  Attributes:
    user_status_logs (UserStatusLog)
      List of status logs for the user.
  """

  def __init__(self):
    self._user_status_logs = []
    self._freeze()

  @property
  def user_status_logs(self) -> Optional[List[Optional['UserStatusLog']]]:
    """List of status logs for the user."""
    return self._user_status_logs

  @user_status_logs.setter
  def user_status_logs(self, user_status_logs: Optional[List[Optional['UserStatusLog']]]):
    if user_status_logs is None:
      del self.user_status_logs
      return
    if not isinstance(user_status_logs, list):
      raise TypeError('user_status_logs must be of type list')
    if not all([isinstance(t, UserStatusLog) for t in user_status_logs]):
      raise TypeError('user_status_logs must contain only items of type UserStatusLog')
    self._user_status_logs = user_status_logs


class GrantSiteAdminRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user who will be given admin privileges. Must only have a 'google.com'
      or 'kaggle.com' OAuth login.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    r"""
    The user who will be given admin privileges. Must only have a 'google.com'
    or 'kaggle.com' OAuth login.
    """
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class RevokeSiteAdminRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user who's admin privileges will be taken away.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user who's admin privileges will be taken away."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class UnverifyPhoneRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User to unverify.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """User to unverify."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class UserStatusLog(KaggleObject):
  r"""
  Attributes:
    status_id (int)
      Status that the user was changed to.
    log_date (datetime)
      The date the status was changed.
    reason (str)
      The reason the status was changed.
  """

  def __init__(self):
    self._status_id = 0
    self._log_date = None
    self._reason = None
    self._freeze()

  @property
  def status_id(self) -> int:
    """Status that the user was changed to."""
    return self._status_id

  @status_id.setter
  def status_id(self, status_id: int):
    if status_id is None:
      del self.status_id
      return
    if not isinstance(status_id, int):
      raise TypeError('status_id must be of type int')
    self._status_id = status_id

  @property
  def log_date(self) -> datetime:
    """The date the status was changed."""
    return self._log_date

  @log_date.setter
  def log_date(self, log_date: datetime):
    if log_date is None:
      del self.log_date
      return
    if not isinstance(log_date, datetime):
      raise TypeError('log_date must be of type datetime')
    self._log_date = log_date

  @property
  def reason(self) -> str:
    """The reason the status was changed."""
    return self._reason or ""

  @reason.setter
  def reason(self, reason: Optional[str]):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


BulkSetKaggleXRoleRequest._fields = [
  FieldMetadata("usernames", "usernames", "_usernames", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("role", "role", "_role", KaggleXRole, KaggleXRole.KAGGLE_X_ROLE_UNSPECIFIED, EnumSerializer()),
]

BulkVerifyPhoneRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("phoneNumbers", "phone_numbers", "_phone_numbers", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("forceVerify", "force_verify", "_force_verify", bool, False, PredefinedSerializer()),
]

CreateKaggleAccountRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("password", "password", "_password", str, "", PredefinedSerializer()),
]

GetNewPasswordRequest._fields = []

GetNewPasswordResponse._fields = [
  FieldMetadata("newPassword", "new_password", "_new_password", str, "", PredefinedSerializer()),
]

GetUserIdByUsernameOrEmailRequest._fields = [
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
]

GetUserIdByUsernameOrEmailResponse._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserStatusLogsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserStatusLogsResponse._fields = [
  FieldMetadata("userStatusLogs", "user_status_logs", "_user_status_logs", UserStatusLog, [], ListSerializer(KaggleObjectSerializer())),
]

GrantSiteAdminRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

RevokeSiteAdminRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UnverifyPhoneRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UserStatusLog._fields = [
  FieldMetadata("statusId", "status_id", "_status_id", int, 0, PredefinedSerializer()),
  FieldMetadata("logDate", "log_date", "_log_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, None, PredefinedSerializer(), optional=True),
]

