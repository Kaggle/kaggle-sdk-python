from kagglesdk.common.types.http_redirect import HttpRedirect
from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.notifications.types.notifications_service import AddTestNotificationRequest, AddTestNotificationResponse, GetUserNotificationSettingsRequest, GetUserNotificationSettingsResponse, GetUserNotificationsRequest, GetUserNotificationsResponse, MarkAllNotificationsRequest, MarkNotificationsRequest, OpenNotificationRequest, SetUserNotificationSettingsRequest

class NotificationsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def mark_notifications(self, request: MarkNotificationsRequest = None):
    r"""
    Set the read or viewed status on a single notification or many
    notifications.

    Args:
      request (MarkNotificationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MarkNotificationsRequest()

    self._client.call("notifications.NotificationsService", "MarkNotifications", request, None)

  def get_user_notifications(self, request: GetUserNotificationsRequest = None) -> GetUserNotificationsResponse:
    r"""
    Get the list of notifications for the current user.

    Args:
      request (GetUserNotificationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserNotificationsRequest()

    return self._client.call("notifications.NotificationsService", "GetUserNotifications", request, GetUserNotificationsResponse)

  def add_test_notification(self, request: AddTestNotificationRequest = None) -> AddTestNotificationResponse:
    r"""
    directly creates a new notification in the notification table and sends
    email.

    Args:
      request (AddTestNotificationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddTestNotificationRequest()

    return self._client.call("notifications.NotificationsService", "AddTestNotification", request, AddTestNotificationResponse)

  def mark_all_notifications(self, request: MarkAllNotificationsRequest = None):
    r"""
    Mark all notification as (read|viewed) for a user.

    Args:
      request (MarkAllNotificationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MarkAllNotificationsRequest()

    self._client.call("notifications.NotificationsService", "MarkAllNotifications", request, None)

  def open_notification(self, request: OpenNotificationRequest = None) -> HttpRedirect:
    r"""
    'Open' a notification, visiting the target url, and taking the requested
    action.

    Args:
      request (OpenNotificationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = OpenNotificationRequest()

    return self._client.call("notifications.NotificationsService", "OpenNotification", request, HttpRedirect)

  def set_user_notification_settings(self, request: SetUserNotificationSettingsRequest = None):
    r"""
    Set the notification settings to the given settings, only updating any
    values that are actually set

    Args:
      request (SetUserNotificationSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetUserNotificationSettingsRequest()

    self._client.call("notifications.NotificationsService", "SetUserNotificationSettings", request, None)

  def get_user_notification_settings(self, request: GetUserNotificationSettingsRequest = None) -> GetUserNotificationSettingsResponse:
    r"""
    Retrieves the current user's notification settings, providing defaults if
    user hasn't set a value

    Args:
      request (GetUserNotificationSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserNotificationSettingsRequest()

    return self._client.call("notifications.NotificationsService", "GetUserNotificationSettings", request, GetUserNotificationSettingsResponse)
