from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional, List, Dict

class CreateIpBanRequest(KaggleObject):
  r"""
  Attributes:
    ip_range (str)
      The exact IPv4 IP (e.g. '1.2.3.4') or a valid CIDR range
      (e.g. '1.2.3.4/24').
    comment (str)
      An optional comment explaining why the ban was performed.
  """

  def __init__(self):
    self._ip_range = ""
    self._comment = None
    self._freeze()

  @property
  def ip_range(self) -> str:
    r"""
    The exact IPv4 IP (e.g. '1.2.3.4') or a valid CIDR range
    (e.g. '1.2.3.4/24').
    """
    return self._ip_range

  @ip_range.setter
  def ip_range(self, ip_range: str):
    if ip_range is None:
      del self.ip_range
      return
    if not isinstance(ip_range, str):
      raise TypeError('ip_range must be of type str')
    self._ip_range = ip_range

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


class DeleteIpBanRequest(KaggleObject):
  r"""
  Attributes:
    ip_ban_id (int)
      The id of the existing ban to delete.
  """

  def __init__(self):
    self._ip_ban_id = 0
    self._freeze()

  @property
  def ip_ban_id(self) -> int:
    """The id of the existing ban to delete."""
    return self._ip_ban_id

  @ip_ban_id.setter
  def ip_ban_id(self, ip_ban_id: int):
    if ip_ban_id is None:
      del self.ip_ban_id
      return
    if not isinstance(ip_ban_id, int):
      raise TypeError('ip_ban_id must be of type int')
    self._ip_ban_id = ip_ban_id


class IpBan(KaggleObject):
  r"""
  Attributes:
    ip_ban_id (int)
      The unique identifier for the ban.
    ip_range (str)
      The exact IPv4 IP (e.g. '1.2.3.4') or a valid CIDR range
      (e.g. '1.2.3.4/24').
    creator_username (str)
      The Kaggle (admin) username who banned the IP range.
    comment (str)
      An optional comment explaining why the ban was performed.
    create_time (datetime)
      The absolute point in time when the IP ban was created.
  """

  def __init__(self):
    self._ip_ban_id = 0
    self._ip_range = ""
    self._creator_username = ""
    self._comment = ""
    self._create_time = None
    self._freeze()

  @property
  def ip_ban_id(self) -> int:
    """The unique identifier for the ban."""
    return self._ip_ban_id

  @ip_ban_id.setter
  def ip_ban_id(self, ip_ban_id: int):
    if ip_ban_id is None:
      del self.ip_ban_id
      return
    if not isinstance(ip_ban_id, int):
      raise TypeError('ip_ban_id must be of type int')
    self._ip_ban_id = ip_ban_id

  @property
  def ip_range(self) -> str:
    r"""
    The exact IPv4 IP (e.g. '1.2.3.4') or a valid CIDR range
    (e.g. '1.2.3.4/24').
    """
    return self._ip_range

  @ip_range.setter
  def ip_range(self, ip_range: str):
    if ip_range is None:
      del self.ip_range
      return
    if not isinstance(ip_range, str):
      raise TypeError('ip_range must be of type str')
    self._ip_range = ip_range

  @property
  def creator_username(self) -> str:
    """The Kaggle (admin) username who banned the IP range."""
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
    return self._comment

  @comment.setter
  def comment(self, comment: str):
    if comment is None:
      del self.comment
      return
    if not isinstance(comment, str):
      raise TypeError('comment must be of type str')
    self._comment = comment

  @property
  def create_time(self) -> datetime:
    """The absolute point in time when the IP ban was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time


class ListIpBansRequest(KaggleObject):
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


class ListIpBansResponse(KaggleObject):
  r"""
  Attributes:
    ip_bans (IpBan)
      A list of all active IP bans.
    next_page_token (str)
      Token to retrieve the next page of results, or empty if there are no more
      results in the list.
  """

  def __init__(self):
    self._ip_bans = []
    self._next_page_token = ""
    self._freeze()

  @property
  def ip_bans(self) -> Optional[List[Optional['IpBan']]]:
    """A list of all active IP bans."""
    return self._ip_bans

  @ip_bans.setter
  def ip_bans(self, ip_bans: Optional[List[Optional['IpBan']]]):
    if ip_bans is None:
      del self.ip_bans
      return
    if not isinstance(ip_bans, list):
      raise TypeError('ip_bans must be of type list')
    if not all([isinstance(t, IpBan) for t in ip_bans]):
      raise TypeError('ip_bans must contain only items of type IpBan')
    self._ip_bans = ip_bans

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


class TestIpBansRequest(KaggleObject):
  r"""
  Attributes:
    ips (str)
      The IP address(es) (separated by spaces or commas) to test to see if
      they're banned.
  """

  def __init__(self):
    self._ips = ""
    self._freeze()

  @property
  def ips(self) -> str:
    r"""
    The IP address(es) (separated by spaces or commas) to test to see if
    they're banned.
    """
    return self._ips

  @ips.setter
  def ips(self, ips: str):
    if ips is None:
      del self.ips
      return
    if not isinstance(ips, str):
      raise TypeError('ips must be of type str')
    self._ips = ips


class TestIpBansResponse(KaggleObject):
  r"""
  Attributes:
    ip_bans (IpBan)
      Maps between the parsed IP(s) from the request to its existing IpBan if it
      exists. If it doesn't exist, an empty IpBan (with id 0) will be returned.
  """

  def __init__(self):
    self._ip_bans = {}
    self._freeze()

  @property
  def ip_bans(self) -> Optional[Dict[str, Optional['IpBan']]]:
    r"""
    Maps between the parsed IP(s) from the request to its existing IpBan if it
    exists. If it doesn't exist, an empty IpBan (with id 0) will be returned.
    """
    return self._ip_bans

  @ip_bans.setter
  def ip_bans(self, ip_bans: Optional[Dict[str, Optional['IpBan']]]):
    if ip_bans is None:
      del self.ip_bans
      return
    if not isinstance(ip_bans, dict):
      raise TypeError('ip_bans must be of type dict')
    if not all([isinstance(v, IpBan) for k, v in ip_bans]):
      raise TypeError('ip_bans must contain only items of type IpBan')
    self._ip_bans = ip_bans


CreateIpBanRequest._fields = [
  FieldMetadata("ipRange", "ip_range", "_ip_range", str, "", PredefinedSerializer()),
  FieldMetadata("comment", "comment", "_comment", str, None, PredefinedSerializer(), optional=True),
]

DeleteIpBanRequest._fields = [
  FieldMetadata("ipBanId", "ip_ban_id", "_ip_ban_id", int, 0, PredefinedSerializer()),
]

IpBan._fields = [
  FieldMetadata("ipBanId", "ip_ban_id", "_ip_ban_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ipRange", "ip_range", "_ip_range", str, "", PredefinedSerializer()),
  FieldMetadata("creatorUsername", "creator_username", "_creator_username", str, "", PredefinedSerializer()),
  FieldMetadata("comment", "comment", "_comment", str, "", PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
]

ListIpBansRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ListIpBansResponse._fields = [
  FieldMetadata("ipBans", "ip_bans", "_ip_bans", IpBan, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

TestIpBansRequest._fields = [
  FieldMetadata("ips", "ips", "_ips", str, "", PredefinedSerializer()),
]

TestIpBansResponse._fields = [
  FieldMetadata("ipBans", "ip_bans", "_ip_bans", IpBan, {}, MapSerializer(KaggleObjectSerializer())),
]

