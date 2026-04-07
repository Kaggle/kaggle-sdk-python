import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class CompetitionMetricSubCategory(enum.Enum):
  r"""
  A Competition Metric Sub Category is a valid Tag ID from a short,
  predetermined list of Tags used to classify metrics
  """
  COMPETITION_METRIC_SUB_CATEGORY_UNSPECIFIED = 0
  COMPETITION_METRIC_SUB_CATEGORY_CLASSIFICATION = 13302
  COMPETITION_METRIC_SUB_CATEGORY_REGRESSION = 14203
  COMPETITION_METRIC_SUB_CATEGORY_CLUSTERING = 13304
  COMPETITION_METRIC_SUB_CATEGORY_OBJECT_DETECTION = 17074
  COMPETITION_METRIC_SUB_CATEGORY_OTHER = 16790
  COMPETITION_METRIC_SUB_CATEGORY_SEGMENTATION = 17143
  COMPETITION_METRIC_SUB_CATEGORY_DISTANCE = 17144
  COMPETITION_METRIC_SUB_CATEGORY_RETRIEVAL_RANKING = 17145

class CompetitionMetricTypeId(enum.Enum):
  r"""
  These enum values correspond to the ID values of CompetitionMetricType rows
  in the database.
  """
  COMPETITION_METRIC_TYPE_ID_UNSPECIFIED = 0
  COMPETITION_METRIC_TYPE_ID_DEFAULT = 1
  r"""
  Community metrics and most admin metrics should use the default
  Orchestrator Kernel at
  https://admin.kaggle.com/code/metric/competition-metrics-orchestrator
  """
  COMPETITION_METRIC_TYPE_ID_NO_ORCHESTRATOR = 2
  r"""
  Admins may create metrics that do not have an Orchestrator so that they
  don't need to adhere to the default metric interface. However, these
  metrics will need to fulfill the job of both a metric and orchestrator.
  """
  COMPETITION_METRIC_TYPE_ID_STAGING = 3
  r"""
  Admins may create metrics using a Staging version of the Orchestrator to
  test riskier changes
  https://www.kaggle.com/code/metric/staging-competition-metrics-orchestrator
  """

class EnvironmentRenderType(enum.Enum):
  ENVIRONMENT_RENDER_TYPE_UNSPECIFIED = 0
  ENVIRONMENT_RENDER_TYPE_JSON = 1
  ENVIRONMENT_RENDER_TYPE_HTML = 2
  """Generate .html file from episode json"""
  ENVIRONMENT_RENDER_TYPE_VIDEO = 3
  """Generate .webm file from episode json"""
  ENVIRONMENT_RENDER_TYPE_LIVE_VIDEO = 4
  """Generate .webm file and episode json simultaneously during the episode run"""

class EvaluationAlgorithmState(enum.Enum):
  EVALUATION_ALGORITHM_STATE_UNSPECIFIED = 0
  DRAFT = 1
  """Metrics which do not yet have a validated version."""
  AVAILABLE = 2
  """Metrics which have at least one validated version and are available for use"""
  BANNED = 3
  r"""
  Metrics which have a high enough failure rate that they should be
  unavailable for additional competitions
  """
  DEPRECATED = 4
  r"""
  Metrics which cannot be added to any new competitions but remain in use for
  existing deployments
  """
  LEGACY = 5
  """C# metrics which are evaluated on the Comps Worker"""
  ENVIRONMENT = 6
  """Environment (Simulations) metrics"""
  DELETED = 7
  """Metrics that have had their source Kernel deleted."""

class CompetitionMetricVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
    source_kernel_session_id (int)
      The KernelSession upon which validation was run
    is_valid (bool)
      Whether validation succeeded on this version. Unset if validation has not
      yet completed.
    validation_error (str)
      If validation failed, the reason why. Should be human readable to be
      displayed on the metric Kernel Viewer
    source_kernel_version_number (int)
      The version of the Kernel used for this metric version's source code.
    detailed_description (str)
      The docstring extracted at validation time to be displayed to hosts setting
      up competitions. Required for valid versions.
    has_non_standard_submissions (bool)
      Whether this metric expects submissions that are not the usual CSV or
      Parquet.
  """

  def __init__(self):
    self._id = 0
    self._source_kernel_session_id = 0
    self._is_valid = None
    self._validation_error = None
    self._source_kernel_version_number = 0
    self._detailed_description = None
    self._has_non_standard_submissions = False
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
  def source_kernel_session_id(self) -> int:
    """The KernelSession upon which validation was run"""
    return self._source_kernel_session_id

  @source_kernel_session_id.setter
  def source_kernel_session_id(self, source_kernel_session_id: int):
    if source_kernel_session_id is None:
      del self.source_kernel_session_id
      return
    if not isinstance(source_kernel_session_id, int):
      raise TypeError('source_kernel_session_id must be of type int')
    self._source_kernel_session_id = source_kernel_session_id

  @property
  def is_valid(self) -> bool:
    r"""
    Whether validation succeeded on this version. Unset if validation has not
    yet completed.
    """
    return self._is_valid or False

  @is_valid.setter
  def is_valid(self, is_valid: Optional[bool]):
    if is_valid is None:
      del self.is_valid
      return
    if not isinstance(is_valid, bool):
      raise TypeError('is_valid must be of type bool')
    self._is_valid = is_valid

  @property
  def validation_error(self) -> str:
    r"""
    If validation failed, the reason why. Should be human readable to be
    displayed on the metric Kernel Viewer
    """
    return self._validation_error or ""

  @validation_error.setter
  def validation_error(self, validation_error: Optional[str]):
    if validation_error is None:
      del self.validation_error
      return
    if not isinstance(validation_error, str):
      raise TypeError('validation_error must be of type str')
    self._validation_error = validation_error

  @property
  def source_kernel_version_number(self) -> int:
    """The version of the Kernel used for this metric version's source code."""
    return self._source_kernel_version_number

  @source_kernel_version_number.setter
  def source_kernel_version_number(self, source_kernel_version_number: int):
    if source_kernel_version_number is None:
      del self.source_kernel_version_number
      return
    if not isinstance(source_kernel_version_number, int):
      raise TypeError('source_kernel_version_number must be of type int')
    self._source_kernel_version_number = source_kernel_version_number

  @property
  def detailed_description(self) -> str:
    r"""
    The docstring extracted at validation time to be displayed to hosts setting
    up competitions. Required for valid versions.
    """
    return self._detailed_description or ""

  @detailed_description.setter
  def detailed_description(self, detailed_description: Optional[str]):
    if detailed_description is None:
      del self.detailed_description
      return
    if not isinstance(detailed_description, str):
      raise TypeError('detailed_description must be of type str')
    self._detailed_description = detailed_description

  @property
  def has_non_standard_submissions(self) -> bool:
    r"""
    Whether this metric expects submissions that are not the usual CSV or
    Parquet.
    """
    return self._has_non_standard_submissions

  @has_non_standard_submissions.setter
  def has_non_standard_submissions(self, has_non_standard_submissions: bool):
    if has_non_standard_submissions is None:
      del self.has_non_standard_submissions
      return
    if not isinstance(has_non_standard_submissions, bool):
      raise TypeError('has_non_standard_submissions must be of type bool')
    self._has_non_standard_submissions = has_non_standard_submissions


class EvaluationAlgorithm(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    is_max (bool)
    is_public (bool)
    is_environment (bool)
      Simulations metrics
    environment_render_type (EnvironmentRenderType)
    kernel_id (int)
      Kernel metrics
    latest_competition_metric_version_id (int)
    state (EvaluationAlgorithmState)
    pass_complete_submission (bool)
      Whether each call to `score` should receive the entire user submission
      rather than a public/private split.
    allow_internet (bool)
      Admins can always use internet, but this flag can be set by admins to
      allow-list non-admin metrics. Should only be used with trusted Community
      hosts.
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._is_max = False
    self._is_public = False
    self._is_environment = False
    self._environment_render_type = EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED
    self._kernel_id = None
    self._latest_competition_metric_version_id = None
    self._state = EvaluationAlgorithmState.EVALUATION_ALGORITHM_STATE_UNSPECIFIED
    self._pass_complete_submission = False
    self._allow_internet = False
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
  def is_max(self) -> bool:
    return self._is_max

  @is_max.setter
  def is_max(self, is_max: bool):
    if is_max is None:
      del self.is_max
      return
    if not isinstance(is_max, bool):
      raise TypeError('is_max must be of type bool')
    self._is_max = is_max

  @property
  def is_public(self) -> bool:
    return self._is_public

  @is_public.setter
  def is_public(self, is_public: bool):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def is_environment(self) -> bool:
    """Simulations metrics"""
    return self._is_environment

  @is_environment.setter
  def is_environment(self, is_environment: bool):
    if is_environment is None:
      del self.is_environment
      return
    if not isinstance(is_environment, bool):
      raise TypeError('is_environment must be of type bool')
    self._is_environment = is_environment

  @property
  def environment_render_type(self) -> 'EnvironmentRenderType':
    return self._environment_render_type

  @environment_render_type.setter
  def environment_render_type(self, environment_render_type: 'EnvironmentRenderType'):
    if environment_render_type is None:
      del self.environment_render_type
      return
    if not isinstance(environment_render_type, EnvironmentRenderType):
      raise TypeError('environment_render_type must be of type EnvironmentRenderType')
    self._environment_render_type = environment_render_type

  @property
  def kernel_id(self) -> int:
    """Kernel metrics"""
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: Optional[int]):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def latest_competition_metric_version_id(self) -> int:
    return self._latest_competition_metric_version_id or 0

  @latest_competition_metric_version_id.setter
  def latest_competition_metric_version_id(self, latest_competition_metric_version_id: Optional[int]):
    if latest_competition_metric_version_id is None:
      del self.latest_competition_metric_version_id
      return
    if not isinstance(latest_competition_metric_version_id, int):
      raise TypeError('latest_competition_metric_version_id must be of type int')
    self._latest_competition_metric_version_id = latest_competition_metric_version_id

  @property
  def state(self) -> 'EvaluationAlgorithmState':
    return self._state

  @state.setter
  def state(self, state: 'EvaluationAlgorithmState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, EvaluationAlgorithmState):
      raise TypeError('state must be of type EvaluationAlgorithmState')
    self._state = state

  @property
  def pass_complete_submission(self) -> bool:
    r"""
    Whether each call to `score` should receive the entire user submission
    rather than a public/private split.
    """
    return self._pass_complete_submission

  @pass_complete_submission.setter
  def pass_complete_submission(self, pass_complete_submission: bool):
    if pass_complete_submission is None:
      del self.pass_complete_submission
      return
    if not isinstance(pass_complete_submission, bool):
      raise TypeError('pass_complete_submission must be of type bool')
    self._pass_complete_submission = pass_complete_submission

  @property
  def allow_internet(self) -> bool:
    r"""
    Admins can always use internet, but this flag can be set by admins to
    allow-list non-admin metrics. Should only be used with trusted Community
    hosts.
    """
    return self._allow_internet

  @allow_internet.setter
  def allow_internet(self, allow_internet: bool):
    if allow_internet is None:
      del self.allow_internet
      return
    if not isinstance(allow_internet, bool):
      raise TypeError('allow_internet must be of type bool')
    self._allow_internet = allow_internet


CompetitionMetricVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceKernelSessionId", "source_kernel_session_id", "_source_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isValid", "is_valid", "_is_valid", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("validationError", "validation_error", "_validation_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceKernelVersionNumber", "source_kernel_version_number", "_source_kernel_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("detailedDescription", "detailed_description", "_detailed_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasNonStandardSubmissions", "has_non_standard_submissions", "_has_non_standard_submissions", bool, False, PredefinedSerializer()),
]

EvaluationAlgorithm._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("isMax", "is_max", "_is_max", bool, False, PredefinedSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, False, PredefinedSerializer()),
  FieldMetadata("isEnvironment", "is_environment", "_is_environment", bool, False, PredefinedSerializer()),
  FieldMetadata("environmentRenderType", "environment_render_type", "_environment_render_type", EnvironmentRenderType, EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("latestCompetitionMetricVersionId", "latest_competition_metric_version_id", "_latest_competition_metric_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("state", "state", "_state", EvaluationAlgorithmState, EvaluationAlgorithmState.EVALUATION_ALGORITHM_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("passCompleteSubmission", "pass_complete_submission", "_pass_complete_submission", bool, False, PredefinedSerializer()),
  FieldMetadata("allowInternet", "allow_internet", "_allow_internet", bool, False, PredefinedSerializer()),
]

