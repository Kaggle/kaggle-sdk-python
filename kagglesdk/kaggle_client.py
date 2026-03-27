from kagglesdk.abuse.services.abuse_service import AbuseClient
from kagglesdk.active_events.services.active_event_service import ActiveEventClient
from kagglesdk.admin.services.admin_service import AdminClient
from kagglesdk.admin.services.codelab_service import CodelabClient
from kagglesdk.admin.services.debug_service import DebugClient
from kagglesdk.admin.services.domain_ban_service import DomainBanClient
from kagglesdk.admin.services.genie_service import GenieClient
from kagglesdk.admin.services.inbox_file_service import InboxFileClient
from kagglesdk.admin.services.ip_ban_service import IpBanClient
from kagglesdk.admin.services.logging_service import LoggingClient
from kagglesdk.admin.services.organizations_service import OrganizationsClient
from kagglesdk.admin.services.rate_limit_service import RateLimitClient
from kagglesdk.agents.services.agent_exam_admin_service import AgentExamAdminClient
from kagglesdk.benchmarks.services.benchmark_admin_service import BenchmarkAdminClient
from kagglesdk.benchmarks.services.benchmark_model_service import BenchmarkModelClient
from kagglesdk.benchmarks.services.benchmark_service import BenchmarkClient
from kagglesdk.benchmarks.services.benchmark_task_run_service import BenchmarkTaskRunClient
from kagglesdk.benchmarks.services.benchmark_task_service import BenchmarkTaskClient
from kagglesdk.blobs.services.blob_service import BlobClient
from kagglesdk.cms.services.legacy_cms_service import LegacyCmsClient
from kagglesdk.common.services.caching_service import CachingClient
from kagglesdk.community.services.badges_admin_service import BadgesAdminClient
from kagglesdk.community.services.badges_service import BadgesClient
from kagglesdk.community.services.content_service import ContentClient
from kagglesdk.community.services.organizations_service import OrganizationsV2Client
from kagglesdk.community.services.votes_service import VotesClient
from kagglesdk.competitions.services.admin_service import AdminClient
from kagglesdk.competitions.services.benchmark_service import BenchmarkClient
from kagglesdk.competitions.services.competition_service import CompetitionClient
from kagglesdk.competitions.services.episode_service import EpisodeClient
from kagglesdk.competitions.services.hackathon_service import HackathonClient
from kagglesdk.competitions.services.host_service import HostClient
from kagglesdk.competitions.services.leaderboard_service import LeaderboardClient
from kagglesdk.competitions.services.metric_service import MetricClient
from kagglesdk.competitions.services.page_service import PageClient
from kagglesdk.competitions.services.rerun_service import RerunClient
from kagglesdk.competitions.services.rescore_service import RescoreClient
from kagglesdk.competitions.services.submission_service import SubmissionClient
from kagglesdk.competitions.services.team_service import TeamClient
from kagglesdk.competitions.services.user_service import UserClient
from kagglesdk.competitions.legacy.services.legacy_competition_background_service import LegacyCompetitionBackgroundClient
from kagglesdk.competitions.legacy.services.legacy_competition_host_service import LegacyCompetitionHostClient
from kagglesdk.competitions.legacy.services.legacy_competition_service import LegacyCompetitionClient
from kagglesdk.competitions.legacy.services.legacy_submission_service import LegacySubmissionClient
from kagglesdk.content_discovery.services.content_discovery_service import ContentDiscoveryClient
from kagglesdk.datasets.services.dataset_admin_service import DatasetAdminClient
from kagglesdk.datasets.services.dataset_detail_service import DatasetDetailClient
from kagglesdk.datasets.services.dataset_service import DatasetClient
from kagglesdk.datasets.databundles.services.databundle_service import DatabundleClient
from kagglesdk.diagnostics.services.metrics_service import MetricsClient
from kagglesdk.discussions.services.discussions_service import DiscussionsClient
from kagglesdk.discussions.services.writeups_service import WriteUpsClient
from kagglesdk.education.services.education_service import EducationClient
from kagglesdk.featured_resources.services.featured_resources_service import FeaturedResourcesClient
from kagglesdk.kernels.services.kernels_service import KernelsClient
from kagglesdk.kernels.services.legacy_kernels_service import LegacyKernelsClient
from kagglesdk.licenses.services.licenses_service import LicensesClient
from kagglesdk.models.services.model_admin_service import ModelAdminClient
from kagglesdk.models.services.model_proxy_internal_service import ModelProxyInternalClient
from kagglesdk.models.services.model_proxy_service import ModelProxyClient
from kagglesdk.models.services.model_service import ModelClient
from kagglesdk.newsfeed.services.newsfeed_web_service import NewsfeedWebClient
from kagglesdk.notifications.services.notifications_service import NotificationsClient
from kagglesdk.notifications.services.subscription_service import SubscriptionClient
from kagglesdk.open_graph.services.open_graph_service import OpenGraphClient
from kagglesdk.routing.services.routing_service import RoutingClient
from kagglesdk.search.services.index_service import IndexClient
from kagglesdk.search.services.search_content_service import SearchContentClient
from kagglesdk.search.services.search_service import SearchWebClient
from kagglesdk.security.services.iam_service import IamClient
from kagglesdk.security.services.oauth_service import OAuthClient
from kagglesdk.tags.services.tag_service import TagClient
from kagglesdk.testing.services.test_service import TestClient
from kagglesdk.user_secrets.services.user_secrets_service import UserSecretsClient
from kagglesdk.users.services.account_service import AccountClient
from kagglesdk.users.services.bookmark_service import BookmarkClient
from kagglesdk.users.services.captcha_service import CaptchaClient
from kagglesdk.users.services.collections_service import CollectionsClient
from kagglesdk.users.services.content_deletion_service import ContentDeletionClient
from kagglesdk.users.services.discord_service import DiscordClient
from kagglesdk.users.services.genie_service import GenieClient
from kagglesdk.users.services.group_service import GroupClient
from kagglesdk.users.services.hats_service import HatsClient
from kagglesdk.users.services.homepage_service import HomePageClient
from kagglesdk.users.services.legacy_organizations_service import LegacyOrganizationsClient
from kagglesdk.users.services.legacy_users_service import LegacyUsersClient
from kagglesdk.users.services.moderation_public_service import ModerationPublicClient
from kagglesdk.users.services.moderation_service import ModerationClient
from kagglesdk.users.services.nudge_service import NudgeClient
from kagglesdk.users.services.profile_service import ProfileClient
from kagglesdk.users.services.progression_service import ProgressionClient
from kagglesdk.users.services.ranking_service import RankingClient
from kagglesdk.users.services.recently_viewed_item_service import RecentlyViewedClient
from kagglesdk.users.services.users_service import UsersClient
from kagglesdk.users.services.verification_service import VerificationClient
from kagglesdk.kaggle_env import KaggleEnv
from kagglesdk.kaggle_http_client import KaggleHttpClient


class KaggleClient(object):
  class Abuse(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.abuse_client = AbuseClient(http_client)

  class ActiveEvents(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.active_event_client = ActiveEventClient(http_client)

  class Admin(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.admin_client = AdminClient(http_client)
      self.codelab_client = CodelabClient(http_client)
      self.debug_client = DebugClient(http_client)
      self.domain_ban_client = DomainBanClient(http_client)
      self.genie_client = GenieClient(http_client)
      self.inbox_file_client = InboxFileClient(http_client)
      self.ip_ban_client = IpBanClient(http_client)
      self.logging_client = LoggingClient(http_client)
      self.organizations_client = OrganizationsClient(http_client)
      self.rate_limit_client = RateLimitClient(http_client)

  class Agents(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.agent_exam_admin_client = AgentExamAdminClient(http_client)

  class Benchmarks(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.benchmark_admin_client = BenchmarkAdminClient(http_client)
      self.benchmark_model_client = BenchmarkModelClient(http_client)
      self.benchmark_client = BenchmarkClient(http_client)
      self.benchmark_task_run_client = BenchmarkTaskRunClient(http_client)
      self.benchmark_task_client = BenchmarkTaskClient(http_client)

  class Blobs(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.blob_client = BlobClient(http_client)

  class Cms(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.legacy_cms_client = LegacyCmsClient(http_client)

  class Common(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.caching_client = CachingClient(http_client)

  class Community(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.badges_admin_client = BadgesAdminClient(http_client)
      self.badges_client = BadgesClient(http_client)
      self.content_client = ContentClient(http_client)
      self.organizations_v2client = OrganizationsV2Client(http_client)
      self.votes_client = VotesClient(http_client)

  class Competitions(object):
    class Legacy(object):
      def __init__(self, http_client: KaggleHttpClient):
        self.legacy_competition_background_client = LegacyCompetitionBackgroundClient(http_client)
        self.legacy_competition_host_client = LegacyCompetitionHostClient(http_client)
        self.legacy_competition_client = LegacyCompetitionClient(http_client)
        self.legacy_submission_client = LegacySubmissionClient(http_client)

    def __init__(self, http_client: KaggleHttpClient):
      self.legacy = KaggleClient.Competitions.Legacy(http_client)
      self.admin_client = AdminClient(http_client)
      self.benchmark_client = BenchmarkClient(http_client)
      self.competition_client = CompetitionClient(http_client)
      self.episode_client = EpisodeClient(http_client)
      self.hackathon_client = HackathonClient(http_client)
      self.host_client = HostClient(http_client)
      self.leaderboard_client = LeaderboardClient(http_client)
      self.metric_client = MetricClient(http_client)
      self.page_client = PageClient(http_client)
      self.rerun_client = RerunClient(http_client)
      self.rescore_client = RescoreClient(http_client)
      self.submission_client = SubmissionClient(http_client)
      self.team_client = TeamClient(http_client)
      self.user_client = UserClient(http_client)

  class ContentDiscovery(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.content_discovery_client = ContentDiscoveryClient(http_client)

  class Datasets(object):
    class Databundles(object):
      def __init__(self, http_client: KaggleHttpClient):
        self.databundle_client = DatabundleClient(http_client)

    def __init__(self, http_client: KaggleHttpClient):
      self.databundles = KaggleClient.Datasets.Databundles(http_client)
      self.dataset_admin_client = DatasetAdminClient(http_client)
      self.dataset_detail_client = DatasetDetailClient(http_client)
      self.dataset_client = DatasetClient(http_client)

  class Diagnostics(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.metrics_client = MetricsClient(http_client)

  class Discussions(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.discussions_client = DiscussionsClient(http_client)
      self.write_ups_client = WriteUpsClient(http_client)

  class Education(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.education_client = EducationClient(http_client)

  class FeaturedResources(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.featured_resources_client = FeaturedResourcesClient(http_client)

  class Kernels(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.kernels_client = KernelsClient(http_client)
      self.legacy_kernels_client = LegacyKernelsClient(http_client)

  class Licenses(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.licenses_client = LicensesClient(http_client)

  class Models(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.model_admin_client = ModelAdminClient(http_client)
      self.model_proxy_internal_client = ModelProxyInternalClient(http_client)
      self.model_proxy_client = ModelProxyClient(http_client)
      self.model_client = ModelClient(http_client)

  class Newsfeed(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.newsfeed_web_client = NewsfeedWebClient(http_client)

  class Notifications(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.notifications_client = NotificationsClient(http_client)
      self.subscription_client = SubscriptionClient(http_client)

  class OpenGraph(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.open_graph_client = OpenGraphClient(http_client)

  class Routing(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.routing_client = RoutingClient(http_client)

  class Search(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.index_client = IndexClient(http_client)
      self.search_content_client = SearchContentClient(http_client)
      self.search_web_client = SearchWebClient(http_client)

  class Security(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.iam_client = IamClient(http_client)
      self.oauth_client = OAuthClient(http_client)

  class Tags(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.tag_client = TagClient(http_client)

  class Testing(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.test_client = TestClient(http_client)

  class Users(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.account_client = AccountClient(http_client)
      self.bookmark_client = BookmarkClient(http_client)
      self.captcha_client = CaptchaClient(http_client)
      self.collections_client = CollectionsClient(http_client)
      self.content_deletion_client = ContentDeletionClient(http_client)
      self.discord_client = DiscordClient(http_client)
      self.genie_client = GenieClient(http_client)
      self.group_client = GroupClient(http_client)
      self.hats_client = HatsClient(http_client)
      self.home_page_client = HomePageClient(http_client)
      self.legacy_organizations_client = LegacyOrganizationsClient(http_client)
      self.legacy_users_client = LegacyUsersClient(http_client)
      self.moderation_public_client = ModerationPublicClient(http_client)
      self.moderation_client = ModerationClient(http_client)
      self.nudge_client = NudgeClient(http_client)
      self.profile_client = ProfileClient(http_client)
      self.progression_client = ProgressionClient(http_client)
      self.ranking_client = RankingClient(http_client)
      self.recently_viewed_client = RecentlyViewedClient(http_client)
      self.users_client = UsersClient(http_client)
      self.verification_client = VerificationClient(http_client)

  class UserSecrets(object):
    def __init__(self, http_client: KaggleHttpClient):
      self.user_secrets_client = UserSecretsClient(http_client)

  def __init__(self, env: KaggleEnv = None, verbose: bool = False):
    self.abuse = KaggleClient.Abuse(http_client)
    self.active_events = KaggleClient.ActiveEvents(http_client)
    self.admin = KaggleClient.Admin(http_client)
    self.agents = KaggleClient.Agents(http_client)
    self.benchmarks = KaggleClient.Benchmarks(http_client)
    self.blobs = KaggleClient.Blobs(http_client)
    self.cms = KaggleClient.Cms(http_client)
    self.common = KaggleClient.Common(http_client)
    self.community = KaggleClient.Community(http_client)
    self.competitions = KaggleClient.Competitions(http_client)
    self.content_discovery = KaggleClient.ContentDiscovery(http_client)
    self.datasets = KaggleClient.Datasets(http_client)
    self.diagnostics = KaggleClient.Diagnostics(http_client)
    self.discussions = KaggleClient.Discussions(http_client)
    self.education = KaggleClient.Education(http_client)
    self.featured_resources = KaggleClient.FeaturedResources(http_client)
    self.kernels = KaggleClient.Kernels(http_client)
    self.licenses = KaggleClient.Licenses(http_client)
    self.models = KaggleClient.Models(http_client)
    self.newsfeed = KaggleClient.Newsfeed(http_client)
    self.notifications = KaggleClient.Notifications(http_client)
    self.open_graph = KaggleClient.OpenGraph(http_client)
    self.routing = KaggleClient.Routing(http_client)
    self.search = KaggleClient.Search(http_client)
    self.security = KaggleClient.Security(http_client)
    self.tags = KaggleClient.Tags(http_client)
    self.testing = KaggleClient.Testing(http_client)
    self.users = KaggleClient.Users(http_client)
    self.user_secrets = KaggleClient.UserSecrets(http_client)

  def _renew_iap_token(self) -> str:
    return self.admin.admin_client.renew_iap_token()

  def __enter__(self):
    self._http_client.__enter__()
    return self

  def __exit__(self, exc_type, exc_value, tb):
    self._http_client.__exit__(exc_type, exc_value, tb)
