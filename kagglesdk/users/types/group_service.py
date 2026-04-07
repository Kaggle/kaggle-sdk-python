from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.group_types import SynchronizedGroup, UserManagedGroup, UserManagedGroupInvite, UserManagedGroupMembership
from kagglesdk.users.types.groups_enum import GroupInviteState, GroupMembershipRole, ListUserManagedGroupInvitesOrderBy, ListUserManagedGroupMembershipsOrderBy, ListUserManagedGroupsOrderBy, OrderByDirection
from typing import Optional, List

class CreateSynchronizedGroupRequest(KaggleObject):
  r"""
  Attributes:
    group (SynchronizedGroup)
  """

  def __init__(self):
    self._group = None
    self._freeze()

  @property
  def group(self) -> Optional['SynchronizedGroup']:
    return self._group

  @group.setter
  def group(self, group: Optional['SynchronizedGroup']):
    if group is None:
      del self.group
      return
    if not isinstance(group, SynchronizedGroup):
      raise TypeError('group must be of type SynchronizedGroup')
    self._group = group


class CreateUserManagedGroupInviteRequest(KaggleObject):
  r"""
  Attributes:
    group_slug (str)
      The group to create the invitation for.
    invited_username (str)
      The invitee's username.
    invited_user_role (GroupMembershipRole)
      The invitee's role in the group after accepting the invitation.
  """

  def __init__(self):
    self._group_slug = ""
    self._invited_username = ""
    self._invited_user_role = GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED
    self._freeze()

  @property
  def group_slug(self) -> str:
    """The group to create the invitation for."""
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
  def invited_username(self) -> str:
    """The invitee's username."""
    return self._invited_username

  @invited_username.setter
  def invited_username(self, invited_username: str):
    if invited_username is None:
      del self.invited_username
      return
    if not isinstance(invited_username, str):
      raise TypeError('invited_username must be of type str')
    self._invited_username = invited_username

  @property
  def invited_user_role(self) -> 'GroupMembershipRole':
    """The invitee's role in the group after accepting the invitation."""
    return self._invited_user_role

  @invited_user_role.setter
  def invited_user_role(self, invited_user_role: 'GroupMembershipRole'):
    if invited_user_role is None:
      del self.invited_user_role
      return
    if not isinstance(invited_user_role, GroupMembershipRole):
      raise TypeError('invited_user_role must be of type GroupMembershipRole')
    self._invited_user_role = invited_user_role


class CreateUserManagedGroupMembershipRequest(KaggleObject):
  r"""
  Attributes:
    group_slug (str)
    share_token (str)
      The URL part corresponding to a group share token.
  """

  def __init__(self):
    self._group_slug = ""
    self._share_token = ""
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
  def share_token(self) -> str:
    """The URL part corresponding to a group share token."""
    return self._share_token

  @share_token.setter
  def share_token(self, share_token: str):
    if share_token is None:
      del self.share_token
      return
    if not isinstance(share_token, str):
      raise TypeError('share_token must be of type str')
    self._share_token = share_token


class CreateUserManagedGroupRequest(KaggleObject):
  r"""
  Attributes:
    group (UserManagedGroup)
  """

  def __init__(self):
    self._group = None
    self._freeze()

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


class DeleteSynchronizedGroupRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
  """

  def __init__(self):
    self._id = 0
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


class DeleteUserManagedGroupMembershipRequest(KaggleObject):
  r"""
  Attributes:
    group_slug (str)
    username (str)
      If unset, the current user is used.
  """

  def __init__(self):
    self._group_slug = ""
    self._username = None
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
  def username(self) -> str:
    """If unset, the current user is used."""
    return self._username or ""

  @username.setter
  def username(self, username: Optional[str]):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username


class DeleteUserManagedGroupRequest(KaggleObject):
  r"""
  Attributes:
    slug (str)
  """

  def __init__(self):
    self._slug = ""
    self._freeze()

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


class GetUserManagedGroupInviteRequest(KaggleObject):
  r"""
  Attributes:
    invite_id (int)
    group_slug (str)
      Find the latest invite for the current user for the given group.
  """

  def __init__(self):
    self._invite_id = None
    self._group_slug = None
    self._freeze()

  @property
  def invite_id(self) -> int:
    return self._invite_id or 0

  @invite_id.setter
  def invite_id(self, invite_id: int):
    if invite_id is None:
      del self.invite_id
      return
    if not isinstance(invite_id, int):
      raise TypeError('invite_id must be of type int')
    del self.group_slug
    self._invite_id = invite_id

  @property
  def group_slug(self) -> str:
    """Find the latest invite for the current user for the given group."""
    return self._group_slug or ""

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    del self.invite_id
    self._group_slug = group_slug


class GetUserManagedGroupRequest(KaggleObject):
  r"""
  Attributes:
    slug (str)
    read_mask (FieldMask)
    share_token (str)
  """

  def __init__(self):
    self._slug = ""
    self._read_mask = None
    self._share_token = None
    self._freeze()

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
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask

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


class ListSynchronizedGroupsRequest(KaggleObject):
  r"""
  Attributes:
    search_query (str)
      If specified, returns groups matching the search query. The query is
      searched in group name and description.
    page_size (int)
      The number of groups to return at once.
    page_token (str)
      Token given from previous call, returns the next page of results.
    read_mask (FieldMask)
  """

  def __init__(self):
    self._search_query = None
    self._page_size = None
    self._page_token = None
    self._read_mask = None
    self._freeze()

  @property
  def search_query(self) -> str:
    r"""
    If specified, returns groups matching the search query. The query is
    searched in group name and description.
    """
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def page_size(self) -> int:
    """The number of groups to return at once."""
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    """Token given from previous call, returns the next page of results."""
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListSynchronizedGroupsResponse(KaggleObject):
  r"""
  Attributes:
    groups (SynchronizedGroup)
      List of groups accessible to the current user.
    next_page_token (str)
      Page token for the next page of results.
  """

  def __init__(self):
    self._groups = []
    self._next_page_token = None
    self._freeze()

  @property
  def groups(self) -> Optional[List[Optional['SynchronizedGroup']]]:
    """List of groups accessible to the current user."""
    return self._groups

  @groups.setter
  def groups(self, groups: Optional[List[Optional['SynchronizedGroup']]]):
    if groups is None:
      del self.groups
      return
    if not isinstance(groups, list):
      raise TypeError('groups must be of type list')
    if not all([isinstance(t, SynchronizedGroup) for t in groups]):
      raise TypeError('groups must contain only items of type SynchronizedGroup')
    self._groups = groups

  @property
  def next_page_token(self) -> str:
    """Page token for the next page of results."""
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ListUserManagedGroupInvitesFilter(KaggleObject):
  r"""
  Attributes:
    search_query (str)
      If specified, returns invites matching the search query. The query is
      searched in username, group slug and name.
    roles (GroupMembershipRole)
    states (GroupInviteState)
    include_only_latest_user_invite (bool)
      Only include the latest invite sent to a user and excludes previous
      invites.
  """

  def __init__(self):
    self._search_query = None
    self._roles = []
    self._states = []
    self._include_only_latest_user_invite = None
    self._freeze()

  @property
  def search_query(self) -> str:
    r"""
    If specified, returns invites matching the search query. The query is
    searched in username, group slug and name.
    """
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def roles(self) -> Optional[List['GroupMembershipRole']]:
    return self._roles

  @roles.setter
  def roles(self, roles: Optional[List['GroupMembershipRole']]):
    if roles is None:
      del self.roles
      return
    if not isinstance(roles, list):
      raise TypeError('roles must be of type list')
    if not all([isinstance(t, GroupMembershipRole) for t in roles]):
      raise TypeError('roles must contain only items of type GroupMembershipRole')
    self._roles = roles

  @property
  def states(self) -> Optional[List['GroupInviteState']]:
    return self._states

  @states.setter
  def states(self, states: Optional[List['GroupInviteState']]):
    if states is None:
      del self.states
      return
    if not isinstance(states, list):
      raise TypeError('states must be of type list')
    if not all([isinstance(t, GroupInviteState) for t in states]):
      raise TypeError('states must contain only items of type GroupInviteState')
    self._states = states

  @property
  def include_only_latest_user_invite(self) -> bool:
    r"""
    Only include the latest invite sent to a user and excludes previous
    invites.
    """
    return self._include_only_latest_user_invite or False

  @include_only_latest_user_invite.setter
  def include_only_latest_user_invite(self, include_only_latest_user_invite: Optional[bool]):
    if include_only_latest_user_invite is None:
      del self.include_only_latest_user_invite
      return
    if not isinstance(include_only_latest_user_invite, bool):
      raise TypeError('include_only_latest_user_invite must be of type bool')
    self._include_only_latest_user_invite = include_only_latest_user_invite


class ListUserManagedGroupInvitesRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    my_invite (bool)
      List my invites to join a group.
    group_slug (str)
      List invites for a given group (admins & owners).
    filter (ListUserManagedGroupInvitesFilter)
    order_by (ListUserManagedGroupInvitesOrderBy)
    order_by_direction (OrderByDirection)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._my_invite = None
    self._group_slug = None
    self._filter = None
    self._order_by = ListUserManagedGroupInvitesOrderBy.LIST_USER_MANAGED_GROUP_INVITES_ORDER_BY_CREATE_TIME
    self._order_by_direction = OrderByDirection.ASC
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def my_invite(self) -> bool:
    """List my invites to join a group."""
    return self._my_invite or False

  @my_invite.setter
  def my_invite(self, my_invite: bool):
    if my_invite is None:
      del self.my_invite
      return
    if not isinstance(my_invite, bool):
      raise TypeError('my_invite must be of type bool')
    del self.group_slug
    self._my_invite = my_invite

  @property
  def group_slug(self) -> str:
    """List invites for a given group (admins & owners)."""
    return self._group_slug or ""

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    del self.my_invite
    self._group_slug = group_slug

  @property
  def filter(self) -> Optional['ListUserManagedGroupInvitesFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListUserManagedGroupInvitesFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListUserManagedGroupInvitesFilter):
      raise TypeError('filter must be of type ListUserManagedGroupInvitesFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListUserManagedGroupInvitesOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListUserManagedGroupInvitesOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListUserManagedGroupInvitesOrderBy):
      raise TypeError('order_by must be of type ListUserManagedGroupInvitesOrderBy')
    self._order_by = order_by

  @property
  def order_by_direction(self) -> 'OrderByDirection':
    return self._order_by_direction

  @order_by_direction.setter
  def order_by_direction(self, order_by_direction: 'OrderByDirection'):
    if order_by_direction is None:
      del self.order_by_direction
      return
    if not isinstance(order_by_direction, OrderByDirection):
      raise TypeError('order_by_direction must be of type OrderByDirection')
    self._order_by_direction = order_by_direction


class ListUserManagedGroupInvitesResponse(KaggleObject):
  r"""
  Attributes:
    invites (UserManagedGroupInvite)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._invites = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def invites(self) -> Optional[List[Optional['UserManagedGroupInvite']]]:
    return self._invites

  @invites.setter
  def invites(self, invites: Optional[List[Optional['UserManagedGroupInvite']]]):
    if invites is None:
      del self.invites
      return
    if not isinstance(invites, list):
      raise TypeError('invites must be of type list')
    if not all([isinstance(t, UserManagedGroupInvite) for t in invites]):
      raise TypeError('invites must contain only items of type UserManagedGroupInvite')
    self._invites = invites

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ListUserManagedGroupMembershipsFilter(KaggleObject):
  r"""
  Attributes:
    search_query (str)
      If specified, returns invites matching the search query. The query is
      searched in username, group slug and name.
    roles (GroupMembershipRole)
  """

  def __init__(self):
    self._search_query = None
    self._roles = []
    self._freeze()

  @property
  def search_query(self) -> str:
    r"""
    If specified, returns invites matching the search query. The query is
    searched in username, group slug and name.
    """
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def roles(self) -> Optional[List['GroupMembershipRole']]:
    return self._roles

  @roles.setter
  def roles(self, roles: Optional[List['GroupMembershipRole']]):
    if roles is None:
      del self.roles
      return
    if not isinstance(roles, list):
      raise TypeError('roles must be of type list')
    if not all([isinstance(t, GroupMembershipRole) for t in roles]):
      raise TypeError('roles must contain only items of type GroupMembershipRole')
    self._roles = roles


class ListUserManagedGroupMembershipsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    group_slug (str)
    filter (ListUserManagedGroupMembershipsFilter)
    order_by (ListUserManagedGroupMembershipsOrderBy)
    order_by_direction (OrderByDirection)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._group_slug = ""
    self._filter = None
    self._order_by = ListUserManagedGroupMembershipsOrderBy.LIST_USER_MANAGED_GROUP_MEMBERSHIPS_ORDER_BY_USERNAME
    self._order_by_direction = OrderByDirection.ASC
    self._read_mask = None
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

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
  def filter(self) -> Optional['ListUserManagedGroupMembershipsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListUserManagedGroupMembershipsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListUserManagedGroupMembershipsFilter):
      raise TypeError('filter must be of type ListUserManagedGroupMembershipsFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListUserManagedGroupMembershipsOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListUserManagedGroupMembershipsOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListUserManagedGroupMembershipsOrderBy):
      raise TypeError('order_by must be of type ListUserManagedGroupMembershipsOrderBy')
    self._order_by = order_by

  @property
  def order_by_direction(self) -> 'OrderByDirection':
    return self._order_by_direction

  @order_by_direction.setter
  def order_by_direction(self, order_by_direction: 'OrderByDirection'):
    if order_by_direction is None:
      del self.order_by_direction
      return
    if not isinstance(order_by_direction, OrderByDirection):
      raise TypeError('order_by_direction must be of type OrderByDirection')
    self._order_by_direction = order_by_direction

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListUserManagedGroupMembershipsResponse(KaggleObject):
  r"""
  Attributes:
    memberships (UserManagedGroupMembership)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._memberships = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def memberships(self) -> Optional[List[Optional['UserManagedGroupMembership']]]:
    return self._memberships

  @memberships.setter
  def memberships(self, memberships: Optional[List[Optional['UserManagedGroupMembership']]]):
    if memberships is None:
      del self.memberships
      return
    if not isinstance(memberships, list):
      raise TypeError('memberships must be of type list')
    if not all([isinstance(t, UserManagedGroupMembership) for t in memberships]):
      raise TypeError('memberships must contain only items of type UserManagedGroupMembership')
    self._memberships = memberships

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ListUserManagedGroupsFilter(KaggleObject):
  r"""
  Attributes:
    current_user_roles (GroupMembershipRole)
    search_query (str)
      If specified, returns groups matching the search query. The query is
      searched in group name, slug and description.
  """

  def __init__(self):
    self._current_user_roles = []
    self._search_query = None
    self._freeze()

  @property
  def current_user_roles(self) -> Optional[List['GroupMembershipRole']]:
    return self._current_user_roles

  @current_user_roles.setter
  def current_user_roles(self, current_user_roles: Optional[List['GroupMembershipRole']]):
    if current_user_roles is None:
      del self.current_user_roles
      return
    if not isinstance(current_user_roles, list):
      raise TypeError('current_user_roles must be of type list')
    if not all([isinstance(t, GroupMembershipRole) for t in current_user_roles]):
      raise TypeError('current_user_roles must contain only items of type GroupMembershipRole')
    self._current_user_roles = current_user_roles

  @property
  def search_query(self) -> str:
    r"""
    If specified, returns groups matching the search query. The query is
    searched in group name, slug and description.
    """
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query


class ListUserManagedGroupsRequest(KaggleObject):
  r"""
  This RPC will only return groups which the current user is a part of.

  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    filter (ListUserManagedGroupsFilter)
    order_by (ListUserManagedGroupsOrderBy)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._filter = None
    self._order_by = ListUserManagedGroupsOrderBy.LIST_USER_MANAGED_GROUPS_ORDER_BY_RECENT
    self._read_mask = None
    self._freeze()

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def filter(self) -> Optional['ListUserManagedGroupsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListUserManagedGroupsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListUserManagedGroupsFilter):
      raise TypeError('filter must be of type ListUserManagedGroupsFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListUserManagedGroupsOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListUserManagedGroupsOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListUserManagedGroupsOrderBy):
      raise TypeError('order_by must be of type ListUserManagedGroupsOrderBy')
    self._order_by = order_by

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListUserManagedGroupsResponse(KaggleObject):
  r"""
  Attributes:
    groups (UserManagedGroup)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._groups = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def groups(self) -> Optional[List[Optional['UserManagedGroup']]]:
    return self._groups

  @groups.setter
  def groups(self, groups: Optional[List[Optional['UserManagedGroup']]]):
    if groups is None:
      del self.groups
      return
    if not isinstance(groups, list):
      raise TypeError('groups must be of type list')
    if not all([isinstance(t, UserManagedGroup) for t in groups]):
      raise TypeError('groups must contain only items of type UserManagedGroup')
    self._groups = groups

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class TransferUserManagedGroupOwnershipRequest(KaggleObject):
  r"""
  Attributes:
    group_slug (str)
    new_owner_username (str)
  """

  def __init__(self):
    self._group_slug = ""
    self._new_owner_username = ""
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
  def new_owner_username(self) -> str:
    return self._new_owner_username

  @new_owner_username.setter
  def new_owner_username(self, new_owner_username: str):
    if new_owner_username is None:
      del self.new_owner_username
      return
    if not isinstance(new_owner_username, str):
      raise TypeError('new_owner_username must be of type str')
    self._new_owner_username = new_owner_username


class UpdateSynchronizedGroupRequest(KaggleObject):
  r"""
  Attributes:
    group (SynchronizedGroup)
  """

  def __init__(self):
    self._group = None
    self._freeze()

  @property
  def group(self) -> Optional['SynchronizedGroup']:
    return self._group

  @group.setter
  def group(self, group: Optional['SynchronizedGroup']):
    if group is None:
      del self.group
      return
    if not isinstance(group, SynchronizedGroup):
      raise TypeError('group must be of type SynchronizedGroup')
    self._group = group


class UpdateUserManagedGroupInviteRequest(KaggleObject):
  r"""
  Attributes:
    invite (UserManagedGroupInvite)
      The invite's `id` field is used to identify the invite to update.
    update_mask (FieldMask)
  """

  def __init__(self):
    self._invite = None
    self._update_mask = None
    self._freeze()

  @property
  def invite(self) -> Optional['UserManagedGroupInvite']:
    """The invite's `id` field is used to identify the invite to update."""
    return self._invite

  @invite.setter
  def invite(self, invite: Optional['UserManagedGroupInvite']):
    if invite is None:
      del self.invite
      return
    if not isinstance(invite, UserManagedGroupInvite):
      raise TypeError('invite must be of type UserManagedGroupInvite')
    self._invite = invite

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateUserManagedGroupMembershipRequest(KaggleObject):
  r"""
  Attributes:
    membership (UserManagedGroupMembership)
      The `group_slug` & `user.user_name` fields are used to identify the group
      membership to update.
    update_mask (FieldMask)
  """

  def __init__(self):
    self._membership = None
    self._update_mask = None
    self._freeze()

  @property
  def membership(self) -> Optional['UserManagedGroupMembership']:
    r"""
    The `group_slug` & `user.user_name` fields are used to identify the group
    membership to update.
    """
    return self._membership

  @membership.setter
  def membership(self, membership: Optional['UserManagedGroupMembership']):
    if membership is None:
      del self.membership
      return
    if not isinstance(membership, UserManagedGroupMembership):
      raise TypeError('membership must be of type UserManagedGroupMembership')
    self._membership = membership

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateUserManagedGroupRequest(KaggleObject):
  r"""
  Attributes:
    group (UserManagedGroup)
      The group's `slug` field is used to identify the group to update.
    update_mask (FieldMask)
  """

  def __init__(self):
    self._group = None
    self._update_mask = None
    self._freeze()

  @property
  def group(self) -> Optional['UserManagedGroup']:
    """The group's `slug` field is used to identify the group to update."""
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
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


CreateSynchronizedGroupRequest._fields = [
  FieldMetadata("group", "group", "_group", SynchronizedGroup, None, KaggleObjectSerializer()),
]

CreateUserManagedGroupInviteRequest._fields = [
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("invitedUsername", "invited_username", "_invited_username", str, "", PredefinedSerializer()),
  FieldMetadata("invitedUserRole", "invited_user_role", "_invited_user_role", GroupMembershipRole, GroupMembershipRole.GROUP_MEMBERSHIP_ROLE_UNSPECIFIED, EnumSerializer()),
]

CreateUserManagedGroupMembershipRequest._fields = [
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("shareToken", "share_token", "_share_token", str, "", PredefinedSerializer()),
]

CreateUserManagedGroupRequest._fields = [
  FieldMetadata("group", "group", "_group", UserManagedGroup, None, KaggleObjectSerializer()),
]

DeleteSynchronizedGroupRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DeleteUserManagedGroupMembershipRequest._fields = [
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
]

DeleteUserManagedGroupRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
]

GetUserManagedGroupInviteRequest._fields = [
  FieldMetadata("inviteId", "invite_id", "_invite_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, None, PredefinedSerializer(), optional=True),
]

GetUserManagedGroupRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("shareToken", "share_token", "_share_token", str, None, PredefinedSerializer(), optional=True),
]

ListSynchronizedGroupsRequest._fields = [
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListSynchronizedGroupsResponse._fields = [
  FieldMetadata("groups", "groups", "_groups", SynchronizedGroup, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListUserManagedGroupInvitesFilter._fields = [
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("roles", "roles", "_roles", GroupMembershipRole, [], ListSerializer(EnumSerializer())),
  FieldMetadata("states", "states", "_states", GroupInviteState, [], ListSerializer(EnumSerializer())),
  FieldMetadata("includeOnlyLatestUserInvite", "include_only_latest_user_invite", "_include_only_latest_user_invite", bool, None, PredefinedSerializer(), optional=True),
]

ListUserManagedGroupInvitesRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("myInvite", "my_invite", "_my_invite", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListUserManagedGroupInvitesFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListUserManagedGroupInvitesOrderBy, ListUserManagedGroupInvitesOrderBy.LIST_USER_MANAGED_GROUP_INVITES_ORDER_BY_CREATE_TIME, EnumSerializer()),
  FieldMetadata("orderByDirection", "order_by_direction", "_order_by_direction", OrderByDirection, OrderByDirection.ASC, EnumSerializer()),
]

ListUserManagedGroupInvitesResponse._fields = [
  FieldMetadata("invites", "invites", "_invites", UserManagedGroupInvite, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListUserManagedGroupMembershipsFilter._fields = [
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("roles", "roles", "_roles", GroupMembershipRole, [], ListSerializer(EnumSerializer())),
]

ListUserManagedGroupMembershipsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("filter", "filter", "_filter", ListUserManagedGroupMembershipsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListUserManagedGroupMembershipsOrderBy, ListUserManagedGroupMembershipsOrderBy.LIST_USER_MANAGED_GROUP_MEMBERSHIPS_ORDER_BY_USERNAME, EnumSerializer()),
  FieldMetadata("orderByDirection", "order_by_direction", "_order_by_direction", OrderByDirection, OrderByDirection.ASC, EnumSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListUserManagedGroupMembershipsResponse._fields = [
  FieldMetadata("memberships", "memberships", "_memberships", UserManagedGroupMembership, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListUserManagedGroupsFilter._fields = [
  FieldMetadata("currentUserRoles", "current_user_roles", "_current_user_roles", GroupMembershipRole, [], ListSerializer(EnumSerializer())),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
]

ListUserManagedGroupsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListUserManagedGroupsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListUserManagedGroupsOrderBy, ListUserManagedGroupsOrderBy.LIST_USER_MANAGED_GROUPS_ORDER_BY_RECENT, EnumSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListUserManagedGroupsResponse._fields = [
  FieldMetadata("groups", "groups", "_groups", UserManagedGroup, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

TransferUserManagedGroupOwnershipRequest._fields = [
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, "", PredefinedSerializer()),
  FieldMetadata("newOwnerUsername", "new_owner_username", "_new_owner_username", str, "", PredefinedSerializer()),
]

UpdateSynchronizedGroupRequest._fields = [
  FieldMetadata("group", "group", "_group", SynchronizedGroup, None, KaggleObjectSerializer()),
]

UpdateUserManagedGroupInviteRequest._fields = [
  FieldMetadata("invite", "invite", "_invite", UserManagedGroupInvite, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateUserManagedGroupMembershipRequest._fields = [
  FieldMetadata("membership", "membership", "_membership", UserManagedGroupMembership, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateUserManagedGroupRequest._fields = [
  FieldMetadata("group", "group", "_group", UserManagedGroup, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

