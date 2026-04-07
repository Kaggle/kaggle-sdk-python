import enum
from kagglesdk.competitions.types.notebook import CompetitionNotebook
from kagglesdk.competitions.types.submission import Submission
from kagglesdk.competitions.types.team import SubmissionLimitInfo
from kagglesdk.kaggle_object import *
from typing import Optional, List, Dict

class SubmissionNotAllowedReasonCode(enum.Enum):
  SUBMISSION_NOT_ALLOWED_REASON_CODE_UNSPECIFIED = 0
  SUBMISSION_NOT_ALLOWED_REASON_CODE_COMPETITION_DISABLED = 1
  """The Comp has disabled submissions."""
  SUBMISSION_NOT_ALLOWED_REASON_CODE_TEAM_NOT_FOUND = 2
  """Current User did not have Team in given comp."""
  SUBMISSION_NOT_ALLOWED_REASON_CODE_TEAM_ALLOWANCE_EXCEEDED = 3
  """Checks the Current User's Team's Daily/Global Submission allowance."""
  SUBMISSION_NOT_ALLOWED_REASON_CODE_KERNEL_STILL_RUNNING = 4
  SUBMISSION_NOT_ALLOWED_REASON_CODE_KERNEL_RUNTIME_EXCEEDED = 5
  SUBMISSION_NOT_ALLOWED_REASON_CODE_MISSING_COMPETITION_DATASOURCE = 6
  SUBMISSION_NOT_ALLOWED_REASON_CODE_HAS_OTHER_COMPETITION_DATASOURCE = 7
  SUBMISSION_NOT_ALLOWED_REASON_CODE_HAS_DATASET_DATASOURCE = 8
  SUBMISSION_NOT_ALLOWED_REASON_CODE_HAS_KERNEL_DATASOURCE = 9
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_GPU = 10
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_INTERNET = 11
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_CUSTOM_DOCKER_IMAGE = 12
  SUBMISSION_NOT_ALLOWED_REASON_CODE_INPUT_KERNEL_REJECTED = 13
  SUBMISSION_NOT_ALLOWED_REASON_CODE_WRONG_FILE_NAME = 14
  SUBMISSION_NOT_ALLOWED_REASON_CODE_KERNEL_READ_ERROR = 15
  r"""
  GetKernelRun() can fail if the Kernel was determined to be orphaned
  and reaped.
  """
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_TPU = 16
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_NON_STANDARD_DATASET = 17
  SUBMISSION_NOT_ALLOWED_REASON_CODE_DATASET_SIZE_EXCEEDED = 18
  SUBMISSION_NOT_ALLOWED_REASON_CODE_NOT_PYTHON = 19
  SUBMISSION_NOT_ALLOWED_REASON_CODE_USES_NON_VERSIONED_DATASET = 20
  SUBMISSION_NOT_ALLOWED_REASON_CODE_EVALUATION_NOT_SETUP = 21
  SUBMISSION_NOT_ALLOWED_REASON_CODE_COMPETITION_NOT_LAUNCHED = 22
  SUBMISSION_NOT_ALLOWED_REASON_CODE_KERNEL_USES_PAID_TIER = 23
  SUBMISSION_NOT_ALLOWED_REASON_CODE_FILE_BLOB_NOT_FOUND = 24
  SUBMISSION_NOT_ALLOWED_REASON_CODE_FILE_TOO_LARGE = 25
  SUBMISSION_NOT_ALLOWED_REASON_CODE_KERNEL_FILE_NOT_FOUND = 26
  SUBMISSION_NOT_ALLOWED_REASON_CODE_INCORRECT_SUBMISSION_TYPE = 27
  SUBMISSION_NOT_ALLOWED_REASON_CODE_NEW_ENTRANTS_DISABLED = 28
  SUBMISSION_NOT_ALLOWED_REASON_CODE_MISSING_MODEL_DATASOURCE = 29
  SUBMISSION_NOT_ALLOWED_REASON_CODE_NOT_PACKAGE_NOTEBOOK = 30
  SUBMISSION_NOT_ALLOWED_REASON_CODE_PACKAGE_WITH_ERROR = 31

class CanSubmitRequest(KaggleObject):
  r"""
  Attributes:
    create_request (CreateSubmissionRequest)
  """

  def __init__(self):
    self._create_request = None
    self._freeze()

  @property
  def create_request(self) -> Optional['CreateSubmissionRequest']:
    return self._create_request

  @create_request.setter
  def create_request(self, create_request: Optional['CreateSubmissionRequest']):
    if create_request is None:
      del self.create_request
      return
    if not isinstance(create_request, CreateSubmissionRequest):
      raise TypeError('create_request must be of type CreateSubmissionRequest')
    self._create_request = create_request


class CanSubmitResponse(KaggleObject):
  r"""
  Attributes:
    can_submit (bool)
    not_allowed_reasons (SubmissionNotAllowedReason)
      can_submit == not_allowed_reasons.is_empty()
    submission_limit_info (SubmissionLimitInfo)
      The Team's submission limit stats, including how many they are allowed to
      submit right now, if team present.
    required_file_name (str)
      The filename required for all Kernel Submissions for this Competition,
      or '' if the Competition has no such constraint.
  """

  def __init__(self):
    self._can_submit = False
    self._not_allowed_reasons = []
    self._submission_limit_info = None
    self._required_file_name = ""
    self._freeze()

  @property
  def can_submit(self) -> bool:
    return self._can_submit

  @can_submit.setter
  def can_submit(self, can_submit: bool):
    if can_submit is None:
      del self.can_submit
      return
    if not isinstance(can_submit, bool):
      raise TypeError('can_submit must be of type bool')
    self._can_submit = can_submit

  @property
  def not_allowed_reasons(self) -> Optional[List[Optional['SubmissionNotAllowedReason']]]:
    """can_submit == not_allowed_reasons.is_empty()"""
    return self._not_allowed_reasons

  @not_allowed_reasons.setter
  def not_allowed_reasons(self, not_allowed_reasons: Optional[List[Optional['SubmissionNotAllowedReason']]]):
    if not_allowed_reasons is None:
      del self.not_allowed_reasons
      return
    if not isinstance(not_allowed_reasons, list):
      raise TypeError('not_allowed_reasons must be of type list')
    if not all([isinstance(t, SubmissionNotAllowedReason) for t in not_allowed_reasons]):
      raise TypeError('not_allowed_reasons must contain only items of type SubmissionNotAllowedReason')
    self._not_allowed_reasons = not_allowed_reasons

  @property
  def submission_limit_info(self) -> Optional['SubmissionLimitInfo']:
    r"""
    The Team's submission limit stats, including how many they are allowed to
    submit right now, if team present.
    """
    return self._submission_limit_info

  @submission_limit_info.setter
  def submission_limit_info(self, submission_limit_info: Optional['SubmissionLimitInfo']):
    if submission_limit_info is None:
      del self.submission_limit_info
      return
    if not isinstance(submission_limit_info, SubmissionLimitInfo):
      raise TypeError('submission_limit_info must be of type SubmissionLimitInfo')
    self._submission_limit_info = submission_limit_info

  @property
  def required_file_name(self) -> str:
    r"""
    The filename required for all Kernel Submissions for this Competition,
    or '' if the Competition has no such constraint.
    """
    return self._required_file_name

  @required_file_name.setter
  def required_file_name(self, required_file_name: str):
    if required_file_name is None:
      del self.required_file_name
      return
    if not isinstance(required_file_name, str):
      raise TypeError('required_file_name must be of type str')
    self._required_file_name = required_file_name


class ClearLeaderboardSubmissionsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The competition to have its leaderboard cleared.
    user_visible_reason (str)
      Filled in by admin / engineer to specify why a submission is invalidated.
  """

  def __init__(self):
    self._competition_id = 0
    self._user_visible_reason = ""
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The competition to have its leaderboard cleared."""
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
  def user_visible_reason(self) -> str:
    """Filled in by admin / engineer to specify why a submission is invalidated."""
    return self._user_visible_reason

  @user_visible_reason.setter
  def user_visible_reason(self, user_visible_reason: str):
    if user_visible_reason is None:
      del self.user_visible_reason
      return
    if not isinstance(user_visible_reason, str):
      raise TypeError('user_visible_reason must be of type str')
    self._user_visible_reason = user_visible_reason


class ClearLeaderboardSubmissionsResponse(KaggleObject):
  r"""
  Attributes:
    submissions_cleared (int)
      The number of submissions that were impacted.
  """

  def __init__(self):
    self._submissions_cleared = 0
    self._freeze()

  @property
  def submissions_cleared(self) -> int:
    """The number of submissions that were impacted."""
    return self._submissions_cleared

  @submissions_cleared.setter
  def submissions_cleared(self, submissions_cleared: int):
    if submissions_cleared is None:
      del self.submissions_cleared
      return
    if not isinstance(submissions_cleared, int):
      raise TypeError('submissions_cleared must be of type int')
    self._submissions_cleared = submissions_cleared


class CreateSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    kernel_source (CreateSubmissionRequest.KernelSource)
    file_source (CreateSubmissionRequest.FileSource)
    description (str)
      If empty string, a default based on the filename will be chosen.
    sandbox (bool)
      Only hosts or admins can set true.  If set, submission will be made under
      the Sandbox team, where it can later be converted to a Benchmark team.
    benchmark_model_version_id (int)
      Admin-Only
      When set, will perform a submission on behalf of a benchmark model version
      team.
  """

  class FileSource(KaggleObject):
    r"""
    Attributes:
      gcs_blob_token (str)
        Token for GCS upload of user's submission file in our temp (inbox) dir.
        'file_name' will be inferred from the GCS blob.
    """

    def __init__(self):
      self._gcs_blob_token = ""
      self._freeze()

    @property
    def gcs_blob_token(self) -> str:
      r"""
      Token for GCS upload of user's submission file in our temp (inbox) dir.
      'file_name' will be inferred from the GCS blob.
      """
      return self._gcs_blob_token

    @gcs_blob_token.setter
    def gcs_blob_token(self, gcs_blob_token: str):
      if gcs_blob_token is None:
        del self.gcs_blob_token
        return
      if not isinstance(gcs_blob_token, str):
        raise TypeError('gcs_blob_token must be of type str')
      self._gcs_blob_token = gcs_blob_token


  class KernelSource(KaggleObject):
    r"""
    Attributes:
      kernel_run_id (int)
        AKA kernel_session_id AKA script_version_id
      file_name (str)
        Filename in the Output Files of the above Kernel Session.
        Can only be unset when submitting a Package Notebook.
      skip_output_file_check (bool)
        Do not verify that the output file is present.
        For the CreateSubmissionHandler, if this is true then the
        competition must be a synchronous rerun competition.
    """

    def __init__(self):
      self._kernel_run_id = 0
      self._file_name = None
      self._skip_output_file_check = False
      self._freeze()

    @property
    def kernel_run_id(self) -> int:
      """AKA kernel_session_id AKA script_version_id"""
      return self._kernel_run_id

    @kernel_run_id.setter
    def kernel_run_id(self, kernel_run_id: int):
      if kernel_run_id is None:
        del self.kernel_run_id
        return
      if not isinstance(kernel_run_id, int):
        raise TypeError('kernel_run_id must be of type int')
      self._kernel_run_id = kernel_run_id

    @property
    def file_name(self) -> str:
      r"""
      Filename in the Output Files of the above Kernel Session.
      Can only be unset when submitting a Package Notebook.
      """
      return self._file_name or ""

    @file_name.setter
    def file_name(self, file_name: Optional[str]):
      if file_name is None:
        del self.file_name
        return
      if not isinstance(file_name, str):
        raise TypeError('file_name must be of type str')
      self._file_name = file_name

    @property
    def skip_output_file_check(self) -> bool:
      r"""
      Do not verify that the output file is present.
      For the CreateSubmissionHandler, if this is true then the
      competition must be a synchronous rerun competition.
      """
      return self._skip_output_file_check

    @skip_output_file_check.setter
    def skip_output_file_check(self, skip_output_file_check: bool):
      if skip_output_file_check is None:
        del self.skip_output_file_check
        return
      if not isinstance(skip_output_file_check, bool):
        raise TypeError('skip_output_file_check must be of type bool')
      self._skip_output_file_check = skip_output_file_check


  def __init__(self):
    self._competition_id = 0
    self._kernel_source = None
    self._file_source = None
    self._description = ""
    self._sandbox = False
    self._benchmark_model_version_id = None
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
  def kernel_source(self) -> Optional['CreateSubmissionRequest.KernelSource']:
    return self._kernel_source or None

  @kernel_source.setter
  def kernel_source(self, kernel_source: Optional['CreateSubmissionRequest.KernelSource']):
    if kernel_source is None:
      del self.kernel_source
      return
    if not isinstance(kernel_source, CreateSubmissionRequest.KernelSource):
      raise TypeError('kernel_source must be of type CreateSubmissionRequest.KernelSource')
    del self.file_source
    self._kernel_source = kernel_source

  @property
  def file_source(self) -> Optional['CreateSubmissionRequest.FileSource']:
    return self._file_source or None

  @file_source.setter
  def file_source(self, file_source: Optional['CreateSubmissionRequest.FileSource']):
    if file_source is None:
      del self.file_source
      return
    if not isinstance(file_source, CreateSubmissionRequest.FileSource):
      raise TypeError('file_source must be of type CreateSubmissionRequest.FileSource')
    del self.kernel_source
    self._file_source = file_source

  @property
  def description(self) -> str:
    """If empty string, a default based on the filename will be chosen."""
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
  def sandbox(self) -> bool:
    r"""
    Only hosts or admins can set true.  If set, submission will be made under
    the Sandbox team, where it can later be converted to a Benchmark team.
    """
    return self._sandbox

  @sandbox.setter
  def sandbox(self, sandbox: bool):
    if sandbox is None:
      del self.sandbox
      return
    if not isinstance(sandbox, bool):
      raise TypeError('sandbox must be of type bool')
    self._sandbox = sandbox

  @property
  def benchmark_model_version_id(self) -> int:
    r"""
    Admin-Only
    When set, will perform a submission on behalf of a benchmark model version
    team.
    """
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id


class GetSubmissionLimitInfoRequest(KaggleObject):
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


class GetSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
  """

  def __init__(self):
    self._submission_id = 0
    self._freeze()

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


class InvalidateSubmissionsRequest(KaggleObject):
  r"""
  Attributes:
    submission_ids (int)
      Submission ids to invalidate
    user_visible_reason (str)
      Filled in by admin / engineer to specify why an episode is invalidated.
  """

  def __init__(self):
    self._submission_ids = []
    self._user_visible_reason = ""
    self._freeze()

  @property
  def submission_ids(self) -> Optional[List[int]]:
    """Submission ids to invalidate"""
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
  def user_visible_reason(self) -> str:
    """Filled in by admin / engineer to specify why an episode is invalidated."""
    return self._user_visible_reason

  @user_visible_reason.setter
  def user_visible_reason(self, user_visible_reason: str):
    if user_visible_reason is None:
      del self.user_visible_reason
      return
    if not isinstance(user_visible_reason, str):
      raise TypeError('user_visible_reason must be of type str')
    self._user_visible_reason = user_visible_reason


class ListSubmissionsRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    selector (ListSubmissionsRequest.Selector)
    page_size (int)
    page_token (str)
      Enables retrieval of more data from the same query.  Should only be set
      to the `ListSubmissionsResponse.next_page_token` value returned by a
      previous ListSubmissions call with the exact same `selector` value.
      Otherwise should be set to '', indicating a fresh query.
  """

  class Selector(KaggleObject):
    r"""
    Attributes:
      list_option (ListSubmissionsRequest.Selector.ListOption)
      sort_option (ListSubmissionsRequest.Selector.SortOption)
      exclude_after_deadline_submissions (bool)
      submission_ids (int)
        If using the BY_ID list option, the specific ids to list.
    """

    class ListOption(enum.Enum):
      LIST_OPTION_DEFAULT = 0
      r"""
      List all otherwise matching submissions.
      TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)
      """
      LIST_OPTION_SUCCESSFUL = 1
      """List only successful submissions."""
      LIST_OPTION_SELECTED = 2
      """List only selected submissions."""
      LIST_OPTION_ERROR = 3
      """List only errored submissions."""
      LIST_OPTION_BY_ID = 4
      """List the exact submissions specified by id."""

    class SortOption(enum.Enum):
      SORT_OPTION_DEFAULT = 0
      r"""
      Sort by date submitted, newest submissions first.
      TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)
      """
      SORT_OPTION_NAME = 1
      """Sort by the name in alphabetical order."""
      SORT_OPTION_PRIVATE_SCORE = 2
      """Sort by the private score, highest score first."""
      SORT_OPTION_PUBLIC_SCORE = 3
      """Sort by the public score, highest score first."""

    def __init__(self):
      self._list_option = self.ListOption.LIST_OPTION_DEFAULT
      self._sort_option = self.SortOption.SORT_OPTION_DEFAULT
      self._exclude_after_deadline_submissions = None
      self._submission_ids = []
      self._freeze()

    @property
    def list_option(self) -> 'ListSubmissionsRequest.Selector.ListOption':
      return self._list_option

    @list_option.setter
    def list_option(self, list_option: 'ListSubmissionsRequest.Selector.ListOption'):
      if list_option is None:
        del self.list_option
        return
      if not isinstance(list_option, ListSubmissionsRequest.Selector.ListOption):
        raise TypeError('list_option must be of type ListSubmissionsRequest.Selector.ListOption')
      self._list_option = list_option

    @property
    def sort_option(self) -> 'ListSubmissionsRequest.Selector.SortOption':
      return self._sort_option

    @sort_option.setter
    def sort_option(self, sort_option: 'ListSubmissionsRequest.Selector.SortOption'):
      if sort_option is None:
        del self.sort_option
        return
      if not isinstance(sort_option, ListSubmissionsRequest.Selector.SortOption):
        raise TypeError('sort_option must be of type ListSubmissionsRequest.Selector.SortOption')
      self._sort_option = sort_option

    @property
    def exclude_after_deadline_submissions(self) -> bool:
      return self._exclude_after_deadline_submissions or False

    @exclude_after_deadline_submissions.setter
    def exclude_after_deadline_submissions(self, exclude_after_deadline_submissions: Optional[bool]):
      if exclude_after_deadline_submissions is None:
        del self.exclude_after_deadline_submissions
        return
      if not isinstance(exclude_after_deadline_submissions, bool):
        raise TypeError('exclude_after_deadline_submissions must be of type bool')
      self._exclude_after_deadline_submissions = exclude_after_deadline_submissions

    @property
    def submission_ids(self) -> Optional[List[int]]:
      """If using the BY_ID list option, the specific ids to list."""
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


  def __init__(self):
    self._team_id = 0
    self._selector = None
    self._page_size = 0
    self._page_token = ""
    self._freeze()

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
  def selector(self) -> Optional['ListSubmissionsRequest.Selector']:
    return self._selector

  @selector.setter
  def selector(self, selector: Optional['ListSubmissionsRequest.Selector']):
    if selector is None:
      del self.selector
      return
    if not isinstance(selector, ListSubmissionsRequest.Selector):
      raise TypeError('selector must be of type ListSubmissionsRequest.Selector')
    self._selector = selector

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

  @property
  def page_token(self) -> str:
    r"""
    Enables retrieval of more data from the same query.  Should only be set
    to the `ListSubmissionsResponse.next_page_token` value returned by a
    previous ListSubmissions call with the exact same `selector` value.
    Otherwise should be set to '', indicating a fresh query.
    """
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListSubmissionsResponse(KaggleObject):
  r"""
  Attributes:
    submissions (Submission)
    next_page_token (str)
      Enables retrieval of more data from the same query.  See the `page_token`
      field from `ListSubmissionsRequest` above.  If the value is '', it means
      no further results for the request.
    notebooks (CompetitionNotebook)
      The unordered list of Notebooks, if present, for all Submission
      objects above. This should be treated as a dictionary into which each
      Submission above can lookup using SubmissionId.
    selected_submission_ids (int)
      Ids of all selected submissions for the team. Results might not be
      included in the returned submissions above due to ListOption or
      pagination.
    private_eligible_submission_ids (int)
      Ids of all submissions that are either manually selected or eligible to be
      auto-selected. This list is used after a competition closes to show
      which submissions were scored. Results might not be included
      in the returned submissions above due to ListOption or pagination.
    host_visible_errors (str)
      If the calling user is a host of the competition or admin, a map of
      submission IDs to host visible errors for the submissions (if any).
  """

  def __init__(self):
    self._submissions = []
    self._next_page_token = ""
    self._notebooks = []
    self._selected_submission_ids = []
    self._private_eligible_submission_ids = []
    self._host_visible_errors = {}
    self._freeze()

  @property
  def submissions(self) -> Optional[List[Optional['Submission']]]:
    return self._submissions

  @submissions.setter
  def submissions(self, submissions: Optional[List[Optional['Submission']]]):
    if submissions is None:
      del self.submissions
      return
    if not isinstance(submissions, list):
      raise TypeError('submissions must be of type list')
    if not all([isinstance(t, Submission) for t in submissions]):
      raise TypeError('submissions must contain only items of type Submission')
    self._submissions = submissions

  @property
  def next_page_token(self) -> str:
    r"""
    Enables retrieval of more data from the same query.  See the `page_token`
    field from `ListSubmissionsRequest` above.  If the value is '', it means
    no further results for the request.
    """
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def notebooks(self) -> Optional[List[Optional['CompetitionNotebook']]]:
    r"""
    The unordered list of Notebooks, if present, for all Submission
    objects above. This should be treated as a dictionary into which each
    Submission above can lookup using SubmissionId.
    """
    return self._notebooks

  @notebooks.setter
  def notebooks(self, notebooks: Optional[List[Optional['CompetitionNotebook']]]):
    if notebooks is None:
      del self.notebooks
      return
    if not isinstance(notebooks, list):
      raise TypeError('notebooks must be of type list')
    if not all([isinstance(t, CompetitionNotebook) for t in notebooks]):
      raise TypeError('notebooks must contain only items of type CompetitionNotebook')
    self._notebooks = notebooks

  @property
  def selected_submission_ids(self) -> Optional[List[int]]:
    r"""
    Ids of all selected submissions for the team. Results might not be
    included in the returned submissions above due to ListOption or
    pagination.
    """
    return self._selected_submission_ids

  @selected_submission_ids.setter
  def selected_submission_ids(self, selected_submission_ids: Optional[List[int]]):
    if selected_submission_ids is None:
      del self.selected_submission_ids
      return
    if not isinstance(selected_submission_ids, list):
      raise TypeError('selected_submission_ids must be of type list')
    if not all([isinstance(t, int) for t in selected_submission_ids]):
      raise TypeError('selected_submission_ids must contain only items of type int')
    self._selected_submission_ids = selected_submission_ids

  @property
  def private_eligible_submission_ids(self) -> Optional[List[int]]:
    r"""
    Ids of all submissions that are either manually selected or eligible to be
    auto-selected. This list is used after a competition closes to show
    which submissions were scored. Results might not be included
    in the returned submissions above due to ListOption or pagination.
    """
    return self._private_eligible_submission_ids

  @private_eligible_submission_ids.setter
  def private_eligible_submission_ids(self, private_eligible_submission_ids: Optional[List[int]]):
    if private_eligible_submission_ids is None:
      del self.private_eligible_submission_ids
      return
    if not isinstance(private_eligible_submission_ids, list):
      raise TypeError('private_eligible_submission_ids must be of type list')
    if not all([isinstance(t, int) for t in private_eligible_submission_ids]):
      raise TypeError('private_eligible_submission_ids must contain only items of type int')
    self._private_eligible_submission_ids = private_eligible_submission_ids

  @property
  def host_visible_errors(self) -> Optional[Dict[int, str]]:
    r"""
    If the calling user is a host of the competition or admin, a map of
    submission IDs to host visible errors for the submissions (if any).
    """
    return self._host_visible_errors

  @host_visible_errors.setter
  def host_visible_errors(self, host_visible_errors: Optional[Dict[int, str]]):
    if host_visible_errors is None:
      del self.host_visible_errors
      return
    if not isinstance(host_visible_errors, dict):
      raise TypeError('host_visible_errors must be of type dict')
    if not all([isinstance(v, str) for k, v in host_visible_errors]):
      raise TypeError('host_visible_errors must contain only items of type str')
    self._host_visible_errors = host_visible_errors


class SubmissionNotAllowedReason(KaggleObject):
  r"""
  Attributes:
    code (SubmissionNotAllowedReasonCode)
    message (str)
  """

  def __init__(self):
    self._code = SubmissionNotAllowedReasonCode.SUBMISSION_NOT_ALLOWED_REASON_CODE_UNSPECIFIED
    self._message = ""
    self._freeze()

  @property
  def code(self) -> 'SubmissionNotAllowedReasonCode':
    return self._code

  @code.setter
  def code(self, code: 'SubmissionNotAllowedReasonCode'):
    if code is None:
      del self.code
      return
    if not isinstance(code, SubmissionNotAllowedReasonCode):
      raise TypeError('code must be of type SubmissionNotAllowedReasonCode')
    self._code = code

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


class UpdateSubmissionDescriptionRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
    description (str)
  """

  def __init__(self):
    self._submission_id = 0
    self._description = ""
    self._freeze()

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


class UpdateSubmissionSelectionRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
    select (bool)
      True to select, false to unselect.
  """

  def __init__(self):
    self._submission_id = 0
    self._select = False
    self._freeze()

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

  @property
  def select(self) -> bool:
    """True to select, false to unselect."""
    return self._select

  @select.setter
  def select(self, select: bool):
    if select is None:
      del self.select
      return
    if not isinstance(select, bool):
      raise TypeError('select must be of type bool')
    self._select = select


class UpdateSubmissionSelectionResponse(KaggleObject):
  r"""
  Attributes:
    submission (Submission)
    selected_submission_ids (int)
      Ids of all selected submissions for the team.
    private_eligible_submission_ids (int)
      Ids of all submissions that are either manually selected or eligible to be
      auto-selected. This list is used after a competition closes to show
      which submissions were scored.
  """

  class ErrorReason(enum.Enum):
    r"""
    If we fail for known reasons, we throw CanonicalException with ErrorInfo
    using one of these values. On success we return an empty message.
    """
    ERROR_REASON_UNSPECIFIED = 0
    SELECTIONS_DISABLED = 1
    NOT_TEAM_LEADER = 2
    TOO_MANY_SELECTED = 3
    INVALID_SUBMISSION = 4
    ALREADY_HAS_VALUE = 5

  def __init__(self):
    self._submission = None
    self._selected_submission_ids = []
    self._private_eligible_submission_ids = []
    self._freeze()

  @property
  def submission(self) -> Optional['Submission']:
    return self._submission

  @submission.setter
  def submission(self, submission: Optional['Submission']):
    if submission is None:
      del self.submission
      return
    if not isinstance(submission, Submission):
      raise TypeError('submission must be of type Submission')
    self._submission = submission

  @property
  def selected_submission_ids(self) -> Optional[List[int]]:
    """Ids of all selected submissions for the team."""
    return self._selected_submission_ids

  @selected_submission_ids.setter
  def selected_submission_ids(self, selected_submission_ids: Optional[List[int]]):
    if selected_submission_ids is None:
      del self.selected_submission_ids
      return
    if not isinstance(selected_submission_ids, list):
      raise TypeError('selected_submission_ids must be of type list')
    if not all([isinstance(t, int) for t in selected_submission_ids]):
      raise TypeError('selected_submission_ids must contain only items of type int')
    self._selected_submission_ids = selected_submission_ids

  @property
  def private_eligible_submission_ids(self) -> Optional[List[int]]:
    r"""
    Ids of all submissions that are either manually selected or eligible to be
    auto-selected. This list is used after a competition closes to show
    which submissions were scored.
    """
    return self._private_eligible_submission_ids

  @private_eligible_submission_ids.setter
  def private_eligible_submission_ids(self, private_eligible_submission_ids: Optional[List[int]]):
    if private_eligible_submission_ids is None:
      del self.private_eligible_submission_ids
      return
    if not isinstance(private_eligible_submission_ids, list):
      raise TypeError('private_eligible_submission_ids must be of type list')
    if not all([isinstance(t, int) for t in private_eligible_submission_ids]):
      raise TypeError('private_eligible_submission_ids must contain only items of type int')
    self._private_eligible_submission_ids = private_eligible_submission_ids


CanSubmitRequest._fields = [
  FieldMetadata("createRequest", "create_request", "_create_request", CreateSubmissionRequest, None, KaggleObjectSerializer()),
]

CanSubmitResponse._fields = [
  FieldMetadata("canSubmit", "can_submit", "_can_submit", bool, False, PredefinedSerializer()),
  FieldMetadata("notAllowedReasons", "not_allowed_reasons", "_not_allowed_reasons", SubmissionNotAllowedReason, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("submissionLimitInfo", "submission_limit_info", "_submission_limit_info", SubmissionLimitInfo, None, KaggleObjectSerializer()),
  FieldMetadata("requiredFileName", "required_file_name", "_required_file_name", str, "", PredefinedSerializer()),
]

ClearLeaderboardSubmissionsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userVisibleReason", "user_visible_reason", "_user_visible_reason", str, "", PredefinedSerializer()),
]

ClearLeaderboardSubmissionsResponse._fields = [
  FieldMetadata("submissionsCleared", "submissions_cleared", "_submissions_cleared", int, 0, PredefinedSerializer()),
]

CreateSubmissionRequest.FileSource._fields = [
  FieldMetadata("gcsBlobToken", "gcs_blob_token", "_gcs_blob_token", str, "", PredefinedSerializer()),
]

CreateSubmissionRequest.KernelSource._fields = [
  FieldMetadata("kernelRunId", "kernel_run_id", "_kernel_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skipOutputFileCheck", "skip_output_file_check", "_skip_output_file_check", bool, False, PredefinedSerializer()),
]

CreateSubmissionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelSource", "kernel_source", "_kernel_source", CreateSubmissionRequest.KernelSource, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("fileSource", "file_source", "_file_source", CreateSubmissionRequest.FileSource, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("sandbox", "sandbox", "_sandbox", bool, False, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
]

GetSubmissionLimitInfoRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetSubmissionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
]

InvalidateSubmissionsRequest._fields = [
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("userVisibleReason", "user_visible_reason", "_user_visible_reason", str, "", PredefinedSerializer()),
]

ListSubmissionsRequest.Selector._fields = [
  FieldMetadata("listOption", "list_option", "_list_option", ListSubmissionsRequest.Selector.ListOption, ListSubmissionsRequest.Selector.ListOption.LIST_OPTION_DEFAULT, EnumSerializer()),
  FieldMetadata("sortOption", "sort_option", "_sort_option", ListSubmissionsRequest.Selector.SortOption, ListSubmissionsRequest.Selector.SortOption.SORT_OPTION_DEFAULT, EnumSerializer()),
  FieldMetadata("excludeAfterDeadlineSubmissions", "exclude_after_deadline_submissions", "_exclude_after_deadline_submissions", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListSubmissionsRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, 0, PredefinedSerializer()),
  FieldMetadata("selector", "selector", "_selector", ListSubmissionsRequest.Selector, None, KaggleObjectSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ListSubmissionsResponse._fields = [
  FieldMetadata("submissions", "submissions", "_submissions", Submission, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("notebooks", "notebooks", "_notebooks", CompetitionNotebook, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("selectedSubmissionIds", "selected_submission_ids", "_selected_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("privateEligibleSubmissionIds", "private_eligible_submission_ids", "_private_eligible_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("hostVisibleErrors", "host_visible_errors", "_host_visible_errors", str, {}, MapSerializer(PredefinedSerializer())),
]

SubmissionNotAllowedReason._fields = [
  FieldMetadata("code", "code", "_code", SubmissionNotAllowedReasonCode, SubmissionNotAllowedReasonCode.SUBMISSION_NOT_ALLOWED_REASON_CODE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

UpdateSubmissionDescriptionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
]

UpdateSubmissionSelectionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("select", "select", "_select", bool, False, PredefinedSerializer()),
]

UpdateSubmissionSelectionResponse._fields = [
  FieldMetadata("submission", "submission", "_submission", Submission, None, KaggleObjectSerializer()),
  FieldMetadata("selectedSubmissionIds", "selected_submission_ids", "_selected_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("privateEligibleSubmissionIds", "private_eligible_submission_ids", "_private_eligible_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
]

