import enum
from kagglesdk.cms.types.legacy_cms_service import CmsPage
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.profile_service import GetProfileResponse
from typing import Optional

class GetPageDataByUrlRequest(KaggleObject):
  r"""
  Attributes:
    relative_url (str)
      Relative url of a user profile or CMS page. For example: 'bestfitting'
      (user profile) or 'covid19' (a CMS page).
  """

  def __init__(self):
    self._relative_url = ""
    self._freeze()

  @property
  def relative_url(self) -> str:
    r"""
    Relative url of a user profile or CMS page. For example: 'bestfitting'
    (user profile) or 'covid19' (a CMS page).
    """
    return self._relative_url

  @relative_url.setter
  def relative_url(self, relative_url: str):
    if relative_url is None:
      del self.relative_url
      return
    if not isinstance(relative_url, str):
      raise TypeError('relative_url must be of type str')
    self._relative_url = relative_url


class GetPageDataByUrlResponse(KaggleObject):
  r"""
  Attributes:
    page_type (GetPageDataByUrlResponse.PageType)
    user_profile (GetProfileResponse)
    cms_page (CmsPage)
  """

  class PageType(enum.Enum):
    PAGE_TYPE_UNSPECIFIED = 0
    USER_PROFILE = 1
    CMS_PAGE = 2

  def __init__(self):
    self._page_type = self.PageType.PAGE_TYPE_UNSPECIFIED
    self._user_profile = None
    self._cms_page = None
    self._freeze()

  @property
  def page_type(self) -> 'GetPageDataByUrlResponse.PageType':
    return self._page_type

  @page_type.setter
  def page_type(self, page_type: 'GetPageDataByUrlResponse.PageType'):
    if page_type is None:
      del self.page_type
      return
    if not isinstance(page_type, GetPageDataByUrlResponse.PageType):
      raise TypeError('page_type must be of type GetPageDataByUrlResponse.PageType')
    self._page_type = page_type

  @property
  def user_profile(self) -> Optional['GetProfileResponse']:
    return self._user_profile or None

  @user_profile.setter
  def user_profile(self, user_profile: Optional['GetProfileResponse']):
    if user_profile is None:
      del self.user_profile
      return
    if not isinstance(user_profile, GetProfileResponse):
      raise TypeError('user_profile must be of type GetProfileResponse')
    del self.cms_page
    self._user_profile = user_profile

  @property
  def cms_page(self) -> Optional['CmsPage']:
    return self._cms_page or None

  @cms_page.setter
  def cms_page(self, cms_page: Optional['CmsPage']):
    if cms_page is None:
      del self.cms_page
      return
    if not isinstance(cms_page, CmsPage):
      raise TypeError('cms_page must be of type CmsPage')
    del self.user_profile
    self._cms_page = cms_page


GetPageDataByUrlRequest._fields = [
  FieldMetadata("relativeUrl", "relative_url", "_relative_url", str, "", PredefinedSerializer()),
]

GetPageDataByUrlResponse._fields = [
  FieldMetadata("pageType", "page_type", "_page_type", GetPageDataByUrlResponse.PageType, GetPageDataByUrlResponse.PageType.PAGE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userProfile", "user_profile", "_user_profile", GetProfileResponse, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("cmsPage", "cms_page", "_cms_page", CmsPage, None, KaggleObjectSerializer(), optional=True),
]

