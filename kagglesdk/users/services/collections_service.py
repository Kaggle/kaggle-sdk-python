from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.collections_service import CreateCollectionItemsRequest, CreateCollectionRequest, CreateCollectionResponse, DeleteCollectionItemsRequest, DeleteCollectionRequest, ListCollectionsRequest, ListCollectionsResponse, UpdateCollectionRequest

class CollectionsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_collections(self, request: ListCollectionsRequest = None) -> ListCollectionsResponse:
    r"""
    Returns a list of custom collections created by the current user

    Args:
      request (ListCollectionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCollectionsRequest()

    return self._client.call("users.CollectionsService", "ListCollections", request, ListCollectionsResponse)

  def create_collection(self, request: CreateCollectionRequest = None) -> CreateCollectionResponse:
    r"""
    Creates a new collection for the current user

    Args:
      request (CreateCollectionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCollectionRequest()

    return self._client.call("users.CollectionsService", "CreateCollection", request, CreateCollectionResponse)

  def update_collection(self, request: UpdateCollectionRequest = None):
    r"""
    Updates an existing collection created by the current user

    Args:
      request (UpdateCollectionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCollectionRequest()

    self._client.call("users.CollectionsService", "UpdateCollection", request, None)

  def delete_collection(self, request: DeleteCollectionRequest = None):
    r"""
    Deletes an existing collection created by the current user

    Args:
      request (DeleteCollectionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCollectionRequest()

    self._client.call("users.CollectionsService", "DeleteCollection", request, None)

  def create_collection_items(self, request: CreateCollectionItemsRequest = None):
    r"""
    Creates items inside an existing collection created by the current user

    Args:
      request (CreateCollectionItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCollectionItemsRequest()

    self._client.call("users.CollectionsService", "CreateCollectionItems", request, None)

  def delete_collection_items(self, request: DeleteCollectionItemsRequest = None):
    r"""
    Deletes items from an existing collection created by the current user

    Args:
      request (DeleteCollectionItemsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCollectionItemsRequest()

    self._client.call("users.CollectionsService", "DeleteCollectionItems", request, None)
