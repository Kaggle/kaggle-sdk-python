from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class DomainType(enum.Enum):
  DOMAIN_TYPE_UNSPECIFIED = 0
  DOMAIN_TYPE_EMAIL = 1
  """Raw email domain to check against the user-provided email address"""
  DOMAIN_TYPE_MX = 2
  """Mail Exchange"""
  DOMAIN_TYPE_SOA = 3
  """Start of Authority"""
  DOMAIN_TYPE_MX_A = 4
  """IPv4 address of MX"""
  DOMAIN_TYPE_MX_A_PTR = 5
  """Domain which is a reverse lookup of MX-A"""
  DOMAIN_TYPE_MX_MX = 6
  """MX for the MX domain"""

class BannedDomain(KaggleObject):
  r"""
  Attributes:
    id (int)
    domain (str)
      The domain OR IPv4 address of the domain that is banned.
    domain_type (DomainType)
      Type of domain.
    creator_username (str)
      The Kaggle (admin) username who banned the domain.
    comment (str)
      An optional comment explaining why the ban was performed.
    create_time (datetime)
      The absolute point in time when the domain ban was created.
  """

  def __init__(self):
    self._id = 0
    self._domain = ""
    self._domain_type = DomainType.DOMAIN_TYPE_UNSPECIFIED
    self._creator_username = ""
    self._comment = None
    self._create_time = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def domain(self) -> str:
    """The domain OR IPv4 address of the domain that is banned."""
    return self._domain

  @domain.setter
  def domain(self, domain: str):
    if domain is None:
      del self.domain
      return
    if not isinstance(domain, str):
      raise TypeError('domain must be of type str')
    self._domain = domain

  @property
  def domain_type(self) -> 'DomainType':
    """Type of domain."""
    return self._domain_type

  @domain_type.setter
  def domain_type(self, domain_type: 'DomainType'):
    if domain_type is None:
      del self.domain_type
      return
    if not isinstance(domain_type, DomainType):
      raise TypeError('domain_type must be of type DomainType')
    self._domain_type = domain_type

  @property
  def creator_username(self) -> str:
    """The Kaggle (admin) username who banned the domain."""
    return self._creator_username

  @creator_username.setter
  def creator_username(self, creator_username: str):
    if creator_username is None:
      del self.creator_username
      return
    if not isinstance(creator_username, str):
      raise TypeError('creator_username must be of type str')
    self._creator_username = creator_username

  @property
  def comment(self) -> str:
    """An optional comment explaining why the ban was performed."""
    return self._comment or ""

  @comment.setter
  def comment(self, comment: Optional[str]):
    if comment is None:
      del self.comment
      return
    if not isinstance(comment, str):
      raise TypeError('comment must be of type str')
    self._comment = comment

  @property
  def create_time(self) -> datetime:
    """The absolute point in time when the domain ban was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time


class CreateBannedDomainRequest(KaggleObject):
  r"""
  Attributes:
    domain (str)
      The domain OR IPv4 address of the domain to ban.
    domain_type (DomainType)
      Type of domain.
    comment (str)
      An optional comment explaining why the ban was performed.
  """

  def __init__(self):
    self._domain = ""
    self._domain_type = DomainType.DOMAIN_TYPE_UNSPECIFIED
    self._comment = None
    self._freeze()

  @property
  def domain(self) -> str:
    """The domain OR IPv4 address of the domain to ban."""
    return self._domain

  @domain.setter
  def domain(self, domain: str):
    if domain is None:
      del self.domain
      return
    if not isinstance(domain, str):
      raise TypeError('domain must be of type str')
    self._domain = domain

  @property
  def domain_type(self) -> 'DomainType':
    """Type of domain."""
    return self._domain_type

  @domain_type.setter
  def domain_type(self, domain_type: 'DomainType'):
    if domain_type is None:
      del self.domain_type
      return
    if not isinstance(domain_type, DomainType):
      raise TypeError('domain_type must be of type DomainType')
    self._domain_type = domain_type

  @property
  def comment(self) -> str:
    """An optional comment explaining why the ban was performed."""
    return self._comment or ""

  @comment.setter
  def comment(self, comment: Optional[str]):
    if comment is None:
      del self.comment
      return
    if not isinstance(comment, str):
      raise TypeError('comment must be of type str')
    self._comment = comment


class DeleteBannedDomainRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the existing ban to delete.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the existing ban to delete."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class ListBannedDomainsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
      The maximum number of bans to return.
    page_token (str)
      The `next_page_token` value returned from a previous request, if any.
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = ""
    self._freeze()

  @property
  def page_size(self) -> int:
    """The maximum number of bans to return."""
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    """The `next_page_token` value returned from a previous request, if any."""
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListBannedDomainsResponse(KaggleObject):
  r"""
  Attributes:
    banned_domains (BannedDomain)
      A list of all active domain bans.
    next_page_token (str)
      Token to retrieve the next page of results, or empty if there are no more
      results in the list.
  """

  def __init__(self):
    self._banned_domains = []
    self._next_page_token = ""
    self._freeze()

  @property
  def banned_domains(self) -> Optional[List[Optional['BannedDomain']]]:
    """A list of all active domain bans."""
    return self._banned_domains

  @banned_domains.setter
  def banned_domains(self, banned_domains: Optional[List[Optional['BannedDomain']]]):
    if banned_domains is None:
      del self.banned_domains
      return
    if not isinstance(banned_domains, list):
      raise TypeError('banned_domains must be of type list')
    if not all([isinstance(t, BannedDomain) for t in banned_domains]):
      raise TypeError('banned_domains must contain only items of type BannedDomain')
    self._banned_domains = banned_domains

  @property
  def next_page_token(self) -> str:
    r"""
    Token to retrieve the next page of results, or empty if there are no more
    results in the list.
    """
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class TestDomainRequest(KaggleObject):
  r"""
  Attributes:
    domain (str)
      The domain OR IPv4 address of the domain to test.
  """

  def __init__(self):
    self._domain = ""
    self._freeze()

  @property
  def domain(self) -> str:
    """The domain OR IPv4 address of the domain to test."""
    return self._domain

  @domain.setter
  def domain(self, domain: str):
    if domain is None:
      del self.domain
      return
    if not isinstance(domain, str):
      raise TypeError('domain must be of type str')
    self._domain = domain


class TestDomainResponse(KaggleObject):
  r"""
  Attributes:
    is_banned (bool)
    details (str)
  """

  def __init__(self):
    self._is_banned = False
    self._details = ""
    self._freeze()

  @property
  def is_banned(self) -> bool:
    return self._is_banned

  @is_banned.setter
  def is_banned(self, is_banned: bool):
    if is_banned is None:
      del self.is_banned
      return
    if not isinstance(is_banned, bool):
      raise TypeError('is_banned must be of type bool')
    self._is_banned = is_banned

  @property
  def details(self) -> str:
    return self._details

  @details.setter
  def details(self, details: str):
    if details is None:
      del self.details
      return
    if not isinstance(details, str):
      raise TypeError('details must be of type str')
    self._details = details


BannedDomain._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("domain", "domain", "_domain", str, "", PredefinedSerializer()),
  FieldMetadata("domainType", "domain_type", "_domain_type", DomainType, DomainType.DOMAIN_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("creatorUsername", "creator_username", "_creator_username", str, "", PredefinedSerializer()),
  FieldMetadata("comment", "comment", "_comment", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
]

CreateBannedDomainRequest._fields = [
  FieldMetadata("domain", "domain", "_domain", str, "", PredefinedSerializer()),
  FieldMetadata("domainType", "domain_type", "_domain_type", DomainType, DomainType.DOMAIN_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("comment", "comment", "_comment", str, None, PredefinedSerializer(), optional=True),
]

DeleteBannedDomainRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

ListBannedDomainsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ListBannedDomainsResponse._fields = [
  FieldMetadata("bannedDomains", "banned_domains", "_banned_domains", BannedDomain, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

TestDomainRequest._fields = [
  FieldMetadata("domain", "domain", "_domain", str, "", PredefinedSerializer()),
]

TestDomainResponse._fields = [
  FieldMetadata("isBanned", "is_banned", "_is_banned", bool, False, PredefinedSerializer()),
  FieldMetadata("details", "details", "_details", str, "", PredefinedSerializer()),
]

