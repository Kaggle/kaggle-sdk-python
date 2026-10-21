from datetime import datetime, timedelta
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkArenaArtifactType, BenchmarkCandidateType, BenchmarkEnqueueSkipPolicy, BenchmarkTaskRunState, BenchmarkTaskVersionCreationState, BenchmarkTaskVersionSource
from kagglesdk.benchmarks.types.benchmark_task_run_service import BatchScheduleBenchmarkModelVersionResult
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkTaskDefinition, BenchmarkTaskOptions, BenchmarkTaskValidationStage
from kagglesdk.kaggle_object import *
from typing import List, Optional

class ApiBatchScheduleBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    task_slugs (ApiBenchmarkTaskSlug)
    model_version_slugs (str)
      Canonical BenchmarkModelVersion.Slug values (e.g.
      'claude-sonnet-4-6-default').
    agent_slugs (str)
      Canonical Agent.Slug values (e.g.
      'claude-code-2.1.216-opus-4.8-high'). Agents are backed by model versions
      and follow the same validation checks.
    reasoning_effort (str)
      Reasoning effort to evaluate each model version at (e.g. 'high'). Each
      model version must have a config declaring this effort, matched as an exact
      string; one that doesn't is rejected with InvalidArgument. Without this the
      run inherits the default agent's effort. Setting it alongside agent_slugs
      is rejected with InvalidArgument, since an agent already pins its own
      effort.
    enqueue (bool)
      When true, the runs are appended to the async scheduler queue via the
      internal EnqueueBenchmarkTaskRuns path instead of being scheduled
      synchronously. Requires the BENCHMARK_SCHEDULER feature, enforced by that
      nested handler; a caller without it gets NOT_FOUND. A task slug that pins
      version_number queues that version.
    skip_policy (BenchmarkEnqueueSkipPolicy)
      Which pairs with existing runs to leave alone when enqueuing; rejected
      without enqueue. Unspecified means MISSING_OR_ERRORED, so a pair whose
      latest run completed, or that has a run in flight, is not queued again: set
      ALL to re-run it. A pair left alone is still reported in results, with
      run_skipped_reason saying so.
    stale_after (timedelta)
      Required by, and only valid with, STALER_THAN.
    benchmark (ApiBenchmarkSlug)
      The benchmark to attribute the queued runs to; rejected without enqueue.
      Attributed runs take the benchmark's scheduler priority, Model Proxy quota
      bucket and dispatch pause, so the caller must be able to edit it. Every
      task must be mapped under the resolved benchmark version, or the request
      is rejected with InvalidArgument.
  """

  def __init__(self):
    self._task_slugs = []
    self._model_version_slugs = []
    self._agent_slugs = []
    self._reasoning_effort = None
    self._enqueue = None
    self._skip_policy = BenchmarkEnqueueSkipPolicy.BENCHMARK_ENQUEUE_SKIP_POLICY_UNSPECIFIED
    self._stale_after = None
    self._benchmark = None
    self._freeze()

  @property
  def task_slugs(self) -> Optional[List[Optional['ApiBenchmarkTaskSlug']]]:
    return self._task_slugs

  @task_slugs.setter
  def task_slugs(self, task_slugs: Optional[List[Optional['ApiBenchmarkTaskSlug']]]):
    if task_slugs is None:
      del self.task_slugs
      return
    if not isinstance(task_slugs, list):
      raise TypeError('task_slugs must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskSlug) for t in task_slugs]):
      raise TypeError('task_slugs must contain only items of type ApiBenchmarkTaskSlug')
    self._task_slugs = task_slugs

  @property
  def model_version_slugs(self) -> Optional[List[str]]:
    r"""
    Canonical BenchmarkModelVersion.Slug values (e.g.
    'claude-sonnet-4-6-default').
    """
    return self._model_version_slugs

  @model_version_slugs.setter
  def model_version_slugs(self, model_version_slugs: Optional[List[str]]):
    if model_version_slugs is None:
      del self.model_version_slugs
      return
    if not isinstance(model_version_slugs, list):
      raise TypeError('model_version_slugs must be of type list')
    if not all([isinstance(t, str) for t in model_version_slugs]):
      raise TypeError('model_version_slugs must contain only items of type str')
    self._model_version_slugs = model_version_slugs

  @property
  def agent_slugs(self) -> Optional[List[str]]:
    r"""
    Canonical Agent.Slug values (e.g.
    'claude-code-2.1.216-opus-4.8-high'). Agents are backed by model versions
    and follow the same validation checks.
    """
    return self._agent_slugs

  @agent_slugs.setter
  def agent_slugs(self, agent_slugs: Optional[List[str]]):
    if agent_slugs is None:
      del self.agent_slugs
      return
    if not isinstance(agent_slugs, list):
      raise TypeError('agent_slugs must be of type list')
    if not all([isinstance(t, str) for t in agent_slugs]):
      raise TypeError('agent_slugs must contain only items of type str')
    self._agent_slugs = agent_slugs

  @property
  def reasoning_effort(self) -> str:
    r"""
    Reasoning effort to evaluate each model version at (e.g. 'high'). Each
    model version must have a config declaring this effort, matched as an exact
    string; one that doesn't is rejected with InvalidArgument. Without this the
    run inherits the default agent's effort. Setting it alongside agent_slugs
    is rejected with InvalidArgument, since an agent already pins its own
    effort.
    """
    return self._reasoning_effort or ""

  @reasoning_effort.setter
  def reasoning_effort(self, reasoning_effort: Optional[str]):
    if reasoning_effort is None:
      del self.reasoning_effort
      return
    if not isinstance(reasoning_effort, str):
      raise TypeError('reasoning_effort must be of type str')
    self._reasoning_effort = reasoning_effort

  @property
  def enqueue(self) -> bool:
    r"""
    When true, the runs are appended to the async scheduler queue via the
    internal EnqueueBenchmarkTaskRuns path instead of being scheduled
    synchronously. Requires the BENCHMARK_SCHEDULER feature, enforced by that
    nested handler; a caller without it gets NOT_FOUND. A task slug that pins
    version_number queues that version.
    """
    return self._enqueue or False

  @enqueue.setter
  def enqueue(self, enqueue: Optional[bool]):
    if enqueue is None:
      del self.enqueue
      return
    if not isinstance(enqueue, bool):
      raise TypeError('enqueue must be of type bool')
    self._enqueue = enqueue

  @property
  def skip_policy(self) -> 'BenchmarkEnqueueSkipPolicy':
    r"""
    Which pairs with existing runs to leave alone when enqueuing; rejected
    without enqueue. Unspecified means MISSING_OR_ERRORED, so a pair whose
    latest run completed, or that has a run in flight, is not queued again: set
    ALL to re-run it. A pair left alone is still reported in results, with
    run_skipped_reason saying so.
    """
    return self._skip_policy

  @skip_policy.setter
  def skip_policy(self, skip_policy: 'BenchmarkEnqueueSkipPolicy'):
    if skip_policy is None:
      del self.skip_policy
      return
    if not isinstance(skip_policy, BenchmarkEnqueueSkipPolicy):
      raise TypeError('skip_policy must be of type BenchmarkEnqueueSkipPolicy')
    self._skip_policy = skip_policy

  @property
  def stale_after(self) -> timedelta:
    """Required by, and only valid with, STALER_THAN."""
    return self._stale_after or None

  @stale_after.setter
  def stale_after(self, stale_after: Optional[timedelta]):
    if stale_after is None:
      del self.stale_after
      return
    if not isinstance(stale_after, timedelta):
      raise TypeError('stale_after must be of type timedelta')
    self._stale_after = stale_after

  @property
  def benchmark(self) -> Optional['ApiBenchmarkSlug']:
    r"""
    The benchmark to attribute the queued runs to; rejected without enqueue.
    Attributed runs take the benchmark's scheduler priority, Model Proxy quota
    bucket and dispatch pause, so the caller must be able to edit it. Every
    task must be mapped under the resolved benchmark version, or the request
    is rejected with InvalidArgument.
    """
    return self._benchmark

  @benchmark.setter
  def benchmark(self, benchmark: Optional['ApiBenchmarkSlug']):
    if benchmark is None:
      del self.benchmark
      return
    if not isinstance(benchmark, ApiBenchmarkSlug):
      raise TypeError('benchmark must be of type ApiBenchmarkSlug')
    self._benchmark = benchmark

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/schedule'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiBatchScheduleBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    results (BatchScheduleBenchmarkModelVersionResult)
  """

  def __init__(self):
    self._results = []
    self._freeze()

  @property
  def results(self) -> Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]:
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, BatchScheduleBenchmarkModelVersionResult) for t in results]):
      raise TypeError('results must contain only items of type BatchScheduleBenchmarkModelVersionResult')
    self._results = results


class ApiBenchmarkSlug(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      If omitted: use the current user's slug
    benchmark_slug (str)
    version_number (int)
      If omitted: the current published version, or the draft when there is
      none.
  """

  def __init__(self):
    self._owner_slug = None
    self._benchmark_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """If omitted: use the current user's slug"""
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: Optional[str]):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    return self._benchmark_slug

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: str):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug

  @property
  def version_number(self) -> int:
    r"""
    If omitted: the current published version, or the draft when there is
    none.
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class ApiBenchmarkTask(KaggleObject):
  r"""
  API equivalent of the BenchmarkTask + BenchmarkTaskVersion from
  benchmark_types.proto.

  Attributes:
    slug (ApiBenchmarkTaskSlug)
      Identifier for the task (+version)
    url (str)
      URL to the created task (or new task version)
    error (str)
      Optional error string.
    creation_state (BenchmarkTaskVersionCreationState)
      Creation state of the task version. See
      BenchmarkTaskVersion.creation_state.
    create_time (datetime)
      When this task version was created.
    creation_error_message (str)
      Error message from task version creation, if it failed.
    is_public (bool)
      Whether the task itself is public.
    source_kernel_id (int)
      ID of the backing notebook (kernel) associated with the task, if any.
    is_backing_notebook_published (bool)
      Whether the backing notebook (`source_kernel_id`) is published (public).
      Null when the task has no backing notebook.
    options (BenchmarkTaskOptions)
      Options persisted on the task version (e.g. data sources). Echoed back
      from CreateBenchmarkTask so callers can see what was attached, and
      returned on reads so the CLI can display the currently-attached sources.
      De-duplicated relative to the request input.
    source (BenchmarkTaskVersionSource)
      How this task version was produced (sandbox publish, CLI, notebook
      editor, etc.). Mirrors BenchmarkTaskVersion.source from the internal
      proto; carried through so API consumers can label sandbox-origin
      tasks distinctly from manually authored ones.
    description (str)
      Markdown details shown on the task page, from the task's current version.
    tags (str)
      Tag names on the task, in their canonical stored form (lowercase).
    provenance_sources (str)
      Free-text provenance for the data/code behind the task, from the task's
      current version. Stored as at most 4000 characters after sanitization;
      longer values are rejected with InvalidArgument on update.
    citations (ApiBenchmarkTaskCitation)
      Citations on the task's current version.
    candidate_type (BenchmarkCandidateType)
      The kind of candidate this task version runs against (model versions vs.
      agents). Mirrors BenchmarkTaskVersion.candidate_type from the internal
      proto.
    definition (BenchmarkTaskDefinition)
      What backs this task version, returned in the same shape
      CreateBenchmarkTask accepts, so a client can compare the task it declared
      against what the server stored. Populated by GetBenchmarkTask and
      ListBenchmarkTasks only when `include_definition` is set, since it costs
      several extra reads.

      Three fields will not match what was sent, so a client comparing the two
      should skip them:
       * `secrets` is always empty. Secret values are stored in the caller's
         UserSecrets, not on the task version. The references do come back, as
         `env_variables` entries with `is_secret_name` set.
       * `nested_virtualization_required` is always false. It is applied to the
         session when the task runs and is not stored on the task version.
       * `title` is always set. It holds the stored name, which is trimmed and
         which defaults to the task slug when the client sent no title, so a
         task's first version can report a title the client never sent.

      The first two are empty for everyone, so `definition_partial` stays false
      for them -- nothing was hidden from this particular caller.

      Separately, slugs naming a candidate, auxiliary config or dataset the
      reader cannot read are omitted, and `env_variables` is omitted wholesale
      unless the caller could update the task. `definition_partial` is set
      whenever anything is omitted for one of those reasons.
    definition_partial (bool)
      True when `definition` is missing something the version declares.
      Separates 'declares no default candidate' from 'declares one that did not
      come back', which otherwise look identical and would have a client push a
      spurious change. False when `definition` is unset.

      Usually this means the caller may not read what was named. It is also set
      when a referenced dataset cannot be named -- one still being created, say
      -- so a client cannot read it as a statement about its own permissions.
    artifact_path (str)
      Glob, relative to a run's output root, naming the file the task's preview
      shows, e.g. *.mp4. Unset if the task has none.
    artifact_type (BenchmarkArenaArtifactType)
      How the artifact is rendered. Set iff artifact_path is.
    are_run_artifacts_public (bool)
      Whether everyone who can read the task can also read its raw run artifacts
      (run.json, logs, output files, trajectories), rather than only the task's
      writers.
  """

  def __init__(self):
    self._slug = None
    self._url = ""
    self._error = None
    self._creation_state = BenchmarkTaskVersionCreationState.BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED
    self._create_time = None
    self._creation_error_message = None
    self._is_public = None
    self._source_kernel_id = None
    self._is_backing_notebook_published = None
    self._options = None
    self._source = BenchmarkTaskVersionSource.BENCHMARK_TASK_VERSION_SOURCE_UNSPECIFIED
    self._description = None
    self._tags = []
    self._provenance_sources = None
    self._citations = []
    self._candidate_type = BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED
    self._definition = None
    self._definition_partial = False
    self._artifact_path = None
    self._artifact_type = None
    self._are_run_artifacts_public = None
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    """Identifier for the task (+version)"""
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def url(self) -> str:
    """URL to the created task (or new task version)"""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def error(self) -> str:
    """Optional error string."""
    return self._error or ""

  @error.setter
  def error(self, error: Optional[str]):
    if error is None:
      del self.error
      return
    if not isinstance(error, str):
      raise TypeError('error must be of type str')
    self._error = error

  @property
  def creation_state(self) -> 'BenchmarkTaskVersionCreationState':
    r"""
    Creation state of the task version. See
    BenchmarkTaskVersion.creation_state.
    """
    return self._creation_state

  @creation_state.setter
  def creation_state(self, creation_state: 'BenchmarkTaskVersionCreationState'):
    if creation_state is None:
      del self.creation_state
      return
    if not isinstance(creation_state, BenchmarkTaskVersionCreationState):
      raise TypeError('creation_state must be of type BenchmarkTaskVersionCreationState')
    self._creation_state = creation_state

  @property
  def create_time(self) -> datetime:
    """When this task version was created."""
    return self._create_time

  @create_time.setter
  def create_time(self, create_time: datetime):
    if create_time is None:
      del self.create_time
      return
    if not isinstance(create_time, datetime):
      raise TypeError('create_time must be of type datetime')
    self._create_time = create_time

  @property
  def creation_error_message(self) -> str:
    """Error message from task version creation, if it failed."""
    return self._creation_error_message or ""

  @creation_error_message.setter
  def creation_error_message(self, creation_error_message: Optional[str]):
    if creation_error_message is None:
      del self.creation_error_message
      return
    if not isinstance(creation_error_message, str):
      raise TypeError('creation_error_message must be of type str')
    self._creation_error_message = creation_error_message

  @property
  def is_public(self) -> bool:
    """Whether the task itself is public."""
    return self._is_public or False

  @is_public.setter
  def is_public(self, is_public: Optional[bool]):
    if is_public is None:
      del self.is_public
      return
    if not isinstance(is_public, bool):
      raise TypeError('is_public must be of type bool')
    self._is_public = is_public

  @property
  def source_kernel_id(self) -> int:
    """ID of the backing notebook (kernel) associated with the task, if any."""
    return self._source_kernel_id or 0

  @source_kernel_id.setter
  def source_kernel_id(self, source_kernel_id: Optional[int]):
    if source_kernel_id is None:
      del self.source_kernel_id
      return
    if not isinstance(source_kernel_id, int):
      raise TypeError('source_kernel_id must be of type int')
    self._source_kernel_id = source_kernel_id

  @property
  def is_backing_notebook_published(self) -> bool:
    r"""
    Whether the backing notebook (`source_kernel_id`) is published (public).
    Null when the task has no backing notebook.
    """
    return self._is_backing_notebook_published or False

  @is_backing_notebook_published.setter
  def is_backing_notebook_published(self, is_backing_notebook_published: Optional[bool]):
    if is_backing_notebook_published is None:
      del self.is_backing_notebook_published
      return
    if not isinstance(is_backing_notebook_published, bool):
      raise TypeError('is_backing_notebook_published must be of type bool')
    self._is_backing_notebook_published = is_backing_notebook_published

  @property
  def are_run_artifacts_public(self) -> bool:
    r"""
    Whether everyone who can read the task can also read its raw run artifacts
    (run.json, logs, output files, trajectories), rather than only the task's
    writers.
    """
    return self._are_run_artifacts_public or False

  @are_run_artifacts_public.setter
  def are_run_artifacts_public(self, are_run_artifacts_public: Optional[bool]):
    if are_run_artifacts_public is None:
      del self.are_run_artifacts_public
      return
    if not isinstance(are_run_artifacts_public, bool):
      raise TypeError('are_run_artifacts_public must be of type bool')
    self._are_run_artifacts_public = are_run_artifacts_public

  @property
  def options(self) -> Optional['BenchmarkTaskOptions']:
    r"""
    Options persisted on the task version (e.g. data sources). Echoed back
    from CreateBenchmarkTask so callers can see what was attached, and
    returned on reads so the CLI can display the currently-attached sources.
    De-duplicated relative to the request input.
    """
    return self._options or None

  @options.setter
  def options(self, options: Optional[Optional['BenchmarkTaskOptions']]):
    if options is None:
      del self.options
      return
    if not isinstance(options, BenchmarkTaskOptions):
      raise TypeError('options must be of type BenchmarkTaskOptions')
    self._options = options

  @property
  def source(self) -> 'BenchmarkTaskVersionSource':
    r"""
    How this task version was produced (sandbox publish, CLI, notebook
    editor, etc.). Mirrors BenchmarkTaskVersion.source from the internal
    proto; carried through so API consumers can label sandbox-origin
    tasks distinctly from manually authored ones.
    """
    return self._source

  @source.setter
  def source(self, source: 'BenchmarkTaskVersionSource'):
    if source is None:
      del self.source
      return
    if not isinstance(source, BenchmarkTaskVersionSource):
      raise TypeError('source must be of type BenchmarkTaskVersionSource')
    self._source = source

  @property
  def description(self) -> str:
    """Markdown details shown on the task page, from the task's current version."""
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def tags(self) -> Optional[List[str]]:
    """Tag names on the task, in their canonical stored form (lowercase)."""
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[str]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, str) for t in tags]):
      raise TypeError('tags must contain only items of type str')
    self._tags = tags

  @property
  def provenance_sources(self) -> str:
    r"""
    Free-text provenance for the data/code behind the task, from the task's
    current version. Stored as at most 4000 characters after sanitization;
    longer values are rejected with InvalidArgument on update.
    """
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: Optional[str]):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def citations(self) -> Optional[List[Optional['ApiBenchmarkTaskCitation']]]:
    """Citations on the task's current version."""
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['ApiBenchmarkTaskCitation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskCitation) for t in citations]):
      raise TypeError('citations must contain only items of type ApiBenchmarkTaskCitation')
    self._citations = citations

  @property
  def candidate_type(self) -> 'BenchmarkCandidateType':
    r"""
    The kind of candidate this task version runs against (model versions vs.
    agents). Mirrors BenchmarkTaskVersion.candidate_type from the internal
    proto.
    """
    return self._candidate_type

  @candidate_type.setter
  def candidate_type(self, candidate_type: 'BenchmarkCandidateType'):
    if candidate_type is None:
      del self.candidate_type
      return
    if not isinstance(candidate_type, BenchmarkCandidateType):
      raise TypeError('candidate_type must be of type BenchmarkCandidateType')
    self._candidate_type = candidate_type

  @property
  def definition(self) -> Optional['BenchmarkTaskDefinition']:
    r"""
    What backs this task version, returned in the same shape
    CreateBenchmarkTask accepts, so a client can compare the task it declared
    against what the server stored. Populated by GetBenchmarkTask and
    ListBenchmarkTasks only when `include_definition` is set, since it costs
    several extra reads.

    Three fields will not match what was sent, so a client comparing the two
    should skip them:
     * `secrets` is always empty. Secret values are stored in the caller's
       UserSecrets, not on the task version. The references do come back, as
       `env_variables` entries with `is_secret_name` set.
     * `nested_virtualization_required` is always false. It is applied to the
       session when the task runs and is not stored on the task version.
     * `title` is always set. It holds the stored name, which is trimmed and
       which defaults to the task slug when the client sent no title, so a
       task's first version can report a title the client never sent.

    The first two are empty for everyone, so `definition_partial` stays false
    for them -- nothing was hidden from this particular caller.

    Separately, slugs naming a candidate, auxiliary config or dataset the
    reader cannot read are omitted, and `env_variables` is omitted wholesale
    unless the caller could update the task. `definition_partial` is set
    whenever anything is omitted for one of those reasons.
    """
    return self._definition or None

  @definition.setter
  def definition(self, definition: Optional[Optional['BenchmarkTaskDefinition']]):
    if definition is None:
      del self.definition
      return
    if not isinstance(definition, BenchmarkTaskDefinition):
      raise TypeError('definition must be of type BenchmarkTaskDefinition')
    self._definition = definition

  @property
  def definition_partial(self) -> bool:
    r"""
    True when `definition` is missing something the version declares.
    Separates 'declares no default candidate' from 'declares one that did not
    come back', which otherwise look identical and would have a client push a
    spurious change. False when `definition` is unset.

    Usually this means the caller may not read what was named. It is also set
    when a referenced dataset cannot be named -- one still being created, say
    -- so a client cannot read it as a statement about its own permissions.
    """
    return self._definition_partial

  @definition_partial.setter
  def definition_partial(self, definition_partial: bool):
    if definition_partial is None:
      del self.definition_partial
      return
    if not isinstance(definition_partial, bool):
      raise TypeError('definition_partial must be of type bool')
    self._definition_partial = definition_partial

  @property
  def artifact_path(self) -> str:
    r"""
    Glob, relative to a run's output root, naming the file the task's preview
    shows, e.g. *.mp4. Unset if the task has none.
    """
    return self._artifact_path or ""

  @artifact_path.setter
  def artifact_path(self, artifact_path: Optional[str]):
    if artifact_path is None:
      del self.artifact_path
      return
    if not isinstance(artifact_path, str):
      raise TypeError('artifact_path must be of type str')
    self._artifact_path = artifact_path

  @property
  def artifact_type(self) -> 'BenchmarkArenaArtifactType':
    """How the artifact is rendered. Set iff artifact_path is."""
    return self._artifact_type or BenchmarkArenaArtifactType.BENCHMARK_ARENA_ARTIFACT_TYPE_UNSPECIFIED

  @artifact_type.setter
  def artifact_type(self, artifact_type: Optional['BenchmarkArenaArtifactType']):
    if artifact_type is None:
      del self.artifact_type
      return
    if not isinstance(artifact_type, BenchmarkArenaArtifactType):
      raise TypeError('artifact_type must be of type BenchmarkArenaArtifactType')
    self._artifact_type = artifact_type


class ApiBenchmarkTaskCitation(KaggleObject):
  r"""
  A reference supporting the data or code behind a benchmark task.

  Attributes:
    title (str)
      Display text for the reference. Free-form; not validated.
    url (str)
      Link to the reference, normalized to an absolute http(s) URL. A value with
      no scheme is stored as http://, so this may differ from what was sent.
  """

  def __init__(self):
    self._title = ""
    self._url = ""
    self._freeze()

  @property
  def title(self) -> str:
    """Display text for the reference. Free-form; not validated."""
    return self._title

  @title.setter
  def title(self, title: str):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def url(self) -> str:
    r"""
    Link to the reference, normalized to an absolute http(s) URL. A value with
    no scheme is stored as http://, so this may differ from what was sent.
    """
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url


class ApiBenchmarkTaskRun(KaggleObject):
  r"""
  API equivalent of the BenchmarkTaskRun from benchmark_types.proto.

  Attributes:
    task_slug (ApiBenchmarkTaskSlug)
      Task that was invoked.
    model_version_slug (str)
      Model candidate against the task. This is the canonical
      BenchmarkModelVersion.Slug (e.g. 'claude-sonnet-4-6-default'), matching
      the format produced by BatchScheduleBenchmarkTaskRuns.
    id (int)
      Run identifier.
    state (BenchmarkTaskRunState)
      State of the run
    start_time (datetime)
      Start time of the run
    end_time (datetime)
      End time of the run
    error_message (str)
      Error message if the run failed
    agent_slug (str)
      Agent candidate against the task, when the run was scheduled against an
      agent rather than a bare model version. This is the Agent.Slug; unset for
      model-version runs.
    model_version_config_slug (str)
      The resolved BenchmarkModelVersionConfig the run was dispatched against.
      This is the BenchmarkModelVersionConfig.Slug. During the current transition
      to config-based dispatch, this is only set when the run was scheduled with
      a reasoning effort; runs against a bare model version (and historical runs
      that predate the configs table) leave it unset.
    result (ApiBenchmarkTaskRunResult)
      Result the run produced (score or pass/fail). Unset for runs that have not
      produced a result (e.g. still queued/running, errored, or no result
      recorded).
  """

  def __init__(self):
    self._task_slug = None
    self._model_version_slug = ""
    self._id = 0
    self._state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._start_time = None
    self._end_time = None
    self._error_message = None
    self._agent_slug = None
    self._model_version_config_slug = None
    self._result = None
    self._freeze()

  @property
  def task_slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    """Task that was invoked."""
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: Optional['ApiBenchmarkTaskSlug']):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, ApiBenchmarkTaskSlug):
      raise TypeError('task_slug must be of type ApiBenchmarkTaskSlug')
    self._task_slug = task_slug

  @property
  def model_version_slug(self) -> str:
    r"""
    Model candidate against the task. This is the canonical
    BenchmarkModelVersion.Slug (e.g. 'claude-sonnet-4-6-default'), matching
    the format produced by BatchScheduleBenchmarkTaskRuns.
    """
    return self._model_version_slug

  @model_version_slug.setter
  def model_version_slug(self, model_version_slug: str):
    if model_version_slug is None:
      del self.model_version_slug
      return
    if not isinstance(model_version_slug, str):
      raise TypeError('model_version_slug must be of type str')
    self._model_version_slug = model_version_slug

  @property
  def id(self) -> int:
    """Run identifier."""
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def state(self) -> 'BenchmarkTaskRunState':
    """State of the run"""
    return self._state

  @state.setter
  def state(self, state: 'BenchmarkTaskRunState'):
    if state is None:
      del self.state
      return
    if not isinstance(state, BenchmarkTaskRunState):
      raise TypeError('state must be of type BenchmarkTaskRunState')
    self._state = state

  @property
  def start_time(self) -> datetime:
    """Start time of the run"""
    return self._start_time or None

  @start_time.setter
  def start_time(self, start_time: Optional[datetime]):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    """End time of the run"""
    return self._end_time or None

  @end_time.setter
  def end_time(self, end_time: Optional[datetime]):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time

  @property
  def error_message(self) -> str:
    """Error message if the run failed"""
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message

  @property
  def agent_slug(self) -> str:
    r"""
    Agent candidate against the task, when the run was scheduled against an
    agent rather than a bare model version. This is the Agent.Slug; unset for
    model-version runs.
    """
    return self._agent_slug or ""

  @agent_slug.setter
  def agent_slug(self, agent_slug: Optional[str]):
    if agent_slug is None:
      del self.agent_slug
      return
    if not isinstance(agent_slug, str):
      raise TypeError('agent_slug must be of type str')
    self._agent_slug = agent_slug

  @property
  def model_version_config_slug(self) -> str:
    r"""
    The resolved BenchmarkModelVersionConfig the run was dispatched against.
    This is the BenchmarkModelVersionConfig.Slug. During the current transition
    to config-based dispatch, this is only set when the run was scheduled with
    a reasoning effort; runs against a bare model version (and historical runs
    that predate the configs table) leave it unset.
    """
    return self._model_version_config_slug or ""

  @model_version_config_slug.setter
  def model_version_config_slug(self, model_version_config_slug: Optional[str]):
    if model_version_config_slug is None:
      del self.model_version_config_slug
      return
    if not isinstance(model_version_config_slug, str):
      raise TypeError('model_version_config_slug must be of type str')
    self._model_version_config_slug = model_version_config_slug

  @property
  def result(self) -> Optional['ApiBenchmarkTaskRunResult']:
    r"""
    Result the run produced (score or pass/fail). Unset for runs that have not
    produced a result (e.g. still queued/running, errored, or no result
    recorded).
    """
    return self._result or None

  @result.setter
  def result(self, result: Optional[Optional['ApiBenchmarkTaskRunResult']]):
    if result is None:
      del self.result
      return
    if not isinstance(result, ApiBenchmarkTaskRunResult):
      raise TypeError('result must be of type ApiBenchmarkTaskRunResult')
    self._result = result


class ApiBenchmarkTaskRunIds(KaggleObject):
  r"""
  A repeated field cannot live in a oneof directly, hence the wrapper.

  Attributes:
    ids (int)
  """

  def __init__(self):
    self._ids = []
    self._freeze()

  @property
  def ids(self) -> Optional[List[int]]:
    return self._ids

  @ids.setter
  def ids(self, ids: Optional[List[int]]):
    if ids is None:
      del self.ids
      return
    if not isinstance(ids, list):
      raise TypeError('ids must be of type list')
    if not all([isinstance(t, int) for t in ids]):
      raise TypeError('ids must contain only items of type int')
    self._ids = ids


class ApiBenchmarkTaskRunResult(KaggleObject):
  r"""
  Minimal public view of a run's result. Mirrors the numeric/boolean value the
  task UI renders; the internal BenchmarkTaskRunResult carries additional
  metrics/assertions that are intentionally not exposed here for now.

  Attributes:
    numeric_result (float)
    boolean_result (bool)
  """

  def __init__(self):
    self._numeric_result = None
    self._boolean_result = None
    self._freeze()

  @property
  def numeric_result(self) -> float:
    return self._numeric_result or 0.0

  @numeric_result.setter
  def numeric_result(self, numeric_result: float):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, float):
      raise TypeError('numeric_result must be of type float')
    del self.boolean_result
    self._numeric_result = numeric_result

  @property
  def boolean_result(self) -> bool:
    return self._boolean_result or False

  @boolean_result.setter
  def boolean_result(self, boolean_result: bool):
    if boolean_result is None:
      del self.boolean_result
      return
    if not isinstance(boolean_result, bool):
      raise TypeError('boolean_result must be of type bool')
    del self.numeric_result
    self._boolean_result = boolean_result


class ApiBenchmarkTaskSlug(KaggleObject):
  r"""
  This is an identifier, equivalent of a task version ID

  Attributes:
    owner_slug (str)
      The owner slug
      If omitted: use the current user's slug
    task_slug (str)
      The task slug
    version_number (int)
      Version number
      If omitted: use the latest version
  """

  def __init__(self):
    self._owner_slug = None
    self._task_slug = ""
    self._version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    r"""
    The owner slug
    If omitted: use the current user's slug
    """
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: Optional[str]):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def task_slug(self) -> str:
    """The task slug"""
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: str):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, str):
      raise TypeError('task_slug must be of type str')
    self._task_slug = task_slug

  @property
  def version_number(self) -> int:
    r"""
    Version number
    If omitted: use the latest version
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class ApiBenchmarkTaskSlugs(KaggleObject):
  r"""
  A repeated field cannot live in a oneof directly, hence the wrapper.

  Attributes:
    slugs (ApiBenchmarkTaskSlug)
  """

  def __init__(self):
    self._slugs = []
    self._freeze()

  @property
  def slugs(self) -> Optional[List[Optional['ApiBenchmarkTaskSlug']]]:
    return self._slugs

  @slugs.setter
  def slugs(self, slugs: Optional[List[Optional['ApiBenchmarkTaskSlug']]]):
    if slugs is None:
      del self.slugs
      return
    if not isinstance(slugs, list):
      raise TypeError('slugs must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskSlug) for t in slugs]):
      raise TypeError('slugs must contain only items of type ApiBenchmarkTaskSlug')
    self._slugs = slugs


class ApiCancelBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    task_slugs (ApiBenchmarkTaskSlugs)
      Every run of these tasks.
    model_version (ApiModelVersionCandidate)
    agent_slug (str)
      A canonical Agent.Slug (e.g. 'claude-code-2.1.216-opus-4.8-high').
    include_active (bool)
      When false, only queued runs are cancelled, leaving in-flight work alone.
      When true, running runs are also terminated.
    run_ids (ApiBenchmarkTaskRunIds)
      Exactly these runs, addressed by the ids ApiBenchmarkTaskRun reports.
  """

  def __init__(self):
    self._task_slugs = None
    self._model_version = None
    self._agent_slug = None
    self._include_active = False
    self._run_ids = None
    self._freeze()

  @property
  def task_slugs(self) -> Optional['ApiBenchmarkTaskSlugs']:
    """Every run of these tasks."""
    return self._task_slugs or None

  @task_slugs.setter
  def task_slugs(self, task_slugs: Optional['ApiBenchmarkTaskSlugs']):
    if task_slugs is None:
      del self.task_slugs
      return
    if not isinstance(task_slugs, ApiBenchmarkTaskSlugs):
      raise TypeError('task_slugs must be of type ApiBenchmarkTaskSlugs')
    del self.run_ids
    self._task_slugs = task_slugs

  @property
  def run_ids(self) -> Optional['ApiBenchmarkTaskRunIds']:
    """Exactly these runs, addressed by the ids ApiBenchmarkTaskRun reports."""
    return self._run_ids or None

  @run_ids.setter
  def run_ids(self, run_ids: Optional['ApiBenchmarkTaskRunIds']):
    if run_ids is None:
      del self.run_ids
      return
    if not isinstance(run_ids, ApiBenchmarkTaskRunIds):
      raise TypeError('run_ids must be of type ApiBenchmarkTaskRunIds')
    del self.task_slugs
    self._run_ids = run_ids

  @property
  def model_version(self) -> Optional['ApiModelVersionCandidate']:
    return self._model_version or None

  @model_version.setter
  def model_version(self, model_version: Optional['ApiModelVersionCandidate']):
    if model_version is None:
      del self.model_version
      return
    if not isinstance(model_version, ApiModelVersionCandidate):
      raise TypeError('model_version must be of type ApiModelVersionCandidate')
    del self.agent_slug
    self._model_version = model_version

  @property
  def agent_slug(self) -> str:
    """A canonical Agent.Slug (e.g. 'claude-code-2.1.216-opus-4.8-high')."""
    return self._agent_slug or ""

  @agent_slug.setter
  def agent_slug(self, agent_slug: str):
    if agent_slug is None:
      del self.agent_slug
      return
    if not isinstance(agent_slug, str):
      raise TypeError('agent_slug must be of type str')
    del self.model_version
    self._agent_slug = agent_slug

  @property
  def include_active(self) -> bool:
    r"""
    When false, only queued runs are cancelled, leaving in-flight work alone.
    When true, running runs are also terminated.
    """
    return self._include_active

  @include_active.setter
  def include_active(self, include_active: bool):
    if include_active is None:
      del self.include_active
      return
    if not isinstance(include_active, bool):
      raise TypeError('include_active must be of type bool')
    self._include_active = include_active

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/cancel'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiCancelBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    queued_cancelled_count (int)
      Number of queued runs cancelled.
    active_terminated_count (int)
      Number of running runs whose sessions were successfully terminated. Only
      ever non-zero when include_active was set. A run whose session could not
      be reached is left running and excluded from this count, so a caller that
      needs everything stopped should re-issue the request until it stops
      reporting fewer than it expects.
  """

  def __init__(self):
    self._queued_cancelled_count = 0
    self._active_terminated_count = 0
    self._freeze()

  @property
  def queued_cancelled_count(self) -> int:
    """Number of queued runs cancelled."""
    return self._queued_cancelled_count

  @queued_cancelled_count.setter
  def queued_cancelled_count(self, queued_cancelled_count: int):
    if queued_cancelled_count is None:
      del self.queued_cancelled_count
      return
    if not isinstance(queued_cancelled_count, int):
      raise TypeError('queued_cancelled_count must be of type int')
    self._queued_cancelled_count = queued_cancelled_count

  @property
  def active_terminated_count(self) -> int:
    r"""
    Number of running runs whose sessions were successfully terminated. Only
    ever non-zero when include_active was set. A run whose session could not
    be reached is left running and excluded from this count, so a caller that
    needs everything stopped should re-issue the request until it stops
    reporting fewer than it expects.
    """
    return self._active_terminated_count

  @active_terminated_count.setter
  def active_terminated_count(self, active_terminated_count: int):
    if active_terminated_count is None:
      del self.active_terminated_count
      return
    if not isinstance(active_terminated_count, int):
      raise TypeError('active_terminated_count must be of type int')
    self._active_terminated_count = active_terminated_count

  @property
  def queuedCancelledCount(self):
    return self.queued_cancelled_count

  @property
  def activeTerminatedCount(self):
    return self.active_terminated_count


class ApiCreateBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (str)
      The slug for the task without the user's namespace. (ex: my-task instead of
      username/my-task). This should match the slug in the kaggle-benchmarks
      decorator in the code.
    text (str)
      The task's (or task version's) source code
    options (BenchmarkTaskOptions)
      Optional task options (e.g. data sources) to attach to the underlying
      notebook for this task version. Changing the options bumps the task
      version.

      Semantics for omitted/empty fields: each sub-field within `options` is
      applied as-given. Omitting `options` entirely on a new version is
      equivalent to sending an empty `BenchmarkTaskOptions`, which clears
      all previously-attached sources for that version. Callers that want to
      preserve the previous version's options must echo them back on each
      push.
    definition (BenchmarkTaskDefinition)
      What backs this task (notebook / docker image / Harbor Kaggle datasets)
      and any per-type configuration. Pairs with the BenchmarkTaskDefinitionType
      enum stored on the entity.
    validation_config (ApiTaskCreationValidationConfig)
      Optional. How the created task version is validated.
  """

  def __init__(self):
    self._slug = ""
    self._text = ""
    self._options = None
    self._definition = None
    self._validation_config = None
    self._freeze()

  @property
  def slug(self) -> str:
    r"""
    The slug for the task without the user's namespace. (ex: my-task instead of
    username/my-task). This should match the slug in the kaggle-benchmarks
    decorator in the code.
    """
    return self._slug

  @slug.setter
  def slug(self, slug: str):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, str):
      raise TypeError('slug must be of type str')
    self._slug = slug

  @property
  def text(self) -> str:
    """The task's (or task version's) source code"""
    return self._text

  @text.setter
  def text(self, text: str):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

  @property
  def options(self) -> Optional['BenchmarkTaskOptions']:
    r"""
    Optional task options (e.g. data sources) to attach to the underlying
    notebook for this task version. Changing the options bumps the task
    version.

    Semantics for omitted/empty fields: each sub-field within `options` is
    applied as-given. Omitting `options` entirely on a new version is
    equivalent to sending an empty `BenchmarkTaskOptions`, which clears
    all previously-attached sources for that version. Callers that want to
    preserve the previous version's options must echo them back on each
    push.
    """
    return self._options or None

  @options.setter
  def options(self, options: Optional[Optional['BenchmarkTaskOptions']]):
    if options is None:
      del self.options
      return
    if not isinstance(options, BenchmarkTaskOptions):
      raise TypeError('options must be of type BenchmarkTaskOptions')
    self._options = options

  @property
  def definition(self) -> Optional['BenchmarkTaskDefinition']:
    r"""
    What backs this task (notebook / docker image / Harbor Kaggle datasets)
    and any per-type configuration. Pairs with the BenchmarkTaskDefinitionType
    enum stored on the entity.
    """
    return self._definition or None

  @definition.setter
  def definition(self, definition: Optional[Optional['BenchmarkTaskDefinition']]):
    if definition is None:
      del self.definition
      return
    if not isinstance(definition, BenchmarkTaskDefinition):
      raise TypeError('definition must be of type BenchmarkTaskDefinition')
    self._definition = definition

  @property
  def validation_config(self) -> Optional['ApiTaskCreationValidationConfig']:
    """Optional. How the created task version is validated."""
    return self._validation_config or None

  @validation_config.setter
  def validation_config(self, validation_config: Optional[Optional['ApiTaskCreationValidationConfig']]):
    if validation_config is None:
      del self.validation_config
      return
    if not isinstance(validation_config, ApiTaskCreationValidationConfig):
      raise TypeError('validation_config must be of type ApiTaskCreationValidationConfig')
    self._validation_config = validation_config

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/push'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiDownloadBenchmarkTaskRunOutputRequest(KaggleObject):
  r"""
  Attributes:
    run_id (int)
    include_source (bool)
      When true, the returned zip also contains the kernel session's source
      files. For benchmark task runs (which are notebook kernels) that means
      `__notebook__.ipynb` and `__notebook_source__.ipynb`.
  """

  def __init__(self):
    self._run_id = 0
    self._include_source = False
    self._freeze()

  @property
  def run_id(self) -> int:
    return self._run_id

  @run_id.setter
  def run_id(self, run_id: int):
    if run_id is None:
      del self.run_id
      return
    if not isinstance(run_id, int):
      raise TypeError('run_id must be of type int')
    self._run_id = run_id

  @property
  def include_source(self) -> bool:
    r"""
    When true, the returned zip also contains the kernel session's source
    files. For benchmark task runs (which are notebook kernels) that means
    `__notebook__.ipynb` and `__notebook_source__.ipynb`.
    """
    return self._include_source

  @include_source.setter
  def include_source(self, include_source: bool):
    if include_source is None:
      del self.include_source
      return
    if not isinstance(include_source, bool):
      raise TypeError('include_source must be of type bool')
    self._include_source = include_source

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/{run_id}/output'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/tasks/runs/{run_id}/output'


class ApiGetBenchmarkSchedulerStatusRequest(KaggleObject):
  r"""
  No scope field: this endpoint always reports the caller's own runs.

  """

  pass
  def endpoint(self):
    path = '/api/v1/benchmarks/scheduler/status'
    return path.format_map(self.to_field_map(self))


class ApiGetBenchmarkTaskQuotaRequest(KaggleObject):
  r"""
  """

  pass
  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/quota'
    return path.format_map(self.to_field_map(self))


class ApiGetBenchmarkTaskQuotaResponse(KaggleObject):
  r"""
  Attributes:
    daily_quota_used (float)
      How much quota that was used in the time period (daily), in USD.
    total_daily_quota_allowed (float)
      Upper limit of allowed quota in the time period (daily), in USD.
  """

  def __init__(self):
    self._daily_quota_used = 0.0
    self._total_daily_quota_allowed = 0.0
    self._freeze()

  @property
  def daily_quota_used(self) -> float:
    """How much quota that was used in the time period (daily), in USD."""
    return self._daily_quota_used

  @daily_quota_used.setter
  def daily_quota_used(self, daily_quota_used: float):
    if daily_quota_used is None:
      del self.daily_quota_used
      return
    if not isinstance(daily_quota_used, float):
      raise TypeError('daily_quota_used must be of type float')
    self._daily_quota_used = daily_quota_used

  @property
  def total_daily_quota_allowed(self) -> float:
    """Upper limit of allowed quota in the time period (daily), in USD."""
    return self._total_daily_quota_allowed

  @total_daily_quota_allowed.setter
  def total_daily_quota_allowed(self, total_daily_quota_allowed: float):
    if total_daily_quota_allowed is None:
      del self.total_daily_quota_allowed
      return
    if not isinstance(total_daily_quota_allowed, float):
      raise TypeError('total_daily_quota_allowed must be of type float')
    self._total_daily_quota_allowed = total_daily_quota_allowed

  @property
  def dailyQuotaUsed(self):
    return self.daily_quota_used

  @property
  def totalDailyQuotaAllowed(self):
    return self.total_daily_quota_allowed


class ApiGetBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (ApiBenchmarkTaskSlug)
    include_definition (bool)
      Populate `definition` and `definition_partial`. Off by default since it
      costs extra reads.
  """

  def __init__(self):
    self._slug = None
    self._include_definition = False
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def include_definition(self) -> bool:
    r"""
    Populate `definition` and `definition_partial`. Off by default since it
    costs extra reads.
    """
    return self._include_definition

  @include_definition.setter
  def include_definition(self, include_definition: bool):
    if include_definition is None:
      del self.include_definition
      return
    if not isinstance(include_definition, bool):
      raise TypeError('include_definition must be of type bool')
    self._include_definition = include_definition

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/{slug.task_slug}'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/tasks/{slug.task_slug}'


class ApiGetBenchmarkTaskRunLogsRequest(KaggleObject):
  r"""
  Attributes:
    run_id (int)
  """

  def __init__(self):
    self._run_id = 0
    self._freeze()

  @property
  def run_id(self) -> int:
    return self._run_id

  @run_id.setter
  def run_id(self, run_id: int):
    if run_id is None:
      del self.run_id
      return
    if not isinstance(run_id, int):
      raise TypeError('run_id must be of type int')
    self._run_id = run_id

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/{run_id}/logs'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/benchmarks/tasks/runs/{run_id}/logs'


class ApiListBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    task_slug (ApiBenchmarkTaskSlug)
    model_version_slugs (str)
      Filter to runs for these model versions. Accepts the canonical
      BenchmarkModelVersion.Slug (preferred, e.g. 'claude-sonnet-4-6-default')
      or the legacy ModelProxySlug (e.g. 'anthropic/claude-sonnet-4-6@default')
      for backward compatibility.
    page_size (int)
    page_token (str)
    skip (int)
  """

  def __init__(self):
    self._task_slug = None
    self._model_version_slugs = []
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._freeze()

  @property
  def task_slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    return self._task_slug

  @task_slug.setter
  def task_slug(self, task_slug: Optional['ApiBenchmarkTaskSlug']):
    if task_slug is None:
      del self.task_slug
      return
    if not isinstance(task_slug, ApiBenchmarkTaskSlug):
      raise TypeError('task_slug must be of type ApiBenchmarkTaskSlug')
    self._task_slug = task_slug

  @property
  def model_version_slugs(self) -> Optional[List[str]]:
    r"""
    Filter to runs for these model versions. Accepts the canonical
    BenchmarkModelVersion.Slug (preferred, e.g. 'claude-sonnet-4-6-default')
    or the legacy ModelProxySlug (e.g. 'anthropic/claude-sonnet-4-6@default')
    for backward compatibility.
    """
    return self._model_version_slugs

  @model_version_slugs.setter
  def model_version_slugs(self, model_version_slugs: Optional[List[str]]):
    if model_version_slugs is None:
      del self.model_version_slugs
      return
    if not isinstance(model_version_slugs, list):
      raise TypeError('model_version_slugs must be of type list')
    if not all([isinstance(t, str) for t in model_version_slugs]):
      raise TypeError('model_version_slugs must contain only items of type str')
    self._model_version_slugs = model_version_slugs

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/runs/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    runs (ApiBenchmarkTaskRun)
    total_results (int)
    next_page_token (str)
  """

  def __init__(self):
    self._runs = []
    self._total_results = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def runs(self) -> Optional[List[Optional['ApiBenchmarkTaskRun']]]:
    return self._runs

  @runs.setter
  def runs(self, runs: Optional[List[Optional['ApiBenchmarkTaskRun']]]):
    if runs is None:
      del self.runs
      return
    if not isinstance(runs, list):
      raise TypeError('runs must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskRun) for t in runs]):
      raise TypeError('runs must contain only items of type ApiBenchmarkTaskRun')
    self._runs = runs

  @property
  def total_results(self) -> int:
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def totalResults(self):
    return self.total_results

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiListBenchmarkTasksRequest(KaggleObject):
  r"""
  Attributes:
    status_filter (str)
      Filter by task creation status (e.g. 'created', 'error').
    regex_filter (str)
      Filter task slugs by regular expression.
    page_size (int)
    page_token (str)
    skip (int)
    owner_slug (str)
      Filter to tasks owned by this user (their username / profile slug). Only
      tasks the caller is allowed to see are returned, so pass your own slug to
      list just the tasks you created. When omitted, returns tasks the caller
      owns or collaborates on.
    benchmark_slug (str)
      Filter to the tasks belonging to this benchmark, identified by its slug
      (paired with owner_slug, which then names the benchmark's owner rather than
      the task's owner). Resolves to the benchmark version's mapped child tasks.
      When omitted, the listing is not scoped to a benchmark.
    version_number (int)
      Optional benchmark version to target when benchmark_slug is set. When
      omitted, the benchmark's current published (or draft) version is used.
    include_definition (bool)
      Populate `definition` and `definition_partial` on each task. Off by
      default since it costs extra reads.
  """

  def __init__(self):
    self._status_filter = None
    self._regex_filter = None
    self._page_size = 0
    self._page_token = ""
    self._skip = 0
    self._owner_slug = None
    self._benchmark_slug = None
    self._version_number = None
    self._include_definition = False
    self._freeze()

  @property
  def status_filter(self) -> str:
    """Filter by task creation status (e.g. 'created', 'error')."""
    return self._status_filter or ""

  @status_filter.setter
  def status_filter(self, status_filter: Optional[str]):
    if status_filter is None:
      del self.status_filter
      return
    if not isinstance(status_filter, str):
      raise TypeError('status_filter must be of type str')
    self._status_filter = status_filter

  @property
  def regex_filter(self) -> str:
    """Filter task slugs by regular expression."""
    return self._regex_filter or ""

  @regex_filter.setter
  def regex_filter(self, regex_filter: Optional[str]):
    if regex_filter is None:
      del self.regex_filter
      return
    if not isinstance(regex_filter, str):
      raise TypeError('regex_filter must be of type str')
    self._regex_filter = regex_filter

  @property
  def page_size(self) -> int:
    return self._page_size

  @page_size.setter
  def page_size(self, page_size: int):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token

  @page_token.setter
  def page_token(self, page_token: str):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def owner_slug(self) -> str:
    r"""
    Filter to tasks owned by this user (their username / profile slug). Only
    tasks the caller is allowed to see are returned, so pass your own slug to
    list just the tasks you created. When omitted, returns tasks the caller
    owns or collaborates on.
    """
    return self._owner_slug or ""

  @owner_slug.setter
  def owner_slug(self, owner_slug: Optional[str]):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def benchmark_slug(self) -> str:
    r"""
    Filter to the tasks belonging to this benchmark, identified by its slug
    (paired with owner_slug, which then names the benchmark's owner rather than
    the task's owner). Resolves to the benchmark version's mapped child tasks.
    When omitted, the listing is not scoped to a benchmark.
    """
    return self._benchmark_slug or ""

  @benchmark_slug.setter
  def benchmark_slug(self, benchmark_slug: Optional[str]):
    if benchmark_slug is None:
      del self.benchmark_slug
      return
    if not isinstance(benchmark_slug, str):
      raise TypeError('benchmark_slug must be of type str')
    self._benchmark_slug = benchmark_slug

  @property
  def version_number(self) -> int:
    r"""
    Optional benchmark version to target when benchmark_slug is set. When
    omitted, the benchmark's current published (or draft) version is used.
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number

  @property
  def include_definition(self) -> bool:
    r"""
    Populate `definition` and `definition_partial` on each task. Off by
    default since it costs extra reads.
    """
    return self._include_definition

  @include_definition.setter
  def include_definition(self, include_definition: bool):
    if include_definition is None:
      del self.include_definition
      return
    if not isinstance(include_definition, bool):
      raise TypeError('include_definition must be of type bool')
    self._include_definition = include_definition

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/list'
    return path.format_map(self.to_field_map(self))


class ApiListBenchmarkTasksResponse(KaggleObject):
  r"""
  Attributes:
    tasks (ApiBenchmarkTask)
    total_results (int)
    next_page_token (str)
  """

  def __init__(self):
    self._tasks = []
    self._total_results = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['ApiBenchmarkTask']]]:
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['ApiBenchmarkTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, ApiBenchmarkTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type ApiBenchmarkTask')
    self._tasks = tasks

  @property
  def total_results(self) -> int:
    return self._total_results

  @total_results.setter
  def total_results(self, total_results: int):
    if total_results is None:
      del self.total_results
      return
    if not isinstance(total_results, int):
      raise TypeError('total_results must be of type int')
    self._total_results = total_results

  @property
  def next_page_token(self) -> str:
    return self._next_page_token

  @next_page_token.setter
  def next_page_token(self, next_page_token: str):
    if next_page_token is None:
      del self.next_page_token
      return
    if not isinstance(next_page_token, str):
      raise TypeError('next_page_token must be of type str')
    self._next_page_token = next_page_token

  @property
  def totalResults(self):
    return self.total_results

  @property
  def nextPageToken(self):
    return self.next_page_token


class ApiModelVersionCandidate(KaggleObject):
  r"""
  Slug-keyed counterpart of ModelVersionCandidate.

  Attributes:
    model_version_slug (str)
      A canonical BenchmarkModelVersion.Slug (e.g. 'claude-sonnet-4-6-default').
    reasoning_effort (str)
      Narrow to the runs evaluating the model version at this reasoning effort
      (e.g. 'high'), matched as an exact string against the model version's
      configs. Unset means 'any effort'.
  """

  def __init__(self):
    self._model_version_slug = ""
    self._reasoning_effort = None
    self._freeze()

  @property
  def model_version_slug(self) -> str:
    """A canonical BenchmarkModelVersion.Slug (e.g. 'claude-sonnet-4-6-default')."""
    return self._model_version_slug

  @model_version_slug.setter
  def model_version_slug(self, model_version_slug: str):
    if model_version_slug is None:
      del self.model_version_slug
      return
    if not isinstance(model_version_slug, str):
      raise TypeError('model_version_slug must be of type str')
    self._model_version_slug = model_version_slug

  @property
  def reasoning_effort(self) -> str:
    r"""
    Narrow to the runs evaluating the model version at this reasoning effort
    (e.g. 'high'), matched as an exact string against the model version's
    configs. Unset means 'any effort'.
    """
    return self._reasoning_effort or ""

  @reasoning_effort.setter
  def reasoning_effort(self, reasoning_effort: Optional[str]):
    if reasoning_effort is None:
      del self.reasoning_effort
      return
    if not isinstance(reasoning_effort, str):
      raise TypeError('reasoning_effort must be of type str')
    self._reasoning_effort = reasoning_effort


class ApiPublishBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (ApiBenchmarkTaskSlug)
      The task to publish.
    publish_backing_notebook (bool)
      When true, also publishes the backing notebook (`source_kernel_id`) in
      the same request. When false/unset, the backing notebook is left alone.
      Unpublishing the notebook is not supported through this endpoint.
    publish_run_artifacts (bool)
      When true, also makes the task's raw run artifacts (run.json, logs, output
      files, trajectories) visible to everyone. When false/unset, only the
      task's writers can see them and everyone else sees scores only. Hiding
      them again is not supported through this endpoint.
  """

  def __init__(self):
    self._slug = None
    self._publish_backing_notebook = False
    self._publish_run_artifacts = False
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    """The task to publish."""
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def publish_backing_notebook(self) -> bool:
    r"""
    When true, also publishes the backing notebook (`source_kernel_id`) in
    the same request. When false/unset, the backing notebook is left alone.
    Unpublishing the notebook is not supported through this endpoint.
    """
    return self._publish_backing_notebook

  @publish_backing_notebook.setter
  def publish_backing_notebook(self, publish_backing_notebook: bool):
    if publish_backing_notebook is None:
      del self.publish_backing_notebook
      return
    if not isinstance(publish_backing_notebook, bool):
      raise TypeError('publish_backing_notebook must be of type bool')
    self._publish_backing_notebook = publish_backing_notebook

  @property
  def publish_run_artifacts(self) -> bool:
    r"""
    When true, also makes the task's raw run artifacts (run.json, logs, output
    files, trajectories) visible to everyone. When false/unset, only the
    task's writers can see them and everyone else sees scores only. Hiding
    them again is not supported through this endpoint.
    """
    return self._publish_run_artifacts

  @publish_run_artifacts.setter
  def publish_run_artifacts(self, publish_run_artifacts: bool):
    if publish_run_artifacts is None:
      del self.publish_run_artifacts
      return
    if not isinstance(publish_run_artifacts, bool):
      raise TypeError('publish_run_artifacts must be of type bool')
    self._publish_run_artifacts = publish_run_artifacts

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/{slug.task_slug}/publish'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiTaskCreationValidationConfig(KaggleObject):
  r"""
  The public API input shape of TaskCreationValidationConfig.

  Attributes:
    validation_stages (ApiValidationStage)
      The validation stages to run against the task version.
  """

  def __init__(self):
    self._validation_stages = []
    self._freeze()

  @property
  def validation_stages(self) -> Optional[List[Optional['ApiValidationStage']]]:
    """The validation stages to run against the task version."""
    return self._validation_stages

  @validation_stages.setter
  def validation_stages(self, validation_stages: Optional[List[Optional['ApiValidationStage']]]):
    if validation_stages is None:
      del self.validation_stages
      return
    if not isinstance(validation_stages, list):
      raise TypeError('validation_stages must be of type list')
    if not all([isinstance(t, ApiValidationStage) for t in validation_stages]):
      raise TypeError('validation_stages must contain only items of type ApiValidationStage')
    self._validation_stages = validation_stages


class ApiUpdateBenchmarkTaskRequest(KaggleObject):
  r"""
  Attributes:
    slug (ApiBenchmarkTaskSlug)
      The task to update. `owner_slug` is optional and defaults to the
      authenticated user. `version_number` is rejected here: the fields below
      always write the task's current version. Use UpdateBenchmarkTaskVersion to
      target a specific version.
    description (str)
      Markdown details shown on the task page. HTML is sanitized before storage,
      so the value read back may differ from what was sent.
    tags (str)
      Human-readable tag names (e.g. 'computer vision'). Replaces the task's
      current tags. Matching is case-insensitive and ignores surrounding
      whitespace; names are echoed back in their canonical stored form, which
      may differ in case from what was sent. Names that don't match a known tag
      are skipped and returned in `invalid_tags`.
    provenance_sources (str)
      Free-text provenance for the data/code behind the task. Values longer than
      4000 characters after sanitization are rejected with InvalidArgument.
    citations (ApiBenchmarkTaskCitation)
      Replaces the full citation list for the current version. A citation whose
      `url` can't be parsed as an http(s) URL is dropped rather than failing the
      request; the rest are still applied.
    update_mask (FieldMask)
      Which of the above to write. Only fields named here are read.
  """

  def __init__(self):
    self._slug = None
    self._description = None
    self._tags = []
    self._provenance_sources = None
    self._citations = []
    self._update_mask = None
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    r"""
    The task to update. `owner_slug` is optional and defaults to the
    authenticated user. `version_number` is rejected here: the fields below
    always write the task's current version. Use UpdateBenchmarkTaskVersion to
    target a specific version.
    """
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def description(self) -> str:
    r"""
    Markdown details shown on the task page. HTML is sanitized before storage,
    so the value read back may differ from what was sent.
    """
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def tags(self) -> Optional[List[str]]:
    r"""
    Human-readable tag names (e.g. 'computer vision'). Replaces the task's
    current tags. Matching is case-insensitive and ignores surrounding
    whitespace; names are echoed back in their canonical stored form, which
    may differ in case from what was sent. Names that don't match a known tag
    are skipped and returned in `invalid_tags`.
    """
    return self._tags

  @tags.setter
  def tags(self, tags: Optional[List[str]]):
    if tags is None:
      del self.tags
      return
    if not isinstance(tags, list):
      raise TypeError('tags must be of type list')
    if not all([isinstance(t, str) for t in tags]):
      raise TypeError('tags must contain only items of type str')
    self._tags = tags

  @property
  def provenance_sources(self) -> str:
    r"""
    Free-text provenance for the data/code behind the task. Values longer than
    4000 characters after sanitization are rejected with InvalidArgument.
    """
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: Optional[str]):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def citations(self) -> Optional[List[Optional['ApiBenchmarkTaskCitation']]]:
    r"""
    Replaces the full citation list for the current version. A citation whose
    `url` can't be parsed as an http(s) URL is dropped rather than failing the
    request; the rest are still applied.
    """
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['ApiBenchmarkTaskCitation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskCitation) for t in citations]):
      raise TypeError('citations must contain only items of type ApiBenchmarkTaskCitation')
    self._citations = citations

  @property
  def update_mask(self) -> FieldMask:
    """Which of the above to write. Only fields named here are read."""
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/{slug.owner_slug}/{slug.task_slug}/update'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiUpdateBenchmarkTaskResponse(KaggleObject):
  r"""
  Attributes:
    task (ApiBenchmarkTask)
      The task as it stands after the update.
    invalid_tags (str)
      Tag names from the request that didn't match a known tag. These were
      skipped; the remaining tags were applied.
  """

  def __init__(self):
    self._task = None
    self._invalid_tags = []
    self._freeze()

  @property
  def task(self) -> Optional['ApiBenchmarkTask']:
    """The task as it stands after the update."""
    return self._task

  @task.setter
  def task(self, task: Optional['ApiBenchmarkTask']):
    if task is None:
      del self.task
      return
    if not isinstance(task, ApiBenchmarkTask):
      raise TypeError('task must be of type ApiBenchmarkTask')
    self._task = task

  @property
  def invalid_tags(self) -> Optional[List[str]]:
    r"""
    Tag names from the request that didn't match a known tag. These were
    skipped; the remaining tags were applied.
    """
    return self._invalid_tags

  @invalid_tags.setter
  def invalid_tags(self, invalid_tags: Optional[List[str]]):
    if invalid_tags is None:
      del self.invalid_tags
      return
    if not isinstance(invalid_tags, list):
      raise TypeError('invalid_tags must be of type list')
    if not all([isinstance(t, str) for t in invalid_tags]):
      raise TypeError('invalid_tags must contain only items of type str')
    self._invalid_tags = invalid_tags

  @property
  def invalidTags(self):
    return self.invalid_tags


class ApiUpdateBenchmarkTaskVersionRequest(KaggleObject):
  r"""
  Attributes:
    slug (ApiBenchmarkTaskSlug)
      The task version to update. `owner_slug` is optional and defaults to the
      authenticated user. `version_number` names the version written, and over
      HTTP it is a required path segment.
    description (str)
      Markdown details shown on the task page. HTML is sanitized before storage,
      so the value read back may differ from what was sent.
    provenance_sources (str)
      Free-text provenance for the data/code behind the task. Values longer than
      4000 characters after sanitization are rejected with InvalidArgument.
    citations (ApiBenchmarkTaskCitation)
      Replaces the full citation list for this version. A citation whose `url`
      can't be parsed as an http(s) URL is dropped rather than failing the
      request; the rest are still applied.
    update_mask (FieldMask)
      Which of the above to write. Only fields named here are read. `tags` is
      not writable here: tags are task-scoped, so use UpdateBenchmarkTask.
    artifact_path (str)
      The file the task's preview shows, as a glob relative to a run's output
      root. Written together with artifact_type: naming either in update_mask
      writes both, and leaving both unset clears them.
    artifact_type (BenchmarkArenaArtifactType)
  """

  def __init__(self):
    self._slug = None
    self._description = None
    self._provenance_sources = None
    self._citations = []
    self._update_mask = None
    self._artifact_path = None
    self._artifact_type = None
    self._freeze()

  @property
  def slug(self) -> Optional['ApiBenchmarkTaskSlug']:
    r"""
    The task version to update. `owner_slug` is optional and defaults to the
    authenticated user. `version_number` names the version written, and over
    HTTP it is a required path segment.
    """
    return self._slug

  @slug.setter
  def slug(self, slug: Optional['ApiBenchmarkTaskSlug']):
    if slug is None:
      del self.slug
      return
    if not isinstance(slug, ApiBenchmarkTaskSlug):
      raise TypeError('slug must be of type ApiBenchmarkTaskSlug')
    self._slug = slug

  @property
  def description(self) -> str:
    r"""
    Markdown details shown on the task page. HTML is sanitized before storage,
    so the value read back may differ from what was sent.
    """
    return self._description or ""

  @description.setter
  def description(self, description: Optional[str]):
    if description is None:
      del self.description
      return
    if not isinstance(description, str):
      raise TypeError('description must be of type str')
    self._description = description

  @property
  def provenance_sources(self) -> str:
    r"""
    Free-text provenance for the data/code behind the task. Values longer than
    4000 characters after sanitization are rejected with InvalidArgument.
    """
    return self._provenance_sources or ""

  @provenance_sources.setter
  def provenance_sources(self, provenance_sources: Optional[str]):
    if provenance_sources is None:
      del self.provenance_sources
      return
    if not isinstance(provenance_sources, str):
      raise TypeError('provenance_sources must be of type str')
    self._provenance_sources = provenance_sources

  @property
  def citations(self) -> Optional[List[Optional['ApiBenchmarkTaskCitation']]]:
    r"""
    Replaces the full citation list for this version. A citation whose `url`
    can't be parsed as an http(s) URL is dropped rather than failing the
    request; the rest are still applied.
    """
    return self._citations

  @citations.setter
  def citations(self, citations: Optional[List[Optional['ApiBenchmarkTaskCitation']]]):
    if citations is None:
      del self.citations
      return
    if not isinstance(citations, list):
      raise TypeError('citations must be of type list')
    if not all([isinstance(t, ApiBenchmarkTaskCitation) for t in citations]):
      raise TypeError('citations must contain only items of type ApiBenchmarkTaskCitation')
    self._citations = citations

  @property
  def artifact_path(self) -> str:
    r"""
    The file the task's preview shows, as a glob relative to a run's output
    root. Written together with artifact_type: naming either in update_mask
    writes both, and leaving both unset clears them.
    """
    return self._artifact_path or ""

  @artifact_path.setter
  def artifact_path(self, artifact_path: Optional[str]):
    if artifact_path is None:
      del self.artifact_path
      return
    if not isinstance(artifact_path, str):
      raise TypeError('artifact_path must be of type str')
    self._artifact_path = artifact_path

  @property
  def artifact_type(self) -> 'BenchmarkArenaArtifactType':
    return self._artifact_type or BenchmarkArenaArtifactType.BENCHMARK_ARENA_ARTIFACT_TYPE_UNSPECIFIED

  @artifact_type.setter
  def artifact_type(self, artifact_type: Optional['BenchmarkArenaArtifactType']):
    if artifact_type is None:
      del self.artifact_type
      return
    if not isinstance(artifact_type, BenchmarkArenaArtifactType):
      raise TypeError('artifact_type must be of type BenchmarkArenaArtifactType')
    self._artifact_type = artifact_type

  @property
  def update_mask(self) -> FieldMask:
    r"""
    Which of the above to write. Only fields named here are read. `tags` is
    not writable here: tags are task-scoped, so use UpdateBenchmarkTask.
    """
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask

  def endpoint(self):
    path = '/api/v1/benchmarks/tasks/{slug.owner_slug}/{slug.task_slug}/versions/{slug.version_number}/update'
    return path.format_map(self.to_field_map(self))


  @staticmethod
  def method():
    return 'POST'

  @staticmethod
  def body_fields():
    return '*'


class ApiValidationStage(KaggleObject):
  r"""
  The public API input shape of ValidationStage, which identifies the default
  candidate by slug instead of id.

  Attributes:
    type (BenchmarkTaskValidationStage)
      Required. Not UNSPECIFIED.
    default_model_version_slug (str)
      Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default').
      On Harbor tasks, requires override_harness_version: without one the task
      evaluates agents, so pick the model via default_agent_slug instead.
    default_agent_slug (str)
      Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high').
    default_model_version_config_slug (str)
      Canonical BenchmarkModelVersionConfig.slug (e.g.
      'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
      the reasoning effort. Harbor tasks only; requires
      override_harness_version.
  """

  def __init__(self):
    self._type = BenchmarkTaskValidationStage.BENCHMARK_TASK_VALIDATION_STAGE_UNSPECIFIED
    self._default_model_version_slug = None
    self._default_agent_slug = None
    self._default_model_version_config_slug = None
    self._freeze()

  @property
  def type(self) -> 'BenchmarkTaskValidationStage':
    """Required. Not UNSPECIFIED."""
    return self._type

  @type.setter
  def type(self, type: 'BenchmarkTaskValidationStage'):
    if type is None:
      del self.type
      return
    if not isinstance(type, BenchmarkTaskValidationStage):
      raise TypeError('type must be of type BenchmarkTaskValidationStage')
    self._type = type

  @property
  def default_model_version_slug(self) -> str:
    r"""
    Canonical BenchmarkModelVersion.slug (e.g. 'claude-sonnet-4-6-default').
    On Harbor tasks, requires override_harness_version: without one the task
    evaluates agents, so pick the model via default_agent_slug instead.
    """
    return self._default_model_version_slug or ""

  @default_model_version_slug.setter
  def default_model_version_slug(self, default_model_version_slug: str):
    if default_model_version_slug is None:
      del self.default_model_version_slug
      return
    if not isinstance(default_model_version_slug, str):
      raise TypeError('default_model_version_slug must be of type str')
    del self.default_agent_slug
    del self.default_model_version_config_slug
    self._default_model_version_slug = default_model_version_slug

  @property
  def default_agent_slug(self) -> str:
    """Canonical Agent.slug (e.g. 'claude-code-2.1.216-opus-4.8-high')."""
    return self._default_agent_slug or ""

  @default_agent_slug.setter
  def default_agent_slug(self, default_agent_slug: str):
    if default_agent_slug is None:
      del self.default_agent_slug
      return
    if not isinstance(default_agent_slug, str):
      raise TypeError('default_agent_slug must be of type str')
    del self.default_model_version_slug
    del self.default_model_version_config_slug
    self._default_agent_slug = default_agent_slug

  @property
  def default_model_version_config_slug(self) -> str:
    r"""
    Canonical BenchmarkModelVersionConfig.slug (e.g.
    'claude-sonnet-4-6-high'). Like default_model_version_slug, but also pins
    the reasoning effort. Harbor tasks only; requires
    override_harness_version.
    """
    return self._default_model_version_config_slug or ""

  @default_model_version_config_slug.setter
  def default_model_version_config_slug(self, default_model_version_config_slug: str):
    if default_model_version_config_slug is None:
      del self.default_model_version_config_slug
      return
    if not isinstance(default_model_version_config_slug, str):
      raise TypeError('default_model_version_config_slug must be of type str')
    del self.default_model_version_slug
    del self.default_agent_slug
    self._default_model_version_config_slug = default_model_version_config_slug


ApiBatchScheduleBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("taskSlugs", "task_slugs", "_task_slugs", ApiBenchmarkTaskSlug, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("modelVersionSlugs", "model_version_slugs", "_model_version_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("agentSlugs", "agent_slugs", "_agent_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("reasoningEffort", "reasoning_effort", "_reasoning_effort", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("enqueue", "enqueue", "_enqueue", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skipPolicy", "skip_policy", "_skip_policy", BenchmarkEnqueueSkipPolicy, BenchmarkEnqueueSkipPolicy.BENCHMARK_ENQUEUE_SKIP_POLICY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("staleAfter", "stale_after", "_stale_after", timedelta, None, TimeDeltaSerializer(), optional=True),
  FieldMetadata("benchmark", "benchmark", "_benchmark", ApiBenchmarkSlug, None, KaggleObjectSerializer()),
]

ApiBatchScheduleBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("results", "results", "_results", BatchScheduleBenchmarkModelVersionResult, [], ListSerializer(KaggleObjectSerializer())),
]

ApiBenchmarkSlug._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiBenchmarkTask._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("error", "error", "_error", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("creationState", "creation_state", "_creation_state", BenchmarkTaskVersionCreationState, BenchmarkTaskVersionCreationState.BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("createTime", "create_time", "_create_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("creationErrorMessage", "creation_error_message", "_creation_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPublic", "is_public", "_is_public", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("sourceKernelId", "source_kernel_id", "_source_kernel_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isBackingNotebookPublished", "is_backing_notebook_published", "_is_backing_notebook_published", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("options", "options", "_options", BenchmarkTaskOptions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("source", "source", "_source", BenchmarkTaskVersionSource, BenchmarkTaskVersionSource.BENCHMARK_TASK_VERSION_SOURCE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", ApiBenchmarkTaskCitation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("candidateType", "candidate_type", "_candidate_type", BenchmarkCandidateType, BenchmarkCandidateType.BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("definition", "definition", "_definition", BenchmarkTaskDefinition, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("definitionPartial", "definition_partial", "_definition_partial", bool, False, PredefinedSerializer()),
  FieldMetadata("artifactPath", "artifact_path", "_artifact_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("artifactType", "artifact_type", "_artifact_type", BenchmarkArenaArtifactType, None, EnumSerializer(), optional=True),
  FieldMetadata("areRunArtifactsPublic", "are_run_artifacts_public", "_are_run_artifacts_public", bool, None, PredefinedSerializer(), optional=True),
]

ApiBenchmarkTaskCitation._fields = [
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
]

ApiBenchmarkTaskRun._fields = [
  FieldMetadata("taskSlug", "task_slug", "_task_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("state", "state", "_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("agentSlug", "agent_slug", "_agent_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelVersionConfigSlug", "model_version_config_slug", "_model_version_config_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("result", "result", "_result", ApiBenchmarkTaskRunResult, None, KaggleObjectSerializer(), optional=True),
]

ApiBenchmarkTaskRunIds._fields = [
  FieldMetadata("ids", "ids", "_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ApiBenchmarkTaskRunResult._fields = [
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
]

ApiBenchmarkTaskSlug._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("taskSlug", "task_slug", "_task_slug", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

ApiBenchmarkTaskSlugs._fields = [
  FieldMetadata("slugs", "slugs", "_slugs", ApiBenchmarkTaskSlug, [], ListSerializer(KaggleObjectSerializer())),
]

ApiCancelBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("taskSlugs", "task_slugs", "_task_slugs", ApiBenchmarkTaskSlugs, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("modelVersion", "model_version", "_model_version", ApiModelVersionCandidate, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("agentSlug", "agent_slug", "_agent_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includeActive", "include_active", "_include_active", bool, False, PredefinedSerializer()),
  FieldMetadata("runIds", "run_ids", "_run_ids", ApiBenchmarkTaskRunIds, None, KaggleObjectSerializer(), optional=True),
]

ApiCancelBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("queuedCancelledCount", "queued_cancelled_count", "_queued_cancelled_count", int, 0, PredefinedSerializer()),
  FieldMetadata("activeTerminatedCount", "active_terminated_count", "_active_terminated_count", int, 0, PredefinedSerializer()),
]

ApiCreateBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("text", "text", "_text", str, "", PredefinedSerializer()),
  FieldMetadata("options", "options", "_options", BenchmarkTaskOptions, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("definition", "definition", "_definition", BenchmarkTaskDefinition, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("validationConfig", "validation_config", "_validation_config", ApiTaskCreationValidationConfig, None, KaggleObjectSerializer(), optional=True),
]

ApiDownloadBenchmarkTaskRunOutputRequest._fields = [
  FieldMetadata("runId", "run_id", "_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("includeSource", "include_source", "_include_source", bool, False, PredefinedSerializer()),
]

ApiGetBenchmarkSchedulerStatusRequest._fields = []

ApiGetBenchmarkTaskQuotaRequest._fields = []

ApiGetBenchmarkTaskQuotaResponse._fields = [
  FieldMetadata("dailyQuotaUsed", "daily_quota_used", "_daily_quota_used", float, 0.0, PredefinedSerializer()),
  FieldMetadata("totalDailyQuotaAllowed", "total_daily_quota_allowed", "_total_daily_quota_allowed", float, 0.0, PredefinedSerializer()),
]

ApiGetBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("includeDefinition", "include_definition", "_include_definition", bool, False, PredefinedSerializer()),
]

ApiGetBenchmarkTaskRunLogsRequest._fields = [
  FieldMetadata("runId", "run_id", "_run_id", int, 0, PredefinedSerializer()),
]

ApiListBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("taskSlug", "task_slug", "_task_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("modelVersionSlugs", "model_version_slugs", "_model_version_slugs", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
]

ApiListBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("runs", "runs", "_runs", ApiBenchmarkTaskRun, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiListBenchmarkTasksRequest._fields = [
  FieldMetadata("statusFilter", "status_filter", "_status_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("regexFilter", "regex_filter", "_regex_filter", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkSlug", "benchmark_slug", "_benchmark_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includeDefinition", "include_definition", "_include_definition", bool, False, PredefinedSerializer()),
]

ApiListBenchmarkTasksResponse._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", ApiBenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ApiModelVersionCandidate._fields = [
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("reasoningEffort", "reasoning_effort", "_reasoning_effort", str, None, PredefinedSerializer(), optional=True),
]

ApiPublishBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("publishBackingNotebook", "publish_backing_notebook", "_publish_backing_notebook", bool, False, PredefinedSerializer()),
  FieldMetadata("publishRunArtifacts", "publish_run_artifacts", "_publish_run_artifacts", bool, False, PredefinedSerializer()),
]

ApiTaskCreationValidationConfig._fields = [
  FieldMetadata("validationStages", "validation_stages", "_validation_stages", ApiValidationStage, [], ListSerializer(KaggleObjectSerializer())),
]

ApiUpdateBenchmarkTaskRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tags", "tags", "_tags", str, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", ApiBenchmarkTaskCitation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

ApiUpdateBenchmarkTaskResponse._fields = [
  FieldMetadata("task", "task", "_task", ApiBenchmarkTask, None, KaggleObjectSerializer()),
  FieldMetadata("invalidTags", "invalid_tags", "_invalid_tags", str, [], ListSerializer(PredefinedSerializer())),
]

ApiUpdateBenchmarkTaskVersionRequest._fields = [
  FieldMetadata("slug", "slug", "_slug", ApiBenchmarkTaskSlug, None, KaggleObjectSerializer()),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("provenanceSources", "provenance_sources", "_provenance_sources", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("citations", "citations", "_citations", ApiBenchmarkTaskCitation, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("artifactPath", "artifact_path", "_artifact_path", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("artifactType", "artifact_type", "_artifact_type", BenchmarkArenaArtifactType, None, EnumSerializer(), optional=True),
]

ApiValidationStage._fields = [
  FieldMetadata("type", "type", "_type", BenchmarkTaskValidationStage, BenchmarkTaskValidationStage.BENCHMARK_TASK_VALIDATION_STAGE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("defaultModelVersionSlug", "default_model_version_slug", "_default_model_version_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultAgentSlug", "default_agent_slug", "_default_agent_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("defaultModelVersionConfigSlug", "default_model_version_config_slug", "_default_model_version_config_slug", str, None, PredefinedSerializer(), optional=True),
]

