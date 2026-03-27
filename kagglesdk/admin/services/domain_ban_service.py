from kagglesdk.admin.types.domain_ban_service import BannedDomain, CreateBannedDomainRequest, DeleteBannedDomainRequest, ListBannedDomainsRequest, ListBannedDomainsResponse, TestDomainRequest, TestDomainResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DomainBanClient(object):
  """Admin service used for banning email domains (i.e. for malicious users)."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_banned_domains(self, request: ListBannedDomainsRequest = None) -> ListBannedDomainsResponse:
    r"""
    Lists all active domain bans that are being enforced.

    Args:
      request (ListBannedDomainsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBannedDomainsRequest()

    return self._client.call("admin.DomainBanService", "ListBannedDomains", request, ListBannedDomainsResponse)

  def create_banned_domain(self, request: CreateBannedDomainRequest = None) -> BannedDomain:
    r"""
    Bans a particular domain.

    Args:
      request (CreateBannedDomainRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBannedDomainRequest()

    return self._client.call("admin.DomainBanService", "CreateBannedDomain", request, BannedDomain)

  def delete_banned_domain(self, request: DeleteBannedDomainRequest = None):
    r"""
    Unbans an existing domain.

    Args:
      request (DeleteBannedDomainRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBannedDomainRequest()

    self._client.call("admin.DomainBanService", "DeleteBannedDomain", request, None)

  def test_domain(self, request: TestDomainRequest = None) -> TestDomainResponse:
    r"""
    Tests a domain to see if it's banned from any of our checks.

    Args:
      request (TestDomainRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TestDomainRequest()

    return self._client.call("admin.DomainBanService", "TestDomain", request, TestDomainResponse)
