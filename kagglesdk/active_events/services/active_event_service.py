from kagglesdk.active_events.types.active_event import ActiveEvent
from kagglesdk.active_events.types.active_event_service import DeleteActiveEventRequest, DummyActiveEventRequest, GetActiveEventsFirebaseConfigRequest, GetActiveEventsFirebaseConfigResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class ActiveEventClient(object):
  """See go/kaggle-active-events-guide for how to add a new active event."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def delete_active_event(self, request: DeleteActiveEventRequest = None):
    r"""
    DeleteActiveEvent deletes the specified ActiveEvent from firestore under
    the current user.

    Args:
      request (DeleteActiveEventRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteActiveEventRequest()

    self._client.call("active_events.ActiveEventService", "DeleteActiveEvent", request, None)

  def get_active_events_firebase_config(self, request: GetActiveEventsFirebaseConfigRequest = None) -> GetActiveEventsFirebaseConfigResponse:
    r"""
    Args:
      request (GetActiveEventsFirebaseConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetActiveEventsFirebaseConfigRequest()

    return self._client.call("active_events.ActiveEventService", "GetActiveEventsFirebaseConfig", request, GetActiveEventsFirebaseConfigResponse)

  def dummy_active_event(self, request: DummyActiveEventRequest = None) -> ActiveEvent:
    r"""
    Dummy rpc to generate Wire3 format fromJson/toJson typescript methods.
    These methods are used to deserialize enum from Firestore in the frontend.

    Args:
      request (DummyActiveEventRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DummyActiveEventRequest()

    return self._client.call("active_events.ActiveEventService", "DummyActiveEvent", request, ActiveEvent)
