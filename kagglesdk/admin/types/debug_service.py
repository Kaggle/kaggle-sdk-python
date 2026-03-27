from kagglesdk.kaggle_object import *
from typing import Optional

class AskGeminiRequest(KaggleObject):
  r"""
  Attributes:
    prompt (str)
  """

  def __init__(self):
    self._prompt = ""
    self._freeze()

  @property
  def prompt(self) -> str:
    return self._prompt

  @prompt.setter
  def prompt(self, prompt: str):
    if prompt is None:
      del self.prompt
      return
    if not isinstance(prompt, str):
      raise TypeError('prompt must be of type str')
    self._prompt = prompt


class GeminiResponse(KaggleObject):
  r"""
  Attributes:
    response (str)
    error (str)
      Easy way to get fuller error than what /admin/api provides
  """

  def __init__(self):
    self._response = None
    self._error = None
    self._freeze()

  @property
  def response(self) -> str:
    return self._response or ""

  @response.setter
  def response(self, response: str):
    if response is None:
      del self.response
      return
    if not isinstance(response, str):
      raise TypeError('response must be of type str')
    del self.error
    self._response = response

  @property
  def error(self) -> str:
    """Easy way to get fuller error than what /admin/api provides"""
    return self._error or ""

  @error.setter
  def error(self, error: str):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    del self.response
    self._error = error


class SendEmailRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
    subject (str)
    body (str)
    from_ (str)
    reply_to (str)
  """

  def __init__(self):
    self._email = ""
    self._subject = ""
    self._body = ""
    self._from_ = ""
    self._reply_to = ""
    self._freeze()

  @property
  def email(self) -> str:
    return self._email

  @email.setter
  def email(self, email: str):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email

  @property
  def subject(self) -> str:
    return self._subject

  @subject.setter
  def subject(self, subject: str):
    if subject is None:
      del self.subject
      return
    if not isinstance(subject, str):
      raise TypeError('subject must be of type str')
    self._subject = subject

  @property
  def body(self) -> str:
    return self._body

  @body.setter
  def body(self, body: str):
    if body is None:
      del self.body
      return
    if not isinstance(body, str):
      raise TypeError('body must be of type str')
    self._body = body

  @property
  def from_(self) -> str:
    return self._from_

  @from_.setter
  def from_(self, from_: str):
    if from_ is None:
      del self.from_
      return
    if not isinstance(from_, str):
      raise TypeError('from_ must be of type str')
    self._from_ = from_

  @property
  def reply_to(self) -> str:
    return self._reply_to

  @reply_to.setter
  def reply_to(self, reply_to: str):
    if reply_to is None:
      del self.reply_to
      return
    if not isinstance(reply_to, str):
      raise TypeError('reply_to must be of type str')
    self._reply_to = reply_to


class SendEmailResponse(KaggleObject):
  r"""
  Attributes:
    message (str)
  """

  def __init__(self):
    self._message = ""
    self._freeze()

  @property
  def message(self) -> str:
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message


class ThrowCanonicalExceptionRequest(KaggleObject):
  r"""
  Attributes:
    code (int)
  """

  def __init__(self):
    self._code = 0
    self._freeze()

  @property
  def code(self) -> int:
    return self._code

  @code.setter
  def code(self, code: int):
    if code is None:
      del self.code
      return
    if not isinstance(code, int):
      raise TypeError('code must be of type int')
    self._code = code


AskGeminiRequest._fields = [
  FieldMetadata("prompt", "prompt", "_prompt", str, "", PredefinedSerializer()),
]

GeminiResponse._fields = [
  FieldMetadata("response", "response", "_response", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

SendEmailRequest._fields = [
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("subject", "subject", "_subject", str, "", PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", str, "", PredefinedSerializer()),
  FieldMetadata("from", "from_", "_from_", str, "", PredefinedSerializer()),
  FieldMetadata("replyTo", "reply_to", "_reply_to", str, "", PredefinedSerializer()),
]

SendEmailResponse._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
]

ThrowCanonicalExceptionRequest._fields = [
  FieldMetadata("code", "code", "_code", int, 0, PredefinedSerializer()),
]

