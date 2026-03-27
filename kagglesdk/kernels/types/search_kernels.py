import enum
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import DataSourceType
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional

class SearchKernelsOrderBy(enum.Enum):
  SEARCH_KERNELS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_KERNELS_ORDER_BY_TOTAL_COMMENTS = 1

class SearchKernelsDocument(KaggleObject):
  r"""
  Attributes:
    session_id (int)
      The session ID of the Kernel
    has_linked_submission (bool)
      Whether the Kernel has a linked submission
    fork_parent_user (UserAvatar)
      The user of the parent fork of the Kernel
    datasource_name (str)
      The datasource name of the Kernel
    datasource_type (DataSourceType)
      The datasource type of the Kernel
    datasource_is_private (bool)
      Whether the datasource is private
    best_public_score (float)
      The best public score of the Kernel's submission
    is_draft (bool)
      Whether the Kernel is a draft
    fork_parent_kernel_url (str)
      The URL of the parent fork Kernel (enriched)
  """

  def __init__(self):
    self._session_id = None
    self._has_linked_submission = False
    self._fork_parent_user = None
    self._datasource_name = ""
    self._datasource_type = DataSourceType.DATA_SOURCE_TYPE_COMPETITION
    self._datasource_is_private = False
    self._best_public_score = 0.0
    self._is_draft = False
    self._fork_parent_kernel_url = None
    self._freeze()

  @property
  def session_id(self) -> int:
    """The session ID of the Kernel"""
    return self._session_id or 0

  @session_id.setter
  def session_id(self, session_id: Optional[int]):
    if session_id is None:
      del self.session_id
      return
    if not isinstance(session_id, int):
      raise TypeError('session_id must be of type int')
    self._session_id = session_id

  @property
  def has_linked_submission(self) -> bool:
    """Whether the Kernel has a linked submission"""
    return self._has_linked_submission

  @has_linked_submission.setter
  def has_linked_submission(self, has_linked_submission: bool):
    if has_linked_submission is None:
      del self.has_linked_submission
      return
    if not isinstance(has_linked_submission, bool):
      raise TypeError('has_linked_submission must be of type bool')
    self._has_linked_submission = has_linked_submission

  @property
  def fork_parent_user(self) -> Optional['UserAvatar']:
    """The user of the parent fork of the Kernel"""
    return self._fork_parent_user

  @fork_parent_user.setter
  def fork_parent_user(self, fork_parent_user: Optional['UserAvatar']):
    if fork_parent_user is None:
      del self.fork_parent_user
      return
    if not isinstance(fork_parent_user, UserAvatar):
      raise TypeError('fork_parent_user must be of type UserAvatar')
    self._fork_parent_user = fork_parent_user

  @property
  def datasource_name(self) -> str:
    """The datasource name of the Kernel"""
    return self._datasource_name

  @datasource_name.setter
  def datasource_name(self, datasource_name: str):
    if datasource_name is None:
      del self.datasource_name
      return
    if not isinstance(datasource_name, str):
      raise TypeError('datasource_name must be of type str')
    self._datasource_name = datasource_name

  @property
  def datasource_type(self) -> 'DataSourceType':
    """The datasource type of the Kernel"""
    return self._datasource_type

  @datasource_type.setter
  def datasource_type(self, datasource_type: 'DataSourceType'):
    if datasource_type is None:
      del self.datasource_type
      return
    if not isinstance(datasource_type, DataSourceType):
      raise TypeError('datasource_type must be of type DataSourceType')
    self._datasource_type = datasource_type

  @property
  def datasource_is_private(self) -> bool:
    """Whether the datasource is private"""
    return self._datasource_is_private

  @datasource_is_private.setter
  def datasource_is_private(self, datasource_is_private: bool):
    if datasource_is_private is None:
      del self.datasource_is_private
      return
    if not isinstance(datasource_is_private, bool):
      raise TypeError('datasource_is_private must be of type bool')
    self._datasource_is_private = datasource_is_private

  @property
  def best_public_score(self) -> float:
    """The best public score of the Kernel's submission"""
    return self._best_public_score

  @best_public_score.setter
  def best_public_score(self, best_public_score: float):
    if best_public_score is None:
      del self.best_public_score
      return
    if not isinstance(best_public_score, float):
      raise TypeError('best_public_score must be of type float')
    self._best_public_score = best_public_score

  @property
  def is_draft(self) -> bool:
    """Whether the Kernel is a draft"""
    return self._is_draft

  @is_draft.setter
  def is_draft(self, is_draft: bool):
    if is_draft is None:
      del self.is_draft
      return
    if not isinstance(is_draft, bool):
      raise TypeError('is_draft must be of type bool')
    self._is_draft = is_draft

  @property
  def fork_parent_kernel_url(self) -> str:
    """The URL of the parent fork Kernel (enriched)"""
    return self._fork_parent_kernel_url or ""

  @fork_parent_kernel_url.setter
  def fork_parent_kernel_url(self, fork_parent_kernel_url: Optional[str]):
    if fork_parent_kernel_url is None:
      del self.fork_parent_kernel_url
      return
    if not isinstance(fork_parent_kernel_url, str):
      raise TypeError('fork_parent_kernel_url must be of type str')
    self._fork_parent_kernel_url = fork_parent_kernel_url


class SearchKernelsFilters(KaggleObject):
  r"""
  Attributes:
    language (str)
      The Kernel language used to filter documents
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._language = None
    self._earned_medal = None
    self._freeze()

  @property
  def language(self) -> str:
    """The Kernel language used to filter documents"""
    return self._language or ""

  @language.setter
  def language(self, language: Optional[str]):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal


SearchKernelsDocument._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasLinkedSubmission", "has_linked_submission", "_has_linked_submission", bool, False, PredefinedSerializer()),
  FieldMetadata("forkParentUser", "fork_parent_user", "_fork_parent_user", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("datasourceName", "datasource_name", "_datasource_name", str, "", PredefinedSerializer()),
  FieldMetadata("datasourceType", "datasource_type", "_datasource_type", DataSourceType, DataSourceType.DATA_SOURCE_TYPE_COMPETITION, EnumSerializer()),
  FieldMetadata("datasourceIsPrivate", "datasource_is_private", "_datasource_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("bestPublicScore", "best_public_score", "_best_public_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("isDraft", "is_draft", "_is_draft", bool, False, PredefinedSerializer()),
  FieldMetadata("forkParentKernelUrl", "fork_parent_kernel_url", "_fork_parent_kernel_url", str, None, PredefinedSerializer(), optional=True),
]

SearchKernelsFilters._fields = [
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

