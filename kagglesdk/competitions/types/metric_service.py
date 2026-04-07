import enum
from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.competitions.types.evaluation_algorithm import CompetitionMetricSubCategory, CompetitionMetricTypeId, EnvironmentRenderType, EvaluationAlgorithm, EvaluationAlgorithmState
from kagglesdk.kaggle_object import *
from typing import Optional, List

class MetricListAuthorType(enum.Enum):
  METRIC_LIST_AUTHOR_TYPE_UNSPECIFIED = 0
  METRIC_LIST_AUTHOR_TYPE_KAGGLE = 1
  METRIC_LIST_AUTHOR_TYPE_OWN = 2
  METRIC_LIST_AUTHOR_TYPE_SHARED = 3

class MetricListSourceType(enum.Enum):
  METRIC_LIST_SOURCE_TYPE_UNSPECIFIED = 0
  METRIC_LIST_SOURCE_TYPE_NOTEBOOK = 1
  METRIC_LIST_SOURCE_TYPE_LEGACY = 2
  METRIC_LIST_SOURCE_TYPE_SIMULATIONS = 3

class MetricListVisibility(enum.Enum):
  METRIC_LIST_VISIBILITY_UNSPECIFIED = 0
  METRIC_LIST_VISIBILITY_PUBLIC = 1
  METRIC_LIST_VISIBILITY_PRIVATE = 2

class CompetitionMetricMetadata(KaggleObject):
  r"""
  Attributes:
    metric_name (str)
      The current name of the metric. It should be kept in sync with the notebook
      title.
    brief_description (str)
      A short description that shows up when searching for metrics
    sub_category (CompetitionMetricSubCategory)
      The sub category of the metric
    is_max (bool)
      Whether a higher score is better on the leaderboard. Default true.
    pass_complete_submission (bool)
      Whether each call to the `score` function should pass the entire submission
      instead of public/private subsets. Default false.
    is_public (bool)
      Whether this metric should be publicly usable/visible (currently only
      updatable by admins)
    competition_metric_type_id (CompetitionMetricTypeId)
      Used by admins to override the default Orchestrator. Normal users can only
      use DEFAULT.
    scoring_timeout_minutes (int)
      Maximum allowed scoring session duration. May only be set by admins.
    allow_internet (bool)
      Whether to allow internet in metric sessions. May only be set by admins.
  """

  def __init__(self):
    self._metric_name = None
    self._brief_description = None
    self._sub_category = None
    self._is_max = None
    self._pass_complete_submission = None
    self._is_public = None
    self._competition_metric_type_id = None
    self._scoring_timeout_minutes = None
    self._allow_internet = None
    self._freeze()

  @property
  def metric_name(self) -> str:
    r"""
    The current name of the metric. It should be kept in sync with the notebook
    title.
    """
    return self._metric_name or ""

  @metric_name.setter
  def metric_name(self, metric_name: Optional[str]):
    if metric_name is None:
      del self.metric_name
      return
    if not isinstance(metric_name, str):
      raise TypeError('metric_name must be of type str')
    self._metric_name = metric_name

  @property
  def brief_description(self) -> str:
    """A short description that shows up when searching for metrics"""
    return self._brief_description or ""

  @brief_description.setter
  def brief_description(self, brief_description: Optional[str]):
    if brief_description is None:
      del self.brief_description
      return
    if not isinstance(brief_description, str):
      raise TypeError('brief_description must be of type str')
    self._brief_description = brief_description

  @property
  def sub_category(self) -> 'CompetitionMetricSubCategory':
    """The sub category of the metric"""
    return self._sub_category or CompetitionMetricSubCategory.COMPETITION_METRIC_SUB_CATEGORY_UNSPECIFIED

  @sub_category.setter
  def sub_category(self, sub_category: Optional['CompetitionMetricSubCategory']):
    if sub_category is None:
      del self.sub_category
      return
    if not isinstance(sub_category, CompetitionMetricSubCategory):
      raise TypeError('sub_category must be of type CompetitionMetricSubCategory')
    self._sub_category = sub_category

  @property
  def is_max(self) -> bool:
    """Whether a higher score is better on the leaderboard. Default true."""
    return self._is_max or False

  @is_max.setter
  def is_max(self, is_max: Optional[bool]):
    if is_max is None:
      del self.is_max
      return
    if not isinstance(is_max, bool):
      raise TypeError('is_max must be of type bool')
    self._is_max = is_max

  @property
  def pass_complete_submission(self) -> bool:
    r"""
    Whether each call to the `score` function should pass the entire submission
    instead of public/private subsets. Default false.
    """
    return self._pass_complete_submission or False

  @pass_complete_submission.setter
  def pass_complete_submission(self, pass_complete_submission: Optional[bool]):
    if pass_complete_submission is None:
      del self.pass_complete_submission
      return
    if not isinstance(pass_complete_submission, bool):
      raise TypeError('pass_complete_submission must be of type bool')
    self._pass_complete_submission = pass_complete_submission

  @property
  def is_public(self) -> bool:
    r"""
    Whether this metric should be publicly usable/visible (currently only
    updatable by admins)
    """
    return self._is_public or False

  @is_public.setter
  def is_public(self, is_public: Optional[bool]):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def competition_metric_type_id(self) -> 'CompetitionMetricTypeId':
    r"""
    Used by admins to override the default Orchestrator. Normal users can only
    use DEFAULT.
    """
    return self._competition_metric_type_id or CompetitionMetricTypeId.COMPETITION_METRIC_TYPE_ID_UNSPECIFIED

  @competition_metric_type_id.setter
  def competition_metric_type_id(self, competition_metric_type_id: Optional['CompetitionMetricTypeId']):
    if competition_metric_type_id is None:
      del self.competition_metric_type_id
      return
    if not isinstance(competition_metric_type_id, CompetitionMetricTypeId):
      raise TypeError('competition_metric_type_id must be of type CompetitionMetricTypeId')
    self._competition_metric_type_id = competition_metric_type_id

  @property
  def scoring_timeout_minutes(self) -> int:
    """Maximum allowed scoring session duration. May only be set by admins."""
    return self._scoring_timeout_minutes or 0

  @scoring_timeout_minutes.setter
  def scoring_timeout_minutes(self, scoring_timeout_minutes: Optional[int]):
    if scoring_timeout_minutes is None:
      del self.scoring_timeout_minutes
      return
    if not isinstance(scoring_timeout_minutes, int):
      raise TypeError('scoring_timeout_minutes must be of type int')
    self._scoring_timeout_minutes = scoring_timeout_minutes

  @property
  def allow_internet(self) -> bool:
    """Whether to allow internet in metric sessions. May only be set by admins."""
    return self._allow_internet or False

  @allow_internet.setter
  def allow_internet(self, allow_internet: Optional[bool]):
    if allow_internet is None:
      del self.allow_internet
      return
    if not isinstance(allow_internet, bool):
      raise TypeError('allow_internet must be of type bool')
    self._allow_internet = allow_internet


class CreateAdminMetricRequest(KaggleObject):
  r"""
  """

  pass

class CreateCompetitionMetricRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      The Competition on which 'Create a new metric' was clicked
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    """The Competition on which 'Create a new metric' was clicked"""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class CreateCompetitionMetricResponse(KaggleObject):
  r"""
  Attributes:
    http_redirect (HttpRedirect)
    evaluation_algorithm (EvaluationAlgorithm)
      Unset if creation failed
  """

  def __init__(self):
    self._http_redirect = None
    self._evaluation_algorithm = None
    self._freeze()

  @property
  def http_redirect(self) -> Optional['HttpRedirect']:
    return self._http_redirect

  @http_redirect.setter
  def http_redirect(self, http_redirect: Optional['HttpRedirect']):
    if http_redirect is None:
      del self.http_redirect
      return
    if not isinstance(http_redirect, HttpRedirect):
      raise TypeError('http_redirect must be of type HttpRedirect')
    self._http_redirect = http_redirect

  @property
  def evaluation_algorithm(self) -> Optional['EvaluationAlgorithm']:
    """Unset if creation failed"""
    return self._evaluation_algorithm or None

  @evaluation_algorithm.setter
  def evaluation_algorithm(self, evaluation_algorithm: Optional[Optional['EvaluationAlgorithm']]):
    if evaluation_algorithm is None:
      del self.evaluation_algorithm
      return
    if not isinstance(evaluation_algorithm, EvaluationAlgorithm):
      raise TypeError('evaluation_algorithm must be of type EvaluationAlgorithm')
    self._evaluation_algorithm = evaluation_algorithm


class CreateEnvironmentMetricRequest(KaggleObject):
  r"""
  Attributes:
    environment_name (str)
      This should match the folder name for this environment in
      https://github.com/Kaggle/kaggle-environments/tree/master/kaggle_environments/envs
    name (str)
    configuration (str)
      This configuration will be patched on top of the environment's default
      configuration for all episodes using this algorithm
      TODO(aip.dev/140): (-- api-linter: core::0140::abbreviations=disabled --)
    player_count_specification (str)
      This is a comma separated list of the number of players that can play in
      each game, e.g. 1,2,4 or 2,2,2,4 (the latter giving a higher chance of
      2-player games)
      TODO(aip.dev/140): (-- api-linter: core::0140::abbreviations=disabled --)
    render_type (EnvironmentRenderType)
  """

  def __init__(self):
    self._environment_name = ""
    self._name = ""
    self._configuration = ""
    self._player_count_specification = ""
    self._render_type = EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def environment_name(self) -> str:
    r"""
    This should match the folder name for this environment in
    https://github.com/Kaggle/kaggle-environments/tree/master/kaggle_environments/envs
    """
    return self._environment_name

  @environment_name.setter
  def environment_name(self, environment_name: str):
    if environment_name is None:
      del self.environment_name
      return
    if not isinstance(environment_name, str):
      raise TypeError('environment_name must be of type str')
    self._environment_name = environment_name

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
  def configuration(self) -> str:
    r"""
    This configuration will be patched on top of the environment's default
    configuration for all episodes using this algorithm
    TODO(aip.dev/140): (-- api-linter: core::0140::abbreviations=disabled --)
    """
    return self._configuration

  @configuration.setter
  def configuration(self, configuration: str):
    if configuration is None:
      del self.configuration
      return
    if not isinstance(configuration, str):
      raise TypeError('configuration must be of type str')
    self._configuration = configuration

  @property
  def player_count_specification(self) -> str:
    r"""
    This is a comma separated list of the number of players that can play in
    each game, e.g. 1,2,4 or 2,2,2,4 (the latter giving a higher chance of
    2-player games)
    TODO(aip.dev/140): (-- api-linter: core::0140::abbreviations=disabled --)
    """
    return self._player_count_specification

  @player_count_specification.setter
  def player_count_specification(self, player_count_specification: str):
    if player_count_specification is None:
      del self.player_count_specification
      return
    if not isinstance(player_count_specification, str):
      raise TypeError('player_count_specification must be of type str')
    self._player_count_specification = player_count_specification

  @property
  def render_type(self) -> 'EnvironmentRenderType':
    return self._render_type

  @render_type.setter
  def render_type(self, render_type: 'EnvironmentRenderType'):
    if render_type is None:
      del self.render_type
      return
    if not isinstance(render_type, EnvironmentRenderType):
      raise TypeError('render_type must be of type EnvironmentRenderType')
    self._render_type = render_type


class GetCompetitionMetricMetadataRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id


class GetCompetitionMetricVersionRequest(KaggleObject):
  r"""
  Attributes:
    competition_metric_version_id (int)
    source_kernel_session_id (int)
  """

  def __init__(self):
    self._competition_metric_version_id = None
    self._source_kernel_session_id = None
    self._freeze()

  @property
  def competition_metric_version_id(self) -> int:
    return self._competition_metric_version_id or 0

  @competition_metric_version_id.setter
  def competition_metric_version_id(self, competition_metric_version_id: int):
    if competition_metric_version_id is None:
      del self.competition_metric_version_id
      return
    if not isinstance(competition_metric_version_id, int):
      raise TypeError('competition_metric_version_id must be of type int')
    del self.source_kernel_session_id
    self._competition_metric_version_id = competition_metric_version_id

  @property
  def source_kernel_session_id(self) -> int:
    return self._source_kernel_session_id or 0

  @source_kernel_session_id.setter
  def source_kernel_session_id(self, source_kernel_session_id: int):
    if source_kernel_session_id is None:
      del self.source_kernel_session_id
      return
    if not isinstance(source_kernel_session_id, int):
      raise TypeError('source_kernel_session_id must be of type int')
    del self.competition_metric_version_id
    self._source_kernel_session_id = source_kernel_session_id


class ListCompetitionMetricsRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  Attributes:
    author_type (MetricListAuthorType)
      Default to all if unset or unspecified
    source_type (MetricListSourceType)
      Default to all if unset or unspecified
    visibility (MetricListVisibility)
      Default to all if unset or unspecified
  """

  def __init__(self):
    self._author_type = None
    self._source_type = None
    self._visibility = None
    self._freeze()

  @property
  def author_type(self) -> 'MetricListAuthorType':
    """Default to all if unset or unspecified"""
    return self._author_type or MetricListAuthorType.METRIC_LIST_AUTHOR_TYPE_UNSPECIFIED

  @author_type.setter
  def author_type(self, author_type: Optional['MetricListAuthorType']):
    if author_type is None:
      del self.author_type
      return
    if not isinstance(author_type, MetricListAuthorType):
      raise TypeError('author_type must be of type MetricListAuthorType')
    self._author_type = author_type

  @property
  def source_type(self) -> 'MetricListSourceType':
    """Default to all if unset or unspecified"""
    return self._source_type or MetricListSourceType.METRIC_LIST_SOURCE_TYPE_UNSPECIFIED

  @source_type.setter
  def source_type(self, source_type: Optional['MetricListSourceType']):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, MetricListSourceType):
      raise TypeError('source_type must be of type MetricListSourceType')
    self._source_type = source_type

  @property
  def visibility(self) -> 'MetricListVisibility':
    """Default to all if unset or unspecified"""
    return self._visibility or MetricListVisibility.METRIC_LIST_VISIBILITY_UNSPECIFIED

  @visibility.setter
  def visibility(self, visibility: Optional['MetricListVisibility']):
    if visibility is None:
      del self.visibility
      return
    if not isinstance(visibility, MetricListVisibility):
      raise TypeError('visibility must be of type MetricListVisibility')
    self._visibility = visibility


class ListCompetitionMetricsResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    metrics (MetricInfo)
  """

  def __init__(self):
    self._metrics = []
    self._freeze()

  @property
  def metrics(self) -> Optional[List[Optional['MetricInfo']]]:
    return self._metrics

  @metrics.setter
  def metrics(self, metrics: Optional[List[Optional['MetricInfo']]]):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, list):
      raise TypeError('metrics must be of type list')
    if not all([isinstance(t, MetricInfo) for t in metrics]):
      raise TypeError('metrics must contain only items of type MetricInfo')
    self._metrics = metrics


class MetricInfo(KaggleObject):
  r"""
  Subset of Metric/EvaluationAlgorithm fields for listing and selecting on the
  Evaluation page.

  Attributes:
    id (int)
    name (str)
    category (CompetitionMetricSubCategory)
    description (str)
    num_competitions (int)
      Number of public, launched competitions using this Metric
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    source_type (MetricListSourceType)
    owner_user_name (str)
    source_uri (str)
      If visible, a link to the metric source
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._category = None
    self._description = None
    self._num_competitions = 0
    self._source_type = MetricListSourceType.METRIC_LIST_SOURCE_TYPE_UNSPECIFIED
    self._owner_user_name = ""
    self._source_uri = None
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
  def category(self) -> 'CompetitionMetricSubCategory':
    return self._category or CompetitionMetricSubCategory.COMPETITION_METRIC_SUB_CATEGORY_UNSPECIFIED

  @category.setter
  def category(self, category: Optional['CompetitionMetricSubCategory']):
    if category is None:
      del self.category
      return
    if not isinstance(category, CompetitionMetricSubCategory):
      raise TypeError('category must be of type CompetitionMetricSubCategory')
    self._category = category

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
  def num_competitions(self) -> int:
    r"""
    Number of public, launched competitions using this Metric
    TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    """
    return self._num_competitions

  @num_competitions.setter
  def num_competitions(self, num_competitions: int):
    if num_competitions is None:
      del self.num_competitions
      return
    if not isinstance(num_competitions, int):
      raise TypeError('num_competitions must be of type int')
    self._num_competitions = num_competitions

  @property
  def source_type(self) -> 'MetricListSourceType':
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'MetricListSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, MetricListSourceType):
      raise TypeError('source_type must be of type MetricListSourceType')
    self._source_type = source_type

  @property
  def owner_user_name(self) -> str:
    return self._owner_user_name

  @owner_user_name.setter
  def owner_user_name(self, owner_user_name: str):
    if owner_user_name is None:
      del self.owner_user_name
      return
    if not isinstance(owner_user_name, str):
      raise TypeError('owner_user_name must be of type str')
    self._owner_user_name = owner_user_name

  @property
  def source_uri(self) -> str:
    """If visible, a link to the metric source"""
    return self._source_uri or ""

  @source_uri.setter
  def source_uri(self, source_uri: Optional[str]):
    if source_uri is None:
      del self.source_uri
      return
    if not isinstance(source_uri, str):
      raise TypeError('source_uri must be of type str')
    self._source_uri = source_uri


class UpdateCompetitionMetricMetadataRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    metadata (CompetitionMetricMetadata)
      Requested metadata settings. Will only update those that are set.
      TODO(aip.dev/134): (-- api-linter:
      core::0134::request-resource-field=disabled --)
  """

  def __init__(self):
    self._kernel_id = 0
    self._metadata = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def metadata(self) -> Optional['CompetitionMetricMetadata']:
    r"""
    Requested metadata settings. Will only update those that are set.
    TODO(aip.dev/134): (-- api-linter:
    core::0134::request-resource-field=disabled --)
    """
    return self._metadata

  @metadata.setter
  def metadata(self, metadata: Optional['CompetitionMetricMetadata']):
    if metadata is None:
      del self.metadata
      return
    if not isinstance(metadata, CompetitionMetricMetadata):
      raise TypeError('metadata must be of type CompetitionMetricMetadata')
    self._metadata = metadata


class UpdateCompetitionMetricRequest(KaggleObject):
  r"""
  Attributes:
    evaluation_algorithm_id (int)
    state (EvaluationAlgorithmState)
      For now, we just support changing the state value. This will typically be
      used to deprecate metrics.
  """

  def __init__(self):
    self._evaluation_algorithm_id = 0
    self._state = EvaluationAlgorithmState.EVALUATION_ALGORITHM_STATE_UNSPECIFIED
    self._freeze()

  @property
  def evaluation_algorithm_id(self) -> int:
    return self._evaluation_algorithm_id

  @evaluation_algorithm_id.setter
  def evaluation_algorithm_id(self, evaluation_algorithm_id: int):
    if evaluation_algorithm_id is None:
      del self.evaluation_algorithm_id
      return
    if not isinstance(evaluation_algorithm_id, int):
      raise TypeError('evaluation_algorithm_id must be of type int')
    self._evaluation_algorithm_id = evaluation_algorithm_id

  @property
  def state(self) -> 'EvaluationAlgorithmState':
    r"""
    For now, we just support changing the state value. This will typically be
    used to deprecate metrics.
    """
    return self._state

  @state.setter
  def state(self, state: 'EvaluationAlgorithmState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, EvaluationAlgorithmState):
      raise TypeError('state must be of type EvaluationAlgorithmState')
    self._state = state


CompetitionMetricMetadata._fields = [
  FieldMetadata("metricName", "metric_name", "_metric_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subCategory", "sub_category", "_sub_category", CompetitionMetricSubCategory, None, EnumSerializer(), optional=True),
  FieldMetadata("isMax", "is_max", "_is_max", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("passCompleteSubmission", "pass_complete_submission", "_pass_complete_submission", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionMetricTypeId", "competition_metric_type_id", "_competition_metric_type_id", CompetitionMetricTypeId, None, EnumSerializer(), optional=True),
  FieldMetadata("scoringTimeoutMinutes", "scoring_timeout_minutes", "_scoring_timeout_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("allowInternet", "allow_internet", "_allow_internet", bool, None, PredefinedSerializer(), optional=True),
]

CreateAdminMetricRequest._fields = []

CreateCompetitionMetricRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

CreateCompetitionMetricResponse._fields = [
  FieldMetadata("httpRedirect", "http_redirect", "_http_redirect", HttpRedirect, None, KaggleObjectSerializer()),
  FieldMetadata("evaluationAlgorithm", "evaluation_algorithm", "_evaluation_algorithm", EvaluationAlgorithm, None, KaggleObjectSerializer(), optional=True),
]

CreateEnvironmentMetricRequest._fields = [
  FieldMetadata("environmentName", "environment_name", "_environment_name", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("configuration", "configuration", "_configuration", str, "", PredefinedSerializer()),
  FieldMetadata("playerCountSpecification", "player_count_specification", "_player_count_specification", str, "", PredefinedSerializer()),
  FieldMetadata("renderType", "render_type", "_render_type", EnvironmentRenderType, EnvironmentRenderType.ENVIRONMENT_RENDER_TYPE_UNSPECIFIED, EnumSerializer()),
]

GetCompetitionMetricMetadataRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetCompetitionMetricVersionRequest._fields = [
  FieldMetadata("competitionMetricVersionId", "competition_metric_version_id", "_competition_metric_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceKernelSessionId", "source_kernel_session_id", "_source_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
]

ListCompetitionMetricsRequest._fields = [
  FieldMetadata("authorType", "author_type", "_author_type", MetricListAuthorType, None, EnumSerializer(), optional=True),
  FieldMetadata("sourceType", "source_type", "_source_type", MetricListSourceType, None, EnumSerializer(), optional=True),
  FieldMetadata("visibility", "visibility", "_visibility", MetricListVisibility, None, EnumSerializer(), optional=True),
]

ListCompetitionMetricsResponse._fields = [
  FieldMetadata("metrics", "metrics", "_metrics", MetricInfo, [], ListSerializer(KaggleObjectSerializer())),
]

MetricInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("category", "category", "_category", CompetitionMetricSubCategory, None, EnumSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numCompetitions", "num_competitions", "_num_competitions", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceType", "source_type", "_source_type", MetricListSourceType, MetricListSourceType.METRIC_LIST_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerUserName", "owner_user_name", "_owner_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("sourceUri", "source_uri", "_source_uri", str, None, PredefinedSerializer(), optional=True),
]

UpdateCompetitionMetricMetadataRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("metadata", "metadata", "_metadata", CompetitionMetricMetadata, None, KaggleObjectSerializer()),
]

UpdateCompetitionMetricRequest._fields = [
  FieldMetadata("evaluationAlgorithmId", "evaluation_algorithm_id", "_evaluation_algorithm_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", EvaluationAlgorithmState, EvaluationAlgorithmState.EVALUATION_ALGORITHM_STATE_UNSPECIFIED, EnumSerializer()),
]

