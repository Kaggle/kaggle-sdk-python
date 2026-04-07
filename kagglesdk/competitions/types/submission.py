from datetime import datetime
from kagglesdk.competitions.types.rerun_state import CompetitionKernelRerunState
from kagglesdk.competitions.types.submission_status import SubmissionStatus
from kagglesdk.kaggle_object import *
from typing import Optional

class KernelSubmission(KaggleObject):
  r"""
  Information about a Kernel-based submission.

  Attributes:
    id (int)
    source_script_version_id (int)
    score_formatted (str)
      Rendered public or private score, depending on the owner competition's
      current leaderboard visibility.
    score_is_private (bool)
      Whether score_formatted refers to public or private score.
  """

  def __init__(self):
    self._id = 0
    self._source_script_version_id = 0
    self._score_formatted = None
    self._score_is_private = False
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
  def source_script_version_id(self) -> int:
    return self._source_script_version_id

  @source_script_version_id.setter
  def source_script_version_id(self, source_script_version_id: int):
    if source_script_version_id is None:
      del self.source_script_version_id
      return
    if not isinstance(source_script_version_id, int):
      raise TypeError('source_script_version_id must be of type int')
    self._source_script_version_id = source_script_version_id

  @property
  def score_formatted(self) -> str:
    r"""
    Rendered public or private score, depending on the owner competition's
    current leaderboard visibility.
    """
    return self._score_formatted or ""

  @score_formatted.setter
  def score_formatted(self, score_formatted: Optional[str]):
    if score_formatted is None:
      del self.score_formatted
      return
    if not isinstance(score_formatted, str):
      raise TypeError('score_formatted must be of type str')
    self._score_formatted = score_formatted

  @property
  def score_is_private(self) -> bool:
    """Whether score_formatted refers to public or private score."""
    return self._score_is_private

  @score_is_private.setter
  def score_is_private(self, score_is_private: bool):
    if score_is_private is None:
      del self.score_is_private
      return
    if not isinstance(score_is_private, bool):
      raise TypeError('score_is_private must be of type bool')
    self._score_is_private = score_is_private


class Submission(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
    details (str)
      AKA description
    submitted_user_id (int)
    date_submitted (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    team_id (int)
    is_selected (bool)
    status (SubmissionStatus)
    is_after_deadline (bool)
    processing_details (str)
    content_length (int)
    sync_rerun_state (CompetitionKernelRerunState)
    public_score_formatted (str)
      Rendered public score, with truncation and zero-padding
    private_score_formatted (str)
      Rendered private score, with truncation and zero-padding
  """

  def __init__(self):
    self._id = 0
    self._title = None
    self._details = None
    self._submitted_user_id = None
    self._date_submitted = None
    self._team_id = 0
    self._is_selected = False
    self._status = SubmissionStatus.PENDING
    self._is_after_deadline = False
    self._processing_details = None
    self._content_length = None
    self._sync_rerun_state = None
    self._public_score_formatted = None
    self._private_score_formatted = None
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
  def details(self) -> str:
    """AKA description"""
    return self._details or ""

  @details.setter
  def details(self, details: Optional[str]):
    if details is None:
      del self.details
      return
    if not isinstance(details, str):
      raise TypeError('details must be of type str')
    self._details = details

  @property
  def submitted_user_id(self) -> int:
    return self._submitted_user_id or 0

  @submitted_user_id.setter
  def submitted_user_id(self, submitted_user_id: Optional[int]):
    if submitted_user_id is None:
      del self.submitted_user_id
      return
    if not isinstance(submitted_user_id, int):
      raise TypeError('submitted_user_id must be of type int')
    self._submitted_user_id = submitted_user_id

  @property
  def date_submitted(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_submitted

  @date_submitted.setter
  def date_submitted(self, date_submitted: datetime):
    if date_submitted is None:
      del self.date_submitted
      return
    if not isinstance(date_submitted, datetime):
      raise TypeError('date_submitted must be of type datetime')
    self._date_submitted = date_submitted

  @property
  def team_id(self) -> int:
    return self._team_id

  @team_id.setter
  def team_id(self, team_id: int):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def is_selected(self) -> bool:
    return self._is_selected

  @is_selected.setter
  def is_selected(self, is_selected: bool):
    if is_selected is None:
      del self.is_selected
      return
    if not isinstance(is_selected, bool):
      raise TypeError('is_selected must be of type bool')
    self._is_selected = is_selected

  @property
  def status(self) -> 'SubmissionStatus':
    return self._status

  @status.setter
  def status(self, status: 'SubmissionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, SubmissionStatus):
      raise TypeError('status must be of type SubmissionStatus')
    self._status = status

  @property
  def is_after_deadline(self) -> bool:
    return self._is_after_deadline

  @is_after_deadline.setter
  def is_after_deadline(self, is_after_deadline: bool):
    if is_after_deadline is None:
      del self.is_after_deadline
      return
    if not isinstance(is_after_deadline, bool):
      raise TypeError('is_after_deadline must be of type bool')
    self._is_after_deadline = is_after_deadline

  @property
  def processing_details(self) -> str:
    return self._processing_details or ""

  @processing_details.setter
  def processing_details(self, processing_details: Optional[str]):
    if processing_details is None:
      del self.processing_details
      return
    if not isinstance(processing_details, str):
      raise TypeError('processing_details must be of type str')
    self._processing_details = processing_details

  @property
  def content_length(self) -> int:
    return self._content_length or 0

  @content_length.setter
  def content_length(self, content_length: Optional[int]):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def sync_rerun_state(self) -> Optional['CompetitionKernelRerunState']:
    return self._sync_rerun_state

  @sync_rerun_state.setter
  def sync_rerun_state(self, sync_rerun_state: Optional['CompetitionKernelRerunState']):
    if sync_rerun_state is None:
      del self.sync_rerun_state
      return
    if not isinstance(sync_rerun_state, CompetitionKernelRerunState):
      raise TypeError('sync_rerun_state must be of type CompetitionKernelRerunState')
    self._sync_rerun_state = sync_rerun_state

  @property
  def public_score_formatted(self) -> str:
    """Rendered public score, with truncation and zero-padding"""
    return self._public_score_formatted or ""

  @public_score_formatted.setter
  def public_score_formatted(self, public_score_formatted: Optional[str]):
    if public_score_formatted is None:
      del self.public_score_formatted
      return
    if not isinstance(public_score_formatted, str):
      raise TypeError('public_score_formatted must be of type str')
    self._public_score_formatted = public_score_formatted

  @property
  def private_score_formatted(self) -> str:
    """Rendered private score, with truncation and zero-padding"""
    return self._private_score_formatted or ""

  @private_score_formatted.setter
  def private_score_formatted(self, private_score_formatted: Optional[str]):
    if private_score_formatted is None:
      del self.private_score_formatted
      return
    if not isinstance(private_score_formatted, str):
      raise TypeError('private_score_formatted must be of type str')
    self._private_score_formatted = private_score_formatted


KernelSubmission._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceScriptVersionId", "source_script_version_id", "_source_script_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scoreFormatted", "score_formatted", "_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scoreIsPrivate", "score_is_private", "_score_is_private", bool, False, PredefinedSerializer()),
]

Submission._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("details", "details", "_details", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submittedUserId", "submitted_user_id", "_submitted_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateSubmitted", "date_submitted", "_date_submitted", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isSelected", "is_selected", "_is_selected", bool, False, PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
  FieldMetadata("isAfterDeadline", "is_after_deadline", "_is_after_deadline", bool, False, PredefinedSerializer()),
  FieldMetadata("processingDetails", "processing_details", "_processing_details", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentLength", "content_length", "_content_length", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("syncRerunState", "sync_rerun_state", "_sync_rerun_state", CompetitionKernelRerunState, None, KaggleObjectSerializer()),
  FieldMetadata("publicScoreFormatted", "public_score_formatted", "_public_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateScoreFormatted", "private_score_formatted", "_private_score_formatted", str, None, PredefinedSerializer(), optional=True),
]

