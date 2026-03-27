from datetime import datetime
import enum
from kagglesdk.admin.types.rate_limit import RateLimitStatus
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.users_enums import UserVerificationStatus
from typing import Optional, List, Dict

class AutoFormPropertyType(enum.Enum):
  BOOL = 0
  CODE = 1
  DATE_TIME = 2
  ENUM = 3
  FLOAT = 4
  INT = 5
  STRING = 6
  TEXT = 7

class ActivityLog(KaggleObject):
  r"""
  Attributes:
    id (int)
    log_date (datetime)
    user_agent (str)
    ip_address (str)
    country (str)
    region (str)
    city (str)
    organization (str)
  """

  def __init__(self):
    self._id = 0
    self._log_date = None
    self._user_agent = None
    self._ip_address = None
    self._country = None
    self._region = None
    self._city = None
    self._organization = None
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
  def log_date(self) -> datetime:
    return self._log_date

  @log_date.setter
  def log_date(self, log_date: datetime):
    if log_date is None:
      del self.log_date
      return
    if not isinstance(log_date, datetime):
      raise TypeError('log_date must be of type datetime')
    self._log_date = log_date

  @property
  def user_agent(self) -> str:
    return self._user_agent or ""

  @user_agent.setter
  def user_agent(self, user_agent: Optional[str]):
    if user_agent is None:
      del self.user_agent
      return
    if not isinstance(user_agent, str):
      raise TypeError('user_agent must be of type str')
    self._user_agent = user_agent

  @property
  def ip_address(self) -> str:
    return self._ip_address or ""

  @ip_address.setter
  def ip_address(self, ip_address: Optional[str]):
    if ip_address is None:
      del self.ip_address
      return
    if not isinstance(ip_address, str):
      raise TypeError('ip_address must be of type str')
    self._ip_address = ip_address

  @property
  def country(self) -> str:
    return self._country or ""

  @country.setter
  def country(self, country: Optional[str]):
    if country is None:
      del self.country
      return
    if not isinstance(country, str):
      raise TypeError('country must be of type str')
    self._country = country

  @property
  def region(self) -> str:
    return self._region or ""

  @region.setter
  def region(self, region: Optional[str]):
    if region is None:
      del self.region
      return
    if not isinstance(region, str):
      raise TypeError('region must be of type str')
    self._region = region

  @property
  def city(self) -> str:
    return self._city or ""

  @city.setter
  def city(self, city: Optional[str]):
    if city is None:
      del self.city
      return
    if not isinstance(city, str):
      raise TypeError('city must be of type str')
    self._city = city

  @property
  def organization(self) -> str:
    return self._organization or ""

  @organization.setter
  def organization(self, organization: Optional[str]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, str):
      raise TypeError('organization must be of type str')
    self._organization = organization


class AddSiteConfigRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
    value (str)
  """

  def __init__(self):
    self._name = ""
    self._value = ""
    self._freeze()

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class AdminUser(KaggleObject):
  r"""
  Attributes:
    id (int)
    most_recent_log (ActivityLog)
    last_verified_phone_number (str)
    has_phone_reputations (bool)
    is_last_phone_number_reputable (bool)
    rate_limit_statuses (RateLimitStatus)
    discord_username (str)
    has_phone_verifications (bool)
    identity_verification_status (UserVerificationStatus)
    phone_verification_status (UserVerificationStatus)
  """

  def __init__(self):
    self._id = 0
    self._most_recent_log = None
    self._last_verified_phone_number = None
    self._has_phone_reputations = None
    self._is_last_phone_number_reputable = None
    self._rate_limit_statuses = []
    self._discord_username = None
    self._has_phone_verifications = None
    self._identity_verification_status = UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED
    self._phone_verification_status = UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED
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
  def most_recent_log(self) -> Optional['ActivityLog']:
    return self._most_recent_log

  @most_recent_log.setter
  def most_recent_log(self, most_recent_log: Optional['ActivityLog']):
    if most_recent_log is None:
      del self.most_recent_log
      return
    if not isinstance(most_recent_log, ActivityLog):
      raise TypeError('most_recent_log must be of type ActivityLog')
    self._most_recent_log = most_recent_log

  @property
  def last_verified_phone_number(self) -> str:
    return self._last_verified_phone_number or ""

  @last_verified_phone_number.setter
  def last_verified_phone_number(self, last_verified_phone_number: Optional[str]):
    if last_verified_phone_number is None:
      del self.last_verified_phone_number
      return
    if not isinstance(last_verified_phone_number, str):
      raise TypeError('last_verified_phone_number must be of type str')
    self._last_verified_phone_number = last_verified_phone_number

  @property
  def has_phone_verifications(self) -> bool:
    return self._has_phone_verifications or False

  @has_phone_verifications.setter
  def has_phone_verifications(self, has_phone_verifications: Optional[bool]):
    if has_phone_verifications is None:
      del self.has_phone_verifications
      return
    if not isinstance(has_phone_verifications, bool):
      raise TypeError('has_phone_verifications must be of type bool')
    self._has_phone_verifications = has_phone_verifications

  @property
  def has_phone_reputations(self) -> bool:
    return self._has_phone_reputations or False

  @has_phone_reputations.setter
  def has_phone_reputations(self, has_phone_reputations: Optional[bool]):
    if has_phone_reputations is None:
      del self.has_phone_reputations
      return
    if not isinstance(has_phone_reputations, bool):
      raise TypeError('has_phone_reputations must be of type bool')
    self._has_phone_reputations = has_phone_reputations

  @property
  def is_last_phone_number_reputable(self) -> bool:
    return self._is_last_phone_number_reputable or False

  @is_last_phone_number_reputable.setter
  def is_last_phone_number_reputable(self, is_last_phone_number_reputable: Optional[bool]):
    if is_last_phone_number_reputable is None:
      del self.is_last_phone_number_reputable
      return
    if not isinstance(is_last_phone_number_reputable, bool):
      raise TypeError('is_last_phone_number_reputable must be of type bool')
    self._is_last_phone_number_reputable = is_last_phone_number_reputable

  @property
  def rate_limit_statuses(self) -> Optional[List[Optional['RateLimitStatus']]]:
    return self._rate_limit_statuses

  @rate_limit_statuses.setter
  def rate_limit_statuses(self, rate_limit_statuses: Optional[List[Optional['RateLimitStatus']]]):
    if rate_limit_statuses is None:
      del self.rate_limit_statuses
      return
    if not isinstance(rate_limit_statuses, list):
      raise TypeError('rate_limit_statuses must be of type list')
    if not all([isinstance(t, RateLimitStatus) for t in rate_limit_statuses]):
      raise TypeError('rate_limit_statuses must contain only items of type RateLimitStatus')
    self._rate_limit_statuses = rate_limit_statuses

  @property
  def discord_username(self) -> str:
    return self._discord_username or ""

  @discord_username.setter
  def discord_username(self, discord_username: Optional[str]):
    if discord_username is None:
      del self.discord_username
      return
    if not isinstance(discord_username, str):
      raise TypeError('discord_username must be of type str')
    self._discord_username = discord_username

  @property
  def identity_verification_status(self) -> 'UserVerificationStatus':
    return self._identity_verification_status

  @identity_verification_status.setter
  def identity_verification_status(self, identity_verification_status: 'UserVerificationStatus'):
    if identity_verification_status is None:
      del self.identity_verification_status
      return
    if not isinstance(identity_verification_status, UserVerificationStatus):
      raise TypeError('identity_verification_status must be of type UserVerificationStatus')
    self._identity_verification_status = identity_verification_status

  @property
  def phone_verification_status(self) -> 'UserVerificationStatus':
    return self._phone_verification_status

  @phone_verification_status.setter
  def phone_verification_status(self, phone_verification_status: 'UserVerificationStatus'):
    if phone_verification_status is None:
      del self.phone_verification_status
      return
    if not isinstance(phone_verification_status, UserVerificationStatus):
      raise TypeError('phone_verification_status must be of type UserVerificationStatus')
    self._phone_verification_status = phone_verification_status


class AutoFormModel(KaggleObject):
  r"""
  Attributes:
    properties (AutoFormProperty)
  """

  def __init__(self):
    self._properties = []
    self._freeze()

  @property
  def properties(self) -> Optional[List[Optional['AutoFormProperty']]]:
    return self._properties

  @properties.setter
  def properties(self, properties: Optional[List[Optional['AutoFormProperty']]]):
    if properties is None:
      del self.properties
      return
    if not isinstance(properties, list):
      raise TypeError('properties must be of type list')
    if not all([isinstance(t, AutoFormProperty) for t in properties]):
      raise TypeError('properties must contain only items of type AutoFormProperty')
    self._properties = properties


class AutoFormProperty(KaggleObject):
  r"""
  Attributes:
    description (str)
    is_nullable (bool)
    is_readonly (bool)
    name (str)
    type (AutoFormPropertyType)
    value (str)
    is_xml (bool)
  """

  def __init__(self):
    self._description = None
    self._is_nullable = False
    self._is_readonly = False
    self._name = None
    self._type = AutoFormPropertyType.BOOL
    self._value = None
    self._is_xml = False
    self._freeze()

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
  def is_nullable(self) -> bool:
    return self._is_nullable

  @is_nullable.setter
  def is_nullable(self, is_nullable: bool):
    if is_nullable is None:
      del self.is_nullable
      return
    if not isinstance(is_nullable, bool):
      raise TypeError('is_nullable must be of type bool')
    self._is_nullable = is_nullable

  @property
  def is_readonly(self) -> bool:
    return self._is_readonly

  @is_readonly.setter
  def is_readonly(self, is_readonly: bool):
    if is_readonly is None:
      del self.is_readonly
      return
    if not isinstance(is_readonly, bool):
      raise TypeError('is_readonly must be of type bool')
    self._is_readonly = is_readonly

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
  def type(self) -> 'AutoFormPropertyType':
    return self._type

  @type.setter
  def type(self, type: 'AutoFormPropertyType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, AutoFormPropertyType):
      raise TypeError('type must be of type AutoFormPropertyType')
    self._type = type

  @property
  def value(self) -> str:
    return self._value or ""

  @value.setter
  def value(self, value: Optional[str]):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

  @property
  def is_xml(self) -> bool:
    return self._is_xml

  @is_xml.setter
  def is_xml(self, is_xml: bool):
    if is_xml is None:
      del self.is_xml
      return
    if not isinstance(is_xml, bool):
      raise TypeError('is_xml must be of type bool')
    self._is_xml = is_xml


class BatchDeleteAccountActivityRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      The list of users to erase activity (i.e. non user-generated content).
    end_time (datetime)
      Exclusive (i.e. up to but not including) time of when to start removing
      activity.
  """

  def __init__(self):
    self._user_ids = []
    self._end_time = None
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The list of users to erase activity (i.e. non user-generated content)."""
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids

  @property
  def end_time(self) -> datetime:
    r"""
    Exclusive (i.e. up to but not including) time of when to start removing
    activity.
    """
    return self._end_time

  @end_time.setter
  def end_time(self, end_time: datetime):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time


class BatchDeleteAccountActivityResponse(KaggleObject):
  r"""
  Attributes:
    impacted_users_count (int)
    affected_rows_count (int)
  """

  def __init__(self):
    self._impacted_users_count = 0
    self._affected_rows_count = 0
    self._freeze()

  @property
  def impacted_users_count(self) -> int:
    return self._impacted_users_count

  @impacted_users_count.setter
  def impacted_users_count(self, impacted_users_count: int):
    if impacted_users_count is None:
      del self.impacted_users_count
      return
    if not isinstance(impacted_users_count, int):
      raise TypeError('impacted_users_count must be of type int')
    self._impacted_users_count = impacted_users_count

  @property
  def affected_rows_count(self) -> int:
    return self._affected_rows_count

  @affected_rows_count.setter
  def affected_rows_count(self, affected_rows_count: int):
    if affected_rows_count is None:
      del self.affected_rows_count
      return
    if not isinstance(affected_rows_count, int):
      raise TypeError('affected_rows_count must be of type int')
    self._affected_rows_count = affected_rows_count


class BulkUpdateEmergencyBannersRequest(KaggleObject):
  r"""
  Attributes:
    banner_config (EmergencyBannersConfig)
      The exact list of banners to have after the update. The previous banner
      config will be replaced with what is supplied here. Recommended usage is to
      call ListEmergencyBanners, then copy-paste the output with modifications.
  """

  def __init__(self):
    self._banner_config = None
    self._freeze()

  @property
  def banner_config(self) -> Optional['EmergencyBannersConfig']:
    r"""
    The exact list of banners to have after the update. The previous banner
    config will be replaced with what is supplied here. Recommended usage is to
    call ListEmergencyBanners, then copy-paste the output with modifications.
    """
    return self._banner_config

  @banner_config.setter
  def banner_config(self, banner_config: Optional['EmergencyBannersConfig']):
    if banner_config is None:
      del self.banner_config
      return
    if not isinstance(banner_config, EmergencyBannersConfig):
      raise TypeError('banner_config must be of type EmergencyBannersConfig')
    self._banner_config = banner_config


class CreateIdmecLinkRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The UserName for the user we're looking up.
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    """The UserName for the user we're looking up."""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class CreateIdmecLinkResponse(KaggleObject):
  r"""
  Attributes:
    access_links (str)
      A list of signed URIs, could be multiple if multiple users with the same
      username were deleted.
  """

  def __init__(self):
    self._access_links = []
    self._freeze()

  @property
  def access_links(self) -> Optional[List[str]]:
    r"""
    A list of signed URIs, could be multiple if multiple users with the same
    username were deleted.
    """
    return self._access_links

  @access_links.setter
  def access_links(self, access_links: Optional[List[str]]):
    if access_links is None:
      del self.access_links
      return
    if not isinstance(access_links, list):
      raise TypeError('access_links must be of type list')
    if not all([isinstance(t, str) for t in access_links]):
      raise TypeError('access_links must contain only items of type str')
    self._access_links = access_links


class DeleteAllEmergencyBannersRequest(KaggleObject):
  r"""
  """

  pass

class DeleteEmergencyBannerRequest(KaggleObject):
  r"""
  Attributes:
    banner_id (str)
      The banner ID to delete, removing it from the site.
  """

  def __init__(self):
    self._banner_id = ""
    self._freeze()

  @property
  def banner_id(self) -> str:
    """The banner ID to delete, removing it from the site."""
    return self._banner_id

  @banner_id.setter
  def banner_id(self, banner_id: str):
    if banner_id is None:
      del self.banner_id
      return
    if not isinstance(banner_id, str):
      raise TypeError('banner_id must be of type str')
    self._banner_id = banner_id


class DeleteSiteConfigRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
  """

  def __init__(self):
    self._id = 0
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


class EmergencyBanner(KaggleObject):
  r"""
  Attributes:
    banner_id (str)
    message_html (str)
    uri_path_regex (str)
  """

  def __init__(self):
    self._banner_id = ""
    self._message_html = ""
    self._uri_path_regex = ""
    self._freeze()

  @property
  def banner_id(self) -> str:
    return self._banner_id

  @banner_id.setter
  def banner_id(self, banner_id: str):
    if banner_id is None:
      del self.banner_id
      return
    if not isinstance(banner_id, str):
      raise TypeError('banner_id must be of type str')
    self._banner_id = banner_id

  @property
  def message_html(self) -> str:
    return self._message_html

  @message_html.setter
  def message_html(self, message_html: str):
    if message_html is None:
      del self.message_html
      return
    if not isinstance(message_html, str):
      raise TypeError('message_html must be of type str')
    self._message_html = message_html

  @property
  def uri_path_regex(self) -> str:
    return self._uri_path_regex

  @uri_path_regex.setter
  def uri_path_regex(self, uri_path_regex: str):
    if uri_path_regex is None:
      del self.uri_path_regex
      return
    if not isinstance(uri_path_regex, str):
      raise TypeError('uri_path_regex must be of type str')
    self._uri_path_regex = uri_path_regex


class EmergencyBannersConfig(KaggleObject):
  r"""
  Attributes:
    banners (EmergencyBanner)
  """

  def __init__(self):
    self._banners = []
    self._freeze()

  @property
  def banners(self) -> Optional[List[Optional['EmergencyBanner']]]:
    return self._banners

  @banners.setter
  def banners(self, banners: Optional[List[Optional['EmergencyBanner']]]):
    if banners is None:
      del self.banners
      return
    if not isinstance(banners, list):
      raise TypeError('banners must be of type list')
    if not all([isinstance(t, EmergencyBanner) for t in banners]):
      raise TypeError('banners must contain only items of type EmergencyBanner')
    self._banners = banners


class GetAdminUserRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = None
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetAllSiteConfigsRequest(KaggleObject):
  r"""
  Attributes:
    force_cache_refresh (bool)
  """

  def __init__(self):
    self._force_cache_refresh = False
    self._freeze()

  @property
  def force_cache_refresh(self) -> bool:
    return self._force_cache_refresh

  @force_cache_refresh.setter
  def force_cache_refresh(self, force_cache_refresh: bool):
    if force_cache_refresh is None:
      del self.force_cache_refresh
      return
    if not isinstance(force_cache_refresh, bool):
      raise TypeError('force_cache_refresh must be of type bool')
    self._force_cache_refresh = force_cache_refresh


class GetAllSiteConfigsResponse(KaggleObject):
  r"""
  Attributes:
    site_configs (SiteConfig)
    current_user_can_see_map (bool)
    current_user_can_see_no_admin_map (bool)
  """

  def __init__(self):
    self._site_configs = []
    self._current_user_can_see_map = {}
    self._current_user_can_see_no_admin_map = {}
    self._freeze()

  @property
  def site_configs(self) -> Optional[List[Optional['SiteConfig']]]:
    return self._site_configs

  @site_configs.setter
  def site_configs(self, site_configs: Optional[List[Optional['SiteConfig']]]):
    if site_configs is None:
      del self.site_configs
      return
    if not isinstance(site_configs, list):
      raise TypeError('site_configs must be of type list')
    if not all([isinstance(t, SiteConfig) for t in site_configs]):
      raise TypeError('site_configs must contain only items of type SiteConfig')
    self._site_configs = site_configs

  @property
  def current_user_can_see_map(self) -> Optional[Dict[str, bool]]:
    return self._current_user_can_see_map

  @current_user_can_see_map.setter
  def current_user_can_see_map(self, current_user_can_see_map: Optional[Dict[str, bool]]):
    if current_user_can_see_map is None:
      del self.current_user_can_see_map
      return
    if not isinstance(current_user_can_see_map, dict):
      raise TypeError('current_user_can_see_map must be of type dict')
    if not all([isinstance(v, bool) for k, v in current_user_can_see_map]):
      raise TypeError('current_user_can_see_map must contain only items of type bool')
    self._current_user_can_see_map = current_user_can_see_map

  @property
  def current_user_can_see_no_admin_map(self) -> Optional[Dict[str, bool]]:
    return self._current_user_can_see_no_admin_map

  @current_user_can_see_no_admin_map.setter
  def current_user_can_see_no_admin_map(self, current_user_can_see_no_admin_map: Optional[Dict[str, bool]]):
    if current_user_can_see_no_admin_map is None:
      del self.current_user_can_see_no_admin_map
      return
    if not isinstance(current_user_can_see_no_admin_map, dict):
      raise TypeError('current_user_can_see_no_admin_map must be of type dict')
    if not all([isinstance(v, bool) for k, v in current_user_can_see_no_admin_map]):
      raise TypeError('current_user_can_see_no_admin_map must contain only items of type bool')
    self._current_user_can_see_no_admin_map = current_user_can_see_no_admin_map


class GetApiMethodSampleRequestRequest(KaggleObject):
  r"""
  Attributes:
    method_name (str)
  """

  def __init__(self):
    self._method_name = ""
    self._freeze()

  @property
  def method_name(self) -> str:
    return self._method_name

  @method_name.setter
  def method_name(self, method_name: str):
    if method_name is None:
      del self.method_name
      return
    if not isinstance(method_name, str):
      raise TypeError('method_name must be of type str')
    self._method_name = method_name


class GetApiMethodSampleRequestResponse(KaggleObject):
  r"""
  Attributes:
    sample_request (str)
    request_proto_uri (str)
    response_proto_uri (str)
  """

  def __init__(self):
    self._sample_request = ""
    self._request_proto_uri = ""
    self._response_proto_uri = ""
    self._freeze()

  @property
  def sample_request(self) -> str:
    return self._sample_request

  @sample_request.setter
  def sample_request(self, sample_request: str):
    if sample_request is None:
      del self.sample_request
      return
    if not isinstance(sample_request, str):
      raise TypeError('sample_request must be of type str')
    self._sample_request = sample_request

  @property
  def request_proto_uri(self) -> str:
    return self._request_proto_uri

  @request_proto_uri.setter
  def request_proto_uri(self, request_proto_uri: str):
    if request_proto_uri is None:
      del self.request_proto_uri
      return
    if not isinstance(request_proto_uri, str):
      raise TypeError('request_proto_uri must be of type str')
    self._request_proto_uri = request_proto_uri

  @property
  def response_proto_uri(self) -> str:
    return self._response_proto_uri

  @response_proto_uri.setter
  def response_proto_uri(self, response_proto_uri: str):
    if response_proto_uri is None:
      del self.response_proto_uri
      return
    if not isinstance(response_proto_uri, str):
      raise TypeError('response_proto_uri must be of type str')
    self._response_proto_uri = response_proto_uri


class GetAutoFormModelRequest(KaggleObject):
  r"""
  Attributes:
    type_name (str)
    id (int)
  """

  def __init__(self):
    self._type_name = None
    self._id = 0
    self._freeze()

  @property
  def type_name(self) -> str:
    return self._type_name or ""

  @type_name.setter
  def type_name(self, type_name: Optional[str]):
    if type_name is None:
      del self.type_name
      return
    if not isinstance(type_name, str):
      raise TypeError('type_name must be of type str')
    self._type_name = type_name

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


class GetSearchIndexStatusRequest(KaggleObject):
  r"""
  Attributes:
    namespace (str)
      Optional namespace filter (e.g., 'prod', 'staging'). If not specified, uses
      current namespace.
  """

  def __init__(self):
    self._namespace = None
    self._freeze()

  @property
  def namespace(self) -> str:
    r"""
    Optional namespace filter (e.g., 'prod', 'staging'). If not specified, uses
    current namespace.
    """
    return self._namespace or ""

  @namespace.setter
  def namespace(self, namespace: Optional[str]):
    if namespace is None:
      del self.namespace
      return
    if not isinstance(namespace, str):
      raise TypeError('namespace must be of type str')
    self._namespace = namespace


class GetSearchIndexStatusResponse(KaggleObject):
  r"""
  Attributes:
    indexes (SearchIndexStatus)
  """

  def __init__(self):
    self._indexes = []
    self._freeze()

  @property
  def indexes(self) -> Optional[List[Optional['SearchIndexStatus']]]:
    return self._indexes

  @indexes.setter
  def indexes(self, indexes: Optional[List[Optional['SearchIndexStatus']]]):
    if indexes is None:
      del self.indexes
      return
    if not isinstance(indexes, list):
      raise TypeError('indexes must be of type list')
    if not all([isinstance(t, SearchIndexStatus) for t in indexes]):
      raise TypeError('indexes must contain only items of type SearchIndexStatus')
    self._indexes = indexes


class ListApiMethodsRequest(KaggleObject):
  r"""
  """

  pass

class ListApiMethodsResponse(KaggleObject):
  r"""
  Attributes:
    method_names (str)
  """

  def __init__(self):
    self._method_names = []
    self._freeze()

  @property
  def method_names(self) -> Optional[List[str]]:
    return self._method_names

  @method_names.setter
  def method_names(self, method_names: Optional[List[str]]):
    if method_names is None:
      del self.method_names
      return
    if not isinstance(method_names, list):
      raise TypeError('method_names must be of type list')
    if not all([isinstance(t, str) for t in method_names]):
      raise TypeError('method_names must contain only items of type str')
    self._method_names = method_names


class ListEmergencyBannersRequest(KaggleObject):
  r"""
  """

  pass

class ListEmergencyBannersResponse(KaggleObject):
  r"""
  Attributes:
    banner_config (EmergencyBannersConfig)
  """

  def __init__(self):
    self._banner_config = None
    self._freeze()

  @property
  def banner_config(self) -> Optional['EmergencyBannersConfig']:
    return self._banner_config

  @banner_config.setter
  def banner_config(self, banner_config: Optional['EmergencyBannersConfig']):
    if banner_config is None:
      del self.banner_config
      return
    if not isinstance(banner_config, EmergencyBannersConfig):
      raise TypeError('banner_config must be of type EmergencyBannersConfig')
    self._banner_config = banner_config


class RenewIapTokenRequest(KaggleObject):
  r"""
  """

  pass

class RenewIapTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
  """

  def __init__(self):
    self._token = ""
    self._freeze()

  @property
  def token(self) -> str:
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class ResetSearchIndexesRequest(KaggleObject):
  r"""
  """

  pass

class ResetSearchIndexRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
  """

  def __init__(self):
    self._name = ""
    self._freeze()

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


class SearchIndexLogEntry(KaggleObject):
  r"""
  Attributes:
    start_date (datetime)
    end_date (datetime)
    duration_seconds (int)
    documents_indexed (int)
    percent_complete (float)
      Percentage complete (0-100), only applicable for in-progress rebuilds
  """

  def __init__(self):
    self._start_date = None
    self._end_date = None
    self._duration_seconds = 0
    self._documents_indexed = 0
    self._percent_complete = None
    self._freeze()

  @property
  def start_date(self) -> datetime:
    return self._start_date

  @start_date.setter
  def start_date(self, start_date: datetime):
    if start_date is None:
      del self.start_date
      return
    if not isinstance(start_date, datetime):
      raise TypeError('start_date must be of type datetime')
    self._start_date = start_date

  @property
  def end_date(self) -> datetime:
    return self._end_date or None

  @end_date.setter
  def end_date(self, end_date: Optional[datetime]):
    if end_date is None:
      del self.end_date
      return
    if not isinstance(end_date, datetime):
      raise TypeError('end_date must be of type datetime')
    self._end_date = end_date

  @property
  def duration_seconds(self) -> int:
    return self._duration_seconds

  @duration_seconds.setter
  def duration_seconds(self, duration_seconds: int):
    if duration_seconds is None:
      del self.duration_seconds
      return
    if not isinstance(duration_seconds, int):
      raise TypeError('duration_seconds must be of type int')
    self._duration_seconds = duration_seconds

  @property
  def documents_indexed(self) -> int:
    return self._documents_indexed

  @documents_indexed.setter
  def documents_indexed(self, documents_indexed: int):
    if documents_indexed is None:
      del self.documents_indexed
      return
    if not isinstance(documents_indexed, int):
      raise TypeError('documents_indexed must be of type int')
    self._documents_indexed = documents_indexed

  @property
  def percent_complete(self) -> float:
    """Percentage complete (0-100), only applicable for in-progress rebuilds"""
    return self._percent_complete or 0.0

  @percent_complete.setter
  def percent_complete(self, percent_complete: Optional[float]):
    if percent_complete is None:
      del self.percent_complete
      return
    if not isinstance(percent_complete, float):
      raise TypeError('percent_complete must be of type float')
    self._percent_complete = percent_complete


class SearchIndexStatus(KaggleObject):
  r"""
  Attributes:
    name (str)
      Index name (e.g., 'datasets', 'kernels')
    rebuild_scheduled (bool)
      Whether a rebuild has been scheduled for the next run
    is_rebuilding (bool)
      Whether a rebuild is currently in progress
    is_running (bool)
      Whether an incremental index is currently running
    last_rebuild (SearchIndexLogEntry)
      Most recent full rebuild log (if any within the last week)
  """

  def __init__(self):
    self._name = ""
    self._rebuild_scheduled = False
    self._is_rebuilding = False
    self._is_running = False
    self._last_rebuild = None
    self._freeze()

  @property
  def name(self) -> str:
    """Index name (e.g., 'datasets', 'kernels')"""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def rebuild_scheduled(self) -> bool:
    """Whether a rebuild has been scheduled for the next run"""
    return self._rebuild_scheduled

  @rebuild_scheduled.setter
  def rebuild_scheduled(self, rebuild_scheduled: bool):
    if rebuild_scheduled is None:
      del self.rebuild_scheduled
      return
    if not isinstance(rebuild_scheduled, bool):
      raise TypeError('rebuild_scheduled must be of type bool')
    self._rebuild_scheduled = rebuild_scheduled

  @property
  def is_rebuilding(self) -> bool:
    """Whether a rebuild is currently in progress"""
    return self._is_rebuilding

  @is_rebuilding.setter
  def is_rebuilding(self, is_rebuilding: bool):
    if is_rebuilding is None:
      del self.is_rebuilding
      return
    if not isinstance(is_rebuilding, bool):
      raise TypeError('is_rebuilding must be of type bool')
    self._is_rebuilding = is_rebuilding

  @property
  def is_running(self) -> bool:
    """Whether an incremental index is currently running"""
    return self._is_running

  @is_running.setter
  def is_running(self, is_running: bool):
    if is_running is None:
      del self.is_running
      return
    if not isinstance(is_running, bool):
      raise TypeError('is_running must be of type bool')
    self._is_running = is_running

  @property
  def last_rebuild(self) -> Optional['SearchIndexLogEntry']:
    """Most recent full rebuild log (if any within the last week)"""
    return self._last_rebuild or None

  @last_rebuild.setter
  def last_rebuild(self, last_rebuild: Optional[Optional['SearchIndexLogEntry']]):
    if last_rebuild is None:
      del self.last_rebuild
      return
    if not isinstance(last_rebuild, SearchIndexLogEntry):
      raise TypeError('last_rebuild must be of type SearchIndexLogEntry')
    self._last_rebuild = last_rebuild


class SiteConfig(KaggleObject):
  r"""
  Attributes:
    id (int)
      Unset if this stems from a FlagDefault annotation and not a DB-backed
      SiteConfig row.
    name (str)
    value (str)
    unused (bool)
      Whether we don't have a corresponding FeatureFlag / OpsFlag defined, and
      thus cannot control behavior somewhere.
    description (str)
  """

  def __init__(self):
    self._id = None
    self._name = ""
    self._value = None
    self._unused = None
    self._description = None
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    Unset if this stems from a FlagDefault annotation and not a DB-backed
    SiteConfig row.
    """
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def value(self) -> str:
    return self._value or ""

  @value.setter
  def value(self, value: Optional[str]):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

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
  def unused(self) -> bool:
    r"""
    Whether we don't have a corresponding FeatureFlag / OpsFlag defined, and
    thus cannot control behavior somewhere.
    """
    return self._unused or False

  @unused.setter
  def unused(self, unused: Optional[bool]):
    if unused is None:
      del self.unused
      return
    if not isinstance(unused, bool):
      raise TypeError('unused must be of type bool')
    self._unused = unused


class UpdateAutoFormModelRequest(KaggleObject):
  r"""
  Attributes:
    type_name (str)
    id (int)
    model (AutoFormModel)
  """

  def __init__(self):
    self._type_name = None
    self._id = 0
    self._model = None
    self._freeze()

  @property
  def type_name(self) -> str:
    return self._type_name or ""

  @type_name.setter
  def type_name(self, type_name: Optional[str]):
    if type_name is None:
      del self.type_name
      return
    if not isinstance(type_name, str):
      raise TypeError('type_name must be of type str')
    self._type_name = type_name

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
  def model(self) -> Optional['AutoFormModel']:
    return self._model or None

  @model.setter
  def model(self, model: Optional[Optional['AutoFormModel']]):
    if model is None:
      del self.model
      return
    if not isinstance(model, AutoFormModel):
      raise TypeError('model must be of type AutoFormModel')
    self._model = model


class UpdateEmergencyBannerRequest(KaggleObject):
  r"""
  Attributes:
    banner_id (str)
      Add or update a single emergency banner.

      The banner ID to add or update.
    message_html (str)
      The HTML message to display in the banner.
    uri_path_regex (str)
      Regex specifying matching pages to display the banner.
  """

  def __init__(self):
    self._banner_id = ""
    self._message_html = ""
    self._uri_path_regex = ""
    self._freeze()

  @property
  def banner_id(self) -> str:
    r"""
    Add or update a single emergency banner.

    The banner ID to add or update.
    """
    return self._banner_id

  @banner_id.setter
  def banner_id(self, banner_id: str):
    if banner_id is None:
      del self.banner_id
      return
    if not isinstance(banner_id, str):
      raise TypeError('banner_id must be of type str')
    self._banner_id = banner_id

  @property
  def message_html(self) -> str:
    """The HTML message to display in the banner."""
    return self._message_html

  @message_html.setter
  def message_html(self, message_html: str):
    if message_html is None:
      del self.message_html
      return
    if not isinstance(message_html, str):
      raise TypeError('message_html must be of type str')
    self._message_html = message_html

  @property
  def uri_path_regex(self) -> str:
    """Regex specifying matching pages to display the banner."""
    return self._uri_path_regex

  @uri_path_regex.setter
  def uri_path_regex(self, uri_path_regex: str):
    if uri_path_regex is None:
      del self.uri_path_regex
      return
    if not isinstance(uri_path_regex, str):
      raise TypeError('uri_path_regex must be of type str')
    self._uri_path_regex = uri_path_regex


class UpdateNonGenieAutoFormModelRequest(KaggleObject):
  r"""
  Attributes:
    type_name (str)
    id (int)
    model (AutoFormModel)
  """

  def __init__(self):
    self._type_name = None
    self._id = 0
    self._model = None
    self._freeze()

  @property
  def type_name(self) -> str:
    return self._type_name or ""

  @type_name.setter
  def type_name(self, type_name: Optional[str]):
    if type_name is None:
      del self.type_name
      return
    if not isinstance(type_name, str):
      raise TypeError('type_name must be of type str')
    self._type_name = type_name

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
  def model(self) -> Optional['AutoFormModel']:
    return self._model or None

  @model.setter
  def model(self, model: Optional[Optional['AutoFormModel']]):
    if model is None:
      del self.model
      return
    if not isinstance(model, AutoFormModel):
      raise TypeError('model must be of type AutoFormModel')
    self._model = model


class UpdateSiteConfigRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    value (str)
  """

  def __init__(self):
    self._id = 0
    self._value = ""
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
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


ActivityLog._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("logDate", "log_date", "_log_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("userAgent", "user_agent", "_user_agent", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ipAddress", "ip_address", "_ip_address", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("country", "country", "_country", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("region", "region", "_region", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("city", "city", "_city", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", str, None, PredefinedSerializer(), optional=True),
]

AddSiteConfigRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

AdminUser._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("mostRecentLog", "most_recent_log", "_most_recent_log", ActivityLog, None, KaggleObjectSerializer()),
  FieldMetadata("lastVerifiedPhoneNumber", "last_verified_phone_number", "_last_verified_phone_number", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasPhoneReputations", "has_phone_reputations", "_has_phone_reputations", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLastPhoneNumberReputable", "is_last_phone_number_reputable", "_is_last_phone_number_reputable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rateLimitStatuses", "rate_limit_statuses", "_rate_limit_statuses", RateLimitStatus, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("discordUsername", "discord_username", "_discord_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasPhoneVerifications", "has_phone_verifications", "_has_phone_verifications", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("identityVerificationStatus", "identity_verification_status", "_identity_verification_status", UserVerificationStatus, UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("phoneVerificationStatus", "phone_verification_status", "_phone_verification_status", UserVerificationStatus, UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED, EnumSerializer()),
]

AutoFormModel._fields = [
  FieldMetadata("properties", "properties", "_properties", AutoFormProperty, [], ListSerializer(KaggleObjectSerializer())),
]

AutoFormProperty._fields = [
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isNullable", "is_nullable", "_is_nullable", bool, False, PredefinedSerializer()),
  FieldMetadata("isReadonly", "is_readonly", "_is_readonly", bool, False, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", AutoFormPropertyType, AutoFormPropertyType.BOOL, EnumSerializer()),
  FieldMetadata("value", "value", "_value", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isXml", "is_xml", "_is_xml", bool, False, PredefinedSerializer()),
]

BatchDeleteAccountActivityRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer()),
]

BatchDeleteAccountActivityResponse._fields = [
  FieldMetadata("impactedUsersCount", "impacted_users_count", "_impacted_users_count", int, 0, PredefinedSerializer()),
  FieldMetadata("affectedRowsCount", "affected_rows_count", "_affected_rows_count", int, 0, PredefinedSerializer()),
]

BulkUpdateEmergencyBannersRequest._fields = [
  FieldMetadata("bannerConfig", "banner_config", "_banner_config", EmergencyBannersConfig, None, KaggleObjectSerializer()),
]

CreateIdmecLinkRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

CreateIdmecLinkResponse._fields = [
  FieldMetadata("accessLinks", "access_links", "_access_links", str, [], ListSerializer(PredefinedSerializer())),
]

DeleteAllEmergencyBannersRequest._fields = []

DeleteEmergencyBannerRequest._fields = [
  FieldMetadata("bannerId", "banner_id", "_banner_id", str, "", PredefinedSerializer()),
]

DeleteSiteConfigRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

EmergencyBanner._fields = [
  FieldMetadata("bannerId", "banner_id", "_banner_id", str, "", PredefinedSerializer()),
  FieldMetadata("messageHtml", "message_html", "_message_html", str, "", PredefinedSerializer()),
  FieldMetadata("uriPathRegex", "uri_path_regex", "_uri_path_regex", str, "", PredefinedSerializer()),
]

EmergencyBannersConfig._fields = [
  FieldMetadata("banners", "banners", "_banners", EmergencyBanner, [], ListSerializer(KaggleObjectSerializer())),
]

GetAdminUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

GetAllSiteConfigsRequest._fields = [
  FieldMetadata("forceCacheRefresh", "force_cache_refresh", "_force_cache_refresh", bool, False, PredefinedSerializer()),
]

GetAllSiteConfigsResponse._fields = [
  FieldMetadata("siteConfigs", "site_configs", "_site_configs", SiteConfig, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("currentUserCanSeeMap", "current_user_can_see_map", "_current_user_can_see_map", bool, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("currentUserCanSeeNoAdminMap", "current_user_can_see_no_admin_map", "_current_user_can_see_no_admin_map", bool, {}, MapSerializer(PredefinedSerializer())),
]

GetApiMethodSampleRequestRequest._fields = [
  FieldMetadata("methodName", "method_name", "_method_name", str, "", PredefinedSerializer()),
]

GetApiMethodSampleRequestResponse._fields = [
  FieldMetadata("sampleRequest", "sample_request", "_sample_request", str, "", PredefinedSerializer()),
  FieldMetadata("requestProtoUri", "request_proto_uri", "_request_proto_uri", str, "", PredefinedSerializer()),
  FieldMetadata("responseProtoUri", "response_proto_uri", "_response_proto_uri", str, "", PredefinedSerializer()),
]

GetAutoFormModelRequest._fields = [
  FieldMetadata("typeName", "type_name", "_type_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

GetSearchIndexStatusRequest._fields = [
  FieldMetadata("namespace", "namespace", "_namespace", str, None, PredefinedSerializer(), optional=True),
]

GetSearchIndexStatusResponse._fields = [
  FieldMetadata("indexes", "indexes", "_indexes", SearchIndexStatus, [], ListSerializer(KaggleObjectSerializer())),
]

ListApiMethodsRequest._fields = []

ListApiMethodsResponse._fields = [
  FieldMetadata("methodNames", "method_names", "_method_names", str, [], ListSerializer(PredefinedSerializer())),
]

ListEmergencyBannersRequest._fields = []

ListEmergencyBannersResponse._fields = [
  FieldMetadata("bannerConfig", "banner_config", "_banner_config", EmergencyBannersConfig, None, KaggleObjectSerializer()),
]

RenewIapTokenRequest._fields = []

RenewIapTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

ResetSearchIndexesRequest._fields = []

ResetSearchIndexRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

SearchIndexLogEntry._fields = [
  FieldMetadata("startDate", "start_date", "_start_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("endDate", "end_date", "_end_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("durationSeconds", "duration_seconds", "_duration_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("documentsIndexed", "documents_indexed", "_documents_indexed", int, 0, PredefinedSerializer()),
  FieldMetadata("percentComplete", "percent_complete", "_percent_complete", float, None, PredefinedSerializer(), optional=True),
]

SearchIndexStatus._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("rebuildScheduled", "rebuild_scheduled", "_rebuild_scheduled", bool, False, PredefinedSerializer()),
  FieldMetadata("isRebuilding", "is_rebuilding", "_is_rebuilding", bool, False, PredefinedSerializer()),
  FieldMetadata("isRunning", "is_running", "_is_running", bool, False, PredefinedSerializer()),
  FieldMetadata("lastRebuild", "last_rebuild", "_last_rebuild", SearchIndexLogEntry, None, KaggleObjectSerializer(), optional=True),
]

SiteConfig._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unused", "unused", "_unused", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

UpdateAutoFormModelRequest._fields = [
  FieldMetadata("typeName", "type_name", "_type_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", AutoFormModel, None, KaggleObjectSerializer(), optional=True),
]

UpdateEmergencyBannerRequest._fields = [
  FieldMetadata("bannerId", "banner_id", "_banner_id", str, "", PredefinedSerializer()),
  FieldMetadata("messageHtml", "message_html", "_message_html", str, "", PredefinedSerializer()),
  FieldMetadata("uriPathRegex", "uri_path_regex", "_uri_path_regex", str, "", PredefinedSerializer()),
]

UpdateNonGenieAutoFormModelRequest._fields = [
  FieldMetadata("typeName", "type_name", "_type_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", AutoFormModel, None, KaggleObjectSerializer(), optional=True),
]

UpdateSiteConfigRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

