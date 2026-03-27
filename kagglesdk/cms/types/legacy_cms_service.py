from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from typing import Optional, List

class CmsFilterBy(enum.Enum):
  CMS_FILTER_BY_UNSPECIFIED = 0
  CMS_FILTER_BY_ALL = 1
  CMS_FILTER_BY_PUBLISHED = 2
  CMS_FILTER_BY_UNPUBLISHED = 3

class CmsGroupBy(enum.Enum):
  CMS_GROUP_BY_UNSPECIFIED = 0
  CMS_GROUP_BY_ALL = 1
  CMS_GROUP_BY_DOCUMENTATION_PAGES = 2

class CmsSortBy(enum.Enum):
  CMS_SORT_BY_UNSPECIFIED = 0
  CMS_SORT_BY_EARLIEST = 1
  CMS_SORT_BY_LATEST = 2
  CMS_SORT_BY_DOC_PAGE_ORDER = 3

class CmsPage(KaggleObject):
  r"""
  Attributes:
    is_creating_page (bool)
    is_editing_page (bool)
    title (str)
    subtitle (str)
    image_url (str)
    mime_type (str)
    page_content (str)
    create_time (datetime)
    id (int)
    is_published (bool)
    url (str)
    user_display_name (str)
    username (str)
    is_doc_page (bool)
    doc_page_order (int)
    allow_unsanitized_html (bool)
    is_new_world (bool)
    twitter_image (str)
  """

  def __init__(self):
    self._is_creating_page = False
    self._is_editing_page = False
    self._title = None
    self._subtitle = None
    self._image_url = None
    self._mime_type = None
    self._page_content = None
    self._create_time = None
    self._id = 0
    self._is_published = False
    self._url = None
    self._user_display_name = None
    self._username = None
    self._is_doc_page = False
    self._doc_page_order = None
    self._allow_unsanitized_html = False
    self._is_new_world = False
    self._twitter_image = None
    self._freeze()

  @property
  def is_creating_page(self) -> bool:
    return self._is_creating_page

  @is_creating_page.setter
  def is_creating_page(self, is_creating_page: bool):
    if is_creating_page is None:
      del self.is_creating_page
      return
    if not isinstance(is_creating_page, bool):
      raise TypeError('is_creating_page must be of type bool')
    self._is_creating_page = is_creating_page

  @property
  def is_editing_page(self) -> bool:
    return self._is_editing_page

  @is_editing_page.setter
  def is_editing_page(self, is_editing_page: bool):
    if is_editing_page is None:
      del self.is_editing_page
      return
    if not isinstance(is_editing_page, bool):
      raise TypeError('is_editing_page must be of type bool')
    self._is_editing_page = is_editing_page

  @property
  def title(self) -> str:
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
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def mime_type(self) -> str:
    return self._mime_type or ""

  @mime_type.setter
  def mime_type(self, mime_type: Optional[str]):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type

  @property
  def page_content(self) -> str:
    return self._page_content or ""

  @page_content.setter
  def page_content(self, page_content: Optional[str]):
    if page_content is None:
      del self.page_content
      return
    if not isinstance(page_content, str):
      raise TypeError('page_content must be of type str')
    self._page_content = page_content

  @property
  def create_time(self) -> datetime:
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
  def is_published(self) -> bool:
    return self._is_published

  @is_published.setter
  def is_published(self, is_published: bool):
    if is_published is None:
      del self.is_published
      return
    if not isinstance(is_published, bool):
      raise TypeError('is_published must be of type bool')
    self._is_published = is_published

  @property
  def url(self) -> str:
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
  def user_display_name(self) -> str:
    return self._user_display_name or ""

  @user_display_name.setter
  def user_display_name(self, user_display_name: Optional[str]):
    if user_display_name is None:
      del self.user_display_name
      return
    if not isinstance(user_display_name, str):
      raise TypeError('user_display_name must be of type str')
    self._user_display_name = user_display_name

  @property
  def username(self) -> str:
    return self._username or ""

  @username.setter
  def username(self, username: Optional[str]):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def is_doc_page(self) -> bool:
    return self._is_doc_page

  @is_doc_page.setter
  def is_doc_page(self, is_doc_page: bool):
    if is_doc_page is None:
      del self.is_doc_page
      return
    if not isinstance(is_doc_page, bool):
      raise TypeError('is_doc_page must be of type bool')
    self._is_doc_page = is_doc_page

  @property
  def doc_page_order(self) -> int:
    return self._doc_page_order or 0

  @doc_page_order.setter
  def doc_page_order(self, doc_page_order: Optional[int]):
    if doc_page_order is None:
      del self.doc_page_order
      return
    if not isinstance(doc_page_order, int):
      raise TypeError('doc_page_order must be of type int')
    self._doc_page_order = doc_page_order

  @property
  def allow_unsanitized_html(self) -> bool:
    return self._allow_unsanitized_html

  @allow_unsanitized_html.setter
  def allow_unsanitized_html(self, allow_unsanitized_html: bool):
    if allow_unsanitized_html is None:
      del self.allow_unsanitized_html
      return
    if not isinstance(allow_unsanitized_html, bool):
      raise TypeError('allow_unsanitized_html must be of type bool')
    self._allow_unsanitized_html = allow_unsanitized_html

  @property
  def is_new_world(self) -> bool:
    return self._is_new_world

  @is_new_world.setter
  def is_new_world(self, is_new_world: bool):
    if is_new_world is None:
      del self.is_new_world
      return
    if not isinstance(is_new_world, bool):
      raise TypeError('is_new_world must be of type bool')
    self._is_new_world = is_new_world

  @property
  def twitter_image(self) -> str:
    return self._twitter_image or ""

  @twitter_image.setter
  def twitter_image(self, twitter_image: Optional[str]):
    if twitter_image is None:
      del self.twitter_image
      return
    if not isinstance(twitter_image, str):
      raise TypeError('twitter_image must be of type str')
    self._twitter_image = twitter_image


class CreatePageRequest(KaggleObject):
  r"""
  Attributes:
    is_doc_page (bool)
  """

  def __init__(self):
    self._is_doc_page = False
    self._freeze()

  @property
  def is_doc_page(self) -> bool:
    return self._is_doc_page

  @is_doc_page.setter
  def is_doc_page(self, is_doc_page: bool):
    if is_doc_page is None:
      del self.is_doc_page
      return
    if not isinstance(is_doc_page, bool):
      raise TypeError('is_doc_page must be of type bool')
    self._is_doc_page = is_doc_page


class CreateTeamMemberRequest(KaggleObject):
  r"""
  Attributes:
    team_member (TeamMember)
  """

  def __init__(self):
    self._team_member = None
    self._freeze()

  @property
  def team_member(self) -> Optional['TeamMember']:
    return self._team_member

  @team_member.setter
  def team_member(self, team_member: Optional['TeamMember']):
    if team_member is None:
      del self.team_member
      return
    if not isinstance(team_member, TeamMember):
      raise TypeError('team_member must be of type TeamMember')
    self._team_member = team_member


class DeleteTeamMemberRequest(KaggleObject):
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


class DocsPage(KaggleObject):
  r"""
  Attributes:
    id (int)
    url (str)
    title (str)
    subtitle (str)
    create_time (datetime)
    doc_page_order (int)
    content (str)
  """

  def __init__(self):
    self._id = 0
    self._url = None
    self._title = None
    self._subtitle = None
    self._create_time = None
    self._doc_page_order = None
    self._content = None
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

  @property
  def url(self) -> str:
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
  def title(self) -> str:
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
  def create_time(self) -> datetime:
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
  def doc_page_order(self) -> int:
    return self._doc_page_order or 0

  @doc_page_order.setter
  def doc_page_order(self, doc_page_order: Optional[int]):
    if doc_page_order is None:
      del self.doc_page_order
      return
    if not isinstance(doc_page_order, int):
      raise TypeError('doc_page_order must be of type int')
    self._doc_page_order = doc_page_order

  @property
  def content(self) -> str:
    return self._content or ""

  @content.setter
  def content(self, content: Optional[str]):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content


class GetPageRequest(KaggleObject):
  r"""
  Attributes:
    page_id (int)
    slug (str)
    is_editing (bool)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_id = None
    self._slug = None
    self._is_editing = False
    self._read_mask = None
    self._freeze()

  @property
  def page_id(self) -> int:
    return self._page_id or 0

  @page_id.setter
  def page_id(self, page_id: int):
    if page_id is None:
      del self.page_id
      return
    if not isinstance(page_id, int):
      raise TypeError('page_id must be of type int')
    del self.slug
    self._page_id = page_id

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    del self.page_id
    self._slug = slug

  @property
  def is_editing(self) -> bool:
    return self._is_editing

  @is_editing.setter
  def is_editing(self, is_editing: bool):
    if is_editing is None:
      del self.is_editing
      return
    if not isinstance(is_editing, bool):
      raise TypeError('is_editing must be of type bool')
    self._is_editing = is_editing

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


class GetPagesRequest(KaggleObject):
  r"""
  Attributes:
    page_ids (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_ids = []
    self._read_mask = None
    self._freeze()

  @property
  def page_ids(self) -> Optional[List[int]]:
    return self._page_ids

  @page_ids.setter
  def page_ids(self, page_ids: Optional[List[int]]):
    if page_ids is None:
      del self.page_ids
      return
    if not isinstance(page_ids, list):
      raise TypeError('page_ids must be of type list')
    if not all([isinstance(t, int) for t in page_ids]):
      raise TypeError('page_ids must contain only items of type int')
    self._page_ids = page_ids

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


class GetPagesResponse(KaggleObject):
  r"""
  Attributes:
    pages (CmsPage)
  """

  def __init__(self):
    self._pages = []
    self._freeze()

  @property
  def pages(self) -> Optional[List[Optional['CmsPage']]]:
    return self._pages

  @pages.setter
  def pages(self, pages: Optional[List[Optional['CmsPage']]]):
    if pages is None:
      del self.pages
      return
    if not isinstance(pages, list):
      raise TypeError('pages must be of type list')
    if not all([isinstance(t, CmsPage) for t in pages]):
      raise TypeError('pages must contain only items of type CmsPage')
    self._pages = pages


class ListDocsRequest(KaggleObject):
  r"""
  Attributes:
    want_content (bool)
  """

  def __init__(self):
    self._want_content = False
    self._freeze()

  @property
  def want_content(self) -> bool:
    return self._want_content

  @want_content.setter
  def want_content(self, want_content: bool):
    if want_content is None:
      del self.want_content
      return
    if not isinstance(want_content, bool):
      raise TypeError('want_content must be of type bool')
    self._want_content = want_content


class ListDocsResponse(KaggleObject):
  r"""
  Attributes:
    docs_pages (DocsPage)
  """

  def __init__(self):
    self._docs_pages = []
    self._freeze()

  @property
  def docs_pages(self) -> Optional[List[Optional['DocsPage']]]:
    return self._docs_pages

  @docs_pages.setter
  def docs_pages(self, docs_pages: Optional[List[Optional['DocsPage']]]):
    if docs_pages is None:
      del self.docs_pages
      return
    if not isinstance(docs_pages, list):
      raise TypeError('docs_pages must be of type list')
    if not all([isinstance(t, DocsPage) for t in docs_pages]):
      raise TypeError('docs_pages must contain only items of type DocsPage')
    self._docs_pages = docs_pages


class ListPagesRequest(KaggleObject):
  r"""
  Attributes:
    filter (CmsFilterBy)
    group (CmsGroupBy)
    sort (CmsSortBy)
    search (str)
  """

  def __init__(self):
    self._filter = None
    self._group = None
    self._sort = None
    self._search = None
    self._freeze()

  @property
  def filter(self) -> 'CmsFilterBy':
    return self._filter or CmsFilterBy.CMS_FILTER_BY_UNSPECIFIED

  @filter.setter
  def filter(self, filter: Optional['CmsFilterBy']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, CmsFilterBy):
      raise TypeError('filter must be of type CmsFilterBy')
    self._filter = filter

  @property
  def group(self) -> 'CmsGroupBy':
    return self._group or CmsGroupBy.CMS_GROUP_BY_UNSPECIFIED

  @group.setter
  def group(self, group: Optional['CmsGroupBy']):
    if group is None:
      del self.group
      return
    if not isinstance(group, CmsGroupBy):
      raise TypeError('group must be of type CmsGroupBy')
    self._group = group

  @property
  def sort(self) -> 'CmsSortBy':
    return self._sort or CmsSortBy.CMS_SORT_BY_UNSPECIFIED

  @sort.setter
  def sort(self, sort: Optional['CmsSortBy']):
    if sort is None:
      del self.sort
      return
    if not isinstance(sort, CmsSortBy):
      raise TypeError('sort must be of type CmsSortBy')
    self._sort = sort

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


class ListPagesResponse(KaggleObject):
  r"""
  Attributes:
    pages (CmsPage)
  """

  def __init__(self):
    self._pages = []
    self._freeze()

  @property
  def pages(self) -> Optional[List[Optional['CmsPage']]]:
    return self._pages

  @pages.setter
  def pages(self, pages: Optional[List[Optional['CmsPage']]]):
    if pages is None:
      del self.pages
      return
    if not isinstance(pages, list):
      raise TypeError('pages must be of type list')
    if not all([isinstance(t, CmsPage) for t in pages]):
      raise TypeError('pages must contain only items of type CmsPage')
    self._pages = pages


class ListTeamMembersRequest(KaggleObject):
  r"""
  """

  pass

class ListTeamMembersResponse(KaggleObject):
  r"""
  Attributes:
    team_members (TeamMember)
  """

  def __init__(self):
    self._team_members = []
    self._freeze()

  @property
  def team_members(self) -> Optional[List[Optional['TeamMember']]]:
    return self._team_members

  @team_members.setter
  def team_members(self, team_members: Optional[List[Optional['TeamMember']]]):
    if team_members is None:
      del self.team_members
      return
    if not isinstance(team_members, list):
      raise TypeError('team_members must be of type list')
    if not all([isinstance(t, TeamMember) for t in team_members]):
      raise TypeError('team_members must contain only items of type TeamMember')
    self._team_members = team_members


class TeamMember(KaggleObject):
  r"""
  Attributes:
    display_name (str)
    role (str)
    bio (str)
    image_url (str)
    kaggle_user_name (str)
    twitter_user_name (str)
    github_user_name (str)
    stack_overflow_user_id (int)
    display_order (int)
    id (int)
  """

  def __init__(self):
    self._display_name = ""
    self._role = ""
    self._bio = None
    self._image_url = None
    self._kaggle_user_name = None
    self._twitter_user_name = None
    self._github_user_name = None
    self._stack_overflow_user_id = None
    self._display_order = None
    self._id = None
    self._freeze()

  @property
  def display_name(self) -> str:
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
  def role(self) -> str:
    return self._role

  @role.setter
  def role(self, role: str):
    if role is None:
      del self.role
      return
    if not isinstance(role, str):
      raise TypeError('role must be of type str')
    self._role = role

  @property
  def bio(self) -> str:
    return self._bio or ""

  @bio.setter
  def bio(self, bio: Optional[str]):
    if bio is None:
      del self.bio
      return
    if not isinstance(bio, str):
      raise TypeError('bio must be of type str')
    self._bio = bio

  @property
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def kaggle_user_name(self) -> str:
    return self._kaggle_user_name or ""

  @kaggle_user_name.setter
  def kaggle_user_name(self, kaggle_user_name: Optional[str]):
    if kaggle_user_name is None:
      del self.kaggle_user_name
      return
    if not isinstance(kaggle_user_name, str):
      raise TypeError('kaggle_user_name must be of type str')
    self._kaggle_user_name = kaggle_user_name

  @property
  def twitter_user_name(self) -> str:
    return self._twitter_user_name or ""

  @twitter_user_name.setter
  def twitter_user_name(self, twitter_user_name: Optional[str]):
    if twitter_user_name is None:
      del self.twitter_user_name
      return
    if not isinstance(twitter_user_name, str):
      raise TypeError('twitter_user_name must be of type str')
    self._twitter_user_name = twitter_user_name

  @property
  def github_user_name(self) -> str:
    return self._github_user_name or ""

  @github_user_name.setter
  def github_user_name(self, github_user_name: Optional[str]):
    if github_user_name is None:
      del self.github_user_name
      return
    if not isinstance(github_user_name, str):
      raise TypeError('github_user_name must be of type str')
    self._github_user_name = github_user_name

  @property
  def stack_overflow_user_id(self) -> int:
    return self._stack_overflow_user_id or 0

  @stack_overflow_user_id.setter
  def stack_overflow_user_id(self, stack_overflow_user_id: Optional[int]):
    if stack_overflow_user_id is None:
      del self.stack_overflow_user_id
      return
    if not isinstance(stack_overflow_user_id, int):
      raise TypeError('stack_overflow_user_id must be of type int')
    self._stack_overflow_user_id = stack_overflow_user_id

  @property
  def display_order(self) -> int:
    return self._display_order or 0

  @display_order.setter
  def display_order(self, display_order: Optional[int]):
    if display_order is None:
      del self.display_order
      return
    if not isinstance(display_order, int):
      raise TypeError('display_order must be of type int')
    self._display_order = display_order

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class TeamMemberDisplayOrder(KaggleObject):
  r"""
  Attributes:
    id (int)
    display_order (int)
  """

  def __init__(self):
    self._id = 0
    self._display_order = 0
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

  @property
  def display_order(self) -> int:
    return self._display_order

  @display_order.setter
  def display_order(self, display_order: int):
    if display_order is None:
      del self.display_order
      return
    if not isinstance(display_order, int):
      raise TypeError('display_order must be of type int')
    self._display_order = display_order


class UpdateDocPageOrderRequest(KaggleObject):
  r"""
  Attributes:
    page_id (int)
    order_num (int)
  """

  def __init__(self):
    self._page_id = 0
    self._order_num = 0
    self._freeze()

  @property
  def page_id(self) -> int:
    return self._page_id

  @page_id.setter
  def page_id(self, page_id: int):
    if page_id is None:
      del self.page_id
      return
    if not isinstance(page_id, int):
      raise TypeError('page_id must be of type int')
    self._page_id = page_id

  @property
  def order_num(self) -> int:
    return self._order_num

  @order_num.setter
  def order_num(self, order_num: int):
    if order_num is None:
      del self.order_num
      return
    if not isinstance(order_num, int):
      raise TypeError('order_num must be of type int')
    self._order_num = order_num


class UpdatePageRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    image_url (str)
    is_published (bool)
    mime_type (str)
    page_content (str)
    subtitle (str)
    title (str)
    url (str)
    is_doc_page (bool)
    doc_page_order (int)
  """

  def __init__(self):
    self._id = 0
    self._image_url = None
    self._is_published = False
    self._mime_type = None
    self._page_content = None
    self._subtitle = None
    self._title = None
    self._url = None
    self._is_doc_page = False
    self._doc_page_order = None
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

  @property
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def is_published(self) -> bool:
    return self._is_published

  @is_published.setter
  def is_published(self, is_published: bool):
    if is_published is None:
      del self.is_published
      return
    if not isinstance(is_published, bool):
      raise TypeError('is_published must be of type bool')
    self._is_published = is_published

  @property
  def mime_type(self) -> str:
    return self._mime_type or ""

  @mime_type.setter
  def mime_type(self, mime_type: Optional[str]):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type

  @property
  def page_content(self) -> str:
    return self._page_content or ""

  @page_content.setter
  def page_content(self, page_content: Optional[str]):
    if page_content is None:
      del self.page_content
      return
    if not isinstance(page_content, str):
      raise TypeError('page_content must be of type str')
    self._page_content = page_content

  @property
  def subtitle(self) -> str:
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
  def title(self) -> str:
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
  def url(self) -> str:
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
  def is_doc_page(self) -> bool:
    return self._is_doc_page

  @is_doc_page.setter
  def is_doc_page(self, is_doc_page: bool):
    if is_doc_page is None:
      del self.is_doc_page
      return
    if not isinstance(is_doc_page, bool):
      raise TypeError('is_doc_page must be of type bool')
    self._is_doc_page = is_doc_page

  @property
  def doc_page_order(self) -> int:
    return self._doc_page_order or 0

  @doc_page_order.setter
  def doc_page_order(self, doc_page_order: Optional[int]):
    if doc_page_order is None:
      del self.doc_page_order
      return
    if not isinstance(doc_page_order, int):
      raise TypeError('doc_page_order must be of type int')
    self._doc_page_order = doc_page_order


class UpdatePageResponse(KaggleObject):
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


class UpdateTeamMemberRequest(KaggleObject):
  r"""
  Attributes:
    team_member (TeamMember)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._team_member = None
    self._update_mask = None
    self._freeze()

  @property
  def team_member(self) -> Optional['TeamMember']:
    return self._team_member

  @team_member.setter
  def team_member(self, team_member: Optional['TeamMember']):
    if team_member is None:
      del self.team_member
      return
    if not isinstance(team_member, TeamMember):
      raise TypeError('team_member must be of type TeamMember')
    self._team_member = team_member

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateTeamMembersDisplayOrderRequest(KaggleObject):
  r"""
  Attributes:
    display_orders (TeamMemberDisplayOrder)
  """

  def __init__(self):
    self._display_orders = []
    self._freeze()

  @property
  def display_orders(self) -> Optional[List[Optional['TeamMemberDisplayOrder']]]:
    return self._display_orders

  @display_orders.setter
  def display_orders(self, display_orders: Optional[List[Optional['TeamMemberDisplayOrder']]]):
    if display_orders is None:
      del self.display_orders
      return
    if not isinstance(display_orders, list):
      raise TypeError('display_orders must be of type list')
    if not all([isinstance(t, TeamMemberDisplayOrder) for t in display_orders]):
      raise TypeError('display_orders must contain only items of type TeamMemberDisplayOrder')
    self._display_orders = display_orders


CmsPage._fields = [
  FieldMetadata("isCreatingPage", "is_creating_page", "_is_creating_page", bool, False, PredefinedSerializer()),
  FieldMetadata("isEditingPage", "is_editing_page", "_is_editing_page", bool, False, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageContent", "page_content", "_page_content", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isPublished", "is_published", "_is_published", bool, False, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isDocPage", "is_doc_page", "_is_doc_page", bool, False, PredefinedSerializer()),
  FieldMetadata("docPageOrder", "doc_page_order", "_doc_page_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("allowUnsanitizedHtml", "allow_unsanitized_html", "_allow_unsanitized_html", bool, False, PredefinedSerializer()),
  FieldMetadata("isNewWorld", "is_new_world", "_is_new_world", bool, False, PredefinedSerializer()),
  FieldMetadata("twitterImage", "twitter_image", "_twitter_image", str, None, PredefinedSerializer(), optional=True),
]

CreatePageRequest._fields = [
  FieldMetadata("isDocPage", "is_doc_page", "_is_doc_page", bool, False, PredefinedSerializer()),
]

CreateTeamMemberRequest._fields = [
  FieldMetadata("teamMember", "team_member", "_team_member", TeamMember, None, KaggleObjectSerializer()),
]

DeleteTeamMemberRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DocsPage._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("docPageOrder", "doc_page_order", "_doc_page_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("content", "content", "_content", str, None, PredefinedSerializer(), optional=True),
]

GetPageRequest._fields = [
  FieldMetadata("pageId", "page_id", "_page_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isEditing", "is_editing", "_is_editing", bool, False, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetPagesRequest._fields = [
  FieldMetadata("pageIds", "page_ids", "_page_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetPagesResponse._fields = [
  FieldMetadata("pages", "pages", "_pages", CmsPage, [], ListSerializer(KaggleObjectSerializer())),
]

ListDocsRequest._fields = [
  FieldMetadata("wantContent", "want_content", "_want_content", bool, False, PredefinedSerializer()),
]

ListDocsResponse._fields = [
  FieldMetadata("docsPages", "docs_pages", "_docs_pages", DocsPage, [], ListSerializer(KaggleObjectSerializer())),
]

ListPagesRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", CmsFilterBy, None, EnumSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", CmsGroupBy, None, EnumSerializer(), optional=True),
  FieldMetadata("sort", "sort", "_sort", CmsSortBy, None, EnumSerializer(), optional=True),
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
]

ListPagesResponse._fields = [
  FieldMetadata("pages", "pages", "_pages", CmsPage, [], ListSerializer(KaggleObjectSerializer())),
]

ListTeamMembersRequest._fields = []

ListTeamMembersResponse._fields = [
  FieldMetadata("teamMembers", "team_members", "_team_members", TeamMember, [], ListSerializer(KaggleObjectSerializer())),
]

TeamMember._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("role", "role", "_role", str, "", PredefinedSerializer()),
  FieldMetadata("bio", "bio", "_bio", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kaggleUserName", "kaggle_user_name", "_kaggle_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("twitterUserName", "twitter_user_name", "_twitter_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("githubUserName", "github_user_name", "_github_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("stackOverflowUserId", "stack_overflow_user_id", "_stack_overflow_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayOrder", "display_order", "_display_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
]

TeamMemberDisplayOrder._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayOrder", "display_order", "_display_order", int, 0, PredefinedSerializer()),
]

UpdateDocPageOrderRequest._fields = [
  FieldMetadata("pageId", "page_id", "_page_id", int, 0, PredefinedSerializer()),
  FieldMetadata("orderNum", "order_num", "_order_num", int, 0, PredefinedSerializer()),
]

UpdatePageRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPublished", "is_published", "_is_published", bool, False, PredefinedSerializer()),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageContent", "page_content", "_page_content", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isDocPage", "is_doc_page", "_is_doc_page", bool, False, PredefinedSerializer()),
  FieldMetadata("docPageOrder", "doc_page_order", "_doc_page_order", int, None, PredefinedSerializer(), optional=True),
]

UpdatePageResponse._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

UpdateTeamMemberRequest._fields = [
  FieldMetadata("teamMember", "team_member", "_team_member", TeamMember, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateTeamMembersDisplayOrderRequest._fields = [
  FieldMetadata("displayOrders", "display_orders", "_display_orders", TeamMemberDisplayOrder, [], ListSerializer(KaggleObjectSerializer())),
]

