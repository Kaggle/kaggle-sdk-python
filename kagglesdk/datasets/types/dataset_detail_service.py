from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.datasets.databundles.types.databundle_enums import ExtendedDataType, HarmonizedDataType
from kagglesdk.datasets.types.dataset_enums import ListDatasetSuggestionBundlesOrderBy, MetadataSuggestionType, SuggestionBundleState, UpdateFeedbackType
from kagglesdk.datasets.types.dataset_types import DatasetAdminSettingsInfo, DatasetFeedbackInfo, DatasetImageInfo, DatasetSettings, DatasetSuggestionBundle, DatasetUsabilityRating, ReviewDatasetSuggestionBundleApproval, ReviewDatasetSuggestionBundleApprovalWithChanges, ReviewDatasetSuggestionBundleRejection
from kagglesdk.discussions.types.discussions_service import CreateTopicRequest
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user import User
from typing import Optional, List

class ArchiveDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle_id (int)
      Id for the DatasetSuggestionBundle to archive.
  """

  def __init__(self):
    self._dataset_suggestion_bundle_id = 0
    self._freeze()

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Id for the DatasetSuggestionBundle to archive."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id


class CreateDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_version_id (int)
      Dataset version to create a suggestion bundle for.
    suggestion_requests (CreateDatasetSuggestionRequest)
      Unit-change suggestions that comprise the bundle. ex:
      'suggestion_requests': [
        {
          'type': 'METADATA_SUGGESTION_TYPE_FILE_DESCRIPTION',
          'firestorePath':'<databundleId>/versions/<databundleVersionId>/files/<fileName>',
          'description': 'This is my new description!',
        },
      ],
    summary (str)
      Summary describing the suggestion.
  """

  def __init__(self):
    self._dataset_version_id = 0
    self._suggestion_requests = []
    self._summary = ""
    self._freeze()

  @property
  def dataset_version_id(self) -> int:
    """Dataset version to create a suggestion bundle for."""
    return self._dataset_version_id

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id

  @property
  def summary(self) -> str:
    """Summary describing the suggestion."""
    return self._summary

  @summary.setter
  def summary(self, summary: str):
    if summary is None:
      del self.summary
      return
    if not isinstance(summary, str):
      raise TypeError('summary must be of type str')
    self._summary = summary

  @property
  def suggestion_requests(self) -> Optional[List[Optional['CreateDatasetSuggestionRequest']]]:
    r"""
    Unit-change suggestions that comprise the bundle. ex:
    'suggestion_requests': [
      {
        'type': 'METADATA_SUGGESTION_TYPE_FILE_DESCRIPTION',
        'firestorePath':'<databundleId>/versions/<databundleVersionId>/files/<fileName>',
        'description': 'This is my new description!',
      },
    ],
    """
    return self._suggestion_requests

  @suggestion_requests.setter
  def suggestion_requests(self, suggestion_requests: Optional[List[Optional['CreateDatasetSuggestionRequest']]]):
    if suggestion_requests is None:
      del self.suggestion_requests
      return
    if not isinstance(suggestion_requests, list):
      raise TypeError('suggestion_requests must be of type list')
    if not all([isinstance(t, CreateDatasetSuggestionRequest) for t in suggestion_requests]):
      raise TypeError('suggestion_requests must contain only items of type CreateDatasetSuggestionRequest')
    self._suggestion_requests = suggestion_requests


class CreateDatasetSuggestionBundleTopicRequest(KaggleObject):
  r"""
  Attributes:
    create_topic_request (CreateTopicRequest)
      The create topic request. Auth for this request will be handled by the
      handler's inner call to CreateTopic.
    dataset_suggestion_bundle_id (int)
      The id for the suggestion bundle that this topic is attached to.
    version (int)
      Version of the suggestion bundle on which a topic is being created.
  """

  def __init__(self):
    self._create_topic_request = None
    self._dataset_suggestion_bundle_id = 0
    self._version = 0
    self._freeze()

  @property
  def create_topic_request(self) -> Optional['CreateTopicRequest']:
    r"""
    The create topic request. Auth for this request will be handled by the
    handler's inner call to CreateTopic.
    """
    return self._create_topic_request

  @create_topic_request.setter
  def create_topic_request(self, create_topic_request: Optional['CreateTopicRequest']):
    if create_topic_request is None:
      del self.create_topic_request
      return
    if not isinstance(create_topic_request, CreateTopicRequest):
      raise TypeError('create_topic_request must be of type CreateTopicRequest')
    self._create_topic_request = create_topic_request

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """The id for the suggestion bundle that this topic is attached to."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id

  @property
  def version(self) -> int:
    """Version of the suggestion bundle on which a topic is being created."""
    return self._version

  @version.setter
  def version(self, version: int):
    if version is None:
      del self.version
      return
    if not isinstance(version, int):
      raise TypeError('version must be of type int')
    self._version = version


class CreateDatasetSuggestionBundleTopicResponse(KaggleObject):
  r"""
  Attributes:
    topic_id (int)
      The created topic ID.
  """

  def __init__(self):
    self._topic_id = 0
    self._freeze()

  @property
  def topic_id(self) -> int:
    """The created topic ID."""
    return self._topic_id

  @topic_id.setter
  def topic_id(self, topic_id: int):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id


class CreateDatasetSuggestionRequest(KaggleObject):
  r"""
  This is a subset of the fields in DatasetSuggestion that a user can provide
  when creating a suggestion bundle. All other fields (ex: state, id) are set
  automatically.

  Attributes:
    type (MetadataSuggestionType)
      Suggestion type, determines which 'data fields' are necessary. For example:
      a COLUMN_DESCRIPTION suggestion requires the FirestorePath and Description
      fields to be present. Checks in the handlers and CHECK constraints on the
      table ensure relevant fields are NON-NULL.
    firestore_path (str)
      Firestore path to the target file who's metadata this suggestion updates.
    description (str)
      Description suggestion, plexed for column and file descriptions.
    harmonized_type (HarmonizedDataType)
      Column HarmonizedDataType suggestion.
    extended_type (ExtendedDataType)
      Column ExtendedDataType suggestion.
  """

  def __init__(self):
    self._type = MetadataSuggestionType.METADATA_SUGGESTION_TYPE_UNSPECIFIED
    self._firestore_path = None
    self._description = None
    self._harmonized_type = None
    self._extended_type = None
    self._freeze()

  @property
  def type(self) -> 'MetadataSuggestionType':
    r"""
    Suggestion type, determines which 'data fields' are necessary. For example:
    a COLUMN_DESCRIPTION suggestion requires the FirestorePath and Description
    fields to be present. Checks in the handlers and CHECK constraints on the
    table ensure relevant fields are NON-NULL.
    """
    return self._type

  @type.setter
  def type(self, type: 'MetadataSuggestionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, MetadataSuggestionType):
      raise TypeError('type must be of type MetadataSuggestionType')
    self._type = type

  @property
  def firestore_path(self) -> str:
    """Firestore path to the target file who's metadata this suggestion updates."""
    return self._firestore_path or ""

  @firestore_path.setter
  def firestore_path(self, firestore_path: Optional[str]):
    if firestore_path is None:
      del self.firestore_path
      return
    if not isinstance(firestore_path, str):
      raise TypeError('firestore_path must be of type str')
    self._firestore_path = firestore_path

  @property
  def description(self) -> str:
    """Description suggestion, plexed for column and file descriptions."""
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def harmonized_type(self) -> 'HarmonizedDataType':
    """Column HarmonizedDataType suggestion."""
    return self._harmonized_type or HarmonizedDataType.STRING

  @harmonized_type.setter
  def harmonized_type(self, harmonized_type: Optional['HarmonizedDataType']):
    if harmonized_type is None:
      del self.harmonized_type
      return
    if not isinstance(harmonized_type, HarmonizedDataType):
      raise TypeError('harmonized_type must be of type HarmonizedDataType')
    self._harmonized_type = harmonized_type

  @property
  def extended_type(self) -> 'ExtendedDataType':
    """Column ExtendedDataType suggestion."""
    return self._extended_type or ExtendedDataType.EXTENDED_DATA_TYPE_UNSPECIFIED

  @extended_type.setter
  def extended_type(self, extended_type: Optional['ExtendedDataType']):
    if extended_type is None:
      del self.extended_type
      return
    if not isinstance(extended_type, ExtendedDataType):
      raise TypeError('extended_type must be of type ExtendedDataType')
    self._extended_type = extended_type


class DeleteDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle_id (int)
      Id for the DatasetSuggestionBundle.
  """

  def __init__(self):
    self._dataset_suggestion_bundle_id = 0
    self._freeze()

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Id for the DatasetSuggestionBundle."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id


class GetDatasetAdminSettingsRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
  """

  def __init__(self):
    self._dataset_id = 0
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id


class GetDatasetAdminSettingsResponse(KaggleObject):
  r"""
  Attributes:
    info (DatasetAdminSettingsInfo)
  """

  def __init__(self):
    self._info = None
    self._freeze()

  @property
  def info(self) -> Optional['DatasetAdminSettingsInfo']:
    return self._info

  @info.setter
  def info(self, info: Optional['DatasetAdminSettingsInfo']):
    if info is None:
      del self.info
      return
    if not isinstance(info, DatasetAdminSettingsInfo):
      raise TypeError('info must be of type DatasetAdminSettingsInfo')
    self._info = info


class GetDatasetBasicsRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    dataset_slug (str)
    hash_link (str)
    dataset_version_number (int)
      if not specified, current version is used
  """

  def __init__(self):
    self._owner_slug = None
    self._dataset_slug = None
    self._hash_link = None
    self._dataset_version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: Optional[str]):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def dataset_slug(self) -> str:
    return self._dataset_slug or ""

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: Optional[str]):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link

  @property
  def dataset_version_number(self) -> int:
    """if not specified, current version is used"""
    return self._dataset_version_number or 0

  @dataset_version_number.setter
  def dataset_version_number(self, dataset_version_number: Optional[int]):
    if dataset_version_number is None:
      del self.dataset_version_number
      return
    if not isinstance(dataset_version_number, int):
      raise TypeError('dataset_version_number must be of type int')
    self._dataset_version_number = dataset_version_number


class GetDatasetFeedbacksRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    hash_link (str)
  """

  def __init__(self):
    self._dataset_id = 0
    self._hash_link = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


class GetDatasetFeedbacksResponse(KaggleObject):
  r"""
  Attributes:
    feedbacks (DatasetFeedbackInfo)
  """

  def __init__(self):
    self._feedbacks = []
    self._freeze()

  @property
  def feedbacks(self) -> Optional[List[Optional['DatasetFeedbackInfo']]]:
    return self._feedbacks

  @feedbacks.setter
  def feedbacks(self, feedbacks: Optional[List[Optional['DatasetFeedbackInfo']]]):
    if feedbacks is None:
      del self.feedbacks
      return
    if not isinstance(feedbacks, list):
      raise TypeError('feedbacks must be of type list')
    if not all([isinstance(t, DatasetFeedbackInfo) for t in feedbacks]):
      raise TypeError('feedbacks must contain only items of type DatasetFeedbackInfo')
    self._feedbacks = feedbacks


class GetDatasetImageInfoRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    dataset_version_id (int)
  """

  def __init__(self):
    self._dataset_id = 0
    self._dataset_version_id = 0
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def dataset_version_id(self) -> int:
    return self._dataset_version_id

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id


class GetDatasetImageInfoResponse(KaggleObject):
  r"""
  Attributes:
    info (DatasetImageInfo)
  """

  def __init__(self):
    self._info = None
    self._freeze()

  @property
  def info(self) -> Optional['DatasetImageInfo']:
    return self._info

  @info.setter
  def info(self, info: Optional['DatasetImageInfo']):
    if info is None:
      del self.info
      return
    if not isinstance(info, DatasetImageInfo):
      raise TypeError('info must be of type DatasetImageInfo')
    self._info = info


class GetDatasetSettingsRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
  """

  def __init__(self):
    self._dataset_id = 0
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id


class GetDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle_id (int)
      Id for the DatasetSuggestionBundle.
  """

  def __init__(self):
    self._dataset_suggestion_bundle_id = 0
    self._freeze()

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Id for the DatasetSuggestionBundle."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id


class GetDatasetUpvotesRequest(KaggleObject):
  r"""
  API to support async loading of upvoters on a dataset
  Migrating away from fetching all of this data on page load in pre-KM view

  Attributes:
    dataset_id (int)
    hash_link (str)
  """

  def __init__(self):
    self._dataset_id = 0
    self._hash_link = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


class GetDatasetUpvotesResponse(KaggleObject):
  r"""
  This message is extremely similar to UpvoteSuggestionDto, though no longer a
  DTO

  Attributes:
    vote_count (int)
    medal_vote_count (int)
    up_voters (User)
  """

  def __init__(self):
    self._vote_count = 0
    self._medal_vote_count = 0
    self._up_voters = []
    self._freeze()

  @property
  def vote_count(self) -> int:
    return self._vote_count

  @vote_count.setter
  def vote_count(self, vote_count: int):
    if vote_count is None:
      del self.vote_count
      return
    if not isinstance(vote_count, int):
      raise TypeError('vote_count must be of type int')
    self._vote_count = vote_count

  @property
  def medal_vote_count(self) -> int:
    return self._medal_vote_count

  @medal_vote_count.setter
  def medal_vote_count(self, medal_vote_count: int):
    if medal_vote_count is None:
      del self.medal_vote_count
      return
    if not isinstance(medal_vote_count, int):
      raise TypeError('medal_vote_count must be of type int')
    self._medal_vote_count = medal_vote_count

  @property
  def up_voters(self) -> Optional[List[Optional['User']]]:
    return self._up_voters

  @up_voters.setter
  def up_voters(self, up_voters: Optional[List[Optional['User']]]):
    if up_voters is None:
      del self.up_voters
      return
    if not isinstance(up_voters, list):
      raise TypeError('up_voters must be of type list')
    if not all([isinstance(t, User) for t in up_voters]):
      raise TypeError('up_voters must contain only items of type User')
    self._up_voters = up_voters


class GetDatasetUsabilityRatingRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    hash_link (str)
  """

  def __init__(self):
    self._dataset_id = 0
    self._hash_link = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def hash_link(self) -> str:
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


class GetDatasetUsabilityRatingResponse(KaggleObject):
  r"""
  Attributes:
    rating (DatasetUsabilityRating)
  """

  def __init__(self):
    self._rating = None
    self._freeze()

  @property
  def rating(self) -> Optional['DatasetUsabilityRating']:
    return self._rating or None

  @rating.setter
  def rating(self, rating: Optional[Optional['DatasetUsabilityRating']]):
    if rating is None:
      del self.rating
      return
    if not isinstance(rating, DatasetUsabilityRating):
      raise TypeError('rating must be of type DatasetUsabilityRating')
    self._rating = rating


class GetDeletedDatasetInfoRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
  """

  def __init__(self):
    self._dataset_id = 0
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id


class GetDeletedDatasetInfoResponse(KaggleObject):
  r"""
  Attributes:
    current_dataset_version_id (int)
    doi (str)
    creation_exception (str)
  """

  def __init__(self):
    self._current_dataset_version_id = 0
    self._doi = None
    self._creation_exception = None
    self._freeze()

  @property
  def current_dataset_version_id(self) -> int:
    return self._current_dataset_version_id

  @current_dataset_version_id.setter
  def current_dataset_version_id(self, current_dataset_version_id: int):
    if current_dataset_version_id is None:
      del self.current_dataset_version_id
      return
    if not isinstance(current_dataset_version_id, int):
      raise TypeError('current_dataset_version_id must be of type int')
    self._current_dataset_version_id = current_dataset_version_id

  @property
  def doi(self) -> str:
    return self._doi or ""

  @doi.setter
  def doi(self, doi: Optional[str]):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi

  @property
  def creation_exception(self) -> str:
    return self._creation_exception or ""

  @creation_exception.setter
  def creation_exception(self, creation_exception: Optional[str]):
    if creation_exception is None:
      del self.creation_exception
      return
    if not isinstance(creation_exception, str):
      raise TypeError('creation_exception must be of type str')
    self._creation_exception = creation_exception


class GetDeletedDoiDatasetVersionInfoRequest(KaggleObject):
  r"""
  Attributes:
    dataset_version_id (int)
  """

  def __init__(self):
    self._dataset_version_id = 0
    self._freeze()

  @property
  def dataset_version_id(self) -> int:
    return self._dataset_version_id

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id


class GetDeletedDoiDatasetVersionInfoResponse(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    doi (str)
    new_version_doi (str)
  """

  def __init__(self):
    self._dataset_id = 0
    self._doi = None
    self._new_version_doi = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def doi(self) -> str:
    return self._doi or ""

  @doi.setter
  def doi(self, doi: Optional[str]):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi

  @property
  def new_version_doi(self) -> str:
    return self._new_version_doi or ""

  @new_version_doi.setter
  def new_version_doi(self, new_version_doi: Optional[str]):
    if new_version_doi is None:
      del self.new_version_doi
      return
    if not isinstance(new_version_doi, str):
      raise TypeError('new_version_doi must be of type str')
    self._new_version_doi = new_version_doi


class ListDatasetSuggestionBundlesFilter(KaggleObject):
  r"""
  Filter options for the ListDatasetSuggestionBundle RPC.
  We'll use this instead of a proper query string as outlined in
  https://google.aip.dev/160 for the sake of brevity. Each present field
  will be logically joined via AND.

  Attributes:
    suggester_user_id (int)
      Match for bundles suggested by this user. This option is only allowed
      for self-queries, i.e. the user is listing their own suggestions.
    bundle_states (SuggestionBundleState)
      Match for bundles in any of the given states.
    suggestion_types (MetadataSuggestionType)
      Match for bundles with a suggestion with the following type(s).
    summary (str)
      Match for substring occurrences in the bundle summary.
    include_ids (int)
      Match for suggestion bundles with the given ids.
  """

  def __init__(self):
    self._suggester_user_id = None
    self._bundle_states = []
    self._suggestion_types = []
    self._summary = None
    self._include_ids = []
    self._freeze()

  @property
  def suggester_user_id(self) -> int:
    r"""
    Match for bundles suggested by this user. This option is only allowed
    for self-queries, i.e. the user is listing their own suggestions.
    """
    return self._suggester_user_id or 0

  @suggester_user_id.setter
  def suggester_user_id(self, suggester_user_id: Optional[int]):
    if suggester_user_id is None:
      del self.suggester_user_id
      return
    if not isinstance(suggester_user_id, int):
      raise TypeError('suggester_user_id must be of type int')
    self._suggester_user_id = suggester_user_id

  @property
  def bundle_states(self) -> Optional[List['SuggestionBundleState']]:
    """Match for bundles in any of the given states."""
    return self._bundle_states

  @bundle_states.setter
  def bundle_states(self, bundle_states: Optional[List['SuggestionBundleState']]):
    if bundle_states is None:
      del self.bundle_states
      return
    if not isinstance(bundle_states, list):
      raise TypeError('bundle_states must be of type list')
    if not all([isinstance(t, SuggestionBundleState) for t in bundle_states]):
      raise TypeError('bundle_states must contain only items of type SuggestionBundleState')
    self._bundle_states = bundle_states

  @property
  def suggestion_types(self) -> Optional[List['MetadataSuggestionType']]:
    """Match for bundles with a suggestion with the following type(s)."""
    return self._suggestion_types

  @suggestion_types.setter
  def suggestion_types(self, suggestion_types: Optional[List['MetadataSuggestionType']]):
    if suggestion_types is None:
      del self.suggestion_types
      return
    if not isinstance(suggestion_types, list):
      raise TypeError('suggestion_types must be of type list')
    if not all([isinstance(t, MetadataSuggestionType) for t in suggestion_types]):
      raise TypeError('suggestion_types must contain only items of type MetadataSuggestionType')
    self._suggestion_types = suggestion_types

  @property
  def summary(self) -> str:
    """Match for substring occurrences in the bundle summary."""
    return self._summary or ""

  @summary.setter
  def summary(self, summary: Optional[str]):
    if summary is None:
      del self.summary
      return
    if not isinstance(summary, str):
      raise TypeError('summary must be of type str')
    self._summary = summary

  @property
  def include_ids(self) -> Optional[List[int]]:
    """Match for suggestion bundles with the given ids."""
    return self._include_ids

  @include_ids.setter
  def include_ids(self, include_ids: Optional[List[int]]):
    if include_ids is None:
      del self.include_ids
      return
    if not isinstance(include_ids, list):
      raise TypeError('include_ids must be of type list')
    if not all([isinstance(t, int) for t in include_ids]):
      raise TypeError('include_ids must contain only items of type int')
    self._include_ids = include_ids


class ListDatasetSuggestionBundlesRequest(KaggleObject):
  r"""
  Attributes:
    dataset_version_id (int)
      Parent dataset version to list suggestions for. If this field is missing,
      we consider all suggestion bundles (this is analogous to the '-' wildcard
      in https://google.aip.dev/159). We also require that the
      'suggester_user_id' filter option is set.
    filter (ListDatasetSuggestionBundlesFilter)
      Filter for bundles under the specified parent dataset version. If no
      dataset version is specified these filters are applied across all
      suggestion bundles.
    page_size (int)
      Maximum number of bundles to return in this request.
    page_token (str)
      Page token received from a previous call. Given all other parameters are
      the same, this token retrieves the subsequent page of results.
    order_by (ListDatasetSuggestionBundlesOrderBy)
      Ordering for returned bundles.
    skip (int)
      Number of bundles to skip (relative to the given page_token).
  """

  def __init__(self):
    self._dataset_version_id = None
    self._filter = None
    self._page_size = 0
    self._page_token = None
    self._order_by = None
    self._skip = None
    self._freeze()

  @property
  def dataset_version_id(self) -> int:
    r"""
    Parent dataset version to list suggestions for. If this field is missing,
    we consider all suggestion bundles (this is analogous to the '-' wildcard
    in https://google.aip.dev/159). We also require that the
    'suggester_user_id' filter option is set.
    """
    return self._dataset_version_id or 0

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: Optional[int]):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id

  @property
  def filter(self) -> Optional['ListDatasetSuggestionBundlesFilter']:
    r"""
    Filter for bundles under the specified parent dataset version. If no
    dataset version is specified these filters are applied across all
    suggestion bundles.
    """
    return self._filter or None

  @filter.setter
  def filter(self, filter: Optional[Optional['ListDatasetSuggestionBundlesFilter']]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListDatasetSuggestionBundlesFilter):
      raise TypeError('filter must be of type ListDatasetSuggestionBundlesFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListDatasetSuggestionBundlesOrderBy':
    """Ordering for returned bundles."""
    return self._order_by or ListDatasetSuggestionBundlesOrderBy.LIST_DATASET_SUGGESTION_BUNDLES_ORDER_BY_UNSPECIFIED

  @order_by.setter
  def order_by(self, order_by: Optional['ListDatasetSuggestionBundlesOrderBy']):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListDatasetSuggestionBundlesOrderBy):
      raise TypeError('order_by must be of type ListDatasetSuggestionBundlesOrderBy')
    self._order_by = order_by

  @property
  def page_size(self) -> int:
    """Maximum number of bundles to return in this request."""
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    r"""
    Page token received from a previous call. Given all other parameters are
    the same, this token retrieves the subsequent page of results.
    """
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    """Number of bundles to skip (relative to the given page_token)."""
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip


class ListDatasetSuggestionBundlesResponse(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundles (DatasetSuggestionBundle)
      Relevant suggestion bundles.
    next_page_token (str)
      Page token for the next page of results.
    total_bundles (int)
      Total number of bundles relative to the filter query (ignoring pagination).
  """

  def __init__(self):
    self._dataset_suggestion_bundles = []
    self._next_page_token = None
    self._total_bundles = 0
    self._freeze()

  @property
  def dataset_suggestion_bundles(self) -> Optional[List[Optional['DatasetSuggestionBundle']]]:
    """Relevant suggestion bundles."""
    return self._dataset_suggestion_bundles

  @dataset_suggestion_bundles.setter
  def dataset_suggestion_bundles(self, dataset_suggestion_bundles: Optional[List[Optional['DatasetSuggestionBundle']]]):
    if dataset_suggestion_bundles is None:
      del self.dataset_suggestion_bundles
      return
    if not isinstance(dataset_suggestion_bundles, list):
      raise TypeError('dataset_suggestion_bundles must be of type list')
    if not all([isinstance(t, DatasetSuggestionBundle) for t in dataset_suggestion_bundles]):
      raise TypeError('dataset_suggestion_bundles must contain only items of type DatasetSuggestionBundle')
    self._dataset_suggestion_bundles = dataset_suggestion_bundles

  @property
  def next_page_token(self) -> str:
    """Page token for the next page of results."""
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def total_bundles(self) -> int:
    """Total number of bundles relative to the filter query (ignoring pagination)."""
    return self._total_bundles

  @total_bundles.setter
  def total_bundles(self, total_bundles: int):
    if total_bundles is None:
      del self.total_bundles
      return
    if not isinstance(total_bundles, int):
      raise TypeError('total_bundles must be of type int')
    self._total_bundles = total_bundles


class ReviewDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle_id (int)
      Id of the suggestion bundle that is being reviewed.
    version (int)
      Version of the suggestion bundle that is being reviewed.
    approval (ReviewDatasetSuggestionBundleApproval)
    approval_with_changes (ReviewDatasetSuggestionBundleApprovalWithChanges)
    rejection (ReviewDatasetSuggestionBundleRejection)
  """

  def __init__(self):
    self._dataset_suggestion_bundle_id = 0
    self._version = 0
    self._approval = None
    self._approval_with_changes = None
    self._rejection = None
    self._freeze()

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Id of the suggestion bundle that is being reviewed."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id

  @property
  def version(self) -> int:
    """Version of the suggestion bundle that is being reviewed."""
    return self._version

  @version.setter
  def version(self, version: int):
    if version is None:
      del self.version
      return
    if not isinstance(version, int):
      raise TypeError('version must be of type int')
    self._version = version

  @property
  def approval(self) -> Optional['ReviewDatasetSuggestionBundleApproval']:
    return self._approval or None

  @approval.setter
  def approval(self, approval: Optional['ReviewDatasetSuggestionBundleApproval']):
    if approval is None:
      del self.approval
      return
    if not isinstance(approval, ReviewDatasetSuggestionBundleApproval):
      raise TypeError('approval must be of type ReviewDatasetSuggestionBundleApproval')
    del self.approval_with_changes
    del self.rejection
    self._approval = approval

  @property
  def approval_with_changes(self) -> Optional['ReviewDatasetSuggestionBundleApprovalWithChanges']:
    return self._approval_with_changes or None

  @approval_with_changes.setter
  def approval_with_changes(self, approval_with_changes: Optional['ReviewDatasetSuggestionBundleApprovalWithChanges']):
    if approval_with_changes is None:
      del self.approval_with_changes
      return
    if not isinstance(approval_with_changes, ReviewDatasetSuggestionBundleApprovalWithChanges):
      raise TypeError('approval_with_changes must be of type ReviewDatasetSuggestionBundleApprovalWithChanges')
    del self.approval
    del self.rejection
    self._approval_with_changes = approval_with_changes

  @property
  def rejection(self) -> Optional['ReviewDatasetSuggestionBundleRejection']:
    return self._rejection or None

  @rejection.setter
  def rejection(self, rejection: Optional['ReviewDatasetSuggestionBundleRejection']):
    if rejection is None:
      del self.rejection
      return
    if not isinstance(rejection, ReviewDatasetSuggestionBundleRejection):
      raise TypeError('rejection must be of type ReviewDatasetSuggestionBundleRejection')
    del self.approval
    del self.approval_with_changes
    self._rejection = rejection


class SetDatasetSettingsRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    settings (DatasetSettings)
  """

  def __init__(self):
    self._dataset_id = 0
    self._settings = None
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def settings(self) -> Optional['DatasetSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['DatasetSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, DatasetSettings):
      raise TypeError('settings must be of type DatasetSettings')
    self._settings = settings


class UnarchiveDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle_id (int)
      Id for the DatasetSuggestionBundle to unarchive.
  """

  def __init__(self):
    self._dataset_suggestion_bundle_id = 0
    self._freeze()

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Id for the DatasetSuggestionBundle to unarchive."""
    return self._dataset_suggestion_bundle_id

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: int):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id


class UpdateDatasetFeedbacksRequest(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    feedback_id (int)
    update_type (UpdateFeedbackType)
  """

  def __init__(self):
    self._dataset_id = 0
    self._feedback_id = 0
    self._update_type = UpdateFeedbackType.UPDATE_FEEDBACK_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def feedback_id(self) -> int:
    return self._feedback_id

  @feedback_id.setter
  def feedback_id(self, feedback_id: int):
    if feedback_id is None:
      del self.feedback_id
      return
    if not isinstance(feedback_id, int):
      raise TypeError('feedback_id must be of type int')
    self._feedback_id = feedback_id

  @property
  def update_type(self) -> 'UpdateFeedbackType':
    return self._update_type

  @update_type.setter
  def update_type(self, update_type: 'UpdateFeedbackType'):
    if update_type is None:
      del self.update_type
      return
    if not isinstance(update_type, UpdateFeedbackType):
      raise TypeError('update_type must be of type UpdateFeedbackType')
    self._update_type = update_type


class UpdateDatasetImagesRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Currently requiring slugs and id for historical reasons (and to do authz
      check). Can be refactored later to just use the id.
    dataset_slug (str)
    dataset_id (int)
    image (CroppedImageUpload)
    original_image_url (str)
    card_image_url (str)
    cover_image_url (str)
    thumbnail_image_url (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._dataset_slug = ""
    self._dataset_id = 0
    self._image = None
    self._original_image_url = ""
    self._card_image_url = ""
    self._cover_image_url = ""
    self._thumbnail_image_url = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    r"""
    Currently requiring slugs and id for historical reasons (and to do authz
    check). Can be refactored later to just use the id.
    """
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def dataset_slug(self) -> str:
    return self._dataset_slug

  @dataset_slug.setter
  def dataset_slug(self, dataset_slug: str):
    if dataset_slug is None:
      del self.dataset_slug
      return
    if not isinstance(dataset_slug, str):
      raise TypeError('dataset_slug must be of type str')
    self._dataset_slug = dataset_slug

  @property
  def dataset_id(self) -> int:
    return self._dataset_id

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def image(self) -> Optional['CroppedImageUpload']:
    return self._image

  @image.setter
  def image(self, image: Optional['CroppedImageUpload']):
    if image is None:
      del self.image
      return
    if not isinstance(image, CroppedImageUpload):
      raise TypeError('image must be of type CroppedImageUpload')
    self._image = image

  @property
  def original_image_url(self) -> str:
    return self._original_image_url

  @original_image_url.setter
  def original_image_url(self, original_image_url: str):
    if original_image_url is None:
      del self.original_image_url
      return
    if not isinstance(original_image_url, str):
      raise TypeError('original_image_url must be of type str')
    self._original_image_url = original_image_url

  @property
  def card_image_url(self) -> str:
    return self._card_image_url

  @card_image_url.setter
  def card_image_url(self, card_image_url: str):
    if card_image_url is None:
      del self.card_image_url
      return
    if not isinstance(card_image_url, str):
      raise TypeError('card_image_url must be of type str')
    self._card_image_url = card_image_url

  @property
  def cover_image_url(self) -> str:
    return self._cover_image_url

  @cover_image_url.setter
  def cover_image_url(self, cover_image_url: str):
    if cover_image_url is None:
      del self.cover_image_url
      return
    if not isinstance(cover_image_url, str):
      raise TypeError('cover_image_url must be of type str')
    self._cover_image_url = cover_image_url

  @property
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: str):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url


class UpdateDatasetImagesResponse(KaggleObject):
  r"""
  Attributes:
    card_image_url (str)
    cover_image_url (str)
    thumbnail_image_url (str)
    original_image_url (str)
    usability_rating (DatasetUsabilityRating)
  """

  def __init__(self):
    self._card_image_url = ""
    self._cover_image_url = ""
    self._thumbnail_image_url = ""
    self._original_image_url = ""
    self._usability_rating = None
    self._freeze()

  @property
  def card_image_url(self) -> str:
    return self._card_image_url

  @card_image_url.setter
  def card_image_url(self, card_image_url: str):
    if card_image_url is None:
      del self.card_image_url
      return
    if not isinstance(card_image_url, str):
      raise TypeError('card_image_url must be of type str')
    self._card_image_url = card_image_url

  @property
  def cover_image_url(self) -> str:
    return self._cover_image_url

  @cover_image_url.setter
  def cover_image_url(self, cover_image_url: str):
    if cover_image_url is None:
      del self.cover_image_url
      return
    if not isinstance(cover_image_url, str):
      raise TypeError('cover_image_url must be of type str')
    self._cover_image_url = cover_image_url

  @property
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: str):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

  @property
  def original_image_url(self) -> str:
    return self._original_image_url

  @original_image_url.setter
  def original_image_url(self, original_image_url: str):
    if original_image_url is None:
      del self.original_image_url
      return
    if not isinstance(original_image_url, str):
      raise TypeError('original_image_url must be of type str')
    self._original_image_url = original_image_url

  @property
  def usability_rating(self) -> Optional['DatasetUsabilityRating']:
    return self._usability_rating

  @usability_rating.setter
  def usability_rating(self, usability_rating: Optional['DatasetUsabilityRating']):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, DatasetUsabilityRating):
      raise TypeError('usability_rating must be of type DatasetUsabilityRating')
    self._usability_rating = usability_rating


class UpdateDatasetSuggestionBundleRequest(KaggleObject):
  r"""
  Attributes:
    dataset_suggestion_bundle (DatasetSuggestionBundle)
      The updated DatasetSuggestionBundle.
    update_mask (FieldMask)
      List of fields to update.
  """

  def __init__(self):
    self._dataset_suggestion_bundle = None
    self._update_mask = None
    self._freeze()

  @property
  def dataset_suggestion_bundle(self) -> Optional['DatasetSuggestionBundle']:
    """The updated DatasetSuggestionBundle."""
    return self._dataset_suggestion_bundle

  @dataset_suggestion_bundle.setter
  def dataset_suggestion_bundle(self, dataset_suggestion_bundle: Optional['DatasetSuggestionBundle']):
    if dataset_suggestion_bundle is None:
      del self.dataset_suggestion_bundle
      return
    if not isinstance(dataset_suggestion_bundle, DatasetSuggestionBundle):
      raise TypeError('dataset_suggestion_bundle must be of type DatasetSuggestionBundle')
    self._dataset_suggestion_bundle = dataset_suggestion_bundle

  @property
  def update_mask(self) -> FieldMask:
    """List of fields to update."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


ArchiveDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
]

CreateDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("suggestionRequests", "suggestion_requests", "_suggestion_requests", CreateDatasetSuggestionRequest, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("summary", "summary", "_summary", str, "", PredefinedSerializer()),
]

CreateDatasetSuggestionBundleTopicRequest._fields = [
  FieldMetadata("createTopicRequest", "create_topic_request", "_create_topic_request", CreateTopicRequest, None, KaggleObjectSerializer()),
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", int, 0, PredefinedSerializer()),
]

CreateDatasetSuggestionBundleTopicResponse._fields = [
  FieldMetadata("topicId", "topic_id", "_topic_id", int, 0, PredefinedSerializer()),
]

CreateDatasetSuggestionRequest._fields = [
  FieldMetadata("type", "type", "_type", MetadataSuggestionType, MetadataSuggestionType.METADATA_SUGGESTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("harmonizedType", "harmonized_type", "_harmonized_type", HarmonizedDataType, None, EnumSerializer(), optional=True),
  FieldMetadata("extendedType", "extended_type", "_extended_type", ExtendedDataType, None, EnumSerializer(), optional=True),
]

DeleteDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
]

GetDatasetAdminSettingsRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
]

GetDatasetAdminSettingsResponse._fields = [
  FieldMetadata("info", "info", "_info", DatasetAdminSettingsInfo, None, KaggleObjectSerializer()),
]

GetDatasetBasicsRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionNumber", "dataset_version_number", "_dataset_version_number", int, None, PredefinedSerializer(), optional=True),
]

GetDatasetFeedbacksRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

GetDatasetFeedbacksResponse._fields = [
  FieldMetadata("feedbacks", "feedbacks", "_feedbacks", DatasetFeedbackInfo, [], ListSerializer(KaggleObjectSerializer())),
]

GetDatasetImageInfoRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
]

GetDatasetImageInfoResponse._fields = [
  FieldMetadata("info", "info", "_info", DatasetImageInfo, None, KaggleObjectSerializer()),
]

GetDatasetSettingsRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
]

GetDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
]

GetDatasetUpvotesRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

GetDatasetUpvotesResponse._fields = [
  FieldMetadata("voteCount", "vote_count", "_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("medalVoteCount", "medal_vote_count", "_medal_vote_count", int, 0, PredefinedSerializer()),
  FieldMetadata("upVoters", "up_voters", "_up_voters", User, [], ListSerializer(KaggleObjectSerializer())),
]

GetDatasetUsabilityRatingRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
]

GetDatasetUsabilityRatingResponse._fields = [
  FieldMetadata("rating", "rating", "_rating", DatasetUsabilityRating, None, KaggleObjectSerializer(), optional=True),
]

GetDeletedDatasetInfoRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
]

GetDeletedDatasetInfoResponse._fields = [
  FieldMetadata("currentDatasetVersionId", "current_dataset_version_id", "_current_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationException", "creation_exception", "_creation_exception", str, None, PredefinedSerializer(), optional=True),
]

GetDeletedDoiDatasetVersionInfoRequest._fields = [
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
]

GetDeletedDoiDatasetVersionInfoResponse._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("newVersionDoi", "new_version_doi", "_new_version_doi", str, None, PredefinedSerializer(), optional=True),
]

ListDatasetSuggestionBundlesFilter._fields = [
  FieldMetadata("suggesterUserId", "suggester_user_id", "_suggester_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bundleStates", "bundle_states", "_bundle_states", SuggestionBundleState, [], ListSerializer(EnumSerializer())),
  FieldMetadata("suggestionTypes", "suggestion_types", "_suggestion_types", MetadataSuggestionType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("summary", "summary", "_summary", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includeIds", "include_ids", "_include_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListDatasetSuggestionBundlesRequest._fields = [
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListDatasetSuggestionBundlesFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("orderBy", "order_by", "_order_by", ListDatasetSuggestionBundlesOrderBy, None, EnumSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
]

ListDatasetSuggestionBundlesResponse._fields = [
  FieldMetadata("datasetSuggestionBundles", "dataset_suggestion_bundles", "_dataset_suggestion_bundles", DatasetSuggestionBundle, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBundles", "total_bundles", "_total_bundles", int, 0, PredefinedSerializer()),
]

ReviewDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", int, 0, PredefinedSerializer()),
  FieldMetadata("approval", "approval", "_approval", ReviewDatasetSuggestionBundleApproval, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("approvalWithChanges", "approval_with_changes", "_approval_with_changes", ReviewDatasetSuggestionBundleApprovalWithChanges, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("rejection", "rejection", "_rejection", ReviewDatasetSuggestionBundleRejection, None, KaggleObjectSerializer(), optional=True),
]

SetDatasetSettingsRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", DatasetSettings, None, KaggleObjectSerializer()),
]

UnarchiveDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, 0, PredefinedSerializer()),
]

UpdateDatasetFeedbacksRequest._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("feedbackId", "feedback_id", "_feedback_id", int, 0, PredefinedSerializer()),
  FieldMetadata("updateType", "update_type", "_update_type", UpdateFeedbackType, UpdateFeedbackType.UPDATE_FEEDBACK_TYPE_UNSPECIFIED, EnumSerializer()),
]

UpdateDatasetImagesRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, "", PredefinedSerializer()),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("image", "image", "_image", CroppedImageUpload, None, KaggleObjectSerializer()),
  FieldMetadata("originalImageUrl", "original_image_url", "_original_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("cardImageUrl", "card_image_url", "_card_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
]

UpdateDatasetImagesResponse._fields = [
  FieldMetadata("cardImageUrl", "card_image_url", "_card_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("originalImageUrl", "original_image_url", "_original_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", DatasetUsabilityRating, None, KaggleObjectSerializer()),
]

UpdateDatasetSuggestionBundleRequest._fields = [
  FieldMetadata("datasetSuggestionBundle", "dataset_suggestion_bundle", "_dataset_suggestion_bundle", DatasetSuggestionBundle, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

