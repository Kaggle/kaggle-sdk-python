from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.support import SupportRequest
from kagglesdk.users.types.users_enums import UserVerificationInquiryState, UserVerificationStatus
from typing import Optional, List, Dict

class PhoneVerificationResult(enum.Enum):
  PHONE_VERIFICATION_RESULT_UNSPECIFIED = 0
  PHONE_VERIFICATION_RESULT_SUCCESS = 1
  PHONE_VERIFICATION_RESULT_SERVICE_UNAVAILABLE = 2
  PHONE_VERIFICATION_RESULT_INVALID_ARGUMENT = 3
  PHONE_VERIFICATION_RESULT_INVALID_RECAPTCHA_TOKEN = 4
  PHONE_VERIFICATION_RESULT_RECAPTCHA_PHONE_RISK_SCORE_TOO_HIGH = 5
  PHONE_VERIFICATION_RESULT_PERMISSION_DENIED = 6
  PHONE_VERIFICATION_RESULT_ALREADY_VERIFIED = 7
  PHONE_VERIFICATION_RESULT_EMAIL_DENYLISTED = 8
  PHONE_VERIFICATION_RESULT_OUT_OF_REGION = 9
  PHONE_VERIFICATION_RESULT_TOO_MANY_REQUESTS = 10
  PHONE_VERIFICATION_RESULT_NOT_REPUTABLE = 11
  PHONE_VERIFICATION_RESULT_NOT_REPUTABLE_ENOUGH_FOR_EMAIL_DOMAIN = 12
  PHONE_VERIFICATION_RESULT_TOO_MANY_DISTINCT_PHONE_NUMBERS = 13
  PHONE_VERIFICATION_RESULT_TOO_MANY_ATTEMPTS_WITH_THE_SAME_NUMBER = 14
  PHONE_VERIFICATION_RESULT_SANCTIONED_REGION = 15
  PHONE_VERIFICATION_RESULT_DUPLICATE_PHONE_NUMBER = 16
  PHONE_VERIFICATION_RESULT_PROVIDER_ERROR = 17
  PHONE_VERIFICATION_RESULT_INTERNAL_ERROR = 18
  PHONE_VERIFICATION_RESULT_MANUAL = 19
  PHONE_VERIFICATION_RESULT_EMAIL_UNTRUSTED = 20

class VerificationMethod(enum.Enum):
  VERIFICATION_METHOD_UNSPECIFIED = 0
  VERIFICATION_METHOD_IDENTITY = 1
  VERIFICATION_METHOD_PHONE = 2

class GetUserVerificationRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      Target user id to retrieve verification information.
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """Target user id to retrieve verification information."""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserVerificationResponse(KaggleObject):
  r"""
  Attributes:
    score (float)
      A user verification score on a scale from 0 - 1.0, where:
      - 0 is 'definitely a bad actor', ex: confirmed bot account
      - 0.5 is neutral / unknown. ex: new users without suspicious traits.
      - 1.0 is 'definitely a good actor', ex: GM verified with Persona

      When making decisions about score, prefer to use UserVerificationHelper's
      convenience methods with abstractions over direct comparisons to the score.

      Scores are updated in a scheduled handler:
      SyncUserVerificationScoresHandler Some users may not have a score if they
      are inactive or new.
    is_legacy_contributor (bool)
      Do not use for new logic. True if the user meets the requirements of the
      legacy Contributor tier, i.e. Has run 1 notebook / script, made 1
      competition submission, posted 1 comment, and given 1 upvote.
    is_phone_verified (bool)
      True if the user has successfully verified their phone number.
    is_identity_verified (bool)
      True if the user has successfully verified their identity..
  """

  def __init__(self):
    self._score = None
    self._is_legacy_contributor = False
    self._is_phone_verified = False
    self._is_identity_verified = False
    self._freeze()

  @property
  def score(self) -> float:
    r"""
    A user verification score on a scale from 0 - 1.0, where:
    - 0 is 'definitely a bad actor', ex: confirmed bot account
    - 0.5 is neutral / unknown. ex: new users without suspicious traits.
    - 1.0 is 'definitely a good actor', ex: GM verified with Persona

    When making decisions about score, prefer to use UserVerificationHelper's
    convenience methods with abstractions over direct comparisons to the score.

    Scores are updated in a scheduled handler:
    SyncUserVerificationScoresHandler Some users may not have a score if they
    are inactive or new.
    """
    return self._score or 0.0

  @score.setter
  def score(self, score: Optional[float]):
    if score is None:
      del self.score
      return
    if not isinstance(score, float):
      raise TypeError('score must be of type float')
    self._score = score

  @property
  def is_legacy_contributor(self) -> bool:
    r"""
    Do not use for new logic. True if the user meets the requirements of the
    legacy Contributor tier, i.e. Has run 1 notebook / script, made 1
    competition submission, posted 1 comment, and given 1 upvote.
    """
    return self._is_legacy_contributor

  @is_legacy_contributor.setter
  def is_legacy_contributor(self, is_legacy_contributor: bool):
    if is_legacy_contributor is None:
      del self.is_legacy_contributor
      return
    if not isinstance(is_legacy_contributor, bool):
      raise TypeError('is_legacy_contributor must be of type bool')
    self._is_legacy_contributor = is_legacy_contributor

  @property
  def is_phone_verified(self) -> bool:
    """True if the user has successfully verified their phone number."""
    return self._is_phone_verified

  @is_phone_verified.setter
  def is_phone_verified(self, is_phone_verified: bool):
    if is_phone_verified is None:
      del self.is_phone_verified
      return
    if not isinstance(is_phone_verified, bool):
      raise TypeError('is_phone_verified must be of type bool')
    self._is_phone_verified = is_phone_verified

  @property
  def is_identity_verified(self) -> bool:
    """True if the user has successfully verified their identity.."""
    return self._is_identity_verified

  @is_identity_verified.setter
  def is_identity_verified(self, is_identity_verified: bool):
    if is_identity_verified is None:
      del self.is_identity_verified
      return
    if not isinstance(is_identity_verified, bool):
      raise TypeError('is_identity_verified must be of type bool')
    self._is_identity_verified = is_identity_verified


class GetVerificationStatusRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    method (VerificationMethod)
  """

  def __init__(self):
    self._user_id = 0
    self._method = VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED
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
  def method(self) -> 'VerificationMethod':
    return self._method

  @method.setter
  def method(self, method: 'VerificationMethod'):
    if method is None:
      del self.method
      return
    if not isinstance(method, VerificationMethod):
      raise TypeError('method must be of type VerificationMethod')
    self._method = method


class GetVerificationStatusResponse(KaggleObject):
  r"""
  Attributes:
    status (UserVerificationStatus)
    is_fallback_from_phone_verification (bool)
      Whether this is an identity verification done instead of phone verification
      due to phone region restrictions.
  """

  def __init__(self):
    self._status = UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED
    self._is_fallback_from_phone_verification = False
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
  def is_fallback_from_phone_verification(self) -> bool:
    r"""
    Whether this is an identity verification done instead of phone verification
    due to phone region restrictions.
    """
    return self._is_fallback_from_phone_verification

  @is_fallback_from_phone_verification.setter
  def is_fallback_from_phone_verification(self, is_fallback_from_phone_verification: bool):
    if is_fallback_from_phone_verification is None:
      del self.is_fallback_from_phone_verification
      return
    if not isinstance(is_fallback_from_phone_verification, bool):
      raise TypeError('is_fallback_from_phone_verification must be of type bool')
    self._is_fallback_from_phone_verification = is_fallback_from_phone_verification


class InvalidateUserVerificationInquiriesRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    method (VerificationMethod)
  """

  def __init__(self):
    self._user_id = 0
    self._method = VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED
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
  def method(self) -> 'VerificationMethod':
    return self._method

  @method.setter
  def method(self, method: 'VerificationMethod'):
    if method is None:
      del self.method
      return
    if not isinstance(method, VerificationMethod):
      raise TypeError('method must be of type VerificationMethod')
    self._method = method


class ListPhoneVerificationsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user id to list phone verifications for.
    phone_number (str)
      The phone number to filter by.
    region_code (str)
      The region code to filter by.
    region_tier (int)
      The region tier to filter by (see http://go/sms-tiers).
    states (UserVerificationInquiryState)
      The state of the inquiry to filter by.
    results (PhoneVerificationResult)
      The result of the inquiry to filter by.
    start_time (datetime)
      Inclusive start time for phone verifications. If not specified, lists all
      recent phone verifications.
    end_time (datetime)
      Inclusive end time for phone verifications. If not specified, lists all
      recent phone verifications.
    page_size (int)
      Number of phone verifications to return. If not specified, returns 200
      phone verifications.
    page_token (str)
      Token to retrieve the next page of results (see
      ListPhoneVerificationsResponse.next_page_token).
  """

  def __init__(self):
    self._user_id = None
    self._phone_number = None
    self._region_code = None
    self._region_tier = None
    self._states = []
    self._results = []
    self._start_time = None
    self._end_time = None
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user id to list phone verifications for."""
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
  def phone_number(self) -> str:
    """The phone number to filter by."""
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
  def region_code(self) -> str:
    """The region code to filter by."""
    return self._region_code or ""

  @region_code.setter
  def region_code(self, region_code: Optional[str]):
    if region_code is None:
      del self.region_code
      return
    if not isinstance(region_code, str):
      raise TypeError('region_code must be of type str')
    self._region_code = region_code

  @property
  def region_tier(self) -> int:
    """The region tier to filter by (see http://go/sms-tiers)."""
    return self._region_tier or 0

  @region_tier.setter
  def region_tier(self, region_tier: Optional[int]):
    if region_tier is None:
      del self.region_tier
      return
    if not isinstance(region_tier, int):
      raise TypeError('region_tier must be of type int')
    self._region_tier = region_tier

  @property
  def states(self) -> Optional[List['UserVerificationInquiryState']]:
    """The state of the inquiry to filter by."""
    return self._states

  @states.setter
  def states(self, states: Optional[List['UserVerificationInquiryState']]):
    if states is None:
      del self.states
      return
    if not isinstance(states, list):
      raise TypeError('states must be of type list')
    if not all([isinstance(t, UserVerificationInquiryState) for t in states]):
      raise TypeError('states must contain only items of type UserVerificationInquiryState')
    self._states = states

  @property
  def results(self) -> Optional[List['PhoneVerificationResult']]:
    """The result of the inquiry to filter by."""
    return self._results

  @results.setter
  def results(self, results: Optional[List['PhoneVerificationResult']]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, PhoneVerificationResult) for t in results]):
      raise TypeError('results must contain only items of type PhoneVerificationResult')
    self._results = results

  @property
  def start_time(self) -> datetime:
    r"""
    Inclusive start time for phone verifications. If not specified, lists all
    recent phone verifications.
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
    Inclusive end time for phone verifications. If not specified, lists all
    recent phone verifications.
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

  @property
  def page_size(self) -> int:
    r"""
    Number of phone verifications to return. If not specified, returns 200
    phone verifications.
    """
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
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
    ListPhoneVerificationsResponse.next_page_token).
    """
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListPhoneVerificationsResponse(KaggleObject):
  r"""
  Attributes:
    phone_verifications (PhoneVerification)
    statistics (PhoneVerificationStatistics)
      Statistics about the phone verifications.
    next_page_token (str)
      Token to retrieve the next page of results (see
      ListPhoneVerificationsRequest.page_token).
  """

  def __init__(self):
    self._phone_verifications = []
    self._statistics = None
    self._next_page_token = None
    self._freeze()

  @property
  def phone_verifications(self) -> Optional[List[Optional['PhoneVerification']]]:
    return self._phone_verifications

  @phone_verifications.setter
  def phone_verifications(self, phone_verifications: Optional[List[Optional['PhoneVerification']]]):
    if phone_verifications is None:
      del self.phone_verifications
      return
    if not isinstance(phone_verifications, list):
      raise TypeError('phone_verifications must be of type list')
    if not all([isinstance(t, PhoneVerification) for t in phone_verifications]):
      raise TypeError('phone_verifications must contain only items of type PhoneVerification')
    self._phone_verifications = phone_verifications

  @property
  def statistics(self) -> Optional['PhoneVerificationStatistics']:
    """Statistics about the phone verifications."""
    return self._statistics

  @statistics.setter
  def statistics(self, statistics: Optional['PhoneVerificationStatistics']):
    if statistics is None:
      del self.statistics
      return
    if not isinstance(statistics, PhoneVerificationStatistics):
      raise TypeError('statistics must be of type PhoneVerificationStatistics')
    self._statistics = statistics

  @property
  def next_page_token(self) -> str:
    r"""
    Token to retrieve the next page of results (see
    ListPhoneVerificationsRequest.page_token).
    """
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ListUserVerificationInquiriesRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The user id to list verifications for.
    verification_method (VerificationMethod)
      The verification method to filter by.
    states (UserVerificationInquiryState)
      The state of the inquiry to filter by.
    start_time (datetime)
      Inclusive start time for verifications. If not specified, lists all
      recent verifications.
    end_time (datetime)
      Inclusive end time for verifications. If not specified, lists all
      recent verifications.
    page_size (int)
      Number of verifications to return. If not specified, returns 200
      verifications.
    page_token (str)
      Token to retrieve the next page of results (see
      ListUserVerificationInquiriesResponse.next_page_token).
  """

  def __init__(self):
    self._user_id = None
    self._verification_method = None
    self._states = []
    self._start_time = None
    self._end_time = None
    self._page_size = None
    self._page_token = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The user id to list verifications for."""
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
  def verification_method(self) -> 'VerificationMethod':
    """The verification method to filter by."""
    return self._verification_method or VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED

  @verification_method.setter
  def verification_method(self, verification_method: Optional['VerificationMethod']):
    if verification_method is None:
      del self.verification_method
      return
    if not isinstance(verification_method, VerificationMethod):
      raise TypeError('verification_method must be of type VerificationMethod')
    self._verification_method = verification_method

  @property
  def states(self) -> Optional[List['UserVerificationInquiryState']]:
    """The state of the inquiry to filter by."""
    return self._states

  @states.setter
  def states(self, states: Optional[List['UserVerificationInquiryState']]):
    if states is None:
      del self.states
      return
    if not isinstance(states, list):
      raise TypeError('states must be of type list')
    if not all([isinstance(t, UserVerificationInquiryState) for t in states]):
      raise TypeError('states must contain only items of type UserVerificationInquiryState')
    self._states = states

  @property
  def start_time(self) -> datetime:
    r"""
    Inclusive start time for verifications. If not specified, lists all
    recent verifications.
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
    Inclusive end time for verifications. If not specified, lists all
    recent verifications.
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

  @property
  def page_size(self) -> int:
    r"""
    Number of verifications to return. If not specified, returns 200
    verifications.
    """
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
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
    ListUserVerificationInquiriesResponse.next_page_token).
    """
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token


class ListUserVerificationInquiriesResponse(KaggleObject):
  r"""
  Attributes:
    user_verification_inquiries (UserVerificationInquiry)
    statistics (UserVerificationInquiryStatistics)
      Statistics about the verifications.
    next_page_token (str)
      Token to retrieve the next page of results (see
      ListUserVerificationInquiriesRequest.page_token).
  """

  def __init__(self):
    self._user_verification_inquiries = []
    self._statistics = None
    self._next_page_token = None
    self._freeze()

  @property
  def user_verification_inquiries(self) -> Optional[List[Optional['UserVerificationInquiry']]]:
    return self._user_verification_inquiries

  @user_verification_inquiries.setter
  def user_verification_inquiries(self, user_verification_inquiries: Optional[List[Optional['UserVerificationInquiry']]]):
    if user_verification_inquiries is None:
      del self.user_verification_inquiries
      return
    if not isinstance(user_verification_inquiries, list):
      raise TypeError('user_verification_inquiries must be of type list')
    if not all([isinstance(t, UserVerificationInquiry) for t in user_verification_inquiries]):
      raise TypeError('user_verification_inquiries must contain only items of type UserVerificationInquiry')
    self._user_verification_inquiries = user_verification_inquiries

  @property
  def statistics(self) -> Optional['UserVerificationInquiryStatistics']:
    """Statistics about the verifications."""
    return self._statistics

  @statistics.setter
  def statistics(self, statistics: Optional['UserVerificationInquiryStatistics']):
    if statistics is None:
      del self.statistics
      return
    if not isinstance(statistics, UserVerificationInquiryStatistics):
      raise TypeError('statistics must be of type UserVerificationInquiryStatistics')
    self._statistics = statistics

  @property
  def next_page_token(self) -> str:
    r"""
    Token to retrieve the next page of results (see
    ListUserVerificationInquiriesRequest.page_token).
    """
    return self._next_page_token or ""

  @next_page_token.setter
  def next_page_token(self, next_page_token: Optional[str]):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token


class ManuallyVerifyUserRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    method (VerificationMethod)
  """

  def __init__(self):
    self._user_id = 0
    self._method = VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED
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
  def method(self) -> 'VerificationMethod':
    return self._method

  @method.setter
  def method(self, method: 'VerificationMethod'):
    if method is None:
      del self.method
      return
    if not isinstance(method, VerificationMethod):
      raise TypeError('method must be of type VerificationMethod')
    self._method = method


class PhoneVerification(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the phone verification.
    user_id (int)
      The user that is verified.
    phone_number (str)
      The phone number that is verified.
    region_code (str)
      The region code of the phone number.
    region_name (str)
      The region name of the phone number.
    region_tier (int)
      The region tier of the phone number (see http://go/sms-tiers)
    create_time (datetime)
      The time when the phone verification was created.
    verify_time (datetime)
      The time when the phone number was verified.
    comments (str)
      Comments about the phone verification if it failed.
    result (PhoneVerificationResult)
      The result of the phone verification.
    inquiry (UserVerificationInquiry)
      User inquiry that this phone verification is associated with.
    support_requests (SupportRequest)
      Any recent phone verification related support requests filed by the user.
  """

  def __init__(self):
    self._id = 0
    self._user_id = 0
    self._phone_number = ""
    self._region_code = None
    self._region_name = None
    self._region_tier = None
    self._create_time = None
    self._verify_time = None
    self._comments = None
    self._result = None
    self._inquiry = None
    self._support_requests = []
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the phone verification."""
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
    """The user that is verified."""
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
    """The phone number that is verified."""
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
  def region_code(self) -> str:
    """The region code of the phone number."""
    return self._region_code or ""

  @region_code.setter
  def region_code(self, region_code: Optional[str]):
    if region_code is None:
      del self.region_code
      return
    if not isinstance(region_code, str):
      raise TypeError('region_code must be of type str')
    self._region_code = region_code

  @property
  def region_name(self) -> str:
    """The region name of the phone number."""
    return self._region_name or ""

  @region_name.setter
  def region_name(self, region_name: Optional[str]):
    if region_name is None:
      del self.region_name
      return
    if not isinstance(region_name, str):
      raise TypeError('region_name must be of type str')
    self._region_name = region_name

  @property
  def region_tier(self) -> int:
    """The region tier of the phone number (see http://go/sms-tiers)"""
    return self._region_tier or 0

  @region_tier.setter
  def region_tier(self, region_tier: Optional[int]):
    if region_tier is None:
      del self.region_tier
      return
    if not isinstance(region_tier, int):
      raise TypeError('region_tier must be of type int')
    self._region_tier = region_tier

  @property
  def create_time(self) -> datetime:
    """The time when the phone verification was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def verify_time(self) -> datetime:
    """The time when the phone number was verified."""
    return self._verify_time or None

  @verify_time.setter
  def verify_time(self, verify_time: Optional[datetime]):
    if verify_time is None:
      del self.verify_time
      return
    if not isinstance(verify_time, datetime):
      raise TypeError('verify_time must be of type datetime')
    self._verify_time = verify_time

  @property
  def comments(self) -> str:
    """Comments about the phone verification if it failed."""
    return self._comments or ""

  @comments.setter
  def comments(self, comments: Optional[str]):
    if comments is None:
      del self.comments
      return
    if not isinstance(comments, str):
      raise TypeError('comments must be of type str')
    self._comments = comments

  @property
  def result(self) -> 'PhoneVerificationResult':
    """The result of the phone verification."""
    return self._result or PhoneVerificationResult.PHONE_VERIFICATION_RESULT_UNSPECIFIED

  @result.setter
  def result(self, result: Optional['PhoneVerificationResult']):
    if result is None:
      del self.result
      return
    if not isinstance(result, PhoneVerificationResult):
      raise TypeError('result must be of type PhoneVerificationResult')
    self._result = result

  @property
  def inquiry(self) -> Optional['UserVerificationInquiry']:
    """User inquiry that this phone verification is associated with."""
    return self._inquiry or None

  @inquiry.setter
  def inquiry(self, inquiry: Optional[Optional['UserVerificationInquiry']]):
    if inquiry is None:
      del self.inquiry
      return
    if not isinstance(inquiry, UserVerificationInquiry):
      raise TypeError('inquiry must be of type UserVerificationInquiry')
    self._inquiry = inquiry

  @property
  def support_requests(self) -> Optional[List[Optional['SupportRequest']]]:
    """Any recent phone verification related support requests filed by the user."""
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


class PhoneVerificationStatistics(KaggleObject):
  r"""
  Attributes:
    count (int)
      Number of phone verifications.
    count_by_region (int)
      Number of phone verifications by region.
    count_by_result (int)
      Number of phone verifications by result.
    count_by_inquiry_state (int)
      Number of phone verifications by state.
  """

  def __init__(self):
    self._count = None
    self._count_by_region = {}
    self._count_by_result = {}
    self._count_by_inquiry_state = {}
    self._freeze()

  @property
  def count(self) -> int:
    """Number of phone verifications."""
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
  def count_by_region(self) -> Optional[Dict[str, int]]:
    """Number of phone verifications by region."""
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

  @property
  def count_by_result(self) -> Optional[Dict[str, int]]:
    """Number of phone verifications by result."""
    return self._count_by_result

  @count_by_result.setter
  def count_by_result(self, count_by_result: Optional[Dict[str, int]]):
    if count_by_result is None:
      del self.count_by_result
      return
    if not isinstance(count_by_result, dict):
      raise TypeError('count_by_result must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_result]):
      raise TypeError('count_by_result must contain only items of type int')
    self._count_by_result = count_by_result

  @property
  def count_by_inquiry_state(self) -> Optional[Dict[str, int]]:
    """Number of phone verifications by state."""
    return self._count_by_inquiry_state

  @count_by_inquiry_state.setter
  def count_by_inquiry_state(self, count_by_inquiry_state: Optional[Dict[str, int]]):
    if count_by_inquiry_state is None:
      del self.count_by_inquiry_state
      return
    if not isinstance(count_by_inquiry_state, dict):
      raise TypeError('count_by_inquiry_state must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_inquiry_state]):
      raise TypeError('count_by_inquiry_state must contain only items of type int')
    self._count_by_inquiry_state = count_by_inquiry_state


class RedactUserVerificationInquiriesRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    method (VerificationMethod)
  """

  def __init__(self):
    self._user_id = 0
    self._method = VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED
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
  def method(self) -> 'VerificationMethod':
    return self._method

  @method.setter
  def method(self, method: 'VerificationMethod'):
    if method is None:
      del self.method
      return
    if not isinstance(method, VerificationMethod):
      raise TypeError('method must be of type VerificationMethod')
    self._method = method


class UserVerificationInquiry(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the inquiry.
    user_id (int)
      The user that is verified.
    user_inquiries_link (str)
      Link to the user's inquiries in Persona
    inquiry_id (str)
      The Id of the inquiry in Persona's system.
    inquiry_link (str)
      Link to the inquiry in Persona
    persona_account_id (str)
      The User's account id with Persona.
    persona_account_link (str)
      Link to the User's account in Persona
    state (UserVerificationInquiryState)
      The state of the inquiry.
    create_time (datetime)
      Time when the row was inserted (automatically populated).
    verification_method (VerificationMethod)
      The verification method used: PHONE or IDENTITY.
    update_time (datetime)
      Time of the most recent State update.
    updated_by_user_id (int)
      The id of the admin user that updated the inquiry.
    support_requests (SupportRequest)
      Any recent identity verification related support requests filed by the
      user.
  """

  def __init__(self):
    self._id = 0
    self._user_id = 0
    self._user_inquiries_link = ""
    self._inquiry_id = ""
    self._inquiry_link = ""
    self._persona_account_id = ""
    self._persona_account_link = None
    self._state = UserVerificationInquiryState.USER_VERIFICATION_INQUIRY_STATE_UNSPECIFIED
    self._create_time = None
    self._verification_method = VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED
    self._update_time = None
    self._updated_by_user_id = None
    self._support_requests = []
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the inquiry."""
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
    """The user that is verified."""
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
  def user_inquiries_link(self) -> str:
    """Link to the user's inquiries in Persona"""
    return self._user_inquiries_link

  @user_inquiries_link.setter
  def user_inquiries_link(self, user_inquiries_link: str):
    if user_inquiries_link is None:
      del self.user_inquiries_link
      return
    if not isinstance(user_inquiries_link, str):
      raise TypeError('user_inquiries_link must be of type str')
    self._user_inquiries_link = user_inquiries_link

  @property
  def inquiry_id(self) -> str:
    """The Id of the inquiry in Persona's system."""
    return self._inquiry_id

  @inquiry_id.setter
  def inquiry_id(self, inquiry_id: str):
    if inquiry_id is None:
      del self.inquiry_id
      return
    if not isinstance(inquiry_id, str):
      raise TypeError('inquiry_id must be of type str')
    self._inquiry_id = inquiry_id

  @property
  def inquiry_link(self) -> str:
    """Link to the inquiry in Persona"""
    return self._inquiry_link

  @inquiry_link.setter
  def inquiry_link(self, inquiry_link: str):
    if inquiry_link is None:
      del self.inquiry_link
      return
    if not isinstance(inquiry_link, str):
      raise TypeError('inquiry_link must be of type str')
    self._inquiry_link = inquiry_link

  @property
  def persona_account_id(self) -> str:
    """The User's account id with Persona."""
    return self._persona_account_id

  @persona_account_id.setter
  def persona_account_id(self, persona_account_id: str):
    if persona_account_id is None:
      del self.persona_account_id
      return
    if not isinstance(persona_account_id, str):
      raise TypeError('persona_account_id must be of type str')
    self._persona_account_id = persona_account_id

  @property
  def persona_account_link(self) -> str:
    """Link to the User's account in Persona"""
    return self._persona_account_link or ""

  @persona_account_link.setter
  def persona_account_link(self, persona_account_link: Optional[str]):
    if persona_account_link is None:
      del self.persona_account_link
      return
    if not isinstance(persona_account_link, str):
      raise TypeError('persona_account_link must be of type str')
    self._persona_account_link = persona_account_link

  @property
  def state(self) -> 'UserVerificationInquiryState':
    """The state of the inquiry."""
    return self._state

  @state.setter
  def state(self, state: 'UserVerificationInquiryState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, UserVerificationInquiryState):
      raise TypeError('state must be of type UserVerificationInquiryState')
    self._state = state

  @property
  def create_time(self) -> datetime:
    """Time when the row was inserted (automatically populated)."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def verification_method(self) -> 'VerificationMethod':
    """The verification method used: PHONE or IDENTITY."""
    return self._verification_method

  @verification_method.setter
  def verification_method(self, verification_method: 'VerificationMethod'):
    if verification_method is None:
      del self.verification_method
      return
    if not isinstance(verification_method, VerificationMethod):
      raise TypeError('verification_method must be of type VerificationMethod')
    self._verification_method = verification_method

  @property
  def update_time(self) -> datetime:
    """Time of the most recent State update."""
    return self._update_time or None

  @update_time.setter
  def update_time(self, update_time: Optional[datetime]):
    if update_time is None:
      del self.update_time
      return
    if not isinstance(update_time, datetime):
      raise TypeError('update_time must be of type datetime')
    self._update_time = update_time

  @property
  def updated_by_user_id(self) -> int:
    """The id of the admin user that updated the inquiry."""
    return self._updated_by_user_id or 0

  @updated_by_user_id.setter
  def updated_by_user_id(self, updated_by_user_id: Optional[int]):
    if updated_by_user_id is None:
      del self.updated_by_user_id
      return
    if not isinstance(updated_by_user_id, int):
      raise TypeError('updated_by_user_id must be of type int')
    self._updated_by_user_id = updated_by_user_id

  @property
  def support_requests(self) -> Optional[List[Optional['SupportRequest']]]:
    r"""
    Any recent identity verification related support requests filed by the
    user.
    """
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


class UserVerificationInquiryStatistics(KaggleObject):
  r"""
  Attributes:
    count (int)
      Number of verifications.
    count_by_verification_method (int)
      Number of verifications by verification method.
    count_by_state (int)
      Number of verifications by state.
  """

  def __init__(self):
    self._count = None
    self._count_by_verification_method = {}
    self._count_by_state = {}
    self._freeze()

  @property
  def count(self) -> int:
    """Number of verifications."""
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
  def count_by_verification_method(self) -> Optional[Dict[str, int]]:
    """Number of verifications by verification method."""
    return self._count_by_verification_method

  @count_by_verification_method.setter
  def count_by_verification_method(self, count_by_verification_method: Optional[Dict[str, int]]):
    if count_by_verification_method is None:
      del self.count_by_verification_method
      return
    if not isinstance(count_by_verification_method, dict):
      raise TypeError('count_by_verification_method must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_verification_method]):
      raise TypeError('count_by_verification_method must contain only items of type int')
    self._count_by_verification_method = count_by_verification_method

  @property
  def count_by_state(self) -> Optional[Dict[str, int]]:
    """Number of verifications by state."""
    return self._count_by_state

  @count_by_state.setter
  def count_by_state(self, count_by_state: Optional[Dict[str, int]]):
    if count_by_state is None:
      del self.count_by_state
      return
    if not isinstance(count_by_state, dict):
      raise TypeError('count_by_state must be of type dict')
    if not all([isinstance(v, int) for k, v in count_by_state]):
      raise TypeError('count_by_state must contain only items of type int')
    self._count_by_state = count_by_state


GetUserVerificationRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserVerificationResponse._fields = [
  FieldMetadata("score", "score", "_score", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isLegacyContributor", "is_legacy_contributor", "_is_legacy_contributor", bool, False, PredefinedSerializer()),
  FieldMetadata("isPhoneVerified", "is_phone_verified", "_is_phone_verified", bool, False, PredefinedSerializer()),
  FieldMetadata("isIdentityVerified", "is_identity_verified", "_is_identity_verified", bool, False, PredefinedSerializer()),
]

GetVerificationStatusRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("method", "method", "_method", VerificationMethod, VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED, EnumSerializer()),
]

GetVerificationStatusResponse._fields = [
  FieldMetadata("status", "status", "_status", UserVerificationStatus, UserVerificationStatus.USER_VERIFICATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isFallbackFromPhoneVerification", "is_fallback_from_phone_verification", "_is_fallback_from_phone_verification", bool, False, PredefinedSerializer()),
]

InvalidateUserVerificationInquiriesRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("method", "method", "_method", VerificationMethod, VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED, EnumSerializer()),
]

ListPhoneVerificationsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regionCode", "region_code", "_region_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regionTier", "region_tier", "_region_tier", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("states", "states", "_states", UserVerificationInquiryState, [], ListSerializer(EnumSerializer())),
  FieldMetadata("results", "results", "_results", PhoneVerificationResult, [], ListSerializer(EnumSerializer())),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListPhoneVerificationsResponse._fields = [
  FieldMetadata("phoneVerifications", "phone_verifications", "_phone_verifications", PhoneVerification, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("statistics", "statistics", "_statistics", PhoneVerificationStatistics, None, KaggleObjectSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListUserVerificationInquiriesRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verificationMethod", "verification_method", "_verification_method", VerificationMethod, None, EnumSerializer(), optional=True),
  FieldMetadata("states", "states", "_states", UserVerificationInquiryState, [], ListSerializer(EnumSerializer())),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
]

ListUserVerificationInquiriesResponse._fields = [
  FieldMetadata("userVerificationInquiries", "user_verification_inquiries", "_user_verification_inquiries", UserVerificationInquiry, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("statistics", "statistics", "_statistics", UserVerificationInquiryStatistics, None, KaggleObjectSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, None, PredefinedSerializer(), optional=True),
]

ManuallyVerifyUserRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("method", "method", "_method", VerificationMethod, VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED, EnumSerializer()),
]

PhoneVerification._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("phoneNumber", "phone_number", "_phone_number", str, "", PredefinedSerializer()),
  FieldMetadata("regionCode", "region_code", "_region_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regionName", "region_name", "_region_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regionTier", "region_tier", "_region_tier", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("verifyTime", "verify_time", "_verify_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("comments", "comments", "_comments", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("result", "result", "_result", PhoneVerificationResult, None, EnumSerializer(), optional=True),
  FieldMetadata("inquiry", "inquiry", "_inquiry", UserVerificationInquiry, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("supportRequests", "support_requests", "_support_requests", SupportRequest, [], ListSerializer(KaggleObjectSerializer())),
]

PhoneVerificationStatistics._fields = [
  FieldMetadata("count", "count", "_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countByRegion", "count_by_region", "_count_by_region", int, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("countByResult", "count_by_result", "_count_by_result", int, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("countByInquiryState", "count_by_inquiry_state", "_count_by_inquiry_state", int, {}, MapSerializer(PredefinedSerializer())),
]

RedactUserVerificationInquiriesRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("method", "method", "_method", VerificationMethod, VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED, EnumSerializer()),
]

UserVerificationInquiry._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userInquiriesLink", "user_inquiries_link", "_user_inquiries_link", str, "", PredefinedSerializer()),
  FieldMetadata("inquiryId", "inquiry_id", "_inquiry_id", str, "", PredefinedSerializer()),
  FieldMetadata("inquiryLink", "inquiry_link", "_inquiry_link", str, "", PredefinedSerializer()),
  FieldMetadata("personaAccountId", "persona_account_id", "_persona_account_id", str, "", PredefinedSerializer()),
  FieldMetadata("personaAccountLink", "persona_account_link", "_persona_account_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("state", "state", "_state", UserVerificationInquiryState, UserVerificationInquiryState.USER_VERIFICATION_INQUIRY_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("verificationMethod", "verification_method", "_verification_method", VerificationMethod, VerificationMethod.VERIFICATION_METHOD_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("updateTime", "update_time", "_update_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("updatedByUserId", "updated_by_user_id", "_updated_by_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("supportRequests", "support_requests", "_support_requests", SupportRequest, [], ListSerializer(KaggleObjectSerializer())),
]

UserVerificationInquiryStatistics._fields = [
  FieldMetadata("count", "count", "_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("countByVerificationMethod", "count_by_verification_method", "_count_by_verification_method", int, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("countByState", "count_by_state", "_count_by_state", int, {}, MapSerializer(PredefinedSerializer())),
]

