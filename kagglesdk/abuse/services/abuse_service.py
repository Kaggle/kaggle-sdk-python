from kagglesdk.abuse.types.abuse_service import AdminAllowlistEntityRequest, RemoveDatasetVersionQuarantineRequest, SetReportedDismissalRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class AbuseClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def set_reported_dismissal(self, request: SetReportedDismissalRequest = None):
    r"""
    Set dismissal state for a given entity (only applicable to notebooks /
    datasets)

    Args:
      request (SetReportedDismissalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetReportedDismissalRequest()

    self._client.call("abuse.AbuseService", "SetReportedDismissal", request, None)

  def admin_allowlist_entity(self, request: AdminAllowlistEntityRequest = None):
    r"""
    An admin only method to allowlist an entity, marking it as no longer
    moderated automatically

    Args:
      request (AdminAllowlistEntityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AdminAllowlistEntityRequest()

    self._client.call("abuse.AbuseService", "AdminAllowlistEntity", request, None)

  def remove_dataset_version_quarantine(self, request: RemoveDatasetVersionQuarantineRequest = None):
    r"""
    Removes a quarantine on a dataset version, if applicable.

    Args:
      request (RemoveDatasetVersionQuarantineRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveDatasetVersionQuarantineRequest()

    self._client.call("abuse.AbuseService", "RemoveDatasetVersionQuarantine", request, None)
