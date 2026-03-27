from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.competitions.types.competition import Reward
from kagglesdk.competitions.types.competition_enums import HostSegment
from kagglesdk.competitions.types.competition_types import PrivacySettings
from kagglesdk.competitions.types.evaluation_algorithm import CompetitionMetricVersion, EvaluationAlgorithm
from kagglesdk.kaggle_object import *
from typing import Optional, List, Dict

class CompetitionPageError(enum.Enum):
  COMPETITION_PAGE_ERROR_UNSPECIFIED = 0
  RESERVED_NAME = 1
  """Page name has special meaning (e.g. 'rules' or 'data') and is reserved."""
  DUPLICATE_NAME = 2
  """Page name is already in use."""
  CONCURRENT_EDIT = 3

class ColumnDefinition(KaggleObject):
  r"""
  Describes a single column in a dataframe.

  Attributes:
    name (str)
    parsing_data_type (str)
  """

  def __init__(self):
    self._name = ""
    self._parsing_data_type = ""
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
  def parsing_data_type(self) -> str:
    return self._parsing_data_type

  @parsing_data_type.setter
  def parsing_data_type(self, parsing_data_type: str):
    if parsing_data_type is None:
      del self.parsing_data_type
      return
    if not isinstance(parsing_data_type, str):
      raise TypeError('parsing_data_type must be of type str')
    self._parsing_data_type = parsing_data_type


class ColumnMapping(KaggleObject):
  r"""
  Attributes:
    column_mappings (ColumnMappingValue)
      Maps column keys to current selected column definition name.
    column_definitions (ColumnDefinition)
  """

  def __init__(self):
    self._column_mappings = {}
    self._column_definitions = []
    self._freeze()

  @property
  def column_mappings(self) -> Optional[Dict[str, Optional['ColumnMappingValue']]]:
    """Maps column keys to current selected column definition name."""
    return self._column_mappings

  @column_mappings.setter
  def column_mappings(self, column_mappings: Optional[Dict[str, Optional['ColumnMappingValue']]]):
    if column_mappings is None:
      del self.column_mappings
      return
    if not isinstance(column_mappings, dict):
      raise TypeError('column_mappings must be of type dict')
    if not all([isinstance(v, ColumnMappingValue) for k, v in column_mappings]):
      raise TypeError('column_mappings must contain only items of type ColumnMappingValue')
    self._column_mappings = column_mappings

  @property
  def column_definitions(self) -> Optional[List[Optional['ColumnDefinition']]]:
    return self._column_definitions

  @column_definitions.setter
  def column_definitions(self, column_definitions: Optional[List[Optional['ColumnDefinition']]]):
    if column_definitions is None:
      del self.column_definitions
      return
    if not isinstance(column_definitions, list):
      raise TypeError('column_definitions must be of type list')
    if not all([isinstance(t, ColumnDefinition) for t in column_definitions]):
      raise TypeError('column_definitions must contain only items of type ColumnDefinition')
    self._column_definitions = column_definitions


class ColumnMappingValue(KaggleObject):
  r"""
  Attributes:
    name (str)
  """

  def __init__(self):
    self._name = None
    self._freeze()

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


class CompetitionSettings(KaggleObject):
  r"""
  Attributes:
    title (str)
    slug (str)
    brief_description (str)
    host_segment (HostSegment)
    organization_id (int)
    deadline (datetime)
    max_team_size (int)
    max_daily_submissions (int)
    num_scored_private_submissions (int)
    counts_towards_ranking (bool)
    counts_towards_tiers (bool)
    disable_kernels (bool)
    private_leaderboard_release_date (datetime)
    citation_author_override (str)
    date_enabled (datetime)
    enable_user_email_share (bool)
    score_truncation_num_decimals (int)
    privacy_settings (PrivacySettings)
    license_id (int)
    required_submission_filename (str)
    reward (Reward)
    num_prizes (int)
  """

  def __init__(self):
    self._title = None
    self._slug = None
    self._brief_description = None
    self._host_segment = None
    self._organization_id = None
    self._deadline = None
    self._max_team_size = None
    self._max_daily_submissions = None
    self._num_scored_private_submissions = None
    self._counts_towards_ranking = None
    self._counts_towards_tiers = None
    self._disable_kernels = None
    self._private_leaderboard_release_date = None
    self._citation_author_override = None
    self._date_enabled = None
    self._enable_user_email_share = None
    self._score_truncation_num_decimals = None
    self._privacy_settings = None
    self._license_id = None
    self._required_submission_filename = None
    self._reward = None
    self._num_prizes = None
    self._freeze()

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
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def brief_description(self) -> str:
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
  def host_segment(self) -> 'HostSegment':
    return self._host_segment or HostSegment.HOST_SEGMENT_UNSPECIFIED

  @host_segment.setter
  def host_segment(self, host_segment: Optional['HostSegment']):
    if host_segment is None:
      del self.host_segment
      return
    if not isinstance(host_segment, HostSegment):
      raise TypeError('host_segment must be of type HostSegment')
    self._host_segment = host_segment

  @property
  def organization_id(self) -> int:
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: Optional[int]):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def deadline(self) -> datetime:
    return self._deadline

  @deadline.setter
  def deadline(self, deadline: datetime):
    if deadline is None:
      del self.deadline
      return
    if not isinstance(deadline, datetime):
      raise TypeError('deadline must be of type datetime')
    self._deadline = deadline

  @property
  def max_team_size(self) -> int:
    return self._max_team_size or 0

  @max_team_size.setter
  def max_team_size(self, max_team_size: Optional[int]):
    if max_team_size is None:
      del self.max_team_size
      return
    if not isinstance(max_team_size, int):
      raise TypeError('max_team_size must be of type int')
    self._max_team_size = max_team_size

  @property
  def max_daily_submissions(self) -> int:
    return self._max_daily_submissions or 0

  @max_daily_submissions.setter
  def max_daily_submissions(self, max_daily_submissions: Optional[int]):
    if max_daily_submissions is None:
      del self.max_daily_submissions
      return
    if not isinstance(max_daily_submissions, int):
      raise TypeError('max_daily_submissions must be of type int')
    self._max_daily_submissions = max_daily_submissions

  @property
  def num_scored_private_submissions(self) -> int:
    return self._num_scored_private_submissions or 0

  @num_scored_private_submissions.setter
  def num_scored_private_submissions(self, num_scored_private_submissions: Optional[int]):
    if num_scored_private_submissions is None:
      del self.num_scored_private_submissions
      return
    if not isinstance(num_scored_private_submissions, int):
      raise TypeError('num_scored_private_submissions must be of type int')
    self._num_scored_private_submissions = num_scored_private_submissions

  @property
  def counts_towards_ranking(self) -> bool:
    return self._counts_towards_ranking or False

  @counts_towards_ranking.setter
  def counts_towards_ranking(self, counts_towards_ranking: Optional[bool]):
    if counts_towards_ranking is None:
      del self.counts_towards_ranking
      return
    if not isinstance(counts_towards_ranking, bool):
      raise TypeError('counts_towards_ranking must be of type bool')
    self._counts_towards_ranking = counts_towards_ranking

  @property
  def counts_towards_tiers(self) -> bool:
    return self._counts_towards_tiers or False

  @counts_towards_tiers.setter
  def counts_towards_tiers(self, counts_towards_tiers: Optional[bool]):
    if counts_towards_tiers is None:
      del self.counts_towards_tiers
      return
    if not isinstance(counts_towards_tiers, bool):
      raise TypeError('counts_towards_tiers must be of type bool')
    self._counts_towards_tiers = counts_towards_tiers

  @property
  def disable_kernels(self) -> bool:
    return self._disable_kernels or False

  @disable_kernels.setter
  def disable_kernels(self, disable_kernels: Optional[bool]):
    if disable_kernels is None:
      del self.disable_kernels
      return
    if not isinstance(disable_kernels, bool):
      raise TypeError('disable_kernels must be of type bool')
    self._disable_kernels = disable_kernels

  @property
  def private_leaderboard_release_date(self) -> datetime:
    return self._private_leaderboard_release_date

  @private_leaderboard_release_date.setter
  def private_leaderboard_release_date(self, private_leaderboard_release_date: datetime):
    if private_leaderboard_release_date is None:
      del self.private_leaderboard_release_date
      return
    if not isinstance(private_leaderboard_release_date, datetime):
      raise TypeError('private_leaderboard_release_date must be of type datetime')
    self._private_leaderboard_release_date = private_leaderboard_release_date

  @property
  def citation_author_override(self) -> str:
    return self._citation_author_override or ""

  @citation_author_override.setter
  def citation_author_override(self, citation_author_override: Optional[str]):
    if citation_author_override is None:
      del self.citation_author_override
      return
    if not isinstance(citation_author_override, str):
      raise TypeError('citation_author_override must be of type str')
    self._citation_author_override = citation_author_override

  @property
  def date_enabled(self) -> datetime:
    return self._date_enabled

  @date_enabled.setter
  def date_enabled(self, date_enabled: datetime):
    if date_enabled is None:
      del self.date_enabled
      return
    if not isinstance(date_enabled, datetime):
      raise TypeError('date_enabled must be of type datetime')
    self._date_enabled = date_enabled

  @property
  def enable_user_email_share(self) -> bool:
    return self._enable_user_email_share or False

  @enable_user_email_share.setter
  def enable_user_email_share(self, enable_user_email_share: Optional[bool]):
    if enable_user_email_share is None:
      del self.enable_user_email_share
      return
    if not isinstance(enable_user_email_share, bool):
      raise TypeError('enable_user_email_share must be of type bool')
    self._enable_user_email_share = enable_user_email_share

  @property
  def score_truncation_num_decimals(self) -> int:
    return self._score_truncation_num_decimals or 0

  @score_truncation_num_decimals.setter
  def score_truncation_num_decimals(self, score_truncation_num_decimals: Optional[int]):
    if score_truncation_num_decimals is None:
      del self.score_truncation_num_decimals
      return
    if not isinstance(score_truncation_num_decimals, int):
      raise TypeError('score_truncation_num_decimals must be of type int')
    self._score_truncation_num_decimals = score_truncation_num_decimals

  @property
  def privacy_settings(self) -> Optional['PrivacySettings']:
    return self._privacy_settings

  @privacy_settings.setter
  def privacy_settings(self, privacy_settings: Optional['PrivacySettings']):
    if privacy_settings is None:
      del self.privacy_settings
      return
    if not isinstance(privacy_settings, PrivacySettings):
      raise TypeError('privacy_settings must be of type PrivacySettings')
    self._privacy_settings = privacy_settings

  @property
  def license_id(self) -> int:
    return self._license_id or 0

  @license_id.setter
  def license_id(self, license_id: Optional[int]):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def required_submission_filename(self) -> str:
    return self._required_submission_filename or ""

  @required_submission_filename.setter
  def required_submission_filename(self, required_submission_filename: Optional[str]):
    if required_submission_filename is None:
      del self.required_submission_filename
      return
    if not isinstance(required_submission_filename, str):
      raise TypeError('required_submission_filename must be of type str')
    self._required_submission_filename = required_submission_filename

  @property
  def reward(self) -> Optional['Reward']:
    return self._reward or None

  @reward.setter
  def reward(self, reward: Optional[Optional['Reward']]):
    if reward is None:
      del self.reward
      return
    if not isinstance(reward, Reward):
      raise TypeError('reward must be of type Reward')
    self._reward = reward

  @property
  def num_prizes(self) -> int:
    return self._num_prizes or 0

  @num_prizes.setter
  def num_prizes(self, num_prizes: Optional[int]):
    if num_prizes is None:
      del self.num_prizes
      return
    if not isinstance(num_prizes, int):
      raise TypeError('num_prizes must be of type int')
    self._num_prizes = num_prizes


class EvaluationInfo(KaggleObject):
  r"""
  Attributes:
    metric (EvaluationAlgorithm)
    metric_version (CompetitionMetricVersion)
    parameters (EvaluationMetricParameter)
    solution_column_mapping (ColumnMapping)
    submission_column_mapping (ColumnMapping)
    solution_info (SolutionInfo)
    can_view_metric (bool)
    evaluation_setup_error (str)
    row_id_column_name (str)
    competition_has_solution (bool)
      HasSolution means that all required steps in the solution setup flow are
      complete. As opposed to solution_info.hasDerived, which only means that the
      derived blob exists.
  """

  def __init__(self):
    self._metric = None
    self._metric_version = None
    self._parameters = []
    self._solution_column_mapping = None
    self._submission_column_mapping = None
    self._solution_info = None
    self._can_view_metric = False
    self._evaluation_setup_error = None
    self._row_id_column_name = None
    self._competition_has_solution = False
    self._freeze()

  @property
  def metric(self) -> Optional['EvaluationAlgorithm']:
    return self._metric

  @metric.setter
  def metric(self, metric: Optional['EvaluationAlgorithm']):
    if metric is None:
      del self.metric
      return
    if not isinstance(metric, EvaluationAlgorithm):
      raise TypeError('metric must be of type EvaluationAlgorithm')
    self._metric = metric

  @property
  def metric_version(self) -> Optional['CompetitionMetricVersion']:
    return self._metric_version

  @metric_version.setter
  def metric_version(self, metric_version: Optional['CompetitionMetricVersion']):
    if metric_version is None:
      del self.metric_version
      return
    if not isinstance(metric_version, CompetitionMetricVersion):
      raise TypeError('metric_version must be of type CompetitionMetricVersion')
    self._metric_version = metric_version

  @property
  def parameters(self) -> Optional[List[Optional['EvaluationMetricParameter']]]:
    return self._parameters

  @parameters.setter
  def parameters(self, parameters: Optional[List[Optional['EvaluationMetricParameter']]]):
    if parameters is None:
      del self.parameters
      return
    if not isinstance(parameters, list):
      raise TypeError('parameters must be of type list')
    if not all([isinstance(t, EvaluationMetricParameter) for t in parameters]):
      raise TypeError('parameters must contain only items of type EvaluationMetricParameter')
    self._parameters = parameters

  @property
  def solution_column_mapping(self) -> Optional['ColumnMapping']:
    return self._solution_column_mapping

  @solution_column_mapping.setter
  def solution_column_mapping(self, solution_column_mapping: Optional['ColumnMapping']):
    if solution_column_mapping is None:
      del self.solution_column_mapping
      return
    if not isinstance(solution_column_mapping, ColumnMapping):
      raise TypeError('solution_column_mapping must be of type ColumnMapping')
    self._solution_column_mapping = solution_column_mapping

  @property
  def submission_column_mapping(self) -> Optional['ColumnMapping']:
    return self._submission_column_mapping

  @submission_column_mapping.setter
  def submission_column_mapping(self, submission_column_mapping: Optional['ColumnMapping']):
    if submission_column_mapping is None:
      del self.submission_column_mapping
      return
    if not isinstance(submission_column_mapping, ColumnMapping):
      raise TypeError('submission_column_mapping must be of type ColumnMapping')
    self._submission_column_mapping = submission_column_mapping

  @property
  def solution_info(self) -> Optional['SolutionInfo']:
    return self._solution_info

  @solution_info.setter
  def solution_info(self, solution_info: Optional['SolutionInfo']):
    if solution_info is None:
      del self.solution_info
      return
    if not isinstance(solution_info, SolutionInfo):
      raise TypeError('solution_info must be of type SolutionInfo')
    self._solution_info = solution_info

  @property
  def can_view_metric(self) -> bool:
    return self._can_view_metric

  @can_view_metric.setter
  def can_view_metric(self, can_view_metric: bool):
    if can_view_metric is None:
      del self.can_view_metric
      return
    if not isinstance(can_view_metric, bool):
      raise TypeError('can_view_metric must be of type bool')
    self._can_view_metric = can_view_metric

  @property
  def evaluation_setup_error(self) -> str:
    return self._evaluation_setup_error or ""

  @evaluation_setup_error.setter
  def evaluation_setup_error(self, evaluation_setup_error: Optional[str]):
    if evaluation_setup_error is None:
      del self.evaluation_setup_error
      return
    if not isinstance(evaluation_setup_error, str):
      raise TypeError('evaluation_setup_error must be of type str')
    self._evaluation_setup_error = evaluation_setup_error

  @property
  def row_id_column_name(self) -> str:
    return self._row_id_column_name or ""

  @row_id_column_name.setter
  def row_id_column_name(self, row_id_column_name: Optional[str]):
    if row_id_column_name is None:
      del self.row_id_column_name
      return
    if not isinstance(row_id_column_name, str):
      raise TypeError('row_id_column_name must be of type str')
    self._row_id_column_name = row_id_column_name

  @property
  def competition_has_solution(self) -> bool:
    r"""
    HasSolution means that all required steps in the solution setup flow are
    complete. As opposed to solution_info.hasDerived, which only means that the
    derived blob exists.
    """
    return self._competition_has_solution

  @competition_has_solution.setter
  def competition_has_solution(self, competition_has_solution: bool):
    if competition_has_solution is None:
      del self.competition_has_solution
      return
    if not isinstance(competition_has_solution, bool):
      raise TypeError('competition_has_solution must be of type bool')
    self._competition_has_solution = competition_has_solution


class EvaluationMetricParameter(KaggleObject):
  r"""
  (Hyper)parameter used to configure an evaluation metric.

  Attributes:
    name (str)
    type (str)
    value (str)
  """

  def __init__(self):
    self._name = ""
    self._type = ""
    self._value = ""
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
  def type(self) -> str:
    return self._type

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class GetHostChecklistRequest(KaggleObject):
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


class GetHostEvaluationInfoRequest(KaggleObject):
  r"""
  All things metrics related:

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


class HostChecklist(KaggleObject):
  r"""
  Attributes:
    is_competition_pending (bool)
    children (HostChecklistItem)
  """

  def __init__(self):
    self._is_competition_pending = False
    self._children = []
    self._freeze()

  @property
  def is_competition_pending(self) -> bool:
    return self._is_competition_pending

  @is_competition_pending.setter
  def is_competition_pending(self, is_competition_pending: bool):
    if is_competition_pending is None:
      del self.is_competition_pending
      return
    if not isinstance(is_competition_pending, bool):
      raise TypeError('is_competition_pending must be of type bool')
    self._is_competition_pending = is_competition_pending

  @property
  def children(self) -> Optional[List[Optional['HostChecklistItem']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['HostChecklistItem']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, HostChecklistItem) for t in children]):
      raise TypeError('children must contain only items of type HostChecklistItem')
    self._children = children


class HostChecklistItem(KaggleObject):
  r"""
  Attributes:
    type (HostChecklistItem.ChecklistItemType)
    ok (bool)
    title (str)
    message (str)
    url (str)
    optional (bool)
  """

  class ChecklistItemType(enum.Enum):
    CHECKLIST_ITEM_TYPE_UNSPECIFIED = 0
    CREATED = 1
    HAS_VALID_DEADLINE = 2
    HAS_RULES_PAGE_CONTENT = 3
    HAS_DATA_PAGE_CONTENT = 4
    HAS_OVERVIEW_CONTENT = 5
    HAS_VALID_METRIC = 6
    HAS_SOLUTION = 7
    HAS_SOLUTION_AND_SUBMISSION_SCHEMAS = 8
    HAS_SANDBOX_SUBMISSION = 9
    HAS_DATASET = 10
    HAS_TAGS = 11
    HAS_IMAGES = 12
    HAS_INVITE = 13
    HAS_LICENSE = 14
    HAS_PRIZES_PAGE_CONTENT = 15
    HAS_JUDGES = 16
    HAS_TRACKS = 17
    HAS_WRITEUPS_CONFIGURED = 18
    HAS_SAMPLE_PROJECT = 19

  def __init__(self):
    self._type = self.ChecklistItemType.CHECKLIST_ITEM_TYPE_UNSPECIFIED
    self._ok = False
    self._title = ""
    self._message = ""
    self._url = ""
    self._optional = False
    self._freeze()

  @property
  def type(self) -> 'HostChecklistItem.ChecklistItemType':
    return self._type

  @type.setter
  def type(self, type: 'HostChecklistItem.ChecklistItemType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HostChecklistItem.ChecklistItemType):
      raise TypeError('type must be of type HostChecklistItem.ChecklistItemType')
    self._type = type

  @property
  def ok(self) -> bool:
    return self._ok

  @ok.setter
  def ok(self, ok: bool):
    if ok is None:
      del self.ok
      return
    if not isinstance(ok, bool):
      raise TypeError('ok must be of type bool')
    self._ok = ok

  @property
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

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

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def optional(self) -> bool:
    return self._optional

  @optional.setter
  def optional(self, optional: bool):
    if optional is None:
      del self.optional
      return
    if not isinstance(optional, bool):
      raise TypeError('optional must be of type bool')
    self._optional = optional


class HostEvaluationInfo(KaggleObject):
  r"""
  Attributes:
    evaluation_info (EvaluationInfo)
  """

  def __init__(self):
    self._evaluation_info = None
    self._freeze()

  @property
  def evaluation_info(self) -> Optional['EvaluationInfo']:
    return self._evaluation_info

  @evaluation_info.setter
  def evaluation_info(self, evaluation_info: Optional['EvaluationInfo']):
    if evaluation_info is None:
      del self.evaluation_info
      return
    if not isinstance(evaluation_info, EvaluationInfo):
      raise TypeError('evaluation_info must be of type EvaluationInfo')
    self._evaluation_info = evaluation_info


class InvalidateSubmissionsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    submission_ids (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._submission_ids = []
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
  def submission_ids(self) -> Optional[List[int]]:
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


class LegacyColumnMapping(KaggleObject):
  r"""
  Differs from ColumnMapping for historical reasons, but should eventually
  merge that one and this one.

  Attributes:
    mapped_column_names (str)
    sampling_percentage (int)
  """

  def __init__(self):
    self._mapped_column_names = {}
    self._sampling_percentage = None
    self._freeze()

  @property
  def mapped_column_names(self) -> Optional[Dict[str, str]]:
    return self._mapped_column_names

  @mapped_column_names.setter
  def mapped_column_names(self, mapped_column_names: Optional[Dict[str, str]]):
    if mapped_column_names is None:
      del self.mapped_column_names
      return
    if not isinstance(mapped_column_names, dict):
      raise TypeError('mapped_column_names must be of type dict')
    if not all([isinstance(v, str) for k, v in mapped_column_names]):
      raise TypeError('mapped_column_names must contain only items of type str')
    self._mapped_column_names = mapped_column_names

  @property
  def sampling_percentage(self) -> int:
    return self._sampling_percentage or 0

  @sampling_percentage.setter
  def sampling_percentage(self, sampling_percentage: Optional[int]):
    if sampling_percentage is None:
      del self.sampling_percentage
      return
    if not isinstance(sampling_percentage, int):
      raise TypeError('sampling_percentage must be of type int')
    self._sampling_percentage = sampling_percentage


class SolutionInfo(KaggleObject):
  r"""
  Attributes:
    has_raw (bool)
    has_derived (bool)
    raw_file_name (str)
    raw_download_url (str)
    raw_file_size_bytes (int)
    upload_date (datetime)
    total_solution_private_rows (int)
    total_solution_public_rows (int)
    total_solution_rows (int)
  """

  def __init__(self):
    self._has_raw = False
    self._has_derived = False
    self._raw_file_name = None
    self._raw_download_url = None
    self._raw_file_size_bytes = None
    self._upload_date = None
    self._total_solution_private_rows = None
    self._total_solution_public_rows = None
    self._total_solution_rows = None
    self._freeze()

  @property
  def has_raw(self) -> bool:
    return self._has_raw

  @has_raw.setter
  def has_raw(self, has_raw: bool):
    if has_raw is None:
      del self.has_raw
      return
    if not isinstance(has_raw, bool):
      raise TypeError('has_raw must be of type bool')
    self._has_raw = has_raw

  @property
  def has_derived(self) -> bool:
    return self._has_derived

  @has_derived.setter
  def has_derived(self, has_derived: bool):
    if has_derived is None:
      del self.has_derived
      return
    if not isinstance(has_derived, bool):
      raise TypeError('has_derived must be of type bool')
    self._has_derived = has_derived

  @property
  def raw_file_name(self) -> str:
    return self._raw_file_name or ""

  @raw_file_name.setter
  def raw_file_name(self, raw_file_name: Optional[str]):
    if raw_file_name is None:
      del self.raw_file_name
      return
    if not isinstance(raw_file_name, str):
      raise TypeError('raw_file_name must be of type str')
    self._raw_file_name = raw_file_name

  @property
  def raw_download_url(self) -> str:
    return self._raw_download_url or ""

  @raw_download_url.setter
  def raw_download_url(self, raw_download_url: Optional[str]):
    if raw_download_url is None:
      del self.raw_download_url
      return
    if not isinstance(raw_download_url, str):
      raise TypeError('raw_download_url must be of type str')
    self._raw_download_url = raw_download_url

  @property
  def raw_file_size_bytes(self) -> int:
    return self._raw_file_size_bytes or 0

  @raw_file_size_bytes.setter
  def raw_file_size_bytes(self, raw_file_size_bytes: Optional[int]):
    if raw_file_size_bytes is None:
      del self.raw_file_size_bytes
      return
    if not isinstance(raw_file_size_bytes, int):
      raise TypeError('raw_file_size_bytes must be of type int')
    self._raw_file_size_bytes = raw_file_size_bytes

  @property
  def upload_date(self) -> datetime:
    return self._upload_date

  @upload_date.setter
  def upload_date(self, upload_date: datetime):
    if upload_date is None:
      del self.upload_date
      return
    if not isinstance(upload_date, datetime):
      raise TypeError('upload_date must be of type datetime')
    self._upload_date = upload_date

  @property
  def total_solution_private_rows(self) -> int:
    return self._total_solution_private_rows or 0

  @total_solution_private_rows.setter
  def total_solution_private_rows(self, total_solution_private_rows: Optional[int]):
    if total_solution_private_rows is None:
      del self.total_solution_private_rows
      return
    if not isinstance(total_solution_private_rows, int):
      raise TypeError('total_solution_private_rows must be of type int')
    self._total_solution_private_rows = total_solution_private_rows

  @property
  def total_solution_public_rows(self) -> int:
    return self._total_solution_public_rows or 0

  @total_solution_public_rows.setter
  def total_solution_public_rows(self, total_solution_public_rows: Optional[int]):
    if total_solution_public_rows is None:
      del self.total_solution_public_rows
      return
    if not isinstance(total_solution_public_rows, int):
      raise TypeError('total_solution_public_rows must be of type int')
    self._total_solution_public_rows = total_solution_public_rows

  @property
  def total_solution_rows(self) -> int:
    return self._total_solution_rows or 0

  @total_solution_rows.setter
  def total_solution_rows(self, total_solution_rows: Optional[int]):
    if total_solution_rows is None:
      del self.total_solution_rows
      return
    if not isinstance(total_solution_rows, int):
      raise TypeError('total_solution_rows must be of type int')
    self._total_solution_rows = total_solution_rows


class UpdateCompetitionSettingsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    settings (CompetitionSettings)
    update_mask (FieldMask)
      Specifies which fields the caller wants to update. Required.
  """

  def __init__(self):
    self._competition_id = 0
    self._settings = None
    self._update_mask = None
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
  def settings(self) -> Optional['CompetitionSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['CompetitionSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, CompetitionSettings):
      raise TypeError('settings must be of type CompetitionSettings')
    self._settings = settings

  @property
  def update_mask(self) -> FieldMask:
    """Specifies which fields the caller wants to update. Required."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateSolutionColumnMappingRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    column_mapping (LegacyColumnMapping)
  """

  def __init__(self):
    self._competition_id = 0
    self._column_mapping = None
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
  def column_mapping(self) -> Optional['LegacyColumnMapping']:
    return self._column_mapping

  @column_mapping.setter
  def column_mapping(self, column_mapping: Optional['LegacyColumnMapping']):
    if column_mapping is None:
      del self.column_mapping
      return
    if not isinstance(column_mapping, LegacyColumnMapping):
      raise TypeError('column_mapping must be of type LegacyColumnMapping')
    self._column_mapping = column_mapping


class UpdateSubmissionColumnMappingRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    column_mapping (LegacyColumnMapping)
  """

  def __init__(self):
    self._competition_id = 0
    self._column_mapping = None
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
  def column_mapping(self) -> Optional['LegacyColumnMapping']:
    return self._column_mapping

  @column_mapping.setter
  def column_mapping(self, column_mapping: Optional['LegacyColumnMapping']):
    if column_mapping is None:
      del self.column_mapping
      return
    if not isinstance(column_mapping, LegacyColumnMapping):
      raise TypeError('column_mapping must be of type LegacyColumnMapping')
    self._column_mapping = column_mapping


ColumnDefinition._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("parsingDataType", "parsing_data_type", "_parsing_data_type", str, "", PredefinedSerializer()),
]

ColumnMapping._fields = [
  FieldMetadata("columnMappings", "column_mappings", "_column_mappings", ColumnMappingValue, {}, MapSerializer(KaggleObjectSerializer())),
  FieldMetadata("columnDefinitions", "column_definitions", "_column_definitions", ColumnDefinition, [], ListSerializer(KaggleObjectSerializer())),
]

ColumnMappingValue._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
]

CompetitionSettings._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, None, EnumSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("maxTeamSize", "max_team_size", "_max_team_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxDailySubmissions", "max_daily_submissions", "_max_daily_submissions", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numScoredPrivateSubmissions", "num_scored_private_submissions", "_num_scored_private_submissions", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countsTowardsRanking", "counts_towards_ranking", "_counts_towards_ranking", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countsTowardsTiers", "counts_towards_tiers", "_counts_towards_tiers", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableKernels", "disable_kernels", "_disable_kernels", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateLeaderboardReleaseDate", "private_leaderboard_release_date", "_private_leaderboard_release_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("citationAuthorOverride", "citation_author_override", "_citation_author_override", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateEnabled", "date_enabled", "_date_enabled", datetime, None, DateTimeSerializer()),
  FieldMetadata("enableUserEmailShare", "enable_user_email_share", "_enable_user_email_share", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scoreTruncationNumDecimals", "score_truncation_num_decimals", "_score_truncation_num_decimals", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privacySettings", "privacy_settings", "_privacy_settings", PrivacySettings, None, KaggleObjectSerializer()),
  FieldMetadata("licenseId", "license_id", "_license_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("requiredSubmissionFilename", "required_submission_filename", "_required_submission_filename", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reward", "reward", "_reward", Reward, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numPrizes", "num_prizes", "_num_prizes", int, None, PredefinedSerializer(), optional=True),
]

EvaluationInfo._fields = [
  FieldMetadata("metric", "metric", "_metric", EvaluationAlgorithm, None, KaggleObjectSerializer()),
  FieldMetadata("metricVersion", "metric_version", "_metric_version", CompetitionMetricVersion, None, KaggleObjectSerializer()),
  FieldMetadata("parameters", "parameters", "_parameters", EvaluationMetricParameter, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("solutionColumnMapping", "solution_column_mapping", "_solution_column_mapping", ColumnMapping, None, KaggleObjectSerializer()),
  FieldMetadata("submissionColumnMapping", "submission_column_mapping", "_submission_column_mapping", ColumnMapping, None, KaggleObjectSerializer()),
  FieldMetadata("solutionInfo", "solution_info", "_solution_info", SolutionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("canViewMetric", "can_view_metric", "_can_view_metric", bool, False, PredefinedSerializer()),
  FieldMetadata("evaluationSetupError", "evaluation_setup_error", "_evaluation_setup_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rowIdColumnName", "row_id_column_name", "_row_id_column_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionHasSolution", "competition_has_solution", "_competition_has_solution", bool, False, PredefinedSerializer()),
]

EvaluationMetricParameter._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

GetHostChecklistRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetHostEvaluationInfoRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

HostChecklist._fields = [
  FieldMetadata("isCompetitionPending", "is_competition_pending", "_is_competition_pending", bool, False, PredefinedSerializer()),
  FieldMetadata("children", "children", "_children", HostChecklistItem, [], ListSerializer(KaggleObjectSerializer())),
]

HostChecklistItem._fields = [
  FieldMetadata("type", "type", "_type", HostChecklistItem.ChecklistItemType, HostChecklistItem.ChecklistItemType.CHECKLIST_ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ok", "ok", "_ok", bool, False, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("optional", "optional", "_optional", bool, False, PredefinedSerializer()),
]

HostEvaluationInfo._fields = [
  FieldMetadata("evaluationInfo", "evaluation_info", "_evaluation_info", EvaluationInfo, None, KaggleObjectSerializer()),
]

InvalidateSubmissionsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("submissionIds", "submission_ids", "_submission_ids", int, [], ListSerializer(PredefinedSerializer())),
]

LegacyColumnMapping._fields = [
  FieldMetadata("mappedColumnNames", "mapped_column_names", "_mapped_column_names", str, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("samplingPercentage", "sampling_percentage", "_sampling_percentage", int, None, PredefinedSerializer(), optional=True),
]

SolutionInfo._fields = [
  FieldMetadata("hasRaw", "has_raw", "_has_raw", bool, False, PredefinedSerializer()),
  FieldMetadata("hasDerived", "has_derived", "_has_derived", bool, False, PredefinedSerializer()),
  FieldMetadata("rawFileName", "raw_file_name", "_raw_file_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rawDownloadUrl", "raw_download_url", "_raw_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rawFileSizeBytes", "raw_file_size_bytes", "_raw_file_size_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("uploadDate", "upload_date", "_upload_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("totalSolutionPrivateRows", "total_solution_private_rows", "_total_solution_private_rows", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalSolutionPublicRows", "total_solution_public_rows", "_total_solution_public_rows", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalSolutionRows", "total_solution_rows", "_total_solution_rows", int, None, PredefinedSerializer(), optional=True),
]

UpdateCompetitionSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", CompetitionSettings, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateSolutionColumnMappingRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("columnMapping", "column_mapping", "_column_mapping", LegacyColumnMapping, None, KaggleObjectSerializer()),
]

UpdateSubmissionColumnMappingRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("columnMapping", "column_mapping", "_column_mapping", LegacyColumnMapping, None, KaggleObjectSerializer()),
]

