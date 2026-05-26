from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.common.types.operations import Operation
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.kernels.types.kernels_api_service import ApiCancelKernelSessionRequest, ApiCancelKernelSessionResponse, ApiCreateKernelSessionRequest, ApiDeleteKernelRequest, ApiDeleteKernelResponse, ApiDownloadKernelOutputRequest, ApiDownloadKernelOutputZipRequest, ApiGetAcceleratorQuotaStatisticsRequest, ApiGetAcceleratorQuotaStatisticsResponse, ApiGetKernelRequest, ApiGetKernelResponse, ApiGetKernelSessionLogsStreamRequest, ApiGetKernelSessionStatusRequest, ApiGetKernelSessionStatusResponse, ApiListKernelFilesRequest, ApiListKernelFilesResponse, ApiListKernelSessionOutputRequest, ApiListKernelSessionOutputResponse, ApiListKernelsRequest, ApiListKernelsResponse, ApiSaveKernelRequest, ApiSaveKernelResponse

class KernelsApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_kernels(self, request: ApiListKernelsRequest = None) -> ApiListKernelsResponse:
    r"""
    Args:
      request (ApiListKernelsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelsRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernels", request, ApiListKernelsResponse)

  def list_kernel_files(self, request: ApiListKernelFilesRequest = None) -> ApiListKernelFilesResponse:
    r"""
    Args:
      request (ApiListKernelFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelFilesRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernelFiles", request, ApiListKernelFilesResponse)

  def get_kernel(self, request: ApiGetKernelRequest = None) -> ApiGetKernelResponse:
    r"""
    Args:
      request (ApiGetKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetKernelRequest()

    return self._client.call("kernels.KernelsApiService", "GetKernel", request, ApiGetKernelResponse)

  def save_kernel(self, request: ApiSaveKernelRequest = None) -> ApiSaveKernelResponse:
    r"""
    Args:
      request (ApiSaveKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiSaveKernelRequest()

    return self._client.call("kernels.KernelsApiService", "SaveKernel", request, ApiSaveKernelResponse)

  def list_kernel_session_output(self, request: ApiListKernelSessionOutputRequest = None) -> ApiListKernelSessionOutputResponse:
    r"""
    Args:
      request (ApiListKernelSessionOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelSessionOutputRequest()

    return self._client.call("kernels.KernelsApiService", "ListKernelSessionOutput", request, ApiListKernelSessionOutputResponse)

  def get_kernel_session_status(self, request: ApiGetKernelSessionStatusRequest = None) -> ApiGetKernelSessionStatusResponse:
    r"""
    Args:
      request (ApiGetKernelSessionStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetKernelSessionStatusRequest()

    return self._client.call("kernels.KernelsApiService", "GetKernelSessionStatus", request, ApiGetKernelSessionStatusResponse)

  def download_kernel_output(self, request: ApiDownloadKernelOutputRequest = None) -> HttpRedirect:
    r"""
    Meant for use by Kaggle Hub (http bindings and terminology align with that)

    Args:
      request (ApiDownloadKernelOutputRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadKernelOutputRequest()

    return self._client.call("kernels.KernelsApiService", "DownloadKernelOutput", request, HttpRedirect)

  def download_kernel_output_zip(self, request: ApiDownloadKernelOutputZipRequest = None) -> FileDownload:
    r"""
    Meant for use by Kaggle Hub (and DownloadKernelOutput above)

    Args:
      request (ApiDownloadKernelOutputZipRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadKernelOutputZipRequest()

    return self._client.call("kernels.KernelsApiService", "DownloadKernelOutputZip", request, FileDownload)

  def delete_kernel(self, request: ApiDeleteKernelRequest = None) -> ApiDeleteKernelResponse:
    r"""
    Args:
      request (ApiDeleteKernelRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteKernelRequest()

    return self._client.call("kernels.KernelsApiService", "DeleteKernel", request, ApiDeleteKernelResponse)

  def cancel_kernel_session(self, request: ApiCancelKernelSessionRequest = None) -> ApiCancelKernelSessionResponse:
    r"""
    Args:
      request (ApiCancelKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCancelKernelSessionRequest()

    return self._client.call("kernels.KernelsApiService", "CancelKernelSession", request, ApiCancelKernelSessionResponse)

  def create_kernel_session(self, request: ApiCreateKernelSessionRequest = None) -> Operation:
    r"""
    Args:
      request (ApiCreateKernelSessionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateKernelSessionRequest()

    return self._client.call("kernels.KernelsApiService", "CreateKernelSession", request, Operation)

  def get_kernel_session_logs_stream(self, request: ApiGetKernelSessionLogsStreamRequest = None) -> FileDownload:
    r"""
    Streams the log output of a notebook session.

    While the session is running (or shortly after), the midtier proxies
    to the per-session log endpoint published by the session manager and
    returns Server-Sent Events (Content-Type: text/event-stream) until the
    upstream sends an `END_OF_LOG` sentinel or the client disconnects.

    If the session has already terminated by the time the request arrives,
    the live stream URL is no longer available; the midtier instead returns
    the persisted log file as written by the worker (Content-Type:
    application/json). Callers should branch on the response Content-Type.

    Args:
      request (ApiGetKernelSessionLogsStreamRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetKernelSessionLogsStreamRequest()

    return self._client.call("kernels.KernelsApiService", "GetKernelSessionLogsStream", request, FileDownload)

  def get_accelerator_quota_statistics(self, request: ApiGetAcceleratorQuotaStatisticsRequest = None) -> ApiGetAcceleratorQuotaStatisticsResponse:
    r"""
    Args:
      request (ApiGetAcceleratorQuotaStatisticsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetAcceleratorQuotaStatisticsRequest()

    return self._client.call("kernels.KernelsApiService", "GetAcceleratorQuotaStatistics", request, ApiGetAcceleratorQuotaStatisticsResponse)
