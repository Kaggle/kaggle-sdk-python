from kagglesdk.kaggle_object import *
from typing import Optional

class AddOrganizationMemberRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to add a member to
    user_id (int)
    user_name (str)
  """

  def __init__(self):
    self._organization_id = 0
    self._user_id = None
    self._user_name = None
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to add a member to"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    del self.user_name
    self._user_id = user_id

  @property
  def user_name(self) -> str:
    return self._user_name or ""

  @user_name.setter
  def user_name(self, user_name: str):
    if user_name is None:
      del self.user_name
      return
    if not isinstance(user_name, str):
      raise TypeError('user_name must be of type str')
    del self.user_id
    self._user_name = user_name


AddOrganizationMemberRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("userName", "user_name", "_user_name", str, None, PredefinedSerializer(), optional=True),
]

