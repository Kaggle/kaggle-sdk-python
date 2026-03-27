from kagglesdk.kaggle_object import *
from typing import Optional, List

class GetOrganizationsRequest(KaggleObject):
  r"""
  Attributes:
    filter (str)
    disable_all_org_for_admins (bool)
  """

  def __init__(self):
    self._filter = None
    self._disable_all_org_for_admins = None
    self._freeze()

  @property
  def filter(self) -> str:
    return self._filter or ""

  @filter.setter
  def filter(self, filter: Optional[str]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, str):
      raise TypeError('filter must be of type str')
    self._filter = filter

  @property
  def disable_all_org_for_admins(self) -> bool:
    return self._disable_all_org_for_admins or False

  @disable_all_org_for_admins.setter
  def disable_all_org_for_admins(self, disable_all_org_for_admins: Optional[bool]):
    if disable_all_org_for_admins is None:
      del self.disable_all_org_for_admins
      return
    if not isinstance(disable_all_org_for_admins, bool):
      raise TypeError('disable_all_org_for_admins must be of type bool')
    self._disable_all_org_for_admins = disable_all_org_for_admins


class GetOrganizationsResponse(KaggleObject):
  r"""
  Attributes:
    organizations (OrganizationCard)
  """

  def __init__(self):
    self._organizations = []
    self._freeze()

  @property
  def organizations(self) -> Optional[List[Optional['OrganizationCard']]]:
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[List[Optional['OrganizationCard']]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, list):
      raise TypeError('organizations must be of type list')
    if not all([isinstance(t, OrganizationCard) for t in organizations]):
      raise TypeError('organizations must contain only items of type OrganizationCard')
    self._organizations = organizations


class OrganizationCard(KaggleObject):
  r"""
  Attributes:
    name (str)
    id (int)
    thumbnail_image_url (str)
    slug (str)
  """

  def __init__(self):
    self._name = ""
    self._id = 0
    self._thumbnail_image_url = ""
    self._slug = ""
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
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: str):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug


GetOrganizationsRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableAllOrgForAdmins", "disable_all_org_for_admins", "_disable_all_org_for_admins", bool, None, PredefinedSerializer(), optional=True),
]

GetOrganizationsResponse._fields = [
  FieldMetadata("organizations", "organizations", "_organizations", OrganizationCard, [], ListSerializer(KaggleObjectSerializer())),
]

OrganizationCard._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
]

