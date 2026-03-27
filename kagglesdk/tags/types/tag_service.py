from kagglesdk.kaggle_object import *
from kagglesdk.tags.types.tag_enums import GetTagsByIdOrderBy, TagType
from typing import List, Optional

class CreateCompetitionTagsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition to tag
    tag_ids (int)
      The tags to apply
  """

  def __init__(self):
    self._competition_id = 0
    self._tag_ids = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition to tag"""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The tags to apply"""
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


class CreateCompetitionTagsResponse(KaggleObject):
  r"""
  """

  pass

class CreateLearnTrackTagsRequest(KaggleObject):
  r"""
  Attributes:
    learn_track_id (int)
      The learn track to tag
    tag_ids (int)
      The tags to apply
  """

  def __init__(self):
    self._learn_track_id = 0
    self._tag_ids = []
    self._freeze()

  @property
  def learn_track_id(self) -> int:
    """The learn track to tag"""
    return self._learn_track_id

  @learn_track_id.setter
  def learn_track_id(self, learn_track_id: int):
    if learn_track_id is None:
      del self.learn_track_id
      return
    if not isinstance(learn_track_id, int):
      raise TypeError('learn_track_id must be of type int')
    self._learn_track_id = learn_track_id

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The tags to apply"""
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


class CreateLearnTrackTagsResponse(KaggleObject):
  r"""
  """

  pass

class CreateTagRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
    display_name (str)
    parent_category_id (int)
    slug (str)
    description (str)
    is_featured (bool)
  """

  def __init__(self):
    self._name = ""
    self._display_name = None
    self._parent_category_id = None
    self._slug = None
    self._description = None
    self._is_featured = None
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
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def parent_category_id(self) -> int:
    return self._parent_category_id or 0

  @parent_category_id.setter
  def parent_category_id(self, parent_category_id: Optional[int]):
    if parent_category_id is None:
      del self.parent_category_id
      return
    if not isinstance(parent_category_id, int):
      raise TypeError('parent_category_id must be of type int')
    self._parent_category_id = parent_category_id

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
  def is_featured(self) -> bool:
    return self._is_featured or False

  @is_featured.setter
  def is_featured(self, is_featured: Optional[bool]):
    if is_featured is None:
      del self.is_featured
      return
    if not isinstance(is_featured, bool):
      raise TypeError('is_featured must be of type bool')
    self._is_featured = is_featured


class DeleteCompetitionTagsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition to untag
    tag_ids (int)
      The tags to remove
  """

  def __init__(self):
    self._competition_id = 0
    self._tag_ids = []
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition to untag"""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The tags to remove"""
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


class DeleteCompetitionTagsResponse(KaggleObject):
  r"""
  """

  pass

class DeleteLearnTrackTagsRequest(KaggleObject):
  r"""
  Attributes:
    learn_track_id (int)
      The learn track to untag
    tag_ids (int)
      The tags to remove
  """

  def __init__(self):
    self._learn_track_id = 0
    self._tag_ids = []
    self._freeze()

  @property
  def learn_track_id(self) -> int:
    """The learn track to untag"""
    return self._learn_track_id

  @learn_track_id.setter
  def learn_track_id(self, learn_track_id: int):
    if learn_track_id is None:
      del self.learn_track_id
      return
    if not isinstance(learn_track_id, int):
      raise TypeError('learn_track_id must be of type int')
    self._learn_track_id = learn_track_id

  @property
  def tag_ids(self) -> Optional[List[int]]:
    """The tags to remove"""
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


class DeleteLearnTrackTagsResponse(KaggleObject):
  r"""
  """

  pass

class DeleteTagRequest(KaggleObject):
  r"""
  WARNING: Before running this method, make sure you run GetTaggedEntityCount
  to get an idea of how many rows in each table you'll be deleting! Deletes all
  tags for given ID.

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


class DeleteTagResponse(KaggleObject):
  r"""
  Attributes:
    warning_message (str)
    competition_categories_message (str)
    dataset_categories_message (str)
    forum_topic_categories_message (str)
    kernel_categories_message (str)
    learn_track_categories_message (str)
    user_auto_category_removals_message (str)
  """

  def __init__(self):
    self._warning_message = ""
    self._competition_categories_message = ""
    self._dataset_categories_message = ""
    self._forum_topic_categories_message = ""
    self._kernel_categories_message = ""
    self._learn_track_categories_message = ""
    self._user_auto_category_removals_message = ""
    self._freeze()

  @property
  def warning_message(self) -> str:
    return self._warning_message

  @warning_message.setter
  def warning_message(self, warning_message: str):
    if warning_message is None:
      del self.warning_message
      return
    if not isinstance(warning_message, str):
      raise TypeError('warning_message must be of type str')
    self._warning_message = warning_message

  @property
  def competition_categories_message(self) -> str:
    return self._competition_categories_message

  @competition_categories_message.setter
  def competition_categories_message(self, competition_categories_message: str):
    if competition_categories_message is None:
      del self.competition_categories_message
      return
    if not isinstance(competition_categories_message, str):
      raise TypeError('competition_categories_message must be of type str')
    self._competition_categories_message = competition_categories_message

  @property
  def dataset_categories_message(self) -> str:
    return self._dataset_categories_message

  @dataset_categories_message.setter
  def dataset_categories_message(self, dataset_categories_message: str):
    if dataset_categories_message is None:
      del self.dataset_categories_message
      return
    if not isinstance(dataset_categories_message, str):
      raise TypeError('dataset_categories_message must be of type str')
    self._dataset_categories_message = dataset_categories_message

  @property
  def forum_topic_categories_message(self) -> str:
    return self._forum_topic_categories_message

  @forum_topic_categories_message.setter
  def forum_topic_categories_message(self, forum_topic_categories_message: str):
    if forum_topic_categories_message is None:
      del self.forum_topic_categories_message
      return
    if not isinstance(forum_topic_categories_message, str):
      raise TypeError('forum_topic_categories_message must be of type str')
    self._forum_topic_categories_message = forum_topic_categories_message

  @property
  def kernel_categories_message(self) -> str:
    return self._kernel_categories_message

  @kernel_categories_message.setter
  def kernel_categories_message(self, kernel_categories_message: str):
    if kernel_categories_message is None:
      del self.kernel_categories_message
      return
    if not isinstance(kernel_categories_message, str):
      raise TypeError('kernel_categories_message must be of type str')
    self._kernel_categories_message = kernel_categories_message

  @property
  def learn_track_categories_message(self) -> str:
    return self._learn_track_categories_message

  @learn_track_categories_message.setter
  def learn_track_categories_message(self, learn_track_categories_message: str):
    if learn_track_categories_message is None:
      del self.learn_track_categories_message
      return
    if not isinstance(learn_track_categories_message, str):
      raise TypeError('learn_track_categories_message must be of type str')
    self._learn_track_categories_message = learn_track_categories_message

  @property
  def user_auto_category_removals_message(self) -> str:
    return self._user_auto_category_removals_message

  @user_auto_category_removals_message.setter
  def user_auto_category_removals_message(self, user_auto_category_removals_message: str):
    if user_auto_category_removals_message is None:
      del self.user_auto_category_removals_message
      return
    if not isinstance(user_auto_category_removals_message, str):
      raise TypeError('user_auto_category_removals_message must be of type str')
    self._user_auto_category_removals_message = user_auto_category_removals_message


class GetTaggedEntityCountRequest(KaggleObject):
  r"""
  Count number of entities in each table that fall under the target tag ID.

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


class GetTaggedEntityCountResponse(KaggleObject):
  r"""
  Attributes:
    warning_message (str)
    competition_categories_count (int)
    dataset_categories_count (int)
    forum_topic_categories_count (int)
    kernel_categories_count (int)
    learn_track_categories_count (int)
  """

  def __init__(self):
    self._warning_message = ""
    self._competition_categories_count = 0
    self._dataset_categories_count = 0
    self._forum_topic_categories_count = 0
    self._kernel_categories_count = 0
    self._learn_track_categories_count = 0
    self._freeze()

  @property
  def warning_message(self) -> str:
    return self._warning_message

  @warning_message.setter
  def warning_message(self, warning_message: str):
    if warning_message is None:
      del self.warning_message
      return
    if not isinstance(warning_message, str):
      raise TypeError('warning_message must be of type str')
    self._warning_message = warning_message

  @property
  def competition_categories_count(self) -> int:
    return self._competition_categories_count

  @competition_categories_count.setter
  def competition_categories_count(self, competition_categories_count: int):
    if competition_categories_count is None:
      del self.competition_categories_count
      return
    if not isinstance(competition_categories_count, int):
      raise TypeError('competition_categories_count must be of type int')
    self._competition_categories_count = competition_categories_count

  @property
  def dataset_categories_count(self) -> int:
    return self._dataset_categories_count

  @dataset_categories_count.setter
  def dataset_categories_count(self, dataset_categories_count: int):
    if dataset_categories_count is None:
      del self.dataset_categories_count
      return
    if not isinstance(dataset_categories_count, int):
      raise TypeError('dataset_categories_count must be of type int')
    self._dataset_categories_count = dataset_categories_count

  @property
  def forum_topic_categories_count(self) -> int:
    return self._forum_topic_categories_count

  @forum_topic_categories_count.setter
  def forum_topic_categories_count(self, forum_topic_categories_count: int):
    if forum_topic_categories_count is None:
      del self.forum_topic_categories_count
      return
    if not isinstance(forum_topic_categories_count, int):
      raise TypeError('forum_topic_categories_count must be of type int')
    self._forum_topic_categories_count = forum_topic_categories_count

  @property
  def kernel_categories_count(self) -> int:
    return self._kernel_categories_count

  @kernel_categories_count.setter
  def kernel_categories_count(self, kernel_categories_count: int):
    if kernel_categories_count is None:
      del self.kernel_categories_count
      return
    if not isinstance(kernel_categories_count, int):
      raise TypeError('kernel_categories_count must be of type int')
    self._kernel_categories_count = kernel_categories_count

  @property
  def learn_track_categories_count(self) -> int:
    return self._learn_track_categories_count

  @learn_track_categories_count.setter
  def learn_track_categories_count(self, learn_track_categories_count: int):
    if learn_track_categories_count is None:
      del self.learn_track_categories_count
      return
    if not isinstance(learn_track_categories_count, int):
      raise TypeError('learn_track_categories_count must be of type int')
    self._learn_track_categories_count = learn_track_categories_count


class GetTagHierarchyRequest(KaggleObject):
  r"""
  """

  pass

class GetTagHierarchyResponse(KaggleObject):
  r"""
  Attributes:
    roots (TagNode)
      The roots of various tag linked lists
  """

  def __init__(self):
    self._roots = []
    self._freeze()

  @property
  def roots(self) -> Optional[List[Optional['TagNode']]]:
    """The roots of various tag linked lists"""
    return self._roots

  @roots.setter
  def roots(self, roots: Optional[List[Optional['TagNode']]]):
    if roots is None:
      del self.roots
      return
    if not isinstance(roots, list):
      raise TypeError('roots must be of type list')
    if not all([isinstance(t, TagNode) for t in roots]):
      raise TypeError('roots must contain only items of type TagNode')
    self._roots = roots


class GetTagsByIdRequest(KaggleObject):
  r"""
  Attributes:
    tag_ids (int)
    order_by (GetTagsByIdOrderBy)
  """

  def __init__(self):
    self._tag_ids = []
    self._order_by = None
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
  def order_by(self) -> 'GetTagsByIdOrderBy':
    return self._order_by or GetTagsByIdOrderBy.GET_TAGS_BY_ID_ORDER_BY_UNSPECIFIED

  @order_by.setter
  def order_by(self, order_by: Optional['GetTagsByIdOrderBy']):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, GetTagsByIdOrderBy):
      raise TypeError('order_by must be of type GetTagsByIdOrderBy')
    self._order_by = order_by


class ListTagsRequest(KaggleObject):
  r"""
  Attributes:
    search (str)
    page (int)
  """

  def __init__(self):
    self._search = None
    self._page = 0
    self._freeze()

  @property
  def search(self) -> str:
    return self._search or ""

  @search.setter
  def search(self, search: Optional[str]):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

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


class ListTagsResponse(KaggleObject):
  r"""
  Attributes:
    featured_tags (Tag)
    hot_tags (Tag)
    tags_count (int)
    page_size (int)
  """

  def __init__(self):
    self._featured_tags = []
    self._hot_tags = []
    self._tags_count = 0
    self._page_size = 0
    self._freeze()

  @property
  def featured_tags(self) -> Optional[List[Optional['Tag']]]:
    return self._featured_tags

  @featured_tags.setter
  def featured_tags(self, featured_tags: Optional[List[Optional['Tag']]]):
    if featured_tags is None:
      del self.featured_tags
      return
    if not isinstance(featured_tags, list):
      raise TypeError('featured_tags must be of type list')
    if not all([isinstance(t, Tag) for t in featured_tags]):
      raise TypeError('featured_tags must contain only items of type Tag')
    self._featured_tags = featured_tags

  @property
  def hot_tags(self) -> Optional[List[Optional['Tag']]]:
    return self._hot_tags

  @hot_tags.setter
  def hot_tags(self, hot_tags: Optional[List[Optional['Tag']]]):
    if hot_tags is None:
      del self.hot_tags
      return
    if not isinstance(hot_tags, list):
      raise TypeError('hot_tags must be of type list')
    if not all([isinstance(t, Tag) for t in hot_tags]):
      raise TypeError('hot_tags must contain only items of type Tag')
    self._hot_tags = hot_tags

  @property
  def tags_count(self) -> int:
    return self._tags_count

  @tags_count.setter
  def tags_count(self, tags_count: int):
    if tags_count is None:
      del self.tags_count
      return
    if not isinstance(tags_count, int):
      raise TypeError('tags_count must be of type int')
    self._tags_count = tags_count

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size


class MergeTagRequest(KaggleObject):
  r"""
  WARNING: Before running this method, make sure you run GetTaggedEntityCount
  to get an idea of how many rows in each table you'll be modifying! Merges all
  tags for an ID into a different tag ID.

  Attributes:
    id_to_delete (int)
      Tag ID we want to delete.
    id_to_merge_into (int)
      Tag ID we want to merge into.
  """

  def __init__(self):
    self._id_to_delete = 0
    self._id_to_merge_into = 0
    self._freeze()

  @property
  def id_to_delete(self) -> int:
    """Tag ID we want to delete."""
    return self._id_to_delete

  @id_to_delete.setter
  def id_to_delete(self, id_to_delete: int):
    if id_to_delete is None:
      del self.id_to_delete
      return
    if not isinstance(id_to_delete, int):
      raise TypeError('id_to_delete must be of type int')
    self._id_to_delete = id_to_delete

  @property
  def id_to_merge_into(self) -> int:
    """Tag ID we want to merge into."""
    return self._id_to_merge_into

  @id_to_merge_into.setter
  def id_to_merge_into(self, id_to_merge_into: int):
    if id_to_merge_into is None:
      del self.id_to_merge_into
      return
    if not isinstance(id_to_merge_into, int):
      raise TypeError('id_to_merge_into must be of type int')
    self._id_to_merge_into = id_to_merge_into


class MergeTagResponse(KaggleObject):
  r"""
  Attributes:
    warning_message (str)
    competition_categories_message (str)
    dataset_categories_message (str)
    forum_topic_categories_message (str)
    kernel_categories_message (str)
    learn_track_categories_message (str)
    user_auto_category_removals_message (str)
  """

  def __init__(self):
    self._warning_message = ""
    self._competition_categories_message = ""
    self._dataset_categories_message = ""
    self._forum_topic_categories_message = ""
    self._kernel_categories_message = ""
    self._learn_track_categories_message = ""
    self._user_auto_category_removals_message = ""
    self._freeze()

  @property
  def warning_message(self) -> str:
    return self._warning_message

  @warning_message.setter
  def warning_message(self, warning_message: str):
    if warning_message is None:
      del self.warning_message
      return
    if not isinstance(warning_message, str):
      raise TypeError('warning_message must be of type str')
    self._warning_message = warning_message

  @property
  def competition_categories_message(self) -> str:
    return self._competition_categories_message

  @competition_categories_message.setter
  def competition_categories_message(self, competition_categories_message: str):
    if competition_categories_message is None:
      del self.competition_categories_message
      return
    if not isinstance(competition_categories_message, str):
      raise TypeError('competition_categories_message must be of type str')
    self._competition_categories_message = competition_categories_message

  @property
  def dataset_categories_message(self) -> str:
    return self._dataset_categories_message

  @dataset_categories_message.setter
  def dataset_categories_message(self, dataset_categories_message: str):
    if dataset_categories_message is None:
      del self.dataset_categories_message
      return
    if not isinstance(dataset_categories_message, str):
      raise TypeError('dataset_categories_message must be of type str')
    self._dataset_categories_message = dataset_categories_message

  @property
  def forum_topic_categories_message(self) -> str:
    return self._forum_topic_categories_message

  @forum_topic_categories_message.setter
  def forum_topic_categories_message(self, forum_topic_categories_message: str):
    if forum_topic_categories_message is None:
      del self.forum_topic_categories_message
      return
    if not isinstance(forum_topic_categories_message, str):
      raise TypeError('forum_topic_categories_message must be of type str')
    self._forum_topic_categories_message = forum_topic_categories_message

  @property
  def kernel_categories_message(self) -> str:
    return self._kernel_categories_message

  @kernel_categories_message.setter
  def kernel_categories_message(self, kernel_categories_message: str):
    if kernel_categories_message is None:
      del self.kernel_categories_message
      return
    if not isinstance(kernel_categories_message, str):
      raise TypeError('kernel_categories_message must be of type str')
    self._kernel_categories_message = kernel_categories_message

  @property
  def learn_track_categories_message(self) -> str:
    return self._learn_track_categories_message

  @learn_track_categories_message.setter
  def learn_track_categories_message(self, learn_track_categories_message: str):
    if learn_track_categories_message is None:
      del self.learn_track_categories_message
      return
    if not isinstance(learn_track_categories_message, str):
      raise TypeError('learn_track_categories_message must be of type str')
    self._learn_track_categories_message = learn_track_categories_message

  @property
  def user_auto_category_removals_message(self) -> str:
    return self._user_auto_category_removals_message

  @user_auto_category_removals_message.setter
  def user_auto_category_removals_message(self, user_auto_category_removals_message: str):
    if user_auto_category_removals_message is None:
      del self.user_auto_category_removals_message
      return
    if not isinstance(user_auto_category_removals_message, str):
      raise TypeError('user_auto_category_removals_message must be of type str')
    self._user_auto_category_removals_message = user_auto_category_removals_message


class SearchTagsRequest(KaggleObject):
  r"""
  Attributes:
    search_type (TagType)
    search_query (str)
    show_system_tags (bool)
    skip (int)
    take (int)
    root_category_id (int)
  """

  def __init__(self):
    self._search_type = TagType.TAG_TYPE_UNSPECIFIED
    self._search_query = None
    self._show_system_tags = False
    self._skip = 0
    self._take = 0
    self._root_category_id = None
    self._freeze()

  @property
  def search_type(self) -> 'TagType':
    return self._search_type

  @search_type.setter
  def search_type(self, search_type: 'TagType'):
    if search_type is None:
      del self.search_type
      return
    if not isinstance(search_type, TagType):
      raise TypeError('search_type must be of type TagType')
    self._search_type = search_type

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
  def show_system_tags(self) -> bool:
    return self._show_system_tags

  @show_system_tags.setter
  def show_system_tags(self, show_system_tags: bool):
    if show_system_tags is None:
      del self.show_system_tags
      return
    if not isinstance(show_system_tags, bool):
      raise TypeError('show_system_tags must be of type bool')
    self._show_system_tags = show_system_tags

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def take(self) -> int:
    return self._take

  @take.setter
  def take(self, take: int):
    if take is None:
      del self.take
      return
    if not isinstance(take, int):
      raise TypeError('take must be of type int')
    self._take = take

  @property
  def root_category_id(self) -> int:
    return self._root_category_id or 0

  @root_category_id.setter
  def root_category_id(self, root_category_id: Optional[int]):
    if root_category_id is None:
      del self.root_category_id
      return
    if not isinstance(root_category_id, int):
      raise TypeError('root_category_id must be of type int')
    self._root_category_id = root_category_id


class Tag(KaggleObject):
  r"""
  Attributes:
    id (int)
      The unique identifier for a tag
    name (str)
      The name of a tag
    full_path (str)
      The complete path for a tag, showing its ancestors, separated by >
    listing_url (str)
      The URL to link to an appropriate listing for the tag, e.g. datasets
      listing filtered by tag
    description (str)
      The description for a given tag
    dataset_count (int)
      The count of datasets tagged with a given tag
    competition_count (int)
      The count of competitions tagged with a given tag
    notebook_count (int)
      The count of notebooks tagged with a given tag
    tag_url (str)
      The URL to link directly to a given tag
    display_name (str)
      The display name for a given tag
    google_material_icon (str)
      Google Material Icon (previously FontAwesomeIcon)
    model_count (int)
      The count of models tagged with a given tag
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._full_path = ""
    self._listing_url = ""
    self._description = None
    self._dataset_count = 0
    self._competition_count = 0
    self._notebook_count = 0
    self._tag_url = ""
    self._display_name = ""
    self._google_material_icon = ""
    self._model_count = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The unique identifier for a tag"""
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
  def name(self) -> str:
    """The name of a tag"""
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
  def full_path(self) -> str:
    """The complete path for a tag, showing its ancestors, separated by >"""
    return self._full_path

  @full_path.setter
  def full_path(self, full_path: str):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def listing_url(self) -> str:
    r"""
    The URL to link to an appropriate listing for the tag, e.g. datasets
    listing filtered by tag
    """
    return self._listing_url

  @listing_url.setter
  def listing_url(self, listing_url: str):
    if listing_url is None:
      del self.listing_url
      return
    if not isinstance(listing_url, str):
      raise TypeError('listing_url must be of type str')
    self._listing_url = listing_url

  @property
  def description(self) -> str:
    """The description for a given tag"""
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
  def dataset_count(self) -> int:
    """The count of datasets tagged with a given tag"""
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
    """The count of competitions tagged with a given tag"""
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
  def notebook_count(self) -> int:
    """The count of notebooks tagged with a given tag"""
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
  def model_count(self) -> int:
    """The count of models tagged with a given tag"""
    return self._model_count

  @model_count.setter
  def model_count(self, model_count: int):
    if model_count is None:
      del self.model_count
      return
    if not isinstance(model_count, int):
      raise TypeError('model_count must be of type int')
    self._model_count = model_count

  @property
  def tag_url(self) -> str:
    """The URL to link directly to a given tag"""
    return self._tag_url

  @tag_url.setter
  def tag_url(self, tag_url: str):
    if tag_url is None:
      del self.tag_url
      return
    if not isinstance(tag_url, str):
      raise TypeError('tag_url must be of type str')
    self._tag_url = tag_url

  @property
  def display_name(self) -> str:
    """The display name for a given tag"""
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def google_material_icon(self) -> str:
    """Google Material Icon (previously FontAwesomeIcon)"""
    return self._google_material_icon

  @google_material_icon.setter
  def google_material_icon(self, google_material_icon: str):
    if google_material_icon is None:
      del self.google_material_icon
      return
    if not isinstance(google_material_icon, str):
      raise TypeError('google_material_icon must be of type str')
    self._google_material_icon = google_material_icon


class TagList(KaggleObject):
  r"""
  Attributes:
    tags (Tag)
    type (TagType)
  """

  def __init__(self):
    self._tags = []
    self._type = TagType.TAG_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def tags(self) -> Optional[List[Optional['Tag']]]:
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
  def type(self) -> 'TagType':
    return self._type

  @type.setter
  def type(self, type: 'TagType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, TagType):
      raise TypeError('type must be of type TagType')
    self._type = type


class TagNode(KaggleObject):
  r"""
  Attributes:
    tag (Tag)
      The current node's tag
    children (TagNode)
      Child nodes of the current node
  """

  def __init__(self):
    self._tag = None
    self._children = []
    self._freeze()

  @property
  def tag(self) -> Optional['Tag']:
    """The current node's tag"""
    return self._tag

  @tag.setter
  def tag(self, tag: Optional['Tag']):
    if tag is None:
      del self.tag
      return
    if not isinstance(tag, Tag):
      raise TypeError('tag must be of type Tag')
    self._tag = tag

  @property
  def children(self) -> Optional[List[Optional['TagNode']]]:
    """Child nodes of the current node"""
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['TagNode']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, TagNode) for t in children]):
      raise TypeError('children must contain only items of type TagNode')
    self._children = children


class UpdateForumTopicTagsRequest(KaggleObject):
  r"""
  Attributes:
    forum_topic_id (int)
      The forum topic to tag
    tag_ids (int)
      The set of tags to apply to the forum topic, any existing tags not in the
      set are removed
  """

  def __init__(self):
    self._forum_topic_id = 0
    self._tag_ids = []
    self._freeze()

  @property
  def forum_topic_id(self) -> int:
    """The forum topic to tag"""
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
  def tag_ids(self) -> Optional[List[int]]:
    r"""
    The set of tags to apply to the forum topic, any existing tags not in the
    set are removed
    """
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


class UpdateForumTopicTagsResponse(KaggleObject):
  r"""
  """

  pass

CreateCompetitionTagsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

CreateCompetitionTagsResponse._fields = []

CreateLearnTrackTagsRequest._fields = [
  FieldMetadata("learnTrackId", "learn_track_id", "_learn_track_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

CreateLearnTrackTagsResponse._fields = []

CreateTagRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentCategoryId", "parent_category_id", "_parent_category_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isFeatured", "is_featured", "_is_featured", bool, None, PredefinedSerializer(), optional=True),
]

DeleteCompetitionTagsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

DeleteCompetitionTagsResponse._fields = []

DeleteLearnTrackTagsRequest._fields = [
  FieldMetadata("learnTrackId", "learn_track_id", "_learn_track_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

DeleteLearnTrackTagsResponse._fields = []

DeleteTagRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DeleteTagResponse._fields = [
  FieldMetadata("warningMessage", "warning_message", "_warning_message", str, "", PredefinedSerializer()),
  FieldMetadata("competitionCategoriesMessage", "competition_categories_message", "_competition_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("datasetCategoriesMessage", "dataset_categories_message", "_dataset_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("forumTopicCategoriesMessage", "forum_topic_categories_message", "_forum_topic_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("kernelCategoriesMessage", "kernel_categories_message", "_kernel_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("learnTrackCategoriesMessage", "learn_track_categories_message", "_learn_track_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("userAutoCategoryRemovalsMessage", "user_auto_category_removals_message", "_user_auto_category_removals_message", str, "", PredefinedSerializer()),
]

GetTaggedEntityCountRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

GetTaggedEntityCountResponse._fields = [
  FieldMetadata("warningMessage", "warning_message", "_warning_message", str, "", PredefinedSerializer()),
  FieldMetadata("competitionCategoriesCount", "competition_categories_count", "_competition_categories_count", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetCategoriesCount", "dataset_categories_count", "_dataset_categories_count", int, 0, PredefinedSerializer()),
  FieldMetadata("forumTopicCategoriesCount", "forum_topic_categories_count", "_forum_topic_categories_count", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelCategoriesCount", "kernel_categories_count", "_kernel_categories_count", int, 0, PredefinedSerializer()),
  FieldMetadata("learnTrackCategoriesCount", "learn_track_categories_count", "_learn_track_categories_count", int, 0, PredefinedSerializer()),
]

GetTagHierarchyRequest._fields = []

GetTagHierarchyResponse._fields = [
  FieldMetadata("roots", "roots", "_roots", TagNode, [], ListSerializer(KaggleObjectSerializer())),
]

GetTagsByIdRequest._fields = [
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("orderBy", "order_by", "_order_by", GetTagsByIdOrderBy, None, EnumSerializer(), optional=True),
]

ListTagsRequest._fields = [
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
]

ListTagsResponse._fields = [
  FieldMetadata("featuredTags", "featured_tags", "_featured_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("hotTags", "hot_tags", "_hot_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tagsCount", "tags_count", "_tags_count", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
]

MergeTagRequest._fields = [
  FieldMetadata("idToDelete", "id_to_delete", "_id_to_delete", int, 0, PredefinedSerializer()),
  FieldMetadata("idToMergeInto", "id_to_merge_into", "_id_to_merge_into", int, 0, PredefinedSerializer()),
]

MergeTagResponse._fields = [
  FieldMetadata("warningMessage", "warning_message", "_warning_message", str, "", PredefinedSerializer()),
  FieldMetadata("competitionCategoriesMessage", "competition_categories_message", "_competition_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("datasetCategoriesMessage", "dataset_categories_message", "_dataset_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("forumTopicCategoriesMessage", "forum_topic_categories_message", "_forum_topic_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("kernelCategoriesMessage", "kernel_categories_message", "_kernel_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("learnTrackCategoriesMessage", "learn_track_categories_message", "_learn_track_categories_message", str, "", PredefinedSerializer()),
  FieldMetadata("userAutoCategoryRemovalsMessage", "user_auto_category_removals_message", "_user_auto_category_removals_message", str, "", PredefinedSerializer()),
]

SearchTagsRequest._fields = [
  FieldMetadata("searchType", "search_type", "_search_type", TagType, TagType.TAG_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("showSystemTags", "show_system_tags", "_show_system_tags", bool, False, PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("take", "take", "_take", int, 0, PredefinedSerializer()),
  FieldMetadata("rootCategoryId", "root_category_id", "_root_category_id", int, None, PredefinedSerializer(), optional=True),
]

Tag._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("fullPath", "full_path", "_full_path", str, "", PredefinedSerializer()),
  FieldMetadata("listingUrl", "listing_url", "_listing_url", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("notebookCount", "notebook_count", "_notebook_count", int, 0, PredefinedSerializer()),
  FieldMetadata("tagUrl", "tag_url", "_tag_url", str, "", PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("googleMaterialIcon", "google_material_icon", "_google_material_icon", str, "", PredefinedSerializer()),
  FieldMetadata("modelCount", "model_count", "_model_count", int, 0, PredefinedSerializer()),
]

TagList._fields = [
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("type", "type", "_type", TagType, TagType.TAG_TYPE_UNSPECIFIED, EnumSerializer()),
]

TagNode._fields = [
  FieldMetadata("tag", "tag", "_tag", Tag, None, KaggleObjectSerializer()),
  FieldMetadata("children", "children", "_children", TagNode, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateForumTopicTagsRequest._fields = [
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
]

UpdateForumTopicTagsResponse._fields = []

