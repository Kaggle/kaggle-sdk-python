from kagglesdk.competitions.types.team import Team
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional

class CompetitionUser(KaggleObject):
  r"""
  Attributes:
    user (UserAvatar)
      The user's avatar
    is_admin (bool)
      Whether the user is a site admin.
    is_host (bool)
      Whether the user is a host for this competition.
    is_phone_verified (bool)
      Whether the user has been phone-verified.
    can_participate (bool)
      Whether the user can participate in this competition.
    can_update (bool)
      Whether the user can update this competition.
    has_accepted_rules (bool)
      Whether the user has accepted the competition rules, if necessary.
      If no rules acceptance is required, will always be 'true'.
    team (Team)
      The user's team for this competition, if present.
    is_sharing_email (bool)
      Whether the user is sharing their email with the host of the competition
    bookmarked (bool)
      Whether the user bookmarked this competition.
    is_judge (bool)
      Whether the user is a judge for this hackathon competition.
  """

  def __init__(self):
    self._user = None
    self._is_admin = False
    self._is_host = False
    self._is_phone_verified = False
    self._can_participate = False
    self._can_update = False
    self._has_accepted_rules = None
    self._team = None
    self._is_sharing_email = None
    self._bookmarked = None
    self._is_judge = False
    self._freeze()

  @property
  def user(self) -> Optional['UserAvatar']:
    """The user's avatar"""
    return self._user

  @user.setter
  def user(self, user: Optional['UserAvatar']):
    if user is None:
      del self.user
      return
    if not isinstance(user, UserAvatar):
      raise TypeError('user must be of type UserAvatar')
    self._user = user

  @property
  def is_admin(self) -> bool:
    """Whether the user is a site admin."""
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
  def is_host(self) -> bool:
    """Whether the user is a host for this competition."""
    return self._is_host

  @is_host.setter
  def is_host(self, is_host: bool):
    if is_host is None:
      del self.is_host
      return
    if not isinstance(is_host, bool):
      raise TypeError('is_host must be of type bool')
    self._is_host = is_host

  @property
  def is_phone_verified(self) -> bool:
    """Whether the user has been phone-verified."""
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
  def can_participate(self) -> bool:
    """Whether the user can participate in this competition."""
    return self._can_participate

  @can_participate.setter
  def can_participate(self, can_participate: bool):
    if can_participate is None:
      del self.can_participate
      return
    if not isinstance(can_participate, bool):
      raise TypeError('can_participate must be of type bool')
    self._can_participate = can_participate

  @property
  def can_update(self) -> bool:
    """Whether the user can update this competition."""
    return self._can_update

  @can_update.setter
  def can_update(self, can_update: bool):
    if can_update is None:
      del self.can_update
      return
    if not isinstance(can_update, bool):
      raise TypeError('can_update must be of type bool')
    self._can_update = can_update

  @property
  def has_accepted_rules(self) -> bool:
    r"""
    Whether the user has accepted the competition rules, if necessary.
    If no rules acceptance is required, will always be 'true'.
    """
    return self._has_accepted_rules or False

  @has_accepted_rules.setter
  def has_accepted_rules(self, has_accepted_rules: Optional[bool]):
    if has_accepted_rules is None:
      del self.has_accepted_rules
      return
    if not isinstance(has_accepted_rules, bool):
      raise TypeError('has_accepted_rules must be of type bool')
    self._has_accepted_rules = has_accepted_rules

  @property
  def team(self) -> Optional['Team']:
    """The user's team for this competition, if present."""
    return self._team or None

  @team.setter
  def team(self, team: Optional[Optional['Team']]):
    if team is None:
      del self.team
      return
    if not isinstance(team, Team):
      raise TypeError('team must be of type Team')
    self._team = team

  @property
  def is_sharing_email(self) -> bool:
    """Whether the user is sharing their email with the host of the competition"""
    return self._is_sharing_email or False

  @is_sharing_email.setter
  def is_sharing_email(self, is_sharing_email: Optional[bool]):
    if is_sharing_email is None:
      del self.is_sharing_email
      return
    if not isinstance(is_sharing_email, bool):
      raise TypeError('is_sharing_email must be of type bool')
    self._is_sharing_email = is_sharing_email

  @property
  def bookmarked(self) -> bool:
    """Whether the user bookmarked this competition."""
    return self._bookmarked or False

  @bookmarked.setter
  def bookmarked(self, bookmarked: Optional[bool]):
    if bookmarked is None:
      del self.bookmarked
      return
    if not isinstance(bookmarked, bool):
      raise TypeError('bookmarked must be of type bool')
    self._bookmarked = bookmarked

  @property
  def is_judge(self) -> bool:
    """Whether the user is a judge for this hackathon competition."""
    return self._is_judge

  @is_judge.setter
  def is_judge(self, is_judge: bool):
    if is_judge is None:
      del self.is_judge
      return
    if not isinstance(is_judge, bool):
      raise TypeError('is_judge must be of type bool')
    self._is_judge = is_judge


CompetitionUser._fields = [
  FieldMetadata("user", "user", "_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("isAdmin", "is_admin", "_is_admin", bool, False, PredefinedSerializer()),
  FieldMetadata("isHost", "is_host", "_is_host", bool, False, PredefinedSerializer()),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("canParticipate", "can_participate", "_can_participate", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpdate", "can_update", "_can_update", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAcceptedRules", "has_accepted_rules", "_has_accepted_rules", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("team", "team", "_team", Team, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("isSharingEmail", "is_sharing_email", "_is_sharing_email", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bookmarked", "bookmarked", "_bookmarked", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isJudge", "is_judge", "_is_judge", bool, False, PredefinedSerializer()),
]

