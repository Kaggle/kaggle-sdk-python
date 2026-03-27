from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.tags.types.tag_service import Tag
from kagglesdk.users.types.user import User
from typing import Optional, List

class LearnExerciseInteractionType(enum.Enum):
  LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED = 0
  CHECK = 1
  HINT = 2
  SOLUTION = 3

class LearnExerciseOutcomeType(enum.Enum):
  LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED = 0
  PASS = 1
  FAIL = 2
  EXCEPTION = 3
  UNATTEMPTED = 4

class LearnExerciseQuestionType(enum.Enum):
  LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED = 0
  EQUALITY_CHECK_PROBLEM = 1
  CODING_PROBLEM = 2
  FUNCTION_PROBLEM = 3
  THOUGHT_EXPERIMENT = 4

class LearnLessonDataSourceType(enum.Enum):
  LEARN_LESSON_DATA_SOURCE_TYPE_UNSPECIFIED = 0
  COMPETITION = 1
  DATASET = 2

class LearnNudgeType(enum.Enum):
  COURSE_COMPLETE_NO_BONUS_LESSONS = 0
  COURSE_COMPLETE_WITH_BONUS_LESSONS = 1
  COURSE_INCOMPLETE = 2
  DO_EXERCISE = 3
  DO_TUTORIAL = 4

class LearnTrackerStatus(enum.Enum):
  LEARN_TRACKER_STATUS_UNSPECIFIED = 0
  TRACK_VIEW = 1
  KERNEL_VIEW = 2
  PAGE_VIEW = 3
  EXERCISE_FORK = 4

class AddLessonsToTrackRequest(KaggleObject):
  r"""
  Attributes:
    track_id (int)
    lesson_ids (int)
  """

  def __init__(self):
    self._track_id = 0
    self._lesson_ids = []
    self._freeze()

  @property
  def track_id(self) -> int:
    return self._track_id

  @track_id.setter
  def track_id(self, track_id: int):
    if track_id is None:
      del self.track_id
      return
    if not isinstance(track_id, int):
      raise TypeError('track_id must be of type int')
    self._track_id = track_id

  @property
  def lesson_ids(self) -> Optional[List[int]]:
    return self._lesson_ids

  @lesson_ids.setter
  def lesson_ids(self, lesson_ids: Optional[List[int]]):
    if lesson_ids is None:
      del self.lesson_ids
      return
    if not isinstance(lesson_ids, list):
      raise TypeError('lesson_ids must be of type list')
    if not all([isinstance(t, int) for t in lesson_ids]):
      raise TypeError('lesson_ids must contain only items of type int')
    self._lesson_ids = lesson_ids


class Certificate(KaggleObject):
  r"""
  Attributes:
    author_username (str)
      This is deprecated. Use author_usernames instead.
    completion_date (datetime)
    course_name (str)
    full_username (str)
    gcs_access_image_url (str)
    track_id (int)
    track_url (str)
    author_usernames (str)
    username (str)
  """

  def __init__(self):
    self._author_username = ""
    self._completion_date = None
    self._course_name = ""
    self._full_username = ""
    self._gcs_access_image_url = ""
    self._track_id = 0
    self._track_url = ""
    self._author_usernames = []
    self._username = ""
    self._freeze()

  @property
  def author_username(self) -> str:
    """This is deprecated. Use author_usernames instead."""
    return self._author_username

  @author_username.setter
  def author_username(self, author_username: str):
    if author_username is None:
      del self.author_username
      return
    if not isinstance(author_username, str):
      raise TypeError('author_username must be of type str')
    self._author_username = author_username

  @property
  def completion_date(self) -> datetime:
    return self._completion_date

  @completion_date.setter
  def completion_date(self, completion_date: datetime):
    if completion_date is None:
      del self.completion_date
      return
    if not isinstance(completion_date, datetime):
      raise TypeError('completion_date must be of type datetime')
    self._completion_date = completion_date

  @property
  def course_name(self) -> str:
    return self._course_name

  @course_name.setter
  def course_name(self, course_name: str):
    if course_name is None:
      del self.course_name
      return
    if not isinstance(course_name, str):
      raise TypeError('course_name must be of type str')
    self._course_name = course_name

  @property
  def full_username(self) -> str:
    return self._full_username

  @full_username.setter
  def full_username(self, full_username: str):
    if full_username is None:
      del self.full_username
      return
    if not isinstance(full_username, str):
      raise TypeError('full_username must be of type str')
    self._full_username = full_username

  @property
  def username(self) -> str:
    return self._username

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def gcs_access_image_url(self) -> str:
    return self._gcs_access_image_url

  @gcs_access_image_url.setter
  def gcs_access_image_url(self, gcs_access_image_url: str):
    if gcs_access_image_url is None:
      del self.gcs_access_image_url
      return
    if not isinstance(gcs_access_image_url, str):
      raise TypeError('gcs_access_image_url must be of type str')
    self._gcs_access_image_url = gcs_access_image_url

  @property
  def track_id(self) -> int:
    return self._track_id

  @track_id.setter
  def track_id(self, track_id: int):
    if track_id is None:
      del self.track_id
      return
    if not isinstance(track_id, int):
      raise TypeError('track_id must be of type int')
    self._track_id = track_id

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
  def author_usernames(self) -> Optional[List[str]]:
    return self._author_usernames

  @author_usernames.setter
  def author_usernames(self, author_usernames: Optional[List[str]]):
    if author_usernames is None:
      del self.author_usernames
      return
    if not isinstance(author_usernames, list):
      raise TypeError('author_usernames must be of type list')
    if not all([isinstance(t, str) for t in author_usernames]):
      raise TypeError('author_usernames must contain only items of type str')
    self._author_usernames = author_usernames


class EditLessonRequest(KaggleObject):
  r"""
  Attributes:
    lesson_id (int)
    description (str)
    exercise_kernel_id (int)
    exercise_kernel_version_id (int)
    question_count (int)
    tutorial_kernel_id (int)
    is_extra_credit (bool)
  """

  def __init__(self):
    self._lesson_id = 0
    self._description = None
    self._exercise_kernel_id = None
    self._exercise_kernel_version_id = None
    self._question_count = None
    self._tutorial_kernel_id = None
    self._is_extra_credit = None
    self._freeze()

  @property
  def lesson_id(self) -> int:
    return self._lesson_id

  @lesson_id.setter
  def lesson_id(self, lesson_id: int):
    if lesson_id is None:
      del self.lesson_id
      return
    if not isinstance(lesson_id, int):
      raise TypeError('lesson_id must be of type int')
    self._lesson_id = lesson_id

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
  def exercise_kernel_id(self) -> int:
    return self._exercise_kernel_id or 0

  @exercise_kernel_id.setter
  def exercise_kernel_id(self, exercise_kernel_id: Optional[int]):
    if exercise_kernel_id is None:
      del self.exercise_kernel_id
      return
    if not isinstance(exercise_kernel_id, int):
      raise TypeError('exercise_kernel_id must be of type int')
    self._exercise_kernel_id = exercise_kernel_id

  @property
  def exercise_kernel_version_id(self) -> int:
    return self._exercise_kernel_version_id or 0

  @exercise_kernel_version_id.setter
  def exercise_kernel_version_id(self, exercise_kernel_version_id: Optional[int]):
    if exercise_kernel_version_id is None:
      del self.exercise_kernel_version_id
      return
    if not isinstance(exercise_kernel_version_id, int):
      raise TypeError('exercise_kernel_version_id must be of type int')
    self._exercise_kernel_version_id = exercise_kernel_version_id

  @property
  def question_count(self) -> int:
    return self._question_count or 0

  @question_count.setter
  def question_count(self, question_count: Optional[int]):
    if question_count is None:
      del self.question_count
      return
    if not isinstance(question_count, int):
      raise TypeError('question_count must be of type int')
    self._question_count = question_count

  @property
  def tutorial_kernel_id(self) -> int:
    return self._tutorial_kernel_id or 0

  @tutorial_kernel_id.setter
  def tutorial_kernel_id(self, tutorial_kernel_id: Optional[int]):
    if tutorial_kernel_id is None:
      del self.tutorial_kernel_id
      return
    if not isinstance(tutorial_kernel_id, int):
      raise TypeError('tutorial_kernel_id must be of type int')
    self._tutorial_kernel_id = tutorial_kernel_id

  @property
  def is_extra_credit(self) -> bool:
    return self._is_extra_credit or False

  @is_extra_credit.setter
  def is_extra_credit(self, is_extra_credit: Optional[bool]):
    if is_extra_credit is None:
      del self.is_extra_credit
      return
    if not isinstance(is_extra_credit, bool):
      raise TypeError('is_extra_credit must be of type bool')
    self._is_extra_credit = is_extra_credit


class EduHome(KaggleObject):
  r"""
  Attributes:
    title (str)
    description (str)
    image_url (str)
    tags (str)
  """

  def __init__(self):
    self._title = ""
    self._description = ""
    self._image_url = ""
    self._tags = []
    self._freeze()

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
  def tags(self) -> Optional[List[str]]:
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[str]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, str) for t in tags]):
      raise TypeError('tags must contain only items of type str')
    self._tags = tags


class GetCertificateRequest(KaggleObject):
  r"""
  Attributes:
    username (str)
    track_slug (str)
  """

  def __init__(self):
    self._username = ""
    self._track_slug = ""
    self._freeze()

  @property
  def username(self) -> str:
    return self._username

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    self._username = username

  @property
  def track_slug(self) -> str:
    return self._track_slug

  @track_slug.setter
  def track_slug(self, track_slug: str):
    if track_slug is None:
      del self.track_slug
      return
    if not isinstance(track_slug, str):
      raise TypeError('track_slug must be of type str')
    self._track_slug = track_slug


class GetExerciseVersionsRequest(KaggleObject):
  r"""
  Attributes:
    exercise_id (int)
  """

  def __init__(self):
    self._exercise_id = 0
    self._freeze()

  @property
  def exercise_id(self) -> int:
    return self._exercise_id

  @exercise_id.setter
  def exercise_id(self, exercise_id: int):
    if exercise_id is None:
      del self.exercise_id
      return
    if not isinstance(exercise_id, int):
      raise TypeError('exercise_id must be of type int')
    self._exercise_id = exercise_id


class GetExerciseVersionsResponse(KaggleObject):
  r"""
  Attributes:
    exercise_versions (LearnExerciseVersion)
  """

  def __init__(self):
    self._exercise_versions = []
    self._freeze()

  @property
  def exercise_versions(self) -> Optional[List[Optional['LearnExerciseVersion']]]:
    return self._exercise_versions

  @exercise_versions.setter
  def exercise_versions(self, exercise_versions: Optional[List[Optional['LearnExerciseVersion']]]):
    if exercise_versions is None:
      del self.exercise_versions
      return
    if not isinstance(exercise_versions, list):
      raise TypeError('exercise_versions must be of type list')
    if not all([isinstance(t, LearnExerciseVersion) for t in exercise_versions]):
      raise TypeError('exercise_versions must contain only items of type LearnExerciseVersion')
    self._exercise_versions = exercise_versions


class GetLearnCertificateUploadUrlRequest(KaggleObject):
  r"""
  Attributes:
    content_length (int)
    track_id (int)
  """

  def __init__(self):
    self._content_length = 0
    self._track_id = 0
    self._freeze()

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def track_id(self) -> int:
    return self._track_id

  @track_id.setter
  def track_id(self, track_id: int):
    if track_id is None:
      del self.track_id
      return
    if not isinstance(track_id, int):
      raise TypeError('track_id must be of type int')
    self._track_id = track_id


class GetLearnCertificateUploadUrlResponse(KaggleObject):
  r"""
  Attributes:
    upload_url (str)
  """

  def __init__(self):
    self._upload_url = ""
    self._freeze()

  @property
  def upload_url(self) -> str:
    return self._upload_url

  @upload_url.setter
  def upload_url(self, upload_url: str):
    if upload_url is None:
      del self.upload_url
      return
    if not isinstance(upload_url, str):
      raise TypeError('upload_url must be of type str')
    self._upload_url = upload_url


class GetTrackRequest(KaggleObject):
  r"""
  Attributes:
    track_slug (str)
  """

  def __init__(self):
    self._track_slug = ""
    self._freeze()

  @property
  def track_slug(self) -> str:
    return self._track_slug

  @track_slug.setter
  def track_slug(self, track_slug: str):
    if track_slug is None:
      del self.track_slug
      return
    if not isinstance(track_slug, str):
      raise TypeError('track_slug must be of type str')
    self._track_slug = track_slug


class GetTracksRequest(KaggleObject):
  r"""
  """

  pass

class GetTracksResponse(KaggleObject):
  r"""
  Attributes:
    tracks (LearnTrack)
  """

  def __init__(self):
    self._tracks = []
    self._freeze()

  @property
  def tracks(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['LearnTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, LearnTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type LearnTrack')
    self._tracks = tracks


class LearnExercise(KaggleObject):
  r"""
  Attributes:
    id (int)
    script_id (int)
    name (str)
    url (str)
    author_username (str)
    script_slug (str)
    progress (float)
    last_completion_date (datetime)
      The latest date the user completed this exercise.
  """

  def __init__(self):
    self._id = 0
    self._script_id = 0
    self._name = ""
    self._url = ""
    self._author_username = ""
    self._script_slug = ""
    self._progress = None
    self._last_completion_date = None
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
  def script_id(self) -> int:
    return self._script_id

  @script_id.setter
  def script_id(self, script_id: int):
    if script_id is None:
      del self.script_id
      return
    if not isinstance(script_id, int):
      raise TypeError('script_id must be of type int')
    self._script_id = script_id

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
  def author_username(self) -> str:
    return self._author_username

  @author_username.setter
  def author_username(self, author_username: str):
    if author_username is None:
      del self.author_username
      return
    if not isinstance(author_username, str):
      raise TypeError('author_username must be of type str')
    self._author_username = author_username

  @property
  def script_slug(self) -> str:
    return self._script_slug

  @script_slug.setter
  def script_slug(self, script_slug: str):
    if script_slug is None:
      del self.script_slug
      return
    if not isinstance(script_slug, str):
      raise TypeError('script_slug must be of type str')
    self._script_slug = script_slug

  @property
  def progress(self) -> float:
    return self._progress or 0.0

  @progress.setter
  def progress(self, progress: Optional[float]):
    if progress is None:
      del self.progress
      return
    if not isinstance(progress, float):
      raise TypeError('progress must be of type float')
    self._progress = progress

  @property
  def last_completion_date(self) -> datetime:
    """The latest date the user completed this exercise."""
    return self._last_completion_date

  @last_completion_date.setter
  def last_completion_date(self, last_completion_date: datetime):
    if last_completion_date is None:
      del self.last_completion_date
      return
    if not isinstance(last_completion_date, datetime):
      raise TypeError('last_completion_date must be of type datetime')
    self._last_completion_date = last_completion_date


class LearnExerciseVersion(KaggleObject):
  r"""
  Attributes:
    kernel_version_id (int)
    question_count (int)
  """

  def __init__(self):
    self._kernel_version_id = 0
    self._question_count = 0
    self._freeze()

  @property
  def kernel_version_id(self) -> int:
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def question_count(self) -> int:
    return self._question_count

  @question_count.setter
  def question_count(self, question_count: int):
    if question_count is None:
      del self.question_count
      return
    if not isinstance(question_count, int):
      raise TypeError('question_count must be of type int')
    self._question_count = question_count


class LearnHome(KaggleObject):
  r"""
  Attributes:
    tracks (LearnTrack)
  """

  def __init__(self):
    self._tracks = []
    self._freeze()

  @property
  def tracks(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['LearnTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, LearnTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type LearnTrack')
    self._tracks = tracks


class LearnLesson(KaggleObject):
  r"""
  Attributes:
    id (int)
    description (str)
    learn_tutorial (LearnTutorial)
    learn_exercise (LearnExercise)
    is_extra_credit (bool)
    data_source (LearnLessonDataSource)
  """

  def __init__(self):
    self._id = 0
    self._description = ""
    self._learn_tutorial = None
    self._learn_exercise = None
    self._is_extra_credit = False
    self._data_source = None
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
  def learn_tutorial(self) -> Optional['LearnTutorial']:
    return self._learn_tutorial

  @learn_tutorial.setter
  def learn_tutorial(self, learn_tutorial: Optional['LearnTutorial']):
    if learn_tutorial is None:
      del self.learn_tutorial
      return
    if not isinstance(learn_tutorial, LearnTutorial):
      raise TypeError('learn_tutorial must be of type LearnTutorial')
    self._learn_tutorial = learn_tutorial

  @property
  def learn_exercise(self) -> Optional['LearnExercise']:
    return self._learn_exercise

  @learn_exercise.setter
  def learn_exercise(self, learn_exercise: Optional['LearnExercise']):
    if learn_exercise is None:
      del self.learn_exercise
      return
    if not isinstance(learn_exercise, LearnExercise):
      raise TypeError('learn_exercise must be of type LearnExercise')
    self._learn_exercise = learn_exercise

  @property
  def is_extra_credit(self) -> bool:
    return self._is_extra_credit

  @is_extra_credit.setter
  def is_extra_credit(self, is_extra_credit: bool):
    if is_extra_credit is None:
      del self.is_extra_credit
      return
    if not isinstance(is_extra_credit, bool):
      raise TypeError('is_extra_credit must be of type bool')
    self._is_extra_credit = is_extra_credit

  @property
  def data_source(self) -> Optional['LearnLessonDataSource']:
    return self._data_source

  @data_source.setter
  def data_source(self, data_source: Optional['LearnLessonDataSource']):
    if data_source is None:
      del self.data_source
      return
    if not isinstance(data_source, LearnLessonDataSource):
      raise TypeError('data_source must be of type LearnLessonDataSource')
    self._data_source = data_source


class LearnLessonDataSource(KaggleObject):
  r"""
  Attributes:
    type (LearnLessonDataSourceType)
    id (int)
    url (str)
    thumbnail_image_url (str)
  """

  def __init__(self):
    self._type = LearnLessonDataSourceType.LEARN_LESSON_DATA_SOURCE_TYPE_UNSPECIFIED
    self._id = 0
    self._url = ""
    self._thumbnail_image_url = ""
    self._freeze()

  @property
  def type(self) -> 'LearnLessonDataSourceType':
    return self._type

  @type.setter
  def type(self, type: 'LearnLessonDataSourceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, LearnLessonDataSourceType):
      raise TypeError('type must be of type LearnLessonDataSourceType')
    self._type = type

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


class LearnNudge(KaggleObject):
  r"""
  Attributes:
    course_index (int)
    course_name (str)
    course_slug (str)
    next_item_name (str)
    next_item_url (str)
    next_item_type (LearnNudgeType)
  """

  def __init__(self):
    self._course_index = 0
    self._course_name = ""
    self._course_slug = ""
    self._next_item_name = ""
    self._next_item_url = ""
    self._next_item_type = LearnNudgeType.COURSE_COMPLETE_NO_BONUS_LESSONS
    self._freeze()

  @property
  def course_index(self) -> int:
    return self._course_index

  @course_index.setter
  def course_index(self, course_index: int):
    if course_index is None:
      del self.course_index
      return
    if not isinstance(course_index, int):
      raise TypeError('course_index must be of type int')
    self._course_index = course_index

  @property
  def course_name(self) -> str:
    return self._course_name

  @course_name.setter
  def course_name(self, course_name: str):
    if course_name is None:
      del self.course_name
      return
    if not isinstance(course_name, str):
      raise TypeError('course_name must be of type str')
    self._course_name = course_name

  @property
  def course_slug(self) -> str:
    return self._course_slug

  @course_slug.setter
  def course_slug(self, course_slug: str):
    if course_slug is None:
      del self.course_slug
      return
    if not isinstance(course_slug, str):
      raise TypeError('course_slug must be of type str')
    self._course_slug = course_slug

  @property
  def next_item_name(self) -> str:
    return self._next_item_name

  @next_item_name.setter
  def next_item_name(self, next_item_name: str):
    if next_item_name is None:
      del self.next_item_name
      return
    if not isinstance(next_item_name, str):
      raise TypeError('next_item_name must be of type str')
    self._next_item_name = next_item_name

  @property
  def next_item_url(self) -> str:
    return self._next_item_url

  @next_item_url.setter
  def next_item_url(self, next_item_url: str):
    if next_item_url is None:
      del self.next_item_url
      return
    if not isinstance(next_item_url, str):
      raise TypeError('next_item_url must be of type str')
    self._next_item_url = next_item_url

  @property
  def next_item_type(self) -> 'LearnNudgeType':
    return self._next_item_type

  @next_item_type.setter
  def next_item_type(self, next_item_type: 'LearnNudgeType'):
    if next_item_type is None:
      del self.next_item_type
      return
    if not isinstance(next_item_type, LearnNudgeType):
      raise TypeError('next_item_type must be of type LearnNudgeType')
    self._next_item_type = next_item_type


class LearnSeriesNavigationData(KaggleObject):
  r"""
  Attributes:
    learn_course (LearnTrack)
    learn_nudge (LearnNudge)
  """

  def __init__(self):
    self._learn_course = None
    self._learn_nudge = None
    self._freeze()

  @property
  def learn_course(self) -> Optional['LearnTrack']:
    return self._learn_course

  @learn_course.setter
  def learn_course(self, learn_course: Optional['LearnTrack']):
    if learn_course is None:
      del self.learn_course
      return
    if not isinstance(learn_course, LearnTrack):
      raise TypeError('learn_course must be of type LearnTrack')
    self._learn_course = learn_course

  @property
  def learn_nudge(self) -> Optional['LearnNudge']:
    return self._learn_nudge

  @learn_nudge.setter
  def learn_nudge(self, learn_nudge: Optional['LearnNudge']):
    if learn_nudge is None:
      del self.learn_nudge
      return
    if not isinstance(learn_nudge, LearnNudge):
      raise TypeError('learn_nudge must be of type LearnNudge')
    self._learn_nudge = learn_nudge


class LearnTrack(KaggleObject):
  r"""
  Attributes:
    id (int)
    track_index (int)
    name (str)
    description (str)
    has_daily_delivery (bool)
    visible (bool)
    track_slug (str)
    thumbnail_image_url (str)
    estimated_time_hours (int)
    user_progress (float)
    certificate_url (str)
    lessons (LearnLesson)
    prerequisites (LearnTrack)
    dependency_for (LearnTrack)
    authors (User)
    tags (Tag)
    forum_id (int)
  """

  def __init__(self):
    self._id = 0
    self._track_index = 0
    self._name = ""
    self._description = ""
    self._has_daily_delivery = False
    self._visible = False
    self._track_slug = ""
    self._thumbnail_image_url = ""
    self._estimated_time_hours = 0
    self._user_progress = 0.0
    self._certificate_url = ""
    self._lessons = []
    self._prerequisites = []
    self._dependency_for = []
    self._authors = []
    self._tags = []
    self._forum_id = 0
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
  def track_index(self) -> int:
    return self._track_index

  @track_index.setter
  def track_index(self, track_index: int):
    if track_index is None:
      del self.track_index
      return
    if not isinstance(track_index, int):
      raise TypeError('track_index must be of type int')
    self._track_index = track_index

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
  def has_daily_delivery(self) -> bool:
    return self._has_daily_delivery

  @has_daily_delivery.setter
  def has_daily_delivery(self, has_daily_delivery: bool):
    if has_daily_delivery is None:
      del self.has_daily_delivery
      return
    if not isinstance(has_daily_delivery, bool):
      raise TypeError('has_daily_delivery must be of type bool')
    self._has_daily_delivery = has_daily_delivery

  @property
  def visible(self) -> bool:
    return self._visible

  @visible.setter
  def visible(self, visible: bool):
    if visible is None:
      del self.visible
      return
    if not isinstance(visible, bool):
      raise TypeError('visible must be of type bool')
    self._visible = visible

  @property
  def track_slug(self) -> str:
    return self._track_slug

  @track_slug.setter
  def track_slug(self, track_slug: str):
    if track_slug is None:
      del self.track_slug
      return
    if not isinstance(track_slug, str):
      raise TypeError('track_slug must be of type str')
    self._track_slug = track_slug

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
  def estimated_time_hours(self) -> int:
    return self._estimated_time_hours

  @estimated_time_hours.setter
  def estimated_time_hours(self, estimated_time_hours: int):
    if estimated_time_hours is None:
      del self.estimated_time_hours
      return
    if not isinstance(estimated_time_hours, int):
      raise TypeError('estimated_time_hours must be of type int')
    self._estimated_time_hours = estimated_time_hours

  @property
  def user_progress(self) -> float:
    return self._user_progress

  @user_progress.setter
  def user_progress(self, user_progress: float):
    if user_progress is None:
      del self.user_progress
      return
    if not isinstance(user_progress, float):
      raise TypeError('user_progress must be of type float')
    self._user_progress = user_progress

  @property
  def certificate_url(self) -> str:
    return self._certificate_url

  @certificate_url.setter
  def certificate_url(self, certificate_url: str):
    if certificate_url is None:
      del self.certificate_url
      return
    if not isinstance(certificate_url, str):
      raise TypeError('certificate_url must be of type str')
    self._certificate_url = certificate_url

  @property
  def lessons(self) -> Optional[List[Optional['LearnLesson']]]:
    return self._lessons

  @lessons.setter
  def lessons(self, lessons: Optional[List[Optional['LearnLesson']]]):
    if lessons is None:
      del self.lessons
      return
    if not isinstance(lessons, list):
      raise TypeError('lessons must be of type list')
    if not all([isinstance(t, LearnLesson) for t in lessons]):
      raise TypeError('lessons must contain only items of type LearnLesson')
    self._lessons = lessons

  @property
  def prerequisites(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._prerequisites

  @prerequisites.setter
  def prerequisites(self, prerequisites: Optional[List[Optional['LearnTrack']]]):
    if prerequisites is None:
      del self.prerequisites
      return
    if not isinstance(prerequisites, list):
      raise TypeError('prerequisites must be of type list')
    if not all([isinstance(t, LearnTrack) for t in prerequisites]):
      raise TypeError('prerequisites must contain only items of type LearnTrack')
    self._prerequisites = prerequisites

  @property
  def dependency_for(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._dependency_for

  @dependency_for.setter
  def dependency_for(self, dependency_for: Optional[List[Optional['LearnTrack']]]):
    if dependency_for is None:
      del self.dependency_for
      return
    if not isinstance(dependency_for, list):
      raise TypeError('dependency_for must be of type list')
    if not all([isinstance(t, LearnTrack) for t in dependency_for]):
      raise TypeError('dependency_for must contain only items of type LearnTrack')
    self._dependency_for = dependency_for

  @property
  def authors(self) -> Optional[List[Optional['User']]]:
    return self._authors

  @authors.setter
  def authors(self, authors: Optional[List[Optional['User']]]):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, list):
      raise TypeError('authors must be of type list')
    if not all([isinstance(t, User) for t in authors]):
      raise TypeError('authors must contain only items of type User')
    self._authors = authors

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


class LearnTutorial(KaggleObject):
  r"""
  Attributes:
    id (int)
    script_id (int)
    name (str)
    url (str)
    author_display_name (str)
    author_username (str)
    script_slug (str)
    thumbnail_image_url (str)
    creation_date (datetime)
    progress (float)
    last_completion_date (datetime)
      The latest date the user completed this tutorial.
    track_name (str)
      Fields required for displaying tutorial search results
    track_slug (str)
    exercise_description (str)
  """

  def __init__(self):
    self._id = 0
    self._script_id = 0
    self._name = ""
    self._url = ""
    self._author_display_name = ""
    self._author_username = ""
    self._script_slug = ""
    self._thumbnail_image_url = ""
    self._creation_date = None
    self._progress = None
    self._last_completion_date = None
    self._track_name = None
    self._track_slug = None
    self._exercise_description = None
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
  def script_id(self) -> int:
    return self._script_id

  @script_id.setter
  def script_id(self, script_id: int):
    if script_id is None:
      del self.script_id
      return
    if not isinstance(script_id, int):
      raise TypeError('script_id must be of type int')
    self._script_id = script_id

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
  def author_username(self) -> str:
    return self._author_username

  @author_username.setter
  def author_username(self, author_username: str):
    if author_username is None:
      del self.author_username
      return
    if not isinstance(author_username, str):
      raise TypeError('author_username must be of type str')
    self._author_username = author_username

  @property
  def script_slug(self) -> str:
    return self._script_slug

  @script_slug.setter
  def script_slug(self, script_slug: str):
    if script_slug is None:
      del self.script_slug
      return
    if not isinstance(script_slug, str):
      raise TypeError('script_slug must be of type str')
    self._script_slug = script_slug

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
  def progress(self) -> float:
    return self._progress or 0.0

  @progress.setter
  def progress(self, progress: Optional[float]):
    if progress is None:
      del self.progress
      return
    if not isinstance(progress, float):
      raise TypeError('progress must be of type float')
    self._progress = progress

  @property
  def last_completion_date(self) -> datetime:
    """The latest date the user completed this tutorial."""
    return self._last_completion_date

  @last_completion_date.setter
  def last_completion_date(self, last_completion_date: datetime):
    if last_completion_date is None:
      del self.last_completion_date
      return
    if not isinstance(last_completion_date, datetime):
      raise TypeError('last_completion_date must be of type datetime')
    self._last_completion_date = last_completion_date

  @property
  def track_name(self) -> str:
    """Fields required for displaying tutorial search results"""
    return self._track_name or ""

  @track_name.setter
  def track_name(self, track_name: Optional[str]):
    if track_name is None:
      del self.track_name
      return
    if not isinstance(track_name, str):
      raise TypeError('track_name must be of type str')
    self._track_name = track_name

  @property
  def track_slug(self) -> str:
    return self._track_slug or ""

  @track_slug.setter
  def track_slug(self, track_slug: Optional[str]):
    if track_slug is None:
      del self.track_slug
      return
    if not isinstance(track_slug, str):
      raise TypeError('track_slug must be of type str')
    self._track_slug = track_slug

  @property
  def exercise_description(self) -> str:
    return self._exercise_description or ""

  @exercise_description.setter
  def exercise_description(self, exercise_description: Optional[str]):
    if exercise_description is None:
      del self.exercise_description
      return
    if not isinstance(exercise_description, str):
      raise TypeError('exercise_description must be of type str')
    self._exercise_description = exercise_description


class LessonInfo(KaggleObject):
  r"""
  Attributes:
    tracks (LearnTrack)
  """

  def __init__(self):
    self._tracks = []
    self._freeze()

  @property
  def tracks(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['LearnTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, LearnTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type LearnTrack')
    self._tracks = tracks


class ReorderTracksRequest(KaggleObject):
  r"""
  Attributes:
    track_ids (int)
  """

  def __init__(self):
    self._track_ids = []
    self._freeze()

  @property
  def track_ids(self) -> Optional[List[int]]:
    return self._track_ids

  @track_ids.setter
  def track_ids(self, track_ids: Optional[List[int]]):
    if track_ids is None:
      del self.track_ids
      return
    if not isinstance(track_ids, list):
      raise TypeError('track_ids must be of type list')
    if not all([isinstance(t, int) for t in track_ids]):
      raise TypeError('track_ids must contain only items of type int')
    self._track_ids = track_ids


class ReorderTracksResponse(KaggleObject):
  r"""
  Attributes:
    tracks (LearnTrack)
  """

  def __init__(self):
    self._tracks = []
    self._freeze()

  @property
  def tracks(self) -> Optional[List[Optional['LearnTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['LearnTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, LearnTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type LearnTrack')
    self._tracks = tracks


class RescoreExerciseVersionRequest(KaggleObject):
  r"""
  Attributes:
    script_version_id (int)
  """

  def __init__(self):
    self._script_version_id = 0
    self._freeze()

  @property
  def script_version_id(self) -> int:
    return self._script_version_id

  @script_version_id.setter
  def script_version_id(self, script_version_id: int):
    if script_version_id is None:
      del self.script_version_id
      return
    if not isinstance(script_version_id, int):
      raise TypeError('script_version_id must be of type int')
    self._script_version_id = script_version_id


class RescoreResponse(KaggleObject):
  r"""
  Attributes:
    affected_users (int)
  """

  def __init__(self):
    self._affected_users = 0
    self._freeze()

  @property
  def affected_users(self) -> int:
    return self._affected_users

  @affected_users.setter
  def affected_users(self, affected_users: int):
    if affected_users is None:
      del self.affected_users
      return
    if not isinstance(affected_users, int):
      raise TypeError('affected_users must be of type int')
    self._affected_users = affected_users


class TrackEducationRequest(KaggleObject):
  r"""
  Attributes:
    type (LearnTrackerStatus)
    id (str)
  """

  def __init__(self):
    self._type = LearnTrackerStatus.LEARN_TRACKER_STATUS_UNSPECIFIED
    self._id = ""
    self._freeze()

  @property
  def type(self) -> 'LearnTrackerStatus':
    return self._type

  @type.setter
  def type(self, type: 'LearnTrackerStatus'):
    if type is None:
      del self.type
      return
    if not isinstance(type, LearnTrackerStatus):
      raise TypeError('type must be of type LearnTrackerStatus')
    self._type = type

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


class TrackExerciseInteractionRequest(KaggleObject):
  r"""
  Note: this message is temporarily duplicated in education_api_service.proto.
  It will be removed in the future, but any changes here should be reflected
  there as well.

  Attributes:
    exception_class (str)
    failure_message (str)
    interaction_type (LearnExerciseInteractionType)
    learn_tools_version (str)
    fork_parent_script_version_id (int)
    outcome_type (LearnExerciseOutcomeType)
    question_id (str)
    question_type (LearnExerciseQuestionType)
    trace (str)
    value_towards_completion (float)
  """

  def __init__(self):
    self._exception_class = ""
    self._failure_message = ""
    self._interaction_type = LearnExerciseInteractionType.LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED
    self._learn_tools_version = ""
    self._fork_parent_script_version_id = 0
    self._outcome_type = LearnExerciseOutcomeType.LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED
    self._question_id = ""
    self._question_type = LearnExerciseQuestionType.LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED
    self._trace = ""
    self._value_towards_completion = None
    self._freeze()

  @property
  def exception_class(self) -> str:
    return self._exception_class

  @exception_class.setter
  def exception_class(self, exception_class: str):
    if exception_class is None:
      del self.exception_class
      return
    if not isinstance(exception_class, str):
      raise TypeError('exception_class must be of type str')
    self._exception_class = exception_class

  @property
  def failure_message(self) -> str:
    return self._failure_message

  @failure_message.setter
  def failure_message(self, failure_message: str):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def interaction_type(self) -> 'LearnExerciseInteractionType':
    return self._interaction_type

  @interaction_type.setter
  def interaction_type(self, interaction_type: 'LearnExerciseInteractionType'):
    if interaction_type is None:
      del self.interaction_type
      return
    if not isinstance(interaction_type, LearnExerciseInteractionType):
      raise TypeError('interaction_type must be of type LearnExerciseInteractionType')
    self._interaction_type = interaction_type

  @property
  def learn_tools_version(self) -> str:
    return self._learn_tools_version

  @learn_tools_version.setter
  def learn_tools_version(self, learn_tools_version: str):
    if learn_tools_version is None:
      del self.learn_tools_version
      return
    if not isinstance(learn_tools_version, str):
      raise TypeError('learn_tools_version must be of type str')
    self._learn_tools_version = learn_tools_version

  @property
  def fork_parent_script_version_id(self) -> int:
    return self._fork_parent_script_version_id

  @fork_parent_script_version_id.setter
  def fork_parent_script_version_id(self, fork_parent_script_version_id: int):
    if fork_parent_script_version_id is None:
      del self.fork_parent_script_version_id
      return
    if not isinstance(fork_parent_script_version_id, int):
      raise TypeError('fork_parent_script_version_id must be of type int')
    self._fork_parent_script_version_id = fork_parent_script_version_id

  @property
  def outcome_type(self) -> 'LearnExerciseOutcomeType':
    return self._outcome_type

  @outcome_type.setter
  def outcome_type(self, outcome_type: 'LearnExerciseOutcomeType'):
    if outcome_type is None:
      del self.outcome_type
      return
    if not isinstance(outcome_type, LearnExerciseOutcomeType):
      raise TypeError('outcome_type must be of type LearnExerciseOutcomeType')
    self._outcome_type = outcome_type

  @property
  def question_id(self) -> str:
    return self._question_id

  @question_id.setter
  def question_id(self, question_id: str):
    if question_id is None:
      del self.question_id
      return
    if not isinstance(question_id, str):
      raise TypeError('question_id must be of type str')
    self._question_id = question_id

  @property
  def question_type(self) -> 'LearnExerciseQuestionType':
    return self._question_type

  @question_type.setter
  def question_type(self, question_type: 'LearnExerciseQuestionType'):
    if question_type is None:
      del self.question_type
      return
    if not isinstance(question_type, LearnExerciseQuestionType):
      raise TypeError('question_type must be of type LearnExerciseQuestionType')
    self._question_type = question_type

  @property
  def trace(self) -> str:
    return self._trace

  @trace.setter
  def trace(self, trace: str):
    if trace is None:
      del self.trace
      return
    if not isinstance(trace, str):
      raise TypeError('trace must be of type str')
    self._trace = trace

  @property
  def value_towards_completion(self) -> float:
    return self._value_towards_completion or 0.0

  @value_towards_completion.setter
  def value_towards_completion(self, value_towards_completion: Optional[float]):
    if value_towards_completion is None:
      del self.value_towards_completion
      return
    if not isinstance(value_towards_completion, float):
      raise TypeError('value_towards_completion must be of type float')
    self._value_towards_completion = value_towards_completion


class TrackExerciseInteractionResponse(KaggleObject):
  r"""
  Note: this message is temporarily duplicated in education_api_service.proto.
  It will be removed in the future, but any changes here should be reflected
  there as well.

  Attributes:
    nudge (LearnNudge)
    show_login_prompt (bool)
  """

  def __init__(self):
    self._nudge = None
    self._show_login_prompt = False
    self._freeze()

  @property
  def nudge(self) -> Optional['LearnNudge']:
    return self._nudge

  @nudge.setter
  def nudge(self, nudge: Optional['LearnNudge']):
    if nudge is None:
      del self.nudge
      return
    if not isinstance(nudge, LearnNudge):
      raise TypeError('nudge must be of type LearnNudge')
    self._nudge = nudge

  @property
  def show_login_prompt(self) -> bool:
    return self._show_login_prompt

  @show_login_prompt.setter
  def show_login_prompt(self, show_login_prompt: bool):
    if show_login_prompt is None:
      del self.show_login_prompt
      return
    if not isinstance(show_login_prompt, bool):
      raise TypeError('show_login_prompt must be of type bool')
    self._show_login_prompt = show_login_prompt


AddLessonsToTrackRequest._fields = [
  FieldMetadata("trackId", "track_id", "_track_id", int, 0, PredefinedSerializer()),
  FieldMetadata("lessonIds", "lesson_ids", "_lesson_ids", int, [], ListSerializer(PredefinedSerializer())),
]

Certificate._fields = [
  FieldMetadata("authorUsername", "author_username", "_author_username", str, "", PredefinedSerializer()),
  FieldMetadata("completionDate", "completion_date", "_completion_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("courseName", "course_name", "_course_name", str, "", PredefinedSerializer()),
  FieldMetadata("fullUsername", "full_username", "_full_username", str, "", PredefinedSerializer()),
  FieldMetadata("gcsAccessImageUrl", "gcs_access_image_url", "_gcs_access_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("trackId", "track_id", "_track_id", int, 0, PredefinedSerializer()),
  FieldMetadata("trackUrl", "track_url", "_track_url", str, "", PredefinedSerializer()),
  FieldMetadata("authorUsernames", "author_usernames", "_author_usernames", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
]

EditLessonRequest._fields = [
  FieldMetadata("lessonId", "lesson_id", "_lesson_id", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("exerciseKernelId", "exercise_kernel_id", "_exercise_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("exerciseKernelVersionId", "exercise_kernel_version_id", "_exercise_kernel_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("questionCount", "question_count", "_question_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tutorialKernelId", "tutorial_kernel_id", "_tutorial_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isExtraCredit", "is_extra_credit", "_is_extra_credit", bool, None, PredefinedSerializer(), optional=True),
]

EduHome._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("tags", "tags", "_tags", str, [], ListSerializer(PredefinedSerializer())),
]

GetCertificateRequest._fields = [
  FieldMetadata("username", "username", "_username", str, "", PredefinedSerializer()),
  FieldMetadata("trackSlug", "track_slug", "_track_slug", str, "", PredefinedSerializer()),
]

GetExerciseVersionsRequest._fields = [
  FieldMetadata("exerciseId", "exercise_id", "_exercise_id", int, 0, PredefinedSerializer()),
]

GetExerciseVersionsResponse._fields = [
  FieldMetadata("exerciseVersions", "exercise_versions", "_exercise_versions", LearnExerciseVersion, [], ListSerializer(KaggleObjectSerializer())),
]

GetLearnCertificateUploadUrlRequest._fields = [
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("trackId", "track_id", "_track_id", int, 0, PredefinedSerializer()),
]

GetLearnCertificateUploadUrlResponse._fields = [
  FieldMetadata("uploadUrl", "upload_url", "_upload_url", str, "", PredefinedSerializer()),
]

GetTrackRequest._fields = [
  FieldMetadata("trackSlug", "track_slug", "_track_slug", str, "", PredefinedSerializer()),
]

GetTracksRequest._fields = []

GetTracksResponse._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
]

LearnExercise._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptId", "script_id", "_script_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("authorUsername", "author_username", "_author_username", str, "", PredefinedSerializer()),
  FieldMetadata("scriptSlug", "script_slug", "_script_slug", str, "", PredefinedSerializer()),
  FieldMetadata("progress", "progress", "_progress", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastCompletionDate", "last_completion_date", "_last_completion_date", datetime, None, DateTimeSerializer()),
]

LearnExerciseVersion._fields = [
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("questionCount", "question_count", "_question_count", int, 0, PredefinedSerializer()),
]

LearnHome._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
]

LearnLesson._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("learnTutorial", "learn_tutorial", "_learn_tutorial", LearnTutorial, None, KaggleObjectSerializer()),
  FieldMetadata("learnExercise", "learn_exercise", "_learn_exercise", LearnExercise, None, KaggleObjectSerializer()),
  FieldMetadata("isExtraCredit", "is_extra_credit", "_is_extra_credit", bool, False, PredefinedSerializer()),
  FieldMetadata("dataSource", "data_source", "_data_source", LearnLessonDataSource, None, KaggleObjectSerializer()),
]

LearnLessonDataSource._fields = [
  FieldMetadata("type", "type", "_type", LearnLessonDataSourceType, LearnLessonDataSourceType.LEARN_LESSON_DATA_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
]

LearnNudge._fields = [
  FieldMetadata("courseIndex", "course_index", "_course_index", int, 0, PredefinedSerializer()),
  FieldMetadata("courseName", "course_name", "_course_name", str, "", PredefinedSerializer()),
  FieldMetadata("courseSlug", "course_slug", "_course_slug", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemName", "next_item_name", "_next_item_name", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemUrl", "next_item_url", "_next_item_url", str, "", PredefinedSerializer()),
  FieldMetadata("nextItemType", "next_item_type", "_next_item_type", LearnNudgeType, LearnNudgeType.COURSE_COMPLETE_NO_BONUS_LESSONS, EnumSerializer()),
]

LearnSeriesNavigationData._fields = [
  FieldMetadata("learnCourse", "learn_course", "_learn_course", LearnTrack, None, KaggleObjectSerializer()),
  FieldMetadata("learnNudge", "learn_nudge", "_learn_nudge", LearnNudge, None, KaggleObjectSerializer()),
]

LearnTrack._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("trackIndex", "track_index", "_track_index", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("hasDailyDelivery", "has_daily_delivery", "_has_daily_delivery", bool, False, PredefinedSerializer()),
  FieldMetadata("visible", "visible", "_visible", bool, False, PredefinedSerializer()),
  FieldMetadata("trackSlug", "track_slug", "_track_slug", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("estimatedTimeHours", "estimated_time_hours", "_estimated_time_hours", int, 0, PredefinedSerializer()),
  FieldMetadata("userProgress", "user_progress", "_user_progress", float, 0.0, PredefinedSerializer()),
  FieldMetadata("certificateUrl", "certificate_url", "_certificate_url", str, "", PredefinedSerializer()),
  FieldMetadata("lessons", "lessons", "_lessons", LearnLesson, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("prerequisites", "prerequisites", "_prerequisites", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("dependencyFor", "dependency_for", "_dependency_for", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("authors", "authors", "_authors", User, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tags", "tags", "_tags", Tag, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, 0, PredefinedSerializer()),
]

LearnTutorial._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptId", "script_id", "_script_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("authorDisplayName", "author_display_name", "_author_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("authorUsername", "author_username", "_author_username", str, "", PredefinedSerializer()),
  FieldMetadata("scriptSlug", "script_slug", "_script_slug", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("progress", "progress", "_progress", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastCompletionDate", "last_completion_date", "_last_completion_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("trackName", "track_name", "_track_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("trackSlug", "track_slug", "_track_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("exerciseDescription", "exercise_description", "_exercise_description", str, None, PredefinedSerializer(), optional=True),
]

LessonInfo._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
]

ReorderTracksRequest._fields = [
  FieldMetadata("trackIds", "track_ids", "_track_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ReorderTracksResponse._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", LearnTrack, [], ListSerializer(KaggleObjectSerializer())),
]

RescoreExerciseVersionRequest._fields = [
  FieldMetadata("scriptVersionId", "script_version_id", "_script_version_id", int, 0, PredefinedSerializer()),
]

RescoreResponse._fields = [
  FieldMetadata("affectedUsers", "affected_users", "_affected_users", int, 0, PredefinedSerializer()),
]

TrackEducationRequest._fields = [
  FieldMetadata("type", "type", "_type", LearnTrackerStatus, LearnTrackerStatus.LEARN_TRACKER_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
]

TrackExerciseInteractionRequest._fields = [
  FieldMetadata("exceptionClass", "exception_class", "_exception_class", str, "", PredefinedSerializer()),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, "", PredefinedSerializer()),
  FieldMetadata("interactionType", "interaction_type", "_interaction_type", LearnExerciseInteractionType, LearnExerciseInteractionType.LEARN_EXERCISE_INTERACTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("learnToolsVersion", "learn_tools_version", "_learn_tools_version", str, "", PredefinedSerializer()),
  FieldMetadata("forkParentScriptVersionId", "fork_parent_script_version_id", "_fork_parent_script_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("outcomeType", "outcome_type", "_outcome_type", LearnExerciseOutcomeType, LearnExerciseOutcomeType.LEARN_EXERCISE_OUTCOME_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("questionId", "question_id", "_question_id", str, "", PredefinedSerializer()),
  FieldMetadata("questionType", "question_type", "_question_type", LearnExerciseQuestionType, LearnExerciseQuestionType.LEARN_EXERCISE_QUESTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("trace", "trace", "_trace", str, "", PredefinedSerializer()),
  FieldMetadata("valueTowardsCompletion", "value_towards_completion", "_value_towards_completion", float, None, PredefinedSerializer(), optional=True),
]

TrackExerciseInteractionResponse._fields = [
  FieldMetadata("nudge", "nudge", "_nudge", LearnNudge, None, KaggleObjectSerializer()),
  FieldMetadata("showLoginPrompt", "show_login_prompt", "_show_login_prompt", bool, False, PredefinedSerializer()),
]

