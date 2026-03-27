from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.competitions.types.hackathons import CompetitionHackathonSettings, HackathonSlugIdentifier, HackathonTrack, HackathonWriteUp
from kagglesdk.discussions.types.writeups_service import CreateWriteUpRequest, UpdateWriteUpRequest
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class AddJudgeRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    user_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._user_id = 0
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


class AssignPrizeRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    hackathon_track_prize_id (int)
    hackathon_write_up_id (int)
      if unset, removes any assigned write up to that prize
  """

  def __init__(self):
    self._competition_id = 0
    self._hackathon_track_prize_id = 0
    self._hackathon_write_up_id = None
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
  def hackathon_track_prize_id(self) -> int:
    return self._hackathon_track_prize_id

  @hackathon_track_prize_id.setter
  def hackathon_track_prize_id(self, hackathon_track_prize_id: int):
    if hackathon_track_prize_id is None:
      del self.hackathon_track_prize_id
      return
    if not isinstance(hackathon_track_prize_id, int):
      raise TypeError('hackathon_track_prize_id must be of type int')
    self._hackathon_track_prize_id = hackathon_track_prize_id

  @property
  def hackathon_write_up_id(self) -> int:
    """if unset, removes any assigned write up to that prize"""
    return self._hackathon_write_up_id or 0

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: Optional[int]):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    self._hackathon_write_up_id = hackathon_write_up_id


class CheckHackathonWriteupConflictRequest(KaggleObject):
  r"""
  Attributes:
    hackathon_write_up_id (int)
    current_time (datetime)
  """

  def __init__(self):
    self._hackathon_write_up_id = 0
    self._current_time = None
    self._freeze()

  @property
  def hackathon_write_up_id(self) -> int:
    return self._hackathon_write_up_id

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: int):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    self._hackathon_write_up_id = hackathon_write_up_id

  @property
  def current_time(self) -> datetime:
    return self._current_time

  @current_time.setter
  def current_time(self, current_time: datetime):
    if current_time is None:
      del self.current_time
      return
    if not isinstance(current_time, datetime):
      raise TypeError('current_time must be of type datetime')
    self._current_time = current_time


class CheckHackathonWriteupConflictResponse(KaggleObject):
  r"""
  Attributes:
    is_conflict (bool)
    time_until_deadline_seconds (int)
    is_deleted (bool)
  """

  def __init__(self):
    self._is_conflict = False
    self._time_until_deadline_seconds = 0
    self._is_deleted = False
    self._freeze()

  @property
  def is_conflict(self) -> bool:
    return self._is_conflict

  @is_conflict.setter
  def is_conflict(self, is_conflict: bool):
    if is_conflict is None:
      del self.is_conflict
      return
    if not isinstance(is_conflict, bool):
      raise TypeError('is_conflict must be of type bool')
    self._is_conflict = is_conflict

  @property
  def time_until_deadline_seconds(self) -> int:
    return self._time_until_deadline_seconds

  @time_until_deadline_seconds.setter
  def time_until_deadline_seconds(self, time_until_deadline_seconds: int):
    if time_until_deadline_seconds is None:
      del self.time_until_deadline_seconds
      return
    if not isinstance(time_until_deadline_seconds, int):
      raise TypeError('time_until_deadline_seconds must be of type int')
    self._time_until_deadline_seconds = time_until_deadline_seconds

  @property
  def is_deleted(self) -> bool:
    return self._is_deleted

  @is_deleted.setter
  def is_deleted(self, is_deleted: bool):
    if is_deleted is None:
      del self.is_deleted
      return
    if not isinstance(is_deleted, bool):
      raise TypeError('is_deleted must be of type bool')
    self._is_deleted = is_deleted


class CreateHackathonWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    team_id (int)
    create_write_up_request (CreateWriteUpRequest)
    hackathon_track_ids (int)
    competition_id (int)
  """

  def __init__(self):
    self._team_id = None
    self._create_write_up_request = None
    self._hackathon_track_ids = []
    self._competition_id = 0
    self._freeze()

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
  def create_write_up_request(self) -> Optional['CreateWriteUpRequest']:
    return self._create_write_up_request

  @create_write_up_request.setter
  def create_write_up_request(self, create_write_up_request: Optional['CreateWriteUpRequest']):
    if create_write_up_request is None:
      del self.create_write_up_request
      return
    if not isinstance(create_write_up_request, CreateWriteUpRequest):
      raise TypeError('create_write_up_request must be of type CreateWriteUpRequest')
    self._create_write_up_request = create_write_up_request

  @property
  def hackathon_track_ids(self) -> Optional[List[int]]:
    return self._hackathon_track_ids

  @hackathon_track_ids.setter
  def hackathon_track_ids(self, hackathon_track_ids: Optional[List[int]]):
    if hackathon_track_ids is None:
      del self.hackathon_track_ids
      return
    if not isinstance(hackathon_track_ids, list):
      raise TypeError('hackathon_track_ids must be of type list')
    if not all([isinstance(t, int) for t in hackathon_track_ids]):
      raise TypeError('hackathon_track_ids must contain only items of type int')
    self._hackathon_track_ids = hackathon_track_ids

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


class DeleteHackathonWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    hackathon_write_up_id (int)
  """

  def __init__(self):
    self._hackathon_write_up_id = None
    self._freeze()

  @property
  def hackathon_write_up_id(self) -> int:
    return self._hackathon_write_up_id or 0

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: int):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    self._hackathon_write_up_id = hackathon_write_up_id


class FinalizeHackathonPrizesRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      TODO(b/442008536): Add a hackathon specific update winner checker.
  """

  def __init__(self):
    self._competition_id = 0
    self._freeze()

  @property
  def competition_id(self) -> int:
    """TODO(b/442008536): Add a hackathon specific update winner checker."""
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id


class GetCompetitionHackathonSettingsRequest(KaggleObject):
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


class GetHackathonDeadlineTimeRequest(KaggleObject):
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


class GetHackathonDeadlineTimeResponse(KaggleObject):
  r"""
  Attributes:
    time_until_deadline_seconds (int)
  """

  def __init__(self):
    self._time_until_deadline_seconds = 0
    self._freeze()

  @property
  def time_until_deadline_seconds(self) -> int:
    return self._time_until_deadline_seconds

  @time_until_deadline_seconds.setter
  def time_until_deadline_seconds(self, time_until_deadline_seconds: int):
    if time_until_deadline_seconds is None:
      del self.time_until_deadline_seconds
      return
    if not isinstance(time_until_deadline_seconds, int):
      raise TypeError('time_until_deadline_seconds must be of type int')
    self._time_until_deadline_seconds = time_until_deadline_seconds


class GetHackathonWriteupChecklistRequest(KaggleObject):
  r"""
  Attributes:
    hackathon_write_up_id (int)
  """

  def __init__(self):
    self._hackathon_write_up_id = 0
    self._freeze()

  @property
  def hackathon_write_up_id(self) -> int:
    return self._hackathon_write_up_id

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: int):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    self._hackathon_write_up_id = hackathon_write_up_id


class GetHackathonWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    hackathon_write_up_id (int)
    hackathon_slug_identifier (HackathonSlugIdentifier)
  """

  def __init__(self):
    self._hackathon_write_up_id = None
    self._hackathon_slug_identifier = None
    self._freeze()

  @property
  def hackathon_write_up_id(self) -> int:
    return self._hackathon_write_up_id or 0

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: int):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    del self.hackathon_slug_identifier
    self._hackathon_write_up_id = hackathon_write_up_id

  @property
  def hackathon_slug_identifier(self) -> Optional['HackathonSlugIdentifier']:
    return self._hackathon_slug_identifier or None

  @hackathon_slug_identifier.setter
  def hackathon_slug_identifier(self, hackathon_slug_identifier: Optional['HackathonSlugIdentifier']):
    if hackathon_slug_identifier is None:
      del self.hackathon_slug_identifier
      return
    if not isinstance(hackathon_slug_identifier, HackathonSlugIdentifier):
      raise TypeError('hackathon_slug_identifier must be of type HackathonSlugIdentifier')
    del self.hackathon_write_up_id
    self._hackathon_slug_identifier = hackathon_slug_identifier


class HackathonWriteupChecklist(KaggleObject):
  r"""
  Attributes:
    children (HackathonWriteupChecklistItem)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['HackathonWriteupChecklistItem']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['HackathonWriteupChecklistItem']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, HackathonWriteupChecklistItem) for t in children]):
      raise TypeError('children must contain only items of type HackathonWriteupChecklistItem')
    self._children = children


class HackathonWriteupChecklistItem(KaggleObject):
  r"""
  Attributes:
    type (HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType)
    completed (bool)
  """

  class HackathonWriteupChecklistItemType(enum.Enum):
    CHECKLIST_ITEM_TYPE_UNSPECIFIED = 0
    HAS_TRACK = 1
    HAS_TITLE = 2
    HAS_SUBTITLE = 3
    HAS_VIDEO = 4
    HAS_IMAGE = 5
    HAS_DESCRIPTION = 6
    HAS_LINK = 7
    HAS_FILE = 8
    HAS_THUMBNAIL_AND_CARD_IMAGE = 9

  def __init__(self):
    self._type = self.selfType.CHECKLIST_ITEM_TYPE_UNSPECIFIED
    self._completed = False
    self._freeze()

  @property
  def type(self) -> 'HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType':
    return self._type

  @type.setter
  def type(self, type: 'HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType):
      raise TypeError('type must be of type HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType')
    self._type = type

  @property
  def completed(self) -> bool:
    return self._completed

  @completed.setter
  def completed(self, completed: bool):
    if completed is None:
      del self.completed
      return
    if not isinstance(completed, bool):
      raise TypeError('completed must be of type bool')
    self._completed = completed


class JudgeUserInfo(KaggleObject):
  r"""
  Attributes:
    user_avatar (UserAvatar)
    occupation (str)
    organization (str)
  """

  def __init__(self):
    self._user_avatar = None
    self._occupation = None
    self._organization = None
    self._freeze()

  @property
  def user_avatar(self) -> Optional['UserAvatar']:
    return self._user_avatar

  @user_avatar.setter
  def user_avatar(self, user_avatar: Optional['UserAvatar']):
    if user_avatar is None:
      del self.user_avatar
      return
    if not isinstance(user_avatar, UserAvatar):
      raise TypeError('user_avatar must be of type UserAvatar')
    self._user_avatar = user_avatar

  @property
  def occupation(self) -> str:
    return self._occupation or ""

  @occupation.setter
  def occupation(self, occupation: Optional[str]):
    if occupation is None:
      del self.occupation
      return
    if not isinstance(occupation, str):
      raise TypeError('occupation must be of type str')
    self._occupation = occupation

  @property
  def organization(self) -> str:
    return self._organization or ""

  @organization.setter
  def organization(self, organization: Optional[str]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, str):
      raise TypeError('organization must be of type str')
    self._organization = organization


class ListHackathonTracksRequest(KaggleObject):
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


class ListHackathonTracksResponse(KaggleObject):
  r"""
  Attributes:
    tracks (HackathonTrack)
  """

  def __init__(self):
    self._tracks = []
    self._freeze()

  @property
  def tracks(self) -> Optional[List[Optional['HackathonTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['HackathonTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, HackathonTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type HackathonTrack')
    self._tracks = tracks


class ListHackathonWriteUpsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    team_id (int)
      optionally filter responses to this team id
    hackathon_track_ids (int)
      optionally filter responses to these track ids
    published (bool)
      if requesting for your team, you can request to include drafts
      unset = draft/publish, false = draft, true = published
    winner (bool)
      unset = winners/non-winners false = no winners, true = winners
    template (bool)
      unset = template & non-template, false = no templates, true = templates
    page_size (int)
    page_token (str)
    skip (int)
    read_mask (FieldMask)
    host_or_judge (bool)
      optionally filter responses to those owned by hosts or judges
  """

  def __init__(self):
    self._competition_id = 0
    self._team_id = None
    self._hackathon_track_ids = []
    self._published = None
    self._winner = None
    self._template = None
    self._page_size = None
    self._page_token = None
    self._skip = None
    self._read_mask = None
    self._host_or_judge = None
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
  def team_id(self) -> int:
    """optionally filter responses to this team id"""
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
  def host_or_judge(self) -> bool:
    """optionally filter responses to those owned by hosts or judges"""
    return self._host_or_judge or False

  @host_or_judge.setter
  def host_or_judge(self, host_or_judge: Optional[bool]):
    if host_or_judge is None:
      del self.host_or_judge
      return
    if not isinstance(host_or_judge, bool):
      raise TypeError('host_or_judge must be of type bool')
    self._host_or_judge = host_or_judge

  @property
  def hackathon_track_ids(self) -> Optional[List[int]]:
    """optionally filter responses to these track ids"""
    return self._hackathon_track_ids

  @hackathon_track_ids.setter
  def hackathon_track_ids(self, hackathon_track_ids: Optional[List[int]]):
    if hackathon_track_ids is None:
      del self.hackathon_track_ids
      return
    if not isinstance(hackathon_track_ids, list):
      raise TypeError('hackathon_track_ids must be of type list')
    if not all([isinstance(t, int) for t in hackathon_track_ids]):
      raise TypeError('hackathon_track_ids must contain only items of type int')
    self._hackathon_track_ids = hackathon_track_ids

  @property
  def published(self) -> bool:
    r"""
    if requesting for your team, you can request to include drafts
    unset = draft/publish, false = draft, true = published
    """
    return self._published or False

  @published.setter
  def published(self, published: Optional[bool]):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def winner(self) -> bool:
    """unset = winners/non-winners false = no winners, true = winners"""
    return self._winner or False

  @winner.setter
  def winner(self, winner: Optional[bool]):
    if winner is None:
      del self.winner
      return
    if not isinstance(winner, bool):
      raise TypeError('winner must be of type bool')
    self._winner = winner

  @property
  def template(self) -> bool:
    """unset = template & non-template, false = no templates, true = templates"""
    return self._template or False

  @template.setter
  def template(self, template: Optional[bool]):
    if template is None:
      del self.template
      return
    if not isinstance(template, bool):
      raise TypeError('template must be of type bool')
    self._template = template

  @property
  def page_size(self) -> int:
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

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


class ListHackathonWriteUpsResponse(KaggleObject):
  r"""
  Attributes:
    hackathon_write_ups (HackathonWriteUp)
    next_page_token (str)
    total_count (int)
  """

  def __init__(self):
    self._hackathon_write_ups = []
    self._next_page_token = ""
    self._total_count = 0
    self._freeze()

  @property
  def hackathon_write_ups(self) -> Optional[List[Optional['HackathonWriteUp']]]:
    return self._hackathon_write_ups

  @hackathon_write_ups.setter
  def hackathon_write_ups(self, hackathon_write_ups: Optional[List[Optional['HackathonWriteUp']]]):
    if hackathon_write_ups is None:
      del self.hackathon_write_ups
      return
    if not isinstance(hackathon_write_ups, list):
      raise TypeError('hackathon_write_ups must be of type list')
    if not all([isinstance(t, HackathonWriteUp) for t in hackathon_write_ups]):
      raise TypeError('hackathon_write_ups must contain only items of type HackathonWriteUp')
    self._hackathon_write_ups = hackathon_write_ups

  @property
  def next_page_token(self) -> str:
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
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count


class ListJudgesRequest(KaggleObject):
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


class ListJudgesResponse(KaggleObject):
  r"""
  Attributes:
    judges (JudgeUserInfo)
  """

  def __init__(self):
    self._judges = []
    self._freeze()

  @property
  def judges(self) -> Optional[List[Optional['JudgeUserInfo']]]:
    return self._judges

  @judges.setter
  def judges(self, judges: Optional[List[Optional['JudgeUserInfo']]]):
    if judges is None:
      del self.judges
      return
    if not isinstance(judges, list):
      raise TypeError('judges must be of type list')
    if not all([isinstance(t, JudgeUserInfo) for t in judges]):
      raise TypeError('judges must contain only items of type JudgeUserInfo')
    self._judges = judges


class RemoveJudgeRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    user_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._user_id = 0
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


class UpdateCompetitionHackathonSettingsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    settings (CompetitionHackathonSettings)
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
  def settings(self) -> Optional['CompetitionHackathonSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['CompetitionHackathonSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, CompetitionHackathonSettings):
      raise TypeError('settings must be of type CompetitionHackathonSettings')
    self._settings = settings


class UpdateHackathonTracksRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    tracks (HackathonTrack)
  """

  def __init__(self):
    self._competition_id = 0
    self._tracks = []
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
  def tracks(self) -> Optional[List[Optional['HackathonTrack']]]:
    return self._tracks

  @tracks.setter
  def tracks(self, tracks: Optional[List[Optional['HackathonTrack']]]):
    if tracks is None:
      del self.tracks
      return
    if not isinstance(tracks, list):
      raise TypeError('tracks must be of type list')
    if not all([isinstance(t, HackathonTrack) for t in tracks]):
      raise TypeError('tracks must contain only items of type HackathonTrack')
    self._tracks = tracks


class UpdateHackathonWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    hackathon_write_up_id (int)
    update_write_up_request (UpdateWriteUpRequest)
      if included will update the write up
    hackathon_track_ids (int)
      always required, updates the track ids
    template (bool)
      always required, if the write up should be a template
  """

  def __init__(self):
    self._hackathon_write_up_id = 0
    self._update_write_up_request = None
    self._hackathon_track_ids = []
    self._template = False
    self._freeze()

  @property
  def hackathon_write_up_id(self) -> int:
    return self._hackathon_write_up_id

  @hackathon_write_up_id.setter
  def hackathon_write_up_id(self, hackathon_write_up_id: int):
    if hackathon_write_up_id is None:
      del self.hackathon_write_up_id
      return
    if not isinstance(hackathon_write_up_id, int):
      raise TypeError('hackathon_write_up_id must be of type int')
    self._hackathon_write_up_id = hackathon_write_up_id

  @property
  def update_write_up_request(self) -> Optional['UpdateWriteUpRequest']:
    """if included will update the write up"""
    return self._update_write_up_request or None

  @update_write_up_request.setter
  def update_write_up_request(self, update_write_up_request: Optional[Optional['UpdateWriteUpRequest']]):
    if update_write_up_request is None:
      del self.update_write_up_request
      return
    if not isinstance(update_write_up_request, UpdateWriteUpRequest):
      raise TypeError('update_write_up_request must be of type UpdateWriteUpRequest')
    self._update_write_up_request = update_write_up_request

  @property
  def hackathon_track_ids(self) -> Optional[List[int]]:
    """always required, updates the track ids"""
    return self._hackathon_track_ids

  @hackathon_track_ids.setter
  def hackathon_track_ids(self, hackathon_track_ids: Optional[List[int]]):
    if hackathon_track_ids is None:
      del self.hackathon_track_ids
      return
    if not isinstance(hackathon_track_ids, list):
      raise TypeError('hackathon_track_ids must be of type list')
    if not all([isinstance(t, int) for t in hackathon_track_ids]):
      raise TypeError('hackathon_track_ids must contain only items of type int')
    self._hackathon_track_ids = hackathon_track_ids

  @property
  def template(self) -> bool:
    """always required, if the write up should be a template"""
    return self._template

  @template.setter
  def template(self, template: bool):
    if template is None:
      del self.template
      return
    if not isinstance(template, bool):
      raise TypeError('template must be of type bool')
    self._template = template


AddJudgeRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

AssignPrizeRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hackathonTrackPrizeId", "hackathon_track_prize_id", "_hackathon_track_prize_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, None, PredefinedSerializer(), optional=True),
]

CheckHackathonWriteupConflictRequest._fields = [
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentTime", "current_time", "_current_time", datetime, None, DateTimeSerializer()),
]

CheckHackathonWriteupConflictResponse._fields = [
  FieldMetadata("isConflict", "is_conflict", "_is_conflict", bool, False, PredefinedSerializer()),
  FieldMetadata("timeUntilDeadlineSeconds", "time_until_deadline_seconds", "_time_until_deadline_seconds", int, 0, PredefinedSerializer()),
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
]

CreateHackathonWriteUpRequest._fields = [
  FieldMetadata("teamId", "team_id", "_team_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createWriteUpRequest", "create_write_up_request", "_create_write_up_request", CreateWriteUpRequest, None, KaggleObjectSerializer()),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

DeleteHackathonWriteUpRequest._fields = [
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, None, PredefinedSerializer(), optional=True),
]

FinalizeHackathonPrizesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetCompetitionHackathonSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetHackathonDeadlineTimeRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

GetHackathonDeadlineTimeResponse._fields = [
  FieldMetadata("timeUntilDeadlineSeconds", "time_until_deadline_seconds", "_time_until_deadline_seconds", int, 0, PredefinedSerializer()),
]

GetHackathonWriteupChecklistRequest._fields = [
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, 0, PredefinedSerializer()),
]

GetHackathonWriteUpRequest._fields = [
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hackathonSlugIdentifier", "hackathon_slug_identifier", "_hackathon_slug_identifier", HackathonSlugIdentifier, None, KaggleObjectSerializer(), optional=True),
]

HackathonWriteupChecklist._fields = [
  FieldMetadata("children", "children", "_children", HackathonWriteupChecklistItem, [], ListSerializer(KaggleObjectSerializer())),
]

HackathonWriteupChecklistItem._fields = [
  FieldMetadata("type", "type", "_type", HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType, HackathonWriteupChecklistItem.HackathonWriteupChecklistItemType.CHECKLIST_ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("completed", "completed", "_completed", bool, False, PredefinedSerializer()),
]

JudgeUserInfo._fields = [
  FieldMetadata("userAvatar", "user_avatar", "_user_avatar", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("occupation", "occupation", "_occupation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", str, None, PredefinedSerializer(), optional=True),
]

ListHackathonTracksRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListHackathonTracksResponse._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", HackathonTrack, [], ListSerializer(KaggleObjectSerializer())),
]

ListHackathonWriteUpsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("teamId", "team_id", "_team_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("published", "published", "_published", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("winner", "winner", "_winner", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("template", "template", "_template", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("hostOrJudge", "host_or_judge", "_host_or_judge", bool, None, PredefinedSerializer(), optional=True),
]

ListHackathonWriteUpsResponse._fields = [
  FieldMetadata("hackathonWriteUps", "hackathon_write_ups", "_hackathon_write_ups", HackathonWriteUp, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

ListJudgesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListJudgesResponse._fields = [
  FieldMetadata("judges", "judges", "_judges", JudgeUserInfo, [], ListSerializer(KaggleObjectSerializer())),
]

RemoveJudgeRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UpdateCompetitionHackathonSettingsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", CompetitionHackathonSettings, None, KaggleObjectSerializer()),
]

UpdateHackathonTracksRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tracks", "tracks", "_tracks", HackathonTrack, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateHackathonWriteUpRequest._fields = [
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, 0, PredefinedSerializer()),
  FieldMetadata("updateWriteUpRequest", "update_write_up_request", "_update_write_up_request", UpdateWriteUpRequest, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("template", "template", "_template", bool, False, PredefinedSerializer()),
]

