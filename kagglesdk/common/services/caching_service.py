from kagglesdk.common.types.caching_service import InvalidateCacheRequest, InvalidateCacheResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class CachingClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def invalidate_cache(self, request: InvalidateCacheRequest = None) -> InvalidateCacheResponse:
    r"""
    Args:
      request (InvalidateCacheRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateCacheRequest()

    return self._client.call("common.CachingService", "InvalidateCache", request, InvalidateCacheResponse)
