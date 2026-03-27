from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.common_types import Image
from kagglesdk.common.types.vote import VoteButton
from kagglesdk.datasets.databundles.types.databundle_enums import ExtendedDataType, HarmonizedDataType
from kagglesdk.datasets.types.dataset_enums import DatabundleDiffType, DatabundleVersionType, DatasetFileType, FeedbackState, FeedbackType, MetadataSuggestionType, RemoteUrlUpdateFrequency, SuggestionBundleState, SuggestionState
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import LicenseOption
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import CollaboratorType, UserAchievementTier
from typing import Optional, List

class DatasetTab(enum.Enum):
  DATA = 0
  DATA_OLD = 1
  KERNELS = 2
  NOTEBOOKS = 3
  CODE = 4
  DISCUSSION = 5
  ACTIVITY = 6
  METADATA = 7
  SETTINGS = 8
  TASKS = 9
  HOME = 10
  ADMIN = 11
  SUGGESTIONS = 12

class ActionFlags(KaggleObject):
  r"""
  Attributes:
    disable_worker (bool)
    disable_bundle_creation (bool)
    disable_individual_zip_creation (bool)
    disable_raw_upload (bool)
    disable_metadata (bool)
    disable_status (bool)
    disable_status_pub_sub (bool)
    disable_final_result (bool)
    disable_embedded_filesystem (bool)
    disable_decompression (bool)
    disable_directory_zip_creation (bool)
    use_standalone_zipper_for_bundle (bool)
    reuse_original_single_gcs_zip (bool)
      If the user uploaded a single zip file, then we can just use this as the
      bundle.zip. This flag enables that functionality.
    gcs_upload_url (str)
      Use this path instead of the upload path to copy files from.
    spread_csv_sample_rows (bool)
    ignore_missing_gcs_files (bool)
    reduced_watchdog_processing (bool)
    no_single_producer_constrained (bool)
    disable_worker_auto_ack (bool)
    apply_backpressure_when_zipping (bool)
    create_croissant_after_zipping (bool)
    stream_gcs_list_results (bool)
    gcs_filter_glob_pattern (str)
      This value will be used when the worker pulls files from GCS. As a result,
      this will only be used on GCS-based DatabundleVersionTypes: FileSet,
      GcsFileSet, and KernelOutputFileSet. This is currently not exposed to end
      users and provides a workaround for Competitions to specify a subset of
      files from a KernelOutputFileSet. It is mostly untested, so use at your own
      discretion. Link to GCS docs describing syntax:
      https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob
    disable_metrics_calculation (bool)
    enable_copy_in_the_cloud_block (bool)
    enable_copy_in_the_cloud_logging (bool)
    enable_parquet_support (bool)
    is_competition_rerun_dataset (bool)
      This databundle has been identified as part of the Competition team's
      workaround of using Datasets for uploading rerun databundles. In this case
      the DatabundleType will remain Dataset, but the presence of this flag
      indicates that certain parts of databundle processing should be treated as
      a DatabundleType.Competition (e.g. skipping parquet file processing). See
      b/427847808 for follow up.
  """

  def __init__(self):
    self._disable_worker = False
    self._disable_bundle_creation = False
    self._disable_individual_zip_creation = False
    self._disable_raw_upload = False
    self._disable_metadata = False
    self._disable_status = False
    self._disable_status_pub_sub = False
    self._disable_final_result = False
    self._disable_embedded_filesystem = False
    self._disable_decompression = False
    self._disable_directory_zip_creation = False
    self._use_standalone_zipper_for_bundle = False
    self._reuse_original_single_gcs_zip = False
    self._gcs_upload_url = None
    self._spread_csv_sample_rows = None
    self._ignore_missing_gcs_files = None
    self._reduced_watchdog_processing = None
    self._no_single_producer_constrained = None
    self._disable_worker_auto_ack = None
    self._apply_backpressure_when_zipping = None
    self._create_croissant_after_zipping = None
    self._stream_gcs_list_results = None
    self._gcs_filter_glob_pattern = None
    self._disable_metrics_calculation = None
    self._enable_copy_in_the_cloud_block = None
    self._enable_copy_in_the_cloud_logging = None
    self._enable_parquet_support = None
    self._is_competition_rerun_dataset = None
    self._freeze()

  @property
  def disable_worker(self) -> bool:
    return self._disable_worker

  @disable_worker.setter
  def disable_worker(self, disable_worker: bool):
    if disable_worker is None:
      del self.disable_worker
      return
    if not isinstance(disable_worker, bool):
      raise TypeError('disable_worker must be of type bool')
    self._disable_worker = disable_worker

  @property
  def disable_bundle_creation(self) -> bool:
    return self._disable_bundle_creation

  @disable_bundle_creation.setter
  def disable_bundle_creation(self, disable_bundle_creation: bool):
    if disable_bundle_creation is None:
      del self.disable_bundle_creation
      return
    if not isinstance(disable_bundle_creation, bool):
      raise TypeError('disable_bundle_creation must be of type bool')
    self._disable_bundle_creation = disable_bundle_creation

  @property
  def disable_individual_zip_creation(self) -> bool:
    return self._disable_individual_zip_creation

  @disable_individual_zip_creation.setter
  def disable_individual_zip_creation(self, disable_individual_zip_creation: bool):
    if disable_individual_zip_creation is None:
      del self.disable_individual_zip_creation
      return
    if not isinstance(disable_individual_zip_creation, bool):
      raise TypeError('disable_individual_zip_creation must be of type bool')
    self._disable_individual_zip_creation = disable_individual_zip_creation

  @property
  def disable_raw_upload(self) -> bool:
    return self._disable_raw_upload

  @disable_raw_upload.setter
  def disable_raw_upload(self, disable_raw_upload: bool):
    if disable_raw_upload is None:
      del self.disable_raw_upload
      return
    if not isinstance(disable_raw_upload, bool):
      raise TypeError('disable_raw_upload must be of type bool')
    self._disable_raw_upload = disable_raw_upload

  @property
  def disable_metadata(self) -> bool:
    return self._disable_metadata

  @disable_metadata.setter
  def disable_metadata(self, disable_metadata: bool):
    if disable_metadata is None:
      del self.disable_metadata
      return
    if not isinstance(disable_metadata, bool):
      raise TypeError('disable_metadata must be of type bool')
    self._disable_metadata = disable_metadata

  @property
  def disable_status(self) -> bool:
    return self._disable_status

  @disable_status.setter
  def disable_status(self, disable_status: bool):
    if disable_status is None:
      del self.disable_status
      return
    if not isinstance(disable_status, bool):
      raise TypeError('disable_status must be of type bool')
    self._disable_status = disable_status

  @property
  def disable_status_pub_sub(self) -> bool:
    return self._disable_status_pub_sub

  @disable_status_pub_sub.setter
  def disable_status_pub_sub(self, disable_status_pub_sub: bool):
    if disable_status_pub_sub is None:
      del self.disable_status_pub_sub
      return
    if not isinstance(disable_status_pub_sub, bool):
      raise TypeError('disable_status_pub_sub must be of type bool')
    self._disable_status_pub_sub = disable_status_pub_sub

  @property
  def disable_final_result(self) -> bool:
    return self._disable_final_result

  @disable_final_result.setter
  def disable_final_result(self, disable_final_result: bool):
    if disable_final_result is None:
      del self.disable_final_result
      return
    if not isinstance(disable_final_result, bool):
      raise TypeError('disable_final_result must be of type bool')
    self._disable_final_result = disable_final_result

  @property
  def disable_embedded_filesystem(self) -> bool:
    return self._disable_embedded_filesystem

  @disable_embedded_filesystem.setter
  def disable_embedded_filesystem(self, disable_embedded_filesystem: bool):
    if disable_embedded_filesystem is None:
      del self.disable_embedded_filesystem
      return
    if not isinstance(disable_embedded_filesystem, bool):
      raise TypeError('disable_embedded_filesystem must be of type bool')
    self._disable_embedded_filesystem = disable_embedded_filesystem

  @property
  def disable_decompression(self) -> bool:
    return self._disable_decompression

  @disable_decompression.setter
  def disable_decompression(self, disable_decompression: bool):
    if disable_decompression is None:
      del self.disable_decompression
      return
    if not isinstance(disable_decompression, bool):
      raise TypeError('disable_decompression must be of type bool')
    self._disable_decompression = disable_decompression

  @property
  def disable_directory_zip_creation(self) -> bool:
    return self._disable_directory_zip_creation

  @disable_directory_zip_creation.setter
  def disable_directory_zip_creation(self, disable_directory_zip_creation: bool):
    if disable_directory_zip_creation is None:
      del self.disable_directory_zip_creation
      return
    if not isinstance(disable_directory_zip_creation, bool):
      raise TypeError('disable_directory_zip_creation must be of type bool')
    self._disable_directory_zip_creation = disable_directory_zip_creation

  @property
  def use_standalone_zipper_for_bundle(self) -> bool:
    return self._use_standalone_zipper_for_bundle

  @use_standalone_zipper_for_bundle.setter
  def use_standalone_zipper_for_bundle(self, use_standalone_zipper_for_bundle: bool):
    if use_standalone_zipper_for_bundle is None:
      del self.use_standalone_zipper_for_bundle
      return
    if not isinstance(use_standalone_zipper_for_bundle, bool):
      raise TypeError('use_standalone_zipper_for_bundle must be of type bool')
    self._use_standalone_zipper_for_bundle = use_standalone_zipper_for_bundle

  @property
  def reuse_original_single_gcs_zip(self) -> bool:
    r"""
    If the user uploaded a single zip file, then we can just use this as the
    bundle.zip. This flag enables that functionality.
    """
    return self._reuse_original_single_gcs_zip

  @reuse_original_single_gcs_zip.setter
  def reuse_original_single_gcs_zip(self, reuse_original_single_gcs_zip: bool):
    if reuse_original_single_gcs_zip is None:
      del self.reuse_original_single_gcs_zip
      return
    if not isinstance(reuse_original_single_gcs_zip, bool):
      raise TypeError('reuse_original_single_gcs_zip must be of type bool')
    self._reuse_original_single_gcs_zip = reuse_original_single_gcs_zip

  @property
  def gcs_upload_url(self) -> str:
    """Use this path instead of the upload path to copy files from."""
    return self._gcs_upload_url or ""

  @gcs_upload_url.setter
  def gcs_upload_url(self, gcs_upload_url: Optional[str]):
    if gcs_upload_url is None:
      del self.gcs_upload_url
      return
    if not isinstance(gcs_upload_url, str):
      raise TypeError('gcs_upload_url must be of type str')
    self._gcs_upload_url = gcs_upload_url

  @property
  def spread_csv_sample_rows(self) -> bool:
    return self._spread_csv_sample_rows or False

  @spread_csv_sample_rows.setter
  def spread_csv_sample_rows(self, spread_csv_sample_rows: Optional[bool]):
    if spread_csv_sample_rows is None:
      del self.spread_csv_sample_rows
      return
    if not isinstance(spread_csv_sample_rows, bool):
      raise TypeError('spread_csv_sample_rows must be of type bool')
    self._spread_csv_sample_rows = spread_csv_sample_rows

  @property
  def ignore_missing_gcs_files(self) -> bool:
    return self._ignore_missing_gcs_files or False

  @ignore_missing_gcs_files.setter
  def ignore_missing_gcs_files(self, ignore_missing_gcs_files: Optional[bool]):
    if ignore_missing_gcs_files is None:
      del self.ignore_missing_gcs_files
      return
    if not isinstance(ignore_missing_gcs_files, bool):
      raise TypeError('ignore_missing_gcs_files must be of type bool')
    self._ignore_missing_gcs_files = ignore_missing_gcs_files

  @property
  def reduced_watchdog_processing(self) -> bool:
    return self._reduced_watchdog_processing or False

  @reduced_watchdog_processing.setter
  def reduced_watchdog_processing(self, reduced_watchdog_processing: Optional[bool]):
    if reduced_watchdog_processing is None:
      del self.reduced_watchdog_processing
      return
    if not isinstance(reduced_watchdog_processing, bool):
      raise TypeError('reduced_watchdog_processing must be of type bool')
    self._reduced_watchdog_processing = reduced_watchdog_processing

  @property
  def no_single_producer_constrained(self) -> bool:
    return self._no_single_producer_constrained or False

  @no_single_producer_constrained.setter
  def no_single_producer_constrained(self, no_single_producer_constrained: Optional[bool]):
    if no_single_producer_constrained is None:
      del self.no_single_producer_constrained
      return
    if not isinstance(no_single_producer_constrained, bool):
      raise TypeError('no_single_producer_constrained must be of type bool')
    self._no_single_producer_constrained = no_single_producer_constrained

  @property
  def disable_worker_auto_ack(self) -> bool:
    return self._disable_worker_auto_ack or False

  @disable_worker_auto_ack.setter
  def disable_worker_auto_ack(self, disable_worker_auto_ack: Optional[bool]):
    if disable_worker_auto_ack is None:
      del self.disable_worker_auto_ack
      return
    if not isinstance(disable_worker_auto_ack, bool):
      raise TypeError('disable_worker_auto_ack must be of type bool')
    self._disable_worker_auto_ack = disable_worker_auto_ack

  @property
  def apply_backpressure_when_zipping(self) -> bool:
    return self._apply_backpressure_when_zipping or False

  @apply_backpressure_when_zipping.setter
  def apply_backpressure_when_zipping(self, apply_backpressure_when_zipping: Optional[bool]):
    if apply_backpressure_when_zipping is None:
      del self.apply_backpressure_when_zipping
      return
    if not isinstance(apply_backpressure_when_zipping, bool):
      raise TypeError('apply_backpressure_when_zipping must be of type bool')
    self._apply_backpressure_when_zipping = apply_backpressure_when_zipping

  @property
  def create_croissant_after_zipping(self) -> bool:
    return self._create_croissant_after_zipping or False

  @create_croissant_after_zipping.setter
  def create_croissant_after_zipping(self, create_croissant_after_zipping: Optional[bool]):
    if create_croissant_after_zipping is None:
      del self.create_croissant_after_zipping
      return
    if not isinstance(create_croissant_after_zipping, bool):
      raise TypeError('create_croissant_after_zipping must be of type bool')
    self._create_croissant_after_zipping = create_croissant_after_zipping

  @property
  def stream_gcs_list_results(self) -> bool:
    return self._stream_gcs_list_results or False

  @stream_gcs_list_results.setter
  def stream_gcs_list_results(self, stream_gcs_list_results: Optional[bool]):
    if stream_gcs_list_results is None:
      del self.stream_gcs_list_results
      return
    if not isinstance(stream_gcs_list_results, bool):
      raise TypeError('stream_gcs_list_results must be of type bool')
    self._stream_gcs_list_results = stream_gcs_list_results

  @property
  def gcs_filter_glob_pattern(self) -> str:
    r"""
    This value will be used when the worker pulls files from GCS. As a result,
    this will only be used on GCS-based DatabundleVersionTypes: FileSet,
    GcsFileSet, and KernelOutputFileSet. This is currently not exposed to end
    users and provides a workaround for Competitions to specify a subset of
    files from a KernelOutputFileSet. It is mostly untested, so use at your own
    discretion. Link to GCS docs describing syntax:
    https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob
    """
    return self._gcs_filter_glob_pattern or ""

  @gcs_filter_glob_pattern.setter
  def gcs_filter_glob_pattern(self, gcs_filter_glob_pattern: Optional[str]):
    if gcs_filter_glob_pattern is None:
      del self.gcs_filter_glob_pattern
      return
    if not isinstance(gcs_filter_glob_pattern, str):
      raise TypeError('gcs_filter_glob_pattern must be of type str')
    self._gcs_filter_glob_pattern = gcs_filter_glob_pattern

  @property
  def disable_metrics_calculation(self) -> bool:
    return self._disable_metrics_calculation or False

  @disable_metrics_calculation.setter
  def disable_metrics_calculation(self, disable_metrics_calculation: Optional[bool]):
    if disable_metrics_calculation is None:
      del self.disable_metrics_calculation
      return
    if not isinstance(disable_metrics_calculation, bool):
      raise TypeError('disable_metrics_calculation must be of type bool')
    self._disable_metrics_calculation = disable_metrics_calculation

  @property
  def enable_copy_in_the_cloud_block(self) -> bool:
    return self._enable_copy_in_the_cloud_block or False

  @enable_copy_in_the_cloud_block.setter
  def enable_copy_in_the_cloud_block(self, enable_copy_in_the_cloud_block: Optional[bool]):
    if enable_copy_in_the_cloud_block is None:
      del self.enable_copy_in_the_cloud_block
      return
    if not isinstance(enable_copy_in_the_cloud_block, bool):
      raise TypeError('enable_copy_in_the_cloud_block must be of type bool')
    self._enable_copy_in_the_cloud_block = enable_copy_in_the_cloud_block

  @property
  def enable_copy_in_the_cloud_logging(self) -> bool:
    return self._enable_copy_in_the_cloud_logging or False

  @enable_copy_in_the_cloud_logging.setter
  def enable_copy_in_the_cloud_logging(self, enable_copy_in_the_cloud_logging: Optional[bool]):
    if enable_copy_in_the_cloud_logging is None:
      del self.enable_copy_in_the_cloud_logging
      return
    if not isinstance(enable_copy_in_the_cloud_logging, bool):
      raise TypeError('enable_copy_in_the_cloud_logging must be of type bool')
    self._enable_copy_in_the_cloud_logging = enable_copy_in_the_cloud_logging

  @property
  def enable_parquet_support(self) -> bool:
    return self._enable_parquet_support or False

  @enable_parquet_support.setter
  def enable_parquet_support(self, enable_parquet_support: Optional[bool]):
    if enable_parquet_support is None:
      del self.enable_parquet_support
      return
    if not isinstance(enable_parquet_support, bool):
      raise TypeError('enable_parquet_support must be of type bool')
    self._enable_parquet_support = enable_parquet_support

  @property
  def is_competition_rerun_dataset(self) -> bool:
    r"""
    This databundle has been identified as part of the Competition team's
    workaround of using Datasets for uploading rerun databundles. In this case
    the DatabundleType will remain Dataset, but the presence of this flag
    indicates that certain parts of databundle processing should be treated as
    a DatabundleType.Competition (e.g. skipping parquet file processing). See
    b/427847808 for follow up.
    """
    return self._is_competition_rerun_dataset or False

  @is_competition_rerun_dataset.setter
  def is_competition_rerun_dataset(self, is_competition_rerun_dataset: Optional[bool]):
    if is_competition_rerun_dataset is None:
      del self.is_competition_rerun_dataset
      return
    if not isinstance(is_competition_rerun_dataset, bool):
      raise TypeError('is_competition_rerun_dataset must be of type bool')
    self._is_competition_rerun_dataset = is_competition_rerun_dataset


class Citation(KaggleObject):
  r"""
  Attributes:
    id (int)
    title (str)
      Citation Title
    url (str)
      Citation link
  """

  def __init__(self):
    self._id = None
    self._title = None
    self._url = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def title(self) -> str:
    """Citation Title"""
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
  def url(self) -> str:
    """Citation link"""
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class DatabundleInfo(KaggleObject):
  r"""
  Attributes:
    total_size (int)
    is_fileset (bool)
    can_download (bool)
    firestore_path (str)
    download_url (str)
    version_id (int)
    id (int)
    type (DatabundleVersionType)
    last_version_id (int)
    file_extensions (str)
  """

  def __init__(self):
    self._total_size = 0
    self._is_fileset = False
    self._can_download = False
    self._firestore_path = ""
    self._download_url = ""
    self._version_id = 0
    self._id = 0
    self._type = DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED
    self._last_version_id = 0
    self._file_extensions = []
    self._freeze()

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

  @property
  def is_fileset(self) -> bool:
    return self._is_fileset

  @is_fileset.setter
  def is_fileset(self, is_fileset: bool):
    if is_fileset is None:
      del self.is_fileset
      return
    if not isinstance(is_fileset, bool):
      raise TypeError('is_fileset must be of type bool')
    self._is_fileset = is_fileset

  @property
  def can_download(self) -> bool:
    return self._can_download

  @can_download.setter
  def can_download(self, can_download: bool):
    if can_download is None:
      del self.can_download
      return
    if not isinstance(can_download, bool):
      raise TypeError('can_download must be of type bool')
    self._can_download = can_download

  @property
  def firestore_path(self) -> str:
    return self._firestore_path

  @firestore_path.setter
  def firestore_path(self, firestore_path: str):
    if firestore_path is None:
      del self.firestore_path
      return
    if not isinstance(firestore_path, str):
      raise TypeError('firestore_path must be of type str')
    self._firestore_path = firestore_path

  @property
  def download_url(self) -> str:
    return self._download_url

  @download_url.setter
  def download_url(self, download_url: str):
    if download_url is None:
      del self.download_url
      return
    if not isinstance(download_url, str):
      raise TypeError('download_url must be of type str')
    self._download_url = download_url

  @property
  def version_id(self) -> int:
    return self._version_id

  @version_id.setter
  def version_id(self, version_id: int):
    if version_id is None:
      del self.version_id
      return
    if not isinstance(version_id, int):
      raise TypeError('version_id must be of type int')
    self._version_id = version_id

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
  def type(self) -> 'DatabundleVersionType':
    return self._type

  @type.setter
  def type(self, type: 'DatabundleVersionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DatabundleVersionType):
      raise TypeError('type must be of type DatabundleVersionType')
    self._type = type

  @property
  def last_version_id(self) -> int:
    return self._last_version_id

  @last_version_id.setter
  def last_version_id(self, last_version_id: int):
    if last_version_id is None:
      del self.last_version_id
      return
    if not isinstance(last_version_id, int):
      raise TypeError('last_version_id must be of type int')
    self._last_version_id = last_version_id

  @property
  def file_extensions(self) -> Optional[List[str]]:
    return self._file_extensions

  @file_extensions.setter
  def file_extensions(self, file_extensions: Optional[List[str]]):
    if file_extensions is None:
      del self.file_extensions
      return
    if not isinstance(file_extensions, list):
      raise TypeError('file_extensions must be of type list')
    if not all([isinstance(t, str) for t in file_extensions]):
      raise TypeError('file_extensions must contain only items of type str')
    self._file_extensions = file_extensions


class DataCoverageAttribute(KaggleObject):
  r"""
  Data coverage that encompasses both temporal and spatial information.

  Attributes:
    temporal_coverage_from (datetime)
    temporal_coverage_to (datetime)
    spatial_coverage (str)
  """

  def __init__(self):
    self._temporal_coverage_from = None
    self._temporal_coverage_to = None
    self._spatial_coverage = None
    self._freeze()

  @property
  def temporal_coverage_from(self) -> datetime:
    return self._temporal_coverage_from

  @temporal_coverage_from.setter
  def temporal_coverage_from(self, temporal_coverage_from: datetime):
    if temporal_coverage_from is None:
      del self.temporal_coverage_from
      return
    if not isinstance(temporal_coverage_from, datetime):
      raise TypeError('temporal_coverage_from must be of type datetime')
    self._temporal_coverage_from = temporal_coverage_from

  @property
  def temporal_coverage_to(self) -> datetime:
    return self._temporal_coverage_to

  @temporal_coverage_to.setter
  def temporal_coverage_to(self, temporal_coverage_to: datetime):
    if temporal_coverage_to is None:
      del self.temporal_coverage_to
      return
    if not isinstance(temporal_coverage_to, datetime):
      raise TypeError('temporal_coverage_to must be of type datetime')
    self._temporal_coverage_to = temporal_coverage_to

  @property
  def spatial_coverage(self) -> str:
    return self._spatial_coverage or ""

  @spatial_coverage.setter
  def spatial_coverage(self, spatial_coverage: Optional[str]):
    if spatial_coverage is None:
      del self.spatial_coverage
      return
    if not isinstance(spatial_coverage, str):
      raise TypeError('spatial_coverage must be of type str')
    self._spatial_coverage = spatial_coverage


class DatasetActivityPageDiscussion(KaggleObject):
  r"""
  Attributes:
    id (int)
    vote_button_dto (VoteButton)
    avatar (UserAvatar)
    medal (Image)
    title (str)
    time_since_last_activity (str)
    reply_count (int)
    url (str)
  """

  def __init__(self):
    self._id = 0
    self._vote_button_dto = None
    self._avatar = None
    self._medal = None
    self._title = None
    self._time_since_last_activity = None
    self._reply_count = 0
    self._url = None
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
  def vote_button_dto(self) -> Optional['VoteButton']:
    return self._vote_button_dto

  @vote_button_dto.setter
  def vote_button_dto(self, vote_button_dto: Optional['VoteButton']):
    if vote_button_dto is None:
      del self.vote_button_dto
      return
    if not isinstance(vote_button_dto, VoteButton):
      raise TypeError('vote_button_dto must be of type VoteButton')
    self._vote_button_dto = vote_button_dto

  @property
  def avatar(self) -> Optional['UserAvatar']:
    return self._avatar

  @avatar.setter
  def avatar(self, avatar: Optional['UserAvatar']):
    if avatar is None:
      del self.avatar
      return
    if not isinstance(avatar, UserAvatar):
      raise TypeError('avatar must be of type UserAvatar')
    self._avatar = avatar

  @property
  def medal(self) -> Optional['Image']:
    return self._medal

  @medal.setter
  def medal(self, medal: Optional['Image']):
    if medal is None:
      del self.medal
      return
    if not isinstance(medal, Image):
      raise TypeError('medal must be of type Image')
    self._medal = medal

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
  def time_since_last_activity(self) -> str:
    return self._time_since_last_activity or ""

  @time_since_last_activity.setter
  def time_since_last_activity(self, time_since_last_activity: Optional[str]):
    if time_since_last_activity is None:
      del self.time_since_last_activity
      return
    if not isinstance(time_since_last_activity, str):
      raise TypeError('time_since_last_activity must be of type str')
    self._time_since_last_activity = time_since_last_activity

  @property
  def reply_count(self) -> int:
    return self._reply_count

  @reply_count.setter
  def reply_count(self, reply_count: int):
    if reply_count is None:
      del self.reply_count
      return
    if not isinstance(reply_count, int):
      raise TypeError('reply_count must be of type int')
    self._reply_count = reply_count

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class DatasetAdminSettingsInfo(KaggleObject):
  r"""
  Attributes:
    maintainer_organization (Owner)
    slug (str)
  """

  def __init__(self):
    self._maintainer_organization = None
    self._slug = ""
    self._freeze()

  @property
  def maintainer_organization(self) -> Optional['Owner']:
    return self._maintainer_organization

  @maintainer_organization.setter
  def maintainer_organization(self, maintainer_organization: Optional['Owner']):
    if maintainer_organization is None:
      del self.maintainer_organization
      return
    if not isinstance(maintainer_organization, Owner):
      raise TypeError('maintainer_organization must be of type Owner')
    self._maintainer_organization = maintainer_organization

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug


class DatasetCollaborator(KaggleObject):
  r"""
  Attributes:
    username (str)
    group_slug (str)
    role (CollaboratorType)
  """

  def __init__(self):
    self._username = None
    self._group_slug = None
    self._role = CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def username(self) -> str:
    return self._username or ""

  @username.setter
  def username(self, username: str):
    if username is None:
      del self.username
      return
    if not isinstance(username, str):
      raise TypeError('username must be of type str')
    del self.group_slug
    self._username = username

  @property
  def group_slug(self) -> str:
    return self._group_slug or ""

  @group_slug.setter
  def group_slug(self, group_slug: str):
    if group_slug is None:
      del self.group_slug
      return
    if not isinstance(group_slug, str):
      raise TypeError('group_slug must be of type str')
    del self.username
    self._group_slug = group_slug

  @property
  def role(self) -> 'CollaboratorType':
    return self._role

  @role.setter
  def role(self, role: 'CollaboratorType'):
    if role is None:
      del self.role
      return
    if not isinstance(role, CollaboratorType):
      raise TypeError('role must be of type CollaboratorType')
    self._role = role


class DatasetCroissantInfo(KaggleObject):
  r"""
  Attributes:
    auto_gen_croissant_download_url (str)
    can_download_auto_gen_croissant (bool)
    auto_gen_croissant_total_size (int)
  """

  def __init__(self):
    self._auto_gen_croissant_download_url = ""
    self._can_download_auto_gen_croissant = False
    self._auto_gen_croissant_total_size = None
    self._freeze()

  @property
  def auto_gen_croissant_download_url(self) -> str:
    return self._auto_gen_croissant_download_url

  @auto_gen_croissant_download_url.setter
  def auto_gen_croissant_download_url(self, auto_gen_croissant_download_url: str):
    if auto_gen_croissant_download_url is None:
      del self.auto_gen_croissant_download_url
      return
    if not isinstance(auto_gen_croissant_download_url, str):
      raise TypeError('auto_gen_croissant_download_url must be of type str')
    self._auto_gen_croissant_download_url = auto_gen_croissant_download_url

  @property
  def can_download_auto_gen_croissant(self) -> bool:
    return self._can_download_auto_gen_croissant

  @can_download_auto_gen_croissant.setter
  def can_download_auto_gen_croissant(self, can_download_auto_gen_croissant: bool):
    if can_download_auto_gen_croissant is None:
      del self.can_download_auto_gen_croissant
      return
    if not isinstance(can_download_auto_gen_croissant, bool):
      raise TypeError('can_download_auto_gen_croissant must be of type bool')
    self._can_download_auto_gen_croissant = can_download_auto_gen_croissant

  @property
  def auto_gen_croissant_total_size(self) -> int:
    return self._auto_gen_croissant_total_size or 0

  @auto_gen_croissant_total_size.setter
  def auto_gen_croissant_total_size(self, auto_gen_croissant_total_size: Optional[int]):
    if auto_gen_croissant_total_size is None:
      del self.auto_gen_croissant_total_size
      return
    if not isinstance(auto_gen_croissant_total_size, int):
      raise TypeError('auto_gen_croissant_total_size must be of type int')
    self._auto_gen_croissant_total_size = auto_gen_croissant_total_size


class DatasetDatasourceListItem(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    current_dataset_version_id (int)
    current_dataset_version_number (int)
    type (DatabundleVersionType)
    diff_type (DatabundleDiffType)
    title (str)
    overview (str)
    thumbnail_image_url (str)
    is_private (bool)
    is_deleted (bool)
  """

  def __init__(self):
    self._dataset_id = 0
    self._current_dataset_version_id = 0
    self._current_dataset_version_number = None
    self._type = DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED
    self._diff_type = DatabundleDiffType.REALTIME
    self._title = None
    self._overview = None
    self._thumbnail_image_url = None
    self._is_private = False
    self._is_deleted = False
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
  def current_dataset_version_number(self) -> int:
    return self._current_dataset_version_number or 0

  @current_dataset_version_number.setter
  def current_dataset_version_number(self, current_dataset_version_number: Optional[int]):
    if current_dataset_version_number is None:
      del self.current_dataset_version_number
      return
    if not isinstance(current_dataset_version_number, int):
      raise TypeError('current_dataset_version_number must be of type int')
    self._current_dataset_version_number = current_dataset_version_number

  @property
  def type(self) -> 'DatabundleVersionType':
    return self._type

  @type.setter
  def type(self, type: 'DatabundleVersionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DatabundleVersionType):
      raise TypeError('type must be of type DatabundleVersionType')
    self._type = type

  @property
  def diff_type(self) -> 'DatabundleDiffType':
    return self._diff_type

  @diff_type.setter
  def diff_type(self, diff_type: 'DatabundleDiffType'):
    if diff_type is None:
      del self.diff_type
      return
    if not isinstance(diff_type, DatabundleDiffType):
      raise TypeError('diff_type must be of type DatabundleDiffType')
    self._diff_type = diff_type

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
  def overview(self) -> str:
    return self._overview or ""

  @overview.setter
  def overview(self, overview: Optional[str]):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def thumbnail_image_url(self) -> str:
    return self._thumbnail_image_url or ""

  @thumbnail_image_url.setter
  def thumbnail_image_url(self, thumbnail_image_url: Optional[str]):
    if thumbnail_image_url is None:
      del self.thumbnail_image_url
      return
    if not isinstance(thumbnail_image_url, str):
      raise TypeError('thumbnail_image_url must be of type str')
    self._thumbnail_image_url = thumbnail_image_url

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


class DatasetFeedbackInfo(KaggleObject):
  r"""
  Attributes:
    id (int)
    name (str)
    count (int)
    state (FeedbackState)
    type (FeedbackType)
  """

  def __init__(self):
    self._id = 0
    self._name = ""
    self._count = 0
    self._state = FeedbackState.FEEDBACK_STATE_UNSPECIFIED
    self._type = FeedbackType.FEEDBACK_TYPE_UNSPECIFIED
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
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def state(self) -> 'FeedbackState':
    return self._state

  @state.setter
  def state(self, state: 'FeedbackState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, FeedbackState):
      raise TypeError('state must be of type FeedbackState')
    self._state = state

  @property
  def type(self) -> 'FeedbackType':
    return self._type

  @type.setter
  def type(self, type: 'FeedbackType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, FeedbackType):
      raise TypeError('type must be of type FeedbackType')
    self._type = type


class DatasetFileSummary(KaggleObject):
  r"""
  Attributes:
    file_type (DatasetFileType)
    count (int)
    total_size (int)
  """

  def __init__(self):
    self._file_type = DatasetFileType.DATASET_FILE_TYPE_UNSPECIFIED
    self._count = 0
    self._total_size = 0
    self._freeze()

  @property
  def file_type(self) -> 'DatasetFileType':
    return self._file_type

  @file_type.setter
  def file_type(self, file_type: 'DatasetFileType'):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, DatasetFileType):
      raise TypeError('file_type must be of type DatasetFileType')
    self._file_type = file_type

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size


class DatasetGeneralUpdatableInfo(KaggleObject):
  r"""
  Attributes:
    title (str)
    overview (str)
    license_id (int)
    owner (OwnerDto)
    diff_type (DatabundleDiffType)
    update_frequency (RemoteUrlUpdateFrequency)
    block_task_creation (bool)
    suggestions_enabled (bool)
  """

  def __init__(self):
    self._title = None
    self._overview = None
    self._license_id = None
    self._owner = None
    self._diff_type = None
    self._update_frequency = None
    self._block_task_creation = None
    self._suggestions_enabled = None
    self._freeze()

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
  def overview(self) -> str:
    return self._overview or ""

  @overview.setter
  def overview(self, overview: Optional[str]):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def license_id(self) -> int:
    return self._license_id or 0

  @license_id.setter
  def license_id(self, license_id: Optional[int]):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def owner(self) -> Optional['OwnerDto']:
    return self._owner

  @owner.setter
  def owner(self, owner: Optional['OwnerDto']):
    if owner is None:
      del self.owner
      return
    if not isinstance(owner, OwnerDto):
      raise TypeError('owner must be of type OwnerDto')
    self._owner = owner

  @property
  def diff_type(self) -> 'DatabundleDiffType':
    return self._diff_type or DatabundleDiffType.REALTIME

  @diff_type.setter
  def diff_type(self, diff_type: Optional['DatabundleDiffType']):
    if diff_type is None:
      del self.diff_type
      return
    if not isinstance(diff_type, DatabundleDiffType):
      raise TypeError('diff_type must be of type DatabundleDiffType')
    self._diff_type = diff_type

  @property
  def update_frequency(self) -> 'RemoteUrlUpdateFrequency':
    return self._update_frequency or RemoteUrlUpdateFrequency.DAILY

  @update_frequency.setter
  def update_frequency(self, update_frequency: Optional['RemoteUrlUpdateFrequency']):
    if update_frequency is None:
      del self.update_frequency
      return
    if not isinstance(update_frequency, RemoteUrlUpdateFrequency):
      raise TypeError('update_frequency must be of type RemoteUrlUpdateFrequency')
    self._update_frequency = update_frequency

  @property
  def block_task_creation(self) -> bool:
    return self._block_task_creation or False

  @block_task_creation.setter
  def block_task_creation(self, block_task_creation: Optional[bool]):
    if block_task_creation is None:
      del self.block_task_creation
      return
    if not isinstance(block_task_creation, bool):
      raise TypeError('block_task_creation must be of type bool')
    self._block_task_creation = block_task_creation

  @property
  def suggestions_enabled(self) -> bool:
    return self._suggestions_enabled or False

  @suggestions_enabled.setter
  def suggestions_enabled(self, suggestions_enabled: Optional[bool]):
    if suggestions_enabled is None:
      del self.suggestions_enabled
      return
    if not isinstance(suggestions_enabled, bool):
      raise TypeError('suggestions_enabled must be of type bool')
    self._suggestions_enabled = suggestions_enabled


class DatasetImageInfo(KaggleObject):
  r"""
  Attributes:
    card_image_url (str)
    card_image_left (int)
    card_image_top (int)
    card_image_height (int)
    card_image_width (int)
    cover_image_left (int)
    cover_image_height (int)
    cover_image_top (int)
    cover_image_width (int)
    cover_image_url (str)
    original_image_url (str)
    thumbnail_image_url (str)
  """

  def __init__(self):
    self._card_image_url = ""
    self._card_image_left = 0
    self._card_image_top = 0
    self._card_image_height = 0
    self._card_image_width = 0
    self._cover_image_left = 0
    self._cover_image_height = 0
    self._cover_image_top = 0
    self._cover_image_width = 0
    self._cover_image_url = ""
    self._original_image_url = ""
    self._thumbnail_image_url = ""
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
  def card_image_left(self) -> int:
    return self._card_image_left

  @card_image_left.setter
  def card_image_left(self, card_image_left: int):
    if card_image_left is None:
      del self.card_image_left
      return
    if not isinstance(card_image_left, int):
      raise TypeError('card_image_left must be of type int')
    self._card_image_left = card_image_left

  @property
  def card_image_top(self) -> int:
    return self._card_image_top

  @card_image_top.setter
  def card_image_top(self, card_image_top: int):
    if card_image_top is None:
      del self.card_image_top
      return
    if not isinstance(card_image_top, int):
      raise TypeError('card_image_top must be of type int')
    self._card_image_top = card_image_top

  @property
  def card_image_height(self) -> int:
    return self._card_image_height

  @card_image_height.setter
  def card_image_height(self, card_image_height: int):
    if card_image_height is None:
      del self.card_image_height
      return
    if not isinstance(card_image_height, int):
      raise TypeError('card_image_height must be of type int')
    self._card_image_height = card_image_height

  @property
  def card_image_width(self) -> int:
    return self._card_image_width

  @card_image_width.setter
  def card_image_width(self, card_image_width: int):
    if card_image_width is None:
      del self.card_image_width
      return
    if not isinstance(card_image_width, int):
      raise TypeError('card_image_width must be of type int')
    self._card_image_width = card_image_width

  @property
  def cover_image_left(self) -> int:
    return self._cover_image_left

  @cover_image_left.setter
  def cover_image_left(self, cover_image_left: int):
    if cover_image_left is None:
      del self.cover_image_left
      return
    if not isinstance(cover_image_left, int):
      raise TypeError('cover_image_left must be of type int')
    self._cover_image_left = cover_image_left

  @property
  def cover_image_height(self) -> int:
    return self._cover_image_height

  @cover_image_height.setter
  def cover_image_height(self, cover_image_height: int):
    if cover_image_height is None:
      del self.cover_image_height
      return
    if not isinstance(cover_image_height, int):
      raise TypeError('cover_image_height must be of type int')
    self._cover_image_height = cover_image_height

  @property
  def cover_image_top(self) -> int:
    return self._cover_image_top

  @cover_image_top.setter
  def cover_image_top(self, cover_image_top: int):
    if cover_image_top is None:
      del self.cover_image_top
      return
    if not isinstance(cover_image_top, int):
      raise TypeError('cover_image_top must be of type int')
    self._cover_image_top = cover_image_top

  @property
  def cover_image_width(self) -> int:
    return self._cover_image_width

  @cover_image_width.setter
  def cover_image_width(self, cover_image_width: int):
    if cover_image_width is None:
      del self.cover_image_width
      return
    if not isinstance(cover_image_width, int):
      raise TypeError('cover_image_width must be of type int')
    self._cover_image_width = cover_image_width

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


class DatasetSettings(KaggleObject):
  r"""
  Attributes:
    title (str)
    subtitle (str)
    description (str)
    is_private (bool)
    keywords (str)
    licenses (SettingsLicense)
    collaborators (DatasetCollaborator)
    data (DatasetSettingsFile)
  """

  def __init__(self):
    self._title = None
    self._subtitle = None
    self._description = None
    self._is_private = False
    self._keywords = []
    self._licenses = []
    self._collaborators = []
    self._data = []
    self._freeze()

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
  def subtitle(self) -> str:
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def description(self) -> str:
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
  def keywords(self) -> Optional[List[str]]:
    return self._keywords

  @keywords.setter
  def keywords(self, keywords: Optional[List[str]]):
    if keywords is None:
      del self.keywords
      return
    if not isinstance(keywords, list):
      raise TypeError('keywords must be of type list')
    if not all([isinstance(t, str) for t in keywords]):
      raise TypeError('keywords must contain only items of type str')
    self._keywords = keywords

  @property
  def licenses(self) -> Optional[List[Optional['SettingsLicense']]]:
    return self._licenses

  @licenses.setter
  def licenses(self, licenses: Optional[List[Optional['SettingsLicense']]]):
    if licenses is None:
      del self.licenses
      return
    if not isinstance(licenses, list):
      raise TypeError('licenses must be of type list')
    if not all([isinstance(t, SettingsLicense) for t in licenses]):
      raise TypeError('licenses must contain only items of type SettingsLicense')
    self._licenses = licenses

  @property
  def collaborators(self) -> Optional[List[Optional['DatasetCollaborator']]]:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional[List[Optional['DatasetCollaborator']]]):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, list):
      raise TypeError('collaborators must be of type list')
    if not all([isinstance(t, DatasetCollaborator) for t in collaborators]):
      raise TypeError('collaborators must contain only items of type DatasetCollaborator')
    self._collaborators = collaborators

  @property
  def data(self) -> Optional[List[Optional['DatasetSettingsFile']]]:
    return self._data

  @data.setter
  def data(self, data: Optional[List[Optional['DatasetSettingsFile']]]):
    if data is None:
      del self.data
      return
    if not isinstance(data, list):
      raise TypeError('data must be of type list')
    if not all([isinstance(t, DatasetSettingsFile) for t in data]):
      raise TypeError('data must contain only items of type DatasetSettingsFile')
    self._data = data


class DatasetSettingsFile(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
    total_bytes (int)
    columns (DatasetSettingsFileColumn)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._total_bytes = 0
    self._columns = []
    self._freeze()

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def description(self) -> str:
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
  def total_bytes(self) -> int:
    return self._total_bytes

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

  @property
  def columns(self) -> Optional[List[Optional['DatasetSettingsFileColumn']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['DatasetSettingsFileColumn']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, DatasetSettingsFileColumn) for t in columns]):
      raise TypeError('columns must contain only items of type DatasetSettingsFileColumn')
    self._columns = columns


class DatasetSettingsFileColumn(KaggleObject):
  r"""
  Attributes:
    name (str)
    description (str)
    type (str)
  """

  def __init__(self):
    self._name = ""
    self._description = None
    self._type = None
    self._freeze()

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def description(self) -> str:
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
  def type(self) -> str:
    return self._type or ""

  @type.setter
  def type(self, type: Optional[str]):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type


class DatasetSuggestion(KaggleObject):
  r"""
  Unit-change suggestion. Stored in the DatasetSuggestions table.
  All suggestions:
  * have a single parent DatasetSuggestionBundle
  * are immutable after creation

  Attributes:
    id (int)
      Primary key ID of the suggestion.
    dataset_suggestion_bundle_id (int)
      Parent suggestion bundle ID.
    type (MetadataSuggestionType)
      Suggestion type, determines which 'data fields' are necessary. For example:
      a COLUMN_DESCRIPTION suggestion requires the FirestorePath and Description
      fields to be present. CHECK constraints on the table ensure relevant fields
      are NON NULL.
    state (SuggestionState)
      State of the suggestion.
    version (int)
      Version of the bundle that the suggestion corresponds to. Because
      suggestions are immutable, updates to a suggestion bundle write a new set
      of suggestions at a higher version number.
    create_time (datetime)
      When the suggestion was created.
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
    self._id = None
    self._dataset_suggestion_bundle_id = None
    self._type = MetadataSuggestionType.METADATA_SUGGESTION_TYPE_UNSPECIFIED
    self._state = None
    self._version = None
    self._create_time = None
    self._firestore_path = None
    self._description = None
    self._harmonized_type = None
    self._extended_type = None
    self._freeze()

  @property
  def id(self) -> int:
    """Primary key ID of the suggestion."""
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def dataset_suggestion_bundle_id(self) -> int:
    """Parent suggestion bundle ID."""
    return self._dataset_suggestion_bundle_id or 0

  @dataset_suggestion_bundle_id.setter
  def dataset_suggestion_bundle_id(self, dataset_suggestion_bundle_id: Optional[int]):
    if dataset_suggestion_bundle_id is None:
      del self.dataset_suggestion_bundle_id
      return
    if not isinstance(dataset_suggestion_bundle_id, int):
      raise TypeError('dataset_suggestion_bundle_id must be of type int')
    self._dataset_suggestion_bundle_id = dataset_suggestion_bundle_id

  @property
  def type(self) -> 'MetadataSuggestionType':
    r"""
    Suggestion type, determines which 'data fields' are necessary. For example:
    a COLUMN_DESCRIPTION suggestion requires the FirestorePath and Description
    fields to be present. CHECK constraints on the table ensure relevant fields
    are NON NULL.
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
  def state(self) -> 'SuggestionState':
    """State of the suggestion."""
    return self._state or SuggestionState.SUGGESTION_STATE_UNSPECIFIED

  @state.setter
  def state(self, state: Optional['SuggestionState']):
    if state is None:
      del self.state
      return
    if not isinstance(state, SuggestionState):
      raise TypeError('state must be of type SuggestionState')
    self._state = state

  @property
  def version(self) -> int:
    r"""
    Version of the bundle that the suggestion corresponds to. Because
    suggestions are immutable, updates to a suggestion bundle write a new set
    of suggestions at a higher version number.
    """
    return self._version or 0

  @version.setter
  def version(self, version: Optional[int]):
    if version is None:
      del self.version
      return
    if not isinstance(version, int):
      raise TypeError('version must be of type int')
    self._version = version

  @property
  def create_time(self) -> datetime:
    """When the suggestion was created."""
    return self._create_time or None

  @create_time.setter
  def create_time(self, create_time: Optional[datetime]):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

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


class DatasetSuggestionBundle(KaggleObject):
  r"""
  Bundles of unit-change suggestions. Stored in the
  DatasetSuggestionBundles table. Each field in this proto message corresponds
  with a field in the table unless otherwise marked.

  Attributes:
    id (int)
      Primary key ID of the bundle.
    suggester_user_id (int)
      User (suggester) that created this suggestion bundle.
    approver_user_id (int)
      User (approver) that approved this suggestion bundle. NULL if not yet
      approved.
    dataset_version_id (int)
      Dataset version that these suggestions are being made to.
    state (SuggestionBundleState)
      State of the suggestion bundle.
    current_version (int)
      Latest version number for constituent suggestions in the DatasetSuggestions
      table.
    create_time (datetime)
      When the suggestion bundle was created.
    update_time (datetime)
      When the suggestion bundle was last updated.
    suggestions (DatasetSuggestion)
      Unit-change suggestions comprising the bundle.
      In SQL this is represented by a FK constraint connection from suggestions
      in the DatasetSuggestions table to the DatasetSuggestionBundle.
    suggester_user (UserAvatar)
      Additional suggester user information.
      In SQL this is represented by a FK constraint connection from
      suggester_user_id to the Users table.
    summary (str)
      Summary describing the suggestion bundle.
    approver_note (str)
      Approver note for the suggestion bundle.
    topic_id (int)
      Attached discussion topic id.
  """

  def __init__(self):
    self._id = 0
    self._suggester_user_id = 0
    self._approver_user_id = None
    self._dataset_version_id = 0
    self._state = SuggestionBundleState.SUGGESTION_BUNDLE_STATE_UNSPECIFIED
    self._current_version = 0
    self._create_time = None
    self._update_time = None
    self._suggestions = []
    self._suggester_user = None
    self._summary = ""
    self._approver_note = None
    self._topic_id = None
    self._freeze()

  @property
  def id(self) -> int:
    """Primary key ID of the bundle."""
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
  def suggester_user_id(self) -> int:
    """User (suggester) that created this suggestion bundle."""
    return self._suggester_user_id

  @suggester_user_id.setter
  def suggester_user_id(self, suggester_user_id: int):
    if suggester_user_id is None:
      del self.suggester_user_id
      return
    if not isinstance(suggester_user_id, int):
      raise TypeError('suggester_user_id must be of type int')
    self._suggester_user_id = suggester_user_id

  @property
  def approver_user_id(self) -> int:
    r"""
    User (approver) that approved this suggestion bundle. NULL if not yet
    approved.
    """
    return self._approver_user_id or 0

  @approver_user_id.setter
  def approver_user_id(self, approver_user_id: Optional[int]):
    if approver_user_id is None:
      del self.approver_user_id
      return
    if not isinstance(approver_user_id, int):
      raise TypeError('approver_user_id must be of type int')
    self._approver_user_id = approver_user_id

  @property
  def dataset_version_id(self) -> int:
    """Dataset version that these suggestions are being made to."""
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
  def state(self) -> 'SuggestionBundleState':
    """State of the suggestion bundle."""
    return self._state

  @state.setter
  def state(self, state: 'SuggestionBundleState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, SuggestionBundleState):
      raise TypeError('state must be of type SuggestionBundleState')
    self._state = state

  @property
  def current_version(self) -> int:
    r"""
    Latest version number for constituent suggestions in the DatasetSuggestions
    table.
    """
    return self._current_version

  @current_version.setter
  def current_version(self, current_version: int):
    if current_version is None:
      del self.current_version
      return
    if not isinstance(current_version, int):
      raise TypeError('current_version must be of type int')
    self._current_version = current_version

  @property
  def create_time(self) -> datetime:
    """When the suggestion bundle was created."""
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
  def update_time(self) -> datetime:
    """When the suggestion bundle was last updated."""
    return self._update_time

  @update_time.setter
  def update_time(self, update_time: datetime):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def summary(self) -> str:
    """Summary describing the suggestion bundle."""
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
  def approver_note(self) -> str:
    """Approver note for the suggestion bundle."""
    return self._approver_note or ""

  @approver_note.setter
  def approver_note(self, approver_note: Optional[str]):
    if approver_note is None:
      del self.approver_note
      return
    if not isinstance(approver_note, str):
      raise TypeError('approver_note must be of type str')
    self._approver_note = approver_note

  @property
  def topic_id(self) -> int:
    """Attached discussion topic id."""
    return self._topic_id or 0

  @topic_id.setter
  def topic_id(self, topic_id: Optional[int]):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def suggestions(self) -> Optional[List[Optional['DatasetSuggestion']]]:
    r"""
    Unit-change suggestions comprising the bundle.
    In SQL this is represented by a FK constraint connection from suggestions
    in the DatasetSuggestions table to the DatasetSuggestionBundle.
    """
    return self._suggestions

  @suggestions.setter
  def suggestions(self, suggestions: Optional[List[Optional['DatasetSuggestion']]]):
    if suggestions is None:
      del self.suggestions
      return
    if not isinstance(suggestions, list):
      raise TypeError('suggestions must be of type list')
    if not all([isinstance(t, DatasetSuggestion) for t in suggestions]):
      raise TypeError('suggestions must contain only items of type DatasetSuggestion')
    self._suggestions = suggestions

  @property
  def suggester_user(self) -> Optional['UserAvatar']:
    r"""
    Additional suggester user information.
    In SQL this is represented by a FK constraint connection from
    suggester_user_id to the Users table.
    """
    return self._suggester_user or None

  @suggester_user.setter
  def suggester_user(self, suggester_user: Optional[Optional['UserAvatar']]):
    if suggester_user is None:
      del self.suggester_user
      return
    if not isinstance(suggester_user, UserAvatar):
      raise TypeError('suggester_user must be of type UserAvatar')
    self._suggester_user = suggester_user


class DatasetUsabilityRating(KaggleObject):
  r"""
  Frontend model of usability rating scores for dataset usability rating

  Attributes:
    score (float)
      Final score of the usability rating, out of 1
    column_description_score (float)
      Individual sub-scores for each category, out of 1
    cover_image_score (float)
    file_description_score (float)
    file_format_score (float)
    license_score (float)
    overview_score (float)
    provenance_score (float)
    public_kernel_score (float)
    subtitle_score (float)
    tag_score (float)
    update_frequency_score (float)
  """

  def __init__(self):
    self._score = 0.0
    self._column_description_score = None
    self._cover_image_score = 0.0
    self._file_description_score = 0.0
    self._file_format_score = 0.0
    self._license_score = 0.0
    self._overview_score = 0.0
    self._provenance_score = 0.0
    self._public_kernel_score = 0.0
    self._subtitle_score = 0.0
    self._tag_score = 0.0
    self._update_frequency_score = 0.0
    self._freeze()

  @property
  def score(self) -> float:
    """Final score of the usability rating, out of 1"""
    return self._score

  @score.setter
  def score(self, score: float):
    if score is None:
      del self.score
      return
    if not isinstance(score, float):
      raise TypeError('score must be of type float')
    self._score = score

  @property
  def column_description_score(self) -> float:
    """Individual sub-scores for each category, out of 1"""
    return self._column_description_score or 0.0

  @column_description_score.setter
  def column_description_score(self, column_description_score: Optional[float]):
    if column_description_score is None:
      del self.column_description_score
      return
    if not isinstance(column_description_score, float):
      raise TypeError('column_description_score must be of type float')
    self._column_description_score = column_description_score

  @property
  def cover_image_score(self) -> float:
    return self._cover_image_score

  @cover_image_score.setter
  def cover_image_score(self, cover_image_score: float):
    if cover_image_score is None:
      del self.cover_image_score
      return
    if not isinstance(cover_image_score, float):
      raise TypeError('cover_image_score must be of type float')
    self._cover_image_score = cover_image_score

  @property
  def file_description_score(self) -> float:
    return self._file_description_score

  @file_description_score.setter
  def file_description_score(self, file_description_score: float):
    if file_description_score is None:
      del self.file_description_score
      return
    if not isinstance(file_description_score, float):
      raise TypeError('file_description_score must be of type float')
    self._file_description_score = file_description_score

  @property
  def file_format_score(self) -> float:
    return self._file_format_score

  @file_format_score.setter
  def file_format_score(self, file_format_score: float):
    if file_format_score is None:
      del self.file_format_score
      return
    if not isinstance(file_format_score, float):
      raise TypeError('file_format_score must be of type float')
    self._file_format_score = file_format_score

  @property
  def license_score(self) -> float:
    return self._license_score

  @license_score.setter
  def license_score(self, license_score: float):
    if license_score is None:
      del self.license_score
      return
    if not isinstance(license_score, float):
      raise TypeError('license_score must be of type float')
    self._license_score = license_score

  @property
  def overview_score(self) -> float:
    return self._overview_score

  @overview_score.setter
  def overview_score(self, overview_score: float):
    if overview_score is None:
      del self.overview_score
      return
    if not isinstance(overview_score, float):
      raise TypeError('overview_score must be of type float')
    self._overview_score = overview_score

  @property
  def provenance_score(self) -> float:
    return self._provenance_score

  @provenance_score.setter
  def provenance_score(self, provenance_score: float):
    if provenance_score is None:
      del self.provenance_score
      return
    if not isinstance(provenance_score, float):
      raise TypeError('provenance_score must be of type float')
    self._provenance_score = provenance_score

  @property
  def public_kernel_score(self) -> float:
    return self._public_kernel_score

  @public_kernel_score.setter
  def public_kernel_score(self, public_kernel_score: float):
    if public_kernel_score is None:
      del self.public_kernel_score
      return
    if not isinstance(public_kernel_score, float):
      raise TypeError('public_kernel_score must be of type float')
    self._public_kernel_score = public_kernel_score

  @property
  def subtitle_score(self) -> float:
    return self._subtitle_score

  @subtitle_score.setter
  def subtitle_score(self, subtitle_score: float):
    if subtitle_score is None:
      del self.subtitle_score
      return
    if not isinstance(subtitle_score, float):
      raise TypeError('subtitle_score must be of type float')
    self._subtitle_score = subtitle_score

  @property
  def tag_score(self) -> float:
    return self._tag_score

  @tag_score.setter
  def tag_score(self, tag_score: float):
    if tag_score is None:
      del self.tag_score
      return
    if not isinstance(tag_score, float):
      raise TypeError('tag_score must be of type float')
    self._tag_score = tag_score

  @property
  def update_frequency_score(self) -> float:
    return self._update_frequency_score

  @update_frequency_score.setter
  def update_frequency_score(self, update_frequency_score: float):
    if update_frequency_score is None:
      del self.update_frequency_score
      return
    if not isinstance(update_frequency_score, float):
      raise TypeError('update_frequency_score must be of type float')
    self._update_frequency_score = update_frequency_score


class DatasetVersionAuthor(KaggleObject):
  r"""
  the creation of this version of dataset.

  Attributes:
    dataset_version_author_id (int)
      The backend Id of DatasetVersionAuthor table.
      This is served to frontend, so an update of the exact record can be made.
    author_name (str)
      Author Name.
    author_bio (str)
      Author Biography.
  """

  def __init__(self):
    self._dataset_version_author_id = None
    self._author_name = None
    self._author_bio = None
    self._freeze()

  @property
  def dataset_version_author_id(self) -> int:
    r"""
    The backend Id of DatasetVersionAuthor table.
    This is served to frontend, so an update of the exact record can be made.
    """
    return self._dataset_version_author_id or 0

  @dataset_version_author_id.setter
  def dataset_version_author_id(self, dataset_version_author_id: Optional[int]):
    if dataset_version_author_id is None:
      del self.dataset_version_author_id
      return
    if not isinstance(dataset_version_author_id, int):
      raise TypeError('dataset_version_author_id must be of type int')
    self._dataset_version_author_id = dataset_version_author_id

  @property
  def author_name(self) -> str:
    """Author Name."""
    return self._author_name or ""

  @author_name.setter
  def author_name(self, author_name: Optional[str]):
    if author_name is None:
      del self.author_name
      return
    if not isinstance(author_name, str):
      raise TypeError('author_name must be of type str')
    self._author_name = author_name

  @property
  def author_bio(self) -> str:
    """Author Biography."""
    return self._author_bio or ""

  @author_bio.setter
  def author_bio(self, author_bio: Optional[str]):
    if author_bio is None:
      del self.author_bio
      return
    if not isinstance(author_bio, str):
      raise TypeError('author_bio must be of type str')
    self._author_bio = author_bio


class DatasetVersionMetadata(KaggleObject):
  r"""
  Attributes:
    data_coverage_attribute (DataCoverageAttribute)
      Data coverage, including temporal and spatial.
    collection_methods (str)
      Collection methods for current version of dataset.
    dataset_version_authors (DatasetVersionAuthor)
      Dataset version authors, people (including non-Kaggle users) who helped
      with the creation of this version of dataset.
    doi (str)
      Data object identity for current version of dataset.
    license_id (int)
      License Id for current version of dataset.
    user_specified_sources (str)
      User specified sources for current version of dataset.
    expected_update_frequency (str)
      Expected update frequency of dataset.
    citations (Citation)
      Dataset version citations, papers that discuss the creation of the dataset.
  """

  def __init__(self):
    self._data_coverage_attribute = None
    self._collection_methods = None
    self._dataset_version_authors = []
    self._doi = None
    self._license_id = None
    self._user_specified_sources = None
    self._expected_update_frequency = None
    self._citations = []
    self._freeze()

  @property
  def data_coverage_attribute(self) -> Optional['DataCoverageAttribute']:
    """Data coverage, including temporal and spatial."""
    return self._data_coverage_attribute or None

  @data_coverage_attribute.setter
  def data_coverage_attribute(self, data_coverage_attribute: Optional[Optional['DataCoverageAttribute']]):
    if data_coverage_attribute is None:
      del self.data_coverage_attribute
      return
    if not isinstance(data_coverage_attribute, DataCoverageAttribute):
      raise TypeError('data_coverage_attribute must be of type DataCoverageAttribute')
    self._data_coverage_attribute = data_coverage_attribute

  @property
  def collection_methods(self) -> str:
    """Collection methods for current version of dataset."""
    return self._collection_methods or ""

  @collection_methods.setter
  def collection_methods(self, collection_methods: Optional[str]):
    if collection_methods is None:
      del self.collection_methods
      return
    if not isinstance(collection_methods, str):
      raise TypeError('collection_methods must be of type str')
    self._collection_methods = collection_methods

  @property
  def dataset_version_authors(self) -> Optional[List[Optional['DatasetVersionAuthor']]]:
    r"""
    Dataset version authors, people (including non-Kaggle users) who helped
    with the creation of this version of dataset.
    """
    return self._dataset_version_authors

  @dataset_version_authors.setter
  def dataset_version_authors(self, dataset_version_authors: Optional[List[Optional['DatasetVersionAuthor']]]):
    if dataset_version_authors is None:
      del self.dataset_version_authors
      return
    if not isinstance(dataset_version_authors, list):
      raise TypeError('dataset_version_authors must be of type list')
    if not all([isinstance(t, DatasetVersionAuthor) for t in dataset_version_authors]):
      raise TypeError('dataset_version_authors must contain only items of type DatasetVersionAuthor')
    self._dataset_version_authors = dataset_version_authors

  @property
  def doi(self) -> str:
    """Data object identity for current version of dataset."""
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
  def license_id(self) -> int:
    """License Id for current version of dataset."""
    return self._license_id or 0

  @license_id.setter
  def license_id(self, license_id: Optional[int]):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def user_specified_sources(self) -> str:
    """User specified sources for current version of dataset."""
    return self._user_specified_sources or ""

  @user_specified_sources.setter
  def user_specified_sources(self, user_specified_sources: Optional[str]):
    if user_specified_sources is None:
      del self.user_specified_sources
      return
    if not isinstance(user_specified_sources, str):
      raise TypeError('user_specified_sources must be of type str')
    self._user_specified_sources = user_specified_sources

  @property
  def expected_update_frequency(self) -> str:
    """Expected update frequency of dataset."""
    return self._expected_update_frequency or ""

  @expected_update_frequency.setter
  def expected_update_frequency(self, expected_update_frequency: Optional[str]):
    if expected_update_frequency is None:
      del self.expected_update_frequency
      return
    if not isinstance(expected_update_frequency, str):
      raise TypeError('expected_update_frequency must be of type str')
    self._expected_update_frequency = expected_update_frequency

  @property
  def citations(self) -> Optional[List[Optional['Citation']]]:
    """Dataset version citations, papers that discuss the creation of the dataset."""
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['Citation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, Citation) for t in citations]):
      raise TypeError('citations must contain only items of type Citation')
    self._citations = citations


class ExpectedUpdateFrequency(KaggleObject):
  r"""
  Expected update frequency for the dataset.

  Attributes:
    is_auto_updated_typed_dataset (bool)
      Dataset sources where Kaggle offers the option for automatic scheduled
      updates. Currently, it's either Remote URL or Remote Github sourced
      datasets.
    update_frequency (str)
      Update frequency that:
      1. Kaggle will use for scheduled refreshing from the sources when
      IsAutoUpdatedTypedDataset is true.
      2. User specified, but Kaggle will not perform any scheduled refreshing
      when IsAutoUpdatedTypedDataset is false.
  """

  def __init__(self):
    self._is_auto_updated_typed_dataset = False
    self._update_frequency = ""
    self._freeze()

  @property
  def is_auto_updated_typed_dataset(self) -> bool:
    r"""
    Dataset sources where Kaggle offers the option for automatic scheduled
    updates. Currently, it's either Remote URL or Remote Github sourced
    datasets.
    """
    return self._is_auto_updated_typed_dataset

  @is_auto_updated_typed_dataset.setter
  def is_auto_updated_typed_dataset(self, is_auto_updated_typed_dataset: bool):
    if is_auto_updated_typed_dataset is None:
      del self.is_auto_updated_typed_dataset
      return
    if not isinstance(is_auto_updated_typed_dataset, bool):
      raise TypeError('is_auto_updated_typed_dataset must be of type bool')
    self._is_auto_updated_typed_dataset = is_auto_updated_typed_dataset

  @property
  def update_frequency(self) -> str:
    r"""
    Update frequency that:
    1. Kaggle will use for scheduled refreshing from the sources when
    IsAutoUpdatedTypedDataset is true.
    2. User specified, but Kaggle will not perform any scheduled refreshing
    when IsAutoUpdatedTypedDataset is false.
    """
    return self._update_frequency

  @update_frequency.setter
  def update_frequency(self, update_frequency: str):
    if update_frequency is None:
      del self.update_frequency
      return
    if not isinstance(update_frequency, str):
      raise TypeError('update_frequency must be of type str')
    self._update_frequency = update_frequency


class KernelOutputDatasetReference(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    current_dataset_version_id (int)
    title (str)
    is_private (bool)
    slug (str)
    license (LicenseOption)
    url (str)
    thumbnail_url (str)
  """

  def __init__(self):
    self._dataset_id = 0
    self._current_dataset_version_id = 0
    self._title = ""
    self._is_private = False
    self._slug = ""
    self._license = None
    self._url = None
    self._thumbnail_url = None
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
  def title(self) -> str:
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

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
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def license(self) -> Optional['LicenseOption']:
    return self._license

  @license.setter
  def license(self, license: Optional['LicenseOption']):
    if license is None:
      del self.license
      return
    if not isinstance(license, LicenseOption):
      raise TypeError('license must be of type LicenseOption')
    self._license = license

  @property
  def url(self) -> str:
    return self._url or ""

  @url.setter
  def url(self, url: Optional[str]):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

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


class KernelTaskSubmissionInfo(KaggleObject):
  r"""
  If a notebook is used as a (accepted) submission for a task, this object
  contains the info the frontend needs to display a corresponding info.

  Attributes:
    task_url (str)
    task_title (str)
    dataset_url (str)
    dataset_title (str)
    is_accepted_solution (bool)
  """

  def __init__(self):
    self._task_url = None
    self._task_title = None
    self._dataset_url = None
    self._dataset_title = None
    self._is_accepted_solution = False
    self._freeze()

  @property
  def task_url(self) -> str:
    return self._task_url or ""

  @task_url.setter
  def task_url(self, task_url: Optional[str]):
    if task_url is None:
      del self.task_url
      return
    if not isinstance(task_url, str):
      raise TypeError('task_url must be of type str')
    self._task_url = task_url

  @property
  def task_title(self) -> str:
    return self._task_title or ""

  @task_title.setter
  def task_title(self, task_title: Optional[str]):
    if task_title is None:
      del self.task_title
      return
    if not isinstance(task_title, str):
      raise TypeError('task_title must be of type str')
    self._task_title = task_title

  @property
  def dataset_url(self) -> str:
    return self._dataset_url or ""

  @dataset_url.setter
  def dataset_url(self, dataset_url: Optional[str]):
    if dataset_url is None:
      del self.dataset_url
      return
    if not isinstance(dataset_url, str):
      raise TypeError('dataset_url must be of type str')
    self._dataset_url = dataset_url

  @property
  def dataset_title(self) -> str:
    return self._dataset_title or ""

  @dataset_title.setter
  def dataset_title(self, dataset_title: Optional[str]):
    if dataset_title is None:
      del self.dataset_title
      return
    if not isinstance(dataset_title, str):
      raise TypeError('dataset_title must be of type str')
    self._dataset_title = dataset_title

  @property
  def is_accepted_solution(self) -> bool:
    return self._is_accepted_solution

  @is_accepted_solution.setter
  def is_accepted_solution(self, is_accepted_solution: bool):
    if is_accepted_solution is None:
      del self.is_accepted_solution
      return
    if not isinstance(is_accepted_solution, bool):
      raise TypeError('is_accepted_solution must be of type bool')
    self._is_accepted_solution = is_accepted_solution


class Owner(KaggleObject):
  r"""
  Attributes:
    id (int)
    image_url (str)
    organization (bool)
    max_file_size_bytes (int)
    name (str)
    organization_member_count (int)
    profile_url (str)
    slug (str)
    user_tier (UserAchievementTier)
    twitter (str)
    user_progression_opt_out (bool)
  """

  def __init__(self):
    self._id = 0
    self._image_url = ""
    self._organization = False
    self._max_file_size_bytes = 0
    self._name = ""
    self._organization_member_count = 0
    self._profile_url = ""
    self._slug = ""
    self._user_tier = UserAchievementTier.NOVICE
    self._twitter = None
    self._user_progression_opt_out = False
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
  def image_url(self) -> str:
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def organization(self) -> bool:
    return self._organization

  @organization.setter
  def organization(self, organization: bool):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, bool):
      raise TypeError('organization must be of type bool')
    self._organization = organization

  @property
  def max_file_size_bytes(self) -> int:
    return self._max_file_size_bytes

  @max_file_size_bytes.setter
  def max_file_size_bytes(self, max_file_size_bytes: int):
    if max_file_size_bytes is None:
      del self.max_file_size_bytes
      return
    if not isinstance(max_file_size_bytes, int):
      raise TypeError('max_file_size_bytes must be of type int')
    self._max_file_size_bytes = max_file_size_bytes

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def organization_member_count(self) -> int:
    return self._organization_member_count

  @organization_member_count.setter
  def organization_member_count(self, organization_member_count: int):
    if organization_member_count is None:
      del self.organization_member_count
      return
    if not isinstance(organization_member_count, int):
      raise TypeError('organization_member_count must be of type int')
    self._organization_member_count = organization_member_count

  @property
  def profile_url(self) -> str:
    return self._profile_url

  @profile_url.setter
  def profile_url(self, profile_url: str):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier

  @property
  def user_progression_opt_out(self) -> bool:
    return self._user_progression_opt_out

  @user_progression_opt_out.setter
  def user_progression_opt_out(self, user_progression_opt_out: bool):
    if user_progression_opt_out is None:
      del self.user_progression_opt_out
      return
    if not isinstance(user_progression_opt_out, bool):
      raise TypeError('user_progression_opt_out must be of type bool')
    self._user_progression_opt_out = user_progression_opt_out

  @property
  def twitter(self) -> str:
    return self._twitter or ""

  @twitter.setter
  def twitter(self, twitter: Optional[str]):
    if twitter is None:
      del self.twitter
      return
    if not isinstance(twitter, str):
      raise TypeError('twitter must be of type str')
    self._twitter = twitter


class OwnerDto(KaggleObject):
  r"""
  Attributes:
    id (int)
    image_url (str)
    is_organization (bool)
    name (str)
    profile_url (str)
    slug (str)
    max_file_size_bytes (int)
    user_tier (UserAchievementTier)
    organization_member_count (int)
    progression_opted_out (bool)
  """

  def __init__(self):
    self._id = 0
    self._image_url = None
    self._is_organization = False
    self._name = ""
    self._profile_url = None
    self._slug = ""
    self._max_file_size_bytes = None
    self._user_tier = UserAchievementTier.NOVICE
    self._organization_member_count = None
    self._progression_opted_out = None
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
  def image_url(self) -> str:
    return self._image_url or ""

  @image_url.setter
  def image_url(self, image_url: Optional[str]):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def is_organization(self) -> bool:
    return self._is_organization

  @is_organization.setter
  def is_organization(self, is_organization: bool):
    if is_organization is None:
      del self.is_organization
      return
    if not isinstance(is_organization, bool):
      raise TypeError('is_organization must be of type bool')
    self._is_organization = is_organization

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def profile_url(self) -> str:
    return self._profile_url or ""

  @profile_url.setter
  def profile_url(self, profile_url: Optional[str]):
    if profile_url is None:
      del self.profile_url
      return
    if not isinstance(profile_url, str):
      raise TypeError('profile_url must be of type str')
    self._profile_url = profile_url

  @property
  def slug(self) -> str:
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def max_file_size_bytes(self) -> int:
    return self._max_file_size_bytes or 0

  @max_file_size_bytes.setter
  def max_file_size_bytes(self, max_file_size_bytes: Optional[int]):
    if max_file_size_bytes is None:
      del self.max_file_size_bytes
      return
    if not isinstance(max_file_size_bytes, int):
      raise TypeError('max_file_size_bytes must be of type int')
    self._max_file_size_bytes = max_file_size_bytes

  @property
  def user_tier(self) -> 'UserAchievementTier':
    return self._user_tier

  @user_tier.setter
  def user_tier(self, user_tier: 'UserAchievementTier'):
    if user_tier is None:
      del self.user_tier
      return
    if not isinstance(user_tier, UserAchievementTier):
      raise TypeError('user_tier must be of type UserAchievementTier')
    self._user_tier = user_tier

  @property
  def organization_member_count(self) -> int:
    return self._organization_member_count or 0

  @organization_member_count.setter
  def organization_member_count(self, organization_member_count: Optional[int]):
    if organization_member_count is None:
      del self.organization_member_count
      return
    if not isinstance(organization_member_count, int):
      raise TypeError('organization_member_count must be of type int')
    self._organization_member_count = organization_member_count

  @property
  def progression_opted_out(self) -> bool:
    return self._progression_opted_out or False

  @progression_opted_out.setter
  def progression_opted_out(self, progression_opted_out: Optional[bool]):
    if progression_opted_out is None:
      del self.progression_opted_out
      return
    if not isinstance(progression_opted_out, bool):
      raise TypeError('progression_opted_out must be of type bool')
    self._progression_opted_out = progression_opted_out


class ReviewDatasetSuggestionBundleApproval(KaggleObject):
  r"""
  Attributes:
    note (str)
      Optional note from the reviewer.
  """

  def __init__(self):
    self._note = None
    self._freeze()

  @property
  def note(self) -> str:
    """Optional note from the reviewer."""
    return self._note or ""

  @note.setter
  def note(self, note: Optional[str]):
    if note is None:
      del self.note
      return
    if not isinstance(note, str):
      raise TypeError('note must be of type str')
    self._note = note


class ReviewDatasetSuggestionBundleApprovalWithChanges(KaggleObject):
  r"""
  Attributes:
    note (str)
      A note from the reviewer is required for approvals with changes.
    dataset_suggestion_bundle (DatasetSuggestionBundle)
      The updated DatasetSuggestionBundle.
    update_mask (FieldMask)
      List of fields to update.
  """

  def __init__(self):
    self._note = ""
    self._dataset_suggestion_bundle = None
    self._update_mask = None
    self._freeze()

  @property
  def note(self) -> str:
    """A note from the reviewer is required for approvals with changes."""
    return self._note

  @note.setter
  def note(self, note: str):
    if note is None:
      del self.note
      return
    if not isinstance(note, str):
      raise TypeError('note must be of type str')
    self._note = note

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


class ReviewDatasetSuggestionBundleRejection(KaggleObject):
  r"""
  Attributes:
    note (str)
      A note from the reviewer is required for rejections.
  """

  def __init__(self):
    self._note = ""
    self._freeze()

  @property
  def note(self) -> str:
    """A note from the reviewer is required for rejections."""
    return self._note

  @note.setter
  def note(self, note: str):
    if note is None:
      del self.note
      return
    if not isinstance(note, str):
      raise TypeError('note must be of type str')
    self._note = note


class SettingsLicense(KaggleObject):
  r"""
  Attributes:
    name (str)
  """

  def __init__(self):
    self._name = None
    self._freeze()

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


class StorageLocation(KaggleObject):
  r"""
  Attributes:
    bucket (str)
    path (str)
  """

  def __init__(self):
    self._bucket = None
    self._path = None
    self._freeze()

  @property
  def bucket(self) -> str:
    return self._bucket or ""

  @bucket.setter
  def bucket(self, bucket: Optional[str]):
    if bucket is None:
      del self.bucket
      return
    if not isinstance(bucket, str):
      raise TypeError('bucket must be of type str')
    self._bucket = bucket

  @property
  def path(self) -> str:
    return self._path or ""

  @path.setter
  def path(self, path: Optional[str]):
    if path is None:
      del self.path
      return
    if not isinstance(path, str):
      raise TypeError('path must be of type str')
    self._path = path


ActionFlags._fields = [
  FieldMetadata("disableWorker", "disable_worker", "_disable_worker", bool, False, PredefinedSerializer()),
  FieldMetadata("disableBundleCreation", "disable_bundle_creation", "_disable_bundle_creation", bool, False, PredefinedSerializer()),
  FieldMetadata("disableIndividualZipCreation", "disable_individual_zip_creation", "_disable_individual_zip_creation", bool, False, PredefinedSerializer()),
  FieldMetadata("disableRawUpload", "disable_raw_upload", "_disable_raw_upload", bool, False, PredefinedSerializer()),
  FieldMetadata("disableMetadata", "disable_metadata", "_disable_metadata", bool, False, PredefinedSerializer()),
  FieldMetadata("disableStatus", "disable_status", "_disable_status", bool, False, PredefinedSerializer()),
  FieldMetadata("disableStatusPubSub", "disable_status_pub_sub", "_disable_status_pub_sub", bool, False, PredefinedSerializer()),
  FieldMetadata("disableFinalResult", "disable_final_result", "_disable_final_result", bool, False, PredefinedSerializer()),
  FieldMetadata("disableEmbeddedFilesystem", "disable_embedded_filesystem", "_disable_embedded_filesystem", bool, False, PredefinedSerializer()),
  FieldMetadata("disableDecompression", "disable_decompression", "_disable_decompression", bool, False, PredefinedSerializer()),
  FieldMetadata("disableDirectoryZipCreation", "disable_directory_zip_creation", "_disable_directory_zip_creation", bool, False, PredefinedSerializer()),
  FieldMetadata("useStandaloneZipperForBundle", "use_standalone_zipper_for_bundle", "_use_standalone_zipper_for_bundle", bool, False, PredefinedSerializer()),
  FieldMetadata("reuseOriginalSingleGcsZip", "reuse_original_single_gcs_zip", "_reuse_original_single_gcs_zip", bool, False, PredefinedSerializer()),
  FieldMetadata("gcsUploadUrl", "gcs_upload_url", "_gcs_upload_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("spreadCsvSampleRows", "spread_csv_sample_rows", "_spread_csv_sample_rows", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ignoreMissingGcsFiles", "ignore_missing_gcs_files", "_ignore_missing_gcs_files", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reducedWatchdogProcessing", "reduced_watchdog_processing", "_reduced_watchdog_processing", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("noSingleProducerConstrained", "no_single_producer_constrained", "_no_single_producer_constrained", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableWorkerAutoAck", "disable_worker_auto_ack", "_disable_worker_auto_ack", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("applyBackpressureWhenZipping", "apply_backpressure_when_zipping", "_apply_backpressure_when_zipping", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createCroissantAfterZipping", "create_croissant_after_zipping", "_create_croissant_after_zipping", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("streamGcsListResults", "stream_gcs_list_results", "_stream_gcs_list_results", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gcsFilterGlobPattern", "gcs_filter_glob_pattern", "_gcs_filter_glob_pattern", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("disableMetricsCalculation", "disable_metrics_calculation", "_disable_metrics_calculation", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableCopyInTheCloudBlock", "enable_copy_in_the_cloud_block", "_enable_copy_in_the_cloud_block", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableCopyInTheCloudLogging", "enable_copy_in_the_cloud_logging", "_enable_copy_in_the_cloud_logging", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enableParquetSupport", "enable_parquet_support", "_enable_parquet_support", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isCompetitionRerunDataset", "is_competition_rerun_dataset", "_is_competition_rerun_dataset", bool, None, PredefinedSerializer(), optional=True),
]

Citation._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

DatabundleInfo._fields = [
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("isFileset", "is_fileset", "_is_fileset", bool, False, PredefinedSerializer()),
  FieldMetadata("canDownload", "can_download", "_can_download", bool, False, PredefinedSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, "", PredefinedSerializer()),
  FieldMetadata("versionId", "version_id", "_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", DatabundleVersionType, DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastVersionId", "last_version_id", "_last_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fileExtensions", "file_extensions", "_file_extensions", str, [], ListSerializer(PredefinedSerializer())),
]

DataCoverageAttribute._fields = [
  FieldMetadata("temporalCoverageFrom", "temporal_coverage_from", "_temporal_coverage_from", datetime, None, DateTimeSerializer()),
  FieldMetadata("temporalCoverageTo", "temporal_coverage_to", "_temporal_coverage_to", datetime, None, DateTimeSerializer()),
  FieldMetadata("spatialCoverage", "spatial_coverage", "_spatial_coverage", str, None, PredefinedSerializer(), optional=True),
]

DatasetActivityPageDiscussion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("voteButtonDto", "vote_button_dto", "_vote_button_dto", VoteButton, None, KaggleObjectSerializer()),
  FieldMetadata("avatar", "avatar", "_avatar", UserAvatar, None, KaggleObjectSerializer()),
  FieldMetadata("medal", "medal", "_medal", Image, None, KaggleObjectSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("timeSinceLastActivity", "time_since_last_activity", "_time_since_last_activity", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("replyCount", "reply_count", "_reply_count", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
]

DatasetAdminSettingsInfo._fields = [
  FieldMetadata("maintainerOrganization", "maintainer_organization", "_maintainer_organization", Owner, None, KaggleObjectSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
]

DatasetCollaborator._fields = [
  FieldMetadata("username", "username", "_username", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("groupSlug", "group_slug", "_group_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("role", "role", "_role", CollaboratorType, CollaboratorType.COLLABORATOR_TYPE_UNSPECIFIED, EnumSerializer()),
]

DatasetCroissantInfo._fields = [
  FieldMetadata("autoGenCroissantDownloadUrl", "auto_gen_croissant_download_url", "_auto_gen_croissant_download_url", str, "", PredefinedSerializer()),
  FieldMetadata("canDownloadAutoGenCroissant", "can_download_auto_gen_croissant", "_can_download_auto_gen_croissant", bool, False, PredefinedSerializer()),
  FieldMetadata("autoGenCroissantTotalSize", "auto_gen_croissant_total_size", "_auto_gen_croissant_total_size", int, None, PredefinedSerializer(), optional=True),
]

DatasetDatasourceListItem._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentDatasetVersionId", "current_dataset_version_id", "_current_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentDatasetVersionNumber", "current_dataset_version_number", "_current_dataset_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", DatabundleVersionType, DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("diffType", "diff_type", "_diff_type", DatabundleDiffType, DatabundleDiffType.REALTIME, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("overview", "overview", "_overview", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("isDeleted", "is_deleted", "_is_deleted", bool, False, PredefinedSerializer()),
]

DatasetFeedbackInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", FeedbackState, FeedbackState.FEEDBACK_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", FeedbackType, FeedbackType.FEEDBACK_TYPE_UNSPECIFIED, EnumSerializer()),
]

DatasetFileSummary._fields = [
  FieldMetadata("fileType", "file_type", "_file_type", DatasetFileType, DatasetFileType.DATASET_FILE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

DatasetGeneralUpdatableInfo._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("overview", "overview", "_overview", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("owner", "owner", "_owner", OwnerDto, None, KaggleObjectSerializer()),
  FieldMetadata("diffType", "diff_type", "_diff_type", DatabundleDiffType, None, EnumSerializer(), optional=True),
  FieldMetadata("updateFrequency", "update_frequency", "_update_frequency", RemoteUrlUpdateFrequency, None, EnumSerializer(), optional=True),
  FieldMetadata("blockTaskCreation", "block_task_creation", "_block_task_creation", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("suggestionsEnabled", "suggestions_enabled", "_suggestions_enabled", bool, None, PredefinedSerializer(), optional=True),
]

DatasetImageInfo._fields = [
  FieldMetadata("cardImageUrl", "card_image_url", "_card_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("cardImageLeft", "card_image_left", "_card_image_left", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageTop", "card_image_top", "_card_image_top", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageHeight", "card_image_height", "_card_image_height", int, 0, PredefinedSerializer()),
  FieldMetadata("cardImageWidth", "card_image_width", "_card_image_width", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageLeft", "cover_image_left", "_cover_image_left", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageHeight", "cover_image_height", "_cover_image_height", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageTop", "cover_image_top", "_cover_image_top", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageWidth", "cover_image_width", "_cover_image_width", int, 0, PredefinedSerializer()),
  FieldMetadata("coverImageUrl", "cover_image_url", "_cover_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("originalImageUrl", "original_image_url", "_original_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrl", "thumbnail_image_url", "_thumbnail_image_url", str, "", PredefinedSerializer()),
]

DatasetSettings._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("keywords", "keywords", "_keywords", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("licenses", "licenses", "_licenses", SettingsLicense, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("collaborators", "collaborators", "_collaborators", DatasetCollaborator, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("data", "data", "_data", DatasetSettingsFile, [], ListSerializer(KaggleObjectSerializer())),
]

DatasetSettingsFile._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("columns", "columns", "_columns", DatasetSettingsFileColumn, [], ListSerializer(KaggleObjectSerializer())),
]

DatasetSettingsFileColumn._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", str, None, PredefinedSerializer(), optional=True),
]

DatasetSuggestion._fields = [
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetSuggestionBundleId", "dataset_suggestion_bundle_id", "_dataset_suggestion_bundle_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", MetadataSuggestionType, MetadataSuggestionType.METADATA_SUGGESTION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("state", "state", "_state", SuggestionState, None, EnumSerializer(), optional=True),
  FieldMetadata("version", "version", "_version", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("harmonizedType", "harmonized_type", "_harmonized_type", HarmonizedDataType, None, EnumSerializer(), optional=True),
  FieldMetadata("extendedType", "extended_type", "_extended_type", ExtendedDataType, None, EnumSerializer(), optional=True),
]

DatasetSuggestionBundle._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("suggesterUserId", "suggester_user_id", "_suggester_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("approverUserId", "approver_user_id", "_approver_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", SuggestionBundleState, SuggestionBundleState.SUGGESTION_BUNDLE_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("currentVersion", "current_version", "_current_version", int, 0, PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("suggestions", "suggestions", "_suggestions", DatasetSuggestion, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("suggesterUser", "suggester_user", "_suggester_user", UserAvatar, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("summary", "summary", "_summary", str, "", PredefinedSerializer()),
  FieldMetadata("approverNote", "approver_note", "_approver_note", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
]

DatasetUsabilityRating._fields = [
  FieldMetadata("score", "score", "_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("columnDescriptionScore", "column_description_score", "_column_description_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("coverImageScore", "cover_image_score", "_cover_image_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("fileDescriptionScore", "file_description_score", "_file_description_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("fileFormatScore", "file_format_score", "_file_format_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("licenseScore", "license_score", "_license_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("overviewScore", "overview_score", "_overview_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("provenanceScore", "provenance_score", "_provenance_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("publicKernelScore", "public_kernel_score", "_public_kernel_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("subtitleScore", "subtitle_score", "_subtitle_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("tagScore", "tag_score", "_tag_score", float, 0.0, PredefinedSerializer()),
  FieldMetadata("updateFrequencyScore", "update_frequency_score", "_update_frequency_score", float, 0.0, PredefinedSerializer()),
]

DatasetVersionAuthor._fields = [
  FieldMetadata("datasetVersionAuthorId", "dataset_version_author_id", "_dataset_version_author_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorName", "author_name", "_author_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorBio", "author_bio", "_author_bio", str, None, PredefinedSerializer(), optional=True),
]

DatasetVersionMetadata._fields = [
  FieldMetadata("dataCoverageAttribute", "data_coverage_attribute", "_data_coverage_attribute", DataCoverageAttribute, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("collectionMethods", "collection_methods", "_collection_methods", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionAuthors", "dataset_version_authors", "_dataset_version_authors", DatasetVersionAuthor, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userSpecifiedSources", "user_specified_sources", "_user_specified_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("expectedUpdateFrequency", "expected_update_frequency", "_expected_update_frequency", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", Citation, [], ListSerializer(KaggleObjectSerializer())),
]

ExpectedUpdateFrequency._fields = [
  FieldMetadata("isAutoUpdatedTypedDataset", "is_auto_updated_typed_dataset", "_is_auto_updated_typed_dataset", bool, False, PredefinedSerializer()),
  FieldMetadata("updateFrequency", "update_frequency", "_update_frequency", str, "", PredefinedSerializer()),
]

KernelOutputDatasetReference._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("currentDatasetVersionId", "current_dataset_version_id", "_current_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("license", "license", "_license", LicenseOption, None, KaggleObjectSerializer()),
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, None, PredefinedSerializer(), optional=True),
]

KernelTaskSubmissionInfo._fields = [
  FieldMetadata("taskUrl", "task_url", "_task_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("taskTitle", "task_title", "_task_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetUrl", "dataset_url", "_dataset_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetTitle", "dataset_title", "_dataset_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isAcceptedSolution", "is_accepted_solution", "_is_accepted_solution", bool, False, PredefinedSerializer()),
]

Owner._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("organization", "organization", "_organization", bool, False, PredefinedSerializer()),
  FieldMetadata("maxFileSizeBytes", "max_file_size_bytes", "_max_file_size_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("organizationMemberCount", "organization_member_count", "_organization_member_count", int, 0, PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("twitter", "twitter", "_twitter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userProgressionOptOut", "user_progression_opt_out", "_user_progression_opt_out", bool, False, PredefinedSerializer()),
]

OwnerDto._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isOrganization", "is_organization", "_is_organization", bool, False, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("profileUrl", "profile_url", "_profile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("maxFileSizeBytes", "max_file_size_bytes", "_max_file_size_bytes", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userTier", "user_tier", "_user_tier", UserAchievementTier, UserAchievementTier.NOVICE, EnumSerializer()),
  FieldMetadata("organizationMemberCount", "organization_member_count", "_organization_member_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("progressionOptedOut", "progression_opted_out", "_progression_opted_out", bool, None, PredefinedSerializer(), optional=True),
]

ReviewDatasetSuggestionBundleApproval._fields = [
  FieldMetadata("note", "note", "_note", str, None, PredefinedSerializer(), optional=True),
]

ReviewDatasetSuggestionBundleApprovalWithChanges._fields = [
  FieldMetadata("note", "note", "_note", str, "", PredefinedSerializer()),
  FieldMetadata("datasetSuggestionBundle", "dataset_suggestion_bundle", "_dataset_suggestion_bundle", DatasetSuggestionBundle, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

ReviewDatasetSuggestionBundleRejection._fields = [
  FieldMetadata("note", "note", "_note", str, "", PredefinedSerializer()),
]

SettingsLicense._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
]

StorageLocation._fields = [
  FieldMetadata("bucket", "bucket", "_bucket", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("path", "path", "_path", str, None, PredefinedSerializer(), optional=True),
]

