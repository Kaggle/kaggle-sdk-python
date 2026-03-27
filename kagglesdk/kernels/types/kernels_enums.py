import enum

class AcceleratorType(enum.Enum):
  ACCELERATOR_TYPE_NONE = 0
  r"""
  Note: the enum values below should correspond
  exactly to the values in AcceleratorTypes table.
  These values are also used to embed Kaggle metadata
  into notebooks, which allow export/import of notebooks
  to preserve the notebook's settings. Adding values is
  fine, but they shouldn't be removed/renamed.
  """
  NVIDIA_TESLA_K80 = 1
  GPU = 2
  NVIDIA_TESLA_P100 = 2
  TPU_V2_8 = 3
  TPU_V3_8 = 4
  TPU_V2_32 = 5
  TPU_V2_128 = 6
  TPU_V2_256 = 7
  NVIDIA_TESLA_T4 = 8
  NVIDIA_TESLA_T4_HIGHMEM = 15
  TPU1VM_V3_8 = 9
  TPUVM_V3_8 = 9
  NVIDIA_TESLA_A100 = 10
  NVIDIA_L4 = 11
  TPU_V5E_8 = 12
  NVIDIA_L4_X1 = 13
  TPU_V6E_8 = 14
  NVIDIA_H100 = 16
  NVIDIA_RTX_PRO_6000 = 17

class ColabSubscriptionTier(enum.Enum):
  SUBSCRIPTION_TIER_UNSPECIFIED = 0
  SUBSCRIPTION_TIER_NONE = 1
  SUBSCRIPTION_TIER_PRO = 2
  SUBSCRIPTION_TIER_PRO_PLUS = 3

class DataSourceType(enum.Enum):
  DATA_SOURCE_TYPE_COMPETITION = 0
  DATA_SOURCE_TYPE_DATASET_VERSION = 1
  DATA_SOURCE_TYPE_KERNEL_VERSION = 2
  DATA_SOURCE_TYPE_COMPETITION_EVALUATION = 3
  DATA_SOURCE_TYPE_MODEL_INSTANCE_VERSION = 4

class DockerImagePinningType(enum.Enum):
  DOCKER_IMAGE_PINNING_TYPE_UNSPECIFIED = 0
  DOCKER_IMAGE_PINNING_TYPE_ORIGINAL = 1
  DOCKER_IMAGE_PINNING_TYPE_LATEST = 2

class DockerImageVersionDisabledReason(enum.Enum):
  DOCKER_IMAGE_VERSION_DISABLED_REASON_UNSPECIFIED = 0
  TPU_RESTRICTION = 1

class DockerImageVersionType(enum.Enum):
  DOCKER_IMAGE_VERSION_TYPE_LATEST = 0
  DOCKER_IMAGE_VERSION_TYPE_ORIGINAL = 1
  DOCKER_IMAGE_VERSION_TYPE_COMPETITION = 2

class EditorType(enum.Enum):
  EDITOR_TYPE_UNSPECIFIED = 0
  EDITOR_TYPE_SCRIPT = 1
  EDITOR_TYPE_NOTEBOOK = 2

class KernelAccessType(enum.Enum):
  KERNEL_ACCESS_TYPE_ADMINISTRATIVE = 0
  KERNEL_ACCESS_TYPE_READ = 1
  KERNEL_ACCESS_TYPE_WRITE = 2
  KERNEL_ACCESS_TYPE_COMMENT = 3
  KERNEL_ACCESS_TYPE_EXECUTE = 4
  r"""
  As of now, this should only be used with Benchmark related Kernels - see
  go/cross-user-tasks-runs for details.
  """

class KernelExecutionType(enum.Enum):
  KERNEL_EXECUTION_TYPE_UNSPECIFIED = 0
  SAVE_AND_RUN_ALL = 1
  INTER_ACTIVE = 2
  QUICK_SAVE = 3

class KernelSessionPackageState(enum.Enum):
  PACKAGE_NOT_DETECTED = 0
  PACKAGE_DETECTED = 1

class KernelsListSortType(enum.Enum):
  HOTNESS = 0
  COMMENT_COUNT = 1
  DATE_CREATED = 2
  DATE_RUN = 3
  RELEVANCE = 4
  SCORE_ASCENDING = 5
  SCORE_DESCENDING = 6
  VIEW_COUNT = 7
  VOTE_COUNT = 8

class KernelsListViewType(enum.Enum):
  KERNELS_LIST_VIEW_TYPE_UNSPECIFIED = 0
  PROFILE = 1
  UPVOTED = 2
  EVERYONE = 3
  COLLABORATION = 4
  FORK = 5
  BOOKMARKED = 6
  RECENTLY_VIEWED = 7
  PUBLIC_AND_USERS_PRIVATE = 8

class KernelVersionPinningType(enum.Enum):
  UNPINNED = 0
  PINNED = 1

class KernelVersionType(enum.Enum):
  KERNEL_VERSION_TYPE_UNSPECIFIED = 0
  BATCH = 1
  INTERACTIVE = 2
  QUICK = 3

class KernelWorkerStatus(enum.Enum):
  QUEUED = 0
  RUNNING = 1
  COMPLETE = 2
  ERROR = 3
  CANCEL_REQUESTED = 4
  CANCEL_ACKNOWLEDGED = 5
  NEW_SCRIPT = 6

class Language(enum.Enum):
  LANGUAGE_UNSPECIFIED = 0
  LANGUAGE_PYTHON = 1
  LANGUAGE_R = 2
  LANGUAGE_RMARKDOWN = 3
  LANGUAGE_JULIA = 4
  LANGUAGE_SQLITE = 5

class LegacyDataSourceType(enum.Enum):
  """TODO: Combine this with DataSourceType above."""
  LEGACY_DATA_SOURCE_TYPE_DATASET = 0
  LEGACY_DATA_SOURCE_TYPE_COMPETITION = 1
  LEGACY_DATA_SOURCE_TYPE_KERNEL = 2

class ListResourceReferencesOrderBy(enum.Enum):
  LIST_RESOURCE_REFERENCES_ORDER_BY_UNSPECIFIED = 0
  LIST_RESOURCE_REFERENCES_ORDER_BY_HOTNESS = 1
  LIST_RESOURCE_REFERENCES_ORDER_BY_VOTE_COUNT = 2
  LIST_RESOURCE_REFERENCES_ORDER_BY_NOTEBOOK_COUNT = 3
  LIST_RESOURCE_REFERENCES_ORDER_BY_PUBLISH_TIME = 4
  LIST_RESOURCE_REFERENCES_ORDER_BY_UPDATE_TIME = 5

class PersistenceMode(enum.Enum):
  PERSISTENCE_MODE_UNSPECIFIED = 0
  PERSISTENCE_MODE_NONE = 1
  PERSISTENCE_MODE_FILES = 2
  PERSISTENCE_MODE_VARS = 3
  PERSISTENCE_MODE_FILES_AND_VARS = 4

class ResourceReferenceType(enum.Enum):
  RESOURCE_REFERENCE_TYPE_UNSPECIFIED = 0
  RESOURCE_REFERENCE_TYPE_HUGGING_FACE_MODEL = 1

class ColabNotebookSource(enum.Enum):
  """should roughly mirror go/colab-fileid-sources"""
  COLAB_NOTEBOOK_SOURCE_UNSPECIFIED = 0
  COLAB_NOTEBOOK_SOURCE_DRIVE = 1
  COLAB_NOTEBOOK_SOURCE_URL = 2

class ColabVariant(enum.Enum):
  VARIANT_UNSPECIFIED = 0
  VARIANT_GPU = 1
  VARIANT_TPU = 2

class CreationSourceType(enum.Enum):
  CREATION_SOURCE_TYPE_UNSPECIFIED = 0
  r"""
  This enum is stored in the database, so new values should be added
  sequentially (don't edit field numbers).
  """
  COMPETITION_KERNEL_RERUN = 1
  COMPETITION_METRIC_KERNEL = 2
  COMPETITION_METRIC_VERSION = 3
  SUBMISSION_EVALUATION = 4
  COMPETITION_SYNTHETIC_COPY = 5
  KERNELS_PACKAGE_MANAGER = 6
  BENCHMARK_TASK_VERSION = 7
  BENCHMARK_TASK_RUN = 8
  MODEL_SIGNING = 9

class ListColabSortType(enum.Enum):
  NAME = 0
  VIEWED_BY_ME_TIME = 1
  CREATION_TIME = 2

class ImportType(enum.Enum):
  UNSPECIFIED = 0
  EXTERNAL_SOURCE_URL = 1
  GITHUB = 2
  COLAB = 3
  FILE = 4

