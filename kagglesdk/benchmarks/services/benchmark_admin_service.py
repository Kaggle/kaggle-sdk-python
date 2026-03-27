from kagglesdk.benchmarks.types.benchmark_admin_service import BackfillBenchmarkAclsRequest, BackfillBenchmarkAclsResponse, BackfillBenchmarkRunMetadataRequest, BackfillBenchmarkRunMetadataResponse, BackfillBenchmarkRunStatesRequest, BackfillBenchmarkRunStatesResponse, BackfillBenchmarkUpdateTimeRequest, BackfillBenchmarkUpdateTimeResponse, BulkCreateBenchmarkTasksRequest, BulkCreateBenchmarkTasksResponse, CopyCitationToChildBenchmarkVersionsRequest, CopyCitationToChildBenchmarkVersionsResponse, CopyMediaToChildBenchmarkVersionsRequest, CopyMediaToChildBenchmarkVersionsResponse, GetResearchBenchmarkModelCoverageRequest, GetResearchBenchmarkModelCoverageResponse, InvalidateBenchmarkLeaderboardCacheRequest, InvalidateBenchmarkLeaderboardCacheResponse, MigrateKaggleNotebookMediaRequest, MigrateKaggleNotebookMediaResponse, UpdateBenchmarkTaskOwnerRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BenchmarkAdminClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def invalidate_benchmark_leaderboard_cache(self, request: InvalidateBenchmarkLeaderboardCacheRequest = None) -> InvalidateBenchmarkLeaderboardCacheResponse:
    r"""
    RPC to invalidate/clear the leaderboard cache for a set of benchmark
    versions

    Args:
      request (InvalidateBenchmarkLeaderboardCacheRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateBenchmarkLeaderboardCacheRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "InvalidateBenchmarkLeaderboardCache", request, InvalidateBenchmarkLeaderboardCacheResponse)

  def backfill_benchmark_acls(self, request: BackfillBenchmarkAclsRequest = None) -> BackfillBenchmarkAclsResponse:
    r"""
    RPC To backfill benchmark writer and admin groups.

    Args:
      request (BackfillBenchmarkAclsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackfillBenchmarkAclsRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "BackfillBenchmarkAcls", request, BackfillBenchmarkAclsResponse)

  def bulk_create_benchmark_tasks(self, request: BulkCreateBenchmarkTasksRequest = None) -> BulkCreateBenchmarkTasksResponse:
    r"""
    Admin-only handler for manually creating benchmark tasks and task versions.
    Not to be confused with CreateBenchmarkTask in the Benchmark Task Service
    which creates tasks from notebook outputs.

    Args:
      request (BulkCreateBenchmarkTasksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkCreateBenchmarkTasksRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "BulkCreateBenchmarkTasks", request, BulkCreateBenchmarkTasksResponse)

  def update_benchmark_task_owner(self, request: UpdateBenchmarkTaskOwnerRequest = None):
    r"""
    Args:
      request (UpdateBenchmarkTaskOwnerRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBenchmarkTaskOwnerRequest()

    self._client.call("benchmarks.BenchmarkAdminService", "UpdateBenchmarkTaskOwner", request, None)

  def copy_media_to_child_benchmark_versions(self, request: CopyMediaToChildBenchmarkVersionsRequest = None) -> CopyMediaToChildBenchmarkVersionsResponse:
    r"""
    Admin-only handler that copies media to all mapped child benchmark
    versions.

    Args:
      request (CopyMediaToChildBenchmarkVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CopyMediaToChildBenchmarkVersionsRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "CopyMediaToChildBenchmarkVersions", request, CopyMediaToChildBenchmarkVersionsResponse)

  def copy_citation_to_child_benchmark_versions(self, request: CopyCitationToChildBenchmarkVersionsRequest = None) -> CopyCitationToChildBenchmarkVersionsResponse:
    r"""
    Admin-only handler that copies citation to all mapped child benchmark
    versions.

    Args:
      request (CopyCitationToChildBenchmarkVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CopyCitationToChildBenchmarkVersionsRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "CopyCitationToChildBenchmarkVersions", request, CopyCitationToChildBenchmarkVersionsResponse)

  def migrate_kaggle_notebook_media(self, request: MigrateKaggleNotebookMediaRequest = None) -> MigrateKaggleNotebookMediaResponse:
    r"""
    Admin-only handler that migrates all kaggle notebook media links to the
    'kerneler' account.

    Args:
      request (MigrateKaggleNotebookMediaRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MigrateKaggleNotebookMediaRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "MigrateKaggleNotebookMedia", request, MigrateKaggleNotebookMediaResponse)

  def backfill_benchmark_run_states(self, request: BackfillBenchmarkRunStatesRequest = None) -> BackfillBenchmarkRunStatesResponse:
    r"""
    Admin-only handler that backfills BenchmarkRun.State from the stored
    BenchmarkTaskRun blob in GCS for all runs with UNSPECIFIED state.

    Args:
      request (BackfillBenchmarkRunStatesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackfillBenchmarkRunStatesRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "BackfillBenchmarkRunStates", request, BackfillBenchmarkRunStatesResponse)

  def backfill_benchmark_run_metadata(self, request: BackfillBenchmarkRunMetadataRequest = None) -> BackfillBenchmarkRunMetadataResponse:
    r"""
    Admin-only handler that backfills BenchmarkRun.StartTime and EndTime
    for runs with null values.

    Args:
      request (BackfillBenchmarkRunMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackfillBenchmarkRunMetadataRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "BackfillBenchmarkRunMetadata", request, BackfillBenchmarkRunMetadataResponse)

  def backfill_benchmark_update_time(self, request: BackfillBenchmarkUpdateTimeRequest = None) -> BackfillBenchmarkUpdateTimeResponse:
    r"""
    Admin-only handler that backfills Benchmark.UpdateTime with the maximum
    associated BenchmarkVersion.UpdateTime for each benchmark.

    Args:
      request (BackfillBenchmarkUpdateTimeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackfillBenchmarkUpdateTimeRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "BackfillBenchmarkUpdateTime", request, BackfillBenchmarkUpdateTimeResponse)

  def get_research_benchmark_model_coverage(self, request: GetResearchBenchmarkModelCoverageRequest = None) -> GetResearchBenchmarkModelCoverageResponse:
    r"""
    Returns model coverage information for research benchmarks.
    For each model version with a non-UNSPECIFIED importance level,
    reports whether it has been run on each benchmark version with a
    non-UNSPECIFIED maintenance level.

    Args:
      request (GetResearchBenchmarkModelCoverageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetResearchBenchmarkModelCoverageRequest()

    return self._client.call("benchmarks.BenchmarkAdminService", "GetResearchBenchmarkModelCoverage", request, GetResearchBenchmarkModelCoverageResponse)
