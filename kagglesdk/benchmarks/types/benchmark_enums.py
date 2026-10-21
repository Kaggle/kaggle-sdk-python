import enum

class BenchmarkArenaArtifactType(enum.Enum):
  """How an arena renders a run's artifact."""
  BENCHMARK_ARENA_ARTIFACT_TYPE_UNSPECIFIED = 0
  BENCHMARK_ARENA_ARTIFACT_TYPE_VIDEO = 1
  BENCHMARK_ARENA_ARTIFACT_TYPE_IMAGE = 2
  BENCHMARK_ARENA_ARTIFACT_TYPE_HTML = 3
  """Rendered in a sandboxed iframe."""
  BENCHMARK_ARENA_ARTIFACT_TYPE_TEXT = 4

class BenchmarkCandidateType(enum.Enum):
  r"""
  Saved to the DB. Do not modify existing values.
  The kind of candidate a BenchmarkTaskVersion evaluates.
  """
  BENCHMARK_CANDIDATE_TYPE_UNSPECIFIED = 0
  BENCHMARK_CANDIDATE_TYPE_MODEL_VERSIONS = 1
  BENCHMARK_CANDIDATE_TYPE_AGENTS = 2
  BENCHMARK_CANDIDATE_TYPE_MODEL_VERSION_CONFIGS = 3
  r"""
  TODO(bml): Support this candidate type as part of migrating off of
  ModelVersions. In the meantime, DO NOT PERSIST THIS VALUE IN THE DB
  """

class BenchmarkEnqueueSkipPolicy(enum.Enum):
  r"""
  Which (task version, candidate) pairs an enqueue queues, widening in the
  order below. All but ALL skip pairs whose run is still in flight.
  """
  BENCHMARK_ENQUEUE_SKIP_POLICY_UNSPECIFIED = 0
  BENCHMARK_ENQUEUE_SKIP_POLICY_ALL = 1
  """Queue every pair, existing runs included."""
  BENCHMARK_ENQUEUE_SKIP_POLICY_MISSING_ONLY = 2
  """Queue only pairs with no run at all."""
  BENCHMARK_ENQUEUE_SKIP_POLICY_MISSING_OR_ERRORED = 3
  """... plus pairs whose latest run errored."""
  BENCHMARK_ENQUEUE_SKIP_POLICY_STALER_THAN = 4
  r"""
  ... plus pairs whose run completed before stale_after. A widening rather
  than a stale-only filter: refreshing a sweep fills its gaps too.
  """

class BenchmarkGalleryCardSize(enum.Enum):
  """How large the gallery draws each card."""
  BENCHMARK_GALLERY_CARD_SIZE_UNSPECIFIED = 0
  """Same as MEDIUM."""
  BENCHMARK_GALLERY_CARD_SIZE_EXTRA_SMALL = 1
  BENCHMARK_GALLERY_CARD_SIZE_SMALL = 2
  BENCHMARK_GALLERY_CARD_SIZE_MEDIUM = 3
  BENCHMARK_GALLERY_CARD_SIZE_LARGE = 4
  """One card per row, for outputs such as web pages that need room."""

class BenchmarkModelImportanceLevel(enum.Enum):
  r"""
  Determines whether the model will be run on
  Kaggle-maintained benchmarks
  See http://goto.google.com/kaggle-benchmarks-model-coverage
  """
  BENCHMARK_MODEL_IMPORTANCE_LEVEL_UNSPECIFIED = 0
  CORE = 1
  r"""
  Model should be ran on
  all Kaggle-maintained benchmarks
  """

class BenchmarkTaskVersionCreationState(enum.Enum):
  r"""
  Saved to the DB. Do not modify existing values.
  LINT.IfChange(BenchmarkTaskVersionCreationState)
  """
  BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED = 0
  BENCHMARK_TASK_VERSION_CREATION_STATE_VALIDATING = 8
  """Validation stage runs are in progress."""
  BENCHMARK_TASK_VERSION_CREATION_STATE_VALIDATION_FAILED = 6
  r"""
  The created task failed validation, e.g. a validation stage run's output
  didn't match its expected output.
  """
  BENCHMARK_TASK_VERSION_CREATION_STATE_ERRORED = 4
  """The creation session, or any validation stage run, errored."""
  BENCHMARK_TASK_VERSION_CREATION_STATE_COMPLETED = 3
  BENCHMARK_TASK_VERSION_CREATION_STATE_QUEUED = 1
  r"""
  Deprecated: new task versions shouldn't use these states. Retained because
  existing rows still hold them.
  """
  BENCHMARK_TASK_VERSION_CREATION_STATE_RUNNING = 2
  BENCHMARK_TASK_VERSION_CREATION_STATE_KERNEL_WITHOUT_RUN = 5
  BENCHMARK_TASK_VERSION_CREATION_STATE_NO_MODEL_SPECIFIED = 7

class BenchmarkTaskVersionSource(enum.Enum):
  r"""
  Where a BenchmarkTaskVersion was created from. Used for analytics and future
  per-source policy hooks; sandbox tasks are listed alongside the existing
  manual UNSPECIFIED flow without gating.
  """
  BENCHMARK_TASK_VERSION_SOURCE_UNSPECIFIED = 0
  EVAL_SANDBOX = 1
  """Created by the LIH 'Benchmark Sandbox: Discover What Works' flow."""
  WEB = 2
  r"""
  Created via a kaggle.com web RPC (e.g. CreateBenchmarkTaskFromPrompt,
  CreateBenchmarkTaskFromDockerImage, or saving a benchmark task from a
  kernel session).
  """
  CLI = 3
  """Created via the Kaggle CLI / public BenchmarkTasksApi handler."""

class Modality(enum.Enum):
  """Modality types supported by a benchmark model version."""
  MODALITY_UNSPECIFIED = 0
  MODALITY_TEXT = 1
  MODALITY_IMAGE = 2
  MODALITY_VIDEO = 3
  MODALITY_AUDIO = 4

class BenchmarkCandidateClass(enum.Enum):
  r"""
  The kind of contestant a benchmark candidate is, derived from which of a
  BenchmarkRun's candidate ID columns are populated, or from which mapping
  table selected a candidate onto a leaderboard.

  Distinct from BenchmarkCandidateType, which is a declared column on the task
  version and is stamped inconsistently across write paths: a bulk-import path
  stamps MODEL_VERSIONS on runs that carry an AgentId. This enum is always
  derived, never stored, so it cannot drift the same way.

  What kind of contestant a leaderboard row or a run belongs to. The classes
  are disjoint predicates over the same columns and together cover every run,
  so every candidate falls into exactly one. Rows of different classes rank
  together on one board, which is why 'Opus' and 'Claude Code on Opus' can
  appear as separate results rather than one absorbing the other's runs.
  """
  BENCHMARK_CANDIDATE_CLASS_UNSPECIFIED = 0
  BENCHMARK_CANDIDATE_CLASS_MODEL_VERSION = 1
  r"""
  A bare model version: neither a config nor an agent. Also covers legacy
  rows written before the configs table existed.
  """
  BENCHMARK_CANDIDATE_CLASS_MODEL_VERSION_CONFIG = 2
  """A model version pinned to a config (e.g. a reasoning effort), no harness."""
  BENCHMARK_CANDIDATE_CLASS_AGENT = 3
  r"""
  A harness paired with a config. Identified by the agent alone, since an
  agent pins its own config and model version.
  """

class BenchmarkLeaderboardDisplayType(enum.Enum):
  r"""
  Saved to the DB. Do not modify existing values.
  This enum specifies how task version numeric results should be interpreted
  and displayed on leaderboards.
  LINT.IfChange
  """
  BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED = 0
  PERCENTAGES = 1
  r"""
  Displays 0.XX values as a percentage, rounded to 1 sigfig, ex:
  0.12345 -> 12.3%, 45600.0 -> 4560000.0%, 0.75 -> 75.0%
  """
  COUNTS = 2
  r"""
  Displays value as an absolute count, rounded to nearest integer, ex:
  123, 456, 790
  """
  DOLLARS = 3
  r"""
  Displays value as a dollar and cents amount, rounded to 2 sigfigs, ex:
  $123.45, $456.00, $790.57
  """
  CENTS = 4
  r"""
  Displays value as a cents amount, rounded to 2 sigfigs, ex:
  ¢123.45, ¢456.00, ¢790.57
  """
  RAW_PERCENTAGES = 5
  r"""
  Displays XX values as a percentage, rounded to 1 sigfig, ex:
  75 -> 75.0%, 123 -> 123.0%, 4.56 -> 4.6%
  """
  FLOAT_COUNTS = 6
  r"""
  Displays value as an absolute count, rounded to 1 sigfig, ex:
  123.4, 456.0, 789.6
  """
  RAW_VALUES = 7
  r"""
  Displays the value with 2 decimal places, with no scaling or unit, ex:
  123.44, 456.00, 789.57
  """
  WHOLE_DOLLARS = 8
  r"""
  Displays value as a dollar amount rounded to the nearest whole dollar with
  thousands separators, ex:
  $2,601,845, $456, $790
  """

class BenchmarkTaskRunState(enum.Enum):
  BENCHMARK_TASK_RUN_STATE_UNSPECIFIED = 0
  BENCHMARK_TASK_RUN_STATE_QUEUED = 1
  BENCHMARK_TASK_RUN_STATE_RUNNING = 2
  BENCHMARK_TASK_RUN_STATE_COMPLETED = 3
  BENCHMARK_TASK_RUN_STATE_ERRORED = 4
  BENCHMARK_TASK_RUN_STATE_SCORE_PENDING = 5
  r"""
  Indicates that scoring for the run is still pending.

  For the initial implementation of CompsBench infra (go/compsbench-infra).
  The session has completed running, but we're still awaiting a
  score from the competitions scoring system.
  """

class BenchmarkVersionAgentMappingType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_VERSION_AGENT_MAPPING_TYPE_UNSPECIFIED = 0
  BENCHMARK_VERSION_AGENT_MAPPING_TYPE_PRINCIPAL = 1

