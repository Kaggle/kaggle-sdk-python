from datetime import datetime
from kagglesdk.abuse.types.abuse_enums import PrivatedModerationStatus
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.datasets.types.auto_generated_source import KernelOutputKernelReference
from kagglesdk.datasets.types.dataset_enums import DatabundleDiffType
from kagglesdk.datasets.types.dataset_types import DatabundleInfo, DatasetCroissantInfo, DatasetTab, Owner
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.tags.types.tag_service import TagList
from kagglesdk.users.types.group_types import CollaboratorList
from typing import Optional

class DatasetBasics(KaggleObject):
  r"""
  This is all of the data needed to render the header of the dataset detail
  page

  Attributes:
    dataset_id (int)
    slug (str)
    title (str)
    removed (bool)
    private (bool)
    description (str)
    view_count (int)
    download_count (int)
    script_count (int)
    topic_count (int)
    owner (Owner)
    license (License)
    overview (str)
    can_edit (bool)
    creator_kernel (KernelOutputKernelReference)
    collaborator_list (CollaboratorList)
    cover_image_url (str)
    data (DatabundleInfo)
    vote_count (int)
    medal_url (str)
    download_url (str)
    last_update_time (datetime)
    dataset_version_number (int)
    already_voted_up (bool)
    in_flight (bool)
    creator_display_name (str)
    card_image_url (str)
    categories (TagList)
    bookmarked (bool)
    dataset_external_url (str)
    owner_twitter (str)
    collaborator (bool)
    forum_id (int)
    dataset_version_id (int)
    moderation_status (PrivatedModerationStatus)
    is_reported_banner_dismissed (bool)
    can_perform_admin_tasks (bool)
    dataset_hash_link (str)
    last_version_number (int)
    diff_type (DatabundleDiffType)
    show_admin_allowlist (bool)
    is_reported_modal_dismissed (bool)
    doi (str)
      TODO(http://b/274833571): Move toward a Dataset proto/handler with mask
      support, rather than this page-specific one
    can_delete (bool)
    content_state (ContentState)
    croissant_info (DatasetCroissantInfo)
    pending_suggestion_count (int)
    suggestions_enabled (bool)
    equivalent_external_dataset_url (str)
    has_external_benchmarks (bool)
    creator_user_id (int)
  """

  def __init__(self):
    self._dataset_id = 0
    self._slug = ""
    self._title = ""
    self._removed = False
    self._private = False
    self._description = ""
    self._view_count = 0
    self._download_count = 0
    self._script_count = 0
    self._topic_count = 0
    self._owner = None
    self._license = None
    self._overview = ""
    self._can_edit = False
    self._creator_kernel = None
    self._collaborator_list = None
    self._cover_image_url = ""
    self._data = None
    self._vote_count = 0
    self._medal_url = ""
    self._download_url = ""
    self._last_update_time = None
    self._dataset_version_number = 0
    self._already_voted_up = False
    self._in_flight = False
    self._creator_display_name = ""
    self._card_image_url = ""
    self._categories = None
    self._bookmarked = False
    self._dataset_external_url = ""
    self._owner_twitter = ""
    self._collaborator = False
    self._forum_id = 0
    self._dataset_version_id = 0
    self._moderation_status = PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED
    self._is_reported_banner_dismissed = False
    self._can_perform_admin_tasks = False
    self._dataset_hash_link = ""
    self._last_version_number = 0
    self._diff_type = DatabundleDiffType.REALTIME
    self._show_admin_allowlist = False
    self._is_reported_modal_dismissed = False
    self._doi = None
    self._can_delete = False
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._croissant_info = None
    self._pending_suggestion_count = 0
    self._suggestions_enabled = False
    self._equivalent_external_dataset_url = None
    self._has_external_benchmarks = None
    self._creator_user_id = 0
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

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
  def title(self) -> str:
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
  def removed(self) -> bool:
    return self._removed

  @removed.setter
  def removed(self, removed: bool):
    if removed is None:
      del self.removed
      return
    if not isinstance(removed, bool):
      raise TypeError('removed must be of type bool')
    self._removed = removed

  @property
  def private(self) -> bool:
    return self._private

  @private.setter
  def private(self, private: bool):
    if private is None:
      del self.private
      return
    if not isinstance(private, bool):
      raise TypeError('private must be of type bool')
    self._private = private

  @property
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def view_count(self) -> int:
    return self._view_count

  @view_count.setter
  def view_count(self, view_count: int):
    if view_count is None:
      del self.view_count
      return
    if not isinstance(view_count, int):
      raise TypeError('view_count must be of type int')
    self._view_count = view_count

  @property
  def download_count(self) -> int:
    return self._download_count

  @download_count.setter
  def download_count(self, download_count: int):
    if download_count is None:
      del self.download_count
      return
    if not isinstance(download_count, int):
      raise TypeError('download_count must be of type int')
    self._download_count = download_count

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
  def topic_count(self) -> int:
    return self._topic_count

  @topic_count.setter
  def topic_count(self, topic_count: int):
    if topic_count is None:
      del self.topic_count
      return
    if not isinstance(topic_count, int):
      raise TypeError('topic_count must be of type int')
    self._topic_count = topic_count

  @property
  def owner(self) -> Optional['Owner']:
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['Owner']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Owner):
      raise TypeError('owner must be of type Owner')
    self._owner = owner

  @property
  def license(self) -> Optional['License']:
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def overview(self) -> str:
    return self._overview

  @overview.setter
  def overview(self, overview: str):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def can_edit(self) -> bool:
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
  def creator_kernel(self) -> Optional['KernelOutputKernelReference']:
    return self._creator_kernel

  @creator_kernel.setter
  def creator_kernel(self, creator_kernel: Optional['KernelOutputKernelReference']):
    if creator_kernel is None:
      del self.creator_kernel
      return
    if not isinstance(creator_kernel, KernelOutputKernelReference):
      raise TypeError('creator_kernel must be of type KernelOutputKernelReference')
    self._creator_kernel = creator_kernel

  @property
  def collaborator_list(self) -> Optional['CollaboratorList']:
    return self._collaborator_list

  @collaborator_list.setter
  def collaborator_list(self, collaborator_list: Optional['CollaboratorList']):
    if collaborator_list is None:
      del self.collaborator_list
      return
    if not isinstance(collaborator_list, CollaboratorList):
      raise TypeError('collaborator_list must be of type CollaboratorList')
    self._collaborator_list = collaborator_list

  @property
  def cover_image_url(self) -> str:
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
  def data(self) -> Optional['DatabundleInfo']:
    return self._data

  @data.setter
  def data(self, data: Optional['DatabundleInfo']):
    if data is None:
      del self.data
      return
    if not isinstance(data, DatabundleInfo):
      raise TypeError('data must be of type DatabundleInfo')
    self._data = data

  @property
  def vote_count(self) -> int:
    return self._vote_count

  @vote_count.setter
  def vote_count(self, vote_count: int):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def medal_url(self) -> str:
    return self._medal_url

  @medal_url.setter
  def medal_url(self, medal_url: str):
    if medal_url is None:
      del self.medal_url
      return
    if not isinstance(medal_url, str):
      raise TypeError('medal_url must be of type str')
    self._medal_url = medal_url

  @property
  def download_url(self) -> str:
    return self._download_url

  @download_url.setter
  def download_url(self, download_url: str):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url

  @property
  def last_update_time(self) -> datetime:
    return self._last_update_time

  @last_update_time.setter
  def last_update_time(self, last_update_time: datetime):
    if last_update_time is None:
      del self.last_update_time
      return
    if not isinstance(last_update_time, datetime):
      raise TypeError('last_update_time must be of type datetime')
    self._last_update_time = last_update_time

  @property
  def dataset_version_number(self) -> int:
    return self._dataset_version_number

  @dataset_version_number.setter
  def dataset_version_number(self, dataset_version_number: int):
    if dataset_version_number is None:
      del self.dataset_version_number
      return
    if not isinstance(dataset_version_number, int):
      raise TypeError('dataset_version_number must be of type int')
    self._dataset_version_number = dataset_version_number

  @property
  def already_voted_up(self) -> bool:
    return self._already_voted_up

  @already_voted_up.setter
  def already_voted_up(self, already_voted_up: bool):
    if already_voted_up is None:
      del self.already_voted_up
      return
    if not isinstance(already_voted_up, bool):
      raise TypeError('already_voted_up must be of type bool')
    self._already_voted_up = already_voted_up

  @property
  def in_flight(self) -> bool:
    return self._in_flight

  @in_flight.setter
  def in_flight(self, in_flight: bool):
    if in_flight is None:
      del self.in_flight
      return
    if not isinstance(in_flight, bool):
      raise TypeError('in_flight must be of type bool')
    self._in_flight = in_flight

  @property
  def creator_display_name(self) -> str:
    return self._creator_display_name

  @creator_display_name.setter
  def creator_display_name(self, creator_display_name: str):
    if creator_display_name is None:
      del self.creator_display_name
      return
    if not isinstance(creator_display_name, str):
      raise TypeError('creator_display_name must be of type str')
    self._creator_display_name = creator_display_name

  @property
  def card_image_url(self) -> str:
    return self._card_image_url

  @card_image_url.setter
  def card_image_url(self, card_image_url: str):
    if card_image_url is None:
      del self.card_image_url
      return
    if not isinstance(card_image_url, str):
      raise TypeError('card_image_url must be of type str')
    self._card_image_url = card_image_url

  @property
  def categories(self) -> Optional['TagList']:
    return self._categories

  @categories.setter
  def categories(self, categories: Optional['TagList']):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, TagList):
      raise TypeError('categories must be of type TagList')
    self._categories = categories

  @property
  def bookmarked(self) -> bool:
    return self._bookmarked

  @bookmarked.setter
  def bookmarked(self, bookmarked: bool):
    if bookmarked is None:
      del self.bookmarked
      return
    if not isinstance(bookmarked, bool):
      raise TypeError('bookmarked must be of type bool')
    self._bookmarked = bookmarked

  @property
  def dataset_external_url(self) -> str:
    return self._dataset_external_url

  @dataset_external_url.setter
  def dataset_external_url(self, dataset_external_url: str):
    if dataset_external_url is None:
      del self.dataset_external_url
      return
    if not isinstance(dataset_external_url, str):
      raise TypeError('dataset_external_url must be of type str')
    self._dataset_external_url = dataset_external_url

  @property
  def owner_twitter(self) -> str:
    return self._owner_twitter

  @owner_twitter.setter
  def owner_twitter(self, owner_twitter: str):
    if owner_twitter is None:
      del self.owner_twitter
      return
    if not isinstance(owner_twitter, str):
      raise TypeError('owner_twitter must be of type str')
    self._owner_twitter = owner_twitter

  @property
  def collaborator(self) -> bool:
    return self._collaborator

  @collaborator.setter
  def collaborator(self, collaborator: bool):
    if collaborator is None:
      del self.collaborator
      return
    if not isinstance(collaborator, bool):
      raise TypeError('collaborator must be of type bool')
    self._collaborator = collaborator

  @property
  def forum_id(self) -> int:
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
  def dataset_version_id(self) -> int:
    return self._dataset_version_id

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id

  @property
  def moderation_status(self) -> 'PrivatedModerationStatus':
    return self._moderation_status

  @moderation_status.setter
  def moderation_status(self, moderation_status: 'PrivatedModerationStatus'):
    if moderation_status is None:
      del self.moderation_status
      return
    if not isinstance(moderation_status, PrivatedModerationStatus):
      raise TypeError('moderation_status must be of type PrivatedModerationStatus')
    self._moderation_status = moderation_status

  @property
  def is_reported_banner_dismissed(self) -> bool:
    return self._is_reported_banner_dismissed

  @is_reported_banner_dismissed.setter
  def is_reported_banner_dismissed(self, is_reported_banner_dismissed: bool):
    if is_reported_banner_dismissed is None:
      del self.is_reported_banner_dismissed
      return
    if not isinstance(is_reported_banner_dismissed, bool):
      raise TypeError('is_reported_banner_dismissed must be of type bool')
    self._is_reported_banner_dismissed = is_reported_banner_dismissed

  @property
  def can_perform_admin_tasks(self) -> bool:
    return self._can_perform_admin_tasks

  @can_perform_admin_tasks.setter
  def can_perform_admin_tasks(self, can_perform_admin_tasks: bool):
    if can_perform_admin_tasks is None:
      del self.can_perform_admin_tasks
      return
    if not isinstance(can_perform_admin_tasks, bool):
      raise TypeError('can_perform_admin_tasks must be of type bool')
    self._can_perform_admin_tasks = can_perform_admin_tasks

  @property
  def dataset_hash_link(self) -> str:
    return self._dataset_hash_link

  @dataset_hash_link.setter
  def dataset_hash_link(self, dataset_hash_link: str):
    if dataset_hash_link is None:
      del self.dataset_hash_link
      return
    if not isinstance(dataset_hash_link, str):
      raise TypeError('dataset_hash_link must be of type str')
    self._dataset_hash_link = dataset_hash_link

  @property
  def last_version_number(self) -> int:
    return self._last_version_number

  @last_version_number.setter
  def last_version_number(self, last_version_number: int):
    if last_version_number is None:
      del self.last_version_number
      return
    if not isinstance(last_version_number, int):
      raise TypeError('last_version_number must be of type int')
    self._last_version_number = last_version_number

  @property
  def diff_type(self) -> 'DatabundleDiffType':
    return self._diff_type

  @diff_type.setter
  def diff_type(self, diff_type: 'DatabundleDiffType'):
    if diff_type is None:
      del self.diff_type
      return
    if not isinstance(diff_type, DatabundleDiffType):
      raise TypeError('diff_type must be of type DatabundleDiffType')
    self._diff_type = diff_type

  @property
  def show_admin_allowlist(self) -> bool:
    return self._show_admin_allowlist

  @show_admin_allowlist.setter
  def show_admin_allowlist(self, show_admin_allowlist: bool):
    if show_admin_allowlist is None:
      del self.show_admin_allowlist
      return
    if not isinstance(show_admin_allowlist, bool):
      raise TypeError('show_admin_allowlist must be of type bool')
    self._show_admin_allowlist = show_admin_allowlist

  @property
  def is_reported_modal_dismissed(self) -> bool:
    return self._is_reported_modal_dismissed

  @is_reported_modal_dismissed.setter
  def is_reported_modal_dismissed(self, is_reported_modal_dismissed: bool):
    if is_reported_modal_dismissed is None:
      del self.is_reported_modal_dismissed
      return
    if not isinstance(is_reported_modal_dismissed, bool):
      raise TypeError('is_reported_modal_dismissed must be of type bool')
    self._is_reported_modal_dismissed = is_reported_modal_dismissed

  @property
  def doi(self) -> str:
    r"""
    TODO(http://b/274833571): Move toward a Dataset proto/handler with mask
    support, rather than this page-specific one
    """
    return self._doi or ""

  @doi.setter
  def doi(self, doi: Optional[str]):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi

  @property
  def can_delete(self) -> bool:
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
  def croissant_info(self) -> Optional['DatasetCroissantInfo']:
    return self._croissant_info

  @croissant_info.setter
  def croissant_info(self, croissant_info: Optional['DatasetCroissantInfo']):
    if croissant_info is None:
      del self.croissant_info
      return
    if not isinstance(croissant_info, DatasetCroissantInfo):
      raise TypeError('croissant_info must be of type DatasetCroissantInfo')
    self._croissant_info = croissant_info

  @property
  def pending_suggestion_count(self) -> int:
    return self._pending_suggestion_count

  @pending_suggestion_count.setter
  def pending_suggestion_count(self, pending_suggestion_count: int):
    if pending_suggestion_count is None:
      del self.pending_suggestion_count
      return
    if not isinstance(pending_suggestion_count, int):
      raise TypeError('pending_suggestion_count must be of type int')
    self._pending_suggestion_count = pending_suggestion_count

  @property
  def suggestions_enabled(self) -> bool:
    return self._suggestions_enabled

  @suggestions_enabled.setter
  def suggestions_enabled(self, suggestions_enabled: bool):
    if suggestions_enabled is None:
      del self.suggestions_enabled
      return
    if not isinstance(suggestions_enabled, bool):
      raise TypeError('suggestions_enabled must be of type bool')
    self._suggestions_enabled = suggestions_enabled

  @property
  def equivalent_external_dataset_url(self) -> str:
    return self._equivalent_external_dataset_url or ""

  @equivalent_external_dataset_url.setter
  def equivalent_external_dataset_url(self, equivalent_external_dataset_url: Optional[str]):
    if equivalent_external_dataset_url is None:
      del self.equivalent_external_dataset_url
      return
    if not isinstance(equivalent_external_dataset_url, str):
      raise TypeError('equivalent_external_dataset_url must be of type str')
    self._equivalent_external_dataset_url = equivalent_external_dataset_url

  @property
  def has_external_benchmarks(self) -> bool:
    return self._has_external_benchmarks or False

  @has_external_benchmarks.setter
  def has_external_benchmarks(self, has_external_benchmarks: Optional[bool]):
    if has_external_benchmarks is None:
      del self.has_external_benchmarks
      return
    if not isinstance(has_external_benchmarks, bool):
      raise TypeError('has_external_benchmarks must be of type bool')
    self._has_external_benchmarks = has_external_benchmarks

  @property
  def creator_user_id(self) -> int:
    return self._creator_user_id

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: int):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id


class DatasetMaterialDto(KaggleObject):
  r"""
  Attributes:
    basics (DatasetBasics)
    current_tab (DatasetTab)
    topic_id (int)
    is_new_topic (bool)
    accessed_via_hash_link (bool)
  """

  def __init__(self):
    self._basics = None
    self._current_tab = DatasetTab.DATA
    self._topic_id = None
    self._is_new_topic = False
    self._accessed_via_hash_link = None
    self._freeze()

  @property
  def basics(self) -> Optional['DatasetBasics']:
    return self._basics

  @basics.setter
  def basics(self, basics: Optional['DatasetBasics']):
    if basics is None:
      del self.basics
      return
    if not isinstance(basics, DatasetBasics):
      raise TypeError('basics must be of type DatasetBasics')
    self._basics = basics

  @property
  def current_tab(self) -> 'DatasetTab':
    return self._current_tab

  @current_tab.setter
  def current_tab(self, current_tab: 'DatasetTab'):
    if current_tab is None:
      del self.current_tab
      return
    if not isinstance(current_tab, DatasetTab):
      raise TypeError('current_tab must be of type DatasetTab')
    self._current_tab = current_tab

  @property
  def topic_id(self) -> int:
    return self._topic_id or 0

  @topic_id.setter
  def topic_id(self, topic_id: Optional[int]):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def is_new_topic(self) -> bool:
    return self._is_new_topic

  @is_new_topic.setter
  def is_new_topic(self, is_new_topic: bool):
    if is_new_topic is None:
      del self.is_new_topic
      return
    if not isinstance(is_new_topic, bool):
      raise TypeError('is_new_topic must be of type bool')
    self._is_new_topic = is_new_topic

  @property
  def accessed_via_hash_link(self) -> bool:
    return self._accessed_via_hash_link or False

  @accessed_via_hash_link.setter
  def accessed_via_hash_link(self, accessed_via_hash_link: Optional[bool]):
    if accessed_via_hash_link is None:
      del self.accessed_via_hash_link
      return
    if not isinstance(accessed_via_hash_link, bool):
      raise TypeError('accessed_via_hash_link must be of type bool')
    self._accessed_via_hash_link = accessed_via_hash_link


DatasetBasics._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("removed", "removed", "_removed", bool, False, PredefinedSerializer()),
  FieldMetadata("private", "private", "_private", bool, False, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("viewCount", "view_count", "_view_count", int, 0, PredefinedSerializer()),
  FieldMetadata("downloadCount", "download_count", "_download_count", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptCount", "script_count", "_script_count", int, 0, PredefinedSerializer()),
  FieldMetadata("topicCount", "topic_count", "_topic_count", int, 0, PredefinedSerializer()),
  FieldMetadata("owner", "owner", "_owner", Owner, None, KaggleObjectSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("canEdit", "can_edit", "_can_edit", bool, False, PredefinedSerializer()),
  FieldMetadata("creatorKernel", "creator_kernel", "_creator_kernel", KernelOutputKernelReference, None, KaggleObjectSerializer()),
  FieldMetadata("collaboratorList", "collaborator_list", "_collaborator_list", CollaboratorList, None, KaggleObjectSerializer()),
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("data", "data", "_data", DatabundleInfo, None, KaggleObjectSerializer()),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("medalUrl", "medal_url", "_medal_url", str, "", PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, "", PredefinedSerializer()),
  FieldMetadata("lastUpdateTime", "last_update_time", "_last_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("datasetVersionNumber", "dataset_version_number", "_dataset_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("alreadyVotedUp", "already_voted_up", "_already_voted_up", bool, False, PredefinedSerializer()),
  FieldMetadata("inFlight", "in_flight", "_in_flight", bool, False, PredefinedSerializer()),
  FieldMetadata("creatorDisplayName", "creator_display_name", "_creator_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("cardImageUrl", "card_image_url", "_card_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("categories", "categories", "_categories", TagList, None, KaggleObjectSerializer()),
  FieldMetadata("bookmarked", "bookmarked", "_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("datasetExternalUrl", "dataset_external_url", "_dataset_external_url", str, "", PredefinedSerializer()),
  FieldMetadata("ownerTwitter", "owner_twitter", "_owner_twitter", str, "", PredefinedSerializer()),
  FieldMetadata("collaborator", "collaborator", "_collaborator", bool, False, PredefinedSerializer()),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("moderationStatus", "moderation_status", "_moderation_status", PrivatedModerationStatus, PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isReportedBannerDismissed", "is_reported_banner_dismissed", "_is_reported_banner_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("canPerformAdminTasks", "can_perform_admin_tasks", "_can_perform_admin_tasks", bool, False, PredefinedSerializer()),
  FieldMetadata("datasetHashLink", "dataset_hash_link", "_dataset_hash_link", str, "", PredefinedSerializer()),
  FieldMetadata("lastVersionNumber", "last_version_number", "_last_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("diffType", "diff_type", "_diff_type", DatabundleDiffType, DatabundleDiffType.REALTIME, EnumSerializer()),
  FieldMetadata("showAdminAllowlist", "show_admin_allowlist", "_show_admin_allowlist", bool, False, PredefinedSerializer()),
  FieldMetadata("isReportedModalDismissed", "is_reported_modal_dismissed", "_is_reported_modal_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canDelete", "can_delete", "_can_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("croissantInfo", "croissant_info", "_croissant_info", DatasetCroissantInfo, None, KaggleObjectSerializer()),
  FieldMetadata("pendingSuggestionCount", "pending_suggestion_count", "_pending_suggestion_count", int, 0, PredefinedSerializer()),
  FieldMetadata("suggestionsEnabled", "suggestions_enabled", "_suggestions_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("equivalentExternalDatasetUrl", "equivalent_external_dataset_url", "_equivalent_external_dataset_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasExternalBenchmarks", "has_external_benchmarks", "_has_external_benchmarks", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, 0, PredefinedSerializer()),
]

DatasetMaterialDto._fields = [
  FieldMetadata("basics", "basics", "_basics", DatasetBasics, None, KaggleObjectSerializer()),
  FieldMetadata("currentTab", "current_tab", "_current_tab", DatasetTab, DatasetTab.DATA, EnumSerializer()),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isNewTopic", "is_new_topic", "_is_new_topic", bool, False, PredefinedSerializer()),
  FieldMetadata("accessedViaHashLink", "accessed_via_hash_link", "_accessed_via_hash_link", bool, None, PredefinedSerializer(), optional=True),
]

