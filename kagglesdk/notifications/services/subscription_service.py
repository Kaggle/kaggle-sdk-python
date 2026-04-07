from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.notifications.types.subscription_service import GetMySubscribeStateRequest, GetSubscribeStateResponse, GetUnsubscribeFromObjectDetailsRequest, GetUnsubscribeFromObjectDetailsResponse, LoginlessUnsubscribeFromObjectRequest, LoginlessUnsubscribeFromObjectResponse, SubscribeToRequest

class SubscriptionClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_my_subscribe_state(self, request: GetMySubscribeStateRequest = None) -> GetSubscribeStateResponse:
    r"""
    Args:
      request (GetMySubscribeStateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetMySubscribeStateRequest()

    return self._client.call("notifications.SubscriptionService", "GetMySubscribeState", request, GetSubscribeStateResponse)

  def subscribe_to(self, request: SubscribeToRequest = None):
    r"""
    Args:
      request (SubscribeToRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SubscribeToRequest()

    self._client.call("notifications.SubscriptionService", "SubscribeTo", request, None)

  def loginless_unsubscribe_from_object(self, request: LoginlessUnsubscribeFromObjectRequest = None) -> LoginlessUnsubscribeFromObjectResponse:
    r"""
    Args:
      request (LoginlessUnsubscribeFromObjectRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = LoginlessUnsubscribeFromObjectRequest()

    return self._client.call("notifications.SubscriptionService", "LoginlessUnsubscribeFromObject", request, LoginlessUnsubscribeFromObjectResponse)

  def get_unsubscribe_from_object_details(self, request: GetUnsubscribeFromObjectDetailsRequest = None) -> GetUnsubscribeFromObjectDetailsResponse:
    r"""
    Args:
      request (GetUnsubscribeFromObjectDetailsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUnsubscribeFromObjectDetailsRequest()

    return self._client.call("notifications.SubscriptionService", "GetUnsubscribeFromObjectDetails", request, GetUnsubscribeFromObjectDetailsResponse)
