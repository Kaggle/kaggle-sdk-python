from kagglesdk.community.types.badges_admin_service import BadgeConfig, BadgeStats, BatchCreateBadgeRecipientsRequest, BatchCreateBadgeRecipientsResponse, BatchDeleteBadgeRecipientsRequest, CreateBadgeRecipientRequest, DeleteBadgeConfigRequest, GetBadgeConfigRequest, GetBadgeRecipientsStatusRequest, GetBadgeRecipientsStatusResponse, GetBadgeStatsRequest, ListBadgeConfigsRequest, ListBadgeConfigsResponse, SyncBigQueryBadgeRequest, SyncBigQueryBadgeResponse, TestBigQueryBadgeRequest, TestBigQueryBadgeResponse, UpdateBadgeConfigRequest, UpdateBadgeRecipientRequest
from kagglesdk.community.types.badges_service import BadgeRecipient
from kagglesdk.kaggle_http_client import KaggleHttpClient

class BadgesAdminClient(object):
  """A service to configure and manage badges"""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_badge_config(self, request: GetBadgeConfigRequest = None) -> BadgeConfig:
    r"""
    Gets the full definition of a badge, everything that can be configured.

    Args:
      request (GetBadgeConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBadgeConfigRequest()

    return self._client.call("community.BadgesAdminService", "GetBadgeConfig", request, BadgeConfig)

  def get_badge_stats(self, request: GetBadgeStatsRequest = None) -> BadgeStats:
    r"""
    Args:
      request (GetBadgeStatsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBadgeStatsRequest()

    return self._client.call("community.BadgesAdminService", "GetBadgeStats", request, BadgeStats)

  def list_badge_configs(self, request: ListBadgeConfigsRequest = None) -> ListBadgeConfigsResponse:
    r"""
    Lists the full definition of all badges.

    Args:
      request (ListBadgeConfigsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListBadgeConfigsRequest()

    return self._client.call("community.BadgesAdminService", "ListBadgeConfigs", request, ListBadgeConfigsResponse)

  def update_badge_config(self, request: UpdateBadgeConfigRequest = None) -> BadgeConfig:
    r"""
    Updates the configuration for a badge, or create a new one.

    Args:
      request (UpdateBadgeConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBadgeConfigRequest()

    return self._client.call("community.BadgesAdminService", "UpdateBadgeConfig", request, BadgeConfig)

  def delete_badge_config(self, request: DeleteBadgeConfigRequest = None):
    r"""
    Deletes a badge including all associated data. Should be rarely done

    Args:
      request (DeleteBadgeConfigRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteBadgeConfigRequest()

    self._client.call("community.BadgesAdminService", "DeleteBadgeConfig", request, None)

  def get_badge_recipients_status(self, request: GetBadgeRecipientsStatusRequest = None) -> GetBadgeRecipientsStatusResponse:
    r"""
    Args:
      request (GetBadgeRecipientsStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetBadgeRecipientsStatusRequest()

    return self._client.call("community.BadgesAdminService", "GetBadgeRecipientsStatus", request, GetBadgeRecipientsStatusResponse)

  def create_badge_recipient(self, request: CreateBadgeRecipientRequest = None) -> BadgeRecipient:
    r"""
    Create a recipient of the badge (give the user the badge).

    Args:
      request (CreateBadgeRecipientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateBadgeRecipientRequest()

    return self._client.call("community.BadgesAdminService", "CreateBadgeRecipient", request, BadgeRecipient)

  def batch_create_badge_recipients(self, request: BatchCreateBadgeRecipientsRequest = None) -> BatchCreateBadgeRecipientsResponse:
    r"""
    Creates multiple recipients for a badge.

    Args:
      request (BatchCreateBadgeRecipientsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchCreateBadgeRecipientsRequest()

    return self._client.call("community.BadgesAdminService", "BatchCreateBadgeRecipients", request, BatchCreateBadgeRecipientsResponse)

  def update_badge_recipient(self, request: UpdateBadgeRecipientRequest = None) -> BadgeRecipient:
    r"""
    Update details for the receipt of a badge.

    Args:
      request (UpdateBadgeRecipientRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBadgeRecipientRequest()

    return self._client.call("community.BadgesAdminService", "UpdateBadgeRecipient", request, BadgeRecipient)

  def batch_delete_badge_recipient_request(self, request: BatchDeleteBadgeRecipientsRequest = None):
    r"""
    Remove badge recipients (unassign the badge).

    Args:
      request (BatchDeleteBadgeRecipientsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteBadgeRecipientsRequest()

    self._client.call("community.BadgesAdminService", "BatchDeleteBadgeRecipientRequest", request, None)

  def sync_big_query_badge(self, request: SyncBigQueryBadgeRequest = None) -> SyncBigQueryBadgeResponse:
    r"""
    Runs the configured bigquery to find new/updated recipients for a given
    badge. Runs a single batch's worth of updates.

    Args:
      request (SyncBigQueryBadgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SyncBigQueryBadgeRequest()

    return self._client.call("community.BadgesAdminService", "SyncBigQueryBadge", request, SyncBigQueryBadgeResponse)

  def test_big_query_badge(self, request: TestBigQueryBadgeRequest = None) -> TestBigQueryBadgeResponse:
    r"""
    Used to test the connection to bigquery and the query/view

    Args:
      request (TestBigQueryBadgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TestBigQueryBadgeRequest()

    return self._client.call("community.BadgesAdminService", "TestBigQueryBadge", request, TestBigQueryBadgeResponse)
