from kagglesdk.kaggle_http_client import KaggleHttpClient
from kagglesdk.tags.types.tag_service import CreateCompetitionTagsRequest, CreateCompetitionTagsResponse, CreateLearnTrackTagsRequest, CreateLearnTrackTagsResponse, CreateTagRequest, DeleteCompetitionTagsRequest, DeleteCompetitionTagsResponse, DeleteLearnTrackTagsRequest, DeleteLearnTrackTagsResponse, DeleteTagRequest, DeleteTagResponse, GetTaggedEntityCountRequest, GetTaggedEntityCountResponse, GetTagHierarchyRequest, GetTagHierarchyResponse, GetTagsByIdRequest, ListTagsRequest, ListTagsResponse, MergeTagRequest, MergeTagResponse, SearchTagsRequest, TagList, UpdateForumTopicTagsRequest, UpdateForumTopicTagsResponse

class TagClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def update_forum_topic_tags(self, request: UpdateForumTopicTagsRequest = None) -> UpdateForumTopicTagsResponse:
    r"""
    Tag a given forum topic with one or many tags, removing any tags not
    specified in the request

    Args:
      request (UpdateForumTopicTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateForumTopicTagsRequest()

    return self._client.call("tags.TagService", "UpdateForumTopicTags", request, UpdateForumTopicTagsResponse)

  def create_learn_track_tags(self, request: CreateLearnTrackTagsRequest = None) -> CreateLearnTrackTagsResponse:
    r"""
    Tag a given learn track with one or many tags

    Args:
      request (CreateLearnTrackTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateLearnTrackTagsRequest()

    return self._client.call("tags.TagService", "CreateLearnTrackTags", request, CreateLearnTrackTagsResponse)

  def delete_learn_track_tags(self, request: DeleteLearnTrackTagsRequest = None) -> DeleteLearnTrackTagsResponse:
    r"""
    Untag a given learn track, removing one or many tags

    Args:
      request (DeleteLearnTrackTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteLearnTrackTagsRequest()

    return self._client.call("tags.TagService", "DeleteLearnTrackTags", request, DeleteLearnTrackTagsResponse)

  def get_tags_by_id(self, request: GetTagsByIdRequest = None) -> TagList:
    r"""
    Args:
      request (GetTagsByIdRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTagsByIdRequest()

    return self._client.call("tags.TagService", "GetTagsById", request, TagList)

  def search_tags(self, request: SearchTagsRequest = None) -> TagList:
    r"""
    Args:
      request (SearchTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = SearchTagsRequest()

    return self._client.call("tags.TagService", "SearchTags", request, TagList)

  def create_competition_tags(self, request: CreateCompetitionTagsRequest = None) -> CreateCompetitionTagsResponse:
    r"""
    Tag a given competition with one or many tags

    Args:
      request (CreateCompetitionTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionTagsRequest()

    return self._client.call("tags.TagService", "CreateCompetitionTags", request, CreateCompetitionTagsResponse)

  def delete_competition_tags(self, request: DeleteCompetitionTagsRequest = None) -> DeleteCompetitionTagsResponse:
    r"""
    Untag a given competition, removing one or many tags

    Args:
      request (DeleteCompetitionTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteCompetitionTagsRequest()

    return self._client.call("tags.TagService", "DeleteCompetitionTags", request, DeleteCompetitionTagsResponse)

  def get_tag_hierarchy(self, request: GetTagHierarchyRequest = None) -> GetTagHierarchyResponse:
    r"""
    Fetch the hierarchical structure of all tags

    Args:
      request (GetTagHierarchyRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTagHierarchyRequest()

    return self._client.call("tags.TagService", "GetTagHierarchy", request, GetTagHierarchyResponse)

  def list_tags(self, request: ListTagsRequest = None) -> ListTagsResponse:
    r"""
    Args:
      request (ListTagsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListTagsRequest()

    return self._client.call("tags.TagService", "ListTags", request, ListTagsResponse)

  def create_tag(self, request: CreateTagRequest = None):
    r"""
    Args:
      request (CreateTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateTagRequest()

    self._client.call("tags.TagService", "CreateTag", request, None)

  def delete_tag(self, request: DeleteTagRequest = None) -> DeleteTagResponse:
    r"""
    Args:
      request (DeleteTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteTagRequest()

    return self._client.call("tags.TagService", "DeleteTag", request, DeleteTagResponse)

  def merge_tag(self, request: MergeTagRequest = None) -> MergeTagResponse:
    r"""
    Args:
      request (MergeTagRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = MergeTagRequest()

    return self._client.call("tags.TagService", "MergeTag", request, MergeTagResponse)

  def get_tagged_entity_count(self, request: GetTaggedEntityCountRequest = None) -> GetTaggedEntityCountResponse:
    r"""
    Args:
      request (GetTaggedEntityCountRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTaggedEntityCountRequest()

    return self._client.call("tags.TagService", "GetTaggedEntityCount", request, GetTaggedEntityCountResponse)
