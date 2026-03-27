import enum
from kagglesdk.common.types.common_types import KaggleEntityType
from kagglesdk.kaggle_object import *
from typing import Optional

class ReportedDismissalType(enum.Enum):
  REPORTED_DISMISSAL_TYPE_UNSPECIFIED = 0
  BANNER = 1
  MODAL = 2

class AdminAllowlistEntityRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (int)
      The entity ID to allowlist
    entity_type (KaggleEntityType)
      The entity type of the allowlisted entity
  """

  def __init__(self):
    self._entity_id = 0
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def entity_id(self) -> int:
    """The entity ID to allowlist"""
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
  def entity_type(self) -> 'KaggleEntityType':
    """The entity type of the allowlisted entity"""
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleEntityType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type


class RemoveDatasetVersionQuarantineRequest(KaggleObject):
  r"""
  Attributes:
    dataset_version_id (int)
      The dataset version to unquarantine
    reason (str)
      Admin reasoning for the quarantine removal
  """

  def __init__(self):
    self._dataset_version_id = 0
    self._reason = None
    self._freeze()

  @property
  def dataset_version_id(self) -> int:
    """The dataset version to unquarantine"""
    return self._dataset_version_id

  @dataset_version_id.setter
  def dataset_version_id(self, dataset_version_id: int):
    if dataset_version_id is None:
      del self.dataset_version_id
      return
    if not isinstance(dataset_version_id, int):
      raise TypeError('dataset_version_id must be of type int')
    self._dataset_version_id = dataset_version_id

  @property
  def reason(self) -> str:
    """Admin reasoning for the quarantine removal"""
    return self._reason or ""

  @reason.setter
  def reason(self, reason: Optional[str]):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class SetReportedDismissalRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (int)
      The ID for the entity to dismiss
    entity_type (KaggleEntityType)
      The type for the entity to dismiss
    is_dismissed (bool)
      The value to set dismissal to
    dismissal_type (ReportedDismissalType)
      Whether we're dismissing a banner or a modal
  """

  def __init__(self):
    self._entity_id = 0
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._is_dismissed = False
    self._dismissal_type = ReportedDismissalType.REPORTED_DISMISSAL_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def entity_id(self) -> int:
    """The ID for the entity to dismiss"""
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
  def entity_type(self) -> 'KaggleEntityType':
    """The type for the entity to dismiss"""
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
  def is_dismissed(self) -> bool:
    """The value to set dismissal to"""
    return self._is_dismissed

  @is_dismissed.setter
  def is_dismissed(self, is_dismissed: bool):
    if is_dismissed is None:
      del self.is_dismissed
      return
    if not isinstance(is_dismissed, bool):
      raise TypeError('is_dismissed must be of type bool')
    self._is_dismissed = is_dismissed

  @property
  def dismissal_type(self) -> 'ReportedDismissalType':
    """Whether we're dismissing a banner or a modal"""
    return self._dismissal_type

  @dismissal_type.setter
  def dismissal_type(self, dismissal_type: 'ReportedDismissalType'):
    if dismissal_type is None:
      del self.dismissal_type
      return
    if not isinstance(dismissal_type, ReportedDismissalType):
      raise TypeError('dismissal_type must be of type ReportedDismissalType')
    self._dismissal_type = dismissal_type


AdminAllowlistEntityRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
]

RemoveDatasetVersionQuarantineRequest._fields = [
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, None, PredefinedSerializer(), optional=True),
]

SetReportedDismissalRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isDismissed", "is_dismissed", "_is_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("dismissalType", "dismissal_type", "_dismissal_type", ReportedDismissalType, ReportedDismissalType.REPORTED_DISMISSAL_TYPE_UNSPECIFIED, EnumSerializer()),
]

