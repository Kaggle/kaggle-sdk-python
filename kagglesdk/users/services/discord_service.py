from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.discord_service import DeleteDiscordInfoRequest, GetDiscordInfoRequest, GetDiscordInfoResponse, SyncDiscordUserRequest

class DiscordClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_discord_info(self, request: GetDiscordInfoRequest = None) -> GetDiscordInfoResponse:
    r"""
    Get the discord information related to a user (if any).

    Args:
      request (GetDiscordInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDiscordInfoRequest()

    return self._client.call("users.DiscordService", "GetDiscordInfo", request, GetDiscordInfoResponse)

  def delete_discord_info(self, request: DeleteDiscordInfoRequest = None):
    r"""
    Delete the discord information related to a user, unlinking the accounts.

    Args:
      request (DeleteDiscordInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteDiscordInfoRequest()

    self._client.call("users.DiscordService", "DeleteDiscordInfo", request, None)

  def sync_discord_user(self, request: SyncDiscordUserRequest = None):
    r"""
    Syncs a user to discord, e.g. grant roles and change nickname.

    Args:
      request (SyncDiscordUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SyncDiscordUserRequest()

    self._client.call("users.DiscordService", "SyncDiscordUser", request, None)
