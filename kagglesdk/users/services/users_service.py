from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.users.types.user import User
from kagglesdk.users.types.user_avatar import UserAvatar
from kagglesdk.users.types.users_service import AcceptCookiesRequest, ActivateAccountRequest, CreateUserMessageRequest, CreateUserMessageResponse, DeletePhoneVerificationsRequest, FollowUserRequest, FollowUserResponse, GetClientFeatureFlagsRequest, GetClientFeatureFlagsResponse, GetContactUserInfoRequest, GetContactUserInfoResponse, GetCurrentUserIdRequest, GetCurrentUserIdResponse, GetCurrentUserRequest, GetCurrentUserThemeRequest, GetCurrentUserThemeResponse, GetHomepageStatsDismissedStatusRequest, GetHomepageStatsDismissedStatusResponse, GetMyAttributesRequest, GetMyAttributesResponse, GetOnboardingDismissedStatusRequest, GetOnboardingDismissedStatusResponse, GetUploadWarningDismissedRequest, GetUploadWarningDismissedResponse, GetUserAvatarRequest, GetUserCountRequest, GetUserCountResponse, GetUserEmojiSkinToneRequest, GetUserEmojiSkinToneResponse, GetUserRequest, MigrateTermsAcceptancesRequest, MigrateTermsAcceptancesResponse, SearchOrganizationsRequest, SearchOrganizationsResponse, SearchPlacesRequest, SearchPlacesResponse, SearchUsersSuggestionsRequest, SearchUsersSuggestionsResponse, SetMyAttributesRequest, SetPhoneReputableRequest, SetUploadWarningDismissedRequest, UnfollowUserRequest, UnfollowUserResponse, UnsubscribeNewsletterRequest, UpdateCurrentUserThemeRequest, UpdateHomepageStatsDismissedStatusRequest, UpdateOnboardingDismissedStatusRequest, UpdateUserEmojiSkinToneRequest, UpdateUsersModelProxyQuotaGroupRequest, UpdateUsersModelProxyQuotaGroupResponse

class UsersClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def accept_cookies(self, request: AcceptCookiesRequest = None):
    r"""
    Args:
      request (AcceptCookiesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AcceptCookiesRequest()

    self._client.call("users.UsersService", "AcceptCookies", request, None)

  def activate_account(self, request: ActivateAccountRequest = None):
    r"""
    Args:
      request (ActivateAccountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ActivateAccountRequest()

    self._client.call("users.UsersService", "ActivateAccount", request, None)

  def get_client_feature_flags(self, request: GetClientFeatureFlagsRequest = None) -> GetClientFeatureFlagsResponse:
    r"""
    Returns all client feature flags for the current user. This is used by the
    frontend to fetch feature flags on page load, cached locally using the hash
    from the session cookie.

    Args:
      request (GetClientFeatureFlagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetClientFeatureFlagsRequest()

    return self._client.call("users.UsersService", "GetClientFeatureFlags", request, GetClientFeatureFlagsResponse)

  def delete_phone_verifications(self, request: DeletePhoneVerificationsRequest = None):
    r"""
    Args:
      request (DeletePhoneVerificationsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeletePhoneVerificationsRequest()

    self._client.call("users.UsersService", "DeletePhoneVerifications", request, None)

  def get_my_attributes(self, request: GetMyAttributesRequest = None) -> GetMyAttributesResponse:
    r"""
    Args:
      request (GetMyAttributesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetMyAttributesRequest()

    return self._client.call("users.UsersService", "GetMyAttributes", request, GetMyAttributesResponse)

  def get_user_count(self, request: GetUserCountRequest = None) -> GetUserCountResponse:
    r"""
    Args:
      request (GetUserCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserCountRequest()

    return self._client.call("users.UsersService", "GetUserCount", request, GetUserCountResponse)

  def migrate_terms_acceptances(self, request: MigrateTermsAcceptancesRequest = None) -> MigrateTermsAcceptancesResponse:
    r"""
    Args:
      request (MigrateTermsAcceptancesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MigrateTermsAcceptancesRequest()

    return self._client.call("users.UsersService", "MigrateTermsAcceptances", request, MigrateTermsAcceptancesResponse)

  def follow_user(self, request: FollowUserRequest = None, user_name: str = None) -> FollowUserResponse:
    r"""
    Current user follows the requested user by username

    Args:
      request (FollowUserRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      user_name (str)
        This corresponds to the ``user_name`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([user_name])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = FollowUserRequest()
      if user_name is None:
        raise TypeError('Must specify `user_name`')
      request.user_name = user_name

    if request.user_name is None:
      raise TypeError('Must specify `request.user_name`')
    return self._client.call("users.UsersService", "FollowUser", request, FollowUserResponse)

  def unfollow_user(self, request: UnfollowUserRequest = None) -> UnfollowUserResponse:
    r"""
    Current user unfollows the requested user by username

    Args:
      request (UnfollowUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnfollowUserRequest()

    return self._client.call("users.UsersService", "UnfollowUser", request, UnfollowUserResponse)

  def get_contact_user_info(self, request: GetContactUserInfoRequest = None) -> GetContactUserInfoResponse:
    r"""
    Get information about whether the current user can use the contact user
    feature.

    Args:
      request (GetContactUserInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetContactUserInfoRequest()

    return self._client.call("users.UsersService", "GetContactUserInfo", request, GetContactUserInfoResponse)

  def create_user_message(self, request: CreateUserMessageRequest = None) -> CreateUserMessageResponse:
    r"""
    Send a message to the given user.

    Args:
      request (CreateUserMessageRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateUserMessageRequest()

    return self._client.call("users.UsersService", "CreateUserMessage", request, CreateUserMessageResponse)

  def set_phone_reputable(self, request: SetPhoneReputableRequest = None):
    r"""
    For an admin to set a user's phone reputable.

    Args:
      request (SetPhoneReputableRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetPhoneReputableRequest()

    self._client.call("users.UsersService", "SetPhoneReputable", request, None)

  def get_user(self, request: GetUserRequest = None) -> User:
    r"""
    Fetch information about a given user. Note if this is a different user,
    some fields won't be returned.
    GetUserAvatar should be preferred if the necessary fields are part of that.

    Args:
      request (GetUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserRequest()

    return self._client.call("users.UsersService", "GetUser", request, User)

  def get_user_avatar(self, request: GetUserAvatarRequest = None) -> UserAvatar:
    r"""
    Fetch basic information about a given user, enough to populate a user
    avatar. All returned information is public, so no scrubbing necessary.

    Args:
      request (GetUserAvatarRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserAvatarRequest()

    return self._client.call("users.UsersService", "GetUserAvatar", request, UserAvatar)

  def get_current_user(self, request: GetCurrentUserRequest = None) -> User:
    r"""
    Get the current user, or null if no user is logged in. Note please avoid
    using if you just need the Id.

    Args:
      request (GetCurrentUserRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCurrentUserRequest()

    return self._client.call("users.UsersService", "GetCurrentUser", request, User)

  def get_current_user_id(self, request: GetCurrentUserIdRequest = None) -> GetCurrentUserIdResponse:
    r"""
    Get the id of the current user, or null if no user is logged in. No DB
    access required.

    Args:
      request (GetCurrentUserIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCurrentUserIdRequest()

    return self._client.call("users.UsersService", "GetCurrentUserId", request, GetCurrentUserIdResponse)

  def search_organizations(self, request: SearchOrganizationsRequest = None, query: str = None) -> SearchOrganizationsResponse:
    r"""
    Args:
      request (SearchOrganizationsRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      query (str)
        This corresponds to the ``query`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([query])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = SearchOrganizationsRequest()
      if query is not None:
        request.query = query

    return self._client.call("users.UsersService", "SearchOrganizations", request, SearchOrganizationsResponse)

  def search_places(self, request: SearchPlacesRequest = None, input: str = None) -> SearchPlacesResponse:
    r"""
    Args:
      request (SearchPlacesRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      input (str)
        This corresponds to the ``input`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([input])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = SearchPlacesRequest()
      if input is not None:
        request.input = input

    return self._client.call("users.UsersService", "SearchPlaces", request, SearchPlacesResponse)

  def search_users_suggestions(self, request: SearchUsersSuggestionsRequest = None, page_size: int = None, query: str = None, topic_id: int = None) -> SearchUsersSuggestionsResponse:
    r"""
    Args:
      request (SearchUsersSuggestionsRequest):
        The request object; initialized to empty instance if not specified.
        May not be specified if any of the flattened field params are specified.
      page_size (int)
        This corresponds to the ``page_size`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
      query (str)
        This corresponds to the ``query`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
      topic_id (int)
        This corresponds to the ``topic_id`` field on the ``request`` instance;
        if ``request`` is provided, this should not be set.
    """

    has_flattened_args = any([page_size, query, topic_id])
    if request is not None and has_flattened_args:
      raise ValueError('If the `request` argument is set, then none of '
                       'the individual field arguments should be set.')

    if request is None:
      request = SearchUsersSuggestionsRequest()
      if page_size is not None:
        request.page_size = page_size
      if query is not None:
        request.query = query
      if topic_id is not None:
        request.topic_id = topic_id

    return self._client.call("users.UsersService", "SearchUsersSuggestions", request, SearchUsersSuggestionsResponse)

  def set_my_attributes(self, request: SetMyAttributesRequest = None):
    r"""
    Args:
      request (SetMyAttributesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetMyAttributesRequest()

    self._client.call("users.UsersService", "SetMyAttributes", request, None)

  def unsubscribe_newsletter(self, request: UnsubscribeNewsletterRequest = None):
    r"""
    Args:
      request (UnsubscribeNewsletterRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UnsubscribeNewsletterRequest()

    self._client.call("users.UsersService", "UnsubscribeNewsletter", request, None)

  def update_onboarding_dismissed_status(self, request: UpdateOnboardingDismissedStatusRequest = None):
    r"""
    Args:
      request (UpdateOnboardingDismissedStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateOnboardingDismissedStatusRequest()

    self._client.call("users.UsersService", "UpdateOnboardingDismissedStatus", request, None)

  def get_onboarding_dismissed_status(self, request: GetOnboardingDismissedStatusRequest = None) -> GetOnboardingDismissedStatusResponse:
    r"""
    Args:
      request (GetOnboardingDismissedStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetOnboardingDismissedStatusRequest()

    return self._client.call("users.UsersService", "GetOnboardingDismissedStatus", request, GetOnboardingDismissedStatusResponse)

  def update_homepage_stats_dismissed_status(self, request: UpdateHomepageStatsDismissedStatusRequest = None):
    r"""
    Args:
      request (UpdateHomepageStatsDismissedStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateHomepageStatsDismissedStatusRequest()

    self._client.call("users.UsersService", "UpdateHomepageStatsDismissedStatus", request, None)

  def get_homepage_stats_dismissed_status(self, request: GetHomepageStatsDismissedStatusRequest = None) -> GetHomepageStatsDismissedStatusResponse:
    r"""
    Args:
      request (GetHomepageStatsDismissedStatusRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHomepageStatsDismissedStatusRequest()

    return self._client.call("users.UsersService", "GetHomepageStatsDismissedStatus", request, GetHomepageStatsDismissedStatusResponse)

  def get_upload_warning_dismissed_handler(self, request: GetUploadWarningDismissedRequest = None) -> GetUploadWarningDismissedResponse:
    r"""
    Args:
      request (GetUploadWarningDismissedRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUploadWarningDismissedRequest()

    return self._client.call("users.UsersService", "GetUploadWarningDismissedHandler", request, GetUploadWarningDismissedResponse)

  def set_upload_warning_dismissed_handler(self, request: SetUploadWarningDismissedRequest = None):
    r"""
    Args:
      request (SetUploadWarningDismissedRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SetUploadWarningDismissedRequest()

    self._client.call("users.UsersService", "SetUploadWarningDismissedHandler", request, None)

  def get_user_emoji_skin_tone_handler(self, request: GetUserEmojiSkinToneRequest = None) -> GetUserEmojiSkinToneResponse:
    r"""
    Args:
      request (GetUserEmojiSkinToneRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetUserEmojiSkinToneRequest()

    return self._client.call("users.UsersService", "GetUserEmojiSkinToneHandler", request, GetUserEmojiSkinToneResponse)

  def update_user_emoji_skin_tone_handler(self, request: UpdateUserEmojiSkinToneRequest = None):
    r"""
    Args:
      request (UpdateUserEmojiSkinToneRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUserEmojiSkinToneRequest()

    self._client.call("users.UsersService", "UpdateUserEmojiSkinToneHandler", request, None)

  def update_current_user_theme(self, request: UpdateCurrentUserThemeRequest = None):
    r"""
    Args:
      request (UpdateCurrentUserThemeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCurrentUserThemeRequest()

    self._client.call("users.UsersService", "UpdateCurrentUserTheme", request, None)

  def get_current_user_theme(self, request: GetCurrentUserThemeRequest = None) -> GetCurrentUserThemeResponse:
    r"""
    Args:
      request (GetCurrentUserThemeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCurrentUserThemeRequest()

    return self._client.call("users.UsersService", "GetCurrentUserTheme", request, GetCurrentUserThemeResponse)

  def update_users_model_proxy_quota_group(self, request: UpdateUsersModelProxyQuotaGroupRequest = None) -> UpdateUsersModelProxyQuotaGroupResponse:
    r"""
    Args:
      request (UpdateUsersModelProxyQuotaGroupRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateUsersModelProxyQuotaGroupRequest()

    return self._client.call("users.UsersService", "UpdateUsersModelProxyQuotaGroup", request, UpdateUsersModelProxyQuotaGroupResponse)
