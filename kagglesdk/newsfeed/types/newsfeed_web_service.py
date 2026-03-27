from datetime import datetime
from kagglesdk.competitions.types.team import Team
from kagglesdk.datasets.types.dataset_enums import DatasetFileType
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import EditorType
from kagglesdk.newsfeed.types.newsfeed_service import ItemType
from kagglesdk.users.types.progression_service import GetCurrentUserProgressionResponse
from kagglesdk.users.types.user import User
from kagglesdk.users.types.users_enums import UserAchievementTier
from typing import List, Optional

class GetDsSurveyBannerStateRequest(KaggleObject):
  r"""
  """

  pass

class GetDsSurveyBannerStateResponse(KaggleObject):
  r"""
  Attributes:
    show_banner (bool)
  """

  def __init__(self):
    self._show_banner = False
    self._freeze()

  @property
  def show_banner(self) -> bool:
    return self._show_banner

  @show_banner.setter
  def show_banner(self, show_banner: bool):
    if show_banner is None:
      del self.show_banner
      return
    if not isinstance(show_banner, bool):
      raise TypeError('show_banner must be of type bool')
    self._show_banner = show_banner


class GetNewAndExcitingContentRequest(KaggleObject):
  r"""
  """

  pass

class GetNewAndExcitingContentResponse(KaggleObject):
  r"""
  Attributes:
    items (NewAndExcitingItem)
  """

  def __init__(self):
    self._items = []
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['NewAndExcitingItem']]]:
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['NewAndExcitingItem']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, NewAndExcitingItem) for t in items]):
      raise TypeError('items must contain only items of type NewAndExcitingItem')
    self._items = items


class GetNewsfeedSidebarContentRequest(KaggleObject):
  r"""
  """

  pass

class GetStoriesRequest(KaggleObject):
  r"""
  Attributes:
    page (int)
    page_size (int)
  """

  def __init__(self):
    self._page = 0
    self._page_size = 0
    self._freeze()

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


class GetStoriesResponse(KaggleObject):
  r"""
  Attributes:
    stories (NewsfeedStory)
  """

  def __init__(self):
    self._stories = []
    self._freeze()

  @property
  def stories(self) -> Optional[List[Optional['NewsfeedStory']]]:
    return self._stories

  @stories.setter
  def stories(self, stories: Optional[List[Optional['NewsfeedStory']]]):
    if stories is None:
      del self.stories
      return
    if not isinstance(stories, list):
      raise TypeError('stories must be of type list')
    if not all([isinstance(t, NewsfeedStory) for t in stories]):
      raise TypeError('stories must contain only items of type NewsfeedStory')
    self._stories = stories


class NewAndExcitingItem(KaggleObject):
  r"""
  Attributes:
    category (str)
    title (str)
    description (str)
    image_url (str)
    url (str)
  """

  def __init__(self):
    self._category = ""
    self._title = ""
    self._description = ""
    self._image_url = ""
    self._url = ""
    self._freeze()

  @property
  def category(self) -> str:
    return self._category

  @category.setter
  def category(self, category: str):
    if category is None:
      del self.category
      return
    if not isinstance(category, str):
      raise TypeError('category must be of type str')
    self._category = category

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
  def image_url(self) -> str:
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


class NewsfeedBlog(KaggleObject):
  r"""
  Attributes:
    image_url (str)
    summary (str)
    title (str)
    url (str)
  """

  def __init__(self):
    self._image_url = ""
    self._summary = ""
    self._title = ""
    self._url = ""
    self._freeze()

  @property
  def image_url(self) -> str:
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
  def summary(self) -> str:
    return self._summary

  @summary.setter
  def summary(self, summary: str):
    if summary is None:
      del self.summary
      return
    if not isinstance(summary, str):
      raise TypeError('summary must be of type str')
    self._summary = summary

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


class NewsfeedCompetition(KaggleObject):
  r"""
  Attributes:
    cover_image_url (str)
    current_user_rank (int)
    deadline (datetime)
    title (str)
    image_url (str)
    brief_description (str)
    overview (NewsfeedCompetitionOverview)
    results_are_final (bool)
    reward_quantity (float)
    reward_type (str)
    teams (NewsfeedCompetitionTeam)
    total_entered_teams (int)
    url (str)
    top_solution_write_up_url (str)
      Link to the Forum Topic of the solution writeup linked to the top-ranked
      team who has published a writeup.
  """

  def __init__(self):
    self._cover_image_url = ""
    self._current_user_rank = None
    self._deadline = None
    self._title = None
    self._image_url = ""
    self._brief_description = ""
    self._overview = None
    self._results_are_final = None
    self._reward_quantity = None
    self._reward_type = None
    self._teams = []
    self._total_entered_teams = None
    self._url = None
    self._top_solution_write_up_url = None
    self._freeze()

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
  def current_user_rank(self) -> int:
    return self._current_user_rank or 0

  @current_user_rank.setter
  def current_user_rank(self, current_user_rank: Optional[int]):
    if current_user_rank is None:
      del self.current_user_rank
      return
    if not isinstance(current_user_rank, int):
      raise TypeError('current_user_rank must be of type int')
    self._current_user_rank = current_user_rank

  @property
  def deadline(self) -> datetime:
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
  def image_url(self) -> str:
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
  def brief_description(self) -> str:
    return self._brief_description

  @brief_description.setter
  def brief_description(self, brief_description: str):
    if brief_description is None:
      del self.brief_description
      return
    if not isinstance(brief_description, str):
      raise TypeError('brief_description must be of type str')
    self._brief_description = brief_description

  @property
  def overview(self) -> Optional['NewsfeedCompetitionOverview']:
    return self._overview

  @overview.setter
  def overview(self, overview: Optional['NewsfeedCompetitionOverview']):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, NewsfeedCompetitionOverview):
      raise TypeError('overview must be of type NewsfeedCompetitionOverview')
    self._overview = overview

  @property
  def results_are_final(self) -> bool:
    return self._results_are_final or False

  @results_are_final.setter
  def results_are_final(self, results_are_final: Optional[bool]):
    if results_are_final is None:
      del self.results_are_final
      return
    if not isinstance(results_are_final, bool):
      raise TypeError('results_are_final must be of type bool')
    self._results_are_final = results_are_final

  @property
  def reward_quantity(self) -> float:
    return self._reward_quantity or 0.0

  @reward_quantity.setter
  def reward_quantity(self, reward_quantity: Optional[float]):
    if reward_quantity is None:
      del self.reward_quantity
      return
    if not isinstance(reward_quantity, float):
      raise TypeError('reward_quantity must be of type float')
    self._reward_quantity = reward_quantity

  @property
  def reward_type(self) -> str:
    return self._reward_type or ""

  @reward_type.setter
  def reward_type(self, reward_type: Optional[str]):
    if reward_type is None:
      del self.reward_type
      return
    if not isinstance(reward_type, str):
      raise TypeError('reward_type must be of type str')
    self._reward_type = reward_type

  @property
  def teams(self) -> Optional[List[Optional['NewsfeedCompetitionTeam']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['NewsfeedCompetitionTeam']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, NewsfeedCompetitionTeam) for t in teams]):
      raise TypeError('teams must contain only items of type NewsfeedCompetitionTeam')
    self._teams = teams

  @property
  def total_entered_teams(self) -> int:
    return self._total_entered_teams or 0

  @total_entered_teams.setter
  def total_entered_teams(self, total_entered_teams: Optional[int]):
    if total_entered_teams is None:
      del self.total_entered_teams
      return
    if not isinstance(total_entered_teams, int):
      raise TypeError('total_entered_teams must be of type int')
    self._total_entered_teams = total_entered_teams

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
  def top_solution_write_up_url(self) -> str:
    r"""
    Link to the Forum Topic of the solution writeup linked to the top-ranked
    team who has published a writeup.
    """
    return self._top_solution_write_up_url or ""

  @top_solution_write_up_url.setter
  def top_solution_write_up_url(self, top_solution_write_up_url: Optional[str]):
    if top_solution_write_up_url is None:
      del self.top_solution_write_up_url
      return
    if not isinstance(top_solution_write_up_url, str):
      raise TypeError('top_solution_write_up_url must be of type str')
    self._top_solution_write_up_url = top_solution_write_up_url


class NewsfeedCompetitionOverview(KaggleObject):
  r"""
  Attributes:
    content (str)
    type (str)
  """

  def __init__(self):
    self._content = ""
    self._type = ""
    self._freeze()

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

  @property
  def type(self) -> str:
    return self._type

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type


class NewsfeedCompetitionTeam(KaggleObject):
  r"""
  Attributes:
    name (str)
    rank (int)
    team (Team)
    users (User)
  """

  def __init__(self):
    self._name = ""
    self._rank = None
    self._team = None
    self._users = []
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
  def rank(self) -> int:
    return self._rank or 0

  @rank.setter
  def rank(self, rank: Optional[int]):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

  @property
  def team(self) -> Optional['Team']:
    return self._team

  @team.setter
  def team(self, team: Optional['Team']):
    if team is None:
      del self.team
      return
    if not isinstance(team, Team):
      raise TypeError('team must be of type Team')
    self._team = team

  @property
  def users(self) -> Optional[List[Optional['User']]]:
    return self._users

  @users.setter
  def users(self, users: Optional[List[Optional['User']]]):
    if users is None:
      del self.users
      return
    if not isinstance(users, list):
      raise TypeError('users must be of type list')
    if not all([isinstance(t, User) for t in users]):
      raise TypeError('users must contain only items of type User')
    self._users = users


class NewsfeedDataset(KaggleObject):
  r"""
  Attributes:
    common_file_type (DatasetFileType)
    databundle_version_id (int)
    dataset_is_deleted (bool)
    image_url (str)
    license_name (str)
    overview (str)
    title (str)
    total_size (int)
    total_files (int)
    total_kernels (int)
    total_topics (int)
    total_views (int)
    url (str)
    version_notes (str)
    dataset_id (int)
  """

  def __init__(self):
    self._common_file_type = DatasetFileType.DATASET_FILE_TYPE_UNSPECIFIED
    self._databundle_version_id = None
    self._dataset_is_deleted = False
    self._image_url = None
    self._license_name = ""
    self._overview = ""
    self._title = None
    self._total_size = None
    self._total_files = None
    self._total_kernels = None
    self._total_topics = None
    self._total_views = None
    self._url = None
    self._version_notes = ""
    self._dataset_id = None
    self._freeze()

  @property
  def common_file_type(self) -> 'DatasetFileType':
    return self._common_file_type

  @common_file_type.setter
  def common_file_type(self, common_file_type: 'DatasetFileType'):
    if common_file_type is None:
      del self.common_file_type
      return
    if not isinstance(common_file_type, DatasetFileType):
      raise TypeError('common_file_type must be of type DatasetFileType')
    self._common_file_type = common_file_type

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id or 0

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: Optional[int]):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

  @property
  def dataset_is_deleted(self) -> bool:
    return self._dataset_is_deleted

  @dataset_is_deleted.setter
  def dataset_is_deleted(self, dataset_is_deleted: bool):
    if dataset_is_deleted is None:
      del self.dataset_is_deleted
      return
    if not isinstance(dataset_is_deleted, bool):
      raise TypeError('dataset_is_deleted must be of type bool')
    self._dataset_is_deleted = dataset_is_deleted

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
  def license_name(self) -> str:
    return self._license_name

  @license_name.setter
  def license_name(self, license_name: str):
    if license_name is None:
      del self.license_name
      return
    if not isinstance(license_name, str):
      raise TypeError('license_name must be of type str')
    self._license_name = license_name

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
  def total_size(self) -> int:
    return self._total_size or 0

  @total_size.setter
  def total_size(self, total_size: Optional[int]):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

  @property
  def total_files(self) -> int:
    return self._total_files or 0

  @total_files.setter
  def total_files(self, total_files: Optional[int]):
    if total_files is None:
      del self.total_files
      return
    if not isinstance(total_files, int):
      raise TypeError('total_files must be of type int')
    self._total_files = total_files

  @property
  def total_kernels(self) -> int:
    return self._total_kernels or 0

  @total_kernels.setter
  def total_kernels(self, total_kernels: Optional[int]):
    if total_kernels is None:
      del self.total_kernels
      return
    if not isinstance(total_kernels, int):
      raise TypeError('total_kernels must be of type int')
    self._total_kernels = total_kernels

  @property
  def total_topics(self) -> int:
    return self._total_topics or 0

  @total_topics.setter
  def total_topics(self, total_topics: Optional[int]):
    if total_topics is None:
      del self.total_topics
      return
    if not isinstance(total_topics, int):
      raise TypeError('total_topics must be of type int')
    self._total_topics = total_topics

  @property
  def total_views(self) -> int:
    return self._total_views or 0

  @total_views.setter
  def total_views(self, total_views: Optional[int]):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

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
  def version_notes(self) -> str:
    return self._version_notes

  @version_notes.setter
  def version_notes(self, version_notes: str):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id


class NewsfeedDiscussion(KaggleObject):
  r"""
  Attributes:
    forum_name (str)
    forum_url (str)
    message_id (int)
    message_raw_html (str)
    message_raw_markdown (str)
    message_url (str)
    topic_date (datetime)
    topic_id (int)
    topic_name (str)
    topic_raw_html (str)
    topic_raw_markdown (str)
    topic_url (str)
  """

  def __init__(self):
    self._forum_name = ""
    self._forum_url = None
    self._message_id = None
    self._message_raw_html = ""
    self._message_raw_markdown = None
    self._message_url = ""
    self._topic_date = None
    self._topic_id = None
    self._topic_name = ""
    self._topic_raw_html = ""
    self._topic_raw_markdown = None
    self._topic_url = ""
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
    return self._forum_url or ""

  @forum_url.setter
  def forum_url(self, forum_url: Optional[str]):
    if forum_url is None:
      del self.forum_url
      return
    if not isinstance(forum_url, str):
      raise TypeError('forum_url must be of type str')
    self._forum_url = forum_url

  @property
  def message_id(self) -> int:
    return self._message_id or 0

  @message_id.setter
  def message_id(self, message_id: Optional[int]):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    self._message_id = message_id

  @property
  def message_raw_html(self) -> str:
    return self._message_raw_html

  @message_raw_html.setter
  def message_raw_html(self, message_raw_html: str):
    if message_raw_html is None:
      del self.message_raw_html
      return
    if not isinstance(message_raw_html, str):
      raise TypeError('message_raw_html must be of type str')
    self._message_raw_html = message_raw_html

  @property
  def message_raw_markdown(self) -> str:
    return self._message_raw_markdown or ""

  @message_raw_markdown.setter
  def message_raw_markdown(self, message_raw_markdown: Optional[str]):
    if message_raw_markdown is None:
      del self.message_raw_markdown
      return
    if not isinstance(message_raw_markdown, str):
      raise TypeError('message_raw_markdown must be of type str')
    self._message_raw_markdown = message_raw_markdown

  @property
  def message_url(self) -> str:
    return self._message_url

  @message_url.setter
  def message_url(self, message_url: str):
    if message_url is None:
      del self.message_url
      return
    if not isinstance(message_url, str):
      raise TypeError('message_url must be of type str')
    self._message_url = message_url

  @property
  def topic_date(self) -> datetime:
    return self._topic_date

  @topic_date.setter
  def topic_date(self, topic_date: datetime):
    if topic_date is None:
      del self.topic_date
      return
    if not isinstance(topic_date, datetime):
      raise TypeError('topic_date must be of type datetime')
    self._topic_date = topic_date

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
  def topic_name(self) -> str:
    return self._topic_name

  @topic_name.setter
  def topic_name(self, topic_name: str):
    if topic_name is None:
      del self.topic_name
      return
    if not isinstance(topic_name, str):
      raise TypeError('topic_name must be of type str')
    self._topic_name = topic_name

  @property
  def topic_raw_html(self) -> str:
    return self._topic_raw_html

  @topic_raw_html.setter
  def topic_raw_html(self, topic_raw_html: str):
    if topic_raw_html is None:
      del self.topic_raw_html
      return
    if not isinstance(topic_raw_html, str):
      raise TypeError('topic_raw_html must be of type str')
    self._topic_raw_html = topic_raw_html

  @property
  def topic_raw_markdown(self) -> str:
    return self._topic_raw_markdown or ""

  @topic_raw_markdown.setter
  def topic_raw_markdown(self, topic_raw_markdown: Optional[str]):
    if topic_raw_markdown is None:
      del self.topic_raw_markdown
      return
    if not isinstance(topic_raw_markdown, str):
      raise TypeError('topic_raw_markdown must be of type str')
    self._topic_raw_markdown = topic_raw_markdown

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


class NewsfeedKernel(KaggleObject):
  r"""
  Attributes:
    comment_count (int)
    data_url (str)
    disable_comments (bool)
    file_output_count (int)
    has_multiple_data_sources (bool)
    kernel_id (int)
    kernel_type (EditorType)
    language (str)
    line_count (int)
    name (str)
    run_time_seconds (float)
    url (str)
    views (int)
    visualization_urls (str)
  """

  def __init__(self):
    self._comment_count = 0
    self._data_url = ""
    self._disable_comments = False
    self._file_output_count = None
    self._has_multiple_data_sources = False
    self._kernel_id = None
    self._kernel_type = EditorType.EDITOR_TYPE_UNSPECIFIED
    self._language = ""
    self._line_count = None
    self._name = ""
    self._run_time_seconds = None
    self._url = ""
    self._views = None
    self._visualization_urls = []
    self._freeze()

  @property
  def comment_count(self) -> int:
    return self._comment_count

  @comment_count.setter
  def comment_count(self, comment_count: int):
    if comment_count is None:
      del self.comment_count
      return
    if not isinstance(comment_count, int):
      raise TypeError('comment_count must be of type int')
    self._comment_count = comment_count

  @property
  def data_url(self) -> str:
    return self._data_url

  @data_url.setter
  def data_url(self, data_url: str):
    if data_url is None:
      del self.data_url
      return
    if not isinstance(data_url, str):
      raise TypeError('data_url must be of type str')
    self._data_url = data_url

  @property
  def disable_comments(self) -> bool:
    return self._disable_comments

  @disable_comments.setter
  def disable_comments(self, disable_comments: bool):
    if disable_comments is None:
      del self.disable_comments
      return
    if not isinstance(disable_comments, bool):
      raise TypeError('disable_comments must be of type bool')
    self._disable_comments = disable_comments

  @property
  def file_output_count(self) -> int:
    return self._file_output_count or 0

  @file_output_count.setter
  def file_output_count(self, file_output_count: Optional[int]):
    if file_output_count is None:
      del self.file_output_count
      return
    if not isinstance(file_output_count, int):
      raise TypeError('file_output_count must be of type int')
    self._file_output_count = file_output_count

  @property
  def has_multiple_data_sources(self) -> bool:
    return self._has_multiple_data_sources

  @has_multiple_data_sources.setter
  def has_multiple_data_sources(self, has_multiple_data_sources: bool):
    if has_multiple_data_sources is None:
      del self.has_multiple_data_sources
      return
    if not isinstance(has_multiple_data_sources, bool):
      raise TypeError('has_multiple_data_sources must be of type bool')
    self._has_multiple_data_sources = has_multiple_data_sources

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def kernel_type(self) -> 'EditorType':
    return self._kernel_type

  @kernel_type.setter
  def kernel_type(self, kernel_type: 'EditorType'):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, EditorType):
      raise TypeError('kernel_type must be of type EditorType')
    self._kernel_type = kernel_type

  @property
  def language(self) -> str:
    return self._language

  @language.setter
  def language(self, language: str):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def line_count(self) -> int:
    return self._line_count or 0

  @line_count.setter
  def line_count(self, line_count: Optional[int]):
    if line_count is None:
      del self.line_count
      return
    if not isinstance(line_count, int):
      raise TypeError('line_count must be of type int')
    self._line_count = line_count

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
  def run_time_seconds(self) -> float:
    return self._run_time_seconds or 0.0

  @run_time_seconds.setter
  def run_time_seconds(self, run_time_seconds: Optional[float]):
    if run_time_seconds is None:
      del self.run_time_seconds
      return
    if not isinstance(run_time_seconds, float):
      raise TypeError('run_time_seconds must be of type float')
    self._run_time_seconds = run_time_seconds

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
  def views(self) -> int:
    return self._views or 0

  @views.setter
  def views(self, views: Optional[int]):
    if views is None:
      del self.views
      return
    if not isinstance(views, int):
      raise TypeError('views must be of type int')
    self._views = views

  @property
  def visualization_urls(self) -> Optional[List[str]]:
    return self._visualization_urls

  @visualization_urls.setter
  def visualization_urls(self, visualization_urls: Optional[List[str]]):
    if visualization_urls is None:
      del self.visualization_urls
      return
    if not isinstance(visualization_urls, list):
      raise TypeError('visualization_urls must be of type list')
    if not all([isinstance(t, str) for t in visualization_urls]):
      raise TypeError('visualization_urls must contain only items of type str')
    self._visualization_urls = visualization_urls


class NewsfeedSidebarContent(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    avatar_url (str)
    user_url (str)
    user_tier (UserAchievementTier)
    user_join_date (datetime)
    progression (GetCurrentUserProgressionResponse)
    competition_sidebar_list (NewsfeedSidebarItem)
    dataset_sidebar_list (NewsfeedSidebarItem)
    kernel_sidebar_list (NewsfeedSidebarItem)
  """

  def __init__(self):
    self._user_name = None
    self._avatar_url = None
    self._user_url = None
    self._user_tier = UserAchievementTier.NOVICE
    self._user_join_date = None
    self._progression = None
    self._competition_sidebar_list = []
    self._dataset_sidebar_list = []
    self._kernel_sidebar_list = []
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def avatar_url(self) -> str:
    return self._avatar_url or ""

  @avatar_url.setter
  def avatar_url(self, avatar_url: Optional[str]):
    if avatar_url is None:
      del self.avatar_url
      return
    if not isinstance(avatar_url, str):
      raise TypeError('avatar_url must be of type str')
    self._avatar_url = avatar_url

  @property
  def user_url(self) -> str:
    return self._user_url or ""

  @user_url.setter
  def user_url(self, user_url: Optional[str]):
    if user_url is None:
      del self.user_url
      return
    if not isinstance(user_url, str):
      raise TypeError('user_url must be of type str')
    self._user_url = user_url

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier

  @property
  def user_join_date(self) -> datetime:
    return self._user_join_date

  @user_join_date.setter
  def user_join_date(self, user_join_date: datetime):
    if user_join_date is None:
      del self.user_join_date
      return
    if not isinstance(user_join_date, datetime):
      raise TypeError('user_join_date must be of type datetime')
    self._user_join_date = user_join_date

  @property
  def progression(self) -> Optional['GetCurrentUserProgressionResponse']:
    return self._progression

  @progression.setter
  def progression(self, progression: Optional['GetCurrentUserProgressionResponse']):
    if progression is None:
      del self.progression
      return
    if not isinstance(progression, GetCurrentUserProgressionResponse):
      raise TypeError('progression must be of type GetCurrentUserProgressionResponse')
    self._progression = progression

  @property
  def competition_sidebar_list(self) -> Optional[List[Optional['NewsfeedSidebarItem']]]:
    return self._competition_sidebar_list

  @competition_sidebar_list.setter
  def competition_sidebar_list(self, competition_sidebar_list: Optional[List[Optional['NewsfeedSidebarItem']]]):
    if competition_sidebar_list is None:
      del self.competition_sidebar_list
      return
    if not isinstance(competition_sidebar_list, list):
      raise TypeError('competition_sidebar_list must be of type list')
    if not all([isinstance(t, NewsfeedSidebarItem) for t in competition_sidebar_list]):
      raise TypeError('competition_sidebar_list must contain only items of type NewsfeedSidebarItem')
    self._competition_sidebar_list = competition_sidebar_list

  @property
  def dataset_sidebar_list(self) -> Optional[List[Optional['NewsfeedSidebarItem']]]:
    return self._dataset_sidebar_list

  @dataset_sidebar_list.setter
  def dataset_sidebar_list(self, dataset_sidebar_list: Optional[List[Optional['NewsfeedSidebarItem']]]):
    if dataset_sidebar_list is None:
      del self.dataset_sidebar_list
      return
    if not isinstance(dataset_sidebar_list, list):
      raise TypeError('dataset_sidebar_list must be of type list')
    if not all([isinstance(t, NewsfeedSidebarItem) for t in dataset_sidebar_list]):
      raise TypeError('dataset_sidebar_list must contain only items of type NewsfeedSidebarItem')
    self._dataset_sidebar_list = dataset_sidebar_list

  @property
  def kernel_sidebar_list(self) -> Optional[List[Optional['NewsfeedSidebarItem']]]:
    return self._kernel_sidebar_list

  @kernel_sidebar_list.setter
  def kernel_sidebar_list(self, kernel_sidebar_list: Optional[List[Optional['NewsfeedSidebarItem']]]):
    if kernel_sidebar_list is None:
      del self.kernel_sidebar_list
      return
    if not isinstance(kernel_sidebar_list, list):
      raise TypeError('kernel_sidebar_list must be of type list')
    if not all([isinstance(t, NewsfeedSidebarItem) for t in kernel_sidebar_list]):
      raise TypeError('kernel_sidebar_list must contain only items of type NewsfeedSidebarItem')
    self._kernel_sidebar_list = kernel_sidebar_list


class NewsfeedSidebarItem(KaggleObject):
  r"""
  Attributes:
    image_url (str)
    title (str)
    link_url (str)
    icon (str)
    icon_title (str)
    icon_right (str)
    icon_right_title (str)
    date_created (datetime)
  """

  def __init__(self):
    self._image_url = None
    self._title = None
    self._link_url = None
    self._icon = None
    self._icon_title = None
    self._icon_right = None
    self._icon_right_title = None
    self._date_created = None
    self._freeze()

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
  def link_url(self) -> str:
    return self._link_url or ""

  @link_url.setter
  def link_url(self, link_url: Optional[str]):
    if link_url is None:
      del self.link_url
      return
    if not isinstance(link_url, str):
      raise TypeError('link_url must be of type str')
    self._link_url = link_url

  @property
  def icon(self) -> str:
    return self._icon or ""

  @icon.setter
  def icon(self, icon: Optional[str]):
    if icon is None:
      del self.icon
      return
    if not isinstance(icon, str):
      raise TypeError('icon must be of type str')
    self._icon = icon

  @property
  def icon_title(self) -> str:
    return self._icon_title or ""

  @icon_title.setter
  def icon_title(self, icon_title: Optional[str]):
    if icon_title is None:
      del self.icon_title
      return
    if not isinstance(icon_title, str):
      raise TypeError('icon_title must be of type str')
    self._icon_title = icon_title

  @property
  def icon_right(self) -> str:
    return self._icon_right or ""

  @icon_right.setter
  def icon_right(self, icon_right: Optional[str]):
    if icon_right is None:
      del self.icon_right
      return
    if not isinstance(icon_right, str):
      raise TypeError('icon_right must be of type str')
    self._icon_right = icon_right

  @property
  def icon_right_title(self) -> str:
    return self._icon_right_title or ""

  @icon_right_title.setter
  def icon_right_title(self, icon_right_title: Optional[str]):
    if icon_right_title is None:
      del self.icon_right_title
      return
    if not isinstance(icon_right_title, str):
      raise TypeError('icon_right_title must be of type str')
    self._icon_right_title = icon_right_title

  @property
  def date_created(self) -> datetime:
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created


class NewsfeedStory(KaggleObject):
  r"""
  Attributes:
    action_user (User)
      Only users can do actions on the newsfeed, such as upvoting and commenting
    blog (NewsfeedBlog)
    competition (NewsfeedCompetition)
    dataset (NewsfeedDataset)
    date (datetime)
    discussion (NewsfeedDiscussion)
    is_following_item (bool)
    is_following_user (bool)
    kernel (NewsfeedKernel)
    owner_organization (Organization)
      Owners can be either a user or an organization
    owner_user (User)
    story_info (NewsfeedStoryInfo)
    vote (NewsfeedVote)
  """

  def __init__(self):
    self._action_user = None
    self._blog = None
    self._competition = None
    self._dataset = None
    self._date = None
    self._discussion = None
    self._is_following_item = None
    self._is_following_user = None
    self._kernel = None
    self._owner_organization = None
    self._owner_user = None
    self._story_info = None
    self._vote = None
    self._freeze()

  @property
  def action_user(self) -> Optional['User']:
    """Only users can do actions on the newsfeed, such as upvoting and commenting"""
    return self._action_user

  @action_user.setter
  def action_user(self, action_user: Optional['User']):
    if action_user is None:
      del self.action_user
      return
    if not isinstance(action_user, User):
      raise TypeError('action_user must be of type User')
    self._action_user = action_user

  @property
  def blog(self) -> Optional['NewsfeedBlog']:
    return self._blog

  @blog.setter
  def blog(self, blog: Optional['NewsfeedBlog']):
    if blog is None:
      del self.blog
      return
    if not isinstance(blog, NewsfeedBlog):
      raise TypeError('blog must be of type NewsfeedBlog')
    self._blog = blog

  @property
  def competition(self) -> Optional['NewsfeedCompetition']:
    return self._competition

  @competition.setter
  def competition(self, competition: Optional['NewsfeedCompetition']):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, NewsfeedCompetition):
      raise TypeError('competition must be of type NewsfeedCompetition')
    self._competition = competition

  @property
  def dataset(self) -> Optional['NewsfeedDataset']:
    return self._dataset

  @dataset.setter
  def dataset(self, dataset: Optional['NewsfeedDataset']):
    if dataset is None:
      del self.dataset
      return
    if not isinstance(dataset, NewsfeedDataset):
      raise TypeError('dataset must be of type NewsfeedDataset')
    self._dataset = dataset

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
  def discussion(self) -> Optional['NewsfeedDiscussion']:
    return self._discussion

  @discussion.setter
  def discussion(self, discussion: Optional['NewsfeedDiscussion']):
    if discussion is None:
      del self.discussion
      return
    if not isinstance(discussion, NewsfeedDiscussion):
      raise TypeError('discussion must be of type NewsfeedDiscussion')
    self._discussion = discussion

  @property
  def is_following_item(self) -> bool:
    return self._is_following_item or False

  @is_following_item.setter
  def is_following_item(self, is_following_item: Optional[bool]):
    if is_following_item is None:
      del self.is_following_item
      return
    if not isinstance(is_following_item, bool):
      raise TypeError('is_following_item must be of type bool')
    self._is_following_item = is_following_item

  @property
  def is_following_user(self) -> bool:
    return self._is_following_user or False

  @is_following_user.setter
  def is_following_user(self, is_following_user: Optional[bool]):
    if is_following_user is None:
      del self.is_following_user
      return
    if not isinstance(is_following_user, bool):
      raise TypeError('is_following_user must be of type bool')
    self._is_following_user = is_following_user

  @property
  def kernel(self) -> Optional['NewsfeedKernel']:
    return self._kernel

  @kernel.setter
  def kernel(self, kernel: Optional['NewsfeedKernel']):
    if kernel is None:
      del self.kernel
      return
    if not isinstance(kernel, NewsfeedKernel):
      raise TypeError('kernel must be of type NewsfeedKernel')
    self._kernel = kernel

  @property
  def owner_organization(self) -> Optional['Organization']:
    """Owners can be either a user or an organization"""
    return self._owner_organization

  @owner_organization.setter
  def owner_organization(self, owner_organization: Optional['Organization']):
    if owner_organization is None:
      del self.owner_organization
      return
    if not isinstance(owner_organization, Organization):
      raise TypeError('owner_organization must be of type Organization')
    self._owner_organization = owner_organization

  @property
  def owner_user(self) -> Optional['User']:
    return self._owner_user

  @owner_user.setter
  def owner_user(self, owner_user: Optional['User']):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, User):
      raise TypeError('owner_user must be of type User')
    self._owner_user = owner_user

  @property
  def story_info(self) -> Optional['NewsfeedStoryInfo']:
    return self._story_info

  @story_info.setter
  def story_info(self, story_info: Optional['NewsfeedStoryInfo']):
    if story_info is None:
      del self.story_info
      return
    if not isinstance(story_info, NewsfeedStoryInfo):
      raise TypeError('story_info must be of type NewsfeedStoryInfo')
    self._story_info = story_info

  @property
  def vote(self) -> Optional['NewsfeedVote']:
    return self._vote

  @vote.setter
  def vote(self, vote: Optional['NewsfeedVote']):
    if vote is None:
      del self.vote
      return
    if not isinstance(vote, NewsfeedVote):
      raise TypeError('vote must be of type NewsfeedVote')
    self._vote = vote


class NewsfeedStoryInfo(KaggleObject):
  r"""
  Attributes:
    experiment_id (str)
    id (int)
    sort_id (int)
    story_type (ItemType)
  """

  def __init__(self):
    self._experiment_id = ""
    self._id = 0
    self._sort_id = 0
    self._story_type = ItemType.ITEM_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def experiment_id(self) -> str:
    return self._experiment_id

  @experiment_id.setter
  def experiment_id(self, experiment_id: str):
    if experiment_id is None:
      del self.experiment_id
      return
    if not isinstance(experiment_id, str):
      raise TypeError('experiment_id must be of type str')
    self._experiment_id = experiment_id

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
  def sort_id(self) -> int:
    return self._sort_id

  @sort_id.setter
  def sort_id(self, sort_id: int):
    if sort_id is None:
      del self.sort_id
      return
    if not isinstance(sort_id, int):
      raise TypeError('sort_id must be of type int')
    self._sort_id = sort_id

  @property
  def story_type(self) -> 'ItemType':
    return self._story_type

  @story_type.setter
  def story_type(self, story_type: 'ItemType'):
    if story_type is None:
      del self.story_type
      return
    if not isinstance(story_type, ItemType):
      raise TypeError('story_type must be of type ItemType')
    self._story_type = story_type


class NewsfeedVote(KaggleObject):
  r"""
  Attributes:
    can_downvote (bool)
    can_upvote (bool)
    has_already_downvoted (bool)
    has_already_upvoted (bool)
    vote_count (int)
    kernel_id (int)
    dataset_id (int)
    forum_message_id (int)
  """

  def __init__(self):
    self._can_downvote = False
    self._can_upvote = False
    self._has_already_downvoted = False
    self._has_already_upvoted = False
    self._vote_count = 0
    self._kernel_id = None
    self._dataset_id = None
    self._forum_message_id = None
    self._freeze()

  @property
  def can_downvote(self) -> bool:
    return self._can_downvote

  @can_downvote.setter
  def can_downvote(self, can_downvote: bool):
    if can_downvote is None:
      del self.can_downvote
      return
    if not isinstance(can_downvote, bool):
      raise TypeError('can_downvote must be of type bool')
    self._can_downvote = can_downvote

  @property
  def can_upvote(self) -> bool:
    return self._can_upvote

  @can_upvote.setter
  def can_upvote(self, can_upvote: bool):
    if can_upvote is None:
      del self.can_upvote
      return
    if not isinstance(can_upvote, bool):
      raise TypeError('can_upvote must be of type bool')
    self._can_upvote = can_upvote

  @property
  def has_already_downvoted(self) -> bool:
    return self._has_already_downvoted

  @has_already_downvoted.setter
  def has_already_downvoted(self, has_already_downvoted: bool):
    if has_already_downvoted is None:
      del self.has_already_downvoted
      return
    if not isinstance(has_already_downvoted, bool):
      raise TypeError('has_already_downvoted must be of type bool')
    self._has_already_downvoted = has_already_downvoted

  @property
  def has_already_upvoted(self) -> bool:
    return self._has_already_upvoted

  @has_already_upvoted.setter
  def has_already_upvoted(self, has_already_upvoted: bool):
    if has_already_upvoted is None:
      del self.has_already_upvoted
      return
    if not isinstance(has_already_upvoted, bool):
      raise TypeError('has_already_upvoted must be of type bool')
    self._has_already_upvoted = has_already_upvoted

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
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id or 0

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: Optional[int]):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    self._forum_message_id = forum_message_id


class Organization(KaggleObject):
  r"""
  Attributes:
    id (int)
    creation_date (datetime)
    name (str)
    creator_user (User)
    url (str)
    thumbnail_url (str)
    join_date (datetime)
    location (str)
    dataset_count (int)
    competition_count (int)
    member_count (int)
  """

  def __init__(self):
    self._id = 0
    self._creation_date = None
    self._name = ""
    self._creator_user = None
    self._url = ""
    self._thumbnail_url = ""
    self._join_date = None
    self._location = ""
    self._dataset_count = 0
    self._competition_count = 0
    self._member_count = 0
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
  def creation_date(self) -> datetime:
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date

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
  def creator_user(self) -> Optional['User']:
    return self._creator_user

  @creator_user.setter
  def creator_user(self, creator_user: Optional['User']):
    if creator_user is None:
      del self.creator_user
      return
    if not isinstance(creator_user, User):
      raise TypeError('creator_user must be of type User')
    self._creator_user = creator_user

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
  def thumbnail_url(self) -> str:
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def join_date(self) -> datetime:
    return self._join_date

  @join_date.setter
  def join_date(self, join_date: datetime):
    if join_date is None:
      del self.join_date
      return
    if not isinstance(join_date, datetime):
      raise TypeError('join_date must be of type datetime')
    self._join_date = join_date

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


class SetDsSurveyBannerStateRequest(KaggleObject):
  r"""
  Attributes:
    dismissed (bool)
    clicked (bool)
  """

  def __init__(self):
    self._dismissed = False
    self._clicked = False
    self._freeze()

  @property
  def dismissed(self) -> bool:
    return self._dismissed

  @dismissed.setter
  def dismissed(self, dismissed: bool):
    if dismissed is None:
      del self.dismissed
      return
    if not isinstance(dismissed, bool):
      raise TypeError('dismissed must be of type bool')
    self._dismissed = dismissed

  @property
  def clicked(self) -> bool:
    return self._clicked

  @clicked.setter
  def clicked(self, clicked: bool):
    if clicked is None:
      del self.clicked
      return
    if not isinstance(clicked, bool):
      raise TypeError('clicked must be of type bool')
    self._clicked = clicked


GetDsSurveyBannerStateRequest._fields = []

GetDsSurveyBannerStateResponse._fields = [
  FieldMetadata("showBanner", "show_banner", "_show_banner", bool, False, PredefinedSerializer()),
]

GetNewAndExcitingContentRequest._fields = []

GetNewAndExcitingContentResponse._fields = [
  FieldMetadata("items", "items", "_items", NewAndExcitingItem, [], ListSerializer(KaggleObjectSerializer())),
]

GetNewsfeedSidebarContentRequest._fields = []

GetStoriesRequest._fields = [
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
]

GetStoriesResponse._fields = [
  FieldMetadata("stories", "stories", "_stories", NewsfeedStory, [], ListSerializer(KaggleObjectSerializer())),
]

NewAndExcitingItem._fields = [
  FieldMetadata("category", "category", "_category", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

NewsfeedBlog._fields = [
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("summary", "summary", "_summary", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

NewsfeedCompetition._fields = [
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("currentUserRank", "current_user_rank", "_current_user_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("overview", "overview", "_overview", NewsfeedCompetitionOverview, None, KaggleObjectSerializer()),
  FieldMetadata("resultsAreFinal", "results_are_final", "_results_are_final", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rewardQuantity", "reward_quantity", "_reward_quantity", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rewardType", "reward_type", "_reward_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teams", "teams", "_teams", NewsfeedCompetitionTeam, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalEnteredTeams", "total_entered_teams", "_total_entered_teams", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topSolutionWriteUpUrl", "top_solution_write_up_url", "_top_solution_write_up_url", str, None, PredefinedSerializer(), optional=True),
]

NewsfeedCompetitionOverview._fields = [
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", str, "", PredefinedSerializer()),
]

NewsfeedCompetitionTeam._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("team", "team", "_team", Team, None, KaggleObjectSerializer()),
  FieldMetadata("users", "users", "_users", User, [], ListSerializer(KaggleObjectSerializer())),
]

NewsfeedDataset._fields = [
  FieldMetadata("commonFileType", "common_file_type", "_common_file_type", DatasetFileType, DatasetFileType.DATASET_FILE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetIsDeleted", "dataset_is_deleted", "_dataset_is_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseName", "license_name", "_license_name", str, "", PredefinedSerializer()),
  FieldMetadata("overview", "overview", "_overview", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalSize", "total_size", "_total_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalFiles", "total_files", "_total_files", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalKernels", "total_kernels", "_total_kernels", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalTopics", "total_topics", "_total_topics", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalViews", "total_views", "_total_views", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, "", PredefinedSerializer()),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
]

NewsfeedDiscussion._fields = [
  FieldMetadata("forumName", "forum_name", "_forum_name", str, "", PredefinedSerializer()),
  FieldMetadata("forumUrl", "forum_url", "_forum_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageId", "message_id", "_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageRawHtml", "message_raw_html", "_message_raw_html", str, "", PredefinedSerializer()),
  FieldMetadata("messageRawMarkdown", "message_raw_markdown", "_message_raw_markdown", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageUrl", "message_url", "_message_url", str, "", PredefinedSerializer()),
  FieldMetadata("topicDate", "topic_date", "_topic_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicName", "topic_name", "_topic_name", str, "", PredefinedSerializer()),
  FieldMetadata("topicRawHtml", "topic_raw_html", "_topic_raw_html", str, "", PredefinedSerializer()),
  FieldMetadata("topicRawMarkdown", "topic_raw_markdown", "_topic_raw_markdown", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicUrl", "topic_url", "_topic_url", str, "", PredefinedSerializer()),
]

NewsfeedKernel._fields = [
  FieldMetadata("commentCount", "comment_count", "_comment_count", int, 0, PredefinedSerializer()),
  FieldMetadata("dataUrl", "data_url", "_data_url", str, "", PredefinedSerializer()),
  FieldMetadata("disableComments", "disable_comments", "_disable_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("fileOutputCount", "file_output_count", "_file_output_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasMultipleDataSources", "has_multiple_data_sources", "_has_multiple_data_sources", bool, False, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", EditorType, EditorType.EDITOR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("language", "language", "_language", str, "", PredefinedSerializer()),
  FieldMetadata("lineCount", "line_count", "_line_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("runTimeSeconds", "run_time_seconds", "_run_time_seconds", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("views", "views", "_views", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("visualizationUrls", "visualization_urls", "_visualization_urls", str, [], ListSerializer(PredefinedSerializer())),
]

NewsfeedSidebarContent._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("avatarUrl", "avatar_url", "_avatar_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userUrl", "user_url", "_user_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("userJoinDate", "user_join_date", "_user_join_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("progression", "progression", "_progression", GetCurrentUserProgressionResponse, None, KaggleObjectSerializer()),
  FieldMetadata("competitionSidebarList", "competition_sidebar_list", "_competition_sidebar_list", NewsfeedSidebarItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("datasetSidebarList", "dataset_sidebar_list", "_dataset_sidebar_list", NewsfeedSidebarItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("kernelSidebarList", "kernel_sidebar_list", "_kernel_sidebar_list", NewsfeedSidebarItem, [], ListSerializer(KaggleObjectSerializer())),
]

NewsfeedSidebarItem._fields = [
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("linkUrl", "link_url", "_link_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("icon", "icon", "_icon", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("iconTitle", "icon_title", "_icon_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("iconRight", "icon_right", "_icon_right", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("iconRightTitle", "icon_right_title", "_icon_right_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
]

NewsfeedStory._fields = [
  FieldMetadata("actionUser", "action_user", "_action_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("blog", "blog", "_blog", NewsfeedBlog, None, KaggleObjectSerializer()),
  FieldMetadata("competition", "competition", "_competition", NewsfeedCompetition, None, KaggleObjectSerializer()),
  FieldMetadata("dataset", "dataset", "_dataset", NewsfeedDataset, None, KaggleObjectSerializer()),
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("discussion", "discussion", "_discussion", NewsfeedDiscussion, None, KaggleObjectSerializer()),
  FieldMetadata("isFollowingItem", "is_following_item", "_is_following_item", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isFollowingUser", "is_following_user", "_is_following_user", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernel", "kernel", "_kernel", NewsfeedKernel, None, KaggleObjectSerializer()),
  FieldMetadata("ownerOrganization", "owner_organization", "_owner_organization", Organization, None, KaggleObjectSerializer()),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("storyInfo", "story_info", "_story_info", NewsfeedStoryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("vote", "vote", "_vote", NewsfeedVote, None, KaggleObjectSerializer()),
]

NewsfeedStoryInfo._fields = [
  FieldMetadata("experimentId", "experiment_id", "_experiment_id", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sortId", "sort_id", "_sort_id", int, 0, PredefinedSerializer()),
  FieldMetadata("storyType", "story_type", "_story_type", ItemType, ItemType.ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
]

NewsfeedVote._fields = [
  FieldMetadata("canDownvote", "can_downvote", "_can_downvote", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpvote", "can_upvote", "_can_upvote", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAlreadyDownvoted", "has_already_downvoted", "_has_already_downvoted", bool, False, PredefinedSerializer()),
  FieldMetadata("hasAlreadyUpvoted", "has_already_upvoted", "_has_already_upvoted", bool, False, PredefinedSerializer()),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, None, PredefinedSerializer(), optional=True),
]

Organization._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("creatorUser", "creator_user", "_creator_user", User, None, KaggleObjectSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("joinDate", "join_date", "_join_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("location", "location", "_location", str, "", PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("memberCount", "member_count", "_member_count", int, 0, PredefinedSerializer()),
]

SetDsSurveyBannerStateRequest._fields = [
  FieldMetadata("dismissed", "dismissed", "_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("clicked", "clicked", "_clicked", bool, False, PredefinedSerializer()),
]

