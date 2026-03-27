from datetime import datetime
from kagglesdk.datasets.databundles.types.databundle_enums import DataSourceState, DataSourceType, ExtendedDataType, ExternalCopyStatus, HarmonizedDataType, MetricsCalculationSkipReason, ObjectType
from kagglesdk.datasets.types.dataset_enums import DatabundleDiffType, DatabundleStatus, DatabundleType, DatabundleVersionAnalysisStatus, DatabundleVersionType, RemoteUrlUpdateFrequency
from kagglesdk.datasets.types.dataset_types import StorageLocation
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.models.types.model_enums import ModelFramework, UnifiedModelGatingStatus
from typing import Optional, List, Dict

class BigqueryInfo(KaggleObject):
  r"""
  Attributes:
    project_id (str)
    dataset_id (str)
    source_last_modified_date (datetime)
      Last modified time from dataset as reported by Big Query service
  """

  def __init__(self):
    self._project_id = None
    self._dataset_id = None
    self._source_last_modified_date = None
    self._freeze()

  @property
  def project_id(self) -> str:
    return self._project_id or ""

  @project_id.setter
  def project_id(self, project_id: Optional[str]):
    if project_id is None:
      del self.project_id
      return
    if not isinstance(project_id, str):
      raise TypeError('project_id must be of type str')
    self._project_id = project_id

  @property
  def dataset_id(self) -> str:
    return self._dataset_id or ""

  @dataset_id.setter
  def dataset_id(self, dataset_id: Optional[str]):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, str):
      raise TypeError('dataset_id must be of type str')
    self._dataset_id = dataset_id

  @property
  def source_last_modified_date(self) -> datetime:
    """Last modified time from dataset as reported by Big Query service"""
    return self._source_last_modified_date

  @source_last_modified_date.setter
  def source_last_modified_date(self, source_last_modified_date: datetime):
    if source_last_modified_date is None:
      del self.source_last_modified_date
      return
    if not isinstance(source_last_modified_date, datetime):
      raise TypeError('source_last_modified_date must be of type datetime')
    self._source_last_modified_date = source_last_modified_date


class BigquerySnapshotInfo(KaggleObject):
  r"""
  List of tables in a big query dataset at a given point in time
  This is a snapshot because the tables and table schema does change over time

  Attributes:
    source_last_modified_date (datetime)
    bigquery_tables (TableCollection)
  """

  def __init__(self):
    self._source_last_modified_date = None
    self._bigquery_tables = None
    self._freeze()

  @property
  def source_last_modified_date(self) -> datetime:
    return self._source_last_modified_date

  @source_last_modified_date.setter
  def source_last_modified_date(self, source_last_modified_date: datetime):
    if source_last_modified_date is None:
      del self.source_last_modified_date
      return
    if not isinstance(source_last_modified_date, datetime):
      raise TypeError('source_last_modified_date must be of type datetime')
    self._source_last_modified_date = source_last_modified_date

  @property
  def bigquery_tables(self) -> Optional['TableCollection']:
    return self._bigquery_tables

  @bigquery_tables.setter
  def bigquery_tables(self, bigquery_tables: Optional['TableCollection']):
    if bigquery_tables is None:
      del self.bigquery_tables
      return
    if not isinstance(bigquery_tables, TableCollection):
      raise TypeError('bigquery_tables must be of type TableCollection')
    self._bigquery_tables = bigquery_tables


class BooleanMetrics(KaggleObject):
  r"""
  Attributes:
    true_count (int)
    false_count (int)
  """

  def __init__(self):
    self._true_count = 0
    self._false_count = 0
    self._freeze()

  @property
  def true_count(self) -> int:
    return self._true_count

  @true_count.setter
  def true_count(self, true_count: int):
    if true_count is None:
      del self.true_count
      return
    if not isinstance(true_count, int):
      raise TypeError('true_count must be of type int')
    self._true_count = true_count

  @property
  def false_count(self) -> int:
    return self._false_count

  @false_count.setter
  def false_count(self, false_count: int):
    if false_count is None:
      del self.false_count
      return
    if not isinstance(false_count, int):
      raise TypeError('false_count must be of type int')
    self._false_count = false_count


class BooleanMetricsComputedFields(KaggleObject):
  r"""
  Attributes:
    histogram (Histogram)
  """

  def __init__(self):
    self._histogram = None
    self._freeze()

  @property
  def histogram(self) -> Optional['Histogram']:
    return self._histogram

  @histogram.setter
  def histogram(self, histogram: Optional['Histogram']):
    if histogram is None:
      del self.histogram
      return
    if not isinstance(histogram, Histogram):
      raise TypeError('histogram must be of type Histogram')
    self._histogram = histogram


class ColumnSummaryInfo(KaggleObject):
  r"""
  Attributes:
    column_types (ColumnTypeSummaryInfo)
    sample_column_names (str)
  """

  def __init__(self):
    self._column_types = []
    self._sample_column_names = []
    self._freeze()

  @property
  def column_types(self) -> Optional[List[Optional['ColumnTypeSummaryInfo']]]:
    return self._column_types

  @column_types.setter
  def column_types(self, column_types: Optional[List[Optional['ColumnTypeSummaryInfo']]]):
    if column_types is None:
      del self.column_types
      return
    if not isinstance(column_types, list):
      raise TypeError('column_types must be of type list')
    if not all([isinstance(t, ColumnTypeSummaryInfo) for t in column_types]):
      raise TypeError('column_types must contain only items of type ColumnTypeSummaryInfo')
    self._column_types = column_types

  @property
  def sample_column_names(self) -> Optional[List[str]]:
    return self._sample_column_names

  @sample_column_names.setter
  def sample_column_names(self, sample_column_names: Optional[List[str]]):
    if sample_column_names is None:
      del self.sample_column_names
      return
    if not isinstance(sample_column_names, list):
      raise TypeError('sample_column_names must be of type list')
    if not all([isinstance(t, str) for t in sample_column_names]):
      raise TypeError('sample_column_names must contain only items of type str')
    self._sample_column_names = sample_column_names


class ColumnSummaryInfoComputedFields(KaggleObject):
  r"""
  Attributes:
    total_column_count (int)
  """

  def __init__(self):
    self._total_column_count = 0
    self._freeze()

  @property
  def total_column_count(self) -> int:
    return self._total_column_count

  @total_column_count.setter
  def total_column_count(self, total_column_count: int):
    if total_column_count is None:
      del self.total_column_count
      return
    if not isinstance(total_column_count, int):
      raise TypeError('total_column_count must be of type int')
    self._total_column_count = total_column_count


class ColumnTypeSummaryInfo(KaggleObject):
  r"""
  Attributes:
    column_type (str)
    column_count (int)
    row_count (int)
  """

  def __init__(self):
    self._column_type = None
    self._column_count = 0
    self._row_count = 0
    self._freeze()

  @property
  def column_type(self) -> str:
    return self._column_type or ""

  @column_type.setter
  def column_type(self, column_type: Optional[str]):
    if column_type is None:
      del self.column_type
      return
    if not isinstance(column_type, str):
      raise TypeError('column_type must be of type str')
    self._column_type = column_type

  @property
  def column_count(self) -> int:
    return self._column_count

  @column_count.setter
  def column_count(self, column_count: int):
    if column_count is None:
      del self.column_count
      return
    if not isinstance(column_count, int):
      raise TypeError('column_count must be of type int')
    self._column_count = column_count

  @property
  def row_count(self) -> int:
    return self._row_count

  @row_count.setter
  def row_count(self, row_count: int):
    if row_count is None:
      del self.row_count
      return
    if not isinstance(row_count, int):
      raise TypeError('row_count must be of type int')
    self._row_count = row_count


class ColumnUpdateInfo(KaggleObject):
  r"""
  Attributes:
    firestore_path (str)
    description (str)
    type (HarmonizedDataType)
    extended_type (ExtendedDataType)
  """

  def __init__(self):
    self._firestore_path = ""
    self._description = ""
    self._type = HarmonizedDataType.STRING
    self._extended_type = ExtendedDataType.EXTENDED_DATA_TYPE_UNSPECIFIED
    self._freeze()

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
  def description(self) -> str:
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def type(self) -> 'HarmonizedDataType':
    return self._type

  @type.setter
  def type(self, type: 'HarmonizedDataType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HarmonizedDataType):
      raise TypeError('type must be of type HarmonizedDataType')
    self._type = type

  @property
  def extended_type(self) -> 'ExtendedDataType':
    return self._extended_type

  @extended_type.setter
  def extended_type(self, extended_type: 'ExtendedDataType'):
    if extended_type is None:
      del self.extended_type
      return
    if not isinstance(extended_type, ExtendedDataType):
      raise TypeError('extended_type must be of type ExtendedDataType')
    self._extended_type = extended_type


class CompetitionInfo(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_slug (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._competition_slug = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def competition_slug(self) -> str:
    return self._competition_slug or ""

  @competition_slug.setter
  def competition_slug(self, competition_slug: Optional[str]):
    if competition_slug is None:
      del self.competition_slug
      return
    if not isinstance(competition_slug, str):
      raise TypeError('competition_slug must be of type str')
    self._competition_slug = competition_slug


class CompressionInfo(KaggleObject):
  r"""
  Attributes:
    filename (str)
    file_extension (str)
    file_size (int)
    content_encoding (str)
    content_md5 (str)
    archive_gcs_url (str)
    creation_last_update (datetime)
    creation_percent_complete (float)
  """

  def __init__(self):
    self._filename = None
    self._file_extension = None
    self._file_size = 0
    self._content_encoding = None
    self._content_md5 = None
    self._archive_gcs_url = None
    self._creation_last_update = None
    self._creation_percent_complete = None
    self._freeze()

  @property
  def filename(self) -> str:
    return self._filename or ""

  @filename.setter
  def filename(self, filename: Optional[str]):
    if filename is None:
      del self.filename
      return
    if not isinstance(filename, str):
      raise TypeError('filename must be of type str')
    self._filename = filename

  @property
  def file_extension(self) -> str:
    return self._file_extension or ""

  @file_extension.setter
  def file_extension(self, file_extension: Optional[str]):
    if file_extension is None:
      del self.file_extension
      return
    if not isinstance(file_extension, str):
      raise TypeError('file_extension must be of type str')
    self._file_extension = file_extension

  @property
  def file_size(self) -> int:
    return self._file_size

  @file_size.setter
  def file_size(self, file_size: int):
    if file_size is None:
      del self.file_size
      return
    if not isinstance(file_size, int):
      raise TypeError('file_size must be of type int')
    self._file_size = file_size

  @property
  def content_encoding(self) -> str:
    return self._content_encoding or ""

  @content_encoding.setter
  def content_encoding(self, content_encoding: Optional[str]):
    if content_encoding is None:
      del self.content_encoding
      return
    if not isinstance(content_encoding, str):
      raise TypeError('content_encoding must be of type str')
    self._content_encoding = content_encoding

  @property
  def content_md5(self) -> str:
    return self._content_md5 or ""

  @content_md5.setter
  def content_md5(self, content_md5: Optional[str]):
    if content_md5 is None:
      del self.content_md5
      return
    if not isinstance(content_md5, str):
      raise TypeError('content_md5 must be of type str')
    self._content_md5 = content_md5

  @property
  def archive_gcs_url(self) -> str:
    return self._archive_gcs_url or ""

  @archive_gcs_url.setter
  def archive_gcs_url(self, archive_gcs_url: Optional[str]):
    if archive_gcs_url is None:
      del self.archive_gcs_url
      return
    if not isinstance(archive_gcs_url, str):
      raise TypeError('archive_gcs_url must be of type str')
    self._archive_gcs_url = archive_gcs_url

  @property
  def creation_last_update(self) -> datetime:
    return self._creation_last_update

  @creation_last_update.setter
  def creation_last_update(self, creation_last_update: datetime):
    if creation_last_update is None:
      del self.creation_last_update
      return
    if not isinstance(creation_last_update, datetime):
      raise TypeError('creation_last_update must be of type datetime')
    self._creation_last_update = creation_last_update

  @property
  def creation_percent_complete(self) -> float:
    return self._creation_percent_complete or 0.0

  @creation_percent_complete.setter
  def creation_percent_complete(self, creation_percent_complete: Optional[float]):
    if creation_percent_complete is None:
      del self.creation_percent_complete
      return
    if not isinstance(creation_percent_complete, float):
      raise TypeError('creation_percent_complete must be of type float')
    self._creation_percent_complete = creation_percent_complete


class ContainerInfo(KaggleObject):
  r"""
  Attributes:
    total_children (int)
    count (int)
  """

  def __init__(self):
    self._total_children = 0
    self._count = 0
    self._freeze()

  @property
  def total_children(self) -> int:
    return self._total_children

  @total_children.setter
  def total_children(self, total_children: int):
    if total_children is None:
      del self.total_children
      return
    if not isinstance(total_children, int):
      raise TypeError('total_children must be of type int')
    self._total_children = total_children

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


class CountryMetrics(KaggleObject):
  r"""
  Attributes:
    counts (FrequencyCount)
    unique_value_count (int)
  """

  def __init__(self):
    self._counts = []
    self._unique_value_count = 0
    self._freeze()

  @property
  def counts(self) -> Optional[List[Optional['FrequencyCount']]]:
    return self._counts

  @counts.setter
  def counts(self, counts: Optional[List[Optional['FrequencyCount']]]):
    if counts is None:
      del self.counts
      return
    if not isinstance(counts, list):
      raise TypeError('counts must be of type list')
    if not all([isinstance(t, FrequencyCount) for t in counts]):
      raise TypeError('counts must contain only items of type FrequencyCount')
    self._counts = counts

  @property
  def unique_value_count(self) -> int:
    return self._unique_value_count

  @unique_value_count.setter
  def unique_value_count(self, unique_value_count: int):
    if unique_value_count is None:
      del self.unique_value_count
      return
    if not isinstance(unique_value_count, int):
      raise TypeError('unique_value_count must be of type int')
    self._unique_value_count = unique_value_count


class CountryMetricsComputedFields(KaggleObject):
  r"""
  Attributes:
    most_common_value (str)
    most_common_value_count (int)
  """

  def __init__(self):
    self._most_common_value = None
    self._most_common_value_count = 0
    self._freeze()

  @property
  def most_common_value(self) -> str:
    return self._most_common_value or ""

  @most_common_value.setter
  def most_common_value(self, most_common_value: Optional[str]):
    if most_common_value is None:
      del self.most_common_value
      return
    if not isinstance(most_common_value, str):
      raise TypeError('most_common_value must be of type str')
    self._most_common_value = most_common_value

  @property
  def most_common_value_count(self) -> int:
    return self._most_common_value_count

  @most_common_value_count.setter
  def most_common_value_count(self, most_common_value_count: int):
    if most_common_value_count is None:
      del self.most_common_value_count
      return
    if not isinstance(most_common_value_count, int):
      raise TypeError('most_common_value_count must be of type int')
    self._most_common_value_count = most_common_value_count


class CroissantInfo(KaggleObject):
  r"""
  Croissant-related information on the databundle version.

  Attributes:
    auto_gen_croissant_gcs_url (str)
      GCS Location of the auto-generated croissant JSON file. Only populated if
      auto-generated croissant file was written.
    auto_gen_croissant_create_time (datetime)
      For now, we'll put the date of Croissant generation in Firestore because it
      gives us an easy way to target which ones need updating (either due to bug
      fixes or schema updates). We could do this via GCS metadata but would incur
      another network call per object.
    auto_gen_croissant_total_size (int)
      Like the create time above, this is natively available in GCS metadata but
      spares having to look up the value for every DSDP render--where we'll use
      this value to determine if Croissant is safe to render directly on the
      webpage (~2.5MB limit).
    auto_gen_croissant_version_number (str)
      This is a value that is embedded in the Croissant file itself, but is
      useful to expose for querying/filtering purposes without having to inspect
      the file. Note that this is a string to account for semantic versioning
      (ex: 1.0.0)
  """

  def __init__(self):
    self._auto_gen_croissant_gcs_url = None
    self._auto_gen_croissant_create_time = None
    self._auto_gen_croissant_total_size = None
    self._auto_gen_croissant_version_number = None
    self._freeze()

  @property
  def auto_gen_croissant_gcs_url(self) -> str:
    r"""
    GCS Location of the auto-generated croissant JSON file. Only populated if
    auto-generated croissant file was written.
    """
    return self._auto_gen_croissant_gcs_url or ""

  @auto_gen_croissant_gcs_url.setter
  def auto_gen_croissant_gcs_url(self, auto_gen_croissant_gcs_url: Optional[str]):
    if auto_gen_croissant_gcs_url is None:
      del self.auto_gen_croissant_gcs_url
      return
    if not isinstance(auto_gen_croissant_gcs_url, str):
      raise TypeError('auto_gen_croissant_gcs_url must be of type str')
    self._auto_gen_croissant_gcs_url = auto_gen_croissant_gcs_url

  @property
  def auto_gen_croissant_create_time(self) -> datetime:
    r"""
    For now, we'll put the date of Croissant generation in Firestore because it
    gives us an easy way to target which ones need updating (either due to bug
    fixes or schema updates). We could do this via GCS metadata but would incur
    another network call per object.
    """
    return self._auto_gen_croissant_create_time or None

  @auto_gen_croissant_create_time.setter
  def auto_gen_croissant_create_time(self, auto_gen_croissant_create_time: Optional[datetime]):
    if auto_gen_croissant_create_time is None:
      del self.auto_gen_croissant_create_time
      return
    if not isinstance(auto_gen_croissant_create_time, datetime):
      raise TypeError('auto_gen_croissant_create_time must be of type datetime')
    self._auto_gen_croissant_create_time = auto_gen_croissant_create_time

  @property
  def auto_gen_croissant_total_size(self) -> int:
    r"""
    Like the create time above, this is natively available in GCS metadata but
    spares having to look up the value for every DSDP render--where we'll use
    this value to determine if Croissant is safe to render directly on the
    webpage (~2.5MB limit).
    """
    return self._auto_gen_croissant_total_size or 0

  @auto_gen_croissant_total_size.setter
  def auto_gen_croissant_total_size(self, auto_gen_croissant_total_size: Optional[int]):
    if auto_gen_croissant_total_size is None:
      del self.auto_gen_croissant_total_size
      return
    if not isinstance(auto_gen_croissant_total_size, int):
      raise TypeError('auto_gen_croissant_total_size must be of type int')
    self._auto_gen_croissant_total_size = auto_gen_croissant_total_size

  @property
  def auto_gen_croissant_version_number(self) -> str:
    r"""
    This is a value that is embedded in the Croissant file itself, but is
    useful to expose for querying/filtering purposes without having to inspect
    the file. Note that this is a string to account for semantic versioning
    (ex: 1.0.0)
    """
    return self._auto_gen_croissant_version_number or ""

  @auto_gen_croissant_version_number.setter
  def auto_gen_croissant_version_number(self, auto_gen_croissant_version_number: Optional[str]):
    if auto_gen_croissant_version_number is None:
      del self.auto_gen_croissant_version_number
      return
    if not isinstance(auto_gen_croissant_version_number, str):
      raise TypeError('auto_gen_croissant_version_number must be of type str')
    self._auto_gen_croissant_version_number = auto_gen_croissant_version_number


class Databundle(KaggleObject):
  r"""
  Attributes:
    databundle_info (DatabundleInfo)
    dataset_info (DatasetInfo)
    competition_info (CompetitionInfo)
    remote_datasource_info (RemoteDatasourceInfo)
    bigquery_info (BigqueryInfo)
    github_info (GithubInfo)
    model_instance_info (ModelInstanceInfo)
    hugging_face_info (HuggingFaceInfo)
  """

  def __init__(self):
    self._databundle_info = None
    self._dataset_info = None
    self._competition_info = None
    self._remote_datasource_info = None
    self._bigquery_info = None
    self._github_info = None
    self._model_instance_info = None
    self._hugging_face_info = None
    self._freeze()

  @property
  def databundle_info(self) -> Optional['DatabundleInfo']:
    return self._databundle_info

  @databundle_info.setter
  def databundle_info(self, databundle_info: Optional['DatabundleInfo']):
    if databundle_info is None:
      del self.databundle_info
      return
    if not isinstance(databundle_info, DatabundleInfo):
      raise TypeError('databundle_info must be of type DatabundleInfo')
    self._databundle_info = databundle_info

  @property
  def dataset_info(self) -> Optional['DatasetInfo']:
    return self._dataset_info

  @dataset_info.setter
  def dataset_info(self, dataset_info: Optional['DatasetInfo']):
    if dataset_info is None:
      del self.dataset_info
      return
    if not isinstance(dataset_info, DatasetInfo):
      raise TypeError('dataset_info must be of type DatasetInfo')
    self._dataset_info = dataset_info

  @property
  def competition_info(self) -> Optional['CompetitionInfo']:
    return self._competition_info

  @competition_info.setter
  def competition_info(self, competition_info: Optional['CompetitionInfo']):
    if competition_info is None:
      del self.competition_info
      return
    if not isinstance(competition_info, CompetitionInfo):
      raise TypeError('competition_info must be of type CompetitionInfo')
    self._competition_info = competition_info

  @property
  def model_instance_info(self) -> Optional['ModelInstanceInfo']:
    return self._model_instance_info

  @model_instance_info.setter
  def model_instance_info(self, model_instance_info: Optional['ModelInstanceInfo']):
    if model_instance_info is None:
      del self.model_instance_info
      return
    if not isinstance(model_instance_info, ModelInstanceInfo):
      raise TypeError('model_instance_info must be of type ModelInstanceInfo')
    self._model_instance_info = model_instance_info

  @property
  def remote_datasource_info(self) -> Optional['RemoteDatasourceInfo']:
    return self._remote_datasource_info

  @remote_datasource_info.setter
  def remote_datasource_info(self, remote_datasource_info: Optional['RemoteDatasourceInfo']):
    if remote_datasource_info is None:
      del self.remote_datasource_info
      return
    if not isinstance(remote_datasource_info, RemoteDatasourceInfo):
      raise TypeError('remote_datasource_info must be of type RemoteDatasourceInfo')
    self._remote_datasource_info = remote_datasource_info

  @property
  def bigquery_info(self) -> Optional['BigqueryInfo']:
    return self._bigquery_info

  @bigquery_info.setter
  def bigquery_info(self, bigquery_info: Optional['BigqueryInfo']):
    if bigquery_info is None:
      del self.bigquery_info
      return
    if not isinstance(bigquery_info, BigqueryInfo):
      raise TypeError('bigquery_info must be of type BigqueryInfo')
    self._bigquery_info = bigquery_info

  @property
  def github_info(self) -> Optional['GithubInfo']:
    return self._github_info

  @github_info.setter
  def github_info(self, github_info: Optional['GithubInfo']):
    if github_info is None:
      del self.github_info
      return
    if not isinstance(github_info, GithubInfo):
      raise TypeError('github_info must be of type GithubInfo')
    self._github_info = github_info

  @property
  def hugging_face_info(self) -> Optional['HuggingFaceInfo']:
    return self._hugging_face_info

  @hugging_face_info.setter
  def hugging_face_info(self, hugging_face_info: Optional['HuggingFaceInfo']):
    if hugging_face_info is None:
      del self.hugging_face_info
      return
    if not isinstance(hugging_face_info, HuggingFaceInfo):
      raise TypeError('hugging_face_info must be of type HuggingFaceInfo')
    self._hugging_face_info = hugging_face_info


class DatabundleInfo(KaggleObject):
  r"""
  Attributes:
    current_databundle_version_id (int)
    databundle_type (DatabundleType)
    diff_type (DatabundleDiffType)
    creation_date (datetime)
    creator_user_id (int)
    removal_date (datetime)
    current_good_version_key (str)
      We should only set the CurrentGoodVersionKey if the version
      has been processed successfully, leave null if first version
      is still in progress or if all version are bad.
    lastest_version_key (str)
      This always points to the latest version regardless of status
    versions (DatabundleVersionCollection)
  """

  def __init__(self):
    self._current_databundle_version_id = None
    self._databundle_type = DatabundleType.DATABUNDLE_TYPE_UNSPECIFIED
    self._diff_type = DatabundleDiffType.REALTIME
    self._creation_date = None
    self._creator_user_id = 0
    self._removal_date = None
    self._current_good_version_key = None
    self._lastest_version_key = None
    self._versions = None
    self._freeze()

  @property
  def current_databundle_version_id(self) -> int:
    return self._current_databundle_version_id or 0

  @current_databundle_version_id.setter
  def current_databundle_version_id(self, current_databundle_version_id: Optional[int]):
    if current_databundle_version_id is None:
      del self.current_databundle_version_id
      return
    if not isinstance(current_databundle_version_id, int):
      raise TypeError('current_databundle_version_id must be of type int')
    self._current_databundle_version_id = current_databundle_version_id

  @property
  def databundle_type(self) -> 'DatabundleType':
    return self._databundle_type

  @databundle_type.setter
  def databundle_type(self, databundle_type: 'DatabundleType'):
    if databundle_type is None:
      del self.databundle_type
      return
    if not isinstance(databundle_type, DatabundleType):
      raise TypeError('databundle_type must be of type DatabundleType')
    self._databundle_type = databundle_type

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
  def creation_date(self) -> datetime:
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date

  @property
  def creator_user_id(self) -> int:
    return self._creator_user_id

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: int):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id

  @property
  def removal_date(self) -> datetime:
    return self._removal_date

  @removal_date.setter
  def removal_date(self, removal_date: datetime):
    if removal_date is None:
      del self.removal_date
      return
    if not isinstance(removal_date, datetime):
      raise TypeError('removal_date must be of type datetime')
    self._removal_date = removal_date

  @property
  def current_good_version_key(self) -> str:
    r"""
    We should only set the CurrentGoodVersionKey if the version
    has been processed successfully, leave null if first version
    is still in progress or if all version are bad.
    """
    return self._current_good_version_key or ""

  @current_good_version_key.setter
  def current_good_version_key(self, current_good_version_key: Optional[str]):
    if current_good_version_key is None:
      del self.current_good_version_key
      return
    if not isinstance(current_good_version_key, str):
      raise TypeError('current_good_version_key must be of type str')
    self._current_good_version_key = current_good_version_key

  @property
  def lastest_version_key(self) -> str:
    """This always points to the latest version regardless of status"""
    return self._lastest_version_key or ""

  @lastest_version_key.setter
  def lastest_version_key(self, lastest_version_key: Optional[str]):
    if lastest_version_key is None:
      del self.lastest_version_key
      return
    if not isinstance(lastest_version_key, str):
      raise TypeError('lastest_version_key must be of type str')
    self._lastest_version_key = lastest_version_key

  @property
  def versions(self) -> Optional['DatabundleVersionCollection']:
    return self._versions

  @versions.setter
  def versions(self, versions: Optional['DatabundleVersionCollection']):
    if versions is None:
      del self.versions
      return
    if not isinstance(versions, DatabundleVersionCollection):
      raise TypeError('versions must be of type DatabundleVersionCollection')
    self._versions = versions


class DatabundleOwnerCompetitionInfo(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    scope (str)
  """

  def __init__(self):
    self._competition_id = 0
    self._scope = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def scope(self) -> str:
    return self._scope or ""

  @scope.setter
  def scope(self, scope: Optional[str]):
    if scope is None:
      del self.scope
      return
    if not isinstance(scope, str):
      raise TypeError('scope must be of type str')
    self._scope = scope


class DatabundleOwnerDatasetInfo(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    dataset_version_id (int)
    scope (str)
      security token for accessing dataview service
  """

  def __init__(self):
    self._dataset_id = 0
    self._dataset_version_id = 0
    self._scope = None
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

  @property
  def scope(self) -> str:
    """security token for accessing dataview service"""
    return self._scope or ""

  @scope.setter
  def scope(self, scope: Optional[str]):
    if scope is None:
      del self.scope
      return
    if not isinstance(scope, str):
      raise TypeError('scope must be of type str')
    self._scope = scope


class DatabundleOwnerInfo(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
    dataset (DatabundleOwnerDatasetInfo)
    competition (DatabundleOwnerCompetitionInfo)
    kernel (DatabundleOwnerKernelInfo)
    previews_disabled (bool)
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._dataset = None
    self._competition = None
    self._kernel = None
    self._previews_disabled = False
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

  @property
  def dataset(self) -> Optional['DatabundleOwnerDatasetInfo']:
    return self._dataset

  @dataset.setter
  def dataset(self, dataset: Optional['DatabundleOwnerDatasetInfo']):
    if dataset is None:
      del self.dataset
      return
    if not isinstance(dataset, DatabundleOwnerDatasetInfo):
      raise TypeError('dataset must be of type DatabundleOwnerDatasetInfo')
    self._dataset = dataset

  @property
  def competition(self) -> Optional['DatabundleOwnerCompetitionInfo']:
    return self._competition

  @competition.setter
  def competition(self, competition: Optional['DatabundleOwnerCompetitionInfo']):
    if competition is None:
      del self.competition
      return
    if not isinstance(competition, DatabundleOwnerCompetitionInfo):
      raise TypeError('competition must be of type DatabundleOwnerCompetitionInfo')
    self._competition = competition

  @property
  def kernel(self) -> Optional['DatabundleOwnerKernelInfo']:
    return self._kernel

  @kernel.setter
  def kernel(self, kernel: Optional['DatabundleOwnerKernelInfo']):
    if kernel is None:
      del self.kernel
      return
    if not isinstance(kernel, DatabundleOwnerKernelInfo):
      raise TypeError('kernel must be of type DatabundleOwnerKernelInfo')
    self._kernel = kernel

  @property
  def previews_disabled(self) -> bool:
    return self._previews_disabled

  @previews_disabled.setter
  def previews_disabled(self, previews_disabled: bool):
    if previews_disabled is None:
      del self.previews_disabled
      return
    if not isinstance(previews_disabled, bool):
      raise TypeError('previews_disabled must be of type bool')
    self._previews_disabled = previews_disabled


class DatabundleOwnerKernelInfo(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    kernel_version_id (int)
    scope (str)
  """

  def __init__(self):
    self._kernel_id = 0
    self._kernel_version_id = 0
    self._scope = None
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
  def kernel_version_id(self) -> int:
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def scope(self) -> str:
    return self._scope or ""

  @scope.setter
  def scope(self, scope: Optional[str]):
    if scope is None:
      del self.scope
      return
    if not isinstance(scope, str):
      raise TypeError('scope must be of type str')
    self._scope = scope


class DatabundleVerificationInfo(KaggleObject):
  r"""
  Object holding information that is necessary on the backend to verify the
  user has access to a particular databundle. Included in many DataExplorer
  requests.

  Attributes:
    databundle_version_id (int)
    competition_id (int)
    dataset_id (int)
    dataset_hash_link (str)
    private_databundle_competition_id (int)
    model_instance_version_id (int)
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._competition_id = None
    self._dataset_id = None
    self._dataset_hash_link = None
    self._private_databundle_competition_id = None
    self._model_instance_version_id = None
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id

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
  def dataset_hash_link(self) -> str:
    return self._dataset_hash_link or ""

  @dataset_hash_link.setter
  def dataset_hash_link(self, dataset_hash_link: Optional[str]):
    if dataset_hash_link is None:
      del self.dataset_hash_link
      return
    if not isinstance(dataset_hash_link, str):
      raise TypeError('dataset_hash_link must be of type str')
    self._dataset_hash_link = dataset_hash_link

  @property
  def private_databundle_competition_id(self) -> int:
    return self._private_databundle_competition_id or 0

  @private_databundle_competition_id.setter
  def private_databundle_competition_id(self, private_databundle_competition_id: Optional[int]):
    if private_databundle_competition_id is None:
      del self.private_databundle_competition_id
      return
    if not isinstance(private_databundle_competition_id, int):
      raise TypeError('private_databundle_competition_id must be of type int')
    self._private_databundle_competition_id = private_databundle_competition_id

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id or 0

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: Optional[int]):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    self._model_instance_version_id = model_instance_version_id


class DatabundleVersion(KaggleObject):
  r"""
  NextId: 17

  Attributes:
    databundle_version_info (DatabundleVersionInfo)
    dataset_version_info (DatasetVersionInfo)
    status_info (StatusInfo)
    exception_info (ExceptionInfo)
    fileset_info (DirectoryInfo)
    original_compression_info (CompressionInfo)
    bundle_compression_info (CompressionInfo)
    bigquery_snapshot_info (BigquerySnapshotInfo)
    storage_info (StorageInfo)
    file_summary_info (FileSummaryInfo)
    column_summary_info (ColumnSummaryInfo)
    external_copy_info (ExternalCopyInfo)
    original_remote_url_info (OriginalRemoteUrlInfo)
    model_instance_version_info (ModelInstanceVersionInfo)
    croissant_info (CroissantInfo)
    hash_info (HashInfo)
  """

  def __init__(self):
    self._databundle_version_info = None
    self._dataset_version_info = None
    self._status_info = None
    self._exception_info = None
    self._fileset_info = None
    self._original_compression_info = None
    self._bundle_compression_info = None
    self._bigquery_snapshot_info = None
    self._storage_info = None
    self._file_summary_info = None
    self._column_summary_info = None
    self._external_copy_info = None
    self._original_remote_url_info = None
    self._model_instance_version_info = None
    self._croissant_info = None
    self._hash_info = None
    self._freeze()

  @property
  def databundle_version_info(self) -> Optional['DatabundleVersionInfo']:
    return self._databundle_version_info

  @databundle_version_info.setter
  def databundle_version_info(self, databundle_version_info: Optional['DatabundleVersionInfo']):
    if databundle_version_info is None:
      del self.databundle_version_info
      return
    if not isinstance(databundle_version_info, DatabundleVersionInfo):
      raise TypeError('databundle_version_info must be of type DatabundleVersionInfo')
    self._databundle_version_info = databundle_version_info

  @property
  def dataset_version_info(self) -> Optional['DatasetVersionInfo']:
    return self._dataset_version_info

  @dataset_version_info.setter
  def dataset_version_info(self, dataset_version_info: Optional['DatasetVersionInfo']):
    if dataset_version_info is None:
      del self.dataset_version_info
      return
    if not isinstance(dataset_version_info, DatasetVersionInfo):
      raise TypeError('dataset_version_info must be of type DatasetVersionInfo')
    self._dataset_version_info = dataset_version_info

  @property
  def model_instance_version_info(self) -> Optional['ModelInstanceVersionInfo']:
    return self._model_instance_version_info

  @model_instance_version_info.setter
  def model_instance_version_info(self, model_instance_version_info: Optional['ModelInstanceVersionInfo']):
    if model_instance_version_info is None:
      del self.model_instance_version_info
      return
    if not isinstance(model_instance_version_info, ModelInstanceVersionInfo):
      raise TypeError('model_instance_version_info must be of type ModelInstanceVersionInfo')
    self._model_instance_version_info = model_instance_version_info

  @property
  def status_info(self) -> Optional['StatusInfo']:
    return self._status_info

  @status_info.setter
  def status_info(self, status_info: Optional['StatusInfo']):
    if status_info is None:
      del self.status_info
      return
    if not isinstance(status_info, StatusInfo):
      raise TypeError('status_info must be of type StatusInfo')
    self._status_info = status_info

  @property
  def exception_info(self) -> Optional['ExceptionInfo']:
    return self._exception_info

  @exception_info.setter
  def exception_info(self, exception_info: Optional['ExceptionInfo']):
    if exception_info is None:
      del self.exception_info
      return
    if not isinstance(exception_info, ExceptionInfo):
      raise TypeError('exception_info must be of type ExceptionInfo')
    self._exception_info = exception_info

  @property
  def fileset_info(self) -> Optional['DirectoryInfo']:
    return self._fileset_info

  @fileset_info.setter
  def fileset_info(self, fileset_info: Optional['DirectoryInfo']):
    if fileset_info is None:
      del self.fileset_info
      return
    if not isinstance(fileset_info, DirectoryInfo):
      raise TypeError('fileset_info must be of type DirectoryInfo')
    self._fileset_info = fileset_info

  @property
  def original_compression_info(self) -> Optional['CompressionInfo']:
    return self._original_compression_info

  @original_compression_info.setter
  def original_compression_info(self, original_compression_info: Optional['CompressionInfo']):
    if original_compression_info is None:
      del self.original_compression_info
      return
    if not isinstance(original_compression_info, CompressionInfo):
      raise TypeError('original_compression_info must be of type CompressionInfo')
    self._original_compression_info = original_compression_info

  @property
  def bundle_compression_info(self) -> Optional['CompressionInfo']:
    return self._bundle_compression_info

  @bundle_compression_info.setter
  def bundle_compression_info(self, bundle_compression_info: Optional['CompressionInfo']):
    if bundle_compression_info is None:
      del self.bundle_compression_info
      return
    if not isinstance(bundle_compression_info, CompressionInfo):
      raise TypeError('bundle_compression_info must be of type CompressionInfo')
    self._bundle_compression_info = bundle_compression_info

  @property
  def bigquery_snapshot_info(self) -> Optional['BigquerySnapshotInfo']:
    return self._bigquery_snapshot_info

  @bigquery_snapshot_info.setter
  def bigquery_snapshot_info(self, bigquery_snapshot_info: Optional['BigquerySnapshotInfo']):
    if bigquery_snapshot_info is None:
      del self.bigquery_snapshot_info
      return
    if not isinstance(bigquery_snapshot_info, BigquerySnapshotInfo):
      raise TypeError('bigquery_snapshot_info must be of type BigquerySnapshotInfo')
    self._bigquery_snapshot_info = bigquery_snapshot_info

  @property
  def storage_info(self) -> Optional['StorageInfo']:
    return self._storage_info

  @storage_info.setter
  def storage_info(self, storage_info: Optional['StorageInfo']):
    if storage_info is None:
      del self.storage_info
      return
    if not isinstance(storage_info, StorageInfo):
      raise TypeError('storage_info must be of type StorageInfo')
    self._storage_info = storage_info

  @property
  def file_summary_info(self) -> Optional['FileSummaryInfo']:
    return self._file_summary_info

  @file_summary_info.setter
  def file_summary_info(self, file_summary_info: Optional['FileSummaryInfo']):
    if file_summary_info is None:
      del self.file_summary_info
      return
    if not isinstance(file_summary_info, FileSummaryInfo):
      raise TypeError('file_summary_info must be of type FileSummaryInfo')
    self._file_summary_info = file_summary_info

  @property
  def column_summary_info(self) -> Optional['ColumnSummaryInfo']:
    return self._column_summary_info

  @column_summary_info.setter
  def column_summary_info(self, column_summary_info: Optional['ColumnSummaryInfo']):
    if column_summary_info is None:
      del self.column_summary_info
      return
    if not isinstance(column_summary_info, ColumnSummaryInfo):
      raise TypeError('column_summary_info must be of type ColumnSummaryInfo')
    self._column_summary_info = column_summary_info

  @property
  def external_copy_info(self) -> Optional['ExternalCopyInfo']:
    return self._external_copy_info

  @external_copy_info.setter
  def external_copy_info(self, external_copy_info: Optional['ExternalCopyInfo']):
    if external_copy_info is None:
      del self.external_copy_info
      return
    if not isinstance(external_copy_info, ExternalCopyInfo):
      raise TypeError('external_copy_info must be of type ExternalCopyInfo')
    self._external_copy_info = external_copy_info

  @property
  def original_remote_url_info(self) -> Optional['OriginalRemoteUrlInfo']:
    return self._original_remote_url_info

  @original_remote_url_info.setter
  def original_remote_url_info(self, original_remote_url_info: Optional['OriginalRemoteUrlInfo']):
    if original_remote_url_info is None:
      del self.original_remote_url_info
      return
    if not isinstance(original_remote_url_info, OriginalRemoteUrlInfo):
      raise TypeError('original_remote_url_info must be of type OriginalRemoteUrlInfo')
    self._original_remote_url_info = original_remote_url_info

  @property
  def croissant_info(self) -> Optional['CroissantInfo']:
    return self._croissant_info

  @croissant_info.setter
  def croissant_info(self, croissant_info: Optional['CroissantInfo']):
    if croissant_info is None:
      del self.croissant_info
      return
    if not isinstance(croissant_info, CroissantInfo):
      raise TypeError('croissant_info must be of type CroissantInfo')
    self._croissant_info = croissant_info

  @property
  def hash_info(self) -> Optional['HashInfo']:
    return self._hash_info

  @hash_info.setter
  def hash_info(self, hash_info: Optional['HashInfo']):
    if hash_info is None:
      del self.hash_info
      return
    if not isinstance(hash_info, HashInfo):
      raise TypeError('hash_info must be of type HashInfo')
    self._hash_info = hash_info


class DatabundleVersionCollection(KaggleObject):
  r"""
  """

  pass

class DatabundleVersionCollectionContainerInfo(KaggleObject):
  r"""
  Attributes:
    children (DatabundleVersion)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['DatabundleVersion']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['DatabundleVersion']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, DatabundleVersion) for t in children]):
      raise TypeError('children must contain only items of type DatabundleVersion')
    self._children = children


class DatabundleVersionInfo(KaggleObject):
  r"""
  Attributes:
    version_number (int)
    version_notes (str)
    creator_user_id (int)
    creation_date (datetime)
    removal_date (datetime)
    databundle_version_type (DatabundleVersionType)
    object_type_count (int)
      Maps ObjectType to count
  """

  def __init__(self):
    self._version_number = 0
    self._version_notes = None
    self._creator_user_id = 0
    self._creation_date = None
    self._removal_date = None
    self._databundle_version_type = DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED
    self._object_type_count = {}
    self._freeze()

  @property
  def version_number(self) -> int:
    return self._version_number

  @version_number.setter
  def version_number(self, version_number: int):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def version_notes(self) -> str:
    return self._version_notes or ""

  @version_notes.setter
  def version_notes(self, version_notes: Optional[str]):
    if version_notes is None:
      del self.version_notes
      return
    if not isinstance(version_notes, str):
      raise TypeError('version_notes must be of type str')
    self._version_notes = version_notes

  @property
  def creator_user_id(self) -> int:
    return self._creator_user_id

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: int):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id

  @property
  def creation_date(self) -> datetime:
    return self._creation_date

  @creation_date.setter
  def creation_date(self, creation_date: datetime):
    if creation_date is None:
      del self.creation_date
      return
    if not isinstance(creation_date, datetime):
      raise TypeError('creation_date must be of type datetime')
    self._creation_date = creation_date

  @property
  def removal_date(self) -> datetime:
    return self._removal_date

  @removal_date.setter
  def removal_date(self, removal_date: datetime):
    if removal_date is None:
      del self.removal_date
      return
    if not isinstance(removal_date, datetime):
      raise TypeError('removal_date must be of type datetime')
    self._removal_date = removal_date

  @property
  def databundle_version_type(self) -> 'DatabundleVersionType':
    return self._databundle_version_type

  @databundle_version_type.setter
  def databundle_version_type(self, databundle_version_type: 'DatabundleVersionType'):
    if databundle_version_type is None:
      del self.databundle_version_type
      return
    if not isinstance(databundle_version_type, DatabundleVersionType):
      raise TypeError('databundle_version_type must be of type DatabundleVersionType')
    self._databundle_version_type = databundle_version_type

  @property
  def object_type_count(self) -> Optional[Dict[int, int]]:
    """Maps ObjectType to count"""
    return self._object_type_count

  @object_type_count.setter
  def object_type_count(self, object_type_count: Optional[Dict[int, int]]):
    if object_type_count is None:
      del self.object_type_count
      return
    if not isinstance(object_type_count, dict):
      raise TypeError('object_type_count must be of type dict')
    if not all([isinstance(v, int) for k, v in object_type_count]):
      raise TypeError('object_type_count must contain only items of type int')
    self._object_type_count = object_type_count


class DataObjectBaseInfo(KaggleObject):
  r"""
  This contains fields that are part of every 'DataObject'
  and in C# are part of the 'DataObject' base class. It's not called
  'DataObjectInfo' to avoid confusion with a Firestore type with
  that name.

  Attributes:
    type (ObjectType)
      Used by the frontend to decide which derived class it is.
    key (str)
      Unique identifier for the object.
    path (str)
      RelativePath + Key + ContainerName from parent object.
      This is used to find the subcollection that contains the object in
      firestore
    legacy_entity_id (int)
      DatabundleId, DatabundleVersionId, DatabundleVersionObjectId
      from sql server objects.
    relative_url (str)
      Relative path of this object relative to DatabundleVersion.
      This is intended to be used by UI to access the object as either
      {DatasetSlug}/{RelativeUrl} or
      {CompetitionSlug}/{RelativeUrl}
    name (str)
    description (str)
  """

  def __init__(self):
    self._type = ObjectType.OBJECT_TYPE_GENERIC
    self._key = ""
    self._path = ""
    self._legacy_entity_id = None
    self._relative_url = None
    self._name = ""
    self._description = None
    self._freeze()

  @property
  def type(self) -> 'ObjectType':
    """Used by the frontend to decide which derived class it is."""
    return self._type

  @type.setter
  def type(self, type: 'ObjectType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ObjectType):
      raise TypeError('type must be of type ObjectType')
    self._type = type

  @property
  def key(self) -> str:
    """Unique identifier for the object."""
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def path(self) -> str:
    r"""
    RelativePath + Key + ContainerName from parent object.
    This is used to find the subcollection that contains the object in
    firestore
    """
    return self._path

  @path.setter
  def path(self, path: str):
    if path is None:
      del self.path
      return
    if not isinstance(path, str):
      raise TypeError('path must be of type str')
    self._path = path

  @property
  def legacy_entity_id(self) -> int:
    r"""
    DatabundleId, DatabundleVersionId, DatabundleVersionObjectId
    from sql server objects.
    """
    return self._legacy_entity_id or 0

  @legacy_entity_id.setter
  def legacy_entity_id(self, legacy_entity_id: Optional[int]):
    if legacy_entity_id is None:
      del self.legacy_entity_id
      return
    if not isinstance(legacy_entity_id, int):
      raise TypeError('legacy_entity_id must be of type int')
    self._legacy_entity_id = legacy_entity_id

  @property
  def relative_url(self) -> str:
    r"""
    Relative path of this object relative to DatabundleVersion.
    This is intended to be used by UI to access the object as either
    {DatasetSlug}/{RelativeUrl} or
    {CompetitionSlug}/{RelativeUrl}
    """
    return self._relative_url or ""

  @relative_url.setter
  def relative_url(self, relative_url: Optional[str]):
    if relative_url is None:
      del self.relative_url
      return
    if not isinstance(relative_url, str):
      raise TypeError('relative_url must be of type str')
    self._relative_url = relative_url

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


class DatasetInfo(KaggleObject):
  r"""
  Attributes:
    dataset_id (int)
    dataset_slug (str)
    is_private (bool)
  """

  def __init__(self):
    self._dataset_id = 0
    self._dataset_slug = None
    self._is_private = False
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


class DatasetVersionInfo(KaggleObject):
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


class DataSource(KaggleObject):
  r"""
  Attributes:
    databundle (Databundle)
    databundle_version (DatabundleVersion)
    image_url (str)
    source_url (str)
    slug (str)
    mount_slug (str)
    last_updated (datetime)
    subtitle (str)
    source_type (DataSourceType)
    source_id (int)
    version_number (int)
    state (DataSourceState)
    kernel_output_info (KernelOutputInfo)
    model_info (DataSource.ModelInfo)
    can_edit (bool)
    is_pinned (bool)
  """

  class ModelGatingInfo(KaggleObject):
    r"""
    Attributes:
      is_agreement_gated (bool)
      is_license_gated (bool)
      gating_status (UnifiedModelGatingStatus)
    """

    def __init__(self):
      self._is_agreement_gated = None
      self._is_license_gated = None
      self._gating_status = None
      self._freeze()

    @property
    def is_agreement_gated(self) -> bool:
      return self._is_agreement_gated or False

    @is_agreement_gated.setter
    def is_agreement_gated(self, is_agreement_gated: Optional[bool]):
      if is_agreement_gated is None:
        del self.is_agreement_gated
        return
      if not isinstance(is_agreement_gated, bool):
        raise TypeError('is_agreement_gated must be of type bool')
      self._is_agreement_gated = is_agreement_gated

    @property
    def is_license_gated(self) -> bool:
      return self._is_license_gated or False

    @is_license_gated.setter
    def is_license_gated(self, is_license_gated: Optional[bool]):
      if is_license_gated is None:
        del self.is_license_gated
        return
      if not isinstance(is_license_gated, bool):
        raise TypeError('is_license_gated must be of type bool')
      self._is_license_gated = is_license_gated

    @property
    def gating_status(self) -> 'UnifiedModelGatingStatus':
      return self._gating_status or UnifiedModelGatingStatus.UNIFIED_MODEL_GATING_STATUS_UNSPECIFIED

    @gating_status.setter
    def gating_status(self, gating_status: Optional['UnifiedModelGatingStatus']):
      if gating_status is None:
        del self.gating_status
        return
      if not isinstance(gating_status, UnifiedModelGatingStatus):
        raise TypeError('gating_status must be of type UnifiedModelGatingStatus')
      self._gating_status = gating_status


  class ModelInfo(KaggleObject):
    r"""
    Attributes:
      is_tfhub_model (bool)
      model_framework (ModelFramework)
      license (License)
      can_use (bool)
      gating_info (DataSource.ModelGatingInfo)
    """

    def __init__(self):
      self._is_tfhub_model = False
      self._model_framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
      self._license = None
      self._can_use = None
      self._gating_info = None
      self._freeze()

    @property
    def is_tfhub_model(self) -> bool:
      return self._is_tfhub_model

    @is_tfhub_model.setter
    def is_tfhub_model(self, is_tfhub_model: bool):
      if is_tfhub_model is None:
        del self.is_tfhub_model
        return
      if not isinstance(is_tfhub_model, bool):
        raise TypeError('is_tfhub_model must be of type bool')
      self._is_tfhub_model = is_tfhub_model

    @property
    def model_framework(self) -> 'ModelFramework':
      return self._model_framework

    @model_framework.setter
    def model_framework(self, model_framework: 'ModelFramework'):
      if model_framework is None:
        del self.model_framework
        return
      if not isinstance(model_framework, ModelFramework):
        raise TypeError('model_framework must be of type ModelFramework')
      self._model_framework = model_framework

    @property
    def license(self) -> Optional['License']:
      return self._license

    @license.setter
    def license(self, license: Optional['License']):
      if license is None:
        del self.license
        return
      if not isinstance(license, License):
        raise TypeError('license must be of type License')
      self._license = license

    @property
    def can_use(self) -> bool:
      return self._can_use or False

    @can_use.setter
    def can_use(self, can_use: Optional[bool]):
      if can_use is None:
        del self.can_use
        return
      if not isinstance(can_use, bool):
        raise TypeError('can_use must be of type bool')
      self._can_use = can_use

    @property
    def gating_info(self) -> Optional['DataSource.ModelGatingInfo']:
      return self._gating_info or None

    @gating_info.setter
    def gating_info(self, gating_info: Optional[Optional['DataSource.ModelGatingInfo']]):
      if gating_info is None:
        del self.gating_info
        return
      if not isinstance(gating_info, DataSource.ModelGatingInfo):
        raise TypeError('gating_info must be of type DataSource.ModelGatingInfo')
      self._gating_info = gating_info


  def __init__(self):
    self._databundle = None
    self._databundle_version = None
    self._image_url = ""
    self._source_url = ""
    self._slug = None
    self._mount_slug = None
    self._last_updated = None
    self._subtitle = None
    self._source_type = DataSourceType.DATA_SOURCE_TYPE_UNSPECIFIED
    self._source_id = 0
    self._version_number = None
    self._state = DataSourceState.DATA_SOURCE_STATE_PUBLIC
    self._kernel_output_info = None
    self._model_info = None
    self._can_edit = None
    self._is_pinned = None
    self._freeze()

  @property
  def databundle(self) -> Optional['Databundle']:
    return self._databundle

  @databundle.setter
  def databundle(self, databundle: Optional['Databundle']):
    if databundle is None:
      del self.databundle
      return
    if not isinstance(databundle, Databundle):
      raise TypeError('databundle must be of type Databundle')
    self._databundle = databundle

  @property
  def databundle_version(self) -> Optional['DatabundleVersion']:
    return self._databundle_version

  @databundle_version.setter
  def databundle_version(self, databundle_version: Optional['DatabundleVersion']):
    if databundle_version is None:
      del self.databundle_version
      return
    if not isinstance(databundle_version, DatabundleVersion):
      raise TypeError('databundle_version must be of type DatabundleVersion')
    self._databundle_version = databundle_version

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
  def source_url(self) -> str:
    return self._source_url

  @source_url.setter
  def source_url(self, source_url: str):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    self._source_url = source_url

  @property
  def slug(self) -> str:
    return self._slug or ""

  @slug.setter
  def slug(self, slug: Optional[str]):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def mount_slug(self) -> str:
    return self._mount_slug or ""

  @mount_slug.setter
  def mount_slug(self, mount_slug: Optional[str]):
    if mount_slug is None:
      del self.mount_slug
      return
    if not isinstance(mount_slug, str):
      raise TypeError('mount_slug must be of type str')
    self._mount_slug = mount_slug

  @property
  def last_updated(self) -> datetime:
    return self._last_updated

  @last_updated.setter
  def last_updated(self, last_updated: datetime):
    if last_updated is None:
      del self.last_updated
      return
    if not isinstance(last_updated, datetime):
      raise TypeError('last_updated must be of type datetime')
    self._last_updated = last_updated

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
  def source_type(self) -> 'DataSourceType':
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
  def version_number(self) -> int:
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def state(self) -> 'DataSourceState':
    return self._state

  @state.setter
  def state(self, state: 'DataSourceState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, DataSourceState):
      raise TypeError('state must be of type DataSourceState')
    self._state = state

  @property
  def kernel_output_info(self) -> Optional['KernelOutputInfo']:
    return self._kernel_output_info

  @kernel_output_info.setter
  def kernel_output_info(self, kernel_output_info: Optional['KernelOutputInfo']):
    if kernel_output_info is None:
      del self.kernel_output_info
      return
    if not isinstance(kernel_output_info, KernelOutputInfo):
      raise TypeError('kernel_output_info must be of type KernelOutputInfo')
    self._kernel_output_info = kernel_output_info

  @property
  def can_edit(self) -> bool:
    return self._can_edit or False

  @can_edit.setter
  def can_edit(self, can_edit: Optional[bool]):
    if can_edit is None:
      del self.can_edit
      return
    if not isinstance(can_edit, bool):
      raise TypeError('can_edit must be of type bool')
    self._can_edit = can_edit

  @property
  def is_pinned(self) -> bool:
    return self._is_pinned or False

  @is_pinned.setter
  def is_pinned(self, is_pinned: Optional[bool]):
    if is_pinned is None:
      del self.is_pinned
      return
    if not isinstance(is_pinned, bool):
      raise TypeError('is_pinned must be of type bool')
    self._is_pinned = is_pinned

  @property
  def model_info(self) -> Optional['DataSource.ModelInfo']:
    return self._model_info

  @model_info.setter
  def model_info(self, model_info: Optional['DataSource.ModelInfo']):
    if model_info is None:
      del self.model_info
      return
    if not isinstance(model_info, DataSource.ModelInfo):
      raise TypeError('model_info must be of type DataSource.ModelInfo')
    self._model_info = model_info


class DateTimeHistogram(KaggleObject):
  r"""
  Attributes:
    buckets (DateTimeHistogramBucket)
  """

  def __init__(self):
    self._buckets = []
    self._freeze()

  @property
  def buckets(self) -> Optional[List[Optional['DateTimeHistogramBucket']]]:
    return self._buckets

  @buckets.setter
  def buckets(self, buckets: Optional[List[Optional['DateTimeHistogramBucket']]]):
    if buckets is None:
      del self.buckets
      return
    if not isinstance(buckets, list):
      raise TypeError('buckets must be of type list')
    if not all([isinstance(t, DateTimeHistogramBucket) for t in buckets]):
      raise TypeError('buckets must contain only items of type DateTimeHistogramBucket')
    self._buckets = buckets


class DateTimeHistogramBucket(KaggleObject):
  r"""
  Attributes:
    index (int)
    label (str)
    left_value (datetime)
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    right_value (datetime)
    count (int)
  """

  def __init__(self):
    self._index = 0
    self._label = None
    self._left_value = None
    self._right_value = None
    self._count = 0
    self._freeze()

  @property
  def index(self) -> int:
    return self._index

  @index.setter
  def index(self, index: int):
    if index is None:
      del self.index
      return
    if not isinstance(index, int):
      raise TypeError('index must be of type int')
    self._index = index

  @property
  def label(self) -> str:
    return self._label or ""

  @label.setter
  def label(self, label: Optional[str]):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label

  @property
  def left_value(self) -> datetime:
    r"""
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._left_value

  @left_value.setter
  def left_value(self, left_value: datetime):
    if left_value is None:
      del self.left_value
      return
    if not isinstance(left_value, datetime):
      raise TypeError('left_value must be of type datetime')
    self._left_value = left_value

  @property
  def right_value(self) -> datetime:
    return self._right_value

  @right_value.setter
  def right_value(self, right_value: datetime):
    if right_value is None:
      del self.right_value
      return
    if not isinstance(right_value, datetime):
      raise TypeError('right_value must be of type datetime')
    self._right_value = right_value

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


class DateTimeMetrics(KaggleObject):
  r"""
  Attributes:
    mean (datetime)
    minimum (datetime)
    maximum (datetime)
    histogram (DateTimeHistogram)
  """

  def __init__(self):
    self._mean = None
    self._minimum = None
    self._maximum = None
    self._histogram = None
    self._freeze()

  @property
  def mean(self) -> datetime:
    return self._mean

  @mean.setter
  def mean(self, mean: datetime):
    if mean is None:
      del self.mean
      return
    if not isinstance(mean, datetime):
      raise TypeError('mean must be of type datetime')
    self._mean = mean

  @property
  def minimum(self) -> datetime:
    return self._minimum

  @minimum.setter
  def minimum(self, minimum: datetime):
    if minimum is None:
      del self.minimum
      return
    if not isinstance(minimum, datetime):
      raise TypeError('minimum must be of type datetime')
    self._minimum = minimum

  @property
  def maximum(self) -> datetime:
    return self._maximum

  @maximum.setter
  def maximum(self, maximum: datetime):
    if maximum is None:
      del self.maximum
      return
    if not isinstance(maximum, datetime):
      raise TypeError('maximum must be of type datetime')
    self._maximum = maximum

  @property
  def histogram(self) -> Optional['DateTimeHistogram']:
    return self._histogram

  @histogram.setter
  def histogram(self, histogram: Optional['DateTimeHistogram']):
    if histogram is None:
      del self.histogram
      return
    if not isinstance(histogram, DateTimeHistogram):
      raise TypeError('histogram must be of type DateTimeHistogram')
    self._histogram = histogram


class Directory(KaggleObject):
  r"""
  Attributes:
    directory_info (DirectoryInfo)
    compression_info (CompressionInfo)
    kernel_session_info (KernelSessionInfo)
  """

  def __init__(self):
    self._directory_info = None
    self._compression_info = None
    self._kernel_session_info = None
    self._freeze()

  @property
  def directory_info(self) -> Optional['DirectoryInfo']:
    return self._directory_info

  @directory_info.setter
  def directory_info(self, directory_info: Optional['DirectoryInfo']):
    if directory_info is None:
      del self.directory_info
      return
    if not isinstance(directory_info, DirectoryInfo):
      raise TypeError('directory_info must be of type DirectoryInfo')
    self._directory_info = directory_info

  @property
  def compression_info(self) -> Optional['CompressionInfo']:
    return self._compression_info

  @compression_info.setter
  def compression_info(self, compression_info: Optional['CompressionInfo']):
    if compression_info is None:
      del self.compression_info
      return
    if not isinstance(compression_info, CompressionInfo):
      raise TypeError('compression_info must be of type CompressionInfo')
    self._compression_info = compression_info

  @property
  def kernel_session_info(self) -> Optional['KernelSessionInfo']:
    return self._kernel_session_info

  @kernel_session_info.setter
  def kernel_session_info(self, kernel_session_info: Optional['KernelSessionInfo']):
    if kernel_session_info is None:
      del self.kernel_session_info
      return
    if not isinstance(kernel_session_info, KernelSessionInfo):
      raise TypeError('kernel_session_info must be of type KernelSessionInfo')
    self._kernel_session_info = kernel_session_info


class DirectoryCollection(KaggleObject):
  r"""
  """

  pass

class DirectoryCollectionContainerInfo(KaggleObject):
  r"""
  Attributes:
    children (Directory)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['Directory']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['Directory']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, Directory) for t in children]):
      raise TypeError('children must contain only items of type Directory')
    self._children = children


class DirectoryInfo(KaggleObject):
  r"""
  Attributes:
    total_size (int)
    download_url (str)
    directories (DirectoryCollection)
    files (FileCollection)
  """

  def __init__(self):
    self._total_size = 0
    self._download_url = None
    self._directories = None
    self._files = None
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
  def directories(self) -> Optional['DirectoryCollection']:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional['DirectoryCollection']):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, DirectoryCollection):
      raise TypeError('directories must be of type DirectoryCollection')
    self._directories = directories

  @property
  def files(self) -> Optional['FileCollection']:
    return self._files

  @files.setter
  def files(self, files: Optional['FileCollection']):
    if files is None:
      del self.files
      return
    if not isinstance(files, FileCollection):
      raise TypeError('files must be of type FileCollection')
    self._files = files


class ExcelInfo(KaggleObject):
  r"""
  Attributes:
    tables (TableCollection)
  """

  def __init__(self):
    self._tables = None
    self._freeze()

  @property
  def tables(self) -> Optional['TableCollection']:
    return self._tables

  @tables.setter
  def tables(self, tables: Optional['TableCollection']):
    if tables is None:
      del self.tables
      return
    if not isinstance(tables, TableCollection):
      raise TypeError('tables must be of type TableCollection')
    self._tables = tables


class ExceptionInfo(KaggleObject):
  r"""
  Attributes:
    critical_exception (str)
      Critical exceptions are errors that cause the worker pipeline to stop, i.e.
      the databundle to fail.
    warning_exceptions (str)
      Warning exceptions are non-critical, the worker keeps processing. They are
      stored for information only.
    analysis_exception (str)
      An analysis exception is any critical exception that causes the
      AnalysisPipeline to stop
  """

  def __init__(self):
    self._critical_exception = None
    self._warning_exceptions = []
    self._analysis_exception = None
    self._freeze()

  @property
  def critical_exception(self) -> str:
    r"""
    Critical exceptions are errors that cause the worker pipeline to stop, i.e.
    the databundle to fail.
    """
    return self._critical_exception or ""

  @critical_exception.setter
  def critical_exception(self, critical_exception: Optional[str]):
    if critical_exception is None:
      del self.critical_exception
      return
    if not isinstance(critical_exception, str):
      raise TypeError('critical_exception must be of type str')
    self._critical_exception = critical_exception

  @property
  def warning_exceptions(self) -> Optional[List[str]]:
    r"""
    Warning exceptions are non-critical, the worker keeps processing. They are
    stored for information only.
    """
    return self._warning_exceptions

  @warning_exceptions.setter
  def warning_exceptions(self, warning_exceptions: Optional[List[str]]):
    if warning_exceptions is None:
      del self.warning_exceptions
      return
    if not isinstance(warning_exceptions, list):
      raise TypeError('warning_exceptions must be of type list')
    if not all([isinstance(t, str) for t in warning_exceptions]):
      raise TypeError('warning_exceptions must contain only items of type str')
    self._warning_exceptions = warning_exceptions

  @property
  def analysis_exception(self) -> str:
    r"""
    An analysis exception is any critical exception that causes the
    AnalysisPipeline to stop
    """
    return self._analysis_exception or ""

  @analysis_exception.setter
  def analysis_exception(self, analysis_exception: Optional[str]):
    if analysis_exception is None:
      del self.analysis_exception
      return
    if not isinstance(analysis_exception, str):
      raise TypeError('analysis_exception must be of type str')
    self._analysis_exception = analysis_exception


class ExternalCopy(KaggleObject):
  r"""
  Attributes:
    bucket (str)
    path (str)
    region (str)
    last_copied (datetime)
    status (ExternalCopyStatus)
    last_update (datetime)
    percent_finished (float)
  """

  def __init__(self):
    self._bucket = None
    self._path = None
    self._region = None
    self._last_copied = None
    self._status = ExternalCopyStatus.EXTERNAL_COPY_STATUS_UNSPECIFIED
    self._last_update = None
    self._percent_finished = None
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

  @property
  def region(self) -> str:
    return self._region or ""

  @region.setter
  def region(self, region: Optional[str]):
    if region is None:
      del self.region
      return
    if not isinstance(region, str):
      raise TypeError('region must be of type str')
    self._region = region

  @property
  def last_copied(self) -> datetime:
    return self._last_copied

  @last_copied.setter
  def last_copied(self, last_copied: datetime):
    if last_copied is None:
      del self.last_copied
      return
    if not isinstance(last_copied, datetime):
      raise TypeError('last_copied must be of type datetime')
    self._last_copied = last_copied

  @property
  def status(self) -> 'ExternalCopyStatus':
    return self._status

  @status.setter
  def status(self, status: 'ExternalCopyStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, ExternalCopyStatus):
      raise TypeError('status must be of type ExternalCopyStatus')
    self._status = status

  @property
  def last_update(self) -> datetime:
    return self._last_update

  @last_update.setter
  def last_update(self, last_update: datetime):
    if last_update is None:
      del self.last_update
      return
    if not isinstance(last_update, datetime):
      raise TypeError('last_update must be of type datetime')
    self._last_update = last_update

  @property
  def percent_finished(self) -> float:
    return self._percent_finished or 0.0

  @percent_finished.setter
  def percent_finished(self, percent_finished: Optional[float]):
    if percent_finished is None:
      del self.percent_finished
      return
    if not isinstance(percent_finished, float):
      raise TypeError('percent_finished must be of type float')
    self._percent_finished = percent_finished


class ExternalCopyInfo(KaggleObject):
  r"""
  Attributes:
    external_copies (ExternalCopy)
  """

  def __init__(self):
    self._external_copies = []
    self._freeze()

  @property
  def external_copies(self) -> Optional[List[Optional['ExternalCopy']]]:
    return self._external_copies

  @external_copies.setter
  def external_copies(self, external_copies: Optional[List[Optional['ExternalCopy']]]):
    if external_copies is None:
      del self.external_copies
      return
    if not isinstance(external_copies, list):
      raise TypeError('external_copies must be of type list')
    if not all([isinstance(t, ExternalCopy) for t in external_copies]):
      raise TypeError('external_copies must contain only items of type ExternalCopy')
    self._external_copies = external_copies


class File(KaggleObject):
  r"""
  Attributes:
    file_info (FileInfo)
    file_table_info (FileTableInfo)
      Csv, Tsv, etc
    table_info (TableInfo)
    sqlite_info (SqliteInfo)
    excel_info (ExcelInfo)
    remote_url_info (RemoteUrlInfo)
    kernel_session_info (KernelSessionInfo)
  """

  def __init__(self):
    self._file_info = None
    self._file_table_info = None
    self._table_info = None
    self._sqlite_info = None
    self._excel_info = None
    self._remote_url_info = None
    self._kernel_session_info = None
    self._freeze()

  @property
  def file_info(self) -> Optional['FileInfo']:
    return self._file_info

  @file_info.setter
  def file_info(self, file_info: Optional['FileInfo']):
    if file_info is None:
      del self.file_info
      return
    if not isinstance(file_info, FileInfo):
      raise TypeError('file_info must be of type FileInfo')
    self._file_info = file_info

  @property
  def file_table_info(self) -> Optional['FileTableInfo']:
    """Csv, Tsv, etc"""
    return self._file_table_info

  @file_table_info.setter
  def file_table_info(self, file_table_info: Optional['FileTableInfo']):
    if file_table_info is None:
      del self.file_table_info
      return
    if not isinstance(file_table_info, FileTableInfo):
      raise TypeError('file_table_info must be of type FileTableInfo')
    self._file_table_info = file_table_info

  @property
  def table_info(self) -> Optional['TableInfo']:
    return self._table_info

  @table_info.setter
  def table_info(self, table_info: Optional['TableInfo']):
    if table_info is None:
      del self.table_info
      return
    if not isinstance(table_info, TableInfo):
      raise TypeError('table_info must be of type TableInfo')
    self._table_info = table_info

  @property
  def sqlite_info(self) -> Optional['SqliteInfo']:
    return self._sqlite_info

  @sqlite_info.setter
  def sqlite_info(self, sqlite_info: Optional['SqliteInfo']):
    if sqlite_info is None:
      del self.sqlite_info
      return
    if not isinstance(sqlite_info, SqliteInfo):
      raise TypeError('sqlite_info must be of type SqliteInfo')
    self._sqlite_info = sqlite_info

  @property
  def excel_info(self) -> Optional['ExcelInfo']:
    return self._excel_info

  @excel_info.setter
  def excel_info(self, excel_info: Optional['ExcelInfo']):
    if excel_info is None:
      del self.excel_info
      return
    if not isinstance(excel_info, ExcelInfo):
      raise TypeError('excel_info must be of type ExcelInfo')
    self._excel_info = excel_info

  @property
  def remote_url_info(self) -> Optional['RemoteUrlInfo']:
    return self._remote_url_info

  @remote_url_info.setter
  def remote_url_info(self, remote_url_info: Optional['RemoteUrlInfo']):
    if remote_url_info is None:
      del self.remote_url_info
      return
    if not isinstance(remote_url_info, RemoteUrlInfo):
      raise TypeError('remote_url_info must be of type RemoteUrlInfo')
    self._remote_url_info = remote_url_info

  @property
  def kernel_session_info(self) -> Optional['KernelSessionInfo']:
    return self._kernel_session_info

  @kernel_session_info.setter
  def kernel_session_info(self, kernel_session_info: Optional['KernelSessionInfo']):
    if kernel_session_info is None:
      del self.kernel_session_info
      return
    if not isinstance(kernel_session_info, KernelSessionInfo):
      raise TypeError('kernel_session_info must be of type KernelSessionInfo')
    self._kernel_session_info = kernel_session_info


class FileCollection(KaggleObject):
  r"""
  """

  pass

class FileCollectionContainerInfo(KaggleObject):
  r"""
  Attributes:
    children (File)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['File']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['File']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, File) for t in children]):
      raise TypeError('children must contain only items of type File')
    self._children = children


class FileExtensionSummaryInfo(KaggleObject):
  r"""
  Attributes:
    extension (str)
    file_count (int)
    total_size (int)
  """

  def __init__(self):
    self._extension = ""
    self._file_count = 0
    self._total_size = 0
    self._freeze()

  @property
  def extension(self) -> str:
    return self._extension

  @extension.setter
  def extension(self, extension: str):
    if extension is None:
      del self.extension
      return
    if not isinstance(extension, str):
      raise TypeError('extension must be of type str')
    self._extension = extension

  @property
  def file_count(self) -> int:
    return self._file_count

  @file_count.setter
  def file_count(self, file_count: int):
    if file_count is None:
      del self.file_count
      return
    if not isinstance(file_count, int):
      raise TypeError('file_count must be of type int')
    self._file_count = file_count

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


class FileInfo(KaggleObject):
  r"""
  Attributes:
    size (int)
    full_path (str)
    download_url (str)
    file_extension (str)
    content_type (str)
    content_md5 (str)
    gcs_url (str)
    gcs_compressed_url (str)
  """

  def __init__(self):
    self._size = 0
    self._full_path = ""
    self._download_url = None
    self._file_extension = ""
    self._content_type = ""
    self._content_md5 = ""
    self._gcs_url = None
    self._gcs_compressed_url = None
    self._freeze()

  @property
  def size(self) -> int:
    return self._size

  @size.setter
  def size(self, size: int):
    if size is None:
      del self.size
      return
    if not isinstance(size, int):
      raise TypeError('size must be of type int')
    self._size = size

  @property
  def full_path(self) -> str:
    return self._full_path

  @full_path.setter
  def full_path(self, full_path: str):
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
  def file_extension(self) -> str:
    return self._file_extension

  @file_extension.setter
  def file_extension(self, file_extension: str):
    if file_extension is None:
      del self.file_extension
      return
    if not isinstance(file_extension, str):
      raise TypeError('file_extension must be of type str')
    self._file_extension = file_extension

  @property
  def content_type(self) -> str:
    return self._content_type

  @content_type.setter
  def content_type(self, content_type: str):
    if content_type is None:
      del self.content_type
      return
    if not isinstance(content_type, str):
      raise TypeError('content_type must be of type str')
    self._content_type = content_type

  @property
  def content_md5(self) -> str:
    return self._content_md5

  @content_md5.setter
  def content_md5(self, content_md5: str):
    if content_md5 is None:
      del self.content_md5
      return
    if not isinstance(content_md5, str):
      raise TypeError('content_md5 must be of type str')
    self._content_md5 = content_md5

  @property
  def gcs_url(self) -> str:
    return self._gcs_url or ""

  @gcs_url.setter
  def gcs_url(self, gcs_url: Optional[str]):
    if gcs_url is None:
      del self.gcs_url
      return
    if not isinstance(gcs_url, str):
      raise TypeError('gcs_url must be of type str')
    self._gcs_url = gcs_url

  @property
  def gcs_compressed_url(self) -> str:
    return self._gcs_compressed_url or ""

  @gcs_compressed_url.setter
  def gcs_compressed_url(self, gcs_compressed_url: Optional[str]):
    if gcs_compressed_url is None:
      del self.gcs_compressed_url
      return
    if not isinstance(gcs_compressed_url, str):
      raise TypeError('gcs_compressed_url must be of type str')
    self._gcs_compressed_url = gcs_compressed_url


class FileSummaryInfo(KaggleObject):
  r"""
  Attributes:
    file_types (FileExtensionSummaryInfo)
    sample_file_names (str)
  """

  def __init__(self):
    self._file_types = []
    self._sample_file_names = []
    self._freeze()

  @property
  def file_types(self) -> Optional[List[Optional['FileExtensionSummaryInfo']]]:
    return self._file_types

  @file_types.setter
  def file_types(self, file_types: Optional[List[Optional['FileExtensionSummaryInfo']]]):
    if file_types is None:
      del self.file_types
      return
    if not isinstance(file_types, list):
      raise TypeError('file_types must be of type list')
    if not all([isinstance(t, FileExtensionSummaryInfo) for t in file_types]):
      raise TypeError('file_types must contain only items of type FileExtensionSummaryInfo')
    self._file_types = file_types

  @property
  def sample_file_names(self) -> Optional[List[str]]:
    return self._sample_file_names

  @sample_file_names.setter
  def sample_file_names(self, sample_file_names: Optional[List[str]]):
    if sample_file_names is None:
      del self.sample_file_names
      return
    if not isinstance(sample_file_names, list):
      raise TypeError('sample_file_names must be of type list')
    if not all([isinstance(t, str) for t in sample_file_names]):
      raise TypeError('sample_file_names must contain only items of type str')
    self._sample_file_names = sample_file_names


class FileSummaryInfoComputedFields(KaggleObject):
  r"""
  Attributes:
    total_file_count (int)
  """

  def __init__(self):
    self._total_file_count = 0
    self._freeze()

  @property
  def total_file_count(self) -> int:
    return self._total_file_count

  @total_file_count.setter
  def total_file_count(self, total_file_count: int):
    if total_file_count is None:
      del self.total_file_count
      return
    if not isinstance(total_file_count, int):
      raise TypeError('total_file_count must be of type int')
    self._total_file_count = total_file_count


class FileTableInfo(KaggleObject):
  r"""
  Attributes:
    includes_header (bool)
    header_row (int)
    delimiter (str)
  """

  def __init__(self):
    self._includes_header = False
    self._header_row = 0
    self._delimiter = None
    self._freeze()

  @property
  def includes_header(self) -> bool:
    return self._includes_header

  @includes_header.setter
  def includes_header(self, includes_header: bool):
    if includes_header is None:
      del self.includes_header
      return
    if not isinstance(includes_header, bool):
      raise TypeError('includes_header must be of type bool')
    self._includes_header = includes_header

  @property
  def header_row(self) -> int:
    return self._header_row

  @header_row.setter
  def header_row(self, header_row: int):
    if header_row is None:
      del self.header_row
      return
    if not isinstance(header_row, int):
      raise TypeError('header_row must be of type int')
    self._header_row = header_row

  @property
  def delimiter(self) -> str:
    return self._delimiter or ""

  @delimiter.setter
  def delimiter(self, delimiter: Optional[str]):
    if delimiter is None:
      del self.delimiter
      return
    if not isinstance(delimiter, str):
      raise TypeError('delimiter must be of type str')
    self._delimiter = delimiter


class FrequencyCount(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (int)
  """

  def __init__(self):
    self._key = ""
    self._value = 0
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def value(self) -> int:
    return self._value

  @value.setter
  def value(self, value: int):
    if value is None:
      del self.value
      return
    if not isinstance(value, int):
      raise TypeError('value must be of type int')
    self._value = value


class GithubInfo(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    repository_slug (str)
    last_updated_hash (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._repository_slug = ""
    self._last_updated_hash = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
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
  def repository_slug(self) -> str:
    return self._repository_slug

  @repository_slug.setter
  def repository_slug(self, repository_slug: str):
    if repository_slug is None:
      del self.repository_slug
      return
    if not isinstance(repository_slug, str):
      raise TypeError('repository_slug must be of type str')
    self._repository_slug = repository_slug

  @property
  def last_updated_hash(self) -> str:
    return self._last_updated_hash or ""

  @last_updated_hash.setter
  def last_updated_hash(self, last_updated_hash: Optional[str]):
    if last_updated_hash is None:
      del self.last_updated_hash
      return
    if not isinstance(last_updated_hash, str):
      raise TypeError('last_updated_hash must be of type str')
    self._last_updated_hash = last_updated_hash


class HashInfo(KaggleObject):
  r"""
  Attributes:
    raw_data_hash (str)
      Aggregate hash of the raw files in this databundle version. Only aggregated
      for versions with <= 10,000 files. Aggregated by Md5 hashing the files at
      StorageInfo.raw_data_location in lexicographical order.
    upload_data_hash (str)
      Aggregate hash of the uploaded files in this databundle version. Aggregated
      by Md5 hashing the files at StorageInfo.upload_data_location in
      lexicographical order.
  """

  def __init__(self):
    self._raw_data_hash = None
    self._upload_data_hash = None
    self._freeze()

  @property
  def raw_data_hash(self) -> str:
    r"""
    Aggregate hash of the raw files in this databundle version. Only aggregated
    for versions with <= 10,000 files. Aggregated by Md5 hashing the files at
    StorageInfo.raw_data_location in lexicographical order.
    """
    return self._raw_data_hash or ""

  @raw_data_hash.setter
  def raw_data_hash(self, raw_data_hash: Optional[str]):
    if raw_data_hash is None:
      del self.raw_data_hash
      return
    if not isinstance(raw_data_hash, str):
      raise TypeError('raw_data_hash must be of type str')
    self._raw_data_hash = raw_data_hash

  @property
  def upload_data_hash(self) -> str:
    r"""
    Aggregate hash of the uploaded files in this databundle version. Aggregated
    by Md5 hashing the files at StorageInfo.upload_data_location in
    lexicographical order.
    """
    return self._upload_data_hash or ""

  @upload_data_hash.setter
  def upload_data_hash(self, upload_data_hash: Optional[str]):
    if upload_data_hash is None:
      del self.upload_data_hash
      return
    if not isinstance(upload_data_hash, str):
      raise TypeError('upload_data_hash must be of type str')
    self._upload_data_hash = upload_data_hash


class Histogram(KaggleObject):
  r"""
  Attributes:
    buckets (HistogramBucket)
    type (HarmonizedDataType)
  """

  def __init__(self):
    self._buckets = []
    self._type = HarmonizedDataType.STRING
    self._freeze()

  @property
  def buckets(self) -> Optional[List[Optional['HistogramBucket']]]:
    return self._buckets

  @buckets.setter
  def buckets(self, buckets: Optional[List[Optional['HistogramBucket']]]):
    if buckets is None:
      del self.buckets
      return
    if not isinstance(buckets, list):
      raise TypeError('buckets must be of type list')
    if not all([isinstance(t, HistogramBucket) for t in buckets]):
      raise TypeError('buckets must contain only items of type HistogramBucket')
    self._buckets = buckets

  @property
  def type(self) -> 'HarmonizedDataType':
    return self._type

  @type.setter
  def type(self, type: 'HarmonizedDataType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HarmonizedDataType):
      raise TypeError('type must be of type HarmonizedDataType')
    self._type = type


class HistogramBucket(KaggleObject):
  r"""
  Attributes:
    index (int)
    label (str)
    left_value (float)
    right_value (float)
    count (int)
  """

  def __init__(self):
    self._index = 0
    self._label = None
    self._left_value = 0.0
    self._right_value = 0.0
    self._count = 0
    self._freeze()

  @property
  def index(self) -> int:
    return self._index

  @index.setter
  def index(self, index: int):
    if index is None:
      del self.index
      return
    if not isinstance(index, int):
      raise TypeError('index must be of type int')
    self._index = index

  @property
  def label(self) -> str:
    return self._label or ""

  @label.setter
  def label(self, label: Optional[str]):
    if label is None:
      del self.label
      return
    if not isinstance(label, str):
      raise TypeError('label must be of type str')
    self._label = label

  @property
  def left_value(self) -> float:
    return self._left_value

  @left_value.setter
  def left_value(self, left_value: float):
    if left_value is None:
      del self.left_value
      return
    if not isinstance(left_value, float):
      raise TypeError('left_value must be of type float')
    self._left_value = left_value

  @property
  def right_value(self) -> float:
    return self._right_value

  @right_value.setter
  def right_value(self, right_value: float):
    if right_value is None:
      del self.right_value
      return
    if not isinstance(right_value, float):
      raise TypeError('right_value must be of type float')
    self._right_value = right_value

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


class HuggingFaceInfo(KaggleObject):
  r"""
  Attributes:
    url (str)
    repo_id (str)
    revision (str)
    encrypted_hugging_face_access_token (str)
  """

  def __init__(self):
    self._url = ""
    self._repo_id = ""
    self._revision = ""
    self._encrypted_hugging_face_access_token = None
    self._freeze()

  @property
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def repo_id(self) -> str:
    return self._repo_id

  @repo_id.setter
  def repo_id(self, repo_id: str):
    if repo_id is None:
      del self.repo_id
      return
    if not isinstance(repo_id, str):
      raise TypeError('repo_id must be of type str')
    self._repo_id = repo_id

  @property
  def revision(self) -> str:
    return self._revision

  @revision.setter
  def revision(self, revision: str):
    if revision is None:
      del self.revision
      return
    if not isinstance(revision, str):
      raise TypeError('revision must be of type str')
    self._revision = revision

  @property
  def encrypted_hugging_face_access_token(self) -> str:
    return self._encrypted_hugging_face_access_token or ""

  @encrypted_hugging_face_access_token.setter
  def encrypted_hugging_face_access_token(self, encrypted_hugging_face_access_token: Optional[str]):
    if encrypted_hugging_face_access_token is None:
      del self.encrypted_hugging_face_access_token
      return
    if not isinstance(encrypted_hugging_face_access_token, str):
      raise TypeError('encrypted_hugging_face_access_token must be of type str')
    self._encrypted_hugging_face_access_token = encrypted_hugging_face_access_token


class KernelOutputInfo(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
    url (str)
  """

  def __init__(self):
    self._kernel_id = 0
    self._url = ""
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
  def url(self) -> str:
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class KernelSessionInfo(KaggleObject):
  r"""
  Attributes:
    kernel_session_id (int)
  """

  def __init__(self):
    self._kernel_session_id = 0
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


class ModelInstanceInfo(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    model_instance_id (int)
    is_private (bool)
  """

  def __init__(self):
    self._model_id = 0
    self._model_instance_id = 0
    self._is_private = False
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id

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


class ModelInstanceVersionInfo(KaggleObject):
  r"""
  Attributes:
    model_instance_version_id (int)
  """

  def __init__(self):
    self._model_instance_version_id = 0
    self._freeze()

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: int):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    self._model_instance_version_id = model_instance_version_id


class NumericMetrics(KaggleObject):
  r"""
  Attributes:
    finite_count (int)
    infinite_count (int)
    mean (float)
    standard_deviation (float)
    minimum (float)
    minimum_finite (float)
    maximum (float)
    maximum_finite (float)
    quantiles (Quantile)
    histogram (Histogram)
  """

  def __init__(self):
    self._finite_count = 0
    self._infinite_count = 0
    self._mean = 0.0
    self._standard_deviation = 0.0
    self._minimum = 0.0
    self._minimum_finite = 0.0
    self._maximum = 0.0
    self._maximum_finite = 0.0
    self._quantiles = []
    self._histogram = None
    self._freeze()

  @property
  def finite_count(self) -> int:
    return self._finite_count

  @finite_count.setter
  def finite_count(self, finite_count: int):
    if finite_count is None:
      del self.finite_count
      return
    if not isinstance(finite_count, int):
      raise TypeError('finite_count must be of type int')
    self._finite_count = finite_count

  @property
  def infinite_count(self) -> int:
    return self._infinite_count

  @infinite_count.setter
  def infinite_count(self, infinite_count: int):
    if infinite_count is None:
      del self.infinite_count
      return
    if not isinstance(infinite_count, int):
      raise TypeError('infinite_count must be of type int')
    self._infinite_count = infinite_count

  @property
  def mean(self) -> float:
    return self._mean

  @mean.setter
  def mean(self, mean: float):
    if mean is None:
      del self.mean
      return
    if not isinstance(mean, float):
      raise TypeError('mean must be of type float')
    self._mean = mean

  @property
  def standard_deviation(self) -> float:
    return self._standard_deviation

  @standard_deviation.setter
  def standard_deviation(self, standard_deviation: float):
    if standard_deviation is None:
      del self.standard_deviation
      return
    if not isinstance(standard_deviation, float):
      raise TypeError('standard_deviation must be of type float')
    self._standard_deviation = standard_deviation

  @property
  def minimum(self) -> float:
    return self._minimum

  @minimum.setter
  def minimum(self, minimum: float):
    if minimum is None:
      del self.minimum
      return
    if not isinstance(minimum, float):
      raise TypeError('minimum must be of type float')
    self._minimum = minimum

  @property
  def minimum_finite(self) -> float:
    return self._minimum_finite

  @minimum_finite.setter
  def minimum_finite(self, minimum_finite: float):
    if minimum_finite is None:
      del self.minimum_finite
      return
    if not isinstance(minimum_finite, float):
      raise TypeError('minimum_finite must be of type float')
    self._minimum_finite = minimum_finite

  @property
  def maximum(self) -> float:
    return self._maximum

  @maximum.setter
  def maximum(self, maximum: float):
    if maximum is None:
      del self.maximum
      return
    if not isinstance(maximum, float):
      raise TypeError('maximum must be of type float')
    self._maximum = maximum

  @property
  def maximum_finite(self) -> float:
    return self._maximum_finite

  @maximum_finite.setter
  def maximum_finite(self, maximum_finite: float):
    if maximum_finite is None:
      del self.maximum_finite
      return
    if not isinstance(maximum_finite, float):
      raise TypeError('maximum_finite must be of type float')
    self._maximum_finite = maximum_finite

  @property
  def quantiles(self) -> Optional[List[Optional['Quantile']]]:
    return self._quantiles

  @quantiles.setter
  def quantiles(self, quantiles: Optional[List[Optional['Quantile']]]):
    if quantiles is None:
      del self.quantiles
      return
    if not isinstance(quantiles, list):
      raise TypeError('quantiles must be of type list')
    if not all([isinstance(t, Quantile) for t in quantiles]):
      raise TypeError('quantiles must contain only items of type Quantile')
    self._quantiles = quantiles

  @property
  def histogram(self) -> Optional['Histogram']:
    return self._histogram

  @histogram.setter
  def histogram(self, histogram: Optional['Histogram']):
    if histogram is None:
      del self.histogram
      return
    if not isinstance(histogram, Histogram):
      raise TypeError('histogram must be of type Histogram')
    self._histogram = histogram


class OriginalRemoteUrlInfo(KaggleObject):
  r"""
  List of remote URLs originally added by the user upon upload (on the level of
  a databundle version). Each file already stores its own remote URL, so why do
  we need to store this in addition?
  - If users specify zip files as a remote URL, then this zip gets unpacked
  automatically
  - When processing happens on the worker, the zip gets uncompressed and we
  keep only the files in there
  - The files themselves don't have a remote URL
  - Subsequent request then fail because there's files in a remote url dataset
  without actual URLs To fix this situation, we need to store the original URLs
  that were used, which is what this object is for.

  Attributes:
    original_remote_urls (RemoteUrlInfo)
  """

  def __init__(self):
    self._original_remote_urls = []
    self._freeze()

  @property
  def original_remote_urls(self) -> Optional[List[Optional['RemoteUrlInfo']]]:
    return self._original_remote_urls

  @original_remote_urls.setter
  def original_remote_urls(self, original_remote_urls: Optional[List[Optional['RemoteUrlInfo']]]):
    if original_remote_urls is None:
      del self.original_remote_urls
      return
    if not isinstance(original_remote_urls, list):
      raise TypeError('original_remote_urls must be of type list')
    if not all([isinstance(t, RemoteUrlInfo) for t in original_remote_urls]):
      raise TypeError('original_remote_urls must contain only items of type RemoteUrlInfo')
    self._original_remote_urls = original_remote_urls


class Quantile(KaggleObject):
  r"""
  Attributes:
    point (float)
    value (float)
  """

  def __init__(self):
    self._point = 0.0
    self._value = 0.0
    self._freeze()

  @property
  def point(self) -> float:
    return self._point

  @point.setter
  def point(self, point: float):
    if point is None:
      del self.point
      return
    if not isinstance(point, float):
      raise TypeError('point must be of type float')
    self._point = point

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, value: float):
    if value is None:
      del self.value
      return
    if not isinstance(value, float):
      raise TypeError('value must be of type float')
    self._value = value


class RemoteDatasourceInfo(KaggleObject):
  r"""
  Attributes:
    update_frequency (RemoteUrlUpdateFrequency)
  """

  def __init__(self):
    self._update_frequency = RemoteUrlUpdateFrequency.DAILY
    self._freeze()

  @property
  def update_frequency(self) -> 'RemoteUrlUpdateFrequency':
    return self._update_frequency

  @update_frequency.setter
  def update_frequency(self, update_frequency: 'RemoteUrlUpdateFrequency'):
    if update_frequency is None:
      del self.update_frequency
      return
    if not isinstance(update_frequency, RemoteUrlUpdateFrequency):
      raise TypeError('update_frequency must be of type RemoteUrlUpdateFrequency')
    self._update_frequency = update_frequency


class RemoteUrlInfo(KaggleObject):
  r"""
  Attributes:
    url (str)
    name (str)
  """

  def __init__(self):
    self._url = None
    self._name = None
    self._freeze()

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


class SqliteInfo(KaggleObject):
  r"""
  Attributes:
    tables (TableCollection)
  """

  def __init__(self):
    self._tables = None
    self._freeze()

  @property
  def tables(self) -> Optional['TableCollection']:
    return self._tables

  @tables.setter
  def tables(self, tables: Optional['TableCollection']):
    if tables is None:
      del self.tables
      return
    if not isinstance(tables, TableCollection):
      raise TypeError('tables must be of type TableCollection')
    self._tables = tables


class StatusInfo(KaggleObject):
  r"""
  Attributes:
    status (DatabundleStatus)
    status_message (str)
    percentage_completed (float)
    analysis_status (DatabundleVersionAnalysisStatus)
  """

  def __init__(self):
    self._status = DatabundleStatus.DATABUNDLE_STATUS_CREATED
    self._status_message = None
    self._percentage_completed = 0.0
    self._analysis_status = None
    self._freeze()

  @property
  def status(self) -> 'DatabundleStatus':
    return self._status

  @status.setter
  def status(self, status: 'DatabundleStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, DatabundleStatus):
      raise TypeError('status must be of type DatabundleStatus')
    self._status = status

  @property
  def status_message(self) -> str:
    return self._status_message or ""

  @status_message.setter
  def status_message(self, status_message: Optional[str]):
    if status_message is None:
      del self.status_message
      return
    if not isinstance(status_message, str):
      raise TypeError('status_message must be of type str')
    self._status_message = status_message

  @property
  def percentage_completed(self) -> float:
    return self._percentage_completed

  @percentage_completed.setter
  def percentage_completed(self, percentage_completed: float):
    if percentage_completed is None:
      del self.percentage_completed
      return
    if not isinstance(percentage_completed, float):
      raise TypeError('percentage_completed must be of type float')
    self._percentage_completed = percentage_completed

  @property
  def analysis_status(self) -> 'DatabundleVersionAnalysisStatus':
    return self._analysis_status or DatabundleVersionAnalysisStatus.DATABUNDLE_VERSION_ANALYSIS_STATUS_UNSPECIFIED

  @analysis_status.setter
  def analysis_status(self, analysis_status: Optional['DatabundleVersionAnalysisStatus']):
    if analysis_status is None:
      del self.analysis_status
      return
    if not isinstance(analysis_status, DatabundleVersionAnalysisStatus):
      raise TypeError('analysis_status must be of type DatabundleVersionAnalysisStatus')
    self._analysis_status = analysis_status


class StorageInfo(KaggleObject):
  r"""
  Attributes:
    upload_data_location (StorageLocation)
    raw_data_location (StorageLocation)
    individual_compressed_location (StorageLocation)
    bundle_archive_location (StorageLocation)
    file_system_location (StorageLocation)
    auto_gen_croissant_location (StorageLocation)
  """

  def __init__(self):
    self._upload_data_location = None
    self._raw_data_location = None
    self._individual_compressed_location = None
    self._bundle_archive_location = None
    self._file_system_location = None
    self._auto_gen_croissant_location = None
    self._freeze()

  @property
  def upload_data_location(self) -> Optional['StorageLocation']:
    return self._upload_data_location

  @upload_data_location.setter
  def upload_data_location(self, upload_data_location: Optional['StorageLocation']):
    if upload_data_location is None:
      del self.upload_data_location
      return
    if not isinstance(upload_data_location, StorageLocation):
      raise TypeError('upload_data_location must be of type StorageLocation')
    self._upload_data_location = upload_data_location

  @property
  def raw_data_location(self) -> Optional['StorageLocation']:
    return self._raw_data_location

  @raw_data_location.setter
  def raw_data_location(self, raw_data_location: Optional['StorageLocation']):
    if raw_data_location is None:
      del self.raw_data_location
      return
    if not isinstance(raw_data_location, StorageLocation):
      raise TypeError('raw_data_location must be of type StorageLocation')
    self._raw_data_location = raw_data_location

  @property
  def individual_compressed_location(self) -> Optional['StorageLocation']:
    return self._individual_compressed_location

  @individual_compressed_location.setter
  def individual_compressed_location(self, individual_compressed_location: Optional['StorageLocation']):
    if individual_compressed_location is None:
      del self.individual_compressed_location
      return
    if not isinstance(individual_compressed_location, StorageLocation):
      raise TypeError('individual_compressed_location must be of type StorageLocation')
    self._individual_compressed_location = individual_compressed_location

  @property
  def bundle_archive_location(self) -> Optional['StorageLocation']:
    return self._bundle_archive_location

  @bundle_archive_location.setter
  def bundle_archive_location(self, bundle_archive_location: Optional['StorageLocation']):
    if bundle_archive_location is None:
      del self.bundle_archive_location
      return
    if not isinstance(bundle_archive_location, StorageLocation):
      raise TypeError('bundle_archive_location must be of type StorageLocation')
    self._bundle_archive_location = bundle_archive_location

  @property
  def file_system_location(self) -> Optional['StorageLocation']:
    return self._file_system_location

  @file_system_location.setter
  def file_system_location(self, file_system_location: Optional['StorageLocation']):
    if file_system_location is None:
      del self.file_system_location
      return
    if not isinstance(file_system_location, StorageLocation):
      raise TypeError('file_system_location must be of type StorageLocation')
    self._file_system_location = file_system_location

  @property
  def auto_gen_croissant_location(self) -> Optional['StorageLocation']:
    return self._auto_gen_croissant_location

  @auto_gen_croissant_location.setter
  def auto_gen_croissant_location(self, auto_gen_croissant_location: Optional['StorageLocation']):
    if auto_gen_croissant_location is None:
      del self.auto_gen_croissant_location
      return
    if not isinstance(auto_gen_croissant_location, StorageLocation):
      raise TypeError('auto_gen_croissant_location must be of type StorageLocation')
    self._auto_gen_croissant_location = auto_gen_croissant_location


class StringMetrics(KaggleObject):
  r"""
  Attributes:
    counts (FrequencyCount)
    unique_value_count (int)
  """

  def __init__(self):
    self._counts = []
    self._unique_value_count = 0
    self._freeze()

  @property
  def counts(self) -> Optional[List[Optional['FrequencyCount']]]:
    return self._counts

  @counts.setter
  def counts(self, counts: Optional[List[Optional['FrequencyCount']]]):
    if counts is None:
      del self.counts
      return
    if not isinstance(counts, list):
      raise TypeError('counts must be of type list')
    if not all([isinstance(t, FrequencyCount) for t in counts]):
      raise TypeError('counts must contain only items of type FrequencyCount')
    self._counts = counts

  @property
  def unique_value_count(self) -> int:
    return self._unique_value_count

  @unique_value_count.setter
  def unique_value_count(self, unique_value_count: int):
    if unique_value_count is None:
      del self.unique_value_count
      return
    if not isinstance(unique_value_count, int):
      raise TypeError('unique_value_count must be of type int')
    self._unique_value_count = unique_value_count


class StringMetricsComputedFields(KaggleObject):
  r"""
  Attributes:
    most_common_value (str)
    most_common_value_count (int)
  """

  def __init__(self):
    self._most_common_value = None
    self._most_common_value_count = 0
    self._freeze()

  @property
  def most_common_value(self) -> str:
    return self._most_common_value or ""

  @most_common_value.setter
  def most_common_value(self, most_common_value: Optional[str]):
    if most_common_value is None:
      del self.most_common_value
      return
    if not isinstance(most_common_value, str):
      raise TypeError('most_common_value must be of type str')
    self._most_common_value = most_common_value

  @property
  def most_common_value_count(self) -> int:
    return self._most_common_value_count

  @most_common_value_count.setter
  def most_common_value_count(self, most_common_value_count: int):
    if most_common_value_count is None:
      del self.most_common_value_count
      return
    if not isinstance(most_common_value_count, int):
      raise TypeError('most_common_value_count must be of type int')
    self._most_common_value_count = most_common_value_count


class Table(KaggleObject):
  r"""
  Attributes:
    table_info (TableInfo)
  """

  def __init__(self):
    self._table_info = None
    self._freeze()

  @property
  def table_info(self) -> Optional['TableInfo']:
    return self._table_info

  @table_info.setter
  def table_info(self, table_info: Optional['TableInfo']):
    if table_info is None:
      del self.table_info
      return
    if not isinstance(table_info, TableInfo):
      raise TypeError('table_info must be of type TableInfo')
    self._table_info = table_info


class TableCollection(KaggleObject):
  r"""
  """

  pass

class TableCollectionContainerInfo(KaggleObject):
  r"""
  Attributes:
    children (Table)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['Table']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['Table']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, Table) for t in children]):
      raise TypeError('children must contain only items of type Table')
    self._children = children


class TableColumn(KaggleObject):
  r"""
  Attributes:
    table_column_info (TableColumnInfo)
    table_column_metrics (TableColumnMetrics)
  """

  def __init__(self):
    self._table_column_info = None
    self._table_column_metrics = None
    self._freeze()

  @property
  def table_column_info(self) -> Optional['TableColumnInfo']:
    return self._table_column_info

  @table_column_info.setter
  def table_column_info(self, table_column_info: Optional['TableColumnInfo']):
    if table_column_info is None:
      del self.table_column_info
      return
    if not isinstance(table_column_info, TableColumnInfo):
      raise TypeError('table_column_info must be of type TableColumnInfo')
    self._table_column_info = table_column_info

  @property
  def table_column_metrics(self) -> Optional['TableColumnMetrics']:
    return self._table_column_metrics

  @table_column_metrics.setter
  def table_column_metrics(self, table_column_metrics: Optional['TableColumnMetrics']):
    if table_column_metrics is None:
      del self.table_column_metrics
      return
    if not isinstance(table_column_metrics, TableColumnMetrics):
      raise TypeError('table_column_metrics must be of type TableColumnMetrics')
    self._table_column_metrics = table_column_metrics


class TableColumnCollection(KaggleObject):
  r"""
  """

  pass

class TableColumnCollectionContainerInfo(KaggleObject):
  r"""
  Attributes:
    children (TableColumn)
  """

  def __init__(self):
    self._children = []
    self._freeze()

  @property
  def children(self) -> Optional[List[Optional['TableColumn']]]:
    return self._children

  @children.setter
  def children(self, children: Optional[List[Optional['TableColumn']]]):
    if children is None:
      del self.children
      return
    if not isinstance(children, list):
      raise TypeError('children must be of type list')
    if not all([isinstance(t, TableColumn) for t in children]):
      raise TypeError('children must contain only items of type TableColumn')
    self._children = children


class TableColumnInfo(KaggleObject):
  r"""
  Attributes:
    order (int)
      This class is intented to be embedded in DataObjects.TableColumn
      Name & Description are already part of that class no need to repeat
    original_type (str)
    type (HarmonizedDataType)
    extended_type (ExtendedDataType)
    is_nullable (bool)
    is_primary_key (bool)
    is_label (bool)
    type_is_suggested (bool)
      These fields are used in the frontend to indicate whether the column's type
      and description values are set via a suggestion (and hence should be
      rendered differently). See https://github.com/Kaggle/kaggleazure/pull/27980
      for other options considered - we're open to trying another alternative
      (ex: moving fully to the client) if this leads to issues.
    description_is_suggested (bool)
  """

  def __init__(self):
    self._order = None
    self._original_type = None
    self._type = HarmonizedDataType.STRING
    self._extended_type = ExtendedDataType.EXTENDED_DATA_TYPE_UNSPECIFIED
    self._is_nullable = None
    self._is_primary_key = None
    self._is_label = None
    self._type_is_suggested = None
    self._description_is_suggested = None
    self._freeze()

  @property
  def order(self) -> int:
    r"""
    This class is intented to be embedded in DataObjects.TableColumn
    Name & Description are already part of that class no need to repeat
    """
    return self._order or 0

  @order.setter
  def order(self, order: Optional[int]):
    if order is None:
      del self.order
      return
    if not isinstance(order, int):
      raise TypeError('order must be of type int')
    self._order = order

  @property
  def original_type(self) -> str:
    return self._original_type or ""

  @original_type.setter
  def original_type(self, original_type: Optional[str]):
    if original_type is None:
      del self.original_type
      return
    if not isinstance(original_type, str):
      raise TypeError('original_type must be of type str')
    self._original_type = original_type

  @property
  def type(self) -> 'HarmonizedDataType':
    return self._type

  @type.setter
  def type(self, type: 'HarmonizedDataType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, HarmonizedDataType):
      raise TypeError('type must be of type HarmonizedDataType')
    self._type = type

  @property
  def extended_type(self) -> 'ExtendedDataType':
    return self._extended_type

  @extended_type.setter
  def extended_type(self, extended_type: 'ExtendedDataType'):
    if extended_type is None:
      del self.extended_type
      return
    if not isinstance(extended_type, ExtendedDataType):
      raise TypeError('extended_type must be of type ExtendedDataType')
    self._extended_type = extended_type

  @property
  def is_nullable(self) -> bool:
    return self._is_nullable or False

  @is_nullable.setter
  def is_nullable(self, is_nullable: Optional[bool]):
    if is_nullable is None:
      del self.is_nullable
      return
    if not isinstance(is_nullable, bool):
      raise TypeError('is_nullable must be of type bool')
    self._is_nullable = is_nullable

  @property
  def is_primary_key(self) -> bool:
    return self._is_primary_key or False

  @is_primary_key.setter
  def is_primary_key(self, is_primary_key: Optional[bool]):
    if is_primary_key is None:
      del self.is_primary_key
      return
    if not isinstance(is_primary_key, bool):
      raise TypeError('is_primary_key must be of type bool')
    self._is_primary_key = is_primary_key

  @property
  def is_label(self) -> bool:
    return self._is_label or False

  @is_label.setter
  def is_label(self, is_label: Optional[bool]):
    if is_label is None:
      del self.is_label
      return
    if not isinstance(is_label, bool):
      raise TypeError('is_label must be of type bool')
    self._is_label = is_label

  @property
  def type_is_suggested(self) -> bool:
    r"""
    These fields are used in the frontend to indicate whether the column's type
    and description values are set via a suggestion (and hence should be
    rendered differently). See https://github.com/Kaggle/kaggleazure/pull/27980
    for other options considered - we're open to trying another alternative
    (ex: moving fully to the client) if this leads to issues.
    """
    return self._type_is_suggested or False

  @type_is_suggested.setter
  def type_is_suggested(self, type_is_suggested: Optional[bool]):
    if type_is_suggested is None:
      del self.type_is_suggested
      return
    if not isinstance(type_is_suggested, bool):
      raise TypeError('type_is_suggested must be of type bool')
    self._type_is_suggested = type_is_suggested

  @property
  def description_is_suggested(self) -> bool:
    return self._description_is_suggested or False

  @description_is_suggested.setter
  def description_is_suggested(self, description_is_suggested: Optional[bool]):
    if description_is_suggested is None:
      del self.description_is_suggested
      return
    if not isinstance(description_is_suggested, bool):
      raise TypeError('description_is_suggested must be of type bool')
    self._description_is_suggested = description_is_suggested


class TableColumnMetrics(KaggleObject):
  r"""
  Attributes:
    error_message (str)
    null_count (int)
    non_null_count (int)
    valid_count (int)
    invalid_count (int)
    boolean_metrics (BooleanMetrics)
      Depending on the type of the column, only one of these is actually set.
    numeric_metrics (NumericMetrics)
    date_time_metrics (DateTimeMetrics)
    string_metrics (StringMetrics)
    country_metrics (CountryMetrics)
  """

  def __init__(self):
    self._error_message = None
    self._null_count = 0
    self._non_null_count = 0
    self._valid_count = 0
    self._invalid_count = 0
    self._boolean_metrics = None
    self._numeric_metrics = None
    self._date_time_metrics = None
    self._string_metrics = None
    self._country_metrics = None
    self._freeze()

  @property
  def error_message(self) -> str:
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def null_count(self) -> int:
    return self._null_count

  @null_count.setter
  def null_count(self, null_count: int):
    if null_count is None:
      del self.null_count
      return
    if not isinstance(null_count, int):
      raise TypeError('null_count must be of type int')
    self._null_count = null_count

  @property
  def non_null_count(self) -> int:
    return self._non_null_count

  @non_null_count.setter
  def non_null_count(self, non_null_count: int):
    if non_null_count is None:
      del self.non_null_count
      return
    if not isinstance(non_null_count, int):
      raise TypeError('non_null_count must be of type int')
    self._non_null_count = non_null_count

  @property
  def valid_count(self) -> int:
    return self._valid_count

  @valid_count.setter
  def valid_count(self, valid_count: int):
    if valid_count is None:
      del self.valid_count
      return
    if not isinstance(valid_count, int):
      raise TypeError('valid_count must be of type int')
    self._valid_count = valid_count

  @property
  def invalid_count(self) -> int:
    return self._invalid_count

  @invalid_count.setter
  def invalid_count(self, invalid_count: int):
    if invalid_count is None:
      del self.invalid_count
      return
    if not isinstance(invalid_count, int):
      raise TypeError('invalid_count must be of type int')
    self._invalid_count = invalid_count

  @property
  def boolean_metrics(self) -> Optional['BooleanMetrics']:
    """Depending on the type of the column, only one of these is actually set."""
    return self._boolean_metrics

  @boolean_metrics.setter
  def boolean_metrics(self, boolean_metrics: Optional['BooleanMetrics']):
    if boolean_metrics is None:
      del self.boolean_metrics
      return
    if not isinstance(boolean_metrics, BooleanMetrics):
      raise TypeError('boolean_metrics must be of type BooleanMetrics')
    self._boolean_metrics = boolean_metrics

  @property
  def numeric_metrics(self) -> Optional['NumericMetrics']:
    return self._numeric_metrics

  @numeric_metrics.setter
  def numeric_metrics(self, numeric_metrics: Optional['NumericMetrics']):
    if numeric_metrics is None:
      del self.numeric_metrics
      return
    if not isinstance(numeric_metrics, NumericMetrics):
      raise TypeError('numeric_metrics must be of type NumericMetrics')
    self._numeric_metrics = numeric_metrics

  @property
  def date_time_metrics(self) -> Optional['DateTimeMetrics']:
    return self._date_time_metrics

  @date_time_metrics.setter
  def date_time_metrics(self, date_time_metrics: Optional['DateTimeMetrics']):
    if date_time_metrics is None:
      del self.date_time_metrics
      return
    if not isinstance(date_time_metrics, DateTimeMetrics):
      raise TypeError('date_time_metrics must be of type DateTimeMetrics')
    self._date_time_metrics = date_time_metrics

  @property
  def string_metrics(self) -> Optional['StringMetrics']:
    return self._string_metrics

  @string_metrics.setter
  def string_metrics(self, string_metrics: Optional['StringMetrics']):
    if string_metrics is None:
      del self.string_metrics
      return
    if not isinstance(string_metrics, StringMetrics):
      raise TypeError('string_metrics must be of type StringMetrics')
    self._string_metrics = string_metrics

  @property
  def country_metrics(self) -> Optional['CountryMetrics']:
    return self._country_metrics

  @country_metrics.setter
  def country_metrics(self, country_metrics: Optional['CountryMetrics']):
    if country_metrics is None:
      del self.country_metrics
      return
    if not isinstance(country_metrics, CountryMetrics):
      raise TypeError('country_metrics must be of type CountryMetrics')
    self._country_metrics = country_metrics


class TableColumnMetricsComputedFields(KaggleObject):
  r"""
  Attributes:
    total_count (int)
  """

  def __init__(self):
    self._total_count = 0
    self._freeze()

  @property
  def total_count(self) -> int:
    return self._total_count

  @total_count.setter
  def total_count(self, total_count: int):
    if total_count is None:
      del self.total_count
      return
    if not isinstance(total_count, int):
      raise TypeError('total_count must be of type int')
    self._total_count = total_count


class TableInfo(KaggleObject):
  r"""
  Attributes:
    total_rows (int)
    table_columns (TableColumnCollection)
    metrics_calculation_skip_reason (MetricsCalculationSkipReason)
  """

  def __init__(self):
    self._total_rows = 0
    self._table_columns = None
    self._metrics_calculation_skip_reason = None
    self._freeze()

  @property
  def total_rows(self) -> int:
    return self._total_rows

  @total_rows.setter
  def total_rows(self, total_rows: int):
    if total_rows is None:
      del self.total_rows
      return
    if not isinstance(total_rows, int):
      raise TypeError('total_rows must be of type int')
    self._total_rows = total_rows

  @property
  def table_columns(self) -> Optional['TableColumnCollection']:
    return self._table_columns

  @table_columns.setter
  def table_columns(self, table_columns: Optional['TableColumnCollection']):
    if table_columns is None:
      del self.table_columns
      return
    if not isinstance(table_columns, TableColumnCollection):
      raise TypeError('table_columns must be of type TableColumnCollection')
    self._table_columns = table_columns

  @property
  def metrics_calculation_skip_reason(self) -> 'MetricsCalculationSkipReason':
    return self._metrics_calculation_skip_reason or MetricsCalculationSkipReason.METRICS_CALCULATION_SKIP_REASON_UNSPECIFIED

  @metrics_calculation_skip_reason.setter
  def metrics_calculation_skip_reason(self, metrics_calculation_skip_reason: Optional['MetricsCalculationSkipReason']):
    if metrics_calculation_skip_reason is None:
      del self.metrics_calculation_skip_reason
      return
    if not isinstance(metrics_calculation_skip_reason, MetricsCalculationSkipReason):
      raise TypeError('metrics_calculation_skip_reason must be of type MetricsCalculationSkipReason')
    self._metrics_calculation_skip_reason = metrics_calculation_skip_reason


class TableInfoComputedFields(KaggleObject):
  r"""
  Attributes:
    total_columns (int)
  """

  def __init__(self):
    self._total_columns = 0
    self._freeze()

  @property
  def total_columns(self) -> int:
    return self._total_columns

  @total_columns.setter
  def total_columns(self, total_columns: int):
    if total_columns is None:
      del self.total_columns
      return
    if not isinstance(total_columns, int):
      raise TypeError('total_columns must be of type int')
    self._total_columns = total_columns


BigqueryInfo._fields = [
  FieldMetadata("projectId", "project_id", "_project_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceLastModifiedDate", "source_last_modified_date", "_source_last_modified_date", datetime, None, DateTimeSerializer()),
]

BigquerySnapshotInfo._fields = [
  FieldMetadata("sourceLastModifiedDate", "source_last_modified_date", "_source_last_modified_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("bigqueryTables", "bigquery_tables", "_bigquery_tables", TableCollection, None, KaggleObjectSerializer()),
]

BooleanMetrics._fields = [
  FieldMetadata("trueCount", "true_count", "_true_count", int, 0, PredefinedSerializer()),
  FieldMetadata("falseCount", "false_count", "_false_count", int, 0, PredefinedSerializer()),
]

BooleanMetricsComputedFields._fields = [
  FieldMetadata("histogram", "histogram", "_histogram", Histogram, None, KaggleObjectSerializer()),
]

ColumnSummaryInfo._fields = [
  FieldMetadata("columnTypes", "column_types", "_column_types", ColumnTypeSummaryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("sampleColumnNames", "sample_column_names", "_sample_column_names", str, [], ListSerializer(PredefinedSerializer())),
]

ColumnSummaryInfoComputedFields._fields = [
  FieldMetadata("totalColumnCount", "total_column_count", "_total_column_count", int, 0, PredefinedSerializer()),
]

ColumnTypeSummaryInfo._fields = [
  FieldMetadata("columnType", "column_type", "_column_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("columnCount", "column_count", "_column_count", int, 0, PredefinedSerializer()),
  FieldMetadata("rowCount", "row_count", "_row_count", int, 0, PredefinedSerializer()),
]

ColumnUpdateInfo._fields = [
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", HarmonizedDataType, HarmonizedDataType.STRING, EnumSerializer()),
  FieldMetadata("extendedType", "extended_type", "_extended_type", ExtendedDataType, ExtendedDataType.EXTENDED_DATA_TYPE_UNSPECIFIED, EnumSerializer()),
]

CompetitionInfo._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionSlug", "competition_slug", "_competition_slug", str, None, PredefinedSerializer(), optional=True),
]

CompressionInfo._fields = [
  FieldMetadata("filename", "filename", "_filename", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileExtension", "file_extension", "_file_extension", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileSize", "file_size", "_file_size", int, 0, PredefinedSerializer()),
  FieldMetadata("contentEncoding", "content_encoding", "_content_encoding", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentMd5", "content_md5", "_content_md5", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("archiveGcsUrl", "archive_gcs_url", "_archive_gcs_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationLastUpdate", "creation_last_update", "_creation_last_update", datetime, None, DateTimeSerializer()),
  FieldMetadata("creationPercentComplete", "creation_percent_complete", "_creation_percent_complete", float, None, PredefinedSerializer(), optional=True),
]

ContainerInfo._fields = [
  FieldMetadata("totalChildren", "total_children", "_total_children", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

CountryMetrics._fields = [
  FieldMetadata("counts", "counts", "_counts", FrequencyCount, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("uniqueValueCount", "unique_value_count", "_unique_value_count", int, 0, PredefinedSerializer()),
]

CountryMetricsComputedFields._fields = [
  FieldMetadata("mostCommonValue", "most_common_value", "_most_common_value", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mostCommonValueCount", "most_common_value_count", "_most_common_value_count", int, 0, PredefinedSerializer()),
]

CroissantInfo._fields = [
  FieldMetadata("autoGenCroissantGcsUrl", "auto_gen_croissant_gcs_url", "_auto_gen_croissant_gcs_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("autoGenCroissantCreateTime", "auto_gen_croissant_create_time", "_auto_gen_croissant_create_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("autoGenCroissantTotalSize", "auto_gen_croissant_total_size", "_auto_gen_croissant_total_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("autoGenCroissantVersionNumber", "auto_gen_croissant_version_number", "_auto_gen_croissant_version_number", str, None, PredefinedSerializer(), optional=True),
]

Databundle._fields = [
  FieldMetadata("databundleInfo", "databundle_info", "_databundle_info", DatabundleInfo, None, KaggleObjectSerializer()),
  FieldMetadata("datasetInfo", "dataset_info", "_dataset_info", DatasetInfo, None, KaggleObjectSerializer()),
  FieldMetadata("competitionInfo", "competition_info", "_competition_info", CompetitionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("remoteDatasourceInfo", "remote_datasource_info", "_remote_datasource_info", RemoteDatasourceInfo, None, KaggleObjectSerializer()),
  FieldMetadata("bigqueryInfo", "bigquery_info", "_bigquery_info", BigqueryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("githubInfo", "github_info", "_github_info", GithubInfo, None, KaggleObjectSerializer()),
  FieldMetadata("modelInstanceInfo", "model_instance_info", "_model_instance_info", ModelInstanceInfo, None, KaggleObjectSerializer()),
  FieldMetadata("huggingFaceInfo", "hugging_face_info", "_hugging_face_info", HuggingFaceInfo, None, KaggleObjectSerializer()),
]

DatabundleInfo._fields = [
  FieldMetadata("currentDatabundleVersionId", "current_databundle_version_id", "_current_databundle_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("databundleType", "databundle_type", "_databundle_type", DatabundleType, DatabundleType.DATABUNDLE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("diffType", "diff_type", "_diff_type", DatabundleDiffType, DatabundleDiffType.REALTIME, EnumSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("removalDate", "removal_date", "_removal_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("currentGoodVersionKey", "current_good_version_key", "_current_good_version_key", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastestVersionKey", "lastest_version_key", "_lastest_version_key", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versions", "versions", "_versions", DatabundleVersionCollection, None, KaggleObjectSerializer()),
]

DatabundleOwnerCompetitionInfo._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scope", "scope", "_scope", str, None, PredefinedSerializer(), optional=True),
]

DatabundleOwnerDatasetInfo._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scope", "scope", "_scope", str, None, PredefinedSerializer(), optional=True),
]

DatabundleOwnerInfo._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("dataset", "dataset", "_dataset", DatabundleOwnerDatasetInfo, None, KaggleObjectSerializer()),
  FieldMetadata("competition", "competition", "_competition", DatabundleOwnerCompetitionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("kernel", "kernel", "_kernel", DatabundleOwnerKernelInfo, None, KaggleObjectSerializer()),
  FieldMetadata("previewsDisabled", "previews_disabled", "_previews_disabled", bool, False, PredefinedSerializer()),
]

DatabundleOwnerKernelInfo._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("scope", "scope", "_scope", str, None, PredefinedSerializer(), optional=True),
]

DatabundleVerificationInfo._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetHashLink", "dataset_hash_link", "_dataset_hash_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("privateDatabundleCompetitionId", "private_databundle_competition_id", "_private_databundle_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, None, PredefinedSerializer(), optional=True),
]

DatabundleVersion._fields = [
  FieldMetadata("databundleVersionInfo", "databundle_version_info", "_databundle_version_info", DatabundleVersionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("datasetVersionInfo", "dataset_version_info", "_dataset_version_info", DatasetVersionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("statusInfo", "status_info", "_status_info", StatusInfo, None, KaggleObjectSerializer()),
  FieldMetadata("exceptionInfo", "exception_info", "_exception_info", ExceptionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("filesetInfo", "fileset_info", "_fileset_info", DirectoryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("originalCompressionInfo", "original_compression_info", "_original_compression_info", CompressionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("bundleCompressionInfo", "bundle_compression_info", "_bundle_compression_info", CompressionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("bigquerySnapshotInfo", "bigquery_snapshot_info", "_bigquery_snapshot_info", BigquerySnapshotInfo, None, KaggleObjectSerializer()),
  FieldMetadata("storageInfo", "storage_info", "_storage_info", StorageInfo, None, KaggleObjectSerializer()),
  FieldMetadata("fileSummaryInfo", "file_summary_info", "_file_summary_info", FileSummaryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("columnSummaryInfo", "column_summary_info", "_column_summary_info", ColumnSummaryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("externalCopyInfo", "external_copy_info", "_external_copy_info", ExternalCopyInfo, None, KaggleObjectSerializer()),
  FieldMetadata("originalRemoteUrlInfo", "original_remote_url_info", "_original_remote_url_info", OriginalRemoteUrlInfo, None, KaggleObjectSerializer()),
  FieldMetadata("modelInstanceVersionInfo", "model_instance_version_info", "_model_instance_version_info", ModelInstanceVersionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("croissantInfo", "croissant_info", "_croissant_info", CroissantInfo, None, KaggleObjectSerializer()),
  FieldMetadata("hashInfo", "hash_info", "_hash_info", HashInfo, None, KaggleObjectSerializer()),
]

DatabundleVersionCollection._fields = []

DatabundleVersionCollectionContainerInfo._fields = [
  FieldMetadata("children", "children", "_children", DatabundleVersion, [], ListSerializer(KaggleObjectSerializer())),
]

DatabundleVersionInfo._fields = [
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("creationDate", "creation_date", "_creation_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("removalDate", "removal_date", "_removal_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("databundleVersionType", "databundle_version_type", "_databundle_version_type", DatabundleVersionType, DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("objectTypeCount", "object_type_count", "_object_type_count", int, {}, MapSerializer(PredefinedSerializer())),
]

DataObjectBaseInfo._fields = [
  FieldMetadata("type", "type", "_type", ObjectType, ObjectType.OBJECT_TYPE_GENERIC, EnumSerializer()),
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("path", "path", "_path", str, "", PredefinedSerializer()),
  FieldMetadata("legacyEntityId", "legacy_entity_id", "_legacy_entity_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("relativeUrl", "relative_url", "_relative_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
]

DatasetInfo._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetSlug", "dataset_slug", "_dataset_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
]

DatasetVersionInfo._fields = [
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
]

DataSource.ModelGatingInfo._fields = [
  FieldMetadata("isAgreementGated", "is_agreement_gated", "_is_agreement_gated", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLicenseGated", "is_license_gated", "_is_license_gated", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gatingStatus", "gating_status", "_gating_status", UnifiedModelGatingStatus, None, EnumSerializer(), optional=True),
]

DataSource.ModelInfo._fields = [
  FieldMetadata("isTfhubModel", "is_tfhub_model", "_is_tfhub_model", bool, False, PredefinedSerializer()),
  FieldMetadata("modelFramework", "model_framework", "_model_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("canUse", "can_use", "_can_use", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gatingInfo", "gating_info", "_gating_info", DataSource.ModelGatingInfo, None, KaggleObjectSerializer(), optional=True),
]

DataSource._fields = [
  FieldMetadata("databundle", "databundle", "_databundle", Databundle, None, KaggleObjectSerializer()),
  FieldMetadata("databundleVersion", "databundle_version", "_databundle_version", DatabundleVersion, None, KaggleObjectSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mountSlug", "mount_slug", "_mount_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastUpdated", "last_updated", "_last_updated", datetime, None, DateTimeSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceType", "source_type", "_source_type", DataSourceType, DataSourceType.DATA_SOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("sourceId", "source_id", "_source_id", int, 0, PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("state", "state", "_state", DataSourceState, DataSourceState.DATA_SOURCE_STATE_PUBLIC, EnumSerializer()),
  FieldMetadata("kernelOutputInfo", "kernel_output_info", "_kernel_output_info", KernelOutputInfo, None, KaggleObjectSerializer()),
  FieldMetadata("modelInfo", "model_info", "_model_info", DataSource.ModelInfo, None, KaggleObjectSerializer()),
  FieldMetadata("canEdit", "can_edit", "_can_edit", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPinned", "is_pinned", "_is_pinned", bool, None, PredefinedSerializer(), optional=True),
]

DateTimeHistogram._fields = [
  FieldMetadata("buckets", "buckets", "_buckets", DateTimeHistogramBucket, [], ListSerializer(KaggleObjectSerializer())),
]

DateTimeHistogramBucket._fields = [
  FieldMetadata("index", "index", "_index", int, 0, PredefinedSerializer()),
  FieldMetadata("label", "label", "_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("leftValue", "left_value", "_left_value", datetime, None, DateTimeSerializer()),
  FieldMetadata("rightValue", "right_value", "_right_value", datetime, None, DateTimeSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

DateTimeMetrics._fields = [
  FieldMetadata("mean", "mean", "_mean", datetime, None, DateTimeSerializer()),
  FieldMetadata("minimum", "minimum", "_minimum", datetime, None, DateTimeSerializer()),
  FieldMetadata("maximum", "maximum", "_maximum", datetime, None, DateTimeSerializer()),
  FieldMetadata("histogram", "histogram", "_histogram", DateTimeHistogram, None, KaggleObjectSerializer()),
]

Directory._fields = [
  FieldMetadata("directoryInfo", "directory_info", "_directory_info", DirectoryInfo, None, KaggleObjectSerializer()),
  FieldMetadata("compressionInfo", "compression_info", "_compression_info", CompressionInfo, None, KaggleObjectSerializer()),
  FieldMetadata("kernelSessionInfo", "kernel_session_info", "_kernel_session_info", KernelSessionInfo, None, KaggleObjectSerializer()),
]

DirectoryCollection._fields = []

DirectoryCollectionContainerInfo._fields = [
  FieldMetadata("children", "children", "_children", Directory, [], ListSerializer(KaggleObjectSerializer())),
]

DirectoryInfo._fields = [
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("directories", "directories", "_directories", DirectoryCollection, None, KaggleObjectSerializer()),
  FieldMetadata("files", "files", "_files", FileCollection, None, KaggleObjectSerializer()),
]

ExcelInfo._fields = [
  FieldMetadata("tables", "tables", "_tables", TableCollection, None, KaggleObjectSerializer()),
]

ExceptionInfo._fields = [
  FieldMetadata("criticalException", "critical_exception", "_critical_exception", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("warningExceptions", "warning_exceptions", "_warning_exceptions", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("analysisException", "analysis_exception", "_analysis_exception", str, None, PredefinedSerializer(), optional=True),
]

ExternalCopy._fields = [
  FieldMetadata("bucket", "bucket", "_bucket", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("path", "path", "_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("region", "region", "_region", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastCopied", "last_copied", "_last_copied", datetime, None, DateTimeSerializer()),
  FieldMetadata("status", "status", "_status", ExternalCopyStatus, ExternalCopyStatus.EXTERNAL_COPY_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("lastUpdate", "last_update", "_last_update", datetime, None, DateTimeSerializer()),
  FieldMetadata("percentFinished", "percent_finished", "_percent_finished", float, None, PredefinedSerializer(), optional=True),
]

ExternalCopyInfo._fields = [
  FieldMetadata("externalCopies", "external_copies", "_external_copies", ExternalCopy, [], ListSerializer(KaggleObjectSerializer())),
]

File._fields = [
  FieldMetadata("fileInfo", "file_info", "_file_info", FileInfo, None, KaggleObjectSerializer()),
  FieldMetadata("fileTableInfo", "file_table_info", "_file_table_info", FileTableInfo, None, KaggleObjectSerializer()),
  FieldMetadata("tableInfo", "table_info", "_table_info", TableInfo, None, KaggleObjectSerializer()),
  FieldMetadata("sqliteInfo", "sqlite_info", "_sqlite_info", SqliteInfo, None, KaggleObjectSerializer()),
  FieldMetadata("excelInfo", "excel_info", "_excel_info", ExcelInfo, None, KaggleObjectSerializer()),
  FieldMetadata("remoteUrlInfo", "remote_url_info", "_remote_url_info", RemoteUrlInfo, None, KaggleObjectSerializer()),
  FieldMetadata("kernelSessionInfo", "kernel_session_info", "_kernel_session_info", KernelSessionInfo, None, KaggleObjectSerializer()),
]

FileCollection._fields = []

FileCollectionContainerInfo._fields = [
  FieldMetadata("children", "children", "_children", File, [], ListSerializer(KaggleObjectSerializer())),
]

FileExtensionSummaryInfo._fields = [
  FieldMetadata("extension", "extension", "_extension", str, "", PredefinedSerializer()),
  FieldMetadata("fileCount", "file_count", "_file_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

FileInfo._fields = [
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
  FieldMetadata("fullPath", "full_path", "_full_path", str, "", PredefinedSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fileExtension", "file_extension", "_file_extension", str, "", PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, "", PredefinedSerializer()),
  FieldMetadata("contentMd5", "content_md5", "_content_md5", str, "", PredefinedSerializer()),
  FieldMetadata("gcsUrl", "gcs_url", "_gcs_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("gcsCompressedUrl", "gcs_compressed_url", "_gcs_compressed_url", str, None, PredefinedSerializer(), optional=True),
]

FileSummaryInfo._fields = [
  FieldMetadata("fileTypes", "file_types", "_file_types", FileExtensionSummaryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("sampleFileNames", "sample_file_names", "_sample_file_names", str, [], ListSerializer(PredefinedSerializer())),
]

FileSummaryInfoComputedFields._fields = [
  FieldMetadata("totalFileCount", "total_file_count", "_total_file_count", int, 0, PredefinedSerializer()),
]

FileTableInfo._fields = [
  FieldMetadata("includesHeader", "includes_header", "_includes_header", bool, False, PredefinedSerializer()),
  FieldMetadata("headerRow", "header_row", "_header_row", int, 0, PredefinedSerializer()),
  FieldMetadata("delimiter", "delimiter", "_delimiter", str, None, PredefinedSerializer(), optional=True),
]

FrequencyCount._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", int, 0, PredefinedSerializer()),
]

GithubInfo._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("repositorySlug", "repository_slug", "_repository_slug", str, "", PredefinedSerializer()),
  FieldMetadata("lastUpdatedHash", "last_updated_hash", "_last_updated_hash", str, None, PredefinedSerializer(), optional=True),
]

HashInfo._fields = [
  FieldMetadata("rawDataHash", "raw_data_hash", "_raw_data_hash", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("uploadDataHash", "upload_data_hash", "_upload_data_hash", str, None, PredefinedSerializer(), optional=True),
]

Histogram._fields = [
  FieldMetadata("buckets", "buckets", "_buckets", HistogramBucket, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("type", "type", "_type", HarmonizedDataType, HarmonizedDataType.STRING, EnumSerializer()),
]

HistogramBucket._fields = [
  FieldMetadata("index", "index", "_index", int, 0, PredefinedSerializer()),
  FieldMetadata("label", "label", "_label", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("leftValue", "left_value", "_left_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("rightValue", "right_value", "_right_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

HuggingFaceInfo._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("repoId", "repo_id", "_repo_id", str, "", PredefinedSerializer()),
  FieldMetadata("revision", "revision", "_revision", str, "", PredefinedSerializer()),
  FieldMetadata("encryptedHuggingFaceAccessToken", "encrypted_hugging_face_access_token", "_encrypted_hugging_face_access_token", str, None, PredefinedSerializer(), optional=True),
]

KernelOutputInfo._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

KernelSessionInfo._fields = [
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, 0, PredefinedSerializer()),
]

ModelInstanceInfo._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isPrivate", "is_private", "_is_private", bool, False, PredefinedSerializer()),
]

ModelInstanceVersionInfo._fields = [
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
]

NumericMetrics._fields = [
  FieldMetadata("finiteCount", "finite_count", "_finite_count", int, 0, PredefinedSerializer()),
  FieldMetadata("infiniteCount", "infinite_count", "_infinite_count", int, 0, PredefinedSerializer()),
  FieldMetadata("mean", "mean", "_mean", float, 0.0, PredefinedSerializer()),
  FieldMetadata("standardDeviation", "standard_deviation", "_standard_deviation", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minimum", "minimum", "_minimum", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minimumFinite", "minimum_finite", "_minimum_finite", float, 0.0, PredefinedSerializer()),
  FieldMetadata("maximum", "maximum", "_maximum", float, 0.0, PredefinedSerializer()),
  FieldMetadata("maximumFinite", "maximum_finite", "_maximum_finite", float, 0.0, PredefinedSerializer()),
  FieldMetadata("quantiles", "quantiles", "_quantiles", Quantile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("histogram", "histogram", "_histogram", Histogram, None, KaggleObjectSerializer()),
]

OriginalRemoteUrlInfo._fields = [
  FieldMetadata("originalRemoteUrls", "original_remote_urls", "_original_remote_urls", RemoteUrlInfo, [], ListSerializer(KaggleObjectSerializer())),
]

Quantile._fields = [
  FieldMetadata("point", "point", "_point", float, 0.0, PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", float, 0.0, PredefinedSerializer()),
]

RemoteDatasourceInfo._fields = [
  FieldMetadata("updateFrequency", "update_frequency", "_update_frequency", RemoteUrlUpdateFrequency, RemoteUrlUpdateFrequency.DAILY, EnumSerializer()),
]

RemoteUrlInfo._fields = [
  FieldMetadata("url", "url", "_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
]

SqliteInfo._fields = [
  FieldMetadata("tables", "tables", "_tables", TableCollection, None, KaggleObjectSerializer()),
]

StatusInfo._fields = [
  FieldMetadata("status", "status", "_status", DatabundleStatus, DatabundleStatus.DATABUNDLE_STATUS_CREATED, EnumSerializer()),
  FieldMetadata("statusMessage", "status_message", "_status_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("percentageCompleted", "percentage_completed", "_percentage_completed", float, 0.0, PredefinedSerializer()),
  FieldMetadata("analysisStatus", "analysis_status", "_analysis_status", DatabundleVersionAnalysisStatus, None, EnumSerializer(), optional=True),
]

StorageInfo._fields = [
  FieldMetadata("uploadDataLocation", "upload_data_location", "_upload_data_location", StorageLocation, None, KaggleObjectSerializer()),
  FieldMetadata("rawDataLocation", "raw_data_location", "_raw_data_location", StorageLocation, None, KaggleObjectSerializer()),
  FieldMetadata("individualCompressedLocation", "individual_compressed_location", "_individual_compressed_location", StorageLocation, None, KaggleObjectSerializer()),
  FieldMetadata("bundleArchiveLocation", "bundle_archive_location", "_bundle_archive_location", StorageLocation, None, KaggleObjectSerializer()),
  FieldMetadata("fileSystemLocation", "file_system_location", "_file_system_location", StorageLocation, None, KaggleObjectSerializer()),
  FieldMetadata("autoGenCroissantLocation", "auto_gen_croissant_location", "_auto_gen_croissant_location", StorageLocation, None, KaggleObjectSerializer()),
]

StringMetrics._fields = [
  FieldMetadata("counts", "counts", "_counts", FrequencyCount, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("uniqueValueCount", "unique_value_count", "_unique_value_count", int, 0, PredefinedSerializer()),
]

StringMetricsComputedFields._fields = [
  FieldMetadata("mostCommonValue", "most_common_value", "_most_common_value", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("mostCommonValueCount", "most_common_value_count", "_most_common_value_count", int, 0, PredefinedSerializer()),
]

Table._fields = [
  FieldMetadata("tableInfo", "table_info", "_table_info", TableInfo, None, KaggleObjectSerializer()),
]

TableCollection._fields = []

TableCollectionContainerInfo._fields = [
  FieldMetadata("children", "children", "_children", Table, [], ListSerializer(KaggleObjectSerializer())),
]

TableColumn._fields = [
  FieldMetadata("tableColumnInfo", "table_column_info", "_table_column_info", TableColumnInfo, None, KaggleObjectSerializer()),
  FieldMetadata("tableColumnMetrics", "table_column_metrics", "_table_column_metrics", TableColumnMetrics, None, KaggleObjectSerializer()),
]

TableColumnCollection._fields = []

TableColumnCollectionContainerInfo._fields = [
  FieldMetadata("children", "children", "_children", TableColumn, [], ListSerializer(KaggleObjectSerializer())),
]

TableColumnInfo._fields = [
  FieldMetadata("order", "order", "_order", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("originalType", "original_type", "_original_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", HarmonizedDataType, HarmonizedDataType.STRING, EnumSerializer()),
  FieldMetadata("extendedType", "extended_type", "_extended_type", ExtendedDataType, ExtendedDataType.EXTENDED_DATA_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isNullable", "is_nullable", "_is_nullable", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPrimaryKey", "is_primary_key", "_is_primary_key", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLabel", "is_label", "_is_label", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("typeIsSuggested", "type_is_suggested", "_type_is_suggested", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("descriptionIsSuggested", "description_is_suggested", "_description_is_suggested", bool, None, PredefinedSerializer(), optional=True),
]

TableColumnMetrics._fields = [
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("nullCount", "null_count", "_null_count", int, 0, PredefinedSerializer()),
  FieldMetadata("nonNullCount", "non_null_count", "_non_null_count", int, 0, PredefinedSerializer()),
  FieldMetadata("validCount", "valid_count", "_valid_count", int, 0, PredefinedSerializer()),
  FieldMetadata("invalidCount", "invalid_count", "_invalid_count", int, 0, PredefinedSerializer()),
  FieldMetadata("booleanMetrics", "boolean_metrics", "_boolean_metrics", BooleanMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("numericMetrics", "numeric_metrics", "_numeric_metrics", NumericMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("dateTimeMetrics", "date_time_metrics", "_date_time_metrics", DateTimeMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("stringMetrics", "string_metrics", "_string_metrics", StringMetrics, None, KaggleObjectSerializer()),
  FieldMetadata("countryMetrics", "country_metrics", "_country_metrics", CountryMetrics, None, KaggleObjectSerializer()),
]

TableColumnMetricsComputedFields._fields = [
  FieldMetadata("totalCount", "total_count", "_total_count", int, 0, PredefinedSerializer()),
]

TableInfo._fields = [
  FieldMetadata("totalRows", "total_rows", "_total_rows", int, 0, PredefinedSerializer()),
  FieldMetadata("tableColumns", "table_columns", "_table_columns", TableColumnCollection, None, KaggleObjectSerializer()),
  FieldMetadata("metricsCalculationSkipReason", "metrics_calculation_skip_reason", "_metrics_calculation_skip_reason", MetricsCalculationSkipReason, None, EnumSerializer(), optional=True),
]

TableInfoComputedFields._fields = [
  FieldMetadata("totalColumns", "total_columns", "_total_columns", int, 0, PredefinedSerializer()),
]

