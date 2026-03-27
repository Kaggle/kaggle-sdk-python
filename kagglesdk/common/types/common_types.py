import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class KaggleEntityType(enum.Enum):
  r"""
  This is a moderation-specific enum and its values correspond to rows in the
  ModerationEntityTypes table so make sure to prepare a database migration to
  insert a new row to that table if you add a new value here.
  Consider using kaggle.security.ResourceType if you want a way to handle
  multiple resources types in a generic way.
  """
  KAGGLE_ENTITY_TYPE_UNSPECIFIED = 0
  """LINT.IfChange"""
  USER = 1
  FORUM_MESSAGE = 2
  FORUM_TOPIC = 3
  COMPETITION = 4
  NOTEBOOK = 5
  DATASET = 6
  TEAM = 7
  ORGANIZATION = 8
  MODEL = 9
  DATASET_SUGGESTION_BUNDLE = 10
  MODEL_INSTANCE = 11
  GROUP = 12
  BENCHMARK = 13
  USER_ATTRIBUTE = 14
  RESOURCE_REFERENCE = 15
  BENCHMARK_TASK = 16

class PageMessageType(enum.Enum):
  ERROR = 0
  INFO = 1
  WARNING = 2
  SUCCESS = 3
  SITE = 4

class Category(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    full_path (str)
    listing_url (str)
    description (str)
    is_inherited (bool)
    dataset_count (int)
    competition_count (int)
    script_count (int)
    total_count (int)
    tag_url (str)
  """

  def __init__(self):
    self._id = 0
    self._name = None
    self._full_path = None
    self._listing_url = None
    self._description = None
    self._is_inherited = False
    self._dataset_count = 0
    self._competition_count = 0
    self._script_count = 0
    self._total_count = 0
    self._tag_url = None
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
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def full_path(self) -> str:
    return self._full_path or ""

  @full_path.setter
  def full_path(self, full_path: Optional[str]):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def listing_url(self) -> str:
    return self._listing_url or ""

  @listing_url.setter
  def listing_url(self, listing_url: Optional[str]):
    if listing_url is None:
      del self.listing_url
      return
    if not isinstance(listing_url, str):
      raise TypeError('listing_url must be of type str')
    self._listing_url = listing_url

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def is_inherited(self) -> bool:
    return self._is_inherited

  @is_inherited.setter
  def is_inherited(self, is_inherited: bool):
    if is_inherited is None:
      del self.is_inherited
      return
    if not isinstance(is_inherited, bool):
      raise TypeError('is_inherited must be of type bool')
    self._is_inherited = is_inherited

  @property
  def dataset_count(self) -> int:
    return self._dataset_count

  @dataset_count.setter
  def dataset_count(self, dataset_count: int):
    if dataset_count is None:
      del self.dataset_count
      return
    if not isinstance(dataset_count, int):
      raise TypeError('dataset_count must be of type int')
    self._dataset_count = dataset_count

  @property
  def competition_count(self) -> int:
    return self._competition_count

  @competition_count.setter
  def competition_count(self, competition_count: int):
    if competition_count is None:
      del self.competition_count
      return
    if not isinstance(competition_count, int):
      raise TypeError('competition_count must be of type int')
    self._competition_count = competition_count

  @property
  def script_count(self) -> int:
    return self._script_count

  @script_count.setter
  def script_count(self, script_count: int):
    if script_count is None:
      del self.script_count
      return
    if not isinstance(script_count, int):
      raise TypeError('script_count must be of type int')
    self._script_count = script_count

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def tag_url(self) -> str:
    return self._tag_url or ""

  @tag_url.setter
  def tag_url(self, tag_url: Optional[str]):
    if tag_url is None:
      del self.tag_url
      return
    if not isinstance(tag_url, str):
      raise TypeError('tag_url must be of type str')
    self._tag_url = tag_url


class DiskUsageLimits(KaggleObject):
  r"""
  Attributes:
    public_limits (DiskUsagePublicLimits)
    private_quota (DiskUsagePrivateLimits)
    max_files (int)
  """

  def __init__(self):
    self._public_limits = None
    self._private_quota = None
    self._max_files = 0
    self._freeze()

  @property
  def public_limits(self) -> Optional['DiskUsagePublicLimits']:
    return self._public_limits

  @public_limits.setter
  def public_limits(self, public_limits: Optional['DiskUsagePublicLimits']):
    if public_limits is None:
      del self.public_limits
      return
    if not isinstance(public_limits, DiskUsagePublicLimits):
      raise TypeError('public_limits must be of type DiskUsagePublicLimits')
    self._public_limits = public_limits

  @property
  def private_quota(self) -> Optional['DiskUsagePrivateLimits']:
    return self._private_quota

  @private_quota.setter
  def private_quota(self, private_quota: Optional['DiskUsagePrivateLimits']):
    if private_quota is None:
      del self.private_quota
      return
    if not isinstance(private_quota, DiskUsagePrivateLimits):
      raise TypeError('private_quota must be of type DiskUsagePrivateLimits')
    self._private_quota = private_quota

  @property
  def max_files(self) -> int:
    return self._max_files

  @max_files.setter
  def max_files(self, max_files: int):
    if max_files is None:
      del self.max_files
      return
    if not isinstance(max_files, int):
      raise TypeError('max_files must be of type int')
    self._max_files = max_files


class DiskUsagePrivateLimits(KaggleObject):
  r"""
  Attributes:
    total_bytes (int)
    used_bytes (int)
    total_bytes_all_versions (int)
    used_bytes_all_versions (int)
  """

  def __init__(self):
    self._total_bytes = 0
    self._used_bytes = 0
    self._total_bytes_all_versions = 0
    self._used_bytes_all_versions = 0
    self._freeze()

  @property
  def total_bytes(self) -> int:
    return self._total_bytes

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

  @property
  def used_bytes(self) -> int:
    return self._used_bytes

  @used_bytes.setter
  def used_bytes(self, used_bytes: int):
    if used_bytes is None:
      del self.used_bytes
      return
    if not isinstance(used_bytes, int):
      raise TypeError('used_bytes must be of type int')
    self._used_bytes = used_bytes

  @property
  def total_bytes_all_versions(self) -> int:
    return self._total_bytes_all_versions

  @total_bytes_all_versions.setter
  def total_bytes_all_versions(self, total_bytes_all_versions: int):
    if total_bytes_all_versions is None:
      del self.total_bytes_all_versions
      return
    if not isinstance(total_bytes_all_versions, int):
      raise TypeError('total_bytes_all_versions must be of type int')
    self._total_bytes_all_versions = total_bytes_all_versions

  @property
  def used_bytes_all_versions(self) -> int:
    return self._used_bytes_all_versions

  @used_bytes_all_versions.setter
  def used_bytes_all_versions(self, used_bytes_all_versions: int):
    if used_bytes_all_versions is None:
      del self.used_bytes_all_versions
      return
    if not isinstance(used_bytes_all_versions, int):
      raise TypeError('used_bytes_all_versions must be of type int')
    self._used_bytes_all_versions = used_bytes_all_versions


class DiskUsagePublicLimits(KaggleObject):
  r"""
  Attributes:
    max_bytes (int)
    is_organization_limit (bool)
    is_admin_limit (bool)
  """

  def __init__(self):
    self._max_bytes = 0
    self._is_organization_limit = False
    self._is_admin_limit = False
    self._freeze()

  @property
  def max_bytes(self) -> int:
    return self._max_bytes

  @max_bytes.setter
  def max_bytes(self, max_bytes: int):
    if max_bytes is None:
      del self.max_bytes
      return
    if not isinstance(max_bytes, int):
      raise TypeError('max_bytes must be of type int')
    self._max_bytes = max_bytes

  @property
  def is_organization_limit(self) -> bool:
    return self._is_organization_limit

  @is_organization_limit.setter
  def is_organization_limit(self, is_organization_limit: bool):
    if is_organization_limit is None:
      del self.is_organization_limit
      return
    if not isinstance(is_organization_limit, bool):
      raise TypeError('is_organization_limit must be of type bool')
    self._is_organization_limit = is_organization_limit

  @property
  def is_admin_limit(self) -> bool:
    return self._is_admin_limit

  @is_admin_limit.setter
  def is_admin_limit(self, is_admin_limit: bool):
    if is_admin_limit is None:
      del self.is_admin_limit
      return
    if not isinstance(is_admin_limit, bool):
      raise TypeError('is_admin_limit must be of type bool')
    self._is_admin_limit = is_admin_limit


class Image(KaggleObject):
  r"""
  Attributes:
    src (str)
    alt (str)
  """

  def __init__(self):
    self._src = None
    self._alt = None
    self._freeze()

  @property
  def src(self) -> str:
    return self._src or ""

  @src.setter
  def src(self, src: Optional[str]):
    if src is None:
      del self.src
      return
    if not isinstance(src, str):
      raise TypeError('src must be of type str')
    self._src = src

  @property
  def alt(self) -> str:
    return self._alt or ""

  @alt.setter
  def alt(self, alt: Optional[str]):
    if alt is None:
      del self.alt
      return
    if not isinstance(alt, str):
      raise TypeError('alt must be of type str')
    self._alt = alt


class PageMessage(KaggleObject):
  r"""
  Attributes:
    id (str)
    type (PageMessageType)
    message (str)
    dangerous_html_message (str)
    is_persistent (bool)
    fa_icon (str)
  """

  def __init__(self):
    self._id = None
    self._type = None
    self._message = None
    self._dangerous_html_message = None
    self._is_persistent = None
    self._fa_icon = None
    self._freeze()

  @property
  def id(self) -> str:
    return self._id or ""

  @id.setter
  def id(self, id: Optional[str]):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def type(self) -> 'PageMessageType':
    return self._type or PageMessageType.ERROR

  @type.setter
  def type(self, type: Optional['PageMessageType']):
    if type is None:
      del self.type
      return
    if not isinstance(type, PageMessageType):
      raise TypeError('type must be of type PageMessageType')
    self._type = type

  @property
  def message(self) -> str:
    return self._message or ""

  @message.setter
  def message(self, message: Optional[str]):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def dangerous_html_message(self) -> str:
    return self._dangerous_html_message or ""

  @dangerous_html_message.setter
  def dangerous_html_message(self, dangerous_html_message: Optional[str]):
    if dangerous_html_message is None:
      del self.dangerous_html_message
      return
    if not isinstance(dangerous_html_message, str):
      raise TypeError('dangerous_html_message must be of type str')
    self._dangerous_html_message = dangerous_html_message

  @property
  def is_persistent(self) -> bool:
    return self._is_persistent or False

  @is_persistent.setter
  def is_persistent(self, is_persistent: Optional[bool]):
    if is_persistent is None:
      del self.is_persistent
      return
    if not isinstance(is_persistent, bool):
      raise TypeError('is_persistent must be of type bool')
    self._is_persistent = is_persistent

  @property
  def fa_icon(self) -> str:
    return self._fa_icon or ""

  @fa_icon.setter
  def fa_icon(self, fa_icon: Optional[str]):
    if fa_icon is None:
      del self.fa_icon
      return
    if not isinstance(fa_icon, str):
      raise TypeError('fa_icon must be of type str')
    self._fa_icon = fa_icon


Category._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fullPath", "full_path", "_full_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("listingUrl", "listing_url", "_listing_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isInherited", "is_inherited", "_is_inherited", bool, False, PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptCount", "script_count", "_script_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
  FieldMetadata("tagUrl", "tag_url", "_tag_url", str, None, PredefinedSerializer(), optional=True),
]

DiskUsageLimits._fields = [
  FieldMetadata("publicLimits", "public_limits", "_public_limits", DiskUsagePublicLimits, None, KaggleObjectSerializer()),
  FieldMetadata("privateQuota", "private_quota", "_private_quota", DiskUsagePrivateLimits, None, KaggleObjectSerializer()),
  FieldMetadata("maxFiles", "max_files", "_max_files", int, 0, PredefinedSerializer()),
]

DiskUsagePrivateLimits._fields = [
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("usedBytes", "used_bytes", "_used_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalBytesAllVersions", "total_bytes_all_versions", "_total_bytes_all_versions", int, 0, PredefinedSerializer()),
  FieldMetadata("usedBytesAllVersions", "used_bytes_all_versions", "_used_bytes_all_versions", int, 0, PredefinedSerializer()),
]

DiskUsagePublicLimits._fields = [
  FieldMetadata("maxBytes", "max_bytes", "_max_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("isOrganizationLimit", "is_organization_limit", "_is_organization_limit", bool, False, PredefinedSerializer()),
  FieldMetadata("isAdminLimit", "is_admin_limit", "_is_admin_limit", bool, False, PredefinedSerializer()),
]

Image._fields = [
  FieldMetadata("src", "src", "_src", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("alt", "alt", "_alt", str, None, PredefinedSerializer(), optional=True),
]

PageMessage._fields = [
  FieldMetadata("id", "id", "_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", PageMessageType, None, EnumSerializer(), optional=True),
  FieldMetadata("message", "message", "_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dangerousHtmlMessage", "dangerous_html_message", "_dangerous_html_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPersistent", "is_persistent", "_is_persistent", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("faIcon", "fa_icon", "_fa_icon", str, None, PredefinedSerializer(), optional=True),
]

