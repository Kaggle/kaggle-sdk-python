from kagglesdk.common.types.common_types import KaggleEntityType
from kagglesdk.kaggle_object import *
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class BackFillVoteForeignKeysRequest(KaggleObject):
  r"""
  Attributes:
    batch_size (int)
      How many of each type to update. Only updates those that need it, so can
      keep recalling this
  """

  def __init__(self):
    self._batch_size = 0
    self._freeze()

  @property
  def batch_size(self) -> int:
    r"""
    How many of each type to update. Only updates those that need it, so can
    keep recalling this
    """
    return self._batch_size

  @batch_size.setter
  def batch_size(self, batch_size: int):
    if batch_size is None:
      del self.batch_size
      return
    if not isinstance(batch_size, int):
      raise TypeError('batch_size must be of type int')
    self._batch_size = batch_size


class BackFillVoteForeignKeysResponse(KaggleObject):
  r"""
  Attributes:
    count_forum_messages_updated (int)
      How many forum messages were updated (only updated if it changed something)
    count_kernels_updated (int)
      How many kernels were updated (only updated if it changed something)
    count_datasets_updated (int)
      How many datasets were updated (only updated if it changed something)
    count_models_updated (int)
      How many models were updated (only updated if it changed something)
  """

  def __init__(self):
    self._count_forum_messages_updated = 0
    self._count_kernels_updated = 0
    self._count_datasets_updated = 0
    self._count_models_updated = 0
    self._freeze()

  @property
  def count_forum_messages_updated(self) -> int:
    """How many forum messages were updated (only updated if it changed something)"""
    return self._count_forum_messages_updated

  @count_forum_messages_updated.setter
  def count_forum_messages_updated(self, count_forum_messages_updated: int):
    if count_forum_messages_updated is None:
      del self.count_forum_messages_updated
      return
    if not isinstance(count_forum_messages_updated, int):
      raise TypeError('count_forum_messages_updated must be of type int')
    self._count_forum_messages_updated = count_forum_messages_updated

  @property
  def count_kernels_updated(self) -> int:
    """How many kernels were updated (only updated if it changed something)"""
    return self._count_kernels_updated

  @count_kernels_updated.setter
  def count_kernels_updated(self, count_kernels_updated: int):
    if count_kernels_updated is None:
      del self.count_kernels_updated
      return
    if not isinstance(count_kernels_updated, int):
      raise TypeError('count_kernels_updated must be of type int')
    self._count_kernels_updated = count_kernels_updated

  @property
  def count_datasets_updated(self) -> int:
    """How many datasets were updated (only updated if it changed something)"""
    return self._count_datasets_updated

  @count_datasets_updated.setter
  def count_datasets_updated(self, count_datasets_updated: int):
    if count_datasets_updated is None:
      del self.count_datasets_updated
      return
    if not isinstance(count_datasets_updated, int):
      raise TypeError('count_datasets_updated must be of type int')
    self._count_datasets_updated = count_datasets_updated

  @property
  def count_models_updated(self) -> int:
    """How many models were updated (only updated if it changed something)"""
    return self._count_models_updated

  @count_models_updated.setter
  def count_models_updated(self, count_models_updated: int):
    if count_models_updated is None:
      del self.count_models_updated
      return
    if not isinstance(count_models_updated, int):
      raise TypeError('count_models_updated must be of type int')
    self._count_models_updated = count_models_updated


class BackFillVotesRequest(KaggleObject):
  r"""
  Attributes:
    start_id (int)
      The starting id (inclusive) for what range of votes to copy.
      This id comes from the source table
    end_id (int)
      The ending id (inclusive) for what range of votes to copy.
    batch_size (int)
      How many to process in a single batch
    entity_type (KaggleEntityType)
      What content type of votes to copy over
    fork_votes (bool)
      Copy over votes generated from forks, only valid for notebooks
  """

  def __init__(self):
    self._start_id = 0
    self._end_id = 0
    self._batch_size = 0
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._fork_votes = False
    self._freeze()

  @property
  def start_id(self) -> int:
    r"""
    The starting id (inclusive) for what range of votes to copy.
    This id comes from the source table
    """
    return self._start_id

  @start_id.setter
  def start_id(self, start_id: int):
    if start_id is None:
      del self.start_id
      return
    if not isinstance(start_id, int):
      raise TypeError('start_id must be of type int')
    self._start_id = start_id

  @property
  def end_id(self) -> int:
    """The ending id (inclusive) for what range of votes to copy."""
    return self._end_id

  @end_id.setter
  def end_id(self, end_id: int):
    if end_id is None:
      del self.end_id
      return
    if not isinstance(end_id, int):
      raise TypeError('end_id must be of type int')
    self._end_id = end_id

  @property
  def batch_size(self) -> int:
    """How many to process in a single batch"""
    return self._batch_size

  @batch_size.setter
  def batch_size(self, batch_size: int):
    if batch_size is None:
      del self.batch_size
      return
    if not isinstance(batch_size, int):
      raise TypeError('batch_size must be of type int')
    self._batch_size = batch_size

  @property
  def entity_type(self) -> 'KaggleEntityType':
    """What content type of votes to copy over"""
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleEntityType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type

  @property
  def fork_votes(self) -> bool:
    """Copy over votes generated from forks, only valid for notebooks"""
    return self._fork_votes

  @fork_votes.setter
  def fork_votes(self, fork_votes: bool):
    if fork_votes is None:
      del self.fork_votes
      return
    if not isinstance(fork_votes, bool):
      raise TypeError('fork_votes must be of type bool')
    self._fork_votes = fork_votes


class BackFillVotesResponse(KaggleObject):
  r"""
  Attributes:
    new_count (int)
      The number of new votes copied over
    changed_count (int)
      The number of votes that had changes
    unchanged_count (int)
      The number of votes that were not copied because they were identical
    error (str)
      Message of any error that occured
  """

  def __init__(self):
    self._new_count = 0
    self._changed_count = 0
    self._unchanged_count = 0
    self._error = None
    self._freeze()

  @property
  def new_count(self) -> int:
    """The number of new votes copied over"""
    return self._new_count

  @new_count.setter
  def new_count(self, new_count: int):
    if new_count is None:
      del self.new_count
      return
    if not isinstance(new_count, int):
      raise TypeError('new_count must be of type int')
    self._new_count = new_count

  @property
  def changed_count(self) -> int:
    """The number of votes that had changes"""
    return self._changed_count

  @changed_count.setter
  def changed_count(self, changed_count: int):
    if changed_count is None:
      del self.changed_count
      return
    if not isinstance(changed_count, int):
      raise TypeError('changed_count must be of type int')
    self._changed_count = changed_count

  @property
  def unchanged_count(self) -> int:
    """The number of votes that were not copied because they were identical"""
    return self._unchanged_count

  @unchanged_count.setter
  def unchanged_count(self, unchanged_count: int):
    if unchanged_count is None:
      del self.unchanged_count
      return
    if not isinstance(unchanged_count, int):
      raise TypeError('unchanged_count must be of type int')
    self._unchanged_count = unchanged_count

  @property
  def error(self) -> str:
    """Message of any error that occured"""
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error


class BatchRecalculateScoresRequest(KaggleObject):
  r"""
  Attributes:
    start_id (int)
      The starting id (inclusive) for the range of entities to update
    end_id (int)
      The ending id (inclusive) for the range of entities to update
    entity_type (KaggleEntityType)
      What content type of the entities, all entities must be the same type (call
      multiple times for different entities)
    max_update_count (int)
      The maximum number of updates to do. The check if an entity cached score is
      correct is cheap and done DB-side but any changes are updated individually
      and cause a re-index for search, so the range of ids to scan can be much
      larger than the number of updates should be. Note this can also be 0 if you
      only want to check without updates
  """

  def __init__(self):
    self._start_id = 0
    self._end_id = 0
    self._entity_type = KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED
    self._max_update_count = 0
    self._freeze()

  @property
  def start_id(self) -> int:
    """The starting id (inclusive) for the range of entities to update"""
    return self._start_id

  @start_id.setter
  def start_id(self, start_id: int):
    if start_id is None:
      del self.start_id
      return
    if not isinstance(start_id, int):
      raise TypeError('start_id must be of type int')
    self._start_id = start_id

  @property
  def end_id(self) -> int:
    """The ending id (inclusive) for the range of entities to update"""
    return self._end_id

  @end_id.setter
  def end_id(self, end_id: int):
    if end_id is None:
      del self.end_id
      return
    if not isinstance(end_id, int):
      raise TypeError('end_id must be of type int')
    self._end_id = end_id

  @property
  def entity_type(self) -> 'KaggleEntityType':
    r"""
    What content type of the entities, all entities must be the same type (call
    multiple times for different entities)
    """
    return self._entity_type

  @entity_type.setter
  def entity_type(self, entity_type: 'KaggleEntityType'):
    if entity_type is None:
      del self.entity_type
      return
    if not isinstance(entity_type, KaggleEntityType):
      raise TypeError('entity_type must be of type KaggleEntityType')
    self._entity_type = entity_type

  @property
  def max_update_count(self) -> int:
    r"""
    The maximum number of updates to do. The check if an entity cached score is
    correct is cheap and done DB-side but any changes are updated individually
    and cause a re-index for search, so the range of ids to scan can be much
    larger than the number of updates should be. Note this can also be 0 if you
    only want to check without updates
    """
    return self._max_update_count

  @max_update_count.setter
  def max_update_count(self, max_update_count: int):
    if max_update_count is None:
      del self.max_update_count
      return
    if not isinstance(max_update_count, int):
      raise TypeError('max_update_count must be of type int')
    self._max_update_count = max_update_count


class BatchRecalculateScoresResponse(KaggleObject):
  r"""
  Attributes:
    changed_count (int)
      The number of entities that had changes
    unchanged_count (int)
      The number of entities that were already up-to-date
    updated_count (int)
      The number of entities that were successfully updated
    error (str)
      Any error that occured while trying to update the scores
  """

  def __init__(self):
    self._changed_count = 0
    self._unchanged_count = 0
    self._updated_count = 0
    self._error = None
    self._freeze()

  @property
  def changed_count(self) -> int:
    """The number of entities that had changes"""
    return self._changed_count

  @changed_count.setter
  def changed_count(self, changed_count: int):
    if changed_count is None:
      del self.changed_count
      return
    if not isinstance(changed_count, int):
      raise TypeError('changed_count must be of type int')
    self._changed_count = changed_count

  @property
  def unchanged_count(self) -> int:
    """The number of entities that were already up-to-date"""
    return self._unchanged_count

  @unchanged_count.setter
  def unchanged_count(self, unchanged_count: int):
    if unchanged_count is None:
      del self.unchanged_count
      return
    if not isinstance(unchanged_count, int):
      raise TypeError('unchanged_count must be of type int')
    self._unchanged_count = unchanged_count

  @property
  def updated_count(self) -> int:
    """The number of entities that were successfully updated"""
    return self._updated_count

  @updated_count.setter
  def updated_count(self, updated_count: int):
    if updated_count is None:
      del self.updated_count
      return
    if not isinstance(updated_count, int):
      raise TypeError('updated_count must be of type int')
    self._updated_count = updated_count

  @property
  def error(self) -> str:
    """Any error that occured while trying to update the scores"""
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error


class BatchRecalculateVotesRequest(KaggleObject):
  r"""
  Attributes:
    start_id (int)
      The Id of the vote entry to start with (inclusive)
    stop_id (int)
      The Id of the vote entry to stop at (inclusive)
    batch_size (int)
      How many to process in one batch
  """

  def __init__(self):
    self._start_id = 0
    self._stop_id = 0
    self._batch_size = 0
    self._freeze()

  @property
  def start_id(self) -> int:
    """The Id of the vote entry to start with (inclusive)"""
    return self._start_id

  @start_id.setter
  def start_id(self, start_id: int):
    if start_id is None:
      del self.start_id
      return
    if not isinstance(start_id, int):
      raise TypeError('start_id must be of type int')
    self._start_id = start_id

  @property
  def stop_id(self) -> int:
    """The Id of the vote entry to stop at (inclusive)"""
    return self._stop_id

  @stop_id.setter
  def stop_id(self, stop_id: int):
    if stop_id is None:
      del self.stop_id
      return
    if not isinstance(stop_id, int):
      raise TypeError('stop_id must be of type int')
    self._stop_id = stop_id

  @property
  def batch_size(self) -> int:
    """How many to process in one batch"""
    return self._batch_size

  @batch_size.setter
  def batch_size(self, batch_size: int):
    if batch_size is None:
      del self.batch_size
      return
    if not isinstance(batch_size, int):
      raise TypeError('batch_size must be of type int')
    self._batch_size = batch_size


class BatchRecalculateVotesResponse(KaggleObject):
  r"""
  Attributes:
    success_count (int)
      The number of votes successfully processed
    changed_count (int)
      The number of votes that had changes
    error (str)
      Message of any error that occured
  """

  def __init__(self):
    self._success_count = 0
    self._changed_count = 0
    self._error = None
    self._freeze()

  @property
  def success_count(self) -> int:
    """The number of votes successfully processed"""
    return self._success_count

  @success_count.setter
  def success_count(self, success_count: int):
    if success_count is None:
      del self.success_count
      return
    if not isinstance(success_count, int):
      raise TypeError('success_count must be of type int')
    self._success_count = success_count

  @property
  def changed_count(self) -> int:
    """The number of votes that had changes"""
    return self._changed_count

  @changed_count.setter
  def changed_count(self, changed_count: int):
    if changed_count is None:
      del self.changed_count
      return
    if not isinstance(changed_count, int):
      raise TypeError('changed_count must be of type int')
    self._changed_count = changed_count

  @property
  def error(self) -> str:
    """Message of any error that occured"""
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error


class GetVoteRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (VoteEntity)
  """

  def __init__(self):
    self._entity_id = None
    self._freeze()

  @property
  def entity_id(self) -> Optional['VoteEntity']:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: Optional['VoteEntity']):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, VoteEntity):
      raise TypeError('entity_id must be of type VoteEntity')
    self._entity_id = entity_id


class GetVoteTotalsRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (VoteEntity)
  """

  def __init__(self):
    self._entity_id = None
    self._freeze()

  @property
  def entity_id(self) -> Optional['VoteEntity']:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: Optional['VoteEntity']):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, VoteEntity):
      raise TypeError('entity_id must be of type VoteEntity')
    self._entity_id = entity_id


class GetVoteTotalsResponse(KaggleObject):
  r"""
  Attributes:
    total_votes (int)
      The total number of votes, all votes included
    total_score (int)
      The total score from the votes (up-down), all votes included
    medal_eligible_upvote_count (int)
      The number of upvotes that count towards medals
  """

  def __init__(self):
    self._total_votes = 0
    self._total_score = 0
    self._medal_eligible_upvote_count = 0
    self._freeze()

  @property
  def total_votes(self) -> int:
    """The total number of votes, all votes included"""
    return self._total_votes

  @total_votes.setter
  def total_votes(self, total_votes: int):
    if total_votes is None:
      del self.total_votes
      return
    if not isinstance(total_votes, int):
      raise TypeError('total_votes must be of type int')
    self._total_votes = total_votes

  @property
  def total_score(self) -> int:
    """The total score from the votes (up-down), all votes included"""
    return self._total_score

  @total_score.setter
  def total_score(self, total_score: int):
    if total_score is None:
      del self.total_score
      return
    if not isinstance(total_score, int):
      raise TypeError('total_score must be of type int')
    self._total_score = total_score

  @property
  def medal_eligible_upvote_count(self) -> int:
    """The number of upvotes that count towards medals"""
    return self._medal_eligible_upvote_count

  @medal_eligible_upvote_count.setter
  def medal_eligible_upvote_count(self, medal_eligible_upvote_count: int):
    if medal_eligible_upvote_count is None:
      del self.medal_eligible_upvote_count
      return
    if not isinstance(medal_eligible_upvote_count, int):
      raise TypeError('medal_eligible_upvote_count must be of type int')
    self._medal_eligible_upvote_count = medal_eligible_upvote_count


class ListUpvotersRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (VoteEntity)
  """

  def __init__(self):
    self._entity_id = None
    self._freeze()

  @property
  def entity_id(self) -> Optional['VoteEntity']:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: Optional['VoteEntity']):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, VoteEntity):
      raise TypeError('entity_id must be of type VoteEntity')
    self._entity_id = entity_id


class ListUpvotersResponse(KaggleObject):
  r"""
  Attributes:
    users (UserAvatar)
      All the users who upvoted this, in user avatar format
    medal_eligible_vote_count (int)
      Total number of votes that count towards medals.
  """

  def __init__(self):
    self._users = []
    self._medal_eligible_vote_count = 0
    self._freeze()

  @property
  def users(self) -> Optional[List[Optional['UserAvatar']]]:
    """All the users who upvoted this, in user avatar format"""
    return self._users

  @users.setter
  def users(self, users: Optional[List[Optional['UserAvatar']]]):
    if users is None:
      del self.users
      return
    if not isinstance(users, list):
      raise TypeError('users must be of type list')
    if not all([isinstance(t, UserAvatar) for t in users]):
      raise TypeError('users must contain only items of type UserAvatar')
    self._users = users

  @property
  def medal_eligible_vote_count(self) -> int:
    """Total number of votes that count towards medals."""
    return self._medal_eligible_vote_count

  @medal_eligible_vote_count.setter
  def medal_eligible_vote_count(self, medal_eligible_vote_count: int):
    if medal_eligible_vote_count is None:
      del self.medal_eligible_vote_count
      return
    if not isinstance(medal_eligible_vote_count, int):
      raise TypeError('medal_eligible_vote_count must be of type int')
    self._medal_eligible_vote_count = medal_eligible_vote_count


class UpdateVoteRequest(KaggleObject):
  r"""
  Attributes:
    entity_id (VoteEntity)
    vote (Vote)
      Vote to update
    is_from_fork (bool)
      If true, this upvote comes automatically from the action of forking a
      notebook
  """

  def __init__(self):
    self._entity_id = None
    self._vote = None
    self._is_from_fork = None
    self._freeze()

  @property
  def entity_id(self) -> Optional['VoteEntity']:
    return self._entity_id

  @entity_id.setter
  def entity_id(self, entity_id: Optional['VoteEntity']):
    if entity_id is None:
      del self.entity_id
      return
    if not isinstance(entity_id, VoteEntity):
      raise TypeError('entity_id must be of type VoteEntity')
    self._entity_id = entity_id

  @property
  def vote(self) -> Optional['Vote']:
    """Vote to update"""
    return self._vote

  @vote.setter
  def vote(self, vote: Optional['Vote']):
    if vote is None:
      del self.vote
      return
    if not isinstance(vote, Vote):
      raise TypeError('vote must be of type Vote')
    self._vote = vote

  @property
  def is_from_fork(self) -> bool:
    r"""
    If true, this upvote comes automatically from the action of forking a
    notebook
    """
    return self._is_from_fork or False

  @is_from_fork.setter
  def is_from_fork(self, is_from_fork: Optional[bool]):
    if is_from_fork is None:
      del self.is_from_fork
      return
    if not isinstance(is_from_fork, bool):
      raise TypeError('is_from_fork must be of type bool')
    self._is_from_fork = is_from_fork


class Vote(KaggleObject):
  r"""
  Attributes:
    score (int)
      The score of this vote, (-1,0,1).
    id (int)
    is_self_vote (bool)
  """

  def __init__(self):
    self._score = 0
    self._id = None
    self._is_self_vote = None
    self._freeze()

  @property
  def score(self) -> int:
    """The score of this vote, (-1,0,1)."""
    return self._score

  @score.setter
  def score(self, score: int):
    if score is None:
      del self.score
      return
    if not isinstance(score, int):
      raise TypeError('score must be of type int')
    self._score = score

  @property
  def id(self) -> int:
    return self._id or 0

  @id.setter
  def id(self, id: Optional[int]):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def is_self_vote(self) -> bool:
    return self._is_self_vote or False

  @is_self_vote.setter
  def is_self_vote(self, is_self_vote: Optional[bool]):
    if is_self_vote is None:
      del self.is_self_vote
      return
    if not isinstance(is_self_vote, bool):
      raise TypeError('is_self_vote must be of type bool')
    self._is_self_vote = is_self_vote


class VoteEntity(KaggleObject):
  r"""
  Union type of all the allowable entity Ids

  Attributes:
    forum_message_id (int)
    dataset_id (int)
    kernel_id (int)
    model_id (int)
    resource_reference_id (int)
    hash_link (str)
      For datasets only, a hashlink for the dataset, to bypass auth checks
    benchmark_task_id (int)
    benchmark_id (int)
  """

  def __init__(self):
    self._forum_message_id = None
    self._dataset_id = None
    self._kernel_id = None
    self._model_id = None
    self._resource_reference_id = None
    self._hash_link = None
    self._benchmark_task_id = None
    self._benchmark_id = None
    self._freeze()

  @property
  def forum_message_id(self) -> int:
    return self._forum_message_id or 0

  @forum_message_id.setter
  def forum_message_id(self, forum_message_id: int):
    if forum_message_id is None:
      del self.forum_message_id
      return
    if not isinstance(forum_message_id, int):
      raise TypeError('forum_message_id must be of type int')
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.resource_reference_id
    del self.benchmark_task_id
    del self.benchmark_id
    self._forum_message_id = forum_message_id

  @property
  def dataset_id(self) -> int:
    return self._dataset_id or 0

  @dataset_id.setter
  def dataset_id(self, dataset_id: int):
    if dataset_id is None:
      del self.dataset_id
      return
    if not isinstance(dataset_id, int):
      raise TypeError('dataset_id must be of type int')
    del self.forum_message_id
    del self.kernel_id
    del self.model_id
    del self.resource_reference_id
    del self.benchmark_task_id
    del self.benchmark_id
    self._dataset_id = dataset_id

  @property
  def kernel_id(self) -> int:
    return self._kernel_id or 0

  @kernel_id.setter
  def kernel_id(self, kernel_id: int):
    if kernel_id is None:
      del self.kernel_id
      return
    if not isinstance(kernel_id, int):
      raise TypeError('kernel_id must be of type int')
    del self.forum_message_id
    del self.dataset_id
    del self.model_id
    del self.resource_reference_id
    del self.benchmark_task_id
    del self.benchmark_id
    self._kernel_id = kernel_id

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: int):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    del self.forum_message_id
    del self.dataset_id
    del self.kernel_id
    del self.resource_reference_id
    del self.benchmark_task_id
    del self.benchmark_id
    self._model_id = model_id

  @property
  def resource_reference_id(self) -> int:
    return self._resource_reference_id or 0

  @resource_reference_id.setter
  def resource_reference_id(self, resource_reference_id: int):
    if resource_reference_id is None:
      del self.resource_reference_id
      return
    if not isinstance(resource_reference_id, int):
      raise TypeError('resource_reference_id must be of type int')
    del self.forum_message_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.benchmark_task_id
    del self.benchmark_id
    self._resource_reference_id = resource_reference_id

  @property
  def benchmark_task_id(self) -> int:
    return self._benchmark_task_id or 0

  @benchmark_task_id.setter
  def benchmark_task_id(self, benchmark_task_id: int):
    if benchmark_task_id is None:
      del self.benchmark_task_id
      return
    if not isinstance(benchmark_task_id, int):
      raise TypeError('benchmark_task_id must be of type int')
    del self.forum_message_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.resource_reference_id
    del self.benchmark_id
    self._benchmark_task_id = benchmark_task_id

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id or 0

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    del self.forum_message_id
    del self.dataset_id
    del self.kernel_id
    del self.model_id
    del self.resource_reference_id
    del self.benchmark_task_id
    self._benchmark_id = benchmark_id

  @property
  def hash_link(self) -> str:
    """For datasets only, a hashlink for the dataset, to bypass auth checks"""
    return self._hash_link or ""

  @hash_link.setter
  def hash_link(self, hash_link: Optional[str]):
    if hash_link is None:
      del self.hash_link
      return
    if not isinstance(hash_link, str):
      raise TypeError('hash_link must be of type str')
    self._hash_link = hash_link


BackFillVoteForeignKeysRequest._fields = [
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
]

BackFillVoteForeignKeysResponse._fields = [
  FieldMetadata("countForumMessagesUpdated", "count_forum_messages_updated", "_count_forum_messages_updated", int, 0, PredefinedSerializer()),
  FieldMetadata("countKernelsUpdated", "count_kernels_updated", "_count_kernels_updated", int, 0, PredefinedSerializer()),
  FieldMetadata("countDatasetsUpdated", "count_datasets_updated", "_count_datasets_updated", int, 0, PredefinedSerializer()),
  FieldMetadata("countModelsUpdated", "count_models_updated", "_count_models_updated", int, 0, PredefinedSerializer()),
]

BackFillVotesRequest._fields = [
  FieldMetadata("startId", "start_id", "_start_id", int, 0, PredefinedSerializer()),
  FieldMetadata("endId", "end_id", "_end_id", int, 0, PredefinedSerializer()),
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("forkVotes", "fork_votes", "_fork_votes", bool, False, PredefinedSerializer()),
]

BackFillVotesResponse._fields = [
  FieldMetadata("newCount", "new_count", "_new_count", int, 0, PredefinedSerializer()),
  FieldMetadata("changedCount", "changed_count", "_changed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("unchangedCount", "unchanged_count", "_unchanged_count", int, 0, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

BatchRecalculateScoresRequest._fields = [
  FieldMetadata("startId", "start_id", "_start_id", int, 0, PredefinedSerializer()),
  FieldMetadata("endId", "end_id", "_end_id", int, 0, PredefinedSerializer()),
  FieldMetadata("entityType", "entity_type", "_entity_type", KaggleEntityType, KaggleEntityType.KAGGLE_ENTITY_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("maxUpdateCount", "max_update_count", "_max_update_count", int, 0, PredefinedSerializer()),
]

BatchRecalculateScoresResponse._fields = [
  FieldMetadata("changedCount", "changed_count", "_changed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("unchangedCount", "unchanged_count", "_unchanged_count", int, 0, PredefinedSerializer()),
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

BatchRecalculateVotesRequest._fields = [
  FieldMetadata("startId", "start_id", "_start_id", int, 0, PredefinedSerializer()),
  FieldMetadata("stopId", "stop_id", "_stop_id", int, 0, PredefinedSerializer()),
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
]

BatchRecalculateVotesResponse._fields = [
  FieldMetadata("successCount", "success_count", "_success_count", int, 0, PredefinedSerializer()),
  FieldMetadata("changedCount", "changed_count", "_changed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
]

GetVoteRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", VoteEntity, None, KaggleObjectSerializer()),
]

GetVoteTotalsRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", VoteEntity, None, KaggleObjectSerializer()),
]

GetVoteTotalsResponse._fields = [
  FieldMetadata("totalVotes", "total_votes", "_total_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("totalScore", "total_score", "_total_score", int, 0, PredefinedSerializer()),
  FieldMetadata("medalEligibleUpvoteCount", "medal_eligible_upvote_count", "_medal_eligible_upvote_count", int, 0, PredefinedSerializer()),
]

ListUpvotersRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", VoteEntity, None, KaggleObjectSerializer()),
]

ListUpvotersResponse._fields = [
  FieldMetadata("users", "users", "_users", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("medalEligibleVoteCount", "medal_eligible_vote_count", "_medal_eligible_vote_count", int, 0, PredefinedSerializer()),
]

UpdateVoteRequest._fields = [
  FieldMetadata("entityId", "entity_id", "_entity_id", VoteEntity, None, KaggleObjectSerializer()),
  FieldMetadata("vote", "vote", "_vote", Vote, None, KaggleObjectSerializer()),
  FieldMetadata("isFromFork", "is_from_fork", "_is_from_fork", bool, None, PredefinedSerializer(), optional=True),
]

Vote._fields = [
  FieldMetadata("score", "score", "_score", int, 0, PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isSelfVote", "is_self_vote", "_is_self_vote", bool, None, PredefinedSerializer(), optional=True),
]

VoteEntity._fields = [
  FieldMetadata("forumMessageId", "forum_message_id", "_forum_message_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("resourceReferenceId", "resource_reference_id", "_resource_reference_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("hashLink", "hash_link", "_hash_link", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskId", "benchmark_task_id", "_benchmark_task_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, None, PredefinedSerializer(), optional=True),
]

