from kagglesdk.kaggle_object import *
from typing import Optional

class Organization(KaggleObject):
  r"""
  TODO: Move into Kaggle.Sdk.Users namespace and apply to existing code which
  uses Kaggle.Sdk.Models.Organization, which should be deleted. Subset of the
  full Organization object with everything needed for our new world where
  Organization pages are turned down, and only shown with minimal details in
  Comps and Datasets pages.

  Attributes:
    slug (str)
    name (str)
    thumbnail_image_url (str)
    profile_url (str)
  """

  def __init__(self):
    self._slug = ""
    self._name = ""
    self._thumbnail_image_url = None
    self._profile_url = ""
    self._freeze()

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
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url or ""

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: Optional[str]):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

  @property
  def profile_url(self) -> str:
    return self._profile_url

  @profile_url.setter
  def profile_url(self, profile_url: str):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url


Organization._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, "", PredefinedSerializer()),
]

