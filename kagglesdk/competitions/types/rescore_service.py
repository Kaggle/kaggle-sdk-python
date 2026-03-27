from datetime import datetime
from kagglesdk.competitions.types.rescore import RescoreState, RescoreType
from kagglesdk.kaggle_object import *
from typing import Optional, List

class BulkRescoreInfo(KaggleObject):
  r"""
  Attributes:
    id (int)
    date_initiated (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    state_counts (RescoreStateCount)
  """

  def __init__(self):
    self._id = 0
    self._date_initiated = None
    self._state_counts = []
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
  def date_initiated(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_initiated

  @date_initiated.setter
  def date_initiated(self, date_initiated: datetime):
    if date_initiated is None:
      del self.date_initiated
      return
    if not isinstance(date_initiated, datetime):
      raise TypeError('date_initiated must be of type datetime')
    self._date_initiated = date_initiated

  @property
  def state_counts(self) -> Optional[List[Optional['RescoreStateCount']]]:
    return self._state_counts

  @state_counts.setter
  def state_counts(self, state_counts: Optional[List[Optional['RescoreStateCount']]]):
    if state_counts is None:
      del self.state_counts
      return
    if not isinstance(state_counts, list):
      raise TypeError('state_counts must be of type list')
    if not all([isinstance(t, RescoreStateCount) for t in state_counts]):
      raise TypeError('state_counts must contain only items of type RescoreStateCount')
    self._state_counts = state_counts


class CancelBulkRescoreRequest(KaggleObject):
  r"""
  Attributes:
    bulk_rescore_id (int)
  """

  def __init__(self):
    self._bulk_rescore_id = 0
    self._freeze()

  @property
  def bulk_rescore_id(self) -> int:
    return self._bulk_rescore_id

  @bulk_rescore_id.setter
  def bulk_rescore_id(self, bulk_rescore_id: int):
    if bulk_rescore_id is None:
      del self.bulk_rescore_id
      return
    if not isinstance(bulk_rescore_id, int):
      raise TypeError('bulk_rescore_id must be of type int')
    self._bulk_rescore_id = bulk_rescore_id


class CancelBulkRescoreResponse(KaggleObject):
  r"""
  Attributes:
    num_canceled (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
  """

  def __init__(self):
    self._num_canceled = 0
    self._freeze()

  @property
  def num_canceled(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_canceled

  @num_canceled.setter
  def num_canceled(self, num_canceled: int):
    if num_canceled is None:
      del self.num_canceled
      return
    if not isinstance(num_canceled, int):
      raise TypeError('num_canceled must be of type int')
    self._num_canceled = num_canceled


class InitiateBulkRescoreRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    rescore_type (RescoreType)
    num_submissions (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    submission_ids (int)
      If rescore_type is MANUAL, at least one of the following must be set.
    team_ids (int)
    bulk_rerun_id (int)
      If rescore_type is BULK_RERUN, the ID of the Bulk Rerun to rescore.
  """

  def __init__(self):
    self._competition_id = 0
    self._rescore_type = RescoreType.RESCORE_TYPE_UNSPECIFIED
    self._num_submissions = None
    self._submission_ids = []
    self._team_ids = []
    self._bulk_rerun_id = None
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

  @property
  def rescore_type(self) -> 'RescoreType':
    return self._rescore_type

  @rescore_type.setter
  def rescore_type(self, rescore_type: 'RescoreType'):
    if rescore_type is None:
      del self.rescore_type
      return
    if not isinstance(rescore_type, RescoreType):
      raise TypeError('rescore_type must be of type RescoreType')
    self._rescore_type = rescore_type

  @property
  def num_submissions(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_submissions or 0

  @num_submissions.setter
  def num_submissions(self, num_submissions: Optional[int]):
    if num_submissions is None:
      del self.num_submissions
      return
    if not isinstance(num_submissions, int):
      raise TypeError('num_submissions must be of type int')
    self._num_submissions = num_submissions

  @property
  def submission_ids(self) -> Optional[List[int]]:
    """If rescore_type is MANUAL, at least one of the following must be set."""
    return self._submission_ids

  @submission_ids.setter
  def submission_ids(self, submission_ids: Optional[List[int]]):
    if submission_ids is None:
      del self.submission_ids
      return
    if not isinstance(submission_ids, list):
      raise TypeError('submission_ids must be of type list')
    if not all([isinstance(t, int) for t in submission_ids]):
      raise TypeError('submission_ids must contain only items of type int')
    self._submission_ids = submission_ids

  @property
  def team_ids(self) -> Optional[List[int]]:
    return self._team_ids

  @team_ids.setter
  def team_ids(self, team_ids: Optional[List[int]]):
    if team_ids is None:
      del self.team_ids
      return
    if not isinstance(team_ids, list):
      raise TypeError('team_ids must be of type list')
    if not all([isinstance(t, int) for t in team_ids]):
      raise TypeError('team_ids must contain only items of type int')
    self._team_ids = team_ids

  @property
  def bulk_rerun_id(self) -> int:
    """If rescore_type is BULK_RERUN, the ID of the Bulk Rerun to rescore."""
    return self._bulk_rerun_id or 0

  @bulk_rerun_id.setter
  def bulk_rerun_id(self, bulk_rerun_id: Optional[int]):
    if bulk_rerun_id is None:
      del self.bulk_rerun_id
      return
    if not isinstance(bulk_rerun_id, int):
      raise TypeError('bulk_rerun_id must be of type int')
    self._bulk_rerun_id = bulk_rerun_id


class InitiateBulkRescoreResponse(KaggleObject):
  r"""
  Attributes:
    bulk_rescore_id (int)
    num_initiated (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
  """

  def __init__(self):
    self._bulk_rescore_id = 0
    self._num_initiated = 0
    self._freeze()

  @property
  def bulk_rescore_id(self) -> int:
    return self._bulk_rescore_id

  @bulk_rescore_id.setter
  def bulk_rescore_id(self, bulk_rescore_id: int):
    if bulk_rescore_id is None:
      del self.bulk_rescore_id
      return
    if not isinstance(bulk_rescore_id, int):
      raise TypeError('bulk_rescore_id must be of type int')
    self._bulk_rescore_id = bulk_rescore_id

  @property
  def num_initiated(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_initiated

  @num_initiated.setter
  def num_initiated(self, num_initiated: int):
    if num_initiated is None:
      del self.num_initiated
      return
    if not isinstance(num_initiated, int):
      raise TypeError('num_initiated must be of type int')
    self._num_initiated = num_initiated


class ListBulkRescoresRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

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


class ListBulkRescoresResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    bulk_rescores (BulkRescoreInfo)
  """

  def __init__(self):
    self._bulk_rescores = []
    self._freeze()

  @property
  def bulk_rescores(self) -> Optional[List[Optional['BulkRescoreInfo']]]:
    return self._bulk_rescores

  @bulk_rescores.setter
  def bulk_rescores(self, bulk_rescores: Optional[List[Optional['BulkRescoreInfo']]]):
    if bulk_rescores is None:
      del self.bulk_rescores
      return
    if not isinstance(bulk_rescores, list):
      raise TypeError('bulk_rescores must be of type list')
    if not all([isinstance(t, BulkRescoreInfo) for t in bulk_rescores]):
      raise TypeError('bulk_rescores must contain only items of type BulkRescoreInfo')
    self._bulk_rescores = bulk_rescores


class RescoreStateCount(KaggleObject):
  r"""
  Attributes:
    state (RescoreState)
    count (int)
  """

  def __init__(self):
    self._state = RescoreState.RESCORE_STATE_UNSPECIFIED
    self._count = 0
    self._freeze()

  @property
  def state(self) -> 'RescoreState':
    return self._state

  @state.setter
  def state(self, state: 'RescoreState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, RescoreState):
      raise TypeError('state must be of type RescoreState')
    self._state = state

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


class RescoreSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    submission_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._submission_id = 0
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

  @property
  def submission_id(self) -> int:
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: int):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id


BulkRescoreInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dateInitiated", "date_initiated", "_date_initiated", datetime, None, DateTimeSerializer()),
  FieldMetadata("stateCounts", "state_counts", "_state_counts", RescoreStateCount, [], ListSerializer(KaggleObjectSerializer())),
]

CancelBulkRescoreRequest._fields = [
  FieldMetadata("bulkRescoreId", "bulk_rescore_id", "_bulk_rescore_id", int, 0, PredefinedSerializer()),
]

CancelBulkRescoreResponse._fields = [
  FieldMetadata("numCanceled", "num_canceled", "_num_canceled", int, 0, PredefinedSerializer()),
]

InitiateBulkRescoreRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rescoreType", "rescore_type", "_rescore_type", RescoreType, RescoreType.RESCORE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("numSubmissions", "num_submissions", "_num_submissions", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("teamIds", "team_ids", "_team_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("bulkRerunId", "bulk_rerun_id", "_bulk_rerun_id", int, None, PredefinedSerializer(), optional=True),
]

InitiateBulkRescoreResponse._fields = [
  FieldMetadata("bulkRescoreId", "bulk_rescore_id", "_bulk_rescore_id", int, 0, PredefinedSerializer()),
  FieldMetadata("numInitiated", "num_initiated", "_num_initiated", int, 0, PredefinedSerializer()),
]

ListBulkRescoresRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListBulkRescoresResponse._fields = [
  FieldMetadata("bulkRescores", "bulk_rescores", "_bulk_rescores", BulkRescoreInfo, [], ListSerializer(KaggleObjectSerializer())),
]

RescoreStateCount._fields = [
  FieldMetadata("state", "state", "_state", RescoreState, RescoreState.RESCORE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

RescoreSubmissionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
]

