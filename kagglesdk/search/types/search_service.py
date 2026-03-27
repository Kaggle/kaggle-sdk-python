from datetime import datetime
import enum
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkType
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.competitions.types.competition_enums import HostSegment
from kagglesdk.discussions.types.writeup_enums import WriteUpType
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import ResourceReferenceType
from kagglesdk.kernels.types.kernels_types import DataSource
from kagglesdk.models.types.model_enums import GatingAgreementRequestsReviewStatus, ModelFramework, ModelLicense, ModelOwnerType
from kagglesdk.models.types.model_types import ModelGating, ModelInstance, Owner
from kagglesdk.search.types.search_enums import DocumentType
from kagglesdk.tags.types.tag_service import TagList
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import Optional, List

class FilterName(enum.Enum):
  DATE = 0
  IN = 1
  BY = 2
  TAGS = 3
  OWNER = 4
  SORT_BY = 6
  COMPETITION_EVALUATION_ALGORITHM = 7
  DATASET_LICENSE = 8
  DATASET_SIZE = 9
  DATASET_SIZE_GROUP = 10
  DATASET_FILE_TYPES = 11
  NOTEBOOK_LANGUAGE = 12
  VIEWED_BY_YOU = 13
  CREATOR = 15
  MODEL_LICENSE = 16
  MODEL_FRAMEWORK = 17
  EXCLUDE_API_BASED_MODELS = 18
  TOPIC_TYPE = 19
  WRITE_UP_TYPE = 20

class FilterType(enum.Enum):
  RADIO = 0
  CHECKBOX = 1
  TEXT = 2

class SearchIndex(enum.Enum):
  r"""
  Specific search index name used to get/set in recent search
  history results.
  """
  SEARCH_INDEX_UNSPECIFIED = 0
  COMPETITIONS = 1
  DATASETS = 2
  GLOBAL = 3
  KERNELS = 5
  TOPICS = 6
  MODELS = 7

class BenchmarkItemInfo(KaggleObject):
  r"""
  Attributes:
    subtitle (str)
    type (BenchmarkType)
  """

  def __init__(self):
    self._subtitle = ""
    self._type = BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def subtitle(self) -> str:
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
  def type(self) -> 'BenchmarkType':
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkType):
      raise TypeError('type must be of type BenchmarkType')
    self._type = type


class BenchmarkTaskItemInfo(KaggleObject):
  r"""
  Attributes:
    description (str)
  """

  def __init__(self):
    self._description = ""
    self._freeze()

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


class BenchmarkTasksSearchFilter(KaggleObject):
  r"""
  Attributes:
    owner_user_id (int)
    search_query (str)
    ids (int)
    content_state (ContentState)
  """

  def __init__(self):
    self._owner_user_id = None
    self._search_query = None
    self._ids = []
    self._content_state = None
    self._freeze()

  @property
  def owner_user_id(self) -> int:
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids

  @property
  def content_state(self) -> 'ContentState':
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state


class CategoryFilter(KaggleObject):
  r"""
  Attributes:
    name (DocumentType)
    count (int)
  """

  def __init__(self):
    self._name = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._count = 0
    self._freeze()

  @property
  def name(self) -> 'DocumentType':
    return self._name

  @name.setter
  def name(self, name: 'DocumentType'):
    if name is None:
      del self.name
      return
    if not isinstance(name, DocumentType):
      raise TypeError('name must be of type DocumentType')
    self._name = name

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class CommentItemInfo(KaggleObject):
  r"""
  Attributes:
    forum_name (str)
    topic_url (str)
    total_replies (int)
  """

  def __init__(self):
    self._forum_name = ""
    self._topic_url = ""
    self._total_replies = 0
    self._freeze()

  @property
  def forum_name(self) -> str:
    return self._forum_name

  @forum_name.setter
  def forum_name(self, forum_name: str):
    if forum_name is None:
      del self.forum_name
      return
    if not isinstance(forum_name, str):
      raise TypeError('forum_name must be of type str')
    self._forum_name = forum_name

  @property
  def topic_url(self) -> str:
    return self._topic_url

  @topic_url.setter
  def topic_url(self, topic_url: str):
    if topic_url is None:
      del self.topic_url
      return
    if not isinstance(topic_url, str):
      raise TypeError('topic_url must be of type str')
    self._topic_url = topic_url

  @property
  def total_replies(self) -> int:
    return self._total_replies

  @total_replies.setter
  def total_replies(self, total_replies: int):
    if total_replies is None:
      del self.total_replies
      return
    if not isinstance(total_replies, int):
      raise TypeError('total_replies must be of type int')
    self._total_replies = total_replies


class CompetitionItemInfo(KaggleObject):
  r"""
  Attributes:
    teams_count (int)
    deadline_date (datetime)
    prize_value (float)
    type (HostSegment)
    host_name (str)
    subtitle (str)
  """

  def __init__(self):
    self._teams_count = 0
    self._deadline_date = None
    self._prize_value = 0.0
    self._type = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._host_name = ""
    self._subtitle = ""
    self._freeze()

  @property
  def teams_count(self) -> int:
    return self._teams_count

  @teams_count.setter
  def teams_count(self, teams_count: int):
    if teams_count is None:
      del self.teams_count
      return
    if not isinstance(teams_count, int):
      raise TypeError('teams_count must be of type int')
    self._teams_count = teams_count

  @property
  def deadline_date(self) -> datetime:
    return self._deadline_date

  @deadline_date.setter
  def deadline_date(self, deadline_date: datetime):
    if deadline_date is None:
      del self.deadline_date
      return
    if not isinstance(deadline_date, datetime):
      raise TypeError('deadline_date must be of type datetime')
    self._deadline_date = deadline_date

  @property
  def prize_value(self) -> float:
    return self._prize_value

  @prize_value.setter
  def prize_value(self, prize_value: float):
    if prize_value is None:
      del self.prize_value
      return
    if not isinstance(prize_value, float):
      raise TypeError('prize_value must be of type float')
    self._prize_value = prize_value

  @property
  def type(self) -> 'HostSegment':
    return self._type

  @type.setter
  def type(self, type: 'HostSegment'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HostSegment):
      raise TypeError('type must be of type HostSegment')
    self._type = type

  @property
  def host_name(self) -> str:
    return self._host_name

  @host_name.setter
  def host_name(self, host_name: str):
    if host_name is None:
      del self.host_name
      return
    if not isinstance(host_name, str):
      raise TypeError('host_name must be of type str')
    self._host_name = host_name

  @property
  def subtitle(self) -> str:
    return self._subtitle

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle


class CourseItemInfo(KaggleObject):
  r"""
  Attributes:
    estimated_hours (int)
    description (str)
  """

  def __init__(self):
    self._estimated_hours = 0
    self._description = ""
    self._freeze()

  @property
  def estimated_hours(self) -> int:
    return self._estimated_hours

  @estimated_hours.setter
  def estimated_hours(self, estimated_hours: int):
    if estimated_hours is None:
      del self.estimated_hours
      return
    if not isinstance(estimated_hours, int):
      raise TypeError('estimated_hours must be of type int')
    self._estimated_hours = estimated_hours

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


class DatasetItemInfo(KaggleObject):
  r"""
  Attributes:
    size (int)
    file_types (str)
    current_dataset_version_id (int)
    dataset_slug (str)
    total_downloads (int)
    subtitle (str)
  """

  def __init__(self):
    self._size = 0
    self._file_types = []
    self._current_dataset_version_id = 0
    self._dataset_slug = ""
    self._total_downloads = 0
    self._subtitle = ""
    self._freeze()

  @property
  def size(self) -> int:
    return self._size

  @size.setter
  def size(self, size: int):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size

  @property
  def file_types(self) -> Optional[List[str]]:
    return self._file_types

  @file_types.setter
  def file_types(self, file_types: Optional[List[str]]):
    if file_types is None:
      del self.file_types
      return
    if not isinstance(file_types, list):
      raise TypeError('file_types must be of type list')
    if not all([isinstance(t, str) for t in file_types]):
      raise TypeError('file_types must contain only items of type str')
    self._file_types = file_types

  @property
  def current_dataset_version_id(self) -> int:
    return self._current_dataset_version_id

  @current_dataset_version_id.setter
  def current_dataset_version_id(self, current_dataset_version_id: int):
    if current_dataset_version_id is None:
      del self.current_dataset_version_id
      return
    if not isinstance(current_dataset_version_id, int):
      raise TypeError('current_dataset_version_id must be of type int')
    self._current_dataset_version_id = current_dataset_version_id

  @property
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def total_downloads(self) -> int:
    return self._total_downloads

  @total_downloads.setter
  def total_downloads(self, total_downloads: int):
    if total_downloads is None:
      del self.total_downloads
      return
    if not isinstance(total_downloads, int):
      raise TypeError('total_downloads must be of type int')
    self._total_downloads = total_downloads

  @property
  def subtitle(self) -> str:
    return self._subtitle

  @subtitle.setter
  def subtitle(self, subtitle: str):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle


class FilterOption(KaggleObject):
  r"""
  Attributes:
    name (str)
    count (int)
  """

  def __init__(self):
    self._name = ""
    self._count = 0
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
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class FullSearchResponse(KaggleObject):
  r"""
  Attributes:
    documents (SearchItem)
    count (int)
    filters (SearchFilter)
    categories (CategoryFilter)
  """

  def __init__(self):
    self._documents = []
    self._count = 0
    self._filters = []
    self._categories = []
    self._freeze()

  @property
  def documents(self) -> Optional[List[Optional['SearchItem']]]:
    return self._documents

  @documents.setter
  def documents(self, documents: Optional[List[Optional['SearchItem']]]):
    if documents is None:
      del self.documents
      return
    if not isinstance(documents, list):
      raise TypeError('documents must be of type list')
    if not all([isinstance(t, SearchItem) for t in documents]):
      raise TypeError('documents must contain only items of type SearchItem')
    self._documents = documents

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def filters(self) -> Optional[List[Optional['SearchFilter']]]:
    return self._filters

  @filters.setter
  def filters(self, filters: Optional[List[Optional['SearchFilter']]]):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, list):
      raise TypeError('filters must be of type list')
    if not all([isinstance(t, SearchFilter) for t in filters]):
      raise TypeError('filters must contain only items of type SearchFilter')
    self._filters = filters

  @property
  def categories(self) -> Optional[List[Optional['CategoryFilter']]]:
    return self._categories

  @categories.setter
  def categories(self, categories: Optional[List[Optional['CategoryFilter']]]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, list):
      raise TypeError('categories must be of type list')
    if not all([isinstance(t, CategoryFilter) for t in categories]):
      raise TypeError('categories must contain only items of type CategoryFilter')
    self._categories = categories


class FullSearchWebRequest(KaggleObject):
  r"""
  Attributes:
    query (str)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    page (int)
    results_per_page (int)
    show_private (bool)
      Option to filter out private content, this treats the searcher as an
      anonymous user
  """

  def __init__(self):
    self._query = None
    self._page = 0
    self._results_per_page = 0
    self._show_private = False
    self._freeze()

  @property
  def query(self) -> str:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._query or None

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def page(self) -> int:
    return self._page

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def results_per_page(self) -> int:
    return self._results_per_page

  @results_per_page.setter
  def results_per_page(self, results_per_page: int):
    if results_per_page is None:
      del self.results_per_page
      return
    if not isinstance(results_per_page, int):
      raise TypeError('results_per_page must be of type int')
    self._results_per_page = results_per_page

  @property
  def show_private(self) -> bool:
    r"""
    Option to filter out private content, this treats the searcher as an
    anonymous user
    """
    return self._show_private

  @show_private.setter
  def show_private(self, show_private: bool):
    if show_private is None:
      del self.show_private
      return
    if not isinstance(show_private, bool):
      raise TypeError('show_private must be of type bool')
    self._show_private = show_private


class GetAutoCompleteSuggestionsRequest(KaggleObject):
  r"""
  Attributes:
    prefix (str)
  """

  def __init__(self):
    self._prefix = ""
    self._freeze()

  @property
  def prefix(self) -> str:
    return self._prefix

  @prefix.setter
  def prefix(self, prefix: str):
    if prefix is None:
      del self.prefix
      return
    if not isinstance(prefix, str):
      raise TypeError('prefix must be of type str')
    self._prefix = prefix


class GetAutoCompleteSuggestionsResponse(KaggleObject):
  r"""
  Attributes:
    auto_complete_suggestions (str)
  """

  def __init__(self):
    self._auto_complete_suggestions = []
    self._freeze()

  @property
  def auto_complete_suggestions(self) -> Optional[List[str]]:
    return self._auto_complete_suggestions

  @auto_complete_suggestions.setter
  def auto_complete_suggestions(self, auto_complete_suggestions: Optional[List[str]]):
    if auto_complete_suggestions is None:
      del self.auto_complete_suggestions
      return
    if not isinstance(auto_complete_suggestions, list):
      raise TypeError('auto_complete_suggestions must be of type list')
    if not all([isinstance(t, str) for t in auto_complete_suggestions]):
      raise TypeError('auto_complete_suggestions must contain only items of type str')
    self._auto_complete_suggestions = auto_complete_suggestions


class GetPopularTagsRequest(KaggleObject):
  r"""
  """

  pass

class GetPopularTagsResponse(KaggleObject):
  r"""
  Attributes:
    popular_tags (FilterOption)
  """

  def __init__(self):
    self._popular_tags = []
    self._freeze()

  @property
  def popular_tags(self) -> Optional[List[Optional['FilterOption']]]:
    return self._popular_tags

  @popular_tags.setter
  def popular_tags(self, popular_tags: Optional[List[Optional['FilterOption']]]):
    if popular_tags is None:
      del self.popular_tags
      return
    if not isinstance(popular_tags, list):
      raise TypeError('popular_tags must be of type list')
    if not all([isinstance(t, FilterOption) for t in popular_tags]):
      raise TypeError('popular_tags must contain only items of type FilterOption')
    self._popular_tags = popular_tags


class GetRecentSearchesRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    specific_search_indices (SearchIndex)
      If empty, will not filter out any query histories based
      on search indices.
      List of specific search indices to limit the result to only
      search queries made from these indices.
  """

  def __init__(self):
    self._user_id = None
    self._specific_search_indices = []
    self._freeze()

  @property
  def user_id(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._user_id or None

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def specific_search_indices(self) -> Optional[List['SearchIndex']]:
    r"""
    If empty, will not filter out any query histories based
    on search indices.
    List of specific search indices to limit the result to only
    search queries made from these indices.
    """
    return self._specific_search_indices

  @specific_search_indices.setter
  def specific_search_indices(self, specific_search_indices: Optional[List['SearchIndex']]):
    if specific_search_indices is None:
      del self.specific_search_indices
      return
    if not isinstance(specific_search_indices, list):
      raise TypeError('specific_search_indices must be of type list')
    if not all([isinstance(t, SearchIndex) for t in specific_search_indices]):
      raise TypeError('specific_search_indices must contain only items of type SearchIndex')
    self._specific_search_indices = specific_search_indices


class GetRecentSearchesResponse(KaggleObject):
  r"""
  Attributes:
    recent_searches (str)
  """

  def __init__(self):
    self._recent_searches = []
    self._freeze()

  @property
  def recent_searches(self) -> Optional[List[str]]:
    return self._recent_searches

  @recent_searches.setter
  def recent_searches(self, recent_searches: Optional[List[str]]):
    if recent_searches is None:
      del self.recent_searches
      return
    if not isinstance(recent_searches, list):
      raise TypeError('recent_searches must be of type list')
    if not all([isinstance(t, str) for t in recent_searches]):
      raise TypeError('recent_searches must contain only items of type str')
    self._recent_searches = recent_searches


class GetTrendingSearchesRequest(KaggleObject):
  r"""
  """

  pass

class GetTrendingSearchesResponse(KaggleObject):
  r"""
  Attributes:
    trending_searches (str)
  """

  def __init__(self):
    self._trending_searches = []
    self._freeze()

  @property
  def trending_searches(self) -> Optional[List[str]]:
    return self._trending_searches

  @trending_searches.setter
  def trending_searches(self, trending_searches: Optional[List[str]]):
    if trending_searches is None:
      del self.trending_searches
      return
    if not isinstance(trending_searches, list):
      raise TypeError('trending_searches must be of type list')
    if not all([isinstance(t, str) for t in trending_searches]):
      raise TypeError('trending_searches must contain only items of type str')
    self._trending_searches = trending_searches


class KernelItemInfo(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
      The current or most recently created kernel session id for the kernel.
    has_data_output_files (bool)
      Ex: Whether a kernel could be used as a data input to another kernel. This
      does not include visualization outputs.
    is_utility_script (bool)
    has_collaborators (bool)
    total_comments (int)
    data_sources (DataSource)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._has_data_output_files = False
    self._is_utility_script = False
    self._has_collaborators = False
    self._total_comments = 0
    self._data_sources = []
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    """The current or most recently created kernel session id for the kernel."""
    return self._kernel_session_id

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id

  @property
  def has_data_output_files(self) -> bool:
    r"""
    Ex: Whether a kernel could be used as a data input to another kernel. This
    does not include visualization outputs.
    """
    return self._has_data_output_files

  @has_data_output_files.setter
  def has_data_output_files(self, has_data_output_files: bool):
    if has_data_output_files is None:
      del self.has_data_output_files
      return
    if not isinstance(has_data_output_files, bool):
      raise TypeError('has_data_output_files must be of type bool')
    self._has_data_output_files = has_data_output_files

  @property
  def is_utility_script(self) -> bool:
    return self._is_utility_script

  @is_utility_script.setter
  def is_utility_script(self, is_utility_script: bool):
    if is_utility_script is None:
      del self.is_utility_script
      return
    if not isinstance(is_utility_script, bool):
      raise TypeError('is_utility_script must be of type bool')
    self._is_utility_script = is_utility_script

  @property
  def has_collaborators(self) -> bool:
    return self._has_collaborators

  @has_collaborators.setter
  def has_collaborators(self, has_collaborators: bool):
    if has_collaborators is None:
      del self.has_collaborators
      return
    if not isinstance(has_collaborators, bool):
      raise TypeError('has_collaborators must be of type bool')
    self._has_collaborators = has_collaborators

  @property
  def total_comments(self) -> int:
    return self._total_comments

  @total_comments.setter
  def total_comments(self, total_comments: int):
    if total_comments is None:
      del self.total_comments
      return
    if not isinstance(total_comments, int):
      raise TypeError('total_comments must be of type int')
    self._total_comments = total_comments

  @property
  def data_sources(self) -> Optional[List[Optional['DataSource']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSource']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSource) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSource')
    self._data_sources = data_sources


class LogSearchRequest(KaggleObject):
  r"""
  Attributes:
    index (str)
    is_quick (bool)
    query (str)
    rank (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    id (str)
    url (str)
    seconds_spent_searching (float)
    token (str)
    is_private (bool)
    client_events_session_id (str)
      Browser session ID from ka_sessionid cookie to track search activity within
      a session.
  """

  def __init__(self):
    self._index = ""
    self._is_quick = False
    self._query = ""
    self._rank = None
    self._id = None
    self._url = None
    self._seconds_spent_searching = 0.0
    self._token = None
    self._is_private = None
    self._client_events_session_id = None
    self._freeze()

  @property
  def index(self) -> str:
    return self._index

  @index.setter
  def index(self, index: str):
    if index is None:
      del self.index
      return
    if not isinstance(index, str):
      raise TypeError('index must be of type str')
    self._index = index

  @property
  def is_quick(self) -> bool:
    return self._is_quick

  @is_quick.setter
  def is_quick(self, is_quick: bool):
    if is_quick is None:
      del self.is_quick
      return
    if not isinstance(is_quick, bool):
      raise TypeError('is_quick must be of type bool')
    self._is_quick = is_quick

  @property
  def query(self) -> str:
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
  def rank(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._rank or None

  @rank.setter
  def rank(self, rank: Optional[int]):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

  @property
  def id(self) -> str:
    return self._id or None

  @id.setter
  def id(self, id: Optional[str]):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def url(self) -> str:
    return self._url or None

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def seconds_spent_searching(self) -> float:
    return self._seconds_spent_searching

  @seconds_spent_searching.setter
  def seconds_spent_searching(self, seconds_spent_searching: float):
    if seconds_spent_searching is None:
      del self.seconds_spent_searching
      return
    if not isinstance(seconds_spent_searching, float):
      raise TypeError('seconds_spent_searching must be of type float')
    self._seconds_spent_searching = seconds_spent_searching

  @property
  def token(self) -> str:
    return self._token or None

  @token.setter
  def token(self, token: Optional[str]):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def is_private(self) -> bool:
    return self._is_private or None

  @is_private.setter
  def is_private(self, is_private: Optional[bool]):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def client_events_session_id(self) -> str:
    r"""
    Browser session ID from ka_sessionid cookie to track search activity within
    a session.
    """
    return self._client_events_session_id or ""

  @client_events_session_id.setter
  def client_events_session_id(self, client_events_session_id: Optional[str]):
    if client_events_session_id is None:
      del self.client_events_session_id
      return
    if not isinstance(client_events_session_id, str):
      raise TypeError('client_events_session_id must be of type str')
    self._client_events_session_id = client_events_session_id


class ModelItemInfo(KaggleObject):
  r"""
  Attributes:
    notebook_count (int)
    subtitle (str)
    categories (TagList)
      The items below are used by the Input Selector in the kernel editor.
    instances (ModelInstance)
    full_url (str)
    owner (Owner)
    publish_time (datetime)
    slug (str)
    model_gating (ModelGating)
    user_consent_status (GatingAgreementRequestsReviewStatus)
  """

  def __init__(self):
    self._notebook_count = 0
    self._subtitle = ""
    self._categories = None
    self._instances = []
    self._full_url = None
    self._owner = None
    self._publish_time = None
    self._slug = None
    self._model_gating = None
    self._user_consent_status = None
    self._freeze()

  @property
  def notebook_count(self) -> int:
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count

  @property
  def subtitle(self) -> str:
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
  def categories(self) -> Optional['TagList']:
    """The items below are used by the Input Selector in the kernel editor."""
    return self._categories or None

  @categories.setter
  def categories(self, categories: Optional[Optional['TagList']]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, TagList):
      raise TypeError('categories must be of type TagList')
    self._categories = categories

  @property
  def instances(self) -> Optional[List[Optional['ModelInstance']]]:
    return self._instances

  @instances.setter
  def instances(self, instances: Optional[List[Optional['ModelInstance']]]):
    if instances is None:
      del self.instances
      return
    if not isinstance(instances, list):
      raise TypeError('instances must be of type list')
    if not all([isinstance(t, ModelInstance) for t in instances]):
      raise TypeError('instances must contain only items of type ModelInstance')
    self._instances = instances

  @property
  def full_url(self) -> str:
    return self._full_url or ""

  @full_url.setter
  def full_url(self, full_url: Optional[str]):
    if full_url is None:
      del self.full_url
      return
    if not isinstance(full_url, str):
      raise TypeError('full_url must be of type str')
    self._full_url = full_url

  @property
  def owner(self) -> Optional['Owner']:
    return self._owner or None

  @owner.setter
  def owner(self, owner: Optional[Optional['Owner']]):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, Owner):
      raise TypeError('owner must be of type Owner')
    self._owner = owner

  @property
  def publish_time(self) -> datetime:
    return self._publish_time or None

  @publish_time.setter
  def publish_time(self, publish_time: Optional[datetime]):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def slug(self) -> str:
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
  def model_gating(self) -> Optional['ModelGating']:
    return self._model_gating or None

  @model_gating.setter
  def model_gating(self, model_gating: Optional[Optional['ModelGating']]):
    if model_gating is None:
      del self.model_gating
      return
    if not isinstance(model_gating, ModelGating):
      raise TypeError('model_gating must be of type ModelGating')
    self._model_gating = model_gating

  @property
  def user_consent_status(self) -> 'GatingAgreementRequestsReviewStatus':
    return self._user_consent_status or GatingAgreementRequestsReviewStatus.GATING_AGREEMENT_REQUESTS_REVIEW_STATUS_UNSPECIFIED

  @user_consent_status.setter
  def user_consent_status(self, user_consent_status: Optional['GatingAgreementRequestsReviewStatus']):
    if user_consent_status is None:
      del self.user_consent_status
      return
    if not isinstance(user_consent_status, GatingAgreementRequestsReviewStatus):
      raise TypeError('user_consent_status must be of type GatingAgreementRequestsReviewStatus')
    self._user_consent_status = user_consent_status


class ModelsSearchFilter(KaggleObject):
  r"""
  TODO(253661181): according to AIP https://google.aip.dev/160,
    we should use strings for the entire filter object

  Attributes:
    tag_ids (int)
    framework (ModelFramework)
    search_query (str)
    owner_id (int)
    min_bytes (int)
    max_bytes (int)
    license (ModelLicense)
    fine_tunable (bool)
    organization_id (int)
    views (ModelView)
    min_usability_rating (float)
      not have access to CurrentUser context
    id (int)
    exclude_api_models (bool)
    is_writer_collaborator (bool)
    owner_type (ModelOwnerType)
    only_vertex_models (bool)
    is_admin_collaborator (bool)
    is_currently_featured (bool)
    is_previously_featured (bool)
  """

  def __init__(self):
    self._tag_ids = []
    self._framework = None
    self._search_query = None
    self._owner_id = None
    self._min_bytes = None
    self._max_bytes = None
    self._license = None
    self._fine_tunable = None
    self._organization_id = None
    self._views = []
    self._min_usability_rating = None
    self._id = []
    self._exclude_api_models = None
    self._is_writer_collaborator = None
    self._owner_type = None
    self._only_vertex_models = None
    self._is_admin_collaborator = None
    self._is_currently_featured = None
    self._is_previously_featured = None
    self._freeze()

  @property
  def tag_ids(self) -> Optional[List[int]]:
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
  def framework(self) -> 'ModelFramework':
    return self._framework or ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED

  @framework.setter
  def framework(self, framework: Optional['ModelFramework']):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def min_bytes(self) -> int:
    return self._min_bytes or 0

  @min_bytes.setter
  def min_bytes(self, min_bytes: Optional[int]):
    if min_bytes is None:
      del self.min_bytes
      return
    if not isinstance(min_bytes, int):
      raise TypeError('min_bytes must be of type int')
    self._min_bytes = min_bytes

  @property
  def max_bytes(self) -> int:
    return self._max_bytes or 0

  @max_bytes.setter
  def max_bytes(self, max_bytes: Optional[int]):
    if max_bytes is None:
      del self.max_bytes
      return
    if not isinstance(max_bytes, int):
      raise TypeError('max_bytes must be of type int')
    self._max_bytes = max_bytes

  @property
  def license(self) -> 'ModelLicense':
    return self._license or ModelLicense.UNSPECIFIED

  @license.setter
  def license(self, license: Optional['ModelLicense']):
    if license is None:
      del self.license
      return
    if not isinstance(license, ModelLicense):
      raise TypeError('license must be of type ModelLicense')
    self._license = license

  @property
  def fine_tunable(self) -> bool:
    return self._fine_tunable or False

  @fine_tunable.setter
  def fine_tunable(self, fine_tunable: Optional[bool]):
    if fine_tunable is None:
      del self.fine_tunable
      return
    if not isinstance(fine_tunable, bool):
      raise TypeError('fine_tunable must be of type bool')
    self._fine_tunable = fine_tunable

  @property
  def owner_id(self) -> int:
    return self._owner_id or 0

  @owner_id.setter
  def owner_id(self, owner_id: int):
    if owner_id is None:
      del self.owner_id
      return
    if not isinstance(owner_id, int):
      raise TypeError('owner_id must be of type int')
    del self.organization_id
    self._owner_id = owner_id

  @property
  def organization_id(self) -> int:
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    del self.owner_id
    self._organization_id = organization_id

  @property
  def views(self) -> Optional[List[Optional['ModelView']]]:
    return self._views

  @views.setter
  def views(self, views: Optional[List[Optional['ModelView']]]):
    if views is None:
      del self.views
      return
    if not isinstance(views, list):
      raise TypeError('views must be of type list')
    if not all([isinstance(t, ModelView) for t in views]):
      raise TypeError('views must contain only items of type ModelView')
    self._views = views

  @property
  def min_usability_rating(self) -> float:
    """not have access to CurrentUser context"""
    return self._min_usability_rating or 0.0

  @min_usability_rating.setter
  def min_usability_rating(self, min_usability_rating: Optional[float]):
    if min_usability_rating is None:
      del self.min_usability_rating
      return
    if not isinstance(min_usability_rating, float):
      raise TypeError('min_usability_rating must be of type float')
    self._min_usability_rating = min_usability_rating

  @property
  def id(self) -> Optional[List[int]]:
    return self._id

  @id.setter
  def id(self, id: Optional[List[int]]):
    if id is None:
      del self.id
      return
    if not isinstance(id, list):
      raise TypeError('id must be of type list')
    if not all([isinstance(t, int) for t in id]):
      raise TypeError('id must contain only items of type int')
    self._id = id

  @property
  def exclude_api_models(self) -> bool:
    return self._exclude_api_models or False

  @exclude_api_models.setter
  def exclude_api_models(self, exclude_api_models: Optional[bool]):
    if exclude_api_models is None:
      del self.exclude_api_models
      return
    if not isinstance(exclude_api_models, bool):
      raise TypeError('exclude_api_models must be of type bool')
    self._exclude_api_models = exclude_api_models

  @property
  def is_writer_collaborator(self) -> bool:
    return self._is_writer_collaborator or False

  @is_writer_collaborator.setter
  def is_writer_collaborator(self, is_writer_collaborator: Optional[bool]):
    if is_writer_collaborator is None:
      del self.is_writer_collaborator
      return
    if not isinstance(is_writer_collaborator, bool):
      raise TypeError('is_writer_collaborator must be of type bool')
    self._is_writer_collaborator = is_writer_collaborator

  @property
  def owner_type(self) -> 'ModelOwnerType':
    return self._owner_type or ModelOwnerType.MODEL_OWNER_TYPE_UNSPECIFIED

  @owner_type.setter
  def owner_type(self, owner_type: Optional['ModelOwnerType']):
    if owner_type is None:
      del self.owner_type
      return
    if not isinstance(owner_type, ModelOwnerType):
      raise TypeError('owner_type must be of type ModelOwnerType')
    self._owner_type = owner_type

  @property
  def only_vertex_models(self) -> bool:
    return self._only_vertex_models or False

  @only_vertex_models.setter
  def only_vertex_models(self, only_vertex_models: Optional[bool]):
    if only_vertex_models is None:
      del self.only_vertex_models
      return
    if not isinstance(only_vertex_models, bool):
      raise TypeError('only_vertex_models must be of type bool')
    self._only_vertex_models = only_vertex_models

  @property
  def is_admin_collaborator(self) -> bool:
    return self._is_admin_collaborator or False

  @is_admin_collaborator.setter
  def is_admin_collaborator(self, is_admin_collaborator: Optional[bool]):
    if is_admin_collaborator is None:
      del self.is_admin_collaborator
      return
    if not isinstance(is_admin_collaborator, bool):
      raise TypeError('is_admin_collaborator must be of type bool')
    self._is_admin_collaborator = is_admin_collaborator

  @property
  def is_currently_featured(self) -> bool:
    return self._is_currently_featured or False

  @is_currently_featured.setter
  def is_currently_featured(self, is_currently_featured: Optional[bool]):
    if is_currently_featured is None:
      del self.is_currently_featured
      return
    if not isinstance(is_currently_featured, bool):
      raise TypeError('is_currently_featured must be of type bool')
    self._is_currently_featured = is_currently_featured

  @property
  def is_previously_featured(self) -> bool:
    return self._is_previously_featured or False

  @is_previously_featured.setter
  def is_previously_featured(self, is_previously_featured: Optional[bool]):
    if is_previously_featured is None:
      del self.is_previously_featured
      return
    if not isinstance(is_previously_featured, bool):
      raise TypeError('is_previously_featured must be of type bool')
    self._is_previously_featured = is_previously_featured


class ModelView(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    view_time (datetime)
  """

  def __init__(self):
    self._model_id = 0
    self._view_time = None
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
  def view_time(self) -> datetime:
    return self._view_time

  @view_time.setter
  def view_time(self, view_time: datetime):
    if view_time is None:
      del self.view_time
      return
    if not isinstance(view_time, datetime):
      raise TypeError('view_time must be of type datetime')
    self._view_time = view_time


class OrganizationItemInfo(KaggleObject):
  r"""
  Attributes:
    location (str)
    dataset_count (int)
    competition_count (int)
    member_count (int)
  """

  def __init__(self):
    self._location = ""
    self._dataset_count = 0
    self._competition_count = 0
    self._member_count = 0
    self._freeze()

  @property
  def location(self) -> str:
    return self._location

  @location.setter
  def location(self, location: str):
    if location is None:
      del self.location
      return
    if not isinstance(location, str):
      raise TypeError('location must be of type str')
    self._location = location

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
  def member_count(self) -> int:
    return self._member_count

  @member_count.setter
  def member_count(self, member_count: int):
    if member_count is None:
      del self.member_count
      return
    if not isinstance(member_count, int):
      raise TypeError('member_count must be of type int')
    self._member_count = member_count


class ResourceReferenceItemInfo(KaggleObject):
  r"""
  Attributes:
    notebook_count (int)
    full_url (str)
    publish_time (datetime)
    slug (str)
  """

  def __init__(self):
    self._notebook_count = 0
    self._full_url = None
    self._publish_time = None
    self._slug = None
    self._freeze()

  @property
  def notebook_count(self) -> int:
    return self._notebook_count

  @notebook_count.setter
  def notebook_count(self, notebook_count: int):
    if notebook_count is None:
      del self.notebook_count
      return
    if not isinstance(notebook_count, int):
      raise TypeError('notebook_count must be of type int')
    self._notebook_count = notebook_count

  @property
  def full_url(self) -> str:
    return self._full_url or ""

  @full_url.setter
  def full_url(self, full_url: Optional[str]):
    if full_url is None:
      del self.full_url
      return
    if not isinstance(full_url, str):
      raise TypeError('full_url must be of type str')
    self._full_url = full_url

  @property
  def publish_time(self) -> datetime:
    return self._publish_time or None

  @publish_time.setter
  def publish_time(self, publish_time: Optional[datetime]):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug


class ResourceReferencesSearchFilter(KaggleObject):
  r"""
  Attributes:
    type (ResourceReferenceType)
    owner_identifier (str)
    search_query (str)
    ids (int)
    content_state (ContentState)
  """

  def __init__(self):
    self._type = ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED
    self._owner_identifier = None
    self._search_query = None
    self._ids = []
    self._content_state = None
    self._freeze()

  @property
  def type(self) -> 'ResourceReferenceType':
    return self._type

  @type.setter
  def type(self, type: 'ResourceReferenceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ResourceReferenceType):
      raise TypeError('type must be of type ResourceReferenceType')
    self._type = type

  @property
  def owner_identifier(self) -> str:
    return self._owner_identifier or ""

  @owner_identifier.setter
  def owner_identifier(self, owner_identifier: Optional[str]):
    if owner_identifier is None:
      del self.owner_identifier
      return
    if not isinstance(owner_identifier, str):
      raise TypeError('owner_identifier must be of type str')
    self._owner_identifier = owner_identifier

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids

  @property
  def content_state(self) -> 'ContentState':
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state


class SearchFilter(KaggleObject):
  r"""
  Attributes:
    name (FilterName)
    type (FilterType)
    options (FilterOption)
    categories (DocumentType)
  """

  def __init__(self):
    self._name = FilterName.DATE
    self._type = FilterType.RADIO
    self._options = []
    self._categories = []
    self._freeze()

  @property
  def name(self) -> 'FilterName':
    return self._name

  @name.setter
  def name(self, name: 'FilterName'):
    if name is None:
      del self.name
      return
    if not isinstance(name, FilterName):
      raise TypeError('name must be of type FilterName')
    self._name = name

  @property
  def type(self) -> 'FilterType':
    return self._type

  @type.setter
  def type(self, type: 'FilterType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, FilterType):
      raise TypeError('type must be of type FilterType')
    self._type = type

  @property
  def options(self) -> Optional[List[Optional['FilterOption']]]:
    return self._options

  @options.setter
  def options(self, options: Optional[List[Optional['FilterOption']]]):
    if options is None:
      del self.options
      return
    if not isinstance(options, list):
      raise TypeError('options must be of type list')
    if not all([isinstance(t, FilterOption) for t in options]):
      raise TypeError('options must contain only items of type FilterOption')
    self._options = options

  @property
  def categories(self) -> Optional[List['DocumentType']]:
    return self._categories

  @categories.setter
  def categories(self, categories: Optional[List['DocumentType']]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, list):
      raise TypeError('categories must be of type list')
    if not all([isinstance(t, DocumentType) for t in categories]):
      raise TypeError('categories must contain only items of type DocumentType')
    self._categories = categories


class SearchItem(KaggleObject):
  r"""
  Attributes:
    id (str)
    document_type (DocumentType)
    database_id (int)
    title (str)
    url (str)
    thumbnail_image_url (str)
    rank (int)
    score (float)
    is_private (bool)
    votes (int)
    date (datetime)
    author_slug (str)
    comment_info (CommentItemInfo)
    competition_info (CompetitionItemInfo)
    dataset_info (DatasetItemInfo)
    kernel_info (KernelItemInfo)
    topic_info (TopicItemInfo)
    user_info (UserItemInfo)
    author_display_name (str)
    organization_info (OrganizationItemInfo)
    matched_text (str)
    is_created_by_current_user (bool)
    model_info (ModelItemInfo)
    course_info (CourseItemInfo)
    tutorial_info (TutorialItemInfo)
    author_tier (UserAchievementTier)
    resource_reference_info (ResourceReferenceItemInfo)
    author_progression_opt_out (bool)
    benchmark_info (BenchmarkItemInfo)
    benchmark_task_info (BenchmarkTaskItemInfo)
  """

  def __init__(self):
    self._id = ""
    self._document_type = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._database_id = 0
    self._title = ""
    self._url = ""
    self._thumbnail_image_url = ""
    self._rank = 0
    self._score = 0.0
    self._is_private = False
    self._votes = 0
    self._date = None
    self._author_slug = ""
    self._comment_info = None
    self._competition_info = None
    self._dataset_info = None
    self._kernel_info = None
    self._topic_info = None
    self._user_info = None
    self._author_display_name = ""
    self._organization_info = None
    self._matched_text = ""
    self._is_created_by_current_user = False
    self._model_info = None
    self._course_info = None
    self._tutorial_info = None
    self._author_tier = None
    self._resource_reference_info = None
    self._author_progression_opt_out = False
    self._benchmark_info = None
    self._benchmark_task_info = None
    self._freeze()

  @property
  def id(self) -> str:
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def document_type(self) -> 'DocumentType':
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
  def database_id(self) -> int:
    return self._database_id

  @database_id.setter
  def database_id(self, database_id: int):
    if database_id is None:
      del self.database_id
      return
    if not isinstance(database_id, int):
      raise TypeError('database_id must be of type int')
    self._database_id = database_id

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
  def rank(self) -> int:
    return self._rank

  @rank.setter
  def rank(self, rank: int):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

  @property
  def score(self) -> float:
    return self._score

  @score.setter
  def score(self, score: float):
    if score is None:
      del self.score
      return
    if not isinstance(score, float):
      raise TypeError('score must be of type float')
    self._score = score

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def votes(self) -> int:
    return self._votes

  @votes.setter
  def votes(self, votes: int):
    if votes is None:
      del self.votes
      return
    if not isinstance(votes, int):
      raise TypeError('votes must be of type int')
    self._votes = votes

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
  def author_slug(self) -> str:
    return self._author_slug

  @author_slug.setter
  def author_slug(self, author_slug: str):
    if author_slug is None:
      del self.author_slug
      return
    if not isinstance(author_slug, str):
      raise TypeError('author_slug must be of type str')
    self._author_slug = author_slug

  @property
  def author_display_name(self) -> str:
    return self._author_display_name

  @author_display_name.setter
  def author_display_name(self, author_display_name: str):
    if author_display_name is None:
      del self.author_display_name
      return
    if not isinstance(author_display_name, str):
      raise TypeError('author_display_name must be of type str')
    self._author_display_name = author_display_name

  @property
  def author_tier(self) -> 'UserAchievementTier':
    return self._author_tier or UserAchievementTier.NOVICE

  @author_tier.setter
  def author_tier(self, author_tier: Optional['UserAchievementTier']):
    if author_tier is None:
      del self.author_tier
      return
    if not isinstance(author_tier, UserAchievementTier):
      raise TypeError('author_tier must be of type UserAchievementTier')
    self._author_tier = author_tier

  @property
  def author_progression_opt_out(self) -> bool:
    return self._author_progression_opt_out

  @author_progression_opt_out.setter
  def author_progression_opt_out(self, author_progression_opt_out: bool):
    if author_progression_opt_out is None:
      del self.author_progression_opt_out
      return
    if not isinstance(author_progression_opt_out, bool):
      raise TypeError('author_progression_opt_out must be of type bool')
    self._author_progression_opt_out = author_progression_opt_out

  @property
  def comment_info(self) -> Optional['CommentItemInfo']:
    return self._comment_info or None

  @comment_info.setter
  def comment_info(self, comment_info: Optional['CommentItemInfo']):
    if comment_info is None:
      del self.comment_info
      return
    if not isinstance(comment_info, CommentItemInfo):
      raise TypeError('comment_info must be of type CommentItemInfo')
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._comment_info = comment_info

  @property
  def competition_info(self) -> Optional['CompetitionItemInfo']:
    return self._competition_info or None

  @competition_info.setter
  def competition_info(self, competition_info: Optional['CompetitionItemInfo']):
    if competition_info is None:
      del self.competition_info
      return
    if not isinstance(competition_info, CompetitionItemInfo):
      raise TypeError('competition_info must be of type CompetitionItemInfo')
    del self.comment_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._competition_info = competition_info

  @property
  def dataset_info(self) -> Optional['DatasetItemInfo']:
    return self._dataset_info or None

  @dataset_info.setter
  def dataset_info(self, dataset_info: Optional['DatasetItemInfo']):
    if dataset_info is None:
      del self.dataset_info
      return
    if not isinstance(dataset_info, DatasetItemInfo):
      raise TypeError('dataset_info must be of type DatasetItemInfo')
    del self.comment_info
    del self.competition_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._dataset_info = dataset_info

  @property
  def kernel_info(self) -> Optional['KernelItemInfo']:
    return self._kernel_info or None

  @kernel_info.setter
  def kernel_info(self, kernel_info: Optional['KernelItemInfo']):
    if kernel_info is None:
      del self.kernel_info
      return
    if not isinstance(kernel_info, KernelItemInfo):
      raise TypeError('kernel_info must be of type KernelItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._kernel_info = kernel_info

  @property
  def topic_info(self) -> Optional['TopicItemInfo']:
    return self._topic_info or None

  @topic_info.setter
  def topic_info(self, topic_info: Optional['TopicItemInfo']):
    if topic_info is None:
      del self.topic_info
      return
    if not isinstance(topic_info, TopicItemInfo):
      raise TypeError('topic_info must be of type TopicItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._topic_info = topic_info

  @property
  def user_info(self) -> Optional['UserItemInfo']:
    return self._user_info or None

  @user_info.setter
  def user_info(self, user_info: Optional['UserItemInfo']):
    if user_info is None:
      del self.user_info
      return
    if not isinstance(user_info, UserItemInfo):
      raise TypeError('user_info must be of type UserItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._user_info = user_info

  @property
  def organization_info(self) -> Optional['OrganizationItemInfo']:
    return self._organization_info or None

  @organization_info.setter
  def organization_info(self, organization_info: Optional['OrganizationItemInfo']):
    if organization_info is None:
      del self.organization_info
      return
    if not isinstance(organization_info, OrganizationItemInfo):
      raise TypeError('organization_info must be of type OrganizationItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._organization_info = organization_info

  @property
  def model_info(self) -> Optional['ModelItemInfo']:
    return self._model_info or None

  @model_info.setter
  def model_info(self, model_info: Optional['ModelItemInfo']):
    if model_info is None:
      del self.model_info
      return
    if not isinstance(model_info, ModelItemInfo):
      raise TypeError('model_info must be of type ModelItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._model_info = model_info

  @property
  def course_info(self) -> Optional['CourseItemInfo']:
    return self._course_info or None

  @course_info.setter
  def course_info(self, course_info: Optional['CourseItemInfo']):
    if course_info is None:
      del self.course_info
      return
    if not isinstance(course_info, CourseItemInfo):
      raise TypeError('course_info must be of type CourseItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._course_info = course_info

  @property
  def tutorial_info(self) -> Optional['TutorialItemInfo']:
    return self._tutorial_info or None

  @tutorial_info.setter
  def tutorial_info(self, tutorial_info: Optional['TutorialItemInfo']):
    if tutorial_info is None:
      del self.tutorial_info
      return
    if not isinstance(tutorial_info, TutorialItemInfo):
      raise TypeError('tutorial_info must be of type TutorialItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.resource_reference_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._tutorial_info = tutorial_info

  @property
  def resource_reference_info(self) -> Optional['ResourceReferenceItemInfo']:
    return self._resource_reference_info or None

  @resource_reference_info.setter
  def resource_reference_info(self, resource_reference_info: Optional['ResourceReferenceItemInfo']):
    if resource_reference_info is None:
      del self.resource_reference_info
      return
    if not isinstance(resource_reference_info, ResourceReferenceItemInfo):
      raise TypeError('resource_reference_info must be of type ResourceReferenceItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.benchmark_info
    del self.benchmark_task_info
    self._resource_reference_info = resource_reference_info

  @property
  def benchmark_info(self) -> Optional['BenchmarkItemInfo']:
    return self._benchmark_info or None

  @benchmark_info.setter
  def benchmark_info(self, benchmark_info: Optional['BenchmarkItemInfo']):
    if benchmark_info is None:
      del self.benchmark_info
      return
    if not isinstance(benchmark_info, BenchmarkItemInfo):
      raise TypeError('benchmark_info must be of type BenchmarkItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_task_info
    self._benchmark_info = benchmark_info

  @property
  def benchmark_task_info(self) -> Optional['BenchmarkTaskItemInfo']:
    return self._benchmark_task_info or None

  @benchmark_task_info.setter
  def benchmark_task_info(self, benchmark_task_info: Optional['BenchmarkTaskItemInfo']):
    if benchmark_task_info is None:
      del self.benchmark_task_info
      return
    if not isinstance(benchmark_task_info, BenchmarkTaskItemInfo):
      raise TypeError('benchmark_task_info must be of type BenchmarkTaskItemInfo')
    del self.comment_info
    del self.competition_info
    del self.dataset_info
    del self.kernel_info
    del self.topic_info
    del self.user_info
    del self.organization_info
    del self.model_info
    del self.course_info
    del self.tutorial_info
    del self.resource_reference_info
    del self.benchmark_info
    self._benchmark_task_info = benchmark_task_info

  @property
  def matched_text(self) -> str:
    return self._matched_text

  @matched_text.setter
  def matched_text(self, matched_text: str):
    if matched_text is None:
      del self.matched_text
      return
    if not isinstance(matched_text, str):
      raise TypeError('matched_text must be of type str')
    self._matched_text = matched_text

  @property
  def is_created_by_current_user(self) -> bool:
    return self._is_created_by_current_user

  @is_created_by_current_user.setter
  def is_created_by_current_user(self, is_created_by_current_user: bool):
    if is_created_by_current_user is None:
      del self.is_created_by_current_user
      return
    if not isinstance(is_created_by_current_user, bool):
      raise TypeError('is_created_by_current_user must be of type bool')
    self._is_created_by_current_user = is_created_by_current_user


class SearchResultGroup(KaggleObject):
  r"""
  Attributes:
    documents (SearchItem)
    type (DocumentType)
    count (int)
  """

  def __init__(self):
    self._documents = []
    self._type = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._count = 0
    self._freeze()

  @property
  def documents(self) -> Optional[List[Optional['SearchItem']]]:
    return self._documents

  @documents.setter
  def documents(self, documents: Optional[List[Optional['SearchItem']]]):
    if documents is None:
      del self.documents
      return
    if not isinstance(documents, list):
      raise TypeError('documents must be of type list')
    if not all([isinstance(t, SearchItem) for t in documents]):
      raise TypeError('documents must contain only items of type SearchItem')
    self._documents = documents

  @property
  def type(self) -> 'DocumentType':
    return self._type

  @type.setter
  def type(self, type: 'DocumentType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DocumentType):
      raise TypeError('type must be of type DocumentType')
    self._type = type

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class SuggestedSearchResponse(KaggleObject):
  r"""
  Attributes:
    groups (SearchResultGroup)
  """

  def __init__(self):
    self._groups = []
    self._freeze()

  @property
  def groups(self) -> Optional[List[Optional['SearchResultGroup']]]:
    return self._groups

  @groups.setter
  def groups(self, groups: Optional[List[Optional['SearchResultGroup']]]):
    if groups is None:
      del self.groups
      return
    if not isinstance(groups, list):
      raise TypeError('groups must be of type list')
    if not all([isinstance(t, SearchResultGroup) for t in groups]):
      raise TypeError('groups must contain only items of type SearchResultGroup')
    self._groups = groups


class SuggestedSearchWebRequest(KaggleObject):
  r"""
  Attributes:
    query (str)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
  """

  def __init__(self):
    self._query = None
    self._freeze()

  @property
  def query(self) -> str:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._query or None

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query


class TopicItemInfo(KaggleObject):
  r"""
  Attributes:
    forum_name (str)
    forum_url (str)
    total_comments (int)
    is_write_up (bool)
      TODO(b/432302801): Remove is_write_up and prefer using write_up_info
    write_up_info (WriteUpItemInfo)
  """

  def __init__(self):
    self._forum_name = ""
    self._forum_url = ""
    self._total_comments = 0
    self._is_write_up = False
    self._write_up_info = None
    self._freeze()

  @property
  def forum_name(self) -> str:
    return self._forum_name

  @forum_name.setter
  def forum_name(self, forum_name: str):
    if forum_name is None:
      del self.forum_name
      return
    if not isinstance(forum_name, str):
      raise TypeError('forum_name must be of type str')
    self._forum_name = forum_name

  @property
  def forum_url(self) -> str:
    return self._forum_url

  @forum_url.setter
  def forum_url(self, forum_url: str):
    if forum_url is None:
      del self.forum_url
      return
    if not isinstance(forum_url, str):
      raise TypeError('forum_url must be of type str')
    self._forum_url = forum_url

  @property
  def total_comments(self) -> int:
    return self._total_comments

  @total_comments.setter
  def total_comments(self, total_comments: int):
    if total_comments is None:
      del self.total_comments
      return
    if not isinstance(total_comments, int):
      raise TypeError('total_comments must be of type int')
    self._total_comments = total_comments

  @property
  def is_write_up(self) -> bool:
    """TODO(b/432302801): Remove is_write_up and prefer using write_up_info"""
    return self._is_write_up

  @is_write_up.setter
  def is_write_up(self, is_write_up: bool):
    if is_write_up is None:
      del self.is_write_up
      return
    if not isinstance(is_write_up, bool):
      raise TypeError('is_write_up must be of type bool')
    self._is_write_up = is_write_up

  @property
  def write_up_info(self) -> Optional['WriteUpItemInfo']:
    return self._write_up_info or None

  @write_up_info.setter
  def write_up_info(self, write_up_info: Optional[Optional['WriteUpItemInfo']]):
    if write_up_info is None:
      del self.write_up_info
      return
    if not isinstance(write_up_info, WriteUpItemInfo):
      raise TypeError('write_up_info must be of type WriteUpItemInfo')
    self._write_up_info = write_up_info


class TutorialItemInfo(KaggleObject):
  r"""
  Attributes:
    track_name (str)
    track_url (str)
    exercise_description (str)
  """

  def __init__(self):
    self._track_name = ""
    self._track_url = ""
    self._exercise_description = ""
    self._freeze()

  @property
  def track_name(self) -> str:
    return self._track_name

  @track_name.setter
  def track_name(self, track_name: str):
    if track_name is None:
      del self.track_name
      return
    if not isinstance(track_name, str):
      raise TypeError('track_name must be of type str')
    self._track_name = track_name

  @property
  def track_url(self) -> str:
    return self._track_url

  @track_url.setter
  def track_url(self, track_url: str):
    if track_url is None:
      del self.track_url
      return
    if not isinstance(track_url, str):
      raise TypeError('track_url must be of type str')
    self._track_url = track_url

  @property
  def exercise_description(self) -> str:
    return self._exercise_description

  @exercise_description.setter
  def exercise_description(self, exercise_description: str):
    if exercise_description is None:
      del self.exercise_description
      return
    if not isinstance(exercise_description, str):
      raise TypeError('exercise_description must be of type str')
    self._exercise_description = exercise_description


class UserItemInfo(KaggleObject):
  r"""
  Attributes:
    location (str)
    register_date (datetime)
    job (str)
  """

  def __init__(self):
    self._location = ""
    self._register_date = None
    self._job = ""
    self._freeze()

  @property
  def location(self) -> str:
    return self._location

  @location.setter
  def location(self, location: str):
    if location is None:
      del self.location
      return
    if not isinstance(location, str):
      raise TypeError('location must be of type str')
    self._location = location

  @property
  def register_date(self) -> datetime:
    return self._register_date

  @register_date.setter
  def register_date(self, register_date: datetime):
    if register_date is None:
      del self.register_date
      return
    if not isinstance(register_date, datetime):
      raise TypeError('register_date must be of type datetime')
    self._register_date = register_date

  @property
  def job(self) -> str:
    return self._job

  @job.setter
  def job(self, job: str):
    if job is None:
      del self.job
      return
    if not isinstance(job, str):
      raise TypeError('job must be of type str')
    self._job = job


class WriteUpCompetitionInfo(KaggleObject):
  r"""
  Attributes:
    competition_title (str)
      Title of the Competition or Hackathon
    competition_url (str)
      Url of the Competition or Hackathon
    deadline (datetime)
      Deadline of the Competition or Hackathon
    write_up_leaderboard_rank (int)
      Rank of Competition Solution WriteUp on Leaderboard
    leaderboard_url (str)
      Leaderboard Tab Url for Competition
    winners_url (str)
      Winners Tab Url of Hackathon
    is_hackathon_winner (bool)
      Boolean to tell if user's WriteUp is winner of Hackathon
    competition_id (int)
      Id of the Competition
  """

  def __init__(self):
    self._competition_title = ""
    self._competition_url = ""
    self._deadline = None
    self._write_up_leaderboard_rank = None
    self._leaderboard_url = None
    self._winners_url = None
    self._is_hackathon_winner = None
    self._competition_id = 0
    self._freeze()

  @property
  def competition_title(self) -> str:
    """Title of the Competition or Hackathon"""
    return self._competition_title

  @competition_title.setter
  def competition_title(self, competition_title: str):
    if competition_title is None:
      del self.competition_title
      return
    if not isinstance(competition_title, str):
      raise TypeError('competition_title must be of type str')
    self._competition_title = competition_title

  @property
  def competition_url(self) -> str:
    """Url of the Competition or Hackathon"""
    return self._competition_url

  @competition_url.setter
  def competition_url(self, competition_url: str):
    if competition_url is None:
      del self.competition_url
      return
    if not isinstance(competition_url, str):
      raise TypeError('competition_url must be of type str')
    self._competition_url = competition_url

  @property
  def deadline(self) -> datetime:
    """Deadline of the Competition or Hackathon"""
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline

  @property
  def write_up_leaderboard_rank(self) -> int:
    """Rank of Competition Solution WriteUp on Leaderboard"""
    return self._write_up_leaderboard_rank or 0

  @write_up_leaderboard_rank.setter
  def write_up_leaderboard_rank(self, write_up_leaderboard_rank: Optional[int]):
    if write_up_leaderboard_rank is None:
      del self.write_up_leaderboard_rank
      return
    if not isinstance(write_up_leaderboard_rank, int):
      raise TypeError('write_up_leaderboard_rank must be of type int')
    self._write_up_leaderboard_rank = write_up_leaderboard_rank

  @property
  def leaderboard_url(self) -> str:
    """Leaderboard Tab Url for Competition"""
    return self._leaderboard_url or ""

  @leaderboard_url.setter
  def leaderboard_url(self, leaderboard_url: Optional[str]):
    if leaderboard_url is None:
      del self.leaderboard_url
      return
    if not isinstance(leaderboard_url, str):
      raise TypeError('leaderboard_url must be of type str')
    self._leaderboard_url = leaderboard_url

  @property
  def winners_url(self) -> str:
    """Winners Tab Url of Hackathon"""
    return self._winners_url or ""

  @winners_url.setter
  def winners_url(self, winners_url: Optional[str]):
    if winners_url is None:
      del self.winners_url
      return
    if not isinstance(winners_url, str):
      raise TypeError('winners_url must be of type str')
    self._winners_url = winners_url

  @property
  def is_hackathon_winner(self) -> bool:
    """Boolean to tell if user's WriteUp is winner of Hackathon"""
    return self._is_hackathon_winner or False

  @is_hackathon_winner.setter
  def is_hackathon_winner(self, is_hackathon_winner: Optional[bool]):
    if is_hackathon_winner is None:
      del self.is_hackathon_winner
      return
    if not isinstance(is_hackathon_winner, bool):
      raise TypeError('is_hackathon_winner must be of type bool')
    self._is_hackathon_winner = is_hackathon_winner

  @property
  def competition_id(self) -> int:
    """Id of the Competition"""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class WriteUpItemInfo(KaggleObject):
  r"""
  Attributes:
    type (WriteUpType)
      Type of WriteUp
    subtitle (str)
      Subtitle of WriteUp
    collaborators (UserAvatar)
      List of WriteUp collaborators
    competition_info (WriteUpCompetitionInfo)
      Competition metadata associated with WriteUp
    content_state (ContentState)
      Content State of WriteUp
    team_name (str)
      Name of the team that owns the WriteUp
    id (int)
      Id of the WriteUp
    hackathon_track_ids (int)
      The track ids of the Hackathon
  """

  def __init__(self):
    self._type = WriteUpType.WRITE_UP_TYPE_UNSPECIFIED
    self._subtitle = None
    self._collaborators = []
    self._competition_info = None
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._team_name = None
    self._id = 0
    self._hackathon_track_ids = []
    self._freeze()

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
  def subtitle(self) -> str:
    """Subtitle of WriteUp"""
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
  def collaborators(self) -> Optional[List[Optional['UserAvatar']]]:
    """List of WriteUp collaborators"""
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
  def competition_info(self) -> Optional['WriteUpCompetitionInfo']:
    """Competition metadata associated with WriteUp"""
    return self._competition_info or None

  @competition_info.setter
  def competition_info(self, competition_info: Optional[Optional['WriteUpCompetitionInfo']]):
    if competition_info is None:
      del self.competition_info
      return
    if not isinstance(competition_info, WriteUpCompetitionInfo):
      raise TypeError('competition_info must be of type WriteUpCompetitionInfo')
    self._competition_info = competition_info

  @property
  def content_state(self) -> 'ContentState':
    """Content State of WriteUp"""
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
  def team_name(self) -> str:
    """Name of the team that owns the WriteUp"""
    return self._team_name or ""

  @team_name.setter
  def team_name(self, team_name: Optional[str]):
    if team_name is None:
      del self.team_name
      return
    if not isinstance(team_name, str):
      raise TypeError('team_name must be of type str')
    self._team_name = team_name

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
  def hackathon_track_ids(self) -> Optional[List[int]]:
    """The track ids of the Hackathon"""
    return self._hackathon_track_ids

  @hackathon_track_ids.setter
  def hackathon_track_ids(self, hackathon_track_ids: Optional[List[int]]):
    if hackathon_track_ids is None:
      del self.hackathon_track_ids
      return
    if not isinstance(hackathon_track_ids, list):
      raise TypeError('hackathon_track_ids must be of type list')
    if not all([isinstance(t, int) for t in hackathon_track_ids]):
      raise TypeError('hackathon_track_ids must contain only items of type int')
    self._hackathon_track_ids = hackathon_track_ids


BenchmarkItemInfo._fields = [
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkType, BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED, EnumSerializer()),
]

BenchmarkTaskItemInfo._fields = [
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
]

BenchmarkTasksSearchFilter._fields = [
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
]

CategoryFilter._fields = [
  FieldMetadata("name", "name", "_name", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

CommentItemInfo._fields = [
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("topicUrl", "topic_url", "_topic_url", str, "", PredefinedSerializer()),
  FieldMetadata("totalReplies", "total_replies", "_total_replies", int, 0, PredefinedSerializer()),
]

CompetitionItemInfo._fields = [
  FieldMetadata("teamsCount", "teams_count", "_teams_count", int, 0, PredefinedSerializer()),
  FieldMetadata("deadlineDate", "deadline_date", "_deadline_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("prizeValue", "prize_value", "_prize_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("hostName", "host_name", "_host_name", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
]

CourseItemInfo._fields = [
  FieldMetadata("estimatedHours", "estimated_hours", "_estimated_hours", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
]

DatasetItemInfo._fields = [
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
  FieldMetadata("fileTypes", "file_types", "_file_types", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("currentDatasetVersionId", "current_dataset_version_id", "_current_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("totalDownloads", "total_downloads", "_total_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
]

FilterOption._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

FullSearchResponse._fields = [
  FieldMetadata("documents", "documents", "_documents", SearchItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("filters", "filters", "_filters", SearchFilter, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("categories", "categories", "_categories", CategoryFilter, [], ListSerializer(KaggleObjectSerializer())),
]

FullSearchWebRequest._fields = [
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("resultsPerPage", "results_per_page", "_results_per_page", int, 0, PredefinedSerializer()),
  FieldMetadata("showPrivate", "show_private", "_show_private", bool, False, PredefinedSerializer()),
]

GetAutoCompleteSuggestionsRequest._fields = [
  FieldMetadata("prefix", "prefix", "_prefix", str, "", PredefinedSerializer()),
]

GetAutoCompleteSuggestionsResponse._fields = [
  FieldMetadata("autoCompleteSuggestions", "auto_complete_suggestions", "_auto_complete_suggestions", str, [], ListSerializer(PredefinedSerializer())),
]

GetPopularTagsRequest._fields = []

GetPopularTagsResponse._fields = [
  FieldMetadata("popularTags", "popular_tags", "_popular_tags", FilterOption, [], ListSerializer(KaggleObjectSerializer())),
]

GetRecentSearchesRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("specificSearchIndices", "specific_search_indices", "_specific_search_indices", SearchIndex, [], ListSerializer(EnumSerializer())),
]

GetRecentSearchesResponse._fields = [
  FieldMetadata("recentSearches", "recent_searches", "_recent_searches", str, [], ListSerializer(PredefinedSerializer())),
]

GetTrendingSearchesRequest._fields = []

GetTrendingSearchesResponse._fields = [
  FieldMetadata("trendingSearches", "trending_searches", "_trending_searches", str, [], ListSerializer(PredefinedSerializer())),
]

KernelItemInfo._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hasDataOutputFiles", "has_data_output_files", "_has_data_output_files", bool, False, PredefinedSerializer()),
  FieldMetadata("isUtilityScript", "is_utility_script", "_is_utility_script", bool, False, PredefinedSerializer()),
  FieldMetadata("hasCollaborators", "has_collaborators", "_has_collaborators", bool, False, PredefinedSerializer()),
  FieldMetadata("totalComments", "total_comments", "_total_comments", int, 0, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSource, [], ListSerializer(KaggleObjectSerializer())),
]

LogSearchRequest._fields = [
  FieldMetadata("index", "index", "_index", str, "", PredefinedSerializer()),
  FieldMetadata("isQuick", "is_quick", "_is_quick", bool, False, PredefinedSerializer()),
  FieldMetadata("query", "query", "_query", str, "", PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secondsSpentSearching", "seconds_spent_searching", "_seconds_spent_searching", float, 0.0, PredefinedSerializer()),
  FieldMetadata("token", "token", "_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("clientEventsSessionId", "client_events_session_id", "_client_events_session_id", str, None, PredefinedSerializer(), optional=True),
]

ModelItemInfo._fields = [
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, "", PredefinedSerializer()),
  FieldMetadata("categories", "categories", "_categories", TagList, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("instances", "instances", "_instances", ModelInstance, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("fullUrl", "full_url", "_full_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("owner", "owner", "_owner", Owner, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelGating", "model_gating", "_model_gating", ModelGating, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userConsentStatus", "user_consent_status", "_user_consent_status", GatingAgreementRequestsReviewStatus, None, EnumSerializer(), optional=True),
]

ModelsSearchFilter._fields = [
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, None, EnumSerializer(), optional=True),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerId", "owner_id", "_owner_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("minBytes", "min_bytes", "_min_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxBytes", "max_bytes", "_max_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("license", "license", "_license", ModelLicense, None, EnumSerializer(), optional=True),
  FieldMetadata("fineTunable", "fine_tunable", "_fine_tunable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("views", "views", "_views", ModelView, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("minUsabilityRating", "min_usability_rating", "_min_usability_rating", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("excludeApiModels", "exclude_api_models", "_exclude_api_models", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isWriterCollaborator", "is_writer_collaborator", "_is_writer_collaborator", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerType", "owner_type", "_owner_type", ModelOwnerType, None, EnumSerializer(), optional=True),
  FieldMetadata("onlyVertexModels", "only_vertex_models", "_only_vertex_models", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isAdminCollaborator", "is_admin_collaborator", "_is_admin_collaborator", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isCurrentlyFeatured", "is_currently_featured", "_is_currently_featured", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPreviouslyFeatured", "is_previously_featured", "_is_previously_featured", bool, None, PredefinedSerializer(), optional=True),
]

ModelView._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("viewTime", "view_time", "_view_time", datetime, None, DateTimeSerializer()),
]

OrganizationItemInfo._fields = [
  FieldMetadata("location", "location", "_location", str, "", PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("memberCount", "member_count", "_member_count", int, 0, PredefinedSerializer()),
]

ResourceReferenceItemInfo._fields = [
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
  FieldMetadata("fullUrl", "full_url", "_full_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
]

ResourceReferencesSearchFilter._fields = [
  FieldMetadata("type", "type", "_type", ResourceReferenceType, ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerIdentifier", "owner_identifier", "_owner_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
]

SearchFilter._fields = [
  FieldMetadata("name", "name", "_name", FilterName, FilterName.DATE, EnumSerializer()),
  FieldMetadata("type", "type", "_type", FilterType, FilterType.RADIO, EnumSerializer()),
  FieldMetadata("options", "options", "_options", FilterOption, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("categories", "categories", "_categories", DocumentType, [], ListSerializer(EnumSerializer())),
]

SearchItem._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
  FieldMetadata("documentType", "document_type", "_document_type", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("databaseId", "database_id", "_database_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, 0, PredefinedSerializer()),
  FieldMetadata("score", "score", "_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("votes", "votes", "_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("authorSlug", "author_slug", "_author_slug", str, "", PredefinedSerializer()),
  FieldMetadata("commentInfo", "comment_info", "_comment_info", CommentItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competitionInfo", "competition_info", "_competition_info", CompetitionItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("datasetInfo", "dataset_info", "_dataset_info", DatasetItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelInfo", "kernel_info", "_kernel_info", KernelItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("topicInfo", "topic_info", "_topic_info", TopicItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("userInfo", "user_info", "_user_info", UserItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authorDisplayName", "author_display_name", "_author_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("organizationInfo", "organization_info", "_organization_info", OrganizationItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("matchedText", "matched_text", "_matched_text", str, "", PredefinedSerializer()),
  FieldMetadata("isCreatedByCurrentUser", "is_created_by_current_user", "_is_created_by_current_user", bool, False, PredefinedSerializer()),
  FieldMetadata("modelInfo", "model_info", "_model_info", ModelItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("courseInfo", "course_info", "_course_info", CourseItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("tutorialInfo", "tutorial_info", "_tutorial_info", TutorialItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authorTier", "author_tier", "_author_tier", UserAchievementTier, None, EnumSerializer(), optional=True),
  FieldMetadata("resourceReferenceInfo", "resource_reference_info", "_resource_reference_info", ResourceReferenceItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("authorProgressionOptOut", "author_progression_opt_out", "_author_progression_opt_out", bool, False, PredefinedSerializer()),
  FieldMetadata("benchmarkInfo", "benchmark_info", "_benchmark_info", BenchmarkItemInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkTaskInfo", "benchmark_task_info", "_benchmark_task_info", BenchmarkTaskItemInfo, None, KaggleObjectSerializer(), optional=True),
]

SearchResultGroup._fields = [
  FieldMetadata("documents", "documents", "_documents", SearchItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("type", "type", "_type", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

SuggestedSearchResponse._fields = [
  FieldMetadata("groups", "groups", "_groups", SearchResultGroup, [], ListSerializer(KaggleObjectSerializer())),
]

SuggestedSearchWebRequest._fields = [
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
]

TopicItemInfo._fields = [
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("forumUrl", "forum_url", "_forum_url", str, "", PredefinedSerializer()),
  FieldMetadata("totalComments", "total_comments", "_total_comments", int, 0, PredefinedSerializer()),
  FieldMetadata("isWriteUp", "is_write_up", "_is_write_up", bool, False, PredefinedSerializer()),
  FieldMetadata("writeUpInfo", "write_up_info", "_write_up_info", WriteUpItemInfo, None, KaggleObjectSerializer(), optional=True),
]

TutorialItemInfo._fields = [
  FieldMetadata("trackName", "track_name", "_track_name", str, "", PredefinedSerializer()),
  FieldMetadata("trackUrl", "track_url", "_track_url", str, "", PredefinedSerializer()),
  FieldMetadata("exerciseDescription", "exercise_description", "_exercise_description", str, "", PredefinedSerializer()),
]

UserItemInfo._fields = [
  FieldMetadata("location", "location", "_location", str, "", PredefinedSerializer()),
  FieldMetadata("registerDate", "register_date", "_register_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("job", "job", "_job", str, "", PredefinedSerializer()),
]

WriteUpCompetitionInfo._fields = [
  FieldMetadata("competitionTitle", "competition_title", "_competition_title", str, "", PredefinedSerializer()),
  FieldMetadata("competitionUrl", "competition_url", "_competition_url", str, "", PredefinedSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("writeUpLeaderboardRank", "write_up_leaderboard_rank", "_write_up_leaderboard_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("leaderboardUrl", "leaderboard_url", "_leaderboard_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("winnersUrl", "winners_url", "_winners_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isHackathonWinner", "is_hackathon_winner", "_is_hackathon_winner", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

WriteUpItemInfo._fields = [
  FieldMetadata("type", "type", "_type", WriteUpType, WriteUpType.WRITE_UP_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("competitionInfo", "competition_info", "_competition_info", WriteUpCompetitionInfo, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("teamName", "team_name", "_team_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
]

