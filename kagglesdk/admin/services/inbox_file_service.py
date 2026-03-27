from kagglesdk.admin.types.inbox_file_service import CreateInboxFileRequest, CreateInboxFileResponse, DeleteInboxFileRequest, ListInboxFilesRequest, ListInboxFilesResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class InboxFileClient(object):
  """File drop/pickup functionality."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_inbox_file(self, request: CreateInboxFileRequest = None) -> CreateInboxFileResponse:
    r"""
    Creates (aka 'drops') a new file into the inbox.

    Args:
      request (CreateInboxFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateInboxFileRequest()

    return self._client.call("admin.InboxFileService", "CreateInboxFile", request, CreateInboxFileResponse)

  def list_inbox_files(self, request: ListInboxFilesRequest = None) -> ListInboxFilesResponse:
    r"""
    Lists all available inbox files (optionally filtering to just a specific
    directory)

    Args:
      request (ListInboxFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListInboxFilesRequest()

    return self._client.call("admin.InboxFileService", "ListInboxFiles", request, ListInboxFilesResponse)

  def delete_inbox_file(self, request: DeleteInboxFileRequest = None):
    r"""
    Deletes an existing inbox file.

    Args:
      request (DeleteInboxFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteInboxFileRequest()

    self._client.call("admin.InboxFileService", "DeleteInboxFile", request, None)
