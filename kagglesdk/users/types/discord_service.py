from kagglesdk.kaggle_object import *
from typing import Optional

class DeleteDiscordInfoRequest(KaggleObject):
  r"""
  """

  pass

class DiscordUserInfo(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The discord user id, used for API calls.
    login (str)
      The full username as it appears on discord (e.g. `mirhagk#0123`, or just
      `mirhagk` for new usernames).
    avatar_url (str)
      The full URL for the user's avatar.
  """

  def __init__(self):
    self._user_id = 0
    self._login = ""
    self._avatar_url = ""
    self._freeze()

  @property
  def user_id(self) -> int:
    """The discord user id, used for API calls."""
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
  def login(self) -> str:
    r"""
    The full username as it appears on discord (e.g. `mirhagk#0123`, or just
    `mirhagk` for new usernames).
    """
    return self._login

  @login.setter
  def login(self, login: str):
    if login is None:
      del self.login
      return
    if not isinstance(login, str):
      raise TypeError('login must be of type str')
    self._login = login

  @property
  def avatar_url(self) -> str:
    """The full URL for the user's avatar."""
    return self._avatar_url

  @avatar_url.setter
  def avatar_url(self, avatar_url: str):
    if avatar_url is None:
      del self.avatar_url
      return
    if not isinstance(avatar_url, str):
      raise TypeError('avatar_url must be of type str')
    self._avatar_url = avatar_url


class GetDiscordInfoRequest(KaggleObject):
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


class GetDiscordInfoResponse(KaggleObject):
  r"""
  Attributes:
    secret_id (int)
      The UserSecret that stores the access token for the user.
    user_info (DiscordUserInfo)
      The user's associated Discord account's login.
  """

  def __init__(self):
    self._secret_id = 0
    self._user_info = None
    self._freeze()

  @property
  def secret_id(self) -> int:
    """The UserSecret that stores the access token for the user."""
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
  def user_info(self) -> Optional['DiscordUserInfo']:
    """The user's associated Discord account's login."""
    return self._user_info

  @user_info.setter
  def user_info(self, user_info: Optional['DiscordUserInfo']):
    if user_info is None:
      del self.user_info
      return
    if not isinstance(user_info, DiscordUserInfo):
      raise TypeError('user_info must be of type DiscordUserInfo')
    self._user_info = user_info


class SyncDiscordUserRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    ignore_non_discord_user (bool)
      If true then user's who aren't linked to discord will just return success.
      False and NotFound will be thrown.
  """

  def __init__(self):
    self._user_id = 0
    self._ignore_non_discord_user = False
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
  def ignore_non_discord_user(self) -> bool:
    r"""
    If true then user's who aren't linked to discord will just return success.
    False and NotFound will be thrown.
    """
    return self._ignore_non_discord_user

  @ignore_non_discord_user.setter
  def ignore_non_discord_user(self, ignore_non_discord_user: bool):
    if ignore_non_discord_user is None:
      del self.ignore_non_discord_user
      return
    if not isinstance(ignore_non_discord_user, bool):
      raise TypeError('ignore_non_discord_user must be of type bool')
    self._ignore_non_discord_user = ignore_non_discord_user


DeleteDiscordInfoRequest._fields = []

DiscordUserInfo._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("login", "login", "_login", str, "", PredefinedSerializer()),
  FieldMetadata("avatarUrl", "avatar_url", "_avatar_url", str, "", PredefinedSerializer()),
]

GetDiscordInfoRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetDiscordInfoResponse._fields = [
  FieldMetadata("secretId", "secret_id", "_secret_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userInfo", "user_info", "_user_info", DiscordUserInfo, None, KaggleObjectSerializer()),
]

SyncDiscordUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ignoreNonDiscordUser", "ignore_non_discord_user", "_ignore_non_discord_user", bool, False, PredefinedSerializer()),
]

