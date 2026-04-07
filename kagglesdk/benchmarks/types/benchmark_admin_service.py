from datetime import datetime
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkTaskRunState
from kagglesdk.benchmarks.types.benchmark_task_run_service import BatchScheduleBenchmarkModelVersionResult
from kagglesdk.benchmarks.types.benchmark_types import BenchmarkTask, BenchmarkVersion
from kagglesdk.kaggle_object import *
from typing import List, Optional

class AdminScheduleBenchmarkTaskRunsRequest(KaggleObject):
  r"""
  Attributes:
    model_version_id (int)
  """

  def __init__(self):
    self._model_version_id = 0
    self._freeze()

  @property
  def model_version_id(self) -> int:
    return self._model_version_id

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    self._model_version_id = model_version_id


class AdminScheduleBenchmarkTaskRunsResponse(KaggleObject):
  r"""
  Attributes:
    model_version_id (int)
    results (AdminScheduleBenchmarkTaskRunsResult)
  """

  def __init__(self):
    self._model_version_id = 0
    self._results = []
    self._freeze()

  @property
  def model_version_id(self) -> int:
    return self._model_version_id

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    self._model_version_id = model_version_id

  @property
  def results(self) -> Optional[List[Optional['AdminScheduleBenchmarkTaskRunsResult']]]:
    return self._results

  @results.setter
  def results(self, results: Optional[List[Optional['AdminScheduleBenchmarkTaskRunsResult']]]):
    if results is None:
      del self.results
      return
    if not isinstance(results, list):
      raise TypeError('results must be of type list')
    if not all([isinstance(t, AdminScheduleBenchmarkTaskRunsResult) for t in results]):
      raise TypeError('results must contain only items of type AdminScheduleBenchmarkTaskRunsResult')
    self._results = results


class AdminScheduleBenchmarkTaskRunsResult(KaggleObject):
  r"""
  Per-benchmark-version results from scheduling task runs.
  See BatchScheduleBenchmarkModelVersionResult for individual task results.

  Attributes:
    benchmark_version_id (int)
    benchmark_version_results (BatchScheduleBenchmarkModelVersionResult)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._benchmark_version_results = []
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def benchmark_version_results(self) -> Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]:
    return self._benchmark_version_results

  @benchmark_version_results.setter
  def benchmark_version_results(self, benchmark_version_results: Optional[List[Optional['BatchScheduleBenchmarkModelVersionResult']]]):
    if benchmark_version_results is None:
      del self.benchmark_version_results
      return
    if not isinstance(benchmark_version_results, list):
      raise TypeError('benchmark_version_results must be of type list')
    if not all([isinstance(t, BatchScheduleBenchmarkModelVersionResult) for t in benchmark_version_results]):
      raise TypeError('benchmark_version_results must contain only items of type BatchScheduleBenchmarkModelVersionResult')
    self._benchmark_version_results = benchmark_version_results


class BackfillBenchmarkAclsRequest(KaggleObject):
  r"""
  """

  pass

class BackfillBenchmarkAclsResponse(KaggleObject):
  r"""
  Attributes:
    affected_benchmarks_count (int)
  """

  def __init__(self):
    self._affected_benchmarks_count = 0
    self._freeze()

  @property
  def affected_benchmarks_count(self) -> int:
    return self._affected_benchmarks_count

  @affected_benchmarks_count.setter
  def affected_benchmarks_count(self, affected_benchmarks_count: int):
    if affected_benchmarks_count is None:
      del self.affected_benchmarks_count
      return
    if not isinstance(affected_benchmarks_count, int):
      raise TypeError('affected_benchmarks_count must be of type int')
    self._affected_benchmarks_count = affected_benchmarks_count


class BackfillBenchmarkRunMetadataRequest(KaggleObject):
  r"""
  Attributes:
    batch_size (int)
      Maximum number of runs with null start/end time to process in this batch.
      If not set or <= 0, defaults to 500.
  """

  def __init__(self):
    self._batch_size = 0
    self._freeze()

  @property
  def batch_size(self) -> int:
    r"""
    Maximum number of runs with null start/end time to process in this batch.
    If not set or <= 0, defaults to 500.
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


class BackfillBenchmarkRunMetadataResponse(KaggleObject):
  r"""
  Attributes:
    transaction_succeeded (bool)
      Whether the final DB transaction succeeded
    transaction_error_message (str)
      Error message if transaction failed
    updated_count (int)
      Counts
    skipped_count (int)
    failed_count (int)
    update_results (BenchmarkRunMetadataUpdateResult)
      Detailed results
    failures (BenchmarkRunMetadataFailure)
    remaining_count (int)
      Number of runs with null start/end time still remaining after this batch
  """

  def __init__(self):
    self._transaction_succeeded = False
    self._transaction_error_message = ""
    self._updated_count = 0
    self._skipped_count = 0
    self._failed_count = 0
    self._update_results = []
    self._failures = []
    self._remaining_count = 0
    self._freeze()

  @property
  def transaction_succeeded(self) -> bool:
    """Whether the final DB transaction succeeded"""
    return self._transaction_succeeded

  @transaction_succeeded.setter
  def transaction_succeeded(self, transaction_succeeded: bool):
    if transaction_succeeded is None:
      del self.transaction_succeeded
      return
    if not isinstance(transaction_succeeded, bool):
      raise TypeError('transaction_succeeded must be of type bool')
    self._transaction_succeeded = transaction_succeeded

  @property
  def transaction_error_message(self) -> str:
    """Error message if transaction failed"""
    return self._transaction_error_message

  @transaction_error_message.setter
  def transaction_error_message(self, transaction_error_message: str):
    if transaction_error_message is None:
      del self.transaction_error_message
      return
    if not isinstance(transaction_error_message, str):
      raise TypeError('transaction_error_message must be of type str')
    self._transaction_error_message = transaction_error_message

  @property
  def updated_count(self) -> int:
    """Counts"""
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
  def skipped_count(self) -> int:
    return self._skipped_count

  @skipped_count.setter
  def skipped_count(self, skipped_count: int):
    if skipped_count is None:
      del self.skipped_count
      return
    if not isinstance(skipped_count, int):
      raise TypeError('skipped_count must be of type int')
    self._skipped_count = skipped_count

  @property
  def failed_count(self) -> int:
    return self._failed_count

  @failed_count.setter
  def failed_count(self, failed_count: int):
    if failed_count is None:
      del self.failed_count
      return
    if not isinstance(failed_count, int):
      raise TypeError('failed_count must be of type int')
    self._failed_count = failed_count

  @property
  def update_results(self) -> Optional[List[Optional['BenchmarkRunMetadataUpdateResult']]]:
    """Detailed results"""
    return self._update_results

  @update_results.setter
  def update_results(self, update_results: Optional[List[Optional['BenchmarkRunMetadataUpdateResult']]]):
    if update_results is None:
      del self.update_results
      return
    if not isinstance(update_results, list):
      raise TypeError('update_results must be of type list')
    if not all([isinstance(t, BenchmarkRunMetadataUpdateResult) for t in update_results]):
      raise TypeError('update_results must contain only items of type BenchmarkRunMetadataUpdateResult')
    self._update_results = update_results

  @property
  def failures(self) -> Optional[List[Optional['BenchmarkRunMetadataFailure']]]:
    return self._failures

  @failures.setter
  def failures(self, failures: Optional[List[Optional['BenchmarkRunMetadataFailure']]]):
    if failures is None:
      del self.failures
      return
    if not isinstance(failures, list):
      raise TypeError('failures must be of type list')
    if not all([isinstance(t, BenchmarkRunMetadataFailure) for t in failures]):
      raise TypeError('failures must contain only items of type BenchmarkRunMetadataFailure')
    self._failures = failures

  @property
  def remaining_count(self) -> int:
    """Number of runs with null start/end time still remaining after this batch"""
    return self._remaining_count

  @remaining_count.setter
  def remaining_count(self, remaining_count: int):
    if remaining_count is None:
      del self.remaining_count
      return
    if not isinstance(remaining_count, int):
      raise TypeError('remaining_count must be of type int')
    self._remaining_count = remaining_count


class BackfillBenchmarkRunStatesRequest(KaggleObject):
  r"""
  Attributes:
    batch_size (int)
      Maximum number of UNSPECIFIED runs to process in this batch.
      If not set or <= 0, defaults to 500.
  """

  def __init__(self):
    self._batch_size = 0
    self._freeze()

  @property
  def batch_size(self) -> int:
    r"""
    Maximum number of UNSPECIFIED runs to process in this batch.
    If not set or <= 0, defaults to 500.
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


class BackfillBenchmarkRunStatesResponse(KaggleObject):
  r"""
  Attributes:
    transaction_succeeded (bool)
      Whether the final DB transaction succeeded
    transaction_error_message (str)
      Error message if transaction failed
    updated_count (int)
      Counts
    skipped_count (int)
    failed_count (int)
    update_results (BenchmarkRunStateUpdateResult)
      Detailed results (populated regardless of transaction success)
    skipped_runs (BenchmarkRunStateSkipped)
    failures (BenchmarkRunStateFailure)
    remaining_count (int)
      Number of UNSPECIFIED runs still remaining after this batch
  """

  def __init__(self):
    self._transaction_succeeded = False
    self._transaction_error_message = ""
    self._updated_count = 0
    self._skipped_count = 0
    self._failed_count = 0
    self._update_results = []
    self._skipped_runs = []
    self._failures = []
    self._remaining_count = 0
    self._freeze()

  @property
  def transaction_succeeded(self) -> bool:
    """Whether the final DB transaction succeeded"""
    return self._transaction_succeeded

  @transaction_succeeded.setter
  def transaction_succeeded(self, transaction_succeeded: bool):
    if transaction_succeeded is None:
      del self.transaction_succeeded
      return
    if not isinstance(transaction_succeeded, bool):
      raise TypeError('transaction_succeeded must be of type bool')
    self._transaction_succeeded = transaction_succeeded

  @property
  def transaction_error_message(self) -> str:
    """Error message if transaction failed"""
    return self._transaction_error_message

  @transaction_error_message.setter
  def transaction_error_message(self, transaction_error_message: str):
    if transaction_error_message is None:
      del self.transaction_error_message
      return
    if not isinstance(transaction_error_message, str):
      raise TypeError('transaction_error_message must be of type str')
    self._transaction_error_message = transaction_error_message

  @property
  def updated_count(self) -> int:
    """Counts"""
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
  def skipped_count(self) -> int:
    return self._skipped_count

  @skipped_count.setter
  def skipped_count(self, skipped_count: int):
    if skipped_count is None:
      del self.skipped_count
      return
    if not isinstance(skipped_count, int):
      raise TypeError('skipped_count must be of type int')
    self._skipped_count = skipped_count

  @property
  def failed_count(self) -> int:
    return self._failed_count

  @failed_count.setter
  def failed_count(self, failed_count: int):
    if failed_count is None:
      del self.failed_count
      return
    if not isinstance(failed_count, int):
      raise TypeError('failed_count must be of type int')
    self._failed_count = failed_count

  @property
  def update_results(self) -> Optional[List[Optional['BenchmarkRunStateUpdateResult']]]:
    """Detailed results (populated regardless of transaction success)"""
    return self._update_results

  @update_results.setter
  def update_results(self, update_results: Optional[List[Optional['BenchmarkRunStateUpdateResult']]]):
    if update_results is None:
      del self.update_results
      return
    if not isinstance(update_results, list):
      raise TypeError('update_results must be of type list')
    if not all([isinstance(t, BenchmarkRunStateUpdateResult) for t in update_results]):
      raise TypeError('update_results must contain only items of type BenchmarkRunStateUpdateResult')
    self._update_results = update_results

  @property
  def skipped_runs(self) -> Optional[List[Optional['BenchmarkRunStateSkipped']]]:
    return self._skipped_runs

  @skipped_runs.setter
  def skipped_runs(self, skipped_runs: Optional[List[Optional['BenchmarkRunStateSkipped']]]):
    if skipped_runs is None:
      del self.skipped_runs
      return
    if not isinstance(skipped_runs, list):
      raise TypeError('skipped_runs must be of type list')
    if not all([isinstance(t, BenchmarkRunStateSkipped) for t in skipped_runs]):
      raise TypeError('skipped_runs must contain only items of type BenchmarkRunStateSkipped')
    self._skipped_runs = skipped_runs

  @property
  def failures(self) -> Optional[List[Optional['BenchmarkRunStateFailure']]]:
    return self._failures

  @failures.setter
  def failures(self, failures: Optional[List[Optional['BenchmarkRunStateFailure']]]):
    if failures is None:
      del self.failures
      return
    if not isinstance(failures, list):
      raise TypeError('failures must be of type list')
    if not all([isinstance(t, BenchmarkRunStateFailure) for t in failures]):
      raise TypeError('failures must contain only items of type BenchmarkRunStateFailure')
    self._failures = failures

  @property
  def remaining_count(self) -> int:
    """Number of UNSPECIFIED runs still remaining after this batch"""
    return self._remaining_count

  @remaining_count.setter
  def remaining_count(self, remaining_count: int):
    if remaining_count is None:
      del self.remaining_count
      return
    if not isinstance(remaining_count, int):
      raise TypeError('remaining_count must be of type int')
    self._remaining_count = remaining_count


class BackfillBenchmarkUpdateTimeRequest(KaggleObject):
  r"""
  Attributes:
    batch_size (int)
      Maximum number of benchmarks to process in this batch.
      If not set or <= 0, defaults to 500.
  """

  def __init__(self):
    self._batch_size = 0
    self._freeze()

  @property
  def batch_size(self) -> int:
    r"""
    Maximum number of benchmarks to process in this batch.
    If not set or <= 0, defaults to 500.
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


class BackfillBenchmarkUpdateTimeResponse(KaggleObject):
  r"""
  Attributes:
    transaction_succeeded (bool)
      Whether the final DB transaction succeeded
    transaction_error_message (str)
      Error message if transaction failed
    updated_count (int)
      Counts
    skipped_count (int)
    failed_count (int)
    update_results (BenchmarkUpdateTimeResult)
      Detailed results
    failures (BenchmarkUpdateTimeFailure)
    remaining_count (int)
      Number of benchmarks still remaining after this batch
  """

  def __init__(self):
    self._transaction_succeeded = False
    self._transaction_error_message = ""
    self._updated_count = 0
    self._skipped_count = 0
    self._failed_count = 0
    self._update_results = []
    self._failures = []
    self._remaining_count = 0
    self._freeze()

  @property
  def transaction_succeeded(self) -> bool:
    """Whether the final DB transaction succeeded"""
    return self._transaction_succeeded

  @transaction_succeeded.setter
  def transaction_succeeded(self, transaction_succeeded: bool):
    if transaction_succeeded is None:
      del self.transaction_succeeded
      return
    if not isinstance(transaction_succeeded, bool):
      raise TypeError('transaction_succeeded must be of type bool')
    self._transaction_succeeded = transaction_succeeded

  @property
  def transaction_error_message(self) -> str:
    """Error message if transaction failed"""
    return self._transaction_error_message

  @transaction_error_message.setter
  def transaction_error_message(self, transaction_error_message: str):
    if transaction_error_message is None:
      del self.transaction_error_message
      return
    if not isinstance(transaction_error_message, str):
      raise TypeError('transaction_error_message must be of type str')
    self._transaction_error_message = transaction_error_message

  @property
  def updated_count(self) -> int:
    """Counts"""
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
  def skipped_count(self) -> int:
    return self._skipped_count

  @skipped_count.setter
  def skipped_count(self, skipped_count: int):
    if skipped_count is None:
      del self.skipped_count
      return
    if not isinstance(skipped_count, int):
      raise TypeError('skipped_count must be of type int')
    self._skipped_count = skipped_count

  @property
  def failed_count(self) -> int:
    return self._failed_count

  @failed_count.setter
  def failed_count(self, failed_count: int):
    if failed_count is None:
      del self.failed_count
      return
    if not isinstance(failed_count, int):
      raise TypeError('failed_count must be of type int')
    self._failed_count = failed_count

  @property
  def update_results(self) -> Optional[List[Optional['BenchmarkUpdateTimeResult']]]:
    """Detailed results"""
    return self._update_results

  @update_results.setter
  def update_results(self, update_results: Optional[List[Optional['BenchmarkUpdateTimeResult']]]):
    if update_results is None:
      del self.update_results
      return
    if not isinstance(update_results, list):
      raise TypeError('update_results must be of type list')
    if not all([isinstance(t, BenchmarkUpdateTimeResult) for t in update_results]):
      raise TypeError('update_results must contain only items of type BenchmarkUpdateTimeResult')
    self._update_results = update_results

  @property
  def failures(self) -> Optional[List[Optional['BenchmarkUpdateTimeFailure']]]:
    return self._failures

  @failures.setter
  def failures(self, failures: Optional[List[Optional['BenchmarkUpdateTimeFailure']]]):
    if failures is None:
      del self.failures
      return
    if not isinstance(failures, list):
      raise TypeError('failures must be of type list')
    if not all([isinstance(t, BenchmarkUpdateTimeFailure) for t in failures]):
      raise TypeError('failures must contain only items of type BenchmarkUpdateTimeFailure')
    self._failures = failures

  @property
  def remaining_count(self) -> int:
    """Number of benchmarks still remaining after this batch"""
    return self._remaining_count

  @remaining_count.setter
  def remaining_count(self, remaining_count: int):
    if remaining_count is None:
      del self.remaining_count
      return
    if not isinstance(remaining_count, int):
      raise TypeError('remaining_count must be of type int')
    self._remaining_count = remaining_count


class BenchmarkCoverageInfo(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
    full_slug (str)
    number_of_tasks_ran (int)
    total_number_of_tasks (int)
    name (str)
    error_messages (str)
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._full_slug = ""
    self._number_of_tasks_ran = 0
    self._total_number_of_tasks = 0
    self._name = ""
    self._error_messages = []
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id

  @property
  def full_slug(self) -> str:
    return self._full_slug

  @full_slug.setter
  def full_slug(self, full_slug: str):
    if full_slug is None:
      del self.full_slug
      return
    if not isinstance(full_slug, str):
      raise TypeError('full_slug must be of type str')
    self._full_slug = full_slug

  @property
  def number_of_tasks_ran(self) -> int:
    return self._number_of_tasks_ran

  @number_of_tasks_ran.setter
  def number_of_tasks_ran(self, number_of_tasks_ran: int):
    if number_of_tasks_ran is None:
      del self.number_of_tasks_ran
      return
    if not isinstance(number_of_tasks_ran, int):
      raise TypeError('number_of_tasks_ran must be of type int')
    self._number_of_tasks_ran = number_of_tasks_ran

  @property
  def total_number_of_tasks(self) -> int:
    return self._total_number_of_tasks

  @total_number_of_tasks.setter
  def total_number_of_tasks(self, total_number_of_tasks: int):
    if total_number_of_tasks is None:
      del self.total_number_of_tasks
      return
    if not isinstance(total_number_of_tasks, int):
      raise TypeError('total_number_of_tasks must be of type int')
    self._total_number_of_tasks = total_number_of_tasks

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def error_messages(self) -> Optional[List[str]]:
    return self._error_messages

  @error_messages.setter
  def error_messages(self, error_messages: Optional[List[str]]):
    if error_messages is None:
      del self.error_messages
      return
    if not isinstance(error_messages, list):
      raise TypeError('error_messages must be of type list')
    if not all([isinstance(t, str) for t in error_messages]):
      raise TypeError('error_messages must contain only items of type str')
    self._error_messages = error_messages


class BenchmarkRunMetadataFailure(KaggleObject):
  r"""
  Attributes:
    benchmark_run_id (int)
    error_message (str)
  """

  def __init__(self):
    self._benchmark_run_id = 0
    self._error_message = ""
    self._freeze()

  @property
  def benchmark_run_id(self) -> int:
    return self._benchmark_run_id

  @benchmark_run_id.setter
  def benchmark_run_id(self, benchmark_run_id: int):
    if benchmark_run_id is None:
      del self.benchmark_run_id
      return
    if not isinstance(benchmark_run_id, int):
      raise TypeError('benchmark_run_id must be of type int')
    self._benchmark_run_id = benchmark_run_id

  @property
  def error_message(self) -> str:
    return self._error_message

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class BenchmarkRunMetadataUpdateResult(KaggleObject):
  r"""
  Attributes:
    benchmark_run_id (int)
    source (str)
      The source used for backfill: 'evaluation_date' or 'create_time'
    start_time (datetime)
    end_time (datetime)
  """

  def __init__(self):
    self._benchmark_run_id = 0
    self._source = ""
    self._start_time = None
    self._end_time = None
    self._freeze()

  @property
  def benchmark_run_id(self) -> int:
    return self._benchmark_run_id

  @benchmark_run_id.setter
  def benchmark_run_id(self, benchmark_run_id: int):
    if benchmark_run_id is None:
      del self.benchmark_run_id
      return
    if not isinstance(benchmark_run_id, int):
      raise TypeError('benchmark_run_id must be of type int')
    self._benchmark_run_id = benchmark_run_id

  @property
  def source(self) -> str:
    """The source used for backfill: 'evaluation_date' or 'create_time'"""
    return self._source

  @source.setter
  def source(self, source: str):
    if source is None:
      del self.source
      return
    if not isinstance(source, str):
      raise TypeError('source must be of type str')
    self._source = source

  @property
  def start_time(self) -> datetime:
    return self._start_time

  @start_time.setter
  def start_time(self, start_time: datetime):
    if start_time is None:
      del self.start_time
      return
    if not isinstance(start_time, datetime):
      raise TypeError('start_time must be of type datetime')
    self._start_time = start_time

  @property
  def end_time(self) -> datetime:
    return self._end_time

  @end_time.setter
  def end_time(self, end_time: datetime):
    if end_time is None:
      del self.end_time
      return
    if not isinstance(end_time, datetime):
      raise TypeError('end_time must be of type datetime')
    self._end_time = end_time


class BenchmarkRunStateFailure(KaggleObject):
  r"""
  Attributes:
    benchmark_run_id (int)
    benchmark_task_version_id (int)
    benchmark_model_version_id (int)
    error_message (str)
  """

  def __init__(self):
    self._benchmark_run_id = 0
    self._benchmark_task_version_id = 0
    self._benchmark_model_version_id = 0
    self._error_message = ""
    self._freeze()

  @property
  def benchmark_run_id(self) -> int:
    return self._benchmark_run_id

  @benchmark_run_id.setter
  def benchmark_run_id(self, benchmark_run_id: int):
    if benchmark_run_id is None:
      del self.benchmark_run_id
      return
    if not isinstance(benchmark_run_id, int):
      raise TypeError('benchmark_run_id must be of type int')
    self._benchmark_run_id = benchmark_run_id

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def error_message(self) -> str:
    return self._error_message

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class BenchmarkRunStateSkipped(KaggleObject):
  r"""
  Attributes:
    benchmark_run_id (int)
    benchmark_task_version_id (int)
    benchmark_model_version_id (int)
    blob_state (BenchmarkTaskRunState)
    reason (str)
  """

  def __init__(self):
    self._benchmark_run_id = 0
    self._benchmark_task_version_id = 0
    self._benchmark_model_version_id = 0
    self._blob_state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._reason = ""
    self._freeze()

  @property
  def benchmark_run_id(self) -> int:
    return self._benchmark_run_id

  @benchmark_run_id.setter
  def benchmark_run_id(self, benchmark_run_id: int):
    if benchmark_run_id is None:
      del self.benchmark_run_id
      return
    if not isinstance(benchmark_run_id, int):
      raise TypeError('benchmark_run_id must be of type int')
    self._benchmark_run_id = benchmark_run_id

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def blob_state(self) -> 'BenchmarkTaskRunState':
    return self._blob_state

  @blob_state.setter
  def blob_state(self, blob_state: 'BenchmarkTaskRunState'):
    if blob_state is None:
      del self.blob_state
      return
    if not isinstance(blob_state, BenchmarkTaskRunState):
      raise TypeError('blob_state must be of type BenchmarkTaskRunState')
    self._blob_state = blob_state

  @property
  def reason(self) -> str:
    return self._reason

  @reason.setter
  def reason(self, reason: str):
    if reason is None:
      del self.reason
      return
    if not isinstance(reason, str):
      raise TypeError('reason must be of type str')
    self._reason = reason


class BenchmarkRunStateUpdateResult(KaggleObject):
  r"""
  Attributes:
    benchmark_run_id (int)
    benchmark_task_version_id (int)
    benchmark_model_version_id (int)
    old_state (BenchmarkTaskRunState)
    new_state (BenchmarkTaskRunState)
  """

  def __init__(self):
    self._benchmark_run_id = 0
    self._benchmark_task_version_id = 0
    self._benchmark_model_version_id = 0
    self._old_state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._new_state = BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED
    self._freeze()

  @property
  def benchmark_run_id(self) -> int:
    return self._benchmark_run_id

  @benchmark_run_id.setter
  def benchmark_run_id(self, benchmark_run_id: int):
    if benchmark_run_id is None:
      del self.benchmark_run_id
      return
    if not isinstance(benchmark_run_id, int):
      raise TypeError('benchmark_run_id must be of type int')
    self._benchmark_run_id = benchmark_run_id

  @property
  def benchmark_task_version_id(self) -> int:
    return self._benchmark_task_version_id

  @benchmark_task_version_id.setter
  def benchmark_task_version_id(self, benchmark_task_version_id: int):
    if benchmark_task_version_id is None:
      del self.benchmark_task_version_id
      return
    if not isinstance(benchmark_task_version_id, int):
      raise TypeError('benchmark_task_version_id must be of type int')
    self._benchmark_task_version_id = benchmark_task_version_id

  @property
  def benchmark_model_version_id(self) -> int:
    return self._benchmark_model_version_id

  @benchmark_model_version_id.setter
  def benchmark_model_version_id(self, benchmark_model_version_id: int):
    if benchmark_model_version_id is None:
      del self.benchmark_model_version_id
      return
    if not isinstance(benchmark_model_version_id, int):
      raise TypeError('benchmark_model_version_id must be of type int')
    self._benchmark_model_version_id = benchmark_model_version_id

  @property
  def old_state(self) -> 'BenchmarkTaskRunState':
    return self._old_state

  @old_state.setter
  def old_state(self, old_state: 'BenchmarkTaskRunState'):
    if old_state is None:
      del self.old_state
      return
    if not isinstance(old_state, BenchmarkTaskRunState):
      raise TypeError('old_state must be of type BenchmarkTaskRunState')
    self._old_state = old_state

  @property
  def new_state(self) -> 'BenchmarkTaskRunState':
    return self._new_state

  @new_state.setter
  def new_state(self, new_state: 'BenchmarkTaskRunState'):
    if new_state is None:
      del self.new_state
      return
    if not isinstance(new_state, BenchmarkTaskRunState):
      raise TypeError('new_state must be of type BenchmarkTaskRunState')
    self._new_state = new_state


class BenchmarkUpdateTimeFailure(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
    error_message (str)
  """

  def __init__(self):
    self._benchmark_id = 0
    self._error_message = ""
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def error_message(self) -> str:
    return self._error_message

  @error_message.setter
  def error_message(self, error_message: str):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


class BenchmarkUpdateTimeResult(KaggleObject):
  r"""
  Attributes:
    benchmark_id (int)
    old_update_time (datetime)
    new_update_time (datetime)
    source_benchmark_version_id (int)
      The BenchmarkVersion ID that had the max UpdateTime
  """

  def __init__(self):
    self._benchmark_id = 0
    self._old_update_time = None
    self._new_update_time = None
    self._source_benchmark_version_id = 0
    self._freeze()

  @property
  def benchmark_id(self) -> int:
    return self._benchmark_id

  @benchmark_id.setter
  def benchmark_id(self, benchmark_id: int):
    if benchmark_id is None:
      del self.benchmark_id
      return
    if not isinstance(benchmark_id, int):
      raise TypeError('benchmark_id must be of type int')
    self._benchmark_id = benchmark_id

  @property
  def old_update_time(self) -> datetime:
    return self._old_update_time

  @old_update_time.setter
  def old_update_time(self, old_update_time: datetime):
    if old_update_time is None:
      del self.old_update_time
      return
    if not isinstance(old_update_time, datetime):
      raise TypeError('old_update_time must be of type datetime')
    self._old_update_time = old_update_time

  @property
  def new_update_time(self) -> datetime:
    return self._new_update_time

  @new_update_time.setter
  def new_update_time(self, new_update_time: datetime):
    if new_update_time is None:
      del self.new_update_time
      return
    if not isinstance(new_update_time, datetime):
      raise TypeError('new_update_time must be of type datetime')
    self._new_update_time = new_update_time

  @property
  def source_benchmark_version_id(self) -> int:
    """The BenchmarkVersion ID that had the max UpdateTime"""
    return self._source_benchmark_version_id

  @source_benchmark_version_id.setter
  def source_benchmark_version_id(self, source_benchmark_version_id: int):
    if source_benchmark_version_id is None:
      del self.source_benchmark_version_id
      return
    if not isinstance(source_benchmark_version_id, int):
      raise TypeError('source_benchmark_version_id must be of type int')
    self._source_benchmark_version_id = source_benchmark_version_id


class BulkCreateBenchmarkTasksRequest(KaggleObject):
  r"""
  Attributes:
    tasks (BenchmarkTask)
      Benchmark tasks to create.
  """

  def __init__(self):
    self._tasks = []
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['BenchmarkTask']]]:
    """Benchmark tasks to create."""
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['BenchmarkTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, BenchmarkTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type BenchmarkTask')
    self._tasks = tasks


class BulkCreateBenchmarkTasksResponse(KaggleObject):
  r"""
  Attributes:
    created_tasks (BenchmarkTask)
  """

  def __init__(self):
    self._created_tasks = []
    self._freeze()

  @property
  def created_tasks(self) -> Optional[List[Optional['BenchmarkTask']]]:
    return self._created_tasks

  @created_tasks.setter
  def created_tasks(self, created_tasks: Optional[List[Optional['BenchmarkTask']]]):
    if created_tasks is None:
      del self.created_tasks
      return
    if not isinstance(created_tasks, list):
      raise TypeError('created_tasks must be of type list')
    if not all([isinstance(t, BenchmarkTask) for t in created_tasks]):
      raise TypeError('created_tasks must contain only items of type BenchmarkTask')
    self._created_tasks = created_tasks


class CopyCitationToChildBenchmarkVersionsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
      Benchmark Version id to propagate the citation from.
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """Benchmark Version id to propagate the citation from."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id


class CopyCitationToChildBenchmarkVersionsResponse(KaggleObject):
  r"""
  Attributes:
    affected_benchmark_versions_count (int)
  """

  def __init__(self):
    self._affected_benchmark_versions_count = 0
    self._freeze()

  @property
  def affected_benchmark_versions_count(self) -> int:
    return self._affected_benchmark_versions_count

  @affected_benchmark_versions_count.setter
  def affected_benchmark_versions_count(self, affected_benchmark_versions_count: int):
    if affected_benchmark_versions_count is None:
      del self.affected_benchmark_versions_count
      return
    if not isinstance(affected_benchmark_versions_count, int):
      raise TypeError('affected_benchmark_versions_count must be of type int')
    self._affected_benchmark_versions_count = affected_benchmark_versions_count


class CopyMediaToChildBenchmarkVersionsRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_id (int)
      Benchmark Version id to propagate media from.
  """

  def __init__(self):
    self._benchmark_version_id = 0
    self._freeze()

  @property
  def benchmark_version_id(self) -> int:
    """Benchmark Version id to propagate media from."""
    return self._benchmark_version_id

  @benchmark_version_id.setter
  def benchmark_version_id(self, benchmark_version_id: int):
    if benchmark_version_id is None:
      del self.benchmark_version_id
      return
    if not isinstance(benchmark_version_id, int):
      raise TypeError('benchmark_version_id must be of type int')
    self._benchmark_version_id = benchmark_version_id


class CopyMediaToChildBenchmarkVersionsResponse(KaggleObject):
  r"""
  Attributes:
    affected_benchmark_versions_count (int)
    new_media_count (int)
  """

  def __init__(self):
    self._affected_benchmark_versions_count = 0
    self._new_media_count = 0
    self._freeze()

  @property
  def affected_benchmark_versions_count(self) -> int:
    return self._affected_benchmark_versions_count

  @affected_benchmark_versions_count.setter
  def affected_benchmark_versions_count(self, affected_benchmark_versions_count: int):
    if affected_benchmark_versions_count is None:
      del self.affected_benchmark_versions_count
      return
    if not isinstance(affected_benchmark_versions_count, int):
      raise TypeError('affected_benchmark_versions_count must be of type int')
    self._affected_benchmark_versions_count = affected_benchmark_versions_count

  @property
  def new_media_count(self) -> int:
    return self._new_media_count

  @new_media_count.setter
  def new_media_count(self, new_media_count: int):
    if new_media_count is None:
      del self.new_media_count
      return
    if not isinstance(new_media_count, int):
      raise TypeError('new_media_count must be of type int')
    self._new_media_count = new_media_count


class GetResearchBenchmarkModelCoverageRequest(KaggleObject):
  r"""
  """

  pass

class GetResearchBenchmarkModelCoverageResponse(KaggleObject):
  r"""
  Attributes:
    model_infos (ModelCoverageInfo)
      Each row
    total_number_of_tasks_on_all_benchmarks (int)
      Total number of tasks across all benchmarks (same for every model).
  """

  def __init__(self):
    self._model_infos = []
    self._total_number_of_tasks_on_all_benchmarks = 0
    self._freeze()

  @property
  def model_infos(self) -> Optional[List[Optional['ModelCoverageInfo']]]:
    """Each row"""
    return self._model_infos

  @model_infos.setter
  def model_infos(self, model_infos: Optional[List[Optional['ModelCoverageInfo']]]):
    if model_infos is None:
      del self.model_infos
      return
    if not isinstance(model_infos, list):
      raise TypeError('model_infos must be of type list')
    if not all([isinstance(t, ModelCoverageInfo) for t in model_infos]):
      raise TypeError('model_infos must contain only items of type ModelCoverageInfo')
    self._model_infos = model_infos

  @property
  def total_number_of_tasks_on_all_benchmarks(self) -> int:
    """Total number of tasks across all benchmarks (same for every model)."""
    return self._total_number_of_tasks_on_all_benchmarks

  @total_number_of_tasks_on_all_benchmarks.setter
  def total_number_of_tasks_on_all_benchmarks(self, total_number_of_tasks_on_all_benchmarks: int):
    if total_number_of_tasks_on_all_benchmarks is None:
      del self.total_number_of_tasks_on_all_benchmarks
      return
    if not isinstance(total_number_of_tasks_on_all_benchmarks, int):
      raise TypeError('total_number_of_tasks_on_all_benchmarks must be of type int')
    self._total_number_of_tasks_on_all_benchmarks = total_number_of_tasks_on_all_benchmarks


class InvalidateBenchmarkLeaderboardCacheRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_version_ids (int)
      List of IDs of benchmark versions that need to have cache invalidated
  """

  def __init__(self):
    self._benchmark_version_ids = []
    self._freeze()

  @property
  def benchmark_version_ids(self) -> Optional[List[int]]:
    """List of IDs of benchmark versions that need to have cache invalidated"""
    return self._benchmark_version_ids

  @benchmark_version_ids.setter
  def benchmark_version_ids(self, benchmark_version_ids: Optional[List[int]]):
    if benchmark_version_ids is None:
      del self.benchmark_version_ids
      return
    if not isinstance(benchmark_version_ids, list):
      raise TypeError('benchmark_version_ids must be of type list')
    if not all([isinstance(t, int) for t in benchmark_version_ids]):
      raise TypeError('benchmark_version_ids must contain only items of type int')
    self._benchmark_version_ids = benchmark_version_ids


class InvalidateBenchmarkLeaderboardCacheResponse(KaggleObject):
  r"""
  Attributes:
    invalidated_benchmark_versions (BenchmarkVersion)
  """

  def __init__(self):
    self._invalidated_benchmark_versions = []
    self._freeze()

  @property
  def invalidated_benchmark_versions(self) -> Optional[List[Optional['BenchmarkVersion']]]:
    return self._invalidated_benchmark_versions

  @invalidated_benchmark_versions.setter
  def invalidated_benchmark_versions(self, invalidated_benchmark_versions: Optional[List[Optional['BenchmarkVersion']]]):
    if invalidated_benchmark_versions is None:
      del self.invalidated_benchmark_versions
      return
    if not isinstance(invalidated_benchmark_versions, list):
      raise TypeError('invalidated_benchmark_versions must be of type list')
    if not all([isinstance(t, BenchmarkVersion) for t in invalidated_benchmark_versions]):
      raise TypeError('invalidated_benchmark_versions must contain only items of type BenchmarkVersion')
    self._invalidated_benchmark_versions = invalidated_benchmark_versions


class MigrateKaggleNotebookMediaRequest(KaggleObject):
  r"""
  """

  pass

class MigrateKaggleNotebookMediaResponse(KaggleObject):
  r"""
  Attributes:
    media_affected_count (int)
  """

  def __init__(self):
    self._media_affected_count = 0
    self._freeze()

  @property
  def media_affected_count(self) -> int:
    return self._media_affected_count

  @media_affected_count.setter
  def media_affected_count(self, media_affected_count: int):
    if media_affected_count is None:
      del self.media_affected_count
      return
    if not isinstance(media_affected_count, int):
      raise TypeError('media_affected_count must be of type int')
    self._media_affected_count = media_affected_count


class ModelCoverageInfo(KaggleObject):
  r"""
  Attributes:
    model_version_id (int)
    model_version_slug (str)
    benchmark_infos (BenchmarkCoverageInfo)
      The information needed for each benchmark column.
      Will be the same length for each model.
    number_of_tasks_ran_on_all_benchmarks (int)
      Aggregated count of tasks ran across all benchmarks.
  """

  def __init__(self):
    self._model_version_id = 0
    self._model_version_slug = ""
    self._benchmark_infos = []
    self._number_of_tasks_ran_on_all_benchmarks = 0
    self._freeze()

  @property
  def model_version_id(self) -> int:
    return self._model_version_id

  @model_version_id.setter
  def model_version_id(self, model_version_id: int):
    if model_version_id is None:
      del self.model_version_id
      return
    if not isinstance(model_version_id, int):
      raise TypeError('model_version_id must be of type int')
    self._model_version_id = model_version_id

  @property
  def model_version_slug(self) -> str:
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
  def benchmark_infos(self) -> Optional[List[Optional['BenchmarkCoverageInfo']]]:
    r"""
    The information needed for each benchmark column.
    Will be the same length for each model.
    """
    return self._benchmark_infos

  @benchmark_infos.setter
  def benchmark_infos(self, benchmark_infos: Optional[List[Optional['BenchmarkCoverageInfo']]]):
    if benchmark_infos is None:
      del self.benchmark_infos
      return
    if not isinstance(benchmark_infos, list):
      raise TypeError('benchmark_infos must be of type list')
    if not all([isinstance(t, BenchmarkCoverageInfo) for t in benchmark_infos]):
      raise TypeError('benchmark_infos must contain only items of type BenchmarkCoverageInfo')
    self._benchmark_infos = benchmark_infos

  @property
  def number_of_tasks_ran_on_all_benchmarks(self) -> int:
    """Aggregated count of tasks ran across all benchmarks."""
    return self._number_of_tasks_ran_on_all_benchmarks

  @number_of_tasks_ran_on_all_benchmarks.setter
  def number_of_tasks_ran_on_all_benchmarks(self, number_of_tasks_ran_on_all_benchmarks: int):
    if number_of_tasks_ran_on_all_benchmarks is None:
      del self.number_of_tasks_ran_on_all_benchmarks
      return
    if not isinstance(number_of_tasks_ran_on_all_benchmarks, int):
      raise TypeError('number_of_tasks_ran_on_all_benchmarks must be of type int')
    self._number_of_tasks_ran_on_all_benchmarks = number_of_tasks_ran_on_all_benchmarks


class UpdateBenchmarkTaskOwnerRequest(KaggleObject):
  r"""
  Attributes:
    benchmark_task_id (int)
    user_id (int)
      ID of the user to set as the owner of the BenchmarkTask
  """

  def __init__(self):
    self._benchmark_task_id = 0
    self._user_id = 0
    self._freeze()

  @property
  def benchmark_task_id(self) -> int:
    return self._benchmark_task_id

  @benchmark_task_id.setter
  def benchmark_task_id(self, benchmark_task_id: int):
    if benchmark_task_id is None:
      del self.benchmark_task_id
      return
    if not isinstance(benchmark_task_id, int):
      raise TypeError('benchmark_task_id must be of type int')
    self._benchmark_task_id = benchmark_task_id

  @property
  def user_id(self) -> int:
    """ID of the user to set as the owner of the BenchmarkTask"""
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


AdminScheduleBenchmarkTaskRunsRequest._fields = [
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
]

AdminScheduleBenchmarkTaskRunsResponse._fields = [
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("results", "results", "_results", AdminScheduleBenchmarkTaskRunsResult, [], ListSerializer(KaggleObjectSerializer())),
]

AdminScheduleBenchmarkTaskRunsResult._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkVersionResults", "benchmark_version_results", "_benchmark_version_results", BatchScheduleBenchmarkModelVersionResult, [], ListSerializer(KaggleObjectSerializer())),
]

BackfillBenchmarkAclsRequest._fields = []

BackfillBenchmarkAclsResponse._fields = [
  FieldMetadata("affectedBenchmarksCount", "affected_benchmarks_count", "_affected_benchmarks_count", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkRunMetadataRequest._fields = [
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkRunMetadataResponse._fields = [
  FieldMetadata("transactionSucceeded", "transaction_succeeded", "_transaction_succeeded", bool, False, PredefinedSerializer()),
  FieldMetadata("transactionErrorMessage", "transaction_error_message", "_transaction_error_message", str, "", PredefinedSerializer()),
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
  FieldMetadata("skippedCount", "skipped_count", "_skipped_count", int, 0, PredefinedSerializer()),
  FieldMetadata("failedCount", "failed_count", "_failed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("updateResults", "update_results", "_update_results", BenchmarkRunMetadataUpdateResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("failures", "failures", "_failures", BenchmarkRunMetadataFailure, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("remainingCount", "remaining_count", "_remaining_count", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkRunStatesRequest._fields = [
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkRunStatesResponse._fields = [
  FieldMetadata("transactionSucceeded", "transaction_succeeded", "_transaction_succeeded", bool, False, PredefinedSerializer()),
  FieldMetadata("transactionErrorMessage", "transaction_error_message", "_transaction_error_message", str, "", PredefinedSerializer()),
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
  FieldMetadata("skippedCount", "skipped_count", "_skipped_count", int, 0, PredefinedSerializer()),
  FieldMetadata("failedCount", "failed_count", "_failed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("updateResults", "update_results", "_update_results", BenchmarkRunStateUpdateResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("skippedRuns", "skipped_runs", "_skipped_runs", BenchmarkRunStateSkipped, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("failures", "failures", "_failures", BenchmarkRunStateFailure, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("remainingCount", "remaining_count", "_remaining_count", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkUpdateTimeRequest._fields = [
  FieldMetadata("batchSize", "batch_size", "_batch_size", int, 0, PredefinedSerializer()),
]

BackfillBenchmarkUpdateTimeResponse._fields = [
  FieldMetadata("transactionSucceeded", "transaction_succeeded", "_transaction_succeeded", bool, False, PredefinedSerializer()),
  FieldMetadata("transactionErrorMessage", "transaction_error_message", "_transaction_error_message", str, "", PredefinedSerializer()),
  FieldMetadata("updatedCount", "updated_count", "_updated_count", int, 0, PredefinedSerializer()),
  FieldMetadata("skippedCount", "skipped_count", "_skipped_count", int, 0, PredefinedSerializer()),
  FieldMetadata("failedCount", "failed_count", "_failed_count", int, 0, PredefinedSerializer()),
  FieldMetadata("updateResults", "update_results", "_update_results", BenchmarkUpdateTimeResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("failures", "failures", "_failures", BenchmarkUpdateTimeFailure, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("remainingCount", "remaining_count", "_remaining_count", int, 0, PredefinedSerializer()),
]

BenchmarkCoverageInfo._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("fullSlug", "full_slug", "_full_slug", str, "", PredefinedSerializer()),
  FieldMetadata("numberOfTasksRan", "number_of_tasks_ran", "_number_of_tasks_ran", int, 0, PredefinedSerializer()),
  FieldMetadata("totalNumberOfTasks", "total_number_of_tasks", "_total_number_of_tasks", int, 0, PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("errorMessages", "error_messages", "_error_messages", str, [], ListSerializer(PredefinedSerializer())),
]

BenchmarkRunMetadataFailure._fields = [
  FieldMetadata("benchmarkRunId", "benchmark_run_id", "_benchmark_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
]

BenchmarkRunMetadataUpdateResult._fields = [
  FieldMetadata("benchmarkRunId", "benchmark_run_id", "_benchmark_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("source", "source", "_source", str, "", PredefinedSerializer()),
  FieldMetadata("startTime", "start_time", "_start_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("endTime", "end_time", "_end_time", datetime, None, DateTimeSerializer()),
]

BenchmarkRunStateFailure._fields = [
  FieldMetadata("benchmarkRunId", "benchmark_run_id", "_benchmark_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
]

BenchmarkRunStateSkipped._fields = [
  FieldMetadata("benchmarkRunId", "benchmark_run_id", "_benchmark_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("blobState", "blob_state", "_blob_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("reason", "reason", "_reason", str, "", PredefinedSerializer()),
]

BenchmarkRunStateUpdateResult._fields = [
  FieldMetadata("benchmarkRunId", "benchmark_run_id", "_benchmark_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelVersionId", "benchmark_model_version_id", "_benchmark_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("oldState", "old_state", "_old_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("newState", "new_state", "_new_state", BenchmarkTaskRunState, BenchmarkTaskRunState.BENCHMARK_TASK_RUN_STATE_UNSPECIFIED, EnumSerializer()),
]

BenchmarkUpdateTimeFailure._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
]

BenchmarkUpdateTimeResult._fields = [
  FieldMetadata("benchmarkId", "benchmark_id", "_benchmark_id", int, 0, PredefinedSerializer()),
  FieldMetadata("oldUpdateTime", "old_update_time", "_old_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("newUpdateTime", "new_update_time", "_new_update_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("sourceBenchmarkVersionId", "source_benchmark_version_id", "_source_benchmark_version_id", int, 0, PredefinedSerializer()),
]

BulkCreateBenchmarkTasksRequest._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", BenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
]

BulkCreateBenchmarkTasksResponse._fields = [
  FieldMetadata("createdTasks", "created_tasks", "_created_tasks", BenchmarkTask, [], ListSerializer(KaggleObjectSerializer())),
]

CopyCitationToChildBenchmarkVersionsRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
]

CopyCitationToChildBenchmarkVersionsResponse._fields = [
  FieldMetadata("affectedBenchmarkVersionsCount", "affected_benchmark_versions_count", "_affected_benchmark_versions_count", int, 0, PredefinedSerializer()),
]

CopyMediaToChildBenchmarkVersionsRequest._fields = [
  FieldMetadata("benchmarkVersionId", "benchmark_version_id", "_benchmark_version_id", int, 0, PredefinedSerializer()),
]

CopyMediaToChildBenchmarkVersionsResponse._fields = [
  FieldMetadata("affectedBenchmarkVersionsCount", "affected_benchmark_versions_count", "_affected_benchmark_versions_count", int, 0, PredefinedSerializer()),
  FieldMetadata("newMediaCount", "new_media_count", "_new_media_count", int, 0, PredefinedSerializer()),
]

GetResearchBenchmarkModelCoverageRequest._fields = []

GetResearchBenchmarkModelCoverageResponse._fields = [
  FieldMetadata("modelInfos", "model_infos", "_model_infos", ModelCoverageInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalNumberOfTasksOnAllBenchmarks", "total_number_of_tasks_on_all_benchmarks", "_total_number_of_tasks_on_all_benchmarks", int, 0, PredefinedSerializer()),
]

InvalidateBenchmarkLeaderboardCacheRequest._fields = [
  FieldMetadata("benchmarkVersionIds", "benchmark_version_ids", "_benchmark_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

InvalidateBenchmarkLeaderboardCacheResponse._fields = [
  FieldMetadata("invalidatedBenchmarkVersions", "invalidated_benchmark_versions", "_invalidated_benchmark_versions", BenchmarkVersion, [], ListSerializer(KaggleObjectSerializer())),
]

MigrateKaggleNotebookMediaRequest._fields = []

MigrateKaggleNotebookMediaResponse._fields = [
  FieldMetadata("mediaAffectedCount", "media_affected_count", "_media_affected_count", int, 0, PredefinedSerializer()),
]

ModelCoverageInfo._fields = [
  FieldMetadata("modelVersionId", "model_version_id", "_model_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, "", PredefinedSerializer()),
  FieldMetadata("benchmarkInfos", "benchmark_infos", "_benchmark_infos", BenchmarkCoverageInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numberOfTasksRanOnAllBenchmarks", "number_of_tasks_ran_on_all_benchmarks", "_number_of_tasks_ran_on_all_benchmarks", int, 0, PredefinedSerializer()),
]

UpdateBenchmarkTaskOwnerRequest._fields = [
  FieldMetadata("benchmarkTaskId", "benchmark_task_id", "_benchmark_task_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

