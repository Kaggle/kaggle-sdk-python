from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.competitions.types.competition import Competition
from kagglesdk.competitions.types.competition_enums import CompetitionDatabundleType
from kagglesdk.competitions.types.competition_types import DatabundleBasicInfo
from kagglesdk.competitions.types.competition_user import CompetitionUser
from kagglesdk.competitions.types.team import SubmissionLimitInfo, Team
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.progression_service import Medal
from typing import List, Optional, Dict

class CheckCompetitionsAccessRequest(KaggleObject):
  r"""
  Attributes:
    competition_ids (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._competition_ids = []
    self._read_mask = None
    self._freeze()

  @property
  def competition_ids(self) -> Optional[List[int]]:
    return self._competition_ids

  @competition_ids.setter
  def competition_ids(self, competition_ids: Optional[List[int]]):
    if competition_ids is None:
      del self.competition_ids
      return
    if not isinstance(competition_ids, list):
      raise TypeError('competition_ids must be of type list')
    if not all([isinstance(t, int) for t in competition_ids]):
      raise TypeError('competition_ids must contain only items of type int')
    self._competition_ids = competition_ids

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class CheckCompetitionsAccessResponse(KaggleObject):
  r"""
  Attributes:
    access (CompetitionAccess)
      Map from the competition ID to the access for the current user. The key set
      is guaranteed to contain all competition IDs from the request.
  """

  def __init__(self):
    self._access = {}
    self._freeze()

  @property
  def access(self) -> Optional[Dict[int, Optional['CompetitionAccess']]]:
    r"""
    Map from the competition ID to the access for the current user. The key set
    is guaranteed to contain all competition IDs from the request.
    """
    return self._access

  @access.setter
  def access(self, access: Optional[Dict[int, Optional['CompetitionAccess']]]):
    if access is None:
      del self.access
      return
    if not isinstance(access, dict):
      raise TypeError('access must be of type dict')
    if not all([isinstance(v, CompetitionAccess) for k, v in access]):
      raise TypeError('access must contain only items of type CompetitionAccess')
    self._access = access


class CompetitionAccess(KaggleObject):
  r"""
  Attributes:
    can_view (bool)
    has_accepted_rules (bool)
    can_update (bool)
    can_participate (bool)
  """

  def __init__(self):
    self._can_view = None
    self._has_accepted_rules = None
    self._can_update = None
    self._can_participate = None
    self._freeze()

  @property
  def can_view(self) -> bool:
    return self._can_view or False

  @can_view.setter
  def can_view(self, can_view: Optional[bool]):
    if can_view is None:
      del self.can_view
      return
    if not isinstance(can_view, bool):
      raise TypeError('can_view must be of type bool')
    self._can_view = can_view

  @property
  def has_accepted_rules(self) -> bool:
    return self._has_accepted_rules or False

  @has_accepted_rules.setter
  def has_accepted_rules(self, has_accepted_rules: Optional[bool]):
    if has_accepted_rules is None:
      del self.has_accepted_rules
      return
    if not isinstance(has_accepted_rules, bool):
      raise TypeError('has_accepted_rules must be of type bool')
    self._has_accepted_rules = has_accepted_rules

  @property
  def can_update(self) -> bool:
    return self._can_update or False

  @can_update.setter
  def can_update(self, can_update: Optional[bool]):
    if can_update is None:
      del self.can_update
      return
    if not isinstance(can_update, bool):
      raise TypeError('can_update must be of type bool')
    self._can_update = can_update

  @property
  def can_participate(self) -> bool:
    return self._can_participate or False

  @can_participate.setter
  def can_participate(self, can_participate: Optional[bool]):
    if can_participate is None:
      del self.can_participate
      return
    if not isinstance(can_participate, bool):
      raise TypeError('can_participate must be of type bool')
    self._can_participate = can_participate


class CompetitionCertificate(KaggleObject):
  r"""
  Attributes:
    user_display_name (str)
    user_id (int)
    medal (Medal)
    deadline (datetime)
    competition_id (int)
    competition_title (str)
    competition_name (str)
    rank (int)
    total_teams (int)
    image_url (str)
  """

  def __init__(self):
    self._user_display_name = ""
    self._user_id = 0
    self._medal = Medal.MEDAL_UNSPECIFIED
    self._deadline = None
    self._competition_id = 0
    self._competition_title = ""
    self._competition_name = ""
    self._rank = 0
    self._total_teams = 0
    self._image_url = ""
    self._freeze()

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

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def medal(self) -> 'Medal':
    return self._medal

  @medal.setter
  def medal(self, medal: 'Medal'):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

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
  def competition_title(self) -> str:
    return self._competition_title

  @competition_title.setter
  def competition_title(self, competition_title: str):
    if competition_title is None:
      del self.competition_title
      return
    if not isinstance(competition_title, str):
      raise TypeError('competition_title must be of type str')
    self._competition_title = competition_title

  @property
  def competition_name(self) -> str:
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
  def rank(self) -> int:
    return self._rank

  @rank.setter
  def rank(self, rank: int):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank

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
  def image_url(self) -> str:
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url


class DatabundleFileInfo(KaggleObject):
  r"""
  Attributes:
    info (DatabundleBasicInfo)
    synthetic_info (DatabundleBasicInfo)
      Generative template competitions have synthetic copies with different
      sizes and dimensions than the base competition.
  """

  def __init__(self):
    self._info = None
    self._synthetic_info = None
    self._freeze()

  @property
  def info(self) -> Optional['DatabundleBasicInfo']:
    return self._info

  @info.setter
  def info(self, info: Optional['DatabundleBasicInfo']):
    if info is None:
      del self.info
      return
    if not isinstance(info, DatabundleBasicInfo):
      raise TypeError('info must be of type DatabundleBasicInfo')
    self._info = info

  @property
  def synthetic_info(self) -> Optional['DatabundleBasicInfo']:
    r"""
    Generative template competitions have synthetic copies with different
    sizes and dimensions than the base competition.
    """
    return self._synthetic_info

  @synthetic_info.setter
  def synthetic_info(self, synthetic_info: Optional['DatabundleBasicInfo']):
    if synthetic_info is None:
      del self.synthetic_info
      return
    if not isinstance(synthetic_info, DatabundleBasicInfo):
      raise TypeError('synthetic_info must be of type DatabundleBasicInfo')
    self._synthetic_info = synthetic_info


class GetCompetitionCertificateRequest(KaggleObject):
  r"""
  This request uses user_name and competition_name instead of IDs since the
  certificate is accessed on the frontend via a URL that contains them.

  Attributes:
    user_name (str)
    competition_name (str)
  """

  def __init__(self):
    self._user_name = ""
    self._competition_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def competition_name(self) -> str:
    return self._competition_name

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name


class GetCompetitionCertificateUploadUrlRequest(KaggleObject):
  r"""
  Attributes:
    content_length (int)
    recipient_user_id (int)
    competition_id (int)
  """

  def __init__(self):
    self._content_length = 0
    self._recipient_user_id = 0
    self._competition_id = 0
    self._freeze()

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def recipient_user_id(self) -> int:
    return self._recipient_user_id

  @recipient_user_id.setter
  def recipient_user_id(self, recipient_user_id: int):
    if recipient_user_id is None:
      del self.recipient_user_id
      return
    if not isinstance(recipient_user_id, int):
      raise TypeError('recipient_user_id must be of type int')
    self._recipient_user_id = recipient_user_id

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


class GetCompetitionCertificateUploadUrlResponse(KaggleObject):
  r"""
  Attributes:
    upload_url (str)
  """

  def __init__(self):
    self._upload_url = ""
    self._freeze()

  @property
  def upload_url(self) -> str:
    return self._upload_url

  @upload_url.setter
  def upload_url(self, upload_url: str):
    if upload_url is None:
      del self.upload_url
      return
    if not isinstance(upload_url, str):
      raise TypeError('upload_url must be of type str')
    self._upload_url = upload_url


class GetCompetitionCitationRequest(KaggleObject):
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


class GetCompetitionCitationResponse(KaggleObject):
  r"""
  Attributes:
    bib_tex (str)
      For now, we only support Kaggle-generated BibTeX. Eventually we hope to
      support DOI.
    estimated_rendered_citation (str)
      Pseudo-APA style, single-line citation used as a preview on the UI.
      Attempt at emulating how LaTeX would render the BibTeX.
    citation_authors (str)
  """

  def __init__(self):
    self._bib_tex = ""
    self._estimated_rendered_citation = ""
    self._citation_authors = ""
    self._freeze()

  @property
  def bib_tex(self) -> str:
    r"""
    For now, we only support Kaggle-generated BibTeX. Eventually we hope to
    support DOI.
    """
    return self._bib_tex

  @bib_tex.setter
  def bib_tex(self, bib_tex: str):
    if bib_tex is None:
      del self.bib_tex
      return
    if not isinstance(bib_tex, str):
      raise TypeError('bib_tex must be of type str')
    self._bib_tex = bib_tex

  @property
  def estimated_rendered_citation(self) -> str:
    r"""
    Pseudo-APA style, single-line citation used as a preview on the UI.
    Attempt at emulating how LaTeX would render the BibTeX.
    """
    return self._estimated_rendered_citation

  @estimated_rendered_citation.setter
  def estimated_rendered_citation(self, estimated_rendered_citation: str):
    if estimated_rendered_citation is None:
      del self.estimated_rendered_citation
      return
    if not isinstance(estimated_rendered_citation, str):
      raise TypeError('estimated_rendered_citation must be of type str')
    self._estimated_rendered_citation = estimated_rendered_citation

  @property
  def citation_authors(self) -> str:
    return self._citation_authors

  @citation_authors.setter
  def citation_authors(self, citation_authors: str):
    if citation_authors is None:
      del self.citation_authors
      return
    if not isinstance(citation_authors, str):
      raise TypeError('citation_authors must be of type str')
    self._citation_authors = citation_authors


class GetCompetitionDatabundleVersionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_databundle_type (CompetitionDatabundleType)
  """

  def __init__(self):
    self._competition_id = 0
    self._competition_databundle_type = CompetitionDatabundleType.COMPETITION_DATABUNDLE_TYPE_UNSPECIFIED
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
  def competition_databundle_type(self) -> 'CompetitionDatabundleType':
    return self._competition_databundle_type

  @competition_databundle_type.setter
  def competition_databundle_type(self, competition_databundle_type: 'CompetitionDatabundleType'):
    if competition_databundle_type is None:
      del self.competition_databundle_type
      return
    if not isinstance(competition_databundle_type, CompetitionDatabundleType):
      raise TypeError('competition_databundle_type must be of type CompetitionDatabundleType')
    self._competition_databundle_type = competition_databundle_type


class GetCompetitionDatabundleVersionResponse(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id


class GetCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_name (str)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._competition_id = None
    self._competition_name = None
    self._read_mask = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.competition_name
    self._competition_id = competition_id

  @property
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: str):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    del self.competition_id
    self._competition_name = competition_name

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetProfileUserStatsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      user whose profile is being viewed
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """user whose profile is being viewed"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetProfileUserStatsResponse(KaggleObject):
  r"""
  Attributes:
    competitions_count (int)
      how many competitions has user_id participated in
    solo_competitions_count (int)
      how many competitions has user_id participated in without being in a team
    team_competitions_count (int)
      how many competitions has user_id participated in while in a team
  """

  def __init__(self):
    self._competitions_count = 0
    self._solo_competitions_count = 0
    self._team_competitions_count = 0
    self._freeze()

  @property
  def competitions_count(self) -> int:
    """how many competitions has user_id participated in"""
    return self._competitions_count

  @competitions_count.setter
  def competitions_count(self, competitions_count: int):
    if competitions_count is None:
      del self.competitions_count
      return
    if not isinstance(competitions_count, int):
      raise TypeError('competitions_count must be of type int')
    self._competitions_count = competitions_count

  @property
  def solo_competitions_count(self) -> int:
    """how many competitions has user_id participated in without being in a team"""
    return self._solo_competitions_count

  @solo_competitions_count.setter
  def solo_competitions_count(self, solo_competitions_count: int):
    if solo_competitions_count is None:
      del self.solo_competitions_count
      return
    if not isinstance(solo_competitions_count, int):
      raise TypeError('solo_competitions_count must be of type int')
    self._solo_competitions_count = solo_competitions_count

  @property
  def team_competitions_count(self) -> int:
    """how many competitions has user_id participated in while in a team"""
    return self._team_competitions_count

  @team_competitions_count.setter
  def team_competitions_count(self, team_competitions_count: int):
    if team_competitions_count is None:
      del self.team_competitions_count
      return
    if not isinstance(team_competitions_count, int):
      raise TypeError('team_competitions_count must be of type int')
    self._team_competitions_count = team_competitions_count


class HasCompetitionEmailInviteRequest(KaggleObject):
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


class HasCompetitionEmailInviteResponse(KaggleObject):
  r"""
  Attributes:
    has_email_invite (bool)
  """

  def __init__(self):
    self._has_email_invite = False
    self._freeze()

  @property
  def has_email_invite(self) -> bool:
    return self._has_email_invite

  @has_email_invite.setter
  def has_email_invite(self, has_email_invite: bool):
    if has_email_invite is None:
      del self.has_email_invite
      return
    if not isinstance(has_email_invite, bool):
      raise TypeError('has_email_invite must be of type bool')
    self._has_email_invite = has_email_invite


class ListCompetitionsRequest(KaggleObject):
  r"""
  Attributes:
    selector (ListCompetitionsRequest.Selector)
      Defines the query to perform.
    page_size (int)
      Max number of results to return.  Defaults to 1000 if unset.
    page_token (str)
      Enables retrieval of more data from the same query.  Should only be set
      to the `ListCompetitionsResponse.next_page_token` value returned by a
      previous ListCompetitions call with the exact same `selector` value.
      Otherwise should be set to '', indicating a fresh query.
    read_mask (FieldMask)
    model_id (int)
      If specified, lists competitions with public notebook submissions that
      have the indicated model attached.
      TODO(b/300139458): Ideally this would reside in the Selector, but nested
      IAM permission checks are currently disabled
  """

  class Selector(KaggleObject):
    r"""
    Defines the query parameters.

    Attributes:
      competition_ids (int)
        Returns competitions matching the provided ID's. If ID's are specified
        here, the below fields are not used.
      list_option (ListCompetitionsRequest.Selector.ListOption)
        Defines the type of competitions to be returned. Only has an effect if
        competition_ids is unset.
      list_for_user_id (int)
        If specified, lists relative to the given user, otherwise lists relative
        to calling user by default. Only allowed if list_option is USER_ENTERED
        or USER_HOSTED. Results will still be restricted and scrubbed relative to
        the calling user.
      host_segment_id_filter (int)
        Defines the category of competitions to be returned. This is temporarily
        an int32, but will eventually be migrated to an enum. The category values
        are:
        UNSPECIFIED = 0
        FEATURED = 1
        RESEARCH = 2
        RECRUITMENT = 3
        GETTING_STARTED = 5
        MASTERS = 6
        PLAYGROUND = 8
        COMMUNITY = 10
        Only has an effect if competition_ids is unset.
        If set, only take Comps with the given HostSegment.  If unset, and
        `list_option` is neither USER_ENTERED nor USER_HOSTED, we will ignore
        InClass competitions from the query.
        Using HostSegment directly is buggy (build-sdk fails), so just use the
        id for now.
        --)
      prestige_filter (ListCompetitionsRequest.Selector.PrestigeFilter)
        If provided, add a constraint for competitions with matching prestige.
      visibility_filter (ListCompetitionsRequest.Selector.VisibilityFilter)
        If provided, add a constraint for competitions' visibility status
      participation_filter (ListCompetitionsRequest.Selector.ParticipationFilter)
        If provided, add a constraint for competitions' participation status
      tag_ids (int)
        Foreign keys to Categories table. If provided, we only take Comps with
        matching CompetitionCategory entries.
      exclude_tag_ids (int)
        Foreign keys to Categories table. If provided, we exclude Comps with
        matching CompetitionCategory entries.
      sort_option (ListCompetitionsRequest.Selector.SortOption)
        Defines the order in which results should be returned. Only has an
        effect if competition_ids is unset.
      search_query (str)
        String search term. Only has an effect if competition_ids is unset.
      require_simulations (bool)
        If true, only return simulation competitions
        (Competition.CompetitionSimulationSettingsId != null)
      require_kernels (bool)
        If true, only return competitions with Notebooks enabled (HasScripts
        bit).
      require_hackathons (bool)
        If true, only return hackathon competitions
    """

    class ListOption(enum.Enum):
      """Predefined query types."""
      LIST_OPTION_DEFAULT = 0
      r"""
      Displays launched competitions.
      TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)
      """
      LIST_OPTION_USER_ENTERED = 1
      r"""
      Competitions that the current user has entered.
      team. --)
      """
      LIST_OPTION_USER_HOSTED = 2
      """Competitions that the current user is a host for."""
      LIST_OPTION_UNLAUNCHED = 3
      """Unlaunched competitions.  Must be admin to use this."""
      LIST_OPTION_ACTIVE = 4
      """Displays active competitions."""
      LIST_OPTION_COMPLETED = 5
      """Displays completed competitions"""
      LIST_OPTION_USER_YOUR_WORK = 6
      r"""
      Displays all competitions in the Current User's Your Work section.
      rules acceptances, and Leaderboard presence. --)
      """
      LIST_OPTION_USER_BOOKMARKED = 7
      """Displays bookmarked competitions"""
      LIST_OPTION_PUBLICLY_CLONEABLE = 8
      """Displays publicly cloneable competitions the user can clone"""
      LIST_OPTION_HAS_SYNTHETIC_COPIES = 9
      """Displays competitions that have synthetic copies."""
      LIST_OPTION_SPOTLIGHT_SHELF = 10
      """Displays spotlight community competitions"""
      LIST_OPTION_GETTING_STARTED_SHELF = 11
      """Displays getting-started competitions"""

    class ParticipationFilter(enum.Enum):
      PARTICIPATION_FILTER_UNSPECIFIED = 0
      """Does not add a constraint for visibility."""
      PARTICIPATION_FILTER_OPEN = 1
      """Only returns competitions that anyone is able to join."""
      PARTICIPATION_FILTER_LIMITED = 2
      """Only returns competitions with limited participation."""

    class PrestigeFilter(enum.Enum):
      """Optional filters for competition prestige type."""
      PRESTIGE_FILTER_UNSPECIFIED = 0
      """Does not add a constraint for prestige type."""
      PRESTIGE_FILTER_MONEY = 1
      """Only returns competitions with monetary prizes."""
      PRESTIGE_FILTER_MEDALS = 2
      """Only returns competitions which award medals."""
      PRESTIGE_FILTER_OTHER = 3
      """Only returns competitions which do not award money nor medals."""

    class SortOption(enum.Enum):
      """Predefined sort orders."""
      SORT_OPTION_DEFAULT = 0
      r"""
      Currently equal to NEWEST.
      TODO(aip.dev/126): (-- api-linter: core::0126::unspecified=disabled --)
      """
      SORT_OPTION_NEWEST = 1
      """Shows the newest competitions first."""
      SORT_OPTION_OLDEST = 2
      """Shows the oldest competitions first."""
      SORT_OPTION_REWARD = 3
      """Sorts by the competition's prize money."""
      SORT_OPTION_NUM_TEAMS = 4
      r"""
      Sorts by the number of teams.
      descending. --)
      """
      SORT_OPTION_RECENTLY_CLOSED = 5
      """Shows the recently closed competitions first."""

    class VisibilityFilter(enum.Enum):
      """Optional filters for competition visibility."""
      VISIBILITY_FILTER_UNSPECIFIED = 0
      """Does not add a constraint for visibility."""
      VISIBILITY_FILTER_PUBLIC = 1
      """Only returns publicly visible competitions (anonymous users can see)."""
      VISIBILITY_FILTER_PUBLIC_AND_PRIVATE_LEADERBOARD = 2
      r"""
      Only returns publicly visible competitions whose Private Leaderboard
      is also visible.
      """

    def __init__(self):
      self._competition_ids = []
      self._list_option = self.ListOption.LIST_OPTION_DEFAULT
      self._list_for_user_id = None
      self._host_segment_id_filter = 0
      self._prestige_filter = self.PrestigeFilter.PRESTIGE_FILTER_UNSPECIFIED
      self._visibility_filter = self.VisibilityFilter.VISIBILITY_FILTER_UNSPECIFIED
      self._participation_filter = self.ParticipationFilter.PARTICIPATION_FILTER_UNSPECIFIED
      self._tag_ids = []
      self._exclude_tag_ids = []
      self._sort_option = self.SortOption.SORT_OPTION_DEFAULT
      self._search_query = ""
      self._require_simulations = False
      self._require_kernels = False
      self._require_hackathons = False
      self._freeze()

    @property
    def competition_ids(self) -> Optional[List[int]]:
      r"""
      Returns competitions matching the provided ID's. If ID's are specified
      here, the below fields are not used.
      """
      return self._competition_ids

    @competition_ids.setter
    def competition_ids(self, competition_ids: Optional[List[int]]):
      if competition_ids is None:
        del self.competition_ids
        return
      if not isinstance(competition_ids, list):
        raise TypeError('competition_ids must be of type list')
      if not all([isinstance(t, int) for t in competition_ids]):
        raise TypeError('competition_ids must contain only items of type int')
      self._competition_ids = competition_ids

    @property
    def list_option(self) -> 'ListCompetitionsRequest.Selector.ListOption':
      r"""
      Defines the type of competitions to be returned. Only has an effect if
      competition_ids is unset.
      """
      return self._list_option

    @list_option.setter
    def list_option(self, list_option: 'ListCompetitionsRequest.Selector.ListOption'):
      if list_option is None:
        del self.list_option
        return
      if not isinstance(list_option, ListCompetitionsRequest.Selector.ListOption):
        raise TypeError('list_option must be of type ListCompetitionsRequest.Selector.ListOption')
      self._list_option = list_option

    @property
    def list_for_user_id(self) -> int:
      r"""
      If specified, lists relative to the given user, otherwise lists relative
      to calling user by default. Only allowed if list_option is USER_ENTERED
      or USER_HOSTED. Results will still be restricted and scrubbed relative to
      the calling user.
      """
      return self._list_for_user_id or 0

    @list_for_user_id.setter
    def list_for_user_id(self, list_for_user_id: Optional[int]):
      if list_for_user_id is None:
        del self.list_for_user_id
        return
      if not isinstance(list_for_user_id, int):
        raise TypeError('list_for_user_id must be of type int')
      self._list_for_user_id = list_for_user_id

    @property
    def host_segment_id_filter(self) -> int:
      r"""
      Defines the category of competitions to be returned. This is temporarily
      an int32, but will eventually be migrated to an enum. The category values
      are:
      UNSPECIFIED = 0
      FEATURED = 1
      RESEARCH = 2
      RECRUITMENT = 3
      GETTING_STARTED = 5
      MASTERS = 6
      PLAYGROUND = 8
      COMMUNITY = 10
      Only has an effect if competition_ids is unset.
      If set, only take Comps with the given HostSegment.  If unset, and
      `list_option` is neither USER_ENTERED nor USER_HOSTED, we will ignore
      InClass competitions from the query.
      Using HostSegment directly is buggy (build-sdk fails), so just use the
      id for now.
      --)
      """
      return self._host_segment_id_filter

    @host_segment_id_filter.setter
    def host_segment_id_filter(self, host_segment_id_filter: int):
      if host_segment_id_filter is None:
        del self.host_segment_id_filter
        return
      if not isinstance(host_segment_id_filter, int):
        raise TypeError('host_segment_id_filter must be of type int')
      self._host_segment_id_filter = host_segment_id_filter

    @property
    def prestige_filter(self) -> 'ListCompetitionsRequest.Selector.PrestigeFilter':
      """If provided, add a constraint for competitions with matching prestige."""
      return self._prestige_filter

    @prestige_filter.setter
    def prestige_filter(self, prestige_filter: 'ListCompetitionsRequest.Selector.PrestigeFilter'):
      if prestige_filter is None:
        del self.prestige_filter
        return
      if not isinstance(prestige_filter, ListCompetitionsRequest.Selector.PrestigeFilter):
        raise TypeError('prestige_filter must be of type ListCompetitionsRequest.Selector.PrestigeFilter')
      self._prestige_filter = prestige_filter

    @property
    def visibility_filter(self) -> 'ListCompetitionsRequest.Selector.VisibilityFilter':
      """If provided, add a constraint for competitions' visibility status"""
      return self._visibility_filter

    @visibility_filter.setter
    def visibility_filter(self, visibility_filter: 'ListCompetitionsRequest.Selector.VisibilityFilter'):
      if visibility_filter is None:
        del self.visibility_filter
        return
      if not isinstance(visibility_filter, ListCompetitionsRequest.Selector.VisibilityFilter):
        raise TypeError('visibility_filter must be of type ListCompetitionsRequest.Selector.VisibilityFilter')
      self._visibility_filter = visibility_filter

    @property
    def participation_filter(self) -> 'ListCompetitionsRequest.Selector.ParticipationFilter':
      """If provided, add a constraint for competitions' participation status"""
      return self._participation_filter

    @participation_filter.setter
    def participation_filter(self, participation_filter: 'ListCompetitionsRequest.Selector.ParticipationFilter'):
      if participation_filter is None:
        del self.participation_filter
        return
      if not isinstance(participation_filter, ListCompetitionsRequest.Selector.ParticipationFilter):
        raise TypeError('participation_filter must be of type ListCompetitionsRequest.Selector.ParticipationFilter')
      self._participation_filter = participation_filter

    @property
    def tag_ids(self) -> Optional[List[int]]:
      r"""
      Foreign keys to Categories table. If provided, we only take Comps with
      matching CompetitionCategory entries.
      """
      return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids: Optional[List[int]]):
      if tag_ids is None:
        del self.tag_ids
        return
      if not isinstance(tag_ids, list):
        raise TypeError('tag_ids must be of type list')
      if not all([isinstance(t, int) for t in tag_ids]):
        raise TypeError('tag_ids must contain only items of type int')
      self._tag_ids = tag_ids

    @property
    def exclude_tag_ids(self) -> Optional[List[int]]:
      r"""
      Foreign keys to Categories table. If provided, we exclude Comps with
      matching CompetitionCategory entries.
      """
      return self._exclude_tag_ids

    @exclude_tag_ids.setter
    def exclude_tag_ids(self, exclude_tag_ids: Optional[List[int]]):
      if exclude_tag_ids is None:
        del self.exclude_tag_ids
        return
      if not isinstance(exclude_tag_ids, list):
        raise TypeError('exclude_tag_ids must be of type list')
      if not all([isinstance(t, int) for t in exclude_tag_ids]):
        raise TypeError('exclude_tag_ids must contain only items of type int')
      self._exclude_tag_ids = exclude_tag_ids

    @property
    def sort_option(self) -> 'ListCompetitionsRequest.Selector.SortOption':
      r"""
      Defines the order in which results should be returned. Only has an
      effect if competition_ids is unset.
      """
      return self._sort_option

    @sort_option.setter
    def sort_option(self, sort_option: 'ListCompetitionsRequest.Selector.SortOption'):
      if sort_option is None:
        del self.sort_option
        return
      if not isinstance(sort_option, ListCompetitionsRequest.Selector.SortOption):
        raise TypeError('sort_option must be of type ListCompetitionsRequest.Selector.SortOption')
      self._sort_option = sort_option

    @property
    def search_query(self) -> str:
      """String search term. Only has an effect if competition_ids is unset."""
      return self._search_query

    @search_query.setter
    def search_query(self, search_query: str):
      if search_query is None:
        del self.search_query
        return
      if not isinstance(search_query, str):
        raise TypeError('search_query must be of type str')
      self._search_query = search_query

    @property
    def require_simulations(self) -> bool:
      r"""
      If true, only return simulation competitions
      (Competition.CompetitionSimulationSettingsId != null)
      """
      return self._require_simulations

    @require_simulations.setter
    def require_simulations(self, require_simulations: bool):
      if require_simulations is None:
        del self.require_simulations
        return
      if not isinstance(require_simulations, bool):
        raise TypeError('require_simulations must be of type bool')
      self._require_simulations = require_simulations

    @property
    def require_kernels(self) -> bool:
      r"""
      If true, only return competitions with Notebooks enabled (HasScripts
      bit).
      """
      return self._require_kernels

    @require_kernels.setter
    def require_kernels(self, require_kernels: bool):
      if require_kernels is None:
        del self.require_kernels
        return
      if not isinstance(require_kernels, bool):
        raise TypeError('require_kernels must be of type bool')
      self._require_kernels = require_kernels

    @property
    def require_hackathons(self) -> bool:
      """If true, only return hackathon competitions"""
      return self._require_hackathons

    @require_hackathons.setter
    def require_hackathons(self, require_hackathons: bool):
      if require_hackathons is None:
        del self.require_hackathons
        return
      if not isinstance(require_hackathons, bool):
        raise TypeError('require_hackathons must be of type bool')
      self._require_hackathons = require_hackathons


  def __init__(self):
    self._selector = None
    self._page_size = 0
    self._page_token = ""
    self._read_mask = None
    self._model_id = None
    self._freeze()

  @property
  def selector(self) -> Optional['ListCompetitionsRequest.Selector']:
    """Defines the query to perform."""
    return self._selector

  @selector.setter
  def selector(self, selector: Optional['ListCompetitionsRequest.Selector']):
    if selector is None:
      del self.selector
      return
    if not isinstance(selector, ListCompetitionsRequest.Selector):
      raise TypeError('selector must be of type ListCompetitionsRequest.Selector')
    self._selector = selector

  @property
  def page_size(self) -> int:
    """Max number of results to return.  Defaults to 1000 if unset."""
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
    to the `ListCompetitionsResponse.next_page_token` value returned by a
    previous ListCompetitions call with the exact same `selector` value.
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

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask

  @property
  def model_id(self) -> int:
    r"""
    If specified, lists competitions with public notebook submissions that
    have the indicated model attached.
    TODO(b/300139458): Ideally this would reside in the Selector, but nested
    IAM permission checks are currently disabled
    """
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: Optional[int]):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id


class ListCompetitionsResponse(KaggleObject):
  r"""
  Lists the requests competitions as well as the user's teams in those
  competitions.
  (-- api-linter: core::0132::response-unknown-fields=disabled --)

  Attributes:
    competitions (Competition)
      The results of the listing.
    user_teams (Team)
      The current user's active team for each of the returned competitions, if it
      exists. Order is unspecified, but can be matched with team.competition_id.
    team_submission_limit_infos (SubmissionLimitInfo)
      Maps each teamId from user_teams to its submission limit data.
      Only populated if list_for_user_id is unset or set to current user, for
      privacy reasons.
    team_ranks (int)
      Maps each teamId from user_teams to its current primary Rank, if it has
      one. Primary Rank will be from Private LB if competition is closed and
      private LB is publicly available, otherwise Public.
    next_page_token (str)
      Enables retrieval of more data from the same query.  See the `page_token`
      field from `ListCompetitionsRequest` above.  If the value is '', it means
      no further results for the request.
    total_results (int)
      Used for pagination or otherwise displaying how many results are in a
      filtered collection before pageSize and page are applied
    thumbnail_image_urls (str)
      Signed thumbnail image URLs for the competitions returned on the response.
      Generated in bulk for performance.
    header_image_urls (str)
      Signed header image URLs for the competitions returned on the response.
      Generated in bulk for performance.
    competition_users (CompetitionUser)
      Maps each competitionId from competitions to the current user's context on
      that competition
      TODO(b/307284127): Migrate above team info to the CompetitionUser message
    databundle_file_infos (DatabundleFileInfo)
      Basic info about files contained in the databundle for the competitions
      returned on the response. Only supported for
      LIST_OPTION_HAS_SYNTHETIC_COPIES and LIST_OPTION_PUBLICLY_CLONEABLE
  """

  def __init__(self):
    self._competitions = []
    self._user_teams = []
    self._team_submission_limit_infos = {}
    self._team_ranks = {}
    self._next_page_token = ""
    self._total_results = 0
    self._thumbnail_image_urls = {}
    self._header_image_urls = {}
    self._competition_users = {}
    self._databundle_file_infos = {}
    self._freeze()

  @property
  def competitions(self) -> Optional[List[Optional['Competition']]]:
    """The results of the listing."""
    return self._competitions

  @competitions.setter
  def competitions(self, competitions: Optional[List[Optional['Competition']]]):
    if competitions is None:
      del self.competitions
      return
    if not isinstance(competitions, list):
      raise TypeError('competitions must be of type list')
    if not all([isinstance(t, Competition) for t in competitions]):
      raise TypeError('competitions must contain only items of type Competition')
    self._competitions = competitions

  @property
  def user_teams(self) -> Optional[List[Optional['Team']]]:
    r"""
    The current user's active team for each of the returned competitions, if it
    exists. Order is unspecified, but can be matched with team.competition_id.
    """
    return self._user_teams

  @user_teams.setter
  def user_teams(self, user_teams: Optional[List[Optional['Team']]]):
    if user_teams is None:
      del self.user_teams
      return
    if not isinstance(user_teams, list):
      raise TypeError('user_teams must be of type list')
    if not all([isinstance(t, Team) for t in user_teams]):
      raise TypeError('user_teams must contain only items of type Team')
    self._user_teams = user_teams

  @property
  def team_submission_limit_infos(self) -> Optional[Dict[int, Optional['SubmissionLimitInfo']]]:
    r"""
    Maps each teamId from user_teams to its submission limit data.
    Only populated if list_for_user_id is unset or set to current user, for
    privacy reasons.
    """
    return self._team_submission_limit_infos

  @team_submission_limit_infos.setter
  def team_submission_limit_infos(self, team_submission_limit_infos: Optional[Dict[int, Optional['SubmissionLimitInfo']]]):
    if team_submission_limit_infos is None:
      del self.team_submission_limit_infos
      return
    if not isinstance(team_submission_limit_infos, dict):
      raise TypeError('team_submission_limit_infos must be of type dict')
    if not all([isinstance(v, SubmissionLimitInfo) for k, v in team_submission_limit_infos]):
      raise TypeError('team_submission_limit_infos must contain only items of type SubmissionLimitInfo')
    self._team_submission_limit_infos = team_submission_limit_infos

  @property
  def team_ranks(self) -> Optional[Dict[int, int]]:
    r"""
    Maps each teamId from user_teams to its current primary Rank, if it has
    one. Primary Rank will be from Private LB if competition is closed and
    private LB is publicly available, otherwise Public.
    """
    return self._team_ranks

  @team_ranks.setter
  def team_ranks(self, team_ranks: Optional[Dict[int, int]]):
    if team_ranks is None:
      del self.team_ranks
      return
    if not isinstance(team_ranks, dict):
      raise TypeError('team_ranks must be of type dict')
    if not all([isinstance(v, int) for k, v in team_ranks]):
      raise TypeError('team_ranks must contain only items of type int')
    self._team_ranks = team_ranks

  @property
  def competition_users(self) -> Optional[Dict[int, Optional['CompetitionUser']]]:
    r"""
    Maps each competitionId from competitions to the current user's context on
    that competition
    TODO(b/307284127): Migrate above team info to the CompetitionUser message
    """
    return self._competition_users

  @competition_users.setter
  def competition_users(self, competition_users: Optional[Dict[int, Optional['CompetitionUser']]]):
    if competition_users is None:
      del self.competition_users
      return
    if not isinstance(competition_users, dict):
      raise TypeError('competition_users must be of type dict')
    if not all([isinstance(v, CompetitionUser) for k, v in competition_users]):
      raise TypeError('competition_users must contain only items of type CompetitionUser')
    self._competition_users = competition_users

  @property
  def next_page_token(self) -> str:
    r"""
    Enables retrieval of more data from the same query.  See the `page_token`
    field from `ListCompetitionsRequest` above.  If the value is '', it means
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
  def total_results(self) -> int:
    r"""
    Used for pagination or otherwise displaying how many results are in a
    filtered collection before pageSize and page are applied
    """
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results

  @property
  def thumbnail_image_urls(self) -> Optional[Dict[int, str]]:
    r"""
    Signed thumbnail image URLs for the competitions returned on the response.
    Generated in bulk for performance.
    """
    return self._thumbnail_image_urls

  @thumbnail_image_urls.setter
  def thumbnail_image_urls(self, thumbnail_image_urls: Optional[Dict[int, str]]):
    if thumbnail_image_urls is None:
      del self.thumbnail_image_urls
      return
    if not isinstance(thumbnail_image_urls, dict):
      raise TypeError('thumbnail_image_urls must be of type dict')
    if not all([isinstance(v, str) for k, v in thumbnail_image_urls]):
      raise TypeError('thumbnail_image_urls must contain only items of type str')
    self._thumbnail_image_urls = thumbnail_image_urls

  @property
  def header_image_urls(self) -> Optional[Dict[int, str]]:
    r"""
    Signed header image URLs for the competitions returned on the response.
    Generated in bulk for performance.
    """
    return self._header_image_urls

  @header_image_urls.setter
  def header_image_urls(self, header_image_urls: Optional[Dict[int, str]]):
    if header_image_urls is None:
      del self.header_image_urls
      return
    if not isinstance(header_image_urls, dict):
      raise TypeError('header_image_urls must be of type dict')
    if not all([isinstance(v, str) for k, v in header_image_urls]):
      raise TypeError('header_image_urls must contain only items of type str')
    self._header_image_urls = header_image_urls

  @property
  def databundle_file_infos(self) -> Optional[Dict[int, Optional['DatabundleFileInfo']]]:
    r"""
    Basic info about files contained in the databundle for the competitions
    returned on the response. Only supported for
    LIST_OPTION_HAS_SYNTHETIC_COPIES and LIST_OPTION_PUBLICLY_CLONEABLE
    """
    return self._databundle_file_infos

  @databundle_file_infos.setter
  def databundle_file_infos(self, databundle_file_infos: Optional[Dict[int, Optional['DatabundleFileInfo']]]):
    if databundle_file_infos is None:
      del self.databundle_file_infos
      return
    if not isinstance(databundle_file_infos, dict):
      raise TypeError('databundle_file_infos must be of type dict')
    if not all([isinstance(v, DatabundleFileInfo) for k, v in databundle_file_infos]):
      raise TypeError('databundle_file_infos must contain only items of type DatabundleFileInfo')
    self._databundle_file_infos = databundle_file_infos


class PromptWriteUpsRequest(KaggleObject):
  r"""
  Attributes:
    user_prompt (str)
    system_prompt (str)
    competition_id (int)
  """

  def __init__(self):
    self._user_prompt = ""
    self._system_prompt = None
    self._competition_id = None
    self._freeze()

  @property
  def user_prompt(self) -> str:
    return self._user_prompt

  @user_prompt.setter
  def user_prompt(self, user_prompt: str):
    if user_prompt is None:
      del self.user_prompt
      return
    if not isinstance(user_prompt, str):
      raise TypeError('user_prompt must be of type str')
    self._user_prompt = user_prompt

  @property
  def system_prompt(self) -> str:
    return self._system_prompt or ""

  @system_prompt.setter
  def system_prompt(self, system_prompt: Optional[str]):
    if system_prompt is None:
      del self.system_prompt
      return
    if not isinstance(system_prompt, str):
      raise TypeError('system_prompt must be of type str')
    self._system_prompt = system_prompt

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class PromptWriteUpsResponse(KaggleObject):
  r"""
  Attributes:
    generated_response (str)
  """

  def __init__(self):
    self._generated_response = ""
    self._freeze()

  @property
  def generated_response(self) -> str:
    return self._generated_response

  @generated_response.setter
  def generated_response(self, generated_response: str):
    if generated_response is None:
      del self.generated_response
      return
    if not isinstance(generated_response, str):
      raise TypeError('generated_response must be of type str')
    self._generated_response = generated_response


CheckCompetitionsAccessRequest._fields = [
  FieldMetadata("competitionIds", "competition_ids", "_competition_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

CheckCompetitionsAccessResponse._fields = [
  FieldMetadata("access", "access", "_access", CompetitionAccess, {}, MapSerializer(KaggleObjectSerializer())),
]

CompetitionAccess._fields = [
  FieldMetadata("canView", "can_view", "_can_view", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasAcceptedRules", "has_accepted_rules", "_has_accepted_rules", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canUpdate", "can_update", "_can_update", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canParticipate", "can_participate", "_can_participate", bool, None, PredefinedSerializer(), optional=True),
]

CompetitionCertificate._fields = [
  FieldMetadata("userDisplayName", "user_display_name", "_user_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("medal", "medal", "_medal", Medal, Medal.MEDAL_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("deadline", "deadline", "_deadline", datetime, None, DateTimeSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionTitle", "competition_title", "_competition_title", str, "", PredefinedSerializer()),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("rank", "rank", "_rank", int, 0, PredefinedSerializer()),
  FieldMetadata("totalTeams", "total_teams", "_total_teams", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
]

DatabundleFileInfo._fields = [
  FieldMetadata("info", "info", "_info", DatabundleBasicInfo, None, KaggleObjectSerializer()),
  FieldMetadata("syntheticInfo", "synthetic_info", "_synthetic_info", DatabundleBasicInfo, None, KaggleObjectSerializer()),
]

GetCompetitionCertificateRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
]

GetCompetitionCertificateUploadUrlRequest._fields = [
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("recipientUserId", "recipient_user_id", "_recipient_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetCompetitionCertificateUploadUrlResponse._fields = [
  FieldMetadata("uploadUrl", "upload_url", "_upload_url", str, "", PredefinedSerializer()),
]

GetCompetitionCitationRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetCompetitionCitationResponse._fields = [
  FieldMetadata("bibTex", "bib_tex", "_bib_tex", str, "", PredefinedSerializer()),
  FieldMetadata("estimatedRenderedCitation", "estimated_rendered_citation", "_estimated_rendered_citation", str, "", PredefinedSerializer()),
  FieldMetadata("citationAuthors", "citation_authors", "_citation_authors", str, "", PredefinedSerializer()),
]

GetCompetitionDatabundleVersionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionDatabundleType", "competition_databundle_type", "_competition_databundle_type", CompetitionDatabundleType, CompetitionDatabundleType.COMPETITION_DATABUNDLE_TYPE_UNSPECIFIED, EnumSerializer()),
]

GetCompetitionDatabundleVersionResponse._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
]

GetCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetProfileUserStatsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetProfileUserStatsResponse._fields = [
  FieldMetadata("competitionsCount", "competitions_count", "_competitions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("soloCompetitionsCount", "solo_competitions_count", "_solo_competitions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("teamCompetitionsCount", "team_competitions_count", "_team_competitions_count", int, 0, PredefinedSerializer()),
]

HasCompetitionEmailInviteRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

HasCompetitionEmailInviteResponse._fields = [
  FieldMetadata("hasEmailInvite", "has_email_invite", "_has_email_invite", bool, False, PredefinedSerializer()),
]

ListCompetitionsRequest.Selector._fields = [
  FieldMetadata("competitionIds", "competition_ids", "_competition_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("listOption", "list_option", "_list_option", ListCompetitionsRequest.Selector.ListOption, ListCompetitionsRequest.Selector.ListOption.LIST_OPTION_DEFAULT, EnumSerializer()),
  FieldMetadata("listForUserId", "list_for_user_id", "_list_for_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hostSegmentIdFilter", "host_segment_id_filter", "_host_segment_id_filter", int, 0, PredefinedSerializer()),
  FieldMetadata("prestigeFilter", "prestige_filter", "_prestige_filter", ListCompetitionsRequest.Selector.PrestigeFilter, ListCompetitionsRequest.Selector.PrestigeFilter.PRESTIGE_FILTER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("visibilityFilter", "visibility_filter", "_visibility_filter", ListCompetitionsRequest.Selector.VisibilityFilter, ListCompetitionsRequest.Selector.VisibilityFilter.VISIBILITY_FILTER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("participationFilter", "participation_filter", "_participation_filter", ListCompetitionsRequest.Selector.ParticipationFilter, ListCompetitionsRequest.Selector.ParticipationFilter.PARTICIPATION_FILTER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("excludeTagIds", "exclude_tag_ids", "_exclude_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("sortOption", "sort_option", "_sort_option", ListCompetitionsRequest.Selector.SortOption, ListCompetitionsRequest.Selector.SortOption.SORT_OPTION_DEFAULT, EnumSerializer()),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, "", PredefinedSerializer()),
  FieldMetadata("requireSimulations", "require_simulations", "_require_simulations", bool, False, PredefinedSerializer()),
  FieldMetadata("requireKernels", "require_kernels", "_require_kernels", bool, False, PredefinedSerializer()),
  FieldMetadata("requireHackathons", "require_hackathons", "_require_hackathons", bool, False, PredefinedSerializer()),
]

ListCompetitionsRequest._fields = [
  FieldMetadata("selector", "selector", "_selector", ListCompetitionsRequest.Selector, None, KaggleObjectSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

ListCompetitionsResponse._fields = [
  FieldMetadata("competitions", "competitions", "_competitions", Competition, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("userTeams", "user_teams", "_user_teams", Team, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("teamSubmissionLimitInfos", "team_submission_limit_infos", "_team_submission_limit_infos", SubmissionLimitInfo, {}, MapSerializer(KaggleObjectSerializer())),
  FieldMetadata("teamRanks", "team_ranks", "_team_ranks", int, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrls", "thumbnail_image_urls", "_thumbnail_image_urls", str, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("headerImageUrls", "header_image_urls", "_header_image_urls", str, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("competitionUsers", "competition_users", "_competition_users", CompetitionUser, {}, MapSerializer(KaggleObjectSerializer())),
  FieldMetadata("databundleFileInfos", "databundle_file_infos", "_databundle_file_infos", DatabundleFileInfo, {}, MapSerializer(KaggleObjectSerializer())),
]

PromptWriteUpsRequest._fields = [
  FieldMetadata("userPrompt", "user_prompt", "_user_prompt", str, "", PredefinedSerializer()),
  FieldMetadata("systemPrompt", "system_prompt", "_system_prompt", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
]

PromptWriteUpsResponse._fields = [
  FieldMetadata("generatedResponse", "generated_response", "_generated_response", str, "", PredefinedSerializer()),
]

