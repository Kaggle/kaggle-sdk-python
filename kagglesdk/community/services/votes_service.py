from kagglesdk.community.types.votes_service import BackFillVoteForeignKeysRequest, BackFillVoteForeignKeysResponse, BackFillVotesRequest, BackFillVotesResponse, BatchRecalculateScoresRequest, BatchRecalculateScoresResponse, BatchRecalculateVotesRequest, BatchRecalculateVotesResponse, GetVoteRequest, GetVoteTotalsRequest, GetVoteTotalsResponse, ListUpvotersRequest, ListUpvotersResponse, UpdateVoteRequest, Vote
from kagglesdk.kaggle_http_client import KaggleHttpClient

class VotesClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def get_vote(self, request: GetVoteRequest = None) -> Vote:
    r"""
    Gets the vote the current user has for the given entity.

    Args:
      request (GetVoteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetVoteRequest()

    return self._client.call("community.VotesService", "GetVote", request, Vote)

  def update_vote(self, request: UpdateVoteRequest = None) -> Vote:
    r"""
    Updates a vote (creating if needed). Use to upvote, downvote or delete a
    vote.

    Args:
      request (UpdateVoteRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateVoteRequest()

    return self._client.call("community.VotesService", "UpdateVote", request, Vote)

  def get_vote_totals(self, request: GetVoteTotalsRequest = None) -> GetVoteTotalsResponse:
    r"""
    Get vote totals for the entity (e.g. TotalScore and TotalVotes).

    Args:
      request (GetVoteTotalsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetVoteTotalsRequest()

    return self._client.call("community.VotesService", "GetVoteTotals", request, GetVoteTotalsResponse)

  def list_upvoters(self, request: ListUpvotersRequest = None) -> ListUpvotersResponse:
    r"""
    List all the users who upvoted the content

    Args:
      request (ListUpvotersRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListUpvotersRequest()

    return self._client.call("community.VotesService", "ListUpvoters", request, ListUpvotersResponse)

  def batch_recalculate_votes(self, request: BatchRecalculateVotesRequest = None) -> BatchRecalculateVotesResponse:
    r"""
    Recalculates the VoteIgnoreReason for a sequence of votes

    Args:
      request (BatchRecalculateVotesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchRecalculateVotesRequest()

    return self._client.call("community.VotesService", "BatchRecalculateVotes", request, BatchRecalculateVotesResponse)

  def batch_recalculate_scores(self, request: BatchRecalculateScoresRequest = None) -> BatchRecalculateScoresResponse:
    r"""
    Recalculate the score for a series of entities, making sure the cached
    value matches what's calculated

    Args:
      request (BatchRecalculateScoresRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BatchRecalculateScoresRequest()

    return self._client.call("community.VotesService", "BatchRecalculateScores", request, BatchRecalculateScoresResponse)

  def back_fill_votes(self, request: BackFillVotesRequest = None) -> BackFillVotesResponse:
    r"""
    Args:
      request (BackFillVotesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackFillVotesRequest()

    return self._client.call("community.VotesService", "BackFillVotes", request, BackFillVotesResponse)

  def back_fill_vote_foreign_keys(self, request: BackFillVoteForeignKeysRequest = None) -> BackFillVoteForeignKeysResponse:
    r"""
    Args:
      request (BackFillVoteForeignKeysRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = BackFillVoteForeignKeysRequest()

    return self._client.call("community.VotesService", "BackFillVoteForeignKeys", request, BackFillVoteForeignKeysResponse)
