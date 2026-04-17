from kagglesdk.competitions.types.hackathons import HackathonTrack, HackathonWriteUp
from kagglesdk.kaggle_object import *
from typing import List, Optional

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

  def endpoint(self):
    path = '/api/v1/competitions/{competition_id}/hackathon-tracks'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_id}/hackathon-tracks'


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

  @property
  def hackathonWriteUps(self):
    return self.hackathon_write_ups

  @property
  def nextPageToken(self):
    return self.next_page_token

  @property
  def totalCount(self):
    return self.total_count


ListHackathonTracksRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
]

ListHackathonTracksResponse._fields = [
  FieldMetadata("tracks", "tracks", "_tracks", HackathonTrack, [], ListSerializer(KaggleObjectSerializer())),
]

ListHackathonWriteUpsResponse._fields = [
  FieldMetadata("hackathonWriteUps", "hackathon_write_ups", "_hackathon_write_ups", HackathonWriteUp, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

