from datetime import datetime
import enum
from kagglesdk.benchmarks.types.search_benchmark_tasks import SearchBenchmarkTasksDocument
from kagglesdk.benchmarks.types.search_benchmarks import SearchBenchmarksDocument
from kagglesdk.competitions.types.search_competitions import SearchCompetitionsDocument, SearchCompetitionsFilters, SearchCompetitionsOrderBy
from kagglesdk.datasets.types.search_datasets import SearchDatasetsDocument, SearchDatasetsFilters, SearchDatasetsOrderBy
from kagglesdk.discussions.types.search_discussions import SearchDiscussionsDocument, SearchDiscussionsFilters, SearchDiscussionsOrderBy
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.search_kernels import SearchKernelsDocument, SearchKernelsFilters, SearchKernelsOrderBy
from kagglesdk.models.types.search_models import SearchModelsDocument, SearchModelsFilters, SearchModelsOrderBy
from kagglesdk.search.types.search_enums import DocumentType, ListSearchContentOrderBy, OwnerType, PrivacyFilter
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.search_users import SearchUsersDocument, SearchUsersFilters, SearchUsersOrderBy
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class ListType(enum.Enum):
  LIST_TYPE_UNSPECIFIED = 0
  LIST_TYPE_LANDING_CARDS = 1
  LIST_TYPE_LANDING_LIST = 2
  LIST_TYPE_USER_PROFILE = 3
  LIST_TYPE_YOUR_WORK = 4
  LIST_TYPE_COLLECTIONS = 5
  LIST_TYPE_BOOKMARKS = 6
  LIST_TYPE_ORGANIZATION_PROFILE = 7
  LIST_TYPE_COMPETITION_COLLECTIONS = 8
  r"""
  Same as LIST_TYPE_COLLECTIONS, but omits some indexes (for performance)
  that aren't used
  """
  LIST_TYPE_ACTIVE_COMPETITIONS = 9
  r"""
  A special purpose listing type for showing a user's active & recently
  submitted-to competitions
  """
  LIST_TYPE_RANKINGS = 10
  """Listing type for the rankings page, expected to list users."""

class Vote(enum.Enum):
  VOTE_UNSPECIFIED = 0
  VOTE_UP = 1
  VOTE_DOWN = 2

class EnrichedInfo(KaggleObject):
  r"""
  Attributes:
    url (str)
      The URL of the document
    current_user_can_edit (bool)
      Whether the current user has permissions to edit the document
    current_user_vote (Vote)
      The vote made by the current user (if applicable)
    collaborators (UserAvatar)
      The avatar of the collaborators of the document
    current_user_can_delete (bool)
      Whether the current user has permissions to delete the document
    current_user_can_pin (bool)
      Whether the current user has permissions to pin the document
  """

  def __init__(self):
    self._url = ""
    self._current_user_can_edit = False
    self._current_user_vote = None
    self._collaborators = []
    self._current_user_can_delete = False
    self._current_user_can_pin = False
    self._freeze()

  @property
  def url(self) -> str:
    """The URL of the document"""
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
  def current_user_can_edit(self) -> bool:
    """Whether the current user has permissions to edit the document"""
    return self._current_user_can_edit

  @current_user_can_edit.setter
  def current_user_can_edit(self, current_user_can_edit: bool):
    if current_user_can_edit is None:
      del self.current_user_can_edit
      return
    if not isinstance(current_user_can_edit, bool):
      raise TypeError('current_user_can_edit must be of type bool')
    self._current_user_can_edit = current_user_can_edit

  @property
  def current_user_vote(self) -> 'Vote':
    """The vote made by the current user (if applicable)"""
    return self._current_user_vote or Vote.VOTE_UNSPECIFIED

  @current_user_vote.setter
  def current_user_vote(self, current_user_vote: Optional['Vote']):
    if current_user_vote is None:
      del self.current_user_vote
      return
    if not isinstance(current_user_vote, Vote):
      raise TypeError('current_user_vote must be of type Vote')
    self._current_user_vote = current_user_vote

  @property
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    """The avatar of the collaborators of the document"""
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
  def current_user_can_delete(self) -> bool:
    """Whether the current user has permissions to delete the document"""
    return self._current_user_can_delete

  @current_user_can_delete.setter
  def current_user_can_delete(self, current_user_can_delete: bool):
    if current_user_can_delete is None:
      del self.current_user_can_delete
      return
    if not isinstance(current_user_can_delete, bool):
      raise TypeError('current_user_can_delete must be of type bool')
    self._current_user_can_delete = current_user_can_delete

  @property
  def current_user_can_pin(self) -> bool:
    """Whether the current user has permissions to pin the document"""
    return self._current_user_can_pin

  @current_user_can_pin.setter
  def current_user_can_pin(self, current_user_can_pin: bool):
    if current_user_can_pin is None:
      del self.current_user_can_pin
      return
    if not isinstance(current_user_can_pin, bool):
      raise TypeError('current_user_can_pin must be of type bool')
    self._current_user_can_pin = current_user_can_pin


class ListSearchContentAggregation(KaggleObject):
  r"""
  Attributes:
    document_type (DocumentType)
      The document type to aggregate on
    competition_id (int)
      The document type to aggregate on
    count (int)
      The count of documents of the given type
  """

  def __init__(self):
    self._document_type = None
    self._competition_id = None
    self._count = 0
    self._freeze()

  @property
  def document_type(self) -> 'DocumentType':
    """The document type to aggregate on"""
    return self._document_type or DocumentType.DOCUMENT_TYPE_UNSPECIFIED

  @document_type.setter
  def document_type(self, document_type: Optional['DocumentType']):
    if document_type is None:
      del self.document_type
      return
    if not isinstance(document_type, DocumentType):
      raise TypeError('document_type must be of type DocumentType')
    self._document_type = document_type

  @property
  def competition_id(self) -> int:
    """The document type to aggregate on"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def count(self) -> int:
    """The count of documents of the given type"""
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class ListSearchContentCountGroupings(KaggleObject):
  r"""
  Attributes:
    by_document_type (bool)
      Whether to group counts by document type
    by_competition_id (bool)
      Whether to group counts by competition ID
  """

  def __init__(self):
    self._by_document_type = None
    self._by_competition_id = None
    self._freeze()

  @property
  def by_document_type(self) -> bool:
    """Whether to group counts by document type"""
    return self._by_document_type or False

  @by_document_type.setter
  def by_document_type(self, by_document_type: Optional[bool]):
    if by_document_type is None:
      del self.by_document_type
      return
    if not isinstance(by_document_type, bool):
      raise TypeError('by_document_type must be of type bool')
    self._by_document_type = by_document_type

  @property
  def by_competition_id(self) -> bool:
    """Whether to group counts by competition ID"""
    return self._by_competition_id or False

  @by_competition_id.setter
  def by_competition_id(self, by_competition_id: Optional[bool]):
    if by_competition_id is None:
      del self.by_competition_id
      return
    if not isinstance(by_competition_id, bool):
      raise TypeError('by_competition_id must be of type bool')
    self._by_competition_id = by_competition_id


class ListSearchContentDocument(KaggleObject):
  r"""
  Attributes:
    id (int)
      The DB ID (i.e. the PK from the table) of the document
    document_id (str)
      The Elastic string document ID (e.g. 'dataset-1234')
    document_type (DocumentType)
      The type of content of the document
    title (str)
      The canonical title of the document
    subtitle (str)
      The canonical subtitle of the document
    image_url (str)
      The thumbnail URL of the document
    slug (str)
      The slug of the document (which may be close to the url)
    create_time (datetime)
      The canonical creation time of the document; May mean different things
      between content types
    update_time (datetime)
      The canonical update time of the document; May be different between
      content types
    is_private (bool)
      Whether the content is marked as private
    votes (int)
      The total votes (or score, if downvotes are supported) for the document
    medal (Medal)
      The medal the document has received (user-specific for Competitions)
    is_current_user_bookmarked (bool)
      Whether the current user has the document bookmarked
    total_comments (int)
      The total comments a document has received
    owner_user (UserAvatar)
    owner_organization (OrganizationCard)
    tags (Tag)
      All tags applied to the document
    enriched_info (EnrichedInfo)
      Additional canonical info to be enriched by the document type's domain
    competition_document (SearchCompetitionsDocument)
    dataset_document (SearchDatasetsDocument)
    discussion_document (SearchDiscussionsDocument)
    kernel_document (SearchKernelsDocument)
    model_document (SearchModelsDocument)
    user_document (SearchUsersDocument)
    benchmark_task_document (SearchBenchmarkTasksDocument)
    benchmark_document (SearchBenchmarksDocument)
  """

  def __init__(self):
    self._id = 0
    self._document_id = ""
    self._document_type = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._title = ""
    self._subtitle = None
    self._image_url = ""
    self._slug = None
    self._create_time = None
    self._update_time = None
    self._is_private = None
    self._votes = None
    self._medal = None
    self._is_current_user_bookmarked = False
    self._total_comments = None
    self._owner_user = None
    self._owner_organization = None
    self._tags = []
    self._enriched_info = None
    self._competition_document = None
    self._dataset_document = None
    self._discussion_document = None
    self._kernel_document = None
    self._model_document = None
    self._user_document = None
    self._benchmark_task_document = None
    self._benchmark_document = None
    self._freeze()

  @property
  def id(self) -> int:
    """The DB ID (i.e. the PK from the table) of the document"""
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
  def document_id(self) -> str:
    """The Elastic string document ID (e.g. 'dataset-1234')"""
    return self._document_id

  @document_id.setter
  def document_id(self, document_id: str):
    if document_id is None:
      del self.document_id
      return
    if not isinstance(document_id, str):
      raise TypeError('document_id must be of type str')
    self._document_id = document_id

  @property
  def document_type(self) -> 'DocumentType':
    """The type of content of the document"""
    return self._document_type

  @document_type.setter
  def document_type(self, document_type: 'DocumentType'):
    if document_type is None:
      del self.document_type
      return
    if not isinstance(document_type, DocumentType):
      raise TypeError('document_type must be of type DocumentType')
    self._document_type = document_type

  @property
  def title(self) -> str:
    """The canonical title of the document"""
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
    """The canonical subtitle of the document"""
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
  def image_url(self) -> str:
    """The thumbnail URL of the document"""
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def slug(self) -> str:
    """The slug of the document (which may be close to the url)"""
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
  def create_time(self) -> datetime:
    r"""
    The canonical creation time of the document; May mean different things
    between content types
    """
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
    r"""
    The canonical update time of the document; May be different between
    content types
    """
    return self._update_time or None

  @update_time.setter
  def update_time(self, update_time: Optional[datetime]):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def is_private(self) -> bool:
    """Whether the content is marked as private"""
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
  def votes(self) -> int:
    """The total votes (or score, if downvotes are supported) for the document"""
    return self._votes or 0

  @votes.setter
  def votes(self, votes: Optional[int]):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, int):
      raise TypeError('votes must be of type int')
    self._votes = votes

  @property
  def medal(self) -> 'Medal':
    """The medal the document has received (user-specific for Competitions)"""
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
  def is_current_user_bookmarked(self) -> bool:
    """Whether the current user has the document bookmarked"""
    return self._is_current_user_bookmarked

  @is_current_user_bookmarked.setter
  def is_current_user_bookmarked(self, is_current_user_bookmarked: bool):
    if is_current_user_bookmarked is None:
      del self.is_current_user_bookmarked
      return
    if not isinstance(is_current_user_bookmarked, bool):
      raise TypeError('is_current_user_bookmarked must be of type bool')
    self._is_current_user_bookmarked = is_current_user_bookmarked

  @property
  def total_comments(self) -> int:
    """The total comments a document has received"""
    return self._total_comments or 0

  @total_comments.setter
  def total_comments(self, total_comments: Optional[int]):
    if total_comments is None:
      del self.total_comments
      return
    if not isinstance(total_comments, int):
      raise TypeError('total_comments must be of type int')
    self._total_comments = total_comments

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
  def tags(self) -> Optional[List[Optional['Tag']]]:
    """All tags applied to the document"""
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
  def enriched_info(self) -> Optional['EnrichedInfo']:
    """Additional canonical info to be enriched by the document type's domain"""
    return self._enriched_info

  @enriched_info.setter
  def enriched_info(self, enriched_info: Optional['EnrichedInfo']):
    if enriched_info is None:
      del self.enriched_info
      return
    if not isinstance(enriched_info, EnrichedInfo):
      raise TypeError('enriched_info must be of type EnrichedInfo')
    self._enriched_info = enriched_info

  @property
  def competition_document(self) -> Optional['SearchCompetitionsDocument']:
    return self._competition_document or None

  @competition_document.setter
  def competition_document(self, competition_document: Optional['SearchCompetitionsDocument']):
    if competition_document is None:
      del self.competition_document
      return
    if not isinstance(competition_document, SearchCompetitionsDocument):
      raise TypeError('competition_document must be of type SearchCompetitionsDocument')
    del self.dataset_document
    del self.discussion_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._competition_document = competition_document

  @property
  def dataset_document(self) -> Optional['SearchDatasetsDocument']:
    return self._dataset_document or None

  @dataset_document.setter
  def dataset_document(self, dataset_document: Optional['SearchDatasetsDocument']):
    if dataset_document is None:
      del self.dataset_document
      return
    if not isinstance(dataset_document, SearchDatasetsDocument):
      raise TypeError('dataset_document must be of type SearchDatasetsDocument')
    del self.competition_document
    del self.discussion_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._dataset_document = dataset_document

  @property
  def discussion_document(self) -> Optional['SearchDiscussionsDocument']:
    return self._discussion_document or None

  @discussion_document.setter
  def discussion_document(self, discussion_document: Optional['SearchDiscussionsDocument']):
    if discussion_document is None:
      del self.discussion_document
      return
    if not isinstance(discussion_document, SearchDiscussionsDocument):
      raise TypeError('discussion_document must be of type SearchDiscussionsDocument')
    del self.competition_document
    del self.dataset_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._discussion_document = discussion_document

  @property
  def kernel_document(self) -> Optional['SearchKernelsDocument']:
    return self._kernel_document or None

  @kernel_document.setter
  def kernel_document(self, kernel_document: Optional['SearchKernelsDocument']):
    if kernel_document is None:
      del self.kernel_document
      return
    if not isinstance(kernel_document, SearchKernelsDocument):
      raise TypeError('kernel_document must be of type SearchKernelsDocument')
    del self.competition_document
    del self.dataset_document
    del self.discussion_document
    del self.model_document
    del self.user_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._kernel_document = kernel_document

  @property
  def model_document(self) -> Optional['SearchModelsDocument']:
    return self._model_document or None

  @model_document.setter
  def model_document(self, model_document: Optional['SearchModelsDocument']):
    if model_document is None:
      del self.model_document
      return
    if not isinstance(model_document, SearchModelsDocument):
      raise TypeError('model_document must be of type SearchModelsDocument')
    del self.competition_document
    del self.dataset_document
    del self.discussion_document
    del self.kernel_document
    del self.user_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._model_document = model_document

  @property
  def user_document(self) -> Optional['SearchUsersDocument']:
    return self._user_document or None

  @user_document.setter
  def user_document(self, user_document: Optional['SearchUsersDocument']):
    if user_document is None:
      del self.user_document
      return
    if not isinstance(user_document, SearchUsersDocument):
      raise TypeError('user_document must be of type SearchUsersDocument')
    del self.competition_document
    del self.dataset_document
    del self.discussion_document
    del self.kernel_document
    del self.model_document
    del self.benchmark_task_document
    del self.benchmark_document
    self._user_document = user_document

  @property
  def benchmark_task_document(self) -> Optional['SearchBenchmarkTasksDocument']:
    return self._benchmark_task_document or None

  @benchmark_task_document.setter
  def benchmark_task_document(self, benchmark_task_document: Optional['SearchBenchmarkTasksDocument']):
    if benchmark_task_document is None:
      del self.benchmark_task_document
      return
    if not isinstance(benchmark_task_document, SearchBenchmarkTasksDocument):
      raise TypeError('benchmark_task_document must be of type SearchBenchmarkTasksDocument')
    del self.competition_document
    del self.dataset_document
    del self.discussion_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    del self.benchmark_document
    self._benchmark_task_document = benchmark_task_document

  @property
  def benchmark_document(self) -> Optional['SearchBenchmarksDocument']:
    return self._benchmark_document or None

  @benchmark_document.setter
  def benchmark_document(self, benchmark_document: Optional['SearchBenchmarksDocument']):
    if benchmark_document is None:
      del self.benchmark_document
      return
    if not isinstance(benchmark_document, SearchBenchmarksDocument):
      raise TypeError('benchmark_document must be of type SearchBenchmarksDocument')
    del self.competition_document
    del self.dataset_document
    del self.discussion_document
    del self.kernel_document
    del self.model_document
    del self.user_document
    del self.benchmark_task_document
    self._benchmark_document = benchmark_document


class ListSearchContentFilters(KaggleObject):
  r"""
  Attributes:
    query (str)
      The free-text query the user entered to filter results
    list_type (ListType)
      The type of list being requested
    privacy (PrivacyFilter)
      The privacy filter to apply
    owner_type (OwnerType)
      The owner type filter to apply
    document_types (DocumentType)
      The document type filter to apply
    tag_ids (int)
      The tags to use to filter the documents
    collection_id (int)
      The collection to use to filter the documents
    competition_ids (int)
      The Competitions to use to filter the documents
    only_counts (bool)
      Whether to only return counts by document type (vs. full document results)
    owner_user_id (int)
      The owner user to filter the documents
    owner_organization_id (int)
      The owner organization to filter the documents
    count_groupings (ListSearchContentCountGroupings)
      The groupings used for aggregating counts
    competition_filters (SearchCompetitionsFilters)
      The set of Competition filters to filter the documents
    dataset_filters (SearchDatasetsFilters)
      The set of Dataset filters to filter the documents
    discussion_filters (SearchDiscussionsFilters)
      The set of Discussion filters to filter the documents
    kernel_filters (SearchKernelsFilters)
      The set of Kernel filters to filter the documents
    model_filters (SearchModelsFilters)
      The set of Model filters to filter the documents
    shared_via_groups (str)
      List of groups to filter the documents. If specified, only resourced shared
      via one or more of these groups will be returned.
    user_filters (SearchUsersFilters)
      The set of User filters to filter the documents
  """

  def __init__(self):
    self._query = ""
    self._list_type = ListType.LIST_TYPE_UNSPECIFIED
    self._privacy = PrivacyFilter.ALL
    self._owner_type = OwnerType.OWNER_TYPE_UNSPECIFIED
    self._document_types = []
    self._tag_ids = []
    self._collection_id = None
    self._competition_ids = []
    self._only_counts = None
    self._owner_user_id = None
    self._owner_organization_id = None
    self._count_groupings = None
    self._competition_filters = None
    self._dataset_filters = None
    self._discussion_filters = None
    self._kernel_filters = None
    self._model_filters = None
    self._shared_via_groups = []
    self._user_filters = None
    self._freeze()

  @property
  def query(self) -> str:
    """The free-text query the user entered to filter results"""
    return self._query

  @query.setter
  def query(self, query: str):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def list_type(self) -> 'ListType':
    """The type of list being requested"""
    return self._list_type

  @list_type.setter
  def list_type(self, list_type: 'ListType'):
    if list_type is None:
      del self.list_type
      return
    if not isinstance(list_type, ListType):
      raise TypeError('list_type must be of type ListType')
    self._list_type = list_type

  @property
  def privacy(self) -> 'PrivacyFilter':
    """The privacy filter to apply"""
    return self._privacy

  @privacy.setter
  def privacy(self, privacy: 'PrivacyFilter'):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, PrivacyFilter):
      raise TypeError('privacy must be of type PrivacyFilter')
    self._privacy = privacy

  @property
  def owner_type(self) -> 'OwnerType':
    """The owner type filter to apply"""
    return self._owner_type

  @owner_type.setter
  def owner_type(self, owner_type: 'OwnerType'):
    if owner_type is None:
      del self.owner_type
      return
    if not isinstance(owner_type, OwnerType):
      raise TypeError('owner_type must be of type OwnerType')
    self._owner_type = owner_type

  @property
  def document_types(self) -> Optional[List['DocumentType']]:
    """The document type filter to apply"""
    return self._document_types

  @document_types.setter
  def document_types(self, document_types: Optional[List['DocumentType']]):
    if document_types is None:
      del self.document_types
      return
    if not isinstance(document_types, list):
      raise TypeError('document_types must be of type list')
    if not all([isinstance(t, DocumentType) for t in document_types]):
      raise TypeError('document_types must contain only items of type DocumentType')
    self._document_types = document_types

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The tags to use to filter the documents"""
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
  def collection_id(self) -> int:
    """The collection to use to filter the documents"""
    return self._collection_id or 0

  @collection_id.setter
  def collection_id(self, collection_id: Optional[int]):
    if collection_id is None:
      del self.collection_id
      return
    if not isinstance(collection_id, int):
      raise TypeError('collection_id must be of type int')
    self._collection_id = collection_id

  @property
  def competition_ids(self) -> Optional[List[int]]:
    """The Competitions to use to filter the documents"""
    return self._competition_ids

  @competition_ids.setter
  def competition_ids(self, competition_ids: Optional[List[int]]):
    if competition_ids is None:
      del self.competition_ids
      return
    if not isinstance(competition_ids, list):
      raise TypeError('competition_ids must be of type list')
    if not all([isinstance(t, int) for t in competition_ids]):
      raise TypeError('competition_ids must contain only items of type int')
    self._competition_ids = competition_ids

  @property
  def only_counts(self) -> bool:
    """Whether to only return counts by document type (vs. full document results)"""
    return self._only_counts or False

  @only_counts.setter
  def only_counts(self, only_counts: Optional[bool]):
    if only_counts is None:
      del self.only_counts
      return
    if not isinstance(only_counts, bool):
      raise TypeError('only_counts must be of type bool')
    self._only_counts = only_counts

  @property
  def owner_user_id(self) -> int:
    """The owner user to filter the documents"""
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: int):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    del self.owner_organization_id
    self._owner_user_id = owner_user_id

  @property
  def owner_organization_id(self) -> int:
    """The owner organization to filter the documents"""
    return self._owner_organization_id or 0

  @owner_organization_id.setter
  def owner_organization_id(self, owner_organization_id: int):
    if owner_organization_id is None:
      del self.owner_organization_id
      return
    if not isinstance(owner_organization_id, int):
      raise TypeError('owner_organization_id must be of type int')
    del self.owner_user_id
    self._owner_organization_id = owner_organization_id

  @property
  def count_groupings(self) -> Optional['ListSearchContentCountGroupings']:
    """The groupings used for aggregating counts"""
    return self._count_groupings

  @count_groupings.setter
  def count_groupings(self, count_groupings: Optional['ListSearchContentCountGroupings']):
    if count_groupings is None:
      del self.count_groupings
      return
    if not isinstance(count_groupings, ListSearchContentCountGroupings):
      raise TypeError('count_groupings must be of type ListSearchContentCountGroupings')
    self._count_groupings = count_groupings

  @property
  def shared_via_groups(self) -> Optional[List[str]]:
    r"""
    List of groups to filter the documents. If specified, only resourced shared
    via one or more of these groups will be returned.
    """
    return self._shared_via_groups

  @shared_via_groups.setter
  def shared_via_groups(self, shared_via_groups: Optional[List[str]]):
    if shared_via_groups is None:
      del self.shared_via_groups
      return
    if not isinstance(shared_via_groups, list):
      raise TypeError('shared_via_groups must be of type list')
    if not all([isinstance(t, str) for t in shared_via_groups]):
      raise TypeError('shared_via_groups must contain only items of type str')
    self._shared_via_groups = shared_via_groups

  @property
  def competition_filters(self) -> Optional['SearchCompetitionsFilters']:
    """The set of Competition filters to filter the documents"""
    return self._competition_filters

  @competition_filters.setter
  def competition_filters(self, competition_filters: Optional['SearchCompetitionsFilters']):
    if competition_filters is None:
      del self.competition_filters
      return
    if not isinstance(competition_filters, SearchCompetitionsFilters):
      raise TypeError('competition_filters must be of type SearchCompetitionsFilters')
    self._competition_filters = competition_filters

  @property
  def dataset_filters(self) -> Optional['SearchDatasetsFilters']:
    """The set of Dataset filters to filter the documents"""
    return self._dataset_filters

  @dataset_filters.setter
  def dataset_filters(self, dataset_filters: Optional['SearchDatasetsFilters']):
    if dataset_filters is None:
      del self.dataset_filters
      return
    if not isinstance(dataset_filters, SearchDatasetsFilters):
      raise TypeError('dataset_filters must be of type SearchDatasetsFilters')
    self._dataset_filters = dataset_filters

  @property
  def discussion_filters(self) -> Optional['SearchDiscussionsFilters']:
    """The set of Discussion filters to filter the documents"""
    return self._discussion_filters

  @discussion_filters.setter
  def discussion_filters(self, discussion_filters: Optional['SearchDiscussionsFilters']):
    if discussion_filters is None:
      del self.discussion_filters
      return
    if not isinstance(discussion_filters, SearchDiscussionsFilters):
      raise TypeError('discussion_filters must be of type SearchDiscussionsFilters')
    self._discussion_filters = discussion_filters

  @property
  def kernel_filters(self) -> Optional['SearchKernelsFilters']:
    """The set of Kernel filters to filter the documents"""
    return self._kernel_filters

  @kernel_filters.setter
  def kernel_filters(self, kernel_filters: Optional['SearchKernelsFilters']):
    if kernel_filters is None:
      del self.kernel_filters
      return
    if not isinstance(kernel_filters, SearchKernelsFilters):
      raise TypeError('kernel_filters must be of type SearchKernelsFilters')
    self._kernel_filters = kernel_filters

  @property
  def model_filters(self) -> Optional['SearchModelsFilters']:
    """The set of Model filters to filter the documents"""
    return self._model_filters

  @model_filters.setter
  def model_filters(self, model_filters: Optional['SearchModelsFilters']):
    if model_filters is None:
      del self.model_filters
      return
    if not isinstance(model_filters, SearchModelsFilters):
      raise TypeError('model_filters must be of type SearchModelsFilters')
    self._model_filters = model_filters

  @property
  def user_filters(self) -> Optional['SearchUsersFilters']:
    """The set of User filters to filter the documents"""
    return self._user_filters

  @user_filters.setter
  def user_filters(self, user_filters: Optional['SearchUsersFilters']):
    if user_filters is None:
      del self.user_filters
      return
    if not isinstance(user_filters, SearchUsersFilters):
      raise TypeError('user_filters must be of type SearchUsersFilters')
    self._user_filters = user_filters


class ListSearchContentRequest(KaggleObject):
  r"""
  Attributes:
    filters (ListSearchContentFilters)
      Canonical filters to apply to the search
    canonical_order_by (ListSearchContentOrderBy)
      Canonical order to apply to the results
    competitions_order_by (SearchCompetitionsOrderBy)
      Competitions order to apply to the results
    datasets_order_by (SearchDatasetsOrderBy)
      Datasets order to apply to the results
    kernels_order_by (SearchKernelsOrderBy)
      Kernels order to apply to the results
    models_order_by (SearchModelsOrderBy)
      Models order to apply to the results
    discussions_order_by (SearchDiscussionsOrderBy)
      Discussions order to apply to the results
    page_token (str)
      Page token for paging (see aip.dev/158)
    page_size (int)
      Number of documents per page to return
    skip (int)
      How many results to skip
    users_order_by (SearchUsersOrderBy)
      Users order to apply to the results
  """

  def __init__(self):
    self._filters = None
    self._canonical_order_by = None
    self._competitions_order_by = None
    self._datasets_order_by = None
    self._kernels_order_by = None
    self._models_order_by = None
    self._discussions_order_by = None
    self._page_token = ""
    self._page_size = 0
    self._skip = 0
    self._users_order_by = None
    self._freeze()

  @property
  def filters(self) -> Optional['ListSearchContentFilters']:
    """Canonical filters to apply to the search"""
    return self._filters

  @filters.setter
  def filters(self, filters: Optional['ListSearchContentFilters']):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, ListSearchContentFilters):
      raise TypeError('filters must be of type ListSearchContentFilters')
    self._filters = filters

  @property
  def canonical_order_by(self) -> 'ListSearchContentOrderBy':
    """Canonical order to apply to the results"""
    return self._canonical_order_by or ListSearchContentOrderBy.LIST_SEARCH_CONTENT_ORDER_BY_UNSPECIFIED

  @canonical_order_by.setter
  def canonical_order_by(self, canonical_order_by: 'ListSearchContentOrderBy'):
    if canonical_order_by is None:
      del self.canonical_order_by
      return
    if not isinstance(canonical_order_by, ListSearchContentOrderBy):
      raise TypeError('canonical_order_by must be of type ListSearchContentOrderBy')
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._canonical_order_by = canonical_order_by

  @property
  def competitions_order_by(self) -> 'SearchCompetitionsOrderBy':
    """Competitions order to apply to the results"""
    return self._competitions_order_by or SearchCompetitionsOrderBy.SEARCH_COMPETITIONS_ORDER_BY_UNSPECIFIED

  @competitions_order_by.setter
  def competitions_order_by(self, competitions_order_by: 'SearchCompetitionsOrderBy'):
    if competitions_order_by is None:
      del self.competitions_order_by
      return
    if not isinstance(competitions_order_by, SearchCompetitionsOrderBy):
      raise TypeError('competitions_order_by must be of type SearchCompetitionsOrderBy')
    del self.canonical_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._competitions_order_by = competitions_order_by

  @property
  def datasets_order_by(self) -> 'SearchDatasetsOrderBy':
    """Datasets order to apply to the results"""
    return self._datasets_order_by or SearchDatasetsOrderBy.SEARCH_DATASETS_ORDER_BY_UNSPECIFIED

  @datasets_order_by.setter
  def datasets_order_by(self, datasets_order_by: 'SearchDatasetsOrderBy'):
    if datasets_order_by is None:
      del self.datasets_order_by
      return
    if not isinstance(datasets_order_by, SearchDatasetsOrderBy):
      raise TypeError('datasets_order_by must be of type SearchDatasetsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._datasets_order_by = datasets_order_by

  @property
  def kernels_order_by(self) -> 'SearchKernelsOrderBy':
    """Kernels order to apply to the results"""
    return self._kernels_order_by or SearchKernelsOrderBy.SEARCH_KERNELS_ORDER_BY_UNSPECIFIED

  @kernels_order_by.setter
  def kernels_order_by(self, kernels_order_by: 'SearchKernelsOrderBy'):
    if kernels_order_by is None:
      del self.kernels_order_by
      return
    if not isinstance(kernels_order_by, SearchKernelsOrderBy):
      raise TypeError('kernels_order_by must be of type SearchKernelsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.models_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._kernels_order_by = kernels_order_by

  @property
  def models_order_by(self) -> 'SearchModelsOrderBy':
    """Models order to apply to the results"""
    return self._models_order_by or SearchModelsOrderBy.MODELS_SEARCH_ORDER_BY_UNSPECIFIED

  @models_order_by.setter
  def models_order_by(self, models_order_by: 'SearchModelsOrderBy'):
    if models_order_by is None:
      del self.models_order_by
      return
    if not isinstance(models_order_by, SearchModelsOrderBy):
      raise TypeError('models_order_by must be of type SearchModelsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.discussions_order_by
    del self.users_order_by
    self._models_order_by = models_order_by

  @property
  def discussions_order_by(self) -> 'SearchDiscussionsOrderBy':
    """Discussions order to apply to the results"""
    return self._discussions_order_by or SearchDiscussionsOrderBy.SEARCH_DISCUSSIONS_ORDER_BY_UNSPECIFIED

  @discussions_order_by.setter
  def discussions_order_by(self, discussions_order_by: 'SearchDiscussionsOrderBy'):
    if discussions_order_by is None:
      del self.discussions_order_by
      return
    if not isinstance(discussions_order_by, SearchDiscussionsOrderBy):
      raise TypeError('discussions_order_by must be of type SearchDiscussionsOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.users_order_by
    self._discussions_order_by = discussions_order_by

  @property
  def users_order_by(self) -> 'SearchUsersOrderBy':
    """Users order to apply to the results"""
    return self._users_order_by or SearchUsersOrderBy.SEARCH_USERS_ORDER_BY_UNSPECIFIED

  @users_order_by.setter
  def users_order_by(self, users_order_by: 'SearchUsersOrderBy'):
    if users_order_by is None:
      del self.users_order_by
      return
    if not isinstance(users_order_by, SearchUsersOrderBy):
      raise TypeError('users_order_by must be of type SearchUsersOrderBy')
    del self.canonical_order_by
    del self.competitions_order_by
    del self.datasets_order_by
    del self.kernels_order_by
    del self.models_order_by
    del self.discussions_order_by
    self._users_order_by = users_order_by

  @property
  def page_token(self) -> str:
    """Page token for paging (see aip.dev/158)"""
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def page_size(self) -> int:
    """Number of documents per page to return"""
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
  def skip(self) -> int:
    """How many results to skip"""
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip


class ListSearchContentResponse(KaggleObject):
  r"""
  Attributes:
    documents (ListSearchContentDocument)
      The list of documents returned after filtering
    total_documents (int)
      The total number of documents matching any filters
    next_page_token (str)
      The token to request the next page
    aggregations (ListSearchContentAggregation)
      Any aggregations that have been computed for this query
  """

  def __init__(self):
    self._documents = []
    self._total_documents = 0
    self._next_page_token = ""
    self._aggregations = []
    self._freeze()

  @property
  def documents(self) -> Optional[List[Optional['ListSearchContentDocument']]]:
    """The list of documents returned after filtering"""
    return self._documents

  @documents.setter
  def documents(self, documents: Optional[List[Optional['ListSearchContentDocument']]]):
    if documents is None:
      del self.documents
      return
    if not isinstance(documents, list):
      raise TypeError('documents must be of type list')
    if not all([isinstance(t, ListSearchContentDocument) for t in documents]):
      raise TypeError('documents must contain only items of type ListSearchContentDocument')
    self._documents = documents

  @property
  def total_documents(self) -> int:
    """The total number of documents matching any filters"""
    return self._total_documents

  @total_documents.setter
  def total_documents(self, total_documents: int):
    if total_documents is None:
      del self.total_documents
      return
    if not isinstance(total_documents, int):
      raise TypeError('total_documents must be of type int')
    self._total_documents = total_documents

  @property
  def next_page_token(self) -> str:
    """The token to request the next page"""
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def aggregations(self) -> Optional[List[Optional['ListSearchContentAggregation']]]:
    """Any aggregations that have been computed for this query"""
    return self._aggregations

  @aggregations.setter
  def aggregations(self, aggregations: Optional[List[Optional['ListSearchContentAggregation']]]):
    if aggregations is None:
      del self.aggregations
      return
    if not isinstance(aggregations, list):
      raise TypeError('aggregations must be of type list')
    if not all([isinstance(t, ListSearchContentAggregation) for t in aggregations]):
      raise TypeError('aggregations must contain only items of type ListSearchContentAggregation')
    self._aggregations = aggregations


EnrichedInfo._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("currentUserCanEdit", "current_user_can_edit", "_current_user_can_edit", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserVote", "current_user_vote", "_current_user_vote", Vote, None, EnumSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("currentUserCanDelete", "current_user_can_delete", "_current_user_can_delete", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserCanPin", "current_user_can_pin", "_current_user_can_pin", bool, False, PredefinedSerializer()),
]

ListSearchContentAggregation._fields = [
  FieldMetadata("documentType", "document_type", "_document_type", DocumentType, None, EnumSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

ListSearchContentCountGroupings._fields = [
  FieldMetadata("byDocumentType", "by_document_type", "_by_document_type", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("byCompetitionId", "by_competition_id", "_by_competition_id", bool, None, PredefinedSerializer(), optional=True),
]

ListSearchContentDocument._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("documentId", "document_id", "_document_id", str, "", PredefinedSerializer()),
  FieldMetadata("documentType", "document_type", "_document_type", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("votes", "votes", "_votes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", Medal, None, EnumSerializer(), optional=True),
  FieldMetadata("isCurrentUserBookmarked", "is_current_user_bookmarked", "_is_current_user_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("totalComments", "total_comments", "_total_comments", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("ownerOrganization", "owner_organization", "_owner_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("enrichedInfo", "enriched_info", "_enriched_info", EnrichedInfo, None, KaggleObjectSerializer()),
  FieldMetadata("competitionDocument", "competition_document", "_competition_document", SearchCompetitionsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("datasetDocument", "dataset_document", "_dataset_document", SearchDatasetsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("discussionDocument", "discussion_document", "_discussion_document", SearchDiscussionsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelDocument", "kernel_document", "_kernel_document", SearchKernelsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("modelDocument", "model_document", "_model_document", SearchModelsDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userDocument", "user_document", "_user_document", SearchUsersDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkTaskDocument", "benchmark_task_document", "_benchmark_task_document", SearchBenchmarkTasksDocument, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkDocument", "benchmark_document", "_benchmark_document", SearchBenchmarksDocument, None, KaggleObjectSerializer(), optional=True),
]

ListSearchContentFilters._fields = [
  FieldMetadata("query", "query", "_query", str, "", PredefinedSerializer()),
  FieldMetadata("listType", "list_type", "_list_type", ListType, ListType.LIST_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("privacy", "privacy", "_privacy", PrivacyFilter, PrivacyFilter.ALL, EnumSerializer()),
  FieldMetadata("ownerType", "owner_type", "_owner_type", OwnerType, OwnerType.OWNER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("documentTypes", "document_types", "_document_types", DocumentType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("collectionId", "collection_id", "_collection_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionIds", "competition_ids", "_competition_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("onlyCounts", "only_counts", "_only_counts", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerOrganizationId", "owner_organization_id", "_owner_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countGroupings", "count_groupings", "_count_groupings", ListSearchContentCountGroupings, None, KaggleObjectSerializer()),
  FieldMetadata("competitionFilters", "competition_filters", "_competition_filters", SearchCompetitionsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("datasetFilters", "dataset_filters", "_dataset_filters", SearchDatasetsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("discussionFilters", "discussion_filters", "_discussion_filters", SearchDiscussionsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("kernelFilters", "kernel_filters", "_kernel_filters", SearchKernelsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("modelFilters", "model_filters", "_model_filters", SearchModelsFilters, None, KaggleObjectSerializer()),
  FieldMetadata("sharedViaGroups", "shared_via_groups", "_shared_via_groups", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userFilters", "user_filters", "_user_filters", SearchUsersFilters, None, KaggleObjectSerializer()),
]

ListSearchContentRequest._fields = [
  FieldMetadata("filters", "filters", "_filters", ListSearchContentFilters, None, KaggleObjectSerializer()),
  FieldMetadata("canonicalOrderBy", "canonical_order_by", "_canonical_order_by", ListSearchContentOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("competitionsOrderBy", "competitions_order_by", "_competitions_order_by", SearchCompetitionsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("datasetsOrderBy", "datasets_order_by", "_datasets_order_by", SearchDatasetsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("kernelsOrderBy", "kernels_order_by", "_kernels_order_by", SearchKernelsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("modelsOrderBy", "models_order_by", "_models_order_by", SearchModelsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("discussionsOrderBy", "discussions_order_by", "_discussions_order_by", SearchDiscussionsOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("usersOrderBy", "users_order_by", "_users_order_by", SearchUsersOrderBy, None, EnumSerializer(), optional=True),
]

ListSearchContentResponse._fields = [
  FieldMetadata("documents", "documents", "_documents", ListSearchContentDocument, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalDocuments", "total_documents", "_total_documents", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("aggregations", "aggregations", "_aggregations", ListSearchContentAggregation, [], ListSerializer(KaggleObjectSerializer())),
]

