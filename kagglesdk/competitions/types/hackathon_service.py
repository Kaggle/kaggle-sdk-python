from kagglesdk.competitions.types.hackathons import HackathonWriteUp
from kagglesdk.kaggle_object import *
from typing import List, Optional

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


ListHackathonWriteUpsResponse._fields = [
  FieldMetadata("hackathonWriteUps", "hackathon_write_ups", "_hackathon_write_ups", HackathonWriteUp, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

