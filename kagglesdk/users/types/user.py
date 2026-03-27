from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_login import UserLogin
from kagglesdk.users.types.users_enums import UserAchievementTier, UserVerificationStatus
from typing import Optional, List

class User(KaggleObject):
  r"""
  Attributes:
    id (int)
    display_name (str)
    email (str)
    edited_email (str)
    edited_email_code (str)
    user_name (str)
    thumbnail_url (str)
    profile_url (str)
    register_date (datetime)
    last_visit_date (datetime)
    status_id (int)
    performance_tier (UserAchievementTier)
    user_logins (UserLogin)
    group_ids (int)
    is_admin (bool)
    is_kaggle_bot (bool)
    can_act (bool)
    can_be_seen (bool)
    thumbnail_name (str)
    is_phone_verified (bool)
    grandfathered_competition_tier (int)
    is_new_user (bool)
    security_stamp (datetime)
    http_accept_language (str)
    identity_verification_status (UserVerificationStatus)
      Only populated if explicitly requested
    phone_verification_status (UserVerificationStatus)
    country_code (str)
    progression_opt_out (bool)
  """

  def __init__(self):
    self._id = None
    self._display_name = None
    self._email = None
    self._edited_email = None
    self._edited_email_code = None
    self._user_name = None
    self._thumbnail_url = None
    self._profile_url = None
    self._register_date = None
    self._last_visit_date = None
    self._status_id = 0
    self._performance_tier = UserAchievementTier.NOVICE
    self._user_logins = []
    self._group_ids = []
    self._is_admin = False
    self._is_kaggle_bot = False
    self._can_act = False
    self._can_be_seen = False
    self._thumbnail_name = None
    self._is_phone_verified = False
    self._grandfathered_competition_tier = None
    self._is_new_user = False
    self._security_stamp = None
    self._http_accept_language = None
    self._identity_verification_status = None
    self._phone_verification_status = None
    self._country_code = None
    self._progression_opt_out = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

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
  def edited_email(self) -> str:
    return self._edited_email or ""

  @edited_email.setter
  def edited_email(self, edited_email: Optional[str]):
    if edited_email is None:
      del self.edited_email
      return
    if not isinstance(edited_email, str):
      raise TypeError('edited_email must be of type str')
    self._edited_email = edited_email

  @property
  def edited_email_code(self) -> str:
    return self._edited_email_code or ""

  @edited_email_code.setter
  def edited_email_code(self, edited_email_code: Optional[str]):
    if edited_email_code is None:
      del self.edited_email_code
      return
    if not isinstance(edited_email_code, str):
      raise TypeError('edited_email_code must be of type str')
    self._edited_email_code = edited_email_code

  @property
  def user_name(self) -> str:
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def profile_url(self) -> str:
    return self._profile_url or ""

  @profile_url.setter
  def profile_url(self, profile_url: Optional[str]):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def register_date(self) -> datetime:
    return self._register_date

  @register_date.setter
  def register_date(self, register_date: datetime):
    if register_date is None:
      del self.register_date
      return
    if not isinstance(register_date, datetime):
      raise TypeError('register_date must be of type datetime')
    self._register_date = register_date

  @property
  def last_visit_date(self) -> datetime:
    return self._last_visit_date

  @last_visit_date.setter
  def last_visit_date(self, last_visit_date: datetime):
    if last_visit_date is None:
      del self.last_visit_date
      return
    if not isinstance(last_visit_date, datetime):
      raise TypeError('last_visit_date must be of type datetime')
    self._last_visit_date = last_visit_date

  @property
  def status_id(self) -> int:
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
  def performance_tier(self) -> 'UserAchievementTier':
    return self._performance_tier

  @performance_tier.setter
  def performance_tier(self, performance_tier: 'UserAchievementTier'):
    if performance_tier is None:
      del self.performance_tier
      return
    if not isinstance(performance_tier, UserAchievementTier):
      raise TypeError('performance_tier must be of type UserAchievementTier')
    self._performance_tier = performance_tier

  @property
  def user_logins(self) -> Optional[List[Optional['UserLogin']]]:
    return self._user_logins

  @user_logins.setter
  def user_logins(self, user_logins: Optional[List[Optional['UserLogin']]]):
    if user_logins is None:
      del self.user_logins
      return
    if not isinstance(user_logins, list):
      raise TypeError('user_logins must be of type list')
    if not all([isinstance(t, UserLogin) for t in user_logins]):
      raise TypeError('user_logins must contain only items of type UserLogin')
    self._user_logins = user_logins

  @property
  def group_ids(self) -> Optional[List[int]]:
    return self._group_ids

  @group_ids.setter
  def group_ids(self, group_ids: Optional[List[int]]):
    if group_ids is None:
      del self.group_ids
      return
    if not isinstance(group_ids, list):
      raise TypeError('group_ids must be of type list')
    if not all([isinstance(t, int) for t in group_ids]):
      raise TypeError('group_ids must contain only items of type int')
    self._group_ids = group_ids

  @property
  def is_admin(self) -> bool:
    return self._is_admin

  @is_admin.setter
  def is_admin(self, is_admin: bool):
    if is_admin is None:
      del self.is_admin
      return
    if not isinstance(is_admin, bool):
      raise TypeError('is_admin must be of type bool')
    self._is_admin = is_admin

  @property
  def is_kaggle_bot(self) -> bool:
    return self._is_kaggle_bot

  @is_kaggle_bot.setter
  def is_kaggle_bot(self, is_kaggle_bot: bool):
    if is_kaggle_bot is None:
      del self.is_kaggle_bot
      return
    if not isinstance(is_kaggle_bot, bool):
      raise TypeError('is_kaggle_bot must be of type bool')
    self._is_kaggle_bot = is_kaggle_bot

  @property
  def can_act(self) -> bool:
    return self._can_act

  @can_act.setter
  def can_act(self, can_act: bool):
    if can_act is None:
      del self.can_act
      return
    if not isinstance(can_act, bool):
      raise TypeError('can_act must be of type bool')
    self._can_act = can_act

  @property
  def can_be_seen(self) -> bool:
    return self._can_be_seen

  @can_be_seen.setter
  def can_be_seen(self, can_be_seen: bool):
    if can_be_seen is None:
      del self.can_be_seen
      return
    if not isinstance(can_be_seen, bool):
      raise TypeError('can_be_seen must be of type bool')
    self._can_be_seen = can_be_seen

  @property
  def thumbnail_name(self) -> str:
    return self._thumbnail_name or ""

  @thumbnail_name.setter
  def thumbnail_name(self, thumbnail_name: Optional[str]):
    if thumbnail_name is None:
      del self.thumbnail_name
      return
    if not isinstance(thumbnail_name, str):
      raise TypeError('thumbnail_name must be of type str')
    self._thumbnail_name = thumbnail_name

  @property
  def is_phone_verified(self) -> bool:
    return self._is_phone_verified

  @is_phone_verified.setter
  def is_phone_verified(self, is_phone_verified: bool):
    if is_phone_verified is None:
      del self.is_phone_verified
      return
    if not isinstance(is_phone_verified, bool):
      raise TypeError('is_phone_verified must be of type bool')
    self._is_phone_verified = is_phone_verified

  @property
  def grandfathered_competition_tier(self) -> int:
    return self._grandfathered_competition_tier or 0

  @grandfathered_competition_tier.setter
  def grandfathered_competition_tier(self, grandfathered_competition_tier: Optional[int]):
    if grandfathered_competition_tier is None:
      del self.grandfathered_competition_tier
      return
    if not isinstance(grandfathered_competition_tier, int):
      raise TypeError('grandfathered_competition_tier must be of type int')
    self._grandfathered_competition_tier = grandfathered_competition_tier

  @property
  def is_new_user(self) -> bool:
    return self._is_new_user

  @is_new_user.setter
  def is_new_user(self, is_new_user: bool):
    if is_new_user is None:
      del self.is_new_user
      return
    if not isinstance(is_new_user, bool):
      raise TypeError('is_new_user must be of type bool')
    self._is_new_user = is_new_user

  @property
  def security_stamp(self) -> datetime:
    return self._security_stamp

  @security_stamp.setter
  def security_stamp(self, security_stamp: datetime):
    if security_stamp is None:
      del self.security_stamp
      return
    if not isinstance(security_stamp, datetime):
      raise TypeError('security_stamp must be of type datetime')
    self._security_stamp = security_stamp

  @property
  def http_accept_language(self) -> str:
    return self._http_accept_language or ""

  @http_accept_language.setter
  def http_accept_language(self, http_accept_language: Optional[str]):
    if http_accept_language is None:
      del self.http_accept_language
      return
    if not isinstance(http_accept_language, str):
      raise TypeError('http_accept_language must be of type str')
    self._http_accept_language = http_accept_language

  @property
  def identity_verification_status(self) -> 'UserVerificationStatus':
    """Only populated if explicitly requested"""
    return self._identity_verification_status or UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED

  @identity_verification_status.setter
  def identity_verification_status(self, identity_verification_status: Optional['UserVerificationStatus']):
    if identity_verification_status is None:
      del self.identity_verification_status
      return
    if not isinstance(identity_verification_status, UserVerificationStatus):
      raise TypeError('identity_verification_status must be of type UserVerificationStatus')
    self._identity_verification_status = identity_verification_status

  @property
  def phone_verification_status(self) -> 'UserVerificationStatus':
    return self._phone_verification_status or UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED

  @phone_verification_status.setter
  def phone_verification_status(self, phone_verification_status: Optional['UserVerificationStatus']):
    if phone_verification_status is None:
      del self.phone_verification_status
      return
    if not isinstance(phone_verification_status, UserVerificationStatus):
      raise TypeError('phone_verification_status must be of type UserVerificationStatus')
    self._phone_verification_status = phone_verification_status

  @property
  def country_code(self) -> str:
    return self._country_code or ""

  @country_code.setter
  def country_code(self, country_code: Optional[str]):
    if country_code is None:
      del self.country_code
      return
    if not isinstance(country_code, str):
      raise TypeError('country_code must be of type str')
    self._country_code = country_code

  @property
  def progression_opt_out(self) -> bool:
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out


User._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("editedEmail", "edited_email", "_edited_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("editedEmailCode", "edited_email_code", "_edited_email_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("registerDate", "register_date", "_register_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastVisitDate", "last_visit_date", "_last_visit_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("statusId", "status_id", "_status_id", int, 0, PredefinedSerializer()),
  FieldMetadata("performanceTier", "performance_tier", "_performance_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("userLogins", "user_logins", "_user_logins", UserLogin, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("groupIds", "group_ids", "_group_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("isAdmin", "is_admin", "_is_admin", bool, False, PredefinedSerializer()),
  FieldMetadata("isKaggleBot", "is_kaggle_bot", "_is_kaggle_bot", bool, False, PredefinedSerializer()),
  FieldMetadata("canAct", "can_act", "_can_act", bool, False, PredefinedSerializer()),
  FieldMetadata("canBeSeen", "can_be_seen", "_can_be_seen", bool, False, PredefinedSerializer()),
  FieldMetadata("thumbnailName", "thumbnail_name", "_thumbnail_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("grandfatheredCompetitionTier", "grandfathered_competition_tier", "_grandfathered_competition_tier", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isNewUser", "is_new_user", "_is_new_user", bool, False, PredefinedSerializer()),
  FieldMetadata("securityStamp", "security_stamp", "_security_stamp", datetime, None, DateTimeSerializer()),
  FieldMetadata("httpAcceptLanguage", "http_accept_language", "_http_accept_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("identityVerificationStatus", "identity_verification_status", "_identity_verification_status", UserVerificationStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("phoneVerificationStatus", "phone_verification_status", "_phone_verification_status", UserVerificationStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("countryCode", "country_code", "_country_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

