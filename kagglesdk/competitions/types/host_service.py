from datetime import datetime
from kagglesdk.competitions.types.competition import PubliclyCloneable
from kagglesdk.competitions.types.competition_enums import HostSegment
from kagglesdk.kaggle_object import *
from typing import Optional

class CompetitionSettings(KaggleObject):
  r"""
  Unified competition settings. See go/unified-competition-settings
  Field names match the Competition message when possible. Note this is
  not 1-1 with the Competition message because the Competition message:
  - does not contain all Competition settings
  - contains fields that will never be updateable
  - may not have a structure that's conducive to certain update operations
    For example, adding/removing entries from long repeated fields.

  Attributes:
    title (str)
      GENERAL SETTINGS GROUP (field numbers 1-19)
    brief_description (str)
      'Subtitle' in the UI.
    competition_name (str)
       'URL' in the UI.
    host_segment (HostSegment)
      GENERAL SETTINGS GROUP: ADMIN ONLY
       'Category' in the UI.
    organization_id (int)
       'Creating As' in the UI.
    rules_required (bool)
       'Require Rules Agreement' in the UI.
    publicly_cloneable (PubliclyCloneable)
      Indicates if a competition is marked for anyone to clone.
    has_scripts (bool)
       'Enable Notebooks' in the UI.
    requires_identity_verification (bool)
      ACCESS & TEAMS SETTINGS GROUP: ADMIN ONLY
      Whether identity verification with Persona is required to submit an entry
      to the competition.
    enable_team_files (bool)
      'Enable Team File Drop' in the UI.
    team_file_deadline (datetime)
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
      Should only be set if enable_team_files is true.
      Team File Drop Deadline' in the UI.
    team_merger_explicit_deadline (datetime)
      KEY DATES SETTINGS GROUP: ADMIN ONLY
      'Team Merger Deadline' in the UI.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    prohibit_new_entrants_explicit_deadline (datetime)
      'New Entrants Deadline' in the UI.
      TODO(b/409380918): prohibit_new_entrants may affect value of
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
    kernels_publishing_disabled_deadline (datetime)
      Whether publishing of Kernels associated with this competition is currently
      disabled (derived from checking DisableKernelsPublishing and
      KernelsPublishingDeadline).
      Should only be set if has_scripts is true.
      'Disable Public Notebooks Until' in the UI.
    disable_submissions (bool)
    public_leaderboard_disclaimer_message (str)
    has_leaderboard (bool)
      SUBMISSIONS & LEADERBOARD SETTINGS GROUP: ADMIN ONLY
      'Show Leaderboard' in the UI.
    disable_leaderboard_prize_indicator (bool)
      'Show Leaderboard Prize Indicator' in the UI.
    withold_final_leaderboard_until_it_has_been_verified (bool)
      'Hold Final Leaderboard for Verification' in the UI.
    final_leaderboard_has_been_verified (bool)
      Should only be set if withold_final_leaderboard_until_it_has_been_verified
      is true.
      'Final Leaderboard Verified' in the UI.
    final_leaderboard_disclaimer_message (str)
      'Private Leaderboard Disclaimer' in the UI.
    only_allow_kernel_submissions (bool)
      CODE COMPETITION SETTINGS GROUP (field numbers 100-119)
      'Code Competition' in the UI. Whether competitors must submit a Notebook.
    uses_synchronous_reruns (bool)
      'Uses Synchronous Reruns' in the UI.
    max_cpu_runtime_minutes (int)
      'Max CPU Runtime Minutes' in the UI.
    max_gpu_runtime_minutes (int)
      'Max GPU Runtime Minutes' in the UI.
    rerun_override_kernel_id (int)
      Host-authored template Notebook the frontend wraps the user's artifact
      (e.g. skill.md) into before submitting. Parallels
      main_py_override_kernel_id.
  """

  def __init__(self):
    self._title = ""
    self._brief_description = ""
    self._competition_name = ""
    self._host_segment = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._organization_id = 0
    self._rules_required = False
    self._publicly_cloneable = None
    self._has_scripts = False
    self._requires_identity_verification = False
    self._enable_team_files = False
    self._team_file_deadline = None
    self._team_merger_explicit_deadline = None
    self._prohibit_new_entrants_explicit_deadline = None
    self._kernels_publishing_disabled_deadline = None
    self._disable_submissions = False
    self._public_leaderboard_disclaimer_message = ""
    self._has_leaderboard = False
    self._disable_leaderboard_prize_indicator = False
    self._withold_final_leaderboard_until_it_has_been_verified = False
    self._final_leaderboard_has_been_verified = False
    self._final_leaderboard_disclaimer_message = ""
    self._only_allow_kernel_submissions = False
    self._uses_synchronous_reruns = False
    self._max_cpu_runtime_minutes = None
    self._max_gpu_runtime_minutes = None
    self._rerun_override_kernel_id = None
    self._freeze()

  @property
  def title(self) -> str:
    """GENERAL SETTINGS GROUP (field numbers 1-19)"""
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
    """'Subtitle' in the UI."""
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
  def competition_name(self) -> str:
    """ 'URL' in the UI."""
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
  def host_segment(self) -> 'HostSegment':
    r"""
    GENERAL SETTINGS GROUP: ADMIN ONLY
     'Category' in the UI.
    """
    return self._host_segment

  @host_segment.setter
  def host_segment(self, host_segment: 'HostSegment'):
    if host_segment is None:
      del self.host_segment
      return
    if not isinstance(host_segment, HostSegment):
      raise TypeError('host_segment must be of type HostSegment')
    self._host_segment = host_segment

  @property
  def organization_id(self) -> int:
    """ 'Creating As' in the UI."""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def rules_required(self) -> bool:
    """ 'Require Rules Agreement' in the UI."""
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
  def publicly_cloneable(self) -> 'PubliclyCloneable':
    """Indicates if a competition is marked for anyone to clone."""
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
  def has_scripts(self) -> bool:
    """ 'Enable Notebooks' in the UI."""
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
  def requires_identity_verification(self) -> bool:
    r"""
    ACCESS & TEAMS SETTINGS GROUP: ADMIN ONLY
    Whether identity verification with Persona is required to submit an entry
    to the competition.
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
  def enable_team_files(self) -> bool:
    """'Enable Team File Drop' in the UI."""
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
    Should only be set if enable_team_files is true.
    Team File Drop Deadline' in the UI.
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
  def team_merger_explicit_deadline(self) -> datetime:
    r"""
    KEY DATES SETTINGS GROUP: ADMIN ONLY
    'Team Merger Deadline' in the UI.
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
    'New Entrants Deadline' in the UI.
    TODO(b/409380918): prohibit_new_entrants may affect value of
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
    Whether publishing of Kernels associated with this competition is currently
    disabled (derived from checking DisableKernelsPublishing and
    KernelsPublishingDeadline).
    Should only be set if has_scripts is true.
    'Disable Public Notebooks Until' in the UI.
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
  def public_leaderboard_disclaimer_message(self) -> str:
    return self._public_leaderboard_disclaimer_message

  @public_leaderboard_disclaimer_message.setter
  def public_leaderboard_disclaimer_message(self, public_leaderboard_disclaimer_message: str):
    if public_leaderboard_disclaimer_message is None:
      del self.public_leaderboard_disclaimer_message
      return
    if not isinstance(public_leaderboard_disclaimer_message, str):
      raise TypeError('public_leaderboard_disclaimer_message must be of type str')
    self._public_leaderboard_disclaimer_message = public_leaderboard_disclaimer_message

  @property
  def has_leaderboard(self) -> bool:
    r"""
    SUBMISSIONS & LEADERBOARD SETTINGS GROUP: ADMIN ONLY
    'Show Leaderboard' in the UI.
    """
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
  def disable_leaderboard_prize_indicator(self) -> bool:
    """'Show Leaderboard Prize Indicator' in the UI."""
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
  def withold_final_leaderboard_until_it_has_been_verified(self) -> bool:
    """'Hold Final Leaderboard for Verification' in the UI."""
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
  def final_leaderboard_has_been_verified(self) -> bool:
    r"""
    Should only be set if withold_final_leaderboard_until_it_has_been_verified
    is true.
    'Final Leaderboard Verified' in the UI.
    """
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
  def final_leaderboard_disclaimer_message(self) -> str:
    """'Private Leaderboard Disclaimer' in the UI."""
    return self._final_leaderboard_disclaimer_message

  @final_leaderboard_disclaimer_message.setter
  def final_leaderboard_disclaimer_message(self, final_leaderboard_disclaimer_message: str):
    if final_leaderboard_disclaimer_message is None:
      del self.final_leaderboard_disclaimer_message
      return
    if not isinstance(final_leaderboard_disclaimer_message, str):
      raise TypeError('final_leaderboard_disclaimer_message must be of type str')
    self._final_leaderboard_disclaimer_message = final_leaderboard_disclaimer_message

  @property
  def only_allow_kernel_submissions(self) -> bool:
    r"""
    CODE COMPETITION SETTINGS GROUP (field numbers 100-119)
    'Code Competition' in the UI. Whether competitors must submit a Notebook.
    """
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
  def uses_synchronous_reruns(self) -> bool:
    """'Uses Synchronous Reruns' in the UI."""
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
  def max_cpu_runtime_minutes(self) -> int:
    """'Max CPU Runtime Minutes' in the UI."""
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
    """'Max GPU Runtime Minutes' in the UI."""
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
  def rerun_override_kernel_id(self) -> int:
    r"""
    Host-authored template Notebook the frontend wraps the user's artifact
    (e.g. skill.md) into before submitting. Parallels
    main_py_override_kernel_id.
    """
    return self._rerun_override_kernel_id or 0

  @rerun_override_kernel_id.setter
  def rerun_override_kernel_id(self, rerun_override_kernel_id: Optional[int]):
    if rerun_override_kernel_id is None:
      del self.rerun_override_kernel_id
      return
    if not isinstance(rerun_override_kernel_id, int):
      raise TypeError('rerun_override_kernel_id must be of type int')
    self._rerun_override_kernel_id = rerun_override_kernel_id


CompetitionSettings._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rulesRequired", "rules_required", "_rules_required", bool, False, PredefinedSerializer()),
  FieldMetadata("publiclyCloneable", "publicly_cloneable", "_publicly_cloneable", PubliclyCloneable, None, EnumSerializer(), optional=True),
  FieldMetadata("hasScripts", "has_scripts", "_has_scripts", bool, False, PredefinedSerializer()),
  FieldMetadata("requiresIdentityVerification", "requires_identity_verification", "_requires_identity_verification", bool, False, PredefinedSerializer()),
  FieldMetadata("enableTeamFiles", "enable_team_files", "_enable_team_files", bool, False, PredefinedSerializer()),
  FieldMetadata("teamFileDeadline", "team_file_deadline", "_team_file_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamMergerExplicitDeadline", "team_merger_explicit_deadline", "_team_merger_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("prohibitNewEntrantsExplicitDeadline", "prohibit_new_entrants_explicit_deadline", "_prohibit_new_entrants_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("kernelsPublishingDisabledDeadline", "kernels_publishing_disabled_deadline", "_kernels_publishing_disabled_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("disableSubmissions", "disable_submissions", "_disable_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("publicLeaderboardDisclaimerMessage", "public_leaderboard_disclaimer_message", "_public_leaderboard_disclaimer_message", str, "", PredefinedSerializer()),
  FieldMetadata("hasLeaderboard", "has_leaderboard", "_has_leaderboard", bool, False, PredefinedSerializer()),
  FieldMetadata("disableLeaderboardPrizeIndicator", "disable_leaderboard_prize_indicator", "_disable_leaderboard_prize_indicator", bool, False, PredefinedSerializer()),
  FieldMetadata("witholdFinalLeaderboardUntilItHasBeenVerified", "withold_final_leaderboard_until_it_has_been_verified", "_withold_final_leaderboard_until_it_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("finalLeaderboardHasBeenVerified", "final_leaderboard_has_been_verified", "_final_leaderboard_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("finalLeaderboardDisclaimerMessage", "final_leaderboard_disclaimer_message", "_final_leaderboard_disclaimer_message", str, "", PredefinedSerializer()),
  FieldMetadata("onlyAllowKernelSubmissions", "only_allow_kernel_submissions", "_only_allow_kernel_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("usesSynchronousReruns", "uses_synchronous_reruns", "_uses_synchronous_reruns", bool, False, PredefinedSerializer()),
  FieldMetadata("maxCpuRuntimeMinutes", "max_cpu_runtime_minutes", "_max_cpu_runtime_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("maxGpuRuntimeMinutes", "max_gpu_runtime_minutes", "_max_gpu_runtime_minutes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("rerunOverrideKernelId", "rerun_override_kernel_id", "_rerun_override_kernel_id", int, None, PredefinedSerializer(), optional=True),
]

