from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.common_types import Category
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.datasets.types.dataset_types import KernelTaskSubmissionInfo
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import CreationSourceType, DataSourceType, KernelsListSortType, KernelsListViewType, ListResourceReferencesOrderBy, ResourceReferenceType
from kagglesdk.users.types.progression_service import Medal
from kagglesdk.users.types.user import User
from typing import Optional, List

class AccessBehavior(enum.Enum):
  RETURN_SHELL_ENTRY = 0
  RETURN_NOTHING = 1

class CreateKernelPinRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    competition_id (int)
      TODO(b/244443172): add user_id here
    dataset_id (int)
    model_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._competition_id = None
    self._dataset_id = None
    self._model_id = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def competition_id(self) -> int:
    """TODO(b/244443172): add user_id here"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.model_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    self._model_id = model_id


class CreateKernelPinResponse(KaggleObject):
  r"""
  Attributes:
    kernel_pinned (bool)
  """

  def __init__(self):
    self._kernel_pinned = False
    self._freeze()

  @property
  def kernel_pinned(self) -> bool:
    return self._kernel_pinned

  @kernel_pinned.setter
  def kernel_pinned(self, kernel_pinned: bool):
    if kernel_pinned is None:
      del self.kernel_pinned
      return
    if not isinstance(kernel_pinned, bool):
      raise TypeError('kernel_pinned must be of type bool')
    self._kernel_pinned = kernel_pinned


class CreationSource(KaggleObject):
  r"""
  Attributes:
    type (CreationSourceType)
    id (int)
  """

  def __init__(self):
    self._type = CreationSourceType.CREATION_SOURCE_TYPE_UNSPECIFIED
    self._id = 0
    self._freeze()

  @property
  def type(self) -> 'CreationSourceType':
    return self._type

  @type.setter
  def type(self, type: 'CreationSourceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, CreationSourceType):
      raise TypeError('type must be of type CreationSourceType')
    self._type = type

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class DataSource(KaggleObject):
  r"""
  Attributes:
    reference (DataSourceReference)
    name (str)
    data_source_url (str)
    thumbnail_url (str)
    is_private (bool)
    variation_slug (str)
  """

  def __init__(self):
    self._reference = None
    self._name = None
    self._data_source_url = None
    self._thumbnail_url = None
    self._is_private = False
    self._variation_slug = None
    self._freeze()

  @property
  def reference(self) -> Optional['DataSourceReference']:
    return self._reference

  @reference.setter
  def reference(self, reference: Optional['DataSourceReference']):
    if reference is None:
      del self.reference
      return
    if not isinstance(reference, DataSourceReference):
      raise TypeError('reference must be of type DataSourceReference')
    self._reference = reference

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def data_source_url(self) -> str:
    return self._data_source_url or ""

  @data_source_url.setter
  def data_source_url(self, data_source_url: Optional[str]):
    if data_source_url is None:
      del self.data_source_url
      return
    if not isinstance(data_source_url, str):
      raise TypeError('data_source_url must be of type str')
    self._data_source_url = data_source_url

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url or ""

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: Optional[str]):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def variation_slug(self) -> str:
    return self._variation_slug or ""

  @variation_slug.setter
  def variation_slug(self, variation_slug: Optional[str]):
    if variation_slug is None:
      del self.variation_slug
      return
    if not isinstance(variation_slug, str):
      raise TypeError('variation_slug must be of type str')
    self._variation_slug = variation_slug


class DataSourceReference(KaggleObject):
  r"""
  Attributes:
    source_type (DataSourceType)
      Supports Competition, CompetitionEvaluation, DatasetVersion, KernelVersion,
      and ModelInstanceVersion
    source_id (int)
      CompetitionId for Competition and CompetitionEvaluation
      DatasetVersionId for DatasetVersions
      KernelSessionId for KernelVersions
      ModelInstanceVersionId for ModelInstanceVersions
    dataset_id (int)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
      Used for denormalizing KernelDatasetDataSources to improve performance
      This value needs to be set for DataSourceType.DatasetVersion
    databundle_version_id (int)
      Represents the low-level DatabundleVersion to use for this datasource.
      Currently only used for Competition datasources, since a Competition's
      databundle can be updated over time, or reruns may use a different
      databundle altogether. This field does not need to be set, it will be
      auto-populated with the Competition's current DBVID if not. DatasetVersion
      implies DatabundleVersion (and it cannot change) so Dataset datasources
      don't need this.
    mount_slug (str)
      The sub-directory used for mounting in a kernel's input directory or empty
      if data source should be mounted directly in the input path (legacy,
      single-source session).
    is_source_id_pinned (bool)
      Whether the source_id should be pinned or if it should always use the
      latest version of the source. Not applicable for Competitions.
    submission_id (int)
      If DataSourceType.CompetitionEvaluation, the Submission ID to evaluate.
    model_instance_id (int)
      If DataSourceType == ModelInstanceVersion, then SourceId =
      ModelInstanceVersion, and this is the ModelInstanceId.
    model_id (int)
      If DataSourceType == ModelInstanceVersion, then SourceId =
      ModelInstanceVersion, and this is the ModelId.
  """

  def __init__(self):
    self._source_type = DataSourceType.DATA_SOURCE_TYPE_COMPETITION
    self._source_id = 0
    self._dataset_id = None
    self._databundle_version_id = None
    self._mount_slug = None
    self._is_source_id_pinned = None
    self._submission_id = None
    self._model_instance_id = None
    self._model_id = None
    self._freeze()

  @property
  def source_type(self) -> 'DataSourceType':
    r"""
    Supports Competition, CompetitionEvaluation, DatasetVersion, KernelVersion,
    and ModelInstanceVersion
    """
    return self._source_type

  @source_type.setter
  def source_type(self, source_type: 'DataSourceType'):
    if source_type is None:
      del self.source_type
      return
    if not isinstance(source_type, DataSourceType):
      raise TypeError('source_type must be of type DataSourceType')
    self._source_type = source_type

  @property
  def source_id(self) -> int:
    r"""
    CompetitionId for Competition and CompetitionEvaluation
    DatasetVersionId for DatasetVersions
    KernelSessionId for KernelVersions
    ModelInstanceVersionId for ModelInstanceVersions
    """
    return self._source_id

  @source_id.setter
  def source_id(self, source_id: int):
    if source_id is None:
      del self.source_id
      return
    if not isinstance(source_id, int):
      raise TypeError('source_id must be of type int')
    self._source_id = source_id

  @property
  def dataset_id(self) -> int:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    Used for denormalizing KernelDatasetDataSources to improve performance
    This value needs to be set for DataSourceType.DatasetVersion
    """
    return self._dataset_id or None

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def databundle_version_id(self) -> int:
    r"""
    Represents the low-level DatabundleVersion to use for this datasource.
    Currently only used for Competition datasources, since a Competition's
    databundle can be updated over time, or reruns may use a different
    databundle altogether. This field does not need to be set, it will be
    auto-populated with the Competition's current DBVID if not. DatasetVersion
    implies DatabundleVersion (and it cannot change) so Dataset datasources
    don't need this.
    """
    return self._databundle_version_id or None

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: Optional[int]):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

  @property
  def mount_slug(self) -> str:
    r"""
    The sub-directory used for mounting in a kernel's input directory or empty
    if data source should be mounted directly in the input path (legacy,
    single-source session).
    """
    return self._mount_slug or None

  @mount_slug.setter
  def mount_slug(self, mount_slug: Optional[str]):
    if mount_slug is None:
      del self.mount_slug
      return
    if not isinstance(mount_slug, str):
      raise TypeError('mount_slug must be of type str')
    self._mount_slug = mount_slug

  @property
  def is_source_id_pinned(self) -> bool:
    r"""
    Whether the source_id should be pinned or if it should always use the
    latest version of the source. Not applicable for Competitions.
    """
    return self._is_source_id_pinned or None

  @is_source_id_pinned.setter
  def is_source_id_pinned(self, is_source_id_pinned: Optional[bool]):
    if is_source_id_pinned is None:
      del self.is_source_id_pinned
      return
    if not isinstance(is_source_id_pinned, bool):
      raise TypeError('is_source_id_pinned must be of type bool')
    self._is_source_id_pinned = is_source_id_pinned

  @property
  def submission_id(self) -> int:
    """If DataSourceType.CompetitionEvaluation, the Submission ID to evaluate."""
    return self._submission_id or 0

  @submission_id.setter
  def submission_id(self, submission_id: Optional[int]):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def model_instance_id(self) -> int:
    r"""
    If DataSourceType == ModelInstanceVersion, then SourceId =
    ModelInstanceVersion, and this is the ModelInstanceId.
    """
    return self._model_instance_id or 0

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: Optional[int]):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id

  @property
  def model_id(self) -> int:
    r"""
    If DataSourceType == ModelInstanceVersion, then SourceId =
    ModelInstanceVersion, and this is the ModelId.
    """
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: Optional[int]):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id


class DeleteKernelPinRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    competition_id (int)
      TODO(b/244443172): add user_id here
    dataset_id (int)
    model_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._competition_id = None
    self._dataset_id = None
    self._model_id = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def competition_id(self) -> int:
    """TODO(b/244443172): add user_id here"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.model_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    self._model_id = model_id


class DeleteKernelPinResponse(KaggleObject):
  r"""
  Attributes:
    kernel_pinned (bool)
  """

  def __init__(self):
    self._kernel_pinned = False
    self._freeze()

  @property
  def kernel_pinned(self) -> bool:
    return self._kernel_pinned

  @kernel_pinned.setter
  def kernel_pinned(self, kernel_pinned: bool):
    if kernel_pinned is None:
      del self.kernel_pinned
      return
    if not isinstance(kernel_pinned, bool):
      raise TypeError('kernel_pinned must be of type bool')
    self._kernel_pinned = kernel_pinned


class ForkParentInfo(KaggleObject):
  r"""
  Attributes:
    is_deleted (bool)
      If IsDeleted || !IsVisible, some other fields may be empty.
    is_visible (bool)
    author_display_name (str)
    kernel_id (int)
    kernel_url (str)
  """

  def __init__(self):
    self._is_deleted = False
    self._is_visible = False
    self._author_display_name = None
    self._kernel_id = 0
    self._kernel_url = None
    self._freeze()

  @property
  def is_deleted(self) -> bool:
    """If IsDeleted || !IsVisible, some other fields may be empty."""
    return self._is_deleted

  @is_deleted.setter
  def is_deleted(self, is_deleted: bool):
    if is_deleted is None:
      del self.is_deleted
      return
    if not isinstance(is_deleted, bool):
      raise TypeError('is_deleted must be of type bool')
    self._is_deleted = is_deleted

  @property
  def is_visible(self) -> bool:
    return self._is_visible

  @is_visible.setter
  def is_visible(self, is_visible: bool):
    if is_visible is None:
      del self.is_visible
      return
    if not isinstance(is_visible, bool):
      raise TypeError('is_visible must be of type bool')
    self._is_visible = is_visible

  @property
  def author_display_name(self) -> str:
    return self._author_display_name or ""

  @author_display_name.setter
  def author_display_name(self, author_display_name: Optional[str]):
    if author_display_name is None:
      del self.author_display_name
      return
    if not isinstance(author_display_name, str):
      raise TypeError('author_display_name must be of type str')
    self._author_display_name = author_display_name

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def kernel_url(self) -> str:
    return self._kernel_url or ""

  @kernel_url.setter
  def kernel_url(self, kernel_url: Optional[str]):
    if kernel_url is None:
      del self.kernel_url
      return
    if not isinstance(kernel_url, str):
      raise TypeError('kernel_url must be of type str')
    self._kernel_url = kernel_url


class GetKernelListDetailsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_ids (int)
    unauthorized_access_behavior (AccessBehavior)
    deleted_access_behavior (AccessBehavior)
    exclude_results_files_outputs (bool)
      The following 5 fields are for controlling output file responses
    want_output_files (bool)
    output_file_types (str)
    max_output_files_per_kernel (int)
    gcs_timeout_ms (int)
    read_mask (FieldMask)
    include_invalid_data_sources (bool)
  """

  def __init__(self):
    self._kernel_ids = []
    self._unauthorized_access_behavior = AccessBehavior.RETURN_SHELL_ENTRY
    self._deleted_access_behavior = AccessBehavior.RETURN_SHELL_ENTRY
    self._exclude_results_files_outputs = False
    self._want_output_files = False
    self._output_file_types = []
    self._max_output_files_per_kernel = None
    self._gcs_timeout_ms = None
    self._read_mask = None
    self._include_invalid_data_sources = False
    self._freeze()

  @property
  def kernel_ids(self) -> Optional[List[int]]:
    return self._kernel_ids

  @kernel_ids.setter
  def kernel_ids(self, kernel_ids: Optional[List[int]]):
    if kernel_ids is None:
      del self.kernel_ids
      return
    if not isinstance(kernel_ids, list):
      raise TypeError('kernel_ids must be of type list')
    if not all([isinstance(t, int) for t in kernel_ids]):
      raise TypeError('kernel_ids must contain only items of type int')
    self._kernel_ids = kernel_ids

  @property
  def unauthorized_access_behavior(self) -> 'AccessBehavior':
    return self._unauthorized_access_behavior

  @unauthorized_access_behavior.setter
  def unauthorized_access_behavior(self, unauthorized_access_behavior: 'AccessBehavior'):
    if unauthorized_access_behavior is None:
      del self.unauthorized_access_behavior
      return
    if not isinstance(unauthorized_access_behavior, AccessBehavior):
      raise TypeError('unauthorized_access_behavior must be of type AccessBehavior')
    self._unauthorized_access_behavior = unauthorized_access_behavior

  @property
  def deleted_access_behavior(self) -> 'AccessBehavior':
    return self._deleted_access_behavior

  @deleted_access_behavior.setter
  def deleted_access_behavior(self, deleted_access_behavior: 'AccessBehavior'):
    if deleted_access_behavior is None:
      del self.deleted_access_behavior
      return
    if not isinstance(deleted_access_behavior, AccessBehavior):
      raise TypeError('deleted_access_behavior must be of type AccessBehavior')
    self._deleted_access_behavior = deleted_access_behavior

  @property
  def exclude_results_files_outputs(self) -> bool:
    """The following 5 fields are for controlling output file responses"""
    return self._exclude_results_files_outputs

  @exclude_results_files_outputs.setter
  def exclude_results_files_outputs(self, exclude_results_files_outputs: bool):
    if exclude_results_files_outputs is None:
      del self.exclude_results_files_outputs
      return
    if not isinstance(exclude_results_files_outputs, bool):
      raise TypeError('exclude_results_files_outputs must be of type bool')
    self._exclude_results_files_outputs = exclude_results_files_outputs

  @property
  def want_output_files(self) -> bool:
    return self._want_output_files

  @want_output_files.setter
  def want_output_files(self, want_output_files: bool):
    if want_output_files is None:
      del self.want_output_files
      return
    if not isinstance(want_output_files, bool):
      raise TypeError('want_output_files must be of type bool')
    self._want_output_files = want_output_files

  @property
  def include_invalid_data_sources(self) -> bool:
    return self._include_invalid_data_sources

  @include_invalid_data_sources.setter
  def include_invalid_data_sources(self, include_invalid_data_sources: bool):
    if include_invalid_data_sources is None:
      del self.include_invalid_data_sources
      return
    if not isinstance(include_invalid_data_sources, bool):
      raise TypeError('include_invalid_data_sources must be of type bool')
    self._include_invalid_data_sources = include_invalid_data_sources

  @property
  def output_file_types(self) -> Optional[List[str]]:
    return self._output_file_types

  @output_file_types.setter
  def output_file_types(self, output_file_types: Optional[List[str]]):
    if output_file_types is None:
      del self.output_file_types
      return
    if not isinstance(output_file_types, list):
      raise TypeError('output_file_types must be of type list')
    if not all([isinstance(t, str) for t in output_file_types]):
      raise TypeError('output_file_types must contain only items of type str')
    self._output_file_types = output_file_types

  @property
  def max_output_files_per_kernel(self) -> int:
    return self._max_output_files_per_kernel or 0

  @max_output_files_per_kernel.setter
  def max_output_files_per_kernel(self, max_output_files_per_kernel: Optional[int]):
    if max_output_files_per_kernel is None:
      del self.max_output_files_per_kernel
      return
    if not isinstance(max_output_files_per_kernel, int):
      raise TypeError('max_output_files_per_kernel must be of type int')
    self._max_output_files_per_kernel = max_output_files_per_kernel

  @property
  def gcs_timeout_ms(self) -> int:
    return self._gcs_timeout_ms or 0

  @gcs_timeout_ms.setter
  def gcs_timeout_ms(self, gcs_timeout_ms: Optional[int]):
    if gcs_timeout_ms is None:
      del self.gcs_timeout_ms
      return
    if not isinstance(gcs_timeout_ms, int):
      raise TypeError('gcs_timeout_ms must be of type int')
    self._gcs_timeout_ms = gcs_timeout_ms

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class KernelList(KaggleObject):
  r"""
  Attributes:
    total_count (int)
      This is the total number of kernels that match the specified filters, even
      though the Kernels IEnumerable below will contain only a single page of
      results.
    kernels (KernelListItem)
    pinned_kernels (KernelListItem)
  """

  def __init__(self):
    self._total_count = None
    self._kernels = []
    self._pinned_kernels = []
    self._freeze()

  @property
  def total_count(self) -> int:
    r"""
    This is the total number of kernels that match the specified filters, even
    though the Kernels IEnumerable below will contain only a single page of
    results.
    """
    return self._total_count or 0

  @total_count.setter
  def total_count(self, total_count: Optional[int]):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def kernels(self) -> Optional[List[Optional['KernelListItem']]]:
    return self._kernels

  @kernels.setter
  def kernels(self, kernels: Optional[List[Optional['KernelListItem']]]):
    if kernels is None:
      del self.kernels
      return
    if not isinstance(kernels, list):
      raise TypeError('kernels must be of type list')
    if not all([isinstance(t, KernelListItem) for t in kernels]):
      raise TypeError('kernels must contain only items of type KernelListItem')
    self._kernels = kernels

  @property
  def pinned_kernels(self) -> Optional[List[Optional['KernelListItem']]]:
    return self._pinned_kernels

  @pinned_kernels.setter
  def pinned_kernels(self, pinned_kernels: Optional[List[Optional['KernelListItem']]]):
    if pinned_kernels is None:
      del self.pinned_kernels
      return
    if not isinstance(pinned_kernels, list):
      raise TypeError('pinned_kernels must be of type list')
    if not all([isinstance(t, KernelListItem) for t in pinned_kernels]):
      raise TypeError('pinned_kernels must contain only items of type KernelListItem')
    self._pinned_kernels = pinned_kernels


class KernelListItem(KaggleObject):
  r"""
  Attributes:
    author (User)
    current_user_has_voted_for_this_script (bool)
    data_sources (DataSource)
    fork_diff_lines_changed (int)
    fork_diff_lines_deleted (int)
    fork_diff_lines_inserted (int)
    fork_diff_url (str)
    has_collaborators (bool)
    id (int)
    script_version_id (int)
    is_fork (bool)
    is_private (bool)
    language_name (str)
    ace_language_name (str)
    is_notebook (bool)
    is_gpu_enabled (bool)
    best_public_score (float)
    forum_topic_id (int)
    last_run_execution_time_seconds (int)
    medal (Medal)
    categories (Category)
    title (str)
    total_comments (int)
    total_forks (int)
    total_scripts (int)
    total_views (int)
    total_votes (int)
    total_lines (int)
    current_user_has_bookmarked (bool)
    is_running (bool)
    is_deleted (bool)
    is_my_uncommitted_draft (bool)
    current_url_slug (str)
    script_version_date_created (datetime)
    date_evaluated (datetime)
    output_files (KernelSessionOutputFile)
    can_current_user_delete_kernel (bool)
    can_current_user_edit_kernel (bool)
    has_linked_submission (bool)
      Whether or not any child KernelSession was used to make a successful
      Competition Submission
    disable_comments (bool)
    task_submission_info (KernelTaskSubmissionInfo)
    fork_parent_info (ForkParentInfo)
    card_image_url (str)
    date_output_to_dataset_enabled (datetime)
    last_run_time (datetime)
      On rare occasions, back-end queueing errors result in DateEvaluated being
      blank. This causes the front-end to freak out, so we stick in an innocuous
      value.
    script_url (str)
    script_comments_url (str)
    script_input_url (str)
    script_edit_url (str)
    has_data_output_files (bool)
      It's expensive to get details for output files, and sometimes we just need
      to know there are data outputs. Ex: when considering a kernel as a data
      input source for another kernel. This does not include visualization
      outputs.
    date_output_to_model_enabled (datetime)
  """

  def __init__(self):
    self._author = None
    self._current_user_has_voted_for_this_script = False
    self._data_sources = []
    self._fork_diff_lines_changed = 0
    self._fork_diff_lines_deleted = 0
    self._fork_diff_lines_inserted = 0
    self._fork_diff_url = None
    self._has_collaborators = False
    self._id = 0
    self._script_version_id = None
    self._is_fork = False
    self._is_private = False
    self._language_name = None
    self._ace_language_name = None
    self._is_notebook = False
    self._is_gpu_enabled = False
    self._best_public_score = None
    self._forum_topic_id = None
    self._last_run_execution_time_seconds = None
    self._medal = Medal.MEDAL_UNSPECIFIED
    self._categories = []
    self._title = None
    self._total_comments = 0
    self._total_forks = 0
    self._total_scripts = 0
    self._total_views = 0
    self._total_votes = 0
    self._total_lines = 0
    self._current_user_has_bookmarked = False
    self._is_running = False
    self._is_deleted = False
    self._is_my_uncommitted_draft = False
    self._current_url_slug = None
    self._script_version_date_created = None
    self._date_evaluated = None
    self._output_files = []
    self._can_current_user_delete_kernel = False
    self._can_current_user_edit_kernel = False
    self._has_linked_submission = False
    self._disable_comments = False
    self._task_submission_info = None
    self._fork_parent_info = None
    self._card_image_url = None
    self._date_output_to_dataset_enabled = None
    self._last_run_time = None
    self._script_url = ""
    self._script_comments_url = ""
    self._script_input_url = ""
    self._script_edit_url = ""
    self._has_data_output_files = False
    self._date_output_to_model_enabled = None
    self._freeze()

  @property
  def author(self) -> Optional['User']:
    return self._author

  @author.setter
  def author(self, author: Optional['User']):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author

  @property
  def current_user_has_voted_for_this_script(self) -> bool:
    return self._current_user_has_voted_for_this_script

  @current_user_has_voted_for_this_script.setter
  def current_user_has_voted_for_this_script(self, current_user_has_voted_for_this_script: bool):
    if current_user_has_voted_for_this_script is None:
      del self.current_user_has_voted_for_this_script
      return
    if not isinstance(current_user_has_voted_for_this_script, bool):
      raise TypeError('current_user_has_voted_for_this_script must be of type bool')
    self._current_user_has_voted_for_this_script = current_user_has_voted_for_this_script

  @property
  def data_sources(self) -> Optional[List[Optional['DataSource']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSource']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSource) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSource')
    self._data_sources = data_sources

  @property
  def fork_diff_lines_changed(self) -> int:
    return self._fork_diff_lines_changed

  @fork_diff_lines_changed.setter
  def fork_diff_lines_changed(self, fork_diff_lines_changed: int):
    if fork_diff_lines_changed is None:
      del self.fork_diff_lines_changed
      return
    if not isinstance(fork_diff_lines_changed, int):
      raise TypeError('fork_diff_lines_changed must be of type int')
    self._fork_diff_lines_changed = fork_diff_lines_changed

  @property
  def fork_diff_lines_deleted(self) -> int:
    return self._fork_diff_lines_deleted

  @fork_diff_lines_deleted.setter
  def fork_diff_lines_deleted(self, fork_diff_lines_deleted: int):
    if fork_diff_lines_deleted is None:
      del self.fork_diff_lines_deleted
      return
    if not isinstance(fork_diff_lines_deleted, int):
      raise TypeError('fork_diff_lines_deleted must be of type int')
    self._fork_diff_lines_deleted = fork_diff_lines_deleted

  @property
  def fork_diff_lines_inserted(self) -> int:
    return self._fork_diff_lines_inserted

  @fork_diff_lines_inserted.setter
  def fork_diff_lines_inserted(self, fork_diff_lines_inserted: int):
    if fork_diff_lines_inserted is None:
      del self.fork_diff_lines_inserted
      return
    if not isinstance(fork_diff_lines_inserted, int):
      raise TypeError('fork_diff_lines_inserted must be of type int')
    self._fork_diff_lines_inserted = fork_diff_lines_inserted

  @property
  def fork_diff_url(self) -> str:
    return self._fork_diff_url or ""

  @fork_diff_url.setter
  def fork_diff_url(self, fork_diff_url: Optional[str]):
    if fork_diff_url is None:
      del self.fork_diff_url
      return
    if not isinstance(fork_diff_url, str):
      raise TypeError('fork_diff_url must be of type str')
    self._fork_diff_url = fork_diff_url

  @property
  def has_collaborators(self) -> bool:
    return self._has_collaborators

  @has_collaborators.setter
  def has_collaborators(self, has_collaborators: bool):
    if has_collaborators is None:
      del self.has_collaborators
      return
    if not isinstance(has_collaborators, bool):
      raise TypeError('has_collaborators must be of type bool')
    self._has_collaborators = has_collaborators

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def script_version_id(self) -> int:
    return self._script_version_id or 0

  @script_version_id.setter
  def script_version_id(self, script_version_id: Optional[int]):
    if script_version_id is None:
      del self.script_version_id
      return
    if not isinstance(script_version_id, int):
      raise TypeError('script_version_id must be of type int')
    self._script_version_id = script_version_id

  @property
  def is_fork(self) -> bool:
    return self._is_fork

  @is_fork.setter
  def is_fork(self, is_fork: bool):
    if is_fork is None:
      del self.is_fork
      return
    if not isinstance(is_fork, bool):
      raise TypeError('is_fork must be of type bool')
    self._is_fork = is_fork

  @property
  def is_private(self) -> bool:
    return self._is_private

  @is_private.setter
  def is_private(self, is_private: bool):
    if is_private is None:
      del self.is_private
      return
    if not isinstance(is_private, bool):
      raise TypeError('is_private must be of type bool')
    self._is_private = is_private

  @property
  def language_name(self) -> str:
    return self._language_name or ""

  @language_name.setter
  def language_name(self, language_name: Optional[str]):
    if language_name is None:
      del self.language_name
      return
    if not isinstance(language_name, str):
      raise TypeError('language_name must be of type str')
    self._language_name = language_name

  @property
  def ace_language_name(self) -> str:
    return self._ace_language_name or ""

  @ace_language_name.setter
  def ace_language_name(self, ace_language_name: Optional[str]):
    if ace_language_name is None:
      del self.ace_language_name
      return
    if not isinstance(ace_language_name, str):
      raise TypeError('ace_language_name must be of type str')
    self._ace_language_name = ace_language_name

  @property
  def is_notebook(self) -> bool:
    return self._is_notebook

  @is_notebook.setter
  def is_notebook(self, is_notebook: bool):
    if is_notebook is None:
      del self.is_notebook
      return
    if not isinstance(is_notebook, bool):
      raise TypeError('is_notebook must be of type bool')
    self._is_notebook = is_notebook

  @property
  def is_gpu_enabled(self) -> bool:
    return self._is_gpu_enabled

  @is_gpu_enabled.setter
  def is_gpu_enabled(self, is_gpu_enabled: bool):
    if is_gpu_enabled is None:
      del self.is_gpu_enabled
      return
    if not isinstance(is_gpu_enabled, bool):
      raise TypeError('is_gpu_enabled must be of type bool')
    self._is_gpu_enabled = is_gpu_enabled

  @property
  def best_public_score(self) -> float:
    return self._best_public_score or 0.0

  @best_public_score.setter
  def best_public_score(self, best_public_score: Optional[float]):
    if best_public_score is None:
      del self.best_public_score
      return
    if not isinstance(best_public_score, float):
      raise TypeError('best_public_score must be of type float')
    self._best_public_score = best_public_score

  @property
  def forum_topic_id(self) -> int:
    return self._forum_topic_id or 0

  @forum_topic_id.setter
  def forum_topic_id(self, forum_topic_id: Optional[int]):
    if forum_topic_id is None:
      del self.forum_topic_id
      return
    if not isinstance(forum_topic_id, int):
      raise TypeError('forum_topic_id must be of type int')
    self._forum_topic_id = forum_topic_id

  @property
  def last_run_execution_time_seconds(self) -> int:
    return self._last_run_execution_time_seconds or 0

  @last_run_execution_time_seconds.setter
  def last_run_execution_time_seconds(self, last_run_execution_time_seconds: Optional[int]):
    if last_run_execution_time_seconds is None:
      del self.last_run_execution_time_seconds
      return
    if not isinstance(last_run_execution_time_seconds, int):
      raise TypeError('last_run_execution_time_seconds must be of type int')
    self._last_run_execution_time_seconds = last_run_execution_time_seconds

  @property
  def medal(self) -> 'Medal':
    return self._medal

  @medal.setter
  def medal(self, medal: 'Medal'):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Medal):
      raise TypeError('medal must be of type Medal')
    self._medal = medal

  @property
  def categories(self) -> Optional[List[Optional['Category']]]:
    return self._categories

  @categories.setter
  def categories(self, categories: Optional[List[Optional['Category']]]):
    if categories is None:
      del self.categories
      return
    if not isinstance(categories, list):
      raise TypeError('categories must be of type list')
    if not all([isinstance(t, Category) for t in categories]):
      raise TypeError('categories must contain only items of type Category')
    self._categories = categories

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def total_comments(self) -> int:
    return self._total_comments

  @total_comments.setter
  def total_comments(self, total_comments: int):
    if total_comments is None:
      del self.total_comments
      return
    if not isinstance(total_comments, int):
      raise TypeError('total_comments must be of type int')
    self._total_comments = total_comments

  @property
  def total_forks(self) -> int:
    return self._total_forks

  @total_forks.setter
  def total_forks(self, total_forks: int):
    if total_forks is None:
      del self.total_forks
      return
    if not isinstance(total_forks, int):
      raise TypeError('total_forks must be of type int')
    self._total_forks = total_forks

  @property
  def total_scripts(self) -> int:
    return self._total_scripts

  @total_scripts.setter
  def total_scripts(self, total_scripts: int):
    if total_scripts is None:
      del self.total_scripts
      return
    if not isinstance(total_scripts, int):
      raise TypeError('total_scripts must be of type int')
    self._total_scripts = total_scripts

  @property
  def total_views(self) -> int:
    return self._total_views

  @total_views.setter
  def total_views(self, total_views: int):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def total_lines(self) -> int:
    return self._total_lines

  @total_lines.setter
  def total_lines(self, total_lines: int):
    if total_lines is None:
      del self.total_lines
      return
    if not isinstance(total_lines, int):
      raise TypeError('total_lines must be of type int')
    self._total_lines = total_lines

  @property
  def current_user_has_bookmarked(self) -> bool:
    return self._current_user_has_bookmarked

  @current_user_has_bookmarked.setter
  def current_user_has_bookmarked(self, current_user_has_bookmarked: bool):
    if current_user_has_bookmarked is None:
      del self.current_user_has_bookmarked
      return
    if not isinstance(current_user_has_bookmarked, bool):
      raise TypeError('current_user_has_bookmarked must be of type bool')
    self._current_user_has_bookmarked = current_user_has_bookmarked

  @property
  def is_running(self) -> bool:
    return self._is_running

  @is_running.setter
  def is_running(self, is_running: bool):
    if is_running is None:
      del self.is_running
      return
    if not isinstance(is_running, bool):
      raise TypeError('is_running must be of type bool')
    self._is_running = is_running

  @property
  def is_deleted(self) -> bool:
    return self._is_deleted

  @is_deleted.setter
  def is_deleted(self, is_deleted: bool):
    if is_deleted is None:
      del self.is_deleted
      return
    if not isinstance(is_deleted, bool):
      raise TypeError('is_deleted must be of type bool')
    self._is_deleted = is_deleted

  @property
  def is_my_uncommitted_draft(self) -> bool:
    return self._is_my_uncommitted_draft

  @is_my_uncommitted_draft.setter
  def is_my_uncommitted_draft(self, is_my_uncommitted_draft: bool):
    if is_my_uncommitted_draft is None:
      del self.is_my_uncommitted_draft
      return
    if not isinstance(is_my_uncommitted_draft, bool):
      raise TypeError('is_my_uncommitted_draft must be of type bool')
    self._is_my_uncommitted_draft = is_my_uncommitted_draft

  @property
  def current_url_slug(self) -> str:
    return self._current_url_slug or ""

  @current_url_slug.setter
  def current_url_slug(self, current_url_slug: Optional[str]):
    if current_url_slug is None:
      del self.current_url_slug
      return
    if not isinstance(current_url_slug, str):
      raise TypeError('current_url_slug must be of type str')
    self._current_url_slug = current_url_slug

  @property
  def script_version_date_created(self) -> datetime:
    return self._script_version_date_created

  @script_version_date_created.setter
  def script_version_date_created(self, script_version_date_created: datetime):
    if script_version_date_created is None:
      del self.script_version_date_created
      return
    if not isinstance(script_version_date_created, datetime):
      raise TypeError('script_version_date_created must be of type datetime')
    self._script_version_date_created = script_version_date_created

  @property
  def date_evaluated(self) -> datetime:
    return self._date_evaluated

  @date_evaluated.setter
  def date_evaluated(self, date_evaluated: datetime):
    if date_evaluated is None:
      del self.date_evaluated
      return
    if not isinstance(date_evaluated, datetime):
      raise TypeError('date_evaluated must be of type datetime')
    self._date_evaluated = date_evaluated

  @property
  def output_files(self) -> Optional[List[Optional['KernelSessionOutputFile']]]:
    return self._output_files

  @output_files.setter
  def output_files(self, output_files: Optional[List[Optional['KernelSessionOutputFile']]]):
    if output_files is None:
      del self.output_files
      return
    if not isinstance(output_files, list):
      raise TypeError('output_files must be of type list')
    if not all([isinstance(t, KernelSessionOutputFile) for t in output_files]):
      raise TypeError('output_files must contain only items of type KernelSessionOutputFile')
    self._output_files = output_files

  @property
  def can_current_user_delete_kernel(self) -> bool:
    return self._can_current_user_delete_kernel

  @can_current_user_delete_kernel.setter
  def can_current_user_delete_kernel(self, can_current_user_delete_kernel: bool):
    if can_current_user_delete_kernel is None:
      del self.can_current_user_delete_kernel
      return
    if not isinstance(can_current_user_delete_kernel, bool):
      raise TypeError('can_current_user_delete_kernel must be of type bool')
    self._can_current_user_delete_kernel = can_current_user_delete_kernel

  @property
  def can_current_user_edit_kernel(self) -> bool:
    return self._can_current_user_edit_kernel

  @can_current_user_edit_kernel.setter
  def can_current_user_edit_kernel(self, can_current_user_edit_kernel: bool):
    if can_current_user_edit_kernel is None:
      del self.can_current_user_edit_kernel
      return
    if not isinstance(can_current_user_edit_kernel, bool):
      raise TypeError('can_current_user_edit_kernel must be of type bool')
    self._can_current_user_edit_kernel = can_current_user_edit_kernel

  @property
  def has_linked_submission(self) -> bool:
    r"""
    Whether or not any child KernelSession was used to make a successful
    Competition Submission
    """
    return self._has_linked_submission

  @has_linked_submission.setter
  def has_linked_submission(self, has_linked_submission: bool):
    if has_linked_submission is None:
      del self.has_linked_submission
      return
    if not isinstance(has_linked_submission, bool):
      raise TypeError('has_linked_submission must be of type bool')
    self._has_linked_submission = has_linked_submission

  @property
  def disable_comments(self) -> bool:
    return self._disable_comments

  @disable_comments.setter
  def disable_comments(self, disable_comments: bool):
    if disable_comments is None:
      del self.disable_comments
      return
    if not isinstance(disable_comments, bool):
      raise TypeError('disable_comments must be of type bool')
    self._disable_comments = disable_comments

  @property
  def task_submission_info(self) -> Optional['KernelTaskSubmissionInfo']:
    return self._task_submission_info

  @task_submission_info.setter
  def task_submission_info(self, task_submission_info: Optional['KernelTaskSubmissionInfo']):
    if task_submission_info is None:
      del self.task_submission_info
      return
    if not isinstance(task_submission_info, KernelTaskSubmissionInfo):
      raise TypeError('task_submission_info must be of type KernelTaskSubmissionInfo')
    self._task_submission_info = task_submission_info

  @property
  def fork_parent_info(self) -> Optional['ForkParentInfo']:
    return self._fork_parent_info

  @fork_parent_info.setter
  def fork_parent_info(self, fork_parent_info: Optional['ForkParentInfo']):
    if fork_parent_info is None:
      del self.fork_parent_info
      return
    if not isinstance(fork_parent_info, ForkParentInfo):
      raise TypeError('fork_parent_info must be of type ForkParentInfo')
    self._fork_parent_info = fork_parent_info

  @property
  def card_image_url(self) -> str:
    return self._card_image_url or ""

  @card_image_url.setter
  def card_image_url(self, card_image_url: Optional[str]):
    if card_image_url is None:
      del self.card_image_url
      return
    if not isinstance(card_image_url, str):
      raise TypeError('card_image_url must be of type str')
    self._card_image_url = card_image_url

  @property
  def date_output_to_dataset_enabled(self) -> datetime:
    return self._date_output_to_dataset_enabled

  @date_output_to_dataset_enabled.setter
  def date_output_to_dataset_enabled(self, date_output_to_dataset_enabled: datetime):
    if date_output_to_dataset_enabled is None:
      del self.date_output_to_dataset_enabled
      return
    if not isinstance(date_output_to_dataset_enabled, datetime):
      raise TypeError('date_output_to_dataset_enabled must be of type datetime')
    self._date_output_to_dataset_enabled = date_output_to_dataset_enabled

  @property
  def date_output_to_model_enabled(self) -> datetime:
    return self._date_output_to_model_enabled

  @date_output_to_model_enabled.setter
  def date_output_to_model_enabled(self, date_output_to_model_enabled: datetime):
    if date_output_to_model_enabled is None:
      del self.date_output_to_model_enabled
      return
    if not isinstance(date_output_to_model_enabled, datetime):
      raise TypeError('date_output_to_model_enabled must be of type datetime')
    self._date_output_to_model_enabled = date_output_to_model_enabled

  @property
  def last_run_time(self) -> datetime:
    r"""
    On rare occasions, back-end queueing errors result in DateEvaluated being
    blank. This causes the front-end to freak out, so we stick in an innocuous
    value.
    """
    return self._last_run_time

  @last_run_time.setter
  def last_run_time(self, last_run_time: datetime):
    if last_run_time is None:
      del self.last_run_time
      return
    if not isinstance(last_run_time, datetime):
      raise TypeError('last_run_time must be of type datetime')
    self._last_run_time = last_run_time

  @property
  def script_url(self) -> str:
    return self._script_url

  @script_url.setter
  def script_url(self, script_url: str):
    if script_url is None:
      del self.script_url
      return
    if not isinstance(script_url, str):
      raise TypeError('script_url must be of type str')
    self._script_url = script_url

  @property
  def script_comments_url(self) -> str:
    return self._script_comments_url

  @script_comments_url.setter
  def script_comments_url(self, script_comments_url: str):
    if script_comments_url is None:
      del self.script_comments_url
      return
    if not isinstance(script_comments_url, str):
      raise TypeError('script_comments_url must be of type str')
    self._script_comments_url = script_comments_url

  @property
  def script_input_url(self) -> str:
    return self._script_input_url

  @script_input_url.setter
  def script_input_url(self, script_input_url: str):
    if script_input_url is None:
      del self.script_input_url
      return
    if not isinstance(script_input_url, str):
      raise TypeError('script_input_url must be of type str')
    self._script_input_url = script_input_url

  @property
  def script_edit_url(self) -> str:
    return self._script_edit_url

  @script_edit_url.setter
  def script_edit_url(self, script_edit_url: str):
    if script_edit_url is None:
      del self.script_edit_url
      return
    if not isinstance(script_edit_url, str):
      raise TypeError('script_edit_url must be of type str')
    self._script_edit_url = script_edit_url

  @property
  def has_data_output_files(self) -> bool:
    r"""
    It's expensive to get details for output files, and sometimes we just need
    to know there are data outputs. Ex: when considering a kernel as a data
    input source for another kernel. This does not include visualization
    outputs.
    """
    return self._has_data_output_files

  @has_data_output_files.setter
  def has_data_output_files(self, has_data_output_files: bool):
    if has_data_output_files is None:
      del self.has_data_output_files
      return
    if not isinstance(has_data_output_files, bool):
      raise TypeError('has_data_output_files must be of type bool')
    self._has_data_output_files = has_data_output_files


class KernelPinListItem(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    competition_id (int)
      TODO(b/244443172): add user_id here
    dataset_id (int)
    model_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._competition_id = None
    self._dataset_id = None
    self._model_id = None
    self._freeze()

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def competition_id(self) -> int:
    """TODO(b/244443172): add user_id here"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.model_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    self._model_id = model_id


class KernelSessionOutputFile(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
    kernel_id (int)
    name (str)
    content_length (int)
    full_path (str)
    download_url (str)
    file_type (str)
  """

  def __init__(self):
    self._kernel_session_id = 0
    self._kernel_id = 0
    self._name = None
    self._content_length = 0
    self._full_path = None
    self._download_url = None
    self._file_type = None
    self._freeze()

  @property
  def kernel_session_id(self) -> int:
    return self._kernel_session_id

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    self._kernel_session_id = kernel_session_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    self._kernel_id = kernel_id

  @property
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def content_length(self) -> int:
    return self._content_length

  @content_length.setter
  def content_length(self, content_length: int):
    if content_length is None:
      del self.content_length
      return
    if not isinstance(content_length, int):
      raise TypeError('content_length must be of type int')
    self._content_length = content_length

  @property
  def full_path(self) -> str:
    return self._full_path or ""

  @full_path.setter
  def full_path(self, full_path: Optional[str]):
    if full_path is None:
      del self.full_path
      return
    if not isinstance(full_path, str):
      raise TypeError('full_path must be of type str')
    self._full_path = full_path

  @property
  def download_url(self) -> str:
    return self._download_url or ""

  @download_url.setter
  def download_url(self, download_url: Optional[str]):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url

  @property
  def file_type(self) -> str:
    return self._file_type or ""

  @file_type.setter
  def file_type(self, file_type: Optional[str]):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, str):
      raise TypeError('file_type must be of type str')
    self._file_type = file_type


class ListKernelIdsRequest(KaggleObject):
  r"""
  Attributes:
    after (int)
    competition_id (int)
    dataset_id (int)
    datasource_type (str)
    fork_parent_script_id (int)
    group (KernelsListViewType)
    kernel_type (str)
    language (str)
    output_type (str)
    exclude_results_files_outputs (bool)
    page (int)
    page_size (int)
    sort_by (KernelsListSortType)
    user_id (int)
    tag_ids (str)
      SmartList can't handle int[], so we use a comma-delimited string of ints.
      TODO - SmartList is no more, consider changing this to int.
    want_output_files (bool)
    has_gpu_run (bool)
    privacy (str)
      Whether to return public, private kernels or both. Ignored if Group !=
      (Profile or Collaboration).
    exclude_kernel_ids (int)
    model_instance_ids (int)
      List Kernels associated with any of these ModelInstances.
      Useful for targeting any Kernels that associate to Models of a given
      framework or variation slug. Logic for determining this is expected to be
      handled client-side for now, but could change later to take optional
      framework and/or variation_slug fields. http://go/mdp-notebook-filtering
    model_ids (int)
      List Kernels associated with these Models. The first Model specified is
      used for fetching pinned Kernels.
    exclude_non_accessed_datasources (bool)
      Filter out Kernels where the specified datasource's IsAccessed field is set
      to false (only models as of now)
    resource_reference_id (int)
      List Kernels associated with this ResourceReferenceId
  """

  def __init__(self):
    self._after = None
    self._competition_id = None
    self._dataset_id = None
    self._datasource_type = None
    self._fork_parent_script_id = None
    self._group = KernelsListViewType.KERNELS_LIST_VIEW_TYPE_UNSPECIFIED
    self._kernel_type = None
    self._language = None
    self._output_type = None
    self._exclude_results_files_outputs = False
    self._page = 0
    self._page_size = 0
    self._sort_by = KernelsListSortType.HOTNESS
    self._user_id = None
    self._tag_ids = None
    self._want_output_files = False
    self._has_gpu_run = None
    self._privacy = None
    self._exclude_kernel_ids = []
    self._model_instance_ids = []
    self._model_ids = []
    self._exclude_non_accessed_datasources = None
    self._resource_reference_id = None
    self._freeze()

  @property
  def after(self) -> int:
    return self._after or 0

  @after.setter
  def after(self, after: Optional[int]):
    if after is None:
      del self.after
      return
    if not isinstance(after, int):
      raise TypeError('after must be of type int')
    self._after = after

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[int]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    self._dataset_id = dataset_id

  @property
  def datasource_type(self) -> str:
    return self._datasource_type or ""

  @datasource_type.setter
  def datasource_type(self, datasource_type: Optional[str]):
    if datasource_type is None:
      del self.datasource_type
      return
    if not isinstance(datasource_type, str):
      raise TypeError('datasource_type must be of type str')
    self._datasource_type = datasource_type

  @property
  def fork_parent_script_id(self) -> int:
    return self._fork_parent_script_id or 0

  @fork_parent_script_id.setter
  def fork_parent_script_id(self, fork_parent_script_id: Optional[int]):
    if fork_parent_script_id is None:
      del self.fork_parent_script_id
      return
    if not isinstance(fork_parent_script_id, int):
      raise TypeError('fork_parent_script_id must be of type int')
    self._fork_parent_script_id = fork_parent_script_id

  @property
  def group(self) -> 'KernelsListViewType':
    return self._group

  @group.setter
  def group(self, group: 'KernelsListViewType'):
    if group is None:
      del self.group
      return
    if not isinstance(group, KernelsListViewType):
      raise TypeError('group must be of type KernelsListViewType')
    self._group = group

  @property
  def kernel_type(self) -> str:
    return self._kernel_type or ""

  @kernel_type.setter
  def kernel_type(self, kernel_type: Optional[str]):
    if kernel_type is None:
      del self.kernel_type
      return
    if not isinstance(kernel_type, str):
      raise TypeError('kernel_type must be of type str')
    self._kernel_type = kernel_type

  @property
  def language(self) -> str:
    return self._language or ""

  @language.setter
  def language(self, language: Optional[str]):
    if language is None:
      del self.language
      return
    if not isinstance(language, str):
      raise TypeError('language must be of type str')
    self._language = language

  @property
  def output_type(self) -> str:
    return self._output_type or ""

  @output_type.setter
  def output_type(self, output_type: Optional[str]):
    if output_type is None:
      del self.output_type
      return
    if not isinstance(output_type, str):
      raise TypeError('output_type must be of type str')
    self._output_type = output_type

  @property
  def exclude_results_files_outputs(self) -> bool:
    return self._exclude_results_files_outputs

  @exclude_results_files_outputs.setter
  def exclude_results_files_outputs(self, exclude_results_files_outputs: bool):
    if exclude_results_files_outputs is None:
      del self.exclude_results_files_outputs
      return
    if not isinstance(exclude_results_files_outputs, bool):
      raise TypeError('exclude_results_files_outputs must be of type bool')
    self._exclude_results_files_outputs = exclude_results_files_outputs

  @property
  def page(self) -> int:
    return self._page

  @page.setter
  def page(self, page: int):
    if page is None:
      del self.page
      return
    if not isinstance(page, int):
      raise TypeError('page must be of type int')
    self._page = page

  @property
  def page_size(self) -> int:
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
  def sort_by(self) -> 'KernelsListSortType':
    return self._sort_by

  @sort_by.setter
  def sort_by(self, sort_by: 'KernelsListSortType'):
    if sort_by is None:
      del self.sort_by
      return
    if not isinstance(sort_by, KernelsListSortType):
      raise TypeError('sort_by must be of type KernelsListSortType')
    self._sort_by = sort_by

  @property
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def tag_ids(self) -> str:
    r"""
    SmartList can't handle int[], so we use a comma-delimited string of ints.
    TODO - SmartList is no more, consider changing this to int.
    """
    return self._tag_ids or ""

  @tag_ids.setter
  def tag_ids(self, tag_ids: Optional[str]):
    if tag_ids is None:
      del self.tag_ids
      return
    if not isinstance(tag_ids, str):
      raise TypeError('tag_ids must be of type str')
    self._tag_ids = tag_ids

  @property
  def want_output_files(self) -> bool:
    return self._want_output_files

  @want_output_files.setter
  def want_output_files(self, want_output_files: bool):
    if want_output_files is None:
      del self.want_output_files
      return
    if not isinstance(want_output_files, bool):
      raise TypeError('want_output_files must be of type bool')
    self._want_output_files = want_output_files

  @property
  def has_gpu_run(self) -> bool:
    return self._has_gpu_run or False

  @has_gpu_run.setter
  def has_gpu_run(self, has_gpu_run: Optional[bool]):
    if has_gpu_run is None:
      del self.has_gpu_run
      return
    if not isinstance(has_gpu_run, bool):
      raise TypeError('has_gpu_run must be of type bool')
    self._has_gpu_run = has_gpu_run

  @property
  def privacy(self) -> str:
    r"""
    Whether to return public, private kernels or both. Ignored if Group !=
    (Profile or Collaboration).
    """
    return self._privacy or ""

  @privacy.setter
  def privacy(self, privacy: Optional[str]):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, str):
      raise TypeError('privacy must be of type str')
    self._privacy = privacy

  @property
  def exclude_kernel_ids(self) -> Optional[List[int]]:
    return self._exclude_kernel_ids

  @exclude_kernel_ids.setter
  def exclude_kernel_ids(self, exclude_kernel_ids: Optional[List[int]]):
    if exclude_kernel_ids is None:
      del self.exclude_kernel_ids
      return
    if not isinstance(exclude_kernel_ids, list):
      raise TypeError('exclude_kernel_ids must be of type list')
    if not all([isinstance(t, int) for t in exclude_kernel_ids]):
      raise TypeError('exclude_kernel_ids must contain only items of type int')
    self._exclude_kernel_ids = exclude_kernel_ids

  @property
  def model_ids(self) -> Optional[List[int]]:
    r"""
    List Kernels associated with these Models. The first Model specified is
    used for fetching pinned Kernels.
    """
    return self._model_ids

  @model_ids.setter
  def model_ids(self, model_ids: Optional[List[int]]):
    if model_ids is None:
      del self.model_ids
      return
    if not isinstance(model_ids, list):
      raise TypeError('model_ids must be of type list')
    if not all([isinstance(t, int) for t in model_ids]):
      raise TypeError('model_ids must contain only items of type int')
    self._model_ids = model_ids

  @property
  def model_instance_ids(self) -> Optional[List[int]]:
    r"""
    List Kernels associated with any of these ModelInstances.
    Useful for targeting any Kernels that associate to Models of a given
    framework or variation slug. Logic for determining this is expected to be
    handled client-side for now, but could change later to take optional
    framework and/or variation_slug fields. http://go/mdp-notebook-filtering
    """
    return self._model_instance_ids

  @model_instance_ids.setter
  def model_instance_ids(self, model_instance_ids: Optional[List[int]]):
    if model_instance_ids is None:
      del self.model_instance_ids
      return
    if not isinstance(model_instance_ids, list):
      raise TypeError('model_instance_ids must be of type list')
    if not all([isinstance(t, int) for t in model_instance_ids]):
      raise TypeError('model_instance_ids must contain only items of type int')
    self._model_instance_ids = model_instance_ids

  @property
  def exclude_non_accessed_datasources(self) -> bool:
    r"""
    Filter out Kernels where the specified datasource's IsAccessed field is set
    to false (only models as of now)
    """
    return self._exclude_non_accessed_datasources or False

  @exclude_non_accessed_datasources.setter
  def exclude_non_accessed_datasources(self, exclude_non_accessed_datasources: Optional[bool]):
    if exclude_non_accessed_datasources is None:
      del self.exclude_non_accessed_datasources
      return
    if not isinstance(exclude_non_accessed_datasources, bool):
      raise TypeError('exclude_non_accessed_datasources must be of type bool')
    self._exclude_non_accessed_datasources = exclude_non_accessed_datasources

  @property
  def resource_reference_id(self) -> int:
    """List Kernels associated with this ResourceReferenceId"""
    return self._resource_reference_id or 0

  @resource_reference_id.setter
  def resource_reference_id(self, resource_reference_id: Optional[int]):
    if resource_reference_id is None:
      del self.resource_reference_id
      return
    if not isinstance(resource_reference_id, int):
      raise TypeError('resource_reference_id must be of type int')
    self._resource_reference_id = resource_reference_id


class ListKernelPinsRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
      TODO(b/244443172): add user_id here
    dataset_id (int)
    model_id (int)
  """

  def __init__(self):
    self._competition_id = None
    self._dataset_id = None
    self._model_id = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    """TODO(b/244443172): add user_id here"""
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.dataset_id
    del self.model_id
    self._competition_id = competition_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.competition_id
    del self.model_id
    self._dataset_id = dataset_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.competition_id
    del self.dataset_id
    self._model_id = model_id


class ListKernelPinsResponse(KaggleObject):
  r"""
  Attributes:
    kernel_pins (KernelPinListItem)
  """

  def __init__(self):
    self._kernel_pins = []
    self._freeze()

  @property
  def kernel_pins(self) -> Optional[List[Optional['KernelPinListItem']]]:
    return self._kernel_pins

  @kernel_pins.setter
  def kernel_pins(self, kernel_pins: Optional[List[Optional['KernelPinListItem']]]):
    if kernel_pins is None:
      del self.kernel_pins
      return
    if not isinstance(kernel_pins, list):
      raise TypeError('kernel_pins must be of type list')
    if not all([isinstance(t, KernelPinListItem) for t in kernel_pins]):
      raise TypeError('kernel_pins must contain only items of type KernelPinListItem')
    self._kernel_pins = kernel_pins


class ListKernelsRequest(KaggleObject):
  r"""
  Attributes:
    kernel_filter_criteria (SearchKernelIdsRequest)
    detail_filter_criteria (GetKernelListDetailsRequest)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._kernel_filter_criteria = None
    self._detail_filter_criteria = None
    self._read_mask = None
    self._freeze()

  @property
  def kernel_filter_criteria(self) -> Optional['SearchKernelIdsRequest']:
    return self._kernel_filter_criteria

  @kernel_filter_criteria.setter
  def kernel_filter_criteria(self, kernel_filter_criteria: Optional['SearchKernelIdsRequest']):
    if kernel_filter_criteria is None:
      del self.kernel_filter_criteria
      return
    if not isinstance(kernel_filter_criteria, SearchKernelIdsRequest):
      raise TypeError('kernel_filter_criteria must be of type SearchKernelIdsRequest')
    self._kernel_filter_criteria = kernel_filter_criteria

  @property
  def detail_filter_criteria(self) -> Optional['GetKernelListDetailsRequest']:
    return self._detail_filter_criteria

  @detail_filter_criteria.setter
  def detail_filter_criteria(self, detail_filter_criteria: Optional['GetKernelListDetailsRequest']):
    if detail_filter_criteria is None:
      del self.detail_filter_criteria
      return
    if not isinstance(detail_filter_criteria, GetKernelListDetailsRequest):
      raise TypeError('detail_filter_criteria must be of type GetKernelListDetailsRequest')
    self._detail_filter_criteria = detail_filter_criteria

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask or None

  @read_mask.setter
  def read_mask(self, read_mask: Optional[FieldMask]):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListResourceReferencesByIdsRequest(KaggleObject):
  r"""
  Attributes:
    resource_reference_ids (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._resource_reference_ids = []
    self._read_mask = None
    self._freeze()

  @property
  def resource_reference_ids(self) -> Optional[List[int]]:
    return self._resource_reference_ids

  @resource_reference_ids.setter
  def resource_reference_ids(self, resource_reference_ids: Optional[List[int]]):
    if resource_reference_ids is None:
      del self.resource_reference_ids
      return
    if not isinstance(resource_reference_ids, list):
      raise TypeError('resource_reference_ids must be of type list')
    if not all([isinstance(t, int) for t in resource_reference_ids]):
      raise TypeError('resource_reference_ids must contain only items of type int')
    self._resource_reference_ids = resource_reference_ids

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListResourceReferencesFilter(KaggleObject):
  r"""
  Attributes:
    type (ResourceReferenceType)
    owner_identifier (str)
    search_query (str)
    ids (int)
  """

  def __init__(self):
    self._type = ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED
    self._owner_identifier = None
    self._search_query = None
    self._ids = []
    self._freeze()

  @property
  def type(self) -> 'ResourceReferenceType':
    return self._type

  @type.setter
  def type(self, type: 'ResourceReferenceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ResourceReferenceType):
      raise TypeError('type must be of type ResourceReferenceType')
    self._type = type

  @property
  def owner_identifier(self) -> str:
    return self._owner_identifier or ""

  @owner_identifier.setter
  def owner_identifier(self, owner_identifier: Optional[str]):
    if owner_identifier is None:
      del self.owner_identifier
      return
    if not isinstance(owner_identifier, str):
      raise TypeError('owner_identifier must be of type str')
    self._owner_identifier = owner_identifier

  @property
  def search_query(self) -> str:
    return self._search_query or ""

  @search_query.setter
  def search_query(self, search_query: Optional[str]):
    if search_query is None:
      del self.search_query
      return
    if not isinstance(search_query, str):
      raise TypeError('search_query must be of type str')
    self._search_query = search_query

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids


class ListResourceReferencesRequest(KaggleObject):
  r"""
  Attributes:
    filter (ListResourceReferencesFilter)
    order_by (ListResourceReferencesOrderBy)
    page_size (int)
    page_token (str)
    read_mask (FieldMask)
    skip (int)
  """

  def __init__(self):
    self._filter = None
    self._order_by = ListResourceReferencesOrderBy.LIST_RESOURCE_REFERENCES_ORDER_BY_UNSPECIFIED
    self._page_size = 0
    self._page_token = ""
    self._read_mask = None
    self._skip = 0
    self._freeze()

  @property
  def filter(self) -> Optional['ListResourceReferencesFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListResourceReferencesFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListResourceReferencesFilter):
      raise TypeError('filter must be of type ListResourceReferencesFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListResourceReferencesOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListResourceReferencesOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListResourceReferencesOrderBy):
      raise TypeError('order_by must be of type ListResourceReferencesOrderBy')
    self._order_by = order_by

  @property
  def page_size(self) -> int:
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
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListResourceReferencesResponse(KaggleObject):
  r"""
  Attributes:
    resource_references (ResourceReference)
    next_page_token (str)
    total_results (int)
  """

  def __init__(self):
    self._resource_references = []
    self._next_page_token = ""
    self._total_results = 0
    self._freeze()

  @property
  def resource_references(self) -> Optional[List[Optional['ResourceReference']]]:
    return self._resource_references

  @resource_references.setter
  def resource_references(self, resource_references: Optional[List[Optional['ResourceReference']]]):
    if resource_references is None:
      del self.resource_references
      return
    if not isinstance(resource_references, list):
      raise TypeError('resource_references must be of type list')
    if not all([isinstance(t, ResourceReference) for t in resource_references]):
      raise TypeError('resource_references must contain only items of type ResourceReference')
    self._resource_references = resource_references

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def total_results(self) -> int:
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results


class ResourceReference(KaggleObject):
  r"""
  ResourceReference Types

  Attributes:
    id (int)
    type (ResourceReferenceType)
    resource_identifier (str)
    owner_identifier (str)
    is_gated_resource (bool)
    publish_time (datetime)
    create_time (datetime)
    remove_time (datetime)
    content_state (ContentState)
    last_synced_version_identifier (str)
    last_synced_time (datetime)
    card_content (str)
    total_views (int)
    total_scripts (int)
    total_votes (int)
    last_modified_time (datetime)
    has_up_voted (bool)
  """

  def __init__(self):
    self._id = 0
    self._type = ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED
    self._resource_identifier = ""
    self._owner_identifier = None
    self._is_gated_resource = False
    self._publish_time = None
    self._create_time = None
    self._remove_time = None
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._last_synced_version_identifier = None
    self._last_synced_time = None
    self._card_content = ""
    self._total_views = 0
    self._total_scripts = 0
    self._total_votes = 0
    self._last_modified_time = None
    self._has_up_voted = False
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def type(self) -> 'ResourceReferenceType':
    return self._type

  @type.setter
  def type(self, type: 'ResourceReferenceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ResourceReferenceType):
      raise TypeError('type must be of type ResourceReferenceType')
    self._type = type

  @property
  def resource_identifier(self) -> str:
    return self._resource_identifier

  @resource_identifier.setter
  def resource_identifier(self, resource_identifier: str):
    if resource_identifier is None:
      del self.resource_identifier
      return
    if not isinstance(resource_identifier, str):
      raise TypeError('resource_identifier must be of type str')
    self._resource_identifier = resource_identifier

  @property
  def owner_identifier(self) -> str:
    return self._owner_identifier or ""

  @owner_identifier.setter
  def owner_identifier(self, owner_identifier: Optional[str]):
    if owner_identifier is None:
      del self.owner_identifier
      return
    if not isinstance(owner_identifier, str):
      raise TypeError('owner_identifier must be of type str')
    self._owner_identifier = owner_identifier

  @property
  def is_gated_resource(self) -> bool:
    return self._is_gated_resource

  @is_gated_resource.setter
  def is_gated_resource(self, is_gated_resource: bool):
    if is_gated_resource is None:
      del self.is_gated_resource
      return
    if not isinstance(is_gated_resource, bool):
      raise TypeError('is_gated_resource must be of type bool')
    self._is_gated_resource = is_gated_resource

  @property
  def publish_time(self) -> datetime:
    return self._publish_time or None

  @publish_time.setter
  def publish_time(self, publish_time: Optional[datetime]):
    if publish_time is None:
      del self.publish_time
      return
    if not isinstance(publish_time, datetime):
      raise TypeError('publish_time must be of type datetime')
    self._publish_time = publish_time

  @property
  def create_time(self) -> datetime:
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def remove_time(self) -> datetime:
    return self._remove_time or None

  @remove_time.setter
  def remove_time(self, remove_time: Optional[datetime]):
    if remove_time is None:
      del self.remove_time
      return
    if not isinstance(remove_time, datetime):
      raise TypeError('remove_time must be of type datetime')
    self._remove_time = remove_time

  @property
  def content_state(self) -> 'ContentState':
    return self._content_state

  @content_state.setter
  def content_state(self, content_state: 'ContentState'):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def last_synced_version_identifier(self) -> str:
    return self._last_synced_version_identifier or ""

  @last_synced_version_identifier.setter
  def last_synced_version_identifier(self, last_synced_version_identifier: Optional[str]):
    if last_synced_version_identifier is None:
      del self.last_synced_version_identifier
      return
    if not isinstance(last_synced_version_identifier, str):
      raise TypeError('last_synced_version_identifier must be of type str')
    self._last_synced_version_identifier = last_synced_version_identifier

  @property
  def last_synced_time(self) -> datetime:
    return self._last_synced_time or None

  @last_synced_time.setter
  def last_synced_time(self, last_synced_time: Optional[datetime]):
    if last_synced_time is None:
      del self.last_synced_time
      return
    if not isinstance(last_synced_time, datetime):
      raise TypeError('last_synced_time must be of type datetime')
    self._last_synced_time = last_synced_time

  @property
  def card_content(self) -> str:
    return self._card_content

  @card_content.setter
  def card_content(self, card_content: str):
    if card_content is None:
      del self.card_content
      return
    if not isinstance(card_content, str):
      raise TypeError('card_content must be of type str')
    self._card_content = card_content

  @property
  def total_views(self) -> int:
    return self._total_views

  @total_views.setter
  def total_views(self, total_views: int):
    if total_views is None:
      del self.total_views
      return
    if not isinstance(total_views, int):
      raise TypeError('total_views must be of type int')
    self._total_views = total_views

  @property
  def total_scripts(self) -> int:
    return self._total_scripts

  @total_scripts.setter
  def total_scripts(self, total_scripts: int):
    if total_scripts is None:
      del self.total_scripts
      return
    if not isinstance(total_scripts, int):
      raise TypeError('total_scripts must be of type int')
    self._total_scripts = total_scripts

  @property
  def total_votes(self) -> int:
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def last_modified_time(self) -> datetime:
    return self._last_modified_time or None

  @last_modified_time.setter
  def last_modified_time(self, last_modified_time: Optional[datetime]):
    if last_modified_time is None:
      del self.last_modified_time
      return
    if not isinstance(last_modified_time, datetime):
      raise TypeError('last_modified_time must be of type datetime')
    self._last_modified_time = last_modified_time

  @property
  def has_up_voted(self) -> bool:
    return self._has_up_voted

  @has_up_voted.setter
  def has_up_voted(self, has_up_voted: bool):
    if has_up_voted is None:
      del self.has_up_voted
      return
    if not isinstance(has_up_voted, bool):
      raise TypeError('has_up_voted must be of type bool')
    self._has_up_voted = has_up_voted


class ResourceReferenceIdentifier(KaggleObject):
  r"""
  Attributes:
    type (ResourceReferenceType)
    owner_identifier (str)
    resource_identifier (str)
  """

  def __init__(self):
    self._type = ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED
    self._owner_identifier = None
    self._resource_identifier = ""
    self._freeze()

  @property
  def type(self) -> 'ResourceReferenceType':
    return self._type

  @type.setter
  def type(self, type: 'ResourceReferenceType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ResourceReferenceType):
      raise TypeError('type must be of type ResourceReferenceType')
    self._type = type

  @property
  def owner_identifier(self) -> str:
    return self._owner_identifier or ""

  @owner_identifier.setter
  def owner_identifier(self, owner_identifier: Optional[str]):
    if owner_identifier is None:
      del self.owner_identifier
      return
    if not isinstance(owner_identifier, str):
      raise TypeError('owner_identifier must be of type str')
    self._owner_identifier = owner_identifier

  @property
  def resource_identifier(self) -> str:
    return self._resource_identifier

  @resource_identifier.setter
  def resource_identifier(self, resource_identifier: str):
    if resource_identifier is None:
      del self.resource_identifier
      return
    if not isinstance(resource_identifier, str):
      raise TypeError('resource_identifier must be of type str')
    self._resource_identifier = resource_identifier


class ResourceReferencesList(KaggleObject):
  r"""
  Attributes:
    total_count (int)
    resource_references (ResourceReference)
  """

  def __init__(self):
    self._total_count = None
    self._resource_references = []
    self._freeze()

  @property
  def total_count(self) -> int:
    return self._total_count or 0

  @total_count.setter
  def total_count(self, total_count: Optional[int]):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count

  @property
  def resource_references(self) -> Optional[List[Optional['ResourceReference']]]:
    return self._resource_references

  @resource_references.setter
  def resource_references(self, resource_references: Optional[List[Optional['ResourceReference']]]):
    if resource_references is None:
      del self.resource_references
      return
    if not isinstance(resource_references, list):
      raise TypeError('resource_references must be of type list')
    if not all([isinstance(t, ResourceReference) for t in resource_references]):
      raise TypeError('resource_references must contain only items of type ResourceReference')
    self._resource_references = resource_references


class SearchKernelIdsRequest(KaggleObject):
  r"""
  Attributes:
    search (str)
    list_request (ListKernelIdsRequest)
  """

  def __init__(self):
    self._search = None
    self._list_request = None
    self._freeze()

  @property
  def search(self) -> str:
    return self._search or ""

  @search.setter
  def search(self, search: Optional[str]):
    if search is None:
      del self.search
      return
    if not isinstance(search, str):
      raise TypeError('search must be of type str')
    self._search = search

  @property
  def list_request(self) -> Optional['ListKernelIdsRequest']:
    return self._list_request

  @list_request.setter
  def list_request(self, list_request: Optional['ListKernelIdsRequest']):
    if list_request is None:
      del self.list_request
      return
    if not isinstance(list_request, ListKernelIdsRequest):
      raise TypeError('list_request must be of type ListKernelIdsRequest')
    self._list_request = list_request


CreateKernelPinRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

CreateKernelPinResponse._fields = [
  FieldMetadata("kernelPinned", "kernel_pinned", "_kernel_pinned", bool, False, PredefinedSerializer()),
]

CreationSource._fields = [
  FieldMetadata("type", "type", "_type", CreationSourceType, CreationSourceType.CREATION_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

DataSource._fields = [
  FieldMetadata("reference", "reference", "_reference", DataSourceReference, None, KaggleObjectSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dataSourceUrl", "data_source_url", "_data_source_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("variationSlug", "variation_slug", "_variation_slug", str, None, PredefinedSerializer(), optional=True),
]

DataSourceReference._fields = [
  FieldMetadata("sourceType", "source_type", "_source_type", DataSourceType, DataSourceType.DATA_SOURCE_TYPE_COMPETITION, EnumSerializer()),
  FieldMetadata("sourceId", "source_id", "_source_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mountSlug", "mount_slug", "_mount_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isSourceIdPinned", "is_source_id_pinned", "_is_source_id_pinned", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

DeleteKernelPinRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

DeleteKernelPinResponse._fields = [
  FieldMetadata("kernelPinned", "kernel_pinned", "_kernel_pinned", bool, False, PredefinedSerializer()),
]

ForkParentInfo._fields = [
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("isVisible", "is_visible", "_is_visible", bool, False, PredefinedSerializer()),
  FieldMetadata("authorDisplayName", "author_display_name", "_author_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelUrl", "kernel_url", "_kernel_url", str, None, PredefinedSerializer(), optional=True),
]

GetKernelListDetailsRequest._fields = [
  FieldMetadata("kernelIds", "kernel_ids", "_kernel_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("unauthorizedAccessBehavior", "unauthorized_access_behavior", "_unauthorized_access_behavior", AccessBehavior, AccessBehavior.RETURN_SHELL_ENTRY, EnumSerializer()),
  FieldMetadata("deletedAccessBehavior", "deleted_access_behavior", "_deleted_access_behavior", AccessBehavior, AccessBehavior.RETURN_SHELL_ENTRY, EnumSerializer()),
  FieldMetadata("excludeResultsFilesOutputs", "exclude_results_files_outputs", "_exclude_results_files_outputs", bool, False, PredefinedSerializer()),
  FieldMetadata("wantOutputFiles", "want_output_files", "_want_output_files", bool, False, PredefinedSerializer()),
  FieldMetadata("outputFileTypes", "output_file_types", "_output_file_types", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("maxOutputFilesPerKernel", "max_output_files_per_kernel", "_max_output_files_per_kernel", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gcsTimeoutMs", "gcs_timeout_ms", "_gcs_timeout_ms", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("includeInvalidDataSources", "include_invalid_data_sources", "_include_invalid_data_sources", bool, False, PredefinedSerializer()),
]

KernelList._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernels", "kernels", "_kernels", KernelListItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("pinnedKernels", "pinned_kernels", "_pinned_kernels", KernelListItem, [], ListSerializer(KaggleObjectSerializer())),
]

KernelListItem._fields = [
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer()),
  FieldMetadata("currentUserHasVotedForThisScript", "current_user_has_voted_for_this_script", "_current_user_has_voted_for_this_script", bool, False, PredefinedSerializer()),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSource, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("forkDiffLinesChanged", "fork_diff_lines_changed", "_fork_diff_lines_changed", int, 0, PredefinedSerializer()),
  FieldMetadata("forkDiffLinesDeleted", "fork_diff_lines_deleted", "_fork_diff_lines_deleted", int, 0, PredefinedSerializer()),
  FieldMetadata("forkDiffLinesInserted", "fork_diff_lines_inserted", "_fork_diff_lines_inserted", int, 0, PredefinedSerializer()),
  FieldMetadata("forkDiffUrl", "fork_diff_url", "_fork_diff_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hasCollaborators", "has_collaborators", "_has_collaborators", bool, False, PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scriptVersionId", "script_version_id", "_script_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isFork", "is_fork", "_is_fork", bool, False, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("languageName", "language_name", "_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("aceLanguageName", "ace_language_name", "_ace_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isNotebook", "is_notebook", "_is_notebook", bool, False, PredefinedSerializer()),
  FieldMetadata("isGpuEnabled", "is_gpu_enabled", "_is_gpu_enabled", bool, False, PredefinedSerializer()),
  FieldMetadata("bestPublicScore", "best_public_score", "_best_public_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forumTopicId", "forum_topic_id", "_forum_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastRunExecutionTimeSeconds", "last_run_execution_time_seconds", "_last_run_execution_time_seconds", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("medal", "medal", "_medal", Medal, Medal.MEDAL_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("categories", "categories", "_categories", Category, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalComments", "total_comments", "_total_comments", int, 0, PredefinedSerializer()),
  FieldMetadata("totalForks", "total_forks", "_total_forks", int, 0, PredefinedSerializer()),
  FieldMetadata("totalScripts", "total_scripts", "_total_scripts", int, 0, PredefinedSerializer()),
  FieldMetadata("totalViews", "total_views", "_total_views", int, 0, PredefinedSerializer()),
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalLines", "total_lines", "_total_lines", int, 0, PredefinedSerializer()),
  FieldMetadata("currentUserHasBookmarked", "current_user_has_bookmarked", "_current_user_has_bookmarked", bool, False, PredefinedSerializer()),
  FieldMetadata("isRunning", "is_running", "_is_running", bool, False, PredefinedSerializer()),
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
  FieldMetadata("isMyUncommittedDraft", "is_my_uncommitted_draft", "_is_my_uncommitted_draft", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUrlSlug", "current_url_slug", "_current_url_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("scriptVersionDateCreated", "script_version_date_created", "_script_version_date_created", datetime, None, DateTimeSerializer()),
  FieldMetadata("dateEvaluated", "date_evaluated", "_date_evaluated", datetime, None, DateTimeSerializer()),
  FieldMetadata("outputFiles", "output_files", "_output_files", KernelSessionOutputFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("canCurrentUserDeleteKernel", "can_current_user_delete_kernel", "_can_current_user_delete_kernel", bool, False, PredefinedSerializer()),
  FieldMetadata("canCurrentUserEditKernel", "can_current_user_edit_kernel", "_can_current_user_edit_kernel", bool, False, PredefinedSerializer()),
  FieldMetadata("hasLinkedSubmission", "has_linked_submission", "_has_linked_submission", bool, False, PredefinedSerializer()),
  FieldMetadata("disableComments", "disable_comments", "_disable_comments", bool, False, PredefinedSerializer()),
  FieldMetadata("taskSubmissionInfo", "task_submission_info", "_task_submission_info", KernelTaskSubmissionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("forkParentInfo", "fork_parent_info", "_fork_parent_info", ForkParentInfo, None, KaggleObjectSerializer()),
  FieldMetadata("cardImageUrl", "card_image_url", "_card_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dateOutputToDatasetEnabled", "date_output_to_dataset_enabled", "_date_output_to_dataset_enabled", datetime, None, DateTimeSerializer()),
  FieldMetadata("lastRunTime", "last_run_time", "_last_run_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("scriptUrl", "script_url", "_script_url", str, "", PredefinedSerializer()),
  FieldMetadata("scriptCommentsUrl", "script_comments_url", "_script_comments_url", str, "", PredefinedSerializer()),
  FieldMetadata("scriptInputUrl", "script_input_url", "_script_input_url", str, "", PredefinedSerializer()),
  FieldMetadata("scriptEditUrl", "script_edit_url", "_script_edit_url", str, "", PredefinedSerializer()),
  FieldMetadata("hasDataOutputFiles", "has_data_output_files", "_has_data_output_files", bool, False, PredefinedSerializer()),
  FieldMetadata("dateOutputToModelEnabled", "date_output_to_model_enabled", "_date_output_to_model_enabled", datetime, None, DateTimeSerializer()),
]

KernelPinListItem._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

KernelSessionOutputFile._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("fullPath", "full_path", "_full_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileType", "file_type", "_file_type", str, None, PredefinedSerializer(), optional=True),
]

ListKernelIdsRequest._fields = [
  FieldMetadata("after", "after", "_after", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasourceType", "datasource_type", "_datasource_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forkParentScriptId", "fork_parent_script_id", "_fork_parent_script_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("group", "group", "_group", KernelsListViewType, KernelsListViewType.KERNELS_LIST_VIEW_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("kernelType", "kernel_type", "_kernel_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("language", "language", "_language", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputType", "output_type", "_output_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("excludeResultsFilesOutputs", "exclude_results_files_outputs", "_exclude_results_files_outputs", bool, False, PredefinedSerializer()),
  FieldMetadata("page", "page", "_page", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("sortBy", "sort_by", "_sort_by", KernelsListSortType, KernelsListSortType.HOTNESS, EnumSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tagIds", "tag_ids", "_tag_ids", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("wantOutputFiles", "want_output_files", "_want_output_files", bool, False, PredefinedSerializer()),
  FieldMetadata("hasGpuRun", "has_gpu_run", "_has_gpu_run", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privacy", "privacy", "_privacy", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("excludeKernelIds", "exclude_kernel_ids", "_exclude_kernel_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("modelInstanceIds", "model_instance_ids", "_model_instance_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("modelIds", "model_ids", "_model_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("excludeNonAccessedDatasources", "exclude_non_accessed_datasources", "_exclude_non_accessed_datasources", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resourceReferenceId", "resource_reference_id", "_resource_reference_id", int, None, PredefinedSerializer(), optional=True),
]

ListKernelPinsRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
]

ListKernelPinsResponse._fields = [
  FieldMetadata("kernelPins", "kernel_pins", "_kernel_pins", KernelPinListItem, [], ListSerializer(KaggleObjectSerializer())),
]

ListKernelsRequest._fields = [
  FieldMetadata("kernelFilterCriteria", "kernel_filter_criteria", "_kernel_filter_criteria", SearchKernelIdsRequest, None, KaggleObjectSerializer()),
  FieldMetadata("detailFilterCriteria", "detail_filter_criteria", "_detail_filter_criteria", GetKernelListDetailsRequest, None, KaggleObjectSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer(), optional=True),
]

ListResourceReferencesByIdsRequest._fields = [
  FieldMetadata("resourceReferenceIds", "resource_reference_ids", "_resource_reference_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListResourceReferencesFilter._fields = [
  FieldMetadata("type", "type", "_type", ResourceReferenceType, ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerIdentifier", "owner_identifier", "_owner_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("searchQuery", "search_query", "_search_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListResourceReferencesRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListResourceReferencesFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListResourceReferencesOrderBy, ListResourceReferencesOrderBy.LIST_RESOURCE_REFERENCES_ORDER_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
]

ListResourceReferencesResponse._fields = [
  FieldMetadata("resourceReferences", "resource_references", "_resource_references", ResourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
]

ResourceReference._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", ResourceReferenceType, ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("resourceIdentifier", "resource_identifier", "_resource_identifier", str, "", PredefinedSerializer()),
  FieldMetadata("ownerIdentifier", "owner_identifier", "_owner_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isGatedResource", "is_gated_resource", "_is_gated_resource", bool, False, PredefinedSerializer()),
  FieldMetadata("publishTime", "publish_time", "_publish_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("removeTime", "remove_time", "_remove_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastSyncedVersionIdentifier", "last_synced_version_identifier", "_last_synced_version_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastSyncedTime", "last_synced_time", "_last_synced_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("cardContent", "card_content", "_card_content", str, "", PredefinedSerializer()),
  FieldMetadata("totalViews", "total_views", "_total_views", int, 0, PredefinedSerializer()),
  FieldMetadata("totalScripts", "total_scripts", "_total_scripts", int, 0, PredefinedSerializer()),
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("lastModifiedTime", "last_modified_time", "_last_modified_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("hasUpVoted", "has_up_voted", "_has_up_voted", bool, False, PredefinedSerializer()),
]

ResourceReferenceIdentifier._fields = [
  FieldMetadata("type", "type", "_type", ResourceReferenceType, ResourceReferenceType.RESOURCE_REFERENCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerIdentifier", "owner_identifier", "_owner_identifier", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resourceIdentifier", "resource_identifier", "_resource_identifier", str, "", PredefinedSerializer()),
]

ResourceReferencesList._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resourceReferences", "resource_references", "_resource_references", ResourceReference, [], ListSerializer(KaggleObjectSerializer())),
]

SearchKernelIdsRequest._fields = [
  FieldMetadata("search", "search", "_search", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("listRequest", "list_request", "_list_request", ListKernelIdsRequest, None, KaggleObjectSerializer()),
]

