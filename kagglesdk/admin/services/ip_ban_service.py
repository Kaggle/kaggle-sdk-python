from kagglesdk.admin.types.ip_ban_service import CreateIpBanRequest, DeleteIpBanRequest, IpBan, ListIpBansRequest, ListIpBansResponse, TestIpBansRequest, TestIpBansResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class IpBanClient(object):
  """Admin service used for banning IP addresses (i.e. for malicious users)."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_ip_bans(self, request: ListIpBansRequest = None) -> ListIpBansResponse:
    r"""
    Lists all active IP bans that are being enforced.

    Args:
      request (ListIpBansRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListIpBansRequest()

    return self._client.call("admin.IpBanService", "ListIpBans", request, ListIpBansResponse)

  def create_ip_ban(self, request: CreateIpBanRequest = None) -> IpBan:
    r"""
    Bans a particular IP range.

    Args:
      request (CreateIpBanRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateIpBanRequest()

    return self._client.call("admin.IpBanService", "CreateIpBan", request, IpBan)

  def delete_ip_ban(self, request: DeleteIpBanRequest = None):
    r"""
    Unbans an existing IP range.

    Args:
      request (DeleteIpBanRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteIpBanRequest()

    self._client.call("admin.IpBanService", "DeleteIpBan", request, None)

  def test_ip_bans(self, request: TestIpBansRequest = None) -> TestIpBansResponse:
    r"""
    Test to see if IP address(es) is/are banned.

    Args:
      request (TestIpBansRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TestIpBansRequest()

    return self._client.call("admin.IpBanService", "TestIpBans", request, TestIpBansResponse)
