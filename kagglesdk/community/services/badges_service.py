from kagglesdk.community.types.badges_service import GetBadgeRequest, GetUserBadgeRequest, ListBadgeRecipientsRequest, ListBadgeRecipientsResponse, ListBadgesRequest, ListBadgesResponse, ListUserBadgesRequest, ListUserBadgesResponse, UpdateUserBadgeRequest
from kagglesdk.community.types.badges_types import Badge, UserBadge
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BadgesClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_badge(self, request: GetBadgeRequest = None) -> Badge:
    r"""
    Gets the definition for a badge, all the publicly available information.

    Args:
      request (GetBadgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBadgeRequest()

    return self._client.call("community.BadgesService", "GetBadge", request, Badge)

  def list_user_badges(self, request: ListUserBadgesRequest = None) -> ListUserBadgesResponse:
    r"""
    Returns the list of badges for a given user. By default only shows publicly
    visible badges, but if the current user is being viewed then hidden badges
    can be included if requested.

    Args:
      request (ListUserBadgesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUserBadgesRequest()

    return self._client.call("community.BadgesService", "ListUserBadges", request, ListUserBadgesResponse)

  def list_badges(self, request: ListBadgesRequest = None) -> ListBadgesResponse:
    r"""
    Returns the list of badges and the number of users that have earned that
    badge. Only returns badges that have been issued at least once. Used for
    rendering the awards tab of the rankings page
    (http://screen/6VdPYZPvmiCD4w2).

    Args:
      request (ListBadgesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBadgesRequest()

    return self._client.call("community.BadgesService", "ListBadges", request, ListBadgesResponse)

  def list_badge_recipients(self, request: ListBadgeRecipientsRequest = None) -> ListBadgeRecipientsResponse:
    r"""
    List all the users who have received a badge.

    Args:
      request (ListBadgeRecipientsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBadgeRecipientsRequest()

    return self._client.call("community.BadgesService", "ListBadgeRecipients", request, ListBadgeRecipientsResponse)

  def update_user_badge(self, request: UpdateUserBadgeRequest = None) -> UserBadge:
    r"""
    Update information related to a user’s badge, such as whether it's hidden
    or highlighted.

    Args:
      request (UpdateUserBadgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserBadgeRequest()

    return self._client.call("community.BadgesService", "UpdateUserBadge", request, UserBadge)

  def get_user_badge(self, request: GetUserBadgeRequest = None) -> UserBadge:
    r"""
    Returns a badge earned by a particular user.

    Args:
      request (GetUserBadgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserBadgeRequest()

    return self._client.call("community.BadgesService", "GetUserBadge", request, UserBadge)
