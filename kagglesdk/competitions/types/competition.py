from datetime import datetime
import enum
from kagglesdk.competitions.foreign.types.category import Category
from kagglesdk.competitions.foreign.types.organization import Organization
from kagglesdk.competitions.types.evaluation_algorithm import CompetitionMetricVersion, EvaluationAlgorithm
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from typing import Optional, List

class ParticipationLevel(enum.Enum):
  PARTICIPATION_LEVEL_UNSPECIFIED = 0
  PARTICIPATION_LEVEL_ANYONE = 1
  PARTICIPATION_LEVEL_LINK = 2
  PARTICIPATION_LEVEL_EMAIL_LIST = 3

class PubliclyCloneable(enum.Enum):
  PUBLICLY_CLONEABLE_UNSPECIFIED = 0
  """not cloneable"""
  PUBLICLY_CLONEABLE_WITH_PRIVATE_SOLUTION_FILE = 1
  r"""
  publicly cloneable - cloning this competition will NOT give you access to
  solution file
  """
  PUBLICLY_CLONEABLE_WITH_PUBLIC_SOLUTION_FILE = 2
  r"""
  publicly cloneable - cloning this competition will give you access to the
  solution file
  """

class RewardTypeId(enum.Enum):
  REWARD_TYPE_ID_UNSPECIFIED = 0
  USD = 1
  KUDOS = 2
  AUD = 3
  EUR = 4
  JOBS = 5
  SWAG = 6
  GBP = 7
  KNOWLEDGE = 8
  PRIZES = 9

class Competition(KaggleObject):
  r"""
  Attributes:
    id (int)
      The competition ID.
    competition_name (str)
      The name of the competition as it appears in the URL.
    title (str)
      The name of the competition as it appears in the title.
    brief_description (str)
      A short description of the competition.
    date_enabled (datetime)
      The competition's start date in UTC
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    deadline (datetime)
      The competition's deadline in UTC
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    has_leaderboard (bool)
    leaderboard_percentage (int)
    max_daily_submissions (int)
      The maximum number of submissions a team can make each day.
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    num_scored_submissions (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    has_solution (bool)
    num_prizes (int)
      TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    forum_id (int)
    final_leaderboard_has_been_verified (bool)
    disable_submissions (bool)
    is_private (bool)
    user_rank_multiplier (float)
    limited_participation_group_id (int)
    withold_final_leaderboard_until_it_has_been_verified (bool)
    public_leaderboard_disclaimer_message (str)
    final_leaderboard_disclaimer_message (str)
    date_created (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    disable_leaderboard_prize_indicator (bool)
    competition_host_segment_id (int)
    max_team_size (int)
    prohibit_new_entrants (bool)
    medals_allowed (bool)
    enable_team_files (bool)
    team_file_deadline (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    prohibit_solution_download (bool)
    total_solution_rows (int)
    team_merger_explicit_deadline (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    prohibit_new_entrants_explicit_deadline (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    kernels_publishing_disabled_deadline (datetime)
      Deadline until which users cannot make competition notebooks public.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    organization_id (int)
    has_cover_image_url (bool)
    show_private_leaderboard (bool)
    is_team_count_overridden (bool)
    has_scripts (bool)
    share_token (str)
    only_allow_kernel_submissions (bool)
    total_teams (int)
    total_competitors (int)
    total_submissions (int)
    rules_required (bool)
    uses_synchronous_reruns (bool)
    post_processor_kernel_id (int)
    max_cpu_runtime_minutes (int)
    max_gpu_runtime_minutes (int)
    private_leaderboard_release_date (datetime)
      Optional timestamp when the private leaderboard should be released.
      Directly acts on the ShowPrivateLeaderboard computed column.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    cloned_from_competition_id (int)
      optional field to track cloning
    row_id_column_name (str)
      For Kernels-based metrics, the name of the ID column to expect in the
      solution and submission.
    required_submission_filename (str)
      Some competitions require a specific submission file name. This is most
      commonly used if they require a .zip or a non-standard file extension.
      Kernels-only competitions will default to requiring 'submission.csv' if
      this is not set.
    template (bool)
    evaluation_algorithm (EvaluationAlgorithm)
    categories (Category)
      The categories assigned to the competition.
    organization (Organization)
    competition_metric_version (CompetitionMetricVersion)
    launched (bool)
      Indicates if the competition is launched or not
    kernels_publishing_disabled_now (bool)
      Whether publishing of Kernels associated with this competition is currently
      disabled (derived from checking DisableKernelsPublishing and
      KernelsPublishingDeadline).
    publicly_cloneable (PubliclyCloneable)
      Indicates if a competition is marked for anyone to clone
    evaluation_setup_error (str)
      Error with the current evaluation setup, if any.
    restrict_link_to_email_list (bool)
      If the competition share link should be restricted by email list.
    created_by_user_id (int)
      The ID for the user who created the competition.
    enable_user_email_share (bool)
      If the competition host is asking participants to share their email
    license (License)
    host_name (str)
      Organization if present or Kaggle, or fall back on createdByUser
    score_truncation_num_decimals (int)
      b/300473593: Currently inferred from LeaderboardDisplayFormat but should be
      pinocchio'd into a Real Field and drop LDF
    locked (bool)
      We lock competitions 7 days after they complete to prevent further updates.
    total_joined_users (int)
    requires_identity_verification (bool)
      Whether identity verification with Persona is required to submit to this
      Competition.
    submission_size_limit_mb (int)
    reward (Reward)
    hackathon (bool)
    simulation (bool)
    uses_hearth (bool)
    accepts_package_submissions (bool)
  """

  def __init__(self):
    self._id = 0
    self._competition_name = ""
    self._title = ""
    self._brief_description = ""
    self._date_enabled = None
    self._deadline = None
    self._has_leaderboard = False
    self._leaderboard_percentage = 0
    self._max_daily_submissions = 0
    self._num_scored_submissions = 0
    self._has_solution = False
    self._num_prizes = 0
    self._forum_id = None
    self._final_leaderboard_has_been_verified = False
    self._disable_submissions = False
    self._is_private = False
    self._user_rank_multiplier = 0.0
    self._limited_participation_group_id = None
    self._withold_final_leaderboard_until_it_has_been_verified = False
    self._public_leaderboard_disclaimer_message = None
    self._final_leaderboard_disclaimer_message = None
    self._date_created = None
    self._disable_leaderboard_prize_indicator = False
    self._competition_host_segment_id = 0
    self._max_team_size = 0
    self._prohibit_new_entrants = False
    self._medals_allowed = False
    self._enable_team_files = False
    self._team_file_deadline = None
    self._prohibit_solution_download = False
    self._total_solution_rows = None
    self._team_merger_explicit_deadline = None
    self._prohibit_new_entrants_explicit_deadline = None
    self._kernels_publishing_disabled_deadline = None
    self._organization_id = None
    self._has_cover_image_url = False
    self._show_private_leaderboard = False
    self._is_team_count_overridden = False
    self._has_scripts = False
    self._share_token = ""
    self._only_allow_kernel_submissions = False
    self._total_teams = 0
    self._total_competitors = 0
    self._total_submissions = 0
    self._rules_required = False
    self._uses_synchronous_reruns = False
    self._post_processor_kernel_id = None
    self._max_cpu_runtime_minutes = None
    self._max_gpu_runtime_minutes = None
    self._private_leaderboard_release_date = None
    self._cloned_from_competition_id = None
    self._row_id_column_name = None
    self._required_submission_filename = None
    self._template = False
    self._evaluation_algorithm = None
    self._categories = []
    self._organization = None
    self._competition_metric_version = None
    self._launched = False
    self._kernels_publishing_disabled_now = False
    self._publicly_cloneable = None
    self._evaluation_setup_error = None
    self._restrict_link_to_email_list = False
    self._created_by_user_id = None
    self._enable_user_email_share = False
    self._license = None
    self._host_name = ""
    self._score_truncation_num_decimals = 0
    self._locked = False
    self._total_joined_users = 0
    self._requires_identity_verification = False
    self._submission_size_limit_mb = 0
    self._reward = None
    self._hackathon = False
    self._simulation = False
    self._uses_hearth = False
    self._accepts_package_submissions = False
    self._freeze()

  @property
  def id(self) -> int:
    """The competition ID."""
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
  def competition_name(self) -> str:
    """The name of the competition as it appears in the URL."""
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def title(self) -> str:
    """The name of the competition as it appears in the title."""
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
  def brief_description(self) -> str:
    """A short description of the competition."""
    return self._brief_description

  @brief_description.setter
  def brief_description(self, brief_description: str):
    if brief_description is None:
      del self.brief_description
      return
    if not isinstance(brief_description, str):
      raise TypeError('brief_description must be of type str')
    self._brief_description = brief_description

  @property
  def date_enabled(self) -> datetime:
    r"""
    The competition's start date in UTC
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
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
  def deadline(self) -> datetime:
    r"""
    The competition's deadline in UTC
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

  @property
  def has_leaderboard(self) -> bool:
    return self._has_leaderboard

  @has_leaderboard.setter
  def has_leaderboard(self, has_leaderboard: bool):
    if has_leaderboard is None:
      del self.has_leaderboard
      return
    if not isinstance(has_leaderboard, bool):
      raise TypeError('has_leaderboard must be of type bool')
    self._has_leaderboard = has_leaderboard

  @property
  def leaderboard_percentage(self) -> int:
    return self._leaderboard_percentage

  @leaderboard_percentage.setter
  def leaderboard_percentage(self, leaderboard_percentage: int):
    if leaderboard_percentage is None:
      del self.leaderboard_percentage
      return
    if not isinstance(leaderboard_percentage, int):
      raise TypeError('leaderboard_percentage must be of type int')
    self._leaderboard_percentage = leaderboard_percentage

  @property
  def max_daily_submissions(self) -> int:
    r"""
    The maximum number of submissions a team can make each day.
    TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)
    """
    return self._max_daily_submissions

  @max_daily_submissions.setter
  def max_daily_submissions(self, max_daily_submissions: int):
    if max_daily_submissions is None:
      del self.max_daily_submissions
      return
    if not isinstance(max_daily_submissions, int):
      raise TypeError('max_daily_submissions must be of type int')
    self._max_daily_submissions = max_daily_submissions

  @property
  def num_scored_submissions(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_scored_submissions

  @num_scored_submissions.setter
  def num_scored_submissions(self, num_scored_submissions: int):
    if num_scored_submissions is None:
      del self.num_scored_submissions
      return
    if not isinstance(num_scored_submissions, int):
      raise TypeError('num_scored_submissions must be of type int')
    self._num_scored_submissions = num_scored_submissions

  @property
  def has_solution(self) -> bool:
    return self._has_solution

  @has_solution.setter
  def has_solution(self, has_solution: bool):
    if has_solution is None:
      del self.has_solution
      return
    if not isinstance(has_solution, bool):
      raise TypeError('has_solution must be of type bool')
    self._has_solution = has_solution

  @property
  def num_prizes(self) -> int:
    """TODO(aip.dev/141): (-- api-linter: core::0141::count-suffix=disabled --)"""
    return self._num_prizes

  @num_prizes.setter
  def num_prizes(self, num_prizes: int):
    if num_prizes is None:
      del self.num_prizes
      return
    if not isinstance(num_prizes, int):
      raise TypeError('num_prizes must be of type int')
    self._num_prizes = num_prizes

  @property
  def forum_id(self) -> int:
    return self._forum_id or 0

  @forum_id.setter
  def forum_id(self, forum_id: Optional[int]):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

  @property
  def final_leaderboard_has_been_verified(self) -> bool:
    return self._final_leaderboard_has_been_verified

  @final_leaderboard_has_been_verified.setter
  def final_leaderboard_has_been_verified(self, final_leaderboard_has_been_verified: bool):
    if final_leaderboard_has_been_verified is None:
      del self.final_leaderboard_has_been_verified
      return
    if not isinstance(final_leaderboard_has_been_verified, bool):
      raise TypeError('final_leaderboard_has_been_verified must be of type bool')
    self._final_leaderboard_has_been_verified = final_leaderboard_has_been_verified

  @property
  def disable_submissions(self) -> bool:
    return self._disable_submissions

  @disable_submissions.setter
  def disable_submissions(self, disable_submissions: bool):
    if disable_submissions is None:
      del self.disable_submissions
      return
    if not isinstance(disable_submissions, bool):
      raise TypeError('disable_submissions must be of type bool')
    self._disable_submissions = disable_submissions

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def user_rank_multiplier(self) -> float:
    return self._user_rank_multiplier

  @user_rank_multiplier.setter
  def user_rank_multiplier(self, user_rank_multiplier: float):
    if user_rank_multiplier is None:
      del self.user_rank_multiplier
      return
    if not isinstance(user_rank_multiplier, float):
      raise TypeError('user_rank_multiplier must be of type float')
    self._user_rank_multiplier = user_rank_multiplier

  @property
  def limited_participation_group_id(self) -> int:
    return self._limited_participation_group_id or 0

  @limited_participation_group_id.setter
  def limited_participation_group_id(self, limited_participation_group_id: Optional[int]):
    if limited_participation_group_id is None:
      del self.limited_participation_group_id
      return
    if not isinstance(limited_participation_group_id, int):
      raise TypeError('limited_participation_group_id must be of type int')
    self._limited_participation_group_id = limited_participation_group_id

  @property
  def withold_final_leaderboard_until_it_has_been_verified(self) -> bool:
    return self._withold_final_leaderboard_until_it_has_been_verified

  @withold_final_leaderboard_until_it_has_been_verified.setter
  def withold_final_leaderboard_until_it_has_been_verified(self, withold_final_leaderboard_until_it_has_been_verified: bool):
    if withold_final_leaderboard_until_it_has_been_verified is None:
      del self.withold_final_leaderboard_until_it_has_been_verified
      return
    if not isinstance(withold_final_leaderboard_until_it_has_been_verified, bool):
      raise TypeError('withold_final_leaderboard_until_it_has_been_verified must be of type bool')
    self._withold_final_leaderboard_until_it_has_been_verified = withold_final_leaderboard_until_it_has_been_verified

  @property
  def public_leaderboard_disclaimer_message(self) -> str:
    return self._public_leaderboard_disclaimer_message or ""

  @public_leaderboard_disclaimer_message.setter
  def public_leaderboard_disclaimer_message(self, public_leaderboard_disclaimer_message: Optional[str]):
    if public_leaderboard_disclaimer_message is None:
      del self.public_leaderboard_disclaimer_message
      return
    if not isinstance(public_leaderboard_disclaimer_message, str):
      raise TypeError('public_leaderboard_disclaimer_message must be of type str')
    self._public_leaderboard_disclaimer_message = public_leaderboard_disclaimer_message

  @property
  def final_leaderboard_disclaimer_message(self) -> str:
    return self._final_leaderboard_disclaimer_message or ""

  @final_leaderboard_disclaimer_message.setter
  def final_leaderboard_disclaimer_message(self, final_leaderboard_disclaimer_message: Optional[str]):
    if final_leaderboard_disclaimer_message is None:
      del self.final_leaderboard_disclaimer_message
      return
    if not isinstance(final_leaderboard_disclaimer_message, str):
      raise TypeError('final_leaderboard_disclaimer_message must be of type str')
    self._final_leaderboard_disclaimer_message = final_leaderboard_disclaimer_message

  @property
  def date_created(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._date_created

  @date_created.setter
  def date_created(self, date_created: datetime):
    if date_created is None:
      del self.date_created
      return
    if not isinstance(date_created, datetime):
      raise TypeError('date_created must be of type datetime')
    self._date_created = date_created

  @property
  def disable_leaderboard_prize_indicator(self) -> bool:
    return self._disable_leaderboard_prize_indicator

  @disable_leaderboard_prize_indicator.setter
  def disable_leaderboard_prize_indicator(self, disable_leaderboard_prize_indicator: bool):
    if disable_leaderboard_prize_indicator is None:
      del self.disable_leaderboard_prize_indicator
      return
    if not isinstance(disable_leaderboard_prize_indicator, bool):
      raise TypeError('disable_leaderboard_prize_indicator must be of type bool')
    self._disable_leaderboard_prize_indicator = disable_leaderboard_prize_indicator

  @property
  def competition_host_segment_id(self) -> int:
    return self._competition_host_segment_id

  @competition_host_segment_id.setter
  def competition_host_segment_id(self, competition_host_segment_id: int):
    if competition_host_segment_id is None:
      del self.competition_host_segment_id
      return
    if not isinstance(competition_host_segment_id, int):
      raise TypeError('competition_host_segment_id must be of type int')
    self._competition_host_segment_id = competition_host_segment_id

  @property
  def max_team_size(self) -> int:
    return self._max_team_size

  @max_team_size.setter
  def max_team_size(self, max_team_size: int):
    if max_team_size is None:
      del self.max_team_size
      return
    if not isinstance(max_team_size, int):
      raise TypeError('max_team_size must be of type int')
    self._max_team_size = max_team_size

  @property
  def prohibit_new_entrants(self) -> bool:
    return self._prohibit_new_entrants

  @prohibit_new_entrants.setter
  def prohibit_new_entrants(self, prohibit_new_entrants: bool):
    if prohibit_new_entrants is None:
      del self.prohibit_new_entrants
      return
    if not isinstance(prohibit_new_entrants, bool):
      raise TypeError('prohibit_new_entrants must be of type bool')
    self._prohibit_new_entrants = prohibit_new_entrants

  @property
  def medals_allowed(self) -> bool:
    return self._medals_allowed

  @medals_allowed.setter
  def medals_allowed(self, medals_allowed: bool):
    if medals_allowed is None:
      del self.medals_allowed
      return
    if not isinstance(medals_allowed, bool):
      raise TypeError('medals_allowed must be of type bool')
    self._medals_allowed = medals_allowed

  @property
  def enable_team_files(self) -> bool:
    return self._enable_team_files

  @enable_team_files.setter
  def enable_team_files(self, enable_team_files: bool):
    if enable_team_files is None:
      del self.enable_team_files
      return
    if not isinstance(enable_team_files, bool):
      raise TypeError('enable_team_files must be of type bool')
    self._enable_team_files = enable_team_files

  @property
  def team_file_deadline(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._team_file_deadline

  @team_file_deadline.setter
  def team_file_deadline(self, team_file_deadline: datetime):
    if team_file_deadline is None:
      del self.team_file_deadline
      return
    if not isinstance(team_file_deadline, datetime):
      raise TypeError('team_file_deadline must be of type datetime')
    self._team_file_deadline = team_file_deadline

  @property
  def prohibit_solution_download(self) -> bool:
    return self._prohibit_solution_download

  @prohibit_solution_download.setter
  def prohibit_solution_download(self, prohibit_solution_download: bool):
    if prohibit_solution_download is None:
      del self.prohibit_solution_download
      return
    if not isinstance(prohibit_solution_download, bool):
      raise TypeError('prohibit_solution_download must be of type bool')
    self._prohibit_solution_download = prohibit_solution_download

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

  @property
  def team_merger_explicit_deadline(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._team_merger_explicit_deadline

  @team_merger_explicit_deadline.setter
  def team_merger_explicit_deadline(self, team_merger_explicit_deadline: datetime):
    if team_merger_explicit_deadline is None:
      del self.team_merger_explicit_deadline
      return
    if not isinstance(team_merger_explicit_deadline, datetime):
      raise TypeError('team_merger_explicit_deadline must be of type datetime')
    self._team_merger_explicit_deadline = team_merger_explicit_deadline

  @property
  def prohibit_new_entrants_explicit_deadline(self) -> datetime:
    r"""
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._prohibit_new_entrants_explicit_deadline

  @prohibit_new_entrants_explicit_deadline.setter
  def prohibit_new_entrants_explicit_deadline(self, prohibit_new_entrants_explicit_deadline: datetime):
    if prohibit_new_entrants_explicit_deadline is None:
      del self.prohibit_new_entrants_explicit_deadline
      return
    if not isinstance(prohibit_new_entrants_explicit_deadline, datetime):
      raise TypeError('prohibit_new_entrants_explicit_deadline must be of type datetime')
    self._prohibit_new_entrants_explicit_deadline = prohibit_new_entrants_explicit_deadline

  @property
  def kernels_publishing_disabled_deadline(self) -> datetime:
    r"""
    Deadline until which users cannot make competition notebooks public.
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
    return self._kernels_publishing_disabled_deadline

  @kernels_publishing_disabled_deadline.setter
  def kernels_publishing_disabled_deadline(self, kernels_publishing_disabled_deadline: datetime):
    if kernels_publishing_disabled_deadline is None:
      del self.kernels_publishing_disabled_deadline
      return
    if not isinstance(kernels_publishing_disabled_deadline, datetime):
      raise TypeError('kernels_publishing_disabled_deadline must be of type datetime')
    self._kernels_publishing_disabled_deadline = kernels_publishing_disabled_deadline

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
  def has_cover_image_url(self) -> bool:
    return self._has_cover_image_url

  @has_cover_image_url.setter
  def has_cover_image_url(self, has_cover_image_url: bool):
    if has_cover_image_url is None:
      del self.has_cover_image_url
      return
    if not isinstance(has_cover_image_url, bool):
      raise TypeError('has_cover_image_url must be of type bool')
    self._has_cover_image_url = has_cover_image_url

  @property
  def show_private_leaderboard(self) -> bool:
    return self._show_private_leaderboard

  @show_private_leaderboard.setter
  def show_private_leaderboard(self, show_private_leaderboard: bool):
    if show_private_leaderboard is None:
      del self.show_private_leaderboard
      return
    if not isinstance(show_private_leaderboard, bool):
      raise TypeError('show_private_leaderboard must be of type bool')
    self._show_private_leaderboard = show_private_leaderboard

  @property
  def is_team_count_overridden(self) -> bool:
    return self._is_team_count_overridden

  @is_team_count_overridden.setter
  def is_team_count_overridden(self, is_team_count_overridden: bool):
    if is_team_count_overridden is None:
      del self.is_team_count_overridden
      return
    if not isinstance(is_team_count_overridden, bool):
      raise TypeError('is_team_count_overridden must be of type bool')
    self._is_team_count_overridden = is_team_count_overridden

  @property
  def has_scripts(self) -> bool:
    return self._has_scripts

  @has_scripts.setter
  def has_scripts(self, has_scripts: bool):
    if has_scripts is None:
      del self.has_scripts
      return
    if not isinstance(has_scripts, bool):
      raise TypeError('has_scripts must be of type bool')
    self._has_scripts = has_scripts

  @property
  def share_token(self) -> str:
    return self._share_token

  @share_token.setter
  def share_token(self, share_token: str):
    if share_token is None:
      del self.share_token
      return
    if not isinstance(share_token, str):
      raise TypeError('share_token must be of type str')
    self._share_token = share_token

  @property
  def only_allow_kernel_submissions(self) -> bool:
    return self._only_allow_kernel_submissions

  @only_allow_kernel_submissions.setter
  def only_allow_kernel_submissions(self, only_allow_kernel_submissions: bool):
    if only_allow_kernel_submissions is None:
      del self.only_allow_kernel_submissions
      return
    if not isinstance(only_allow_kernel_submissions, bool):
      raise TypeError('only_allow_kernel_submissions must be of type bool')
    self._only_allow_kernel_submissions = only_allow_kernel_submissions

  @property
  def total_teams(self) -> int:
    return self._total_teams

  @total_teams.setter
  def total_teams(self, total_teams: int):
    if total_teams is None:
      del self.total_teams
      return
    if not isinstance(total_teams, int):
      raise TypeError('total_teams must be of type int')
    self._total_teams = total_teams

  @property
  def total_competitors(self) -> int:
    return self._total_competitors

  @total_competitors.setter
  def total_competitors(self, total_competitors: int):
    if total_competitors is None:
      del self.total_competitors
      return
    if not isinstance(total_competitors, int):
      raise TypeError('total_competitors must be of type int')
    self._total_competitors = total_competitors

  @property
  def total_submissions(self) -> int:
    return self._total_submissions

  @total_submissions.setter
  def total_submissions(self, total_submissions: int):
    if total_submissions is None:
      del self.total_submissions
      return
    if not isinstance(total_submissions, int):
      raise TypeError('total_submissions must be of type int')
    self._total_submissions = total_submissions

  @property
  def rules_required(self) -> bool:
    return self._rules_required

  @rules_required.setter
  def rules_required(self, rules_required: bool):
    if rules_required is None:
      del self.rules_required
      return
    if not isinstance(rules_required, bool):
      raise TypeError('rules_required must be of type bool')
    self._rules_required = rules_required

  @property
  def uses_synchronous_reruns(self) -> bool:
    return self._uses_synchronous_reruns

  @uses_synchronous_reruns.setter
  def uses_synchronous_reruns(self, uses_synchronous_reruns: bool):
    if uses_synchronous_reruns is None:
      del self.uses_synchronous_reruns
      return
    if not isinstance(uses_synchronous_reruns, bool):
      raise TypeError('uses_synchronous_reruns must be of type bool')
    self._uses_synchronous_reruns = uses_synchronous_reruns

  @property
  def post_processor_kernel_id(self) -> int:
    return self._post_processor_kernel_id or 0

  @post_processor_kernel_id.setter
  def post_processor_kernel_id(self, post_processor_kernel_id: Optional[int]):
    if post_processor_kernel_id is None:
      del self.post_processor_kernel_id
      return
    if not isinstance(post_processor_kernel_id, int):
      raise TypeError('post_processor_kernel_id must be of type int')
    self._post_processor_kernel_id = post_processor_kernel_id

  @property
  def max_cpu_runtime_minutes(self) -> int:
    return self._max_cpu_runtime_minutes or 0

  @max_cpu_runtime_minutes.setter
  def max_cpu_runtime_minutes(self, max_cpu_runtime_minutes: Optional[int]):
    if max_cpu_runtime_minutes is None:
      del self.max_cpu_runtime_minutes
      return
    if not isinstance(max_cpu_runtime_minutes, int):
      raise TypeError('max_cpu_runtime_minutes must be of type int')
    self._max_cpu_runtime_minutes = max_cpu_runtime_minutes

  @property
  def max_gpu_runtime_minutes(self) -> int:
    return self._max_gpu_runtime_minutes or 0

  @max_gpu_runtime_minutes.setter
  def max_gpu_runtime_minutes(self, max_gpu_runtime_minutes: Optional[int]):
    if max_gpu_runtime_minutes is None:
      del self.max_gpu_runtime_minutes
      return
    if not isinstance(max_gpu_runtime_minutes, int):
      raise TypeError('max_gpu_runtime_minutes must be of type int')
    self._max_gpu_runtime_minutes = max_gpu_runtime_minutes

  @property
  def private_leaderboard_release_date(self) -> datetime:
    r"""
    Optional timestamp when the private leaderboard should be released.
    Directly acts on the ShowPrivateLeaderboard computed column.
    TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
    --)
    """
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
  def cloned_from_competition_id(self) -> int:
    """optional field to track cloning"""
    return self._cloned_from_competition_id or 0

  @cloned_from_competition_id.setter
  def cloned_from_competition_id(self, cloned_from_competition_id: Optional[int]):
    if cloned_from_competition_id is None:
      del self.cloned_from_competition_id
      return
    if not isinstance(cloned_from_competition_id, int):
      raise TypeError('cloned_from_competition_id must be of type int')
    self._cloned_from_competition_id = cloned_from_competition_id

  @property
  def row_id_column_name(self) -> str:
    r"""
    For Kernels-based metrics, the name of the ID column to expect in the
    solution and submission.
    """
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
  def required_submission_filename(self) -> str:
    r"""
    Some competitions require a specific submission file name. This is most
    commonly used if they require a .zip or a non-standard file extension.
    Kernels-only competitions will default to requiring 'submission.csv' if
    this is not set.
    """
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
  def template(self) -> bool:
    return self._template

  @template.setter
  def template(self, template: bool):
    if template is None:
      del self.template
      return
    if not isinstance(template, bool):
      raise TypeError('template must be of type bool')
    self._template = template

  @property
  def evaluation_algorithm(self) -> Optional['EvaluationAlgorithm']:
    return self._evaluation_algorithm

  @evaluation_algorithm.setter
  def evaluation_algorithm(self, evaluation_algorithm: Optional['EvaluationAlgorithm']):
    if evaluation_algorithm is None:
      del self.evaluation_algorithm
      return
    if not isinstance(evaluation_algorithm, EvaluationAlgorithm):
      raise TypeError('evaluation_algorithm must be of type EvaluationAlgorithm')
    self._evaluation_algorithm = evaluation_algorithm

  @property
  def categories(self) -> Optional[List[Optional['Category']]]:
    """The categories assigned to the competition."""
    return self._categories

  @categories.setter
  def categories(self, categories: Optional[List[Optional['Category']]]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, list):
      raise TypeError('categories must be of type list')
    if not all([isinstance(t, Category) for t in categories]):
      raise TypeError('categories must contain only items of type Category')
    self._categories = categories

  @property
  def organization(self) -> Optional['Organization']:
    return self._organization

  @organization.setter
  def organization(self, organization: Optional['Organization']):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, Organization):
      raise TypeError('organization must be of type Organization')
    self._organization = organization

  @property
  def competition_metric_version(self) -> Optional['CompetitionMetricVersion']:
    return self._competition_metric_version

  @competition_metric_version.setter
  def competition_metric_version(self, competition_metric_version: Optional['CompetitionMetricVersion']):
    if competition_metric_version is None:
      del self.competition_metric_version
      return
    if not isinstance(competition_metric_version, CompetitionMetricVersion):
      raise TypeError('competition_metric_version must be of type CompetitionMetricVersion')
    self._competition_metric_version = competition_metric_version

  @property
  def launched(self) -> bool:
    """Indicates if the competition is launched or not"""
    return self._launched

  @launched.setter
  def launched(self, launched: bool):
    if launched is None:
      del self.launched
      return
    if not isinstance(launched, bool):
      raise TypeError('launched must be of type bool')
    self._launched = launched

  @property
  def kernels_publishing_disabled_now(self) -> bool:
    r"""
    Whether publishing of Kernels associated with this competition is currently
    disabled (derived from checking DisableKernelsPublishing and
    KernelsPublishingDeadline).
    """
    return self._kernels_publishing_disabled_now

  @kernels_publishing_disabled_now.setter
  def kernels_publishing_disabled_now(self, kernels_publishing_disabled_now: bool):
    if kernels_publishing_disabled_now is None:
      del self.kernels_publishing_disabled_now
      return
    if not isinstance(kernels_publishing_disabled_now, bool):
      raise TypeError('kernels_publishing_disabled_now must be of type bool')
    self._kernels_publishing_disabled_now = kernels_publishing_disabled_now

  @property
  def publicly_cloneable(self) -> 'PubliclyCloneable':
    """Indicates if a competition is marked for anyone to clone"""
    return self._publicly_cloneable or PubliclyCloneable.PUBLICLY_CLONEABLE_UNSPECIFIED

  @publicly_cloneable.setter
  def publicly_cloneable(self, publicly_cloneable: Optional['PubliclyCloneable']):
    if publicly_cloneable is None:
      del self.publicly_cloneable
      return
    if not isinstance(publicly_cloneable, PubliclyCloneable):
      raise TypeError('publicly_cloneable must be of type PubliclyCloneable')
    self._publicly_cloneable = publicly_cloneable

  @property
  def evaluation_setup_error(self) -> str:
    """Error with the current evaluation setup, if any."""
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
  def restrict_link_to_email_list(self) -> bool:
    """If the competition share link should be restricted by email list."""
    return self._restrict_link_to_email_list

  @restrict_link_to_email_list.setter
  def restrict_link_to_email_list(self, restrict_link_to_email_list: bool):
    if restrict_link_to_email_list is None:
      del self.restrict_link_to_email_list
      return
    if not isinstance(restrict_link_to_email_list, bool):
      raise TypeError('restrict_link_to_email_list must be of type bool')
    self._restrict_link_to_email_list = restrict_link_to_email_list

  @property
  def created_by_user_id(self) -> int:
    """The ID for the user who created the competition."""
    return self._created_by_user_id or 0

  @created_by_user_id.setter
  def created_by_user_id(self, created_by_user_id: Optional[int]):
    if created_by_user_id is None:
      del self.created_by_user_id
      return
    if not isinstance(created_by_user_id, int):
      raise TypeError('created_by_user_id must be of type int')
    self._created_by_user_id = created_by_user_id

  @property
  def enable_user_email_share(self) -> bool:
    """If the competition host is asking participants to share their email"""
    return self._enable_user_email_share

  @enable_user_email_share.setter
  def enable_user_email_share(self, enable_user_email_share: bool):
    if enable_user_email_share is None:
      del self.enable_user_email_share
      return
    if not isinstance(enable_user_email_share, bool):
      raise TypeError('enable_user_email_share must be of type bool')
    self._enable_user_email_share = enable_user_email_share

  @property
  def license(self) -> Optional['License']:
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def host_name(self) -> str:
    """Organization if present or Kaggle, or fall back on createdByUser"""
    return self._host_name

  @host_name.setter
  def host_name(self, host_name: str):
    if host_name is None:
      del self.host_name
      return
    if not isinstance(host_name, str):
      raise TypeError('host_name must be of type str')
    self._host_name = host_name

  @property
  def score_truncation_num_decimals(self) -> int:
    r"""
    b/300473593: Currently inferred from LeaderboardDisplayFormat but should be
    pinocchio'd into a Real Field and drop LDF
    """
    return self._score_truncation_num_decimals

  @score_truncation_num_decimals.setter
  def score_truncation_num_decimals(self, score_truncation_num_decimals: int):
    if score_truncation_num_decimals is None:
      del self.score_truncation_num_decimals
      return
    if not isinstance(score_truncation_num_decimals, int):
      raise TypeError('score_truncation_num_decimals must be of type int')
    self._score_truncation_num_decimals = score_truncation_num_decimals

  @property
  def locked(self) -> bool:
    """We lock competitions 7 days after they complete to prevent further updates."""
    return self._locked

  @locked.setter
  def locked(self, locked: bool):
    if locked is None:
      del self.locked
      return
    if not isinstance(locked, bool):
      raise TypeError('locked must be of type bool')
    self._locked = locked

  @property
  def total_joined_users(self) -> int:
    return self._total_joined_users

  @total_joined_users.setter
  def total_joined_users(self, total_joined_users: int):
    if total_joined_users is None:
      del self.total_joined_users
      return
    if not isinstance(total_joined_users, int):
      raise TypeError('total_joined_users must be of type int')
    self._total_joined_users = total_joined_users

  @property
  def requires_identity_verification(self) -> bool:
    r"""
    Whether identity verification with Persona is required to submit to this
    Competition.
    """
    return self._requires_identity_verification

  @requires_identity_verification.setter
  def requires_identity_verification(self, requires_identity_verification: bool):
    if requires_identity_verification is None:
      del self.requires_identity_verification
      return
    if not isinstance(requires_identity_verification, bool):
      raise TypeError('requires_identity_verification must be of type bool')
    self._requires_identity_verification = requires_identity_verification

  @property
  def submission_size_limit_mb(self) -> int:
    return self._submission_size_limit_mb

  @submission_size_limit_mb.setter
  def submission_size_limit_mb(self, submission_size_limit_mb: int):
    if submission_size_limit_mb is None:
      del self.submission_size_limit_mb
      return
    if not isinstance(submission_size_limit_mb, int):
      raise TypeError('submission_size_limit_mb must be of type int')
    self._submission_size_limit_mb = submission_size_limit_mb

  @property
  def reward(self) -> Optional['Reward']:
    return self._reward

  @reward.setter
  def reward(self, reward: Optional['Reward']):
    if reward is None:
      del self.reward
      return
    if not isinstance(reward, Reward):
      raise TypeError('reward must be of type Reward')
    self._reward = reward

  @property
  def hackathon(self) -> bool:
    return self._hackathon

  @hackathon.setter
  def hackathon(self, hackathon: bool):
    if hackathon is None:
      del self.hackathon
      return
    if not isinstance(hackathon, bool):
      raise TypeError('hackathon must be of type bool')
    self._hackathon = hackathon

  @property
  def simulation(self) -> bool:
    return self._simulation

  @simulation.setter
  def simulation(self, simulation: bool):
    if simulation is None:
      del self.simulation
      return
    if not isinstance(simulation, bool):
      raise TypeError('simulation must be of type bool')
    self._simulation = simulation

  @property
  def uses_hearth(self) -> bool:
    return self._uses_hearth

  @uses_hearth.setter
  def uses_hearth(self, uses_hearth: bool):
    if uses_hearth is None:
      del self.uses_hearth
      return
    if not isinstance(uses_hearth, bool):
      raise TypeError('uses_hearth must be of type bool')
    self._uses_hearth = uses_hearth

  @property
  def accepts_package_submissions(self) -> bool:
    return self._accepts_package_submissions

  @accepts_package_submissions.setter
  def accepts_package_submissions(self, accepts_package_submissions: bool):
    if accepts_package_submissions is None:
      del self.accepts_package_submissions
      return
    if not isinstance(accepts_package_submissions, bool):
      raise TypeError('accepts_package_submissions must be of type bool')
    self._accepts_package_submissions = accepts_package_submissions


class Reward(KaggleObject):
  r"""
  TODO(b/350786629): make the DB change to set RewardTypeId and rewardQuantity
  default to 0 and change rewardQuantity type from decimal to int.

  Attributes:
    id (RewardTypeId)
    quantity (int)
    clarification (str)
  """

  def __init__(self):
    self._id = RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED
    self._quantity = 0
    self._clarification = None
    self._freeze()

  @property
  def id(self) -> 'RewardTypeId':
    return self._id

  @id.setter
  def id(self, id: 'RewardTypeId'):
    if id is None:
      del self.id
      return
    if not isinstance(id, RewardTypeId):
      raise TypeError('id must be of type RewardTypeId')
    self._id = id

  @property
  def quantity(self) -> int:
    return self._quantity

  @quantity.setter
  def quantity(self, quantity: int):
    if quantity is None:
      del self.quantity
      return
    if not isinstance(quantity, int):
      raise TypeError('quantity must be of type int')
    self._quantity = quantity

  @property
  def clarification(self) -> str:
    return self._clarification or ""

  @clarification.setter
  def clarification(self, clarification: Optional[str]):
    if clarification is None:
      del self.clarification
      return
    if not isinstance(clarification, str):
      raise TypeError('clarification must be of type str')
    self._clarification = clarification


Competition._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("dateEnabled", "date_enabled", "_date_enabled", datetime, None, DateTimeSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("hasLeaderboard", "has_leaderboard", "_has_leaderboard", bool, False, PredefinedSerializer()),
  FieldMetadata("leaderboardPercentage", "leaderboard_percentage", "_leaderboard_percentage", int, 0, PredefinedSerializer()),
  FieldMetadata("maxDailySubmissions", "max_daily_submissions", "_max_daily_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("numScoredSubmissions", "num_scored_submissions", "_num_scored_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("hasSolution", "has_solution", "_has_solution", bool, False, PredefinedSerializer()),
  FieldMetadata("numPrizes", "num_prizes", "_num_prizes", int, 0, PredefinedSerializer()),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("finalLeaderboardHasBeenVerified", "final_leaderboard_has_been_verified", "_final_leaderboard_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("disableSubmissions", "disable_submissions", "_disable_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("userRankMultiplier", "user_rank_multiplier", "_user_rank_multiplier", float, 0.0, PredefinedSerializer()),
  FieldMetadata("limitedParticipationGroupId", "limited_participation_group_id", "_limited_participation_group_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("witholdFinalLeaderboardUntilItHasBeenVerified", "withold_final_leaderboard_until_it_has_been_verified", "_withold_final_leaderboard_until_it_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("publicLeaderboardDisclaimerMessage", "public_leaderboard_disclaimer_message", "_public_leaderboard_disclaimer_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("finalLeaderboardDisclaimerMessage", "final_leaderboard_disclaimer_message", "_final_leaderboard_disclaimer_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateCreated", "date_created", "_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("disableLeaderboardPrizeIndicator", "disable_leaderboard_prize_indicator", "_disable_leaderboard_prize_indicator", bool, False, PredefinedSerializer()),
  FieldMetadata("competitionHostSegmentId", "competition_host_segment_id", "_competition_host_segment_id", int, 0, PredefinedSerializer()),
  FieldMetadata("maxTeamSize", "max_team_size", "_max_team_size", int, 0, PredefinedSerializer()),
  FieldMetadata("prohibitNewEntrants", "prohibit_new_entrants", "_prohibit_new_entrants", bool, False, PredefinedSerializer()),
  FieldMetadata("medalsAllowed", "medals_allowed", "_medals_allowed", bool, False, PredefinedSerializer()),
  FieldMetadata("enableTeamFiles", "enable_team_files", "_enable_team_files", bool, False, PredefinedSerializer()),
  FieldMetadata("teamFileDeadline", "team_file_deadline", "_team_file_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("prohibitSolutionDownload", "prohibit_solution_download", "_prohibit_solution_download", bool, False, PredefinedSerializer()),
  FieldMetadata("totalSolutionRows", "total_solution_rows", "_total_solution_rows", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("teamMergerExplicitDeadline", "team_merger_explicit_deadline", "_team_merger_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("prohibitNewEntrantsExplicitDeadline", "prohibit_new_entrants_explicit_deadline", "_prohibit_new_entrants_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("kernelsPublishingDisabledDeadline", "kernels_publishing_disabled_deadline", "_kernels_publishing_disabled_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasCoverImageUrl", "has_cover_image_url", "_has_cover_image_url", bool, False, PredefinedSerializer()),
  FieldMetadata("showPrivateLeaderboard", "show_private_leaderboard", "_show_private_leaderboard", bool, False, PredefinedSerializer()),
  FieldMetadata("isTeamCountOverridden", "is_team_count_overridden", "_is_team_count_overridden", bool, False, PredefinedSerializer()),
  FieldMetadata("hasScripts", "has_scripts", "_has_scripts", bool, False, PredefinedSerializer()),
  FieldMetadata("shareToken", "share_token", "_share_token", str, "", PredefinedSerializer()),
  FieldMetadata("onlyAllowKernelSubmissions", "only_allow_kernel_submissions", "_only_allow_kernel_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("totalTeams", "total_teams", "_total_teams", int, 0, PredefinedSerializer()),
  FieldMetadata("totalCompetitors", "total_competitors", "_total_competitors", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSubmissions", "total_submissions", "_total_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("rulesRequired", "rules_required", "_rules_required", bool, False, PredefinedSerializer()),
  FieldMetadata("usesSynchronousReruns", "uses_synchronous_reruns", "_uses_synchronous_reruns", bool, False, PredefinedSerializer()),
  FieldMetadata("postProcessorKernelId", "post_processor_kernel_id", "_post_processor_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxCpuRuntimeMinutes", "max_cpu_runtime_minutes", "_max_cpu_runtime_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxGpuRuntimeMinutes", "max_gpu_runtime_minutes", "_max_gpu_runtime_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateLeaderboardReleaseDate", "private_leaderboard_release_date", "_private_leaderboard_release_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("clonedFromCompetitionId", "cloned_from_competition_id", "_cloned_from_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rowIdColumnName", "row_id_column_name", "_row_id_column_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("requiredSubmissionFilename", "required_submission_filename", "_required_submission_filename", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("template", "template", "_template", bool, False, PredefinedSerializer()),
  FieldMetadata("evaluationAlgorithm", "evaluation_algorithm", "_evaluation_algorithm", EvaluationAlgorithm, None, KaggleObjectSerializer()),
  FieldMetadata("categories", "categories", "_categories", Category, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("organization", "organization", "_organization", Organization, None, KaggleObjectSerializer()),
  FieldMetadata("competitionMetricVersion", "competition_metric_version", "_competition_metric_version", CompetitionMetricVersion, None, KaggleObjectSerializer()),
  FieldMetadata("launched", "launched", "_launched", bool, False, PredefinedSerializer()),
  FieldMetadata("kernelsPublishingDisabledNow", "kernels_publishing_disabled_now", "_kernels_publishing_disabled_now", bool, False, PredefinedSerializer()),
  FieldMetadata("publiclyCloneable", "publicly_cloneable", "_publicly_cloneable", PubliclyCloneable, None, EnumSerializer(), optional=True),
  FieldMetadata("evaluationSetupError", "evaluation_setup_error", "_evaluation_setup_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("restrictLinkToEmailList", "restrict_link_to_email_list", "_restrict_link_to_email_list", bool, False, PredefinedSerializer()),
  FieldMetadata("createdByUserId", "created_by_user_id", "_created_by_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableUserEmailShare", "enable_user_email_share", "_enable_user_email_share", bool, False, PredefinedSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("hostName", "host_name", "_host_name", str, "", PredefinedSerializer()),
  FieldMetadata("scoreTruncationNumDecimals", "score_truncation_num_decimals", "_score_truncation_num_decimals", int, 0, PredefinedSerializer()),
  FieldMetadata("locked", "locked", "_locked", bool, False, PredefinedSerializer()),
  FieldMetadata("totalJoinedUsers", "total_joined_users", "_total_joined_users", int, 0, PredefinedSerializer()),
  FieldMetadata("requiresIdentityVerification", "requires_identity_verification", "_requires_identity_verification", bool, False, PredefinedSerializer()),
  FieldMetadata("submissionSizeLimitMb", "submission_size_limit_mb", "_submission_size_limit_mb", int, 0, PredefinedSerializer()),
  FieldMetadata("reward", "reward", "_reward", Reward, None, KaggleObjectSerializer()),
  FieldMetadata("hackathon", "hackathon", "_hackathon", bool, False, PredefinedSerializer()),
  FieldMetadata("simulation", "simulation", "_simulation", bool, False, PredefinedSerializer()),
  FieldMetadata("usesHearth", "uses_hearth", "_uses_hearth", bool, False, PredefinedSerializer()),
  FieldMetadata("acceptsPackageSubmissions", "accepts_package_submissions", "_accepts_package_submissions", bool, False, PredefinedSerializer()),
]

Reward._fields = [
  FieldMetadata("id", "id", "_id", RewardTypeId, RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("quantity", "quantity", "_quantity", int, 0, PredefinedSerializer()),
  FieldMetadata("clarification", "clarification", "_clarification", str, None, PredefinedSerializer(), optional=True),
]

