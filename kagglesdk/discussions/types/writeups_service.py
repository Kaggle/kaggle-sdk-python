from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.discussions.types.discussions_service import Message
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.discussions.types.writeup_types import WriteUpLink
from kagglesdk.kaggle_object import *
from typing import List, Optional, Dict

class BatchForceUpdateWriteUpContentStateRequest(KaggleObject):
  r"""
  Attributes:
    write_up_ids (int)
      One or more WriteUp primary key ids
    target_content_state (ContentState)
      The desired ContentState for the list of Writeups to be transitioned to.
    target_published_hackathon_license_id (int)
      The desired license id to set on hackathon write ups, if transitioned to
      published. Ignored for all other Writeup types or if Hackathon Writeups are
      not moving to published.
  """

  def __init__(self):
    self._write_up_ids = []
    self._target_content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._target_published_hackathon_license_id = None
    self._freeze()

  @property
  def write_up_ids(self) -> Optional[List[int]]:
    """One or more WriteUp primary key ids"""
    return self._write_up_ids

  @write_up_ids.setter
  def write_up_ids(self, write_up_ids: Optional[List[int]]):
    if write_up_ids is None:
      del self.write_up_ids
      return
    if not isinstance(write_up_ids, list):
      raise TypeError('write_up_ids must be of type list')
    if not all([isinstance(t, int) for t in write_up_ids]):
      raise TypeError('write_up_ids must contain only items of type int')
    self._write_up_ids = write_up_ids

  @property
  def target_content_state(self) -> 'ContentState':
    """The desired ContentState for the list of Writeups to be transitioned to."""
    return self._target_content_state

  @target_content_state.setter
  def target_content_state(self, target_content_state: 'ContentState'):
    if target_content_state is None:
      del self.target_content_state
      return
    if not isinstance(target_content_state, ContentState):
      raise TypeError('target_content_state must be of type ContentState')
    self._target_content_state = target_content_state

  @property
  def target_published_hackathon_license_id(self) -> int:
    r"""
    The desired license id to set on hackathon write ups, if transitioned to
    published. Ignored for all other Writeup types or if Hackathon Writeups are
    not moving to published.
    """
    return self._target_published_hackathon_license_id or 0

  @target_published_hackathon_license_id.setter
  def target_published_hackathon_license_id(self, target_published_hackathon_license_id: Optional[int]):
    if target_published_hackathon_license_id is None:
      del self.target_published_hackathon_license_id
      return
    if not isinstance(target_published_hackathon_license_id, int):
      raise TypeError('target_published_hackathon_license_id must be of type int')
    self._target_published_hackathon_license_id = target_published_hackathon_license_id


class BatchForceUpdateWriteUpContentStateResponse(KaggleObject):
  r"""
  Attributes:
    updated_write_up_ids (int)
      The WriteUp ids that were successfully updated.
    updated_write_up_count (int)
      The number of WriteUp ids that were successfully updated.
    failed_write_up_ids (int)
      The WriteUp ids that were not successfully updated.
    failed_write_up_count (int)
      The number of WriteUp ids that were not successfully updated.
  """

  def __init__(self):
    self._updated_write_up_ids = []
    self._updated_write_up_count = 0
    self._failed_write_up_ids = []
    self._failed_write_up_count = 0
    self._freeze()

  @property
  def updated_write_up_ids(self) -> Optional[List[int]]:
    """The WriteUp ids that were successfully updated."""
    return self._updated_write_up_ids

  @updated_write_up_ids.setter
  def updated_write_up_ids(self, updated_write_up_ids: Optional[List[int]]):
    if updated_write_up_ids is None:
      del self.updated_write_up_ids
      return
    if not isinstance(updated_write_up_ids, list):
      raise TypeError('updated_write_up_ids must be of type list')
    if not all([isinstance(t, int) for t in updated_write_up_ids]):
      raise TypeError('updated_write_up_ids must contain only items of type int')
    self._updated_write_up_ids = updated_write_up_ids

  @property
  def updated_write_up_count(self) -> int:
    """The number of WriteUp ids that were successfully updated."""
    return self._updated_write_up_count

  @updated_write_up_count.setter
  def updated_write_up_count(self, updated_write_up_count: int):
    if updated_write_up_count is None:
      del self.updated_write_up_count
      return
    if not isinstance(updated_write_up_count, int):
      raise TypeError('updated_write_up_count must be of type int')
    self._updated_write_up_count = updated_write_up_count

  @property
  def failed_write_up_ids(self) -> Optional[List[int]]:
    """The WriteUp ids that were not successfully updated."""
    return self._failed_write_up_ids

  @failed_write_up_ids.setter
  def failed_write_up_ids(self, failed_write_up_ids: Optional[List[int]]):
    if failed_write_up_ids is None:
      del self.failed_write_up_ids
      return
    if not isinstance(failed_write_up_ids, list):
      raise TypeError('failed_write_up_ids must be of type list')
    if not all([isinstance(t, int) for t in failed_write_up_ids]):
      raise TypeError('failed_write_up_ids must contain only items of type int')
    self._failed_write_up_ids = failed_write_up_ids

  @property
  def failed_write_up_count(self) -> int:
    """The number of WriteUp ids that were not successfully updated."""
    return self._failed_write_up_count

  @failed_write_up_count.setter
  def failed_write_up_count(self, failed_write_up_count: int):
    if failed_write_up_count is None:
      del self.failed_write_up_count
      return
    if not isinstance(failed_write_up_count, int):
      raise TypeError('failed_write_up_count must be of type int')
    self._failed_write_up_count = failed_write_up_count


class CopyWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    source_write_up_id (int)
      ID of the WriteUp to copy.
    target_forum_id (int)
      ID of the Forum where the new WriteUp should be created.
    target_team_id (int)
      Optional: ID of the Team who should own the new WriteUp (for hackathon
      projects).
    target_competition_id (int)
      Optional: ID of the Competition where the new WriteUp should be created.
    target_owner_host_user_id (int)
      Optional: User ID of the host that should own the new WriteUp.
    target_owner_judge_user_id (int)
      Optional: User ID of the judge that should own the new WriteUp.
    track_id_mapping (int)
      Optional: mapping of source track IDs to target track IDs.
  """

  def __init__(self):
    self._source_write_up_id = 0
    self._target_forum_id = 0
    self._target_team_id = None
    self._target_competition_id = None
    self._target_owner_host_user_id = None
    self._target_owner_judge_user_id = None
    self._track_id_mapping = {}
    self._freeze()

  @property
  def source_write_up_id(self) -> int:
    """ID of the WriteUp to copy."""
    return self._source_write_up_id

  @source_write_up_id.setter
  def source_write_up_id(self, source_write_up_id: int):
    if source_write_up_id is None:
      del self.source_write_up_id
      return
    if not isinstance(source_write_up_id, int):
      raise TypeError('source_write_up_id must be of type int')
    self._source_write_up_id = source_write_up_id

  @property
  def target_forum_id(self) -> int:
    """ID of the Forum where the new WriteUp should be created."""
    return self._target_forum_id

  @target_forum_id.setter
  def target_forum_id(self, target_forum_id: int):
    if target_forum_id is None:
      del self.target_forum_id
      return
    if not isinstance(target_forum_id, int):
      raise TypeError('target_forum_id must be of type int')
    self._target_forum_id = target_forum_id

  @property
  def target_team_id(self) -> int:
    r"""
    Optional: ID of the Team who should own the new WriteUp (for hackathon
    projects).
    """
    return self._target_team_id or 0

  @target_team_id.setter
  def target_team_id(self, target_team_id: Optional[int]):
    if target_team_id is None:
      del self.target_team_id
      return
    if not isinstance(target_team_id, int):
      raise TypeError('target_team_id must be of type int')
    self._target_team_id = target_team_id

  @property
  def target_competition_id(self) -> int:
    """Optional: ID of the Competition where the new WriteUp should be created."""
    return self._target_competition_id or 0

  @target_competition_id.setter
  def target_competition_id(self, target_competition_id: Optional[int]):
    if target_competition_id is None:
      del self.target_competition_id
      return
    if not isinstance(target_competition_id, int):
      raise TypeError('target_competition_id must be of type int')
    self._target_competition_id = target_competition_id

  @property
  def target_owner_host_user_id(self) -> int:
    """Optional: User ID of the host that should own the new WriteUp."""
    return self._target_owner_host_user_id or 0

  @target_owner_host_user_id.setter
  def target_owner_host_user_id(self, target_owner_host_user_id: Optional[int]):
    if target_owner_host_user_id is None:
      del self.target_owner_host_user_id
      return
    if not isinstance(target_owner_host_user_id, int):
      raise TypeError('target_owner_host_user_id must be of type int')
    self._target_owner_host_user_id = target_owner_host_user_id

  @property
  def target_owner_judge_user_id(self) -> int:
    """Optional: User ID of the judge that should own the new WriteUp."""
    return self._target_owner_judge_user_id or 0

  @target_owner_judge_user_id.setter
  def target_owner_judge_user_id(self, target_owner_judge_user_id: Optional[int]):
    if target_owner_judge_user_id is None:
      del self.target_owner_judge_user_id
      return
    if not isinstance(target_owner_judge_user_id, int):
      raise TypeError('target_owner_judge_user_id must be of type int')
    self._target_owner_judge_user_id = target_owner_judge_user_id

  @property
  def track_id_mapping(self) -> Optional[Dict[int, int]]:
    """Optional: mapping of source track IDs to target track IDs."""
    return self._track_id_mapping

  @track_id_mapping.setter
  def track_id_mapping(self, track_id_mapping: Optional[Dict[int, int]]):
    if track_id_mapping is None:
      del self.track_id_mapping
      return
    if not isinstance(track_id_mapping, dict):
      raise TypeError('track_id_mapping must be of type dict')
    if not all([isinstance(v, int) for k, v in track_id_mapping]):
      raise TypeError('track_id_mapping must contain only items of type int')
    self._track_id_mapping = track_id_mapping


class CreateWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    title (str)
      Title of the WriteUp
    subtitle (str)
      Subtitle of the WriteUp
    slug (str)
      Unique path identifier used to create URLs
    message (Message)
      The message content & blobs of WriteUp
    type (WriteUpType)
      Type of WriteUp
    write_up_links (WriteUpLink)
      List of links embedded in WriteUp
    tag_ids (int)
      List of tags associated with WriteUp
    forum_id (int)
      Id of Forum to host WriteUp
    image (CroppedImageUpload)
      Information representing the cover and thumbnail images
    omit_message_in_response (bool)
      TODO: b/374113999 - remove this when we can map a ForumMessage without
      checking authz prematurely.
  """

  def __init__(self):
    self._title = ""
    self._subtitle = ""
    self._slug = ""
    self._message = None
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._write_up_links = []
    self._tag_ids = []
    self._forum_id = 0
    self._image = None
    self._omit_message_in_response = None
    self._freeze()

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
  def slug(self) -> str:
    """Unique path identifier used to create URLs"""
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
  def message(self) -> Optional['Message']:
    """The message content & blobs of WriteUp"""
    return self._message

  @message.setter
  def message(self, message: Optional['Message']):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message

  @property
  def type(self) -> 'WriteUpType':
    """Type of WriteUp"""
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
  def write_up_links(self) -> Optional[List[Optional['WriteUpLink']]]:
    """List of links embedded in WriteUp"""
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
  def tag_ids(self) -> Optional[List[int]]:
    """List of tags associated with WriteUp"""
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids

  @property
  def forum_id(self) -> int:
    """Id of Forum to host WriteUp"""
    return self._forum_id

  @forum_id.setter
  def forum_id(self, forum_id: int):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

  @property
  def image(self) -> Optional['CroppedImageUpload']:
    """Information representing the cover and thumbnail images"""
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
  def omit_message_in_response(self) -> bool:
    r"""
    TODO: b/374113999 - remove this when we can map a ForumMessage without
    checking authz prematurely.
    """
    return self._omit_message_in_response or False

  @omit_message_in_response.setter
  def omit_message_in_response(self, omit_message_in_response: Optional[bool]):
    if omit_message_in_response is None:
      del self.omit_message_in_response
      return
    if not isinstance(omit_message_in_response, bool):
      raise TypeError('omit_message_in_response must be of type bool')
    self._omit_message_in_response = omit_message_in_response


class DeleteWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    write_up_id (int)
      Id of the WriteUp to delete
  """

  def __init__(self):
    self._write_up_id = 0
    self._freeze()

  @property
  def write_up_id(self) -> int:
    """Id of the WriteUp to delete"""
    return self._write_up_id

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    self._write_up_id = write_up_id


class GetWriteUpBySlugRequest(KaggleObject):
  r"""
  Attributes:
    slug (str)
      Slug of the WriteUp
    user_name (str)
      Username of the user who created the WriteUp
    competition_name (str)
      Name of the Competition that the WriteUp lives under
    forum_name (str)
      Name of the forum that hosts the WriteUp (Currently only
      used for Blogs)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._slug = ""
    self._user_name = None
    self._competition_name = None
    self._forum_name = None
    self._read_mask = None
    self._freeze()

  @property
  def slug(self) -> str:
    """Slug of the WriteUp"""
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
  def user_name(self) -> str:
    """Username of the user who created the WriteUp"""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.competition_name
    del self.forum_name
    self._user_name = user_name

  @property
  def competition_name(self) -> str:
    """Name of the Competition that the WriteUp lives under"""
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    del self.user_name
    del self.forum_name
    self._competition_name = competition_name

  @property
  def forum_name(self) -> str:
    r"""
    Name of the forum that hosts the WriteUp (Currently only
    used for Blogs)
    """
    return self._forum_name or ""

  @forum_name.setter
  def forum_name(self, forum_name: str):
    if forum_name is None:
      del self.forum_name
      return
    if not isinstance(forum_name, str):
      raise TypeError('forum_name must be of type str')
    del self.user_name
    del self.competition_name
    self._forum_name = forum_name

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetWriteUpByTopicIdRequest(KaggleObject):
  r"""
  Attributes:
    forum_topic_id (int)
      Id of the forum topic associated with the WriteUp
    read_mask (FieldMask)
  """

  def __init__(self):
    self._forum_topic_id = 0
    self._read_mask = None
    self._freeze()

  @property
  def forum_topic_id(self) -> int:
    """Id of the forum topic associated with the WriteUp"""
    return self._forum_topic_id

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: int):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetWriteUpLinkMetadataRequest(KaggleObject):
  r"""
  Attributes:
    url (str)
  """

  def __init__(self):
    self._url = ""
    self._freeze()

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


class GetWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    write_up_id (int)
      ID of the WriteUp
    read_mask (FieldMask)
  """

  def __init__(self):
    self._write_up_id = 0
    self._read_mask = None
    self._freeze()

  @property
  def write_up_id(self) -> int:
    """ID of the WriteUp"""
    return self._write_up_id

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    self._write_up_id = write_up_id

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class TagIdList(KaggleObject):
  r"""
  Attributes:
    tag_ids (int)
      List of links embedded in the WriteUp
  """

  def __init__(self):
    self._tag_ids = []
    self._freeze()

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """List of links embedded in the WriteUp"""
    return self._tag_ids

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[List[int]]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, list):
      raise TypeError('tag_ids must be of type list')
    if not all([isinstance(t, int) for t in tag_ids]):
      raise TypeError('tag_ids must contain only items of type int')
    self._tag_ids = tag_ids


class ToggleBetweenCompetitionSolutionAndForumTopicRequest(KaggleObject):
  r"""
  Attributes:
    write_up_forum_topic_id (int)
  """

  def __init__(self):
    self._write_up_forum_topic_id = 0
    self._freeze()

  @property
  def write_up_forum_topic_id(self) -> int:
    return self._write_up_forum_topic_id

  @write_up_forum_topic_id.setter
  def write_up_forum_topic_id(self, write_up_forum_topic_id: int):
    if write_up_forum_topic_id is None:
      del self.write_up_forum_topic_id
      return
    if not isinstance(write_up_forum_topic_id, int):
      raise TypeError('write_up_forum_topic_id must be of type int')
    self._write_up_forum_topic_id = write_up_forum_topic_id


class ToggleBetweenCompetitionSolutionAndForumTopicResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
  """

  def __init__(self):
    self._message = ""
    self._freeze()

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


class UpdateWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    write_up_id (int)
      ID of the WriteUp
    title (str)
      Title of the WriteUp
    subtitle (str)
      Subtitle of the WriteUp
    message (Message)
      The message content & blobs of the WriteUp
    write_up_link_list (WriteUpLinkList)
      Wrapper to make WriteUpLinks nullable
    tag_id_list (TagIdList)
      Wrapper to make TagIds nullable
    content_state (ContentState)
      Represents the content state of the WriteUp
    slug (str)
      Slug of the WriteUp
    image (CroppedImageUpload)
      Information representing the cover and thumbnail images
    license_id (int)
      Id for the License that should apply to the WriteUp
    authors (str)
      List of authors for attribution
  """

  def __init__(self):
    self._write_up_id = 0
    self._title = None
    self._subtitle = None
    self._message = None
    self._write_up_link_list = None
    self._tag_id_list = None
    self._content_state = None
    self._slug = None
    self._image = None
    self._license_id = None
    self._authors = None
    self._freeze()

  @property
  def write_up_id(self) -> int:
    """ID of the WriteUp"""
    return self._write_up_id

  @write_up_id.setter
  def write_up_id(self, write_up_id: int):
    if write_up_id is None:
      del self.write_up_id
      return
    if not isinstance(write_up_id, int):
      raise TypeError('write_up_id must be of type int')
    self._write_up_id = write_up_id

  @property
  def title(self) -> str:
    """Title of the WriteUp"""
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def subtitle(self) -> str:
    """Subtitle of the WriteUp"""
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def message(self) -> Optional['Message']:
    """The message content & blobs of the WriteUp"""
    return self._message or None

  @message.setter
  def message(self, message: Optional[Optional['Message']]):
    if message is None:
      del self.message
      return
    if not isinstance(message, Message):
      raise TypeError('message must be of type Message')
    self._message = message

  @property
  def write_up_link_list(self) -> Optional['WriteUpLinkList']:
    """Wrapper to make WriteUpLinks nullable"""
    return self._write_up_link_list or None

  @write_up_link_list.setter
  def write_up_link_list(self, write_up_link_list: Optional[Optional['WriteUpLinkList']]):
    if write_up_link_list is None:
      del self.write_up_link_list
      return
    if not isinstance(write_up_link_list, WriteUpLinkList):
      raise TypeError('write_up_link_list must be of type WriteUpLinkList')
    self._write_up_link_list = write_up_link_list

  @property
  def tag_id_list(self) -> Optional['TagIdList']:
    """Wrapper to make TagIds nullable"""
    return self._tag_id_list or None

  @tag_id_list.setter
  def tag_id_list(self, tag_id_list: Optional[Optional['TagIdList']]):
    if tag_id_list is None:
      del self.tag_id_list
      return
    if not isinstance(tag_id_list, TagIdList):
      raise TypeError('tag_id_list must be of type TagIdList')
    self._tag_id_list = tag_id_list

  @property
  def content_state(self) -> 'ContentState':
    """Represents the content state of the WriteUp"""
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def slug(self) -> str:
    """Slug of the WriteUp"""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def image(self) -> Optional['CroppedImageUpload']:
    """Information representing the cover and thumbnail images"""
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
  def license_id(self) -> int:
    """Id for the License that should apply to the WriteUp"""
    return self._license_id or 0

  @license_id.setter
  def license_id(self, license_id: Optional[int]):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def authors(self) -> str:
    """List of authors for attribution"""
    return self._authors or ""

  @authors.setter
  def authors(self, authors: Optional[str]):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, str):
      raise TypeError('authors must be of type str')
    self._authors = authors


class WriteUpLinkList(KaggleObject):
  r"""
  Attributes:
    write_up_links (WriteUpLink)
      List of links embedded in the WriteUp
  """

  def __init__(self):
    self._write_up_links = []
    self._freeze()

  @property
  def write_up_links(self) -> Optional[List[Optional['WriteUpLink']]]:
    """List of links embedded in the WriteUp"""
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


BatchForceUpdateWriteUpContentStateRequest._fields = [
  FieldMetadata("writeUpIds", "write_up_ids", "_write_up_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("targetContentState", "target_content_state", "_target_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("targetPublishedHackathonLicenseId", "target_published_hackathon_license_id", "_target_published_hackathon_license_id", int, None, PredefinedSerializer(), optional=True),
]

BatchForceUpdateWriteUpContentStateResponse._fields = [
  FieldMetadata("updatedWriteUpIds", "updated_write_up_ids", "_updated_write_up_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("updatedWriteUpCount", "updated_write_up_count", "_updated_write_up_count", int, 0, PredefinedSerializer()),
  FieldMetadata("failedWriteUpIds", "failed_write_up_ids", "_failed_write_up_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("failedWriteUpCount", "failed_write_up_count", "_failed_write_up_count", int, 0, PredefinedSerializer()),
]

CopyWriteUpRequest._fields = [
  FieldMetadata("sourceWriteUpId", "source_write_up_id", "_source_write_up_id", int, 0, PredefinedSerializer()),
  FieldMetadata("targetForumId", "target_forum_id", "_target_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("targetTeamId", "target_team_id", "_target_team_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("targetCompetitionId", "target_competition_id", "_target_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("targetOwnerHostUserId", "target_owner_host_user_id", "_target_owner_host_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("targetOwnerJudgeUserId", "target_owner_judge_user_id", "_target_owner_judge_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("trackIdMapping", "track_id_mapping", "_track_id_mapping", int, {}, MapSerializer(PredefinedSerializer())),
]

CreateWriteUpRequest._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer()),
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("writeUpLinks", "write_up_links", "_write_up_links", WriteUpLink, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("image", "image", "_image", CroppedImageUpload, None, KaggleObjectSerializer()),
  FieldMetadata("omitMessageInResponse", "omit_message_in_response", "_omit_message_in_response", bool, None, PredefinedSerializer(), optional=True),
]

DeleteWriteUpRequest._fields = [
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, 0, PredefinedSerializer()),
]

GetWriteUpBySlugRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumName", "forum_name", "_forum_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetWriteUpByTopicIdRequest._fields = [
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetWriteUpLinkMetadataRequest._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

GetWriteUpRequest._fields = [
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

TagIdList._fields = [
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ToggleBetweenCompetitionSolutionAndForumTopicRequest._fields = [
  FieldMetadata("writeUpForumTopicId", "write_up_forum_topic_id", "_write_up_forum_topic_id", int, 0, PredefinedSerializer()),
]

ToggleBetweenCompetitionSolutionAndForumTopicResponse._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

UpdateWriteUpRequest._fields = [
  FieldMetadata("writeUpId", "write_up_id", "_write_up_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("message", "message", "_message", Message, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("writeUpLinkList", "write_up_link_list", "_write_up_link_list", WriteUpLinkList, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("tagIdList", "tag_id_list", "_tag_id_list", TagIdList, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("image", "image", "_image", CroppedImageUpload, None, KaggleObjectSerializer()),
  FieldMetadata("licenseId", "license_id", "_license_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authors", "authors", "_authors", str, None, PredefinedSerializer(), optional=True),
]

WriteUpLinkList._fields = [
  FieldMetadata("writeUpLinks", "write_up_links", "_write_up_links", WriteUpLink, [], ListSerializer(KaggleObjectSerializer())),
]

