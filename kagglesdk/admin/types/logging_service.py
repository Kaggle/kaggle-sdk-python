import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class CreateLogMessageRequest(KaggleObject):
  r"""
  Attributes:
    source (str)
      The logger/source from where the log message will be generated from.
    level (CreateLogMessageRequest.LogLevel)
      The severity level of the message to report.
    message (str)
      The message text to log.
  """

  class LogLevel(enum.Enum):
    r"""
    These intentionally match Microsoft.Extensions.Logging.LogLevel
    and must match exactly or it won't parse correctly.
    """
    NONE = 0
    CRITICAL = 1
    ERROR = 2
    WARNING = 3
    INFORMATION = 4
    DEBUG = 5
    TRACE = 6

  def __init__(self):
    self._source = ""
    self._level = self.LogLevel.NONE
    self._message = ""
    self._freeze()

  @property
  def source(self) -> str:
    """The logger/source from where the log message will be generated from."""
    return self._source

  @source.setter
  def source(self, source: str):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source

  @property
  def level(self) -> 'CreateLogMessageRequest.LogLevel':
    """The severity level of the message to report."""
    return self._level

  @level.setter
  def level(self, level: 'CreateLogMessageRequest.LogLevel'):
    if level is None:
      del self.level
      return
    if not isinstance(level, CreateLogMessageRequest.LogLevel):
      raise TypeError('level must be of type CreateLogMessageRequest.LogLevel')
    self._level = level

  @property
  def message(self) -> str:
    """The message text to log."""
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


class CreateLogMessageResponse(KaggleObject):
  r"""
  """

  pass

CreateLogMessageRequest._fields = [
  FieldMetadata("source", "source", "_source", str, "", PredefinedSerializer()),
  FieldMetadata("level", "level", "_level", CreateLogMessageRequest.LogLevel, CreateLogMessageRequest.LogLevel.NONE, EnumSerializer()),
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

CreateLogMessageResponse._fields = []

