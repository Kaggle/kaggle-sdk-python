from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.legacy_organizations_service import GetOrganizationsRequest, GetOrganizationsResponse

class LegacyOrganizationsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_organizations(self, request: GetOrganizationsRequest = None) -> GetOrganizationsResponse:
    r"""
    Fetches organizations for the current user

    Args:
      request (GetOrganizationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOrganizationsRequest()

    return self._client.call("users.LegacyOrganizationsService", "GetOrganizations", request, GetOrganizationsResponse)
