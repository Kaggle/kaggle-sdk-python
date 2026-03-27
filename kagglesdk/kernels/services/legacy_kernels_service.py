from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.kernels.types.legacy_kernels_service import GetKernelViewModelRequest, GetKernelViewModelResponse

class LegacyKernelsClient(object):
  r"""
  These RPCs are implemented in Kaggle.Services.Legacy due to dependency
  issues:
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_kernel_view_model(self, request: GetKernelViewModelRequest = None) -> GetKernelViewModelResponse:
    r"""
    Args:
      request (GetKernelViewModelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetKernelViewModelRequest()

    return self._client.call("kernels.LegacyKernelsService", "GetKernelViewModel", request, GetKernelViewModelResponse)
