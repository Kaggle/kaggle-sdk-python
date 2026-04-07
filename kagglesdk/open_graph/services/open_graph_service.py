from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.open_graph.types.open_graph_service import BatchGetOpenGraphImageMetadataRequest, BatchGetOpenGraphImageMetadataResponse, GetLatestOpenGraphImageMetadataRequest, GetLatestOpenGraphImageMetadataResponse

class OpenGraphClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def batch_get_open_graph_image_metadata(self, request: BatchGetOpenGraphImageMetadataRequest = None) -> BatchGetOpenGraphImageMetadataResponse:
    r"""
    Args:
      request (BatchGetOpenGraphImageMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchGetOpenGraphImageMetadataRequest()

    return self._client.call("open_graph.OpenGraphService", "BatchGetOpenGraphImageMetadata", request, BatchGetOpenGraphImageMetadataResponse)

  def get_latest_open_graph_image_metadata(self, request: GetLatestOpenGraphImageMetadataRequest = None) -> GetLatestOpenGraphImageMetadataResponse:
    r"""
    Fetches the latest OpenGraphImageMetadata for a specified resource

    Args:
      request (GetLatestOpenGraphImageMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLatestOpenGraphImageMetadataRequest()

    return self._client.call("open_graph.OpenGraphService", "GetLatestOpenGraphImageMetadata", request, GetLatestOpenGraphImageMetadataResponse)
