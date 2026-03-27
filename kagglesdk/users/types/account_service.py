from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkIdentifier, TaskIdentifier
from kagglesdk.kaggle_object import *
from kagglesdk.security.types.security_types import ApiToken, ApiTokenStatus, ApiTokenType
from kagglesdk.users.types.moderation_public_service import AppealType, PolicyViolationId
from kagglesdk.users.types.support import ContactSupportReason, ContactSupportType, SupportRequest
from kagglesdk.users.types.users_enums import LoginMessageId, RegistrationInfoFields, UserVerificationStatus
from typing import List, Optional, Dict

class StartMigrateSsoOutcome(enum.Enum):
  GOOGLE_SSO_EXISTS = 0
  EMAIL_LOGIN_EXISTS = 1
  CREATE_PASSWORD = 2

class PhoneVerificationFailureReason(enum.Enum):
  PHONE_VERIFICATION_FAILURE_REASON_UNSPECIFIED = 0
  DUPLICATE_PHONE_NUMBER = 1

class TakeoutType(enum.Enum):
  TAKEOUT_TYPE_UNSPECIFIED = 0
  IDMEC_PRE_SOFT_DELETE = 1
  IDMEC_POST_SOFT_DELETE = 3
  USER_TAKEOUT = 2

class ValidateResetPasswordCodeOutcome(enum.Enum):
  VALIDATE_RESET_PASSWORD_CODE_OUTCOME_UNSPECIFIED = 0
  VALIDATE_RESET_PASSWORD_CODE_OUTCOME_INVALID_CODE = 1
  """Code was not valid."""
  VALIDATE_RESET_PASSWORD_CODE_OUTCOME_USER_BANNED = 2
  """Code was valid, but the user is banned."""
  VALIDATE_RESET_PASSWORD_CODE_OUTCOME_SUCCESS = 3
  """No problems."""
  VALIDATE_RESET_PASSWORD_CODE_OUTCOME_SUCCESS_USER_HAS_GOOGLE_LOGIN = 4
  """No problems, but the user also has a google login they could use."""

class BatchSoftDeleteAccountsRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      The list of users to delete. Will skip any already deleted users and
      continue processing if some encounter errors.
    reason (str)
      The reason to use for each deletion.
  """

  def __init__(self):
    self._user_ids = []
    self._reason = ""
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    r"""
    The list of users to delete. Will skip any already deleted users and
    continue processing if some encounter errors.
    """
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids

  @property
  def reason(self) -> str:
    """The reason to use for each deletion."""
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class BatchSoftDeleteAccountsResponse(KaggleObject):
  r"""
  Attributes:
    successfully_deleted_user_ids (int)
      The list of users that were successfully deleted.
    already_deleted_user_ids (int)
      The list of users that were skipped because they were already deleted.
    errored_user_ids (int)
      The list of users that encountered errors.
  """

  def __init__(self):
    self._successfully_deleted_user_ids = []
    self._already_deleted_user_ids = []
    self._errored_user_ids = []
    self._freeze()

  @property
  def successfully_deleted_user_ids(self) -> Optional[List[int]]:
    """The list of users that were successfully deleted."""
    return self._successfully_deleted_user_ids

  @successfully_deleted_user_ids.setter
  def successfully_deleted_user_ids(self, successfully_deleted_user_ids: Optional[List[int]]):
    if successfully_deleted_user_ids is None:
      del self.successfully_deleted_user_ids
      return
    if not isinstance(successfully_deleted_user_ids, list):
      raise TypeError('successfully_deleted_user_ids must be of type list')
    if not all([isinstance(t, int) for t in successfully_deleted_user_ids]):
      raise TypeError('successfully_deleted_user_ids must contain only items of type int')
    self._successfully_deleted_user_ids = successfully_deleted_user_ids

  @property
  def already_deleted_user_ids(self) -> Optional[List[int]]:
    """The list of users that were skipped because they were already deleted."""
    return self._already_deleted_user_ids

  @already_deleted_user_ids.setter
  def already_deleted_user_ids(self, already_deleted_user_ids: Optional[List[int]]):
    if already_deleted_user_ids is None:
      del self.already_deleted_user_ids
      return
    if not isinstance(already_deleted_user_ids, list):
      raise TypeError('already_deleted_user_ids must be of type list')
    if not all([isinstance(t, int) for t in already_deleted_user_ids]):
      raise TypeError('already_deleted_user_ids must contain only items of type int')
    self._already_deleted_user_ids = already_deleted_user_ids

  @property
  def errored_user_ids(self) -> Optional[List[int]]:
    """The list of users that encountered errors."""
    return self._errored_user_ids

  @errored_user_ids.setter
  def errored_user_ids(self, errored_user_ids: Optional[List[int]]):
    if errored_user_ids is None:
      del self.errored_user_ids
      return
    if not isinstance(errored_user_ids, list):
      raise TypeError('errored_user_ids must be of type list')
    if not all([isinstance(t, int) for t in errored_user_ids]):
      raise TypeError('errored_user_ids must contain only items of type int')
    self._errored_user_ids = errored_user_ids


class ContactPageDto(KaggleObject):
  r"""
  Attributes:
    forgot_password_link (str)
    competitions_link (str)
    datasets_link (str)
    new_dataset_link (str)
    datasets_forum_link (str)
    host_link (str)
    community_competitions_overview_link (str)
    migrate_deprecated_sso_link (str)
    compliance_link (str)
  """

  def __init__(self):
    self._forgot_password_link = ""
    self._competitions_link = ""
    self._datasets_link = ""
    self._new_dataset_link = ""
    self._datasets_forum_link = ""
    self._host_link = ""
    self._community_competitions_overview_link = ""
    self._migrate_deprecated_sso_link = ""
    self._compliance_link = ""
    self._freeze()

  @property
  def forgot_password_link(self) -> str:
    return self._forgot_password_link

  @forgot_password_link.setter
  def forgot_password_link(self, forgot_password_link: str):
    if forgot_password_link is None:
      del self.forgot_password_link
      return
    if not isinstance(forgot_password_link, str):
      raise TypeError('forgot_password_link must be of type str')
    self._forgot_password_link = forgot_password_link

  @property
  def competitions_link(self) -> str:
    return self._competitions_link

  @competitions_link.setter
  def competitions_link(self, competitions_link: str):
    if competitions_link is None:
      del self.competitions_link
      return
    if not isinstance(competitions_link, str):
      raise TypeError('competitions_link must be of type str')
    self._competitions_link = competitions_link

  @property
  def datasets_link(self) -> str:
    return self._datasets_link

  @datasets_link.setter
  def datasets_link(self, datasets_link: str):
    if datasets_link is None:
      del self.datasets_link
      return
    if not isinstance(datasets_link, str):
      raise TypeError('datasets_link must be of type str')
    self._datasets_link = datasets_link

  @property
  def new_dataset_link(self) -> str:
    return self._new_dataset_link

  @new_dataset_link.setter
  def new_dataset_link(self, new_dataset_link: str):
    if new_dataset_link is None:
      del self.new_dataset_link
      return
    if not isinstance(new_dataset_link, str):
      raise TypeError('new_dataset_link must be of type str')
    self._new_dataset_link = new_dataset_link

  @property
  def datasets_forum_link(self) -> str:
    return self._datasets_forum_link

  @datasets_forum_link.setter
  def datasets_forum_link(self, datasets_forum_link: str):
    if datasets_forum_link is None:
      del self.datasets_forum_link
      return
    if not isinstance(datasets_forum_link, str):
      raise TypeError('datasets_forum_link must be of type str')
    self._datasets_forum_link = datasets_forum_link

  @property
  def host_link(self) -> str:
    return self._host_link

  @host_link.setter
  def host_link(self, host_link: str):
    if host_link is None:
      del self.host_link
      return
    if not isinstance(host_link, str):
      raise TypeError('host_link must be of type str')
    self._host_link = host_link

  @property
  def community_competitions_overview_link(self) -> str:
    return self._community_competitions_overview_link

  @community_competitions_overview_link.setter
  def community_competitions_overview_link(self, community_competitions_overview_link: str):
    if community_competitions_overview_link is None:
      del self.community_competitions_overview_link
      return
    if not isinstance(community_competitions_overview_link, str):
      raise TypeError('community_competitions_overview_link must be of type str')
    self._community_competitions_overview_link = community_competitions_overview_link

  @property
  def migrate_deprecated_sso_link(self) -> str:
    return self._migrate_deprecated_sso_link

  @migrate_deprecated_sso_link.setter
  def migrate_deprecated_sso_link(self, migrate_deprecated_sso_link: str):
    if migrate_deprecated_sso_link is None:
      del self.migrate_deprecated_sso_link
      return
    if not isinstance(migrate_deprecated_sso_link, str):
      raise TypeError('migrate_deprecated_sso_link must be of type str')
    self._migrate_deprecated_sso_link = migrate_deprecated_sso_link

  @property
  def compliance_link(self) -> str:
    return self._compliance_link

  @compliance_link.setter
  def compliance_link(self, compliance_link: str):
    if compliance_link is None:
      del self.compliance_link
      return
    if not isinstance(compliance_link, str):
      raise TypeError('compliance_link must be of type str')
    self._compliance_link = compliance_link


class ContactSupportRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
    email (str)
    responses (str)
    question (str)
    require_captcha (bool)
    captcha_response (str)
    user_name (str)
      An optional user-supplied username (when logged out).
    type (ContactSupportType)
    reason (ContactSupportReason)
    appeal_type (AppealType)
      The type of appeal, if applicable
  """

  def __init__(self):
    self._name = ""
    self._email = ""
    self._responses = {}
    self._question = None
    self._require_captcha = False
    self._captcha_response = None
    self._user_name = None
    self._type = ContactSupportType.CONTACT_SUPPORT_TYPE_UNSPECIFIED
    self._reason = ContactSupportReason.CONTACT_SUPPORT_REASON_UNSPECIFIED
    self._appeal_type = None
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
  def user_name(self) -> str:
    """An optional user-supplied username (when logged out)."""
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: Optional[str]):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def responses(self) -> Optional[Dict[str, str]]:
    return self._responses

  @responses.setter
  def responses(self, responses: Optional[Dict[str, str]]):
    if responses is None:
      del self.responses
      return
    if not isinstance(responses, dict):
      raise TypeError('responses must be of type dict')
    if not all([isinstance(v, str) for k, v in responses]):
      raise TypeError('responses must contain only items of type str')
    self._responses = responses

  @property
  def question(self) -> str:
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
  def require_captcha(self) -> bool:
    return self._require_captcha

  @require_captcha.setter
  def require_captcha(self, require_captcha: bool):
    if require_captcha is None:
      del self.require_captcha
      return
    if not isinstance(require_captcha, bool):
      raise TypeError('require_captcha must be of type bool')
    self._require_captcha = require_captcha

  @property
  def captcha_response(self) -> str:
    return self._captcha_response or ""

  @captcha_response.setter
  def captcha_response(self, captcha_response: Optional[str]):
    if captcha_response is None:
      del self.captcha_response
      return
    if not isinstance(captcha_response, str):
      raise TypeError('captcha_response must be of type str')
    self._captcha_response = captcha_response

  @property
  def type(self) -> 'ContactSupportType':
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
  def appeal_type(self) -> 'AppealType':
    """The type of appeal, if applicable"""
    return self._appeal_type or AppealType.APPEAL_TYPE_UNSPECIFIED

  @appeal_type.setter
  def appeal_type(self, appeal_type: Optional['AppealType']):
    if appeal_type is None:
      del self.appeal_type
      return
    if not isinstance(appeal_type, AppealType):
      raise TypeError('appeal_type must be of type AppealType')
    self._appeal_type = appeal_type


class CurrentUserPenalty(KaggleObject):
  r"""
  Attributes:
    id (int)
      The ID of the penalty
    log_time (datetime)
      The date & time the penalty was issued
    policy_violation_descriptions (str)
      The user-visible list of violations for the penalty
    suspension_duration_days (int)
      The duration (in days) of the suspension
    suspension_lift_time (datetime)
      The date & time the suspension was/will be lifted
    other_violation (str)
      Any other violation notes provided to the user
    appeal_approval_time (datetime)
      The date & time the penalty appeal was approved
  """

  def __init__(self):
    self._id = 0
    self._log_time = None
    self._policy_violation_descriptions = []
    self._suspension_duration_days = None
    self._suspension_lift_time = None
    self._other_violation = None
    self._appeal_approval_time = None
    self._freeze()

  @property
  def id(self) -> int:
    """The ID of the penalty"""
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
  def log_time(self) -> datetime:
    """The date & time the penalty was issued"""
    return self._log_time

  @log_time.setter
  def log_time(self, log_time: datetime):
    if log_time is None:
      del self.log_time
      return
    if not isinstance(log_time, datetime):
      raise TypeError('log_time must be of type datetime')
    self._log_time = log_time

  @property
  def policy_violation_descriptions(self) -> Optional[List[str]]:
    """The user-visible list of violations for the penalty"""
    return self._policy_violation_descriptions

  @policy_violation_descriptions.setter
  def policy_violation_descriptions(self, policy_violation_descriptions: Optional[List[str]]):
    if policy_violation_descriptions is None:
      del self.policy_violation_descriptions
      return
    if not isinstance(policy_violation_descriptions, list):
      raise TypeError('policy_violation_descriptions must be of type list')
    if not all([isinstance(t, str) for t in policy_violation_descriptions]):
      raise TypeError('policy_violation_descriptions must contain only items of type str')
    self._policy_violation_descriptions = policy_violation_descriptions

  @property
  def suspension_duration_days(self) -> int:
    """The duration (in days) of the suspension"""
    return self._suspension_duration_days or 0

  @suspension_duration_days.setter
  def suspension_duration_days(self, suspension_duration_days: Optional[int]):
    if suspension_duration_days is None:
      del self.suspension_duration_days
      return
    if not isinstance(suspension_duration_days, int):
      raise TypeError('suspension_duration_days must be of type int')
    self._suspension_duration_days = suspension_duration_days

  @property
  def suspension_lift_time(self) -> datetime:
    """The date & time the suspension was/will be lifted"""
    return self._suspension_lift_time or None

  @suspension_lift_time.setter
  def suspension_lift_time(self, suspension_lift_time: Optional[datetime]):
    if suspension_lift_time is None:
      del self.suspension_lift_time
      return
    if not isinstance(suspension_lift_time, datetime):
      raise TypeError('suspension_lift_time must be of type datetime')
    self._suspension_lift_time = suspension_lift_time

  @property
  def other_violation(self) -> str:
    """Any other violation notes provided to the user"""
    return self._other_violation or ""

  @other_violation.setter
  def other_violation(self, other_violation: Optional[str]):
    if other_violation is None:
      del self.other_violation
      return
    if not isinstance(other_violation, str):
      raise TypeError('other_violation must be of type str')
    self._other_violation = other_violation

  @property
  def appeal_approval_time(self) -> datetime:
    """The date & time the penalty appeal was approved"""
    return self._appeal_approval_time or None

  @appeal_approval_time.setter
  def appeal_approval_time(self, appeal_approval_time: Optional[datetime]):
    if appeal_approval_time is None:
      del self.appeal_approval_time
      return
    if not isinstance(appeal_approval_time, datetime):
      raise TypeError('appeal_approval_time must be of type datetime')
    self._appeal_approval_time = appeal_approval_time


class DeleteCurrentAccountRequest(KaggleObject):
  r"""
  Attributes:
    reason (str)
      The user-provided reason for why they are deleting their account.
    captcha_response_token (str)
      The response from the captcha to validate.
  """

  def __init__(self):
    self._reason = ""
    self._captcha_response_token = ""
    self._freeze()

  @property
  def reason(self) -> str:
    """The user-provided reason for why they are deleting their account."""
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason

  @property
  def captcha_response_token(self) -> str:
    """The response from the captcha to validate."""
    return self._captcha_response_token

  @captcha_response_token.setter
  def captcha_response_token(self, captcha_response_token: str):
    if captcha_response_token is None:
      del self.captcha_response_token
      return
    if not isinstance(captcha_response_token, str):
      raise TypeError('captcha_response_token must be of type str')
    self._captcha_response_token = captcha_response_token


class ExpireApiTokenRequest(KaggleObject):
  r"""
  Attributes:
    token_id (int)
      Id of the token.
    token (str)
      Value of the token.
    reason (str)
      Reason why this token is expired.
  """

  def __init__(self):
    self._token_id = None
    self._token = None
    self._reason = None
    self._freeze()

  @property
  def token_id(self) -> int:
    """Id of the token."""
    return self._token_id or 0

  @token_id.setter
  def token_id(self, token_id: int):
    if token_id is None:
      del self.token_id
      return
    if not isinstance(token_id, int):
      raise TypeError('token_id must be of type int')
    del self.token
    self._token_id = token_id

  @property
  def token(self) -> str:
    """Value of the token."""
    return self._token or ""

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    del self.token_id
    self._token = token

  @property
  def reason(self) -> str:
    """Reason why this token is expired."""
    return self._reason or ""

  @reason.setter
  def reason(self, reason: Optional[str]):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class ExpireApiTokensRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      Username of the user whose api tokens will be expired/invalidated.
    reason (str)
      Why are we expiring api tokens of the user.
  """

  def __init__(self):
    self._user_name = ""
    self._reason = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    """Username of the user whose api tokens will be expired/invalidated."""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def reason(self) -> str:
    """Why are we expiring api tokens of the user."""
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class GenerateAnalyticsTokenRequest(KaggleObject):
  r"""
  """

  pass

class GenerateAnalyticsTokenResponse(KaggleObject):
  r"""
  Attributes:
    token (str)
  """

  def __init__(self):
    self._token = ""
    self._freeze()

  @property
  def token(self) -> str:
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class GenerateApiTokenRequest(KaggleObject):
  r"""
  Attributes:
    api_token (ApiToken)
      Details of the Api token to generate. If unspecified, generates an unscoped
      token (e.g., ApiV1 legacy key/token).
  """

  def __init__(self):
    self._api_token = None
    self._freeze()

  @property
  def api_token(self) -> Optional['ApiToken']:
    r"""
    Details of the Api token to generate. If unspecified, generates an unscoped
    token (e.g., ApiV1 legacy key/token).
    """
    return self._api_token

  @api_token.setter
  def api_token(self, api_token: Optional['ApiToken']):
    if api_token is None:
      del self.api_token
      return
    if not isinstance(api_token, ApiToken):
      raise TypeError('api_token must be of type ApiToken')
    self._api_token = api_token


class GenerateApiTokenResponse(KaggleObject):
  r"""
  Attributes:
    user_name (str)
    api_token (str)
  """

  def __init__(self):
    self._user_name = ""
    self._api_token = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def api_token(self) -> str:
    return self._api_token

  @api_token.setter
  def api_token(self, api_token: str):
    if api_token is None:
      del self.api_token
      return
    if not isinstance(api_token, str):
      raise TypeError('api_token must be of type str')
    self._api_token = api_token


class GetBuildInfoRequest(KaggleObject):
  r"""
  """

  pass

class GetBuildInfoResponse(KaggleObject):
  r"""
  Attributes:
    is_debug (bool)
    machine_name (str)
    build_hash (str)
    commit_url (str)
    local_dashboard_url (str)
  """

  def __init__(self):
    self._is_debug = False
    self._machine_name = ""
    self._build_hash = ""
    self._commit_url = ""
    self._local_dashboard_url = None
    self._freeze()

  @property
  def is_debug(self) -> bool:
    return self._is_debug

  @is_debug.setter
  def is_debug(self, is_debug: bool):
    if is_debug is None:
      del self.is_debug
      return
    if not isinstance(is_debug, bool):
      raise TypeError('is_debug must be of type bool')
    self._is_debug = is_debug

  @property
  def machine_name(self) -> str:
    return self._machine_name

  @machine_name.setter
  def machine_name(self, machine_name: str):
    if machine_name is None:
      del self.machine_name
      return
    if not isinstance(machine_name, str):
      raise TypeError('machine_name must be of type str')
    self._machine_name = machine_name

  @property
  def build_hash(self) -> str:
    return self._build_hash

  @build_hash.setter
  def build_hash(self, build_hash: str):
    if build_hash is None:
      del self.build_hash
      return
    if not isinstance(build_hash, str):
      raise TypeError('build_hash must be of type str')
    self._build_hash = build_hash

  @property
  def commit_url(self) -> str:
    return self._commit_url

  @commit_url.setter
  def commit_url(self, commit_url: str):
    if commit_url is None:
      del self.commit_url
      return
    if not isinstance(commit_url, str):
      raise TypeError('commit_url must be of type str')
    self._commit_url = commit_url

  @property
  def local_dashboard_url(self) -> str:
    return self._local_dashboard_url or ""

  @local_dashboard_url.setter
  def local_dashboard_url(self, local_dashboard_url: Optional[str]):
    if local_dashboard_url is None:
      del self.local_dashboard_url
      return
    if not isinstance(local_dashboard_url, str):
      raise TypeError('local_dashboard_url must be of type str')
    self._local_dashboard_url = local_dashboard_url


class GetPhoneVerificationStatusRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetPhoneVerificationStatusResponse(KaggleObject):
  r"""
  Attributes:
    status (UserVerificationStatus)
    reason (PhoneVerificationFailureReason)
  """

  def __init__(self):
    self._status = UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED
    self._reason = PhoneVerificationFailureReason.PHONE_VERIFICATION_FAILURE_REASON_UNSPECIFIED
    self._freeze()

  @property
  def status(self) -> 'UserVerificationStatus':
    return self._status

  @status.setter
  def status(self, status: 'UserVerificationStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, UserVerificationStatus):
      raise TypeError('status must be of type UserVerificationStatus')
    self._status = status

  @property
  def reason(self) -> 'PhoneVerificationFailureReason':
    return self._reason

  @reason.setter
  def reason(self, reason: 'PhoneVerificationFailureReason'):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, PhoneVerificationFailureReason):
      raise TypeError('reason must be of type PhoneVerificationFailureReason')
    self._reason = reason


class GetSupportPhoneNumbersRequest(KaggleObject):
  r"""
  """

  pass

class GetSupportPhoneNumbersResponse(KaggleObject):
  r"""
  Attributes:
    phone_info (SupportPhoneInfo)
  """

  def __init__(self):
    self._phone_info = []
    self._freeze()

  @property
  def phone_info(self) -> Optional[List[Optional['SupportPhoneInfo']]]:
    return self._phone_info

  @phone_info.setter
  def phone_info(self, phone_info: Optional[List[Optional['SupportPhoneInfo']]]):
    if phone_info is None:
      del self.phone_info
      return
    if not isinstance(phone_info, list):
      raise TypeError('phone_info must be of type list')
    if not all([isinstance(t, SupportPhoneInfo) for t in phone_info]):
      raise TypeError('phone_info must contain only items of type SupportPhoneInfo')
    self._phone_info = phone_info


class ListApiTokensRequest(KaggleObject):
  r"""
  Attributes:
    type (ApiTokenType)
      Filter tokens by their type.
    status (ApiTokenStatus)
      Filter tokens by their status.
    page_size (int)
      Maximum number of tokens to return.
    page_token (str)
      Token to retrieve the next page of results (see
      ListTokensResponse.next_page_token).
    read_mask (FieldMask)
  """

  def __init__(self):
    self._type = ApiTokenType.API_TOKEN_TYPE_UNSPECIFIED
    self._status = ApiTokenStatus.API_TOKEN_STATUS_UNSPECIFIED
    self._page_size = 0
    self._page_token = ""
    self._read_mask = None
    self._freeze()

  @property
  def type(self) -> 'ApiTokenType':
    """Filter tokens by their type."""
    return self._type

  @type.setter
  def type(self, type: 'ApiTokenType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, ApiTokenType):
      raise TypeError('type must be of type ApiTokenType')
    self._type = type

  @property
  def status(self) -> 'ApiTokenStatus':
    """Filter tokens by their status."""
    return self._status

  @status.setter
  def status(self, status: 'ApiTokenStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, ApiTokenStatus):
      raise TypeError('status must be of type ApiTokenStatus')
    self._status = status

  @property
  def page_size(self) -> int:
    """Maximum number of tokens to return."""
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
    r"""
    Token to retrieve the next page of results (see
    ListTokensResponse.next_page_token).
    """
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListApiTokensResponse(KaggleObject):
  r"""
  Attributes:
    tokens (ApiToken)
      List of tokens.
    next_page_token (str)
      Page token to retrieve the next page of results (see
      ListTokensRequest.page_token).
  """

  def __init__(self):
    self._tokens = []
    self._next_page_token = ""
    self._freeze()

  @property
  def tokens(self) -> Optional[List[Optional['ApiToken']]]:
    """List of tokens."""
    return self._tokens

  @tokens.setter
  def tokens(self, tokens: Optional[List[Optional['ApiToken']]]):
    if tokens is None:
      del self.tokens
      return
    if not isinstance(tokens, list):
      raise TypeError('tokens must be of type list')
    if not all([isinstance(t, ApiToken) for t in tokens]):
      raise TypeError('tokens must contain only items of type ApiToken')
    self._tokens = tokens

  @property
  def next_page_token(self) -> str:
    r"""
    Page token to retrieve the next page of results (see
    ListTokensRequest.page_token).
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


class ListCurrentUserModerationHistoryRequest(KaggleObject):
  r"""
  """

  pass

class ListCurrentUserModerationHistoryResponse(KaggleObject):
  r"""
  Attributes:
    user_penalties (CurrentUserPenalty)
      The list of penalties for the current user
  """

  def __init__(self):
    self._user_penalties = []
    self._freeze()

  @property
  def user_penalties(self) -> Optional[List[Optional['CurrentUserPenalty']]]:
    """The list of penalties for the current user"""
    return self._user_penalties

  @user_penalties.setter
  def user_penalties(self, user_penalties: Optional[List[Optional['CurrentUserPenalty']]]):
    if user_penalties is None:
      del self.user_penalties
      return
    if not isinstance(user_penalties, list):
      raise TypeError('user_penalties must be of type list')
    if not all([isinstance(t, CurrentUserPenalty) for t in user_penalties]):
      raise TypeError('user_penalties must contain only items of type CurrentUserPenalty')
    self._user_penalties = user_penalties


class ListSupportRequestsRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      Id of the users to list support requests for. If not specified, lists all
      recent support requests.
    type (ContactSupportType)
      Type of support requests. If not specified, lists all recent support
      requests.
    reasons (ContactSupportReason)
      Reason(s) for support requests. If not specified, lists all recent
      support requests.
    start_time (datetime)
      Inclusive start time for support requests. If not specified, lists all
      recent support requests.
    end_time (datetime)
      Inclusive end time for support requests. If not specified, lists all
      recent support requests.
  """

  def __init__(self):
    self._user_ids = []
    self._type = None
    self._reasons = []
    self._start_time = None
    self._end_time = None
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    r"""
    Id of the users to list support requests for. If not specified, lists all
    recent support requests.
    """
    return self._user_ids

  @user_ids.setter
  def user_ids(self, user_ids: Optional[List[int]]):
    if user_ids is None:
      del self.user_ids
      return
    if not isinstance(user_ids, list):
      raise TypeError('user_ids must be of type list')
    if not all([isinstance(t, int) for t in user_ids]):
      raise TypeError('user_ids must contain only items of type int')
    self._user_ids = user_ids

  @property
  def type(self) -> 'ContactSupportType':
    r"""
    Type of support requests. If not specified, lists all recent support
    requests.
    """
    return self._type or ContactSupportType.CONTACT_SUPPORT_TYPE_UNSPECIFIED

  @type.setter
  def type(self, type: Optional['ContactSupportType']):
    if type is None:
      del self.type
      return
    if not isinstance(type, ContactSupportType):
      raise TypeError('type must be of type ContactSupportType')
    self._type = type

  @property
  def reasons(self) -> Optional[List['ContactSupportReason']]:
    r"""
    Reason(s) for support requests. If not specified, lists all recent
    support requests.
    """
    return self._reasons

  @reasons.setter
  def reasons(self, reasons: Optional[List['ContactSupportReason']]):
    if reasons is None:
      del self.reasons
      return
    if not isinstance(reasons, list):
      raise TypeError('reasons must be of type list')
    if not all([isinstance(t, ContactSupportReason) for t in reasons]):
      raise TypeError('reasons must contain only items of type ContactSupportReason')
    self._reasons = reasons

  @property
  def start_time(self) -> datetime:
    r"""
    Inclusive start time for support requests. If not specified, lists all
    recent support requests.
    """
    return self._start_time or None

  @start_time.setter
  def start_time(self, start_time: Optional[datetime]):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    r"""
    Inclusive end time for support requests. If not specified, lists all
    recent support requests.
    """
    return self._end_time or None

  @end_time.setter
  def end_time(self, end_time: Optional[datetime]):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time


class ListSupportRequestsResponse(KaggleObject):
  r"""
  Attributes:
    support_requests (SupportRequest)
    statistics (SupportRequestStatistics)
      Statistics about the support requests.
  """

  def __init__(self):
    self._support_requests = []
    self._statistics = None
    self._freeze()

  @property
  def support_requests(self) -> Optional[List[Optional['SupportRequest']]]:
    return self._support_requests

  @support_requests.setter
  def support_requests(self, support_requests: Optional[List[Optional['SupportRequest']]]):
    if support_requests is None:
      del self.support_requests
      return
    if not isinstance(support_requests, list):
      raise TypeError('support_requests must be of type list')
    if not all([isinstance(t, SupportRequest) for t in support_requests]):
      raise TypeError('support_requests must contain only items of type SupportRequest')
    self._support_requests = support_requests

  @property
  def statistics(self) -> Optional['SupportRequestStatistics']:
    """Statistics about the support requests."""
    return self._statistics

  @statistics.setter
  def statistics(self, statistics: Optional['SupportRequestStatistics']):
    if statistics is None:
      del self.statistics
      return
    if not isinstance(statistics, SupportRequestStatistics):
      raise TypeError('statistics must be of type SupportRequestStatistics')
    self._statistics = statistics


class NewEmailRegistrationUserRequest(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      The display name for the new user.
    user_name (str)
      The username for the new user.
    email (str)
      The email for the new user.
    password (str)
      The password for the new user.
    captcha_response (str)
      The captcha response from the registration page.
    i_wish_to_subscribe_to_your_newsletter (bool)
      Whether the new user wants to subscribe to receiving Kaggle news.
    return_url (str)
      The URL to redirect the user to after successful registration.
    news_email_signup_was_opt_out (bool)
      Whether opt-out logic was used for the email signup.
  """

  def __init__(self):
    self._display_name = ""
    self._user_name = ""
    self._email = ""
    self._password = ""
    self._captcha_response = ""
    self._i_wish_to_subscribe_to_your_newsletter = False
    self._return_url = ""
    self._news_email_signup_was_opt_out = False
    self._freeze()

  @property
  def display_name(self) -> str:
    """The display name for the new user."""
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
  def user_name(self) -> str:
    """The username for the new user."""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def email(self) -> str:
    """The email for the new user."""
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
  def password(self) -> str:
    """The password for the new user."""
    return self._password

  @password.setter
  def password(self, password: str):
    if password is None:
      del self.password
      return
    if not isinstance(password, str):
      raise TypeError('password must be of type str')
    self._password = password

  @property
  def captcha_response(self) -> str:
    """The captcha response from the registration page."""
    return self._captcha_response

  @captcha_response.setter
  def captcha_response(self, captcha_response: str):
    if captcha_response is None:
      del self.captcha_response
      return
    if not isinstance(captcha_response, str):
      raise TypeError('captcha_response must be of type str')
    self._captcha_response = captcha_response

  @property
  def i_wish_to_subscribe_to_your_newsletter(self) -> bool:
    """Whether the new user wants to subscribe to receiving Kaggle news."""
    return self._i_wish_to_subscribe_to_your_newsletter

  @i_wish_to_subscribe_to_your_newsletter.setter
  def i_wish_to_subscribe_to_your_newsletter(self, i_wish_to_subscribe_to_your_newsletter: bool):
    if i_wish_to_subscribe_to_your_newsletter is None:
      del self.i_wish_to_subscribe_to_your_newsletter
      return
    if not isinstance(i_wish_to_subscribe_to_your_newsletter, bool):
      raise TypeError('i_wish_to_subscribe_to_your_newsletter must be of type bool')
    self._i_wish_to_subscribe_to_your_newsletter = i_wish_to_subscribe_to_your_newsletter

  @property
  def return_url(self) -> str:
    """The URL to redirect the user to after successful registration."""
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url

  @property
  def news_email_signup_was_opt_out(self) -> bool:
    """Whether opt-out logic was used for the email signup."""
    return self._news_email_signup_was_opt_out

  @news_email_signup_was_opt_out.setter
  def news_email_signup_was_opt_out(self, news_email_signup_was_opt_out: bool):
    if news_email_signup_was_opt_out is None:
      del self.news_email_signup_was_opt_out
      return
    if not isinstance(news_email_signup_was_opt_out, bool):
      raise TypeError('news_email_signup_was_opt_out must be of type bool')
    self._news_email_signup_was_opt_out = news_email_signup_was_opt_out


class NewEmailRegistrationUserResponse(KaggleObject):
  r"""
  Attributes:
    errors (RegistrationError)
      The registration errors for each field on the form.
    created_user_id (int)
      The user ID that was created for the user.
  """

  def __init__(self):
    self._errors = []
    self._created_user_id = 0
    self._freeze()

  @property
  def errors(self) -> Optional[List[Optional['RegistrationError']]]:
    """The registration errors for each field on the form."""
    return self._errors

  @errors.setter
  def errors(self, errors: Optional[List[Optional['RegistrationError']]]):
    if errors is None:
      del self.errors
      return
    if not isinstance(errors, list):
      raise TypeError('errors must be of type list')
    if not all([isinstance(t, RegistrationError) for t in errors]):
      raise TypeError('errors must contain only items of type RegistrationError')
    self._errors = errors

  @property
  def created_user_id(self) -> int:
    """The user ID that was created for the user."""
    return self._created_user_id

  @created_user_id.setter
  def created_user_id(self, created_user_id: int):
    if created_user_id is None:
      del self.created_user_id
      return
    if not isinstance(created_user_id, int):
      raise TypeError('created_user_id must be of type int')
    self._created_user_id = created_user_id


class RegistrationError(KaggleObject):
  r"""
  Attributes:
    field (RegistrationInfoFields)
      The field on the registration form.
    message_id (LoginMessageId)
      The ID of the message to display to the user.
  """

  def __init__(self):
    self._field = RegistrationInfoFields.REGISTRATION_INFO_FIELDS_UNSPECIFIED
    self._message_id = LoginMessageId.LOGIN_MESSAGE_ID_UNSPECIFIED
    self._freeze()

  @property
  def field(self) -> 'RegistrationInfoFields':
    """The field on the registration form."""
    return self._field

  @field.setter
  def field(self, field: 'RegistrationInfoFields'):
    if field is None:
      del self.field
      return
    if not isinstance(field, RegistrationInfoFields):
      raise TypeError('field must be of type RegistrationInfoFields')
    self._field = field

  @property
  def message_id(self) -> 'LoginMessageId':
    """The ID of the message to display to the user."""
    return self._message_id

  @message_id.setter
  def message_id(self, message_id: 'LoginMessageId'):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, LoginMessageId):
      raise TypeError('message_id must be of type LoginMessageId')
    self._message_id = message_id


class RegistrationValidationRequest(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      The display name for the new user.
    user_name (str)
      The username for the new user.
    email (str)
      The email for the new user.
    password (str)
      The password for the new user.
    captcha (str)
      The captcha response from the registration page.
  """

  def __init__(self):
    self._display_name = ""
    self._user_name = ""
    self._email = ""
    self._password = ""
    self._captcha = ""
    self._freeze()

  @property
  def display_name(self) -> str:
    """The display name for the new user."""
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
  def user_name(self) -> str:
    """The username for the new user."""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name

  @property
  def email(self) -> str:
    """The email for the new user."""
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
  def password(self) -> str:
    """The password for the new user."""
    return self._password

  @password.setter
  def password(self, password: str):
    if password is None:
      del self.password
      return
    if not isinstance(password, str):
      raise TypeError('password must be of type str')
    self._password = password

  @property
  def captcha(self) -> str:
    """The captcha response from the registration page."""
    return self._captcha

  @captcha.setter
  def captcha(self, captcha: str):
    if captcha is None:
      del self.captcha
      return
    if not isinstance(captcha, str):
      raise TypeError('captcha must be of type str')
    self._captcha = captcha


class RegistrationValidationResponse(KaggleObject):
  r"""
  Attributes:
    errors (RegistrationError)
      The registration errors for each field on the form.
  """

  def __init__(self):
    self._errors = []
    self._freeze()

  @property
  def errors(self) -> Optional[List[Optional['RegistrationError']]]:
    """The registration errors for each field on the form."""
    return self._errors

  @errors.setter
  def errors(self, errors: Optional[List[Optional['RegistrationError']]]):
    if errors is None:
      del self.errors
      return
    if not isinstance(errors, list):
      raise TypeError('errors must be of type list')
    if not all([isinstance(t, RegistrationError) for t in errors]):
      raise TypeError('errors must contain only items of type RegistrationError')
    self._errors = errors


class ReportContentRequest(KaggleObject):
  r"""
  Attributes:
    author_user_name (str)
      The username of the author of the content being reported
    author_user_id (int)
      The ID of the author of the content being reported
    explanation (str)
      The additional details provided by the user for the report. Only some
      policy violations expect an explanation and are allowlisted.
    message_id (int)
      The ID of the forum message being reported
    kernel_session_id (int)
      The ID of the kernel session being reported
    dataset_version_id (int)
      The ID of the dataset version being reported
    model_version_id (int)
      The ID of the model version being reported
    profile_user_id (int)
      The ID of the user being reported (when reporting username/display
      name/bio)
    competition_id (int)
      The ID of the user being reported (when reporting username/display
      name/bio)
    organization_id (int)
      The ID of the organization being reported
    policy_violation_id (PolicyViolationId)
      The ID of the policy violation being reported.
    group_id (int)
      The ID of the group being reported
    write_up_message_id (int)
      The ID of the writeup forum message being reported
    benchmark_identifier (BenchmarkIdentifier)
      The ID of the benchmark being reported
    benchmark_task_identifier (TaskIdentifier)
      The ID of the benchmark task being reported
  """

  def __init__(self):
    self._author_user_name = None
    self._author_user_id = None
    self._explanation = None
    self._message_id = None
    self._kernel_session_id = None
    self._dataset_version_id = None
    self._model_version_id = None
    self._profile_user_id = None
    self._competition_id = None
    self._organization_id = None
    self._policy_violation_id = PolicyViolationId.POLICY_VIOLATION_ID_UNSPECIFIED
    self._group_id = None
    self._write_up_message_id = None
    self._benchmark_identifier = None
    self._benchmark_task_identifier = None
    self._freeze()

  @property
  def author_user_name(self) -> str:
    """The username of the author of the content being reported"""
    return self._author_user_name or ""

  @author_user_name.setter
  def author_user_name(self, author_user_name: str):
    if author_user_name is None:
      del self.author_user_name
      return
    if not isinstance(author_user_name, str):
      raise TypeError('author_user_name must be of type str')
    del self.author_user_id
    self._author_user_name = author_user_name

  @property
  def author_user_id(self) -> int:
    """The ID of the author of the content being reported"""
    return self._author_user_id or 0

  @author_user_id.setter
  def author_user_id(self, author_user_id: int):
    if author_user_id is None:
      del self.author_user_id
      return
    if not isinstance(author_user_id, int):
      raise TypeError('author_user_id must be of type int')
    del self.author_user_name
    self._author_user_id = author_user_id

  @property
  def policy_violation_id(self) -> 'PolicyViolationId':
    """The ID of the policy violation being reported."""
    return self._policy_violation_id

  @policy_violation_id.setter
  def policy_violation_id(self, policy_violation_id: 'PolicyViolationId'):
    if policy_violation_id is None:
      del self.policy_violation_id
      return
    if not isinstance(policy_violation_id, PolicyViolationId):
      raise TypeError('policy_violation_id must be of type PolicyViolationId')
    self._policy_violation_id = policy_violation_id

  @property
  def explanation(self) -> str:
    r"""
    The additional details provided by the user for the report. Only some
    policy violations expect an explanation and are allowlisted.
    """
    return self._explanation or ""

  @explanation.setter
  def explanation(self, explanation: Optional[str]):
    if explanation is None:
      del self.explanation
      return
    if not isinstance(explanation, str):
      raise TypeError('explanation must be of type str')
    self._explanation = explanation

  @property
  def message_id(self) -> int:
    """The ID of the forum message being reported"""
    return self._message_id or 0

  @message_id.setter
  def message_id(self, message_id: int):
    if message_id is None:
      del self.message_id
      return
    if not isinstance(message_id, int):
      raise TypeError('message_id must be of type int')
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._message_id = message_id

  @property
  def write_up_message_id(self) -> int:
    """The ID of the writeup forum message being reported"""
    return self._write_up_message_id or 0

  @write_up_message_id.setter
  def write_up_message_id(self, write_up_message_id: int):
    if write_up_message_id is None:
      del self.write_up_message_id
      return
    if not isinstance(write_up_message_id, int):
      raise TypeError('write_up_message_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._write_up_message_id = write_up_message_id

  @property
  def kernel_session_id(self) -> int:
    """The ID of the kernel session being reported"""
    return self._kernel_session_id or 0

  @kernel_session_id.setter
  def kernel_session_id(self, kernel_session_id: int):
    if kernel_session_id is None:
      del self.kernel_session_id
      return
    if not isinstance(kernel_session_id, int):
      raise TypeError('kernel_session_id must be of type int')
    del self.message_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._kernel_session_id = kernel_session_id

  @property
  def dataset_version_id(self) -> int:
    """The ID of the dataset version being reported"""
    return self._dataset_version_id or 0

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._dataset_version_id = dataset_version_id

  @property
  def model_version_id(self) -> int:
    """The ID of the model version being reported"""
    return self._model_version_id or 0

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._model_version_id = model_version_id

  @property
  def profile_user_id(self) -> int:
    r"""
    The ID of the user being reported (when reporting username/display
    name/bio)
    """
    return self._profile_user_id or 0

  @profile_user_id.setter
  def profile_user_id(self, profile_user_id: int):
    if profile_user_id is None:
      del self.profile_user_id
      return
    if not isinstance(profile_user_id, int):
      raise TypeError('profile_user_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._profile_user_id = profile_user_id

  @property
  def competition_id(self) -> int:
    r"""
    The ID of the user being reported (when reporting username/display
    name/bio)
    """
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: int):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._competition_id = competition_id

  @property
  def organization_id(self) -> int:
    """The ID of the organization being reported"""
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._organization_id = organization_id

  @property
  def group_id(self) -> int:
    """The ID of the group being reported"""
    return self._group_id or 0

  @group_id.setter
  def group_id(self, group_id: int):
    if group_id is None:
      del self.group_id
      return
    if not isinstance(group_id, int):
      raise TypeError('group_id must be of type int')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.write_up_message_id
    del self.benchmark_identifier
    del self.benchmark_task_identifier
    self._group_id = group_id

  @property
  def benchmark_identifier(self) -> Optional['BenchmarkIdentifier']:
    """The ID of the benchmark being reported"""
    return self._benchmark_identifier or None

  @benchmark_identifier.setter
  def benchmark_identifier(self, benchmark_identifier: Optional['BenchmarkIdentifier']):
    if benchmark_identifier is None:
      del self.benchmark_identifier
      return
    if not isinstance(benchmark_identifier, BenchmarkIdentifier):
      raise TypeError('benchmark_identifier must be of type BenchmarkIdentifier')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_task_identifier
    self._benchmark_identifier = benchmark_identifier

  @property
  def benchmark_task_identifier(self) -> Optional['TaskIdentifier']:
    """The ID of the benchmark task being reported"""
    return self._benchmark_task_identifier or None

  @benchmark_task_identifier.setter
  def benchmark_task_identifier(self, benchmark_task_identifier: Optional['TaskIdentifier']):
    if benchmark_task_identifier is None:
      del self.benchmark_task_identifier
      return
    if not isinstance(benchmark_task_identifier, TaskIdentifier):
      raise TypeError('benchmark_task_identifier must be of type TaskIdentifier')
    del self.message_id
    del self.kernel_session_id
    del self.dataset_version_id
    del self.model_version_id
    del self.profile_user_id
    del self.competition_id
    del self.organization_id
    del self.group_id
    del self.write_up_message_id
    del self.benchmark_identifier
    self._benchmark_task_identifier = benchmark_task_identifier


class ResendVerificationEmailRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
    user_id (int)
    return_url (str)
  """

  def __init__(self):
    self._email = None
    self._user_id = None
    self._return_url = None
    self._freeze()

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
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def return_url(self) -> str:
    return self._return_url or ""

  @return_url.setter
  def return_url(self, return_url: Optional[str]):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class ResetPasswordRequest(KaggleObject):
  r"""
  Attributes:
    return_url (str)
      The url the user started the password reset flow on (to send the back to).
    user_id (int)
      The user whose password we're trying to reset. Must match the code.
    new_password (str)
      The new password the user would like.
    reset_password_code (str)
      The reset code, an alphanumeric 6-character code generated by the start of
      the flow.
  """

  def __init__(self):
    self._return_url = None
    self._user_id = 0
    self._new_password = None
    self._reset_password_code = None
    self._freeze()

  @property
  def return_url(self) -> str:
    """The url the user started the password reset flow on (to send the back to)."""
    return self._return_url or ""

  @return_url.setter
  def return_url(self, return_url: Optional[str]):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url

  @property
  def user_id(self) -> int:
    """The user whose password we're trying to reset. Must match the code."""
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
  def new_password(self) -> str:
    """The new password the user would like."""
    return self._new_password or ""

  @new_password.setter
  def new_password(self, new_password: Optional[str]):
    if new_password is None:
      del self.new_password
      return
    if not isinstance(new_password, str):
      raise TypeError('new_password must be of type str')
    self._new_password = new_password

  @property
  def reset_password_code(self) -> str:
    r"""
    The reset code, an alphanumeric 6-character code generated by the start of
    the flow.
    """
    return self._reset_password_code or ""

  @reset_password_code.setter
  def reset_password_code(self, reset_password_code: Optional[str]):
    if reset_password_code is None:
      del self.reset_password_code
      return
    if not isinstance(reset_password_code, str):
      raise TypeError('reset_password_code must be of type str')
    self._reset_password_code = reset_password_code


class ResetPasswordResponse(KaggleObject):
  r"""
  Attributes:
    return_url (str)
      The URl of where the user should be redirected to.
  """

  def __init__(self):
    self._return_url = ""
    self._freeze()

  @property
  def return_url(self) -> str:
    """The URl of where the user should be redirected to."""
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class SignOutRequest(KaggleObject):
  r"""
  """

  pass

class SoftDeleteAccountRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The id of the user to delete.
    reason (str)
      The reason the account is being deleted.
  """

  def __init__(self):
    self._user_id = 0
    self._reason = ""
    self._freeze()

  @property
  def user_id(self) -> int:
    """The id of the user to delete."""
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
  def reason(self) -> str:
    """The reason the account is being deleted."""
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class SoftDeleteAccountResponse(KaggleObject):
  r"""
  Attributes:
    user_soft_deleted (bool)
      Whether the user was successfully deleted.
  """

  def __init__(self):
    self._user_soft_deleted = False
    self._freeze()

  @property
  def user_soft_deleted(self) -> bool:
    """Whether the user was successfully deleted."""
    return self._user_soft_deleted

  @user_soft_deleted.setter
  def user_soft_deleted(self, user_soft_deleted: bool):
    if user_soft_deleted is None:
      del self.user_soft_deleted
      return
    if not isinstance(user_soft_deleted, bool):
      raise TypeError('user_soft_deleted must be of type bool')
    self._user_soft_deleted = user_soft_deleted


class StartMigrateSsoRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
    return_url (str)
  """

  def __init__(self):
    self._email = None
    self._return_url = None
    self._freeze()

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
  def return_url(self) -> str:
    return self._return_url or ""

  @return_url.setter
  def return_url(self, return_url: Optional[str]):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class StartMigrateSsoResponse(KaggleObject):
  r"""
  Attributes:
    outcome (StartMigrateSsoOutcome)
    user_id (int)
  """

  def __init__(self):
    self._outcome = StartMigrateSsoOutcome.GOOGLE_SSO_EXISTS
    self._user_id = None
    self._freeze()

  @property
  def outcome(self) -> 'StartMigrateSsoOutcome':
    return self._outcome

  @outcome.setter
  def outcome(self, outcome: 'StartMigrateSsoOutcome'):
    if outcome is None:
      del self.outcome
      return
    if not isinstance(outcome, StartMigrateSsoOutcome):
      raise TypeError('outcome must be of type StartMigrateSsoOutcome')
    self._outcome = outcome

  @property
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class StartPhoneVerificationRequest(KaggleObject):
  r"""
  Attributes:
    phone_number (str)
      The phone number to verify
    captcha_response (str)
      The captcha response from the phone verification page
    redirect_url (str)
      The URL to return the user to after completing verification
  """

  def __init__(self):
    self._phone_number = ""
    self._captcha_response = ""
    self._redirect_url = ""
    self._freeze()

  @property
  def phone_number(self) -> str:
    """The phone number to verify"""
    return self._phone_number

  @phone_number.setter
  def phone_number(self, phone_number: str):
    if phone_number is None:
      del self.phone_number
      return
    if not isinstance(phone_number, str):
      raise TypeError('phone_number must be of type str')
    self._phone_number = phone_number

  @property
  def captcha_response(self) -> str:
    """The captcha response from the phone verification page"""
    return self._captcha_response

  @captcha_response.setter
  def captcha_response(self, captcha_response: str):
    if captcha_response is None:
      del self.captcha_response
      return
    if not isinstance(captcha_response, str):
      raise TypeError('captcha_response must be of type str')
    self._captcha_response = captcha_response

  @property
  def redirect_url(self) -> str:
    """The URL to return the user to after completing verification"""
    return self._redirect_url

  @redirect_url.setter
  def redirect_url(self, redirect_url: str):
    if redirect_url is None:
      del self.redirect_url
      return
    if not isinstance(redirect_url, str):
      raise TypeError('redirect_url must be of type str')
    self._redirect_url = redirect_url


class StartPhoneVerificationResponse(KaggleObject):
  r"""
  Attributes:
    phone_verified (bool)
      Whether the user is already phone verified
    redirect_url (str)
      If set, the client should redirect the user to this URL to start the
      phone verification flow. If not set, user should've received an SMS
      containing a verification code already, so the client should display
      the verification code entry form.
    fallback_to_identity_verification (bool)
      Whether the user should be requested to do identity/selfie verification
      instead of phone verification due to region restrictions or other reasons.
  """

  def __init__(self):
    self._phone_verified = False
    self._redirect_url = ""
    self._fallback_to_identity_verification = False
    self._freeze()

  @property
  def phone_verified(self) -> bool:
    """Whether the user is already phone verified"""
    return self._phone_verified

  @phone_verified.setter
  def phone_verified(self, phone_verified: bool):
    if phone_verified is None:
      del self.phone_verified
      return
    if not isinstance(phone_verified, bool):
      raise TypeError('phone_verified must be of type bool')
    self._phone_verified = phone_verified

  @property
  def redirect_url(self) -> str:
    r"""
    If set, the client should redirect the user to this URL to start the
    phone verification flow. If not set, user should've received an SMS
    containing a verification code already, so the client should display
    the verification code entry form.
    """
    return self._redirect_url

  @redirect_url.setter
  def redirect_url(self, redirect_url: str):
    if redirect_url is None:
      del self.redirect_url
      return
    if not isinstance(redirect_url, str):
      raise TypeError('redirect_url must be of type str')
    self._redirect_url = redirect_url

  @property
  def fallback_to_identity_verification(self) -> bool:
    r"""
    Whether the user should be requested to do identity/selfie verification
    instead of phone verification due to region restrictions or other reasons.
    """
    return self._fallback_to_identity_verification

  @fallback_to_identity_verification.setter
  def fallback_to_identity_verification(self, fallback_to_identity_verification: bool):
    if fallback_to_identity_verification is None:
      del self.fallback_to_identity_verification
      return
    if not isinstance(fallback_to_identity_verification, bool):
      raise TypeError('fallback_to_identity_verification must be of type bool')
    self._fallback_to_identity_verification = fallback_to_identity_verification


class StartResetPasswordRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
      The email of the user who's password is being reset. If there's a matching
      user an email will be sent to this address. If there's no matching user,
      the response will be identical, but without any email being sent.
    return_url (str)
      The return Url for after this process is complete, sent as part of a link
      to the user's email.
  """

  def __init__(self):
    self._email = ""
    self._return_url = None
    self._freeze()

  @property
  def email(self) -> str:
    r"""
    The email of the user who's password is being reset. If there's a matching
    user an email will be sent to this address. If there's no matching user,
    the response will be identical, but without any email being sent.
    """
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
  def return_url(self) -> str:
    r"""
    The return Url for after this process is complete, sent as part of a link
    to the user's email.
    """
    return self._return_url or ""

  @return_url.setter
  def return_url(self, return_url: Optional[str]):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class SupportPhoneInfo(KaggleObject):
  r"""
  Attributes:
    country_code (str)
      2-digit country code
    country_name (str)
      Full country name, to display
    phone_number (str)
      The local phone number for support.
    support_hours_description (str)
      Textual description of the hours that support is open.
  """

  def __init__(self):
    self._country_code = ""
    self._country_name = ""
    self._phone_number = ""
    self._support_hours_description = ""
    self._freeze()

  @property
  def country_code(self) -> str:
    """2-digit country code"""
    return self._country_code

  @country_code.setter
  def country_code(self, country_code: str):
    if country_code is None:
      del self.country_code
      return
    if not isinstance(country_code, str):
      raise TypeError('country_code must be of type str')
    self._country_code = country_code

  @property
  def country_name(self) -> str:
    """Full country name, to display"""
    return self._country_name

  @country_name.setter
  def country_name(self, country_name: str):
    if country_name is None:
      del self.country_name
      return
    if not isinstance(country_name, str):
      raise TypeError('country_name must be of type str')
    self._country_name = country_name

  @property
  def phone_number(self) -> str:
    """The local phone number for support."""
    return self._phone_number

  @phone_number.setter
  def phone_number(self, phone_number: str):
    if phone_number is None:
      del self.phone_number
      return
    if not isinstance(phone_number, str):
      raise TypeError('phone_number must be of type str')
    self._phone_number = phone_number

  @property
  def support_hours_description(self) -> str:
    """Textual description of the hours that support is open."""
    return self._support_hours_description

  @support_hours_description.setter
  def support_hours_description(self, support_hours_description: str):
    if support_hours_description is None:
      del self.support_hours_description
      return
    if not isinstance(support_hours_description, str):
      raise TypeError('support_hours_description must be of type str')
    self._support_hours_description = support_hours_description


class SupportRequestStatistics(KaggleObject):
  r"""
  Attributes:
    count (int)
      Number of support requests.
    count_by_reason (int)
      Number of support requests by reason.
    count_by_region (int)
      Number of support requests by region.
  """

  def __init__(self):
    self._count = None
    self._count_by_reason = {}
    self._count_by_region = {}
    self._freeze()

  @property
  def count(self) -> int:
    """Number of support requests."""
    return self._count or 0

  @count.setter
  def count(self, count: Optional[int]):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def count_by_reason(self) -> Optional[Dict[str, int]]:
    """Number of support requests by reason."""
    return self._count_by_reason

  @count_by_reason.setter
  def count_by_reason(self, count_by_reason: Optional[Dict[str, int]]):
    if count_by_reason is None:
      del self.count_by_reason
      return
    if not isinstance(count_by_reason, dict):
      raise TypeError('count_by_reason must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_reason]):
      raise TypeError('count_by_reason must contain only items of type int')
    self._count_by_reason = count_by_reason

  @property
  def count_by_region(self) -> Optional[Dict[str, int]]:
    """Number of support requests by region."""
    return self._count_by_region

  @count_by_region.setter
  def count_by_region(self, count_by_region: Optional[Dict[str, int]]):
    if count_by_region is None:
      del self.count_by_region
      return
    if not isinstance(count_by_region, dict):
      raise TypeError('count_by_region must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_region]):
      raise TypeError('count_by_region must contain only items of type int')
    self._count_by_region = count_by_region


class TakeoutUserRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    takeout_type (TakeoutType)
  """

  def __init__(self):
    self._user_id = 0
    self._takeout_type = TakeoutType.TAKEOUT_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def user_id(self) -> int:
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
  def takeout_type(self) -> 'TakeoutType':
    return self._takeout_type

  @takeout_type.setter
  def takeout_type(self, takeout_type: 'TakeoutType'):
    if takeout_type is None:
      del self.takeout_type
      return
    if not isinstance(takeout_type, TakeoutType):
      raise TypeError('takeout_type must be of type TakeoutType')
    self._takeout_type = takeout_type


class TakeoutUserResponse(KaggleObject):
  r"""
  Attributes:
    read_access_url (str)
      A secure URL that allows time-limited access to a file without
      authentication. Should be treated very carefully.
    bucket_url (str)
      The url to the folder that contains the takeout data.
  """

  def __init__(self):
    self._read_access_url = None
    self._bucket_url = None
    self._freeze()

  @property
  def read_access_url(self) -> str:
    r"""
    A secure URL that allows time-limited access to a file without
    authentication. Should be treated very carefully.
    """
    return self._read_access_url or ""

  @read_access_url.setter
  def read_access_url(self, read_access_url: Optional[str]):
    if read_access_url is None:
      del self.read_access_url
      return
    if not isinstance(read_access_url, str):
      raise TypeError('read_access_url must be of type str')
    self._read_access_url = read_access_url

  @property
  def bucket_url(self) -> str:
    """The url to the folder that contains the takeout data."""
    return self._bucket_url or ""

  @bucket_url.setter
  def bucket_url(self, bucket_url: Optional[str]):
    if bucket_url is None:
      del self.bucket_url
      return
    if not isinstance(bucket_url, str):
      raise TypeError('bucket_url must be of type str')
    self._bucket_url = bucket_url


class ValidateResetPasswordCodeRequest(KaggleObject):
  r"""
  Attributes:
    email (str)
      The email address of the user you are validating the password of.
    reset_password_code (str)
      The code sent to email of the password to reset.
    resend_if_expired (bool)
      Whether the code should automatically be resent if it is expired.
    return_url (str)
      The return url for the user, needed for resending the code.
  """

  def __init__(self):
    self._email = ""
    self._reset_password_code = ""
    self._resend_if_expired = False
    self._return_url = None
    self._freeze()

  @property
  def email(self) -> str:
    """The email address of the user you are validating the password of."""
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
  def reset_password_code(self) -> str:
    """The code sent to email of the password to reset."""
    return self._reset_password_code

  @reset_password_code.setter
  def reset_password_code(self, reset_password_code: str):
    if reset_password_code is None:
      del self.reset_password_code
      return
    if not isinstance(reset_password_code, str):
      raise TypeError('reset_password_code must be of type str')
    self._reset_password_code = reset_password_code

  @property
  def resend_if_expired(self) -> bool:
    """Whether the code should automatically be resent if it is expired."""
    return self._resend_if_expired

  @resend_if_expired.setter
  def resend_if_expired(self, resend_if_expired: bool):
    if resend_if_expired is None:
      del self.resend_if_expired
      return
    if not isinstance(resend_if_expired, bool):
      raise TypeError('resend_if_expired must be of type bool')
    self._resend_if_expired = resend_if_expired

  @property
  def return_url(self) -> str:
    """The return url for the user, needed for resending the code."""
    return self._return_url or ""

  @return_url.setter
  def return_url(self, return_url: Optional[str]):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url


class ValidateResetPasswordCodeResponse(KaggleObject):
  r"""
  Attributes:
    outcome (ValidateResetPasswordCodeOutcome)
      What was the outcome of validating the code.
    user_id (int)
      The user id of the matching user. Only returned if code and email are a
      valid match.
  """

  def __init__(self):
    self._outcome = ValidateResetPasswordCodeOutcome.VALIDATE_RESET_PASSWORD_CODE_OUTCOME_UNSPECIFIED
    self._user_id = None
    self._freeze()

  @property
  def outcome(self) -> 'ValidateResetPasswordCodeOutcome':
    """What was the outcome of validating the code."""
    return self._outcome

  @outcome.setter
  def outcome(self, outcome: 'ValidateResetPasswordCodeOutcome'):
    if outcome is None:
      del self.outcome
      return
    if not isinstance(outcome, ValidateResetPasswordCodeOutcome):
      raise TypeError('outcome must be of type ValidateResetPasswordCodeOutcome')
    self._outcome = outcome

  @property
  def user_id(self) -> int:
    r"""
    The user id of the matching user. Only returned if code and email are a
    valid match.
    """
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class VerifyAccountEmailRequest(KaggleObject):
  r"""
  Attributes:
    verification_code (str)
      The verification code typed in by the user
    user_id (int)
      The user to be verified.
    return_url (str)
      Their return URL, used in case the email needs to be resent.
    registration_session_id (str)
      The id of the session that initiated the new account registration.
  """

  def __init__(self):
    self._verification_code = ""
    self._user_id = 0
    self._return_url = ""
    self._registration_session_id = ""
    self._freeze()

  @property
  def verification_code(self) -> str:
    """The verification code typed in by the user"""
    return self._verification_code

  @verification_code.setter
  def verification_code(self, verification_code: str):
    if verification_code is None:
      del self.verification_code
      return
    if not isinstance(verification_code, str):
      raise TypeError('verification_code must be of type str')
    self._verification_code = verification_code

  @property
  def user_id(self) -> int:
    """The user to be verified."""
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
  def return_url(self) -> str:
    """Their return URL, used in case the email needs to be resent."""
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url

  @property
  def registration_session_id(self) -> str:
    """The id of the session that initiated the new account registration."""
    return self._registration_session_id

  @registration_session_id.setter
  def registration_session_id(self, registration_session_id: str):
    if registration_session_id is None:
      del self.registration_session_id
      return
    if not isinstance(registration_session_id, str):
      raise TypeError('registration_session_id must be of type str')
    self._registration_session_id = registration_session_id


class VerifyAccountEmailResponse(KaggleObject):
  r"""
  Attributes:
    local_return_url (str)
      The given return url, verified to be a local url (safe to redirect to).
  """

  def __init__(self):
    self._local_return_url = ""
    self._freeze()

  @property
  def local_return_url(self) -> str:
    """The given return url, verified to be a local url (safe to redirect to)."""
    return self._local_return_url

  @local_return_url.setter
  def local_return_url(self, local_return_url: str):
    if local_return_url is None:
      del self.local_return_url
      return
    if not isinstance(local_return_url, str):
      raise TypeError('local_return_url must be of type str')
    self._local_return_url = local_return_url


class VerifyPhoneDto(KaggleObject):
  r"""
  Attributes:
    return_url (str)
    already_sent_code (bool)
  """

  def __init__(self):
    self._return_url = ""
    self._already_sent_code = False
    self._freeze()

  @property
  def return_url(self) -> str:
    return self._return_url

  @return_url.setter
  def return_url(self, return_url: str):
    if return_url is None:
      del self.return_url
      return
    if not isinstance(return_url, str):
      raise TypeError('return_url must be of type str')
    self._return_url = return_url

  @property
  def already_sent_code(self) -> bool:
    return self._already_sent_code

  @already_sent_code.setter
  def already_sent_code(self, already_sent_code: bool):
    if already_sent_code is None:
      del self.already_sent_code
      return
    if not isinstance(already_sent_code, bool):
      raise TypeError('already_sent_code must be of type bool')
    self._already_sent_code = already_sent_code


class VerifyPhoneRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    phone_number (str)
    force_verify (bool)
  """

  def __init__(self):
    self._user_id = 0
    self._phone_number = None
    self._force_verify = False
    self._freeze()

  @property
  def user_id(self) -> int:
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
  def force_verify(self) -> bool:
    return self._force_verify

  @force_verify.setter
  def force_verify(self, force_verify: bool):
    if force_verify is None:
      del self.force_verify
      return
    if not isinstance(force_verify, bool):
      raise TypeError('force_verify must be of type bool')
    self._force_verify = force_verify


BatchSoftDeleteAccountsRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
]

BatchSoftDeleteAccountsResponse._fields = [
  FieldMetadata("successfullyDeletedUserIds", "successfully_deleted_user_ids", "_successfully_deleted_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("alreadyDeletedUserIds", "already_deleted_user_ids", "_already_deleted_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("erroredUserIds", "errored_user_ids", "_errored_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ContactPageDto._fields = [
  FieldMetadata("forgotPasswordLink", "forgot_password_link", "_forgot_password_link", str, "", PredefinedSerializer()),
  FieldMetadata("competitionsLink", "competitions_link", "_competitions_link", str, "", PredefinedSerializer()),
  FieldMetadata("datasetsLink", "datasets_link", "_datasets_link", str, "", PredefinedSerializer()),
  FieldMetadata("newDatasetLink", "new_dataset_link", "_new_dataset_link", str, "", PredefinedSerializer()),
  FieldMetadata("datasetsForumLink", "datasets_forum_link", "_datasets_forum_link", str, "", PredefinedSerializer()),
  FieldMetadata("hostLink", "host_link", "_host_link", str, "", PredefinedSerializer()),
  FieldMetadata("communityCompetitionsOverviewLink", "community_competitions_overview_link", "_community_competitions_overview_link", str, "", PredefinedSerializer()),
  FieldMetadata("migrateDeprecatedSsoLink", "migrate_deprecated_sso_link", "_migrate_deprecated_sso_link", str, "", PredefinedSerializer()),
  FieldMetadata("complianceLink", "compliance_link", "_compliance_link", str, "", PredefinedSerializer()),
]

ContactSupportRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("responses", "responses", "_responses", str, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("question", "question", "_question", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("requireCaptcha", "require_captcha", "_require_captcha", bool, False, PredefinedSerializer()),
  FieldMetadata("captchaResponse", "captcha_response", "_captcha_response", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", ContactSupportType, ContactSupportType.CONTACT_SUPPORT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("reason", "reason", "_reason", ContactSupportReason, ContactSupportReason.CONTACT_SUPPORT_REASON_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("appealType", "appeal_type", "_appeal_type", AppealType, None, EnumSerializer(), optional=True),
]

CurrentUserPenalty._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("logTime", "log_time", "_log_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("policyViolationDescriptions", "policy_violation_descriptions", "_policy_violation_descriptions", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("suspensionDurationDays", "suspension_duration_days", "_suspension_duration_days", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("suspensionLiftTime", "suspension_lift_time", "_suspension_lift_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("otherViolation", "other_violation", "_other_violation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("appealApprovalTime", "appeal_approval_time", "_appeal_approval_time", datetime, None, DateTimeSerializer(), optional=True),
]

DeleteCurrentAccountRequest._fields = [
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
  FieldMetadata("captchaResponseToken", "captcha_response_token", "_captcha_response_token", str, "", PredefinedSerializer()),
]

ExpireApiTokenRequest._fields = [
  FieldMetadata("tokenId", "token_id", "_token_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("token", "token", "_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reason", "reason", "_reason", str, None, PredefinedSerializer(), optional=True),
]

ExpireApiTokensRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
]

GenerateAnalyticsTokenRequest._fields = []

GenerateAnalyticsTokenResponse._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

GenerateApiTokenRequest._fields = [
  FieldMetadata("apiToken", "api_token", "_api_token", ApiToken, None, KaggleObjectSerializer()),
]

GenerateApiTokenResponse._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("apiToken", "api_token", "_api_token", str, "", PredefinedSerializer()),
]

GetBuildInfoRequest._fields = []

GetBuildInfoResponse._fields = [
  FieldMetadata("isDebug", "is_debug", "_is_debug", bool, False, PredefinedSerializer()),
  FieldMetadata("machineName", "machine_name", "_machine_name", str, "", PredefinedSerializer()),
  FieldMetadata("buildHash", "build_hash", "_build_hash", str, "", PredefinedSerializer()),
  FieldMetadata("commitUrl", "commit_url", "_commit_url", str, "", PredefinedSerializer()),
  FieldMetadata("localDashboardUrl", "local_dashboard_url", "_local_dashboard_url", str, None, PredefinedSerializer(), optional=True),
]

GetPhoneVerificationStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetPhoneVerificationStatusResponse._fields = [
  FieldMetadata("status", "status", "_status", UserVerificationStatus, UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("reason", "reason", "_reason", PhoneVerificationFailureReason, PhoneVerificationFailureReason.PHONE_VERIFICATION_FAILURE_REASON_UNSPECIFIED, EnumSerializer()),
]

GetSupportPhoneNumbersRequest._fields = []

GetSupportPhoneNumbersResponse._fields = [
  FieldMetadata("phoneInfo", "phone_info", "_phone_info", SupportPhoneInfo, [], ListSerializer(KaggleObjectSerializer())),
]

ListApiTokensRequest._fields = [
  FieldMetadata("type", "type", "_type", ApiTokenType, ApiTokenType.API_TOKEN_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("status", "status", "_status", ApiTokenStatus, ApiTokenStatus.API_TOKEN_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListApiTokensResponse._fields = [
  FieldMetadata("tokens", "tokens", "_tokens", ApiToken, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListCurrentUserModerationHistoryRequest._fields = []

ListCurrentUserModerationHistoryResponse._fields = [
  FieldMetadata("userPenalties", "user_penalties", "_user_penalties", CurrentUserPenalty, [], ListSerializer(KaggleObjectSerializer())),
]

ListSupportRequestsRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("type", "type", "_type", ContactSupportType, None, EnumSerializer(), optional=True),
  FieldMetadata("reasons", "reasons", "_reasons", ContactSupportReason, [], ListSerializer(EnumSerializer())),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer(), optional=True),
]

ListSupportRequestsResponse._fields = [
  FieldMetadata("supportRequests", "support_requests", "_support_requests", SupportRequest, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("statistics", "statistics", "_statistics", SupportRequestStatistics, None, KaggleObjectSerializer()),
]

NewEmailRegistrationUserRequest._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("password", "password", "_password", str, "", PredefinedSerializer()),
  FieldMetadata("captchaResponse", "captcha_response", "_captcha_response", str, "", PredefinedSerializer()),
  FieldMetadata("iWishToSubscribeToYourNewsletter", "i_wish_to_subscribe_to_your_newsletter", "_i_wish_to_subscribe_to_your_newsletter", bool, False, PredefinedSerializer()),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
  FieldMetadata("newsEmailSignupWasOptOut", "news_email_signup_was_opt_out", "_news_email_signup_was_opt_out", bool, False, PredefinedSerializer()),
]

NewEmailRegistrationUserResponse._fields = [
  FieldMetadata("errors", "errors", "_errors", RegistrationError, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("createdUserId", "created_user_id", "_created_user_id", int, 0, PredefinedSerializer()),
]

RegistrationError._fields = [
  FieldMetadata("field", "field", "_field", RegistrationInfoFields, RegistrationInfoFields.REGISTRATION_INFO_FIELDS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("messageId", "message_id", "_message_id", LoginMessageId, LoginMessageId.LOGIN_MESSAGE_ID_UNSPECIFIED, EnumSerializer()),
]

RegistrationValidationRequest._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("password", "password", "_password", str, "", PredefinedSerializer()),
  FieldMetadata("captcha", "captcha", "_captcha", str, "", PredefinedSerializer()),
]

RegistrationValidationResponse._fields = [
  FieldMetadata("errors", "errors", "_errors", RegistrationError, [], ListSerializer(KaggleObjectSerializer())),
]

ReportContentRequest._fields = [
  FieldMetadata("authorUserName", "author_user_name", "_author_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("authorUserId", "author_user_id", "_author_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("explanation", "explanation", "_explanation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("messageId", "message_id", "_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("profileUserId", "profile_user_id", "_profile_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("policyViolationId", "policy_violation_id", "_policy_violation_id", PolicyViolationId, PolicyViolationId.POLICY_VIOLATION_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("groupId", "group_id", "_group_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("writeUpMessageId", "write_up_message_id", "_write_up_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkIdentifier", "benchmark_identifier", "_benchmark_identifier", BenchmarkIdentifier, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("benchmarkTaskIdentifier", "benchmark_task_identifier", "_benchmark_task_identifier", TaskIdentifier, None, KaggleObjectSerializer(), optional=True),
]

ResendVerificationEmailRequest._fields = [
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, None, PredefinedSerializer(), optional=True),
]

ResetPasswordRequest._fields = [
  FieldMetadata("returnUrl", "return_url", "_return_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("newPassword", "new_password", "_new_password", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resetPasswordCode", "reset_password_code", "_reset_password_code", str, None, PredefinedSerializer(), optional=True),
]

ResetPasswordResponse._fields = [
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
]

SignOutRequest._fields = []

SoftDeleteAccountRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
]

SoftDeleteAccountResponse._fields = [
  FieldMetadata("userSoftDeleted", "user_soft_deleted", "_user_soft_deleted", bool, False, PredefinedSerializer()),
]

StartMigrateSsoRequest._fields = [
  FieldMetadata("email", "email", "_email", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, None, PredefinedSerializer(), optional=True),
]

StartMigrateSsoResponse._fields = [
  FieldMetadata("outcome", "outcome", "_outcome", StartMigrateSsoOutcome, StartMigrateSsoOutcome.GOOGLE_SSO_EXISTS, EnumSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

StartPhoneVerificationRequest._fields = [
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, "", PredefinedSerializer()),
  FieldMetadata("captchaResponse", "captcha_response", "_captcha_response", str, "", PredefinedSerializer()),
  FieldMetadata("redirectUrl", "redirect_url", "_redirect_url", str, "", PredefinedSerializer()),
]

StartPhoneVerificationResponse._fields = [
  FieldMetadata("phoneVerified", "phone_verified", "_phone_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("redirectUrl", "redirect_url", "_redirect_url", str, "", PredefinedSerializer()),
  FieldMetadata("fallbackToIdentityVerification", "fallback_to_identity_verification", "_fallback_to_identity_verification", bool, False, PredefinedSerializer()),
]

StartResetPasswordRequest._fields = [
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, None, PredefinedSerializer(), optional=True),
]

SupportPhoneInfo._fields = [
  FieldMetadata("countryCode", "country_code", "_country_code", str, "", PredefinedSerializer()),
  FieldMetadata("countryName", "country_name", "_country_name", str, "", PredefinedSerializer()),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, "", PredefinedSerializer()),
  FieldMetadata("supportHoursDescription", "support_hours_description", "_support_hours_description", str, "", PredefinedSerializer()),
]

SupportRequestStatistics._fields = [
  FieldMetadata("count", "count", "_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countByReason", "count_by_reason", "_count_by_reason", int, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("countByRegion", "count_by_region", "_count_by_region", int, {}, MapSerializer(PredefinedSerializer())),
]

TakeoutUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("takeoutType", "takeout_type", "_takeout_type", TakeoutType, TakeoutType.TAKEOUT_TYPE_UNSPECIFIED, EnumSerializer()),
]

TakeoutUserResponse._fields = [
  FieldMetadata("readAccessUrl", "read_access_url", "_read_access_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("bucketUrl", "bucket_url", "_bucket_url", str, None, PredefinedSerializer(), optional=True),
]

ValidateResetPasswordCodeRequest._fields = [
  FieldMetadata("email", "email", "_email", str, "", PredefinedSerializer()),
  FieldMetadata("resetPasswordCode", "reset_password_code", "_reset_password_code", str, "", PredefinedSerializer()),
  FieldMetadata("resendIfExpired", "resend_if_expired", "_resend_if_expired", bool, False, PredefinedSerializer()),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, None, PredefinedSerializer(), optional=True),
]

ValidateResetPasswordCodeResponse._fields = [
  FieldMetadata("outcome", "outcome", "_outcome", ValidateResetPasswordCodeOutcome, ValidateResetPasswordCodeOutcome.VALIDATE_RESET_PASSWORD_CODE_OUTCOME_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

VerifyAccountEmailRequest._fields = [
  FieldMetadata("verificationCode", "verification_code", "_verification_code", str, "", PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
  FieldMetadata("registrationSessionId", "registration_session_id", "_registration_session_id", str, "", PredefinedSerializer()),
]

VerifyAccountEmailResponse._fields = [
  FieldMetadata("localReturnUrl", "local_return_url", "_local_return_url", str, "", PredefinedSerializer()),
]

VerifyPhoneDto._fields = [
  FieldMetadata("returnUrl", "return_url", "_return_url", str, "", PredefinedSerializer()),
  FieldMetadata("alreadySentCode", "already_sent_code", "_already_sent_code", bool, False, PredefinedSerializer()),
]

VerifyPhoneRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("forceVerify", "force_verify", "_force_verify", bool, False, PredefinedSerializer()),
]

