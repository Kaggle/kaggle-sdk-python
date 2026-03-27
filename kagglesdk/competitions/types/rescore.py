import enum

class RescoreType(enum.Enum):
  RESCORE_TYPE_UNSPECIFIED = 0
  RESCORE_TYPE_ALL = 1
  RESCORE_TYPE_PENDING = 2
  RESCORE_TYPE_ERRORED = 3
  RESCORE_TYPE_COMPLETED = 4
  RESCORE_TYPE_BULK_RERUN = 5
  RESCORE_TYPE_MANUAL = 6

class RescoreState(enum.Enum):
  RESCORE_STATE_UNSPECIFIED = 0
  RESCORE_STATE_INITIATED = 1
  """The Rescore has been created, but scoring has not started yet."""
  RESCORE_STATE_SCORING = 2
  """Scoring has begun."""
  RESCORE_STATE_SUBMISSION_ERROR = 3
  """Scoring failed due to a user error with the submission."""
  RESCORE_STATE_SUCCEEDED = 4
  """Scoring succeeded."""
  RESCORE_STATE_CANCELED = 5
  r"""
  Scoring was canceled, either via the admin UI or a Kernel Session
  cancellation.
  """
  RESCORE_STATE_PROCESSING_ERROR = 6
  """Scoring failed due to an internal error, and a retry is recommended."""
  RESCORE_STATE_QUEUED = 7
  """The Rescore has been queued to be scored."""
  RESCORE_STATE_COMPLETED_AWAITING_PUBLISH = 8
  """Scoring completed successfully and is pending a batch publish."""

