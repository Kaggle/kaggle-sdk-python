from kagglesdk.discussions.types.writeups_api_service import ApiGetResolvedWriteUpLinksRequest, ApiGetResolvedWriteUpLinksResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class WriteUpsApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_resolved_write_up_links(self, request: ApiGetResolvedWriteUpLinksRequest = None) -> ApiGetResolvedWriteUpLinksResponse:
    r"""
    Args:
      request (ApiGetResolvedWriteUpLinksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetResolvedWriteUpLinksRequest()

    return self._client.call("discussions.WriteUpsApiService", "GetResolvedWriteUpLinks", request, ApiGetResolvedWriteUpLinksResponse)
