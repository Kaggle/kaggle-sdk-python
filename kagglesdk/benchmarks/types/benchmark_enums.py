import enum

class BenchmarkLeaderboardDisplayType(enum.Enum):
  r"""
  Saved to the DB. Do not modify existing values.
  This enum specifies how task version numeric results should be interpreted
  and displayed on leaderboards
  """
  BENCHMARK_LEADERBOARD_DISPLAY_TYPE_UNSPECIFIED = 0
  PERCENTAGES = 1
  r"""
  Displays value as a percentage, rounded to 1 sigfig, ex:
  12345.0 -> 1234500.0%, 45600.0 -> 4560000.0%, 0.75 -> 75.0%
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
  FLOAT_PERCENTAGES = 5
  r"""
  Displays float values as a percentage, rounded to 1 sigfig, ex:
  0.0075 -> 75.0%, 0.123 -> 1230.0 %, 4.56 -> 45600.0%
  """
  FLOAT_COUNTS = 6
  r"""
  Displays value as an absolute count, rounded to 1 sigfig, ex:
  123.4, 456.0, 789.6
  """

class BenchmarkMediaType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_MEDIA_TYPE_UNSPECIFIED = 0
  PAPER = 1
  BLOG_POST = 2
  TECHNICAL_REPORT = 3
  KAGGLE_DATASET = 4
  KAGGLE_COMPETITION = 5
  KAGGLE_NOTEBOOK = 6
  WEBSITE = 7
  YOUTUBE = 8

class BenchmarkTaskType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_TASK_TYPE_UNSPECIFIED = 0
  BENCHMARK_TASK_TYPE_PERSONAL = 1
  BENCHMARK_TASK_TYPE_BENCHMARK = 2

class BenchmarkTaskVersionAggregationType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_TASK_VERSION_AGGREGATION_TYPE_UNSPECIFIED = 0
  r"""
  Does not aggregate child task version run results.
  Values are determined by own associated run results
  """
  AVERAGE = 1
  r"""
  Values are determined by averaging child task version run results with
  numeric values. Task versions with boolean/NULL run results are ignored.
  """
  NOOP = 2
  """Does not have values, directly displays child task version run results."""
  WEIGHTED_AVERAGE = 3
  r"""
  Values are determined by applying a weight to each child task version
  numeric run result (specified per-mapping, default value 1), summing the
  total of weighted values, and dividing by the total of weights.

  I.e.: (W[0] * X[0] + W[1] * X[1] + W[2] * X[2] + . . . + W[n-1] * X[n-1]) /
  (W[0] + W[1] + W[2] + . . . + W[n-1])

  Task versions with boolean/NULL run results are ignored.
  """
  PERCENTAGE_PASSED = 4
  r"""
  Values are determined by calculating the percentage of child task version
  with boolean run results that are TRUE. Task versions with numeric/NULL run
  results are ignored.
  """

class BenchmarkTaskVersionMappingType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_TASK_VERSION_MAPPING_TYPE_UNSPECIFIED = 0
  BENCHMARK_TASK_VERSION_MAPPING_TYPE_PRINCIPAL = 1
  r"""
  Principal mappings are treated as the most important. They are:
  1) Included in the aggregate calculation
  2) Can be sorted on
  3) Have prominent display UI
  """
  BENCHMARK_TASK_VERSION_MAPPING_TYPE_INFORMATIONAL = 2
  r"""
  Informational mappings are less important and provide context. They are:
  1) Not included in the aggregate calculation
  2) Can't be sorted on (except as tie-breakers after sorting on a principal)
  3) Have less prominent display UI
  """

class BenchmarkType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_TYPE_UNSPECIFIED = 0
  INDIVIDUAL = 1
  """A single benchmark"""
  SUITE = 2
  """A collection of sub-benchmarks"""
  GAME = 3
  r"""
  An individual benchmark that involves models facing off head-to-head.
  Admin-only.
  """
  PERSONAL = 4
  """a collection of tasks for Personal Benchmarks"""

class BenchmarkVersionMappingType(enum.Enum):
  r"""
  TODO(bml): Remove this once the new mapping table migration is done.
  Saved to the DB. Do not modify existing values.
  """
  BENCHMARK_VERSION_MAPPING_TYPE_UNSPECIFIED = 0
  PRINCIPAL = 1
  r"""
  Principal mappings are treated as the most important. They are:
  1) Included in the aggregate calculation
  2) Can be sorted on
  3) Have prominent display UI
  """
  INFORMATIONAL = 2
  r"""
  Informational mappings are less important and provide context. They are:
  1) Not included in the aggregate calculation
  2) Can't be sorted on (except as tie-breakers after sorting on a principal)
  3) Have less prominent display UI
  """

class BenchmarkVersionModelMappingType(enum.Enum):
  """Saved to the DB. Do not modify existing values."""
  BENCHMARK_VERSION_MODEL_MAPPING_TYPE_UNSPECIFIED = 0
  BENCHMARK_VERSION_MODEL_MAPPING_TYPE_PRINCIPAL = 1
  """Principal-mapped models are actual 'contestants' on the leaderboard."""
  BENCHMARK_VERSION_MODEL_MAPPING_TYPE_INFORMATIONAL = 2
  """Information-mapped models provide context, ex: as baseline models."""

class ListBenchmarksOrderBy(enum.Enum):
  LIST_BENCHMARKS_ORDER_BY_UNSPECIFIED = 0
  LIST_BENCHMARKS_ORDER_BY_RECENTLY_CREATED = 1
  LIST_BENCHMARKS_ORDER_BY_RECENTLY_UPDATED = 2
  LIST_BENCHMARKS_ORDER_BY_TOP_LEVEL_BENCHMARKS = 3
  LIST_BENCHMARKS_ORDER_BY_MOST_VOTES = 4
  LIST_BENCHMARKS_ORDER_BY_MOST_VIEWS = 5
  LIST_BENCHMARKS_ORDER_BY_MOST_DOWNLOADS = 6

class ListBenchmarkTasksOrderBy(enum.Enum):
  LIST_BENCHMARK_TASKS_ORDER_BY_UNSPECIFIED = 0
  LIST_BENCHMARK_TASKS_ORDER_BY_RECENTLY_CREATED = 1

class SortOrder(enum.Enum):
  r"""
  Saved to the DB. Do not modify existing values.
  Specifies the default sort order for leaderboard results.
  """
  SORT_ORDER_UNSPECIFIED = 0
  ASCENDING = 1
  """Sort results in ascending order (lowest first)."""
  DESCENDING = 2
  """Sort results in descending order (highest first)."""

class ValidateSaveBenchmarkTaskValidationResult(enum.Enum):
  VALIDATION_RESULT_UNDEFINED = 0
  VALIDATION_RESULT_SUCCESS = 1
  """Used if there is no error"""
  VALIDATION_RESULT_CONFLICTING_SLUG = 2
  r"""
  used to tell the user there is a conflicting task name slug on a different
  notebook
  """

class BenchmarkMaintenanceLevel(enum.Enum):
  r"""
  Whether Kaggle will maintain this benchmark by updating
  it with what we deem as core models.
  See http://goto.google.com/kaggle-benchmarks-model-coverage
  """
  BENCHMARK_MAINTENANCE_LEVEL_UNSPECIFIED = 0
  KAGGLE_MAINTAINED = 1
  """Kaggle will run core models on this benchmark"""

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

class BenchmarkTaskDefinitionType(enum.Enum):
  BENCHMARK_TASK_DEFINITION_TYPE_UNSPECIFIED = 0
  """Research Benchmarks will use this until they transition"""
  NOTEBOOK = 1
  PROMPTFOO = 2

class BenchmarkTaskRunState(enum.Enum):
  BENCHMARK_TASK_RUN_STATE_UNSPECIFIED = 0
  BENCHMARK_TASK_RUN_STATE_QUEUED = 1
  BENCHMARK_TASK_RUN_STATE_RUNNING = 2
  BENCHMARK_TASK_RUN_STATE_COMPLETED = 3
  BENCHMARK_TASK_RUN_STATE_ERRORED = 4

class BenchmarkTaskRunAssertionStatus(enum.Enum):
  BENCHMARK_TASK_RUN_ASSERTION_STATUS_UNSPECIFIED = 0
  BENCHMARK_TASK_RUN_ASSERTION_STATUS_PASSED = 1
  BENCHMARK_TASK_RUN_ASSERTION_STATUS_FAILED = 2
  BENCHMARK_TASK_RUN_ASSERTION_STATUS_ERRORED = 3

class BenchmarkTaskRunResultType(enum.Enum):
  BENCHMARK_TASK_RUN_RESULT_TYPE_UNSPECIFIED = 0
  r"""
  In practice, this could probably default to AGGREGATED since there's no
  need to specify a type if there's only public results.
  """
  AGGREGATED = 1
  r"""
  For public/private split Tasks, this would be an aggregate of the 2 splits
  Otherwise, this is analogous to PUBLIC
  """
  PUBLIC = 2
  r"""
  The results just from the public split
  For non-split Tasks, this is the same as AGGREGATED
  """
  PRIVATE = 3
  """The results just from the private split"""

