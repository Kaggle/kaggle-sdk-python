from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.testing.types.test_service import CreateTestAccountRequest, CreateTestAccountResponse, DeleteTestAccountRequest, ListTestAccountsRequest, ListTestAccountsResponse

class TestClient(object):
  """Local-only integration testing service"""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_test_account(self, request: CreateTestAccountRequest = None) -> CreateTestAccountResponse:
    r"""
    Creates an ephemeral test account for e2e testing.
    Returns credentials that can be used to log in as this account.

    Args:
      request (CreateTestAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTestAccountRequest()

    return self._client.call("testing.TestService", "CreateTestAccount", request, CreateTestAccountResponse)

  def delete_test_account(self, request: DeleteTestAccountRequest = None):
    r"""
    Deletes a test account. Only accounts with TestAccount role can be deleted.

    Args:
      request (DeleteTestAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteTestAccountRequest()

    self._client.call("testing.TestService", "DeleteTestAccount", request, None)

  def list_test_accounts(self, request: ListTestAccountsRequest = None) -> ListTestAccountsResponse:
    r"""
    Lists active test accounts. Useful for debugging and cleanup.

    Args:
      request (ListTestAccountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListTestAccountsRequest()

    return self._client.call("testing.TestService", "ListTestAccounts", request, ListTestAccountsResponse)
