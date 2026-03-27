import enum
from kagglesdk.datasets.types.dataset_enums import DatabundleVersionType, DatasetFileType, DatasetFileTypeGroup, DatasetLicenseGroup, DatasetSizeGroup
from kagglesdk.kaggle_object import *
from typing import List, Optional

class SearchDatasetsOrderBy(enum.Enum):
  SEARCH_DATASETS_ORDER_BY_UNSPECIFIED = 0
  SEARCH_DATASETS_ORDER_BY_USABILITY_RATING = 1

class SearchDatasetsDocument(KaggleObject):
  r"""
  Attributes:
    usability_rating (float)
      The usability rating of the Dataset
    file_count (int)
      How many files the Dataset has
    file_types (DatasetFileType)
      The file types of all the files in the Dataset
    size (int)
      The size of the Dataset
    databundle_version_type (DatabundleVersionType)
      The type of the Dataset (see DatabundleVersionType enum values)
  """

  def __init__(self):
    self._usability_rating = 0.0
    self._file_count = 0
    self._file_types = []
    self._size = 0
    self._databundle_version_type = DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def usability_rating(self) -> float:
    """The usability rating of the Dataset"""
    return self._usability_rating

  @usability_rating.setter
  def usability_rating(self, usability_rating: float):
    if usability_rating is None:
      del self.usability_rating
      return
    if not isinstance(usability_rating, float):
      raise TypeError('usability_rating must be of type float')
    self._usability_rating = usability_rating

  @property
  def file_count(self) -> int:
    """How many files the Dataset has"""
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
  def file_types(self) -> Optional[List['DatasetFileType']]:
    """The file types of all the files in the Dataset"""
    return self._file_types

  @file_types.setter
  def file_types(self, file_types: Optional[List['DatasetFileType']]):
    if file_types is None:
      del self.file_types
      return
    if not isinstance(file_types, list):
      raise TypeError('file_types must be of type list')
    if not all([isinstance(t, DatasetFileType) for t in file_types]):
      raise TypeError('file_types must contain only items of type DatasetFileType')
    self._file_types = file_types

  @property
  def size(self) -> int:
    """The size of the Dataset"""
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
  def databundle_version_type(self) -> 'DatabundleVersionType':
    """The type of the Dataset (see DatabundleVersionType enum values)"""
    return self._databundle_version_type

  @databundle_version_type.setter
  def databundle_version_type(self, databundle_version_type: 'DatabundleVersionType'):
    if databundle_version_type is None:
      del self.databundle_version_type
      return
    if not isinstance(databundle_version_type, DatabundleVersionType):
      raise TypeError('databundle_version_type must be of type DatabundleVersionType')
    self._databundle_version_type = databundle_version_type


class SearchDatasetsFilters(KaggleObject):
  r"""
  Attributes:
    file_type (DatasetFileTypeGroup)
      The file types used to filter the documents
    license_group (DatasetLicenseGroup)
      The license groups used to filter the documents
    size (DatasetSizeGroup)
      The dataset size range used to filter the documents
    earned_medal (bool)
      Whether to return documents that the owner_user_id earned a medal for.
  """

  def __init__(self):
    self._file_type = DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL
    self._license_group = None
    self._size = None
    self._earned_medal = None
    self._freeze()

  @property
  def file_type(self) -> 'DatasetFileTypeGroup':
    """The file types used to filter the documents"""
    return self._file_type

  @file_type.setter
  def file_type(self, file_type: 'DatasetFileTypeGroup'):
    if file_type is None:
      del self.file_type
      return
    if not isinstance(file_type, DatasetFileTypeGroup):
      raise TypeError('file_type must be of type DatasetFileTypeGroup')
    self._file_type = file_type

  @property
  def license_group(self) -> 'DatasetLicenseGroup':
    """The license groups used to filter the documents"""
    return self._license_group or DatasetLicenseGroup.DATASET_LICENSE_GROUP_ALL

  @license_group.setter
  def license_group(self, license_group: Optional['DatasetLicenseGroup']):
    if license_group is None:
      del self.license_group
      return
    if not isinstance(license_group, DatasetLicenseGroup):
      raise TypeError('license_group must be of type DatasetLicenseGroup')
    self._license_group = license_group

  @property
  def size(self) -> 'DatasetSizeGroup':
    """The dataset size range used to filter the documents"""
    return self._size or DatasetSizeGroup.DATASET_SIZE_GROUP_ALL

  @size.setter
  def size(self, size: Optional['DatasetSizeGroup']):
    if size is None:
      del self.size
      return
    if not isinstance(size, DatasetSizeGroup):
      raise TypeError('size must be of type DatasetSizeGroup')
    self._size = size

  @property
  def earned_medal(self) -> bool:
    """Whether to return documents that the owner_user_id earned a medal for."""
    return self._earned_medal or False

  @earned_medal.setter
  def earned_medal(self, earned_medal: Optional[bool]):
    if earned_medal is None:
      del self.earned_medal
      return
    if not isinstance(earned_medal, bool):
      raise TypeError('earned_medal must be of type bool')
    self._earned_medal = earned_medal


SearchDatasetsDocument._fields = [
  FieldMetadata("usabilityRating", "usability_rating", "_usability_rating", float, 0.0, PredefinedSerializer()),
  FieldMetadata("fileCount", "file_count", "_file_count", int, 0, PredefinedSerializer()),
  FieldMetadata("fileTypes", "file_types", "_file_types", DatasetFileType, [], ListSerializer(EnumSerializer())),
  FieldMetadata("size", "size", "_size", int, 0, PredefinedSerializer()),
  FieldMetadata("databundleVersionType", "databundle_version_type", "_databundle_version_type", DatabundleVersionType, DatabundleVersionType.DATABUNDLE_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
]

SearchDatasetsFilters._fields = [
  FieldMetadata("fileType", "file_type", "_file_type", DatasetFileTypeGroup, DatasetFileTypeGroup.DATASET_FILE_TYPE_GROUP_ALL, EnumSerializer()),
  FieldMetadata("licenseGroup", "license_group", "_license_group", DatasetLicenseGroup, None, EnumSerializer(), optional=True),
  FieldMetadata("size", "size", "_size", DatasetSizeGroup, None, EnumSerializer(), optional=True),
  FieldMetadata("earnedMedal", "earned_medal", "_earned_medal", bool, None, PredefinedSerializer(), optional=True),
]

