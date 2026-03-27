from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_proxy_internal_service import CreateModelProxyTokenRequest, CreateModelProxyTokenResponse, ListModelBackendsRequest, ListModelBackendsResponse

class ModelProxyInternalClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_model_proxy_token(self, request: CreateModelProxyTokenRequest = None) -> CreateModelProxyTokenResponse:
    r"""
    Args:
      request (CreateModelProxyTokenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateModelProxyTokenRequest()

    return self._client.call("models.ModelProxyInternalService", "CreateModelProxyToken", request, CreateModelProxyTokenResponse)

  def list_model_backends(self, request: ListModelBackendsRequest = None) -> ListModelBackendsResponse:
    r"""
    Args:
      request (ListModelBackendsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListModelBackendsRequest()

    return self._client.call("models.ModelProxyInternalService", "ListModelBackends", request, ListModelBackendsResponse)
