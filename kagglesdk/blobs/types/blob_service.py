from datetime import datetime
from kagglesdk.blobs.types.client_blob_bucket import ClientBlobBucket
from kagglesdk.kaggle_object import *
from typing import Optional

class StartBlobUploadRequest(KaggleObject):
  r"""
  Attributes:
    bucket (ClientBlobBucket)
      The destination bucket where to upload the blob.
      NOTE: Untrusted clients will be able to change this.
    name (str)
      Name (e.g. file name) of the blob.
    content_type (str)
      Content/MIME type (e.g. 'text/plain').
    content_length (int)
      Size in bytes of the blob.
    last_update_time (datetime)
      Optional user-reported time when the blob was last updated/modified.
  """

  def __init__(self):
    self._bucket = ClientBlobBucket.CLIENT_BLOB_BUCKET_UNSPECIFIED
    self._name = ""
    self._content_type = None
    self._content_length = 0
    self._last_update_time = None
    self._freeze()

  @property
  def bucket(self) -> 'ClientBlobBucket':
    r"""
    The destination bucket where to upload the blob.
    NOTE: Untrusted clients will be able to change this.
    """
    return self._bucket

  @bucket.setter
  def bucket(self, bucket: 'ClientBlobBucket'):
    if bucket is None:
      del self.bucket
      return
    if not isinstance(bucket, ClientBlobBucket):
      raise TypeError('bucket must be of type ClientBlobBucket')
    self._bucket = bucket

  @property
  def name(self) -> str:
    """Name (e.g. file name) of the blob."""
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
  def content_type(self) -> str:
    """Content/MIME type (e.g. 'text/plain')."""
    return self._content_type or ""

  @content_type.setter
  def content_type(self, content_type: Optional[str]):
    if content_type is None:
      del self.content_type
      return
    if not isinstance(content_type, str):
      raise TypeError('content_type must be of type str')
    self._content_type = content_type

  @property
  def content_length(self) -> int:
    """Size in bytes of the blob."""
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
  def last_update_time(self) -> datetime:
    """Optional user-reported time when the blob was last updated/modified."""
    return self._last_update_time

  @last_update_time.setter
  def last_update_time(self, last_update_time: datetime):
    if last_update_time is None:
      del self.last_update_time
      return
    if not isinstance(last_update_time, datetime):
      raise TypeError('last_update_time must be of type datetime')
    self._last_update_time = last_update_time


class StartBlobUploadResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
      Opaque string token used to reference the new blob/file.
    create_url (str)
      URL to use to start the upload.
  """

  def __init__(self):
    self._token = ""
    self._create_url = ""
    self._freeze()

  @property
  def token(self) -> str:
    """Opaque string token used to reference the new blob/file."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def create_url(self) -> str:
    """URL to use to start the upload."""
    return self._create_url

  @create_url.setter
  def create_url(self, create_url: str):
    if create_url is None:
      del self.create_url
      return
    if not isinstance(create_url, str):
      raise TypeError('create_url must be of type str')
    self._create_url = create_url


StartBlobUploadRequest._fields = [
  FieldMetadata("bucket", "bucket", "_bucket", ClientBlobBucket, ClientBlobBucket.CLIENT_BLOB_BUCKET_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("lastUpdateTime", "last_update_time", "_last_update_time", datetime, None, DateTimeSerializer()),
]

StartBlobUploadResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
  FieldMetadata("createUrl", "create_url", "_create_url", str, "", PredefinedSerializer()),
]

