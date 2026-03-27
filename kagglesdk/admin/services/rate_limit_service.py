from kagglesdk.admin.types.rate_limit_service import BatchResetRateLimitStatusesRequest, BatchResetRateLimitStatusesResponse, ListRateLimitsRequest, ListRateLimitsResponse, ListRateLimitStatusesRequest, ListRateLimitStatusesResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class RateLimitClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_rate_limits(self, request: ListRateLimitsRequest = None) -> ListRateLimitsResponse:
    r"""
    Lists rate limit definitions.

    Args:
      request (ListRateLimitsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListRateLimitsRequest()

    return self._client.call("admin.RateLimitService", "ListRateLimits", request, ListRateLimitsResponse)

  def list_rate_limit_statuses(self, request: ListRateLimitStatusesRequest = None) -> ListRateLimitStatusesResponse:
    r"""
    Lists all rate limits statuses (that optionally match filters).

    Args:
      request (ListRateLimitStatusesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListRateLimitStatusesRequest()

    return self._client.call("admin.RateLimitService", "ListRateLimitStatuses", request, ListRateLimitStatusesResponse)

  def batch_reset_rate_limit_statuses(self, request: BatchResetRateLimitStatusesRequest = None) -> BatchResetRateLimitStatusesResponse:
    r"""
    Resets multiple rate limit statuses.

    Args:
      request (BatchResetRateLimitStatusesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchResetRateLimitStatusesRequest()

    return self._client.call("admin.RateLimitService", "BatchResetRateLimitStatuses", request, BatchResetRateLimitStatusesResponse)
