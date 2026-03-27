from kagglesdk.discussions.types.writeup_types import WriteUp, WriteUpLinkMetadata
from kagglesdk.discussions.types.writeups_service import BatchForceUpdateWriteUpContentStateRequest, BatchForceUpdateWriteUpContentStateResponse, CopyWriteUpRequest, CreateWriteUpRequest, DeleteWriteUpRequest, GetWriteUpBySlugRequest, GetWriteUpByTopicIdRequest, GetWriteUpLinkMetadataRequest, GetWriteUpRequest, ToggleBetweenCompetitionSolutionAndForumTopicRequest, ToggleBetweenCompetitionSolutionAndForumTopicResponse, UpdateWriteUpRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class WriteUpsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_write_up(self, request: CreateWriteUpRequest = None) -> WriteUp:
    r"""
    Creates a new WriteUp

    Args:
      request (CreateWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateWriteUpRequest()

    return self._client.call("discussions.WriteUpsService", "CreateWriteUp", request, WriteUp)

  def update_write_up(self, request: UpdateWriteUpRequest = None) -> WriteUp:
    r"""
    Updates an existing WriteUp by ID

    Args:
      request (UpdateWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateWriteUpRequest()

    return self._client.call("discussions.WriteUpsService", "UpdateWriteUp", request, WriteUp)

  def delete_write_up(self, request: DeleteWriteUpRequest = None):
    r"""
    Deletes a WriteUp

    Args:
      request (DeleteWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteWriteUpRequest()

    self._client.call("discussions.WriteUpsService", "DeleteWriteUp", request, None)

  def get_write_up_by_id(self, request: GetWriteUpRequest = None) -> WriteUp:
    r"""
    Gets an existing WriteUp by ID

    Args:
      request (GetWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetWriteUpRequest()

    return self._client.call("discussions.WriteUpsService", "GetWriteUpById", request, WriteUp)

  def get_write_up_by_slug(self, request: GetWriteUpBySlugRequest = None) -> WriteUp:
    r"""
    Gets an existing WriteUp by slug

    Args:
      request (GetWriteUpBySlugRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetWriteUpBySlugRequest()

    return self._client.call("discussions.WriteUpsService", "GetWriteUpBySlug", request, WriteUp)

  def get_write_up_by_topic_id(self, request: GetWriteUpByTopicIdRequest = None) -> WriteUp:
    r"""
    Gets an existing WriteUp by topic id

    Args:
      request (GetWriteUpByTopicIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetWriteUpByTopicIdRequest()

    return self._client.call("discussions.WriteUpsService", "GetWriteUpByTopicId", request, WriteUp)

  def get_write_up_link_metadata(self, request: GetWriteUpLinkMetadataRequest = None) -> WriteUpLinkMetadata:
    r"""
    Gets a WriteUpLink's metadata information to be used to create/update a
    WriteUpLink

    Args:
      request (GetWriteUpLinkMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetWriteUpLinkMetadataRequest()

    return self._client.call("discussions.WriteUpsService", "GetWriteUpLinkMetadata", request, WriteUpLinkMetadata)

  def toggle_between_competition_solution_and_forum_topic(self, request: ToggleBetweenCompetitionSolutionAndForumTopicRequest = None) -> ToggleBetweenCompetitionSolutionAndForumTopicResponse:
    r"""
    Converts a specified competition solution forum topic into a WriteUp

    Args:
      request (ToggleBetweenCompetitionSolutionAndForumTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ToggleBetweenCompetitionSolutionAndForumTopicRequest()

    return self._client.call("discussions.WriteUpsService", "ToggleBetweenCompetitionSolutionAndForumTopic", request, ToggleBetweenCompetitionSolutionAndForumTopicResponse)

  def batch_force_update_write_up_content_state(self, request: BatchForceUpdateWriteUpContentStateRequest = None) -> BatchForceUpdateWriteUpContentStateResponse:
    r"""
    Updates one or more Writeups ContentState, via underlying ForumTopic.
    If a Hackathon Writeup is provided, and the target content state is to be
    published / submitted, we will also populate the license and authors
    columns on the WriteUp table.

    Args:
      request (BatchForceUpdateWriteUpContentStateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchForceUpdateWriteUpContentStateRequest()

    return self._client.call("discussions.WriteUpsService", "BatchForceUpdateWriteUpContentState", request, BatchForceUpdateWriteUpContentStateResponse)

  def copy_write_up(self, request: CopyWriteUpRequest = None) -> WriteUp:
    r"""
    Deep-copies a WriteUp and its associated entities (ForumTopic, links,
    assets).

    Args:
      request (CopyWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CopyWriteUpRequest()

    return self._client.call("discussions.WriteUpsService", "CopyWriteUp", request, WriteUp)
