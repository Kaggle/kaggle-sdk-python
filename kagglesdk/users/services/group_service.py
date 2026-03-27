from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.group_service import CreateSynchronizedGroupRequest, CreateUserManagedGroupInviteRequest, CreateUserManagedGroupMembershipRequest, CreateUserManagedGroupRequest, DeleteSynchronizedGroupRequest, DeleteUserManagedGroupMembershipRequest, DeleteUserManagedGroupRequest, GetUserManagedGroupInviteRequest, GetUserManagedGroupRequest, ListSynchronizedGroupsRequest, ListSynchronizedGroupsResponse, ListUserManagedGroupInvitesRequest, ListUserManagedGroupInvitesResponse, ListUserManagedGroupMembershipsRequest, ListUserManagedGroupMembershipsResponse, ListUserManagedGroupsRequest, ListUserManagedGroupsResponse, TransferUserManagedGroupOwnershipRequest, UpdateSynchronizedGroupRequest, UpdateUserManagedGroupInviteRequest, UpdateUserManagedGroupMembershipRequest, UpdateUserManagedGroupRequest
from kagglesdk.users.types.group_types import SynchronizedGroup, UserManagedGroup, UserManagedGroupInvite, UserManagedGroupMembership

class GroupClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_synchronized_group(self, request: CreateSynchronizedGroupRequest = None) -> SynchronizedGroup:
    r"""
    Args:
      request (CreateSynchronizedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateSynchronizedGroupRequest()

    return self._client.call("users.GroupService", "CreateSynchronizedGroup", request, SynchronizedGroup)

  def update_synchronized_group(self, request: UpdateSynchronizedGroupRequest = None) -> SynchronizedGroup:
    r"""
    Args:
      request (UpdateSynchronizedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSynchronizedGroupRequest()

    return self._client.call("users.GroupService", "UpdateSynchronizedGroup", request, SynchronizedGroup)

  def delete_synchronized_group(self, request: DeleteSynchronizedGroupRequest = None):
    r"""
    Args:
      request (DeleteSynchronizedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteSynchronizedGroupRequest()

    self._client.call("users.GroupService", "DeleteSynchronizedGroup", request, None)

  def create_user_managed_group(self, request: CreateUserManagedGroupRequest = None) -> UserManagedGroup:
    r"""
    Args:
      request (CreateUserManagedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserManagedGroupRequest()

    return self._client.call("users.GroupService", "CreateUserManagedGroup", request, UserManagedGroup)

  def get_user_managed_group(self, request: GetUserManagedGroupRequest = None) -> UserManagedGroup:
    r"""
    Args:
      request (GetUserManagedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserManagedGroupRequest()

    return self._client.call("users.GroupService", "GetUserManagedGroup", request, UserManagedGroup)

  def update_user_managed_group(self, request: UpdateUserManagedGroupRequest = None) -> UserManagedGroup:
    r"""
    Args:
      request (UpdateUserManagedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserManagedGroupRequest()

    return self._client.call("users.GroupService", "UpdateUserManagedGroup", request, UserManagedGroup)

  def delete_user_managed_group(self, request: DeleteUserManagedGroupRequest = None):
    r"""
    Args:
      request (DeleteUserManagedGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteUserManagedGroupRequest()

    self._client.call("users.GroupService", "DeleteUserManagedGroup", request, None)

  def list_user_managed_groups(self, request: ListUserManagedGroupsRequest = None) -> ListUserManagedGroupsResponse:
    r"""
    Args:
      request (ListUserManagedGroupsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserManagedGroupsRequest()

    return self._client.call("users.GroupService", "ListUserManagedGroups", request, ListUserManagedGroupsResponse)

  def transfer_user_managed_group_ownership(self, request: TransferUserManagedGroupOwnershipRequest = None) -> UserManagedGroup:
    r"""
    Args:
      request (TransferUserManagedGroupOwnershipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TransferUserManagedGroupOwnershipRequest()

    return self._client.call("users.GroupService", "TransferUserManagedGroupOwnership", request, UserManagedGroup)

  def create_user_managed_group_invite(self, request: CreateUserManagedGroupInviteRequest = None) -> UserManagedGroupInvite:
    r"""
    Args:
      request (CreateUserManagedGroupInviteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserManagedGroupInviteRequest()

    return self._client.call("users.GroupService", "CreateUserManagedGroupInvite", request, UserManagedGroupInvite)

  def get_user_managed_group_invite(self, request: GetUserManagedGroupInviteRequest = None) -> UserManagedGroupInvite:
    r"""
    Args:
      request (GetUserManagedGroupInviteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserManagedGroupInviteRequest()

    return self._client.call("users.GroupService", "GetUserManagedGroupInvite", request, UserManagedGroupInvite)

  def list_user_managed_group_invites(self, request: ListUserManagedGroupInvitesRequest = None) -> ListUserManagedGroupInvitesResponse:
    r"""
    Args:
      request (ListUserManagedGroupInvitesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserManagedGroupInvitesRequest()

    return self._client.call("users.GroupService", "ListUserManagedGroupInvites", request, ListUserManagedGroupInvitesResponse)

  def update_user_managed_group_invite(self, request: UpdateUserManagedGroupInviteRequest = None) -> UserManagedGroupInvite:
    r"""
    Args:
      request (UpdateUserManagedGroupInviteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserManagedGroupInviteRequest()

    return self._client.call("users.GroupService", "UpdateUserManagedGroupInvite", request, UserManagedGroupInvite)

  def list_user_managed_group_memberships(self, request: ListUserManagedGroupMembershipsRequest = None) -> ListUserManagedGroupMembershipsResponse:
    r"""
    Args:
      request (ListUserManagedGroupMembershipsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserManagedGroupMembershipsRequest()

    return self._client.call("users.GroupService", "ListUserManagedGroupMemberships", request, ListUserManagedGroupMembershipsResponse)

  def create_user_managed_group_membership(self, request: CreateUserManagedGroupMembershipRequest = None) -> UserManagedGroupMembership:
    r"""
    Args:
      request (CreateUserManagedGroupMembershipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserManagedGroupMembershipRequest()

    return self._client.call("users.GroupService", "CreateUserManagedGroupMembership", request, UserManagedGroupMembership)

  def update_user_managed_group_membership(self, request: UpdateUserManagedGroupMembershipRequest = None) -> UserManagedGroupMembership:
    r"""
    Args:
      request (UpdateUserManagedGroupMembershipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserManagedGroupMembershipRequest()

    return self._client.call("users.GroupService", "UpdateUserManagedGroupMembership", request, UserManagedGroupMembership)

  def delete_user_managed_group_membership(self, request: DeleteUserManagedGroupMembershipRequest = None):
    r"""
    Args:
      request (DeleteUserManagedGroupMembershipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteUserManagedGroupMembershipRequest()

    self._client.call("users.GroupService", "DeleteUserManagedGroupMembership", request, None)

  def list_synchronized_groups(self, request: ListSynchronizedGroupsRequest = None) -> ListSynchronizedGroupsResponse:
    r"""
    Args:
      request (ListSynchronizedGroupsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSynchronizedGroupsRequest()

    return self._client.call("users.GroupService", "ListSynchronizedGroups", request, ListSynchronizedGroupsResponse)
