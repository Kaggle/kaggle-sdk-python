from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import Optional

class InvalidateCompetitionSyntheticCopiesRequest(KaggleObject):
  r"""
  Attributes:
    base_competition_id (int)
      We will invalidate all synthetic copies of this competition.
  """

  def __init__(self):
    self._base_competition_id = 0
    self._freeze()

  @property
  def base_competition_id(self) -> int:
    """We will invalidate all synthetic copies of this competition."""
    return self._base_competition_id

  @base_competition_id.setter
  def base_competition_id(self, base_competition_id: int):
    if base_competition_id is None:
      del self.base_competition_id
      return
    if not isinstance(base_competition_id, int):
      raise TypeError('base_competition_id must be of type int')
    self._base_competition_id = base_competition_id


class InvalidateCompetitionSyntheticCopiesResponse(KaggleObject):
  r"""
  Attributes:
    num_invalidated (int)
  """

  def __init__(self):
    self._num_invalidated = 0
    self._freeze()

  @property
  def num_invalidated(self) -> int:
    return self._num_invalidated

  @num_invalidated.setter
  def num_invalidated(self, num_invalidated: int):
    if num_invalidated is None:
      del self.num_invalidated
      return
    if not isinstance(num_invalidated, int):
      raise TypeError('num_invalidated must be of type int')
    self._num_invalidated = num_invalidated


class RecreateCompetitionDatabundleArchiveRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class RecreateCompetitionDatabundleArchiveResponse(KaggleObject):
  r"""
  """

  pass

class SetCompetitionDeadlineNowRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class SetCompetitionDeadlineNowResponse(KaggleObject):
  r"""
  Attributes:
    deadline (datetime)
      The new/updated competition deadline.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
  """

  def __init__(self):
    self._deadline = None
    self._freeze()

  @property
  def deadline(self) -> datetime:
    r"""
    The new/updated competition deadline.
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline


InvalidateCompetitionSyntheticCopiesRequest._fields = [
  FieldMetadata("baseCompetitionId", "base_competition_id", "_base_competition_id", int, 0, PredefinedSerializer()),
]

InvalidateCompetitionSyntheticCopiesResponse._fields = [
  FieldMetadata("numInvalidated", "num_invalidated", "_num_invalidated", int, 0, PredefinedSerializer()),
]

RecreateCompetitionDatabundleArchiveRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

RecreateCompetitionDatabundleArchiveResponse._fields = []

SetCompetitionDeadlineNowRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

SetCompetitionDeadlineNowResponse._fields = [
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
]

