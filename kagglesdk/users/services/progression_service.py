from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.progression_service import BatchSetUsersToRecalcRequest, BatchSetUsersToRecalcResponse, BatchUpdateUserAchievementsRequest, BatchUpdateUserAchievementsResponse, GetCurrentUserProgressionRequest, GetCurrentUserProgressionResponse, PerformMedalCeremonyExperimentRequest, PerformMedalCeremonyExperimentResponse, UpdateUserAchievementsRequest, UpdateUserAchievementsResponse

class ProgressionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_current_user_progression(self, request: GetCurrentUserProgressionRequest = None) -> GetCurrentUserProgressionResponse:
    r"""
    Gets the progression tiers and current rankings for the current user

    Args:
      request (GetCurrentUserProgressionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCurrentUserProgressionRequest()

    return self._client.call("users.ProgressionService", "GetCurrentUserProgression", request, GetCurrentUserProgressionResponse)

  def update_user_achievements(self, request: UpdateUserAchievementsRequest = None) -> UpdateUserAchievementsResponse:
    r"""
    Syncs the progression medals and tiers for the given user with individual
    content medals and achievements

    Args:
      request (UpdateUserAchievementsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserAchievementsRequest()

    return self._client.call("users.ProgressionService", "UpdateUserAchievements", request, UpdateUserAchievementsResponse)

  def batch_set_users_to_recalc(self, request: BatchSetUsersToRecalcRequest = None) -> BatchSetUsersToRecalcResponse:
    r"""
    Sets a list of users by user ids to recalc performance tier.

    Args:
      request (BatchSetUsersToRecalcRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchSetUsersToRecalcRequest()

    return self._client.call("users.ProgressionService", "BatchSetUsersToRecalc", request, BatchSetUsersToRecalcResponse)

  def batch_update_user_achievements(self, request: BatchUpdateUserAchievementsRequest = None) -> BatchUpdateUserAchievementsResponse:
    r"""
    Updates UserAchievements for a list of users by user ids.
    This naturally occurs during the medal ceremony, but sometimes we want to
    one-off update users' achievements. For example, after a data migration, or
    if the medal ceremony threw exceptions and we're in a state where users
    have medals, but their achievements are not updated. ex: http://b/424290878

    Args:
      request (BatchUpdateUserAchievementsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchUpdateUserAchievementsRequest()

    return self._client.call("users.ProgressionService", "BatchUpdateUserAchievements", request, BatchUpdateUserAchievementsResponse)

  def perform_medal_ceremony_experiment(self, request: PerformMedalCeremonyExperimentRequest = None) -> PerformMedalCeremonyExperimentResponse:
    r"""
    A test route that runs a 'what-if' version of the medal ceremony and logs
    what would change. Used to test out changes to the medal ceremony on live
    data without breaking anything.

    Args:
      request (PerformMedalCeremonyExperimentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PerformMedalCeremonyExperimentRequest()

    return self._client.call("users.ProgressionService", "PerformMedalCeremonyExperiment", request, PerformMedalCeremonyExperimentResponse)
