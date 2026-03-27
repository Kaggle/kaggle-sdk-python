from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.moderation_public_service import ListViolationDescriptionsRequest, ListViolationDescriptionsResponse

class ModerationPublicClient(object):
  """Publicly accessible moderation service (as opposed to the admin-only one)."""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def list_violation_descriptions(self, request: ListViolationDescriptionsRequest = None) -> ListViolationDescriptionsResponse:
    r"""
    Args:
      request (ListViolationDescriptionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListViolationDescriptionsRequest()

    return self._client.call("users.ModerationPublicService", "ListViolationDescriptions", request, ListViolationDescriptionsResponse)
