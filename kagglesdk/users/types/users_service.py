from datetime import datetime
import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_enums import QuotaTier
from typing import List, Optional, Dict

class AttributeId(enum.Enum):
  ATTRIBUTE_ID_UNSPECIFIED = 0
  ATTRIBUTE_ID_NOTIFICATIONS_SUBSCRIBE_TO_KAGGLE_NEWSLETTER = 17
  ATTRIBUTE_ID_ADDRESS_COUNTRY = 18
  ATTRIBUTE_ID_ADDRESS_REGION = 19
  ATTRIBUTE_ID_ADDRESS_CITY = 20
  ATTRIBUTE_ID_WEBSITE = 26
  ATTRIBUTE_ID_LINKEDIN_URL = 27
  ATTRIBUTE_ID_TWITTER_USER_NAME = 28
  ATTRIBUTE_ID_GITHUB_USER_NAME = 29
  ATTRIBUTE_ID_BIO = 42
  ATTRIBUTE_ID_SPAMMY = 92
  ATTRIBUTE_ID_OCCUPATION = 96
  ATTRIBUTE_ID_ORGANIZATION = 97
  ATTRIBUTE_ID_DISCUSSION_SETTINGS = 102
  ATTRIBUTE_ID_NOTIFICATIONS_ENABLED = 109
  ATTRIBUTE_ID_NOTIFICATIONS_AT_MENTIONS_SETTING = 110
  ATTRIBUTE_ID_NOTIFICATIONS_BLOCK_COLLABORATION_EMAILS = 111
  ATTRIBUTE_ID_NOTIFICATIONS_DEFAULT_DELIVERY_SETTING = 113
  ATTRIBUTE_ID_NOTIFICATIONS_AGGREGATION_TYPE = 114
  ATTRIBUTE_ID_DISMISSABLE_BANNER_NEWSFEED = 115
  ATTRIBUTE_ID_KERNEL_EDITOR_NOTEBOOKS_DARK_MODE = 116
  ATTRIBUTE_ID_KERNEL_EDITOR_SCRIPTS_DARK_MODE = 117
  ATTRIBUTE_ID_HATS_LAST_DISMISSAL_DATE = 120
  ATTRIBUTE_ID_HATS_LAST_CLICK_DATE = 121
  ATTRIBUTE_ID_NOTIFICATIONS_NOTIFICATIONS_AT_MENTION_FOLLOWED_USER = 124
  ATTRIBUTE_ID_NOTIFICATIONS_NOTIFICATIONS_AT_MENTION_REGULAR_USER = 125
  ATTRIBUTE_ID_NOTIFICATIONS_COMPETITION_ANNOUNCEMENTS = 128
  ATTRIBUTE_ID_NOTIFICATIONS_COMPETITION_TEAM_UPDATES = 129
  ATTRIBUTE_ID_NOTIFICATIONS_ENGAGED_TOPIC_COMMENT = 130
  ATTRIBUTE_ID_NOTIFICATIONS_DATASET_ALERTS = 131
  ATTRIBUTE_ID_DATA_SCIENCE_AND_MACHINE_LEARNING_SURVEY_2020_INTERACTION = 132
  ATTRIBUTE_ID_REGISTRATION_RETURN_URL = 133
  ATTRIBUTE_ID_TAG_COMMUNITY_FILTER = 134
  ATTRIBUTE_ID_NOTIFICATIONS_NOTEBOOK_ALERTS = 136
  ATTRIBUTE_ID_BOOKMARKS_COMPETITIONS_MIGRATED = 137
  ATTRIBUTE_ID_BOOKMARKS_DATASETS_MIGRATED = 138
  ATTRIBUTE_ID_BOOKMARKS_FORUM_TOPICS_MIGRATED = 139
  ATTRIBUTE_ID_BOOKMARKS_KERNELS_MIGRATED = 140
  ATTRIBUTE_ID_EMAIL_NUDGES_DISABLED = 141
  ATTRIBUTE_ID_EMPLOYER_NUDGES_DISABLED = 142
  ATTRIBUTE_ID_GOOGLE_ML_SUMMIT_2021_INTERACTION = 143
  ATTRIBUTE_ID_REGISTRATION_NEWS_EMAIL_SIGNUP_WAS_OPT_OUT = 144
  ATTRIBUTE_ID_NOTIFICATIONS_USER_NEW_FOLLOWER = 145
  ATTRIBUTE_ID_DS_SURVEY_2021_BANNER_LAST_CLICK_DATE = 146
  ATTRIBUTE_ID_DS_SURVEY_2021_BANNER_LAST_DISMISSAL_DATE = 147
  ATTRIBUTE_ID_DS_SURVEY_2021_NUDGE_LAST_CLICK_DATE = 148
  ATTRIBUTE_ID_DS_SURVEY_2021_NUDGE_LAST_DISMISSAL_DATE = 149
  ATTRIBUTE_ID_MODERATION_REPORTED_BANNER_DISMISSED_KERNEL_IDS = 150
  ATTRIBUTE_ID_MODERATION_REPORTED_BANNER_DISMISSED_DATASET_IDS = 151
  ATTRIBUTE_ID_MODERATION_REPORTED_MODAL_DISMISSED_KERNEL_IDS = 152
  ATTRIBUTE_ID_MODERATION_REPORTED_MODAL_DISMISSED_DATASET_IDS = 153
  ATTRIBUTE_ID_HOMEPAGE_ONBOARDING_DISMISSED = 154
  ATTRIBUTE_ID_CUSTOM_NUDGES_DISABLED = 155
  ATTRIBUTE_ID_IMAGE_UPLOAD_WARNING_DISMISSED = 156
  ATTRIBUTE_ID_HOMEPAGE_STATS_DISMISSED = 157
  ATTRIBUTE_ID_REGISTRATION_ND4C_COUNTRY = 158
  r"""
  The user's country code during registration, if they are in an ND4C
  applicable country. Used by welcome email.
  """
  ATTRIBUTE_ID_TAGLINE = 159
  ATTRIBUTE_ID_DATASET_FEEDBACKS_NUDGES_DISABLED = 160
  """Whether the user should be shown dataset feedbacks nudges."""
  ATTRIBUTE_ID_PRONOUNS = 161
  ATTRIBUTE_ID_USER_EMOJI_SKIN_TONE = 162
  ATTRIBUTE_ID_KAGGLE_X_ROLE = 163
  """The KaggleX role (mentor, mentee)"""
  ATTRIBUTE_ID_NOTIFICATIONS_ORGANIZATION_ALERTS = 164
  ATTRIBUTE_ID_THEME = 165
  ATTRIBUTE_ID_NOTIFICATIONS_DATASET_SUGGESTION_REVIEWED = 166
  ATTRIBUTE_ID_ORGANIZATION_OVERVIEW = 167
  ATTRIBUTE_ID_LEGACY_ORGANIZATION_APPROVAL = 168
  """Indicates whether a legacy organization has been approved"""
  ATTRIBUTE_ID_PROFILE_VISIBILITY_SETTINGS = 169
  """Controls visibility of profile sections"""
  ATTRIBUTE_ID_NOTIFICATIONS_GROUPS = 170
  ATTRIBUTE_ID_NOTIFICATIONS_SHARED_RESOURCES = 171
  ATTRIBUTE_ID_PROGRESSION_OPT_OUT = 172
  ATTRIBUTE_ID_LOCATION_SHARING_OPT_OUT = 173
  ATTRIBUTE_ID_HIDDEN_COMPETITION_IDS = 174
  ATTRIBUTE_ID_KERNEL_FORK_VOTE_OPT_OUT = 175
  r"""
  Controls whether or not votes are given to the original notebook when a
  fork action is taken.
  """
  ATTRIBUTE_ID_KERNEL_FORK_VOTE_SNACKBAR_OPT_OUT = 176
  r"""
  Controls whether or not informational snackbar / toast should be shown on
  forked kernels after a vote has been given to the fork parent.
  """
  ATTRIBUTE_ID_PROFILE_SECTION_ORDER = 177
  """Controls the order of sections on the About tab of the user profile"""
  ATTRIBUTE_ID_TEST_RUN_ID = 178
  """Stores the test run ID for ephemeral test accounts created by e2e tests"""
  ATTRIBUTE_ID_NOTIFICATIONS_BENCHMARK_ALERTS = 179
  """How to receive notifications about benchmarks you subscribe to"""
  ATTRIBUTE_ID_NOTIFICATIONS_BENCHMARK_RUN_ALERTS = 180
  """How to receive notifications about benchmark runs you own"""
  ATTRIBUTE_ID_NOTIFICATIONS_NEW_MODEL_ALERTS = 181
  """How to receive notifications about new models on benchmarks you subscribe to"""

class ContactUserInfoError(enum.Enum):
  CONTACT_USER_INFO_ERROR_UNSPECIFIED = 0
  CONTACT_USER_INFO_QUOTA_REACHED = 2
  CONTACT_USER_INFO_NOT_PHONE_VERIFIED = 3

class HomepageStatsDismissedState(enum.Enum):
  DEFAULT = 0
  DISMISSED = 1
  DISPLAYED = 2

class Theme(enum.Enum):
  THEME_UNSPECIFIED = 0
  THEME_LIGHT = 1
  THEME_DARK = 2
  THEME_DEVICE = 3

class AcceptCookiesRequest(KaggleObject):
  r"""
  """

  pass

class ActivateAccountRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    reason (str)
    verification_code (str)
  """

  def __init__(self):
    self._user_id = 0
    self._reason = None
    self._verification_code = None
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
  def reason(self) -> str:
    return self._reason or ""

  @reason.setter
  def reason(self, reason: Optional[str]):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason

  @property
  def verification_code(self) -> str:
    return self._verification_code or ""

  @verification_code.setter
  def verification_code(self, verification_code: Optional[str]):
    if verification_code is None:
      del self.verification_code
      return
    if not isinstance(verification_code, str):
      raise TypeError('verification_code must be of type str')
    self._verification_code = verification_code


class AttributeValue(KaggleObject):
  r"""
  Attributes:
    attribute_id (AttributeId)
      The attribute ID for the corresponding value
    value (str)
      The value for this attribute
  """

  def __init__(self):
    self._attribute_id = AttributeId.ATTRIBUTE_ID_UNSPECIFIED
    self._value = None
    self._freeze()

  @property
  def attribute_id(self) -> 'AttributeId':
    """The attribute ID for the corresponding value"""
    return self._attribute_id

  @attribute_id.setter
  def attribute_id(self, attribute_id: 'AttributeId'):
    if attribute_id is None:
      del self.attribute_id
      return
    if not isinstance(attribute_id, AttributeId):
      raise TypeError('attribute_id must be of type AttributeId')
    self._attribute_id = attribute_id

  @property
  def value(self) -> str:
    """The value for this attribute"""
    return self._value or ""

  @value.setter
  def value(self, value: Optional[str]):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class CreateUserMessageRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user to send a message to.
    subject (str)
      The subject of the message.
    body (str)
      The body of the message. Text only (no markdown/html).
  """

  def __init__(self):
    self._user_id = 0
    self._subject = ""
    self._body = ""
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user to send a message to."""
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
  def subject(self) -> str:
    """The subject of the message."""
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
    """The body of the message. Text only (no markdown/html)."""
    return self._body

  @body.setter
  def body(self, body: str):
    if body is None:
      del self.body
      return
    if not isinstance(body, str):
      raise TypeError('body must be of type str')
    self._body = body


class CreateUserMessageResponse(KaggleObject):
  r"""
  """

  pass

class DeletePhoneVerificationsRequest(KaggleObject):
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


class FollowUserRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The username of the user to follow
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    """The username of the user to follow"""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class FollowUserResponse(KaggleObject):
  r"""
  """

  pass

class GetClientFeatureFlagsRequest(KaggleObject):
  r"""
  Attributes:
    expected_hash (str)
      Optional hash to validate against. If the hash matches the current feature
      flags state, an empty response with only the hash is returned to save
      bandwidth.
  """

  def __init__(self):
    self._expected_hash = None
    self._freeze()

  @property
  def expected_hash(self) -> str:
    r"""
    Optional hash to validate against. If the hash matches the current feature
    flags state, an empty response with only the hash is returned to save
    bandwidth.
    """
    return self._expected_hash or ""

  @expected_hash.setter
  def expected_hash(self, expected_hash: Optional[str]):
    if expected_hash is None:
      del self.expected_hash
      return
    if not isinstance(expected_hash, str):
      raise TypeError('expected_hash must be of type str')
    self._expected_hash = expected_hash


class GetClientFeatureFlagsResponse(KaggleObject):
  r"""
  Attributes:
    hash (str)
      A hash of the feature flags state. This is used by the frontend to cache
      feature flags and detect when they need to be re-fetched.
    feature_flags (str)
      List of boolean feature flags that the user can see.
    feature_flag_values (str)
      Map of value-based feature flags.
  """

  def __init__(self):
    self._hash = ""
    self._feature_flags = []
    self._feature_flag_values = {}
    self._freeze()

  @property
  def hash(self) -> str:
    r"""
    A hash of the feature flags state. This is used by the frontend to cache
    feature flags and detect when they need to be re-fetched.
    """
    return self._hash

  @hash.setter
  def hash(self, hash: str):
    if hash is None:
      del self.hash
      return
    if not isinstance(hash, str):
      raise TypeError('hash must be of type str')
    self._hash = hash

  @property
  def feature_flags(self) -> Optional[List[str]]:
    """List of boolean feature flags that the user can see."""
    return self._feature_flags

  @feature_flags.setter
  def feature_flags(self, feature_flags: Optional[List[str]]):
    if feature_flags is None:
      del self.feature_flags
      return
    if not isinstance(feature_flags, list):
      raise TypeError('feature_flags must be of type list')
    if not all([isinstance(t, str) for t in feature_flags]):
      raise TypeError('feature_flags must contain only items of type str')
    self._feature_flags = feature_flags

  @property
  def feature_flag_values(self) -> Optional[Dict[str, str]]:
    """Map of value-based feature flags."""
    return self._feature_flag_values

  @feature_flag_values.setter
  def feature_flag_values(self, feature_flag_values: Optional[Dict[str, str]]):
    if feature_flag_values is None:
      del self.feature_flag_values
      return
    if not isinstance(feature_flag_values, dict):
      raise TypeError('feature_flag_values must be of type dict')
    if not all([isinstance(v, str) for k, v in feature_flag_values]):
      raise TypeError('feature_flag_values must contain only items of type str')
    self._feature_flag_values = feature_flag_values


class GetContactUserInfoRequest(KaggleObject):
  r"""
  """

  pass

class GetContactUserInfoResponse(KaggleObject):
  r"""
  Attributes:
    can_send (bool)
    emails_remaining (int)
    error (ContactUserInfoError)
  """

  def __init__(self):
    self._can_send = False
    self._emails_remaining = 0
    self._error = ContactUserInfoError.CONTACT_USER_INFO_ERROR_UNSPECIFIED
    self._freeze()

  @property
  def can_send(self) -> bool:
    return self._can_send

  @can_send.setter
  def can_send(self, can_send: bool):
    if can_send is None:
      del self.can_send
      return
    if not isinstance(can_send, bool):
      raise TypeError('can_send must be of type bool')
    self._can_send = can_send

  @property
  def emails_remaining(self) -> int:
    return self._emails_remaining

  @emails_remaining.setter
  def emails_remaining(self, emails_remaining: int):
    if emails_remaining is None:
      del self.emails_remaining
      return
    if not isinstance(emails_remaining, int):
      raise TypeError('emails_remaining must be of type int')
    self._emails_remaining = emails_remaining

  @property
  def error(self) -> 'ContactUserInfoError':
    return self._error

  @error.setter
  def error(self, error: 'ContactUserInfoError'):
    if error is None:
      del self.error
      return
    if not isinstance(error, ContactUserInfoError):
      raise TypeError('error must be of type ContactUserInfoError')
    self._error = error


class GetCurrentUserIdRequest(KaggleObject):
  r"""
  """

  pass

class GetCurrentUserIdResponse(KaggleObject):
  r"""
  Attributes:
    current_user_id (int)
      Id of the current user, or null if the user isn't logged in.
  """

  def __init__(self):
    self._current_user_id = None
    self._freeze()

  @property
  def current_user_id(self) -> int:
    """Id of the current user, or null if the user isn't logged in."""
    return self._current_user_id or 0

  @current_user_id.setter
  def current_user_id(self, current_user_id: Optional[int]):
    if current_user_id is None:
      del self.current_user_id
      return
    if not isinstance(current_user_id, int):
      raise TypeError('current_user_id must be of type int')
    self._current_user_id = current_user_id


class GetCurrentUserRequest(KaggleObject):
  r"""
  Attributes:
    include_groups (bool)
      Whether to also load the groups the user is a part of.
    include_logins (bool)
      Whether to also load the logins of the user. Defaults to false since it is
      not useful in most cases and can be expensive.
    include_verification_status (bool)
      Whether to also load the user's identity verification status. Defaults to
      false since it is not useful in most cases and requires an additional join.
  """

  def __init__(self):
    self._include_groups = False
    self._include_logins = False
    self._include_verification_status = False
    self._freeze()

  @property
  def include_groups(self) -> bool:
    """Whether to also load the groups the user is a part of."""
    return self._include_groups

  @include_groups.setter
  def include_groups(self, include_groups: bool):
    if include_groups is None:
      del self.include_groups
      return
    if not isinstance(include_groups, bool):
      raise TypeError('include_groups must be of type bool')
    self._include_groups = include_groups

  @property
  def include_logins(self) -> bool:
    r"""
    Whether to also load the logins of the user. Defaults to false since it is
    not useful in most cases and can be expensive.
    """
    return self._include_logins

  @include_logins.setter
  def include_logins(self, include_logins: bool):
    if include_logins is None:
      del self.include_logins
      return
    if not isinstance(include_logins, bool):
      raise TypeError('include_logins must be of type bool')
    self._include_logins = include_logins

  @property
  def include_verification_status(self) -> bool:
    r"""
    Whether to also load the user's identity verification status. Defaults to
    false since it is not useful in most cases and requires an additional join.
    """
    return self._include_verification_status

  @include_verification_status.setter
  def include_verification_status(self, include_verification_status: bool):
    if include_verification_status is None:
      del self.include_verification_status
      return
    if not isinstance(include_verification_status, bool):
      raise TypeError('include_verification_status must be of type bool')
    self._include_verification_status = include_verification_status


class GetCurrentUserThemeRequest(KaggleObject):
  r"""
  """

  pass

class GetCurrentUserThemeResponse(KaggleObject):
  r"""
  Attributes:
    theme (Theme)
  """

  def __init__(self):
    self._theme = Theme.THEME_UNSPECIFIED
    self._freeze()

  @property
  def theme(self) -> 'Theme':
    return self._theme

  @theme.setter
  def theme(self, theme: 'Theme'):
    if theme is None:
      del self.theme
      return
    if not isinstance(theme, Theme):
      raise TypeError('theme must be of type Theme')
    self._theme = theme


class GetHomepageStatsDismissedStatusRequest(KaggleObject):
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


class GetHomepageStatsDismissedStatusResponse(KaggleObject):
  r"""
  Attributes:
    state (HomepageStatsDismissedState)
  """

  def __init__(self):
    self._state = HomepageStatsDismissedState.DEFAULT
    self._freeze()

  @property
  def state(self) -> 'HomepageStatsDismissedState':
    return self._state

  @state.setter
  def state(self, state: 'HomepageStatsDismissedState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, HomepageStatsDismissedState):
      raise TypeError('state must be of type HomepageStatsDismissedState')
    self._state = state


class GetMyAttributesRequest(KaggleObject):
  r"""
  Attributes:
    attributes (AttributeId)
  """

  def __init__(self):
    self._attributes = []
    self._freeze()

  @property
  def attributes(self) -> Optional[List['AttributeId']]:
    return self._attributes

  @attributes.setter
  def attributes(self, attributes: Optional[List['AttributeId']]):
    if attributes is None:
      del self.attributes
      return
    if not isinstance(attributes, list):
      raise TypeError('attributes must be of type list')
    if not all([isinstance(t, AttributeId) for t in attributes]):
      raise TypeError('attributes must contain only items of type AttributeId')
    self._attributes = attributes


class GetMyAttributesResponse(KaggleObject):
  r"""
  Attributes:
    attributes (str)
  """

  def __init__(self):
    self._attributes = []
    self._freeze()

  @property
  def attributes(self) -> Optional[List[str]]:
    return self._attributes

  @attributes.setter
  def attributes(self, attributes: Optional[List[str]]):
    if attributes is None:
      del self.attributes
      return
    if not isinstance(attributes, list):
      raise TypeError('attributes must be of type list')
    if not all([isinstance(t, str) for t in attributes]):
      raise TypeError('attributes must contain only items of type str')
    self._attributes = attributes


class GetOnboardingDismissedStatusRequest(KaggleObject):
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


class GetOnboardingDismissedStatusResponse(KaggleObject):
  r"""
  Attributes:
    is_dismissed (bool)
  """

  def __init__(self):
    self._is_dismissed = False
    self._freeze()

  @property
  def is_dismissed(self) -> bool:
    return self._is_dismissed

  @is_dismissed.setter
  def is_dismissed(self, is_dismissed: bool):
    if is_dismissed is None:
      del self.is_dismissed
      return
    if not isinstance(is_dismissed, bool):
      raise TypeError('is_dismissed must be of type bool')
    self._is_dismissed = is_dismissed


class GetUploadWarningDismissedRequest(KaggleObject):
  r"""
  """

  pass

class GetUploadWarningDismissedResponse(KaggleObject):
  r"""
  Attributes:
    is_dismissed (bool)
  """

  def __init__(self):
    self._is_dismissed = False
    self._freeze()

  @property
  def is_dismissed(self) -> bool:
    return self._is_dismissed

  @is_dismissed.setter
  def is_dismissed(self, is_dismissed: bool):
    if is_dismissed is None:
      del self.is_dismissed
      return
    if not isinstance(is_dismissed, bool):
      raise TypeError('is_dismissed must be of type bool')
    self._is_dismissed = is_dismissed


class GetUserAvatarRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User to retrieve information about.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """User to retrieve information about."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserCountRequest(KaggleObject):
  r"""
  """

  pass

class GetUserCountResponse(KaggleObject):
  r"""
  Attributes:
    user_count (int)
  """

  def __init__(self):
    self._user_count = 0
    self._freeze()

  @property
  def user_count(self) -> int:
    return self._user_count

  @user_count.setter
  def user_count(self, user_count: int):
    if user_count is None:
      del self.user_count
      return
    if not isinstance(user_count, int):
      raise TypeError('user_count must be of type int')
    self._user_count = user_count


class GetUserEmojiSkinToneRequest(KaggleObject):
  r"""
  """

  pass

class GetUserEmojiSkinToneResponse(KaggleObject):
  r"""
  Attributes:
    skin_tone (int)
  """

  def __init__(self):
    self._skin_tone = 0
    self._freeze()

  @property
  def skin_tone(self) -> int:
    return self._skin_tone

  @skin_tone.setter
  def skin_tone(self, skin_tone: int):
    if skin_tone is None:
      del self.skin_tone
      return
    if not isinstance(skin_tone, int):
      raise TypeError('skin_tone must be of type int')
    self._skin_tone = skin_tone


class GetUserRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      User to retrieve information about.
    read_mask (FieldMask)
      Which fields to retrieve (to avoid loading unnecessary fields).
  """

  def __init__(self):
    self._user_id = None
    self._read_mask = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """User to retrieve information about."""
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
  def read_mask(self) -> FieldMask:
    """Which fields to retrieve (to avoid loading unnecessary fields)."""
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class MigrateTermsAcceptancesRequest(KaggleObject):
  r"""
  Attributes:
    date (datetime)
    page_size (int)
    pages_to_retrieve_per_run (int)
  """

  def __init__(self):
    self._date = None
    self._page_size = 0
    self._pages_to_retrieve_per_run = 0
    self._freeze()

  @property
  def date(self) -> datetime:
    return self._date

  @date.setter
  def date(self, date: datetime):
    if date is None:
      del self.date
      return
    if not isinstance(date, datetime):
      raise TypeError('date must be of type datetime')
    self._date = date

  @property
  def page_size(self) -> int:
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
  def pages_to_retrieve_per_run(self) -> int:
    return self._pages_to_retrieve_per_run

  @pages_to_retrieve_per_run.setter
  def pages_to_retrieve_per_run(self, pages_to_retrieve_per_run: int):
    if pages_to_retrieve_per_run is None:
      del self.pages_to_retrieve_per_run
      return
    if not isinstance(pages_to_retrieve_per_run, int):
      raise TypeError('pages_to_retrieve_per_run must be of type int')
    self._pages_to_retrieve_per_run = pages_to_retrieve_per_run


class MigrateTermsAcceptancesResponse(KaggleObject):
  r"""
  Attributes:
    unsuccessful_migrations (int)
  """

  def __init__(self):
    self._unsuccessful_migrations = 0
    self._freeze()

  @property
  def unsuccessful_migrations(self) -> int:
    return self._unsuccessful_migrations

  @unsuccessful_migrations.setter
  def unsuccessful_migrations(self, unsuccessful_migrations: int):
    if unsuccessful_migrations is None:
      del self.unsuccessful_migrations
      return
    if not isinstance(unsuccessful_migrations, int):
      raise TypeError('unsuccessful_migrations must be of type int')
    self._unsuccessful_migrations = unsuccessful_migrations


class Place(KaggleObject):
  r"""
  Attributes:
    display_location (str)
    normalized_location (str)
  """

  def __init__(self):
    self._display_location = None
    self._normalized_location = None
    self._freeze()

  @property
  def display_location(self) -> str:
    return self._display_location or ""

  @display_location.setter
  def display_location(self, display_location: Optional[str]):
    if display_location is None:
      del self.display_location
      return
    if not isinstance(display_location, str):
      raise TypeError('display_location must be of type str')
    self._display_location = display_location

  @property
  def normalized_location(self) -> str:
    return self._normalized_location or ""

  @normalized_location.setter
  def normalized_location(self, normalized_location: Optional[str]):
    if normalized_location is None:
      del self.normalized_location
      return
    if not isinstance(normalized_location, str):
      raise TypeError('normalized_location must be of type str')
    self._normalized_location = normalized_location


class SearchOrganizationsRequest(KaggleObject):
  r"""
  Search for user attributes organization.

  Attributes:
    query (str)
  """

  def __init__(self):
    self._query = None
    self._freeze()

  @property
  def query(self) -> str:
    return self._query or ""

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query


class SearchOrganizationsResponse(KaggleObject):
  r"""
  Attributes:
    organizations (int)
  """

  def __init__(self):
    self._organizations = {}
    self._freeze()

  @property
  def organizations(self) -> Optional[Dict[str, int]]:
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[Dict[str, int]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, dict):
      raise TypeError('organizations must be of type dict')
    if not all([isinstance(v, int) for k, v in organizations]):
      raise TypeError('organizations must contain only items of type int')
    self._organizations = organizations


class SearchPlacesRequest(KaggleObject):
  r"""
  Attributes:
    input (str)
  """

  def __init__(self):
    self._input = None
    self._freeze()

  @property
  def input(self) -> str:
    return self._input or ""

  @input.setter
  def input(self, input: Optional[str]):
    if input is None:
      del self.input
      return
    if not isinstance(input, str):
      raise TypeError('input must be of type str')
    self._input = input


class SearchPlacesResponse(KaggleObject):
  r"""
  Attributes:
    places (Place)
  """

  def __init__(self):
    self._places = []
    self._freeze()

  @property
  def places(self) -> Optional[List[Optional['Place']]]:
    return self._places

  @places.setter
  def places(self, places: Optional[List[Optional['Place']]]):
    if places is None:
      del self.places
      return
    if not isinstance(places, list):
      raise TypeError('places must be of type list')
    if not all([isinstance(t, Place) for t in places]):
      raise TypeError('places must contain only items of type Place')
    self._places = places


class SearchUsersSuggestionsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    query (str)
    topic_id (int)
    competition_id (int)
    restrict_to_given_entity (bool)
  """

  def __init__(self):
    self._page_size = 0
    self._query = None
    self._topic_id = None
    self._competition_id = None
    self._restrict_to_given_entity = None
    self._freeze()

  @property
  def page_size(self) -> int:
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
  def query(self) -> str:
    return self._query or ""

  @query.setter
  def query(self, query: Optional[str]):
    if query is None:
      del self.query
      return
    if not isinstance(query, str):
      raise TypeError('query must be of type str')
    self._query = query

  @property
  def topic_id(self) -> int:
    return self._topic_id or 0

  @topic_id.setter
  def topic_id(self, topic_id: Optional[int]):
    if topic_id is None:
      del self.topic_id
      return
    if not isinstance(topic_id, int):
      raise TypeError('topic_id must be of type int')
    self._topic_id = topic_id

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def restrict_to_given_entity(self) -> bool:
    return self._restrict_to_given_entity or False

  @restrict_to_given_entity.setter
  def restrict_to_given_entity(self, restrict_to_given_entity: Optional[bool]):
    if restrict_to_given_entity is None:
      del self.restrict_to_given_entity
      return
    if not isinstance(restrict_to_given_entity, bool):
      raise TypeError('restrict_to_given_entity must be of type bool')
    self._restrict_to_given_entity = restrict_to_given_entity


class SearchUsersSuggestionsResponse(KaggleObject):
  r"""
  Attributes:
    users_suggestions (UserAvatar)
  """

  def __init__(self):
    self._users_suggestions = []
    self._freeze()

  @property
  def users_suggestions(self) -> Optional[List[Optional['UserAvatar']]]:
    return self._users_suggestions

  @users_suggestions.setter
  def users_suggestions(self, users_suggestions: Optional[List[Optional['UserAvatar']]]):
    if users_suggestions is None:
      del self.users_suggestions
      return
    if not isinstance(users_suggestions, list):
      raise TypeError('users_suggestions must be of type list')
    if not all([isinstance(t, UserAvatar) for t in users_suggestions]):
      raise TypeError('users_suggestions must contain only items of type UserAvatar')
    self._users_suggestions = users_suggestions


class SetMyAttributesRequest(KaggleObject):
  r"""
  Attributes:
    attributes (AttributeValue)
  """

  def __init__(self):
    self._attributes = []
    self._freeze()

  @property
  def attributes(self) -> Optional[List[Optional['AttributeValue']]]:
    return self._attributes

  @attributes.setter
  def attributes(self, attributes: Optional[List[Optional['AttributeValue']]]):
    if attributes is None:
      del self.attributes
      return
    if not isinstance(attributes, list):
      raise TypeError('attributes must be of type list')
    if not all([isinstance(t, AttributeValue) for t in attributes]):
      raise TypeError('attributes must contain only items of type AttributeValue')
    self._attributes = attributes


class SetPhoneReputableRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    phone_number (str)
    force (bool)
  """

  def __init__(self):
    self._user_id = 0
    self._phone_number = None
    self._force = False
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
  def force(self) -> bool:
    return self._force

  @force.setter
  def force(self, force: bool):
    if force is None:
      del self.force
      return
    if not isinstance(force, bool):
      raise TypeError('force must be of type bool')
    self._force = force


class SetUploadWarningDismissedRequest(KaggleObject):
  r"""
  """

  pass

class UnfollowUserRequest(KaggleObject):
  r"""
  Attributes:
    user_name (str)
      The username of the user to unfollow
  """

  def __init__(self):
    self._user_name = ""
    self._freeze()

  @property
  def user_name(self) -> str:
    """The username of the user to unfollow"""
    return self._user_name

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    self._user_name = user_name


class UnfollowUserResponse(KaggleObject):
  r"""
  """

  pass

class UnsubscribeNewsletterRequest(KaggleObject):
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


class UpdateCurrentUserThemeRequest(KaggleObject):
  r"""
  Attributes:
    theme (Theme)
  """

  def __init__(self):
    self._theme = Theme.THEME_UNSPECIFIED
    self._freeze()

  @property
  def theme(self) -> 'Theme':
    return self._theme

  @theme.setter
  def theme(self, theme: 'Theme'):
    if theme is None:
      del self.theme
      return
    if not isinstance(theme, Theme):
      raise TypeError('theme must be of type Theme')
    self._theme = theme


class UpdateHomepageStatsDismissedStatusRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    state (HomepageStatsDismissedState)
  """

  def __init__(self):
    self._user_id = 0
    self._state = HomepageStatsDismissedState.DEFAULT
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
  def state(self) -> 'HomepageStatsDismissedState':
    return self._state

  @state.setter
  def state(self, state: 'HomepageStatsDismissedState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, HomepageStatsDismissedState):
      raise TypeError('state must be of type HomepageStatsDismissedState')
    self._state = state


class UpdateOnboardingDismissedStatusRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    is_dismissed (bool)
  """

  def __init__(self):
    self._user_id = 0
    self._is_dismissed = False
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
  def is_dismissed(self) -> bool:
    return self._is_dismissed

  @is_dismissed.setter
  def is_dismissed(self, is_dismissed: bool):
    if is_dismissed is None:
      del self.is_dismissed
      return
    if not isinstance(is_dismissed, bool):
      raise TypeError('is_dismissed must be of type bool')
    self._is_dismissed = is_dismissed


class UpdateUserEmojiSkinToneRequest(KaggleObject):
  r"""
  Attributes:
    skin_tone (int)
  """

  def __init__(self):
    self._skin_tone = 0
    self._freeze()

  @property
  def skin_tone(self) -> int:
    return self._skin_tone

  @skin_tone.setter
  def skin_tone(self, skin_tone: int):
    if skin_tone is None:
      del self.skin_tone
      return
    if not isinstance(skin_tone, int):
      raise TypeError('skin_tone must be of type int')
    self._skin_tone = skin_tone


class UpdateUsersModelProxyQuotaGroupRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
    quota_tier (QuotaTier)
  """

  def __init__(self):
    self._user_ids = []
    self._quota_tier = QuotaTier.QUOTA_TIER_UNSPECIFIED
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
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
  def quota_tier(self) -> 'QuotaTier':
    return self._quota_tier

  @quota_tier.setter
  def quota_tier(self, quota_tier: 'QuotaTier'):
    if quota_tier is None:
      del self.quota_tier
      return
    if not isinstance(quota_tier, QuotaTier):
      raise TypeError('quota_tier must be of type QuotaTier')
    self._quota_tier = quota_tier


class UpdateUsersModelProxyQuotaGroupResponse(KaggleObject):
  r"""
  Attributes:
    user_results (UserResult)
  """

  def __init__(self):
    self._user_results = []
    self._freeze()

  @property
  def user_results(self) -> Optional[List[Optional['UserResult']]]:
    return self._user_results

  @user_results.setter
  def user_results(self, user_results: Optional[List[Optional['UserResult']]]):
    if user_results is None:
      del self.user_results
      return
    if not isinstance(user_results, list):
      raise TypeError('user_results must be of type list')
    if not all([isinstance(t, UserResult) for t in user_results]):
      raise TypeError('user_results must contain only items of type UserResult')
    self._user_results = user_results


class UserResult(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    already_in_tier (bool)
    sent_email (bool)
    added_to_tier (QuotaTier)
    removed_from_tier (QuotaTier)
  """

  def __init__(self):
    self._user_id = 0
    self._already_in_tier = False
    self._sent_email = False
    self._added_to_tier = None
    self._removed_from_tier = None
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
  def already_in_tier(self) -> bool:
    return self._already_in_tier

  @already_in_tier.setter
  def already_in_tier(self, already_in_tier: bool):
    if already_in_tier is None:
      del self.already_in_tier
      return
    if not isinstance(already_in_tier, bool):
      raise TypeError('already_in_tier must be of type bool')
    self._already_in_tier = already_in_tier

  @property
  def sent_email(self) -> bool:
    return self._sent_email

  @sent_email.setter
  def sent_email(self, sent_email: bool):
    if sent_email is None:
      del self.sent_email
      return
    if not isinstance(sent_email, bool):
      raise TypeError('sent_email must be of type bool')
    self._sent_email = sent_email

  @property
  def added_to_tier(self) -> 'QuotaTier':
    return self._added_to_tier or QuotaTier.QUOTA_TIER_UNSPECIFIED

  @added_to_tier.setter
  def added_to_tier(self, added_to_tier: Optional['QuotaTier']):
    if added_to_tier is None:
      del self.added_to_tier
      return
    if not isinstance(added_to_tier, QuotaTier):
      raise TypeError('added_to_tier must be of type QuotaTier')
    self._added_to_tier = added_to_tier

  @property
  def removed_from_tier(self) -> 'QuotaTier':
    return self._removed_from_tier or QuotaTier.QUOTA_TIER_UNSPECIFIED

  @removed_from_tier.setter
  def removed_from_tier(self, removed_from_tier: Optional['QuotaTier']):
    if removed_from_tier is None:
      del self.removed_from_tier
      return
    if not isinstance(removed_from_tier, QuotaTier):
      raise TypeError('removed_from_tier must be of type QuotaTier')
    self._removed_from_tier = removed_from_tier


AcceptCookiesRequest._fields = []

ActivateAccountRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verificationCode", "verification_code", "_verification_code", str, None, PredefinedSerializer(), optional=True),
]

AttributeValue._fields = [
  FieldMetadata("attributeId", "attribute_id", "_attribute_id", AttributeId, AttributeId.ATTRIBUTE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("value", "value", "_value", str, None, PredefinedSerializer(), optional=True),
]

CreateUserMessageRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("subject", "subject", "_subject", str, "", PredefinedSerializer()),
  FieldMetadata("body", "body", "_body", str, "", PredefinedSerializer()),
]

CreateUserMessageResponse._fields = []

DeletePhoneVerificationsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

FollowUserRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

FollowUserResponse._fields = []

GetClientFeatureFlagsRequest._fields = [
  FieldMetadata("expectedHash", "expected_hash", "_expected_hash", str, None, PredefinedSerializer(), optional=True),
]

GetClientFeatureFlagsResponse._fields = [
  FieldMetadata("hash", "hash", "_hash", str, "", PredefinedSerializer()),
  FieldMetadata("featureFlags", "feature_flags", "_feature_flags", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("featureFlagValues", "feature_flag_values", "_feature_flag_values", str, {}, MapSerializer(PredefinedSerializer())),
]

GetContactUserInfoRequest._fields = []

GetContactUserInfoResponse._fields = [
  FieldMetadata("canSend", "can_send", "_can_send", bool, False, PredefinedSerializer()),
  FieldMetadata("emailsRemaining", "emails_remaining", "_emails_remaining", int, 0, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", ContactUserInfoError, ContactUserInfoError.CONTACT_USER_INFO_ERROR_UNSPECIFIED, EnumSerializer()),
]

GetCurrentUserIdRequest._fields = []

GetCurrentUserIdResponse._fields = [
  FieldMetadata("currentUserId", "current_user_id", "_current_user_id", int, None, PredefinedSerializer(), optional=True),
]

GetCurrentUserRequest._fields = [
  FieldMetadata("includeGroups", "include_groups", "_include_groups", bool, False, PredefinedSerializer()),
  FieldMetadata("includeLogins", "include_logins", "_include_logins", bool, False, PredefinedSerializer()),
  FieldMetadata("includeVerificationStatus", "include_verification_status", "_include_verification_status", bool, False, PredefinedSerializer()),
]

GetCurrentUserThemeRequest._fields = []

GetCurrentUserThemeResponse._fields = [
  FieldMetadata("theme", "theme", "_theme", Theme, Theme.THEME_UNSPECIFIED, EnumSerializer()),
]

GetHomepageStatsDismissedStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetHomepageStatsDismissedStatusResponse._fields = [
  FieldMetadata("state", "state", "_state", HomepageStatsDismissedState, HomepageStatsDismissedState.DEFAULT, EnumSerializer()),
]

GetMyAttributesRequest._fields = [
  FieldMetadata("attributes", "attributes", "_attributes", AttributeId, [], ListSerializer(EnumSerializer())),
]

GetMyAttributesResponse._fields = [
  FieldMetadata("attributes", "attributes", "_attributes", str, [], ListSerializer(PredefinedSerializer())),
]

GetOnboardingDismissedStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetOnboardingDismissedStatusResponse._fields = [
  FieldMetadata("isDismissed", "is_dismissed", "_is_dismissed", bool, False, PredefinedSerializer()),
]

GetUploadWarningDismissedRequest._fields = []

GetUploadWarningDismissedResponse._fields = [
  FieldMetadata("isDismissed", "is_dismissed", "_is_dismissed", bool, False, PredefinedSerializer()),
]

GetUserAvatarRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserCountRequest._fields = []

GetUserCountResponse._fields = [
  FieldMetadata("userCount", "user_count", "_user_count", int, 0, PredefinedSerializer()),
]

GetUserEmojiSkinToneRequest._fields = []

GetUserEmojiSkinToneResponse._fields = [
  FieldMetadata("skinTone", "skin_tone", "_skin_tone", int, 0, PredefinedSerializer()),
]

GetUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

MigrateTermsAcceptancesRequest._fields = [
  FieldMetadata("date", "date", "_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pagesToRetrievePerRun", "pages_to_retrieve_per_run", "_pages_to_retrieve_per_run", int, 0, PredefinedSerializer()),
]

MigrateTermsAcceptancesResponse._fields = [
  FieldMetadata("unsuccessfulMigrations", "unsuccessful_migrations", "_unsuccessful_migrations", int, 0, PredefinedSerializer()),
]

Place._fields = [
  FieldMetadata("displayLocation", "display_location", "_display_location", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("normalizedLocation", "normalized_location", "_normalized_location", str, None, PredefinedSerializer(), optional=True),
]

SearchOrganizationsRequest._fields = [
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
]

SearchOrganizationsResponse._fields = [
  FieldMetadata("organizations", "organizations", "_organizations", int, {}, MapSerializer(PredefinedSerializer())),
]

SearchPlacesRequest._fields = [
  FieldMetadata("input", "input", "_input", str, None, PredefinedSerializer(), optional=True),
]

SearchPlacesResponse._fields = [
  FieldMetadata("places", "places", "_places", Place, [], ListSerializer(KaggleObjectSerializer())),
]

SearchUsersSuggestionsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("query", "query", "_query", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("topicId", "topic_id", "_topic_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("restrictToGivenEntity", "restrict_to_given_entity", "_restrict_to_given_entity", bool, None, PredefinedSerializer(), optional=True),
]

SearchUsersSuggestionsResponse._fields = [
  FieldMetadata("usersSuggestions", "users_suggestions", "_users_suggestions", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
]

SetMyAttributesRequest._fields = [
  FieldMetadata("attributes", "attributes", "_attributes", AttributeValue, [], ListSerializer(KaggleObjectSerializer())),
]

SetPhoneReputableRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("force", "force", "_force", bool, False, PredefinedSerializer()),
]

SetUploadWarningDismissedRequest._fields = []

UnfollowUserRequest._fields = [
  FieldMetadata("userName", "user_name", "_user_name", str, "", PredefinedSerializer()),
]

UnfollowUserResponse._fields = []

UnsubscribeNewsletterRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

UpdateCurrentUserThemeRequest._fields = [
  FieldMetadata("theme", "theme", "_theme", Theme, Theme.THEME_UNSPECIFIED, EnumSerializer()),
]

UpdateHomepageStatsDismissedStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", HomepageStatsDismissedState, HomepageStatsDismissedState.DEFAULT, EnumSerializer()),
]

UpdateOnboardingDismissedStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isDismissed", "is_dismissed", "_is_dismissed", bool, False, PredefinedSerializer()),
]

UpdateUserEmojiSkinToneRequest._fields = [
  FieldMetadata("skinTone", "skin_tone", "_skin_tone", int, 0, PredefinedSerializer()),
]

UpdateUsersModelProxyQuotaGroupRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("quotaTier", "quota_tier", "_quota_tier", QuotaTier, QuotaTier.QUOTA_TIER_UNSPECIFIED, EnumSerializer()),
]

UpdateUsersModelProxyQuotaGroupResponse._fields = [
  FieldMetadata("userResults", "user_results", "_user_results", UserResult, [], ListSerializer(KaggleObjectSerializer())),
]

UserResult._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("alreadyInTier", "already_in_tier", "_already_in_tier", bool, False, PredefinedSerializer()),
  FieldMetadata("sentEmail", "sent_email", "_sent_email", bool, False, PredefinedSerializer()),
  FieldMetadata("addedToTier", "added_to_tier", "_added_to_tier", QuotaTier, None, EnumSerializer(), optional=True),
  FieldMetadata("removedFromTier", "removed_from_tier", "_removed_from_tier", QuotaTier, None, EnumSerializer(), optional=True),
]

