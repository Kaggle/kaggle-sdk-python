from kagglesdk.competitions.types.page import Page
from kagglesdk.competitions.types.page_service import CreatePageRequest, DeletePageRequest, GetPageRequest, ListPagesRequest, ListPagesResponse, SwapPageOrdersRequest, UpdatePageRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class PageClient(object):
  r"""
  TODO(b/406292857): This service handles pages for Competitions and
  Benchmarks, and has a lot of overlap with CMS page handlers. We should unify
  all 3 in a shared location.
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_page(self, request: GetPageRequest = None) -> Page:
    r"""
    Args:
      request (GetPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetPageRequest()

    return self._client.call("competitions.PageService", "GetPage", request, Page)

  def list_pages(self, request: ListPagesRequest = None) -> ListPagesResponse:
    r"""
    Args:
      request (ListPagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListPagesRequest()

    return self._client.call("competitions.PageService", "ListPages", request, ListPagesResponse)

  def create_page(self, request: CreatePageRequest = None) -> Page:
    r"""
    Args:
      request (CreatePageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreatePageRequest()

    return self._client.call("competitions.PageService", "CreatePage", request, Page)

  def update_page(self, request: UpdatePageRequest = None) -> Page:
    r"""
    Args:
      request (UpdatePageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdatePageRequest()

    return self._client.call("competitions.PageService", "UpdatePage", request, Page)

  def delete_page(self, request: DeletePageRequest = None):
    r"""
    Args:
      request (DeletePageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeletePageRequest()

    self._client.call("competitions.PageService", "DeletePage", request, None)

  def swap_page_orders(self, request: SwapPageOrdersRequest = None):
    r"""
    Args:
      request (SwapPageOrdersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SwapPageOrdersRequest()

    self._client.call("competitions.PageService", "SwapPageOrders", request, None)
