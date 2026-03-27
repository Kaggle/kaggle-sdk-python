import enum

class UserAchievementTier(enum.Enum):
  NOVICE = 0
  CONTRIBUTOR = 1
  EXPERT = 2
  MASTER = 3
  GRANDMASTER = 4
  STAFF = 5
  """Kaggle admins"""
  ORGANIZATION = 11
  """Organizations"""
  RECALC = 21
  """Flag user for tier recalculation"""

class UserVerificationStatus(enum.Enum):
  r"""
  Possible user-facing verification states for determining what actions to give
  them and copy to display.
  """
  USER_VERIFICATION_STATUS_UNSPECIFIED = 0
  """Enum default. Should not be used in practice."""
  USER_VERIFICATION_STATUS_UNVERIFIED = 1
  """The user has not started any verification."""
  USER_VERIFICATION_STATUS_IN_PROGRESS = 2
  """The user started verification but has not finished."""
  USER_VERIFICATION_STATUS_PROCESSING = 3
  """The user finished verification steps but is awaiting a result (edge case)."""
  USER_VERIFICATION_STATUS_VERIFIED = 4
  """The user has successfully verified."""
  USER_VERIFICATION_STATUS_FAILED = 5
  """Verification failed. The user should contact support."""

class CollaboratorType(enum.Enum):
  COLLABORATOR_TYPE_UNSPECIFIED = 0
  READER = 1
  WRITER = 2
  OWNER = 3
  ADMIN = 4

class KaggleXRole(enum.Enum):
  KAGGLE_X_ROLE_UNSPECIFIED = 0
  COHORT_3_MENTOR = 1
  COHORT_3_MENTEE = 2

class LoginMessageId(enum.Enum):
  r"""
  These aren't fully qualified because the transpilier is including the prefix
  on the enum value for some reason
  """
  LOGIN_MESSAGE_ID_UNSPECIFIED = 0
  UNKNOWN = 1
  LOCKED_OUT = 2
  INVALID_LOGIN = 3
  INVALID_GOOGLE_SSO = 4
  MISSING_LOGIN = 5
  DISABLED_LOGIN = 6
  INTERNAL_ERROR = 7
  BANNED_LOGIN = 8
  ALREADY_CONFIRMED = 9
  EXPIRED_CODE = 10
  GOOGLE_SSO_EMAIL_MISSING = 11
  GOOGLE_LINK_SUCCESS = 12
  GOOGLE_SSO_INACTIVE = 13
  ADMINS_USE_GOOGLE = 14
  ADMINS_USE_GOOGLE_EMAIL = 15
  DATASETS_WELCOME = 16
  CAPTCHA_MISSING = 17
  USERNAME_TAKEN = 18
  USERNAME_NUMBER = 19
  USERNAME_ALPHANUMERIC = 20
  USERNAME_MIN_LENGTH = 21
  USERNAME_MAX_LENGTH = 22
  FULL_NAME_LENGTH = 23
  EMAIL_EXISTS = 24
  EMAIL_LENGTH = 25
  INVALID_EMAIL = 26
  PASSWORD_TOO_SHORT = 27
  DATASETS_LOGIN = 28
  TOPIC_LOGIN = 29
  VOTE_LOGIN = 30
  CONTACT_USERS = 31
  USE_GOOGLE_SSO = 32
  MISSING_EMAIL = 33
  MISSING_USER_NAME = 34
  MISSING_DISPLAY_NAME = 35
  MISSING_PASSWORD = 36
  BOOKMARK_LOGIN = 37
  INVALID_CODE = 38
  CHANGE_EMAIL_VERIFY_LOGIN = 39
  FOLLOW_LOGIN = 40
  SUSPENDED_LOGIN = 41
  GOOGLE_SSO_EXISTING_ALIAS = 42
  DATASETS_REPORT_ISSUE_LOGIN = 43
  ADD_TO_COLLECTION_LOGIN = 44

class QuotaTier(enum.Enum):
  QUOTA_TIER_UNSPECIFIED = 0
  DEFAULT_TIER = 1
  HIGH_TIER = 2
  RESTRICTED_TIER = 3
  HACKATHON_TIER = 4
  OVERRIDE_TIER = 5

class RegistrationInfoFields(enum.Enum):
  REGISTRATION_INFO_FIELDS_UNSPECIFIED = 0
  REGISTRATION_INFO_FIELDS_USER_NAME = 1
  REGISTRATION_INFO_FIELDS_DISPLAY_NAME = 2
  REGISTRATION_INFO_FIELDS_EMAIL = 3
  REGISTRATION_INFO_FIELDS_PASSWORD = 4
  REGISTRATION_INFO_FIELDS_CAPTCHA = 5

class UserVerificationInquiryState(enum.Enum):
  r"""
  See go/kaggle-user-verification.
  Enum ordering matters because it matches the logical order of the state
  machine. In the event of a race with other state update events, earlier steps
  cannot overwrite later steps, unless updating to a decision state (approved /
  declined) or resuming an expired inquiry.
  """
  USER_VERIFICATION_INQUIRY_STATE_UNSPECIFIED = 0
  """Enum default. Should not be used in practice."""
  USER_VERIFICATION_INQUIRY_STATE_CREATED = 1
  """The Inquiry was created but the User hasn't started it yet."""
  USER_VERIFICATION_INQUIRY_STATE_PENDING = 2
  """The User started the Inquiry by submitting at least one verification."""
  USER_VERIFICATION_INQUIRY_STATE_EXPIRED = 3
  r"""
  The Inquiry was created but not finished within 24 hours. Can be resumed
  (up to a point).
  """
  USER_VERIFICATION_INQUIRY_STATE_COMPLETED = 4
  r"""
  The User successfully submitted and passed all verifications but hasn't
  received a decision yet.
  """
  USER_VERIFICATION_INQUIRY_STATE_APPROVED = 5
  r"""
  All verifications were submitted and passed, and the Inquiry has passed
  automated/manual review. OR, if this is a manual Inquiry, a Kaggle admin
  bypassed Persona to verify this User.
  """
  USER_VERIFICATION_INQUIRY_STATE_DECLINED = 6
  r"""
  Verifications failed and the user has exceeded the retry limit, or they
  were rejected from automated/manual review.
  """
  USER_VERIFICATION_INQUIRY_STATE_INVALIDATED = 7
  r"""
  Kaggle manually invalidated the Inquiry, requiring the User to re-verify
  from scratch.
  """

