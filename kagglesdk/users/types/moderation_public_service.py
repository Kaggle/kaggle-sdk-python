import enum
from kagglesdk.common.types.common_types import KaggleEntityType
from kagglesdk.kaggle_object import *
from typing import List, Optional

class AppealType(enum.Enum):
  APPEAL_TYPE_UNSPECIFIED = 0
  CONTENT_MODERATION = 1
  """An appeal against moderation action taken on user content"""
  USER_REPORT_NO_ACTION = 2
  """An appeal against moderation taking no action on a user report"""

class PolicyViolationId(enum.Enum):
  POLICY_VIOLATION_ID_UNSPECIFIED = 0
  """DO NOT USE"""
  SPAM_WIDESPREAD = 2
  r"""
  Content that is considered widespread and high-volume spam, e.g.
  bot-created spam
  """
  CHEATING = 3
  """Cheating on competitions"""
  RESOURCE_ABUSE = 4
  """Resource abuse"""
  DUPLICATE_POST = 6
  """Discussion content that is duplicative of other content by the same user"""
  SELF_PROMOTION = 7
  """Discussion content that does not adhere to the self-promotion guidelines"""
  NO_ABUSE_ADMIN = 9
  """Used by admins to republish privated content from reports"""
  DUPLICATE_ACCOUNT = 11
  """Creating multiple Kaggle accounts"""
  VOTE_MANIPULATION = 13
  """Vote manipulation"""
  ABUSIVE_BEHAVIOR = 14
  """Content that is offensive or harassing in nature"""
  NSFW_CONTENT = 15
  """Content that is sexually suggestive or explicit (i.e. NSFW)"""
  LLM_CONTENT = 17
  r"""
  Discussion content that does not adhere to the AI-generated content
  guidelines
  """
  UNRELATED_DATASETS = 18
  """Attaching unrelated datasets to a notebook"""
  LOW_QUALITY = 19
  """Content that is not of genuine value to the community"""
  PLAGIARISM = 20
  """Content that is plagiarized"""
  UNFRIENDLY = 21
  """Discussion content that is unfriendly or unprofessional"""
  JOB_INQUIRY = 22
  """Discussion content that includes job inquiries or postings"""
  COPIED_POST = 25
  """Discussion content that is highly similar to another user's existing post"""
  SPAM_CONTENT = 26
  """Content that does not belong on Kaggle"""
  WRONG_FORUM_OR_TOPIC = 27
  """Discussion content that has been posted in the wrong forum or topic"""
  FREQUENT_SELF_PROMOTION = 28
  """Frequently sharing self-promoting comments"""
  FREQUENT_SPAM_CONTENT = 29
  """Frequently sharing low-quality forum posts or comments"""
  CSAM = 30
  """Content containing CSAM"""
  COPYRIGHT_INFRINGEMENT = 31
  """Content that infringes upon an existing copyright"""
  TERRORIST_CONTENT = 32
  """Content containing pro-terror material"""

class ListViolationDescriptionsRequest(KaggleObject):
  r"""
  """

  pass

class ListViolationDescriptionsResponse(KaggleObject):
  r"""
  Attributes:
    policy_violations (PolicyViolation)
      The list of policy violations that contain descriptions
  """

  def __init__(self):
    self._policy_violations = []
    self._freeze()

  @property
  def policy_violations(self) -> Optional[List[Optional['PolicyViolation']]]:
    """The list of policy violations that contain descriptions"""
    return self._policy_violations

  @policy_violations.setter
  def policy_violations(self, policy_violations: Optional[List[Optional['PolicyViolation']]]):
    if policy_violations is None:
      del self.policy_violations
      return
    if not isinstance(policy_violations, list):
      raise TypeError('policy_violations must be of type list')
    if not all([isinstance(t, PolicyViolation) for t in policy_violations]):
      raise TypeError('policy_violations must contain only items of type PolicyViolation')
    self._policy_violations = policy_violations


class PolicyViolation(KaggleObject):
  r"""
  Attributes:
    id (PolicyViolationId)
      The ID of the policy violation
    name (str)
      The short name of the policy violation
    description (str)
      The user-visible description of the policy violation, including context for
      the content type.
    entity_type (KaggleEntityType)
      The content type tied to the violation
    covered_under_dsa (bool)
      Whether this violation is covered under DSA, and should send an SOR
    public_ui_description (str)
      The user-visible short description of the policy violation, without context
      for the content type, ex: report content flow.
  """

  def __init__(self):
    self._id = PolicyViolationId.POLICY_VIOLATION_ID_UNSPECIFIED
    self._name = ""
    self._description = ""
    self._entity_type = None
    self._covered_under_dsa = False
    self._public_ui_description = ""
    self._freeze()

  @property
  def id(self) -> 'PolicyViolationId':
    """The ID of the policy violation"""
    return self._id

  @id.setter
  def id(self, id: 'PolicyViolationId'):
    if id is None:
      del self.id
      return
    if not isinstance(id, PolicyViolationId):
      raise TypeError('id must be of type PolicyViolationId')
    self._id = id

  @property
  def name(self) -> str:
    """The short name of the policy violation"""
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
  def description(self) -> str:
    r"""
    The user-visible description of the policy violation, including context for
    the content type.
    """
    return self._description

  @description.setter
  def description(self, description: str):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def entity_type(self) -> 'KaggleEntityType':
    """The content type tied to the violation"""
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
  def covered_under_dsa(self) -> bool:
    """Whether this violation is covered under DSA, and should send an SOR"""
    return self._covered_under_dsa

  @covered_under_dsa.setter
  def covered_under_dsa(self, covered_under_dsa: bool):
    if covered_under_dsa is None:
      del self.covered_under_dsa
      return
    if not isinstance(covered_under_dsa, bool):
      raise TypeError('covered_under_dsa must be of type bool')
    self._covered_under_dsa = covered_under_dsa

  @property
  def public_ui_description(self) -> str:
    r"""
    The user-visible short description of the policy violation, without context
    for the content type, ex: report content flow.
    """
    return self._public_ui_description

  @public_ui_description.setter
  def public_ui_description(self, public_ui_description: str):
    if public_ui_description is None:
      del self.public_ui_description
      return
    if not isinstance(public_ui_description, str):
      raise TypeError('public_ui_description must be of type str')
    self._public_ui_description = public_ui_description


ListViolationDescriptionsRequest._fields = []

ListViolationDescriptionsResponse._fields = [
  FieldMetadata("policyViolations", "policy_violations", "_policy_violations", PolicyViolation, [], ListSerializer(KaggleObjectSerializer())),
]

PolicyViolation._fields = [
  FieldMetadata("id", "id", "_id", PolicyViolationId, PolicyViolationId.POLICY_VIOLATION_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("description", "description", "_description", str, "", PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, None, EnumSerializer(), optional=True),
  FieldMetadata("coveredUnderDsa", "covered_under_dsa", "_covered_under_dsa", bool, False, PredefinedSerializer()),
  FieldMetadata("publicUiDescription", "public_ui_description", "_public_ui_description", str, "", PredefinedSerializer()),
]

