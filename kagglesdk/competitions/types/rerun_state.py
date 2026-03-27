import enum
from kagglesdk.competitions.types.submission_status import SubmissionStatus
from kagglesdk.kaggle_object import *
from typing import Optional

class RerunState(enum.Enum):
  RERUN_STATE_UNSPECIFIED = 0
  INITIATED = 1
  KERNEL_RUN_QUEUED = 2
  KERNEL_RUN_RUNNING = 3
  KERNEL_RUN_FAILED_TO_START = 4
  KERNEL_RUN_OUT_OF_MEMORY = 5
  KERNEL_RUN_OUT_OF_DISK = 6
  KERNEL_RUN_TIMEOUT = 7
  SUBMISSION_RUNNING = 8
  SUBMISSION_CSV_NOT_FOUND = 9
  SUBMISSION_FAILED_TO_START = 10
  SUBMISSION_GENERIC_FAILURE = 11
  SUBMISSION_SUCCEEDED = 12
  PUBLISHED = 13
  KERNEL_RUN_CANCELLED = 14
  KERNEL_RUN_UNKNOWN_ERROR = 15
  SUBMISSION_UNKNOWN_ERROR = 16
  KERNEL_RUN_KILLED = 17
  KERNEL_RUN_LIKELY_USER_CODE_ERROR = 18
  KERNEL_RUN_VIOLATED_COMPUTE_CONSTRAINTS = 19
  KERNEL_RUN_REAPED = 20
  SUBMISSION_REAPED = 21
  SUBMISSION_FAILED_TO_PUBLISH = 22
  KERNEL_RUN_MAX_OUTPUT_FILES_EXCEEDED = 23
  KERNEL_RUN_ABORTED_FOR_SUBMISSION_LIMIT = 24
  KERNEL_RUN_NOT_FOUND = 25
  KERNEL_RUN_HEARTH_SERVER_NEVER_STARTED = 26
  KERNEL_RUN_HEARTH_SERVER_CONNECTION_FAILED = 27
  KERNEL_RUN_HEARTH_SERVER_RAISED_EXCEPTION = 28
  KERNEL_RUN_HEARTH_SERVER_MISSING_ENDPOINT = 29
  KERNEL_RUN_HEARTH_GATEWAY_RAISED_EXCEPTION = 30
  KERNEL_RUN_HEARTH_INVALID_SUBMISSION = 31
  KERNEL_RUN_HEARTH_GRPC_DEADLINE_EXCEEDED = 32

class RerunStateErrorCause(enum.Enum):
  RERUN_STATE_ERROR_CAUSE_NONE = 0
  r"""
  (-- aip.dev/not-precedent: This can be used for non-error states and is a
  reasonable default.)
  (-- api-linter: core::0126::unspecified=disabled --)
  """
  RERUN_STATE_ERROR_CAUSE_UNKNOWN = 1
  """This is a real value used for error states."""
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_FAILED_TO_START = 2
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_OUT_OF_MEMORY = 3
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_OUT_OF_DISK = 4
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_TIMEOUT = 5
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_KILLED = 6
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_LIKELY_USER_CODE_ERROR = 7
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_VIOLATED_COMPUTE_CONSTRAINTS = 8
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_REAPED = 9
  RERUN_STATE_ERROR_CAUSE_SUBMISSION_CSV_NOT_FOUND = 10
  RERUN_STATE_ERROR_CAUSE_SUBMISSION_FAILED_TO_START = 11
  RERUN_STATE_ERROR_CAUSE_SUBMISSION_GENERIC_FAILURE = 12
  RERUN_STATE_ERROR_CAUSE_SUBMISSION_REAPED = 13
  RERUN_STATE_ERROR_CAUSE_SUBMISSION_FAILED_TO_PUBLISH = 14
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_MAX_OUTPUT_FILES_EXCEEDED = 15
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_ABORTED_FOR_SUBMISSION_LIMIT = 16
  RERUN_STATE_ERROR_CAUSE_KERNEL_RUN_NOT_FOUND = 17
  RERUN_STATE_ERROR_CAUSE_HEARTH_SERVER_NEVER_STARTED = 18
  RERUN_STATE_ERROR_CAUSE_HEARTH_SERVER_CONNECTION_FAILED = 19
  RERUN_STATE_ERROR_CAUSE_HEARTH_SERVER_RAISED_EXCEPTION = 20
  RERUN_STATE_ERROR_CAUSE_HEARTH_SERVER_MISSING_ENDPOINT = 21
  RERUN_STATE_ERROR_CAUSE_HEARTH_GATEWAY_RAISED_EXCEPTION = 22
  RERUN_STATE_ERROR_CAUSE_HEARTH_INVALID_SUBMISSION = 23
  RERUN_STATE_ERROR_CAUSE_HEARTH_GRPC_DEADLINE_EXCEEDED = 24

class RerunStateName(enum.Enum):
  RERUN_STATE_NAME_UNSPECIFIED = 0
  """Should never actually be used, but best practice for proto enum."""
  RERUN_STATE_NAME_INITIATED = 1
  RERUN_STATE_NAME_KERNEL_RUN_QUEUED = 2
  RERUN_STATE_NAME_KERNEL_RUN_RUNNING = 3
  RERUN_STATE_NAME_KERNEL_RUN_ERROR = 4
  RERUN_STATE_NAME_SUBMISSION_RUNNING = 5
  RERUN_STATE_NAME_SUBMISSION_ERROR = 6
  RERUN_STATE_NAME_SUBMISSION_SUCCEEDED = 7
  RERUN_STATE_NAME_PUBLISHED = 8
  RERUN_STATE_NAME_KERNEL_RUN_CANCELLED = 9

class CompetitionKernelRerunState(KaggleObject):
  r"""
  Attributes:
    id (RerunState)
    name (RerunStateName)
    error_cause (RerunStateErrorCause)
    source_submission_status (SubmissionStatus)
      The status we should apply to the source Submission when moving to this
      Rerun State. Should not be applicable to non-sync rerun comps, which rely
      on Publish to cause changes.
  """

  def __init__(self):
    self._id = RerunState.RERUN_STATE_UNSPECIFIED
    self._name = RerunStateName.RERUN_STATE_NAME_UNSPECIFIED
    self._error_cause = RerunStateErrorCause.RERUN_STATE_ERROR_CAUSE_NONE
    self._source_submission_status = SubmissionStatus.PENDING
    self._freeze()

  @property
  def id(self) -> 'RerunState':
    return self._id

  @id.setter
  def id(self, id: 'RerunState'):
    if id is None:
      del self.id
      return
    if not isinstance(id, RerunState):
      raise TypeError('id must be of type RerunState')
    self._id = id

  @property
  def name(self) -> 'RerunStateName':
    return self._name

  @name.setter
  def name(self, name: 'RerunStateName'):
    if name is None:
      del self.name
      return
    if not isinstance(name, RerunStateName):
      raise TypeError('name must be of type RerunStateName')
    self._name = name

  @property
  def error_cause(self) -> 'RerunStateErrorCause':
    return self._error_cause

  @error_cause.setter
  def error_cause(self, error_cause: 'RerunStateErrorCause'):
    if error_cause is None:
      del self.error_cause
      return
    if not isinstance(error_cause, RerunStateErrorCause):
      raise TypeError('error_cause must be of type RerunStateErrorCause')
    self._error_cause = error_cause

  @property
  def source_submission_status(self) -> 'SubmissionStatus':
    r"""
    The status we should apply to the source Submission when moving to this
    Rerun State. Should not be applicable to non-sync rerun comps, which rely
    on Publish to cause changes.
    """
    return self._source_submission_status

  @source_submission_status.setter
  def source_submission_status(self, source_submission_status: 'SubmissionStatus'):
    if source_submission_status is None:
      del self.source_submission_status
      return
    if not isinstance(source_submission_status, SubmissionStatus):
      raise TypeError('source_submission_status must be of type SubmissionStatus')
    self._source_submission_status = source_submission_status


CompetitionKernelRerunState._fields = [
  FieldMetadata("id", "id", "_id", RerunState, RerunState.RERUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("name", "name", "_name", RerunStateName, RerunStateName.RERUN_STATE_NAME_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("errorCause", "error_cause", "_error_cause", RerunStateErrorCause, RerunStateErrorCause.RERUN_STATE_ERROR_CAUSE_NONE, EnumSerializer()),
  FieldMetadata("sourceSubmissionStatus", "source_submission_status", "_source_submission_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
]

