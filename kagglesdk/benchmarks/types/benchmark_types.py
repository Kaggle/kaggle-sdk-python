from datetime import datetime
import enum
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkLeaderboardDisplayType, BenchmarkMaintenanceLevel, BenchmarkMediaType, BenchmarkModelImportanceLevel, BenchmarkTaskDefinitionType, BenchmarkTaskRunAssertionStatus, BenchmarkTaskRunResultType, BenchmarkTaskRunState, BenchmarkTaskType, BenchmarkTaskVersionAggregationType, BenchmarkTaskVersionMappingType, BenchmarkType, BenchmarkVersionMappingType, BenchmarkVersionModelMappingType, SortOrder
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.tags.types.tag_service import Tag, TagList
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class ContentRole(enum.Enum):
  CONTENT_ROLE_UNSPECIFIED = 0
  CONTENT_ROLE_USER = 1
  """Inputs from the user."""
  CONTENT_ROLE_ASSISTANT = 2
  """Responses from the assistant in a dialogue between user & assistant."""
  CONTENT_ROLE_SYSTEM = 3
  r"""
  System instructions or commands ahead of the conversation. e.g.
  'assistant should be polite and helpful'. These are persistent (across
  turns and queries) and immutable by developers and their end users.
  """
  CONTENT_ROLE_DEVELOPER = 4
  r"""
  Developer instructions, i.e. 'You are a chatbot for Uber.'. These are
  persistent (across turns and queries) but mutable by developers.
  Equivalent of SYSTEM_1 in go/gemini-proto-roles.
  """
  CONTENT_ROLE_CONTEXT = 5
  """Additional documents or information relevant to this conversation."""

class Benchmark(KaggleObject):
  r"""
  TODO(bml): Consider making organization_id and owner_user_id a 'oneof'.

  Attributes:
    id (int)
    name (str)
      The name of the benchmark.
    slug (str)
      The url slug of the benchmark.
    organization_id (int)
      An organization to own the benchmark. By default, the user that created
      the benchmark will own it.
    forum_id (int)
      The discussion forum of the benchmark.
    published (bool)
      Whether this benchmark is publicly visible. This is true iff the entity
      meets all following conditions:
      1) IsPublic bit set to true
      2) ContentStateId field set to 'Published'

      Updating this field to true/false will perform the following operations:
      TRUE:
        1) Set IsPublic = true
        2) Set ContentStateId = 'Published'
      FALSE:
        1) Set IsPublic = false
        2) Set ContentStateId = 'Draft'
    type (BenchmarkType)
      What type of benchmark this is
    owner_user_id (int)
      The owner user of the benchmark.
    media (BenchmarkMedia)
      Media associated with the benchmark.
    task (BenchmarkTask)
      The task associated with this benchmark.
    version (BenchmarkVersion)
      The version associated with this benchmark.
      * CREATE : first version to be created with the parent benchmark.
      * GET    : the latest published version if available. Callers can also
      request a specific version.
      * UPDATE : unused (use UpdateBenchmarkVersion).
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
    topic_count (int)
      The topic count in the associated discussion tab.
    competition_id (int)
      A Competition linked to this benchmark. Admin-only setting.
    categories (TagList)
    owner_user (UserAvatar)
      The associated User, if any. Ignored on create and update.
    vote_count (int)
      Voting fields. HasUpVoted indicates whether current user has voted.
    has_up_voted (bool)
    permissions (Permissions)
    published_versions_count (int)
      A count of the total number of non-deleted and published (public) benchmark
      versions for this benchmark.
    draft_versions_count (int)
      A count of the total number of non-deleted and draft (private) benchmark
      versions for this benchmark. Note:
        * Should only ever be 0 or 1 since we don't allow more than 1 draft
        * Defaults to 0 for users without permissions to see drafts
    view_count (int)
      How many total views the benchmark has received.
    download_count (int)
      How many total downloads the benchmark has received.
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._slug = ""
    self._organization_id = None
    self._forum_id = None
    self._published = False
    self._type = BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED
    self._owner_user_id = None
    self._media = []
    self._task = None
    self._version = None
    self._organization = None
    self._topic_count = None
    self._competition_id = None
    self._categories = None
    self._owner_user = None
    self._vote_count = None
    self._has_up_voted = None
    self._permissions = None
    self._published_versions_count = None
    self._draft_versions_count = None
    self._view_count = None
    self._download_count = None
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
  def name(self) -> str:
    """The name of the benchmark."""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def slug(self) -> str:
    """The url slug of the benchmark."""
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
  def organization_id(self) -> int:
    r"""
    An organization to own the benchmark. By default, the user that created
    the benchmark will own it.
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
  def forum_id(self) -> int:
    """The discussion forum of the benchmark."""
    return self._forum_id or 0

  @forum_id.setter
  def forum_id(self, forum_id: Optional[int]):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

  @property
  def published(self) -> bool:
    r"""
    Whether this benchmark is publicly visible. This is true iff the entity
    meets all following conditions:
    1) IsPublic bit set to true
    2) ContentStateId field set to 'Published'

    Updating this field to true/false will perform the following operations:
    TRUE:
      1) Set IsPublic = true
      2) Set ContentStateId = 'Published'
    FALSE:
      1) Set IsPublic = false
      2) Set ContentStateId = 'Draft'
    """
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def type(self) -> 'BenchmarkType':
    """What type of benchmark this is"""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkType):
      raise TypeError('type must be of type BenchmarkType')
    self._type = type

  @property
  def owner_user_id(self) -> int:
    """The owner user of the benchmark."""
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def media(self) -> Optional[List[Optional['BenchmarkMedia']]]:
    """Media associated with the benchmark."""
    return self._media

  @media.setter
  def media(self, media: Optional[List[Optional['BenchmarkMedia']]]):
    if media is None:
      del self.media
      return
    if not isinstance(media, list):
      raise TypeError('media must be of type list')
    if not all([isinstance(t, BenchmarkMedia) for t in media]):
      raise TypeError('media must contain only items of type BenchmarkMedia')
    self._media = media

  @property
  def task(self) -> Optional['BenchmarkTask']:
    """The task associated with this benchmark."""
    return self._task or None

  @task.setter
  def task(self, task: Optional[Optional['BenchmarkTask']]):
    if task is None:
      del self.task
      return
    if not isinstance(task, BenchmarkTask):
      raise TypeError('task must be of type BenchmarkTask')
    self._task = task

  @property
  def version(self) -> Optional['BenchmarkVersion']:
    r"""
    The version associated with this benchmark.
    * CREATE : first version to be created with the parent benchmark.
    * GET    : the latest published version if available. Callers can also
    request a specific version.
    * UPDATE : unused (use UpdateBenchmarkVersion).
    """
    return self._version

  @version.setter
  def version(self, version: Optional['BenchmarkVersion']):
    if version is None:
      del self.version
      return
    if not isinstance(version, BenchmarkVersion):
      raise TypeError('version must be of type BenchmarkVersion')
    self._version = version

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    """The associated User, if any. Ignored on create and update."""
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional[Optional['UserAvatar']]):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    self._owner_user = owner_user

  @property
  def topic_count(self) -> int:
    """The topic count in the associated discussion tab."""
    return self._topic_count or 0

  @topic_count.setter
  def topic_count(self, topic_count: Optional[int]):
    if topic_count is None:
      del self.topic_count
      return
    if not isinstance(topic_count, int):
      raise TypeError('topic_count must be of type int')
    self._topic_count = topic_count

  @property
  def competition_id(self) -> int:
    """A Competition linked to this benchmark. Admin-only setting."""
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
  def categories(self) -> Optional['TagList']:
    return self._categories or None

  @categories.setter
  def categories(self, categories: Optional[Optional['TagList']]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, TagList):
      raise TypeError('categories must be of type TagList')
    self._categories = categories

  @property
  def vote_count(self) -> int:
    """Voting fields. HasUpVoted indicates whether current user has voted."""
    return self._vote_count or 0

  @vote_count.setter
  def vote_count(self, vote_count: Optional[int]):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def has_up_voted(self) -> bool:
    return self._has_up_voted or False

  @has_up_voted.setter
  def has_up_voted(self, has_up_voted: Optional[bool]):
    if has_up_voted is None:
      del self.has_up_voted
      return
    if not isinstance(has_up_voted, bool):
      raise TypeError('has_up_voted must be of type bool')
    self._has_up_voted = has_up_voted

  @property
  def permissions(self) -> Optional['Permissions']:
    return self._permissions or None

  @permissions.setter
  def permissions(self, permissions: Optional[Optional['Permissions']]):
    if permissions is None:
      del self.permissions
      return
    if not isinstance(permissions, Permissions):
      raise TypeError('permissions must be of type Permissions')
    self._permissions = permissions

  @property
  def view_count(self) -> int:
    """How many total views the benchmark has received."""
    return self._view_count or 0

  @view_count.setter
  def view_count(self, view_count: Optional[int]):
    if view_count is None:
      del self.view_count
      return
    if not isinstance(view_count, int):
      raise TypeError('view_count must be of type int')
    self._view_count = view_count

  @property
  def download_count(self) -> int:
    """How many total downloads the benchmark has received."""
    return self._download_count or 0

  @download_count.setter
  def download_count(self, download_count: Optional[int]):
    if download_count is None:
      del self.download_count
      return
    if not isinstance(download_count, int):
      raise TypeError('download_count must be of type int')
    self._download_count = download_count

  @property
  def published_versions_count(self) -> int:
    r"""
    A count of the total number of non-deleted and published (public) benchmark
    versions for this benchmark.
    """
    return self._published_versions_count or 0

  @published_versions_count.setter
  def published_versions_count(self, published_versions_count: Optional[int]):
    if published_versions_count is None:
      del self.published_versions_count
      return
    if not isinstance(published_versions_count, int):
      raise TypeError('published_versions_count must be of type int')
    self._published_versions_count = published_versions_count

  @property
  def draft_versions_count(self) -> int:
    r"""
    A count of the total number of non-deleted and draft (private) benchmark
    versions for this benchmark. Note:
      * Should only ever be 0 or 1 since we don't allow more than 1 draft
      * Defaults to 0 for users without permissions to see drafts
    """
    return self._draft_versions_count or 0

  @draft_versions_count.setter
  def draft_versions_count(self, draft_versions_count: Optional[int]):
    if draft_versions_count is None:
      del self.draft_versions_count
      return
    if not isinstance(draft_versions_count, int):
      raise TypeError('draft_versions_count must be of type int')
    self._draft_versions_count = draft_versions_count


class BenchmarkAuthor(KaggleObject):
  r"""
  Attributes:
    id (int)
      The backend Id of BenchmarkVersionAuthor / BenchmarkTaskVersionAuthor.
    name (str)
      Author Name.
    bio (str)
      Author Biography.
    website_url (str)
      Author Website.
  """

  def __init__(self):
    self._id = None
    self._name = None
    self._bio = None
    self._website_url = None
    self._freeze()

  @property
  def id(self) -> int:
    """The backend Id of BenchmarkVersionAuthor / BenchmarkTaskVersionAuthor."""
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def name(self) -> str:
    """Author Name."""
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def bio(self) -> str:
    """Author Biography."""
    return self._bio or ""

  @bio.setter
  def bio(self, bio: Optional[str]):
    if bio is None:
      del self.bio
      return
    if not isinstance(bio, str):
      raise TypeError('bio must be of type str')
    self._bio = bio

  @property
  def website_url(self) -> str:
    """Author Website."""
    return self._website_url or ""

  @website_url.setter
  def website_url(self, website_url: Optional[str]):
    if website_url is None:
      del self.website_url
      return
    if not isinstance(website_url, str):
      raise TypeError('website_url must be of type str')
    self._website_url = website_url


class BenchmarkBibtexCitation(KaggleObject):
  r"""
  Relevant fields for creating a BibTex formatted citation for a Benchmark.

  Attributes:
    authors (str)
      Comma-separated list of authors.
    title (str)
      Title of the benchmark.
    url (str)
      Url for the benchmark.
    year (str)
      Year of the benchmark's publication.
    organizations (str)
      Organization that published the benchmark.
  """

  def __init__(self):
    self._authors = ""
    self._title = ""
    self._url = ""
    self._year = ""
    self._organizations = ""
    self._freeze()

  @property
  def authors(self) -> str:
    """Comma-separated list of authors."""
    return self._authors

  @authors.setter
  def authors(self, authors: str):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, str):
      raise TypeError('authors must be of type str')
    self._authors = authors

  @property
  def title(self) -> str:
    """Title of the benchmark."""
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
  def url(self) -> str:
    """Url for the benchmark."""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def year(self) -> str:
    """Year of the benchmark's publication."""
    return self._year

  @year.setter
  def year(self, year: str):
    if year is None:
      del self.year
      return
    if not isinstance(year, str):
      raise TypeError('year must be of type str')
    self._year = year

  @property
  def organizations(self) -> str:
    """Organization that published the benchmark."""
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: str):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, str):
      raise TypeError('organizations must be of type str')
    self._organizations = organizations


class BenchmarkBracket(KaggleObject):
  r"""
  This message is serialized and stored in GCS per benchmark version, for GAME
  benchmarks that have a bracket. Modeled after the schema for react-brackets
  (https://www.npmjs.com/package/react-brackets), with custom fields for
  rendering.

  Attributes:
    rounds (BenchmarkBracketRound)
    start_time (datetime)
      Start and end time of the tournament (for display on the tournament tab
      timeline)
    end_time (datetime)
  """

  def __init__(self):
    self._rounds = []
    self._start_time = None
    self._end_time = None
    self._freeze()

  @property
  def rounds(self) -> Optional[List[Optional['BenchmarkBracketRound']]]:
    return self._rounds

  @rounds.setter
  def rounds(self, rounds: Optional[List[Optional['BenchmarkBracketRound']]]):
    if rounds is None:
      del self.rounds
      return
    if not isinstance(rounds, list):
      raise TypeError('rounds must be of type list')
    if not all([isinstance(t, BenchmarkBracketRound) for t in rounds]):
      raise TypeError('rounds must contain only items of type BenchmarkBracketRound')
    self._rounds = rounds

  @property
  def start_time(self) -> datetime:
    r"""
    Start and end time of the tournament (for display on the tournament tab
    timeline)
    """
    return self._start_time

  @start_time.setter
  def start_time(self, start_time: datetime):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    return self._end_time

  @end_time.setter
  def end_time(self, end_time: datetime):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time


class BenchmarkBracketRound(KaggleObject):
  r"""
  Attributes:
    seeds (BenchmarkBracketSeed)
  """

  def __init__(self):
    self._seeds = []
    self._freeze()

  @property
  def seeds(self) -> Optional[List[Optional['BenchmarkBracketSeed']]]:
    return self._seeds

  @seeds.setter
  def seeds(self, seeds: Optional[List[Optional['BenchmarkBracketSeed']]]):
    if seeds is None:
      del self.seeds
      return
    if not isinstance(seeds, list):
      raise TypeError('seeds must be of type list')
    if not all([isinstance(t, BenchmarkBracketSeed) for t in seeds]):
      raise TypeError('seeds must contain only items of type BenchmarkBracketSeed')
    self._seeds = seeds


class BenchmarkBracketSeed(KaggleObject):
  r"""
  Attributes:
    teams (BenchmarkBracketTeam)
    episode_ids (int)
      If specified, IDs to fetch simulation replays
    live (bool)
      If true, this match is currently being livestreamed.
    replay_url (str)
      If specified, the replay button links to this url instead of episode
      replays.
      If also live, the bracket will use this url to link to the livestream.
  """

  def __init__(self):
    self._teams = []
    self._episode_ids = []
    self._live = None
    self._replay_url = None
    self._freeze()

  @property
  def teams(self) -> Optional[List[Optional['BenchmarkBracketTeam']]]:
    return self._teams

  @teams.setter
  def teams(self, teams: Optional[List[Optional['BenchmarkBracketTeam']]]):
    if teams is None:
      del self.teams
      return
    if not isinstance(teams, list):
      raise TypeError('teams must be of type list')
    if not all([isinstance(t, BenchmarkBracketTeam) for t in teams]):
      raise TypeError('teams must contain only items of type BenchmarkBracketTeam')
    self._teams = teams

  @property
  def episode_ids(self) -> Optional[List[int]]:
    """If specified, IDs to fetch simulation replays"""
    return self._episode_ids

  @episode_ids.setter
  def episode_ids(self, episode_ids: Optional[List[int]]):
    if episode_ids is None:
      del self.episode_ids
      return
    if not isinstance(episode_ids, list):
      raise TypeError('episode_ids must be of type list')
    if not all([isinstance(t, int) for t in episode_ids]):
      raise TypeError('episode_ids must contain only items of type int')
    self._episode_ids = episode_ids

  @property
  def live(self) -> bool:
    """If true, this match is currently being livestreamed."""
    return self._live or False

  @live.setter
  def live(self, live: Optional[bool]):
    if live is None:
      del self.live
      return
    if not isinstance(live, bool):
      raise TypeError('live must be of type bool')
    self._live = live

  @property
  def replay_url(self) -> str:
    r"""
    If specified, the replay button links to this url instead of episode
    replays.
    If also live, the bracket will use this url to link to the livestream.
    """
    return self._replay_url or ""

  @replay_url.setter
  def replay_url(self, replay_url: Optional[str]):
    if replay_url is None:
      del self.replay_url
      return
    if not isinstance(replay_url, str):
      raise TypeError('replay_url must be of type str')
    self._replay_url = replay_url


class BenchmarkBracketTeam(KaggleObject):
  r"""
  Attributes:
    benchmark_model_version_id (int)
      Teams must be represented by a benchmark model version.
      If unset, the bracket will render an empty team; e.g. a placeholder for
      incomplete results.
    benchmark_model (BenchmarkModel)
      This will automatically populate based on the above ID. It is the parent
      model proto with the requested version.
    num_wins (float)
      How many wins this team had in the series / score for the series.
    winner (bool)
      Whether this team is the winning team
    static_logo_path (str)
      Path like /static/... to an image to override the organization's image
  """

  def __init__(self):
    self._benchmark_model_version_id = None
    self._benchmark_model = None
    self._num_wins = None
    self._winner = None
    self._static_logo_path = None
    self._freeze()

  @property
  def benchmark_model_version_id(self) -> int:
    r"""
    Teams must be represented by a benchmark model version.
    If unset, the bracket will render an empty team; e.g. a placeholder for
    incomplete results.
    """
    return self._benchmark_model_version_id or 0

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: Optional[int]):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def benchmark_model(self) -> Optional['BenchmarkModel']:
    r"""
    This will automatically populate based on the above ID. It is the parent
    model proto with the requested version.
    """
    return self._benchmark_model or None

  @benchmark_model.setter
  def benchmark_model(self, benchmark_model: Optional[Optional['BenchmarkModel']]):
    if benchmark_model is None:
      del self.benchmark_model
      return
    if not isinstance(benchmark_model, BenchmarkModel):
      raise TypeError('benchmark_model must be of type BenchmarkModel')
    self._benchmark_model = benchmark_model

  @property
  def num_wins(self) -> float:
    """How many wins this team had in the series / score for the series."""
    return self._num_wins or 0.0

  @num_wins.setter
  def num_wins(self, num_wins: Optional[float]):
    if num_wins is None:
      del self.num_wins
      return
    if not isinstance(num_wins, float):
      raise TypeError('num_wins must be of type float')
    self._num_wins = num_wins

  @property
  def winner(self) -> bool:
    """Whether this team is the winning team"""
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
  def static_logo_path(self) -> str:
    """Path like /static/... to an image to override the organization's image"""
    return self._static_logo_path or ""

  @static_logo_path.setter
  def static_logo_path(self, static_logo_path: Optional[str]):
    if static_logo_path is None:
      del self.static_logo_path
      return
    if not isinstance(static_logo_path, str):
      raise TypeError('static_logo_path must be of type str')
    self._static_logo_path = static_logo_path


class BenchmarkIdentifier(KaggleObject):
  r"""
  Identifier for selecting a specific benchmark.

  Attributes:
    id (int)
    slug_identifier (SlugIdentifier)
    competition_id (int)
      1:1 connection for Benchmarks <-> Simulation Competitions
  """

  def __init__(self):
    self._id = None
    self._slug_identifier = None
    self._competition_id = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    del self.slug_identifier
    del self.competition_id
    self._id = id

  @property
  def slug_identifier(self) -> Optional['SlugIdentifier']:
    return self._slug_identifier or None

  @slug_identifier.setter
  def slug_identifier(self, slug_identifier: Optional['SlugIdentifier']):
    if slug_identifier is None:
      del self.slug_identifier
      return
    if not isinstance(slug_identifier, SlugIdentifier):
      raise TypeError('slug_identifier must be of type SlugIdentifier')
    del self.id
    del self.competition_id
    self._slug_identifier = slug_identifier

  @property
  def competition_id(self) -> int:
    """1:1 connection for Benchmarks <-> Simulation Competitions"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.id
    del self.slug_identifier
    self._competition_id = competition_id


class BenchmarkLeaderboard(KaggleObject):
  r"""
  Attributes:
    headers (BenchmarkLeaderboardHeader)
      Headers of the columns of the leaderboard, each indicates the benchmark
      version for that column and the mapping details for the benchmark version.
    rows (BenchmarkLeaderboardRow)
      Rows of the leaderboard, each of which containing metadata and results for
      a single model version.
  """

  def __init__(self):
    self._headers = []
    self._rows = []
    self._freeze()

  @property
  def headers(self) -> Optional[List[Optional['BenchmarkLeaderboardHeader']]]:
    r"""
    Headers of the columns of the leaderboard, each indicates the benchmark
    version for that column and the mapping details for the benchmark version.
    """
    return self._headers

  @headers.setter
  def headers(self, headers: Optional[List[Optional['BenchmarkLeaderboardHeader']]]):
    if headers is None:
      del self.headers
      return
    if not isinstance(headers, list):
      raise TypeError('headers must be of type list')
    if not all([isinstance(t, BenchmarkLeaderboardHeader) for t in headers]):
      raise TypeError('headers must contain only items of type BenchmarkLeaderboardHeader')
    self._headers = headers

  @property
  def rows(self) -> Optional[List[Optional['BenchmarkLeaderboardRow']]]:
    r"""
    Rows of the leaderboard, each of which containing metadata and results for
    a single model version.
    """
    return self._rows

  @rows.setter
  def rows(self, rows: Optional[List[Optional['BenchmarkLeaderboardRow']]]):
    if rows is None:
      del self.rows
      return
    if not isinstance(rows, list):
      raise TypeError('rows must be of type list')
    if not all([isinstance(t, BenchmarkLeaderboardRow) for t in rows]):
      raise TypeError('rows must contain only items of type BenchmarkLeaderboardRow')
    self._rows = rows


class BenchmarkLeaderboardEntry(KaggleObject):
  r"""
  Attributes:
    model_version_id (int)
    task_version_id (int)
    runs (BenchmarkTaskRun)
      Relevant runs for the given (ModelVersion, TaskVersion) pair. For now, this
      should always just be a single run, since we only display the most recent.
  """

  def __init__(self):
    self._model_version_id = 0
    self._task_version_id = 0
    self._runs = []
    self._freeze()

  @property
  def model_version_id(self) -> int:
    return self._model_version_id

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    self._model_version_id = model_version_id

  @property
  def task_version_id(self) -> int:
    return self._task_version_id

  @task_version_id.setter
  def task_version_id(self, task_version_id: int):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def runs(self) -> Optional[List[Optional['BenchmarkTaskRun']]]:
    r"""
    Relevant runs for the given (ModelVersion, TaskVersion) pair. For now, this
    should always just be a single run, since we only display the most recent.
    """
    return self._runs

  @runs.setter
  def runs(self, runs: Optional[List[Optional['BenchmarkTaskRun']]]):
    if runs is None:
      del self.runs
      return
    if not isinstance(runs, list):
      raise TypeError('runs must be of type list')
    if not all([isinstance(t, BenchmarkTaskRun) for t in runs]):
      raise TypeError('runs must contain only items of type BenchmarkTaskRun')
    self._runs = runs


class BenchmarkLeaderboardHeader(KaggleObject):
  r"""
  Attributes:
    benchmark_version (BenchmarkVersion)
      Benchmark version that comprises a column of the leaderboard.
    benchmark_version_mapping (BenchmarkVersionMapping)
      Additional details on the mapping for this benchmark version (and column).
    task_version (BenchmarkTaskVersion)
      Task version that comprises a column of the leaderboard.
    task_version_mapping (BenchmarkTaskVersionMapping)
      Additional details on the mapping for this task version (and column).
  """

  def __init__(self):
    self._benchmark_version = None
    self._benchmark_version_mapping = None
    self._task_version = None
    self._task_version_mapping = None
    self._freeze()

  @property
  def benchmark_version(self) -> Optional['BenchmarkVersion']:
    """Benchmark version that comprises a column of the leaderboard."""
    return self._benchmark_version

  @benchmark_version.setter
  def benchmark_version(self, benchmark_version: Optional['BenchmarkVersion']):
    if benchmark_version is None:
      del self.benchmark_version
      return
    if not isinstance(benchmark_version, BenchmarkVersion):
      raise TypeError('benchmark_version must be of type BenchmarkVersion')
    self._benchmark_version = benchmark_version

  @property
  def benchmark_version_mapping(self) -> Optional['BenchmarkVersionMapping']:
    """Additional details on the mapping for this benchmark version (and column)."""
    return self._benchmark_version_mapping

  @benchmark_version_mapping.setter
  def benchmark_version_mapping(self, benchmark_version_mapping: Optional['BenchmarkVersionMapping']):
    if benchmark_version_mapping is None:
      del self.benchmark_version_mapping
      return
    if not isinstance(benchmark_version_mapping, BenchmarkVersionMapping):
      raise TypeError('benchmark_version_mapping must be of type BenchmarkVersionMapping')
    self._benchmark_version_mapping = benchmark_version_mapping

  @property
  def task_version(self) -> Optional['BenchmarkTaskVersion']:
    """Task version that comprises a column of the leaderboard."""
    return self._task_version or None

  @task_version.setter
  def task_version(self, task_version: Optional[Optional['BenchmarkTaskVersion']]):
    if task_version is None:
      del self.task_version
      return
    if not isinstance(task_version, BenchmarkTaskVersion):
      raise TypeError('task_version must be of type BenchmarkTaskVersion')
    self._task_version = task_version

  @property
  def task_version_mapping(self) -> Optional['BenchmarkTaskVersionMapping']:
    """Additional details on the mapping for this task version (and column)."""
    return self._task_version_mapping or None

  @task_version_mapping.setter
  def task_version_mapping(self, task_version_mapping: Optional[Optional['BenchmarkTaskVersionMapping']]):
    if task_version_mapping is None:
      del self.task_version_mapping
      return
    if not isinstance(task_version_mapping, BenchmarkTaskVersionMapping):
      raise TypeError('task_version_mapping must be of type BenchmarkTaskVersionMapping')
    self._task_version_mapping = task_version_mapping


class BenchmarkLeaderboardModelVersionHeader(KaggleObject):
  r"""
  Attributes:
    model_version (BenchmarkModelVersion)
      ModelVersion for this header.
    model_version_mapping (BenchmarkVersionModelMapping)
      Describes how this ModelVersion is mapped to this leaderboard.
    medal (Medal)
      Indicates whether this model version has earned a medal on this
      leaderboard. For now, this specifically means that this model version's
      performance on the highest priority task version is within the top 3.
    rank (int)
      This model version's rank in the leaderboard. Used by the FE.
  """

  def __init__(self):
    self._model_version = None
    self._model_version_mapping = None
    self._medal = None
    self._rank = None
    self._freeze()

  @property
  def model_version(self) -> Optional['BenchmarkModelVersion']:
    """ModelVersion for this header."""
    return self._model_version

  @model_version.setter
  def model_version(self, model_version: Optional['BenchmarkModelVersion']):
    if model_version is None:
      del self.model_version
      return
    if not isinstance(model_version, BenchmarkModelVersion):
      raise TypeError('model_version must be of type BenchmarkModelVersion')
    self._model_version = model_version

  @property
  def model_version_mapping(self) -> Optional['BenchmarkVersionModelMapping']:
    """Describes how this ModelVersion is mapped to this leaderboard."""
    return self._model_version_mapping or None

  @model_version_mapping.setter
  def model_version_mapping(self, model_version_mapping: Optional[Optional['BenchmarkVersionModelMapping']]):
    if model_version_mapping is None:
      del self.model_version_mapping
      return
    if not isinstance(model_version_mapping, BenchmarkVersionModelMapping):
      raise TypeError('model_version_mapping must be of type BenchmarkVersionModelMapping')
    self._model_version_mapping = model_version_mapping

  @property
  def medal(self) -> 'Medal':
    r"""
    Indicates whether this model version has earned a medal on this
    leaderboard. For now, this specifically means that this model version's
    performance on the highest priority task version is within the top 3.
    """
    return self._medal or Medal.MEDAL_UNSPECIFIED

  @medal.setter
  def medal(self, medal: Optional['Medal']):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def rank(self) -> int:
    """This model version's rank in the leaderboard. Used by the FE."""
    return self._rank or 0

  @rank.setter
  def rank(self, rank: Optional[int]):
    if rank is None:
      del self.rank
      return
    if not isinstance(rank, int):
      raise TypeError('rank must be of type int')
    self._rank = rank


class BenchmarkLeaderboardRow(KaggleObject):
  r"""
  Attributes:
    model_version (BenchmarkModelVersion)
      The model version represented on the row
    publisher_organization (OrganizationCard)
      The organization that published the parent model.
    publisher_user_id (int)
      User who published the model
    model_license (License)
      The license for the parent model.
    aggregate_score (float)
      The aggregate score of results from all benchmark versions that the model
      will be ranked by on the leaderboard.
      Only null if the model version has no results for any of the benchmark
      versions.
    results (BenchmarkResult)
      An individual result for this model version for each of the benchmark
      versions on the leaderboard.
    model_version_mapping (BenchmarkVersionModelMapping)
      The mapping for this model version
  """

  def __init__(self):
    self._model_version = None
    self._publisher_organization = None
    self._publisher_user_id = None
    self._model_license = None
    self._aggregate_score = None
    self._results = []
    self._model_version_mapping = None
    self._freeze()

  @property
  def model_version(self) -> Optional['BenchmarkModelVersion']:
    """The model version represented on the row"""
    return self._model_version

  @model_version.setter
  def model_version(self, model_version: Optional['BenchmarkModelVersion']):
    if model_version is None:
      del self.model_version
      return
    if not isinstance(model_version, BenchmarkModelVersion):
      raise TypeError('model_version must be of type BenchmarkModelVersion')
    self._model_version = model_version

  @property
  def model_version_mapping(self) -> Optional['BenchmarkVersionModelMapping']:
    """The mapping for this model version"""
    return self._model_version_mapping

  @model_version_mapping.setter
  def model_version_mapping(self, model_version_mapping: Optional['BenchmarkVersionModelMapping']):
    if model_version_mapping is None:
      del self.model_version_mapping
      return
    if not isinstance(model_version_mapping, BenchmarkVersionModelMapping):
      raise TypeError('model_version_mapping must be of type BenchmarkVersionModelMapping')
    self._model_version_mapping = model_version_mapping

  @property
  def publisher_organization(self) -> Optional['OrganizationCard']:
    """The organization that published the parent model."""
    return self._publisher_organization or None

  @publisher_organization.setter
  def publisher_organization(self, publisher_organization: Optional['OrganizationCard']):
    if publisher_organization is None:
      del self.publisher_organization
      return
    if not isinstance(publisher_organization, OrganizationCard):
      raise TypeError('publisher_organization must be of type OrganizationCard')
    del self.publisher_user_id
    self._publisher_organization = publisher_organization

  @property
  def publisher_user_id(self) -> int:
    """User who published the model"""
    return self._publisher_user_id or 0

  @publisher_user_id.setter
  def publisher_user_id(self, publisher_user_id: int):
    if publisher_user_id is None:
      del self.publisher_user_id
      return
    if not isinstance(publisher_user_id, int):
      raise TypeError('publisher_user_id must be of type int')
    del self.publisher_organization
    self._publisher_user_id = publisher_user_id

  @property
  def model_license(self) -> Optional['License']:
    """The license for the parent model."""
    return self._model_license

  @model_license.setter
  def model_license(self, model_license: Optional['License']):
    if model_license is None:
      del self.model_license
      return
    if not isinstance(model_license, License):
      raise TypeError('model_license must be of type License')
    self._model_license = model_license

  @property
  def aggregate_score(self) -> float:
    r"""
    The aggregate score of results from all benchmark versions that the model
    will be ranked by on the leaderboard.
    Only null if the model version has no results for any of the benchmark
    versions.
    """
    return self._aggregate_score or 0.0

  @aggregate_score.setter
  def aggregate_score(self, aggregate_score: Optional[float]):
    if aggregate_score is None:
      del self.aggregate_score
      return
    if not isinstance(aggregate_score, float):
      raise TypeError('aggregate_score must be of type float')
    self._aggregate_score = aggregate_score

  @property
  def results(self) -> Optional[List[Optional['BenchmarkResult']]]:
    r"""
    An individual result for this model version for each of the benchmark
    versions on the leaderboard.
    """
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['BenchmarkResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, BenchmarkResult) for t in results]):
      raise TypeError('results must contain only items of type BenchmarkResult')
    self._results = results


class BenchmarkLeaderboardTaskVersionHeader(KaggleObject):
  r"""
  Attributes:
    task_version (BenchmarkTaskVersion)
    benchmark_version (BenchmarkVersion)
    task_version_mapping (BenchmarkTaskVersionMapping)
      Describes how this (root) TaskVersion is mapped to this leaderboard.
  """

  def __init__(self):
    self._task_version = None
    self._benchmark_version = None
    self._task_version_mapping = None
    self._freeze()

  @property
  def task_version(self) -> Optional['BenchmarkTaskVersion']:
    return self._task_version or None

  @task_version.setter
  def task_version(self, task_version: Optional['BenchmarkTaskVersion']):
    if task_version is None:
      del self.task_version
      return
    if not isinstance(task_version, BenchmarkTaskVersion):
      raise TypeError('task_version must be of type BenchmarkTaskVersion')
    del self.benchmark_version
    self._task_version = task_version

  @property
  def benchmark_version(self) -> Optional['BenchmarkVersion']:
    return self._benchmark_version or None

  @benchmark_version.setter
  def benchmark_version(self, benchmark_version: Optional['BenchmarkVersion']):
    if benchmark_version is None:
      del self.benchmark_version
      return
    if not isinstance(benchmark_version, BenchmarkVersion):
      raise TypeError('benchmark_version must be of type BenchmarkVersion')
    del self.task_version
    self._benchmark_version = benchmark_version

  @property
  def task_version_mapping(self) -> Optional['BenchmarkTaskVersionMapping']:
    """Describes how this (root) TaskVersion is mapped to this leaderboard."""
    return self._task_version_mapping or None

  @task_version_mapping.setter
  def task_version_mapping(self, task_version_mapping: Optional[Optional['BenchmarkTaskVersionMapping']]):
    if task_version_mapping is None:
      del self.task_version_mapping
      return
    if not isinstance(task_version_mapping, BenchmarkTaskVersionMapping):
      raise TypeError('task_version_mapping must be of type BenchmarkTaskVersionMapping')
    self._task_version_mapping = task_version_mapping


class BenchmarkMedia(KaggleObject):
  r"""
  Attributes:
    type (BenchmarkMediaType)
      The type of media.
    url (str)
      The link to the media.
    name (str)
      Optional display name for the media chip. If unset, there is a default per
      type.
  """

  def __init__(self):
    self._type = BenchmarkMediaType.BENCHMARK_MEDIA_TYPE_UNSPECIFIED
    self._url = ""
    self._name = None
    self._freeze()

  @property
  def type(self) -> 'BenchmarkMediaType':
    """The type of media."""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkMediaType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkMediaType):
      raise TypeError('type must be of type BenchmarkMediaType')
    self._type = type

  @property
  def url(self) -> str:
    """The link to the media."""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def name(self) -> str:
    r"""
    Optional display name for the media chip. If unset, there is a default per
    type.
    """
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


class BenchmarkModel(KaggleObject):
  r"""
  Attributes:
    id (int)
      This benchmark model's id.
    display_name (str)
      The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'
    slug (str)
      The slug of the model (plus variation). ex: 'gemini-1.5-pro'
    organization_id (int)
      The organization that published the model.
    owner_user_id (int)
      The user that owns / created this model.
      Filled automatically while creating, can be updated later.
    license_id (int)
      The license for this model.
    default_version_id (int)
      The default version to use for this model.
      Filled automatically while creating, can be updated later.
    version (BenchmarkModelVersion)
      The version associated with this benchmark model.
      * CREATE : first version to be created with the parent benchmark model.
      * GET    : specified version or default if none was specified.
      * UPDATE : unused (use UpdateBenchmarkModelVersion).
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
    license (License)
      The associated License. Ignored on create and update.
    published (bool)
      Whether the benchmark model is published (iff ContentStateId == PUBLISHED).
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._organization_id = None
    self._owner_user_id = None
    self._license_id = 0
    self._default_version_id = None
    self._version = None
    self._organization = None
    self._license = None
    self._published = False
    self._freeze()

  @property
  def id(self) -> int:
    """This benchmark model's id."""
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
  def display_name(self) -> str:
    """The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'"""
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def slug(self) -> str:
    """The slug of the model (plus variation). ex: 'gemini-1.5-pro'"""
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
  def organization_id(self) -> int:
    """The organization that published the model."""
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
  def owner_user_id(self) -> int:
    r"""
    The user that owns / created this model.
    Filled automatically while creating, can be updated later.
    """
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def license_id(self) -> int:
    """The license for this model."""
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def default_version_id(self) -> int:
    r"""
    The default version to use for this model.
    Filled automatically while creating, can be updated later.
    """
    return self._default_version_id or 0

  @default_version_id.setter
  def default_version_id(self, default_version_id: Optional[int]):
    if default_version_id is None:
      del self.default_version_id
      return
    if not isinstance(default_version_id, int):
      raise TypeError('default_version_id must be of type int')
    self._default_version_id = default_version_id

  @property
  def version(self) -> Optional['BenchmarkModelVersion']:
    r"""
    The version associated with this benchmark model.
    * CREATE : first version to be created with the parent benchmark model.
    * GET    : specified version or default if none was specified.
    * UPDATE : unused (use UpdateBenchmarkModelVersion).
    """
    return self._version or None

  @version.setter
  def version(self, version: Optional[Optional['BenchmarkModelVersion']]):
    if version is None:
      del self.version
      return
    if not isinstance(version, BenchmarkModelVersion):
      raise TypeError('version must be of type BenchmarkModelVersion')
    self._version = version

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization

  @organization.setter
  def organization(self, organization: Optional['OrganizationCard']):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def license(self) -> Optional['License']:
    """The associated License. Ignored on create and update."""
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def published(self) -> bool:
    """Whether the benchmark model is published (iff ContentStateId == PUBLISHED)."""
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published


class BenchmarkModelVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the benchmark model version.
    benchmark_model_id (int)
      The id of the parent benchmark model.
    slug (str)
      The slug of the model version. ex: 'gemini-1.5-pro-001'
      Required for CREATE, can be updated later.
    external_url (str)
      An external link to a resource explaining the model version. ex: blog post,
      aistudio, etc.
    knowledge_cutoff (datetime)
      A cutoff date for training data for the model.
    is_default (bool)
      Whether this BenchmarkModelVersion is the default for the parent
      BenchmarkModel.
    published (bool)
      Whether the model version is published (iff ContentStateId == PUBLISHED and
      parent benchmark model has ContentStateId == PUBLISHED).
    allow_model_proxy (bool)
      Whether this BenchmarkModelVersion is supported by model proxy.
    model_proxy_slug (str)
      The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
      Only set when `allow_model_proxy` is true.
    display_name (str)
    description (str)
    organization (OrganizationCard)
      Fields from the model for convenience
    name (str)
    license (License)
    importance_level (BenchmarkModelImportanceLevel)
      Whether this model version is run on Kaggle-maintained benchmarks
  """

  def __init__(self):
    self._id = 0
    self._benchmark_model_id = 0
    self._slug = ""
    self._external_url = None
    self._knowledge_cutoff = None
    self._is_default = False
    self._published = False
    self._allow_model_proxy = False
    self._model_proxy_slug = None
    self._display_name = None
    self._description = None
    self._organization = None
    self._name = None
    self._license = None
    self._importance_level = None
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the benchmark model version."""
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
  def benchmark_model_id(self) -> int:
    """The id of the parent benchmark model."""
    return self._benchmark_model_id

  @benchmark_model_id.setter
  def benchmark_model_id(self, benchmark_model_id: int):
    if benchmark_model_id is None:
      del self.benchmark_model_id
      return
    if not isinstance(benchmark_model_id, int):
      raise TypeError('benchmark_model_id must be of type int')
    self._benchmark_model_id = benchmark_model_id

  @property
  def slug(self) -> str:
    r"""
    The slug of the model version. ex: 'gemini-1.5-pro-001'
    Required for CREATE, can be updated later.
    """
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
  def external_url(self) -> str:
    r"""
    An external link to a resource explaining the model version. ex: blog post,
    aistudio, etc.
    """
    return self._external_url or ""

  @external_url.setter
  def external_url(self, external_url: Optional[str]):
    if external_url is None:
      del self.external_url
      return
    if not isinstance(external_url, str):
      raise TypeError('external_url must be of type str')
    self._external_url = external_url

  @property
  def knowledge_cutoff(self) -> datetime:
    """A cutoff date for training data for the model."""
    return self._knowledge_cutoff or None

  @knowledge_cutoff.setter
  def knowledge_cutoff(self, knowledge_cutoff: Optional[datetime]):
    if knowledge_cutoff is None:
      del self.knowledge_cutoff
      return
    if not isinstance(knowledge_cutoff, datetime):
      raise TypeError('knowledge_cutoff must be of type datetime')
    self._knowledge_cutoff = knowledge_cutoff

  @property
  def is_default(self) -> bool:
    r"""
    Whether this BenchmarkModelVersion is the default for the parent
    BenchmarkModel.
    """
    return self._is_default

  @is_default.setter
  def is_default(self, is_default: bool):
    if is_default is None:
      del self.is_default
      return
    if not isinstance(is_default, bool):
      raise TypeError('is_default must be of type bool')
    self._is_default = is_default

  @property
  def published(self) -> bool:
    r"""
    Whether the model version is published (iff ContentStateId == PUBLISHED and
    parent benchmark model has ContentStateId == PUBLISHED).
    """
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def allow_model_proxy(self) -> bool:
    """Whether this BenchmarkModelVersion is supported by model proxy."""
    return self._allow_model_proxy

  @allow_model_proxy.setter
  def allow_model_proxy(self, allow_model_proxy: bool):
    if allow_model_proxy is None:
      del self.allow_model_proxy
      return
    if not isinstance(allow_model_proxy, bool):
      raise TypeError('allow_model_proxy must be of type bool')
    self._allow_model_proxy = allow_model_proxy

  @property
  def model_proxy_slug(self) -> str:
    r"""
    The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
    Only set when `allow_model_proxy` is true.
    """
    return self._model_proxy_slug or ""

  @model_proxy_slug.setter
  def model_proxy_slug(self, model_proxy_slug: Optional[str]):
    if model_proxy_slug is None:
      del self.model_proxy_slug
      return
    if not isinstance(model_proxy_slug, str):
      raise TypeError('model_proxy_slug must be of type str')
    self._model_proxy_slug = model_proxy_slug

  @property
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """Fields from the model for convenience"""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def license(self) -> Optional['License']:
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def importance_level(self) -> 'BenchmarkModelImportanceLevel':
    """Whether this model version is run on Kaggle-maintained benchmarks"""
    return self._importance_level or BenchmarkModelImportanceLevel.BENCHMARK_MODEL_IMPORTANCE_LEVEL_UNSPECIFIED

  @importance_level.setter
  def importance_level(self, importance_level: Optional['BenchmarkModelImportanceLevel']):
    if importance_level is None:
      del self.importance_level
      return
    if not isinstance(importance_level, BenchmarkModelImportanceLevel):
      raise TypeError('importance_level must be of type BenchmarkModelImportanceLevel')
    self._importance_level = importance_level


class BenchmarkResult(KaggleObject):
  r"""
  TODO(bml): Integrate this proto with personal benchmarks trials.
  Represents the outcome of a benchmark run. All fields are immutable.

  Attributes:
    numeric_result (NumericResult)
    boolean_result (bool)
    custom_additional_results (CustomResult)
      Generic additional results. These are rendered generically on the frontend:
    numeric_result_private (NumericResult)
      Numeric result on the private set of the benchmark version.
    numeric_result_public (NumericResult)
      Numeric result on the public set of the benchmark version.
    evaluation_date (datetime)
      The date on which evaluation was performed.
    task_version_id (int)
      Convenience fields for this result (for the frontend):
  """

  def __init__(self):
    self._numeric_result = None
    self._boolean_result = None
    self._custom_additional_results = []
    self._numeric_result_private = None
    self._numeric_result_public = None
    self._evaluation_date = None
    self._task_version_id = None
    self._freeze()

  @property
  def task_version_id(self) -> int:
    """Convenience fields for this result (for the frontend):"""
    return self._task_version_id or 0

  @task_version_id.setter
  def task_version_id(self, task_version_id: Optional[int]):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def numeric_result(self) -> Optional['NumericResult']:
    return self._numeric_result or None

  @numeric_result.setter
  def numeric_result(self, numeric_result: Optional['NumericResult']):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, NumericResult):
      raise TypeError('numeric_result must be of type NumericResult')
    del self.boolean_result
    self._numeric_result = numeric_result

  @property
  def boolean_result(self) -> bool:
    return self._boolean_result or False

  @boolean_result.setter
  def boolean_result(self, boolean_result: bool):
    if boolean_result is None:
      del self.boolean_result
      return
    if not isinstance(boolean_result, bool):
      raise TypeError('boolean_result must be of type bool')
    del self.numeric_result
    self._boolean_result = boolean_result

  @property
  def custom_additional_results(self) -> Optional[List[Optional['CustomResult']]]:
    """Generic additional results. These are rendered generically on the frontend:"""
    return self._custom_additional_results

  @custom_additional_results.setter
  def custom_additional_results(self, custom_additional_results: Optional[List[Optional['CustomResult']]]):
    if custom_additional_results is None:
      del self.custom_additional_results
      return
    if not isinstance(custom_additional_results, list):
      raise TypeError('custom_additional_results must be of type list')
    if not all([isinstance(t, CustomResult) for t in custom_additional_results]):
      raise TypeError('custom_additional_results must contain only items of type CustomResult')
    self._custom_additional_results = custom_additional_results

  @property
  def numeric_result_private(self) -> Optional['NumericResult']:
    """Numeric result on the private set of the benchmark version."""
    return self._numeric_result_private or None

  @numeric_result_private.setter
  def numeric_result_private(self, numeric_result_private: Optional[Optional['NumericResult']]):
    if numeric_result_private is None:
      del self.numeric_result_private
      return
    if not isinstance(numeric_result_private, NumericResult):
      raise TypeError('numeric_result_private must be of type NumericResult')
    self._numeric_result_private = numeric_result_private

  @property
  def numeric_result_public(self) -> Optional['NumericResult']:
    """Numeric result on the public set of the benchmark version."""
    return self._numeric_result_public or None

  @numeric_result_public.setter
  def numeric_result_public(self, numeric_result_public: Optional[Optional['NumericResult']]):
    if numeric_result_public is None:
      del self.numeric_result_public
      return
    if not isinstance(numeric_result_public, NumericResult):
      raise TypeError('numeric_result_public must be of type NumericResult')
    self._numeric_result_public = numeric_result_public

  @property
  def evaluation_date(self) -> datetime:
    """The date on which evaluation was performed."""
    return self._evaluation_date or None

  @evaluation_date.setter
  def evaluation_date(self, evaluation_date: Optional[datetime]):
    if evaluation_date is None:
      del self.evaluation_date
      return
    if not isinstance(evaluation_date, datetime):
      raise TypeError('evaluation_date must be of type datetime')
    self._evaluation_date = evaluation_date


class BenchmarkSlugSelector(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    benchmark_slug (str)
    version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._benchmark_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    return self._benchmark_slug

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: str):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug

  @property
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class BenchmarkStream(KaggleObject):
  r"""
  Attributes:
    youtube_id (str)
    kick_channel (str)
    name (str)
    description (str)
    image_url (str)
      If unspecified, try to fetch from source
    link_url (str)
      If specified, leads to this url on click instead of the source url
      E.g. Hikaru's stream is backed by Kick but hosted on Chess.com, and we want
      to lead people to Chess.com.
    live (bool)
      Whether this is a currently active livestream
    featured (bool)
      Whether this should be the 'featured' (prominently displayed) stream
    schedule_date (datetime)
      When the livestream is scheduled for. Just the date is displayed.
  """

  def __init__(self):
    self._youtube_id = None
    self._kick_channel = None
    self._name = ""
    self._description = ""
    self._image_url = None
    self._link_url = None
    self._live = None
    self._featured = None
    self._schedule_date = None
    self._freeze()

  @property
  def youtube_id(self) -> str:
    return self._youtube_id or ""

  @youtube_id.setter
  def youtube_id(self, youtube_id: str):
    if youtube_id is None:
      del self.youtube_id
      return
    if not isinstance(youtube_id, str):
      raise TypeError('youtube_id must be of type str')
    del self.kick_channel
    self._youtube_id = youtube_id

  @property
  def kick_channel(self) -> str:
    return self._kick_channel or ""

  @kick_channel.setter
  def kick_channel(self, kick_channel: str):
    if kick_channel is None:
      del self.kick_channel
      return
    if not isinstance(kick_channel, str):
      raise TypeError('kick_channel must be of type str')
    del self.youtube_id
    self._kick_channel = kick_channel

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
  def image_url(self) -> str:
    """If unspecified, try to fetch from source"""
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def link_url(self) -> str:
    r"""
    If specified, leads to this url on click instead of the source url
    E.g. Hikaru's stream is backed by Kick but hosted on Chess.com, and we want
    to lead people to Chess.com.
    """
    return self._link_url or ""

  @link_url.setter
  def link_url(self, link_url: Optional[str]):
    if link_url is None:
      del self.link_url
      return
    if not isinstance(link_url, str):
      raise TypeError('link_url must be of type str')
    self._link_url = link_url

  @property
  def live(self) -> bool:
    """Whether this is a currently active livestream"""
    return self._live or False

  @live.setter
  def live(self, live: Optional[bool]):
    if live is None:
      del self.live
      return
    if not isinstance(live, bool):
      raise TypeError('live must be of type bool')
    self._live = live

  @property
  def featured(self) -> bool:
    """Whether this should be the 'featured' (prominently displayed) stream"""
    return self._featured or False

  @featured.setter
  def featured(self, featured: Optional[bool]):
    if featured is None:
      del self.featured
      return
    if not isinstance(featured, bool):
      raise TypeError('featured must be of type bool')
    self._featured = featured

  @property
  def schedule_date(self) -> datetime:
    """When the livestream is scheduled for. Just the date is displayed."""
    return self._schedule_date or None

  @schedule_date.setter
  def schedule_date(self, schedule_date: Optional[datetime]):
    if schedule_date is None:
      del self.schedule_date
      return
    if not isinstance(schedule_date, datetime):
      raise TypeError('schedule_date must be of type datetime')
    self._schedule_date = schedule_date


class BenchmarkTask(KaggleObject):
  r"""
  Attributes:
    id (int)
      ID of the BenchmarkTask from the DB
    type (BenchmarkTaskType)
      Differentiates between Personal/Research
    version (BenchmarkTaskVersion)
      Nested information for the specific version being requested
    update_time (datetime)
    definition_type (BenchmarkTaskDefinitionType)
      Forward-thinking to a world where we support beyond Kaggle Notebooks. This
      value would be determined at the Top Level Task.
    owner_user_id (int)
    owner_user (UserAvatar)
    source_kernel_id (int)
      The Kernel associated to the `version.source_kernel_session_id`
    slug (str)
      Unique dash-seperated slug for this task
    vote_count (int)
      Voting information for this task
    has_up_voted (bool)
    forum_id (int)
      Discussion forum
    is_public (bool)
    can_administer (bool)
    permissions (Permissions)
      Permissions for the user fetching the task
    categories (TagList)
    latest_version_number (int)
    kernel_permissions (Permissions)
      Permissions for the underlying kernel
    view_count (int)
      How many total views the benchmark task has received.
  """

  def __init__(self):
    self._id = 0
    self._type = BenchmarkTaskType.BENCHMARK_TASK_TYPE_UNSPECIFIED
    self._version = None
    self._update_time = None
    self._definition_type = None
    self._owner_user_id = None
    self._owner_user = None
    self._source_kernel_id = None
    self._slug = None
    self._vote_count = None
    self._has_up_voted = None
    self._forum_id = None
    self._is_public = None
    self._can_administer = None
    self._permissions = None
    self._categories = None
    self._latest_version_number = None
    self._kernel_permissions = None
    self._view_count = None
    self._freeze()

  @property
  def id(self) -> int:
    """ID of the BenchmarkTask from the DB"""
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
  def type(self) -> 'BenchmarkTaskType':
    """Differentiates between Personal/Research"""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkTaskType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkTaskType):
      raise TypeError('type must be of type BenchmarkTaskType')
    self._type = type

  @property
  def version(self) -> Optional['BenchmarkTaskVersion']:
    """Nested information for the specific version being requested"""
    return self._version

  @version.setter
  def version(self, version: Optional['BenchmarkTaskVersion']):
    if version is None:
      del self.version
      return
    if not isinstance(version, BenchmarkTaskVersion):
      raise TypeError('version must be of type BenchmarkTaskVersion')
    self._version = version

  @property
  def update_time(self) -> datetime:
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def definition_type(self) -> 'BenchmarkTaskDefinitionType':
    r"""
    Forward-thinking to a world where we support beyond Kaggle Notebooks. This
    value would be determined at the Top Level Task.
    """
    return self._definition_type or BenchmarkTaskDefinitionType.BENCHMARK_TASK_DEFINITION_TYPE_UNSPECIFIED

  @definition_type.setter
  def definition_type(self, definition_type: Optional['BenchmarkTaskDefinitionType']):
    if definition_type is None:
      del self.definition_type
      return
    if not isinstance(definition_type, BenchmarkTaskDefinitionType):
      raise TypeError('definition_type must be of type BenchmarkTaskDefinitionType')
    self._definition_type = definition_type

  @property
  def owner_user_id(self) -> int:
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional[Optional['UserAvatar']]):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    self._owner_user = owner_user

  @property
  def source_kernel_id(self) -> int:
    """The Kernel associated to the `version.source_kernel_session_id`"""
    return self._source_kernel_id or 0

  @source_kernel_id.setter
  def source_kernel_id(self, source_kernel_id: Optional[int]):
    if source_kernel_id is None:
      del self.source_kernel_id
      return
    if not isinstance(source_kernel_id, int):
      raise TypeError('source_kernel_id must be of type int')
    self._source_kernel_id = source_kernel_id

  @property
  def slug(self) -> str:
    """Unique dash-seperated slug for this task"""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def vote_count(self) -> int:
    """Voting information for this task"""
    return self._vote_count or 0

  @vote_count.setter
  def vote_count(self, vote_count: Optional[int]):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def has_up_voted(self) -> bool:
    return self._has_up_voted or False

  @has_up_voted.setter
  def has_up_voted(self, has_up_voted: Optional[bool]):
    if has_up_voted is None:
      del self.has_up_voted
      return
    if not isinstance(has_up_voted, bool):
      raise TypeError('has_up_voted must be of type bool')
    self._has_up_voted = has_up_voted

  @property
  def forum_id(self) -> int:
    """Discussion forum"""
    return self._forum_id or 0

  @forum_id.setter
  def forum_id(self, forum_id: Optional[int]):
    if forum_id is None:
      del self.forum_id
      return
    if not isinstance(forum_id, int):
      raise TypeError('forum_id must be of type int')
    self._forum_id = forum_id

  @property
  def is_public(self) -> bool:
    return self._is_public or False

  @is_public.setter
  def is_public(self, is_public: Optional[bool]):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def permissions(self) -> Optional['Permissions']:
    """Permissions for the user fetching the task"""
    return self._permissions or None

  @permissions.setter
  def permissions(self, permissions: Optional[Optional['Permissions']]):
    if permissions is None:
      del self.permissions
      return
    if not isinstance(permissions, Permissions):
      raise TypeError('permissions must be of type Permissions')
    self._permissions = permissions

  @property
  def kernel_permissions(self) -> Optional['Permissions']:
    """Permissions for the underlying kernel"""
    return self._kernel_permissions or None

  @kernel_permissions.setter
  def kernel_permissions(self, kernel_permissions: Optional[Optional['Permissions']]):
    if kernel_permissions is None:
      del self.kernel_permissions
      return
    if not isinstance(kernel_permissions, Permissions):
      raise TypeError('kernel_permissions must be of type Permissions')
    self._kernel_permissions = kernel_permissions

  @property
  def can_administer(self) -> bool:
    return self._can_administer or False

  @can_administer.setter
  def can_administer(self, can_administer: Optional[bool]):
    if can_administer is None:
      del self.can_administer
      return
    if not isinstance(can_administer, bool):
      raise TypeError('can_administer must be of type bool')
    self._can_administer = can_administer

  @property
  def categories(self) -> Optional['TagList']:
    return self._categories or None

  @categories.setter
  def categories(self, categories: Optional[Optional['TagList']]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, TagList):
      raise TypeError('categories must be of type TagList')
    self._categories = categories

  @property
  def latest_version_number(self) -> int:
    return self._latest_version_number or 0

  @latest_version_number.setter
  def latest_version_number(self, latest_version_number: Optional[int]):
    if latest_version_number is None:
      del self.latest_version_number
      return
    if not isinstance(latest_version_number, int):
      raise TypeError('latest_version_number must be of type int')
    self._latest_version_number = latest_version_number

  @property
  def view_count(self) -> int:
    """How many total views the benchmark task has received."""
    return self._view_count or 0

  @view_count.setter
  def view_count(self, view_count: Optional[int]):
    if view_count is None:
      del self.view_count
      return
    if not isinstance(view_count, int):
      raise TypeError('view_count must be of type int')
    self._view_count = view_count


class BenchmarkTaskCitation(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
    url (str)
  """

  def __init__(self):
    self._id = None
    self._title = None
    self._url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class BenchmarkTaskRun(KaggleObject):
  r"""
  Represents the invocation of a benchmark task version. All fields are
  immutable.

  Attributes:
    id (int)
      The ID of the run from the database.
      This is used for top-level runs that have been persisted.
    manual_user_id (int)
      If included, indicates that this run was manually entered by this user id.
    task_version (BenchmarkTaskVersion)
      The parent task version that was invoked. For create flows, only the ID
      value is used.
    model_version (BenchmarkModelVersion)
      The benchmark model version that was evaluated against. For create flows,
      only the ID value is used.
      For the main Personal Benchmarks view, this will be useful to correlate
      the predetermined columns. For the Task detail view, this will help
      determine the models to represent in the left sidebar.
    result (BenchmarkResult)
      The result of the run. NOTE: This is a field and proto that is serialized
      into/out of JSON from the DB. It's currently used by Research Benchmarks.
      We'll leave this untouched for Personal Benchmarks, where we'll use the
      'results' field.
    state (BenchmarkTaskRunState)
    start_time (datetime)
    end_time (datetime)
    conversations (Conversation)
      Conversations between various roles in LLM interactions. Nested within
      these conversations is the content needed to build the 'output' section for
      various visualizations.
    results (BenchmarkTaskRunResult)
      This captures the aggregated results for the task (as well as any
      public/private split results when applicable)
    assertions (BenchmarkTaskRunAssertion)
      If applicable, any assertions made during the run. Note that any tasks that
      produce purely numerical values likely won't have assertions.
    subruns (BenchmarkTaskRun)
    py_run_id (str)
      The ID of the run as generated by the Python library.
      This is used for:
       1. New top-level runs that have not yet been persisted to the database.
       2. Sub-task runs, which may not have a corresponding database ID.
    error_message (str)
      details if the run errored out.
    creator_user_id (int)
      The user who triggered the creation of this run
    output_kernel_session_id (int)
      Kernel session associated with this run
  """

  def __init__(self):
    self._id = None
    self._manual_user_id = None
    self._task_version = None
    self._model_version = None
    self._result = None
    self._state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._start_time = None
    self._end_time = None
    self._conversations = []
    self._results = []
    self._assertions = []
    self._subruns = []
    self._py_run_id = None
    self._error_message = None
    self._creator_user_id = None
    self._output_kernel_session_id = None
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    The ID of the run from the database.
    This is used for top-level runs that have been persisted.
    """
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    del self.py_run_id
    self._id = id

  @property
  def py_run_id(self) -> str:
    r"""
    The ID of the run as generated by the Python library.
    This is used for:
     1. New top-level runs that have not yet been persisted to the database.
     2. Sub-task runs, which may not have a corresponding database ID.
    """
    return self._py_run_id or ""

  @py_run_id.setter
  def py_run_id(self, py_run_id: str):
    if py_run_id is None:
      del self.py_run_id
      return
    if not isinstance(py_run_id, str):
      raise TypeError('py_run_id must be of type str')
    del self.id
    self._py_run_id = py_run_id

  @property
  def manual_user_id(self) -> int:
    """If included, indicates that this run was manually entered by this user id."""
    return self._manual_user_id or 0

  @manual_user_id.setter
  def manual_user_id(self, manual_user_id: Optional[int]):
    if manual_user_id is None:
      del self.manual_user_id
      return
    if not isinstance(manual_user_id, int):
      raise TypeError('manual_user_id must be of type int')
    self._manual_user_id = manual_user_id

  @property
  def task_version(self) -> Optional['BenchmarkTaskVersion']:
    r"""
    The parent task version that was invoked. For create flows, only the ID
    value is used.
    """
    return self._task_version

  @task_version.setter
  def task_version(self, task_version: Optional['BenchmarkTaskVersion']):
    if task_version is None:
      del self.task_version
      return
    if not isinstance(task_version, BenchmarkTaskVersion):
      raise TypeError('task_version must be of type BenchmarkTaskVersion')
    self._task_version = task_version

  @property
  def model_version(self) -> Optional['BenchmarkModelVersion']:
    r"""
    The benchmark model version that was evaluated against. For create flows,
    only the ID value is used.
    For the main Personal Benchmarks view, this will be useful to correlate
    the predetermined columns. For the Task detail view, this will help
    determine the models to represent in the left sidebar.
    """
    return self._model_version

  @model_version.setter
  def model_version(self, model_version: Optional['BenchmarkModelVersion']):
    if model_version is None:
      del self.model_version
      return
    if not isinstance(model_version, BenchmarkModelVersion):
      raise TypeError('model_version must be of type BenchmarkModelVersion')
    self._model_version = model_version

  @property
  def result(self) -> Optional['BenchmarkResult']:
    r"""
    The result of the run. NOTE: This is a field and proto that is serialized
    into/out of JSON from the DB. It's currently used by Research Benchmarks.
    We'll leave this untouched for Personal Benchmarks, where we'll use the
    'results' field.
    """
    return self._result

  @result.setter
  def result(self, result: Optional['BenchmarkResult']):
    if result is None:
      del self.result
      return
    if not isinstance(result, BenchmarkResult):
      raise TypeError('result must be of type BenchmarkResult')
    self._result = result

  @property
  def state(self) -> 'BenchmarkTaskRunState':
    return self._state

  @state.setter
  def state(self, state: 'BenchmarkTaskRunState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, BenchmarkTaskRunState):
      raise TypeError('state must be of type BenchmarkTaskRunState')
    self._state = state

  @property
  def start_time(self) -> datetime:
    return self._start_time

  @start_time.setter
  def start_time(self, start_time: datetime):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    return self._end_time

  @end_time.setter
  def end_time(self, end_time: datetime):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time

  @property
  def conversations(self) -> Optional[List[Optional['Conversation']]]:
    r"""
    Conversations between various roles in LLM interactions. Nested within
    these conversations is the content needed to build the 'output' section for
    various visualizations.
    """
    return self._conversations

  @conversations.setter
  def conversations(self, conversations: Optional[List[Optional['Conversation']]]):
    if conversations is None:
      del self.conversations
      return
    if not isinstance(conversations, list):
      raise TypeError('conversations must be of type list')
    if not all([isinstance(t, Conversation) for t in conversations]):
      raise TypeError('conversations must contain only items of type Conversation')
    self._conversations = conversations

  @property
  def results(self) -> Optional[List[Optional['BenchmarkTaskRunResult']]]:
    r"""
    This captures the aggregated results for the task (as well as any
    public/private split results when applicable)
    """
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['BenchmarkTaskRunResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, BenchmarkTaskRunResult) for t in results]):
      raise TypeError('results must contain only items of type BenchmarkTaskRunResult')
    self._results = results

  @property
  def assertions(self) -> Optional[List[Optional['BenchmarkTaskRunAssertion']]]:
    r"""
    If applicable, any assertions made during the run. Note that any tasks that
    produce purely numerical values likely won't have assertions.
    """
    return self._assertions

  @assertions.setter
  def assertions(self, assertions: Optional[List[Optional['BenchmarkTaskRunAssertion']]]):
    if assertions is None:
      del self.assertions
      return
    if not isinstance(assertions, list):
      raise TypeError('assertions must be of type list')
    if not all([isinstance(t, BenchmarkTaskRunAssertion) for t in assertions]):
      raise TypeError('assertions must contain only items of type BenchmarkTaskRunAssertion')
    self._assertions = assertions

  @property
  def subruns(self) -> Optional[List[Optional['BenchmarkTaskRun']]]:
    return self._subruns

  @subruns.setter
  def subruns(self, subruns: Optional[List[Optional['BenchmarkTaskRun']]]):
    if subruns is None:
      del self.subruns
      return
    if not isinstance(subruns, list):
      raise TypeError('subruns must be of type list')
    if not all([isinstance(t, BenchmarkTaskRun) for t in subruns]):
      raise TypeError('subruns must contain only items of type BenchmarkTaskRun')
    self._subruns = subruns

  @property
  def error_message(self) -> str:
    """details if the run errored out."""
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def creator_user_id(self) -> int:
    """The user who triggered the creation of this run"""
    return self._creator_user_id or 0

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: Optional[int]):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id

  @property
  def output_kernel_session_id(self) -> int:
    """Kernel session associated with this run"""
    return self._output_kernel_session_id or 0

  @output_kernel_session_id.setter
  def output_kernel_session_id(self, output_kernel_session_id: Optional[int]):
    if output_kernel_session_id is None:
      del self.output_kernel_session_id
      return
    if not isinstance(output_kernel_session_id, int):
      raise TypeError('output_kernel_session_id must be of type int')
    self._output_kernel_session_id = output_kernel_session_id


class BenchmarkTaskRunAssertion(KaggleObject):
  r"""
  Attributes:
    expectation (str)
      Markdown to represent the assertion's expectation
    status (BenchmarkTaskRunAssertionStatus)
    failure_message (str)
      Message used to explain the failure
    line_number (int)
    definition (str)
    conversation_request_ids (ConversationRequestIdentifier)
  """

  def __init__(self):
    self._expectation = ""
    self._status = BenchmarkTaskRunAssertionStatus.BENCHMARK_TASK_RUN_ASSERTION_STATUS_UNSPECIFIED
    self._failure_message = None
    self._line_number = 0
    self._definition = ""
    self._conversation_request_ids = []
    self._freeze()

  @property
  def expectation(self) -> str:
    """Markdown to represent the assertion's expectation"""
    return self._expectation

  @expectation.setter
  def expectation(self, expectation: str):
    if expectation is None:
      del self.expectation
      return
    if not isinstance(expectation, str):
      raise TypeError('expectation must be of type str')
    self._expectation = expectation

  @property
  def status(self) -> 'BenchmarkTaskRunAssertionStatus':
    return self._status

  @status.setter
  def status(self, status: 'BenchmarkTaskRunAssertionStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, BenchmarkTaskRunAssertionStatus):
      raise TypeError('status must be of type BenchmarkTaskRunAssertionStatus')
    self._status = status

  @property
  def failure_message(self) -> str:
    """Message used to explain the failure"""
    return self._failure_message or ""

  @failure_message.setter
  def failure_message(self, failure_message: Optional[str]):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def line_number(self) -> int:
    return self._line_number

  @line_number.setter
  def line_number(self, line_number: int):
    if line_number is None:
      del self.line_number
      return
    if not isinstance(line_number, int):
      raise TypeError('line_number must be of type int')
    self._line_number = line_number

  @property
  def definition(self) -> str:
    return self._definition

  @definition.setter
  def definition(self, definition: str):
    if definition is None:
      del self.definition
      return
    if not isinstance(definition, str):
      raise TypeError('definition must be of type str')
    self._definition = definition

  @property
  def conversation_request_ids(self) -> Optional[List[Optional['ConversationRequestIdentifier']]]:
    return self._conversation_request_ids

  @conversation_request_ids.setter
  def conversation_request_ids(self, conversation_request_ids: Optional[List[Optional['ConversationRequestIdentifier']]]):
    if conversation_request_ids is None:
      del self.conversation_request_ids
      return
    if not isinstance(conversation_request_ids, list):
      raise TypeError('conversation_request_ids must be of type list')
    if not all([isinstance(t, ConversationRequestIdentifier) for t in conversation_request_ids]):
      raise TypeError('conversation_request_ids must contain only items of type ConversationRequestIdentifier')
    self._conversation_request_ids = conversation_request_ids


class BenchmarkTaskRunResult(KaggleObject):
  r"""
  The result of a BenchmarkTaskRun can either be binary (pass/fail) or
  continuous. NOTE: This proto is specifically for use by Personal Benchmarks
  for now and is distinct from the preexisting BenchmarkResult below.

  Attributes:
    type (BenchmarkTaskRunResultType)
      See the BenchmarkTaskRunResultType enum. This helps de-clutter the proto
      where we need to account for public/private splits with their aggregate
      results.
    numeric_result (NumericResult)
    boolean_result (bool)
    total_metrics (ModelUsageMetrics)
      These are the aggregated metrics for all requests to all LLMs--useful for
      understanding the cost of a whole run, especially when quotas come into
      play
    candidate_metrics (ModelUsageMetrics)
      These are the aggregated metrics for requests to the candidate LLM (AKA the
      associated BenchmarkModelVersion)
    assertion_statuses (BenchmarkTaskRunAssertionStatus)
      This is the flattened sequence of assertion statuses from every depth of
      the task run hierarchy
  """

  def __init__(self):
    self._type = BenchmarkTaskRunResultType.BENCHMARK_TASK_RUN_RESULT_TYPE_UNSPECIFIED
    self._numeric_result = None
    self._boolean_result = None
    self._total_metrics = None
    self._candidate_metrics = None
    self._assertion_statuses = []
    self._freeze()

  @property
  def type(self) -> 'BenchmarkTaskRunResultType':
    r"""
    See the BenchmarkTaskRunResultType enum. This helps de-clutter the proto
    where we need to account for public/private splits with their aggregate
    results.
    """
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkTaskRunResultType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkTaskRunResultType):
      raise TypeError('type must be of type BenchmarkTaskRunResultType')
    self._type = type

  @property
  def numeric_result(self) -> Optional['NumericResult']:
    return self._numeric_result or None

  @numeric_result.setter
  def numeric_result(self, numeric_result: Optional['NumericResult']):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, NumericResult):
      raise TypeError('numeric_result must be of type NumericResult')
    del self.boolean_result
    self._numeric_result = numeric_result

  @property
  def boolean_result(self) -> bool:
    return self._boolean_result or False

  @boolean_result.setter
  def boolean_result(self, boolean_result: bool):
    if boolean_result is None:
      del self.boolean_result
      return
    if not isinstance(boolean_result, bool):
      raise TypeError('boolean_result must be of type bool')
    del self.numeric_result
    self._boolean_result = boolean_result

  @property
  def total_metrics(self) -> Optional['ModelUsageMetrics']:
    r"""
    These are the aggregated metrics for all requests to all LLMs--useful for
    understanding the cost of a whole run, especially when quotas come into
    play
    """
    return self._total_metrics or None

  @total_metrics.setter
  def total_metrics(self, total_metrics: Optional[Optional['ModelUsageMetrics']]):
    if total_metrics is None:
      del self.total_metrics
      return
    if not isinstance(total_metrics, ModelUsageMetrics):
      raise TypeError('total_metrics must be of type ModelUsageMetrics')
    self._total_metrics = total_metrics

  @property
  def candidate_metrics(self) -> Optional['ModelUsageMetrics']:
    r"""
    These are the aggregated metrics for requests to the candidate LLM (AKA the
    associated BenchmarkModelVersion)
    """
    return self._candidate_metrics or None

  @candidate_metrics.setter
  def candidate_metrics(self, candidate_metrics: Optional[Optional['ModelUsageMetrics']]):
    if candidate_metrics is None:
      del self.candidate_metrics
      return
    if not isinstance(candidate_metrics, ModelUsageMetrics):
      raise TypeError('candidate_metrics must be of type ModelUsageMetrics')
    self._candidate_metrics = candidate_metrics

  @property
  def assertion_statuses(self) -> Optional[List['BenchmarkTaskRunAssertionStatus']]:
    r"""
    This is the flattened sequence of assertion statuses from every depth of
    the task run hierarchy
    """
    return self._assertion_statuses

  @assertion_statuses.setter
  def assertion_statuses(self, assertion_statuses: Optional[List['BenchmarkTaskRunAssertionStatus']]):
    if assertion_statuses is None:
      del self.assertion_statuses
      return
    if not isinstance(assertion_statuses, list):
      raise TypeError('assertion_statuses must be of type list')
    if not all([isinstance(t, BenchmarkTaskRunAssertionStatus) for t in assertion_statuses]):
      raise TypeError('assertion_statuses must contain only items of type BenchmarkTaskRunAssertionStatus')
    self._assertion_statuses = assertion_statuses


class BenchmarkTaskVersion(KaggleObject):
  r"""
  Optional fields would be missing for Subtasks, which have no DB
  representation but will have a 'virtual' representation of a Task.

  Attributes:
    id (int)
      The ID of the BenchmarkTaskVersion from the DB. This would change
      whenever the definition of the Benchmark changes (i.e. new notebook version
      or promptfoo config update).
    task_id (int)
      ID of the 'container' BenchmarkTask
    version_number (int)
      The semantic version number that increments from/by 1 as the definition
      changes
    name (str)
      The user-provided name/description for the task. We won't have this for
      Research Benchmarks (at least not initially).
    description (str)
    definition (str)
      The code/configuration that defines the task. We won't have this for
      Research Benchmarks (at least not initially).
    source_kernel_session_id (int)
      The KernelSession that produced this task version's definition
    aggregation_type (BenchmarkTaskVersionAggregationType)
      If specified, indicates that this is an aggregation task version. This
      field specifies how aggregation of child task version run results is done.
    child_task_versions (BenchmarkTaskVersion)
      If applicable, the direct children of this TaskVersion (with no further
      depth included). In practice (for the MVP), this will only be used to load
      Top Level TaskVersions, meaning that this TaskVersion instance is a Root
      Task. Any other further nested TaskVersion information will only be
      accessible via the parent Task's `runs` field.

      NOTE: this field is not set by the SDK mapper and must be populated
      separately. This is done to avoid unnecessary overhead as most fetchers do
      not need this field.
    owner_user (UserAvatar)
      Owner of the parent task
    type (BenchmarkTaskType)
      Type of the parent task
    is_public (bool)
      TaskVersion publicity is tied to the parent task publicity.
    parent_task_version_ids (int)
      Parent task version ids.

      NOTE: this field is not set by the SDK mapper and must be populated
      separately. This is done to avoid unnecessary overhead as most fetchers do
      not need this field.
    display_type (BenchmarkLeaderboardDisplayType)
      Determines how to render values in this task version's leaderboard column.
      Defaults to percentage.
      If this task version gets mapped as a child of another task version, the
      display type is determined at the mapping level.
    source_kernel_id (int)
      Source kernel ID from the parent benchmark task
    permissions (Permissions)
      Permissions for the user fetching the task
    details (str)
    slug (str)
      Task slug
    create_time (datetime)
    precision (int)
      Number of decimal places to display for numeric display types.
      This value is always present - the default is 1 (from the database).
    sort_order (SortOrder)
      Default sort order for leaderboard results on this task version.
    provenance_sources (str)
      User-specified provenance sources text
    citations (BenchmarkTaskCitation)
      Citations associated with this benchmark task version
    citation (BenchmarkBibtexCitation)
      BibTeX citation for this benchmark task version.
  """

  def __init__(self):
    self._id = 0
    self._task_id = None
    self._version_number = None
    self._name = None
    self._description = None
    self._definition = None
    self._source_kernel_session_id = None
    self._aggregation_type = None
    self._child_task_versions = []
    self._owner_user = None
    self._type = BenchmarkTaskType.BENCHMARK_TASK_TYPE_UNSPECIFIED
    self._is_public = None
    self._parent_task_version_ids = []
    self._display_type = BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED
    self._source_kernel_id = None
    self._permissions = None
    self._details = None
    self._slug = None
    self._create_time = None
    self._precision = 0
    self._sort_order = SortOrder.SORT_ORDER_UNSPECIFIED
    self._provenance_sources = None
    self._citations = []
    self._citation = None
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    The ID of the BenchmarkTaskVersion from the DB. This would change
    whenever the definition of the Benchmark changes (i.e. new notebook version
    or promptfoo config update).
    """
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
  def task_id(self) -> int:
    """ID of the 'container' BenchmarkTask"""
    return self._task_id or 0

  @task_id.setter
  def task_id(self, task_id: Optional[int]):
    if task_id is None:
      del self.task_id
      return
    if not isinstance(task_id, int):
      raise TypeError('task_id must be of type int')
    self._task_id = task_id

  @property
  def version_number(self) -> int:
    r"""
    The semantic version number that increments from/by 1 as the definition
    changes
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def name(self) -> str:
    r"""
    The user-provided name/description for the task. We won't have this for
    Research Benchmarks (at least not initially).
    """
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def description(self) -> str:
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def display_type(self) -> 'BenchmarkLeaderboardDisplayType':
    r"""
    Determines how to render values in this task version's leaderboard column.
    Defaults to percentage.
    If this task version gets mapped as a child of another task version, the
    display type is determined at the mapping level.
    """
    return self._display_type

  @display_type.setter
  def display_type(self, display_type: 'BenchmarkLeaderboardDisplayType'):
    if display_type is None:
      del self.display_type
      return
    if not isinstance(display_type, BenchmarkLeaderboardDisplayType):
      raise TypeError('display_type must be of type BenchmarkLeaderboardDisplayType')
    self._display_type = display_type

  @property
  def definition(self) -> str:
    r"""
    The code/configuration that defines the task. We won't have this for
    Research Benchmarks (at least not initially).
    """
    return self._definition or ""

  @definition.setter
  def definition(self, definition: Optional[str]):
    if definition is None:
      del self.definition
      return
    if not isinstance(definition, str):
      raise TypeError('definition must be of type str')
    self._definition = definition

  @property
  def source_kernel_session_id(self) -> int:
    """The KernelSession that produced this task version's definition"""
    return self._source_kernel_session_id or 0

  @source_kernel_session_id.setter
  def source_kernel_session_id(self, source_kernel_session_id: Optional[int]):
    if source_kernel_session_id is None:
      del self.source_kernel_session_id
      return
    if not isinstance(source_kernel_session_id, int):
      raise TypeError('source_kernel_session_id must be of type int')
    self._source_kernel_session_id = source_kernel_session_id

  @property
  def aggregation_type(self) -> 'BenchmarkTaskVersionAggregationType':
    r"""
    If specified, indicates that this is an aggregation task version. This
    field specifies how aggregation of child task version run results is done.
    """
    return self._aggregation_type or BenchmarkTaskVersionAggregationType.BENCHMARK_TASK_VERSION_AGGREGATION_TYPE_UNSPECIFIED

  @aggregation_type.setter
  def aggregation_type(self, aggregation_type: Optional['BenchmarkTaskVersionAggregationType']):
    if aggregation_type is None:
      del self.aggregation_type
      return
    if not isinstance(aggregation_type, BenchmarkTaskVersionAggregationType):
      raise TypeError('aggregation_type must be of type BenchmarkTaskVersionAggregationType')
    self._aggregation_type = aggregation_type

  @property
  def child_task_versions(self) -> Optional[List[Optional['BenchmarkTaskVersion']]]:
    r"""
    If applicable, the direct children of this TaskVersion (with no further
    depth included). In practice (for the MVP), this will only be used to load
    Top Level TaskVersions, meaning that this TaskVersion instance is a Root
    Task. Any other further nested TaskVersion information will only be
    accessible via the parent Task's `runs` field.

    NOTE: this field is not set by the SDK mapper and must be populated
    separately. This is done to avoid unnecessary overhead as most fetchers do
    not need this field.
    """
    return self._child_task_versions

  @child_task_versions.setter
  def child_task_versions(self, child_task_versions: Optional[List[Optional['BenchmarkTaskVersion']]]):
    if child_task_versions is None:
      del self.child_task_versions
      return
    if not isinstance(child_task_versions, list):
      raise TypeError('child_task_versions must be of type list')
    if not all([isinstance(t, BenchmarkTaskVersion) for t in child_task_versions]):
      raise TypeError('child_task_versions must contain only items of type BenchmarkTaskVersion')
    self._child_task_versions = child_task_versions

  @property
  def parent_task_version_ids(self) -> Optional[List[int]]:
    r"""
    Parent task version ids.

    NOTE: this field is not set by the SDK mapper and must be populated
    separately. This is done to avoid unnecessary overhead as most fetchers do
    not need this field.
    """
    return self._parent_task_version_ids

  @parent_task_version_ids.setter
  def parent_task_version_ids(self, parent_task_version_ids: Optional[List[int]]):
    if parent_task_version_ids is None:
      del self.parent_task_version_ids
      return
    if not isinstance(parent_task_version_ids, list):
      raise TypeError('parent_task_version_ids must be of type list')
    if not all([isinstance(t, int) for t in parent_task_version_ids]):
      raise TypeError('parent_task_version_ids must contain only items of type int')
    self._parent_task_version_ids = parent_task_version_ids

  @property
  def is_public(self) -> bool:
    """TaskVersion publicity is tied to the parent task publicity."""
    return self._is_public or False

  @is_public.setter
  def is_public(self, is_public: Optional[bool]):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    """Owner of the parent task"""
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional[Optional['UserAvatar']]):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    self._owner_user = owner_user

  @property
  def type(self) -> 'BenchmarkTaskType':
    """Type of the parent task"""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkTaskType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkTaskType):
      raise TypeError('type must be of type BenchmarkTaskType')
    self._type = type

  @property
  def permissions(self) -> Optional['Permissions']:
    """Permissions for the user fetching the task"""
    return self._permissions or None

  @permissions.setter
  def permissions(self, permissions: Optional[Optional['Permissions']]):
    if permissions is None:
      del self.permissions
      return
    if not isinstance(permissions, Permissions):
      raise TypeError('permissions must be of type Permissions')
    self._permissions = permissions

  @property
  def details(self) -> str:
    return self._details or ""

  @details.setter
  def details(self, details: Optional[str]):
    if details is None:
      del self.details
      return
    if not isinstance(details, str):
      raise TypeError('details must be of type str')
    self._details = details

  @property
  def slug(self) -> str:
    """Task slug"""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def create_time(self) -> datetime:
    return self._create_time or None

  @create_time.setter
  def create_time(self, create_time: Optional[datetime]):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def precision(self) -> int:
    r"""
    Number of decimal places to display for numeric display types.
    This value is always present - the default is 1 (from the database).
    """
    return self._precision

  @precision.setter
  def precision(self, precision: int):
    if precision is None:
      del self.precision
      return
    if not isinstance(precision, int):
      raise TypeError('precision must be of type int')
    self._precision = precision

  @property
  def sort_order(self) -> 'SortOrder':
    """Default sort order for leaderboard results on this task version."""
    return self._sort_order

  @sort_order.setter
  def sort_order(self, sort_order: 'SortOrder'):
    if sort_order is None:
      del self.sort_order
      return
    if not isinstance(sort_order, SortOrder):
      raise TypeError('sort_order must be of type SortOrder')
    self._sort_order = sort_order

  @property
  def provenance_sources(self) -> str:
    """User-specified provenance sources text"""
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: Optional[str]):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def citations(self) -> Optional[List[Optional['BenchmarkTaskCitation']]]:
    """Citations associated with this benchmark task version"""
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['BenchmarkTaskCitation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, BenchmarkTaskCitation) for t in citations]):
      raise TypeError('citations must contain only items of type BenchmarkTaskCitation')
    self._citations = citations

  @property
  def source_kernel_id(self) -> int:
    """Source kernel ID from the parent benchmark task"""
    return self._source_kernel_id or 0

  @source_kernel_id.setter
  def source_kernel_id(self, source_kernel_id: Optional[int]):
    if source_kernel_id is None:
      del self.source_kernel_id
      return
    if not isinstance(source_kernel_id, int):
      raise TypeError('source_kernel_id must be of type int')
    self._source_kernel_id = source_kernel_id

  @property
  def citation(self) -> Optional['BenchmarkBibtexCitation']:
    """BibTeX citation for this benchmark task version."""
    return self._citation or None

  @citation.setter
  def citation(self, citation: Optional[Optional['BenchmarkBibtexCitation']]):
    if citation is None:
      del self.citation
      return
    if not isinstance(citation, BenchmarkBibtexCitation):
      raise TypeError('citation must be of type BenchmarkBibtexCitation')
    self._citation = citation


class BenchmarkTaskVersionMapping(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id for the mapping, note: parent and child id pairs are unique and can also
      function together as a unique identifier.
    parent_task_version_id (int)
      The parent task version.
    child_task_version_id (int)
      The child task version.
    type (BenchmarkTaskVersionMappingType)
      The mapping type. Determines the child task version's precedence in
      aggregate calculation, UI styling and sorting. Defaults to PRIMARY if
      not set.
    priority (int)
      The order in which this child task version is displayed (relative to
      other mapped child task versions). Lowest priority if NULL.
    secondary_sort_task_version_id (int)
      An additional task version to sort by for tie-breaking. Will have no
      effect if the specified task version is not also mapped.
    column_name (str)
      The display name for the child task on leaderboards its mapped to.
    display_type (BenchmarkLeaderboardDisplayType)
      The display type for this results from this mapped TaskVersion.
    sorting_priority (int)
      The ordering for the default task version for sorting (highest is
      selected and priority will be used as a tie-breaker). Lowest priority if
      NULL.
    weight (float)
      If used in average calculations, the weight for this mapped TaskVersion.
    remove_time (datetime)
      Time the mapping was deleted, null if it is not deleted
    precision (int)
      Number of decimal places to display for numeric display types.
      This value is always present - the default is 1 (from the database).
    sort_order (SortOrder)
      Default sort order for leaderboard results on this mapped task version.
  """

  def __init__(self):
    self._id = 0
    self._parent_task_version_id = 0
    self._child_task_version_id = 0
    self._type = BenchmarkTaskVersionMappingType.BENCHMARK_TASK_VERSION_MAPPING_TYPE_UNSPECIFIED
    self._priority = None
    self._secondary_sort_task_version_id = None
    self._column_name = None
    self._display_type = BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED
    self._sorting_priority = None
    self._weight = None
    self._remove_time = None
    self._precision = 0
    self._sort_order = SortOrder.SORT_ORDER_UNSPECIFIED
    self._freeze()

  @property
  def id(self) -> int:
    r"""
    Id for the mapping, note: parent and child id pairs are unique and can also
    function together as a unique identifier.
    """
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
  def parent_task_version_id(self) -> int:
    """The parent task version."""
    return self._parent_task_version_id

  @parent_task_version_id.setter
  def parent_task_version_id(self, parent_task_version_id: int):
    if parent_task_version_id is None:
      del self.parent_task_version_id
      return
    if not isinstance(parent_task_version_id, int):
      raise TypeError('parent_task_version_id must be of type int')
    self._parent_task_version_id = parent_task_version_id

  @property
  def child_task_version_id(self) -> int:
    """The child task version."""
    return self._child_task_version_id

  @child_task_version_id.setter
  def child_task_version_id(self, child_task_version_id: int):
    if child_task_version_id is None:
      del self.child_task_version_id
      return
    if not isinstance(child_task_version_id, int):
      raise TypeError('child_task_version_id must be of type int')
    self._child_task_version_id = child_task_version_id

  @property
  def type(self) -> 'BenchmarkTaskVersionMappingType':
    r"""
    The mapping type. Determines the child task version's precedence in
    aggregate calculation, UI styling and sorting. Defaults to PRIMARY if
    not set.
    """
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkTaskVersionMappingType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkTaskVersionMappingType):
      raise TypeError('type must be of type BenchmarkTaskVersionMappingType')
    self._type = type

  @property
  def priority(self) -> int:
    r"""
    The order in which this child task version is displayed (relative to
    other mapped child task versions). Lowest priority if NULL.
    """
    return self._priority or 0

  @priority.setter
  def priority(self, priority: Optional[int]):
    if priority is None:
      del self.priority
      return
    if not isinstance(priority, int):
      raise TypeError('priority must be of type int')
    self._priority = priority

  @property
  def sorting_priority(self) -> int:
    r"""
    The ordering for the default task version for sorting (highest is
    selected and priority will be used as a tie-breaker). Lowest priority if
    NULL.
    """
    return self._sorting_priority or 0

  @sorting_priority.setter
  def sorting_priority(self, sorting_priority: Optional[int]):
    if sorting_priority is None:
      del self.sorting_priority
      return
    if not isinstance(sorting_priority, int):
      raise TypeError('sorting_priority must be of type int')
    self._sorting_priority = sorting_priority

  @property
  def secondary_sort_task_version_id(self) -> int:
    r"""
    An additional task version to sort by for tie-breaking. Will have no
    effect if the specified task version is not also mapped.
    """
    return self._secondary_sort_task_version_id or 0

  @secondary_sort_task_version_id.setter
  def secondary_sort_task_version_id(self, secondary_sort_task_version_id: Optional[int]):
    if secondary_sort_task_version_id is None:
      del self.secondary_sort_task_version_id
      return
    if not isinstance(secondary_sort_task_version_id, int):
      raise TypeError('secondary_sort_task_version_id must be of type int')
    self._secondary_sort_task_version_id = secondary_sort_task_version_id

  @property
  def column_name(self) -> str:
    """The display name for the child task on leaderboards its mapped to."""
    return self._column_name or ""

  @column_name.setter
  def column_name(self, column_name: Optional[str]):
    if column_name is None:
      del self.column_name
      return
    if not isinstance(column_name, str):
      raise TypeError('column_name must be of type str')
    self._column_name = column_name

  @property
  def display_type(self) -> 'BenchmarkLeaderboardDisplayType':
    """The display type for this results from this mapped TaskVersion."""
    return self._display_type

  @display_type.setter
  def display_type(self, display_type: 'BenchmarkLeaderboardDisplayType'):
    if display_type is None:
      del self.display_type
      return
    if not isinstance(display_type, BenchmarkLeaderboardDisplayType):
      raise TypeError('display_type must be of type BenchmarkLeaderboardDisplayType')
    self._display_type = display_type

  @property
  def precision(self) -> int:
    r"""
    Number of decimal places to display for numeric display types.
    This value is always present - the default is 1 (from the database).
    """
    return self._precision

  @precision.setter
  def precision(self, precision: int):
    if precision is None:
      del self.precision
      return
    if not isinstance(precision, int):
      raise TypeError('precision must be of type int')
    self._precision = precision

  @property
  def weight(self) -> float:
    """If used in average calculations, the weight for this mapped TaskVersion."""
    return self._weight or 0.0

  @weight.setter
  def weight(self, weight: Optional[float]):
    if weight is None:
      del self.weight
      return
    if not isinstance(weight, float):
      raise TypeError('weight must be of type float')
    self._weight = weight

  @property
  def remove_time(self) -> datetime:
    """Time the mapping was deleted, null if it is not deleted"""
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time

  @property
  def sort_order(self) -> 'SortOrder':
    """Default sort order for leaderboard results on this mapped task version."""
    return self._sort_order

  @sort_order.setter
  def sort_order(self, sort_order: 'SortOrder'):
    if sort_order is None:
      del self.sort_order
      return
    if not isinstance(sort_order, SortOrder):
      raise TypeError('sort_order must be of type SortOrder')
    self._sort_order = sort_order


class BenchmarkTopRankingResults(KaggleObject):
  r"""
  Attributes:
    rows (BenchmarkTopRankingResultsRow)
    display_type (BenchmarkLeaderboardDisplayType)
  """

  def __init__(self):
    self._rows = []
    self._display_type = BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def rows(self) -> Optional[List[Optional['BenchmarkTopRankingResultsRow']]]:
    return self._rows

  @rows.setter
  def rows(self, rows: Optional[List[Optional['BenchmarkTopRankingResultsRow']]]):
    if rows is None:
      del self.rows
      return
    if not isinstance(rows, list):
      raise TypeError('rows must be of type list')
    if not all([isinstance(t, BenchmarkTopRankingResultsRow) for t in rows]):
      raise TypeError('rows must contain only items of type BenchmarkTopRankingResultsRow')
    self._rows = rows

  @property
  def display_type(self) -> 'BenchmarkLeaderboardDisplayType':
    return self._display_type

  @display_type.setter
  def display_type(self, display_type: 'BenchmarkLeaderboardDisplayType'):
    if display_type is None:
      del self.display_type
      return
    if not isinstance(display_type, BenchmarkLeaderboardDisplayType):
      raise TypeError('display_type must be of type BenchmarkLeaderboardDisplayType')
    self._display_type = display_type


class BenchmarkTopRankingResultsRow(KaggleObject):
  r"""
  Attributes:
    avatar_url (str)
    model_name (str)
    score (int)
  """

  def __init__(self):
    self._avatar_url = ""
    self._model_name = ""
    self._score = 0
    self._freeze()

  @property
  def avatar_url(self) -> str:
    return self._avatar_url

  @avatar_url.setter
  def avatar_url(self, avatar_url: str):
    if avatar_url is None:
      del self.avatar_url
      return
    if not isinstance(avatar_url, str):
      raise TypeError('avatar_url must be of type str')
    self._avatar_url = avatar_url

  @property
  def model_name(self) -> str:
    return self._model_name

  @model_name.setter
  def model_name(self, model_name: str):
    if model_name is None:
      del self.model_name
      return
    if not isinstance(model_name, str):
      raise TypeError('model_name must be of type str')
    self._model_name = model_name

  @property
  def score(self) -> int:
    return self._score

  @score.setter
  def score(self, score: int):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score


class BenchmarkVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
    benchmark_id (int)
      The parent Benchmark.
      When creating a Benchmark, this field is OUTPUT_ONLY.
      When creating a BenchmarkVersion, this field is REQUIRED.
    version_number (int)
      The version number, relative to the parent benchmark.
    name (str)
      Display name
    description (str)
      Subtitle
    citation (BenchmarkBibtexCitation)
      BibTeX citation fields
    published (bool)
      Whether this benchmark version is publicly visible. This is true iff the
      entity meets all following conditions:
      1) Parent benchmark is published (see benchmark proto)
      2) ContentStateId field set to 'Published'

      Updating this field to true/false will perform the following operations:
      TRUE:
        1) Set the parent Benchmark to published (see benchmark proto)
        2) Set ContentStateId = 'Published'
      FALSE:
        1) Set ContentStateId = 'Draft'
    media (BenchmarkMedia)
      Media associated with the benchmark version
    task_version (BenchmarkTaskVersion)
      The root TaskVersion for this BenchmarkVersion
    publish_time (datetime)
      Time when the version was published
    update_time (datetime)
      Time when the version was updated
    benchmark_model_version_mappings_count (int)
      The number of mapped model versions
    child_benchmark_version_mappings_count (int)
      The number of mapped benchmark versions
    type (BenchmarkType)
      The type of the parent benchmark
    organization (OrganizationCard)
      The associated Organization, if any.
    url (str)
      The url of the benchmark version on kaggle.
    competition_id (int)
      The ID of the competition linked to the parent benchmark
    top_ranking_results (BenchmarkTopRankingResults)
    child_task_version_mappings_count (int)
      The number of mapped task versions
    permissions (Permissions)
    slug (str)
      Benchmark slug
    owner_user (UserAvatar)
      The associated User, if any.
    create_time (datetime)
      Time when the version was created
    maintenance_level (BenchmarkMaintenanceLevel)
      Whether this benchmark version is updated by Kaggle
    citations (BenchmarkTaskCitation)
      Links to external papers or publications related to this benchmark version.
      Distinct from the `citation` field, which holds the BibTeX
      entry for citing the benchmark itself.
    doi (str)
      DOI generated and stored with our DOI provider DataCite.
    authors (BenchmarkAuthor)
      Authors of this benchmark version.
  """

  def __init__(self):
    self._id = 0
    self._benchmark_id = 0
    self._version_number = 0
    self._name = ""
    self._description = ""
    self._citation = None
    self._published = False
    self._media = []
    self._task_version = None
    self._publish_time = None
    self._update_time = None
    self._benchmark_model_version_mappings_count = 0
    self._child_benchmark_version_mappings_count = 0
    self._type = BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED
    self._organization = None
    self._url = None
    self._competition_id = None
    self._top_ranking_results = None
    self._child_task_version_mappings_count = None
    self._permissions = None
    self._slug = None
    self._owner_user = None
    self._create_time = None
    self._maintenance_level = None
    self._citations = []
    self._doi = None
    self._authors = []
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
  def benchmark_id(self) -> int:
    r"""
    The parent Benchmark.
    When creating a Benchmark, this field is OUTPUT_ONLY.
    When creating a BenchmarkVersion, this field is REQUIRED.
    """
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def version_number(self) -> int:
    """The version number, relative to the parent benchmark."""
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def name(self) -> str:
    """Display name"""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def description(self) -> str:
    """Subtitle"""
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
  def citation(self) -> Optional['BenchmarkBibtexCitation']:
    """BibTeX citation fields"""
    return self._citation or None

  @citation.setter
  def citation(self, citation: Optional[Optional['BenchmarkBibtexCitation']]):
    if citation is None:
      del self.citation
      return
    if not isinstance(citation, BenchmarkBibtexCitation):
      raise TypeError('citation must be of type BenchmarkBibtexCitation')
    self._citation = citation

  @property
  def published(self) -> bool:
    r"""
    Whether this benchmark version is publicly visible. This is true iff the
    entity meets all following conditions:
    1) Parent benchmark is published (see benchmark proto)
    2) ContentStateId field set to 'Published'

    Updating this field to true/false will perform the following operations:
    TRUE:
      1) Set the parent Benchmark to published (see benchmark proto)
      2) Set ContentStateId = 'Published'
    FALSE:
      1) Set ContentStateId = 'Draft'
    """
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def media(self) -> Optional[List[Optional['BenchmarkMedia']]]:
    """Media associated with the benchmark version"""
    return self._media

  @media.setter
  def media(self, media: Optional[List[Optional['BenchmarkMedia']]]):
    if media is None:
      del self.media
      return
    if not isinstance(media, list):
      raise TypeError('media must be of type list')
    if not all([isinstance(t, BenchmarkMedia) for t in media]):
      raise TypeError('media must contain only items of type BenchmarkMedia')
    self._media = media

  @property
  def task_version(self) -> Optional['BenchmarkTaskVersion']:
    """The root TaskVersion for this BenchmarkVersion"""
    return self._task_version or None

  @task_version.setter
  def task_version(self, task_version: Optional[Optional['BenchmarkTaskVersion']]):
    if task_version is None:
      del self.task_version
      return
    if not isinstance(task_version, BenchmarkTaskVersion):
      raise TypeError('task_version must be of type BenchmarkTaskVersion')
    self._task_version = task_version

  @property
  def create_time(self) -> datetime:
    """Time when the version was created"""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def publish_time(self) -> datetime:
    """Time when the version was published"""
    return self._publish_time

  @publish_time.setter
  def publish_time(self, publish_time: datetime):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def update_time(self) -> datetime:
    """Time when the version was updated"""
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def benchmark_model_version_mappings_count(self) -> int:
    """The number of mapped model versions"""
    return self._benchmark_model_version_mappings_count

  @benchmark_model_version_mappings_count.setter
  def benchmark_model_version_mappings_count(self, benchmark_model_version_mappings_count: int):
    if benchmark_model_version_mappings_count is None:
      del self.benchmark_model_version_mappings_count
      return
    if not isinstance(benchmark_model_version_mappings_count, int):
      raise TypeError('benchmark_model_version_mappings_count must be of type int')
    self._benchmark_model_version_mappings_count = benchmark_model_version_mappings_count

  @property
  def child_benchmark_version_mappings_count(self) -> int:
    """The number of mapped benchmark versions"""
    return self._child_benchmark_version_mappings_count

  @child_benchmark_version_mappings_count.setter
  def child_benchmark_version_mappings_count(self, child_benchmark_version_mappings_count: int):
    if child_benchmark_version_mappings_count is None:
      del self.child_benchmark_version_mappings_count
      return
    if not isinstance(child_benchmark_version_mappings_count, int):
      raise TypeError('child_benchmark_version_mappings_count must be of type int')
    self._child_benchmark_version_mappings_count = child_benchmark_version_mappings_count

  @property
  def child_task_version_mappings_count(self) -> int:
    """The number of mapped task versions"""
    return self._child_task_version_mappings_count or 0

  @child_task_version_mappings_count.setter
  def child_task_version_mappings_count(self, child_task_version_mappings_count: Optional[int]):
    if child_task_version_mappings_count is None:
      del self.child_task_version_mappings_count
      return
    if not isinstance(child_task_version_mappings_count, int):
      raise TypeError('child_task_version_mappings_count must be of type int')
    self._child_task_version_mappings_count = child_task_version_mappings_count

  @property
  def maintenance_level(self) -> 'BenchmarkMaintenanceLevel':
    """Whether this benchmark version is updated by Kaggle"""
    return self._maintenance_level or BenchmarkMaintenanceLevel.BENCHMARK_MAINTENANCE_LEVEL_UNSPECIFIED

  @maintenance_level.setter
  def maintenance_level(self, maintenance_level: Optional['BenchmarkMaintenanceLevel']):
    if maintenance_level is None:
      del self.maintenance_level
      return
    if not isinstance(maintenance_level, BenchmarkMaintenanceLevel):
      raise TypeError('maintenance_level must be of type BenchmarkMaintenanceLevel')
    self._maintenance_level = maintenance_level

  @property
  def type(self) -> 'BenchmarkType':
    """The type of the parent benchmark"""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkType):
      raise TypeError('type must be of type BenchmarkType')
    self._type = type

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any."""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def url(self) -> str:
    """The url of the benchmark version on kaggle."""
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def competition_id(self) -> int:
    """The ID of the competition linked to the parent benchmark"""
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
  def top_ranking_results(self) -> Optional['BenchmarkTopRankingResults']:
    return self._top_ranking_results or None

  @top_ranking_results.setter
  def top_ranking_results(self, top_ranking_results: Optional[Optional['BenchmarkTopRankingResults']]):
    if top_ranking_results is None:
      del self.top_ranking_results
      return
    if not isinstance(top_ranking_results, BenchmarkTopRankingResults):
      raise TypeError('top_ranking_results must be of type BenchmarkTopRankingResults')
    self._top_ranking_results = top_ranking_results

  @property
  def permissions(self) -> Optional['Permissions']:
    return self._permissions or None

  @permissions.setter
  def permissions(self, permissions: Optional[Optional['Permissions']]):
    if permissions is None:
      del self.permissions
      return
    if not isinstance(permissions, Permissions):
      raise TypeError('permissions must be of type Permissions')
    self._permissions = permissions

  @property
  def slug(self) -> str:
    """Benchmark slug"""
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def owner_user(self) -> Optional['UserAvatar']:
    """The associated User, if any."""
    return self._owner_user or None

  @owner_user.setter
  def owner_user(self, owner_user: Optional[Optional['UserAvatar']]):
    if owner_user is None:
      del self.owner_user
      return
    if not isinstance(owner_user, UserAvatar):
      raise TypeError('owner_user must be of type UserAvatar')
    self._owner_user = owner_user

  @property
  def citations(self) -> Optional[List[Optional['BenchmarkTaskCitation']]]:
    r"""
    Links to external papers or publications related to this benchmark version.
    Distinct from the `citation` field, which holds the BibTeX
    entry for citing the benchmark itself.
    """
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['BenchmarkTaskCitation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, BenchmarkTaskCitation) for t in citations]):
      raise TypeError('citations must contain only items of type BenchmarkTaskCitation')
    self._citations = citations

  @property
  def doi(self) -> str:
    """DOI generated and stored with our DOI provider DataCite."""
    return self._doi or ""

  @doi.setter
  def doi(self, doi: Optional[str]):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi

  @property
  def authors(self) -> Optional[List[Optional['BenchmarkAuthor']]]:
    """Authors of this benchmark version."""
    return self._authors

  @authors.setter
  def authors(self, authors: Optional[List[Optional['BenchmarkAuthor']]]):
    if authors is None:
      del self.authors
      return
    if not isinstance(authors, list):
      raise TypeError('authors must be of type list')
    if not all([isinstance(t, BenchmarkAuthor) for t in authors]):
      raise TypeError('authors must contain only items of type BenchmarkAuthor')
    self._authors = authors


class BenchmarkVersionIdentifier(KaggleObject):
  r"""
  Identifier for selecting a specific benchmark version.

  Attributes:
    version_id_selector (VersionIdSelector)
    published_latest_selector (PublishedLatestSelector)
    version_number_selector (VersionNumberSelector)
    draft_selector (DraftSelector)
    benchmark_slug_selector (BenchmarkSlugSelector)
    latest_selector (LatestSelector)
    latest_visible_selector (LatestVisibleSelector)
  """

  def __init__(self):
    self._version_id_selector = None
    self._published_latest_selector = None
    self._version_number_selector = None
    self._draft_selector = None
    self._benchmark_slug_selector = None
    self._latest_selector = None
    self._latest_visible_selector = None
    self._freeze()

  @property
  def version_id_selector(self) -> Optional['VersionIdSelector']:
    return self._version_id_selector or None

  @version_id_selector.setter
  def version_id_selector(self, version_id_selector: Optional['VersionIdSelector']):
    if version_id_selector is None:
      del self.version_id_selector
      return
    if not isinstance(version_id_selector, VersionIdSelector):
      raise TypeError('version_id_selector must be of type VersionIdSelector')
    del self.published_latest_selector
    del self.version_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    del self.latest_selector
    del self.latest_visible_selector
    self._version_id_selector = version_id_selector

  @property
  def published_latest_selector(self) -> Optional['PublishedLatestSelector']:
    return self._published_latest_selector or None

  @published_latest_selector.setter
  def published_latest_selector(self, published_latest_selector: Optional['PublishedLatestSelector']):
    if published_latest_selector is None:
      del self.published_latest_selector
      return
    if not isinstance(published_latest_selector, PublishedLatestSelector):
      raise TypeError('published_latest_selector must be of type PublishedLatestSelector')
    del self.version_id_selector
    del self.version_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    del self.latest_selector
    del self.latest_visible_selector
    self._published_latest_selector = published_latest_selector

  @property
  def version_number_selector(self) -> Optional['VersionNumberSelector']:
    return self._version_number_selector or None

  @version_number_selector.setter
  def version_number_selector(self, version_number_selector: Optional['VersionNumberSelector']):
    if version_number_selector is None:
      del self.version_number_selector
      return
    if not isinstance(version_number_selector, VersionNumberSelector):
      raise TypeError('version_number_selector must be of type VersionNumberSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    del self.latest_selector
    del self.latest_visible_selector
    self._version_number_selector = version_number_selector

  @property
  def draft_selector(self) -> Optional['DraftSelector']:
    return self._draft_selector or None

  @draft_selector.setter
  def draft_selector(self, draft_selector: Optional['DraftSelector']):
    if draft_selector is None:
      del self.draft_selector
      return
    if not isinstance(draft_selector, DraftSelector):
      raise TypeError('draft_selector must be of type DraftSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.version_number_selector
    del self.benchmark_slug_selector
    del self.latest_selector
    del self.latest_visible_selector
    self._draft_selector = draft_selector

  @property
  def benchmark_slug_selector(self) -> Optional['BenchmarkSlugSelector']:
    return self._benchmark_slug_selector or None

  @benchmark_slug_selector.setter
  def benchmark_slug_selector(self, benchmark_slug_selector: Optional['BenchmarkSlugSelector']):
    if benchmark_slug_selector is None:
      del self.benchmark_slug_selector
      return
    if not isinstance(benchmark_slug_selector, BenchmarkSlugSelector):
      raise TypeError('benchmark_slug_selector must be of type BenchmarkSlugSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.version_number_selector
    del self.draft_selector
    del self.latest_selector
    del self.latest_visible_selector
    self._benchmark_slug_selector = benchmark_slug_selector

  @property
  def latest_selector(self) -> Optional['LatestSelector']:
    return self._latest_selector or None

  @latest_selector.setter
  def latest_selector(self, latest_selector: Optional['LatestSelector']):
    if latest_selector is None:
      del self.latest_selector
      return
    if not isinstance(latest_selector, LatestSelector):
      raise TypeError('latest_selector must be of type LatestSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.version_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    del self.latest_visible_selector
    self._latest_selector = latest_selector

  @property
  def latest_visible_selector(self) -> Optional['LatestVisibleSelector']:
    return self._latest_visible_selector or None

  @latest_visible_selector.setter
  def latest_visible_selector(self, latest_visible_selector: Optional['LatestVisibleSelector']):
    if latest_visible_selector is None:
      del self.latest_visible_selector
      return
    if not isinstance(latest_visible_selector, LatestVisibleSelector):
      raise TypeError('latest_visible_selector must be of type LatestVisibleSelector')
    del self.version_id_selector
    del self.published_latest_selector
    del self.version_number_selector
    del self.draft_selector
    del self.benchmark_slug_selector
    del self.latest_selector
    self._latest_visible_selector = latest_visible_selector


class BenchmarkVersionMapping(KaggleObject):
  r"""
  TODO(bml): Remove after migration to task mappings

  Attributes:
    parent_benchmark_version_id (int)
      The parent benchmark version to map to. This parent benchmark version must
      belong to a SUITE type benchmark.
    child_benchmark_version_id (int)
      The benchmark version to map. This child benchmark version must belong
      to an INDIVIDUAL type benchmark.
    mapping_type (BenchmarkVersionMappingType)
      The mapping type. Determines the child benchmark version's precedence in
      aggregate calculation, UI styling and sorting. Defaults to PRIMARY if
      not set.
    priority (int)
      The order in which this child benchmark version is displayed (relative to
      other mapped child benchmark versions). Lowest priority if NULL.
    secondary_sort_benchmark_version_id (int)
      An additional benchmark version to sort by for tie-breaking. Will have no
      effect if the specified benchmark version is not also mapped. This
      benchmark version must belong to an INDIVIDUAL type benchmark.
  """

  def __init__(self):
    self._parent_benchmark_version_id = 0
    self._child_benchmark_version_id = 0
    self._mapping_type = None
    self._priority = None
    self._secondary_sort_benchmark_version_id = None
    self._freeze()

  @property
  def parent_benchmark_version_id(self) -> int:
    r"""
    The parent benchmark version to map to. This parent benchmark version must
    belong to a SUITE type benchmark.
    """
    return self._parent_benchmark_version_id

  @parent_benchmark_version_id.setter
  def parent_benchmark_version_id(self, parent_benchmark_version_id: int):
    if parent_benchmark_version_id is None:
      del self.parent_benchmark_version_id
      return
    if not isinstance(parent_benchmark_version_id, int):
      raise TypeError('parent_benchmark_version_id must be of type int')
    self._parent_benchmark_version_id = parent_benchmark_version_id

  @property
  def child_benchmark_version_id(self) -> int:
    r"""
    The benchmark version to map. This child benchmark version must belong
    to an INDIVIDUAL type benchmark.
    """
    return self._child_benchmark_version_id

  @child_benchmark_version_id.setter
  def child_benchmark_version_id(self, child_benchmark_version_id: int):
    if child_benchmark_version_id is None:
      del self.child_benchmark_version_id
      return
    if not isinstance(child_benchmark_version_id, int):
      raise TypeError('child_benchmark_version_id must be of type int')
    self._child_benchmark_version_id = child_benchmark_version_id

  @property
  def mapping_type(self) -> 'BenchmarkVersionMappingType':
    r"""
    The mapping type. Determines the child benchmark version's precedence in
    aggregate calculation, UI styling and sorting. Defaults to PRIMARY if
    not set.
    """
    return self._mapping_type or BenchmarkVersionMappingType.BENCHMARK_VERSION_MAPPING_TYPE_UNSPECIFIED

  @mapping_type.setter
  def mapping_type(self, mapping_type: Optional['BenchmarkVersionMappingType']):
    if mapping_type is None:
      del self.mapping_type
      return
    if not isinstance(mapping_type, BenchmarkVersionMappingType):
      raise TypeError('mapping_type must be of type BenchmarkVersionMappingType')
    self._mapping_type = mapping_type

  @property
  def priority(self) -> int:
    r"""
    The order in which this child benchmark version is displayed (relative to
    other mapped child benchmark versions). Lowest priority if NULL.
    """
    return self._priority or 0

  @priority.setter
  def priority(self, priority: Optional[int]):
    if priority is None:
      del self.priority
      return
    if not isinstance(priority, int):
      raise TypeError('priority must be of type int')
    self._priority = priority

  @property
  def secondary_sort_benchmark_version_id(self) -> int:
    r"""
    An additional benchmark version to sort by for tie-breaking. Will have no
    effect if the specified benchmark version is not also mapped. This
    benchmark version must belong to an INDIVIDUAL type benchmark.
    """
    return self._secondary_sort_benchmark_version_id or 0

  @secondary_sort_benchmark_version_id.setter
  def secondary_sort_benchmark_version_id(self, secondary_sort_benchmark_version_id: Optional[int]):
    if secondary_sort_benchmark_version_id is None:
      del self.secondary_sort_benchmark_version_id
      return
    if not isinstance(secondary_sort_benchmark_version_id, int):
      raise TypeError('secondary_sort_benchmark_version_id must be of type int')
    self._secondary_sort_benchmark_version_id = secondary_sort_benchmark_version_id


class BenchmarkVersionModelMapping(KaggleObject):
  r"""
  Attributes:
    id (int)
    parent_benchmark_version_id (int)
      The parent benchmark version to map to.
    child_benchmark_model_version_id (int)
      The benchmark model version to map.
    type (BenchmarkVersionModelMappingType)
      The mapping type.
    remove_time (datetime)
      Time the mapping was deleted, null if it is not deleted
    create_time (datetime)
      Time when the model was added to this benchmark version
  """

  def __init__(self):
    self._id = 0
    self._parent_benchmark_version_id = 0
    self._child_benchmark_model_version_id = 0
    self._type = BenchmarkVersionModelMappingType.BENCHMARK_VERSION_MODEL_MAPPING_TYPE_UNSPECIFIED
    self._remove_time = None
    self._create_time = None
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
  def parent_benchmark_version_id(self) -> int:
    """The parent benchmark version to map to."""
    return self._parent_benchmark_version_id

  @parent_benchmark_version_id.setter
  def parent_benchmark_version_id(self, parent_benchmark_version_id: int):
    if parent_benchmark_version_id is None:
      del self.parent_benchmark_version_id
      return
    if not isinstance(parent_benchmark_version_id, int):
      raise TypeError('parent_benchmark_version_id must be of type int')
    self._parent_benchmark_version_id = parent_benchmark_version_id

  @property
  def child_benchmark_model_version_id(self) -> int:
    """The benchmark model version to map."""
    return self._child_benchmark_model_version_id

  @child_benchmark_model_version_id.setter
  def child_benchmark_model_version_id(self, child_benchmark_model_version_id: int):
    if child_benchmark_model_version_id is None:
      del self.child_benchmark_model_version_id
      return
    if not isinstance(child_benchmark_model_version_id, int):
      raise TypeError('child_benchmark_model_version_id must be of type int')
    self._child_benchmark_model_version_id = child_benchmark_model_version_id

  @property
  def type(self) -> 'BenchmarkVersionModelMappingType':
    """The mapping type."""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkVersionModelMappingType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkVersionModelMappingType):
      raise TypeError('type must be of type BenchmarkVersionModelMappingType')
    self._type = type

  @property
  def remove_time(self) -> datetime:
    """Time the mapping was deleted, null if it is not deleted"""
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time

  @property
  def create_time(self) -> datetime:
    """Time when the model was added to this benchmark version"""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time


class Blob(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      Display name of the blob. Used to provide a label or filename to
      distinguish blobs. It is not currently used in the Gemini
      GenerateContent calls.
    data (bytes)
      Raw bytes from media formats.
      A base64-encoded string in JSON
      (https://protobuf.dev/programming-guides/proto3/#json).
    mime_type (str)
      The IANA standard MIME type of the source data.
  """

  def __init__(self):
    self._display_name = None
    self._data = None
    self._mime_type = None
    self._freeze()

  @property
  def display_name(self) -> str:
    r"""
    Display name of the blob. Used to provide a label or filename to
    distinguish blobs. It is not currently used in the Gemini
    GenerateContent calls.
    """
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def data(self) -> bytes:
    r"""
    Raw bytes from media formats.
    A base64-encoded string in JSON
    (https://protobuf.dev/programming-guides/proto3/#json).
    """
    return self._data or None

  @data.setter
  def data(self, data: Optional[bytes]):
    if data is None:
      del self.data
      return
    if not isinstance(data, bytes):
      raise TypeError('data must be of type bytes')
    self._data = data

  @property
  def mime_type(self) -> str:
    """The IANA standard MIME type of the source data."""
    return self._mime_type or ""

  @mime_type.setter
  def mime_type(self, mime_type: Optional[str]):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type


class Content(KaggleObject):
  r"""
  Contains the multi-parts content of a message.
  Ref: https://ai.google.dev/api/caching#Content

  Attributes:
    parts (Part)
      List of parts that constitute a single message. Each part may have
      a different IANA MIME type.
    role (ContentRole)
    sender_name (str)
      The name of the sender (e.g. the model slug like
      'google/gemini-2.5-flash'). Useful for multi-model conversations where
      different models alternate turns within the same conversation.
  """

  def __init__(self):
    self._parts = []
    self._role = None
    self._sender_name = None
    self._freeze()

  @property
  def parts(self) -> Optional[List[Optional['Part']]]:
    r"""
    List of parts that constitute a single message. Each part may have
    a different IANA MIME type.
    """
    return self._parts

  @parts.setter
  def parts(self, parts: Optional[List[Optional['Part']]]):
    if parts is None:
      del self.parts
      return
    if not isinstance(parts, list):
      raise TypeError('parts must be of type list')
    if not all([isinstance(t, Part) for t in parts]):
      raise TypeError('parts must contain only items of type Part')
    self._parts = parts

  @property
  def role(self) -> 'ContentRole':
    return self._role or ContentRole.CONTENT_ROLE_UNSPECIFIED

  @role.setter
  def role(self, role: Optional['ContentRole']):
    if role is None:
      del self.role
      return
    if not isinstance(role, ContentRole):
      raise TypeError('role must be of type ContentRole')
    self._role = role

  @property
  def sender_name(self) -> str:
    r"""
    The name of the sender (e.g. the model slug like
    'google/gemini-2.5-flash'). Useful for multi-model conversations where
    different models alternate turns within the same conversation.
    """
    return self._sender_name or ""

  @sender_name.setter
  def sender_name(self, sender_name: Optional[str]):
    if sender_name is None:
      del self.sender_name
      return
    if not isinstance(sender_name, str):
      raise TypeError('sender_name must be of type str')
    self._sender_name = sender_name


class Conversation(KaggleObject):
  r"""
  We've moved from 'Chat' to 'Conversation' to align with Open Telemetry specs:
  https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-spans.md

  Attributes:
    id (str)
      Conversation ID generated in Python
    requests (ModelRequest)
      All requests made in this conversation
    metrics (ModelUsageMetrics)
      For convenience, this is the aggregate of all the
      requests.*.metrics for the Conversation
    model_version_slug (str)
      This could also be some other message to group other information about
      the LLM, but at a minimum demonstrates that the model information remains
      fixed apart from the requests/Contents (which do have stated Roles, but
      still happen in the context of a Conversation with a specific LLM)
  """

  def __init__(self):
    self._id = ""
    self._requests = []
    self._metrics = None
    self._model_version_slug = ""
    self._freeze()

  @property
  def id(self) -> str:
    """Conversation ID generated in Python"""
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id

  @property
  def requests(self) -> Optional[List[Optional['ModelRequest']]]:
    """All requests made in this conversation"""
    return self._requests

  @requests.setter
  def requests(self, requests: Optional[List[Optional['ModelRequest']]]):
    if requests is None:
      del self.requests
      return
    if not isinstance(requests, list):
      raise TypeError('requests must be of type list')
    if not all([isinstance(t, ModelRequest) for t in requests]):
      raise TypeError('requests must contain only items of type ModelRequest')
    self._requests = requests

  @property
  def metrics(self) -> Optional['ModelUsageMetrics']:
    r"""
    For convenience, this is the aggregate of all the
    requests.*.metrics for the Conversation
    """
    return self._metrics

  @metrics.setter
  def metrics(self, metrics: Optional['ModelUsageMetrics']):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, ModelUsageMetrics):
      raise TypeError('metrics must be of type ModelUsageMetrics')
    self._metrics = metrics

  @property
  def model_version_slug(self) -> str:
    r"""
    This could also be some other message to group other information about
    the LLM, but at a minimum demonstrates that the model information remains
    fixed apart from the requests/Contents (which do have stated Roles, but
    still happen in the context of a Conversation with a specific LLM)
    """
    return self._model_version_slug

  @model_version_slug.setter
  def model_version_slug(self, model_version_slug: str):
    if model_version_slug is None:
      del self.model_version_slug
      return
    if not isinstance(model_version_slug, str):
      raise TypeError('model_version_slug must be of type str')
    self._model_version_slug = model_version_slug


class ConversationRequestIdentifier(KaggleObject):
  r"""
  Attributes:
    conversation_id (str)
    request_id (str)
  """

  def __init__(self):
    self._conversation_id = ""
    self._request_id = ""
    self._freeze()

  @property
  def conversation_id(self) -> str:
    return self._conversation_id

  @conversation_id.setter
  def conversation_id(self, conversation_id: str):
    if conversation_id is None:
      del self.conversation_id
      return
    if not isinstance(conversation_id, str):
      raise TypeError('conversation_id must be of type str')
    self._conversation_id = conversation_id

  @property
  def request_id(self) -> str:
    return self._request_id

  @request_id.setter
  def request_id(self, request_id: str):
    if request_id is None:
      del self.request_id
      return
    if not isinstance(request_id, str):
      raise TypeError('request_id must be of type str')
    self._request_id = request_id


class CustomResult(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (str)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class DraftSelector(KaggleObject):
  r"""
  Select by the parent benchmark's single draft version (always exists).

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class FileData(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      Display name of the file data. Used to provide a label or filename to
      distinguish file datas. This field is not currently used in the Gemini
      GenerateContent calls.
    file_uri (str)
      The URI of the file. This can be a general http/https URI or a GCS path.
    mime_type (str)
      The IANA standard MIME type of the source data.
  """

  def __init__(self):
    self._display_name = None
    self._file_uri = None
    self._mime_type = None
    self._freeze()

  @property
  def display_name(self) -> str:
    r"""
    Display name of the file data. Used to provide a label or filename to
    distinguish file datas. This field is not currently used in the Gemini
    GenerateContent calls.
    """
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def file_uri(self) -> str:
    """The URI of the file. This can be a general http/https URI or a GCS path."""
    return self._file_uri or ""

  @file_uri.setter
  def file_uri(self, file_uri: Optional[str]):
    if file_uri is None:
      del self.file_uri
      return
    if not isinstance(file_uri, str):
      raise TypeError('file_uri must be of type str')
    self._file_uri = file_uri

  @property
  def mime_type(self) -> str:
    """The IANA standard MIME type of the source data."""
    return self._mime_type or ""

  @mime_type.setter
  def mime_type(self, mime_type: Optional[str]):
    if mime_type is None:
      del self.mime_type
      return
    if not isinstance(mime_type, str):
      raise TypeError('mime_type must be of type str')
    self._mime_type = mime_type


class GameArenaStreams(KaggleObject):
  r"""
  Centralized container for all Game Arena streams, stored as a single GCS
  blob rather than spread across individual benchmark bracket blobs.

  Attributes:
    streams (BenchmarkStream)
  """

  def __init__(self):
    self._streams = []
    self._freeze()

  @property
  def streams(self) -> Optional[List[Optional['BenchmarkStream']]]:
    return self._streams

  @streams.setter
  def streams(self, streams: Optional[List[Optional['BenchmarkStream']]]):
    if streams is None:
      del self.streams
      return
    if not isinstance(streams, list):
      raise TypeError('streams must be of type list')
    if not all([isinstance(t, BenchmarkStream) for t in streams]):
      raise TypeError('streams must contain only items of type BenchmarkStream')
    self._streams = streams


class LatestSelector(KaggleObject):
  r"""
  Select by the parent benchmark's latest version, defaults to NULL.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class LatestVisibleSelector(KaggleObject):
  r"""
  Select by the parent benchmark's latest version visible to the user.
  If the user can read drafts (via IsBenchmarkDraftReadableBy), returns the
  latest version. Otherwise, returns the latest published version.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class ListBenchmarksFilter(KaggleObject):
  r"""
  Attributes:
    benchmark_types (BenchmarkType)
    search_query (str)
    is_currently_featured (bool)
      support featured benchmark shelf
    organization_id (int)
    tag_ids (int)
    include_top_ranking_results (bool)
    benchmark_version_ids (int)
      List parent models of these specific versions. Model results will have the
      version populated. If specified, overrides other filters.
    owner_user_id (int)
    ids (int)
  """

  def __init__(self):
    self._benchmark_types = []
    self._search_query = None
    self._is_currently_featured = None
    self._organization_id = None
    self._tag_ids = []
    self._include_top_ranking_results = None
    self._benchmark_version_ids = []
    self._owner_user_id = None
    self._ids = []
    self._freeze()

  @property
  def benchmark_types(self) -> Optional[List['BenchmarkType']]:
    return self._benchmark_types

  @benchmark_types.setter
  def benchmark_types(self, benchmark_types: Optional[List['BenchmarkType']]):
    if benchmark_types is None:
      del self.benchmark_types
      return
    if not isinstance(benchmark_types, list):
      raise TypeError('benchmark_types must be of type list')
    if not all([isinstance(t, BenchmarkType) for t in benchmark_types]):
      raise TypeError('benchmark_types must contain only items of type BenchmarkType')
    self._benchmark_types = benchmark_types

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def is_currently_featured(self) -> bool:
    """support featured benchmark shelf"""
    return self._is_currently_featured or False

  @is_currently_featured.setter
  def is_currently_featured(self, is_currently_featured: Optional[bool]):
    if is_currently_featured is None:
      del self.is_currently_featured
      return
    if not isinstance(is_currently_featured, bool):
      raise TypeError('is_currently_featured must be of type bool')
    self._is_currently_featured = is_currently_featured

  @property
  def organization_id(self) -> int:
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
  def owner_user_id(self) -> int:
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def tag_ids(self) -> Optional[List[int]]:
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
  def include_top_ranking_results(self) -> bool:
    return self._include_top_ranking_results or False

  @include_top_ranking_results.setter
  def include_top_ranking_results(self, include_top_ranking_results: Optional[bool]):
    if include_top_ranking_results is None:
      del self.include_top_ranking_results
      return
    if not isinstance(include_top_ranking_results, bool):
      raise TypeError('include_top_ranking_results must be of type bool')
    self._include_top_ranking_results = include_top_ranking_results

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids

  @property
  def benchmark_version_ids(self) -> Optional[List[int]]:
    r"""
    List parent models of these specific versions. Model results will have the
    version populated. If specified, overrides other filters.
    """
    return self._benchmark_version_ids

  @benchmark_version_ids.setter
  def benchmark_version_ids(self, benchmark_version_ids: Optional[List[int]]):
    if benchmark_version_ids is None:
      del self.benchmark_version_ids
      return
    if not isinstance(benchmark_version_ids, list):
      raise TypeError('benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_version_ids]):
      raise TypeError('benchmark_version_ids must contain only items of type int')
    self._benchmark_version_ids = benchmark_version_ids


class ListBenchmarkTasksFilter(KaggleObject):
  r"""
  Attributes:
    task_types (BenchmarkTaskType)
    ids (int)
  """

  def __init__(self):
    self._task_types = []
    self._ids = []
    self._freeze()

  @property
  def task_types(self) -> Optional[List['BenchmarkTaskType']]:
    return self._task_types

  @task_types.setter
  def task_types(self, task_types: Optional[List['BenchmarkTaskType']]):
    if task_types is None:
      del self.task_types
      return
    if not isinstance(task_types, list):
      raise TypeError('task_types must be of type list')
    if not all([isinstance(t, BenchmarkTaskType) for t in task_types]):
      raise TypeError('task_types must contain only items of type BenchmarkTaskType')
    self._task_types = task_types

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids


class ModelRequest(KaggleObject):
  r"""
  Request made to a model as part of a Conversation

  Attributes:
    contents (Content)
      Input/output from the request
    metrics (ModelUsageMetrics)
    id (str)
      Model request ID generated in Python
  """

  def __init__(self):
    self._contents = []
    self._metrics = None
    self._id = ""
    self._freeze()

  @property
  def contents(self) -> Optional[List[Optional['Content']]]:
    """Input/output from the request"""
    return self._contents

  @contents.setter
  def contents(self, contents: Optional[List[Optional['Content']]]):
    if contents is None:
      del self.contents
      return
    if not isinstance(contents, list):
      raise TypeError('contents must be of type list')
    if not all([isinstance(t, Content) for t in contents]):
      raise TypeError('contents must contain only items of type Content')
    self._contents = contents

  @property
  def metrics(self) -> Optional['ModelUsageMetrics']:
    return self._metrics

  @metrics.setter
  def metrics(self, metrics: Optional['ModelUsageMetrics']):
    if metrics is None:
      del self.metrics
      return
    if not isinstance(metrics, ModelUsageMetrics):
      raise TypeError('metrics must be of type ModelUsageMetrics')
    self._metrics = metrics

  @property
  def id(self) -> str:
    """Model request ID generated in Python"""
    return self._id

  @id.setter
  def id(self, id: str):
    if id is None:
      del self.id
      return
    if not isinstance(id, str):
      raise TypeError('id must be of type str')
    self._id = id


class ModelUsageMetrics(KaggleObject):
  r"""
  We should aim to keep this aligned with Open Telemetry specs:
  https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-spans.md

  Attributes:
    input_tokens (int)
    output_tokens (int)
    thinking_tokens (int)
    duration_ms (int)
    input_tokens_cost_nanodollars (int)
    output_tokens_cost_nanodollars (int)
    total_backend_latency_ms (int)
  """

  def __init__(self):
    self._input_tokens = 0
    self._output_tokens = 0
    self._thinking_tokens = None
    self._duration_ms = 0
    self._input_tokens_cost_nanodollars = None
    self._output_tokens_cost_nanodollars = None
    self._total_backend_latency_ms = None
    self._freeze()

  @property
  def input_tokens(self) -> int:
    return self._input_tokens

  @input_tokens.setter
  def input_tokens(self, input_tokens: int):
    if input_tokens is None:
      del self.input_tokens
      return
    if not isinstance(input_tokens, int):
      raise TypeError('input_tokens must be of type int')
    self._input_tokens = input_tokens

  @property
  def output_tokens(self) -> int:
    return self._output_tokens

  @output_tokens.setter
  def output_tokens(self, output_tokens: int):
    if output_tokens is None:
      del self.output_tokens
      return
    if not isinstance(output_tokens, int):
      raise TypeError('output_tokens must be of type int')
    self._output_tokens = output_tokens

  @property
  def thinking_tokens(self) -> int:
    return self._thinking_tokens or 0

  @thinking_tokens.setter
  def thinking_tokens(self, thinking_tokens: Optional[int]):
    if thinking_tokens is None:
      del self.thinking_tokens
      return
    if not isinstance(thinking_tokens, int):
      raise TypeError('thinking_tokens must be of type int')
    self._thinking_tokens = thinking_tokens

  @property
  def duration_ms(self) -> int:
    return self._duration_ms

  @duration_ms.setter
  def duration_ms(self, duration_ms: int):
    if duration_ms is None:
      del self.duration_ms
      return
    if not isinstance(duration_ms, int):
      raise TypeError('duration_ms must be of type int')
    self._duration_ms = duration_ms

  @property
  def input_tokens_cost_nanodollars(self) -> int:
    return self._input_tokens_cost_nanodollars or 0

  @input_tokens_cost_nanodollars.setter
  def input_tokens_cost_nanodollars(self, input_tokens_cost_nanodollars: Optional[int]):
    if input_tokens_cost_nanodollars is None:
      del self.input_tokens_cost_nanodollars
      return
    if not isinstance(input_tokens_cost_nanodollars, int):
      raise TypeError('input_tokens_cost_nanodollars must be of type int')
    self._input_tokens_cost_nanodollars = input_tokens_cost_nanodollars

  @property
  def output_tokens_cost_nanodollars(self) -> int:
    return self._output_tokens_cost_nanodollars or 0

  @output_tokens_cost_nanodollars.setter
  def output_tokens_cost_nanodollars(self, output_tokens_cost_nanodollars: Optional[int]):
    if output_tokens_cost_nanodollars is None:
      del self.output_tokens_cost_nanodollars
      return
    if not isinstance(output_tokens_cost_nanodollars, int):
      raise TypeError('output_tokens_cost_nanodollars must be of type int')
    self._output_tokens_cost_nanodollars = output_tokens_cost_nanodollars

  @property
  def total_backend_latency_ms(self) -> int:
    return self._total_backend_latency_ms or 0

  @total_backend_latency_ms.setter
  def total_backend_latency_ms(self, total_backend_latency_ms: Optional[int]):
    if total_backend_latency_ms is None:
      del self.total_backend_latency_ms
      return
    if not isinstance(total_backend_latency_ms, int):
      raise TypeError('total_backend_latency_ms must be of type int')
    self._total_backend_latency_ms = total_backend_latency_ms


class NumericResult(KaggleObject):
  r"""
  Attributes:
    value (float)
    confidence_interval (float)
      Note, while we call this the 'confidence interval' - the value we store
      here is actually the 'confidence radius', it should always be displayed
      as a +- value.
    uneven_confidence_interval (UnevenConfidenceInterval)
      For asymmetric confidence intervals in which the +/- values differ
      If set, prioritized over confidence_interval (if both are set)
  """

  def __init__(self):
    self._value = 0.0
    self._confidence_interval = None
    self._uneven_confidence_interval = None
    self._freeze()

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, value: float):
    if value is None:
      del self.value
      return
    if not isinstance(value, float):
      raise TypeError('value must be of type float')
    self._value = value

  @property
  def confidence_interval(self) -> float:
    r"""
    Note, while we call this the 'confidence interval' - the value we store
    here is actually the 'confidence radius', it should always be displayed
    as a +- value.
    """
    return self._confidence_interval or 0.0

  @confidence_interval.setter
  def confidence_interval(self, confidence_interval: Optional[float]):
    if confidence_interval is None:
      del self.confidence_interval
      return
    if not isinstance(confidence_interval, float):
      raise TypeError('confidence_interval must be of type float')
    self._confidence_interval = confidence_interval

  @property
  def uneven_confidence_interval(self) -> Optional['UnevenConfidenceInterval']:
    r"""
    For asymmetric confidence intervals in which the +/- values differ
    If set, prioritized over confidence_interval (if both are set)
    """
    return self._uneven_confidence_interval or None

  @uneven_confidence_interval.setter
  def uneven_confidence_interval(self, uneven_confidence_interval: Optional[Optional['UnevenConfidenceInterval']]):
    if uneven_confidence_interval is None:
      del self.uneven_confidence_interval
      return
    if not isinstance(uneven_confidence_interval, UnevenConfidenceInterval):
      raise TypeError('uneven_confidence_interval must be of type UnevenConfidenceInterval')
    self._uneven_confidence_interval = uneven_confidence_interval


class Part(KaggleObject):
  r"""
  Ref: https://ai.google.dev/api/caching#Part

  Attributes:
    text (str)
      Text
    inline_data (Blob)
      Inline bytes data
    file_data (FileData)
      URI based data
  """

  def __init__(self):
    self._text = None
    self._inline_data = None
    self._file_data = None
    self._freeze()

  @property
  def text(self) -> str:
    """Text"""
    return self._text or ""

  @text.setter
  def text(self, text: str):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    del self.inline_data
    del self.file_data
    self._text = text

  @property
  def inline_data(self) -> Optional['Blob']:
    """Inline bytes data"""
    return self._inline_data or None

  @inline_data.setter
  def inline_data(self, inline_data: Optional['Blob']):
    if inline_data is None:
      del self.inline_data
      return
    if not isinstance(inline_data, Blob):
      raise TypeError('inline_data must be of type Blob')
    del self.text
    del self.file_data
    self._inline_data = inline_data

  @property
  def file_data(self) -> Optional['FileData']:
    """URI based data"""
    return self._file_data or None

  @file_data.setter
  def file_data(self, file_data: Optional['FileData']):
    if file_data is None:
      del self.file_data
      return
    if not isinstance(file_data, FileData):
      raise TypeError('file_data must be of type FileData')
    del self.text
    del self.inline_data
    self._file_data = file_data


class Permissions(KaggleObject):
  r"""
  Shared permissions sub-message.

  Attributes:
    can_read (bool)
    can_update (bool)
    can_administer (bool)
    is_owner (bool)
    can_execute (bool)
      Whether the caller has execute permissions on the task.
  """

  def __init__(self):
    self._can_read = False
    self._can_update = False
    self._can_administer = False
    self._is_owner = False
    self._can_execute = False
    self._freeze()

  @property
  def can_read(self) -> bool:
    return self._can_read

  @can_read.setter
  def can_read(self, can_read: bool):
    if can_read is None:
      del self.can_read
      return
    if not isinstance(can_read, bool):
      raise TypeError('can_read must be of type bool')
    self._can_read = can_read

  @property
  def can_update(self) -> bool:
    return self._can_update

  @can_update.setter
  def can_update(self, can_update: bool):
    if can_update is None:
      del self.can_update
      return
    if not isinstance(can_update, bool):
      raise TypeError('can_update must be of type bool')
    self._can_update = can_update

  @property
  def can_administer(self) -> bool:
    return self._can_administer

  @can_administer.setter
  def can_administer(self, can_administer: bool):
    if can_administer is None:
      del self.can_administer
      return
    if not isinstance(can_administer, bool):
      raise TypeError('can_administer must be of type bool')
    self._can_administer = can_administer

  @property
  def is_owner(self) -> bool:
    return self._is_owner

  @is_owner.setter
  def is_owner(self, is_owner: bool):
    if is_owner is None:
      del self.is_owner
      return
    if not isinstance(is_owner, bool):
      raise TypeError('is_owner must be of type bool')
    self._is_owner = is_owner

  @property
  def can_execute(self) -> bool:
    """Whether the caller has execute permissions on the task."""
    return self._can_execute

  @can_execute.setter
  def can_execute(self, can_execute: bool):
    if can_execute is None:
      del self.can_execute
      return
    if not isinstance(can_execute, bool):
      raise TypeError('can_execute must be of type bool')
    self._can_execute = can_execute


class PublishedLatestSelector(KaggleObject):
  r"""
  Select by the parent benchmark's latest published version, defaults to NULL.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier


class SampleTask(KaggleObject):
  r"""
  Attributes:
    tag (Tag)
  """

  def __init__(self):
    self._tag = None
    self._freeze()

  @property
  def tag(self) -> Optional['Tag']:
    return self._tag

  @tag.setter
  def tag(self, tag: Optional['Tag']):
    if tag is None:
      del self.tag
      return
    if not isinstance(tag, Tag):
      raise TypeError('tag must be of type Tag')
    self._tag = tag


class SlugIdentifier(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    benchmark_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._benchmark_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    return self._benchmark_slug

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: str):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug


class SlugSelector(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Both of these slugs are required to locate a task
    task_slug (str)
    version_number (int)
      version_number is optional to target an older version of the task. It can
      be ignored if the latest version is sufficient/desired.
  """

  def __init__(self):
    self._owner_slug = ""
    self._task_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """Both of these slugs are required to locate a task"""
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def task_slug(self) -> str:
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: str):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, str):
      raise TypeError('task_slug must be of type str')
    self._task_slug = task_slug

  @property
  def version_number(self) -> int:
    r"""
    version_number is optional to target an older version of the task. It can
    be ignored if the latest version is sufficient/desired.
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class TaskIdentifier(KaggleObject):
  r"""
  Identifier for selecting a specific benchmark task.

  Attributes:
    id (int)
      When targeting the ID of the Task, the latest version will be returned.
    slug_selector (SlugSelector)
      When targeting by slugs, an optional version_number may be provided to
      target a specific version. If excluded, the latest version will be
      returned.
    version_id (int)
      Target a specific version of the Task via the SQL ID of the TaskVersion
    source_kernel_id (int)
      Get the latest version of a task based on the associated Source Kernel Id
  """

  def __init__(self):
    self._id = None
    self._slug_selector = None
    self._version_id = None
    self._source_kernel_id = None
    self._freeze()

  @property
  def id(self) -> int:
    """When targeting the ID of the Task, the latest version will be returned."""
    return self._id or 0

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    del self.slug_selector
    del self.version_id
    del self.source_kernel_id
    self._id = id

  @property
  def slug_selector(self) -> Optional['SlugSelector']:
    r"""
    When targeting by slugs, an optional version_number may be provided to
    target a specific version. If excluded, the latest version will be
    returned.
    """
    return self._slug_selector or None

  @slug_selector.setter
  def slug_selector(self, slug_selector: Optional['SlugSelector']):
    if slug_selector is None:
      del self.slug_selector
      return
    if not isinstance(slug_selector, SlugSelector):
      raise TypeError('slug_selector must be of type SlugSelector')
    del self.id
    del self.version_id
    del self.source_kernel_id
    self._slug_selector = slug_selector

  @property
  def version_id(self) -> int:
    """Target a specific version of the Task via the SQL ID of the TaskVersion"""
    return self._version_id or 0

  @version_id.setter
  def version_id(self, version_id: int):
    if version_id is None:
      del self.version_id
      return
    if not isinstance(version_id, int):
      raise TypeError('version_id must be of type int')
    del self.id
    del self.slug_selector
    del self.source_kernel_id
    self._version_id = version_id

  @property
  def source_kernel_id(self) -> int:
    """Get the latest version of a task based on the associated Source Kernel Id"""
    return self._source_kernel_id or 0

  @source_kernel_id.setter
  def source_kernel_id(self, source_kernel_id: int):
    if source_kernel_id is None:
      del self.source_kernel_id
      return
    if not isinstance(source_kernel_id, int):
      raise TypeError('source_kernel_id must be of type int')
    del self.id
    del self.slug_selector
    del self.version_id
    self._source_kernel_id = source_kernel_id


class UnevenConfidenceInterval(KaggleObject):
  r"""
  Attributes:
    plus (float)
    minus (float)
  """

  def __init__(self):
    self._plus = 0.0
    self._minus = 0.0
    self._freeze()

  @property
  def plus(self) -> float:
    return self._plus

  @plus.setter
  def plus(self, plus: float):
    if plus is None:
      del self.plus
      return
    if not isinstance(plus, float):
      raise TypeError('plus must be of type float')
    self._plus = plus

  @property
  def minus(self) -> float:
    return self._minus

  @minus.setter
  def minus(self, minus: float):
    if minus is None:
      del self.minus
      return
    if not isinstance(minus, float):
      raise TypeError('minus must be of type float')
    self._minus = minus


class UnifiedBenchmarkLeaderboard(KaggleObject):
  r"""
  Attributes:
    task_version_headers (BenchmarkLeaderboardTaskVersionHeader)
      Headers for the TaskVersions (or BenchmarkVersions) in the leaderboard.
    model_version_headers (BenchmarkLeaderboardModelVersionHeader)
      Headers for the ModelVersions in the leaderboard.
    entries (BenchmarkLeaderboardEntry)
      Entries for the leaderboard - represents the data in each 'cell' of the
      leaderboard. Each entry maps to a (TaskVersion, ModelVersion) pair.
  """

  def __init__(self):
    self._task_version_headers = []
    self._model_version_headers = []
    self._entries = []
    self._freeze()

  @property
  def task_version_headers(self) -> Optional[List[Optional['BenchmarkLeaderboardTaskVersionHeader']]]:
    """Headers for the TaskVersions (or BenchmarkVersions) in the leaderboard."""
    return self._task_version_headers

  @task_version_headers.setter
  def task_version_headers(self, task_version_headers: Optional[List[Optional['BenchmarkLeaderboardTaskVersionHeader']]]):
    if task_version_headers is None:
      del self.task_version_headers
      return
    if not isinstance(task_version_headers, list):
      raise TypeError('task_version_headers must be of type list')
    if not all([isinstance(t, BenchmarkLeaderboardTaskVersionHeader) for t in task_version_headers]):
      raise TypeError('task_version_headers must contain only items of type BenchmarkLeaderboardTaskVersionHeader')
    self._task_version_headers = task_version_headers

  @property
  def model_version_headers(self) -> Optional[List[Optional['BenchmarkLeaderboardModelVersionHeader']]]:
    """Headers for the ModelVersions in the leaderboard."""
    return self._model_version_headers

  @model_version_headers.setter
  def model_version_headers(self, model_version_headers: Optional[List[Optional['BenchmarkLeaderboardModelVersionHeader']]]):
    if model_version_headers is None:
      del self.model_version_headers
      return
    if not isinstance(model_version_headers, list):
      raise TypeError('model_version_headers must be of type list')
    if not all([isinstance(t, BenchmarkLeaderboardModelVersionHeader) for t in model_version_headers]):
      raise TypeError('model_version_headers must contain only items of type BenchmarkLeaderboardModelVersionHeader')
    self._model_version_headers = model_version_headers

  @property
  def entries(self) -> Optional[List[Optional['BenchmarkLeaderboardEntry']]]:
    r"""
    Entries for the leaderboard - represents the data in each 'cell' of the
    leaderboard. Each entry maps to a (TaskVersion, ModelVersion) pair.
    """
    return self._entries

  @entries.setter
  def entries(self, entries: Optional[List[Optional['BenchmarkLeaderboardEntry']]]):
    if entries is None:
      del self.entries
      return
    if not isinstance(entries, list):
      raise TypeError('entries must be of type list')
    if not all([isinstance(t, BenchmarkLeaderboardEntry) for t in entries]):
      raise TypeError('entries must contain only items of type BenchmarkLeaderboardEntry')
    self._entries = entries


class VersionIdSelector(KaggleObject):
  r"""
  Select by the benchmark version id. Optional parent benchmark id.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
    id (int)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._id = 0
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier or None

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional[Optional['BenchmarkIdentifier']]):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier

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


class VersionNumberSelector(KaggleObject):
  r"""
  Select by the parent benchmark's version at a particular version number.
  Defaults to NULL.

  Attributes:
    parent_benchmark_identifier (BenchmarkIdentifier)
    version_number (int)
  """

  def __init__(self):
    self._parent_benchmark_identifier = None
    self._version_number = 0
    self._freeze()

  @property
  def parent_benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    return self._parent_benchmark_identifier

  @parent_benchmark_identifier.setter
  def parent_benchmark_identifier(self, parent_benchmark_identifier: Optional['BenchmarkIdentifier']):
    if parent_benchmark_identifier is None:
      del self.parent_benchmark_identifier
      return
    if not isinstance(parent_benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('parent_benchmark_identifier must be of type BenchmarkIdentifier')
    self._parent_benchmark_identifier = parent_benchmark_identifier

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


Benchmark._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkType, BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("media", "media", "_media", BenchmarkMedia, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("task", "task", "_task", BenchmarkTask, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("version", "version", "_version", BenchmarkVersion, None, KaggleObjectSerializer()),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("topicCount", "topic_count", "_topic_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("categories", "categories", "_categories", TagList, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasUpVoted", "has_up_voted", "_has_up_voted", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("permissions", "permissions", "_permissions", Permissions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishedVersionsCount", "published_versions_count", "_published_versions_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("draftVersionsCount", "draft_versions_count", "_draft_versions_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("viewCount", "view_count", "_view_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("downloadCount", "download_count", "_download_count", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkAuthor._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bio", "bio", "_bio", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("websiteUrl", "website_url", "_website_url", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkBibtexCitation._fields = [
  FieldMetadata("authors", "authors", "_authors", str, "", PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("year", "year", "_year", str, "", PredefinedSerializer()),
  FieldMetadata("organizations", "organizations", "_organizations", str, "", PredefinedSerializer()),
]

BenchmarkBracket._fields = [
  FieldMetadata("rounds", "rounds", "_rounds", BenchmarkBracketRound, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer()),
]

BenchmarkBracketRound._fields = [
  FieldMetadata("seeds", "seeds", "_seeds", BenchmarkBracketSeed, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkBracketSeed._fields = [
  FieldMetadata("teams", "teams", "_teams", BenchmarkBracketTeam, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("episodeIds", "episode_ids", "_episode_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("live", "live", "_live", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("replayUrl", "replay_url", "_replay_url", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkBracketTeam._fields = [
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkModel", "benchmark_model", "_benchmark_model", BenchmarkModel, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numWins", "num_wins", "_num_wins", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("winner", "winner", "_winner", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("staticLogoPath", "static_logo_path", "_static_logo_path", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkIdentifier._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slugIdentifier", "slug_identifier", "_slug_identifier", SlugIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkLeaderboard._fields = [
  FieldMetadata("headers", "headers", "_headers", BenchmarkLeaderboardHeader, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("rows", "rows", "_rows", BenchmarkLeaderboardRow, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkLeaderboardEntry._fields = [
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("runs", "runs", "_runs", BenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkLeaderboardHeader._fields = [
  FieldMetadata("benchmarkVersion", "benchmark_version", "_benchmark_version", BenchmarkVersion, None, KaggleObjectSerializer()),
  FieldMetadata("benchmarkVersionMapping", "benchmark_version_mapping", "_benchmark_version_mapping", BenchmarkVersionMapping, None, KaggleObjectSerializer()),
  FieldMetadata("taskVersion", "task_version", "_task_version", BenchmarkTaskVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("taskVersionMapping", "task_version_mapping", "_task_version_mapping", BenchmarkTaskVersionMapping, None, KaggleObjectSerializer(), optional=True),
]

BenchmarkLeaderboardModelVersionHeader._fields = [
  FieldMetadata("modelVersion", "model_version", "_model_version", BenchmarkModelVersion, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionMapping", "model_version_mapping", "_model_version_mapping", BenchmarkVersionModelMapping, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", Medal, None, EnumSerializer(), optional=True),
  FieldMetadata("rank", "rank", "_rank", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkLeaderboardRow._fields = [
  FieldMetadata("modelVersion", "model_version", "_model_version", BenchmarkModelVersion, None, KaggleObjectSerializer()),
  FieldMetadata("publisherOrganization", "publisher_organization", "_publisher_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publisherUserId", "publisher_user_id", "_publisher_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelLicense", "model_license", "_model_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("aggregateScore", "aggregate_score", "_aggregate_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("results", "results", "_results", BenchmarkResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelVersionMapping", "model_version_mapping", "_model_version_mapping", BenchmarkVersionModelMapping, None, KaggleObjectSerializer()),
]

BenchmarkLeaderboardTaskVersionHeader._fields = [
  FieldMetadata("taskVersion", "task_version", "_task_version", BenchmarkTaskVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkVersion", "benchmark_version", "_benchmark_version", BenchmarkVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("taskVersionMapping", "task_version_mapping", "_task_version_mapping", BenchmarkTaskVersionMapping, None, KaggleObjectSerializer(), optional=True),
]

BenchmarkMedia._fields = [
  FieldMetadata("type", "type", "_type", BenchmarkMediaType, BenchmarkMediaType.BENCHMARK_MEDIA_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkModel._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("defaultVersionId", "default_version_id", "_default_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("version", "version", "_version", BenchmarkModelVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
]

BenchmarkModelVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelId", "benchmark_model_id", "_benchmark_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("knowledgeCutoff", "knowledge_cutoff", "_knowledge_cutoff", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("isDefault", "is_default", "_is_default", bool, False, PredefinedSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
  FieldMetadata("allowModelProxy", "allow_model_proxy", "_allow_model_proxy", bool, False, PredefinedSerializer()),
  FieldMetadata("modelProxySlug", "model_proxy_slug", "_model_proxy_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("importanceLevel", "importance_level", "_importance_level", BenchmarkModelImportanceLevel, None, EnumSerializer(), optional=True),
]

BenchmarkResult._fields = [
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("customAdditionalResults", "custom_additional_results", "_custom_additional_results", CustomResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numericResultPrivate", "numeric_result_private", "_numeric_result_private", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericResultPublic", "numeric_result_public", "_numeric_result_public", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("evaluationDate", "evaluation_date", "_evaluation_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkSlugSelector._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkStream._fields = [
  FieldMetadata("youtubeId", "youtube_id", "_youtube_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kickChannel", "kick_channel", "_kick_channel", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("linkUrl", "link_url", "_link_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("live", "live", "_live", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("featured", "featured", "_featured", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scheduleDate", "schedule_date", "_schedule_date", datetime, None, DateTimeSerializer(), optional=True),
]

BenchmarkTask._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkTaskType, BenchmarkTaskType.BENCHMARK_TASK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("version", "version", "_version", BenchmarkTaskVersion, None, KaggleObjectSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("definitionType", "definition_type", "_definition_type", BenchmarkTaskDefinitionType, None, EnumSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("sourceKernelId", "source_kernel_id", "_source_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasUpVoted", "has_up_voted", "_has_up_voted", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumId", "forum_id", "_forum_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("canAdminister", "can_administer", "_can_administer", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("permissions", "permissions", "_permissions", Permissions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("categories", "categories", "_categories", TagList, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("latestVersionNumber", "latest_version_number", "_latest_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelPermissions", "kernel_permissions", "_kernel_permissions", Permissions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("viewCount", "view_count", "_view_count", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskCitation._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskRun._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("manualUserId", "manual_user_id", "_manual_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("taskVersion", "task_version", "_task_version", BenchmarkTaskVersion, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersion", "model_version", "_model_version", BenchmarkModelVersion, None, KaggleObjectSerializer()),
  FieldMetadata("result", "result", "_result", BenchmarkResult, None, KaggleObjectSerializer()),
  FieldMetadata("state", "state", "_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("conversations", "conversations", "_conversations", Conversation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("results", "results", "_results", BenchmarkTaskRunResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("assertions", "assertions", "_assertions", BenchmarkTaskRunAssertion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("subruns", "subruns", "_subruns", BenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("pyRunId", "py_run_id", "_py_run_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputKernelSessionId", "output_kernel_session_id", "_output_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkTaskRunAssertion._fields = [
  FieldMetadata("expectation", "expectation", "_expectation", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", BenchmarkTaskRunAssertionStatus, BenchmarkTaskRunAssertionStatus.BENCHMARK_TASK_RUN_ASSERTION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lineNumber", "line_number", "_line_number", int, 0, PredefinedSerializer()),
  FieldMetadata("definition", "definition", "_definition", str, "", PredefinedSerializer()),
  FieldMetadata("conversationRequestIds", "conversation_request_ids", "_conversation_request_ids", ConversationRequestIdentifier, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkTaskRunResult._fields = [
  FieldMetadata("type", "type", "_type", BenchmarkTaskRunResultType, BenchmarkTaskRunResultType.BENCHMARK_TASK_RUN_RESULT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalMetrics", "total_metrics", "_total_metrics", ModelUsageMetrics, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("candidateMetrics", "candidate_metrics", "_candidate_metrics", ModelUsageMetrics, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("assertionStatuses", "assertion_statuses", "_assertion_statuses", BenchmarkTaskRunAssertionStatus, [], ListSerializer(EnumSerializer())),
]

BenchmarkTaskVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("taskId", "task_id", "_task_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("definition", "definition", "_definition", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceKernelSessionId", "source_kernel_session_id", "_source_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("aggregationType", "aggregation_type", "_aggregation_type", BenchmarkTaskVersionAggregationType, None, EnumSerializer(), optional=True),
  FieldMetadata("childTaskVersions", "child_task_versions", "_child_task_versions", BenchmarkTaskVersion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", BenchmarkTaskType, BenchmarkTaskType.BENCHMARK_TASK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("parentTaskVersionIds", "parent_task_version_ids", "_parent_task_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("displayType", "display_type", "_display_type", BenchmarkLeaderboardDisplayType, BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sourceKernelId", "source_kernel_id", "_source_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("permissions", "permissions", "_permissions", Permissions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("details", "details", "_details", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("precision", "precision", "_precision", int, 0, PredefinedSerializer()),
  FieldMetadata("sortOrder", "sort_order", "_sort_order", SortOrder, SortOrder.SORT_ORDER_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", BenchmarkTaskCitation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("citation", "citation", "_citation", BenchmarkBibtexCitation, None, KaggleObjectSerializer(), optional=True),
]

BenchmarkTaskVersionMapping._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentTaskVersionId", "parent_task_version_id", "_parent_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childTaskVersionId", "child_task_version_id", "_child_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkTaskVersionMappingType, BenchmarkTaskVersionMappingType.BENCHMARK_TASK_VERSION_MAPPING_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("priority", "priority", "_priority", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secondarySortTaskVersionId", "secondary_sort_task_version_id", "_secondary_sort_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("columnName", "column_name", "_column_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayType", "display_type", "_display_type", BenchmarkLeaderboardDisplayType, BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sortingPriority", "sorting_priority", "_sorting_priority", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("weight", "weight", "_weight", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("precision", "precision", "_precision", int, 0, PredefinedSerializer()),
  FieldMetadata("sortOrder", "sort_order", "_sort_order", SortOrder, SortOrder.SORT_ORDER_UNSPECIFIED, EnumSerializer()),
]

BenchmarkTopRankingResults._fields = [
  FieldMetadata("rows", "rows", "_rows", BenchmarkTopRankingResultsRow, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("displayType", "display_type", "_display_type", BenchmarkLeaderboardDisplayType, BenchmarkLeaderboardDisplayType.BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED, EnumSerializer()),
]

BenchmarkTopRankingResultsRow._fields = [
  FieldMetadata("avatarUrl", "avatar_url", "_avatar_url", str, "", PredefinedSerializer()),
  FieldMetadata("modelName", "model_name", "_model_name", str, "", PredefinedSerializer()),
  FieldMetadata("score", "score", "_score", int, 0, PredefinedSerializer()),
]

BenchmarkVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("citation", "citation", "_citation", BenchmarkBibtexCitation, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
  FieldMetadata("media", "media", "_media", BenchmarkMedia, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("taskVersion", "task_version", "_task_version", BenchmarkTaskVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("benchmarkModelVersionMappingsCount", "benchmark_model_version_mappings_count", "_benchmark_model_version_mappings_count", int, 0, PredefinedSerializer()),
  FieldMetadata("childBenchmarkVersionMappingsCount", "child_benchmark_version_mappings_count", "_child_benchmark_version_mappings_count", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkType, BenchmarkType.BENCHMARK_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topRankingResults", "top_ranking_results", "_top_ranking_results", BenchmarkTopRankingResults, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("childTaskVersionMappingsCount", "child_task_version_mappings_count", "_child_task_version_mappings_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("permissions", "permissions", "_permissions", Permissions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUser", "owner_user", "_owner_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("maintenanceLevel", "maintenance_level", "_maintenance_level", BenchmarkMaintenanceLevel, None, EnumSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", BenchmarkTaskCitation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authors", "authors", "_authors", BenchmarkAuthor, [], ListSerializer(KaggleObjectSerializer())),
]

BenchmarkVersionIdentifier._fields = [
  FieldMetadata("versionIdSelector", "version_id_selector", "_version_id_selector", VersionIdSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("publishedLatestSelector", "published_latest_selector", "_published_latest_selector", PublishedLatestSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("versionNumberSelector", "version_number_selector", "_version_number_selector", VersionNumberSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("draftSelector", "draft_selector", "_draft_selector", DraftSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkSlugSelector", "benchmark_slug_selector", "_benchmark_slug_selector", BenchmarkSlugSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("latestSelector", "latest_selector", "_latest_selector", LatestSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("latestVisibleSelector", "latest_visible_selector", "_latest_visible_selector", LatestVisibleSelector, None, KaggleObjectSerializer(), optional=True),
]

BenchmarkVersionMapping._fields = [
  FieldMetadata("parentBenchmarkVersionId", "parent_benchmark_version_id", "_parent_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childBenchmarkVersionId", "child_benchmark_version_id", "_child_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("mappingType", "mapping_type", "_mapping_type", BenchmarkVersionMappingType, None, EnumSerializer(), optional=True),
  FieldMetadata("priority", "priority", "_priority", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("secondarySortBenchmarkVersionId", "secondary_sort_benchmark_version_id", "_secondary_sort_benchmark_version_id", int, None, PredefinedSerializer(), optional=True),
]

BenchmarkVersionModelMapping._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("parentBenchmarkVersionId", "parent_benchmark_version_id", "_parent_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("childBenchmarkModelVersionId", "child_benchmark_model_version_id", "_child_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", BenchmarkVersionModelMappingType, BenchmarkVersionModelMappingType.BENCHMARK_VERSION_MODEL_MAPPING_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
]

Blob._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("data", "data", "_data", bytes, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, None, PredefinedSerializer(), optional=True),
]

Content._fields = [
  FieldMetadata("parts", "parts", "_parts", Part, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("role", "role", "_role", ContentRole, None, EnumSerializer(), optional=True),
  FieldMetadata("senderName", "sender_name", "_sender_name", str, None, PredefinedSerializer(), optional=True),
]

Conversation._fields = [
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
  FieldMetadata("requests", "requests", "_requests", ModelRequest, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("metrics", "metrics", "_metrics", ModelUsageMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
]

ConversationRequestIdentifier._fields = [
  FieldMetadata("conversationId", "conversation_id", "_conversation_id", str, "", PredefinedSerializer()),
  FieldMetadata("requestId", "request_id", "_request_id", str, "", PredefinedSerializer()),
]

CustomResult._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

DraftSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

FileData._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileUri", "file_uri", "_file_uri", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mimeType", "mime_type", "_mime_type", str, None, PredefinedSerializer(), optional=True),
]

GameArenaStreams._fields = [
  FieldMetadata("streams", "streams", "_streams", BenchmarkStream, [], ListSerializer(KaggleObjectSerializer())),
]

LatestSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

LatestVisibleSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

ListBenchmarksFilter._fields = [
  FieldMetadata("benchmarkTypes", "benchmark_types", "_benchmark_types", BenchmarkType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isCurrentlyFeatured", "is_currently_featured", "_is_currently_featured", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("includeTopRankingResults", "include_top_ranking_results", "_include_top_ranking_results", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkVersionIds", "benchmark_version_ids", "_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListBenchmarkTasksFilter._fields = [
  FieldMetadata("taskTypes", "task_types", "_task_types", BenchmarkTaskType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ModelRequest._fields = [
  FieldMetadata("contents", "contents", "_contents", Content, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("metrics", "metrics", "_metrics", ModelUsageMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("id", "id", "_id", str, "", PredefinedSerializer()),
]

ModelUsageMetrics._fields = [
  FieldMetadata("inputTokens", "input_tokens", "_input_tokens", int, 0, PredefinedSerializer()),
  FieldMetadata("outputTokens", "output_tokens", "_output_tokens", int, 0, PredefinedSerializer()),
  FieldMetadata("thinkingTokens", "thinking_tokens", "_thinking_tokens", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("durationMs", "duration_ms", "_duration_ms", int, 0, PredefinedSerializer()),
  FieldMetadata("inputTokensCostNanodollars", "input_tokens_cost_nanodollars", "_input_tokens_cost_nanodollars", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputTokensCostNanodollars", "output_tokens_cost_nanodollars", "_output_tokens_cost_nanodollars", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBackendLatencyMs", "total_backend_latency_ms", "_total_backend_latency_ms", int, None, PredefinedSerializer(), optional=True),
]

NumericResult._fields = [
  FieldMetadata("value", "value", "_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("confidenceInterval", "confidence_interval", "_confidence_interval", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unevenConfidenceInterval", "uneven_confidence_interval", "_uneven_confidence_interval", UnevenConfidenceInterval, None, KaggleObjectSerializer(), optional=True),
]

Part._fields = [
  FieldMetadata("text", "text", "_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("inlineData", "inline_data", "_inline_data", Blob, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("fileData", "file_data", "_file_data", FileData, None, KaggleObjectSerializer(), optional=True),
]

Permissions._fields = [
  FieldMetadata("canRead", "can_read", "_can_read", bool, False, PredefinedSerializer()),
  FieldMetadata("canUpdate", "can_update", "_can_update", bool, False, PredefinedSerializer()),
  FieldMetadata("canAdminister", "can_administer", "_can_administer", bool, False, PredefinedSerializer()),
  FieldMetadata("isOwner", "is_owner", "_is_owner", bool, False, PredefinedSerializer()),
  FieldMetadata("canExecute", "can_execute", "_can_execute", bool, False, PredefinedSerializer()),
]

PublishedLatestSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
]

SampleTask._fields = [
  FieldMetadata("tag", "tag", "_tag", Tag, None, KaggleObjectSerializer()),
]

SlugIdentifier._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
]

SlugSelector._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("taskSlug", "task_slug", "_task_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

TaskIdentifier._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slugSelector", "slug_selector", "_slug_selector", SlugSelector, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("versionId", "version_id", "_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceKernelId", "source_kernel_id", "_source_kernel_id", int, None, PredefinedSerializer(), optional=True),
]

UnevenConfidenceInterval._fields = [
  FieldMetadata("plus", "plus", "_plus", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minus", "minus", "_minus", float, 0.0, PredefinedSerializer()),
]

UnifiedBenchmarkLeaderboard._fields = [
  FieldMetadata("taskVersionHeaders", "task_version_headers", "_task_version_headers", BenchmarkLeaderboardTaskVersionHeader, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelVersionHeaders", "model_version_headers", "_model_version_headers", BenchmarkLeaderboardModelVersionHeader, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("entries", "entries", "_entries", BenchmarkLeaderboardEntry, [], ListSerializer(KaggleObjectSerializer())),
]

VersionIdSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

VersionNumberSelector._fields = [
  FieldMetadata("parentBenchmarkIdentifier", "parent_benchmark_identifier", "_parent_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
]

