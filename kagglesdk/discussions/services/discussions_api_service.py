from kagglesdk.discussions.types.discussions_api_service import ApiGetTopicRequest, ApiGetTopicResponse, ApiListBenchmarkTopicsRequest, ApiListCommentsRequest, ApiListCommentsResponse, ApiListDatasetTopicsRequest, ApiListForumsRequest, ApiListForumsResponse, ApiListKernelTopicsRequest, ApiListModelTopicsRequest, ApiListTopicsRequest, ApiListTopicsResponse
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

  def list_dataset_topics(self, request: ApiListDatasetTopicsRequest = None) -> ApiListTopicsResponse:
    r"""
    List discussion topics for a dataset.

    Args:
      request (ApiListDatasetTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListDatasetTopicsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListDatasetTopics", request, ApiListTopicsResponse)

  def list_model_topics(self, request: ApiListModelTopicsRequest = None) -> ApiListTopicsResponse:
    r"""
    List discussion topics for a model.

    Args:
      request (ApiListModelTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListModelTopicsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListModelTopics", request, ApiListTopicsResponse)

  def list_benchmark_topics(self, request: ApiListBenchmarkTopicsRequest = None) -> ApiListTopicsResponse:
    r"""
    List discussion topics for a benchmark.

    Args:
      request (ApiListBenchmarkTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListBenchmarkTopicsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListBenchmarkTopics", request, ApiListTopicsResponse)

  def list_kernel_topics(self, request: ApiListKernelTopicsRequest = None) -> ApiListTopicsResponse:
    r"""
    List discussion topics for a kernel.

    Args:
      request (ApiListKernelTopicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ApiListKernelTopicsRequest()

    return self._client.call("discussions.DiscussionApiService", "ListKernelTopics", request, ApiListTopicsResponse)
