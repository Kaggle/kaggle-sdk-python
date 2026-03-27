from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.groups_enum import GroupInviteState, GroupMembershipRole, SynchronizedGroupProvider
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import CollaboratorType, UserAchievementTier
from typing import Optional, List

class Collaborator(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    group_id (int)
    group_member_count (int)
    profile_url (str)
    thumbnail_url (str)
    name (str)
    slug (str)
    user_tier (UserAchievementTier)
    join_date (datetime)
    type (CollaboratorType)
    progression_opt_out (bool)
      True if the user is opted out of the progression system.
  """

  def __init__(self):
    self._user_id = None
    self._group_id = None
    self._group_member_count = None
    self._profile_url = ""
    self._thumbnail_url = ""
    self._name = ""
    self._slug = ""
    self._user_tier = UserAchievementTier.NOVICE
    self._join_date = None
    self._type = CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED
    self._progression_opt_out = None
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def group_id(self) -> int:
    return self._group_id or 0

  @group_id.setter
  def group_id(self, group_id: Optional[int]):
    if group_id is None:
      del self.group_id
      return
    if not isinstance(group_id, int):
      raise TypeError('group_id must be of type int')
    self._group_id = group_id

  @property
  def group_member_count(self) -> int:
    return self._group_member_count or 0

  @group_member_count.setter
  def group_member_count(self, group_member_count: Optional[int]):
    if group_member_count is None:
      del self.group_member_count
      return
    if not isinstance(group_member_count, int):
      raise TypeError('group_member_count must be of type int')
    self._group_member_count = group_member_count

  @property
  def profile_url(self) -> str:
    return self._profile_url

  @profile_url.setter
  def profile_url(self, profile_url: str):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

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
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier

  @property
  def join_date(self) -> datetime:
    return self._join_date

  @join_date.setter
  def join_date(self, join_date: datetime):
    if join_date is None:
      del self.join_date
      return
    if not isinstance(join_date, datetime):
      raise TypeError('join_date must be of type datetime')
    self._join_date = join_date

  @property
  def type(self) -> 'CollaboratorType':
    return self._type

  @type.setter
  def type(self, type: 'CollaboratorType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, CollaboratorType):
      raise TypeError('type must be of type CollaboratorType')
    self._type = type

  @property
  def progression_opt_out(self) -> bool:
    """True if the user is opted out of the progression system."""
    return self._progression_opt_out or False

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: Optional[bool]):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out


class CollaboratorList(KaggleObject):
  r"""
  Attributes:
    owner (Collaborator)
    collaborators (Collaborator)
    is_locked (bool)
  """

  def __init__(self):
    self._owner = None
    self._collaborators = []
    self._is_locked = None
    self._freeze()

  @property
  def owner(self) -> Optional['Collaborator']:
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['Collaborator']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Collaborator):
      raise TypeError('owner must be of type Collaborator')
    self._owner = owner

  @property
  def collaborators(self) -> Optional[List[Optional['Collaborator']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['Collaborator']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, Collaborator) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type Collaborator')
    self._collaborators = collaborators

  @property
  def is_locked(self) -> bool:
    return self._is_locked or False

  @is_locked.setter
  def is_locked(self, is_locked: Optional[bool]):
    if is_locked is None:
      del self.is_locked
      return
    if not isinstance(is_locked, bool):
      raise TypeError('is_locked must be of type bool')
    self._is_locked = is_locked


class SynchronizedGroup(KaggleObject):
  r"""
  Attributes:
    id (int)
    group_id (int)
    owner_user_id (int)
    name (str)
    provider (SynchronizedGroupProvider)
    last_update_time (datetime)
    owner (UserAvatar)
    member_count (int)
    current_user_role (GroupMembershipRole)
    avatar_infos (UserAvatar)
      List of up to three avatars sorted by join date.
  """

  def __init__(self):
    self._id = 0
    self._group_id = None
    self._owner_user_id = None
    self._name = ""
    self._provider = SynchronizedGroupProvider.SYNCHRONIZED_GROUP_PROVIDER_UNSPECIFIED
    self._last_update_time = None
    self._owner = None
    self._member_count = None
    self._current_user_role = None
    self._avatar_infos = []
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
  def group_id(self) -> int:
    return self._group_id or 0

  @group_id.setter
  def group_id(self, group_id: Optional[int]):
    if group_id is None:
      del self.group_id
      return
    if not isinstance(group_id, int):
      raise TypeError('group_id must be of type int')
    self._group_id = group_id

  @property
  def owner_user_id(self) -> int:
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

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
  def provider(self) -> 'SynchronizedGroupProvider':
    return self._provider

  @provider.setter
  def provider(self, provider: 'SynchronizedGroupProvider'):
    if provider is None:
      del self.provider
      return
    if not isinstance(provider, SynchronizedGroupProvider):
      raise TypeError('provider must be of type SynchronizedGroupProvider')
    self._provider = provider

  @property
  def last_update_time(self) -> datetime:
    return self._last_update_time

  @last_update_time.setter
  def last_update_time(self, last_update_time: datetime):
    if last_update_time is None:
      del self.last_update_time
      return
    if not isinstance(last_update_time, datetime):
      raise TypeError('last_update_time must be of type datetime')
    self._last_update_time = last_update_time

  @property
  def owner(self) -> Optional['UserAvatar']:
    return self._owner or None

  @owner.setter
  def owner(self, owner: Optional[Optional['UserAvatar']]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, UserAvatar):
      raise TypeError('owner must be of type UserAvatar')
    self._owner = owner

  @property
  def member_count(self) -> int:
    return self._member_count or 0

  @member_count.setter
  def member_count(self, member_count: Optional[int]):
    if member_count is None:
      del self.member_count
      return
    if not isinstance(member_count, int):
      raise TypeError('member_count must be of type int')
    self._member_count = member_count

  @property
  def current_user_role(self) -> 'GroupMembershipRole':
    return self._current_user_role or GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED

  @current_user_role.setter
  def current_user_role(self, current_user_role: Optional['GroupMembershipRole']):
    if current_user_role is None:
      del self.current_user_role
      return
    if not isinstance(current_user_role, GroupMembershipRole):
      raise TypeError('current_user_role must be of type GroupMembershipRole')
    self._current_user_role = current_user_role

  @property
  def avatar_infos(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of up to three avatars sorted by join date."""
    return self._avatar_infos

  @avatar_infos.setter
  def avatar_infos(self, avatar_infos: Optional[List[Optional['UserAvatar']]]):
    if avatar_infos is None:
      del self.avatar_infos
      return
    if not isinstance(avatar_infos, list):
      raise TypeError('avatar_infos must be of type list')
    if not all([isinstance(t, UserAvatar) for t in avatar_infos]):
      raise TypeError('avatar_infos must contain only items of type UserAvatar')
    self._avatar_infos = avatar_infos


class UserManagedGroup(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    slug (str)
    description (str)
    owner (UserAvatar)
    member_count (int)
    current_user_role (GroupMembershipRole)
    avatar_infos (UserAvatar)
      List of up to three avatars sorted by join date.
    share_token (str)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._slug = ""
    self._description = None
    self._owner = None
    self._member_count = None
    self._current_user_role = None
    self._avatar_infos = []
    self._share_token = None
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
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def owner(self) -> Optional['UserAvatar']:
    return self._owner or None

  @owner.setter
  def owner(self, owner: Optional[Optional['UserAvatar']]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, UserAvatar):
      raise TypeError('owner must be of type UserAvatar')
    self._owner = owner

  @property
  def member_count(self) -> int:
    return self._member_count or 0

  @member_count.setter
  def member_count(self, member_count: Optional[int]):
    if member_count is None:
      del self.member_count
      return
    if not isinstance(member_count, int):
      raise TypeError('member_count must be of type int')
    self._member_count = member_count

  @property
  def current_user_role(self) -> 'GroupMembershipRole':
    return self._current_user_role or GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED

  @current_user_role.setter
  def current_user_role(self, current_user_role: Optional['GroupMembershipRole']):
    if current_user_role is None:
      del self.current_user_role
      return
    if not isinstance(current_user_role, GroupMembershipRole):
      raise TypeError('current_user_role must be of type GroupMembershipRole')
    self._current_user_role = current_user_role

  @property
  def avatar_infos(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of up to three avatars sorted by join date."""
    return self._avatar_infos

  @avatar_infos.setter
  def avatar_infos(self, avatar_infos: Optional[List[Optional['UserAvatar']]]):
    if avatar_infos is None:
      del self.avatar_infos
      return
    if not isinstance(avatar_infos, list):
      raise TypeError('avatar_infos must be of type list')
    if not all([isinstance(t, UserAvatar) for t in avatar_infos]):
      raise TypeError('avatar_infos must contain only items of type UserAvatar')
    self._avatar_infos = avatar_infos

  @property
  def share_token(self) -> str:
    return self._share_token or ""

  @share_token.setter
  def share_token(self, share_token: Optional[str]):
    if share_token is None:
      del self.share_token
      return
    if not isinstance(share_token, str):
      raise TypeError('share_token must be of type str')
    self._share_token = share_token


class UserManagedGroupInvite(KaggleObject):
  r"""
  Attributes:
    id (int)
    group (UserManagedGroup)
    invited_user (UserAvatar)
    invited_by_user (UserAvatar)
    invited_user_role (GroupMembershipRole)
    state (GroupInviteState)
    create_time (datetime)
    update_time (datetime)
  """

  def __init__(self):
    self._id = 0
    self._group = None
    self._invited_user = None
    self._invited_by_user = None
    self._invited_user_role = None
    self._state = None
    self._create_time = None
    self._update_time = None
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
  def group(self) -> Optional['UserManagedGroup']:
    return self._group

  @group.setter
  def group(self, group: Optional['UserManagedGroup']):
    if group is None:
      del self.group
      return
    if not isinstance(group, UserManagedGroup):
      raise TypeError('group must be of type UserManagedGroup')
    self._group = group

  @property
  def invited_user(self) -> Optional['UserAvatar']:
    return self._invited_user

  @invited_user.setter
  def invited_user(self, invited_user: Optional['UserAvatar']):
    if invited_user is None:
      del self.invited_user
      return
    if not isinstance(invited_user, UserAvatar):
      raise TypeError('invited_user must be of type UserAvatar')
    self._invited_user = invited_user

  @property
  def invited_by_user(self) -> Optional['UserAvatar']:
    return self._invited_by_user

  @invited_by_user.setter
  def invited_by_user(self, invited_by_user: Optional['UserAvatar']):
    if invited_by_user is None:
      del self.invited_by_user
      return
    if not isinstance(invited_by_user, UserAvatar):
      raise TypeError('invited_by_user must be of type UserAvatar')
    self._invited_by_user = invited_by_user

  @property
  def invited_user_role(self) -> 'GroupMembershipRole':
    return self._invited_user_role or GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED

  @invited_user_role.setter
  def invited_user_role(self, invited_user_role: Optional['GroupMembershipRole']):
    if invited_user_role is None:
      del self.invited_user_role
      return
    if not isinstance(invited_user_role, GroupMembershipRole):
      raise TypeError('invited_user_role must be of type GroupMembershipRole')
    self._invited_user_role = invited_user_role

  @property
  def state(self) -> 'GroupInviteState':
    return self._state or GroupInviteState.GROUP_INVITE_STATE_UNSPECIFIED

  @state.setter
  def state(self, state: Optional['GroupInviteState']):
    if state is None:
      del self.state
      return
    if not isinstance(state, GroupInviteState):
      raise TypeError('state must be of type GroupInviteState')
    self._state = state

  @property
  def create_time(self) -> datetime:
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def update_time(self) -> datetime:
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time


class UserManagedGroupMembership(KaggleObject):
  r"""
  Attributes:
    group_slug (str)
    user (UserAvatar)
    role (GroupMembershipRole)
    join_date (datetime)
  """

  def __init__(self):
    self._group_slug = ""
    self._user = None
    self._role = None
    self._join_date = None
    self._freeze()

  @property
  def group_slug(self) -> str:
    return self._group_slug

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    self._group_slug = group_slug

  @property
  def user(self) -> Optional['UserAvatar']:
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
  def role(self) -> 'GroupMembershipRole':
    return self._role or GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED

  @role.setter
  def role(self, role: Optional['GroupMembershipRole']):
    if role is None:
      del self.role
      return
    if not isinstance(role, GroupMembershipRole):
      raise TypeError('role must be of type GroupMembershipRole')
    self._role = role

  @property
  def join_date(self) -> datetime:
    return self._join_date

  @join_date.setter
  def join_date(self, join_date: datetime):
    if join_date is None:
      del self.join_date
      return
    if not isinstance(join_date, datetime):
      raise TypeError('join_date must be of type datetime')
    self._join_date = join_date


Collaborator._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupId", "group_id", "_group_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupMemberCount", "group_member_count", "_group_member_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("joinDate", "join_date", "_join_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("type", "type", "_type", CollaboratorType, CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, None, PredefinedSerializer(), optional=True),
]

CollaboratorList._fields = [
  FieldMetadata("owner", "owner", "_owner", Collaborator, None, KaggleObjectSerializer()),
  FieldMetadata("collaborators", "collaborators", "_collaborators", Collaborator, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("isLocked", "is_locked", "_is_locked", bool, None, PredefinedSerializer(), optional=True),
]

SynchronizedGroup._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("groupId", "group_id", "_group_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("provider", "provider", "_provider", SynchronizedGroupProvider, SynchronizedGroupProvider.SYNCHRONIZED_GROUP_PROVIDER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastUpdateTime", "last_update_time", "_last_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("owner", "owner", "_owner", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("memberCount", "member_count", "_member_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("currentUserRole", "current_user_role", "_current_user_role", GroupMembershipRole, None, EnumSerializer(), optional=True),
  FieldMetadata("avatarInfos", "avatar_infos", "_avatar_infos", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
]

UserManagedGroup._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("owner", "owner", "_owner", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("memberCount", "member_count", "_member_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("currentUserRole", "current_user_role", "_current_user_role", GroupMembershipRole, None, EnumSerializer(), optional=True),
  FieldMetadata("avatarInfos", "avatar_infos", "_avatar_infos", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("shareToken", "share_token", "_share_token", str, None, PredefinedSerializer(), optional=True),
]

UserManagedGroupInvite._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("group", "group", "_group", UserManagedGroup, None, KaggleObjectSerializer()),
  FieldMetadata("invitedUser", "invited_user", "_invited_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("invitedByUser", "invited_by_user", "_invited_by_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("invitedUserRole", "invited_user_role", "_invited_user_role", GroupMembershipRole, None, EnumSerializer(), optional=True),
  FieldMetadata("state", "state", "_state", GroupInviteState, None, EnumSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
]

UserManagedGroupMembership._fields = [
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("user", "user", "_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("role", "role", "_role", GroupMembershipRole, None, EnumSerializer(), optional=True),
  FieldMetadata("joinDate", "join_date", "_join_date", datetime, None, DateTimeSerializer()),
]

