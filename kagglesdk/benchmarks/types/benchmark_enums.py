import enum

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
  BENCHMARK_TASK_VERSION_CREATION_STATE_QUEUED = 1
  BENCHMARK_TASK_VERSION_CREATION_STATE_RUNNING = 2
  BENCHMARK_TASK_VERSION_CREATION_STATE_COMPLETED = 3
  BENCHMARK_TASK_VERSION_CREATION_STATE_ERRORED = 4
  BENCHMARK_TASK_VERSION_CREATION_STATE_KERNEL_WITHOUT_RUN = 5
  BENCHMARK_TASK_VERSION_CREATION_STATE_VALIDATION_FAILED = 6
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
  Created via the kaggle.com web client (e.g. CreateBenchmarkTaskFromPrompt
  or saving a benchmark task from a kernel session).
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

