from kagglesdk.datasets.databundles.types.databundle_types import ColumnUpdateInfo, DatabundleVerificationInfo, DataSource, Directory, File, Table, TableColumn
from kagglesdk.datasets.types.dataset_enums import DatabundleType
from kagglesdk.datasets.types.dataset_types import DatasetUsabilityRating
from kagglesdk.kaggle_object import *
from kagglesdk.security.types.security_types import KaggleResourceType
from typing import List, Optional

class CheckFileUploadsRequest(KaggleObject):
  r"""
  Perform a validation check on all uploaded files.

  Our initial use case is determining if any of the files are flagged for
  moderation. We compare the files' MD5 hashes against a list of
  known flagged files in the MODERATION_FILE_HASHES ops flag.

  Attributes:
    blob_file_tokens (str)
    entity_type (KaggleResourceType)
      The entity that is being created with these file uploads. ex: Dataset,
      Model, Competition Dataset
  """

  def __init__(self):
    self._blob_file_tokens = []
    self._entity_type = KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def blob_file_tokens(self) -> Optional[List[str]]:
    return self._blob_file_tokens

  @blob_file_tokens.setter
  def blob_file_tokens(self, blob_file_tokens: Optional[List[str]]):
    if blob_file_tokens is None:
      del self.blob_file_tokens
      return
    if not isinstance(blob_file_tokens, list):
      raise TypeError('blob_file_tokens must be of type list')
    if not all([isinstance(t, str) for t in blob_file_tokens]):
      raise TypeError('blob_file_tokens must contain only items of type str')
    self._blob_file_tokens = blob_file_tokens

  @property
  def entity_type(self) -> 'KaggleResourceType':
    r"""
    The entity that is being created with these file uploads. ex: Dataset,
    Model, Competition Dataset
    """
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleResourceType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleResourceType):
      raise TypeError('entity_type must be of type KaggleResourceType')
    self._entity_type = entity_type


class CheckFileUploadsResponse(KaggleObject):
  r"""
  Attributes:
    flagged_files_detected (bool)
      True if any of the uploaded files match (on MD5 hash) with any of the known
      flagged files in the MODERATION_FILE_HASHES ops flag.
  """

  def __init__(self):
    self._flagged_files_detected = False
    self._freeze()

  @property
  def flagged_files_detected(self) -> bool:
    r"""
    True if any of the uploaded files match (on MD5 hash) with any of the known
    flagged files in the MODERATION_FILE_HASHES ops flag.
    """
    return self._flagged_files_detected

  @flagged_files_detected.setter
  def flagged_files_detected(self, flagged_files_detected: bool):
    if flagged_files_detected is None:
      del self.flagged_files_detected
      return
    if not isinstance(flagged_files_detected, bool):
      raise TypeError('flagged_files_detected must be of type bool')
    self._flagged_files_detected = flagged_files_detected


class ColumnBaseInfo(KaggleObject):
  r"""
  Attributes:
    name (str)
    firestore_path (str)
    order (int)
  """

  def __init__(self):
    self._name = ""
    self._firestore_path = ""
    self._order = 0
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
  def order(self) -> int:
    return self._order

  @order.setter
  def order(self, order: int):
    if order is None:
      del self.order
      return
    if not isinstance(order, int):
      raise TypeError('order must be of type int')
    self._order = order


class GetDatabundleExternalChildrenRequest(KaggleObject):
  r"""
  Request to get (more) children for a data object for the data explorer
  frontend component. For example, a directory might contain 100 files, and
  we're showing only the first 50. This request gets triggered for loading the
  next 50.

  Attributes:
    verification_info (DatabundleVerificationInfo)
    firestore_path (str)
      Path for the actual object
    offset (int)
    count (int)
    depth (int)
    enforce_max_depth_constraint (bool)
  """

  def __init__(self):
    self._verification_info = None
    self._firestore_path = None
    self._offset = 0
    self._count = 0
    self._depth = 0
    self._enforce_max_depth_constraint = None
    self._freeze()

  @property
  def verification_info(self) -> Optional['DatabundleVerificationInfo']:
    return self._verification_info

  @verification_info.setter
  def verification_info(self, verification_info: Optional['DatabundleVerificationInfo']):
    if verification_info is None:
      del self.verification_info
      return
    if not isinstance(verification_info, DatabundleVerificationInfo):
      raise TypeError('verification_info must be of type DatabundleVerificationInfo')
    self._verification_info = verification_info

  @property
  def firestore_path(self) -> str:
    """Path for the actual object"""
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
  def offset(self) -> int:
    return self._offset

  @offset.setter
  def offset(self, offset: int):
    if offset is None:
      del self.offset
      return
    if not isinstance(offset, int):
      raise TypeError('offset must be of type int')
    self._offset = offset

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
  def depth(self) -> int:
    return self._depth

  @depth.setter
  def depth(self, depth: int):
    if depth is None:
      del self.depth
      return
    if not isinstance(depth, int):
      raise TypeError('depth must be of type int')
    self._depth = depth

  @property
  def enforce_max_depth_constraint(self) -> bool:
    return self._enforce_max_depth_constraint or False

  @enforce_max_depth_constraint.setter
  def enforce_max_depth_constraint(self, enforce_max_depth_constraint: Optional[bool]):
    if enforce_max_depth_constraint is None:
      del self.enforce_max_depth_constraint
      return
    if not isinstance(enforce_max_depth_constraint, bool):
      raise TypeError('enforce_max_depth_constraint must be of type bool')
    self._enforce_max_depth_constraint = enforce_max_depth_constraint


class GetDatabundleExternalChildrenResponse(KaggleObject):
  r"""
  Attributes:
    directories (Directory)
    files (File)
    tables (Table)
    table_columns (TableColumn)
  """

  def __init__(self):
    self._directories = []
    self._files = []
    self._tables = []
    self._table_columns = []
    self._freeze()

  @property
  def directories(self) -> Optional[List[Optional['Directory']]]:
    return self._directories

  @directories.setter
  def directories(self, directories: Optional[List[Optional['Directory']]]):
    if directories is None:
      del self.directories
      return
    if not isinstance(directories, list):
      raise TypeError('directories must be of type list')
    if not all([isinstance(t, Directory) for t in directories]):
      raise TypeError('directories must contain only items of type Directory')
    self._directories = directories

  @property
  def files(self) -> Optional[List[Optional['File']]]:
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['File']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, File) for t in files]):
      raise TypeError('files must contain only items of type File')
    self._files = files

  @property
  def tables(self) -> Optional[List[Optional['Table']]]:
    return self._tables

  @tables.setter
  def tables(self, tables: Optional[List[Optional['Table']]]):
    if tables is None:
      del self.tables
      return
    if not isinstance(tables, list):
      raise TypeError('tables must be of type list')
    if not all([isinstance(t, Table) for t in tables]):
      raise TypeError('tables must contain only items of type Table')
    self._tables = tables

  @property
  def table_columns(self) -> Optional[List[Optional['TableColumn']]]:
    return self._table_columns

  @table_columns.setter
  def table_columns(self, table_columns: Optional[List[Optional['TableColumn']]]):
    if table_columns is None:
      del self.table_columns
      return
    if not isinstance(table_columns, list):
      raise TypeError('table_columns must be of type list')
    if not all([isinstance(t, TableColumn) for t in table_columns]):
      raise TypeError('table_columns must contain only items of type TableColumn')
    self._table_columns = table_columns


class GetDatabundleExternalColumnsByFirestorePathRequest(KaggleObject):
  r"""
  Request to get columns by FirestorePath (not necessarily in storage order).

  Attributes:
    verification_info (DatabundleVerificationInfo)
    firestore_paths (str)
      Note: These are the paths of individual columns, not the path of the parent
      object!
  """

  def __init__(self):
    self._verification_info = None
    self._firestore_paths = []
    self._freeze()

  @property
  def verification_info(self) -> Optional['DatabundleVerificationInfo']:
    return self._verification_info

  @verification_info.setter
  def verification_info(self, verification_info: Optional['DatabundleVerificationInfo']):
    if verification_info is None:
      del self.verification_info
      return
    if not isinstance(verification_info, DatabundleVerificationInfo):
      raise TypeError('verification_info must be of type DatabundleVerificationInfo')
    self._verification_info = verification_info

  @property
  def firestore_paths(self) -> Optional[List[str]]:
    r"""
    Note: These are the paths of individual columns, not the path of the parent
    object!
    """
    return self._firestore_paths

  @firestore_paths.setter
  def firestore_paths(self, firestore_paths: Optional[List[str]]):
    if firestore_paths is None:
      del self.firestore_paths
      return
    if not isinstance(firestore_paths, list):
      raise TypeError('firestore_paths must be of type list')
    if not all([isinstance(t, str) for t in firestore_paths]):
      raise TypeError('firestore_paths must contain only items of type str')
    self._firestore_paths = firestore_paths


class GetDatabundleExternalColumnsByFirestorePathResponse(KaggleObject):
  r"""
  Attributes:
    columns (TableColumn)
  """

  def __init__(self):
    self._columns = []
    self._freeze()

  @property
  def columns(self) -> Optional[List[Optional['TableColumn']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['TableColumn']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, TableColumn) for t in columns]):
      raise TypeError('columns must contain only items of type TableColumn')
    self._columns = columns


class GetDatabundleExternalColumnsRequest(KaggleObject):
  r"""
  Request to get *all* columns for a given data object (file, table). Since
  this can be a lot of data (e.g. for 10k columns, we're only returning name,
  firestorepath and order here). Which columns are actually displayed will then
  depend on the user's selection (this is just to get a summary and allow them
  to do the selection).

  Attributes:
    verification_info (DatabundleVerificationInfo)
    firestore_path (str)
      Path for the actual object
  """

  def __init__(self):
    self._verification_info = None
    self._firestore_path = None
    self._freeze()

  @property
  def verification_info(self) -> Optional['DatabundleVerificationInfo']:
    return self._verification_info

  @verification_info.setter
  def verification_info(self, verification_info: Optional['DatabundleVerificationInfo']):
    if verification_info is None:
      del self.verification_info
      return
    if not isinstance(verification_info, DatabundleVerificationInfo):
      raise TypeError('verification_info must be of type DatabundleVerificationInfo')
    self._verification_info = verification_info

  @property
  def firestore_path(self) -> str:
    """Path for the actual object"""
    return self._firestore_path or ""

  @firestore_path.setter
  def firestore_path(self, firestore_path: Optional[str]):
    if firestore_path is None:
      del self.firestore_path
      return
    if not isinstance(firestore_path, str):
      raise TypeError('firestore_path must be of type str')
    self._firestore_path = firestore_path


class GetDatabundleExternalColumnsResponse(KaggleObject):
  r"""
  Attributes:
    columns (ColumnBaseInfo)
  """

  def __init__(self):
    self._columns = []
    self._freeze()

  @property
  def columns(self) -> Optional[List[Optional['ColumnBaseInfo']]]:
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['ColumnBaseInfo']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, ColumnBaseInfo) for t in columns]):
      raise TypeError('columns must contain only items of type ColumnBaseInfo')
    self._columns = columns


class GetDatabundleExternalRequest(KaggleObject):
  r"""
  Request to get databundle data (for the data explorer). DatabundleVersionId
  is required, as well as one of CompetitionId or DatasetId.
  - DatabundleVersionId: Main parameter to identify the databundle (version).
  - CompetitionId: Used to identify the competition and to handle access
  checks.
  - DatasetId: Used to identify the dataset and to handle access checks.

  Attributes:
    verification_info (DatabundleVerificationInfo)
  """

  def __init__(self):
    self._verification_info = None
    self._freeze()

  @property
  def verification_info(self) -> Optional['DatabundleVerificationInfo']:
    return self._verification_info

  @verification_info.setter
  def verification_info(self, verification_info: Optional['DatabundleVerificationInfo']):
    if verification_info is None:
      del self.verification_info
      return
    if not isinstance(verification_info, DatabundleVerificationInfo):
      raise TypeError('verification_info must be of type DatabundleVerificationInfo')
    self._verification_info = verification_info


class GetDatabundleExternalResponse(KaggleObject):
  r"""
  Attributes:
    data_source (DataSource)
  """

  def __init__(self):
    self._data_source = None
    self._freeze()

  @property
  def data_source(self) -> Optional['DataSource']:
    return self._data_source

  @data_source.setter
  def data_source(self, data_source: Optional['DataSource']):
    if data_source is None:
      del self.data_source
      return
    if not isinstance(data_source, DataSource):
      raise TypeError('data_source must be of type DataSource')
    self._data_source = data_source


class KickoffDatabundleHasherRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
      Starting request databundle version id (inclusive).
    count (int)
      Number of databundle-hasher requests to publish as an increment from the
      starting version id.
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._count = 0
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    """Starting request databundle version id (inclusive)."""
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
  def count(self) -> int:
    r"""
    Number of databundle-hasher requests to publish as an increment from the
    starting version id.
    """
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class KickoffFirestoreDeleteMigrationRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
      Starting request databundle version id (inclusive).
    count (int)
      Number of delete-migration requests to publish as an increment from the
      starting version id.
    delete_firestore_files (bool)
      Whether to actually delete the files in Firestore or to just emit a log.
    databundle_type (DatabundleType)
      The type of Databundles to include in the query.
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._count = 0
    self._delete_firestore_files = False
    self._databundle_type = DatabundleType.DATABUNDLE_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    """Starting request databundle version id (inclusive)."""
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
  def count(self) -> int:
    r"""
    Number of delete-migration requests to publish as an increment from the
    starting version id.
    """
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
  def delete_firestore_files(self) -> bool:
    """Whether to actually delete the files in Firestore or to just emit a log."""
    return self._delete_firestore_files

  @delete_firestore_files.setter
  def delete_firestore_files(self, delete_firestore_files: bool):
    if delete_firestore_files is None:
      del self.delete_firestore_files
      return
    if not isinstance(delete_firestore_files, bool):
      raise TypeError('delete_firestore_files must be of type bool')
    self._delete_firestore_files = delete_firestore_files

  @property
  def databundle_type(self) -> 'DatabundleType':
    """The type of Databundles to include in the query."""
    return self._databundle_type

  @databundle_type.setter
  def databundle_type(self, databundle_type: 'DatabundleType'):
    if databundle_type is None:
      del self.databundle_type
      return
    if not isinstance(databundle_type, DatabundleType):
      raise TypeError('databundle_type must be of type DatabundleType')
    self._databundle_type = databundle_type


class KickoffFirestoreWriteMigrationRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
      Starting request databundle version id (inclusive).
    count (int)
      Number of write-migration requests to publish as an increment from the
      starting version id.
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._count = 0
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    """Starting request databundle version id (inclusive)."""
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
  def count(self) -> int:
    r"""
    Number of write-migration requests to publish as an increment from the
    starting version id.
    """
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class KickoffHandlerResponse(KaggleObject):
  r"""
  Generic response message for above kickoff handlers.

  Attributes:
    last_databundle_version_id (int)
      Last published message's databundle version id.
  """

  def __init__(self):
    self._last_databundle_version_id = 0
    self._freeze()

  @property
  def last_databundle_version_id(self) -> int:
    """Last published message's databundle version id."""
    return self._last_databundle_version_id

  @last_databundle_version_id.setter
  def last_databundle_version_id(self, last_databundle_version_id: int):
    if last_databundle_version_id is None:
      del self.last_databundle_version_id
      return
    if not isinstance(last_databundle_version_id, int):
      raise TypeError('last_databundle_version_id must be of type int')
    self._last_databundle_version_id = last_databundle_version_id


class RestoreDatabundleVersionRequest(KaggleObject):
  r"""
  Attributes:
    databundle_version_id (int)
      Databundle version id to restore.
  """

  def __init__(self):
    self._databundle_version_id = 0
    self._freeze()

  @property
  def databundle_version_id(self) -> int:
    """Databundle version id to restore."""
    return self._databundle_version_id

  @databundle_version_id.setter
  def databundle_version_id(self, databundle_version_id: int):
    if databundle_version_id is None:
      del self.databundle_version_id
      return
    if not isinstance(databundle_version_id, int):
      raise TypeError('databundle_version_id must be of type int')
    self._databundle_version_id = databundle_version_id


class RestoreDatabundleVersionResponse(KaggleObject):
  r"""
  Attributes:
    count_restored_files (int)
      Number of files restored from GCS.
  """

  def __init__(self):
    self._count_restored_files = 0
    self._freeze()

  @property
  def count_restored_files(self) -> int:
    """Number of files restored from GCS."""
    return self._count_restored_files

  @count_restored_files.setter
  def count_restored_files(self, count_restored_files: int):
    if count_restored_files is None:
      del self.count_restored_files
      return
    if not isinstance(count_restored_files, int):
      raise TypeError('count_restored_files must be of type int')
    self._count_restored_files = count_restored_files


class UpdateDatabundleMetadataExternalRequest(KaggleObject):
  r"""
  Request for changing an object's metadata. This updates an object's
  description as well as optionally the descriptions + types for a set of
  provided columns (which have to be 'under' that object). Note: This currently
  does not return any updates to the usability rating, since it's entirely
  embedded within the data viewer v3. We should probably change this at some
  point.

  Attributes:
    verification_info (DatabundleVerificationInfo)
      For authorization checks.
    firestore_path (str)
      The path of the main object to be updated.
    description (str)
      Description of the main object (file / table) to be updated. Optional (in
      which case only columns are updated).
    columns (ColumnUpdateInfo)
      List of columns under that object to be also updated. Optional (in which
      case only the main description are updated).
  """

  def __init__(self):
    self._verification_info = None
    self._firestore_path = ""
    self._description = None
    self._columns = []
    self._freeze()

  @property
  def verification_info(self) -> Optional['DatabundleVerificationInfo']:
    """For authorization checks."""
    return self._verification_info

  @verification_info.setter
  def verification_info(self, verification_info: Optional['DatabundleVerificationInfo']):
    if verification_info is None:
      del self.verification_info
      return
    if not isinstance(verification_info, DatabundleVerificationInfo):
      raise TypeError('verification_info must be of type DatabundleVerificationInfo')
    self._verification_info = verification_info

  @property
  def firestore_path(self) -> str:
    """The path of the main object to be updated."""
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
    r"""
    Description of the main object (file / table) to be updated. Optional (in
    which case only columns are updated).
    """
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
  def columns(self) -> Optional[List[Optional['ColumnUpdateInfo']]]:
    r"""
    List of columns under that object to be also updated. Optional (in which
    case only the main description are updated).
    """
    return self._columns

  @columns.setter
  def columns(self, columns: Optional[List[Optional['ColumnUpdateInfo']]]):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, list):
      raise TypeError('columns must be of type list')
    if not all([isinstance(t, ColumnUpdateInfo) for t in columns]):
      raise TypeError('columns must contain only items of type ColumnUpdateInfo')
    self._columns = columns


class UpdateDatabundleMetadataExternalResponse(KaggleObject):
  r"""
  Attributes:
    usability_rating (DatasetUsabilityRating)
  """

  def __init__(self):
    self._usability_rating = None
    self._freeze()

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


CheckFileUploadsRequest._fields = [
  FieldMetadata("blobFileTokens", "blob_file_tokens", "_blob_file_tokens", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleResourceType, KaggleResourceType.KAGGLE_RESOURCE_TYPE_UNSPECIFIED, EnumSerializer()),
]

CheckFileUploadsResponse._fields = [
  FieldMetadata("flaggedFilesDetected", "flagged_files_detected", "_flagged_files_detected", bool, False, PredefinedSerializer()),
]

ColumnBaseInfo._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
  FieldMetadata("order", "order", "_order", int, 0, PredefinedSerializer()),
]

GetDatabundleExternalChildrenRequest._fields = [
  FieldMetadata("verificationInfo", "verification_info", "_verification_info", DatabundleVerificationInfo, None, KaggleObjectSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("offset", "offset", "_offset", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("depth", "depth", "_depth", int, 0, PredefinedSerializer()),
  FieldMetadata("enforceMaxDepthConstraint", "enforce_max_depth_constraint", "_enforce_max_depth_constraint", bool, None, PredefinedSerializer(), optional=True),
]

GetDatabundleExternalChildrenResponse._fields = [
  FieldMetadata("directories", "directories", "_directories", Directory, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("files", "files", "_files", File, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tables", "tables", "_tables", Table, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("tableColumns", "table_columns", "_table_columns", TableColumn, [], ListSerializer(KaggleObjectSerializer())),
]

GetDatabundleExternalColumnsByFirestorePathRequest._fields = [
  FieldMetadata("verificationInfo", "verification_info", "_verification_info", DatabundleVerificationInfo, None, KaggleObjectSerializer()),
  FieldMetadata("firestorePaths", "firestore_paths", "_firestore_paths", str, [], ListSerializer(PredefinedSerializer())),
]

GetDatabundleExternalColumnsByFirestorePathResponse._fields = [
  FieldMetadata("columns", "columns", "_columns", TableColumn, [], ListSerializer(KaggleObjectSerializer())),
]

GetDatabundleExternalColumnsRequest._fields = [
  FieldMetadata("verificationInfo", "verification_info", "_verification_info", DatabundleVerificationInfo, None, KaggleObjectSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, None, PredefinedSerializer(), optional=True),
]

GetDatabundleExternalColumnsResponse._fields = [
  FieldMetadata("columns", "columns", "_columns", ColumnBaseInfo, [], ListSerializer(KaggleObjectSerializer())),
]

GetDatabundleExternalRequest._fields = [
  FieldMetadata("verificationInfo", "verification_info", "_verification_info", DatabundleVerificationInfo, None, KaggleObjectSerializer()),
]

GetDatabundleExternalResponse._fields = [
  FieldMetadata("dataSource", "data_source", "_data_source", DataSource, None, KaggleObjectSerializer()),
]

KickoffDatabundleHasherRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

KickoffFirestoreDeleteMigrationRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
  FieldMetadata("deleteFirestoreFiles", "delete_firestore_files", "_delete_firestore_files", bool, False, PredefinedSerializer()),
  FieldMetadata("databundleType", "databundle_type", "_databundle_type", DatabundleType, DatabundleType.DATABUNDLE_TYPE_UNSPECIFIED, EnumSerializer()),
]

KickoffFirestoreWriteMigrationRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

KickoffHandlerResponse._fields = [
  FieldMetadata("lastDatabundleVersionId", "last_databundle_version_id", "_last_databundle_version_id", int, 0, PredefinedSerializer()),
]

RestoreDatabundleVersionRequest._fields = [
  FieldMetadata("databundleVersionId", "databundle_version_id", "_databundle_version_id", int, 0, PredefinedSerializer()),
]

RestoreDatabundleVersionResponse._fields = [
  FieldMetadata("countRestoredFiles", "count_restored_files", "_count_restored_files", int, 0, PredefinedSerializer()),
]

UpdateDatabundleMetadataExternalRequest._fields = [
  FieldMetadata("verificationInfo", "verification_info", "_verification_info", DatabundleVerificationInfo, None, KaggleObjectSerializer()),
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("columns", "columns", "_columns", ColumnUpdateInfo, [], ListSerializer(KaggleObjectSerializer())),
]

UpdateDatabundleMetadataExternalResponse._fields = [
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", DatasetUsabilityRating, None, KaggleObjectSerializer()),
]

