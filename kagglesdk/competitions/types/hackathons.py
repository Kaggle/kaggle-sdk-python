from kagglesdk.competitions.types.competition_enums import HackathonTrackPrizeType
from kagglesdk.competitions.types.team import Team
from kagglesdk.discussions.types.writeup_types import WriteUp
from kagglesdk.kaggle_object import *
from typing import List, Optional

class CompetitionHackathonSettings(KaggleObject):
  r"""
  Attributes:
    allow_multiple_submissions (bool)
    allow_multiple_tracks (bool)
    require_video (bool)
    require_images (bool)
    require_links (bool)
    require_uploads (bool)
    project_description (str)
    forum_announced (bool)
  """

  def __init__(self):
    self._allow_multiple_submissions = False
    self._allow_multiple_tracks = False
    self._require_video = False
    self._require_images = False
    self._require_links = False
    self._require_uploads = False
    self._project_description = ""
    self._forum_announced = False
    self._freeze()

  @property
  def allow_multiple_submissions(self) -> bool:
    return self._allow_multiple_submissions

  @allow_multiple_submissions.setter
  def allow_multiple_submissions(self, allow_multiple_submissions: bool):
    if allow_multiple_submissions is None:
      del self.allow_multiple_submissions
      return
    if not isinstance(allow_multiple_submissions, bool):
      raise TypeError('allow_multiple_submissions must be of type bool')
    self._allow_multiple_submissions = allow_multiple_submissions

  @property
  def allow_multiple_tracks(self) -> bool:
    return self._allow_multiple_tracks

  @allow_multiple_tracks.setter
  def allow_multiple_tracks(self, allow_multiple_tracks: bool):
    if allow_multiple_tracks is None:
      del self.allow_multiple_tracks
      return
    if not isinstance(allow_multiple_tracks, bool):
      raise TypeError('allow_multiple_tracks must be of type bool')
    self._allow_multiple_tracks = allow_multiple_tracks

  @property
  def require_video(self) -> bool:
    return self._require_video

  @require_video.setter
  def require_video(self, require_video: bool):
    if require_video is None:
      del self.require_video
      return
    if not isinstance(require_video, bool):
      raise TypeError('require_video must be of type bool')
    self._require_video = require_video

  @property
  def require_images(self) -> bool:
    return self._require_images

  @require_images.setter
  def require_images(self, require_images: bool):
    if require_images is None:
      del self.require_images
      return
    if not isinstance(require_images, bool):
      raise TypeError('require_images must be of type bool')
    self._require_images = require_images

  @property
  def require_links(self) -> bool:
    return self._require_links

  @require_links.setter
  def require_links(self, require_links: bool):
    if require_links is None:
      del self.require_links
      return
    if not isinstance(require_links, bool):
      raise TypeError('require_links must be of type bool')
    self._require_links = require_links

  @property
  def require_uploads(self) -> bool:
    return self._require_uploads

  @require_uploads.setter
  def require_uploads(self, require_uploads: bool):
    if require_uploads is None:
      del self.require_uploads
      return
    if not isinstance(require_uploads, bool):
      raise TypeError('require_uploads must be of type bool')
    self._require_uploads = require_uploads

  @property
  def project_description(self) -> str:
    return self._project_description

  @project_description.setter
  def project_description(self, project_description: str):
    if project_description is None:
      del self.project_description
      return
    if not isinstance(project_description, str):
      raise TypeError('project_description must be of type str')
    self._project_description = project_description

  @property
  def forum_announced(self) -> bool:
    return self._forum_announced

  @forum_announced.setter
  def forum_announced(self, forum_announced: bool):
    if forum_announced is None:
      del self.forum_announced
      return
    if not isinstance(forum_announced, bool):
      raise TypeError('forum_announced must be of type bool')
    self._forum_announced = forum_announced


class HackathonSlugIdentifier(KaggleObject):
  r"""
  Attributes:
    competition_name (str)
    hackathon_write_up_slug (str)
  """

  def __init__(self):
    self._competition_name = ""
    self._hackathon_write_up_slug = ""
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
  def hackathon_write_up_slug(self) -> str:
    return self._hackathon_write_up_slug

  @hackathon_write_up_slug.setter
  def hackathon_write_up_slug(self, hackathon_write_up_slug: str):
    if hackathon_write_up_slug is None:
      del self.hackathon_write_up_slug
      return
    if not isinstance(hackathon_write_up_slug, str):
      raise TypeError('hackathon_write_up_slug must be of type str')
    self._hackathon_write_up_slug = hackathon_write_up_slug


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
    winning_hackathon_write_up (HackathonWriteUp)
  """

  def __init__(self):
    self._id = 0
    self._title = ""
    self._type = HackathonTrackPrizeType.HACKATHON_TRACK_PRIZE_TYPE_UNSPECIFIED
    self._amount_usd = 0
    self._description = ""
    self._order_index = 0.0
    self._winning_hackathon_write_up = None
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

  @property
  def winning_hackathon_write_up(self) -> Optional['HackathonWriteUp']:
    return self._winning_hackathon_write_up

  @winning_hackathon_write_up.setter
  def winning_hackathon_write_up(self, winning_hackathon_write_up: Optional['HackathonWriteUp']):
    if winning_hackathon_write_up is None:
      del self.winning_hackathon_write_up
      return
    if not isinstance(winning_hackathon_write_up, HackathonWriteUp):
      raise TypeError('winning_hackathon_write_up must be of type HackathonWriteUp')
    self._winning_hackathon_write_up = winning_hackathon_write_up


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


CompetitionHackathonSettings._fields = [
  FieldMetadata("allowMultipleSubmissions", "allow_multiple_submissions", "_allow_multiple_submissions", bool, False, PredefinedSerializer()),
  FieldMetadata("allowMultipleTracks", "allow_multiple_tracks", "_allow_multiple_tracks", bool, False, PredefinedSerializer()),
  FieldMetadata("requireVideo", "require_video", "_require_video", bool, False, PredefinedSerializer()),
  FieldMetadata("requireImages", "require_images", "_require_images", bool, False, PredefinedSerializer()),
  FieldMetadata("requireLinks", "require_links", "_require_links", bool, False, PredefinedSerializer()),
  FieldMetadata("requireUploads", "require_uploads", "_require_uploads", bool, False, PredefinedSerializer()),
  FieldMetadata("projectDescription", "project_description", "_project_description", str, "", PredefinedSerializer()),
  FieldMetadata("forumAnnounced", "forum_announced", "_forum_announced", bool, False, PredefinedSerializer()),
]

HackathonSlugIdentifier._fields = [
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, "", PredefinedSerializer()),
  FieldMetadata("hackathonWriteUpSlug", "hackathon_write_up_slug", "_hackathon_write_up_slug", str, "", PredefinedSerializer()),
]

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
  FieldMetadata("winningHackathonWriteUp", "winning_hackathon_write_up", "_winning_hackathon_write_up", HackathonWriteUp, None, KaggleObjectSerializer()),
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

