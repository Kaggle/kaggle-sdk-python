from kagglesdk.community.types.organization import Organization
from kagglesdk.community.types.organizations_service import CreateOrganizationInviteCodeRequest, CreateOrganizationInviteCodeResponse, CreateOrganizationRequest, CreateOrganizationResponse, DeleteOrganizationMemberRequest, DeleteOrganizationRequest, GetCurrentUserOrganizationsRequest, GetCurrentUserOrganizationsResponse, GetOrganizationMembersRequest, GetOrganizationMembersResponse, GetOrganizationRequest, JoinOrganizationRequest, ListOrganizationContentRequest, ListOrganizationContentResponse, ListOrganizationsRequest, ListOrganizationsResponse, UpdateOrganizationAllowModelGatingRequest, UpdateOrganizationContentStateRequest, UpdateOrganizationOwnershipRequest, UpdateOrganizationRequest, UpdateOrganizationSlugRequest, UpdateOrganizationSlugResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class OrganizationsV2Client(object):
  """TODO: Remove V2 after admin/organizations_service is deprecated"""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_v2organization(self, request: CreateOrganizationRequest = None) -> CreateOrganizationResponse:
    r"""
    This method creates a new organization given some settings

    Args:
      request (CreateOrganizationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateOrganizationRequest()

    return self._client.call("community.OrganizationsV2Service", "CreateV2Organization", request, CreateOrganizationResponse)

  def update_organization(self, request: UpdateOrganizationRequest = None):
    r"""
    This method allows creators to modify their organization's high-level
    settings

    Args:
      request (UpdateOrganizationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOrganizationRequest()

    self._client.call("community.OrganizationsV2Service", "UpdateOrganization", request, None)

  def get_organization(self, request: GetOrganizationRequest = None) -> Organization:
    r"""
    Fetches an organization

    Args:
      request (GetOrganizationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOrganizationRequest()

    return self._client.call("community.OrganizationsV2Service", "GetOrganization", request, Organization)

  def create_organization_invite_code(self, request: CreateOrganizationInviteCodeRequest = None) -> CreateOrganizationInviteCodeResponse:
    r"""
    This method creates an organization invite link which organization creators
    can send to prospective members

    Args:
      request (CreateOrganizationInviteCodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateOrganizationInviteCodeRequest()

    return self._client.call("community.OrganizationsV2Service", "CreateOrganizationInviteCode", request, CreateOrganizationInviteCodeResponse)

  def join_organization(self, request: JoinOrganizationRequest = None):
    r"""
    Join an organization based on an invite link

    Args:
      request (JoinOrganizationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = JoinOrganizationRequest()

    self._client.call("community.OrganizationsV2Service", "JoinOrganization", request, None)

  def get_organization_members(self, request: GetOrganizationMembersRequest = None) -> GetOrganizationMembersResponse:
    r"""
    Fetches all of an organization's members

    Args:
      request (GetOrganizationMembersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOrganizationMembersRequest()

    return self._client.call("community.OrganizationsV2Service", "GetOrganizationMembers", request, GetOrganizationMembersResponse)

  def delete_organization_member(self, request: DeleteOrganizationMemberRequest = None):
    r"""
    Removes an organization membership. Creators are able to remove anyone's
    membership, and any member can remove themselves.

    Args:
      request (DeleteOrganizationMemberRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteOrganizationMemberRequest()

    self._client.call("community.OrganizationsV2Service", "DeleteOrganizationMember", request, None)

  def update_organization_content_state(self, request: UpdateOrganizationContentStateRequest = None):
    r"""
    Admin-only route for approving / denying an organization or moving an
    organization to a quarantined / deleted state

    Args:
      request (UpdateOrganizationContentStateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOrganizationContentStateRequest()

    self._client.call("community.OrganizationsV2Service", "UpdateOrganizationContentState", request, None)

  def update_organization_ownership(self, request: UpdateOrganizationOwnershipRequest = None):
    r"""
    Transfers ownership of an organization to another user

    Args:
      request (UpdateOrganizationOwnershipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOrganizationOwnershipRequest()

    self._client.call("community.OrganizationsV2Service", "UpdateOrganizationOwnership", request, None)

  def get_current_user_organizations(self, request: GetCurrentUserOrganizationsRequest = None) -> GetCurrentUserOrganizationsResponse:
    r"""
    Fetches all of the current user's joined organizations, either as creator
    or a regular member

    Args:
      request (GetCurrentUserOrganizationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCurrentUserOrganizationsRequest()

    return self._client.call("community.OrganizationsV2Service", "GetCurrentUserOrganizations", request, GetCurrentUserOrganizationsResponse)

  def delete_organization(self, request: DeleteOrganizationRequest = None):
    r"""
    Delete an organization, removing all memberships, attributes, and deleting
    its owned models and datasets. Competitions have their OrganizationId
    column marked as NULL.

    Args:
      request (DeleteOrganizationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteOrganizationRequest()

    self._client.call("community.OrganizationsV2Service", "DeleteOrganization", request, None)

  def list_organization_content(self, request: ListOrganizationContentRequest = None) -> ListOrganizationContentResponse:
    r"""
    List high-level organization owned content for the purpose of the overview
    profile page

    Args:
      request (ListOrganizationContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListOrganizationContentRequest()

    return self._client.call("community.OrganizationsV2Service", "ListOrganizationContent", request, ListOrganizationContentResponse)

  def update_organization_allow_model_gating(self, request: UpdateOrganizationAllowModelGatingRequest = None):
    r"""
    Updates an organization's `allows_model_gating` setting, controlling
    whether the organization can use the model gating feature.

    Args:
      request (UpdateOrganizationAllowModelGatingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOrganizationAllowModelGatingRequest()

    self._client.call("community.OrganizationsV2Service", "UpdateOrganizationAllowModelGating", request, None)

  def list_organizations(self, request: ListOrganizationsRequest = None) -> ListOrganizationsResponse:
    r"""
    Lists organizations.

    Args:
      request (ListOrganizationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListOrganizationsRequest()

    return self._client.call("community.OrganizationsV2Service", "ListOrganizations", request, ListOrganizationsResponse)

  def update_organization_slug(self, request: UpdateOrganizationSlugRequest = None) -> UpdateOrganizationSlugResponse:
    r"""
    Args:
      request (UpdateOrganizationSlugRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOrganizationSlugRequest()

    return self._client.call("community.OrganizationsV2Service", "UpdateOrganizationSlug", request, UpdateOrganizationSlugResponse)
