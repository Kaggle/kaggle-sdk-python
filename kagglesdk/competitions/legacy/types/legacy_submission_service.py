from datetime import datetime
from kagglesdk.competitions.types.submission_status import SubmissionStatus
from kagglesdk.kaggle_object import *
from typing import Optional, List

class GetMostRecentSubmissionStatusRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      Must be provided.
    team_id (int)
    submission_id (int)
      All three are optional filters to restrict the Submission search.
    greater_than_submission_id (int)
    ignore_remaining_daily_submissions (bool)
      Whether the skip the extra calculation of this field.
  """

  def __init__(self):
    self._competition_id = 0
    self._team_id = None
    self._submission_id = None
    self._greater_than_submission_id = None
    self._ignore_remaining_daily_submissions = False
    self._freeze()

  @property
  def competition_id(self) -> int:
    """Must be provided."""
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
    """All three are optional filters to restrict the Submission search."""
    return self._submission_id or 0

  @submission_id.setter
  def submission_id(self, submission_id: Optional[int]):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def team_id(self) -> int:
    return self._team_id or 0

  @team_id.setter
  def team_id(self, team_id: Optional[int]):
    if team_id is None:
      del self.team_id
      return
    if not isinstance(team_id, int):
      raise TypeError('team_id must be of type int')
    self._team_id = team_id

  @property
  def greater_than_submission_id(self) -> int:
    return self._greater_than_submission_id or 0

  @greater_than_submission_id.setter
  def greater_than_submission_id(self, greater_than_submission_id: Optional[int]):
    if greater_than_submission_id is None:
      del self.greater_than_submission_id
      return
    if not isinstance(greater_than_submission_id, int):
      raise TypeError('greater_than_submission_id must be of type int')
    self._greater_than_submission_id = greater_than_submission_id

  @property
  def ignore_remaining_daily_submissions(self) -> bool:
    """Whether the skip the extra calculation of this field."""
    return self._ignore_remaining_daily_submissions

  @ignore_remaining_daily_submissions.setter
  def ignore_remaining_daily_submissions(self, ignore_remaining_daily_submissions: bool):
    if ignore_remaining_daily_submissions is None:
      del self.ignore_remaining_daily_submissions
      return
    if not isinstance(ignore_remaining_daily_submissions, bool):
      raise TypeError('ignore_remaining_daily_submissions must be of type bool')
    self._ignore_remaining_daily_submissions = ignore_remaining_daily_submissions


class GetMostRecentSubmissionStatusResponse(KaggleObject):
  r"""
  Attributes:
    submission (LegacySubmissionExtended)
  """

  def __init__(self):
    self._submission = None
    self._freeze()

  @property
  def submission(self) -> Optional['LegacySubmissionExtended']:
    return self._submission

  @submission.setter
  def submission(self, submission: Optional['LegacySubmissionExtended']):
    if submission is None:
      del self.submission
      return
    if not isinstance(submission, LegacySubmissionExtended):
      raise TypeError('submission must be of type LegacySubmissionExtended')
    self._submission = submission


class LegacySandboxSubmission(KaggleObject):
  r"""
  Specifically built for the ListSandboxSubmissions endpoint.

  Attributes:
    id (int)
    name (str)
    public_score_formatted (str)
    private_score_formatted (str)
    submission_status (SubmissionStatus)
    error (str)
    date_submitted (datetime)
    is_benchmark (bool)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._public_score_formatted = None
    self._private_score_formatted = None
    self._submission_status = SubmissionStatus.PENDING
    self._error = None
    self._date_submitted = None
    self._is_benchmark = False
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
  def public_score_formatted(self) -> str:
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
    return self._private_score_formatted or ""

  @private_score_formatted.setter
  def private_score_formatted(self, private_score_formatted: Optional[str]):
    if private_score_formatted is None:
      del self.private_score_formatted
      return
    if not isinstance(private_score_formatted, str):
      raise TypeError('private_score_formatted must be of type str')
    self._private_score_formatted = private_score_formatted

  @property
  def submission_status(self) -> 'SubmissionStatus':
    return self._submission_status

  @submission_status.setter
  def submission_status(self, submission_status: 'SubmissionStatus'):
    if submission_status is None:
      del self.submission_status
      return
    if not isinstance(submission_status, SubmissionStatus):
      raise TypeError('submission_status must be of type SubmissionStatus')
    self._submission_status = submission_status

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def date_submitted(self) -> datetime:
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
  def is_benchmark(self) -> bool:
    return self._is_benchmark

  @is_benchmark.setter
  def is_benchmark(self, is_benchmark: bool):
    if is_benchmark is None:
      del self.is_benchmark
      return
    if not isinstance(is_benchmark, bool):
      raise TypeError('is_benchmark must be of type bool')
    self._is_benchmark = is_benchmark


class LegacySubmissionExtended(KaggleObject):
  r"""
  Contains raw Submission data, as well as extended data about scoring
  progress, such as position in pipeline and estimated wait and score
  durations.

  Attributes:
    name (str)
    public_score_formatted (str)
    private_score_formatted (str)
    previous_best_public_score_formatted (str)
    submission_status (SubmissionStatus)
    error (str)
    elapsed_score_duration_milliseconds (int)
    date_submitted (datetime)
    user_display_name (str)
  """

  def __init__(self):
    self._name = ""
    self._public_score_formatted = None
    self._private_score_formatted = None
    self._previous_best_public_score_formatted = None
    self._submission_status = SubmissionStatus.PENDING
    self._error = None
    self._elapsed_score_duration_milliseconds = None
    self._date_submitted = None
    self._user_display_name = ""
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
  def public_score_formatted(self) -> str:
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
    return self._private_score_formatted or ""

  @private_score_formatted.setter
  def private_score_formatted(self, private_score_formatted: Optional[str]):
    if private_score_formatted is None:
      del self.private_score_formatted
      return
    if not isinstance(private_score_formatted, str):
      raise TypeError('private_score_formatted must be of type str')
    self._private_score_formatted = private_score_formatted

  @property
  def previous_best_public_score_formatted(self) -> str:
    return self._previous_best_public_score_formatted or ""

  @previous_best_public_score_formatted.setter
  def previous_best_public_score_formatted(self, previous_best_public_score_formatted: Optional[str]):
    if previous_best_public_score_formatted is None:
      del self.previous_best_public_score_formatted
      return
    if not isinstance(previous_best_public_score_formatted, str):
      raise TypeError('previous_best_public_score_formatted must be of type str')
    self._previous_best_public_score_formatted = previous_best_public_score_formatted

  @property
  def submission_status(self) -> 'SubmissionStatus':
    return self._submission_status

  @submission_status.setter
  def submission_status(self, submission_status: 'SubmissionStatus'):
    if submission_status is None:
      del self.submission_status
      return
    if not isinstance(submission_status, SubmissionStatus):
      raise TypeError('submission_status must be of type SubmissionStatus')
    self._submission_status = submission_status

  @property
  def error(self) -> str:
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def elapsed_score_duration_milliseconds(self) -> int:
    return self._elapsed_score_duration_milliseconds or 0

  @elapsed_score_duration_milliseconds.setter
  def elapsed_score_duration_milliseconds(self, elapsed_score_duration_milliseconds: Optional[int]):
    if elapsed_score_duration_milliseconds is None:
      del self.elapsed_score_duration_milliseconds
      return
    if not isinstance(elapsed_score_duration_milliseconds, int):
      raise TypeError('elapsed_score_duration_milliseconds must be of type int')
    self._elapsed_score_duration_milliseconds = elapsed_score_duration_milliseconds

  @property
  def date_submitted(self) -> datetime:
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
  def user_display_name(self) -> str:
    return self._user_display_name

  @user_display_name.setter
  def user_display_name(self, user_display_name: str):
    if user_display_name is None:
      del self.user_display_name
      return
    if not isinstance(user_display_name, str):
      raise TypeError('user_display_name must be of type str')
    self._user_display_name = user_display_name


class ListSandboxSubmissionsRequest(KaggleObject):
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


class ListSandboxSubmissionsResponse(KaggleObject):
  r"""
  Attributes:
    sandbox_submissions (LegacySandboxSubmission)
  """

  def __init__(self):
    self._sandbox_submissions = []
    self._freeze()

  @property
  def sandbox_submissions(self) -> Optional[List[Optional['LegacySandboxSubmission']]]:
    return self._sandbox_submissions

  @sandbox_submissions.setter
  def sandbox_submissions(self, sandbox_submissions: Optional[List[Optional['LegacySandboxSubmission']]]):
    if sandbox_submissions is None:
      del self.sandbox_submissions
      return
    if not isinstance(sandbox_submissions, list):
      raise TypeError('sandbox_submissions must be of type list')
    if not all([isinstance(t, LegacySandboxSubmission) for t in sandbox_submissions]):
      raise TypeError('sandbox_submissions must contain only items of type LegacySandboxSubmission')
    self._sandbox_submissions = sandbox_submissions


GetMostRecentSubmissionStatusRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamId", "team_id", "_team_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("greaterThanSubmissionId", "greater_than_submission_id", "_greater_than_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ignoreRemainingDailySubmissions", "ignore_remaining_daily_submissions", "_ignore_remaining_daily_submissions", bool, False, PredefinedSerializer()),
]

GetMostRecentSubmissionStatusResponse._fields = [
  FieldMetadata("submission", "submission", "_submission", LegacySubmissionExtended, None, KaggleObjectSerializer()),
]

LegacySandboxSubmission._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("publicScoreFormatted", "public_score_formatted", "_public_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateScoreFormatted", "private_score_formatted", "_private_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionStatus", "submission_status", "_submission_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateSubmitted", "date_submitted", "_date_submitted", datetime, None, DateTimeSerializer()),
  FieldMetadata("isBenchmark", "is_benchmark", "_is_benchmark", bool, False, PredefinedSerializer()),
]

LegacySubmissionExtended._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("publicScoreFormatted", "public_score_formatted", "_public_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateScoreFormatted", "private_score_formatted", "_private_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("previousBestPublicScoreFormatted", "previous_best_public_score_formatted", "_previous_best_public_score_formatted", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionStatus", "submission_status", "_submission_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("elapsedScoreDurationMilliseconds", "elapsed_score_duration_milliseconds", "_elapsed_score_duration_milliseconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateSubmitted", "date_submitted", "_date_submitted", datetime, None, DateTimeSerializer()),
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, "", PredefinedSerializer()),
]

ListSandboxSubmissionsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListSandboxSubmissionsResponse._fields = [
  FieldMetadata("sandboxSubmissions", "sandbox_submissions", "_sandbox_submissions", LegacySandboxSubmission, [], ListSerializer(KaggleObjectSerializer())),
]

