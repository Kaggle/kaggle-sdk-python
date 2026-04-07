from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.homepage_service import AddSuggestedItemRequest, AddSuggestedItemResponse, DismissSuggestedItemRequest, ForceUpdateLoggedOutHomepageDataRequest, GetHomePageStatsRequest, GetHomePageStatsResponse, GetLoggedOutHomepageDataRequest, GetLoggedOutHomepageDataResponse, GetNextStepsConfigRequest, GetNextStepsConfigResponse, GetNextStepsRequest, GetNextStepsResponse, UpdateUserRegionRequest

class HomePageClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_next_steps(self, request: GetNextStepsRequest = None) -> GetNextStepsResponse:
    r"""
    Get all the data associated with showing the 'Next Steps' section on the
    homepage.

    Args:
      request (GetNextStepsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNextStepsRequest()

    return self._client.call("users.HomePageService", "GetNextSteps", request, GetNextStepsResponse)

  def get_home_page_stats(self, request: GetHomePageStatsRequest = None) -> GetHomePageStatsResponse:
    r"""
    Get all the stats that appear on the homepage for the current logged in
    user.

    Args:
      request (GetHomePageStatsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHomePageStatsRequest()

    return self._client.call("users.HomePageService", "GetHomePageStats", request, GetHomePageStatsResponse)

  def dismiss_suggested_item(self, request: DismissSuggestedItemRequest = None):
    r"""
    Mark a suggested item as dismissed, will put it at the bottom of the list
    and stop showing for today.

    Args:
      request (DismissSuggestedItemRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DismissSuggestedItemRequest()

    self._client.call("users.HomePageService", "DismissSuggestedItem", request, None)

  def get_next_steps_config(self, request: GetNextStepsConfigRequest = None) -> GetNextStepsConfigResponse:
    r"""
    Get all the data needed to configure next steps (admin-only route).

    Args:
      request (GetNextStepsConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNextStepsConfigRequest()

    return self._client.call("users.HomePageService", "GetNextStepsConfig", request, GetNextStepsConfigResponse)

  def add_suggested_item(self, request: AddSuggestedItemRequest = None) -> AddSuggestedItemResponse:
    r"""
    Create a new placeholder suggested item (admin-only route).

    Args:
      request (AddSuggestedItemRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddSuggestedItemRequest()

    return self._client.call("users.HomePageService", "AddSuggestedItem", request, AddSuggestedItemResponse)

  def get_logged_out_homepage_data(self, request: GetLoggedOutHomepageDataRequest = None) -> GetLoggedOutHomepageDataResponse:
    r"""
    Returns all the numerical and listing data required to render the
    logged-out homepage.

    Args:
      request (GetLoggedOutHomepageDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLoggedOutHomepageDataRequest()

    return self._client.call("users.HomePageService", "GetLoggedOutHomepageData", request, GetLoggedOutHomepageDataResponse)

  def force_update_logged_out_homepage_data(self, request: ForceUpdateLoggedOutHomepageDataRequest = None):
    r"""
    Similar to UpdateLoggedOutHomepageData but called from admin-initiated
    flows instead of a scheduled task.

    Args:
      request (ForceUpdateLoggedOutHomepageDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ForceUpdateLoggedOutHomepageDataRequest()

    self._client.call("users.HomePageService", "ForceUpdateLoggedOutHomepageData", request, None)

  def update_user_region(self, request: UpdateUserRegionRequest = None):
    r"""
    Args:
      request (UpdateUserRegionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserRegionRequest()

    self._client.call("users.HomePageService", "UpdateUserRegion", request, None)
