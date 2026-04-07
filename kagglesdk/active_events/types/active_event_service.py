from kagglesdk.active_events.types.active_event import ActiveEvent
from kagglesdk.kaggle_object import *
from typing import Optional

class DeleteActiveEventRequest(KaggleObject):
  r"""
  Attributes:
    event_id (str)
  """

  def __init__(self):
    self._event_id = ""
    self._freeze()

  @property
  def event_id(self) -> str:
    return self._event_id

  @event_id.setter
  def event_id(self, event_id: str):
    if event_id is None:
      del self.event_id
      return
    if not isinstance(event_id, str):
      raise TypeError('event_id must be of type str')
    self._event_id = event_id


class DummyActiveEventRequest(KaggleObject):
  r"""
  Attributes:
    event (ActiveEvent)
  """

  def __init__(self):
    self._event = None
    self._freeze()

  @property
  def event(self) -> Optional['ActiveEvent']:
    return self._event

  @event.setter
  def event(self, event: Optional['ActiveEvent']):
    if event is None:
      del self.event
      return
    if not isinstance(event, ActiveEvent):
      raise TypeError('event must be of type ActiveEvent')
    self._event = event


class FirebaseConfig(KaggleObject):
  r"""
  Attributes:
    api_key (str)
    auth_domain (str)
    database_url (str)
    project_id (str)
    storage_bucket (str)
    messaging_sender_id (str)
    app_id (str)
    proxy_domain (str)
  """

  def __init__(self):
    self._api_key = ""
    self._auth_domain = ""
    self._database_url = ""
    self._project_id = ""
    self._storage_bucket = ""
    self._messaging_sender_id = ""
    self._app_id = ""
    self._proxy_domain = ""
    self._freeze()

  @property
  def api_key(self) -> str:
    return self._api_key

  @api_key.setter
  def api_key(self, api_key: str):
    if api_key is None:
      del self.api_key
      return
    if not isinstance(api_key, str):
      raise TypeError('api_key must be of type str')
    self._api_key = api_key

  @property
  def auth_domain(self) -> str:
    return self._auth_domain

  @auth_domain.setter
  def auth_domain(self, auth_domain: str):
    if auth_domain is None:
      del self.auth_domain
      return
    if not isinstance(auth_domain, str):
      raise TypeError('auth_domain must be of type str')
    self._auth_domain = auth_domain

  @property
  def database_url(self) -> str:
    return self._database_url

  @database_url.setter
  def database_url(self, database_url: str):
    if database_url is None:
      del self.database_url
      return
    if not isinstance(database_url, str):
      raise TypeError('database_url must be of type str')
    self._database_url = database_url

  @property
  def project_id(self) -> str:
    return self._project_id

  @project_id.setter
  def project_id(self, project_id: str):
    if project_id is None:
      del self.project_id
      return
    if not isinstance(project_id, str):
      raise TypeError('project_id must be of type str')
    self._project_id = project_id

  @property
  def storage_bucket(self) -> str:
    return self._storage_bucket

  @storage_bucket.setter
  def storage_bucket(self, storage_bucket: str):
    if storage_bucket is None:
      del self.storage_bucket
      return
    if not isinstance(storage_bucket, str):
      raise TypeError('storage_bucket must be of type str')
    self._storage_bucket = storage_bucket

  @property
  def messaging_sender_id(self) -> str:
    return self._messaging_sender_id

  @messaging_sender_id.setter
  def messaging_sender_id(self, messaging_sender_id: str):
    if messaging_sender_id is None:
      del self.messaging_sender_id
      return
    if not isinstance(messaging_sender_id, str):
      raise TypeError('messaging_sender_id must be of type str')
    self._messaging_sender_id = messaging_sender_id

  @property
  def app_id(self) -> str:
    return self._app_id

  @app_id.setter
  def app_id(self, app_id: str):
    if app_id is None:
      del self.app_id
      return
    if not isinstance(app_id, str):
      raise TypeError('app_id must be of type str')
    self._app_id = app_id

  @property
  def proxy_domain(self) -> str:
    return self._proxy_domain

  @proxy_domain.setter
  def proxy_domain(self, proxy_domain: str):
    if proxy_domain is None:
      del self.proxy_domain
      return
    if not isinstance(proxy_domain, str):
      raise TypeError('proxy_domain must be of type str')
    self._proxy_domain = proxy_domain


class GetActiveEventsFirebaseConfigRequest(KaggleObject):
  r"""
  """

  pass

class GetActiveEventsFirebaseConfigResponse(KaggleObject):
  r"""
  Attributes:
    config (FirebaseConfig)
    auth_token (str)
      Custom auth token for the current user (or empty if logged out).
  """

  def __init__(self):
    self._config = None
    self._auth_token = ""
    self._freeze()

  @property
  def config(self) -> Optional['FirebaseConfig']:
    return self._config

  @config.setter
  def config(self, config: Optional['FirebaseConfig']):
    if config is None:
      del self.config
      return
    if not isinstance(config, FirebaseConfig):
      raise TypeError('config must be of type FirebaseConfig')
    self._config = config

  @property
  def auth_token(self) -> str:
    """Custom auth token for the current user (or empty if logged out)."""
    return self._auth_token

  @auth_token.setter
  def auth_token(self, auth_token: str):
    if auth_token is None:
      del self.auth_token
      return
    if not isinstance(auth_token, str):
      raise TypeError('auth_token must be of type str')
    self._auth_token = auth_token


DeleteActiveEventRequest._fields = [
  FieldMetadata("eventId", "event_id", "_event_id", str, "", PredefinedSerializer()),
]

DummyActiveEventRequest._fields = [
  FieldMetadata("event", "event", "_event", ActiveEvent, None, KaggleObjectSerializer()),
]

FirebaseConfig._fields = [
  FieldMetadata("apiKey", "api_key", "_api_key", str, "", PredefinedSerializer()),
  FieldMetadata("authDomain", "auth_domain", "_auth_domain", str, "", PredefinedSerializer()),
  FieldMetadata("databaseUrl", "database_url", "_database_url", str, "", PredefinedSerializer()),
  FieldMetadata("projectId", "project_id", "_project_id", str, "", PredefinedSerializer()),
  FieldMetadata("storageBucket", "storage_bucket", "_storage_bucket", str, "", PredefinedSerializer()),
  FieldMetadata("messagingSenderId", "messaging_sender_id", "_messaging_sender_id", str, "", PredefinedSerializer()),
  FieldMetadata("appId", "app_id", "_app_id", str, "", PredefinedSerializer()),
  FieldMetadata("proxyDomain", "proxy_domain", "_proxy_domain", str, "", PredefinedSerializer()),
]

GetActiveEventsFirebaseConfigRequest._fields = []

GetActiveEventsFirebaseConfigResponse._fields = [
  FieldMetadata("config", "config", "_config", FirebaseConfig, None, KaggleObjectSerializer()),
  FieldMetadata("authToken", "auth_token", "_auth_token", str, "", PredefinedSerializer()),
]

