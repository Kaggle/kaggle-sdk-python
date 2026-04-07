from kagglesdk.benchmarks.types.benchmark_service import AddBenchmarkTagRequest, AddTasksToBenchmarkRequest, BatchDeleteBenchmarkVersionsRequest, BenchmarkActivityResponse, BulkAddBenchmarkReadCollaboratorsRequest, BulkAddBenchmarkReadCollaboratorsResponse, BulkCreateBenchmarksRequest, BulkCreateBenchmarksResponse, BulkRemoveBenchmarkReadCollaboratorsRequest, BulkRemoveBenchmarkReadCollaboratorsResponse, CreateBenchmarkRequest, CreateBenchmarkVersionDoiRequest, CreateBenchmarkVersionDoiResponse, CreateBenchmarkVersionModelMappingsRequest, CreateBenchmarkVersionModelMappingsResponse, CreateBenchmarkVersionRequest, DeleteBenchmarkRequest, DeleteBenchmarkVersionModelMappingsRequest, DeleteBenchmarkVersionModelMappingsResponse, DeleteBenchmarkVersionRequest, DownloadBenchmarkLeaderboardRequest, GetBenchmarkActivityRequest, GetBenchmarkLeaderboardRequest, GetBenchmarkRecommendationsRequest, GetBenchmarkRecommendationsResponse, GetBenchmarkRequest, GetBenchmarkVersionBracketRequest, GetBenchmarkVersionRequest, GetGameArenaStreamsRequest, GetParentBenchmarkVersionIdsRequest, GetParentBenchmarkVersionIdsResponse, GetUnifiedBenchmarkLeaderboardRequest, GetUserBenchmarkCountsRequest, GetUserBenchmarkCountsResponse, IncrementBenchmarkViewCountRequest, ListBenchmarkSampleTasksRequest, ListBenchmarkSampleTasksResponse, ListBenchmarksRequest, ListBenchmarksResponse, ListBenchmarkVersionMappingsRequest, ListBenchmarkVersionMappingsResponse, ListBenchmarkVersionsRequest, ListBenchmarkVersionsResponse, ListOrganizationsRequest, ListOrganizationsResponse, PublishBenchmarkRequest, PublishBenchmarkVersionRequest, RemoveBenchmarkTagRequest, RemoveTaskFromBenchmarkRequest, RestoreBenchmarkRequest, RestoreBenchmarkVersionRequest, UnpublishBenchmarkRequest, UnpublishBenchmarkVersionRequest, UpdateBenchmarkRequest, UpdateBenchmarkVersionBracketRequest, UpdateBenchmarkVersionRequest, UpdateGameArenaStreamsRequest
from kagglesdk.benchmarks.types.benchmark_types import Benchmark, BenchmarkBracket, BenchmarkLeaderboard, BenchmarkVersion, GameArenaStreams, UnifiedBenchmarkLeaderboard
from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_benchmark(self, request: GetBenchmarkRequest = None) -> Benchmark:
    r"""
    Fetches metadata needed to render a Benchmark page. Data to
    render the leaderboard is obtained via GetBenchmarkLeaderboard.

    Args:
      request (GetBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmark", request, Benchmark)

  def list_benchmarks(self, request: ListBenchmarksRequest = None) -> ListBenchmarksResponse:
    r"""
    Args:
      request (ListBenchmarksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarksRequest()

    return self._client.call("benchmarks.BenchmarkService", "ListBenchmarks", request, ListBenchmarksResponse)

  def create_benchmark(self, request: CreateBenchmarkRequest = None) -> Benchmark:
    r"""
    Args:
      request (CreateBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkRequest()

    return self._client.call("benchmarks.BenchmarkService", "CreateBenchmark", request, Benchmark)

  def bulk_create_benchmarks(self, request: BulkCreateBenchmarksRequest = None) -> BulkCreateBenchmarksResponse:
    r"""
    Admin-only handler for creating benchmarks en-masse.

    Args:
      request (BulkCreateBenchmarksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkCreateBenchmarksRequest()

    return self._client.call("benchmarks.BenchmarkService", "BulkCreateBenchmarks", request, BulkCreateBenchmarksResponse)

  def create_benchmark_version(self, request: CreateBenchmarkVersionRequest = None) -> BenchmarkVersion:
    r"""
    Args:
      request (CreateBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkVersionRequest()

    return self._client.call("benchmarks.BenchmarkService", "CreateBenchmarkVersion", request, BenchmarkVersion)

  def update_benchmark(self, request: UpdateBenchmarkRequest = None) -> Benchmark:
    r"""
    Args:
      request (UpdateBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkRequest()

    return self._client.call("benchmarks.BenchmarkService", "UpdateBenchmark", request, Benchmark)

  def update_benchmark_version(self, request: UpdateBenchmarkVersionRequest = None) -> BenchmarkVersion:
    r"""
    Args:
      request (UpdateBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkVersionRequest()

    return self._client.call("benchmarks.BenchmarkService", "UpdateBenchmarkVersion", request, BenchmarkVersion)

  def get_benchmark_version(self, request: GetBenchmarkVersionRequest = None) -> BenchmarkVersion:
    r"""
    Args:
      request (GetBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkVersionRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmarkVersion", request, BenchmarkVersion)

  def list_benchmark_versions(self, request: ListBenchmarkVersionsRequest = None) -> ListBenchmarkVersionsResponse:
    r"""
    Args:
      request (ListBenchmarkVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkVersionsRequest()

    return self._client.call("benchmarks.BenchmarkService", "ListBenchmarkVersions", request, ListBenchmarkVersionsResponse)

  def bulk_add_benchmark_read_collaborators(self, request: BulkAddBenchmarkReadCollaboratorsRequest = None) -> BulkAddBenchmarkReadCollaboratorsResponse:
    r"""
    Admin-only handler for adding benchmark read collaborators en-masse.

    Args:
      request (BulkAddBenchmarkReadCollaboratorsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkAddBenchmarkReadCollaboratorsRequest()

    return self._client.call("benchmarks.BenchmarkService", "BulkAddBenchmarkReadCollaborators", request, BulkAddBenchmarkReadCollaboratorsResponse)

  def bulk_remove_benchmark_read_collaborators(self, request: BulkRemoveBenchmarkReadCollaboratorsRequest = None) -> BulkRemoveBenchmarkReadCollaboratorsResponse:
    r"""
    Admin-only handler for removing benchmark read collaborators en-masse.

    Args:
      request (BulkRemoveBenchmarkReadCollaboratorsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkRemoveBenchmarkReadCollaboratorsRequest()

    return self._client.call("benchmarks.BenchmarkService", "BulkRemoveBenchmarkReadCollaborators", request, BulkRemoveBenchmarkReadCollaboratorsResponse)

  def list_benchmark_version_mappings(self, request: ListBenchmarkVersionMappingsRequest = None) -> ListBenchmarkVersionMappingsResponse:
    r"""
    Args:
      request (ListBenchmarkVersionMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkVersionMappingsRequest()

    return self._client.call("benchmarks.BenchmarkService", "ListBenchmarkVersionMappings", request, ListBenchmarkVersionMappingsResponse)

  def get_benchmark_leaderboard(self, request: GetBenchmarkLeaderboardRequest = None) -> BenchmarkLeaderboard:
    r"""
    Args:
      request (GetBenchmarkLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkLeaderboardRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmarkLeaderboard", request, BenchmarkLeaderboard)

  def get_unified_benchmark_leaderboard(self, request: GetUnifiedBenchmarkLeaderboardRequest = None) -> UnifiedBenchmarkLeaderboard:
    r"""
    Args:
      request (GetUnifiedBenchmarkLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUnifiedBenchmarkLeaderboardRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetUnifiedBenchmarkLeaderboard", request, UnifiedBenchmarkLeaderboard)

  def delete_benchmark(self, request: DeleteBenchmarkRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "DeleteBenchmark", request, None)

  def delete_benchmark_version(self, request: DeleteBenchmarkVersionRequest = None):
    r"""
    Args:
      request (DeleteBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkVersionRequest()

    self._client.call("benchmarks.BenchmarkService", "DeleteBenchmarkVersion", request, None)

  def batch_delete_benchmark_versions(self, request: BatchDeleteBenchmarkVersionsRequest = None):
    r"""
    Args:
      request (BatchDeleteBenchmarkVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteBenchmarkVersionsRequest()

    self._client.call("benchmarks.BenchmarkService", "BatchDeleteBenchmarkVersions", request, None)

  def restore_benchmark(self, request: RestoreBenchmarkRequest = None):
    r"""
    Restore a moderated benchmark and associated version, ex: after a
    successful user appeal.

    Args:
      request (RestoreBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RestoreBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "RestoreBenchmark", request, None)

  def restore_benchmark_version(self, request: RestoreBenchmarkVersionRequest = None):
    r"""
    Restore a moderated benchmark version and associated task version, ex:
    after a successful user appeal.

    Args:
      request (RestoreBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RestoreBenchmarkVersionRequest()

    self._client.call("benchmarks.BenchmarkService", "RestoreBenchmarkVersion", request, None)

  def list_organizations(self, request: ListOrganizationsRequest = None) -> ListOrganizationsResponse:
    r"""
    Args:
      request (ListOrganizationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListOrganizationsRequest()

    return self._client.call("benchmarks.BenchmarkService", "ListOrganizations", request, ListOrganizationsResponse)

  def add_tasks_to_benchmark(self, request: AddTasksToBenchmarkRequest = None):
    r"""
    Args:
      request (AddTasksToBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddTasksToBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "AddTasksToBenchmark", request, None)

  def remove_task_from_benchmark(self, request: RemoveTaskFromBenchmarkRequest = None):
    r"""
    Args:
      request (RemoveTaskFromBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveTaskFromBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "RemoveTaskFromBenchmark", request, None)

  def add_benchmark_tag(self, request: AddBenchmarkTagRequest = None):
    r"""
    Args:
      request (AddBenchmarkTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddBenchmarkTagRequest()

    self._client.call("benchmarks.BenchmarkService", "AddBenchmarkTag", request, None)

  def remove_benchmark_tag(self, request: RemoveBenchmarkTagRequest = None):
    r"""
    Args:
      request (RemoveBenchmarkTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveBenchmarkTagRequest()

    self._client.call("benchmarks.BenchmarkService", "RemoveBenchmarkTag", request, None)

  def get_benchmark_version_bracket(self, request: GetBenchmarkVersionBracketRequest = None) -> BenchmarkBracket:
    r"""
    Args:
      request (GetBenchmarkVersionBracketRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkVersionBracketRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmarkVersionBracket", request, BenchmarkBracket)

  def update_benchmark_version_bracket(self, request: UpdateBenchmarkVersionBracketRequest = None) -> BenchmarkBracket:
    r"""
    Args:
      request (UpdateBenchmarkVersionBracketRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkVersionBracketRequest()

    return self._client.call("benchmarks.BenchmarkService", "UpdateBenchmarkVersionBracket", request, BenchmarkBracket)

  def get_game_arena_streams(self, request: GetGameArenaStreamsRequest = None) -> GameArenaStreams:
    r"""
    Args:
      request (GetGameArenaStreamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetGameArenaStreamsRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetGameArenaStreams", request, GameArenaStreams)

  def update_game_arena_streams(self, request: UpdateGameArenaStreamsRequest = None) -> GameArenaStreams:
    r"""
    Args:
      request (UpdateGameArenaStreamsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateGameArenaStreamsRequest()

    return self._client.call("benchmarks.BenchmarkService", "UpdateGameArenaStreams", request, GameArenaStreams)

  def list_benchmark_sample_tasks(self, request: ListBenchmarkSampleTasksRequest = None) -> ListBenchmarkSampleTasksResponse:
    r"""
    Args:
      request (ListBenchmarkSampleTasksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBenchmarkSampleTasksRequest()

    return self._client.call("benchmarks.BenchmarkService", "ListBenchmarkSampleTasks", request, ListBenchmarkSampleTasksResponse)

  def create_benchmark_version_model_mappings(self, request: CreateBenchmarkVersionModelMappingsRequest = None) -> CreateBenchmarkVersionModelMappingsResponse:
    r"""
    Args:
      request (CreateBenchmarkVersionModelMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkVersionModelMappingsRequest()

    return self._client.call("benchmarks.BenchmarkService", "CreateBenchmarkVersionModelMappings", request, CreateBenchmarkVersionModelMappingsResponse)

  def delete_benchmark_version_model_mappings(self, request: DeleteBenchmarkVersionModelMappingsRequest = None) -> DeleteBenchmarkVersionModelMappingsResponse:
    r"""
    Args:
      request (DeleteBenchmarkVersionModelMappingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBenchmarkVersionModelMappingsRequest()

    return self._client.call("benchmarks.BenchmarkService", "DeleteBenchmarkVersionModelMappings", request, DeleteBenchmarkVersionModelMappingsResponse)

  def publish_benchmark(self, request: PublishBenchmarkRequest = None):
    r"""
    Args:
      request (PublishBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PublishBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "PublishBenchmark", request, None)

  def unpublish_benchmark(self, request: UnpublishBenchmarkRequest = None):
    r"""
    Args:
      request (UnpublishBenchmarkRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnpublishBenchmarkRequest()

    self._client.call("benchmarks.BenchmarkService", "UnpublishBenchmark", request, None)

  def publish_benchmark_version(self, request: PublishBenchmarkVersionRequest = None):
    r"""
    Args:
      request (PublishBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PublishBenchmarkVersionRequest()

    self._client.call("benchmarks.BenchmarkService", "PublishBenchmarkVersion", request, None)

  def unpublish_benchmark_version(self, request: UnpublishBenchmarkVersionRequest = None):
    r"""
    Args:
      request (UnpublishBenchmarkVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnpublishBenchmarkVersionRequest()

    self._client.call("benchmarks.BenchmarkService", "UnpublishBenchmarkVersion", request, None)

  def download_benchmark_leaderboard(self, request: DownloadBenchmarkLeaderboardRequest = None) -> FileDownload:
    r"""
    Generate a CSV made up of leaderboards from given benchmarks

    Args:
      request (DownloadBenchmarkLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DownloadBenchmarkLeaderboardRequest()

    return self._client.call("benchmarks.BenchmarkService", "DownloadBenchmarkLeaderboard", request, FileDownload)

  def get_user_benchmark_counts(self, request: GetUserBenchmarkCountsRequest = None) -> GetUserBenchmarkCountsResponse:
    r"""
    Args:
      request (GetUserBenchmarkCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserBenchmarkCountsRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetUserBenchmarkCounts", request, GetUserBenchmarkCountsResponse)

  def get_benchmark_recommendations(self, request: GetBenchmarkRecommendationsRequest = None) -> GetBenchmarkRecommendationsResponse:
    r"""
    Args:
      request (GetBenchmarkRecommendationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkRecommendationsRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmarkRecommendations", request, GetBenchmarkRecommendationsResponse)

  def increment_benchmark_view_count(self, request: IncrementBenchmarkViewCountRequest = None):
    r"""
    Args:
      request (IncrementBenchmarkViewCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = IncrementBenchmarkViewCountRequest()

    self._client.call("benchmarks.BenchmarkService", "IncrementBenchmarkViewCount", request, None)

  def get_benchmark_activity(self, request: GetBenchmarkActivityRequest = None) -> BenchmarkActivityResponse:
    r"""
    Args:
      request (GetBenchmarkActivityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBenchmarkActivityRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetBenchmarkActivity", request, BenchmarkActivityResponse)

  def get_parent_benchmark_version_ids(self, request: GetParentBenchmarkVersionIdsRequest = None) -> GetParentBenchmarkVersionIdsResponse:
    r"""
    Args:
      request (GetParentBenchmarkVersionIdsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetParentBenchmarkVersionIdsRequest()

    return self._client.call("benchmarks.BenchmarkService", "GetParentBenchmarkVersionIds", request, GetParentBenchmarkVersionIdsResponse)

  def create_benchmark_version_doi(self, request: CreateBenchmarkVersionDoiRequest = None) -> CreateBenchmarkVersionDoiResponse:
    r"""
    Args:
      request (CreateBenchmarkVersionDoiRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBenchmarkVersionDoiRequest()

    return self._client.call("benchmarks.BenchmarkService", "CreateBenchmarkVersionDoi", request, CreateBenchmarkVersionDoiResponse)
