from kagglesdk.admin.types.organizations_service import AddOrganizationMemberRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class OrganizationsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def add_organization_member(self, request: AddOrganizationMemberRequest = None):
    r"""
    Adds a user to an organization by user name or user ID

    Args:
      request (AddOrganizationMemberRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddOrganizationMemberRequest()

    self._client.call("admin.OrganizationsService", "AddOrganizationMember", request, None)
