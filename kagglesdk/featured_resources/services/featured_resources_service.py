from kagglesdk.featured_resources.types.featured_resources_service import CreateFeaturedResourceRequest, DeleteFeaturedResourceRequest, FeaturedResource, GetFeaturedResourceRequest, UpdateFeaturedResourceRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class FeaturedResourcesClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_featured_resource(self, request: GetFeaturedResourceRequest = None) -> FeaturedResource:
    r"""
    Args:
      request (GetFeaturedResourceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetFeaturedResourceRequest()

    return self._client.call("featured_resources.FeaturedResourcesService", "GetFeaturedResource", request, FeaturedResource)

  def create_featured_resource(self, request: CreateFeaturedResourceRequest = None) -> FeaturedResource:
    r"""
    Args:
      request (CreateFeaturedResourceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateFeaturedResourceRequest()

    return self._client.call("featured_resources.FeaturedResourcesService", "CreateFeaturedResource", request, FeaturedResource)

  def update_featured_resource(self, request: UpdateFeaturedResourceRequest = None) -> FeaturedResource:
    r"""
    Args:
      request (UpdateFeaturedResourceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateFeaturedResourceRequest()

    return self._client.call("featured_resources.FeaturedResourcesService", "UpdateFeaturedResource", request, FeaturedResource)

  def delete_featured_resource(self, request: DeleteFeaturedResourceRequest = None) -> FeaturedResource:
    r"""
    Args:
      request (DeleteFeaturedResourceRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteFeaturedResourceRequest()

    return self._client.call("featured_resources.FeaturedResourcesService", "DeleteFeaturedResource", request, FeaturedResource)
