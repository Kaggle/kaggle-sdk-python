from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class ContactSupportReason(enum.Enum):
  CONTACT_SUPPORT_REASON_UNSPECIFIED = 0
  PHONE_VERIFICATION = 1
  """For phone verification issues."""
  IDENTITY_VERIFICATION = 2
  """For identity verification issues."""
  CAPTCHA = 3
  """For captcha issues."""
  ACCOUNT_TAKEOVER = 4
  """For account takeovers."""
  USERNAME_CHANGE = 5
  """For username changes."""
  LOGIN_METHOD_CHANGE = 6
  """For changing login method."""
  ENFORCEMENT_APPEAL = 7
  """For appeals to enforcement actions."""
  NO_ACTION_APPEAL = 8
  """For appeals to no action."""
  ACCOUNT_WITHDRAWAL = 9
  """For account withdrawal."""
  COMPETITION_RESCORE_REQUEST = 10
  """For competition rescore requests."""
  NEW_ORGANIZATION_REQUEST = 11
  """For new organization requests."""
  ORGANIZATION_DELETION_REQUEST = 12
  """For organization deletion requests."""
  PRIVACY_RELATED_REQUEST = 13
  """For privacy related requests."""
  BUG_REPORT = 14
  """For bug reports."""
  MEDIA_INQUIRY = 15
  """For media inquiries."""
  COMPETITION_TECHNICAL_ISSUE = 16
  """For competitions technical issues."""
  NOTEBOOK_TECHNICAL_ISSUE = 17
  """For notebook technical issues."""
  COMMUNITY_TECHNICAL_ISSUE = 18
  """For community technical issues."""

class ContactSupportType(enum.Enum):
  CONTACT_SUPPORT_TYPE_UNSPECIFIED = 0
  SUPPORT = 1
  """General support."""
  MODERATION = 2
  """For enforcement actions, community guidelines, and appeals."""
  MODEL_PUBLICATIONS = 3
  """For creation of organizations or model publishing."""
  ORGANIZATION_DELETION = 4
  """For deletion of organizations."""
  ORGANIZATION_CREATION = 5
  """For creation of organizations."""

class SupportRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
      Id of the support request.
    user_id (int)
      Id of the user that created the support request.
    logged_out (bool)
      Whether the user was logged out when the support request was created.
    type (ContactSupportType)
      Type of support request.
    reason (ContactSupportReason)
      Reason for the support request.
    question (str)
      Question asked by the user.
    fields (SupportRequestFields)
      Additional fields provided by the user.
    fields_json (str)
      Additional fields provided by the user, in JSON format.
    create_time (datetime)
      Time the support request was created.
  """

  def __init__(self):
    self._id = 0
    self._user_id = 0
    self._logged_out = False
    self._type = ContactSupportType.CONTACT_SUPPORT_TYPE_UNSPECIFIED
    self._reason = ContactSupportReason.CONTACT_SUPPORT_REASON_UNSPECIFIED
    self._question = None
    self._fields = None
    self._fields_json = ""
    self._create_time = None
    self._freeze()

  @property
  def id(self) -> int:
    """Id of the support request."""
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
  def user_id(self) -> int:
    """Id of the user that created the support request."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def logged_out(self) -> bool:
    """Whether the user was logged out when the support request was created."""
    return self._logged_out

  @logged_out.setter
  def logged_out(self, logged_out: bool):
    if logged_out is None:
      del self.logged_out
      return
    if not isinstance(logged_out, bool):
      raise TypeError('logged_out must be of type bool')
    self._logged_out = logged_out

  @property
  def type(self) -> 'ContactSupportType':
    """Type of support request."""
    return self._type

  @type.setter
  def type(self, type: 'ContactSupportType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ContactSupportType):
      raise TypeError('type must be of type ContactSupportType')
    self._type = type

  @property
  def reason(self) -> 'ContactSupportReason':
    """Reason for the support request."""
    return self._reason

  @reason.setter
  def reason(self, reason: 'ContactSupportReason'):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, ContactSupportReason):
      raise TypeError('reason must be of type ContactSupportReason')
    self._reason = reason

  @property
  def question(self) -> str:
    """Question asked by the user."""
    return self._question or ""

  @question.setter
  def question(self, question: Optional[str]):
    if question is None:
      del self.question
      return
    if not isinstance(question, str):
      raise TypeError('question must be of type str')
    self._question = question

  @property
  def fields(self) -> Optional['SupportRequestFields']:
    """Additional fields provided by the user."""
    return self._fields

  @fields.setter
  def fields(self, fields: Optional['SupportRequestFields']):
    if fields is None:
      del self.fields
      return
    if not isinstance(fields, SupportRequestFields):
      raise TypeError('fields must be of type SupportRequestFields')
    self._fields = fields

  @property
  def fields_json(self) -> str:
    """Additional fields provided by the user, in JSON format."""
    return self._fields_json

  @fields_json.setter
  def fields_json(self, fields_json: str):
    if fields_json is None:
      del self.fields_json
      return
    if not isinstance(fields_json, str):
      raise TypeError('fields_json must be of type str')
    self._fields_json = fields_json

  @property
  def create_time(self) -> datetime:
    """Time the support request was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time


class SupportRequestFields(KaggleObject):
  r"""
  Attributes:
    name (str)
    email (str)
    phone_number (str)
    region (str)
    justification (str)
    issue (str)
    repro_steps (str)
    error_messages (str)
    console_error_messages (str)
  """

  def __init__(self):
    self._name = None
    self._email = None
    self._phone_number = None
    self._region = None
    self._justification = None
    self._issue = None
    self._repro_steps = None
    self._error_messages = None
    self._console_error_messages = None
    self._freeze()

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

  @property
  def email(self) -> str:
    return self._email or ""

  @email.setter
  def email(self, email: Optional[str]):
    if email is None:
      del self.email
      return
    if not isinstance(email, str):
      raise TypeError('email must be of type str')
    self._email = email

  @property
  def phone_number(self) -> str:
    return self._phone_number or ""

  @phone_number.setter
  def phone_number(self, phone_number: Optional[str]):
    if phone_number is None:
      del self.phone_number
      return
    if not isinstance(phone_number, str):
      raise TypeError('phone_number must be of type str')
    self._phone_number = phone_number

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
  def justification(self) -> str:
    return self._justification or ""

  @justification.setter
  def justification(self, justification: Optional[str]):
    if justification is None:
      del self.justification
      return
    if not isinstance(justification, str):
      raise TypeError('justification must be of type str')
    self._justification = justification

  @property
  def issue(self) -> str:
    return self._issue or ""

  @issue.setter
  def issue(self, issue: Optional[str]):
    if issue is None:
      del self.issue
      return
    if not isinstance(issue, str):
      raise TypeError('issue must be of type str')
    self._issue = issue

  @property
  def repro_steps(self) -> str:
    return self._repro_steps or ""

  @repro_steps.setter
  def repro_steps(self, repro_steps: Optional[str]):
    if repro_steps is None:
      del self.repro_steps
      return
    if not isinstance(repro_steps, str):
      raise TypeError('repro_steps must be of type str')
    self._repro_steps = repro_steps

  @property
  def error_messages(self) -> str:
    return self._error_messages or ""

  @error_messages.setter
  def error_messages(self, error_messages: Optional[str]):
    if error_messages is None:
      del self.error_messages
      return
    if not isinstance(error_messages, str):
      raise TypeError('error_messages must be of type str')
    self._error_messages = error_messages

  @property
  def console_error_messages(self) -> str:
    return self._console_error_messages or ""

  @console_error_messages.setter
  def console_error_messages(self, console_error_messages: Optional[str]):
    if console_error_messages is None:
      del self.console_error_messages
      return
    if not isinstance(console_error_messages, str):
      raise TypeError('console_error_messages must be of type str')
    self._console_error_messages = console_error_messages


SupportRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("loggedOut", "logged_out", "_logged_out", bool, False, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", ContactSupportType, ContactSupportType.CONTACT_SUPPORT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("reason", "reason", "_reason", ContactSupportReason, ContactSupportReason.CONTACT_SUPPORT_REASON_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("question", "question", "_question", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("fields", "fields", "_fields", SupportRequestFields, None, KaggleObjectSerializer()),
  FieldMetadata("fieldsJson", "fields_json", "_fields_json", str, "", PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
]

SupportRequestFields._fields = [
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("region", "region", "_region", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("justification", "justification", "_justification", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("issue", "issue", "_issue", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reproSteps", "repro_steps", "_repro_steps", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("errorMessages", "error_messages", "_error_messages", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("consoleErrorMessages", "console_error_messages", "_console_error_messages", str, None, PredefinedSerializer(), optional=True),
]

