from kagglesdk.kaggle_object import *

class HttpContent(KaggleObject):
  r"""
  Represents an HTTP content response (e.g. text/plain).
  Patterned after ASP.NET MVC's ContentResult.

  Attributes:
    content (str)
    content_type (str)
    status_code (int)
  """

  def __init__(self):
    self._content = ""
    self._content_type = ""
    self._status_code = 0
    self._freeze()

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

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
  def status_code(self) -> int:
    return self._status_code

  @status_code.setter
  def status_code(self, status_code: int):
    if status_code is None:
      del self.status_code
      return
    if not isinstance(status_code, int):
      raise TypeError('status_code must be of type int')
    self._status_code = status_code


HttpContent._fields = [
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("contentType", "content_type", "_content_type", str, "", PredefinedSerializer()),
  FieldMetadata("statusCode", "status_code", "_status_code", int, 0, PredefinedSerializer()),
]

