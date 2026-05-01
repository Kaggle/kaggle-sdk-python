from kagglesdk.discussions.types.discussions_api_service import ApiGetTopicRequest, ApiGetTopicResponse, ApiListCommentsRequest, ApiListCommentsResponse, ApiListForumsRequest, ApiListForumsResponse, ApiListTopicsRequest, ApiListTopicsResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DiscussionApiClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_forums(self, request: ApiListForumsRequest = None) -> ApiListForumsResponse:
    r"""
    List all top-level discussion forums on Kaggle.

    Args:
      request (ApiListForumsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListForumsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListForums", request, ApiListForumsResponse)

  def list_topics(self, request: ApiListTopicsRequest = None) -> ApiListTopicsResponse:
    r"""
    List and search discussion topics, optionally filtered by forum.

    Args:
      request (ApiListTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListTopicsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListTopics", request, ApiListTopicsResponse)

  def get_topic(self, request: ApiGetTopicRequest = None) -> ApiGetTopicResponse:
    r"""
    Get a single discussion topic by ID.

    Args:
      request (ApiGetTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiGetTopicRequest()

    return self._client.call("discussions.DiscussionApiService", "GetTopic", request, ApiGetTopicResponse)

  def list_comments(self, request: ApiListCommentsRequest = None) -> ApiListCommentsResponse:
    r"""
    List comments for a discussion topic, with pagination.

    Args:
      request (ApiListCommentsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListCommentsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListComments", request, ApiListCommentsResponse)
