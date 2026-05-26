from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.competitions.types.hackathons import HackathonTrack, HackathonWriteUp
from kagglesdk.competitions.types.page import Page
from kagglesdk.kaggle_object import *
from typing import Optional, List

class ApiExportHackathonWriteUpsCsvRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_name (str)
  """

  def __init__(self):
    self._competition_id = None
    self._competition_name = None
    self._freeze()

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

  @property
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: Optional[str]):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/hackathon-write-ups-csv'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/hackathon-write-ups-csv'


class ApiExportHackathonWriteUpsCsvResponse(KaggleObject):
  r"""
  Attributes:
    csv_content (str)
  """

  def __init__(self):
    self._csv_content = ""
    self._freeze()

  @property
  def csv_content(self) -> str:
    return self._csv_content

  @csv_content.setter
  def csv_content(self, csv_content: str):
    if csv_content is None:
      del self.csv_content
      return
    if not isinstance(csv_content, str):
      raise TypeError('csv_content must be of type str')
    self._csv_content = csv_content

  @property
  def csvContent(self):
    return self.csv_content


class ApiGetHackathonOverviewRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._freeze()

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

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/hackathon-overview'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/hackathon-overview'


class ApiGetHackathonOverviewResponse(KaggleObject):
  r"""
  Attributes:
    pages (Page)
  """

  def __init__(self):
    self._pages = []
    self._freeze()

  @property
  def pages(self) -> Optional[List[Optional['Page']]]:
    return self._pages

  @pages.setter
  def pages(self, pages: Optional[List[Optional['Page']]]):
    if pages is None:
      del self.pages
      return
    if not isinstance(pages, list):
      raise TypeError('pages must be of type list')
    if not all([isinstance(t, Page) for t in pages]):
      raise TypeError('pages must contain only items of type Page')
    self._pages = pages


class ApiGetHackathonWriteUpRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
    hackathon_write_up_id (int)
  """

  def __init__(self):
    self._competition_name = ""
    self._hackathon_write_up_id = 0
    self._freeze()

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

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/hackathon-write-ups/{hackathon_write_up_id}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/hackathon-write-ups/{hackathon_write_up_id}'


class ApiListHackathonTracksRequest(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._freeze()

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

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/hackathon-tracks'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/hackathon-tracks'


class ApiListHackathonTracksResponse(KaggleObject):
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


class ApiListHackathonWriteUpsRequest(KaggleObject):
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
    competition_name (str)
  """

  def __init__(self):
    self._competition_id = None
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
    self._competition_name = None
    self._freeze()

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
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: Optional[str]):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/hackathon-write-ups'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/hackathon-write-ups'


class ApiListHackathonWriteUpsResponse(KaggleObject):
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

  @property
  def hackathonWriteUps(self):
    return self.hackathon_write_ups

  @property
  def nextPageToken(self):
    return self.next_page_token

  @property
  def totalCount(self):
    return self.total_count


ApiExportHackathonWriteUpsCsvRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
]

ApiExportHackathonWriteUpsCsvResponse._fields = [
  FieldMetadata("csvContent", "csv_content", "_csv_content", str, "", PredefinedSerializer()),
]

ApiGetHackathonOverviewRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
]

ApiGetHackathonOverviewResponse._fields = [
  FieldMetadata("pages", "pages", "_pages", Page, [], ListSerializer(KaggleObjectSerializer())),
]

ApiGetHackathonWriteUpRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("hackathonWriteUpId", "hackathon_write_up_id", "_hackathon_write_up_id", int, 0, PredefinedSerializer()),
]

ApiListHackathonTracksRequest._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
]

ApiListHackathonTracksResponse._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", HackathonTrack, [], ListSerializer(KaggleObjectSerializer())),
]

ApiListHackathonWriteUpsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
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
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
]

ApiListHackathonWriteUpsResponse._fields = [
  FieldMetadata("hackathonWriteUps", "hackathon_write_ups", "_hackathon_write_ups", HackathonWriteUp, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

