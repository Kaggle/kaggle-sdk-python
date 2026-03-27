import enum

class DatabundleDiffType(enum.Enum):
  REALTIME = 0
  UNVERSIONED = 1
  VERSIONED = 2

class DatabundleStatus(enum.Enum):
  DATABUNDLE_STATUS_CREATED = 0
  DATABUNDLE_STATUS_PROCESSING = 1
  DATABUNDLE_STATUS_ERROR = 2
  DATABUNDLE_STATUS_READY = 3

class DatabundleType(enum.Enum):
  DATABUNDLE_TYPE_UNSPECIFIED = 0
  DATABUNDLE_TYPE_GENERAL = 1
  DATABUNDLE_TYPE_DATASET = 2
  DATABUNDLE_TYPE_COMPETITION = 3
  DATABUNDLE_TYPE_NOTEBOOK = 4
  DATABUNDLE_TYPE_COMPETITION_RERUN = 5
  DATABUNDLE_TYPE_MODEL = 6

class DatabundleVersionAnalysisStatus(enum.Enum):
  DATABUNDLE_VERSION_ANALYSIS_STATUS_UNSPECIFIED = 0
  DATABUNDLE_VERSION_ANALYSIS_STATUS_PROCESSING = 1
  DATABUNDLE_VERSION_ANALYSIS_STATUS_DONE = 2
  DATABUNDLE_VERSION_ANALYSIS_STATUS_FAILED = 3

class DatabundleVersionStatus(enum.Enum):
  NOT_YET_PERSISTED = 0
  BLOBS_RECEIVED = 1
  BLOBS_DECOMPRESSED = 2
  BLOBS_COPIED_TO_SDS = 3
  INDIVIDUAL_BLOBS_COMPRESSED = 4
  READY = 5
  FAILED = 6
  DELETED = 7
  REPROCESSING = 8

class DatabundleVersionType(enum.Enum):
  DATABUNDLE_VERSION_TYPE_UNSPECIFIED = 0
  FILESET = 1
  BIG_QUERY = 2
  REMOTE_URL_FILE_SET = 3
  REMOTE_GIT_REPOSITORY_FILE_SET = 4
  KERNEL_OUTPUT_FILE_SET = 5
  GCS_FILE_SET = 6
  API_MODEL = 7
  REMOTE_HUGGING_FACE_REPOSITORY_FILE_SET = 8

class DatasetActivityType(enum.Enum):
  SCRIPT = 0
  SCRIPT_FORK = 1
  SCRIPT_RUN = 2
  DATASET = 3
  DATASET_VERSION = 4
  COMMENT = 5
  SCRIPT_COMMENT = 6
  TOPIC = 7

class FeedbackState(enum.Enum):
  FEEDBACK_STATE_UNSPECIFIED = 0
  VOTED = 1
  NO_VOTE = 2

class FeedbackType(enum.Enum):
  FEEDBACK_TYPE_UNSPECIFIED = 0
  DATASET_USAGE = 1
  DATASET_PROPERTIES = 2

class MetadataSuggestionType(enum.Enum):
  r"""
  Dataset metadata suggestion types. A custom CHECK constraint on the
  DatasetSuggestions table should exist for each suggestion type.
  """
  METADATA_SUGGESTION_TYPE_UNSPECIFIED = 0
  METADATA_SUGGESTION_TYPE_FILE_DESCRIPTION = 1
  METADATA_SUGGESTION_TYPE_COLUMN_DESCRIPTION = 2
  METADATA_SUGGESTION_TYPE_COLUMN_HARMONIZED_TYPE = 3
  METADATA_SUGGESTION_TYPE_COLUMN_EXTENDED_TYPE = 4

class RemoteUrlUpdateFrequency(enum.Enum):
  DAILY = 0
  WEEKLY = 1
  MONTHLY = 2
  NEVER = 3
  QUARTERLY = 4
  ANNUALLY = 5
  HOURLY = 6
  REMOTE_URL_UPDATE_FREQUENCY_UNSPECIFIED = -1
  r"""
  The value of UNSPECIFIED should be 0 but we can't change the value of DAILY
  because it is serialized as a number in the database (see the Settings
  column in the DatabundleVersions table).
  """

class SuggestionBundleState(enum.Enum):
  r"""
  State of a dataset suggestion bundle.
  Note, new states need to be mapped to user-readable strings, see mappings:
  for notifications at:
  .../PublishDatasetSuggestionReviewedNotificationHandler.cs
  for suggestions tab at:
  .../SuggestionsTab/SuggestionsList/SuggestionStateText.tsx
  """
  SUGGESTION_BUNDLE_STATE_UNSPECIFIED = 0
  SUGGESTION_BUNDLE_STATE_SUBMITTED = 1
  r"""
  Suggester has submitted the suggestion bundle and it is pending review from
  an approver.
  """
  SUGGESTION_BUNDLE_STATE_APPLIED = 2
  r"""
  Suggestion bundle has been applied. This represents the final, successful
  state after suggestions have been approved.
  """
  SUGGESTION_BUNDLE_STATE_REJECTED = 3
  """Suggestion bundle was rejected by an approver."""
  SUGGESTION_BUNDLE_STATE_DELETED = 4
  """Suggestion bundle was deleted by the suggester."""
  SUGGESTION_BUNDLE_STATE_ATTEMPTED = 5
  r"""
  A subset of the suggestion in the bundle may have been applied. Likely, an
  error occured while applying the bundle, and the approver needs to retry.
  """
  SUGGESTION_BUNDLE_STATE_APPROVED_WITH_CHANGES = 6
  r"""
  The suggestion bundle was updated by an approver as part of an 'approve
  with changes' operation.
  """
  SUGGESTION_BUNDLE_STATE_APPLIED_WITH_CHANGES = 7
  r"""
  Suggestion bundle has been applied. This represents the final, successful
  state after suggestions have been 'approved with changes'.
  """

class SuggestionState(enum.Enum):
  """State of a dataset suggestion."""
  SUGGESTION_STATE_UNSPECIFIED = 0
  SUGGESTION_STATE_SUBMITTED = 1
  """Suggestion was created and is pending review from an approver."""
  SUGGESTION_STATE_APPLIED = 2
  """Suggestion has been applied, implies the suggestion was approved."""
  SUGGESTION_STATE_REJECTED = 3
  """Suggestion was rejected by an approver."""
  SUGGESTION_STATE_DELETED = 4
  """Suggestion was deleted by the suggester."""
  SUGGESTION_STATE_ATTEMPTED = 5
  """Suggestion was attempted, but failed. Requires a retry."""

class DatasetFileTypeGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_FILE_TYPE_GROUP_ALL = 0
  DATASET_FILE_TYPE_GROUP_CSV = 1
  DATASET_FILE_TYPE_GROUP_SQLITE = 2
  DATASET_FILE_TYPE_GROUP_JSON = 3
  DATASET_FILE_TYPE_GROUP_BIG_QUERY = 4
  DATASET_FILE_TYPE_GROUP_PARQUET = 5

class DatasetLicenseGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_LICENSE_GROUP_ALL = 0
  DATASET_LICENSE_GROUP_CC = 1
  DATASET_LICENSE_GROUP_GPL = 2
  DATASET_LICENSE_GROUP_ODB = 3
  DATASET_LICENSE_GROUP_OTHER = 4

class DatasetsActivityTypeEnum(enum.Enum):
  DATASETS_ACTIVITY_TYPE_ENUM_UNSPECIFIED = 0
  CREATE = 1
  NEW_VERSION = 2
  FEATURE = 3
  """Values 3 through 10 have been deprecated"""
  SUPER_FEATURE = 4
  UN_FEATURE = 5
  UN_SUPER_FEATURE = 6
  REMOVE = 7
  REMOVE_VERSION = 8
  PUBLISH = 9
  UN_PUBLISH = 10
  MAKE_PUBLIC = 11
  """Values 3 through 10 have been deprecated"""
  MAKE_PRIVATE = 12
  INTRA_VERSION_SCHEMA_UPDATE = 13

class DatasetSelectionGroup(enum.Enum):
  DATASET_SELECTION_GROUP_PUBLIC = 0
  DATASET_SELECTION_GROUP_MY = 1
  DATASET_SELECTION_GROUP_USER = 2
  DATASET_SELECTION_GROUP_USER_SHARED_WITH_ME = 3
  DATASET_SELECTION_GROUP_UPVOTED = 4
  DATASET_SELECTION_GROUP_MY_PRIVATE = 5
  DATASET_SELECTION_GROUP_MY_PUBLIC = 10
  DATASET_SELECTION_GROUP_ORGANIZATION = 6
  DATASET_SELECTION_GROUP_BOOKMARKED = 11
  DATASET_SELECTION_GROUP_COLLABORATION = 12
  DATASET_SELECTION_GROUP_SHARED_WITH_USER = 13
  DATASET_SELECTION_GROUP_FEATURED = 7
  """Old"""
  DATASET_SELECTION_GROUP_ALL = 8
  DATASET_SELECTION_GROUP_UNFEATURED = 9

class DatasetSizeGroup(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_SIZE_GROUP_ALL = 0
  DATASET_SIZE_GROUP_SMALL = 1
  DATASET_SIZE_GROUP_MEDIUM = 2
  DATASET_SIZE_GROUP_LARGE = 3

class DatasetSortBy(enum.Enum):
  r"""
  This enum drives acceptable values from the python API, so avoid changing
  enum member names if possible
  """
  DATASET_SORT_BY_HOTTEST = 0
  DATASET_SORT_BY_VOTES = 1
  DATASET_SORT_BY_UPDATED = 2
  DATASET_SORT_BY_ACTIVE = 3
  """Deprecated"""
  DATASET_SORT_BY_PUBLISHED = 4
  DATASET_SORT_BY_RELEVANCE = 5
  """Old world"""
  DATASET_SORT_BY_LAST_VIEWED = 6
  DATASET_SORT_BY_USABILITY = 7
  DATASET_SORT_BY_DOWNLOAD_COUNT = 8
  DATASET_SORT_BY_NOTEBOOK_COUNT = 9

class DatasetTopicEnum(enum.Enum):
  DATASET_TOPIC_ENUM_UNSPECIFIED = 0
  r"""
  LINT.IfChange
  Non-category (tag) based topics are values 0 - 9, as an arbitrary range
  distinct from category id based values. IFTTT safeguards link the places
  this assumption is used in MT logic.
  """
  POPULAR_DATASET = 1
  TRENDING_DATASET = 2
  TRENDING_TASK = 3
  RECENTLY_VIEWED = 4
  LLM_FINE_TUNING_DATASET = 5
  FEATURED_DATASET = 6
  BUSINESS_DATASET = 11102
  """Enum values below are Categories.Id for the corresponding category (tag)."""
  ARTS_AND_ENTERTAINMENT_DATASET = 2200
  EDUCATION_DATASET = 11105
  HEALTH_DATASET = 11111
  IMAGE_DATASET = 14102
  ECONOMICS_DATASET = 11205
  COVID_DATASET = 16575
  CLASSIFICATION_DATASET = 13302
  NLP_DATASET = 13204
  EARTH_AND_NATURE_DATASET = 7000
  COMPUTER_SCIENCE_DATASET = 12107
  CLOTHING_AND_ACCESSORIES_DATASET = 8301
  INTERNET_DATASET = 12116
  ONLINE_COMMUNITIES_DATASET = 16489
  SOFTWARE_DATASET = 12127
  EXERCISE_DATASET = 4130
  FOOD_DATASET = 16113
  MOVIES_AND_TV_SHOWS_DATASET = 2303
  NEWS_DATASET = 16430
  PROGRAMMING_DATASET = 12125
  BIOLOGY_DATASET = 7100
  SOCIAL_SCIENCE_DATASET = 11200
  MUSIC_DATASET = 2304
  FINANCE_DATASET = 11108
  CANCER_DATASET = 16382
  AUTOMOBILES_AND_VEHICLES_DATASET = 12402
  RETAIL_AND_SHOPPING_DATASET = 16281
  INVESTING_DATASET = 16371
  SPORTS_DATASET = 4141
  STANDARDIZED_TESTING_DATASET = 16410
  TRANSPORTATION_DATASET = 12400
  UNIVERSITIES_AND_COLLEGES_DATASET = 1222
  LAW_DATASET = 11115
  GAMES_DATASET = 2500
  TRAVEL_DATASET = 16461
  SOCIAL_NETWORKS_DATASET = 16502
  SOCIAL_ISSUES_AND_ADVOCACY_DATASET = 16453
  TEXT_DATASET = 14104
  BENCHMARK_DATASET = 17183

class DatasetViewedGroup(enum.Enum):
  DATASET_VIEWED_GROUP_UNSPECIFIED = 0
  DATASET_VIEWED_GROUP_VIEWED = 1

class GcsBucketValidation(enum.Enum):
  GCS_BUCKET_VALIDATION_UNDEFINED = 0
  GCS_BUCKET_OK = 1
  GCS_BUCKET_EMPTY = 2
  GCS_BUCKET_PRIVATE = 3
  GCS_BUCKET_NOT_FOUND = 4
  GCS_BUCKET_REQUESTER_PAYS = 5

class ListDatasetSuggestionBundlesOrderBy(enum.Enum):
  LIST_DATASET_SUGGESTION_BUNDLES_ORDER_BY_UNSPECIFIED = 0
  LIST_DATASET_SUGGESTION_BUNDLES_ORDER_BY_DATE_CREATED = 1
  LIST_DATASET_SUGGESTION_BUNDLES_ORDER_BY_DATE_UPDATED = 2

class UpdateFeedbackType(enum.Enum):
  UPDATE_FEEDBACK_TYPE_UNSPECIFIED = 0
  ADD_VOTE = 1
  REMOVE_VOTE = 2

class DatasetFileType(enum.Enum):
  DATASET_FILE_TYPE_UNSPECIFIED = 0
  DATASET_FILE_TYPE_CSV = 1
  DATASET_FILE_TYPE_JSON = 2
  DATASET_FILE_TYPE_SQLITE = 3
  DATASET_FILE_TYPE_OTHER = 4

