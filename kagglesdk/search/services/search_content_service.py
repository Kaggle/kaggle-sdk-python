from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.search.types.search_content_service import ListSearchContentRequest, ListSearchContentResponse

class SearchContentClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_search_content(self, request: ListSearchContentRequest = None) -> ListSearchContentResponse:
    r"""
    Returns a list of search-backed content using the provide filters/sort

    Args:
      request (ListSearchContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListSearchContentRequest()

    return self._client.call("search.SearchContentService", "ListSearchContent", request, ListSearchContentResponse)
