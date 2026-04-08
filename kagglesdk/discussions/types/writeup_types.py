from datetime import datetime
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.discussions.types.forum_message import CommentForumMessage
from kagglesdk.discussions.types.writeup_enums import WriteUpLinkLocation, WriteUpLinkMediaType, WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.security.types.security_types import KaggleResourceType
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class WriteUp(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the WriteUp
    topic_id (int)
      FK of ForumTopic
    title (str)
      Title of the WriteUp
    subtitle (str)
      Subtitle of the WriteUp
    message (CommentForumMessage)
      Message of the WriteUp
    type (WriteUpType)
      Type of WriteUp used for different contexts (i.e. competition vs hackathon
      WriteUp)
    cover_image_url (str)
      Url of banner image to appear at the top of the WriteUp
    write_up_links (WriteUpLink)
      List of all links included in the WriteUp
    tags (Tag)
      List of tags connected to the WriteUp
    slug (str)
      Unique path name for clean URLs
    url (str)
      On-the-fly created URL pointing to the WriteUp based on the slug
    create_time (datetime)
      Time when WriteUp was created
    update_time (datetime)
      Time when WriteUp was last updated
    can_edit (bool)
      Indicates whether the requesting user has permission to edit the WriteUp
    can_delete (bool)
      Indicates whether the requesting user has permission to delete the WriteUp
    content_state (ContentState)
      Represents the content state of the WriteUp
    is_spammed (bool)
      Indicates whether the WriteUp has been marked as spam by moderation
    license (License)
      The license that applies to the WriteUp
    authors (str)
      Comma-separated list of the authors of the WriteUp
    thumbnail_image_url (str)
      Url of thumbnail image to represent the WriteUp
    original_image_url (str)
      Url of original image that's used by the cover and thumbnail image
    image_info (WriteUpImageInfo)
      Crop settings for cover and thumbnail images
    can_pin (bool)
      Indicates whether the requesting user can pin the WriteUp to their profile
    collaborators (UserAvatar)
      Collaborators on Competition or Hackathon WriteUp, i.e. team members in a
      hackathon competition
    publish_time (datetime)
      Time when WriteUp was last published
  """

  def __init__(self):
    self._id = 0
    self._topic_id = 0
    self._title = ""
    self._subtitle = ""
    self._message = None
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._cover_image_url = ""
    self._write_up_links = []
    self._tags = []
    self._slug = ""
    self._url = ""
    self._create_time = None
    self._update_time = None
    self._can_edit = False
    self._can_delete = False
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._is_spammed = False
    self._license = None
    self._authors = None
    self._thumbnail_image_url = ""
    self._original_image_url = ""
    self._image_info = None
    self._can_pin = False
    self._collaborators = []
    self._publish_time = None
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the WriteUp"""
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
  def topic_id(self) -> int:
    """FK of ForumTopic"""
    return self._topic_id

  @topic_id.setter
  def topic_id(self, topic_id: int):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def title(self) -> str:
    """Title of the WriteUp"""
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def subtitle(self) -> str:
    """Subtitle of the WriteUp"""
    return self._subtitle

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def message(self) -> Optional['CommentForumMessage']:
    """Message of the WriteUp"""
    return self._message

  @message.setter
  def message(self, message: Optional['CommentForumMessage']):
    if message is None:
      del self.message
      return
    if not isinstance(message, CommentForumMessage):
      raise TypeError('message must be of type CommentForumMessage')
    self._message = message

  @property
  def type(self) -> 'WriteUpType':
    r"""
    Type of WriteUp used for different contexts (i.e. competition vs hackathon
    WriteUp)
    """
    return self._type

  @type.setter
  def type(self, type: 'WriteUpType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, WriteUpType):
      raise TypeError('type must be of type WriteUpType')
    self._type = type

  @property
  def cover_image_url(self) -> str:
    """Url of banner image to appear at the top of the WriteUp"""
    return self._cover_image_url

  @cover_image_url.setter
  def cover_image_url(self, cover_image_url: str):
    if cover_image_url is None:
      del self.cover_image_url
      return
    if not isinstance(cover_image_url, str):
      raise TypeError('cover_image_url must be of type str')
    self._cover_image_url = cover_image_url

  @property
  def write_up_links(self) -> Optional[List[Optional['WriteUpLink']]]:
    """List of all links included in the WriteUp"""
    return self._write_up_links

  @write_up_links.setter
  def write_up_links(self, write_up_links: Optional[List[Optional['WriteUpLink']]]):
    if write_up_links is None:
      del self.write_up_links
      return
    if not isinstance(write_up_links, list):
      raise TypeError('write_up_links must be of type list')
    if not all([isinstance(t, WriteUpLink) for t in write_up_links]):
      raise TypeError('write_up_links must contain only items of type WriteUpLink')
    self._write_up_links = write_up_links

  @property
  def tags(self) -> Optional[List[Optional['Tag']]]:
    """List of tags connected to the WriteUp"""
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[Optional['Tag']]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, Tag) for t in tags]):
      raise TypeError('tags must contain only items of type Tag')
    self._tags = tags

  @property
  def slug(self) -> str:
    """Unique path name for clean URLs"""
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
  def url(self) -> str:
    """On-the-fly created URL pointing to the WriteUp based on the slug"""
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
  def create_time(self) -> datetime:
    """Time when WriteUp was created"""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def update_time(self) -> datetime:
    """Time when WriteUp was last updated"""
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def can_edit(self) -> bool:
    """Indicates whether the requesting user has permission to edit the WriteUp"""
    return self._can_edit

  @can_edit.setter
  def can_edit(self, can_edit: bool):
    if can_edit is None:
      del self.can_edit
      return
    if not isinstance(can_edit, bool):
      raise TypeError('can_edit must be of type bool')
    self._can_edit = can_edit

  @property
  def can_delete(self) -> bool:
    """Indicates whether the requesting user has permission to delete the WriteUp"""
    return self._can_delete

  @can_delete.setter
  def can_delete(self, can_delete: bool):
    if can_delete is None:
      del self.can_delete
      return
    if not isinstance(can_delete, bool):
      raise TypeError('can_delete must be of type bool')
    self._can_delete = can_delete

  @property
  def content_state(self) -> 'ContentState':
    """Represents the content state of the WriteUp"""
    return self._content_state

  @content_state.setter
  def content_state(self, content_state: 'ContentState'):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def is_spammed(self) -> bool:
    """Indicates whether the WriteUp has been marked as spam by moderation"""
    return self._is_spammed

  @is_spammed.setter
  def is_spammed(self, is_spammed: bool):
    if is_spammed is None:
      del self.is_spammed
      return
    if not isinstance(is_spammed, bool):
      raise TypeError('is_spammed must be of type bool')
    self._is_spammed = is_spammed

  @property
  def license(self) -> Optional['License']:
    """The license that applies to the WriteUp"""
    return self._license or None

  @license.setter
  def license(self, license: Optional[Optional['License']]):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def authors(self) -> str:
    """Comma-separated list of the authors of the WriteUp"""
    return self._authors or ""

  @authors.setter
  def authors(self, authors: Optional[str]):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, str):
      raise TypeError('authors must be of type str')
    self._authors = authors

  @property
  def thumbnail_image_url(self) -> str:
    """Url of thumbnail image to represent the WriteUp"""
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
  def original_image_url(self) -> str:
    """Url of original image that's used by the cover and thumbnail image"""
    return self._original_image_url

  @original_image_url.setter
  def original_image_url(self, original_image_url: str):
    if original_image_url is None:
      del self.original_image_url
      return
    if not isinstance(original_image_url, str):
      raise TypeError('original_image_url must be of type str')
    self._original_image_url = original_image_url

  @property
  def image_info(self) -> Optional['WriteUpImageInfo']:
    """Crop settings for cover and thumbnail images"""
    return self._image_info

  @image_info.setter
  def image_info(self, image_info: Optional['WriteUpImageInfo']):
    if image_info is None:
      del self.image_info
      return
    if not isinstance(image_info, WriteUpImageInfo):
      raise TypeError('image_info must be of type WriteUpImageInfo')
    self._image_info = image_info

  @property
  def can_pin(self) -> bool:
    """Indicates whether the requesting user can pin the WriteUp to their profile"""
    return self._can_pin

  @can_pin.setter
  def can_pin(self, can_pin: bool):
    if can_pin is None:
      del self.can_pin
      return
    if not isinstance(can_pin, bool):
      raise TypeError('can_pin must be of type bool')
    self._can_pin = can_pin

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    r"""
    Collaborators on Competition or Hackathon WriteUp, i.e. team members in a
    hackathon competition
    """
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['UserAvatar']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, UserAvatar) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type UserAvatar')
    self._collaborators = collaborators

  @property
  def publish_time(self) -> datetime:
    """Time when WriteUp was last published"""
    return self._publish_time

  @publish_time.setter
  def publish_time(self, publish_time: datetime):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time


class WriteUpImageInfo(KaggleObject):
  r"""
  Attributes:
    card_image_left (int)
    card_image_top (int)
    card_image_height (int)
    card_image_width (int)
    cover_image_left (int)
    cover_image_height (int)
    cover_image_top (int)
    cover_image_width (int)
  """

  def __init__(self):
    self._card_image_left = 0
    self._card_image_top = 0
    self._card_image_height = 0
    self._card_image_width = 0
    self._cover_image_left = 0
    self._cover_image_height = 0
    self._cover_image_top = 0
    self._cover_image_width = 0
    self._freeze()

  @property
  def card_image_left(self) -> int:
    return self._card_image_left

  @card_image_left.setter
  def card_image_left(self, card_image_left: int):
    if card_image_left is None:
      del self.card_image_left
      return
    if not isinstance(card_image_left, int):
      raise TypeError('card_image_left must be of type int')
    self._card_image_left = card_image_left

  @property
  def card_image_top(self) -> int:
    return self._card_image_top

  @card_image_top.setter
  def card_image_top(self, card_image_top: int):
    if card_image_top is None:
      del self.card_image_top
      return
    if not isinstance(card_image_top, int):
      raise TypeError('card_image_top must be of type int')
    self._card_image_top = card_image_top

  @property
  def card_image_height(self) -> int:
    return self._card_image_height

  @card_image_height.setter
  def card_image_height(self, card_image_height: int):
    if card_image_height is None:
      del self.card_image_height
      return
    if not isinstance(card_image_height, int):
      raise TypeError('card_image_height must be of type int')
    self._card_image_height = card_image_height

  @property
  def card_image_width(self) -> int:
    return self._card_image_width

  @card_image_width.setter
  def card_image_width(self, card_image_width: int):
    if card_image_width is None:
      del self.card_image_width
      return
    if not isinstance(card_image_width, int):
      raise TypeError('card_image_width must be of type int')
    self._card_image_width = card_image_width

  @property
  def cover_image_left(self) -> int:
    return self._cover_image_left

  @cover_image_left.setter
  def cover_image_left(self, cover_image_left: int):
    if cover_image_left is None:
      del self.cover_image_left
      return
    if not isinstance(cover_image_left, int):
      raise TypeError('cover_image_left must be of type int')
    self._cover_image_left = cover_image_left

  @property
  def cover_image_height(self) -> int:
    return self._cover_image_height

  @cover_image_height.setter
  def cover_image_height(self, cover_image_height: int):
    if cover_image_height is None:
      del self.cover_image_height
      return
    if not isinstance(cover_image_height, int):
      raise TypeError('cover_image_height must be of type int')
    self._cover_image_height = cover_image_height

  @property
  def cover_image_top(self) -> int:
    return self._cover_image_top

  @cover_image_top.setter
  def cover_image_top(self, cover_image_top: int):
    if cover_image_top is None:
      del self.cover_image_top
      return
    if not isinstance(cover_image_top, int):
      raise TypeError('cover_image_top must be of type int')
    self._cover_image_top = cover_image_top

  @property
  def cover_image_width(self) -> int:
    return self._cover_image_width

  @cover_image_width.setter
  def cover_image_width(self, cover_image_width: int):
    if cover_image_width is None:
      del self.cover_image_width
      return
    if not isinstance(cover_image_width, int):
      raise TypeError('cover_image_width must be of type int')
    self._cover_image_width = cover_image_width


class WriteUpLink(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the WriteUpLink
    title (str)
      Title of the link
    sort_key (float)
      Used to specify the sort ordering of links
    location (WriteUpLinkLocation)
      Determines where links should be displayed in the UI
    url (str)
      URL destination of the link
    dataset_id (int)
    kernel_id (int)
    model_id (int)
    description (str)
      Provides more context about the current link
    image (CroppedImageUpload)
      Only eligible on requests. If set, the provided image blob will be
      stored in GCS and a GCS URL associated with the link. 'url' should not be
      set if this field is provided.
    media_type (WriteUpLinkMediaType)
      Indicates the media type of the link's url, as a best effort. This should
      always be set when the link location is 'carousel'.
    resource (WriteUpLinkResource)
      Resource data to be presented in cards
    external_thumbnail_image_url (str)
      External image URL that points to either a thumbnail image or favicon
      icon for a non-Kaggle link
    original_image_url (str)
      Image URL for the full size, uncropped image for a carousel image
      TODO(b/407831686): Clean up this pattern - we shouldn't have a specific
      field that only applies to some types of WriteUpLinks.
    entity_type (KaggleResourceType)
      Specifies if the entity is a dataset, model, or kernel
    benchmark_id (int)
  """

  def __init__(self):
    self._id = 0
    self._title = ""
    self._sort_key = 0.0
    self._location = WriteUpLinkLocation.WRITE_UP_LINK_LOCATION_UNSPECIFIED
    self._url = None
    self._dataset_id = None
    self._kernel_id = None
    self._model_id = None
    self._description = None
    self._image = None
    self._media_type = WriteUpLinkMediaType.WRITE_UP_LINK_MEDIA_TYPE_UNSPECIFIED
    self._resource = None
    self._external_thumbnail_image_url = None
    self._original_image_url = None
    self._entity_type = None
    self._benchmark_id = None
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the WriteUpLink"""
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
  def title(self) -> str:
    """Title of the link"""
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def sort_key(self) -> float:
    """Used to specify the sort ordering of links"""
    return self._sort_key

  @sort_key.setter
  def sort_key(self, sort_key: float):
    if sort_key is None:
      del self.sort_key
      return
    if not isinstance(sort_key, float):
      raise TypeError('sort_key must be of type float')
    self._sort_key = sort_key

  @property
  def location(self) -> 'WriteUpLinkLocation':
    """Determines where links should be displayed in the UI"""
    return self._location

  @location.setter
  def location(self, location: 'WriteUpLinkLocation'):
    if location is None:
      del self.location
      return
    if not isinstance(location, WriteUpLinkLocation):
      raise TypeError('location must be of type WriteUpLinkLocation')
    self._location = location

  @property
  def media_type(self) -> 'WriteUpLinkMediaType':
    r"""
    Indicates the media type of the link's url, as a best effort. This should
    always be set when the link location is 'carousel'.
    """
    return self._media_type

  @media_type.setter
  def media_type(self, media_type: 'WriteUpLinkMediaType'):
    if media_type is None:
      del self.media_type
      return
    if not isinstance(media_type, WriteUpLinkMediaType):
      raise TypeError('media_type must be of type WriteUpLinkMediaType')
    self._media_type = media_type

  @property
  def url(self) -> str:
    """URL destination of the link"""
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.kernel_id
    del self.model_id
    del self.benchmark_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.dataset_id
    del self.model_id
    del self.benchmark_id
    self._kernel_id = kernel_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.benchmark_id
    self._model_id = model_id

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id or 0

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    self._benchmark_id = benchmark_id

  @property
  def description(self) -> str:
    """Provides more context about the current link"""
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
  def image(self) -> Optional['CroppedImageUpload']:
    r"""
    Only eligible on requests. If set, the provided image blob will be
    stored in GCS and a GCS URL associated with the link. 'url' should not be
    set if this field is provided.
    """
    return self._image

  @image.setter
  def image(self, image: Optional['CroppedImageUpload']):
    if image is None:
      del self.image
      return
    if not isinstance(image, CroppedImageUpload):
      raise TypeError('image must be of type CroppedImageUpload')
    self._image = image

  @property
  def resource(self) -> Optional['WriteUpLinkResource']:
    """Resource data to be presented in cards"""
    return self._resource

  @resource.setter
  def resource(self, resource: Optional['WriteUpLinkResource']):
    if resource is None:
      del self.resource
      return
    if not isinstance(resource, WriteUpLinkResource):
      raise TypeError('resource must be of type WriteUpLinkResource')
    self._resource = resource

  @property
  def external_thumbnail_image_url(self) -> str:
    r"""
    External image URL that points to either a thumbnail image or favicon
    icon for a non-Kaggle link
    """
    return self._external_thumbnail_image_url or ""

  @external_thumbnail_image_url.setter
  def external_thumbnail_image_url(self, external_thumbnail_image_url: Optional[str]):
    if external_thumbnail_image_url is None:
      del self.external_thumbnail_image_url
      return
    if not isinstance(external_thumbnail_image_url, str):
      raise TypeError('external_thumbnail_image_url must be of type str')
    self._external_thumbnail_image_url = external_thumbnail_image_url

  @property
  def original_image_url(self) -> str:
    r"""
    Image URL for the full size, uncropped image for a carousel image
    TODO(b/407831686): Clean up this pattern - we shouldn't have a specific
    field that only applies to some types of WriteUpLinks.
    """
    return self._original_image_url or ""

  @original_image_url.setter
  def original_image_url(self, original_image_url: Optional[str]):
    if original_image_url is None:
      del self.original_image_url
      return
    if not isinstance(original_image_url, str):
      raise TypeError('original_image_url must be of type str')
    self._original_image_url = original_image_url

  @property
  def entity_type(self) -> 'KaggleResourceType':
    """Specifies if the entity is a dataset, model, or kernel"""
    return self._entity_type or KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED

  @entity_type.setter
  def entity_type(self, entity_type: Optional['KaggleResourceType']):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleResourceType):
      raise TypeError('entity_type must be of type KaggleResourceType')
    self._entity_type = entity_type


class WriteUpLinkResource(KaggleObject):
  r"""
  Similar to shape and nature to kaggle.users.ProfilePin
  LINT.IfChange

  Attributes:
    date (datetime)
    upvote_count (int)
    medal (Medal)
    owner_user (UserAvatar)
    owner_organization (OrganizationCard)
    collaborators (UserAvatar)
    usability_rating (float)
    thumbnail_image_url (str)
    is_private (bool)
    is_phone_verified (bool)
  """

  def __init__(self):
    self._date = None
    self._upvote_count = None
    self._medal = None
    self._owner_user = None
    self._owner_organization = None
    self._collaborators = []
    self._usability_rating = None
    self._thumbnail_image_url = None
    self._is_private = None
    self._is_phone_verified = None
    self._freeze()

  @property
  def date(self) -> datetime:
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

  @property
  def upvote_count(self) -> int:
    return self._upvote_count or 0

  @upvote_count.setter
  def upvote_count(self, upvote_count: Optional[int]):
    if upvote_count is None:
      del self.upvote_count
      return
    if not isinstance(upvote_count, int):
      raise TypeError('upvote_count must be of type int')
    self._upvote_count = upvote_count

  @property
  def medal(self) -> 'Medal':
    return self._medal or Medal.MEDAL_UNSPECIFIED

  @medal.setter
  def medal(self, medal: Optional['Medal']):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional['UserAvatar']):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    del self.owner_organization
    self._owner_user = owner_user

  @property
  def owner_organization(self) -> Optional['OrganizationCard']:
    return self._owner_organization or None

  @owner_organization.setter
  def owner_organization(self, owner_organization: Optional['OrganizationCard']):
    if owner_organization is None:
      del self.owner_organization
      return
    if not isinstance(owner_organization, OrganizationCard):
      raise TypeError('owner_organization must be of type OrganizationCard')
    del self.owner_user
    self._owner_organization = owner_organization

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['UserAvatar']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, UserAvatar) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type UserAvatar')
    self._collaborators = collaborators

  @property
  def usability_rating(self) -> float:
    return self._usability_rating or 0.0

  @usability_rating.setter
  def usability_rating(self, usability_rating: Optional[float]):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, float):
      raise TypeError('usability_rating must be of type float')
    self._usability_rating = usability_rating

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
  def is_private(self) -> bool:
    return self._is_private or False

  @is_private.setter
  def is_private(self, is_private: Optional[bool]):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def is_phone_verified(self) -> bool:
    return self._is_phone_verified or False

  @is_phone_verified.setter
  def is_phone_verified(self, is_phone_verified: Optional[bool]):
    if is_phone_verified is None:
      del self.is_phone_verified
      return
    if not isinstance(is_phone_verified, bool):
      raise TypeError('is_phone_verified must be of type bool')
    self._is_phone_verified = is_phone_verified


WriteUp._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", CommentForumMessage, None, KaggleObjectSerializer()),
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("writeUpLinks", "write_up_links", "_write_up_links", WriteUpLink, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("canEdit", "can_edit", "_can_edit", bool, False, PredefinedSerializer()),
  FieldMetadata("canDelete", "can_delete", "_can_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isSpammed", "is_spammed", "_is_spammed", bool, False, PredefinedSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authors", "authors", "_authors", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("originalImageUrl", "original_image_url", "_original_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("imageInfo", "image_info", "_image_info", WriteUpImageInfo, None, KaggleObjectSerializer()),
  FieldMetadata("canPin", "can_pin", "_can_pin", bool, False, PredefinedSerializer()),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer()),
]

WriteUpImageInfo._fields = [
  FieldMetadata("cardImageLeft", "card_image_left", "_card_image_left", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageTop", "card_image_top", "_card_image_top", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageHeight", "card_image_height", "_card_image_height", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageWidth", "card_image_width", "_card_image_width", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageLeft", "cover_image_left", "_cover_image_left", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageHeight", "cover_image_height", "_cover_image_height", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageTop", "cover_image_top", "_cover_image_top", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageWidth", "cover_image_width", "_cover_image_width", int, 0, PredefinedSerializer()),
]

WriteUpLink._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("sortKey", "sort_key", "_sort_key", float, 0.0, PredefinedSerializer()),
  FieldMetadata("location", "location", "_location", WriteUpLinkLocation, WriteUpLinkLocation.WRITE_UP_LINK_LOCATION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("image", "image", "_image", CroppedImageUpload, None, KaggleObjectSerializer()),
  FieldMetadata("mediaType", "media_type", "_media_type", WriteUpLinkMediaType, WriteUpLinkMediaType.WRITE_UP_LINK_MEDIA_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("resource", "resource", "_resource", WriteUpLinkResource, None, KaggleObjectSerializer()),
  FieldMetadata("externalThumbnailImageUrl", "external_thumbnail_image_url", "_external_thumbnail_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("originalImageUrl", "original_image_url", "_original_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleResourceType, None, EnumSerializer(), optional=True),
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, None, PredefinedSerializer(), optional=True),
]

WriteUpLinkResource._fields = [
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("upvoteCount", "upvote_count", "_upvote_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", Medal, None, EnumSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("ownerOrganization", "owner_organization", "_owner_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, None, PredefinedSerializer(), optional=True),
]

