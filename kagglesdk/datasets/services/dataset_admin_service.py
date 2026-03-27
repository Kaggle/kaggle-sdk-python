from kagglesdk.datasets.types.dataset_admin_service import RecreateCroissantRequest, RecreateCroissantResponse, SetDatabundleVersionNotesRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DatasetAdminClient(object):
  """Site-admin Dataset functionality"""

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def recreate_croissant(self, request: RecreateCroissantRequest = None) -> RecreateCroissantResponse:
    r"""
    Args:
      request (RecreateCroissantRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecreateCroissantRequest()

    return self._client.call("datasets.DatasetAdminService", "RecreateCroissant", request, RecreateCroissantResponse)

  def set_databundle_version_notes(self, request: SetDatabundleVersionNotesRequest = None):
    r"""
    Args:
      request (SetDatabundleVersionNotesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetDatabundleVersionNotesRequest()

    self._client.call("datasets.DatasetAdminService", "SetDatabundleVersionNotes", request, None)
