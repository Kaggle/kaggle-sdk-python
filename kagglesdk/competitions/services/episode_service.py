from kagglesdk.competitions.types.episode import Episode
from kagglesdk.competitions.types.episode_service import BulkCancelEpisodesRequest, BulkSetEpisodeRewardsRequest, BulkSetEpisodeRewardsResponse, CancelEpisodeRequest, CreateEpisodeRequest, GenerateEpisodesForCompetitionRequest, GenerateEpisodesForCompetitionResponse, GetEpisodeRequest, GetEpisodeResponse, GetEpisodeSummaryRequest, GetEpisodeSummaryResponse, ListEpisodesFromCompetitionRequest, ListEpisodesFromCompetitionResponse, ListEpisodesRequest, ListEpisodesResponse, ListValidationEpisodesRequest, ListValidationEpisodesResponse, MarkEnvironmentSubmissionValidatedRequest, SetEpisodeErroredRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class EpisodeClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_episode(self, request: CreateEpisodeRequest = None) -> Episode:
    r"""
    Args:
      request (CreateEpisodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateEpisodeRequest()

    return self._client.call("competitions.EpisodeService", "CreateEpisode", request, Episode)

  def generate_episodes_for_competition(self, request: GenerateEpisodesForCompetitionRequest = None) -> GenerateEpisodesForCompetitionResponse:
    r"""
    For a given Sims Comp, kick off some new Episodes.  Intended for use
    by the GenerateEpisodes scheduled handler (see below).

    Args:
      request (GenerateEpisodesForCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GenerateEpisodesForCompetitionRequest()

    return self._client.call("competitions.EpisodeService", "GenerateEpisodesForCompetition", request, GenerateEpisodesForCompetitionResponse)

  def get_episode(self, request: GetEpisodeRequest = None) -> GetEpisodeResponse:
    r"""
    Args:
      request (GetEpisodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetEpisodeRequest()

    return self._client.call("competitions.EpisodeService", "GetEpisode", request, GetEpisodeResponse)

  def list_episodes(self, request: ListEpisodesRequest = None) -> ListEpisodesResponse:
    r"""
    Lists Episodes of type Completed for a given filter. Currently top 1000
    only, by most recent EndTime.

    Args:
      request (ListEpisodesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListEpisodesRequest()

    return self._client.call("competitions.EpisodeService", "ListEpisodes", request, ListEpisodesResponse)

  def set_episode_errored(self, request: SetEpisodeErroredRequest = None):
    r"""
    Args:
      request (SetEpisodeErroredRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetEpisodeErroredRequest()

    self._client.call("competitions.EpisodeService", "SetEpisodeErrored", request, None)

  def bulk_set_episode_rewards(self, request: BulkSetEpisodeRewardsRequest = None) -> BulkSetEpisodeRewardsResponse:
    r"""
    Admin-only bulk action: invokes SetEpisodeRewards for every episode that
    matches the provided filter. Defaults to dry_run = true, in which case the
    matching episodes are counted but not processed.

    Args:
      request (BulkSetEpisodeRewardsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkSetEpisodeRewardsRequest()

    return self._client.call("competitions.EpisodeService", "BulkSetEpisodeRewards", request, BulkSetEpisodeRewardsResponse)

  def cancel_episode(self, request: CancelEpisodeRequest = None):
    r"""
    Args:
      request (CancelEpisodeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CancelEpisodeRequest()

    self._client.call("competitions.EpisodeService", "CancelEpisode", request, None)

  def bulk_cancel_episodes(self, request: BulkCancelEpisodesRequest = None):
    r"""
    Args:
      request (BulkCancelEpisodesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BulkCancelEpisodesRequest()

    self._client.call("competitions.EpisodeService", "BulkCancelEpisodes", request, None)

  def list_episodes_from_competition(self, request: ListEpisodesFromCompetitionRequest = None) -> ListEpisodesFromCompetitionResponse:
    r"""
    List all episodes from a provided competition

    Args:
      request (ListEpisodesFromCompetitionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListEpisodesFromCompetitionRequest()

    return self._client.call("competitions.EpisodeService", "ListEpisodesFromCompetition", request, ListEpisodesFromCompetitionResponse)

  def get_episode_summary(self, request: GetEpisodeSummaryRequest = None) -> GetEpisodeSummaryResponse:
    r"""
    Returns per-EpisodeType counts of recent episode activity for a single
    competition: started in the last 24h, currently in-flight, completed in
    the last 24h, and errored in the last 24h. Backs the admin 'Episode
    Summary' tab.

    Args:
      request (GetEpisodeSummaryRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetEpisodeSummaryRequest()

    return self._client.call("competitions.EpisodeService", "GetEpisodeSummary", request, GetEpisodeSummaryResponse)

  def list_validation_episodes(self, request: ListValidationEpisodesRequest = None) -> ListValidationEpisodesResponse:
    r"""
    Args:
      request (ListValidationEpisodesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListValidationEpisodesRequest()

    return self._client.call("competitions.EpisodeService", "ListValidationEpisodes", request, ListValidationEpisodesResponse)

  def mark_environment_submission_validated(self, request: MarkEnvironmentSubmissionValidatedRequest = None):
    r"""
    Args:
      request (MarkEnvironmentSubmissionValidatedRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MarkEnvironmentSubmissionValidatedRequest()

    self._client.call("competitions.EpisodeService", "MarkEnvironmentSubmissionValidated", request, None)
