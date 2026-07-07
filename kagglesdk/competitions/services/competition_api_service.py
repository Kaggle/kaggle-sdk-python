from kagglesdk.common.types.file_download import FileDownload
from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.competitions.types.competition_api_service import ApiCompetition, ApiCompetitionPage, ApiCompetitionSolutionStatus, ApiCreateCodeSubmissionRequest, ApiCreateCodeSubmissionResponse, ApiCreateCompetitionDataRequest, ApiCreateCompetitionDataResponse, ApiCreateCompetitionPageRequest, ApiCreateCompetitionRequest, ApiCreateCompetitionResponse, ApiCreateCompetitionSampleSubmissionRequest, ApiCreateCompetitionSolutionRequest, ApiCreateSubmissionRequest, ApiCreateSubmissionResponse, ApiDeleteCompetitionPageRequest, ApiDownloadDataFileRequest, ApiDownloadDataFilesRequest, ApiDownloadLeaderboardRequest, ApiGetCompetitionDataFilesSummaryRequest, ApiGetCompetitionRequest, ApiGetCompetitionSettingsRequest, ApiGetCompetitionSolutionStatusRequest, ApiGetEpisodeAgentLogsRequest, ApiGetEpisodeReplayRequest, ApiGetLeaderboardRequest, ApiGetLeaderboardResponse, ApiGetSubmissionRequest, ApiLaunchCompetitionRequest, ApiListCompetitionHostsRequest, ApiListCompetitionHostsResponse, ApiListCompetitionPagesRequest, ApiListCompetitionPagesResponse, ApiListCompetitionsRequest, ApiListCompetitionsResponse, ApiListCompetitionTopicsRequest, ApiListCompetitionTopicsResponse, ApiListDataFilesRequest, ApiListDataFilesResponse, ApiListDataTreeFilesRequest, ApiListSubmissionEpisodesRequest, ApiListSubmissionEpisodesResponse, ApiListSubmissionsRequest, ApiListSubmissionsResponse, ApiListTeamPublicSubmissionsRequest, ApiListTeamPublicSubmissionsResponse, ApiListTopicMessagesRequest, ApiListTopicMessagesResponse, ApiStartSubmissionUploadRequest, ApiStartSubmissionUploadResponse, ApiSubmission, ApiUpdateCompetitionPageRequest, ApiUpdateCompetitionSettingsRequest
from kagglesdk.competitions.types.host_service import CompetitionSettings
from kagglesdk.datasets.databundles.types.databundle_api_types import ApiDirectoryContent, ApiFilesSummary
from kagglesdk.kaggle_http_client import KaggleHttpClient

class CompetitionApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_competitions(self, request: ApiListCompetitionsRequest = None) -> ApiListCompetitionsResponse:
    r"""
    Args:
      request (ApiListCompetitionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCompetitionsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListCompetitions", request, ApiListCompetitionsResponse)

  def create_competition(self, request: ApiCreateCompetitionRequest = None) -> ApiCreateCompetitionResponse:
    r"""
    Args:
      request (ApiCreateCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCompetitionRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateCompetition", request, ApiCreateCompetitionResponse)

  def list_submissions(self, request: ApiListSubmissionsRequest = None) -> ApiListSubmissionsResponse:
    r"""
    Args:
      request (ApiListSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListSubmissionsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListSubmissions", request, ApiListSubmissionsResponse)

  def list_team_public_submissions(self, request: ApiListTeamPublicSubmissionsRequest = None) -> ApiListTeamPublicSubmissionsResponse:
    r"""
    Args:
      request (ApiListTeamPublicSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListTeamPublicSubmissionsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListTeamPublicSubmissions", request, ApiListTeamPublicSubmissionsResponse)

  def list_data_files(self, request: ApiListDataFilesRequest = None) -> ApiListDataFilesResponse:
    r"""
    Args:
      request (ApiListDataFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDataFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListDataFiles", request, ApiListDataFilesResponse)

  def list_data_tree_files(self, request: ApiListDataTreeFilesRequest = None) -> ApiDirectoryContent:
    r"""
    Args:
      request (ApiListDataTreeFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDataTreeFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListDataTreeFiles", request, ApiDirectoryContent)

  def get_leaderboard(self, request: ApiGetLeaderboardRequest = None) -> ApiGetLeaderboardResponse:
    r"""
    Args:
      request (ApiGetLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetLeaderboardRequest()

    return self._client.call("competitions.CompetitionApiService", "GetLeaderboard", request, ApiGetLeaderboardResponse)

  def download_leaderboard(self, request: ApiDownloadLeaderboardRequest = None) -> FileDownload:
    r"""
    Args:
      request (ApiDownloadLeaderboardRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadLeaderboardRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadLeaderboard", request, FileDownload)

  def create_submission(self, request: ApiCreateSubmissionRequest = None) -> ApiCreateSubmissionResponse:
    r"""
    Args:
      request (ApiCreateSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateSubmission", request, ApiCreateSubmissionResponse)

  def create_code_submission(self, request: ApiCreateCodeSubmissionRequest = None) -> ApiCreateCodeSubmissionResponse:
    r"""
    Args:
      request (ApiCreateCodeSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCodeSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateCodeSubmission", request, ApiCreateCodeSubmissionResponse)

  def get_submission(self, request: ApiGetSubmissionRequest = None) -> ApiSubmission:
    r"""
    Args:
      request (ApiGetSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetSubmissionRequest()

    return self._client.call("competitions.CompetitionApiService", "GetSubmission", request, ApiSubmission)

  def start_submission_upload(self, request: ApiStartSubmissionUploadRequest = None) -> ApiStartSubmissionUploadResponse:
    r"""
    Args:
      request (ApiStartSubmissionUploadRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiStartSubmissionUploadRequest()

    return self._client.call("competitions.CompetitionApiService", "StartSubmissionUpload", request, ApiStartSubmissionUploadResponse)

  def download_data_files(self, request: ApiDownloadDataFilesRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadDataFilesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDataFilesRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadDataFiles", request, HttpRedirect)

  def download_data_file(self, request: ApiDownloadDataFileRequest = None) -> HttpRedirect:
    r"""
    Args:
      request (ApiDownloadDataFileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDownloadDataFileRequest()

    return self._client.call("competitions.CompetitionApiService", "DownloadDataFile", request, HttpRedirect)

  def get_competition(self, request: ApiGetCompetitionRequest = None) -> ApiCompetition:
    r"""
    Args:
      request (ApiGetCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetition", request, ApiCompetition)

  def get_competition_data_files_summary(self, request: ApiGetCompetitionDataFilesSummaryRequest = None) -> ApiFilesSummary:
    r"""
    Args:
      request (ApiGetCompetitionDataFilesSummaryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionDataFilesSummaryRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetitionDataFilesSummary", request, ApiFilesSummary)

  def list_submission_episodes(self, request: ApiListSubmissionEpisodesRequest = None) -> ApiListSubmissionEpisodesResponse:
    r"""
    Args:
      request (ApiListSubmissionEpisodesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListSubmissionEpisodesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListSubmissionEpisodes", request, ApiListSubmissionEpisodesResponse)

  def get_episode_replay(self, request: ApiGetEpisodeReplayRequest = None) -> FileDownload:
    r"""
    Args:
      request (ApiGetEpisodeReplayRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetEpisodeReplayRequest()

    return self._client.call("competitions.CompetitionApiService", "GetEpisodeReplay", request, FileDownload)

  def get_episode_agent_logs(self, request: ApiGetEpisodeAgentLogsRequest = None) -> FileDownload:
    r"""
    Args:
      request (ApiGetEpisodeAgentLogsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetEpisodeAgentLogsRequest()

    return self._client.call("competitions.CompetitionApiService", "GetEpisodeAgentLogs", request, FileDownload)

  def list_competition_pages(self, request: ApiListCompetitionPagesRequest = None) -> ApiListCompetitionPagesResponse:
    r"""
    Args:
      request (ApiListCompetitionPagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCompetitionPagesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListCompetitionPages", request, ApiListCompetitionPagesResponse)

  def create_competition_page(self, request: ApiCreateCompetitionPageRequest = None) -> ApiCompetitionPage:
    r"""
    Args:
      request (ApiCreateCompetitionPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCompetitionPageRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateCompetitionPage", request, ApiCompetitionPage)

  def update_competition_page(self, request: ApiUpdateCompetitionPageRequest = None) -> ApiCompetitionPage:
    r"""
    Args:
      request (ApiUpdateCompetitionPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateCompetitionPageRequest()

    return self._client.call("competitions.CompetitionApiService", "UpdateCompetitionPage", request, ApiCompetitionPage)

  def delete_competition_page(self, request: ApiDeleteCompetitionPageRequest = None):
    r"""
    Args:
      request (ApiDeleteCompetitionPageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiDeleteCompetitionPageRequest()

    self._client.call("competitions.CompetitionApiService", "DeleteCompetitionPage", request, None)

  def update_competition_settings(self, request: ApiUpdateCompetitionSettingsRequest = None) -> CompetitionSettings:
    r"""
    Args:
      request (ApiUpdateCompetitionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiUpdateCompetitionSettingsRequest()

    return self._client.call("competitions.CompetitionApiService", "UpdateCompetitionSettings", request, CompetitionSettings)

  def get_competition_settings(self, request: ApiGetCompetitionSettingsRequest = None) -> CompetitionSettings:
    r"""
    Args:
      request (ApiGetCompetitionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionSettingsRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetitionSettings", request, CompetitionSettings)

  def launch_competition(self, request: ApiLaunchCompetitionRequest = None):
    r"""
    Args:
      request (ApiLaunchCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiLaunchCompetitionRequest()

    self._client.call("competitions.CompetitionApiService", "LaunchCompetition", request, None)

  def create_competition_data(self, request: ApiCreateCompetitionDataRequest = None) -> ApiCreateCompetitionDataResponse:
    r"""
    Not MCP-exported: the prerequisite blob upload step (start_blob_upload +
    signed-URL PUT) has no MCP equivalent, so the tool would be unusable from
    MCP clients today. Public REST + Python SDK only; the kaggle CLI drives it.

    Args:
      request (ApiCreateCompetitionDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCompetitionDataRequest()

    return self._client.call("competitions.CompetitionApiService", "CreateCompetitionData", request, ApiCreateCompetitionDataResponse)

  def create_competition_solution(self, request: ApiCreateCompetitionSolutionRequest = None):
    r"""
    Not MCP-exported: the prerequisite blob upload step (start_blob_upload +
    signed-URL PUT) has no MCP equivalent, so the tool would be unusable from
    MCP clients today. Public REST + Python SDK only; the kaggle CLI drives it.

    Args:
      request (ApiCreateCompetitionSolutionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCompetitionSolutionRequest()

    self._client.call("competitions.CompetitionApiService", "CreateCompetitionSolution", request, None)

  def get_competition_solution_status(self, request: ApiGetCompetitionSolutionStatusRequest = None) -> ApiCompetitionSolutionStatus:
    r"""
    Args:
      request (ApiGetCompetitionSolutionStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetCompetitionSolutionStatusRequest()

    return self._client.call("competitions.CompetitionApiService", "GetCompetitionSolutionStatus", request, ApiCompetitionSolutionStatus)

  def create_competition_sample_submission(self, request: ApiCreateCompetitionSampleSubmissionRequest = None):
    r"""
    Not MCP-exported: the prerequisite blob upload step (start_blob_upload +
    signed-URL PUT) has no MCP equivalent, so the tool would be unusable from
    MCP clients today. Public REST + Python SDK only; the kaggle CLI drives it.

    Args:
      request (ApiCreateCompetitionSampleSubmissionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiCreateCompetitionSampleSubmissionRequest()

    self._client.call("competitions.CompetitionApiService", "CreateCompetitionSampleSubmission", request, None)

  def list_competition_hosts(self, request: ApiListCompetitionHostsRequest = None) -> ApiListCompetitionHostsResponse:
    r"""
    Args:
      request (ApiListCompetitionHostsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCompetitionHostsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListCompetitionHosts", request, ApiListCompetitionHostsResponse)

  def list_competition_topics(self, request: ApiListCompetitionTopicsRequest = None) -> ApiListCompetitionTopicsResponse:
    r"""
    Args:
      request (ApiListCompetitionTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCompetitionTopicsRequest()

    return self._client.call("competitions.CompetitionApiService", "ListCompetitionTopics", request, ApiListCompetitionTopicsResponse)

  def list_topic_messages(self, request: ApiListTopicMessagesRequest = None) -> ApiListTopicMessagesResponse:
    r"""
    Args:
      request (ApiListTopicMessagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListTopicMessagesRequest()

    return self._client.call("competitions.CompetitionApiService", "ListTopicMessages", request, ApiListTopicMessagesResponse)
