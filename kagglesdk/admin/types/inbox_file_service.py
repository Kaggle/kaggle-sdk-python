from datetime import datetime
from kagglesdk.kaggle_object import *
from typing import List, Optional

class CreateInboxFileRequest(KaggleObject):
  r"""
  Attributes:
    virtual_directory (str)
      Directory name used for tagging the uploaded file.
    blob_file_token (str)
      Token representing the uploaded file.
  """

  def __init__(self):
    self._virtual_directory = ""
    self._blob_file_token = ""
    self._freeze()

  @property
  def virtual_directory(self) -> str:
    """Directory name used for tagging the uploaded file."""
    return self._virtual_directory

  @virtual_directory.setter
  def virtual_directory(self, virtual_directory: str):
    if virtual_directory is None:
      del self.virtual_directory
      return
    if not isinstance(virtual_directory, str):
      raise TypeError('virtual_directory must be of type str')
    self._virtual_directory = virtual_directory

  @property
  def blob_file_token(self) -> str:
    """Token representing the uploaded file."""
    return self._blob_file_token

  @blob_file_token.setter
  def blob_file_token(self, blob_file_token: str):
    if blob_file_token is None:
      del self.blob_file_token
      return
    if not isinstance(blob_file_token, str):
      raise TypeError('blob_file_token must be of type str')
    self._blob_file_token = blob_file_token


class CreateInboxFileResponse(KaggleObject):
  r"""
  NOTE: This is sent to non-admins, so we're intentionally *NOT* sending back
  the full InboxFile (with its URL for a direct download).

  """

  pass

class DeleteInboxFileRequest(KaggleObject):
  r"""
  Attributes:
    inbox_file_id (int)
      Id of the file to delete.
  """

  def __init__(self):
    self._inbox_file_id = 0
    self._freeze()

  @property
  def inbox_file_id(self) -> int:
    """Id of the file to delete."""
    return self._inbox_file_id

  @inbox_file_id.setter
  def inbox_file_id(self, inbox_file_id: int):
    if inbox_file_id is None:
      del self.inbox_file_id
      return
    if not isinstance(inbox_file_id, int):
      raise TypeError('inbox_file_id must be of type int')
    self._inbox_file_id = inbox_file_id


class InboxFile(KaggleObject):
  r"""
  Attributes:
    id (int)
      Unique id for the uploaded file.
    virtual_directory (str)
      The optional virtual directory that contains this file.
    file_name (str)
      The user-visible filename.
    content_length (int)
      The size (in bytes) of the file.
    upload_time (datetime)
      Timestamp of when the file was uploaded.
    download_url (str)
      The download URL.
    gcs_url (str)
      URL of the file in GCS (useful for gsutil usage).
    uploader_info (InboxFileUserInfo)
      Ideally we would just need the user's ID and would be able to fetch info
      for the avatar info, but that currently is ready in the frontend, so we
      instead send the info that the frontend needs: int32 uploader_user_id = 8;
  """

  def __init__(self):
    self._id = 0
    self._virtual_directory = ""
    self._file_name = ""
    self._content_length = 0
    self._upload_time = None
    self._download_url = ""
    self._gcs_url = ""
    self._uploader_info = None
    self._freeze()

  @property
  def id(self) -> int:
    """Unique id for the uploaded file."""
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
  def virtual_directory(self) -> str:
    """The optional virtual directory that contains this file."""
    return self._virtual_directory

  @virtual_directory.setter
  def virtual_directory(self, virtual_directory: str):
    if virtual_directory is None:
      del self.virtual_directory
      return
    if not isinstance(virtual_directory, str):
      raise TypeError('virtual_directory must be of type str')
    self._virtual_directory = virtual_directory

  @property
  def file_name(self) -> str:
    """The user-visible filename."""
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
    """The size (in bytes) of the file."""
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
  def upload_time(self) -> datetime:
    """Timestamp of when the file was uploaded."""
    return self._upload_time

  @upload_time.setter
  def upload_time(self, upload_time: datetime):
    if upload_time is None:
      del self.upload_time
      return
    if not isinstance(upload_time, datetime):
      raise TypeError('upload_time must be of type datetime')
    self._upload_time = upload_time

  @property
  def download_url(self) -> str:
    """The download URL."""
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
  def gcs_url(self) -> str:
    """URL of the file in GCS (useful for gsutil usage)."""
    return self._gcs_url

  @gcs_url.setter
  def gcs_url(self, gcs_url: str):
    if gcs_url is None:
      del self.gcs_url
      return
    if not isinstance(gcs_url, str):
      raise TypeError('gcs_url must be of type str')
    self._gcs_url = gcs_url

  @property
  def uploader_info(self) -> Optional['InboxFileUserInfo']:
    r"""
    Ideally we would just need the user's ID and would be able to fetch info
    for the avatar info, but that currently is ready in the frontend, so we
    instead send the info that the frontend needs: int32 uploader_user_id = 8;
    """
    return self._uploader_info

  @uploader_info.setter
  def uploader_info(self, uploader_info: Optional['InboxFileUserInfo']):
    if uploader_info is None:
      del self.uploader_info
      return
    if not isinstance(uploader_info, InboxFileUserInfo):
      raise TypeError('uploader_info must be of type InboxFileUserInfo')
    self._uploader_info = uploader_info


class InboxFileUserInfo(KaggleObject):
  r"""
  The existing frontend depended on this information. Future updates should
  just use the user id and fetch whatever is needed.

  Attributes:
    id (int)
    display_name (str)
    user_url (str)
    tier (int)
      Performance tier should likely be an enum, but making an integer for
      backwards compatibility
    thumbnail_url (str)
    progression_opt_out (bool)
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._user_url = ""
    self._tier = 0
    self._thumbnail_url = ""
    self._progression_opt_out = False
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
  def display_name(self) -> str:
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def user_url(self) -> str:
    return self._user_url

  @user_url.setter
  def user_url(self, user_url: str):
    if user_url is None:
      del self.user_url
      return
    if not isinstance(user_url, str):
      raise TypeError('user_url must be of type str')
    self._user_url = user_url

  @property
  def tier(self) -> int:
    r"""
    Performance tier should likely be an enum, but making an integer for
    backwards compatibility
    """
    return self._tier

  @tier.setter
  def tier(self, tier: int):
    if tier is None:
      del self.tier
      return
    if not isinstance(tier, int):
      raise TypeError('tier must be of type int')
    self._tier = tier

  @property
  def progression_opt_out(self) -> bool:
    return self._progression_opt_out

  @progression_opt_out.setter
  def progression_opt_out(self, progression_opt_out: bool):
    if progression_opt_out is None:
      del self.progression_opt_out
      return
    if not isinstance(progression_opt_out, bool):
      raise TypeError('progression_opt_out must be of type bool')
    self._progression_opt_out = progression_opt_out

  @property
  def thumbnail_url(self) -> str:
    return self._thumbnail_url

  @thumbnail_url.setter
  def thumbnail_url(self, thumbnail_url: str):
    if thumbnail_url is None:
      del self.thumbnail_url
      return
    if not isinstance(thumbnail_url, str):
      raise TypeError('thumbnail_url must be of type str')
    self._thumbnail_url = thumbnail_url


class ListInboxFilesRequest(KaggleObject):
  r"""
  Attributes:
    virtual_directory (str)
      Optional virtual directory/tag to limit scope of listing.
    page_size (int)
      The maximum number of bans to return.
    page_token (str)
      The `next_page_token` value returned from a previous request, if any.
  """

  def __init__(self):
    self._virtual_directory = ""
    self._page_size = 0
    self._page_token = ""
    self._freeze()

  @property
  def virtual_directory(self) -> str:
    """Optional virtual directory/tag to limit scope of listing."""
    return self._virtual_directory

  @virtual_directory.setter
  def virtual_directory(self, virtual_directory: str):
    if virtual_directory is None:
      del self.virtual_directory
      return
    if not isinstance(virtual_directory, str):
      raise TypeError('virtual_directory must be of type str')
    self._virtual_directory = virtual_directory

  @property
  def page_size(self) -> int:
    """The maximum number of bans to return."""
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
    """The `next_page_token` value returned from a previous request, if any."""
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListInboxFilesResponse(KaggleObject):
  r"""
  Attributes:
    virtual_directory (str)
      The virtual directory that the files belong to.
    inbox_files (InboxFile)
      The listing of files available for download.
    next_page_token (str)
      Token to retrieve the next page of results, or empty if there are no more
      results in the list.
  """

  def __init__(self):
    self._virtual_directory = ""
    self._inbox_files = []
    self._next_page_token = ""
    self._freeze()

  @property
  def virtual_directory(self) -> str:
    """The virtual directory that the files belong to."""
    return self._virtual_directory

  @virtual_directory.setter
  def virtual_directory(self, virtual_directory: str):
    if virtual_directory is None:
      del self.virtual_directory
      return
    if not isinstance(virtual_directory, str):
      raise TypeError('virtual_directory must be of type str')
    self._virtual_directory = virtual_directory

  @property
  def inbox_files(self) -> Optional[List[Optional['InboxFile']]]:
    """The listing of files available for download."""
    return self._inbox_files

  @inbox_files.setter
  def inbox_files(self, inbox_files: Optional[List[Optional['InboxFile']]]):
    if inbox_files is None:
      del self.inbox_files
      return
    if not isinstance(inbox_files, list):
      raise TypeError('inbox_files must be of type list')
    if not all([isinstance(t, InboxFile) for t in inbox_files]):
      raise TypeError('inbox_files must contain only items of type InboxFile')
    self._inbox_files = inbox_files

  @property
  def next_page_token(self) -> str:
    r"""
    Token to retrieve the next page of results, or empty if there are no more
    results in the list.
    """
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


CreateInboxFileRequest._fields = [
  FieldMetadata("virtualDirectory", "virtual_directory", "_virtual_directory", str, "", PredefinedSerializer()),
  FieldMetadata("blobFileToken", "blob_file_token", "_blob_file_token", str, "", PredefinedSerializer()),
]

CreateInboxFileResponse._fields = []

DeleteInboxFileRequest._fields = [
  FieldMetadata("inboxFileId", "inbox_file_id", "_inbox_file_id", int, 0, PredefinedSerializer()),
]

InboxFile._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("virtualDirectory", "virtual_directory", "_virtual_directory", str, "", PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("uploadTime", "upload_time", "_upload_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("downloadUrl", "download_url", "_download_url", str, "", PredefinedSerializer()),
  FieldMetadata("gcsUrl", "gcs_url", "_gcs_url", str, "", PredefinedSerializer()),
  FieldMetadata("uploaderInfo", "uploader_info", "_uploader_info", InboxFileUserInfo, None, KaggleObjectSerializer()),
]

InboxFileUserInfo._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("userUrl", "user_url", "_user_url", str, "", PredefinedSerializer()),
  FieldMetadata("tier", "tier", "_tier", int, 0, PredefinedSerializer()),
  FieldMetadata("thumbnailUrl", "thumbnail_url", "_thumbnail_url", str, "", PredefinedSerializer()),
  FieldMetadata("progressionOptOut", "progression_opt_out", "_progression_opt_out", bool, False, PredefinedSerializer()),
]

ListInboxFilesRequest._fields = [
  FieldMetadata("virtualDirectory", "virtual_directory", "_virtual_directory", str, "", PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ListInboxFilesResponse._fields = [
  FieldMetadata("virtualDirectory", "virtual_directory", "_virtual_directory", str, "", PredefinedSerializer()),
  FieldMetadata("inboxFiles", "inbox_files", "_inbox_files", InboxFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

