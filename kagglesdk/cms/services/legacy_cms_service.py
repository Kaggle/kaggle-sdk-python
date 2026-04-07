from kagglesdk.cms.types.legacy_cms_service import CmsPage, CreatePageRequest, CreateTeamMemberRequest, DeleteTeamMemberRequest, GetPageRequest, GetPagesRequest, GetPagesResponse, ListDocsRequest, ListDocsResponse, ListPagesRequest, ListPagesResponse, ListTeamMembersRequest, ListTeamMembersResponse, TeamMember, UpdateDocPageOrderRequest, UpdatePageRequest, UpdatePageResponse, UpdateTeamMemberRequest, UpdateTeamMembersDisplayOrderRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LegacyCmsClient(object):
  """CMS = Content Management System"""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_page(self, request: CreatePageRequest = None) -> CmsPage:
    r"""
    Creates a stub of a CMS page (but doesn't save it into the database).

    Args:
      request (CreatePageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreatePageRequest()

    return self._client.call("cms.LegacyCmsService", "CreatePage", request, CmsPage)

  def get_page(self, request: GetPageRequest = None) -> CmsPage:
    r"""
    Gets a page by id or slug.

    Args:
      request (GetPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPageRequest()

    return self._client.call("cms.LegacyCmsService", "GetPage", request, CmsPage)

  def get_pages(self, request: GetPagesRequest = None) -> GetPagesResponse:
    r"""
    Get pages by id.

    Args:
      request (GetPagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPagesRequest()

    return self._client.call("cms.LegacyCmsService", "GetPages", request, GetPagesResponse)

  def list_docs(self, request: ListDocsRequest = None) -> ListDocsResponse:
    r"""
    Lists all of the documentation pages (used by the outline sidebar).

    Args:
      request (ListDocsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListDocsRequest()

    return self._client.call("cms.LegacyCmsService", "ListDocs", request, ListDocsResponse)

  def list_pages(self, request: ListPagesRequest = None) -> ListPagesResponse:
    r"""
    Lists all pages (documentation and regular CMS pages).

    Args:
      request (ListPagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListPagesRequest()

    return self._client.call("cms.LegacyCmsService", "ListPages", request, ListPagesResponse)

  def update_doc_page_order(self, request: UpdateDocPageOrderRequest = None):
    r"""
    Allows an admin to specify where on the documentation main page a doc
    page should appear.

    Args:
      request (UpdateDocPageOrderRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDocPageOrderRequest()

    self._client.call("cms.LegacyCmsService", "UpdateDocPageOrder", request, None)

  def update_page(self, request: UpdatePageRequest = None) -> UpdatePageResponse:
    r"""
    Updates the metadata and content of a CMS/doc page.

    Args:
      request (UpdatePageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdatePageRequest()

    return self._client.call("cms.LegacyCmsService", "UpdatePage", request, UpdatePageResponse)

  def create_team_member(self, request: CreateTeamMemberRequest = None) -> TeamMember:
    r"""
    Creates a new team member.

    Args:
      request (CreateTeamMemberRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTeamMemberRequest()

    return self._client.call("cms.LegacyCmsService", "CreateTeamMember", request, TeamMember)

  def update_team_member(self, request: UpdateTeamMemberRequest = None) -> TeamMember:
    r"""
    Updates a team member.

    Args:
      request (UpdateTeamMemberRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateTeamMemberRequest()

    return self._client.call("cms.LegacyCmsService", "UpdateTeamMember", request, TeamMember)

  def list_team_members(self, request: ListTeamMembersRequest = None) -> ListTeamMembersResponse:
    r"""
    Lists all team members.

    Args:
      request (ListTeamMembersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListTeamMembersRequest()

    return self._client.call("cms.LegacyCmsService", "ListTeamMembers", request, ListTeamMembersResponse)

  def delete_team_member(self, request: DeleteTeamMemberRequest = None):
    r"""
    Deletes a team member.

    Args:
      request (DeleteTeamMemberRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteTeamMemberRequest()

    self._client.call("cms.LegacyCmsService", "DeleteTeamMember", request, None)

  def update_team_members_display_order(self, request: UpdateTeamMembersDisplayOrderRequest = None):
    r"""
    Updates the display order of multiple team members.

    Args:
      request (UpdateTeamMembersDisplayOrderRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateTeamMembersDisplayOrderRequest()

    self._client.call("cms.LegacyCmsService", "UpdateTeamMembersDisplayOrder", request, None)
