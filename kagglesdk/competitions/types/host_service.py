from datetime import datetime
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.competitions.legacy.types.legacy_competition_host_service import EvaluationMetricParameter
from kagglesdk.competitions.types.competition import Competition, PubliclyCloneable, Reward
from kagglesdk.competitions.types.competition_email_invite import CompetitionEmailInvite
from kagglesdk.competitions.types.competition_enums import CompetitionPrivacy, HostSegment
from kagglesdk.competitions.types.competition_types import PrivacySettings
from kagglesdk.competitions.types.evaluation_algorithm import CompetitionMetricVersion, EvaluationAlgorithm
from kagglesdk.competitions.types.simulations import CompetitionSimulationSettings
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import LicenseOption
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List, Dict

class AddHostUserRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    host_user_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._host_user_id = 0
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
  def host_user_id(self) -> int:
    return self._host_user_id

  @host_user_id.setter
  def host_user_id(self, host_user_id: int):
    if host_user_id is None:
      del self.host_user_id
      return
    if not isinstance(host_user_id, int):
      raise TypeError('host_user_id must be of type int')
    self._host_user_id = host_user_id


class ClaimCompetitionSyntheticCopyRequest(KaggleObject):
  r"""
  Attributes:
    base_competition_id (int)
    title (str)
    slug (str)
    brief_description (str)
    privacy (CompetitionPrivacy)
    disable_kernels (bool)
    restrict_link_to_email_list (bool)
      restricts those who join the competition via share link to a specific list
      of emails/domains
    reward (Reward)
    host_segment (HostSegment)
  """

  def __init__(self):
    self._base_competition_id = 0
    self._title = ""
    self._slug = ""
    self._brief_description = ""
    self._privacy = CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED
    self._disable_kernels = None
    self._restrict_link_to_email_list = None
    self._reward = None
    self._host_segment = None
    self._freeze()

  @property
  def base_competition_id(self) -> int:
    return self._base_competition_id

  @base_competition_id.setter
  def base_competition_id(self, base_competition_id: int):
    if base_competition_id is None:
      del self.base_competition_id
      return
    if not isinstance(base_competition_id, int):
      raise TypeError('base_competition_id must be of type int')
    self._base_competition_id = base_competition_id

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
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def brief_description(self) -> str:
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
  def privacy(self) -> 'CompetitionPrivacy':
    return self._privacy

  @privacy.setter
  def privacy(self, privacy: 'CompetitionPrivacy'):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, CompetitionPrivacy):
      raise TypeError('privacy must be of type CompetitionPrivacy')
    self._privacy = privacy

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
  def restrict_link_to_email_list(self) -> bool:
    r"""
    restricts those who join the competition via share link to a specific list
    of emails/domains
    """
    return self._restrict_link_to_email_list or False

  @restrict_link_to_email_list.setter
  def restrict_link_to_email_list(self, restrict_link_to_email_list: Optional[bool]):
    if restrict_link_to_email_list is None:
      del self.restrict_link_to_email_list
      return
    if not isinstance(restrict_link_to_email_list, bool):
      raise TypeError('restrict_link_to_email_list must be of type bool')
    self._restrict_link_to_email_list = restrict_link_to_email_list

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


class ClaimCompetitionSyntheticCopyResponse(KaggleObject):
  r"""
  Attributes:
    claimed_competition_id (int)
  """

  def __init__(self):
    self._claimed_competition_id = 0
    self._freeze()

  @property
  def claimed_competition_id(self) -> int:
    return self._claimed_competition_id

  @claimed_competition_id.setter
  def claimed_competition_id(self, claimed_competition_id: int):
    if claimed_competition_id is None:
      del self.claimed_competition_id
      return
    if not isinstance(claimed_competition_id, int):
      raise TypeError('claimed_competition_id must be of type int')
    self._claimed_competition_id = claimed_competition_id


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
    privacy_settings (PrivacySettings)
      ACCESS & TEAMS SETTINGS GROUP (field numbers 20-39)
      'Visibility', 'Who Can Join', and 'Invitation Link' in the UI.
      The field privacy determines visibility. The field restrict_to_email_list
      determines whether the competition share link should be restricted to the
      email list. The field share_token is the 'Invitation Link' slug if the
      competition is private. If the competition is not private, the slug is the
      competition name.
    has_scripts (bool)
       'Enable Notebooks' in the UI.
    enable_user_email_share (bool)
      'Ask participants to share their email addresses when joining' in the UI.
    max_team_size (int)
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
    deadline (datetime)
      KEY DATES SETTINGS GROUP (field numbers 40-59)
      'Competition Deadline' in the UI.
    private_leaderboard_release_date (datetime)
      Directly acts on the ShowPrivateLeaderboard computed column.
      Optional; when the private leaderboard should be released.
      TODO(aip.dev/142): (-- api-linter: core::0142::time-field-names=disabled
      --)
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
    max_daily_submissions (int)
      SUBMISSIONS & LEADERBOARD SETTINGS GROUP (field numbers 60-79)
      'Maximum Daily Submission Limit' in the UI.
    num_scored_submissions (int)
      'Scored Private Submissions' in the UI.
    disable_submissions (bool)
    score_truncation_num_decimals (int)
      'Leaderboard Decimals To Display' in the UI.
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
    reward (Reward)
      PRIZES SETTINGS GROUP (field numbers 80-99)
      Reward.quantity is 'Total Prize Pool' in the UI, and should
      only be set if 'Competition will award prizes' is true.
      Reward.clarification is 'Prize Details (Optional)' in the UI.
      Reward.id is 'Reward Type' in the UI. Reward.id should only be available to
      Admin.
    num_prizes (int)
      PRIZES SETTINGS GROUP: ADMIN ONLY
      'Leaderboard Prize Places' in the UI.
    medals_allowed (bool)
      'Awards Medals' in the UI.
    user_rank_multiplier (float)
      'Awards Points' in the UI.
  """

  def __init__(self):
    self._title = ""
    self._brief_description = ""
    self._competition_name = ""
    self._host_segment = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._organization_id = 0
    self._rules_required = False
    self._publicly_cloneable = None
    self._privacy_settings = None
    self._has_scripts = False
    self._enable_user_email_share = False
    self._max_team_size = 0
    self._requires_identity_verification = False
    self._enable_team_files = False
    self._team_file_deadline = None
    self._deadline = None
    self._private_leaderboard_release_date = None
    self._team_merger_explicit_deadline = None
    self._prohibit_new_entrants_explicit_deadline = None
    self._kernels_publishing_disabled_deadline = None
    self._max_daily_submissions = 0
    self._num_scored_submissions = 0
    self._disable_submissions = False
    self._score_truncation_num_decimals = 0
    self._public_leaderboard_disclaimer_message = ""
    self._has_leaderboard = False
    self._disable_leaderboard_prize_indicator = False
    self._withold_final_leaderboard_until_it_has_been_verified = False
    self._final_leaderboard_has_been_verified = False
    self._final_leaderboard_disclaimer_message = ""
    self._reward = None
    self._num_prizes = 0
    self._medals_allowed = False
    self._user_rank_multiplier = 0.0
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
  def privacy_settings(self) -> Optional['PrivacySettings']:
    r"""
    ACCESS & TEAMS SETTINGS GROUP (field numbers 20-39)
    'Visibility', 'Who Can Join', and 'Invitation Link' in the UI.
    The field privacy determines visibility. The field restrict_to_email_list
    determines whether the competition share link should be restricted to the
    email list. The field share_token is the 'Invitation Link' slug if the
    competition is private. If the competition is not private, the slug is the
    competition name.
    """
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
  def enable_user_email_share(self) -> bool:
    """'Ask participants to share their email addresses when joining' in the UI."""
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
  def deadline(self) -> datetime:
    r"""
    KEY DATES SETTINGS GROUP (field numbers 40-59)
    'Competition Deadline' in the UI.
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
  def private_leaderboard_release_date(self) -> datetime:
    r"""
    Directly acts on the ShowPrivateLeaderboard computed column.
    Optional; when the private leaderboard should be released.
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
  def max_daily_submissions(self) -> int:
    r"""
    SUBMISSIONS & LEADERBOARD SETTINGS GROUP (field numbers 60-79)
    'Maximum Daily Submission Limit' in the UI.
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
    """'Scored Private Submissions' in the UI."""
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
  def score_truncation_num_decimals(self) -> int:
    """'Leaderboard Decimals To Display' in the UI."""
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
  def reward(self) -> Optional['Reward']:
    r"""
    PRIZES SETTINGS GROUP (field numbers 80-99)
    Reward.quantity is 'Total Prize Pool' in the UI, and should
    only be set if 'Competition will award prizes' is true.
    Reward.clarification is 'Prize Details (Optional)' in the UI.
    Reward.id is 'Reward Type' in the UI. Reward.id should only be available to
    Admin.
    """
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
  def num_prizes(self) -> int:
    r"""
    PRIZES SETTINGS GROUP: ADMIN ONLY
    'Leaderboard Prize Places' in the UI.
    """
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
  def medals_allowed(self) -> bool:
    """'Awards Medals' in the UI."""
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
  def user_rank_multiplier(self) -> float:
    """'Awards Points' in the UI."""
    return self._user_rank_multiplier

  @user_rank_multiplier.setter
  def user_rank_multiplier(self, user_rank_multiplier: float):
    if user_rank_multiplier is None:
      del self.user_rank_multiplier
      return
    if not isinstance(user_rank_multiplier, float):
      raise TypeError('user_rank_multiplier must be of type float')
    self._user_rank_multiplier = user_rank_multiplier


class CreateCompetitionEmailInvitesRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    emails_to_add (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._emails_to_add = []
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
  def emails_to_add(self) -> Optional[List[str]]:
    return self._emails_to_add

  @emails_to_add.setter
  def emails_to_add(self, emails_to_add: Optional[List[str]]):
    if emails_to_add is None:
      del self.emails_to_add
      return
    if not isinstance(emails_to_add, list):
      raise TypeError('emails_to_add must be of type list')
    if not all([isinstance(t, str) for t in emails_to_add]):
      raise TypeError('emails_to_add must contain only items of type str')
    self._emails_to_add = emails_to_add


class CreateCompetitionEmailInvitesResponse(KaggleObject):
  r"""
  Attributes:
    email_invites (CompetitionEmailInvite)
  """

  def __init__(self):
    self._email_invites = []
    self._freeze()

  @property
  def email_invites(self) -> Optional[List[Optional['CompetitionEmailInvite']]]:
    return self._email_invites

  @email_invites.setter
  def email_invites(self, email_invites: Optional[List[Optional['CompetitionEmailInvite']]]):
    if email_invites is None:
      del self.email_invites
      return
    if not isinstance(email_invites, list):
      raise TypeError('email_invites must be of type list')
    if not all([isinstance(t, CompetitionEmailInvite) for t in email_invites]):
      raise TypeError('email_invites must contain only items of type CompetitionEmailInvite')
    self._email_invites = email_invites


class CreateCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    title (str)
    slug (str)
    brief_description (str)
    host_segment (HostSegment)
    privacy (CompetitionPrivacy)
    clone_competition_id (int)
      If present, we will clone from this competition, and copy over
      several configuration settings, pages, dataset, evaluation setup, etc.
    disable_kernels (bool)
    restrict_link_to_email_list (bool)
      restricts those who join the competition via share link to a specific list
      of emails/domains
    license_id (int)
    organization_id (int)
      Ties this competition to an organization, i.e. grants all members of an
      organization read-only access to this competition.
    clone_exclude_competition_data (bool)
      If cloning, whether to exclude the competition's data (solution, sandbox
      submissions, images, and databundles).
    reward (Reward)
    hackathon (bool)
      If the competition should be a hackathon competition.
    num_prizes (int)
      TODO(b/372476849): Add num_prizes to Reward and clean up numPrizes.
  """

  def __init__(self):
    self._title = ""
    self._slug = ""
    self._brief_description = ""
    self._host_segment = HostSegment.HOST_SEGMENT_UNSPECIFIED
    self._privacy = CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED
    self._clone_competition_id = None
    self._disable_kernels = None
    self._restrict_link_to_email_list = None
    self._license_id = None
    self._organization_id = None
    self._clone_exclude_competition_data = None
    self._reward = None
    self._hackathon = None
    self._num_prizes = None
    self._freeze()

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
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def brief_description(self) -> str:
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
  def host_segment(self) -> 'HostSegment':
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
  def privacy(self) -> 'CompetitionPrivacy':
    return self._privacy

  @privacy.setter
  def privacy(self, privacy: 'CompetitionPrivacy'):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, CompetitionPrivacy):
      raise TypeError('privacy must be of type CompetitionPrivacy')
    self._privacy = privacy

  @property
  def clone_competition_id(self) -> int:
    r"""
    If present, we will clone from this competition, and copy over
    several configuration settings, pages, dataset, evaluation setup, etc.
    """
    return self._clone_competition_id or 0

  @clone_competition_id.setter
  def clone_competition_id(self, clone_competition_id: Optional[int]):
    if clone_competition_id is None:
      del self.clone_competition_id
      return
    if not isinstance(clone_competition_id, int):
      raise TypeError('clone_competition_id must be of type int')
    self._clone_competition_id = clone_competition_id

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
  def restrict_link_to_email_list(self) -> bool:
    r"""
    restricts those who join the competition via share link to a specific list
    of emails/domains
    """
    return self._restrict_link_to_email_list or False

  @restrict_link_to_email_list.setter
  def restrict_link_to_email_list(self, restrict_link_to_email_list: Optional[bool]):
    if restrict_link_to_email_list is None:
      del self.restrict_link_to_email_list
      return
    if not isinstance(restrict_link_to_email_list, bool):
      raise TypeError('restrict_link_to_email_list must be of type bool')
    self._restrict_link_to_email_list = restrict_link_to_email_list

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
  def organization_id(self) -> int:
    r"""
    Ties this competition to an organization, i.e. grants all members of an
    organization read-only access to this competition.
    """
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
  def clone_exclude_competition_data(self) -> bool:
    r"""
    If cloning, whether to exclude the competition's data (solution, sandbox
    submissions, images, and databundles).
    """
    return self._clone_exclude_competition_data or False

  @clone_exclude_competition_data.setter
  def clone_exclude_competition_data(self, clone_exclude_competition_data: Optional[bool]):
    if clone_exclude_competition_data is None:
      del self.clone_exclude_competition_data
      return
    if not isinstance(clone_exclude_competition_data, bool):
      raise TypeError('clone_exclude_competition_data must be of type bool')
    self._clone_exclude_competition_data = clone_exclude_competition_data

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
  def hackathon(self) -> bool:
    """If the competition should be a hackathon competition."""
    return self._hackathon or False

  @hackathon.setter
  def hackathon(self, hackathon: Optional[bool]):
    if hackathon is None:
      del self.hackathon
      return
    if not isinstance(hackathon, bool):
      raise TypeError('hackathon must be of type bool')
    self._hackathon = hackathon

  @property
  def num_prizes(self) -> int:
    """TODO(b/372476849): Add num_prizes to Reward and clean up numPrizes."""
    return self._num_prizes or 0

  @num_prizes.setter
  def num_prizes(self, num_prizes: Optional[int]):
    if num_prizes is None:
      del self.num_prizes
      return
    if not isinstance(num_prizes, int):
      raise TypeError('num_prizes must be of type int')
    self._num_prizes = num_prizes


class CreateCompetitionResponse(KaggleObject):
  r"""
  Attributes:
    competition (Competition)
  """

  def __init__(self):
    self._competition = None
    self._freeze()

  @property
  def competition(self) -> Optional['Competition']:
    return self._competition

  @competition.setter
  def competition(self, competition: Optional['Competition']):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, Competition):
      raise TypeError('competition must be of type Competition')
    self._competition = competition


class CreateCompetitionSampleSubmissionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    blob_token (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._blob_token = ""
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
  def blob_token(self) -> str:
    return self._blob_token

  @blob_token.setter
  def blob_token(self, blob_token: str):
    if blob_token is None:
      del self.blob_token
      return
    if not isinstance(blob_token, str):
      raise TypeError('blob_token must be of type str')
    self._blob_token = blob_token


class CreateCompetitionSolutionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    blob_token (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._blob_token = ""
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
  def blob_token(self) -> str:
    return self._blob_token

  @blob_token.setter
  def blob_token(self, blob_token: str):
    if blob_token is None:
      del self.blob_token
      return
    if not isinstance(blob_token, str):
      raise TypeError('blob_token must be of type str')
    self._blob_token = blob_token


class DeleteCompetitionEmailInviteRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    email_invite_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._email_invite_id = 0
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
  def email_invite_id(self) -> int:
    return self._email_invite_id

  @email_invite_id.setter
  def email_invite_id(self, email_invite_id: int):
    if email_invite_id is None:
      del self.email_invite_id
      return
    if not isinstance(email_invite_id, int):
      raise TypeError('email_invite_id must be of type int')
    self._email_invite_id = email_invite_id


class DeleteCompetitionRequest(KaggleObject):
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


class DeleteCompetitionResponse(KaggleObject):
  r"""
  """

  pass

class DeleteSolutionFilesRequest(KaggleObject):
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


class GetCompetitionSimulationSettingsRequest(KaggleObject):
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


class GetDatabundleBasicInfoRequest(KaggleObject):
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


class GetPrivacySettingsRequest(KaggleObject):
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


class LaunchCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    future_time (datetime)
      Optional time in the future to launch the competition rather than launching
      it immediately.
  """

  def __init__(self):
    self._competition_id = 0
    self._future_time = None
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
  def future_time(self) -> datetime:
    r"""
    Optional time in the future to launch the competition rather than launching
    it immediately.
    """
    return self._future_time

  @future_time.setter
  def future_time(self, future_time: datetime):
    if future_time is None:
      del self.future_time
      return
    if not isinstance(future_time, datetime):
      raise TypeError('future_time must be of type datetime')
    self._future_time = future_time


class ListCompetitionEmailInvitesRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

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


class ListCompetitionEmailInvitesResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    email_invites (CompetitionEmailInvite)
  """

  def __init__(self):
    self._email_invites = []
    self._freeze()

  @property
  def email_invites(self) -> Optional[List[Optional['CompetitionEmailInvite']]]:
    return self._email_invites

  @email_invites.setter
  def email_invites(self, email_invites: Optional[List[Optional['CompetitionEmailInvite']]]):
    if email_invites is None:
      del self.email_invites
      return
    if not isinstance(email_invites, list):
      raise TypeError('email_invites must be of type list')
    if not all([isinstance(t, CompetitionEmailInvite) for t in email_invites]):
      raise TypeError('email_invites must contain only items of type CompetitionEmailInvite')
    self._email_invites = email_invites


class ListCompetitionLicensesRequest(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-size-field=disabled --)
  TODO(aip.dev/158): (-- api-linter:
  core::0158::request-page-token-field=disabled --)

  """

  pass

class ListCompetitionLicensesResponse(KaggleObject):
  r"""
  TODO(aip.dev/158): (-- api-linter:
  core::0158::response-next-page-token-field=disabled --)

  Attributes:
    licenses (LicenseOption)
  """

  def __init__(self):
    self._licenses = []
    self._freeze()

  @property
  def licenses(self) -> Optional[List[Optional['LicenseOption']]]:
    return self._licenses

  @licenses.setter
  def licenses(self, licenses: Optional[List[Optional['LicenseOption']]]):
    if licenses is None:
      del self.licenses
      return
    if not isinstance(licenses, list):
      raise TypeError('licenses must be of type list')
    if not all([isinstance(t, LicenseOption) for t in licenses]):
      raise TypeError('licenses must contain only items of type LicenseOption')
    self._licenses = licenses


class ListHostUsersRequest(KaggleObject):
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


class ListHostUsersResponse(KaggleObject):
  r"""
  Attributes:
    hosts (UserAvatar)
  """

  def __init__(self):
    self._hosts = []
    self._freeze()

  @property
  def hosts(self) -> Optional[List[Optional['UserAvatar']]]:
    return self._hosts

  @hosts.setter
  def hosts(self, hosts: Optional[List[Optional['UserAvatar']]]):
    if hosts is None:
      del self.hosts
      return
    if not isinstance(hosts, list):
      raise TypeError('hosts must be of type list')
    if not all([isinstance(t, UserAvatar) for t in hosts]):
      raise TypeError('hosts must contain only items of type UserAvatar')
    self._hosts = hosts


class RegenerateShareTokenRequest(KaggleObject):
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


class RemoveHostUserRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    host_user_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._host_user_id = 0
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
  def host_user_id(self) -> int:
    return self._host_user_id

  @host_user_id.setter
  def host_user_id(self, host_user_id: int):
    if host_user_id is None:
      del self.host_user_id
      return
    if not isinstance(host_user_id, int):
      raise TypeError('host_user_id must be of type int')
    self._host_user_id = host_user_id


class SetCompetitionCitationAuthorsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    authors (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._authors = ""
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
  def authors(self) -> str:
    return self._authors

  @authors.setter
  def authors(self, authors: str):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, str):
      raise TypeError('authors must be of type str')
    self._authors = authors


class SetCompetitionMetricRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    evaluation_algorithm_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._evaluation_algorithm_id = 0
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


class SetCompetitionMetricResponse(KaggleObject):
  r"""
  Attributes:
    metric (EvaluationAlgorithm)
    metric_version (CompetitionMetricVersion)
  """

  def __init__(self):
    self._metric = None
    self._metric_version = None
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


class SetEvaluationMetricParametersRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    name_value_pairs (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._name_value_pairs = {}
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
  def name_value_pairs(self) -> Optional[Dict[str, str]]:
    return self._name_value_pairs

  @name_value_pairs.setter
  def name_value_pairs(self, name_value_pairs: Optional[Dict[str, str]]):
    if name_value_pairs is None:
      del self.name_value_pairs
      return
    if not isinstance(name_value_pairs, dict):
      raise TypeError('name_value_pairs must be of type dict')
    if not all([isinstance(v, str) for k, v in name_value_pairs]):
      raise TypeError('name_value_pairs must contain only items of type str')
    self._name_value_pairs = name_value_pairs


class ToggleBenchmarkSubmissionRequest(KaggleObject):
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


class UpdateCompetitionSettingsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      Specifies which Competition to update. Required.
    settings (CompetitionSettings)
      Specifies the data in the Competition to update.
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
    """Specifies which Competition to update. Required."""
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
    """Specifies the data in the Competition to update."""
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


class UpdateCompetitionSettingsResponse(KaggleObject):
  r"""
  Attributes:
    settings (CompetitionSettings)
      Updated competition settings.
  """

  def __init__(self):
    self._settings = None
    self._freeze()

  @property
  def settings(self) -> Optional['CompetitionSettings']:
    """Updated competition settings."""
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['CompetitionSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, CompetitionSettings):
      raise TypeError('settings must be of type CompetitionSettings')
    self._settings = settings


class UpdateCompetitionSimulationSettingsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    settings (CompetitionSimulationSettings)
  """

  def __init__(self):
    self._competition_id = 0
    self._settings = None
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
  def settings(self) -> Optional['CompetitionSimulationSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['CompetitionSimulationSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, CompetitionSimulationSettings):
      raise TypeError('settings must be of type CompetitionSimulationSettings')
    self._settings = settings


class UpdateCurrentCompetitionMetricVersionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      For now we only support updating to the latest version of the metric
      currently set on the Competition.
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    r"""
    For now we only support updating to the latest version of the metric
    currently set on the Competition.
    """
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class UpdateCurrentCompetitionMetricVersionResponse(KaggleObject):
  r"""
  Attributes:
    competition_metric_version (CompetitionMetricVersion)
      The metric version which is now set on the Competition.
    parameters (EvaluationMetricParameter)
      The latest hyperparameter values on the Competition.
  """

  def __init__(self):
    self._competition_metric_version = None
    self._parameters = []
    self._freeze()

  @property
  def competition_metric_version(self) -> Optional['CompetitionMetricVersion']:
    """The metric version which is now set on the Competition."""
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
  def parameters(self) -> Optional[List[Optional['EvaluationMetricParameter']]]:
    """The latest hyperparameter values on the Competition."""
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


class UpdateImagesRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    header (CroppedImageUpload)
    thumbnail (CroppedImageUpload)
  """

  def __init__(self):
    self._competition_id = 0
    self._header = None
    self._thumbnail = None
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
  def header(self) -> Optional['CroppedImageUpload']:
    return self._header

  @header.setter
  def header(self, header: Optional['CroppedImageUpload']):
    if header is None:
      del self.header
      return
    if not isinstance(header, CroppedImageUpload):
      raise TypeError('header must be of type CroppedImageUpload')
    self._header = header

  @property
  def thumbnail(self) -> Optional['CroppedImageUpload']:
    return self._thumbnail

  @thumbnail.setter
  def thumbnail(self, thumbnail: Optional['CroppedImageUpload']):
    if thumbnail is None:
      del self.thumbnail
      return
    if not isinstance(thumbnail, CroppedImageUpload):
      raise TypeError('thumbnail must be of type CroppedImageUpload')
    self._thumbnail = thumbnail


class UpdateImagesResponse(KaggleObject):
  r"""
  Attributes:
    cover_image_url (str)
    thumbnail_image_url (str)
  """

  def __init__(self):
    self._cover_image_url = None
    self._thumbnail_image_url = None
    self._freeze()

  @property
  def cover_image_url(self) -> str:
    return self._cover_image_url or ""

  @cover_image_url.setter
  def cover_image_url(self, cover_image_url: Optional[str]):
    if cover_image_url is None:
      del self.cover_image_url
      return
    if not isinstance(cover_image_url, str):
      raise TypeError('cover_image_url must be of type str')
    self._cover_image_url = cover_image_url

  @property
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url or ""

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: Optional[str]):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url


class UpdateSandboxSubmissionNameRequest(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
    name (str)
  """

  def __init__(self):
    self._submission_id = 0
    self._name = ""
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


class UpdateTeamsVisibilityRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      All teams must be from this competition
    team_ids (int)
    hide (bool)
  """

  def __init__(self):
    self._competition_id = 0
    self._team_ids = []
    self._hide = False
    self._freeze()

  @property
  def competition_id(self) -> int:
    """All teams must be from this competition"""
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
  def team_ids(self) -> Optional[List[int]]:
    return self._team_ids

  @team_ids.setter
  def team_ids(self, team_ids: Optional[List[int]]):
    if team_ids is None:
      del self.team_ids
      return
    if not isinstance(team_ids, list):
      raise TypeError('team_ids must be of type list')
    if not all([isinstance(t, int) for t in team_ids]):
      raise TypeError('team_ids must contain only items of type int')
    self._team_ids = team_ids

  @property
  def hide(self) -> bool:
    return self._hide

  @hide.setter
  def hide(self, hide: bool):
    if hide is None:
      del self.hide
      return
    if not isinstance(hide, bool):
      raise TypeError('hide must be of type bool')
    self._hide = hide


AddHostUserRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hostUserId", "host_user_id", "_host_user_id", int, 0, PredefinedSerializer()),
]

ClaimCompetitionSyntheticCopyRequest._fields = [
  FieldMetadata("baseCompetitionId", "base_competition_id", "_base_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("privacy", "privacy", "_privacy", CompetitionPrivacy, CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("disableKernels", "disable_kernels", "_disable_kernels", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("restrictLinkToEmailList", "restrict_link_to_email_list", "_restrict_link_to_email_list", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reward", "reward", "_reward", Reward, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, None, EnumSerializer(), optional=True),
]

ClaimCompetitionSyntheticCopyResponse._fields = [
  FieldMetadata("claimedCompetitionId", "claimed_competition_id", "_claimed_competition_id", int, 0, PredefinedSerializer()),
]

CompetitionSettings._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("rulesRequired", "rules_required", "_rules_required", bool, False, PredefinedSerializer()),
  FieldMetadata("publiclyCloneable", "publicly_cloneable", "_publicly_cloneable", PubliclyCloneable, None, EnumSerializer(), optional=True),
  FieldMetadata("privacySettings", "privacy_settings", "_privacy_settings", PrivacySettings, None, KaggleObjectSerializer()),
  FieldMetadata("hasScripts", "has_scripts", "_has_scripts", bool, False, PredefinedSerializer()),
  FieldMetadata("enableUserEmailShare", "enable_user_email_share", "_enable_user_email_share", bool, False, PredefinedSerializer()),
  FieldMetadata("maxTeamSize", "max_team_size", "_max_team_size", int, 0, PredefinedSerializer()),
  FieldMetadata("requiresIdentityVerification", "requires_identity_verification", "_requires_identity_verification", bool, False, PredefinedSerializer()),
  FieldMetadata("enableTeamFiles", "enable_team_files", "_enable_team_files", bool, False, PredefinedSerializer()),
  FieldMetadata("teamFileDeadline", "team_file_deadline", "_team_file_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("privateLeaderboardReleaseDate", "private_leaderboard_release_date", "_private_leaderboard_release_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("teamMergerExplicitDeadline", "team_merger_explicit_deadline", "_team_merger_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("prohibitNewEntrantsExplicitDeadline", "prohibit_new_entrants_explicit_deadline", "_prohibit_new_entrants_explicit_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("kernelsPublishingDisabledDeadline", "kernels_publishing_disabled_deadline", "_kernels_publishing_disabled_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("maxDailySubmissions", "max_daily_submissions", "_max_daily_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("numScoredSubmissions", "num_scored_submissions", "_num_scored_submissions", int, 0, PredefinedSerializer()),
  FieldMetadata("disableSubmissions", "disable_submissions", "_disable_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("scoreTruncationNumDecimals", "score_truncation_num_decimals", "_score_truncation_num_decimals", int, 0, PredefinedSerializer()),
  FieldMetadata("publicLeaderboardDisclaimerMessage", "public_leaderboard_disclaimer_message", "_public_leaderboard_disclaimer_message", str, "", PredefinedSerializer()),
  FieldMetadata("hasLeaderboard", "has_leaderboard", "_has_leaderboard", bool, False, PredefinedSerializer()),
  FieldMetadata("disableLeaderboardPrizeIndicator", "disable_leaderboard_prize_indicator", "_disable_leaderboard_prize_indicator", bool, False, PredefinedSerializer()),
  FieldMetadata("witholdFinalLeaderboardUntilItHasBeenVerified", "withold_final_leaderboard_until_it_has_been_verified", "_withold_final_leaderboard_until_it_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("finalLeaderboardHasBeenVerified", "final_leaderboard_has_been_verified", "_final_leaderboard_has_been_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("finalLeaderboardDisclaimerMessage", "final_leaderboard_disclaimer_message", "_final_leaderboard_disclaimer_message", str, "", PredefinedSerializer()),
  FieldMetadata("reward", "reward", "_reward", Reward, None, KaggleObjectSerializer()),
  FieldMetadata("numPrizes", "num_prizes", "_num_prizes", int, 0, PredefinedSerializer()),
  FieldMetadata("medalsAllowed", "medals_allowed", "_medals_allowed", bool, False, PredefinedSerializer()),
  FieldMetadata("userRankMultiplier", "user_rank_multiplier", "_user_rank_multiplier", float, 0.0, PredefinedSerializer()),
]

CreateCompetitionEmailInvitesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("emailsToAdd", "emails_to_add", "_emails_to_add", str, [], ListSerializer(PredefinedSerializer())),
]

CreateCompetitionEmailInvitesResponse._fields = [
  FieldMetadata("emailInvites", "email_invites", "_email_invites", CompetitionEmailInvite, [], ListSerializer(KaggleObjectSerializer())),
]

CreateCompetitionRequest._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("briefDescription", "brief_description", "_brief_description", str, "", PredefinedSerializer()),
  FieldMetadata("hostSegment", "host_segment", "_host_segment", HostSegment, HostSegment.HOST_SEGMENT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("privacy", "privacy", "_privacy", CompetitionPrivacy, CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("cloneCompetitionId", "clone_competition_id", "_clone_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableKernels", "disable_kernels", "_disable_kernels", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("restrictLinkToEmailList", "restrict_link_to_email_list", "_restrict_link_to_email_list", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("cloneExcludeCompetitionData", "clone_exclude_competition_data", "_clone_exclude_competition_data", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reward", "reward", "_reward", Reward, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("hackathon", "hackathon", "_hackathon", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("numPrizes", "num_prizes", "_num_prizes", int, None, PredefinedSerializer(), optional=True),
]

CreateCompetitionResponse._fields = [
  FieldMetadata("competition", "competition", "_competition", Competition, None, KaggleObjectSerializer()),
]

CreateCompetitionSampleSubmissionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("blobToken", "blob_token", "_blob_token", str, "", PredefinedSerializer()),
]

CreateCompetitionSolutionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("blobToken", "blob_token", "_blob_token", str, "", PredefinedSerializer()),
]

DeleteCompetitionEmailInviteRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("emailInviteId", "email_invite_id", "_email_invite_id", int, 0, PredefinedSerializer()),
]

DeleteCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

DeleteCompetitionResponse._fields = []

DeleteSolutionFilesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetCompetitionSimulationSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetDatabundleBasicInfoRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetPrivacySettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

LaunchCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("futureTime", "future_time", "_future_time", datetime, None, DateTimeSerializer()),
]

ListCompetitionEmailInvitesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListCompetitionEmailInvitesResponse._fields = [
  FieldMetadata("emailInvites", "email_invites", "_email_invites", CompetitionEmailInvite, [], ListSerializer(KaggleObjectSerializer())),
]

ListCompetitionLicensesRequest._fields = []

ListCompetitionLicensesResponse._fields = [
  FieldMetadata("licenses", "licenses", "_licenses", LicenseOption, [], ListSerializer(KaggleObjectSerializer())),
]

ListHostUsersRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListHostUsersResponse._fields = [
  FieldMetadata("hosts", "hosts", "_hosts", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
]

RegenerateShareTokenRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

RemoveHostUserRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hostUserId", "host_user_id", "_host_user_id", int, 0, PredefinedSerializer()),
]

SetCompetitionCitationAuthorsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("authors", "authors", "_authors", str, "", PredefinedSerializer()),
]

SetCompetitionMetricRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("evaluationAlgorithmId", "evaluation_algorithm_id", "_evaluation_algorithm_id", int, 0, PredefinedSerializer()),
]

SetCompetitionMetricResponse._fields = [
  FieldMetadata("metric", "metric", "_metric", EvaluationAlgorithm, None, KaggleObjectSerializer()),
  FieldMetadata("metricVersion", "metric_version", "_metric_version", CompetitionMetricVersion, None, KaggleObjectSerializer()),
]

SetEvaluationMetricParametersRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("nameValuePairs", "name_value_pairs", "_name_value_pairs", str, {}, MapSerializer(PredefinedSerializer())),
]

ToggleBenchmarkSubmissionRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
]

UpdateCompetitionSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", CompetitionSettings, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateCompetitionSettingsResponse._fields = [
  FieldMetadata("settings", "settings", "_settings", CompetitionSettings, None, KaggleObjectSerializer()),
]

UpdateCompetitionSimulationSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", CompetitionSimulationSettings, None, KaggleObjectSerializer()),
]

UpdateCurrentCompetitionMetricVersionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

UpdateCurrentCompetitionMetricVersionResponse._fields = [
  FieldMetadata("competitionMetricVersion", "competition_metric_version", "_competition_metric_version", CompetitionMetricVersion, None, KaggleObjectSerializer()),
  FieldMetadata("parameters", "parameters", "_parameters", EvaluationMetricParameter, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateImagesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("header", "header", "_header", CroppedImageUpload, None, KaggleObjectSerializer()),
  FieldMetadata("thumbnail", "thumbnail", "_thumbnail", CroppedImageUpload, None, KaggleObjectSerializer()),
]

UpdateImagesResponse._fields = [
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, None, PredefinedSerializer(), optional=True),
]

UpdateSandboxSubmissionNameRequest._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

UpdateTeamsVisibilityRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamIds", "team_ids", "_team_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("hide", "hide", "_hide", bool, False, PredefinedSerializer()),
]

