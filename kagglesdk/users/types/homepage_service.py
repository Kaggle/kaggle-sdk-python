from datetime import datetime
from kagglesdk.benchmarks.types.benchmark_types import Benchmark
from kagglesdk.competitions.types.competition import Competition
from kagglesdk.datasets.types.dataset_service import DatasetListItem
from kagglesdk.discussions.types.topic_list_item import TopicListItem
from kagglesdk.education.types.education_service import LearnTrack
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_types import KernelListItem
from kagglesdk.models.types.model_types import Model
from kagglesdk.newsfeed.types.newsfeed_web_service import NewAndExcitingItem
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class AddSuggestedItemRequest(KaggleObject):
  r"""
  """

  pass

class AddSuggestedItemResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
      The Id of the newly created suggested item.
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The Id of the newly created suggested item."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class CreationCounts(KaggleObject):
  r"""
  Attributes:
    total_count (int)
      The total number of items created ever by the user.
    last_month_count (int)
      The number created within the last month
  """

  def __init__(self):
    self._total_count = 0
    self._last_month_count = 0
    self._freeze()

  @property
  def total_count(self) -> int:
    """The total number of items created ever by the user."""
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def last_month_count(self) -> int:
    """The number created within the last month"""
    return self._last_month_count

  @last_month_count.setter
  def last_month_count(self, last_month_count: int):
    if last_month_count is None:
      del self.last_month_count
      return
    if not isinstance(last_month_count, int):
      raise TypeError('last_month_count must be of type int')
    self._last_month_count = last_month_count


class DismissSuggestedItemRequest(KaggleObject):
  r"""
  Attributes:
    suggested_item_id (int)
      The id of the suggested item to dismiss.
  """

  def __init__(self):
    self._suggested_item_id = 0
    self._freeze()

  @property
  def suggested_item_id(self) -> int:
    """The id of the suggested item to dismiss."""
    return self._suggested_item_id

  @suggested_item_id.setter
  def suggested_item_id(self, suggested_item_id: int):
    if suggested_item_id is None:
      del self.suggested_item_id
      return
    if not isinstance(suggested_item_id, int):
      raise TypeError('suggested_item_id must be of type int')
    self._suggested_item_id = suggested_item_id


class EntityCountData(KaggleObject):
  r"""
  Approximate counts of products across Kaggle for use on the logged-out
  homepage. These are rounded when used, so accuracy is not a top priority.
  Some fields use int64 because data is sourced from ElasticSearch, which gives
  int64.

  Attributes:
    competition_count (int)
    competition_solution_count (int)
    dataset_count (int)
    kernel_count (int)
    learn_total_hours (int)
    model_count (int)
    user_count (int)
  """

  def __init__(self):
    self._competition_count = 0
    self._competition_solution_count = 0
    self._dataset_count = 0
    self._kernel_count = 0
    self._learn_total_hours = 0
    self._model_count = 0
    self._user_count = 0
    self._freeze()

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
  def competition_solution_count(self) -> int:
    return self._competition_solution_count

  @competition_solution_count.setter
  def competition_solution_count(self, competition_solution_count: int):
    if competition_solution_count is None:
      del self.competition_solution_count
      return
    if not isinstance(competition_solution_count, int):
      raise TypeError('competition_solution_count must be of type int')
    self._competition_solution_count = competition_solution_count

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
  def kernel_count(self) -> int:
    return self._kernel_count

  @kernel_count.setter
  def kernel_count(self, kernel_count: int):
    if kernel_count is None:
      del self.kernel_count
      return
    if not isinstance(kernel_count, int):
      raise TypeError('kernel_count must be of type int')
    self._kernel_count = kernel_count

  @property
  def learn_total_hours(self) -> int:
    return self._learn_total_hours

  @learn_total_hours.setter
  def learn_total_hours(self, learn_total_hours: int):
    if learn_total_hours is None:
      del self.learn_total_hours
      return
    if not isinstance(learn_total_hours, int):
      raise TypeError('learn_total_hours must be of type int')
    self._learn_total_hours = learn_total_hours

  @property
  def model_count(self) -> int:
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
  def user_count(self) -> int:
    return self._user_count

  @user_count.setter
  def user_count(self, user_count: int):
    if user_count is None:
      del self.user_count
      return
    if not isinstance(user_count, int):
      raise TypeError('user_count must be of type int')
    self._user_count = user_count


class EntityListingData(KaggleObject):
  r"""
  Listing results for rendering in product shelves on the logged-out homepage.

  Attributes:
    competitions (Competition)
    competition_solutions (TopicListItem)
    datasets (DatasetListItem)
    kernels (KernelListItem)
    models (Model)
    learn_courses (LearnTrack)
    benchmarks (Benchmark)
  """

  def __init__(self):
    self._competitions = []
    self._competition_solutions = []
    self._datasets = []
    self._kernels = []
    self._models = []
    self._learn_courses = []
    self._benchmarks = []
    self._freeze()

  @property
  def competitions(self) -> Optional[List[Optional['Competition']]]:
    return self._competitions

  @competitions.setter
  def competitions(self, competitions: Optional[List[Optional['Competition']]]):
    if competitions is None:
      del self.competitions
      return
    if not isinstance(competitions, list):
      raise TypeError('competitions must be of type list')
    if not all([isinstance(t, Competition) for t in competitions]):
      raise TypeError('competitions must contain only items of type Competition')
    self._competitions = competitions

  @property
  def competition_solutions(self) -> Optional[List[Optional['TopicListItem']]]:
    return self._competition_solutions

  @competition_solutions.setter
  def competition_solutions(self, competition_solutions: Optional[List[Optional['TopicListItem']]]):
    if competition_solutions is None:
      del self.competition_solutions
      return
    if not isinstance(competition_solutions, list):
      raise TypeError('competition_solutions must be of type list')
    if not all([isinstance(t, TopicListItem) for t in competition_solutions]):
      raise TypeError('competition_solutions must contain only items of type TopicListItem')
    self._competition_solutions = competition_solutions

  @property
  def datasets(self) -> Optional[List[Optional['DatasetListItem']]]:
    return self._datasets

  @datasets.setter
  def datasets(self, datasets: Optional[List[Optional['DatasetListItem']]]):
    if datasets is None:
      del self.datasets
      return
    if not isinstance(datasets, list):
      raise TypeError('datasets must be of type list')
    if not all([isinstance(t, DatasetListItem) for t in datasets]):
      raise TypeError('datasets must contain only items of type DatasetListItem')
    self._datasets = datasets

  @property
  def kernels(self) -> Optional[List[Optional['KernelListItem']]]:
    return self._kernels

  @kernels.setter
  def kernels(self, kernels: Optional[List[Optional['KernelListItem']]]):
    if kernels is None:
      del self.kernels
      return
    if not isinstance(kernels, list):
      raise TypeError('kernels must be of type list')
    if not all([isinstance(t, KernelListItem) for t in kernels]):
      raise TypeError('kernels must contain only items of type KernelListItem')
    self._kernels = kernels

  @property
  def models(self) -> Optional[List[Optional['Model']]]:
    return self._models

  @models.setter
  def models(self, models: Optional[List[Optional['Model']]]):
    if models is None:
      del self.models
      return
    if not isinstance(models, list):
      raise TypeError('models must be of type list')
    if not all([isinstance(t, Model) for t in models]):
      raise TypeError('models must contain only items of type Model')
    self._models = models

  @property
  def learn_courses(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._learn_courses

  @learn_courses.setter
  def learn_courses(self, learn_courses: Optional[List[Optional['LearnTrack']]]):
    if learn_courses is None:
      del self.learn_courses
      return
    if not isinstance(learn_courses, list):
      raise TypeError('learn_courses must be of type list')
    if not all([isinstance(t, LearnTrack) for t in learn_courses]):
      raise TypeError('learn_courses must contain only items of type LearnTrack')
    self._learn_courses = learn_courses

  @property
  def benchmarks(self) -> Optional[List[Optional['Benchmark']]]:
    return self._benchmarks

  @benchmarks.setter
  def benchmarks(self, benchmarks: Optional[List[Optional['Benchmark']]]):
    if benchmarks is None:
      del self.benchmarks
      return
    if not isinstance(benchmarks, list):
      raise TypeError('benchmarks must be of type list')
    if not all([isinstance(t, Benchmark) for t in benchmarks]):
      raise TypeError('benchmarks must contain only items of type Benchmark')
    self._benchmarks = benchmarks


class ForceUpdateLoggedOutHomepageDataRequest(KaggleObject):
  r"""
  """

  pass

class GetHomePageStatsRequest(KaggleObject):
  r"""
  """

  pass

class GetHomePageStatsResponse(KaggleObject):
  r"""
  Attributes:
    datasets (CreationCounts)
      Datasets created in the last month.
    notebooks (CreationCounts)
      Notebooks created in the last month.
    discussions (CreationCounts)
      Topics and comments created by user.
    competitions (CreationCounts)
      Competitions the user has entered.
    courses (CreationCounts)
      Courses the user has completed.
    max_day_streak (int)
      The longest streak of days a user has ever had.
    current_day_streak (int)
      The current streak of days.
  """

  def __init__(self):
    self._datasets = None
    self._notebooks = None
    self._discussions = None
    self._competitions = None
    self._courses = None
    self._max_day_streak = 0
    self._current_day_streak = 0
    self._freeze()

  @property
  def datasets(self) -> Optional['CreationCounts']:
    """Datasets created in the last month."""
    return self._datasets

  @datasets.setter
  def datasets(self, datasets: Optional['CreationCounts']):
    if datasets is None:
      del self.datasets
      return
    if not isinstance(datasets, CreationCounts):
      raise TypeError('datasets must be of type CreationCounts')
    self._datasets = datasets

  @property
  def notebooks(self) -> Optional['CreationCounts']:
    """Notebooks created in the last month."""
    return self._notebooks

  @notebooks.setter
  def notebooks(self, notebooks: Optional['CreationCounts']):
    if notebooks is None:
      del self.notebooks
      return
    if not isinstance(notebooks, CreationCounts):
      raise TypeError('notebooks must be of type CreationCounts')
    self._notebooks = notebooks

  @property
  def discussions(self) -> Optional['CreationCounts']:
    """Topics and comments created by user."""
    return self._discussions

  @discussions.setter
  def discussions(self, discussions: Optional['CreationCounts']):
    if discussions is None:
      del self.discussions
      return
    if not isinstance(discussions, CreationCounts):
      raise TypeError('discussions must be of type CreationCounts')
    self._discussions = discussions

  @property
  def competitions(self) -> Optional['CreationCounts']:
    """Competitions the user has entered."""
    return self._competitions

  @competitions.setter
  def competitions(self, competitions: Optional['CreationCounts']):
    if competitions is None:
      del self.competitions
      return
    if not isinstance(competitions, CreationCounts):
      raise TypeError('competitions must be of type CreationCounts')
    self._competitions = competitions

  @property
  def courses(self) -> Optional['CreationCounts']:
    """Courses the user has completed."""
    return self._courses

  @courses.setter
  def courses(self, courses: Optional['CreationCounts']):
    if courses is None:
      del self.courses
      return
    if not isinstance(courses, CreationCounts):
      raise TypeError('courses must be of type CreationCounts')
    self._courses = courses

  @property
  def max_day_streak(self) -> int:
    """The longest streak of days a user has ever had."""
    return self._max_day_streak

  @max_day_streak.setter
  def max_day_streak(self, max_day_streak: int):
    if max_day_streak is None:
      del self.max_day_streak
      return
    if not isinstance(max_day_streak, int):
      raise TypeError('max_day_streak must be of type int')
    self._max_day_streak = max_day_streak

  @property
  def current_day_streak(self) -> int:
    """The current streak of days."""
    return self._current_day_streak

  @current_day_streak.setter
  def current_day_streak(self, current_day_streak: int):
    if current_day_streak is None:
      del self.current_day_streak
      return
    if not isinstance(current_day_streak, int):
      raise TypeError('current_day_streak must be of type int')
    self._current_day_streak = current_day_streak


class GetLoggedOutHomepageDataRequest(KaggleObject):
  r"""
  """

  pass

class GetLoggedOutHomepageDataResponse(KaggleObject):
  r"""
  Count and listing data used to render the logged-out homepage (2023). See:
  go/k-logged-out-homepage-23-dd

  Attributes:
    count_data (EntityCountData)
    listing_data (EntityListingData)
    new_and_exciting_items (NewAndExcitingItem)
  """

  def __init__(self):
    self._count_data = None
    self._listing_data = None
    self._new_and_exciting_items = []
    self._freeze()

  @property
  def count_data(self) -> Optional['EntityCountData']:
    return self._count_data

  @count_data.setter
  def count_data(self, count_data: Optional['EntityCountData']):
    if count_data is None:
      del self.count_data
      return
    if not isinstance(count_data, EntityCountData):
      raise TypeError('count_data must be of type EntityCountData')
    self._count_data = count_data

  @property
  def listing_data(self) -> Optional['EntityListingData']:
    return self._listing_data

  @listing_data.setter
  def listing_data(self, listing_data: Optional['EntityListingData']):
    if listing_data is None:
      del self.listing_data
      return
    if not isinstance(listing_data, EntityListingData):
      raise TypeError('listing_data must be of type EntityListingData')
    self._listing_data = listing_data

  @property
  def new_and_exciting_items(self) -> Optional[List[Optional['NewAndExcitingItem']]]:
    return self._new_and_exciting_items

  @new_and_exciting_items.setter
  def new_and_exciting_items(self, new_and_exciting_items: Optional[List[Optional['NewAndExcitingItem']]]):
    if new_and_exciting_items is None:
      del self.new_and_exciting_items
      return
    if not isinstance(new_and_exciting_items, list):
      raise TypeError('new_and_exciting_items must be of type list')
    if not all([isinstance(t, NewAndExcitingItem) for t in new_and_exciting_items]):
      raise TypeError('new_and_exciting_items must contain only items of type NewAndExcitingItem')
    self._new_and_exciting_items = new_and_exciting_items


class GetNextStepsConfigRequest(KaggleObject):
  r"""
  """

  pass

class GetNextStepsConfigResponse(KaggleObject):
  r"""
  Attributes:
    suggested_items (SuggestedItem)
  """

  def __init__(self):
    self._suggested_items = []
    self._freeze()

  @property
  def suggested_items(self) -> Optional[List[Optional['SuggestedItem']]]:
    return self._suggested_items

  @suggested_items.setter
  def suggested_items(self, suggested_items: Optional[List[Optional['SuggestedItem']]]):
    if suggested_items is None:
      del self.suggested_items
      return
    if not isinstance(suggested_items, list):
      raise TypeError('suggested_items must be of type list')
    if not all([isinstance(t, SuggestedItem) for t in suggested_items]):
      raise TypeError('suggested_items must contain only items of type SuggestedItem')
    self._suggested_items = suggested_items


class GetNextStepsRequest(KaggleObject):
  r"""
  """

  pass

class GetNextStepsResponse(KaggleObject):
  r"""
  Attributes:
    jump_back_in_items (JumpBackInItem)
      A list of items to show under 'Jump Back In'. Empty if nothing should be
      shown.
    suggested_items (SuggestedItem)
      A list of items to show under 'More to Do'. Could be progression related
      suggestions.
  """

  def __init__(self):
    self._jump_back_in_items = []
    self._suggested_items = []
    self._freeze()

  @property
  def jump_back_in_items(self) -> Optional[List[Optional['JumpBackInItem']]]:
    r"""
    A list of items to show under 'Jump Back In'. Empty if nothing should be
    shown.
    """
    return self._jump_back_in_items

  @jump_back_in_items.setter
  def jump_back_in_items(self, jump_back_in_items: Optional[List[Optional['JumpBackInItem']]]):
    if jump_back_in_items is None:
      del self.jump_back_in_items
      return
    if not isinstance(jump_back_in_items, list):
      raise TypeError('jump_back_in_items must be of type list')
    if not all([isinstance(t, JumpBackInItem) for t in jump_back_in_items]):
      raise TypeError('jump_back_in_items must contain only items of type JumpBackInItem')
    self._jump_back_in_items = jump_back_in_items

  @property
  def suggested_items(self) -> Optional[List[Optional['SuggestedItem']]]:
    r"""
    A list of items to show under 'More to Do'. Could be progression related
    suggestions.
    """
    return self._suggested_items

  @suggested_items.setter
  def suggested_items(self, suggested_items: Optional[List[Optional['SuggestedItem']]]):
    if suggested_items is None:
      del self.suggested_items
      return
    if not isinstance(suggested_items, list):
      raise TypeError('suggested_items must be of type list')
    if not all([isinstance(t, SuggestedItem) for t in suggested_items]):
      raise TypeError('suggested_items must contain only items of type SuggestedItem')
    self._suggested_items = suggested_items


class JumpBackInCompetition(KaggleObject):
  r"""
  Attributes:
    deadline (datetime)
      The deadline for the competition.
    latest_submission_public_score_formatted (str)
      The score of the last submission, if any.
  """

  def __init__(self):
    self._deadline = None
    self._latest_submission_public_score_formatted = None
    self._freeze()

  @property
  def deadline(self) -> datetime:
    """The deadline for the competition."""
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
  def latest_submission_public_score_formatted(self) -> str:
    """The score of the last submission, if any."""
    return self._latest_submission_public_score_formatted or ""

  @latest_submission_public_score_formatted.setter
  def latest_submission_public_score_formatted(self, latest_submission_public_score_formatted: Optional[str]):
    if latest_submission_public_score_formatted is None:
      del self.latest_submission_public_score_formatted
      return
    if not isinstance(latest_submission_public_score_formatted, str):
      raise TypeError('latest_submission_public_score_formatted must be of type str')
    self._latest_submission_public_score_formatted = latest_submission_public_score_formatted


class JumpBackInItem(KaggleObject):
  r"""
  Attributes:
    action_url (str)
      The URL to send the user when they interact with this item.
    image_url (str)
      THe URL of the image to show.
    title (str)
      The title for the item (the name of the dataset/notebook/competition)
    competition (JumpBackInCompetition)
      A competition the user is entered in.
    public_dataset (JumpBackInPublicDataset)
      A public dataset the user owns.
    private_dataset (JumpBackInPrivateDataset)
      A private dataset the user owns.
    public_notebook (JumpBackInPublicNotebook)
      A public notebook the user owns.
    private_notebook (JumpBackInPrivateNotebook)
      A private notebook the user owns.
    learn_course_notebook (JumpBackInLearnCourseNotebook)
      A notebook corresponding to a learn course.
    avatar (UserAvatar)
      The avatar to show.
    id (int)
      The id of the item (used for metrics tracking).
  """

  def __init__(self):
    self._action_url = ""
    self._image_url = None
    self._title = ""
    self._competition = None
    self._public_dataset = None
    self._private_dataset = None
    self._public_notebook = None
    self._private_notebook = None
    self._learn_course_notebook = None
    self._avatar = None
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the item (used for metrics tracking)."""
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
  def action_url(self) -> str:
    """The URL to send the user when they interact with this item."""
    return self._action_url

  @action_url.setter
  def action_url(self, action_url: str):
    if action_url is None:
      del self.action_url
      return
    if not isinstance(action_url, str):
      raise TypeError('action_url must be of type str')
    self._action_url = action_url

  @property
  def title(self) -> str:
    """The title for the item (the name of the dataset/notebook/competition)"""
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
  def image_url(self) -> str:
    """THe URL of the image to show."""
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    del self.avatar
    self._image_url = image_url

  @property
  def avatar(self) -> Optional['UserAvatar']:
    """The avatar to show."""
    return self._avatar or None

  @avatar.setter
  def avatar(self, avatar: Optional['UserAvatar']):
    if avatar is None:
      del self.avatar
      return
    if not isinstance(avatar, UserAvatar):
      raise TypeError('avatar must be of type UserAvatar')
    del self.image_url
    self._avatar = avatar

  @property
  def competition(self) -> Optional['JumpBackInCompetition']:
    """A competition the user is entered in."""
    return self._competition or None

  @competition.setter
  def competition(self, competition: Optional['JumpBackInCompetition']):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, JumpBackInCompetition):
      raise TypeError('competition must be of type JumpBackInCompetition')
    del self.public_dataset
    del self.private_dataset
    del self.public_notebook
    del self.private_notebook
    del self.learn_course_notebook
    self._competition = competition

  @property
  def public_dataset(self) -> Optional['JumpBackInPublicDataset']:
    """A public dataset the user owns."""
    return self._public_dataset or None

  @public_dataset.setter
  def public_dataset(self, public_dataset: Optional['JumpBackInPublicDataset']):
    if public_dataset is None:
      del self.public_dataset
      return
    if not isinstance(public_dataset, JumpBackInPublicDataset):
      raise TypeError('public_dataset must be of type JumpBackInPublicDataset')
    del self.competition
    del self.private_dataset
    del self.public_notebook
    del self.private_notebook
    del self.learn_course_notebook
    self._public_dataset = public_dataset

  @property
  def private_dataset(self) -> Optional['JumpBackInPrivateDataset']:
    """A private dataset the user owns."""
    return self._private_dataset or None

  @private_dataset.setter
  def private_dataset(self, private_dataset: Optional['JumpBackInPrivateDataset']):
    if private_dataset is None:
      del self.private_dataset
      return
    if not isinstance(private_dataset, JumpBackInPrivateDataset):
      raise TypeError('private_dataset must be of type JumpBackInPrivateDataset')
    del self.competition
    del self.public_dataset
    del self.public_notebook
    del self.private_notebook
    del self.learn_course_notebook
    self._private_dataset = private_dataset

  @property
  def public_notebook(self) -> Optional['JumpBackInPublicNotebook']:
    """A public notebook the user owns."""
    return self._public_notebook or None

  @public_notebook.setter
  def public_notebook(self, public_notebook: Optional['JumpBackInPublicNotebook']):
    if public_notebook is None:
      del self.public_notebook
      return
    if not isinstance(public_notebook, JumpBackInPublicNotebook):
      raise TypeError('public_notebook must be of type JumpBackInPublicNotebook')
    del self.competition
    del self.public_dataset
    del self.private_dataset
    del self.private_notebook
    del self.learn_course_notebook
    self._public_notebook = public_notebook

  @property
  def private_notebook(self) -> Optional['JumpBackInPrivateNotebook']:
    """A private notebook the user owns."""
    return self._private_notebook or None

  @private_notebook.setter
  def private_notebook(self, private_notebook: Optional['JumpBackInPrivateNotebook']):
    if private_notebook is None:
      del self.private_notebook
      return
    if not isinstance(private_notebook, JumpBackInPrivateNotebook):
      raise TypeError('private_notebook must be of type JumpBackInPrivateNotebook')
    del self.competition
    del self.public_dataset
    del self.private_dataset
    del self.public_notebook
    del self.learn_course_notebook
    self._private_notebook = private_notebook

  @property
  def learn_course_notebook(self) -> Optional['JumpBackInLearnCourseNotebook']:
    """A notebook corresponding to a learn course."""
    return self._learn_course_notebook or None

  @learn_course_notebook.setter
  def learn_course_notebook(self, learn_course_notebook: Optional['JumpBackInLearnCourseNotebook']):
    if learn_course_notebook is None:
      del self.learn_course_notebook
      return
    if not isinstance(learn_course_notebook, JumpBackInLearnCourseNotebook):
      raise TypeError('learn_course_notebook must be of type JumpBackInLearnCourseNotebook')
    del self.competition
    del self.public_dataset
    del self.private_dataset
    del self.public_notebook
    del self.private_notebook
    self._learn_course_notebook = learn_course_notebook


class JumpBackInLearnCourseNotebook(KaggleObject):
  r"""
  Attributes:
    course_title (str)
      The title of the course.
    lesson_title (str)
      The title of the lesson within the course.
    progress (float)
      How complete the user is on the course from 0-1.
  """

  def __init__(self):
    self._course_title = ""
    self._lesson_title = ""
    self._progress = 0.0
    self._freeze()

  @property
  def course_title(self) -> str:
    """The title of the course."""
    return self._course_title

  @course_title.setter
  def course_title(self, course_title: str):
    if course_title is None:
      del self.course_title
      return
    if not isinstance(course_title, str):
      raise TypeError('course_title must be of type str')
    self._course_title = course_title

  @property
  def lesson_title(self) -> str:
    """The title of the lesson within the course."""
    return self._lesson_title

  @lesson_title.setter
  def lesson_title(self, lesson_title: str):
    if lesson_title is None:
      del self.lesson_title
      return
    if not isinstance(lesson_title, str):
      raise TypeError('lesson_title must be of type str')
    self._lesson_title = lesson_title

  @property
  def progress(self) -> float:
    """How complete the user is on the course from 0-1."""
    return self._progress

  @progress.setter
  def progress(self, progress: float):
    if progress is None:
      del self.progress
      return
    if not isinstance(progress, float):
      raise TypeError('progress must be of type float')
    self._progress = progress


class JumpBackInPrivateDataset(KaggleObject):
  r"""
  Attributes:
    usability_rating (float)
      The usability rating of the dataset.
    last_version_uploaded (datetime)
      The last time a new version was uploaded.
  """

  def __init__(self):
    self._usability_rating = 0.0
    self._last_version_uploaded = None
    self._freeze()

  @property
  def usability_rating(self) -> float:
    """The usability rating of the dataset."""
    return self._usability_rating

  @usability_rating.setter
  def usability_rating(self, usability_rating: float):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, float):
      raise TypeError('usability_rating must be of type float')
    self._usability_rating = usability_rating

  @property
  def last_version_uploaded(self) -> datetime:
    """The last time a new version was uploaded."""
    return self._last_version_uploaded

  @last_version_uploaded.setter
  def last_version_uploaded(self, last_version_uploaded: datetime):
    if last_version_uploaded is None:
      del self.last_version_uploaded
      return
    if not isinstance(last_version_uploaded, datetime):
      raise TypeError('last_version_uploaded must be of type datetime')
    self._last_version_uploaded = last_version_uploaded


class JumpBackInPrivateNotebook(KaggleObject):
  r"""
  Attributes:
    last_commit_completed_at (datetime)
      The time the last run completed for this notebook.
  """

  def __init__(self):
    self._last_commit_completed_at = None
    self._freeze()

  @property
  def last_commit_completed_at(self) -> datetime:
    """The time the last run completed for this notebook."""
    return self._last_commit_completed_at

  @last_commit_completed_at.setter
  def last_commit_completed_at(self, last_commit_completed_at: datetime):
    if last_commit_completed_at is None:
      del self.last_commit_completed_at
      return
    if not isinstance(last_commit_completed_at, datetime):
      raise TypeError('last_commit_completed_at must be of type datetime')
    self._last_commit_completed_at = last_commit_completed_at


class JumpBackInPublicDataset(KaggleObject):
  r"""
  Attributes:
    total_downloads (int)
      The total number of downloads.
    new_downloads (int)
      The number of new downloads in the last week.
  """

  def __init__(self):
    self._total_downloads = 0
    self._new_downloads = 0
    self._freeze()

  @property
  def total_downloads(self) -> int:
    """The total number of downloads."""
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
  def new_downloads(self) -> int:
    """The number of new downloads in the last week."""
    return self._new_downloads

  @new_downloads.setter
  def new_downloads(self, new_downloads: int):
    if new_downloads is None:
      del self.new_downloads
      return
    if not isinstance(new_downloads, int):
      raise TypeError('new_downloads must be of type int')
    self._new_downloads = new_downloads


class JumpBackInPublicNotebook(KaggleObject):
  r"""
  Attributes:
    total_views (int)
      The total number of views of this notebook.
    new_forks (int)
      The number of forks in the last week.
  """

  def __init__(self):
    self._total_views = 0
    self._new_forks = 0
    self._freeze()

  @property
  def total_views(self) -> int:
    """The total number of views of this notebook."""
    return self._total_views

  @total_views.setter
  def total_views(self, total_views: int):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

  @property
  def new_forks(self) -> int:
    """The number of forks in the last week."""
    return self._new_forks

  @new_forks.setter
  def new_forks(self, new_forks: int):
    if new_forks is None:
      del self.new_forks
      return
    if not isinstance(new_forks, int):
      raise TypeError('new_forks must be of type int')
    self._new_forks = new_forks


class SuggestedItem(KaggleObject):
  r"""
  Attributes:
    title (str)
      The title of the suggestion.
    description (str)
      The description for this suggestion. Can contain markdown (specifically
      markdown links).
    action_url (str)
      The URL that the user is taken to when they click this suggestion.
    icon (str)
      The icon to show for this suggestion.
    id (int)
      The identifier for this suggested item (to take actions on)
    progression_status (SuggestedProgressionStatus)
      If this suggestion is a progression suggestion, the information associated
      with that.
  """

  def __init__(self):
    self._title = ""
    self._description = ""
    self._action_url = ""
    self._icon = ""
    self._id = 0
    self._progression_status = None
    self._freeze()

  @property
  def id(self) -> int:
    """The identifier for this suggested item (to take actions on)"""
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
    """The title of the suggestion."""
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
    r"""
    The description for this suggestion. Can contain markdown (specifically
    markdown links).
    """
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
  def action_url(self) -> str:
    """The URL that the user is taken to when they click this suggestion."""
    return self._action_url

  @action_url.setter
  def action_url(self, action_url: str):
    if action_url is None:
      del self.action_url
      return
    if not isinstance(action_url, str):
      raise TypeError('action_url must be of type str')
    self._action_url = action_url

  @property
  def icon(self) -> str:
    """The icon to show for this suggestion."""
    return self._icon

  @icon.setter
  def icon(self, icon: str):
    if icon is None:
      del self.icon
      return
    if not isinstance(icon, str):
      raise TypeError('icon must be of type str')
    self._icon = icon

  @property
  def progression_status(self) -> Optional['SuggestedProgressionStatus']:
    r"""
    If this suggestion is a progression suggestion, the information associated
    with that.
    """
    return self._progression_status

  @progression_status.setter
  def progression_status(self, progression_status: Optional['SuggestedProgressionStatus']):
    if progression_status is None:
      del self.progression_status
      return
    if not isinstance(progression_status, SuggestedProgressionStatus):
      raise TypeError('progression_status must be of type SuggestedProgressionStatus')
    self._progression_status = progression_status


class SuggestedProgressionStatus(KaggleObject):
  r"""
  Attributes:
    is_completed (bool)
      Whether or not this progression item has been completed.
  """

  def __init__(self):
    self._is_completed = False
    self._freeze()

  @property
  def is_completed(self) -> bool:
    """Whether or not this progression item has been completed."""
    return self._is_completed

  @is_completed.setter
  def is_completed(self, is_completed: bool):
    if is_completed is None:
      del self.is_completed
      return
    if not isinstance(is_completed, bool):
      raise TypeError('is_completed must be of type bool')
    self._is_completed = is_completed


class UpdateUserRegionRequest(KaggleObject):
  r"""
  """

  pass

AddSuggestedItemRequest._fields = []

AddSuggestedItemResponse._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

CreationCounts._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
  FieldMetadata("lastMonthCount", "last_month_count", "_last_month_count", int, 0, PredefinedSerializer()),
]

DismissSuggestedItemRequest._fields = [
  FieldMetadata("suggestedItemId", "suggested_item_id", "_suggested_item_id", int, 0, PredefinedSerializer()),
]

EntityCountData._fields = [
  FieldMetadata("competitionCount", "competition_count", "_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionSolutionCount", "competition_solution_count", "_competition_solution_count", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetCount", "dataset_count", "_dataset_count", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelCount", "kernel_count", "_kernel_count", int, 0, PredefinedSerializer()),
  FieldMetadata("learnTotalHours", "learn_total_hours", "_learn_total_hours", int, 0, PredefinedSerializer()),
  FieldMetadata("modelCount", "model_count", "_model_count", int, 0, PredefinedSerializer()),
  FieldMetadata("userCount", "user_count", "_user_count", int, 0, PredefinedSerializer()),
]

EntityListingData._fields = [
  FieldMetadata("competitions", "competitions", "_competitions", Competition, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("competitionSolutions", "competition_solutions", "_competition_solutions", TopicListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("datasets", "datasets", "_datasets", DatasetListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("kernels", "kernels", "_kernels", KernelListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("models", "models", "_models", Model, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("learnCourses", "learn_courses", "_learn_courses", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("benchmarks", "benchmarks", "_benchmarks", Benchmark, [], ListSerializer(KaggleObjectSerializer())),
]

ForceUpdateLoggedOutHomepageDataRequest._fields = []

GetHomePageStatsRequest._fields = []

GetHomePageStatsResponse._fields = [
  FieldMetadata("datasets", "datasets", "_datasets", CreationCounts, None, KaggleObjectSerializer()),
  FieldMetadata("notebooks", "notebooks", "_notebooks", CreationCounts, None, KaggleObjectSerializer()),
  FieldMetadata("discussions", "discussions", "_discussions", CreationCounts, None, KaggleObjectSerializer()),
  FieldMetadata("competitions", "competitions", "_competitions", CreationCounts, None, KaggleObjectSerializer()),
  FieldMetadata("courses", "courses", "_courses", CreationCounts, None, KaggleObjectSerializer()),
  FieldMetadata("maxDayStreak", "max_day_streak", "_max_day_streak", int, 0, PredefinedSerializer()),
  FieldMetadata("currentDayStreak", "current_day_streak", "_current_day_streak", int, 0, PredefinedSerializer()),
]

GetLoggedOutHomepageDataRequest._fields = []

GetLoggedOutHomepageDataResponse._fields = [
  FieldMetadata("countData", "count_data", "_count_data", EntityCountData, None, KaggleObjectSerializer()),
  FieldMetadata("listingData", "listing_data", "_listing_data", EntityListingData, None, KaggleObjectSerializer()),
  FieldMetadata("newAndExcitingItems", "new_and_exciting_items", "_new_and_exciting_items", NewAndExcitingItem, [], ListSerializer(KaggleObjectSerializer())),
]

GetNextStepsConfigRequest._fields = []

GetNextStepsConfigResponse._fields = [
  FieldMetadata("suggestedItems", "suggested_items", "_suggested_items", SuggestedItem, [], ListSerializer(KaggleObjectSerializer())),
]

GetNextStepsRequest._fields = []

GetNextStepsResponse._fields = [
  FieldMetadata("jumpBackInItems", "jump_back_in_items", "_jump_back_in_items", JumpBackInItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("suggestedItems", "suggested_items", "_suggested_items", SuggestedItem, [], ListSerializer(KaggleObjectSerializer())),
]

JumpBackInCompetition._fields = [
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("latestSubmissionPublicScoreFormatted", "latest_submission_public_score_formatted", "_latest_submission_public_score_formatted", str, None, PredefinedSerializer(), optional=True),
]

JumpBackInItem._fields = [
  FieldMetadata("actionUrl", "action_url", "_action_url", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("competition", "competition", "_competition", JumpBackInCompetition, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publicDataset", "public_dataset", "_public_dataset", JumpBackInPublicDataset, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("privateDataset", "private_dataset", "_private_dataset", JumpBackInPrivateDataset, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publicNotebook", "public_notebook", "_public_notebook", JumpBackInPublicNotebook, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("privateNotebook", "private_notebook", "_private_notebook", JumpBackInPrivateNotebook, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("learnCourseNotebook", "learn_course_notebook", "_learn_course_notebook", JumpBackInLearnCourseNotebook, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("avatar", "avatar", "_avatar", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

JumpBackInLearnCourseNotebook._fields = [
  FieldMetadata("courseTitle", "course_title", "_course_title", str, "", PredefinedSerializer()),
  FieldMetadata("lessonTitle", "lesson_title", "_lesson_title", str, "", PredefinedSerializer()),
  FieldMetadata("progress", "progress", "_progress", float, 0.0, PredefinedSerializer()),
]

JumpBackInPrivateDataset._fields = [
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, 0.0, PredefinedSerializer()),
  FieldMetadata("lastVersionUploaded", "last_version_uploaded", "_last_version_uploaded", datetime, None, DateTimeSerializer()),
]

JumpBackInPrivateNotebook._fields = [
  FieldMetadata("lastCommitCompletedAt", "last_commit_completed_at", "_last_commit_completed_at", datetime, None, DateTimeSerializer()),
]

JumpBackInPublicDataset._fields = [
  FieldMetadata("totalDownloads", "total_downloads", "_total_downloads", int, 0, PredefinedSerializer()),
  FieldMetadata("newDownloads", "new_downloads", "_new_downloads", int, 0, PredefinedSerializer()),
]

JumpBackInPublicNotebook._fields = [
  FieldMetadata("totalViews", "total_views", "_total_views", int, 0, PredefinedSerializer()),
  FieldMetadata("newForks", "new_forks", "_new_forks", int, 0, PredefinedSerializer()),
]

SuggestedItem._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("actionUrl", "action_url", "_action_url", str, "", PredefinedSerializer()),
  FieldMetadata("icon", "icon", "_icon", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("progressionStatus", "progression_status", "_progression_status", SuggestedProgressionStatus, None, KaggleObjectSerializer()),
]

SuggestedProgressionStatus._fields = [
  FieldMetadata("isCompleted", "is_completed", "_is_completed", bool, False, PredefinedSerializer()),
]

UpdateUserRegionRequest._fields = []

