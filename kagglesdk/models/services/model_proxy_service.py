from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.models.types.model_proxy_service import GetModelProxyQuotaRequest, GetModelProxyQuotaResponse, GetModelProxyQuotasRequest, GetModelProxyQuotasResponse

class ModelProxyClient(object):
  r"""
  This service is for external facing endpoints. See ModelProxyInternalService
  for internal-only endpoints.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_model_proxy_quota(self, request: GetModelProxyQuotaRequest = None) -> GetModelProxyQuotaResponse:
    r"""
    Returns Model Proxy quota information for the most restrictive quota for
    the current user.

    Args:
      request (GetModelProxyQuotaRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelProxyQuotaRequest()

    return self._client.call("models.ModelProxyService", "GetModelProxyQuota", request, GetModelProxyQuotaResponse)

  def get_model_proxy_quotas(self, request: GetModelProxyQuotasRequest = None) -> GetModelProxyQuotasResponse:
    r"""
    Returns Model Proxy quota information for all quotas for the given user.
    If no user is given, defaults to current user.

    Args:
      request (GetModelProxyQuotasRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetModelProxyQuotasRequest()

    return self._client.call("models.ModelProxyService", "GetModelProxyQuotas", request, GetModelProxyQuotasResponse)
