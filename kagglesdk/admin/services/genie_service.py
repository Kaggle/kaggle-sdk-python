from kagglesdk.admin.types.genie_service import CreateDelegatedUserAccessTokenRequest, CreateDelegatedUserAccessTokenResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class GenieClient(object):
  """Services related exclusively to the 'Genie' admin section."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_delegated_user_access_token(self, request: CreateDelegatedUserAccessTokenRequest = None) -> CreateDelegatedUserAccessTokenResponse:
    r"""
    Create a token that can be used to impersonate another user.

    Args:
      request (CreateDelegatedUserAccessTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDelegatedUserAccessTokenRequest()

    return self._client.call("admin.GenieService", "CreateDelegatedUserAccessToken", request, CreateDelegatedUserAccessTokenResponse)
