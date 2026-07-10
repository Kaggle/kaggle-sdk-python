import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class PubliclyCloneable(enum.Enum):
  PUBLICLY_CLONEABLE_UNSPECIFIED = 0
  """not cloneable"""
  PUBLICLY_CLONEABLE_WITH_PRIVATE_SOLUTION_FILE = 1
  r"""
  publicly cloneable - cloning this competition will NOT give you access to
  solution file
  """
  PUBLICLY_CLONEABLE_WITH_PUBLIC_SOLUTION_FILE = 2
  r"""
  publicly cloneable - cloning this competition will give you access to the
  solution file
  """
  PUBLICLY_CLONEABLE_ENABLE_HACKATHON_CLONING = 3
  """enables non-admin non-host users to clone a closed hackathon competition"""

class RewardTypeId(enum.Enum):
  REWARD_TYPE_ID_UNSPECIFIED = 0
  USD = 1
  KUDOS = 2
  AUD = 3
  EUR = 4
  JOBS = 5
  SWAG = 6
  GBP = 7
  KNOWLEDGE = 8
  PRIZES = 9
  NON_MONETARY = 10

class Reward(KaggleObject):
  r"""
  TODO(b/350786629): make the DB change to set RewardTypeId and rewardQuantity
  default to 0 and change rewardQuantity type from decimal to int.

  Attributes:
    id (RewardTypeId)
    quantity (int)
    clarification (str)
  """

  def __init__(self):
    self._id = RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED
    self._quantity = 0
    self._clarification = None
    self._freeze()

  @property
  def id(self) -> 'RewardTypeId':
    return self._id

  @id.setter
  def id(self, id: 'RewardTypeId'):
    if id is None:
      del self.id
      return
    if not isinstance(id, RewardTypeId):
      raise TypeError('id must be of type RewardTypeId')
    self._id = id

  @property
  def quantity(self) -> int:
    return self._quantity

  @quantity.setter
  def quantity(self, quantity: int):
    if quantity is None:
      del self.quantity
      return
    if not isinstance(quantity, int):
      raise TypeError('quantity must be of type int')
    self._quantity = quantity

  @property
  def clarification(self) -> str:
    return self._clarification or ""

  @clarification.setter
  def clarification(self, clarification: Optional[str]):
    if clarification is None:
      del self.clarification
      return
    if not isinstance(clarification, str):
      raise TypeError('clarification must be of type str')
    self._clarification = clarification


Reward._fields = [
  FieldMetadata("id", "id", "_id", RewardTypeId, RewardTypeId.REWARD_TYPE_ID_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("quantity", "quantity", "_quantity", int, 0, PredefinedSerializer()),
  FieldMetadata("clarification", "clarification", "_clarification", str, None, PredefinedSerializer(), optional=True),
]

