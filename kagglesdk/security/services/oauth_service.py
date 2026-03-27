from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.security.types.oauth_service import CreateOAuthClientRequest, DeleteOAuthClientRequest, FinalizeOAuthFlowRequest, FinalizeOAuthFlowResponse, GetOAuthClientRequest, GetOAuthFlowInfoRequest, ListOAuthClientsRequest, ListOAuthClientsResponse, OAuthFlowInfo, UpdateOAuthClientRequest
from kagglesdk.security.types.security_types import OAuthClient

class OAuthClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_oauth_flow_info(self, request: GetOAuthFlowInfoRequest = None) -> OAuthFlowInfo:
    r"""
    Args:
      request (GetOAuthFlowInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOAuthFlowInfoRequest()

    return self._client.call("security.OAuthService", "GetOAuthFlowInfo", request, OAuthFlowInfo)

  def finalize_oauth_flow(self, request: FinalizeOAuthFlowRequest = None) -> FinalizeOAuthFlowResponse:
    r"""
    Args:
      request (FinalizeOAuthFlowRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FinalizeOAuthFlowRequest()

    return self._client.call("security.OAuthService", "FinalizeOAuthFlow", request, FinalizeOAuthFlowResponse)

  def create_oauth_client(self, request: CreateOAuthClientRequest = None) -> OAuthClient:
    r"""
    Args:
      request (CreateOAuthClientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateOAuthClientRequest()

    return self._client.call("security.OAuthService", "CreateOAuthClient", request, OAuthClient)

  def get_oauth_client(self, request: GetOAuthClientRequest = None) -> OAuthClient:
    r"""
    Args:
      request (GetOAuthClientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOAuthClientRequest()

    return self._client.call("security.OAuthService", "GetOAuthClient", request, OAuthClient)

  def list_oauth_clients(self, request: ListOAuthClientsRequest = None) -> ListOAuthClientsResponse:
    r"""
    Args:
      request (ListOAuthClientsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListOAuthClientsRequest()

    return self._client.call("security.OAuthService", "ListOAuthClients", request, ListOAuthClientsResponse)

  def update_oauth_client(self, request: UpdateOAuthClientRequest = None) -> OAuthClient:
    r"""
    Args:
      request (UpdateOAuthClientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOAuthClientRequest()

    return self._client.call("security.OAuthService", "UpdateOAuthClient", request, OAuthClient)

  def delete_oauth_client(self, request: DeleteOAuthClientRequest = None):
    r"""
    Args:
      request (DeleteOAuthClientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteOAuthClientRequest()

    self._client.call("security.OAuthService", "DeleteOAuthClient", request, None)
