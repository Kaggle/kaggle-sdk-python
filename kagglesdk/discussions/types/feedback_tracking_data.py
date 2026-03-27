from kagglesdk.discussions.types.discussions_enums import FollowUpStatus
from kagglesdk.kaggle_object import *
from typing import Optional

class FeedbackTrackingData(KaggleObject):
  r"""
  This is serialized/deserialized to the database using JsonConvert. Ensure
  backward compatibility with existing data when adding/removing/changing
  fields.

  Attributes:
    buganizer_id (int)
    follow_up_status (FollowUpStatus)
  """

  def __init__(self):
    self._buganizer_id = None
    self._follow_up_status = FollowUpStatus.NONE
    self._freeze()

  @property
  def buganizer_id(self) -> int:
    return self._buganizer_id or 0

  @buganizer_id.setter
  def buganizer_id(self, buganizer_id: Optional[int]):
    if buganizer_id is None:
      del self.buganizer_id
      return
    if not isinstance(buganizer_id, int):
      raise TypeError('buganizer_id must be of type int')
    self._buganizer_id = buganizer_id

  @property
  def follow_up_status(self) -> 'FollowUpStatus':
    return self._follow_up_status

  @follow_up_status.setter
  def follow_up_status(self, follow_up_status: 'FollowUpStatus'):
    if follow_up_status is None:
      del self.follow_up_status
      return
    if not isinstance(follow_up_status, FollowUpStatus):
      raise TypeError('follow_up_status must be of type FollowUpStatus')
    self._follow_up_status = follow_up_status


FeedbackTrackingData._fields = [
  FieldMetadata("buganizerId", "buganizer_id", "_buganizer_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("followUpStatus", "follow_up_status", "_follow_up_status", FollowUpStatus, FollowUpStatus.NONE, EnumSerializer()),
]

