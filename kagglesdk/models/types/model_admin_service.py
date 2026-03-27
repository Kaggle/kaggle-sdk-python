from datetime import datetime
from kagglesdk.kaggle_object import *
from kagglesdk.models.types.model_enums import ModelVersionLinkType
from typing import Optional

class AddModelImplementationRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    implementation_model_id (int)
  """

  def __init__(self):
    self._model_id = 0
    self._implementation_model_id = 0
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def implementation_model_id(self) -> int:
    return self._implementation_model_id

  @implementation_model_id.setter
  def implementation_model_id(self, implementation_model_id: int):
    if implementation_model_id is None:
      del self.implementation_model_id
      return
    if not isinstance(implementation_model_id, int):
      raise TypeError('implementation_model_id must be of type int')
    self._implementation_model_id = implementation_model_id


class AddModelVersionLinkRequest(KaggleObject):
  r"""
  Attributes:
    model_version_id (int)
    url (str)
    type (ModelVersionLinkType)
  """

  def __init__(self):
    self._model_version_id = 0
    self._url = ""
    self._type = ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def model_version_id(self) -> int:
    return self._model_version_id

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    self._model_version_id = model_version_id

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def type(self) -> 'ModelVersionLinkType':
    return self._type

  @type.setter
  def type(self, type: 'ModelVersionLinkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ModelVersionLinkType):
      raise TypeError('type must be of type ModelVersionLinkType')
    self._type = type


class DeleteModelImplementationRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    implementation_model_id (int)
  """

  def __init__(self):
    self._model_id = 0
    self._implementation_model_id = 0
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def implementation_model_id(self) -> int:
    return self._implementation_model_id

  @implementation_model_id.setter
  def implementation_model_id(self, implementation_model_id: int):
    if implementation_model_id is None:
      del self.implementation_model_id
      return
    if not isinstance(implementation_model_id, int):
      raise TypeError('implementation_model_id must be of type int')
    self._implementation_model_id = implementation_model_id


class DeleteModelVersionLinkRequest(KaggleObject):
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


class GetTfHubRedirectRequest(KaggleObject):
  r"""
  Attributes:
    tf_hub_path (str)
  """

  def __init__(self):
    self._tf_hub_path = ""
    self._freeze()

  @property
  def tf_hub_path(self) -> str:
    return self._tf_hub_path

  @tf_hub_path.setter
  def tf_hub_path(self, tf_hub_path: str):
    if tf_hub_path is None:
      del self.tf_hub_path
      return
    if not isinstance(tf_hub_path, str):
      raise TypeError('tf_hub_path must be of type str')
    self._tf_hub_path = tf_hub_path


class GetTfHubRedirectResponse(KaggleObject):
  r"""
  Attributes:
    tf_hub_redirect (TfHubRedirect)
  """

  def __init__(self):
    self._tf_hub_redirect = None
    self._freeze()

  @property
  def tf_hub_redirect(self) -> Optional['TfHubRedirect']:
    return self._tf_hub_redirect

  @tf_hub_redirect.setter
  def tf_hub_redirect(self, tf_hub_redirect: Optional['TfHubRedirect']):
    if tf_hub_redirect is None:
      del self.tf_hub_redirect
      return
    if not isinstance(tf_hub_redirect, TfHubRedirect):
      raise TypeError('tf_hub_redirect must be of type TfHubRedirect')
    self._tf_hub_redirect = tf_hub_redirect


class RecreateModelInstanceVersionArchiveRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_version_id (int)
  """

  def __init__(self):
    self._model_instance_version_id = 0
    self._freeze()

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: int):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    self._model_instance_version_id = model_instance_version_id


class RecreateModelInstanceVersionArchiveResponse(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
      The ID of the databundle version being recreated.
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    """The ID of the databundle version being recreated."""
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id


class ResetModelInstancesVersionsRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    create_time (datetime)
    reset_views_and_downloads (bool)
  """

  def __init__(self):
    self._model_id = 0
    self._create_time = None
    self._reset_views_and_downloads = None
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def create_time(self) -> datetime:
    return self._create_time or None

  @create_time.setter
  def create_time(self, create_time: Optional[datetime]):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def reset_views_and_downloads(self) -> bool:
    return self._reset_views_and_downloads or False

  @reset_views_and_downloads.setter
  def reset_views_and_downloads(self, reset_views_and_downloads: Optional[bool]):
    if reset_views_and_downloads is None:
      del self.reset_views_and_downloads
      return
    if not isinstance(reset_views_and_downloads, bool):
      raise TypeError('reset_views_and_downloads must be of type bool')
    self._reset_views_and_downloads = reset_views_and_downloads


class ResetModelInstancesVersionsResponse(KaggleObject):
  r"""
  """

  pass

class SetTfHubRedirectRequest(KaggleObject):
  r"""
  Attributes:
    tf_hub_redirect (TfHubRedirect)
  """

  def __init__(self):
    self._tf_hub_redirect = None
    self._freeze()

  @property
  def tf_hub_redirect(self) -> Optional['TfHubRedirect']:
    return self._tf_hub_redirect

  @tf_hub_redirect.setter
  def tf_hub_redirect(self, tf_hub_redirect: Optional['TfHubRedirect']):
    if tf_hub_redirect is None:
      del self.tf_hub_redirect
      return
    if not isinstance(tf_hub_redirect, TfHubRedirect):
      raise TypeError('tf_hub_redirect must be of type TfHubRedirect')
    self._tf_hub_redirect = tf_hub_redirect


class SetTfHubRedirectResponse(KaggleObject):
  r"""
  Attributes:
    tf_hub_redirect (TfHubRedirect)
  """

  def __init__(self):
    self._tf_hub_redirect = None
    self._freeze()

  @property
  def tf_hub_redirect(self) -> Optional['TfHubRedirect']:
    return self._tf_hub_redirect

  @tf_hub_redirect.setter
  def tf_hub_redirect(self, tf_hub_redirect: Optional['TfHubRedirect']):
    if tf_hub_redirect is None:
      del self.tf_hub_redirect
      return
    if not isinstance(tf_hub_redirect, TfHubRedirect):
      raise TypeError('tf_hub_redirect must be of type TfHubRedirect')
    self._tf_hub_redirect = tf_hub_redirect


class TfHubRedirect(KaggleObject):
  r"""
  Attributes:
    tf_hub_path (str)
    kaggle_path (str)
    short_kaggle_path (str)
  """

  def __init__(self):
    self._tf_hub_path = ""
    self._kaggle_path = None
    self._short_kaggle_path = None
    self._freeze()

  @property
  def tf_hub_path(self) -> str:
    return self._tf_hub_path

  @tf_hub_path.setter
  def tf_hub_path(self, tf_hub_path: str):
    if tf_hub_path is None:
      del self.tf_hub_path
      return
    if not isinstance(tf_hub_path, str):
      raise TypeError('tf_hub_path must be of type str')
    self._tf_hub_path = tf_hub_path

  @property
  def kaggle_path(self) -> str:
    return self._kaggle_path or ""

  @kaggle_path.setter
  def kaggle_path(self, kaggle_path: Optional[str]):
    if kaggle_path is None:
      del self.kaggle_path
      return
    if not isinstance(kaggle_path, str):
      raise TypeError('kaggle_path must be of type str')
    self._kaggle_path = kaggle_path

  @property
  def short_kaggle_path(self) -> str:
    return self._short_kaggle_path or ""

  @short_kaggle_path.setter
  def short_kaggle_path(self, short_kaggle_path: Optional[str]):
    if short_kaggle_path is None:
      del self.short_kaggle_path
      return
    if not isinstance(short_kaggle_path, str):
      raise TypeError('short_kaggle_path must be of type str')
    self._short_kaggle_path = short_kaggle_path


class UpdateModelSlugRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    old_model_slug (str)
    new_model_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._old_model_slug = ""
    self._new_model_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def old_model_slug(self) -> str:
    return self._old_model_slug

  @old_model_slug.setter
  def old_model_slug(self, old_model_slug: str):
    if old_model_slug is None:
      del self.old_model_slug
      return
    if not isinstance(old_model_slug, str):
      raise TypeError('old_model_slug must be of type str')
    self._old_model_slug = old_model_slug

  @property
  def new_model_slug(self) -> str:
    return self._new_model_slug

  @new_model_slug.setter
  def new_model_slug(self, new_model_slug: str):
    if new_model_slug is None:
      del self.new_model_slug
      return
    if not isinstance(new_model_slug, str):
      raise TypeError('new_model_slug must be of type str')
    self._new_model_slug = new_model_slug


class UpdateModelSlugResponse(KaggleObject):
  r"""
  Attributes:
    new_url (str)
  """

  def __init__(self):
    self._new_url = ""
    self._freeze()

  @property
  def new_url(self) -> str:
    return self._new_url

  @new_url.setter
  def new_url(self, new_url: str):
    if new_url is None:
      del self.new_url
      return
    if not isinstance(new_url, str):
      raise TypeError('new_url must be of type str')
    self._new_url = new_url


AddModelImplementationRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("implementationModelId", "implementation_model_id", "_implementation_model_id", int, 0, PredefinedSerializer()),
]

AddModelVersionLinkRequest._fields = [
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", ModelVersionLinkType, ModelVersionLinkType.MODEL_VERSION_LINK_TYPE_UNSPECIFIED, EnumSerializer()),
]

DeleteModelImplementationRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("implementationModelId", "implementation_model_id", "_implementation_model_id", int, 0, PredefinedSerializer()),
]

DeleteModelVersionLinkRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

GetTfHubRedirectRequest._fields = [
  FieldMetadata("tfHubPath", "tf_hub_path", "_tf_hub_path", str, "", PredefinedSerializer()),
]

GetTfHubRedirectResponse._fields = [
  FieldMetadata("tfHubRedirect", "tf_hub_redirect", "_tf_hub_redirect", TfHubRedirect, None, KaggleObjectSerializer()),
]

RecreateModelInstanceVersionArchiveRequest._fields = [
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
]

RecreateModelInstanceVersionArchiveResponse._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
]

ResetModelInstancesVersionsRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("resetViewsAndDownloads", "reset_views_and_downloads", "_reset_views_and_downloads", bool, None, PredefinedSerializer(), optional=True),
]

ResetModelInstancesVersionsResponse._fields = []

SetTfHubRedirectRequest._fields = [
  FieldMetadata("tfHubRedirect", "tf_hub_redirect", "_tf_hub_redirect", TfHubRedirect, None, KaggleObjectSerializer()),
]

SetTfHubRedirectResponse._fields = [
  FieldMetadata("tfHubRedirect", "tf_hub_redirect", "_tf_hub_redirect", TfHubRedirect, None, KaggleObjectSerializer()),
]

TfHubRedirect._fields = [
  FieldMetadata("tfHubPath", "tf_hub_path", "_tf_hub_path", str, "", PredefinedSerializer()),
  FieldMetadata("kagglePath", "kaggle_path", "_kaggle_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("shortKagglePath", "short_kaggle_path", "_short_kaggle_path", str, None, PredefinedSerializer(), optional=True),
]

UpdateModelSlugRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("oldModelSlug", "old_model_slug", "_old_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("newModelSlug", "new_model_slug", "_new_model_slug", str, "", PredefinedSerializer()),
]

UpdateModelSlugResponse._fields = [
  FieldMetadata("newUrl", "new_url", "_new_url", str, "", PredefinedSerializer()),
]

