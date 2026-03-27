from datetime import datetime
import enum
from kagglesdk.abuse.types.abuse_enums import PolicyViolationSource
from kagglesdk.common.types.common_types import KaggleEntityType
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.moderation_public_service import PolicyViolationId
from typing import List, Optional

class AppealReason(enum.Enum):
  APPEAL_REASON_UNSPECIFIED = 0
  MISTAKEN_JUDGEMENT = 1
  ISSUE_RECTIFIED = 2
  APPEAL_REASON_OTHER = 3

class ModerationEventType(enum.Enum):
  MODERATION_EVENT_TYPE_UNSPECIFIED = 0
  USER_PENALTY = 1
  MODERATION_LOG = 3
  REPORT_AGAINST_USER = 4
  REPORT_FROM_USER = 5
  APPEAL_FOR_USER_REPORT_NO_ACTION = 6
  """An appeal for Kaggle's decision not to take action on a user report"""
  APPEAL_FOR_CONTENT_MODERATION = 7

class ModerationVerdict(enum.Enum):
  MODERATION_VERDICT_UNSPECIFIED = 0
  PENDING = 1
  """The report/appeal hasn't been reviewed yet or is being considered"""
  APPROVED = 2
  """The report/appeal has been approved/upheld"""
  REJECTED = 3
  """The report/appeal has been rejected/overturned"""
  NO_DECISION = 4
  r"""
  The report/appeal is closed as no decision due to lack of user response or
  other reason(s)
  """
  PARTIALLY_APPROVED = 5
  """Partially approved"""

class Penalty(enum.Enum):
  NONE = 0
  WARNING = 1
  SUSPENSION = 2
  BAN = 3
  CONTENT_REMOVAL = 4

class PenaltySourceId(enum.Enum):
  PENALTY_SOURCE_ID_UNSPECIFIED = 0
  REPORTING_MECHANISMS = 1
  TRUSTED_FLAGGER = 2
  VOLUNTARY_INITIATIVE = 3
  ARTICLE_16_NOTICE = 4
  GOVERNMENT_REGULATORY_AUTHORITY = 5
  AUTOMATED_SYSTEMS = 6

class AppealReasonDescription(KaggleObject):
  r"""
  Attributes:
    id (int)
      The ID of the appeal reason
    description (str)
      The description of the appeal reason
  """

  def __init__(self):
    self._id = 0
    self._description = ""
    self._freeze()

  @property
  def id(self) -> int:
    """The ID of the appeal reason"""
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
  def description(self) -> str:
    """The description of the appeal reason"""
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description


class ApproveAppealRequest(KaggleObject):
  r"""
  Attributes:
    user_penalty_id (int)
      The ID of the user penalty being appealed
    reason_ids (int)
      The IDs of the reasons for the appeal approval
    notes (str)
      Additional notes provided for the appeal approval
  """

  def __init__(self):
    self._user_penalty_id = 0
    self._reason_ids = []
    self._notes = None
    self._freeze()

  @property
  def user_penalty_id(self) -> int:
    """The ID of the user penalty being appealed"""
    return self._user_penalty_id

  @user_penalty_id.setter
  def user_penalty_id(self, user_penalty_id: int):
    if user_penalty_id is None:
      del self.user_penalty_id
      return
    if not isinstance(user_penalty_id, int):
      raise TypeError('user_penalty_id must be of type int')
    self._user_penalty_id = user_penalty_id

  @property
  def reason_ids(self) -> Optional[List[int]]:
    """The IDs of the reasons for the appeal approval"""
    return self._reason_ids

  @reason_ids.setter
  def reason_ids(self, reason_ids: Optional[List[int]]):
    if reason_ids is None:
      del self.reason_ids
      return
    if not isinstance(reason_ids, list):
      raise TypeError('reason_ids must be of type list')
    if not all([isinstance(t, int) for t in reason_ids]):
      raise TypeError('reason_ids must contain only items of type int')
    self._reason_ids = reason_ids

  @property
  def notes(self) -> str:
    """Additional notes provided for the appeal approval"""
    return self._notes or ""

  @notes.setter
  def notes(self, notes: Optional[str]):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


class BulkUpdateResponse(KaggleObject):
  r"""
  Attributes:
    total (int)
      Count of users requested to be banned or unbanned
    count_successful (int)
      Count of users who were successfully banned or unbanned
    count_failed (int)
      Count of users who failed to be banned or unbanned
    count_ignored (int)
      Count of users who were already banned or unbanned
    elapsed_time_milliseconds (int)
      How much time in milliseconds it took to complete the request
    failures (FailureResult)
      Failure results by message
  """

  def __init__(self):
    self._total = 0
    self._count_successful = 0
    self._count_failed = 0
    self._count_ignored = 0
    self._elapsed_time_milliseconds = 0
    self._failures = []
    self._freeze()

  @property
  def total(self) -> int:
    """Count of users requested to be banned or unbanned"""
    return self._total

  @total.setter
  def total(self, total: int):
    if total is None:
      del self.total
      return
    if not isinstance(total, int):
      raise TypeError('total must be of type int')
    self._total = total

  @property
  def count_successful(self) -> int:
    """Count of users who were successfully banned or unbanned"""
    return self._count_successful

  @count_successful.setter
  def count_successful(self, count_successful: int):
    if count_successful is None:
      del self.count_successful
      return
    if not isinstance(count_successful, int):
      raise TypeError('count_successful must be of type int')
    self._count_successful = count_successful

  @property
  def count_failed(self) -> int:
    """Count of users who failed to be banned or unbanned"""
    return self._count_failed

  @count_failed.setter
  def count_failed(self, count_failed: int):
    if count_failed is None:
      del self.count_failed
      return
    if not isinstance(count_failed, int):
      raise TypeError('count_failed must be of type int')
    self._count_failed = count_failed

  @property
  def count_ignored(self) -> int:
    """Count of users who were already banned or unbanned"""
    return self._count_ignored

  @count_ignored.setter
  def count_ignored(self, count_ignored: int):
    if count_ignored is None:
      del self.count_ignored
      return
    if not isinstance(count_ignored, int):
      raise TypeError('count_ignored must be of type int')
    self._count_ignored = count_ignored

  @property
  def elapsed_time_milliseconds(self) -> int:
    """How much time in milliseconds it took to complete the request"""
    return self._elapsed_time_milliseconds

  @elapsed_time_milliseconds.setter
  def elapsed_time_milliseconds(self, elapsed_time_milliseconds: int):
    if elapsed_time_milliseconds is None:
      del self.elapsed_time_milliseconds
      return
    if not isinstance(elapsed_time_milliseconds, int):
      raise TypeError('elapsed_time_milliseconds must be of type int')
    self._elapsed_time_milliseconds = elapsed_time_milliseconds

  @property
  def failures(self) -> Optional[List[Optional['FailureResult']]]:
    """Failure results by message"""
    return self._failures

  @failures.setter
  def failures(self, failures: Optional[List[Optional['FailureResult']]]):
    if failures is None:
      del self.failures
      return
    if not isinstance(failures, list):
      raise TypeError('failures must be of type list')
    if not all([isinstance(t, FailureResult) for t in failures]):
      raise TypeError('failures must contain only items of type FailureResult')
    self._failures = failures


class FailureResult(KaggleObject):
  r"""
  Attributes:
    message (str)
      The message of the result
    user_count (int)
      The count of users that resulted in the message
    user_ids (int)
      The list of user IDs that resulted in the message
  """

  def __init__(self):
    self._message = ""
    self._user_count = 0
    self._user_ids = []
    self._freeze()

  @property
  def message(self) -> str:
    """The message of the result"""
    return self._message

  @message.setter
  def message(self, message: str):
    if message is None:
      del self.message
      return
    if not isinstance(message, str):
      raise TypeError('message must be of type str')
    self._message = message

  @property
  def user_count(self) -> int:
    """The count of users that resulted in the message"""
    return self._user_count

  @user_count.setter
  def user_count(self, user_count: int):
    if user_count is None:
      del self.user_count
      return
    if not isinstance(user_count, int):
      raise TypeError('user_count must be of type int')
    self._user_count = user_count

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The list of user IDs that resulted in the message"""
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


class ForceUpdateContentStatesRequest(KaggleObject):
  r"""
  Attributes:
    entity_type (KaggleEntityType)
      The entity type common for the entities having their content state updated.
    entity_ids (int)
      The ids of the entities having their content state updated.
    target_content_state (ContentState)
      The content state that the entities provided should be updated to.
    notes (str)
      Optional notes that will be included in the ContentStateLog.
  """

  def __init__(self):
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._entity_ids = []
    self._target_content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._notes = None
    self._freeze()

  @property
  def entity_type(self) -> 'KaggleEntityType':
    """The entity type common for the entities having their content state updated."""
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleEntityType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type

  @property
  def entity_ids(self) -> Optional[List[int]]:
    """The ids of the entities having their content state updated."""
    return self._entity_ids

  @entity_ids.setter
  def entity_ids(self, entity_ids: Optional[List[int]]):
    if entity_ids is None:
      del self.entity_ids
      return
    if not isinstance(entity_ids, list):
      raise TypeError('entity_ids must be of type list')
    if not all([isinstance(t, int) for t in entity_ids]):
      raise TypeError('entity_ids must contain only items of type int')
    self._entity_ids = entity_ids

  @property
  def target_content_state(self) -> 'ContentState':
    """The content state that the entities provided should be updated to."""
    return self._target_content_state

  @target_content_state.setter
  def target_content_state(self, target_content_state: 'ContentState'):
    if target_content_state is None:
      del self.target_content_state
      return
    if not isinstance(target_content_state, ContentState):
      raise TypeError('target_content_state must be of type ContentState')
    self._target_content_state = target_content_state

  @property
  def notes(self) -> str:
    """Optional notes that will be included in the ContentStateLog."""
    return self._notes or ""

  @notes.setter
  def notes(self, notes: Optional[str]):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


class GetEntityForModerationRequest(KaggleObject):
  r"""
  Attributes:
    creator_user_id (int)
      The ID of the user the entity was created by
    entity_type (KaggleEntityType)
      The type of the entity
    entity_id (int)
      The ID of the entity
    allow_different_creator (bool)
      Whether to still return the info if the owner is
      different than the user specified (e.g. the owner has
      been nulled out, or transferred to a different user)
  """

  def __init__(self):
    self._creator_user_id = 0
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._entity_id = 0
    self._allow_different_creator = None
    self._freeze()

  @property
  def creator_user_id(self) -> int:
    """The ID of the user the entity was created by"""
    return self._creator_user_id

  @creator_user_id.setter
  def creator_user_id(self, creator_user_id: int):
    if creator_user_id is None:
      del self.creator_user_id
      return
    if not isinstance(creator_user_id, int):
      raise TypeError('creator_user_id must be of type int')
    self._creator_user_id = creator_user_id

  @property
  def entity_type(self) -> 'KaggleEntityType':
    """The type of the entity"""
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleEntityType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type

  @property
  def entity_id(self) -> int:
    """The ID of the entity"""
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: int):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, int):
      raise TypeError('entity_id must be of type int')
    self._entity_id = entity_id

  @property
  def allow_different_creator(self) -> bool:
    r"""
    Whether to still return the info if the owner is
    different than the user specified (e.g. the owner has
    been nulled out, or transferred to a different user)
    """
    return self._allow_different_creator or False

  @allow_different_creator.setter
  def allow_different_creator(self, allow_different_creator: Optional[bool]):
    if allow_different_creator is None:
      del self.allow_different_creator
      return
    if not isinstance(allow_different_creator, bool):
      raise TypeError('allow_different_creator must be of type bool')
    self._allow_different_creator = allow_different_creator


class GetEntityForModerationResponse(KaggleObject):
  r"""
  Attributes:
    title (str)
      The title of the requested entity
    create_time (datetime)
      When the requested entity was created
    actual_creator_user_id (int)
      The actual creator UserId of the content;
      NOTE: this is used to allow the return of entities that
      is tied to a user penalty even if they're no longer the
      owner (e.g. the owner has been nulled out, or transferred
      to a different user).
    content_state (ContentState)
      The content state of the entity
  """

  def __init__(self):
    self._title = ""
    self._create_time = None
    self._actual_creator_user_id = None
    self._content_state = None
    self._freeze()

  @property
  def title(self) -> str:
    """The title of the requested entity"""
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def create_time(self) -> datetime:
    """When the requested entity was created"""
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
  def content_state(self) -> 'ContentState':
    """The content state of the entity"""
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def actual_creator_user_id(self) -> int:
    r"""
    The actual creator UserId of the content;
    NOTE: this is used to allow the return of entities that
    is tied to a user penalty even if they're no longer the
    owner (e.g. the owner has been nulled out, or transferred
    to a different user).
    """
    return self._actual_creator_user_id or 0

  @actual_creator_user_id.setter
  def actual_creator_user_id(self, actual_creator_user_id: Optional[int]):
    if actual_creator_user_id is None:
      del self.actual_creator_user_id
      return
    if not isinstance(actual_creator_user_id, int):
      raise TypeError('actual_creator_user_id must be of type int')
    self._actual_creator_user_id = actual_creator_user_id


class IssueUserPenaltyRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The ID of the user being issued the penalty
    penalty (Penalty)
      The penalty being issued
    suspension_duration_days (int)
      The duration (in days) of the suspension
    policy_violation_id (PolicyViolationId)
      The PolicyViolationId tied to this penalty
    other_violation (str)
      Other user-visible violation notes not covered by the list of
      `policy_violation_ids`
    moderator_notes (str)
      Additional admin-only notes/context on the penalty
    penalty_source_id (PenaltySourceId)
      How moderation was made aware of this violation
    violation_contents (ViolationContent)
      The list of content associated with this penalty
    automated_detection (bool)
      Whether the detection of the violation was automated
    automated_decision (bool)
      Whether the decision to take action was automated
    send_sor (bool)
      Whether to send an SOR email to the user (e.g. we don't have to send emails
      when an account is clearly being used solely for spam or other abuse)
    violation_source (PolicyViolationSource)
      What detected the violation
  """

  def __init__(self):
    self._user_id = 0
    self._penalty = Penalty.NONE
    self._suspension_duration_days = None
    self._policy_violation_id = None
    self._other_violation = None
    self._moderator_notes = None
    self._penalty_source_id = None
    self._violation_contents = []
    self._automated_detection = None
    self._automated_decision = None
    self._send_sor = None
    self._violation_source = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """The ID of the user being issued the penalty"""
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
  def penalty(self) -> 'Penalty':
    """The penalty being issued"""
    return self._penalty

  @penalty.setter
  def penalty(self, penalty: 'Penalty'):
    if penalty is None:
      del self.penalty
      return
    if not isinstance(penalty, Penalty):
      raise TypeError('penalty must be of type Penalty')
    self._penalty = penalty

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
  def policy_violation_id(self) -> 'PolicyViolationId':
    """The PolicyViolationId tied to this penalty"""
    return self._policy_violation_id or PolicyViolationId.POLICY_VIOLATION_ID_UNSPECIFIED

  @policy_violation_id.setter
  def policy_violation_id(self, policy_violation_id: Optional['PolicyViolationId']):
    if policy_violation_id is None:
      del self.policy_violation_id
      return
    if not isinstance(policy_violation_id, PolicyViolationId):
      raise TypeError('policy_violation_id must be of type PolicyViolationId')
    self._policy_violation_id = policy_violation_id

  @property
  def other_violation(self) -> str:
    r"""
    Other user-visible violation notes not covered by the list of
    `policy_violation_ids`
    """
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
  def moderator_notes(self) -> str:
    """Additional admin-only notes/context on the penalty"""
    return self._moderator_notes or ""

  @moderator_notes.setter
  def moderator_notes(self, moderator_notes: Optional[str]):
    if moderator_notes is None:
      del self.moderator_notes
      return
    if not isinstance(moderator_notes, str):
      raise TypeError('moderator_notes must be of type str')
    self._moderator_notes = moderator_notes

  @property
  def penalty_source_id(self) -> 'PenaltySourceId':
    """How moderation was made aware of this violation"""
    return self._penalty_source_id or PenaltySourceId.PENALTY_SOURCE_ID_UNSPECIFIED

  @penalty_source_id.setter
  def penalty_source_id(self, penalty_source_id: Optional['PenaltySourceId']):
    if penalty_source_id is None:
      del self.penalty_source_id
      return
    if not isinstance(penalty_source_id, PenaltySourceId):
      raise TypeError('penalty_source_id must be of type PenaltySourceId')
    self._penalty_source_id = penalty_source_id

  @property
  def violation_contents(self) -> Optional[List[Optional['ViolationContent']]]:
    """The list of content associated with this penalty"""
    return self._violation_contents

  @violation_contents.setter
  def violation_contents(self, violation_contents: Optional[List[Optional['ViolationContent']]]):
    if violation_contents is None:
      del self.violation_contents
      return
    if not isinstance(violation_contents, list):
      raise TypeError('violation_contents must be of type list')
    if not all([isinstance(t, ViolationContent) for t in violation_contents]):
      raise TypeError('violation_contents must contain only items of type ViolationContent')
    self._violation_contents = violation_contents

  @property
  def automated_detection(self) -> bool:
    """Whether the detection of the violation was automated"""
    return self._automated_detection or False

  @automated_detection.setter
  def automated_detection(self, automated_detection: Optional[bool]):
    if automated_detection is None:
      del self.automated_detection
      return
    if not isinstance(automated_detection, bool):
      raise TypeError('automated_detection must be of type bool')
    self._automated_detection = automated_detection

  @property
  def automated_decision(self) -> bool:
    """Whether the decision to take action was automated"""
    return self._automated_decision or False

  @automated_decision.setter
  def automated_decision(self, automated_decision: Optional[bool]):
    if automated_decision is None:
      del self.automated_decision
      return
    if not isinstance(automated_decision, bool):
      raise TypeError('automated_decision must be of type bool')
    self._automated_decision = automated_decision

  @property
  def send_sor(self) -> bool:
    r"""
    Whether to send an SOR email to the user (e.g. we don't have to send emails
    when an account is clearly being used solely for spam or other abuse)
    """
    return self._send_sor or False

  @send_sor.setter
  def send_sor(self, send_sor: Optional[bool]):
    if send_sor is None:
      del self.send_sor
      return
    if not isinstance(send_sor, bool):
      raise TypeError('send_sor must be of type bool')
    self._send_sor = send_sor

  @property
  def violation_source(self) -> 'PolicyViolationSource':
    """What detected the violation"""
    return self._violation_source or PolicyViolationSource.POLICY_VIOLATION_SOURCE_UNSPECIFIED

  @violation_source.setter
  def violation_source(self, violation_source: Optional['PolicyViolationSource']):
    if violation_source is None:
      del self.violation_source
      return
    if not isinstance(violation_source, PolicyViolationSource):
      raise TypeError('violation_source must be of type PolicyViolationSource')
    self._violation_source = violation_source


class ListAppealReasonsRequest(KaggleObject):
  r"""
  """

  pass

class ListAppealReasonsResponse(KaggleObject):
  r"""
  Attributes:
    appeal_reasons (AppealReasonDescription)
      The list of appeal reasons
  """

  def __init__(self):
    self._appeal_reasons = []
    self._freeze()

  @property
  def appeal_reasons(self) -> Optional[List[Optional['AppealReasonDescription']]]:
    """The list of appeal reasons"""
    return self._appeal_reasons

  @appeal_reasons.setter
  def appeal_reasons(self, appeal_reasons: Optional[List[Optional['AppealReasonDescription']]]):
    if appeal_reasons is None:
      del self.appeal_reasons
      return
    if not isinstance(appeal_reasons, list):
      raise TypeError('appeal_reasons must be of type list')
    if not all([isinstance(t, AppealReasonDescription) for t in appeal_reasons]):
      raise TypeError('appeal_reasons must contain only items of type AppealReasonDescription')
    self._appeal_reasons = appeal_reasons


class ListPenaltySourcesRequest(KaggleObject):
  r"""
  """

  pass

class ListPenaltySourcesResponse(KaggleObject):
  r"""
  Attributes:
    penalty_sources (PenaltySource)
      The list of penalty sources
  """

  def __init__(self):
    self._penalty_sources = []
    self._freeze()

  @property
  def penalty_sources(self) -> Optional[List[Optional['PenaltySource']]]:
    """The list of penalty sources"""
    return self._penalty_sources

  @penalty_sources.setter
  def penalty_sources(self, penalty_sources: Optional[List[Optional['PenaltySource']]]):
    if penalty_sources is None:
      del self.penalty_sources
      return
    if not isinstance(penalty_sources, list):
      raise TypeError('penalty_sources must be of type list')
    if not all([isinstance(t, PenaltySource) for t in penalty_sources]):
      raise TypeError('penalty_sources must contain only items of type PenaltySource')
    self._penalty_sources = penalty_sources


class ListUserModerationHistoryRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      The ID of the user to fetch the penalty history for
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    """The ID of the user to fetch the penalty history for"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class ListUserModerationHistoryResponse(KaggleObject):
  r"""
  Attributes:
    moderation_events (ModerationEvent)
      The list of penalties for the requested user_id
  """

  def __init__(self):
    self._moderation_events = []
    self._freeze()

  @property
  def moderation_events(self) -> Optional[List[Optional['ModerationEvent']]]:
    """The list of penalties for the requested user_id"""
    return self._moderation_events

  @moderation_events.setter
  def moderation_events(self, moderation_events: Optional[List[Optional['ModerationEvent']]]):
    if moderation_events is None:
      del self.moderation_events
      return
    if not isinstance(moderation_events, list):
      raise TypeError('moderation_events must be of type list')
    if not all([isinstance(t, ModerationEvent) for t in moderation_events]):
      raise TypeError('moderation_events must contain only items of type ModerationEvent')
    self._moderation_events = moderation_events


class ModerationEvent(KaggleObject):
  r"""
  Attributes:
    user_penalty_id (int)
      The ID of the user penalty
    penalty (Penalty)
      The penalty that was issued
    issuer_user_name (str)
      The username of the user that issued the event
    issuer_display_name (str)
      The display name of the user that issued the event
    log_date (datetime)
      The date the penalty was issued
    suspension_duration_days (int)
      The duration (in days) of the suspension
    suspension_lift_date (datetime)
      The date the suspension was/will be lifted
    notes (str)
      Notes of the event
    has_spam_violation (bool)
      Whether the user has a spam violation
    violation (str)
      The violation tied to the event
    event_type (ModerationEventType)
      The type of event
    penalty_source_id (PenaltySourceId)
      How moderation was made aware of this violation
    automated_detection (bool)
      Whether the detection of the violation was automated
    automated_decision (bool)
      Whether the decision to take action was automated
    sor_sent (bool)
      Whether an SOR email was sent to the user
    verdict (ModerationVerdict)
      The verdict of the report/appeal
    entities (ModerationEventEntity)
      The entities associated with the event
    event_id (int)
      The ID associated with the event type (e.g. UserPenalty.Id,
      ModerationLog.Id, FlaggedContent.Id, etc.)
    verdict_moderator_user_name (str)
      The username of the moderator that made the verdict
    verdict_moderator_display_name (str)
      The display name of the moderator that made the verdict
    verdict_time (datetime)
      The date/time the verdict was applied
    verdict_notes (str)
      Any admin-only notes associated with the verdict
  """

  def __init__(self):
    self._user_penalty_id = None
    self._penalty = None
    self._issuer_user_name = ""
    self._issuer_display_name = ""
    self._log_date = None
    self._suspension_duration_days = None
    self._suspension_lift_date = None
    self._notes = ""
    self._has_spam_violation = False
    self._violation = None
    self._event_type = ModerationEventType.MODERATION_EVENT_TYPE_UNSPECIFIED
    self._penalty_source_id = None
    self._automated_detection = None
    self._automated_decision = None
    self._sor_sent = None
    self._verdict = None
    self._entities = []
    self._event_id = 0
    self._verdict_moderator_user_name = None
    self._verdict_moderator_display_name = None
    self._verdict_time = None
    self._verdict_notes = None
    self._freeze()

  @property
  def user_penalty_id(self) -> int:
    """The ID of the user penalty"""
    return self._user_penalty_id or 0

  @user_penalty_id.setter
  def user_penalty_id(self, user_penalty_id: Optional[int]):
    if user_penalty_id is None:
      del self.user_penalty_id
      return
    if not isinstance(user_penalty_id, int):
      raise TypeError('user_penalty_id must be of type int')
    self._user_penalty_id = user_penalty_id

  @property
  def penalty(self) -> 'Penalty':
    """The penalty that was issued"""
    return self._penalty or Penalty.NONE

  @penalty.setter
  def penalty(self, penalty: Optional['Penalty']):
    if penalty is None:
      del self.penalty
      return
    if not isinstance(penalty, Penalty):
      raise TypeError('penalty must be of type Penalty')
    self._penalty = penalty

  @property
  def issuer_user_name(self) -> str:
    """The username of the user that issued the event"""
    return self._issuer_user_name

  @issuer_user_name.setter
  def issuer_user_name(self, issuer_user_name: str):
    if issuer_user_name is None:
      del self.issuer_user_name
      return
    if not isinstance(issuer_user_name, str):
      raise TypeError('issuer_user_name must be of type str')
    self._issuer_user_name = issuer_user_name

  @property
  def issuer_display_name(self) -> str:
    """The display name of the user that issued the event"""
    return self._issuer_display_name

  @issuer_display_name.setter
  def issuer_display_name(self, issuer_display_name: str):
    if issuer_display_name is None:
      del self.issuer_display_name
      return
    if not isinstance(issuer_display_name, str):
      raise TypeError('issuer_display_name must be of type str')
    self._issuer_display_name = issuer_display_name

  @property
  def log_date(self) -> datetime:
    """The date the penalty was issued"""
    return self._log_date

  @log_date.setter
  def log_date(self, log_date: datetime):
    if log_date is None:
      del self.log_date
      return
    if not isinstance(log_date, datetime):
      raise TypeError('log_date must be of type datetime')
    self._log_date = log_date

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
  def suspension_lift_date(self) -> datetime:
    """The date the suspension was/will be lifted"""
    return self._suspension_lift_date or None

  @suspension_lift_date.setter
  def suspension_lift_date(self, suspension_lift_date: Optional[datetime]):
    if suspension_lift_date is None:
      del self.suspension_lift_date
      return
    if not isinstance(suspension_lift_date, datetime):
      raise TypeError('suspension_lift_date must be of type datetime')
    self._suspension_lift_date = suspension_lift_date

  @property
  def notes(self) -> str:
    """Notes of the event"""
    return self._notes

  @notes.setter
  def notes(self, notes: str):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes

  @property
  def has_spam_violation(self) -> bool:
    """Whether the user has a spam violation"""
    return self._has_spam_violation

  @has_spam_violation.setter
  def has_spam_violation(self, has_spam_violation: bool):
    if has_spam_violation is None:
      del self.has_spam_violation
      return
    if not isinstance(has_spam_violation, bool):
      raise TypeError('has_spam_violation must be of type bool')
    self._has_spam_violation = has_spam_violation

  @property
  def violation(self) -> str:
    """The violation tied to the event"""
    return self._violation or ""

  @violation.setter
  def violation(self, violation: Optional[str]):
    if violation is None:
      del self.violation
      return
    if not isinstance(violation, str):
      raise TypeError('violation must be of type str')
    self._violation = violation

  @property
  def event_id(self) -> int:
    r"""
    The ID associated with the event type (e.g. UserPenalty.Id,
    ModerationLog.Id, FlaggedContent.Id, etc.)
    """
    return self._event_id

  @event_id.setter
  def event_id(self, event_id: int):
    if event_id is None:
      del self.event_id
      return
    if not isinstance(event_id, int):
      raise TypeError('event_id must be of type int')
    self._event_id = event_id

  @property
  def event_type(self) -> 'ModerationEventType':
    """The type of event"""
    return self._event_type

  @event_type.setter
  def event_type(self, event_type: 'ModerationEventType'):
    if event_type is None:
      del self.event_type
      return
    if not isinstance(event_type, ModerationEventType):
      raise TypeError('event_type must be of type ModerationEventType')
    self._event_type = event_type

  @property
  def entities(self) -> Optional[List[Optional['ModerationEventEntity']]]:
    """The entities associated with the event"""
    return self._entities

  @entities.setter
  def entities(self, entities: Optional[List[Optional['ModerationEventEntity']]]):
    if entities is None:
      del self.entities
      return
    if not isinstance(entities, list):
      raise TypeError('entities must be of type list')
    if not all([isinstance(t, ModerationEventEntity) for t in entities]):
      raise TypeError('entities must contain only items of type ModerationEventEntity')
    self._entities = entities

  @property
  def penalty_source_id(self) -> 'PenaltySourceId':
    """How moderation was made aware of this violation"""
    return self._penalty_source_id or PenaltySourceId.PENALTY_SOURCE_ID_UNSPECIFIED

  @penalty_source_id.setter
  def penalty_source_id(self, penalty_source_id: Optional['PenaltySourceId']):
    if penalty_source_id is None:
      del self.penalty_source_id
      return
    if not isinstance(penalty_source_id, PenaltySourceId):
      raise TypeError('penalty_source_id must be of type PenaltySourceId')
    self._penalty_source_id = penalty_source_id

  @property
  def automated_detection(self) -> bool:
    """Whether the detection of the violation was automated"""
    return self._automated_detection or False

  @automated_detection.setter
  def automated_detection(self, automated_detection: Optional[bool]):
    if automated_detection is None:
      del self.automated_detection
      return
    if not isinstance(automated_detection, bool):
      raise TypeError('automated_detection must be of type bool')
    self._automated_detection = automated_detection

  @property
  def automated_decision(self) -> bool:
    """Whether the decision to take action was automated"""
    return self._automated_decision or False

  @automated_decision.setter
  def automated_decision(self, automated_decision: Optional[bool]):
    if automated_decision is None:
      del self.automated_decision
      return
    if not isinstance(automated_decision, bool):
      raise TypeError('automated_decision must be of type bool')
    self._automated_decision = automated_decision

  @property
  def sor_sent(self) -> bool:
    """Whether an SOR email was sent to the user"""
    return self._sor_sent or False

  @sor_sent.setter
  def sor_sent(self, sor_sent: Optional[bool]):
    if sor_sent is None:
      del self.sor_sent
      return
    if not isinstance(sor_sent, bool):
      raise TypeError('sor_sent must be of type bool')
    self._sor_sent = sor_sent

  @property
  def verdict(self) -> 'ModerationVerdict':
    """The verdict of the report/appeal"""
    return self._verdict or ModerationVerdict.MODERATION_VERDICT_UNSPECIFIED

  @verdict.setter
  def verdict(self, verdict: Optional['ModerationVerdict']):
    if verdict is None:
      del self.verdict
      return
    if not isinstance(verdict, ModerationVerdict):
      raise TypeError('verdict must be of type ModerationVerdict')
    self._verdict = verdict

  @property
  def verdict_moderator_user_name(self) -> str:
    """The username of the moderator that made the verdict"""
    return self._verdict_moderator_user_name or ""

  @verdict_moderator_user_name.setter
  def verdict_moderator_user_name(self, verdict_moderator_user_name: Optional[str]):
    if verdict_moderator_user_name is None:
      del self.verdict_moderator_user_name
      return
    if not isinstance(verdict_moderator_user_name, str):
      raise TypeError('verdict_moderator_user_name must be of type str')
    self._verdict_moderator_user_name = verdict_moderator_user_name

  @property
  def verdict_moderator_display_name(self) -> str:
    """The display name of the moderator that made the verdict"""
    return self._verdict_moderator_display_name or ""

  @verdict_moderator_display_name.setter
  def verdict_moderator_display_name(self, verdict_moderator_display_name: Optional[str]):
    if verdict_moderator_display_name is None:
      del self.verdict_moderator_display_name
      return
    if not isinstance(verdict_moderator_display_name, str):
      raise TypeError('verdict_moderator_display_name must be of type str')
    self._verdict_moderator_display_name = verdict_moderator_display_name

  @property
  def verdict_time(self) -> datetime:
    """The date/time the verdict was applied"""
    return self._verdict_time or None

  @verdict_time.setter
  def verdict_time(self, verdict_time: Optional[datetime]):
    if verdict_time is None:
      del self.verdict_time
      return
    if not isinstance(verdict_time, datetime):
      raise TypeError('verdict_time must be of type datetime')
    self._verdict_time = verdict_time

  @property
  def verdict_notes(self) -> str:
    """Any admin-only notes associated with the verdict"""
    return self._verdict_notes or ""

  @verdict_notes.setter
  def verdict_notes(self, verdict_notes: Optional[str]):
    if verdict_notes is None:
      del self.verdict_notes
      return
    if not isinstance(verdict_notes, str):
      raise TypeError('verdict_notes must be of type str')
    self._verdict_notes = verdict_notes


class ModerationEventEntity(KaggleObject):
  r"""
  Attributes:
    entity_type (KaggleEntityType)
      The entity type of the related content
    entity_id (int)
      The ID of the related content
    content_title (str)
      The title of the related content
    content_url (str)
      The URL of the related content
    content_state (ContentState)
      The content state of the related entity
    content_create_time (datetime)
      When the content was created
    violation_source (PolicyViolationSource)
      What detected the violation
  """

  def __init__(self):
    self._entity_type = None
    self._entity_id = None
    self._content_title = None
    self._content_url = None
    self._content_state = None
    self._content_create_time = None
    self._violation_source = None
    self._freeze()

  @property
  def entity_type(self) -> 'KaggleEntityType':
    """The entity type of the related content"""
    return self._entity_type or KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED

  @entity_type.setter
  def entity_type(self, entity_type: Optional['KaggleEntityType']):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type

  @property
  def entity_id(self) -> int:
    """The ID of the related content"""
    return self._entity_id or 0

  @entity_id.setter
  def entity_id(self, entity_id: Optional[int]):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, int):
      raise TypeError('entity_id must be of type int')
    self._entity_id = entity_id

  @property
  def content_title(self) -> str:
    """The title of the related content"""
    return self._content_title or ""

  @content_title.setter
  def content_title(self, content_title: Optional[str]):
    if content_title is None:
      del self.content_title
      return
    if not isinstance(content_title, str):
      raise TypeError('content_title must be of type str')
    self._content_title = content_title

  @property
  def content_url(self) -> str:
    """The URL of the related content"""
    return self._content_url or ""

  @content_url.setter
  def content_url(self, content_url: Optional[str]):
    if content_url is None:
      del self.content_url
      return
    if not isinstance(content_url, str):
      raise TypeError('content_url must be of type str')
    self._content_url = content_url

  @property
  def content_state(self) -> 'ContentState':
    """The content state of the related entity"""
    return self._content_state or ContentState.CONTENT_STATE_UNSPECIFIED

  @content_state.setter
  def content_state(self, content_state: Optional['ContentState']):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def content_create_time(self) -> datetime:
    """When the content was created"""
    return self._content_create_time or None

  @content_create_time.setter
  def content_create_time(self, content_create_time: Optional[datetime]):
    if content_create_time is None:
      del self.content_create_time
      return
    if not isinstance(content_create_time, datetime):
      raise TypeError('content_create_time must be of type datetime')
    self._content_create_time = content_create_time

  @property
  def violation_source(self) -> 'PolicyViolationSource':
    """What detected the violation"""
    return self._violation_source or PolicyViolationSource.POLICY_VIOLATION_SOURCE_UNSPECIFIED

  @violation_source.setter
  def violation_source(self, violation_source: Optional['PolicyViolationSource']):
    if violation_source is None:
      del self.violation_source
      return
    if not isinstance(violation_source, PolicyViolationSource):
      raise TypeError('violation_source must be of type PolicyViolationSource')
    self._violation_source = violation_source


class PenaltySource(KaggleObject):
  r"""
  Attributes:
    id (PenaltySourceId)
      The ID of the penalty source
    description (str)
      The user-visible description of the penalty source
  """

  def __init__(self):
    self._id = PenaltySourceId.PENALTY_SOURCE_ID_UNSPECIFIED
    self._description = ""
    self._freeze()

  @property
  def id(self) -> 'PenaltySourceId':
    """The ID of the penalty source"""
    return self._id

  @id.setter
  def id(self, id: 'PenaltySourceId'):
    if id is None:
      del self.id
      return
    if not isinstance(id, PenaltySourceId):
      raise TypeError('id must be of type PenaltySourceId')
    self._id = id

  @property
  def description(self) -> str:
    """The user-visible description of the penalty source"""
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description


class SetUserAppealVerdictRequest(KaggleObject):
  r"""
  Attributes:
    user_appeal_id (int)
      Any UserAppealId to set the verdict & notes for
    verdict (ModerationVerdict)
      The verdict of the appeal
    notes (str)
      The admin-ony notes with more details behind the verdict
    verdict_time_override (datetime)
      A timestamp override to use for verdict time, instead of current time. Used
      when backfilling verdict logs, to avoid inaccuracy in appeal response time.
  """

  def __init__(self):
    self._user_appeal_id = 0
    self._verdict = ModerationVerdict.MODERATION_VERDICT_UNSPECIFIED
    self._notes = ""
    self._verdict_time_override = None
    self._freeze()

  @property
  def user_appeal_id(self) -> int:
    """Any UserAppealId to set the verdict & notes for"""
    return self._user_appeal_id

  @user_appeal_id.setter
  def user_appeal_id(self, user_appeal_id: int):
    if user_appeal_id is None:
      del self.user_appeal_id
      return
    if not isinstance(user_appeal_id, int):
      raise TypeError('user_appeal_id must be of type int')
    self._user_appeal_id = user_appeal_id

  @property
  def verdict(self) -> 'ModerationVerdict':
    """The verdict of the appeal"""
    return self._verdict

  @verdict.setter
  def verdict(self, verdict: 'ModerationVerdict'):
    if verdict is None:
      del self.verdict
      return
    if not isinstance(verdict, ModerationVerdict):
      raise TypeError('verdict must be of type ModerationVerdict')
    self._verdict = verdict

  @property
  def notes(self) -> str:
    """The admin-ony notes with more details behind the verdict"""
    return self._notes

  @notes.setter
  def notes(self, notes: str):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes

  @property
  def verdict_time_override(self) -> datetime:
    r"""
    A timestamp override to use for verdict time, instead of current time. Used
    when backfilling verdict logs, to avoid inaccuracy in appeal response time.
    """
    return self._verdict_time_override or None

  @verdict_time_override.setter
  def verdict_time_override(self, verdict_time_override: Optional[datetime]):
    if verdict_time_override is None:
      del self.verdict_time_override
      return
    if not isinstance(verdict_time_override, datetime):
      raise TypeError('verdict_time_override must be of type datetime')
    self._verdict_time_override = verdict_time_override


class UnbanUsersRequest(KaggleObject):
  r"""
  Attributes:
    user_ids (int)
      The IDs of the users to unban
    appeal_reason (AppealReason)
      Unbanning is effectively appealing the ban; This is the reason that will be
      attached to the appeal
    notes (str)
      Admin-only notes/context on the appeal/unban
  """

  def __init__(self):
    self._user_ids = []
    self._appeal_reason = AppealReason.APPEAL_REASON_UNSPECIFIED
    self._notes = ""
    self._freeze()

  @property
  def user_ids(self) -> Optional[List[int]]:
    """The IDs of the users to unban"""
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
  def appeal_reason(self) -> 'AppealReason':
    r"""
    Unbanning is effectively appealing the ban; This is the reason that will be
    attached to the appeal
    """
    return self._appeal_reason

  @appeal_reason.setter
  def appeal_reason(self, appeal_reason: 'AppealReason'):
    if appeal_reason is None:
      del self.appeal_reason
      return
    if not isinstance(appeal_reason, AppealReason):
      raise TypeError('appeal_reason must be of type AppealReason')
    self._appeal_reason = appeal_reason

  @property
  def notes(self) -> str:
    """Admin-only notes/context on the appeal/unban"""
    return self._notes

  @notes.setter
  def notes(self, notes: str):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


class UnbanUsersResponse(KaggleObject):
  r"""
  Attributes:
    response (BulkUpdateResponse)
  """

  def __init__(self):
    self._response = None
    self._freeze()

  @property
  def response(self) -> Optional['BulkUpdateResponse']:
    return self._response

  @response.setter
  def response(self, response: Optional['BulkUpdateResponse']):
    if response is None:
      del self.response
      return
    if not isinstance(response, BulkUpdateResponse):
      raise TypeError('response must be of type BulkUpdateResponse')
    self._response = response


class ViolationContent(KaggleObject):
  r"""
  Attributes:
    entity (ViolationContentEntity)
    moderation_log_id (int)
  """

  def __init__(self):
    self._entity = None
    self._moderation_log_id = None
    self._freeze()

  @property
  def entity(self) -> Optional['ViolationContentEntity']:
    return self._entity or None

  @entity.setter
  def entity(self, entity: Optional['ViolationContentEntity']):
    if entity is None:
      del self.entity
      return
    if not isinstance(entity, ViolationContentEntity):
      raise TypeError('entity must be of type ViolationContentEntity')
    del self.moderation_log_id
    self._entity = entity

  @property
  def moderation_log_id(self) -> int:
    return self._moderation_log_id or 0

  @moderation_log_id.setter
  def moderation_log_id(self, moderation_log_id: int):
    if moderation_log_id is None:
      del self.moderation_log_id
      return
    if not isinstance(moderation_log_id, int):
      raise TypeError('moderation_log_id must be of type int')
    del self.entity
    self._moderation_log_id = moderation_log_id


class ViolationContentEntity(KaggleObject):
  r"""
  Attributes:
    type (KaggleEntityType)
      The type of the entity
    id (int)
      The ID of the entity
  """

  def __init__(self):
    self._type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._id = 0
    self._freeze()

  @property
  def type(self) -> 'KaggleEntityType':
    """The type of the entity"""
    return self._type

  @type.setter
  def type(self, type: 'KaggleEntityType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, KaggleEntityType):
      raise TypeError('type must be of type KaggleEntityType')
    self._type = type

  @property
  def id(self) -> int:
    """The ID of the entity"""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


AppealReasonDescription._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
]

ApproveAppealRequest._fields = [
  FieldMetadata("userPenaltyId", "user_penalty_id", "_user_penalty_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reasonIds", "reason_ids", "_reason_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
]

BulkUpdateResponse._fields = [
  FieldMetadata("total", "total", "_total", int, 0, PredefinedSerializer()),
  FieldMetadata("countSuccessful", "count_successful", "_count_successful", int, 0, PredefinedSerializer()),
  FieldMetadata("countFailed", "count_failed", "_count_failed", int, 0, PredefinedSerializer()),
  FieldMetadata("countIgnored", "count_ignored", "_count_ignored", int, 0, PredefinedSerializer()),
  FieldMetadata("elapsedTimeMilliseconds", "elapsed_time_milliseconds", "_elapsed_time_milliseconds", int, 0, PredefinedSerializer()),
  FieldMetadata("failures", "failures", "_failures", FailureResult, [], ListSerializer(KaggleObjectSerializer())),
]

FailureResult._fields = [
  FieldMetadata("message", "message", "_message", str, "", PredefinedSerializer()),
  FieldMetadata("userCount", "user_count", "_user_count", int, 0, PredefinedSerializer()),
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ForceUpdateContentStatesRequest._fields = [
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("entityIds", "entity_ids", "_entity_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("targetContentState", "target_content_state", "_target_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
]

GetEntityForModerationRequest._fields = [
  FieldMetadata("creatorUserId", "creator_user_id", "_creator_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("allowDifferentCreator", "allow_different_creator", "_allow_different_creator", bool, None, PredefinedSerializer(), optional=True),
]

GetEntityForModerationResponse._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("actualCreatorUserId", "actual_creator_user_id", "_actual_creator_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
]

IssueUserPenaltyRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("penalty", "penalty", "_penalty", Penalty, Penalty.NONE, EnumSerializer()),
  FieldMetadata("suspensionDurationDays", "suspension_duration_days", "_suspension_duration_days", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("policyViolationId", "policy_violation_id", "_policy_violation_id", PolicyViolationId, None, EnumSerializer(), optional=True),
  FieldMetadata("otherViolation", "other_violation", "_other_violation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("moderatorNotes", "moderator_notes", "_moderator_notes", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("penaltySourceId", "penalty_source_id", "_penalty_source_id", PenaltySourceId, None, EnumSerializer(), optional=True),
  FieldMetadata("violationContents", "violation_contents", "_violation_contents", ViolationContent, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("automatedDetection", "automated_detection", "_automated_detection", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("automatedDecision", "automated_decision", "_automated_decision", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sendSor", "send_sor", "_send_sor", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("violationSource", "violation_source", "_violation_source", PolicyViolationSource, None, EnumSerializer(), optional=True),
]

ListAppealReasonsRequest._fields = []

ListAppealReasonsResponse._fields = [
  FieldMetadata("appealReasons", "appeal_reasons", "_appeal_reasons", AppealReasonDescription, [], ListSerializer(KaggleObjectSerializer())),
]

ListPenaltySourcesRequest._fields = []

ListPenaltySourcesResponse._fields = [
  FieldMetadata("penaltySources", "penalty_sources", "_penalty_sources", PenaltySource, [], ListSerializer(KaggleObjectSerializer())),
]

ListUserModerationHistoryRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

ListUserModerationHistoryResponse._fields = [
  FieldMetadata("moderationEvents", "moderation_events", "_moderation_events", ModerationEvent, [], ListSerializer(KaggleObjectSerializer())),
]

ModerationEvent._fields = [
  FieldMetadata("userPenaltyId", "user_penalty_id", "_user_penalty_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("penalty", "penalty", "_penalty", Penalty, None, EnumSerializer(), optional=True),
  FieldMetadata("issuerUserName", "issuer_user_name", "_issuer_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("issuerDisplayName", "issuer_display_name", "_issuer_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("logDate", "log_date", "_log_date", datetime, None, DateTimeSerializer()),
  FieldMetadata("suspensionDurationDays", "suspension_duration_days", "_suspension_duration_days", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("suspensionLiftDate", "suspension_lift_date", "_suspension_lift_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("notes", "notes", "_notes", str, "", PredefinedSerializer()),
  FieldMetadata("hasSpamViolation", "has_spam_violation", "_has_spam_violation", bool, False, PredefinedSerializer()),
  FieldMetadata("violation", "violation", "_violation", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("eventType", "event_type", "_event_type", ModerationEventType, ModerationEventType.MODERATION_EVENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("penaltySourceId", "penalty_source_id", "_penalty_source_id", PenaltySourceId, None, EnumSerializer(), optional=True),
  FieldMetadata("automatedDetection", "automated_detection", "_automated_detection", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("automatedDecision", "automated_decision", "_automated_decision", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sorSent", "sor_sent", "_sor_sent", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verdict", "verdict", "_verdict", ModerationVerdict, None, EnumSerializer(), optional=True),
  FieldMetadata("entities", "entities", "_entities", ModerationEventEntity, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("eventId", "event_id", "_event_id", int, 0, PredefinedSerializer()),
  FieldMetadata("verdictModeratorUserName", "verdict_moderator_user_name", "_verdict_moderator_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verdictModeratorDisplayName", "verdict_moderator_display_name", "_verdict_moderator_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("verdictTime", "verdict_time", "_verdict_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("verdictNotes", "verdict_notes", "_verdict_notes", str, None, PredefinedSerializer(), optional=True),
]

ModerationEventEntity._fields = [
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, None, EnumSerializer(), optional=True),
  FieldMetadata("entityId", "entity_id", "_entity_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentTitle", "content_title", "_content_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentUrl", "content_url", "_content_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, None, EnumSerializer(), optional=True),
  FieldMetadata("contentCreateTime", "content_create_time", "_content_create_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("violationSource", "violation_source", "_violation_source", PolicyViolationSource, None, EnumSerializer(), optional=True),
]

PenaltySource._fields = [
  FieldMetadata("id", "id", "_id", PenaltySourceId, PenaltySourceId.PENALTY_SOURCE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
]

SetUserAppealVerdictRequest._fields = [
  FieldMetadata("userAppealId", "user_appeal_id", "_user_appeal_id", int, 0, PredefinedSerializer()),
  FieldMetadata("verdict", "verdict", "_verdict", ModerationVerdict, ModerationVerdict.MODERATION_VERDICT_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, "", PredefinedSerializer()),
  FieldMetadata("verdictTimeOverride", "verdict_time_override", "_verdict_time_override", datetime, None, DateTimeSerializer(), optional=True),
]

UnbanUsersRequest._fields = [
  FieldMetadata("userIds", "user_ids", "_user_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("appealReason", "appeal_reason", "_appeal_reason", AppealReason, AppealReason.APPEAL_REASON_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, "", PredefinedSerializer()),
]

UnbanUsersResponse._fields = [
  FieldMetadata("response", "response", "_response", BulkUpdateResponse, None, KaggleObjectSerializer()),
]

ViolationContent._fields = [
  FieldMetadata("entity", "entity", "_entity", ViolationContentEntity, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("moderationLogId", "moderation_log_id", "_moderation_log_id", int, None, PredefinedSerializer(), optional=True),
]

ViolationContentEntity._fields = [
  FieldMetadata("type", "type", "_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

