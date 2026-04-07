from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.bookmark_service import CreateBookmarkRequest, CreateBookmarkResponse, DeleteBookmarkRequest, DeleteBookmarkResponse, ListAllBookmarksRequest, ListAllBookmarksResponse

class BookmarkClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_bookmark(self, request: CreateBookmarkRequest = None) -> CreateBookmarkResponse:
    r"""
    Create bookmark of a given type from an entity ID for the current user

    Args:
      request (CreateBookmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBookmarkRequest()

    return self._client.call("users.BookmarkService", "CreateBookmark", request, CreateBookmarkResponse)

  def delete_bookmark(self, request: DeleteBookmarkRequest = None) -> DeleteBookmarkResponse:
    r"""
    Delete bookmark using bookmark_id, referring to the Bookmark entity for
    current user

    Args:
      request (DeleteBookmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBookmarkRequest()

    return self._client.call("users.BookmarkService", "DeleteBookmark", request, DeleteBookmarkResponse)

  def list_all_bookmarks(self, request: ListAllBookmarksRequest = None) -> ListAllBookmarksResponse:
    r"""
    List all bookmarks for the current user, publicly visible

    Args:
      request (ListAllBookmarksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListAllBookmarksRequest()

    return self._client.call("users.BookmarkService", "ListAllBookmarks", request, ListAllBookmarksResponse)
