from kagglesdk.kaggle_object import *

class BlobFile(KaggleObject):
  r"""
  BlobFile sdk object for BlobService requests/responses.

  Attributes:
    id (int)
    file_name (str)
    content_length (int)
    content_type (str)
    blob_url (str)
  """

  def __init__(self):
    self._id = 0
    self._file_name = ""
    self._content_length = 0
    self._content_type = ""
    self._blob_url = ""
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
  def blob_url(self) -> str:
    return self._blob_url

  @blob_url.setter
  def blob_url(self, blob_url: str):
    if blob_url is None:
      del self.blob_url
      return
    if not isinstance(blob_url, str):
      raise TypeError('blob_url must be of type str')
    self._blob_url = blob_url


BlobFile._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("contentLength", "content_length", "_content_length", int, 0, PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, "", PredefinedSerializer()),
  FieldMetadata("blobUrl", "blob_url", "_blob_url", str, "", PredefinedSerializer()),
]

