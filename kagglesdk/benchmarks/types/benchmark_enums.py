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
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_TASK_VERSION_CREATION_STATE_UNSPECIFIED = 0
  BENCHMARK_TASK_VERSION_CREATION_STATE_QUEUED = 1
  BENCHMARK_TASK_VERSION_CREATION_STATE_RUNNING = 2
  BENCHMARK_TASK_VERSION_CREATION_STATE_COMPLETED = 3
  BENCHMARK_TASK_VERSION_CREATION_STATE_ERRORED = 4

class BenchmarkTaskRunState(enum.Enum):
  BENCHMARK_TASK_RUN_STATE_UNSPECIFIED = 0
  BENCHMARK_TASK_RUN_STATE_QUEUED = 1
  BENCHMARK_TASK_RUN_STATE_RUNNING = 2
  BENCHMARK_TASK_RUN_STATE_COMPLETED = 3
  BENCHMARK_TASK_RUN_STATE_ERRORED = 4

