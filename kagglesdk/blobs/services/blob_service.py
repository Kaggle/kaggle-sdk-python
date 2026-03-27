from kagglesdk.blobs.types.blob_service import StartBlobUploadRequest, StartBlobUploadResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BlobClient(object):
  r"""
  Binary Large OBject (BLOB) service used for uploading files to Google Cloud
  Storage (GCS).
  """

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def start_blob_upload(self, request: StartBlobUploadRequest = None) -> StartBlobUploadResponse:
    r"""
    Starts a blob upload (i.e. reserves a spot for the upload on GCS).

    Args:
      request (StartBlobUploadRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = StartBlobUploadRequest()

    return self._client.call("blobs.BlobService", "StartBlobUpload", request, StartBlobUploadResponse)
