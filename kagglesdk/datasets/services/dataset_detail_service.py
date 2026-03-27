from kagglesdk.datasets.types.dataset_basics_types import DatasetBasics
from kagglesdk.datasets.types.dataset_detail_service import ArchiveDatasetSuggestionBundleRequest, CreateDatasetSuggestionBundleRequest, CreateDatasetSuggestionBundleTopicRequest, CreateDatasetSuggestionBundleTopicResponse, DeleteDatasetSuggestionBundleRequest, GetDatasetAdminSettingsRequest, GetDatasetAdminSettingsResponse, GetDatasetBasicsRequest, GetDatasetFeedbacksRequest, GetDatasetFeedbacksResponse, GetDatasetImageInfoRequest, GetDatasetImageInfoResponse, GetDatasetSettingsRequest, GetDatasetSuggestionBundleRequest, GetDatasetUpvotesRequest, GetDatasetUpvotesResponse, GetDatasetUsabilityRatingRequest, GetDatasetUsabilityRatingResponse, GetDeletedDatasetInfoRequest, GetDeletedDatasetInfoResponse, GetDeletedDoiDatasetVersionInfoRequest, GetDeletedDoiDatasetVersionInfoResponse, ListDatasetSuggestionBundlesRequest, ListDatasetSuggestionBundlesResponse, ReviewDatasetSuggestionBundleRequest, SetDatasetSettingsRequest, UnarchiveDatasetSuggestionBundleRequest, UpdateDatasetFeedbacksRequest, UpdateDatasetImagesRequest, UpdateDatasetImagesResponse, UpdateDatasetSuggestionBundleRequest
from kagglesdk.datasets.types.dataset_types import DatasetSettings, DatasetSuggestionBundle
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DatasetDetailClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_dataset_basics(self, request: GetDatasetBasicsRequest = None) -> DatasetBasics:
    r"""
    Args:
      request (GetDatasetBasicsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetBasicsRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetBasics", request, DatasetBasics)

  def get_dataset_upvotes(self, request: GetDatasetUpvotesRequest = None) -> GetDatasetUpvotesResponse:
    r"""
    Args:
      request (GetDatasetUpvotesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetUpvotesRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetUpvotes", request, GetDatasetUpvotesResponse)

  def get_deleted_dataset_info(self, request: GetDeletedDatasetInfoRequest = None) -> GetDeletedDatasetInfoResponse:
    r"""
    The next three RPCs are legacy and could potentially be merged with
    GetDatasetBasics.
    TODO(http://b/274833571): Move toward a Dataset proto/handler with mask
    support, rather than these specific ones

    Args:
      request (GetDeletedDatasetInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDeletedDatasetInfoRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDeletedDatasetInfo", request, GetDeletedDatasetInfoResponse)

  def get_deleted_doi_dataset_version_info(self, request: GetDeletedDoiDatasetVersionInfoRequest = None) -> GetDeletedDoiDatasetVersionInfoResponse:
    r"""
    Args:
      request (GetDeletedDoiDatasetVersionInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDeletedDoiDatasetVersionInfoRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDeletedDoiDatasetVersionInfo", request, GetDeletedDoiDatasetVersionInfoResponse)

  def get_dataset_settings(self, request: GetDatasetSettingsRequest = None) -> DatasetSettings:
    r"""
    Args:
      request (GetDatasetSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetSettingsRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetSettings", request, DatasetSettings)

  def set_dataset_settings(self, request: SetDatasetSettingsRequest = None):
    r"""
    Args:
      request (SetDatasetSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetDatasetSettingsRequest()

    self._client.call("datasets.DatasetDetailService", "SetDatasetSettings", request, None)

  def get_dataset_usability_rating(self, request: GetDatasetUsabilityRatingRequest = None) -> GetDatasetUsabilityRatingResponse:
    r"""
    Args:
      request (GetDatasetUsabilityRatingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetUsabilityRatingRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetUsabilityRating", request, GetDatasetUsabilityRatingResponse)

  def get_dataset_image_info(self, request: GetDatasetImageInfoRequest = None) -> GetDatasetImageInfoResponse:
    r"""
    Args:
      request (GetDatasetImageInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetImageInfoRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetImageInfo", request, GetDatasetImageInfoResponse)

  def get_dataset_admin_settings(self, request: GetDatasetAdminSettingsRequest = None) -> GetDatasetAdminSettingsResponse:
    r"""
    Args:
      request (GetDatasetAdminSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetAdminSettingsRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetAdminSettings", request, GetDatasetAdminSettingsResponse)

  def update_dataset_images(self, request: UpdateDatasetImagesRequest = None) -> UpdateDatasetImagesResponse:
    r"""
    Args:
      request (UpdateDatasetImagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetImagesRequest()

    return self._client.call("datasets.DatasetDetailService", "UpdateDatasetImages", request, UpdateDatasetImagesResponse)

  def get_dataset_feedbacks(self, request: GetDatasetFeedbacksRequest = None) -> GetDatasetFeedbacksResponse:
    r"""
    Args:
      request (GetDatasetFeedbacksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetFeedbacksRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetFeedbacks", request, GetDatasetFeedbacksResponse)

  def update_dataset_feedbacks(self, request: UpdateDatasetFeedbacksRequest = None):
    r"""
    Args:
      request (UpdateDatasetFeedbacksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetFeedbacksRequest()

    self._client.call("datasets.DatasetDetailService", "UpdateDatasetFeedbacks", request, None)

  def create_dataset_suggestion_bundle(self, request: CreateDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (CreateDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "CreateDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def get_dataset_suggestion_bundle(self, request: GetDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (GetDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "GetDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def update_dataset_suggestion_bundle(self, request: UpdateDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (UpdateDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "UpdateDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def delete_dataset_suggestion_bundle(self, request: DeleteDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (DeleteDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "DeleteDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def list_dataset_suggestion_bundles(self, request: ListDatasetSuggestionBundlesRequest = None) -> ListDatasetSuggestionBundlesResponse:
    r"""
    Args:
      request (ListDatasetSuggestionBundlesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListDatasetSuggestionBundlesRequest()

    return self._client.call("datasets.DatasetDetailService", "ListDatasetSuggestionBundles", request, ListDatasetSuggestionBundlesResponse)

  def review_dataset_suggestion_bundle(self, request: ReviewDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (ReviewDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReviewDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "ReviewDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def create_dataset_suggestion_bundle_topic(self, request: CreateDatasetSuggestionBundleTopicRequest = None) -> CreateDatasetSuggestionBundleTopicResponse:
    r"""
    Args:
      request (CreateDatasetSuggestionBundleTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateDatasetSuggestionBundleTopicRequest()

    return self._client.call("datasets.DatasetDetailService", "CreateDatasetSuggestionBundleTopic", request, CreateDatasetSuggestionBundleTopicResponse)

  def archive_dataset_suggestion_bundle(self, request: ArchiveDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (ArchiveDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ArchiveDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "ArchiveDatasetSuggestionBundle", request, DatasetSuggestionBundle)

  def unarchive_dataset_suggestion_bundle(self, request: UnarchiveDatasetSuggestionBundleRequest = None) -> DatasetSuggestionBundle:
    r"""
    Args:
      request (UnarchiveDatasetSuggestionBundleRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnarchiveDatasetSuggestionBundleRequest()

    return self._client.call("datasets.DatasetDetailService", "UnarchiveDatasetSuggestionBundle", request, DatasetSuggestionBundle)
