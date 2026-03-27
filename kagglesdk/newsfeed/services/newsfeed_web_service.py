from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.newsfeed.types.newsfeed_web_service import GetDsSurveyBannerStateRequest, GetDsSurveyBannerStateResponse, GetNewAndExcitingContentRequest, GetNewAndExcitingContentResponse, GetNewsfeedSidebarContentRequest, GetStoriesRequest, GetStoriesResponse, NewsfeedSidebarContent, SetDsSurveyBannerStateRequest

class NewsfeedWebClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_ds_survey_banner_state(self, request: GetDsSurveyBannerStateRequest = None) -> GetDsSurveyBannerStateResponse:
    r"""
    Args:
      request (GetDsSurveyBannerStateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDsSurveyBannerStateRequest()

    return self._client.call("newsfeed.NewsfeedWebService", "GetDsSurveyBannerState", request, GetDsSurveyBannerStateResponse)

  def get_stories(self, request: GetStoriesRequest = None) -> GetStoriesResponse:
    r"""
    Args:
      request (GetStoriesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetStoriesRequest()

    return self._client.call("newsfeed.NewsfeedWebService", "GetStories", request, GetStoriesResponse)

  def set_ds_survey_banner_state(self, request: SetDsSurveyBannerStateRequest = None):
    r"""
    Args:
      request (SetDsSurveyBannerStateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetDsSurveyBannerStateRequest()

    self._client.call("newsfeed.NewsfeedWebService", "SetDsSurveyBannerState", request, None)

  def get_newsfeed_sidebar_content(self, request: GetNewsfeedSidebarContentRequest = None) -> NewsfeedSidebarContent:
    r"""
    Args:
      request (GetNewsfeedSidebarContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNewsfeedSidebarContentRequest()

    return self._client.call("newsfeed.NewsfeedWebService", "GetNewsfeedSidebarContent", request, NewsfeedSidebarContent)

  def get_new_and_exciting_content(self, request: GetNewAndExcitingContentRequest = None) -> GetNewAndExcitingContentResponse:
    r"""
    Args:
      request (GetNewAndExcitingContentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetNewAndExcitingContentRequest()

    return self._client.call("newsfeed.NewsfeedWebService", "GetNewAndExcitingContent", request, GetNewAndExcitingContentResponse)
