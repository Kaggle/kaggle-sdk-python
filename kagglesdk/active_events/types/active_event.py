from datetime import datetime
import enum
from kagglesdk.competitions.types.submission_status import SubmissionStatus
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import AcceleratorType, ImportType, KernelWorkerStatus
from kagglesdk.models.types.model_enums import ModelFramework
from typing import Optional

class ActiveEvent(KaggleObject):
  r"""
  ActiveEvent holds information about active events for a given user.
  $eventID is a concatenation of:
  - event type prefix (see below)
  - event target ID (e.g. session ID for a KernelSession).
  Path: /users/$userID/activeEvents/$eventID
  Producer: Web Tier
  Consumer: Browser

  Attributes:
    kernel_session (ActiveEvent.KernelSession)
    competition_submission (ActiveEvent.CompetitionSubmission)
    dataset_upload (ActiveEvent.DatasetUpload)
    scheduled_kernel_session (ActiveEvent.ScheduledKernelSession)
    competition_metric_validation (ActiveEvent.CompetitionMetricValidation)
    model_upload (ActiveEvent.ModelUpload)
    kernel_import (ActiveEvent.KernelImport)
    event_start (datetime)
      Time the event started.
    event_end (datetime)
      Time the event ended (success or failure).
    step_start (datetime)
      Time the current step for the event started.
  """

  class CompetitionMetricValidation(KaggleObject):
    r"""
    Attributes:
      competition_metric_version_id (int)
        The metric version which is being validated.
      source_kernel_session_id (int)
        The Kernel Session which was used as the metric version's source.
      metric_name (str)
        The current name of the metric.
      is_valid (bool)
        Whether the version is valid. Unset while validation is running.
      error_message (str)
        If invalid, the reason why.
    """

    def __init__(self):
      self._competition_metric_version_id = 0
      self._source_kernel_session_id = 0
      self._metric_name = ""
      self._is_valid = None
      self._error_message = None
      self._freeze()

    @property
    def competition_metric_version_id(self) -> int:
      """The metric version which is being validated."""
      return self._competition_metric_version_id

    @competition_metric_version_id.setter
    def competition_metric_version_id(self, competition_metric_version_id: int):
      if competition_metric_version_id is None:
        del self.competition_metric_version_id
        return
      if not isinstance(competition_metric_version_id, int):
        raise TypeError('competition_metric_version_id must be of type int')
      self._competition_metric_version_id = competition_metric_version_id

    @property
    def source_kernel_session_id(self) -> int:
      """The Kernel Session which was used as the metric version's source."""
      return self._source_kernel_session_id

    @source_kernel_session_id.setter
    def source_kernel_session_id(self, source_kernel_session_id: int):
      if source_kernel_session_id is None:
        del self.source_kernel_session_id
        return
      if not isinstance(source_kernel_session_id, int):
        raise TypeError('source_kernel_session_id must be of type int')
      self._source_kernel_session_id = source_kernel_session_id

    @property
    def metric_name(self) -> str:
      """The current name of the metric."""
      return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name: str):
      if metric_name is None:
        del self.metric_name
        return
      if not isinstance(metric_name, str):
        raise TypeError('metric_name must be of type str')
      self._metric_name = metric_name

    @property
    def is_valid(self) -> bool:
      """Whether the version is valid. Unset while validation is running."""
      return self._is_valid or False

    @is_valid.setter
    def is_valid(self, is_valid: Optional[bool]):
      if is_valid is None:
        del self.is_valid
        return
      if not isinstance(is_valid, bool):
        raise TypeError('is_valid must be of type bool')
      self._is_valid = is_valid

    @property
    def error_message(self) -> str:
      """If invalid, the reason why."""
      return self._error_message or ""

    @error_message.setter
    def error_message(self, error_message: Optional[str]):
      if error_message is None:
        del self.error_message
        return
      if not isinstance(error_message, str):
        raise TypeError('error_message must be of type str')
      self._error_message = error_message


  class CompetitionSubmission(KaggleObject):
    r"""
    Attributes:
      submission_id (int)
      kernel_session_id (int)
        KernelSessions.Id is set when we didn't end up requesting a submission
        from a kernel run submission. ex: SUBMISSION_FILE_NOT_FOUND.
      url (str)
      competition_id (int)
      competition_title (str)
      competition_thumbnail_image_url (str)
      status (SubmissionStatus)
      error_type (ActiveEvent.CompetitionSubmission.SubmissionErrorType)
        Additional information about a submission error, if available.
      error_details (str)
        To add more information (e.g. - expected file name) in case of an error.
    """

    class SubmissionErrorType(enum.Enum):
      SUBMISSION_ERROR_TYPE_UNSPECIFIED = 0
      SUBMISSION_FILE_NOT_FOUND = 1
      SUBMISSION_LIMIT_EXCEEDED = 2
      SUBMISSION_FILE_SIZE_LIMIT_EXCEEDED = 3

    def __init__(self):
      self._submission_id = None
      self._kernel_session_id = None
      self._url = ""
      self._competition_id = 0
      self._competition_title = ""
      self._competition_thumbnail_image_url = ""
      self._status = SubmissionStatus.PENDING
      self._error_type = self.SubmissionErrorType.SUBMISSION_ERROR_TYPE_UNSPECIFIED
      self._error_details = ""
      self._freeze()

    @property
    def submission_id(self) -> int:
      return self._submission_id or 0

    @submission_id.setter
    def submission_id(self, submission_id: int):
      if submission_id is None:
        del self.submission_id
        return
      if not isinstance(submission_id, int):
        raise TypeError('submission_id must be of type int')
      del self.kernel_session_id
      self._submission_id = submission_id

    @property
    def kernel_session_id(self) -> int:
      r"""
      KernelSessions.Id is set when we didn't end up requesting a submission
      from a kernel run submission. ex: SUBMISSION_FILE_NOT_FOUND.
      """
      return self._kernel_session_id or 0

    @kernel_session_id.setter
    def kernel_session_id(self, kernel_session_id: int):
      if kernel_session_id is None:
        del self.kernel_session_id
        return
      if not isinstance(kernel_session_id, int):
        raise TypeError('kernel_session_id must be of type int')
      del self.submission_id
      self._kernel_session_id = kernel_session_id

    @property
    def url(self) -> str:
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
    def competition_id(self) -> int:
      return self._competition_id

    @competition_id.setter
    def competition_id(self, competition_id: int):
      if competition_id is None:
        del self.competition_id
        return
      if not isinstance(competition_id, int):
        raise TypeError('competition_id must be of type int')
      self._competition_id = competition_id

    @property
    def competition_title(self) -> str:
      return self._competition_title

    @competition_title.setter
    def competition_title(self, competition_title: str):
      if competition_title is None:
        del self.competition_title
        return
      if not isinstance(competition_title, str):
        raise TypeError('competition_title must be of type str')
      self._competition_title = competition_title

    @property
    def competition_thumbnail_image_url(self) -> str:
      return self._competition_thumbnail_image_url

    @competition_thumbnail_image_url.setter
    def competition_thumbnail_image_url(self, competition_thumbnail_image_url: str):
      if competition_thumbnail_image_url is None:
        del self.competition_thumbnail_image_url
        return
      if not isinstance(competition_thumbnail_image_url, str):
        raise TypeError('competition_thumbnail_image_url must be of type str')
      self._competition_thumbnail_image_url = competition_thumbnail_image_url

    @property
    def status(self) -> 'SubmissionStatus':
      return self._status

    @status.setter
    def status(self, status: 'SubmissionStatus'):
      if status is None:
        del self.status
        return
      if not isinstance(status, SubmissionStatus):
        raise TypeError('status must be of type SubmissionStatus')
      self._status = status

    @property
    def error_type(self) -> 'ActiveEvent.CompetitionSubmission.SubmissionErrorType':
      """Additional information about a submission error, if available."""
      return self._error_type

    @error_type.setter
    def error_type(self, error_type: 'ActiveEvent.CompetitionSubmission.SubmissionErrorType'):
      if error_type is None:
        del self.error_type
        return
      if not isinstance(error_type, ActiveEvent.CompetitionSubmission.SubmissionErrorType):
        raise TypeError('error_type must be of type ActiveEvent.CompetitionSubmission.SubmissionErrorType')
      self._error_type = error_type

    @property
    def error_details(self) -> str:
      """To add more information (e.g. - expected file name) in case of an error."""
      return self._error_details

    @error_details.setter
    def error_details(self, error_details: str):
      if error_details is None:
        del self.error_details
        return
      if not isinstance(error_details, str):
        raise TypeError('error_details must be of type str')
      self._error_details = error_details


  class DatasetUpload(KaggleObject):
    r"""
    Attributes:
      dataset_id (int)
      dataset_version_id (int)
      title (str)
      url (str)
      thumbnail_image (str)
      version_notes (str)
      percent_done (float)
      error_message (str)
      status (ActiveEvent.DatasetUpload.DatasetUploadStatus)
      type (ActiveEvent.DatasetUpload.DatasetUploadType)
    """

    class DatasetUploadStatus(enum.Enum):
      DATASET_UPLOAD_STATUS_UNSPECIFIED = 0
      CREATING = 1
      FINISHED = 2
      FAILED = 3

    class DatasetUploadType(enum.Enum):
      DATASET_UPLOAD_TYPE_UNSPECIFIED = 0
      CREATION = 1
      VERSION = 2

    def __init__(self):
      self._dataset_id = 0
      self._dataset_version_id = 0
      self._title = ""
      self._url = ""
      self._thumbnail_image = ""
      self._version_notes = ""
      self._percent_done = 0.0
      self._error_message = ""
      self._status = self.DatasetUploadStatus.DATASET_UPLOAD_STATUS_UNSPECIFIED
      self._type = self.DatasetUploadType.DATASET_UPLOAD_TYPE_UNSPECIFIED
      self._freeze()

    @property
    def dataset_id(self) -> int:
      return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id: int):
      if dataset_id is None:
        del self.dataset_id
        return
      if not isinstance(dataset_id, int):
        raise TypeError('dataset_id must be of type int')
      self._dataset_id = dataset_id

    @property
    def dataset_version_id(self) -> int:
      return self._dataset_version_id

    @dataset_version_id.setter
    def dataset_version_id(self, dataset_version_id: int):
      if dataset_version_id is None:
        del self.dataset_version_id
        return
      if not isinstance(dataset_version_id, int):
        raise TypeError('dataset_version_id must be of type int')
      self._dataset_version_id = dataset_version_id

    @property
    def title(self) -> str:
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
    def thumbnail_image(self) -> str:
      return self._thumbnail_image

    @thumbnail_image.setter
    def thumbnail_image(self, thumbnail_image: str):
      if thumbnail_image is None:
        del self.thumbnail_image
        return
      if not isinstance(thumbnail_image, str):
        raise TypeError('thumbnail_image must be of type str')
      self._thumbnail_image = thumbnail_image

    @property
    def version_notes(self) -> str:
      return self._version_notes

    @version_notes.setter
    def version_notes(self, version_notes: str):
      if version_notes is None:
        del self.version_notes
        return
      if not isinstance(version_notes, str):
        raise TypeError('version_notes must be of type str')
      self._version_notes = version_notes

    @property
    def percent_done(self) -> float:
      return self._percent_done

    @percent_done.setter
    def percent_done(self, percent_done: float):
      if percent_done is None:
        del self.percent_done
        return
      if not isinstance(percent_done, float):
        raise TypeError('percent_done must be of type float')
      self._percent_done = percent_done

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

    @property
    def status(self) -> 'ActiveEvent.DatasetUpload.DatasetUploadStatus':
      return self._status

    @status.setter
    def status(self, status: 'ActiveEvent.DatasetUpload.DatasetUploadStatus'):
      if status is None:
        del self.status
        return
      if not isinstance(status, ActiveEvent.DatasetUpload.DatasetUploadStatus):
        raise TypeError('status must be of type ActiveEvent.DatasetUpload.DatasetUploadStatus')
      self._status = status

    @property
    def type(self) -> 'ActiveEvent.DatasetUpload.DatasetUploadType':
      return self._type

    @type.setter
    def type(self, type: 'ActiveEvent.DatasetUpload.DatasetUploadType'):
      if type is None:
        del self.type
        return
      if not isinstance(type, ActiveEvent.DatasetUpload.DatasetUploadType):
        raise TypeError('type must be of type ActiveEvent.DatasetUpload.DatasetUploadType')
      self._type = type


  class KernelImport(KaggleObject):
    r"""
    Attributes:
      kernel_import_id (str)
      external_source_user_id (str)
      import_type (ImportType)
      import_status (ActiveEvent.KernelImport.ImportStatus)
      file_name (str)
      new_kernel_url (str)
      external_source_avatar_url (str)
    """

    class ImportStatus(enum.Enum):
      IMPORTING = 0
      FINISHED = 1
      FAILED = 2

    def __init__(self):
      self._kernel_import_id = ""
      self._external_source_user_id = None
      self._import_type = ImportType.UNSPECIFIED
      self._import_status = self.ImportStatus.IMPORTING
      self._file_name = ""
      self._new_kernel_url = None
      self._external_source_avatar_url = None
      self._freeze()

    @property
    def kernel_import_id(self) -> str:
      return self._kernel_import_id

    @kernel_import_id.setter
    def kernel_import_id(self, kernel_import_id: str):
      if kernel_import_id is None:
        del self.kernel_import_id
        return
      if not isinstance(kernel_import_id, str):
        raise TypeError('kernel_import_id must be of type str')
      self._kernel_import_id = kernel_import_id

    @property
    def external_source_user_id(self) -> str:
      return self._external_source_user_id or ""

    @external_source_user_id.setter
    def external_source_user_id(self, external_source_user_id: Optional[str]):
      if external_source_user_id is None:
        del self.external_source_user_id
        return
      if not isinstance(external_source_user_id, str):
        raise TypeError('external_source_user_id must be of type str')
      self._external_source_user_id = external_source_user_id

    @property
    def import_type(self) -> 'ImportType':
      return self._import_type

    @import_type.setter
    def import_type(self, import_type: 'ImportType'):
      if import_type is None:
        del self.import_type
        return
      if not isinstance(import_type, ImportType):
        raise TypeError('import_type must be of type ImportType')
      self._import_type = import_type

    @property
    def import_status(self) -> 'ActiveEvent.KernelImport.ImportStatus':
      return self._import_status

    @import_status.setter
    def import_status(self, import_status: 'ActiveEvent.KernelImport.ImportStatus'):
      if import_status is None:
        del self.import_status
        return
      if not isinstance(import_status, ActiveEvent.KernelImport.ImportStatus):
        raise TypeError('import_status must be of type ActiveEvent.KernelImport.ImportStatus')
      self._import_status = import_status

    @property
    def file_name(self) -> str:
      return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
      if file_name is None:
        del self.file_name
        return
      if not isinstance(file_name, str):
        raise TypeError('file_name must be of type str')
      self._file_name = file_name

    @property
    def new_kernel_url(self) -> str:
      return self._new_kernel_url or ""

    @new_kernel_url.setter
    def new_kernel_url(self, new_kernel_url: Optional[str]):
      if new_kernel_url is None:
        del self.new_kernel_url
        return
      if not isinstance(new_kernel_url, str):
        raise TypeError('new_kernel_url must be of type str')
      self._new_kernel_url = new_kernel_url

    @property
    def external_source_avatar_url(self) -> str:
      return self._external_source_avatar_url or ""

    @external_source_avatar_url.setter
    def external_source_avatar_url(self, external_source_avatar_url: Optional[str]):
      if external_source_avatar_url is None:
        del self.external_source_avatar_url
        return
      if not isinstance(external_source_avatar_url, str):
        raise TypeError('external_source_avatar_url must be of type str')
      self._external_source_avatar_url = external_source_avatar_url


  class KernelSession(KaggleObject):
    r"""
    Attributes:
      session_id (int)
        KernelSessions.Id
      kernel_id (int)
        KernelSessions.KernelId
      title (str)
        KernelSession.Title OR the BenchmarkTaskVersion.Name produced as a result
        of the completed session
      worker_status (KernelWorkerStatus)
        KernelSession.WorkerStatus
      type (ActiveEvent.KernelSession.KernelSessionExecutionType)
      accelerator_type (AcceleratorType)
        AcceleratorType
      version_number (int)
        KernelSession.VersionNumber OR the BenchmarkTaskVersion.VersionNumber
        produced as a result of the completed session
      requires_building_packages (bool)
        KernelSession.VersionNumber OR BenchmarkTaskVersion.VersionNumber
      benchmark_task_version_id (int)
        BenchmarkTaskVersion.Id if the session produces a Benchmark Task upon
        completion
      status_message (str)
      model_version_slug (str)
        If the session was run as a benchmark task, this is the slug for the
        model that was evaluated
    """

    class KernelSessionExecutionType(enum.Enum):
      KERNEL_SESSION_TYPE_UNSPECIFIED = 0
      INTERACTIVE = 1
      BATCH = 2

    def __init__(self):
      self._session_id = 0
      self._kernel_id = 0
      self._title = ""
      self._worker_status = KernelWorkerStatus.QUEUED
      self._type = self.KernelSessionExecutionType.KERNEL_SESSION_TYPE_UNSPECIFIED
      self._accelerator_type = AcceleratorType.ACCELERATOR_TYPE_NONE
      self._version_number = 0
      self._requires_building_packages = None
      self._benchmark_task_version_id = None
      self._status_message = None
      self._model_version_slug = None
      self._freeze()

    @property
    def session_id(self) -> int:
      """KernelSessions.Id"""
      return self._session_id

    @session_id.setter
    def session_id(self, session_id: int):
      if session_id is None:
        del self.session_id
        return
      if not isinstance(session_id, int):
        raise TypeError('session_id must be of type int')
      self._session_id = session_id

    @property
    def kernel_id(self) -> int:
      """KernelSessions.KernelId"""
      return self._kernel_id

    @kernel_id.setter
    def kernel_id(self, kernel_id: int):
      if kernel_id is None:
        del self.kernel_id
        return
      if not isinstance(kernel_id, int):
        raise TypeError('kernel_id must be of type int')
      self._kernel_id = kernel_id

    @property
    def benchmark_task_version_id(self) -> int:
      r"""
      BenchmarkTaskVersion.Id if the session produces a Benchmark Task upon
      completion
      """
      return self._benchmark_task_version_id or 0

    @benchmark_task_version_id.setter
    def benchmark_task_version_id(self, benchmark_task_version_id: Optional[int]):
      if benchmark_task_version_id is None:
        del self.benchmark_task_version_id
        return
      if not isinstance(benchmark_task_version_id, int):
        raise TypeError('benchmark_task_version_id must be of type int')
      self._benchmark_task_version_id = benchmark_task_version_id

    @property
    def title(self) -> str:
      r"""
      KernelSession.Title OR the BenchmarkTaskVersion.Name produced as a result
      of the completed session
      """
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
    def worker_status(self) -> 'KernelWorkerStatus':
      """KernelSession.WorkerStatus"""
      return self._worker_status

    @worker_status.setter
    def worker_status(self, worker_status: 'KernelWorkerStatus'):
      if worker_status is None:
        del self.worker_status
        return
      if not isinstance(worker_status, KernelWorkerStatus):
        raise TypeError('worker_status must be of type KernelWorkerStatus')
      self._worker_status = worker_status

    @property
    def status_message(self) -> str:
      return self._status_message or ""

    @status_message.setter
    def status_message(self, status_message: Optional[str]):
      if status_message is None:
        del self.status_message
        return
      if not isinstance(status_message, str):
        raise TypeError('status_message must be of type str')
      self._status_message = status_message

    @property
    def accelerator_type(self) -> 'AcceleratorType':
      """AcceleratorType"""
      return self._accelerator_type

    @accelerator_type.setter
    def accelerator_type(self, accelerator_type: 'AcceleratorType'):
      if accelerator_type is None:
        del self.accelerator_type
        return
      if not isinstance(accelerator_type, AcceleratorType):
        raise TypeError('accelerator_type must be of type AcceleratorType')
      self._accelerator_type = accelerator_type

    @property
    def version_number(self) -> int:
      r"""
      KernelSession.VersionNumber OR the BenchmarkTaskVersion.VersionNumber
      produced as a result of the completed session
      """
      return self._version_number

    @version_number.setter
    def version_number(self, version_number: int):
      if version_number is None:
        del self.version_number
        return
      if not isinstance(version_number, int):
        raise TypeError('version_number must be of type int')
      self._version_number = version_number

    @property
    def requires_building_packages(self) -> bool:
      """KernelSession.VersionNumber OR BenchmarkTaskVersion.VersionNumber"""
      return self._requires_building_packages or False

    @requires_building_packages.setter
    def requires_building_packages(self, requires_building_packages: Optional[bool]):
      if requires_building_packages is None:
        del self.requires_building_packages
        return
      if not isinstance(requires_building_packages, bool):
        raise TypeError('requires_building_packages must be of type bool')
      self._requires_building_packages = requires_building_packages

    @property
    def model_version_slug(self) -> str:
      r"""
      If the session was run as a benchmark task, this is the slug for the
      model that was evaluated
      """
      return self._model_version_slug or ""

    @model_version_slug.setter
    def model_version_slug(self, model_version_slug: Optional[str]):
      if model_version_slug is None:
        del self.model_version_slug
        return
      if not isinstance(model_version_slug, str):
        raise TypeError('model_version_slug must be of type str')
      self._model_version_slug = model_version_slug

    @property
    def type(self) -> 'ActiveEvent.KernelSession.KernelSessionExecutionType':
      return self._type

    @type.setter
    def type(self, type: 'ActiveEvent.KernelSession.KernelSessionExecutionType'):
      if type is None:
        del self.type
        return
      if not isinstance(type, ActiveEvent.KernelSession.KernelSessionExecutionType):
        raise TypeError('type must be of type ActiveEvent.KernelSession.KernelSessionExecutionType')
      self._type = type


  class ModelUpload(KaggleObject):
    r"""
    Attributes:
      model_id (int)
      model_instance_version_id (int)
      title (str)
      framework (ModelFramework)
      variation_slug (str)
      url (str)
      version_notes (str)
      percent_done (float)
      error_message (str)
      status (ActiveEvent.ModelUpload.ModelUploadStatus)
      type (ActiveEvent.ModelUpload.ModelUploadType)
    """

    class ModelUploadStatus(enum.Enum):
      MODEL_UPLOAD_STATUS_UNSPECIFIED = 0
      CREATING = 1
      FINISHED = 2
      FAILED = 3

    class ModelUploadType(enum.Enum):
      DATASET_UPLOAD_TYPE_UNSPECIFIED = 0
      NEW_INSTANCE = 1
      NEW_VERSION = 2

    def __init__(self):
      self._model_id = 0
      self._model_instance_version_id = 0
      self._title = ""
      self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
      self._variation_slug = ""
      self._url = ""
      self._version_notes = ""
      self._percent_done = 0.0
      self._error_message = ""
      self._status = self.ModelUploadStatus.MODEL_UPLOAD_STATUS_UNSPECIFIED
      self._type = self.ModelUploadType.DATASET_UPLOAD_TYPE_UNSPECIFIED
      self._freeze()

    @property
    def model_id(self) -> int:
      return self._model_id

    @model_id.setter
    def model_id(self, model_id: int):
      if model_id is None:
        del self.model_id
        return
      if not isinstance(model_id, int):
        raise TypeError('model_id must be of type int')
      self._model_id = model_id

    @property
    def model_instance_version_id(self) -> int:
      return self._model_instance_version_id

    @model_instance_version_id.setter
    def model_instance_version_id(self, model_instance_version_id: int):
      if model_instance_version_id is None:
        del self.model_instance_version_id
        return
      if not isinstance(model_instance_version_id, int):
        raise TypeError('model_instance_version_id must be of type int')
      self._model_instance_version_id = model_instance_version_id

    @property
    def title(self) -> str:
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
    def framework(self) -> 'ModelFramework':
      return self._framework

    @framework.setter
    def framework(self, framework: 'ModelFramework'):
      if framework is None:
        del self.framework
        return
      if not isinstance(framework, ModelFramework):
        raise TypeError('framework must be of type ModelFramework')
      self._framework = framework

    @property
    def variation_slug(self) -> str:
      return self._variation_slug

    @variation_slug.setter
    def variation_slug(self, variation_slug: str):
      if variation_slug is None:
        del self.variation_slug
        return
      if not isinstance(variation_slug, str):
        raise TypeError('variation_slug must be of type str')
      self._variation_slug = variation_slug

    @property
    def url(self) -> str:
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
    def version_notes(self) -> str:
      return self._version_notes

    @version_notes.setter
    def version_notes(self, version_notes: str):
      if version_notes is None:
        del self.version_notes
        return
      if not isinstance(version_notes, str):
        raise TypeError('version_notes must be of type str')
      self._version_notes = version_notes

    @property
    def percent_done(self) -> float:
      return self._percent_done

    @percent_done.setter
    def percent_done(self, percent_done: float):
      if percent_done is None:
        del self.percent_done
        return
      if not isinstance(percent_done, float):
        raise TypeError('percent_done must be of type float')
      self._percent_done = percent_done

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

    @property
    def status(self) -> 'ActiveEvent.ModelUpload.ModelUploadStatus':
      return self._status

    @status.setter
    def status(self, status: 'ActiveEvent.ModelUpload.ModelUploadStatus'):
      if status is None:
        del self.status
        return
      if not isinstance(status, ActiveEvent.ModelUpload.ModelUploadStatus):
        raise TypeError('status must be of type ActiveEvent.ModelUpload.ModelUploadStatus')
      self._status = status

    @property
    def type(self) -> 'ActiveEvent.ModelUpload.ModelUploadType':
      return self._type

    @type.setter
    def type(self, type: 'ActiveEvent.ModelUpload.ModelUploadType'):
      if type is None:
        del self.type
        return
      if not isinstance(type, ActiveEvent.ModelUpload.ModelUploadType):
        raise TypeError('type must be of type ActiveEvent.ModelUpload.ModelUploadType')
      self._type = type


  class ScheduledKernelSession(KaggleObject):
    r"""
    Attributes:
      scheduled_kernel_session_id (int)
      kernel_id (int)
      title (str)
      iteration (int)
      iterations (int)
      next_session_date (datetime)
    """

    def __init__(self):
      self._scheduled_kernel_session_id = 0
      self._kernel_id = 0
      self._title = ""
      self._iteration = 0
      self._iterations = 0
      self._next_session_date = None
      self._freeze()

    @property
    def scheduled_kernel_session_id(self) -> int:
      return self._scheduled_kernel_session_id

    @scheduled_kernel_session_id.setter
    def scheduled_kernel_session_id(self, scheduled_kernel_session_id: int):
      if scheduled_kernel_session_id is None:
        del self.scheduled_kernel_session_id
        return
      if not isinstance(scheduled_kernel_session_id, int):
        raise TypeError('scheduled_kernel_session_id must be of type int')
      self._scheduled_kernel_session_id = scheduled_kernel_session_id

    @property
    def kernel_id(self) -> int:
      return self._kernel_id

    @kernel_id.setter
    def kernel_id(self, kernel_id: int):
      if kernel_id is None:
        del self.kernel_id
        return
      if not isinstance(kernel_id, int):
        raise TypeError('kernel_id must be of type int')
      self._kernel_id = kernel_id

    @property
    def title(self) -> str:
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
    def iteration(self) -> int:
      return self._iteration

    @iteration.setter
    def iteration(self, iteration: int):
      if iteration is None:
        del self.iteration
        return
      if not isinstance(iteration, int):
        raise TypeError('iteration must be of type int')
      self._iteration = iteration

    @property
    def iterations(self) -> int:
      return self._iterations

    @iterations.setter
    def iterations(self, iterations: int):
      if iterations is None:
        del self.iterations
        return
      if not isinstance(iterations, int):
        raise TypeError('iterations must be of type int')
      self._iterations = iterations

    @property
    def next_session_date(self) -> datetime:
      return self._next_session_date

    @next_session_date.setter
    def next_session_date(self, next_session_date: datetime):
      if next_session_date is None:
        del self.next_session_date
        return
      if not isinstance(next_session_date, datetime):
        raise TypeError('next_session_date must be of type datetime')
      self._next_session_date = next_session_date


  def __init__(self):
    self._kernel_session = None
    self._competition_submission = None
    self._dataset_upload = None
    self._scheduled_kernel_session = None
    self._competition_metric_validation = None
    self._model_upload = None
    self._kernel_import = None
    self._event_start = None
    self._event_end = None
    self._step_start = None
    self._freeze()

  @property
  def kernel_session(self) -> Optional['ActiveEvent.KernelSession']:
    return self._kernel_session or None

  @kernel_session.setter
  def kernel_session(self, kernel_session: Optional['ActiveEvent.KernelSession']):
    if kernel_session is None:
      del self.kernel_session
      return
    if not isinstance(kernel_session, ActiveEvent.KernelSession):
      raise TypeError('kernel_session must be of type ActiveEvent.KernelSession')
    del self.competition_submission
    del self.dataset_upload
    del self.scheduled_kernel_session
    del self.competition_metric_validation
    del self.model_upload
    del self.kernel_import
    self._kernel_session = kernel_session

  @property
  def competition_submission(self) -> Optional['ActiveEvent.CompetitionSubmission']:
    return self._competition_submission or None

  @competition_submission.setter
  def competition_submission(self, competition_submission: Optional['ActiveEvent.CompetitionSubmission']):
    if competition_submission is None:
      del self.competition_submission
      return
    if not isinstance(competition_submission, ActiveEvent.CompetitionSubmission):
      raise TypeError('competition_submission must be of type ActiveEvent.CompetitionSubmission')
    del self.kernel_session
    del self.dataset_upload
    del self.scheduled_kernel_session
    del self.competition_metric_validation
    del self.model_upload
    del self.kernel_import
    self._competition_submission = competition_submission

  @property
  def dataset_upload(self) -> Optional['ActiveEvent.DatasetUpload']:
    return self._dataset_upload or None

  @dataset_upload.setter
  def dataset_upload(self, dataset_upload: Optional['ActiveEvent.DatasetUpload']):
    if dataset_upload is None:
      del self.dataset_upload
      return
    if not isinstance(dataset_upload, ActiveEvent.DatasetUpload):
      raise TypeError('dataset_upload must be of type ActiveEvent.DatasetUpload')
    del self.kernel_session
    del self.competition_submission
    del self.scheduled_kernel_session
    del self.competition_metric_validation
    del self.model_upload
    del self.kernel_import
    self._dataset_upload = dataset_upload

  @property
  def scheduled_kernel_session(self) -> Optional['ActiveEvent.ScheduledKernelSession']:
    return self._scheduled_kernel_session or None

  @scheduled_kernel_session.setter
  def scheduled_kernel_session(self, scheduled_kernel_session: Optional['ActiveEvent.ScheduledKernelSession']):
    if scheduled_kernel_session is None:
      del self.scheduled_kernel_session
      return
    if not isinstance(scheduled_kernel_session, ActiveEvent.ScheduledKernelSession):
      raise TypeError('scheduled_kernel_session must be of type ActiveEvent.ScheduledKernelSession')
    del self.kernel_session
    del self.competition_submission
    del self.dataset_upload
    del self.competition_metric_validation
    del self.model_upload
    del self.kernel_import
    self._scheduled_kernel_session = scheduled_kernel_session

  @property
  def competition_metric_validation(self) -> Optional['ActiveEvent.CompetitionMetricValidation']:
    return self._competition_metric_validation or None

  @competition_metric_validation.setter
  def competition_metric_validation(self, competition_metric_validation: Optional['ActiveEvent.CompetitionMetricValidation']):
    if competition_metric_validation is None:
      del self.competition_metric_validation
      return
    if not isinstance(competition_metric_validation, ActiveEvent.CompetitionMetricValidation):
      raise TypeError('competition_metric_validation must be of type ActiveEvent.CompetitionMetricValidation')
    del self.kernel_session
    del self.competition_submission
    del self.dataset_upload
    del self.scheduled_kernel_session
    del self.model_upload
    del self.kernel_import
    self._competition_metric_validation = competition_metric_validation

  @property
  def model_upload(self) -> Optional['ActiveEvent.ModelUpload']:
    return self._model_upload or None

  @model_upload.setter
  def model_upload(self, model_upload: Optional['ActiveEvent.ModelUpload']):
    if model_upload is None:
      del self.model_upload
      return
    if not isinstance(model_upload, ActiveEvent.ModelUpload):
      raise TypeError('model_upload must be of type ActiveEvent.ModelUpload')
    del self.kernel_session
    del self.competition_submission
    del self.dataset_upload
    del self.scheduled_kernel_session
    del self.competition_metric_validation
    del self.kernel_import
    self._model_upload = model_upload

  @property
  def kernel_import(self) -> Optional['ActiveEvent.KernelImport']:
    return self._kernel_import or None

  @kernel_import.setter
  def kernel_import(self, kernel_import: Optional['ActiveEvent.KernelImport']):
    if kernel_import is None:
      del self.kernel_import
      return
    if not isinstance(kernel_import, ActiveEvent.KernelImport):
      raise TypeError('kernel_import must be of type ActiveEvent.KernelImport')
    del self.kernel_session
    del self.competition_submission
    del self.dataset_upload
    del self.scheduled_kernel_session
    del self.competition_metric_validation
    del self.model_upload
    self._kernel_import = kernel_import

  @property
  def event_start(self) -> datetime:
    """Time the event started."""
    return self._event_start

  @event_start.setter
  def event_start(self, event_start: datetime):
    if event_start is None:
      del self.event_start
      return
    if not isinstance(event_start, datetime):
      raise TypeError('event_start must be of type datetime')
    self._event_start = event_start

  @property
  def event_end(self) -> datetime:
    """Time the event ended (success or failure)."""
    return self._event_end

  @event_end.setter
  def event_end(self, event_end: datetime):
    if event_end is None:
      del self.event_end
      return
    if not isinstance(event_end, datetime):
      raise TypeError('event_end must be of type datetime')
    self._event_end = event_end

  @property
  def step_start(self) -> datetime:
    """Time the current step for the event started."""
    return self._step_start

  @step_start.setter
  def step_start(self, step_start: datetime):
    if step_start is None:
      del self.step_start
      return
    if not isinstance(step_start, datetime):
      raise TypeError('step_start must be of type datetime')
    self._step_start = step_start


ActiveEvent.CompetitionMetricValidation._fields = [
  FieldMetadata("competitionMetricVersionId", "competition_metric_version_id", "_competition_metric_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("sourceKernelSessionId", "source_kernel_session_id", "_source_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("metricName", "metric_name", "_metric_name", str, "", PredefinedSerializer()),
  FieldMetadata("isValid", "is_valid", "_is_valid", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

ActiveEvent.CompetitionSubmission._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelSessionId", "kernel_session_id", "_kernel_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("competitionTitle", "competition_title", "_competition_title", str, "", PredefinedSerializer()),
  FieldMetadata("competitionThumbnailImageUrl", "competition_thumbnail_image_url", "_competition_thumbnail_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", SubmissionStatus, SubmissionStatus.PENDING, EnumSerializer()),
  FieldMetadata("errorType", "error_type", "_error_type", ActiveEvent.CompetitionSubmission.SubmissionErrorType, ActiveEvent.CompetitionSubmission.SubmissionErrorType.SUBMISSION_ERROR_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("errorDetails", "error_details", "_error_details", str, "", PredefinedSerializer()),
]

ActiveEvent.DatasetUpload._fields = [
  FieldMetadata("datasetId", "dataset_id", "_dataset_id", int, 0, PredefinedSerializer()),
  FieldMetadata("datasetVersionId", "dataset_version_id", "_dataset_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImage", "thumbnail_image", "_thumbnail_image", str, "", PredefinedSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, "", PredefinedSerializer()),
  FieldMetadata("percentDone", "percent_done", "_percent_done", float, 0.0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", ActiveEvent.DatasetUpload.DatasetUploadStatus, ActiveEvent.DatasetUpload.DatasetUploadStatus.DATASET_UPLOAD_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", ActiveEvent.DatasetUpload.DatasetUploadType, ActiveEvent.DatasetUpload.DatasetUploadType.DATASET_UPLOAD_TYPE_UNSPECIFIED, EnumSerializer()),
]

ActiveEvent.KernelImport._fields = [
  FieldMetadata("kernelImportId", "kernel_import_id", "_kernel_import_id", str, "", PredefinedSerializer()),
  FieldMetadata("externalSourceUserId", "external_source_user_id", "_external_source_user_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("importType", "import_type", "_import_type", ImportType, ImportType.UNSPECIFIED, EnumSerializer()),
  FieldMetadata("importStatus", "import_status", "_import_status", ActiveEvent.KernelImport.ImportStatus, ActiveEvent.KernelImport.ImportStatus.IMPORTING, EnumSerializer()),
  FieldMetadata("fileName", "file_name", "_file_name", str, "", PredefinedSerializer()),
  FieldMetadata("newKernelUrl", "new_kernel_url", "_new_kernel_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalSourceAvatarUrl", "external_source_avatar_url", "_external_source_avatar_url", str, None, PredefinedSerializer(), optional=True),
]

ActiveEvent.KernelSession._fields = [
  FieldMetadata("sessionId", "session_id", "_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("workerStatus", "worker_status", "_worker_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", ActiveEvent.KernelSession.KernelSessionExecutionType, ActiveEvent.KernelSession.KernelSessionExecutionType.KERNEL_SESSION_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("acceleratorType", "accelerator_type", "_accelerator_type", AcceleratorType, AcceleratorType.ACCELERATOR_TYPE_NONE, EnumSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("requiresBuildingPackages", "requires_building_packages", "_requires_building_packages", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("benchmarkTaskVersionId", "benchmark_task_version_id", "_benchmark_task_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("statusMessage", "status_message", "_status_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelVersionSlug", "model_version_slug", "_model_version_slug", str, None, PredefinedSerializer(), optional=True),
]

ActiveEvent.ModelUpload._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("variationSlug", "variation_slug", "_variation_slug", str, "", PredefinedSerializer()),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, "", PredefinedSerializer()),
  FieldMetadata("percentDone", "percent_done", "_percent_done", float, 0.0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, "", PredefinedSerializer()),
  FieldMetadata("status", "status", "_status", ActiveEvent.ModelUpload.ModelUploadStatus, ActiveEvent.ModelUpload.ModelUploadStatus.MODEL_UPLOAD_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("type", "type", "_type", ActiveEvent.ModelUpload.ModelUploadType, ActiveEvent.ModelUpload.ModelUploadType.DATASET_UPLOAD_TYPE_UNSPECIFIED, EnumSerializer()),
]

ActiveEvent.ScheduledKernelSession._fields = [
  FieldMetadata("scheduledKernelSessionId", "scheduled_kernel_session_id", "_scheduled_kernel_session_id", int, 0, PredefinedSerializer()),
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("iteration", "iteration", "_iteration", int, 0, PredefinedSerializer()),
  FieldMetadata("iterations", "iterations", "_iterations", int, 0, PredefinedSerializer()),
  FieldMetadata("nextSessionDate", "next_session_date", "_next_session_date", datetime, None, DateTimeSerializer()),
]

ActiveEvent._fields = [
  FieldMetadata("kernelSession", "kernel_session", "_kernel_session", ActiveEvent.KernelSession, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competitionSubmission", "competition_submission", "_competition_submission", ActiveEvent.CompetitionSubmission, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("datasetUpload", "dataset_upload", "_dataset_upload", ActiveEvent.DatasetUpload, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("scheduledKernelSession", "scheduled_kernel_session", "_scheduled_kernel_session", ActiveEvent.ScheduledKernelSession, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("competitionMetricValidation", "competition_metric_validation", "_competition_metric_validation", ActiveEvent.CompetitionMetricValidation, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("modelUpload", "model_upload", "_model_upload", ActiveEvent.ModelUpload, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelImport", "kernel_import", "_kernel_import", ActiveEvent.KernelImport, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("eventStart", "event_start", "_event_start", datetime, None, DateTimeSerializer()),
  FieldMetadata("eventEnd", "event_end", "_event_end", datetime, None, DateTimeSerializer()),
  FieldMetadata("stepStart", "step_start", "_step_start", datetime, None, DateTimeSerializer()),
]

