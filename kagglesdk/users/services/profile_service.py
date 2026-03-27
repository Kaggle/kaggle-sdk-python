from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.profile_service import CreateProfilePinRequest, DeleteProfilePinRequest, DiscussionCounts, GetProfilePreviewRequest, GetProfilePreviewResponse, GetProfileRequest, GetProfileResponse, GetUserActivityRequest, GetUserActivityResponse, GetUserDiscussionCountsRequest, GetUserWriteUpCountsRequest, ListFollowersRequest, ListFollowersResponse, ListProfilePinsRequest, ListProfilePinsResponse, UpdateBioRequest, UpdateBioResponse, UpdateCompetitionProfileVisibilityRequest, UpdateProfileImageRequest, UpdateProfileImageResponse, UpdateProfileRequest, UpdateProfileResponse, UpdateProfileSectionOrderRequest, UpdateProfileVisibilityRequest, WriteUpCounts

class ProfileClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def update_bio(self, request: UpdateBioRequest = None) -> UpdateBioResponse:
    r"""
    Updates a user bio, which is a short message about the user.

    Args:
      request (UpdateBioRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateBioRequest()

    return self._client.call("users.ProfileService", "UpdateBio", request, UpdateBioResponse)

  def update_profile_image(self, request: UpdateProfileImageRequest = None) -> UpdateProfileImageResponse:
    r"""
    Updates the user's main profile image.

    Args:
      request (UpdateProfileImageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateProfileImageRequest()

    return self._client.call("users.ProfileService", "UpdateProfileImage", request, UpdateProfileImageResponse)

  def update_profile_visibility(self, request: UpdateProfileVisibilityRequest = None):
    r"""
    Updates current user's profile visibility settings.

    Args:
      request (UpdateProfileVisibilityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateProfileVisibilityRequest()

    self._client.call("users.ProfileService", "UpdateProfileVisibility", request, None)

  def update_profile_section_order(self, request: UpdateProfileSectionOrderRequest = None):
    r"""
    Updates the order of sections on the About tab of the user's profile.

    Args:
      request (UpdateProfileSectionOrderRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateProfileSectionOrderRequest()

    self._client.call("users.ProfileService", "UpdateProfileSectionOrder", request, None)

  def update_competition_profile_visibility(self, request: UpdateCompetitionProfileVisibilityRequest = None):
    r"""
    Updates profile visibility for current user's competitions.

    Args:
      request (UpdateCompetitionProfileVisibilityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionProfileVisibilityRequest()

    self._client.call("users.ProfileService", "UpdateCompetitionProfileVisibility", request, None)

  def update_profile(self, request: UpdateProfileRequest = None) -> UpdateProfileResponse:
    r"""
    Updates various personal information/links about a user

    Args:
      request (UpdateProfileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateProfileRequest()

    return self._client.call("users.ProfileService", "UpdateProfile", request, UpdateProfileResponse)

  def get_profile(self, request: GetProfileRequest = None) -> GetProfileResponse:
    r"""
    Gets a user's public profile information

    Args:
      request (GetProfileRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetProfileRequest()

    return self._client.call("users.ProfileService", "GetProfile", request, GetProfileResponse)

  def get_profile_preview(self, request: GetProfilePreviewRequest = None) -> GetProfilePreviewResponse:
    r"""
    Fetches information used for populating the profile preview feature.

    Args:
      request (GetProfilePreviewRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetProfilePreviewRequest()

    return self._client.call("users.ProfileService", "GetProfilePreview", request, GetProfilePreviewResponse)

  def get_user_activity(self, request: GetUserActivityRequest = None) -> GetUserActivityResponse:
    r"""
    Returns activity information for each day to populate a user's activity
    graph

    Args:
      request (GetUserActivityRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserActivityRequest()

    return self._client.call("users.ProfileService", "GetUserActivity", request, GetUserActivityResponse)

  def get_user_discussion_counts(self, request: GetUserDiscussionCountsRequest = None) -> DiscussionCounts:
    r"""
    Returns total counts of different user discussions engagement, e.g. created
    topics, replies, etc.

    Args:
      request (GetUserDiscussionCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserDiscussionCountsRequest()

    return self._client.call("users.ProfileService", "GetUserDiscussionCounts", request, DiscussionCounts)

  def create_profile_pin(self, request: CreateProfilePinRequest = None):
    r"""
    Pins a piece of content to the user's profile

    Args:
      request (CreateProfilePinRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateProfilePinRequest()

    self._client.call("users.ProfileService", "CreateProfilePin", request, None)

  def delete_profile_pin(self, request: DeleteProfilePinRequest = None):
    r"""
    Unpins a piece of content on the user's profile

    Args:
      request (DeleteProfilePinRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteProfilePinRequest()

    self._client.call("users.ProfileService", "DeleteProfilePin", request, None)

  def list_profile_pins(self, request: ListProfilePinsRequest = None) -> ListProfilePinsResponse:
    r"""
    Lists existing pins for a user's profile

    Args:
      request (ListProfilePinsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListProfilePinsRequest()

    return self._client.call("users.ProfileService", "ListProfilePins", request, ListProfilePinsResponse)

  def list_followers(self, request: ListFollowersRequest = None) -> ListFollowersResponse:
    r"""
    Lists users that follows a user, or that a user follows

    Args:
      request (ListFollowersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListFollowersRequest()

    return self._client.call("users.ProfileService", "ListFollowers", request, ListFollowersResponse)

  def get_user_write_up_counts(self, request: GetUserWriteUpCountsRequest = None) -> WriteUpCounts:
    r"""
    Gets user's WriteUp counts and stats

    Args:
      request (GetUserWriteUpCountsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserWriteUpCountsRequest()

    return self._client.call("users.ProfileService", "GetUserWriteUpCounts", request, WriteUpCounts)
