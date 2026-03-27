from kagglesdk.datasets.databundles.types.databundle_service import CheckFileUploadsRequest, CheckFileUploadsResponse, GetDatabundleExternalChildrenRequest, GetDatabundleExternalChildrenResponse, GetDatabundleExternalColumnsByFirestorePathRequest, GetDatabundleExternalColumnsByFirestorePathResponse, GetDatabundleExternalColumnsRequest, GetDatabundleExternalColumnsResponse, GetDatabundleExternalRequest, GetDatabundleExternalResponse, KickoffDatabundleHasherRequest, KickoffFirestoreDeleteMigrationRequest, KickoffFirestoreWriteMigrationRequest, KickoffHandlerResponse, RestoreDatabundleVersionRequest, RestoreDatabundleVersionResponse, UpdateDatabundleMetadataExternalRequest, UpdateDatabundleMetadataExternalResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DatabundleClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_databundle_external(self, request: GetDatabundleExternalRequest = None) -> GetDatabundleExternalResponse:
    r"""
    Args:
      request (GetDatabundleExternalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleExternalRequest()

    return self._client.call("datasets.databundles.DatabundleService", "GetDatabundleExternal", request, GetDatabundleExternalResponse)

  def get_databundle_external_children(self, request: GetDatabundleExternalChildrenRequest = None) -> GetDatabundleExternalChildrenResponse:
    r"""
    Args:
      request (GetDatabundleExternalChildrenRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleExternalChildrenRequest()

    return self._client.call("datasets.databundles.DatabundleService", "GetDatabundleExternalChildren", request, GetDatabundleExternalChildrenResponse)

  def get_databundle_external_columns(self, request: GetDatabundleExternalColumnsRequest = None) -> GetDatabundleExternalColumnsResponse:
    r"""
    Args:
      request (GetDatabundleExternalColumnsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleExternalColumnsRequest()

    return self._client.call("datasets.databundles.DatabundleService", "GetDatabundleExternalColumns", request, GetDatabundleExternalColumnsResponse)

  def get_databundle_external_columns_by_firestore_path(self, request: GetDatabundleExternalColumnsByFirestorePathRequest = None) -> GetDatabundleExternalColumnsByFirestorePathResponse:
    r"""
    Args:
      request (GetDatabundleExternalColumnsByFirestorePathRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetDatabundleExternalColumnsByFirestorePathRequest()

    return self._client.call("datasets.databundles.DatabundleService", "GetDatabundleExternalColumnsByFirestorePath", request, GetDatabundleExternalColumnsByFirestorePathResponse)

  def update_databundle_metadata_external(self, request: UpdateDatabundleMetadataExternalRequest = None) -> UpdateDatabundleMetadataExternalResponse:
    r"""
    Args:
      request (UpdateDatabundleMetadataExternalRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateDatabundleMetadataExternalRequest()

    return self._client.call("datasets.databundles.DatabundleService", "UpdateDatabundleMetadataExternal", request, UpdateDatabundleMetadataExternalResponse)

  def kickoff_databundle_hasher(self, request: KickoffDatabundleHasherRequest = None) -> KickoffHandlerResponse:
    r"""
    Args:
      request (KickoffDatabundleHasherRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = KickoffDatabundleHasherRequest()

    return self._client.call("datasets.databundles.DatabundleService", "KickoffDatabundleHasher", request, KickoffHandlerResponse)

  def kickoff_firestore_write_migration(self, request: KickoffFirestoreWriteMigrationRequest = None) -> KickoffHandlerResponse:
    r"""
    Args:
      request (KickoffFirestoreWriteMigrationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = KickoffFirestoreWriteMigrationRequest()

    return self._client.call("datasets.databundles.DatabundleService", "KickoffFirestoreWriteMigration", request, KickoffHandlerResponse)

  def kickoff_firestore_delete_migration(self, request: KickoffFirestoreDeleteMigrationRequest = None) -> KickoffHandlerResponse:
    r"""
    Args:
      request (KickoffFirestoreDeleteMigrationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = KickoffFirestoreDeleteMigrationRequest()

    return self._client.call("datasets.databundles.DatabundleService", "KickoffFirestoreDeleteMigration", request, KickoffHandlerResponse)

  def restore_databundle_version(self, request: RestoreDatabundleVersionRequest = None) -> RestoreDatabundleVersionResponse:
    r"""
    Args:
      request (RestoreDatabundleVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RestoreDatabundleVersionRequest()

    return self._client.call("datasets.databundles.DatabundleService", "RestoreDatabundleVersion", request, RestoreDatabundleVersionResponse)

  def check_file_uploads(self, request: CheckFileUploadsRequest = None) -> CheckFileUploadsResponse:
    r"""
    Args:
      request (CheckFileUploadsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckFileUploadsRequest()

    return self._client.call("datasets.databundles.DatabundleService", "CheckFileUploads", request, CheckFileUploadsResponse)
