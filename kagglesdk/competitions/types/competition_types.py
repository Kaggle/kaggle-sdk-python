from kagglesdk.competitions.types.competition_enums import CompetitionPrivacy
from kagglesdk.kaggle_object import *
from typing import List, Optional

class DatabundleBasicInfo(KaggleObject):
  r"""
  Attributes:
    files (DatabundleFile)
      Only includes top-level files.
    has_directories (bool)
      Whether any directories are present in the databundle
    total_size (int)
      Size of the whole databundle (files and directories) in bytes
  """

  def __init__(self):
    self._files = []
    self._has_directories = False
    self._total_size = 0
    self._freeze()

  @property
  def files(self) -> Optional[List[Optional['DatabundleFile']]]:
    """Only includes top-level files."""
    return self._files

  @files.setter
  def files(self, files: Optional[List[Optional['DatabundleFile']]]):
    if files is None:
      del self.files
      return
    if not isinstance(files, list):
      raise TypeError('files must be of type list')
    if not all([isinstance(t, DatabundleFile) for t in files]):
      raise TypeError('files must contain only items of type DatabundleFile')
    self._files = files

  @property
  def has_directories(self) -> bool:
    """Whether any directories are present in the databundle"""
    return self._has_directories

  @has_directories.setter
  def has_directories(self, has_directories: bool):
    if has_directories is None:
      del self.has_directories
      return
    if not isinstance(has_directories, bool):
      raise TypeError('has_directories must be of type bool')
    self._has_directories = has_directories

  @property
  def total_size(self) -> int:
    """Size of the whole databundle (files and directories) in bytes"""
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size


class DatabundleFile(KaggleObject):
  r"""
  Attributes:
    file_name (str)
    content_length (int)
    rows (int)
    columns (int)
  """

  def __init__(self):
    self._file_name = ""
    self._content_length = 0
    self._rows = 0
    self._columns = 0
    self._freeze()

  @property
  def file_name(self) -> str:
    return self._file_name

  @file_name.setter
  def file_name(self, file_name: str):
    if file_name is None:
      del self.file_name
      return
    if not isinstance(file_name, str):
      raise TypeError('file_name must be of type str')
    self._file_name = file_name

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
  def rows(self) -> int:
    return self._rows

  @rows.setter
  def rows(self, rows: int):
    if rows is None:
      del self.rows
      return
    if not isinstance(rows, int):
      raise TypeError('rows must be of type int')
    self._rows = rows

  @property
  def columns(self) -> int:
    return self._columns

  @columns.setter
  def columns(self, columns: int):
    if columns is None:
      del self.columns
      return
    if not isinstance(columns, int):
      raise TypeError('columns must be of type int')
    self._columns = columns


class PrivacySettings(KaggleObject):
  r"""
  Attributes:
    privacy (CompetitionPrivacy)
    share_token (str)
    restrict_to_email_list (bool)
  """

  def __init__(self):
    self._privacy = CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED
    self._share_token = ""
    self._restrict_to_email_list = False
    self._freeze()

  @property
  def privacy(self) -> 'CompetitionPrivacy':
    return self._privacy

  @privacy.setter
  def privacy(self, privacy: 'CompetitionPrivacy'):
    if privacy is None:
      del self.privacy
      return
    if not isinstance(privacy, CompetitionPrivacy):
      raise TypeError('privacy must be of type CompetitionPrivacy')
    self._privacy = privacy

  @property
  def share_token(self) -> str:
    return self._share_token

  @share_token.setter
  def share_token(self, share_token: str):
    if share_token is None:
      del self.share_token
      return
    if not isinstance(share_token, str):
      raise TypeError('share_token must be of type str')
    self._share_token = share_token

  @property
  def restrict_to_email_list(self) -> bool:
    return self._restrict_to_email_list

  @restrict_to_email_list.setter
  def restrict_to_email_list(self, restrict_to_email_list: bool):
    if restrict_to_email_list is None:
      del self.restrict_to_email_list
      return
    if not isinstance(restrict_to_email_list, bool):
      raise TypeError('restrict_to_email_list must be of type bool')
    self._restrict_to_email_list = restrict_to_email_list


DatabundleBasicInfo._fields = [
  FieldMetadata("files", "files", "_files", DatabundleFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("hasDirectories", "has_directories", "_has_directories", bool, False, PredefinedSerializer()),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

DatabundleFile._fields = [
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("rows", "rows", "_rows", int, 0, PredefinedSerializer()),
  FieldMetadata("columns", "columns", "_columns", int, 0, PredefinedSerializer()),
]

PrivacySettings._fields = [
  FieldMetadata("privacy", "privacy", "_privacy", CompetitionPrivacy, CompetitionPrivacy.COMPETITION_PRIVACY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("shareToken", "share_token", "_share_token", str, "", PredefinedSerializer()),
  FieldMetadata("restrictToEmailList", "restrict_to_email_list", "_restrict_to_email_list", bool, False, PredefinedSerializer()),
]

