from kagglesdk.competitions.types.team import Team
from kagglesdk.discussions.types.writeup_types import WriteUp
from kagglesdk.kaggle_object import *
from typing import Optional, List

class HackathonWriteUp(KaggleObject):
  r"""
  Attributes:
    id (int)
    team (Team)
    write_up (WriteUp)
    template (bool)
    hackathon_track_ids (int)
    awarded_hackathon_track_prize_ids (int)
    competition_id (int)
    owner_host_user_id (int)
    owner_judge_user_id (int)
  """

  def __init__(self):
    self._id = 0
    self._team = None
    self._write_up = None
    self._template = False
    self._hackathon_track_ids = []
    self._awarded_hackathon_track_prize_ids = []
    self._competition_id = 0
    self._owner_host_user_id = None
    self._owner_judge_user_id = None
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
  def team(self) -> Optional['Team']:
    return self._team or None

  @team.setter
  def team(self, team: Optional[Optional['Team']]):
    if team is None:
      del self.team
      return
    if not isinstance(team, Team):
      raise TypeError('team must be of type Team')
    self._team = team

  @property
  def write_up(self) -> Optional['WriteUp']:
    return self._write_up

  @write_up.setter
  def write_up(self, write_up: Optional['WriteUp']):
    if write_up is None:
      del self.write_up
      return
    if not isinstance(write_up, WriteUp):
      raise TypeError('write_up must be of type WriteUp')
    self._write_up = write_up

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
  def awarded_hackathon_track_prize_ids(self) -> Optional[List[int]]:
    return self._awarded_hackathon_track_prize_ids

  @awarded_hackathon_track_prize_ids.setter
  def awarded_hackathon_track_prize_ids(self, awarded_hackathon_track_prize_ids: Optional[List[int]]):
    if awarded_hackathon_track_prize_ids is None:
      del self.awarded_hackathon_track_prize_ids
      return
    if not isinstance(awarded_hackathon_track_prize_ids, list):
      raise TypeError('awarded_hackathon_track_prize_ids must be of type list')
    if not all([isinstance(t, int) for t in awarded_hackathon_track_prize_ids]):
      raise TypeError('awarded_hackathon_track_prize_ids must contain only items of type int')
    self._awarded_hackathon_track_prize_ids = awarded_hackathon_track_prize_ids

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
  def owner_host_user_id(self) -> int:
    return self._owner_host_user_id or 0

  @owner_host_user_id.setter
  def owner_host_user_id(self, owner_host_user_id: Optional[int]):
    if owner_host_user_id is None:
      del self.owner_host_user_id
      return
    if not isinstance(owner_host_user_id, int):
      raise TypeError('owner_host_user_id must be of type int')
    self._owner_host_user_id = owner_host_user_id

  @property
  def owner_judge_user_id(self) -> int:
    return self._owner_judge_user_id or 0

  @owner_judge_user_id.setter
  def owner_judge_user_id(self, owner_judge_user_id: Optional[int]):
    if owner_judge_user_id is None:
      del self.owner_judge_user_id
      return
    if not isinstance(owner_judge_user_id, int):
      raise TypeError('owner_judge_user_id must be of type int')
    self._owner_judge_user_id = owner_judge_user_id


HackathonWriteUp._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("team", "team", "_team", Team, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("writeUp", "write_up", "_write_up", WriteUp, None, KaggleObjectSerializer()),
  FieldMetadata("template", "template", "_template", bool, False, PredefinedSerializer()),
  FieldMetadata("hackathonTrackIds", "hackathon_track_ids", "_hackathon_track_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("awardedHackathonTrackPrizeIds", "awarded_hackathon_track_prize_ids", "_awarded_hackathon_track_prize_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("ownerHostUserId", "owner_host_user_id", "_owner_host_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerJudgeUserId", "owner_judge_user_id", "_owner_judge_user_id", int, None, PredefinedSerializer(), optional=True),
]

