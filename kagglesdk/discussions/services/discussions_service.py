from kagglesdk.discussions.types.discussions_service import BatchDeleteMessageRequest, BatchGetForumMessagesRequest, BatchGetForumMessagesResponse, CreateAttachmentRequest, CreateAttachmentResponse, CreateKernelMessageRequest, CreateKernelMessageResponse, CreateReplyRequest, CreateReplyResponse, CreateTopicRequest, CreateTopicResponse, DeleteAttachmentRequest, DeleteMessageRequest, DeleteTopicRequest, GetForumMessagesInTopicRequest, GetForumMessagesInTopicResponse, GetForumMessageUpvotesRequest, GetForumMessageUpvotesResponse, GetForumRequest, GetForumResponse, GetForumTopicByIdRequest, GetForumTopicByIdResponse, GetSiteForumsRequest, GetSiteForumsResponse, GetTopicListByForumIdRequest, GetTopicListResponse, MoveForumTopicToForumRequest, PinForumMessageRequest, ReactToForumMessageRequest, ToggleSpamMessageRequest, ToggleSpamMessageResponse, UpdateFeedbackTrackingDataRequest, UpdateForumMessageSettingsRequest, UpdateForumSettingsRequest, UpdateForumTopicSettingsRequest, UpdateIsThankYouStatusRequest, UpdateManyFeedbackTrackingDataRequest, UpdateMessageRequest, UpdateTopicRequest, VoteOnForumMessageRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class DiscussionsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_kernel_message(self, request: CreateKernelMessageRequest = None) -> CreateKernelMessageResponse:
    r"""
    Creates a comment on a kernel and returns the newly created message ID

    Args:
      request (CreateKernelMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateKernelMessageRequest()

    return self._client.call("discussions.DiscussionsService", "CreateKernelMessage", request, CreateKernelMessageResponse)

  def create_reply(self, request: CreateReplyRequest = None) -> CreateReplyResponse:
    r"""
    Creates a reply to a message and returns the newly created message ID.

    Args:
      request (CreateReplyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateReplyRequest()

    return self._client.call("discussions.DiscussionsService", "CreateReply", request, CreateReplyResponse)

  def create_topic(self, request: CreateTopicRequest = None) -> CreateTopicResponse:
    r"""
    Creates a topic on a forum and returns the newly created topic ID and
    message ID.

    Args:
      request (CreateTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTopicRequest()

    return self._client.call("discussions.DiscussionsService", "CreateTopic", request, CreateTopicResponse)

  def get_forum(self, request: GetForumRequest = None) -> GetForumResponse:
    r"""
    Args:
      request (GetForumRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetForumRequest()

    return self._client.call("discussions.DiscussionsService", "GetForum", request, GetForumResponse)

  def batch_get_forum_messages(self, request: BatchGetForumMessagesRequest = None) -> BatchGetForumMessagesResponse:
    r"""
    Get a list of forum messages by ids.

    Args:
      request (BatchGetForumMessagesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchGetForumMessagesRequest()

    return self._client.call("discussions.DiscussionsService", "BatchGetForumMessages", request, BatchGetForumMessagesResponse)

  def update_message(self, request: UpdateMessageRequest = None):
    r"""
    Updates a message's content.

    Args:
      request (UpdateMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateMessageRequest()

    self._client.call("discussions.DiscussionsService", "UpdateMessage", request, None)

  def update_topic(self, request: UpdateTopicRequest = None):
    r"""
    Updates a topic's name and message content.

    Args:
      request (UpdateTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateTopicRequest()

    self._client.call("discussions.DiscussionsService", "UpdateTopic", request, None)

  def create_attachment(self, request: CreateAttachmentRequest = None) -> CreateAttachmentResponse:
    r"""
    Creates a token & URL for use to upload a discussions attachment to blob
    storage.

    Args:
      request (CreateAttachmentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateAttachmentRequest()

    return self._client.call("discussions.DiscussionsService", "CreateAttachment", request, CreateAttachmentResponse)

  def delete_attachment(self, request: DeleteAttachmentRequest = None):
    r"""
    Deletes an attachment from a discussion post and blob storage.

    Args:
      request (DeleteAttachmentRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteAttachmentRequest()

    self._client.call("discussions.DiscussionsService", "DeleteAttachment", request, None)

  def delete_message(self, request: DeleteMessageRequest = None):
    r"""
    Args:
      request (DeleteMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteMessageRequest()

    self._client.call("discussions.DiscussionsService", "DeleteMessage", request, None)

  def batch_delete_message(self, request: BatchDeleteMessageRequest = None):
    r"""
    Args:
      request (BatchDeleteMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchDeleteMessageRequest()

    self._client.call("discussions.DiscussionsService", "BatchDeleteMessage", request, None)

  def delete_topic(self, request: DeleteTopicRequest = None):
    r"""
    Args:
      request (DeleteTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteTopicRequest()

    self._client.call("discussions.DiscussionsService", "DeleteTopic", request, None)

  def get_site_forums(self, request: GetSiteForumsRequest = None) -> GetSiteForumsResponse:
    r"""
    TODO: Update this route to do query based authorization once that is
    implemented

    Args:
      request (GetSiteForumsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetSiteForumsRequest()

    return self._client.call("discussions.DiscussionsService", "GetSiteForums", request, GetSiteForumsResponse)

  def get_topic_list_by_forum_id(self, request: GetTopicListByForumIdRequest = None) -> GetTopicListResponse:
    r"""
    TODO: Update this route to do query based authorization once that is
    implemented

    Args:
      request (GetTopicListByForumIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTopicListByForumIdRequest()

    return self._client.call("discussions.DiscussionsService", "GetTopicListByForumId", request, GetTopicListResponse)

  def toggle_spam_message(self, request: ToggleSpamMessageRequest = None) -> ToggleSpamMessageResponse:
    r"""
    Args:
      request (ToggleSpamMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ToggleSpamMessageRequest()

    return self._client.call("discussions.DiscussionsService", "ToggleSpamMessage", request, ToggleSpamMessageResponse)

  def update_forum_settings(self, request: UpdateForumSettingsRequest = None):
    r"""
    TODO: This will become ALLOW_LOGGED_IN_OR_ADMIN_IGNORING_FIELD_PERMISSIONS
    after ForumAuthorizer is refactored to not incorporate `IsAdmin` in its
    expressions.

    Args:
      request (UpdateForumSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateForumSettingsRequest()

    self._client.call("discussions.DiscussionsService", "UpdateForumSettings", request, None)

  def update_forum_topic_settings(self, request: UpdateForumTopicSettingsRequest = None):
    r"""
    TODO: This will become ALLOW_LOGGED_IN_OR_ADMIN_IGNORING_FIELD_PERMISSIONS
    after ForumAuthorizer is refactored to not incorporate `IsAdmin` in its
    expressions.

    Args:
      request (UpdateForumTopicSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateForumTopicSettingsRequest()

    self._client.call("discussions.DiscussionsService", "UpdateForumTopicSettings", request, None)

  def update_forum_message_settings(self, request: UpdateForumMessageSettingsRequest = None):
    r"""
    TODO: This will become ALLOW_LOGGED_IN_OR_ADMIN_IGNORING_FIELD_PERMISSIONS
    after ForumAuthorizer is refactored to not incorporate `IsAdmin` in its
    expressions.

    Args:
      request (UpdateForumMessageSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateForumMessageSettingsRequest()

    self._client.call("discussions.DiscussionsService", "UpdateForumMessageSettings", request, None)

  def pin_forum_message(self, request: PinForumMessageRequest = None):
    r"""
    Args:
      request (PinForumMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = PinForumMessageRequest()

    self._client.call("discussions.DiscussionsService", "PinForumMessage", request, None)

  def move_forum_topic_to_forum(self, request: MoveForumTopicToForumRequest = None):
    r"""
    Args:
      request (MoveForumTopicToForumRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MoveForumTopicToForumRequest()

    self._client.call("discussions.DiscussionsService", "MoveForumTopicToForum", request, None)

  def get_forum_message_upvotes(self, request: GetForumMessageUpvotesRequest = None) -> GetForumMessageUpvotesResponse:
    r"""
    Args:
      request (GetForumMessageUpvotesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetForumMessageUpvotesRequest()

    return self._client.call("discussions.DiscussionsService", "GetForumMessageUpvotes", request, GetForumMessageUpvotesResponse)

  def vote_on_forum_message(self, request: VoteOnForumMessageRequest = None):
    r"""
    Args:
      request (VoteOnForumMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = VoteOnForumMessageRequest()

    self._client.call("discussions.DiscussionsService", "VoteOnForumMessage", request, None)

  def react_to_forum_message(self, request: ReactToForumMessageRequest = None):
    r"""
    Args:
      request (ReactToForumMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReactToForumMessageRequest()

    self._client.call("discussions.DiscussionsService", "ReactToForumMessage", request, None)

  def get_forum_messages_in_topic(self, request: GetForumMessagesInTopicRequest = None) -> GetForumMessagesInTopicResponse:
    r"""
    Args:
      request (GetForumMessagesInTopicRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetForumMessagesInTopicRequest()

    return self._client.call("discussions.DiscussionsService", "GetForumMessagesInTopic", request, GetForumMessagesInTopicResponse)

  def update_feedback_tracking_data(self, request: UpdateFeedbackTrackingDataRequest = None):
    r"""
    Args:
      request (UpdateFeedbackTrackingDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateFeedbackTrackingDataRequest()

    self._client.call("discussions.DiscussionsService", "UpdateFeedbackTrackingData", request, None)

  def update_many_feedback_tracking_data(self, request: UpdateManyFeedbackTrackingDataRequest = None):
    r"""
    Args:
      request (UpdateManyFeedbackTrackingDataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateManyFeedbackTrackingDataRequest()

    self._client.call("discussions.DiscussionsService", "UpdateManyFeedbackTrackingData", request, None)

  def update_is_thank_you_status(self, request: UpdateIsThankYouStatusRequest = None):
    r"""
    Set whether the comment is a thank you comment or not

    Args:
      request (UpdateIsThankYouStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateIsThankYouStatusRequest()

    self._client.call("discussions.DiscussionsService", "UpdateIsThankYouStatus", request, None)

  def get_forum_topic_by_id(self, request: GetForumTopicByIdRequest = None) -> GetForumTopicByIdResponse:
    r"""
    TODO: See comment below on GetForumTopicsById

    Args:
      request (GetForumTopicByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetForumTopicByIdRequest()

    return self._client.call("discussions.DiscussionsService", "GetForumTopicById", request, GetForumTopicByIdResponse)
