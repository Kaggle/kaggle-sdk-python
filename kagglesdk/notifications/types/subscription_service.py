from kagglesdk.kaggle_object import *
from kagglesdk.notifications.types.notifications_enums import NotificationRelatedItemType, SettingsPageMessage, SubscribeState, SubscriptionType
from typing import Optional

class GetMySubscribeStateRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    type (SubscriptionType)
  """

  def __init__(self):
    self._id = 0
    self._type = SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE
    self._freeze()

  @property
  def id(self) -> int:
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
  def type(self) -> 'SubscriptionType':
    return self._type

  @type.setter
  def type(self, type: 'SubscriptionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, SubscriptionType):
      raise TypeError('type must be of type SubscriptionType')
    self._type = type


class GetSubscribeStateResponse(KaggleObject):
  r"""
  Attributes:
    state (SubscribeState)
      What state is the subscription in (e.g. subscribed, unsubscribed).
    global_notifications_enabled (bool)
      Whether notifications are globally enabled.
  """

  def __init__(self):
    self._state = SubscribeState.INVALID
    self._global_notifications_enabled = False
    self._freeze()

  @property
  def state(self) -> 'SubscribeState':
    """What state is the subscription in (e.g. subscribed, unsubscribed)."""
    return self._state

  @state.setter
  def state(self, state: 'SubscribeState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, SubscribeState):
      raise TypeError('state must be of type SubscribeState')
    self._state = state

  @property
  def global_notifications_enabled(self) -> bool:
    """Whether notifications are globally enabled."""
    return self._global_notifications_enabled

  @global_notifications_enabled.setter
  def global_notifications_enabled(self, global_notifications_enabled: bool):
    if global_notifications_enabled is None:
      del self.global_notifications_enabled
      return
    if not isinstance(global_notifications_enabled, bool):
      raise TypeError('global_notifications_enabled must be of type bool')
    self._global_notifications_enabled = global_notifications_enabled


class GetUnsubscribeFromObjectDetailsRequest(KaggleObject):
  r"""
  Attributes:
    loginless_token_guid (str)
      Loginless token to allow unsubscribing without logging in.
    token (str)
      A protected token representing the `UnsubscribeFromObjectRequest`
  """

  def __init__(self):
    self._loginless_token_guid = ""
    self._token = ""
    self._freeze()

  @property
  def loginless_token_guid(self) -> str:
    """Loginless token to allow unsubscribing without logging in."""
    return self._loginless_token_guid

  @loginless_token_guid.setter
  def loginless_token_guid(self, loginless_token_guid: str):
    if loginless_token_guid is None:
      del self.loginless_token_guid
      return
    if not isinstance(loginless_token_guid, str):
      raise TypeError('loginless_token_guid must be of type str')
    self._loginless_token_guid = loginless_token_guid

  @property
  def token(self) -> str:
    """A protected token representing the `UnsubscribeFromObjectRequest`"""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class GetUnsubscribeFromObjectDetailsResponse(KaggleObject):
  r"""
  Attributes:
    subscription_type (SubscriptionType)
      What type of subscription is this object
    name (str)
      The name of the object, used for display.
    error_message (SettingsPageMessage)
      If there is an error, this is the relevant message.
  """

  def __init__(self):
    self._subscription_type = SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE
    self._name = ""
    self._error_message = SettingsPageMessage.SETTINGS_PAGE_MESSAGE_UNSPECIFIED
    self._freeze()

  @property
  def subscription_type(self) -> 'SubscriptionType':
    """What type of subscription is this object"""
    return self._subscription_type

  @subscription_type.setter
  def subscription_type(self, subscription_type: 'SubscriptionType'):
    if subscription_type is None:
      del self.subscription_type
      return
    if not isinstance(subscription_type, SubscriptionType):
      raise TypeError('subscription_type must be of type SubscriptionType')
    self._subscription_type = subscription_type

  @property
  def name(self) -> str:
    """The name of the object, used for display."""
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
  def error_message(self) -> 'SettingsPageMessage':
    """If there is an error, this is the relevant message."""
    return self._error_message

  @error_message.setter
  def error_message(self, error_message: 'SettingsPageMessage'):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, SettingsPageMessage):
      raise TypeError('error_message must be of type SettingsPageMessage')
    self._error_message = error_message


class LoginlessUnsubscribeFromObjectRequest(KaggleObject):
  r"""
  Attributes:
    loginless_token_guid (str)
      Loginless token to allow unsubscribing without logging in.
    token (str)
      A protected token representing the `UnsubscribeFromObjectRequest`
  """

  def __init__(self):
    self._loginless_token_guid = ""
    self._token = ""
    self._freeze()

  @property
  def loginless_token_guid(self) -> str:
    """Loginless token to allow unsubscribing without logging in."""
    return self._loginless_token_guid

  @loginless_token_guid.setter
  def loginless_token_guid(self, loginless_token_guid: str):
    if loginless_token_guid is None:
      del self.loginless_token_guid
      return
    if not isinstance(loginless_token_guid, str):
      raise TypeError('loginless_token_guid must be of type str')
    self._loginless_token_guid = loginless_token_guid

  @property
  def token(self) -> str:
    """A protected token representing the `UnsubscribeFromObjectRequest`"""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class LoginlessUnsubscribeFromObjectResponse(KaggleObject):
  r"""
  Attributes:
    message (SettingsPageMessage)
      The message indicating the result.
  """

  def __init__(self):
    self._message = SettingsPageMessage.SETTINGS_PAGE_MESSAGE_UNSPECIFIED
    self._freeze()

  @property
  def message(self) -> 'SettingsPageMessage':
    """The message indicating the result."""
    return self._message

  @message.setter
  def message(self, message: 'SettingsPageMessage'):
    if message is None:
      del self.message
      return
    if not isinstance(message, SettingsPageMessage):
      raise TypeError('message must be of type SettingsPageMessage')
    self._message = message


class SubscribeToRequest(KaggleObject):
  r"""
  Attributes:
    subscribe (SubscribeState)
    is_implicit (bool)
      Is the user being subscribed implicitly (e.g. as a result of commenting) or
      explicitly (as a result of them clicking follow) Implicit subscription
      never overwrites explicit unsubscribing
    id (int)
    type (SubscriptionType)
    parent_type (NotificationRelatedItemType)
    parent_id (int)
  """

  def __init__(self):
    self._subscribe = SubscribeState.INVALID
    self._is_implicit = False
    self._id = None
    self._type = SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE
    self._parent_type = NotificationRelatedItemType.NOTIFICATION_RELATED_ITEM_TYPE_UNSPECIFIED
    self._parent_id = None
    self._freeze()

  @property
  def subscribe(self) -> 'SubscribeState':
    return self._subscribe

  @subscribe.setter
  def subscribe(self, subscribe: 'SubscribeState'):
    if subscribe is None:
      del self.subscribe
      return
    if not isinstance(subscribe, SubscribeState):
      raise TypeError('subscribe must be of type SubscribeState')
    self._subscribe = subscribe

  @property
  def is_implicit(self) -> bool:
    r"""
    Is the user being subscribed implicitly (e.g. as a result of commenting) or
    explicitly (as a result of them clicking follow) Implicit subscription
    never overwrites explicit unsubscribing
    """
    return self._is_implicit

  @is_implicit.setter
  def is_implicit(self, is_implicit: bool):
    if is_implicit is None:
      del self.is_implicit
      return
    if not isinstance(is_implicit, bool):
      raise TypeError('is_implicit must be of type bool')
    self._is_implicit = is_implicit

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def type(self) -> 'SubscriptionType':
    return self._type

  @type.setter
  def type(self, type: 'SubscriptionType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, SubscriptionType):
      raise TypeError('type must be of type SubscriptionType')
    self._type = type

  @property
  def parent_type(self) -> 'NotificationRelatedItemType':
    return self._parent_type

  @parent_type.setter
  def parent_type(self, parent_type: 'NotificationRelatedItemType'):
    if parent_type is None:
      del self.parent_type
      return
    if not isinstance(parent_type, NotificationRelatedItemType):
      raise TypeError('parent_type must be of type NotificationRelatedItemType')
    self._parent_type = parent_type

  @property
  def parent_id(self) -> int:
    return self._parent_id or 0

  @parent_id.setter
  def parent_id(self, parent_id: Optional[int]):
    if parent_id is None:
      del self.parent_id
      return
    if not isinstance(parent_id, int):
      raise TypeError('parent_id must be of type int')
    self._parent_id = parent_id


GetMySubscribeStateRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", SubscriptionType, SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE, EnumSerializer()),
]

GetSubscribeStateResponse._fields = [
  FieldMetadata("state", "state", "_state", SubscribeState, SubscribeState.INVALID, EnumSerializer()),
  FieldMetadata("globalNotificationsEnabled", "global_notifications_enabled", "_global_notifications_enabled", bool, False, PredefinedSerializer()),
]

GetUnsubscribeFromObjectDetailsRequest._fields = [
  FieldMetadata("loginlessTokenGuid", "loginless_token_guid", "_loginless_token_guid", str, "", PredefinedSerializer()),
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

GetUnsubscribeFromObjectDetailsResponse._fields = [
  FieldMetadata("subscriptionType", "subscription_type", "_subscription_type", SubscriptionType, SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE, EnumSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", SettingsPageMessage, SettingsPageMessage.SETTINGS_PAGE_MESSAGE_UNSPECIFIED, EnumSerializer()),
]

LoginlessUnsubscribeFromObjectRequest._fields = [
  FieldMetadata("loginlessTokenGuid", "loginless_token_guid", "_loginless_token_guid", str, "", PredefinedSerializer()),
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

LoginlessUnsubscribeFromObjectResponse._fields = [
  FieldMetadata("message", "message", "_message", SettingsPageMessage, SettingsPageMessage.SETTINGS_PAGE_MESSAGE_UNSPECIFIED, EnumSerializer()),
]

SubscribeToRequest._fields = [
  FieldMetadata("subscribe", "subscribe", "_subscribe", SubscribeState, SubscribeState.INVALID, EnumSerializer()),
  FieldMetadata("isImplicit", "is_implicit", "_is_implicit", bool, False, PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("type", "type", "_type", SubscriptionType, SubscriptionType.SUBSCRIPTION_TYPE_NOT_APPLICABLE, EnumSerializer()),
  FieldMetadata("parentType", "parent_type", "_parent_type", NotificationRelatedItemType, NotificationRelatedItemType.NOTIFICATION_RELATED_ITEM_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("parentId", "parent_id", "_parent_id", int, None, PredefinedSerializer(), optional=True),
]

