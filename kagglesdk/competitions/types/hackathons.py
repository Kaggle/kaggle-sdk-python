from kagglesdk.competitions.types.competition_enums import HackathonTrackPrizeType
from kagglesdk.competitions.types.team import Team
from kagglesdk.discussions.types.writeup_types import WriteUp
from kagglesdk.kaggle_object import *
from typing import Optional, List

class HackathonTrack(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
    description (str)
    prizes (HackathonTrackPrize)
    order_index (float)
  """

  def __init__(self):
    self._id = 0
    self._title = ""
    self._description = ""
    self._prizes = []
    self._order_index = 0.0
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
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def prizes(self) -> Optional[List[Optional['HackathonTrackPrize']]]:
    return self._prizes

  @prizes.setter
  def prizes(self, prizes: Optional[List[Optional['HackathonTrackPrize']]]):
    if prizes is None:
      del self.prizes
      return
    if not isinstance(prizes, list):
      raise TypeError('prizes must be of type list')
    if not all([isinstance(t, HackathonTrackPrize) for t in prizes]):
      raise TypeError('prizes must contain only items of type HackathonTrackPrize')
    self._prizes = prizes

  @property
  def order_index(self) -> float:
    return self._order_index

  @order_index.setter
  def order_index(self, order_index: float):
    if order_index is None:
      del self.order_index
      return
    if not isinstance(order_index, float):
      raise TypeError('order_index must be of type float')
    self._order_index = order_index


class HackathonTrackPrize(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
    type (HackathonTrackPrizeType)
    amount_usd (int)
    description (str)
    order_index (float)
  """

  def __init__(self):
    self._id = 0
    self._title = ""
    self._type = HackathonTrackPrizeType.HACKATHON_TRACK_PRIZE_TYPE_UNSPECIFIED
    self._amount_usd = 0
    self._description = ""
    self._order_index = 0.0
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
  def type(self) -> 'HackathonTrackPrizeType':
    return self._type

  @type.setter
  def type(self, type: 'HackathonTrackPrizeType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HackathonTrackPrizeType):
      raise TypeError('type must be of type HackathonTrackPrizeType')
    self._type = type

  @property
  def amount_usd(self) -> int:
    return self._amount_usd

  @amount_usd.setter
  def amount_usd(self, amount_usd: int):
    if amount_usd is None:
      del self.amount_usd
      return
    if not isinstance(amount_usd, int):
      raise TypeError('amount_usd must be of type int')
    self._amount_usd = amount_usd

  @property
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def order_index(self) -> float:
    return self._order_index

  @order_index.setter
  def order_index(self, order_index: float):
    if order_index is None:
      del self.order_index
      return
    if not isinstance(order_index, float):
      raise TypeError('order_index must be of type float')
    self._order_index = order_index


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


HackathonTrack._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("prizes", "prizes", "_prizes", HackathonTrackPrize, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("orderIndex", "order_index", "_order_index", float, 0.0, PredefinedSerializer()),
]

HackathonTrackPrize._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", HackathonTrackPrizeType, HackathonTrackPrizeType.HACKATHON_TRACK_PRIZE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("amountUsd", "amount_usd", "_amount_usd", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("orderIndex", "order_index", "_order_index", float, 0.0, PredefinedSerializer()),
]

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

