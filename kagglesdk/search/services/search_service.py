from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.search.types.search_service import FullSearchResponse, FullSearchWebRequest, GetAutoCompleteSuggestionsRequest, GetAutoCompleteSuggestionsResponse, GetPopularTagsRequest, GetPopularTagsResponse, GetRecentSearchesRequest, GetRecentSearchesResponse, GetTrendingSearchesRequest, GetTrendingSearchesResponse, LogSearchRequest, SuggestedSearchResponse, SuggestedSearchWebRequest

class SearchWebClient(object):
  r"""
  Search is structured such that some handlers live on a service-host container
  and a proxied by web pods, while some handlers live on the actual web
  monolith. Because a ProtoServiceRegistration requires all RPCs to have mapped
  handlers, it's thus necessary to divide these two services so that web pods
  can have their own RPCs while not defining handlers for the proxied requests.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_auto_complete_suggestions(self, request: GetAutoCompleteSuggestionsRequest = None) -> GetAutoCompleteSuggestionsResponse:
    r"""
    Args:
      request (GetAutoCompleteSuggestionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetAutoCompleteSuggestionsRequest()

    return self._client.call("search.SearchWebService", "GetAutoCompleteSuggestions", request, GetAutoCompleteSuggestionsResponse)

  def get_popular_tags(self, request: GetPopularTagsRequest = None) -> GetPopularTagsResponse:
    r"""
    Args:
      request (GetPopularTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPopularTagsRequest()

    return self._client.call("search.SearchWebService", "GetPopularTags", request, GetPopularTagsResponse)

  def get_recent_searches(self, request: GetRecentSearchesRequest = None) -> GetRecentSearchesResponse:
    r"""
    Args:
      request (GetRecentSearchesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetRecentSearchesRequest()

    return self._client.call("search.SearchWebService", "GetRecentSearches", request, GetRecentSearchesResponse)

  def get_trending_searches(self, request: GetTrendingSearchesRequest = None) -> GetTrendingSearchesResponse:
    r"""
    Args:
      request (GetTrendingSearchesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTrendingSearchesRequest()

    return self._client.call("search.SearchWebService", "GetTrendingSearches", request, GetTrendingSearchesResponse)

  def log_search(self, request: LogSearchRequest = None):
    r"""
    Args:
      request (LogSearchRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LogSearchRequest()

    self._client.call("search.SearchWebService", "LogSearch", request, None)

  def full_search_web(self, request: FullSearchWebRequest = None) -> FullSearchResponse:
    r"""
    Args:
      request (FullSearchWebRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FullSearchWebRequest()

    return self._client.call("search.SearchWebService", "FullSearchWeb", request, FullSearchResponse)

  def suggested_search_web(self, request: SuggestedSearchWebRequest = None) -> SuggestedSearchResponse:
    r"""
    Args:
      request (SuggestedSearchWebRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SuggestedSearchWebRequest()

    return self._client.call("search.SearchWebService", "SuggestedSearchWeb", request, SuggestedSearchResponse)
