from datetime import datetime
from kagglesdk.benchmarks.types.benchmark_enums import BenchmarkModelImportanceLevel, Modality
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import License
from kagglesdk.users.types.legacy_organizations_service import OrganizationCard
from typing import Optional, List

class BenchmarkModel(KaggleObject):
  r"""
  Attributes:
    id (int)
      This benchmark model's id.
    display_name (str)
      The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'
    slug (str)
      The slug of the model (plus variation). ex: 'gemini-1.5-pro'
    organization_id (int)
      The organization that published the model.
    owner_user_id (int)
      The user that owns / created this model.
      Filled automatically while creating, can be updated later.
    license_id (int)
      The license for this model.
    default_version_id (int)
      The default version to use for this model.
      Filled automatically while creating, can be updated later.
    version (BenchmarkModelVersion)
      The version associated with this benchmark model.
      * CREATE : first version to be created with the parent benchmark model.
      * GET    : specified version or default if none was specified.
      * UPDATE : unused (use UpdateBenchmarkModelVersion).
    organization (OrganizationCard)
      The associated Organization, if any. Ignored on create and update.
    license (License)
      The associated License. Ignored on create and update.
    published (bool)
      Whether the benchmark model is published (iff ContentStateId == PUBLISHED).
  """

  def __init__(self):
    self._id = 0
    self._display_name = ""
    self._slug = ""
    self._organization_id = None
    self._owner_user_id = None
    self._license_id = 0
    self._default_version_id = None
    self._version = None
    self._organization = None
    self._license = None
    self._published = False
    self._freeze()

  @property
  def id(self) -> int:
    """This benchmark model's id."""
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
  def display_name(self) -> str:
    """The display name of the model (plus variation). ex: 'Gemini 1.5 Pro'"""
    return self._display_name

  @display_name.setter
  def display_name(self, display_name: str):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def slug(self) -> str:
    """The slug of the model (plus variation). ex: 'gemini-1.5-pro'"""
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
  def organization_id(self) -> int:
    """The organization that published the model."""
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: Optional[int]):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def owner_user_id(self) -> int:
    r"""
    The user that owns / created this model.
    Filled automatically while creating, can be updated later.
    """
    return self._owner_user_id or 0

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: Optional[int]):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id

  @property
  def license_id(self) -> int:
    """The license for this model."""
    return self._license_id

  @license_id.setter
  def license_id(self, license_id: int):
    if license_id is None:
      del self.license_id
      return
    if not isinstance(license_id, int):
      raise TypeError('license_id must be of type int')
    self._license_id = license_id

  @property
  def default_version_id(self) -> int:
    r"""
    The default version to use for this model.
    Filled automatically while creating, can be updated later.
    """
    return self._default_version_id or 0

  @default_version_id.setter
  def default_version_id(self, default_version_id: Optional[int]):
    if default_version_id is None:
      del self.default_version_id
      return
    if not isinstance(default_version_id, int):
      raise TypeError('default_version_id must be of type int')
    self._default_version_id = default_version_id

  @property
  def version(self) -> Optional['BenchmarkModelVersion']:
    r"""
    The version associated with this benchmark model.
    * CREATE : first version to be created with the parent benchmark model.
    * GET    : specified version or default if none was specified.
    * UPDATE : unused (use UpdateBenchmarkModelVersion).
    """
    return self._version or None

  @version.setter
  def version(self, version: Optional[Optional['BenchmarkModelVersion']]):
    if version is None:
      del self.version
      return
    if not isinstance(version, BenchmarkModelVersion):
      raise TypeError('version must be of type BenchmarkModelVersion')
    self._version = version

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """The associated Organization, if any. Ignored on create and update."""
    return self._organization

  @organization.setter
  def organization(self, organization: Optional['OrganizationCard']):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def license(self) -> Optional['License']:
    """The associated License. Ignored on create and update."""
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def published(self) -> bool:
    """Whether the benchmark model is published (iff ContentStateId == PUBLISHED)."""
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published


class BenchmarkModelVersion(KaggleObject):
  r"""
  Attributes:
    id (int)
      The id of the benchmark model version.
    benchmark_model_id (int)
      The id of the parent benchmark model.
    slug (str)
      The slug of the model version. ex: 'gemini-1.5-pro-001'
      Required for CREATE, can be updated later.
    external_url (str)
      An external link to a resource explaining the model version. ex: blog post,
      aistudio, etc.
    knowledge_cutoff (datetime)
      A cutoff date for training data for the model.
    is_default (bool)
      Whether this BenchmarkModelVersion is the default for the parent
      BenchmarkModel.
    published (bool)
      Whether the model version is published (iff ContentStateId == PUBLISHED and
      parent benchmark model has ContentStateId == PUBLISHED).
    allow_model_proxy (bool)
      Whether this BenchmarkModelVersion is supported by model proxy.
    model_proxy_slug (str)
      The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
      Only set when `allow_model_proxy` is true.
    display_name (str)
    description (str)
    organization (OrganizationCard)
      Fields from the model for convenience
    name (str)
    license (License)
    importance_level (BenchmarkModelImportanceLevel)
      Whether this model version is run on Kaggle-maintained benchmarks
    input_modalities (Modality)
      Input modalities supported by this model version.
    output_modalities (Modality)
      Output modalities supported by this model version.
  """

  def __init__(self):
    self._id = 0
    self._benchmark_model_id = 0
    self._slug = ""
    self._external_url = None
    self._knowledge_cutoff = None
    self._is_default = False
    self._published = False
    self._allow_model_proxy = False
    self._model_proxy_slug = None
    self._display_name = None
    self._description = None
    self._organization = None
    self._name = None
    self._license = None
    self._importance_level = None
    self._input_modalities = []
    self._output_modalities = []
    self._freeze()

  @property
  def id(self) -> int:
    """The id of the benchmark model version."""
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
  def benchmark_model_id(self) -> int:
    """The id of the parent benchmark model."""
    return self._benchmark_model_id

  @benchmark_model_id.setter
  def benchmark_model_id(self, benchmark_model_id: int):
    if benchmark_model_id is None:
      del self.benchmark_model_id
      return
    if not isinstance(benchmark_model_id, int):
      raise TypeError('benchmark_model_id must be of type int')
    self._benchmark_model_id = benchmark_model_id

  @property
  def slug(self) -> str:
    r"""
    The slug of the model version. ex: 'gemini-1.5-pro-001'
    Required for CREATE, can be updated later.
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
  def external_url(self) -> str:
    r"""
    An external link to a resource explaining the model version. ex: blog post,
    aistudio, etc.
    """
    return self._external_url or ""

  @external_url.setter
  def external_url(self, external_url: Optional[str]):
    if external_url is None:
      del self.external_url
      return
    if not isinstance(external_url, str):
      raise TypeError('external_url must be of type str')
    self._external_url = external_url

  @property
  def knowledge_cutoff(self) -> datetime:
    """A cutoff date for training data for the model."""
    return self._knowledge_cutoff or None

  @knowledge_cutoff.setter
  def knowledge_cutoff(self, knowledge_cutoff: Optional[datetime]):
    if knowledge_cutoff is None:
      del self.knowledge_cutoff
      return
    if not isinstance(knowledge_cutoff, datetime):
      raise TypeError('knowledge_cutoff must be of type datetime')
    self._knowledge_cutoff = knowledge_cutoff

  @property
  def is_default(self) -> bool:
    r"""
    Whether this BenchmarkModelVersion is the default for the parent
    BenchmarkModel.
    """
    return self._is_default

  @is_default.setter
  def is_default(self, is_default: bool):
    if is_default is None:
      del self.is_default
      return
    if not isinstance(is_default, bool):
      raise TypeError('is_default must be of type bool')
    self._is_default = is_default

  @property
  def published(self) -> bool:
    r"""
    Whether the model version is published (iff ContentStateId == PUBLISHED and
    parent benchmark model has ContentStateId == PUBLISHED).
    """
    return self._published

  @published.setter
  def published(self, published: bool):
    if published is None:
      del self.published
      return
    if not isinstance(published, bool):
      raise TypeError('published must be of type bool')
    self._published = published

  @property
  def allow_model_proxy(self) -> bool:
    """Whether this BenchmarkModelVersion is supported by model proxy."""
    return self._allow_model_proxy

  @allow_model_proxy.setter
  def allow_model_proxy(self, allow_model_proxy: bool):
    if allow_model_proxy is None:
      del self.allow_model_proxy
      return
    if not isinstance(allow_model_proxy, bool):
      raise TypeError('allow_model_proxy must be of type bool')
    self._allow_model_proxy = allow_model_proxy

  @property
  def model_proxy_slug(self) -> str:
    r"""
    The slug used by model proxy. ex: 'google/gemini-2.5-pro'.
    Only set when `allow_model_proxy` is true.
    """
    return self._model_proxy_slug or ""

  @model_proxy_slug.setter
  def model_proxy_slug(self, model_proxy_slug: Optional[str]):
    if model_proxy_slug is None:
      del self.model_proxy_slug
      return
    if not isinstance(model_proxy_slug, str):
      raise TypeError('model_proxy_slug must be of type str')
    self._model_proxy_slug = model_proxy_slug

  @property
  def display_name(self) -> str:
    return self._display_name or ""

  @display_name.setter
  def display_name(self, display_name: Optional[str]):
    if display_name is None:
      del self.display_name
      return
    if not isinstance(display_name, str):
      raise TypeError('display_name must be of type str')
    self._display_name = display_name

  @property
  def description(self) -> str:
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
  def name(self) -> str:
    return self._name or ""

  @name.setter
  def name(self, name: Optional[str]):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def organization(self) -> Optional['OrganizationCard']:
    """Fields from the model for convenience"""
    return self._organization or None

  @organization.setter
  def organization(self, organization: Optional[Optional['OrganizationCard']]):
    if organization is None:
      del self.organization
      return
    if not isinstance(organization, OrganizationCard):
      raise TypeError('organization must be of type OrganizationCard')
    self._organization = organization

  @property
  def license(self) -> Optional['License']:
    return self._license

  @license.setter
  def license(self, license: Optional['License']):
    if license is None:
      del self.license
      return
    if not isinstance(license, License):
      raise TypeError('license must be of type License')
    self._license = license

  @property
  def importance_level(self) -> 'BenchmarkModelImportanceLevel':
    """Whether this model version is run on Kaggle-maintained benchmarks"""
    return self._importance_level or BenchmarkModelImportanceLevel.BENCHMARK_MODEL_IMPORTANCE_LEVEL_UNSPECIFIED

  @importance_level.setter
  def importance_level(self, importance_level: Optional['BenchmarkModelImportanceLevel']):
    if importance_level is None:
      del self.importance_level
      return
    if not isinstance(importance_level, BenchmarkModelImportanceLevel):
      raise TypeError('importance_level must be of type BenchmarkModelImportanceLevel')
    self._importance_level = importance_level

  @property
  def input_modalities(self) -> Optional[List['Modality']]:
    """Input modalities supported by this model version."""
    return self._input_modalities

  @input_modalities.setter
  def input_modalities(self, input_modalities: Optional[List['Modality']]):
    if input_modalities is None:
      del self.input_modalities
      return
    if not isinstance(input_modalities, list):
      raise TypeError('input_modalities must be of type list')
    if not all([isinstance(t, Modality) for t in input_modalities]):
      raise TypeError('input_modalities must contain only items of type Modality')
    self._input_modalities = input_modalities

  @property
  def output_modalities(self) -> Optional[List['Modality']]:
    """Output modalities supported by this model version."""
    return self._output_modalities

  @output_modalities.setter
  def output_modalities(self, output_modalities: Optional[List['Modality']]):
    if output_modalities is None:
      del self.output_modalities
      return
    if not isinstance(output_modalities, list):
      raise TypeError('output_modalities must be of type list')
    if not all([isinstance(t, Modality) for t in output_modalities]):
      raise TypeError('output_modalities must contain only items of type Modality')
    self._output_modalities = output_modalities


class BenchmarkResult(KaggleObject):
  r"""
  TODO(bml): Integrate this proto with personal benchmarks trials.
  Represents the outcome of a benchmark run. All fields are immutable.

  Attributes:
    numeric_result (NumericResult)
    boolean_result (bool)
    custom_additional_results (CustomResult)
      Generic additional results. These are rendered generically on the frontend:
    numeric_result_private (NumericResult)
      Numeric result on the private set of the benchmark version.
    numeric_result_public (NumericResult)
      Numeric result on the public set of the benchmark version.
    evaluation_date (datetime)
      The date on which evaluation was performed.
    task_version_id (int)
      Convenience fields for this result (for the frontend):
  """

  def __init__(self):
    self._numeric_result = None
    self._boolean_result = None
    self._custom_additional_results = []
    self._numeric_result_private = None
    self._numeric_result_public = None
    self._evaluation_date = None
    self._task_version_id = None
    self._freeze()

  @property
  def task_version_id(self) -> int:
    """Convenience fields for this result (for the frontend):"""
    return self._task_version_id or 0

  @task_version_id.setter
  def task_version_id(self, task_version_id: Optional[int]):
    if task_version_id is None:
      del self.task_version_id
      return
    if not isinstance(task_version_id, int):
      raise TypeError('task_version_id must be of type int')
    self._task_version_id = task_version_id

  @property
  def numeric_result(self) -> Optional['NumericResult']:
    return self._numeric_result or None

  @numeric_result.setter
  def numeric_result(self, numeric_result: Optional['NumericResult']):
    if numeric_result is None:
      del self.numeric_result
      return
    if not isinstance(numeric_result, NumericResult):
      raise TypeError('numeric_result must be of type NumericResult')
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

  @property
  def custom_additional_results(self) -> Optional[List[Optional['CustomResult']]]:
    """Generic additional results. These are rendered generically on the frontend:"""
    return self._custom_additional_results

  @custom_additional_results.setter
  def custom_additional_results(self, custom_additional_results: Optional[List[Optional['CustomResult']]]):
    if custom_additional_results is None:
      del self.custom_additional_results
      return
    if not isinstance(custom_additional_results, list):
      raise TypeError('custom_additional_results must be of type list')
    if not all([isinstance(t, CustomResult) for t in custom_additional_results]):
      raise TypeError('custom_additional_results must contain only items of type CustomResult')
    self._custom_additional_results = custom_additional_results

  @property
  def numeric_result_private(self) -> Optional['NumericResult']:
    """Numeric result on the private set of the benchmark version."""
    return self._numeric_result_private or None

  @numeric_result_private.setter
  def numeric_result_private(self, numeric_result_private: Optional[Optional['NumericResult']]):
    if numeric_result_private is None:
      del self.numeric_result_private
      return
    if not isinstance(numeric_result_private, NumericResult):
      raise TypeError('numeric_result_private must be of type NumericResult')
    self._numeric_result_private = numeric_result_private

  @property
  def numeric_result_public(self) -> Optional['NumericResult']:
    """Numeric result on the public set of the benchmark version."""
    return self._numeric_result_public or None

  @numeric_result_public.setter
  def numeric_result_public(self, numeric_result_public: Optional[Optional['NumericResult']]):
    if numeric_result_public is None:
      del self.numeric_result_public
      return
    if not isinstance(numeric_result_public, NumericResult):
      raise TypeError('numeric_result_public must be of type NumericResult')
    self._numeric_result_public = numeric_result_public

  @property
  def evaluation_date(self) -> datetime:
    """The date on which evaluation was performed."""
    return self._evaluation_date or None

  @evaluation_date.setter
  def evaluation_date(self, evaluation_date: Optional[datetime]):
    if evaluation_date is None:
      del self.evaluation_date
      return
    if not isinstance(evaluation_date, datetime):
      raise TypeError('evaluation_date must be of type datetime')
    self._evaluation_date = evaluation_date


class CustomResult(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (str)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value


class NumericResult(KaggleObject):
  r"""
  Attributes:
    value (float)
    confidence_interval (float)
      Note, while we call this the 'confidence interval' - the value we store
      here is actually the 'confidence radius', it should always be displayed
      as a +- value.
    uneven_confidence_interval (UnevenConfidenceInterval)
      For asymmetric confidence intervals in which the +/- values differ
      If set, prioritized over confidence_interval (if both are set)
  """

  def __init__(self):
    self._value = 0.0
    self._confidence_interval = None
    self._uneven_confidence_interval = None
    self._freeze()

  @property
  def value(self) -> float:
    return self._value

  @value.setter
  def value(self, value: float):
    if value is None:
      del self.value
      return
    if not isinstance(value, float):
      raise TypeError('value must be of type float')
    self._value = value

  @property
  def confidence_interval(self) -> float:
    r"""
    Note, while we call this the 'confidence interval' - the value we store
    here is actually the 'confidence radius', it should always be displayed
    as a +- value.
    """
    return self._confidence_interval or 0.0

  @confidence_interval.setter
  def confidence_interval(self, confidence_interval: Optional[float]):
    if confidence_interval is None:
      del self.confidence_interval
      return
    if not isinstance(confidence_interval, float):
      raise TypeError('confidence_interval must be of type float')
    self._confidence_interval = confidence_interval

  @property
  def uneven_confidence_interval(self) -> Optional['UnevenConfidenceInterval']:
    r"""
    For asymmetric confidence intervals in which the +/- values differ
    If set, prioritized over confidence_interval (if both are set)
    """
    return self._uneven_confidence_interval or None

  @uneven_confidence_interval.setter
  def uneven_confidence_interval(self, uneven_confidence_interval: Optional[Optional['UnevenConfidenceInterval']]):
    if uneven_confidence_interval is None:
      del self.uneven_confidence_interval
      return
    if not isinstance(uneven_confidence_interval, UnevenConfidenceInterval):
      raise TypeError('uneven_confidence_interval must be of type UnevenConfidenceInterval')
    self._uneven_confidence_interval = uneven_confidence_interval


class UnevenConfidenceInterval(KaggleObject):
  r"""
  Attributes:
    plus (float)
    minus (float)
  """

  def __init__(self):
    self._plus = 0.0
    self._minus = 0.0
    self._freeze()

  @property
  def plus(self) -> float:
    return self._plus

  @plus.setter
  def plus(self, plus: float):
    if plus is None:
      del self.plus
      return
    if not isinstance(plus, float):
      raise TypeError('plus must be of type float')
    self._plus = plus

  @property
  def minus(self) -> float:
    return self._minus

  @minus.setter
  def minus(self, minus: float):
    if minus is None:
      del self.minus
      return
    if not isinstance(minus, float):
      raise TypeError('minus must be of type float')
    self._minus = minus


BenchmarkModel._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("licenseId", "license_id", "_license_id", int, 0, PredefinedSerializer()),
  FieldMetadata("defaultVersionId", "default_version_id", "_default_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("version", "version", "_version", BenchmarkModelVersion, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer()),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
]

BenchmarkModelVersion._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("benchmarkModelId", "benchmark_model_id", "_benchmark_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("knowledgeCutoff", "knowledge_cutoff", "_knowledge_cutoff", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("isDefault", "is_default", "_is_default", bool, False, PredefinedSerializer()),
  FieldMetadata("published", "published", "_published", bool, False, PredefinedSerializer()),
  FieldMetadata("allowModelProxy", "allow_model_proxy", "_allow_model_proxy", bool, False, PredefinedSerializer()),
  FieldMetadata("modelProxySlug", "model_proxy_slug", "_model_proxy_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organization", "organization", "_organization", OrganizationCard, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("name", "name", "_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("license", "license", "_license", License, None, KaggleObjectSerializer()),
  FieldMetadata("importanceLevel", "importance_level", "_importance_level", BenchmarkModelImportanceLevel, None, EnumSerializer(), optional=True),
  FieldMetadata("inputModalities", "input_modalities", "_input_modalities", Modality, [], ListSerializer(EnumSerializer())),
  FieldMetadata("outputModalities", "output_modalities", "_output_modalities", Modality, [], ListSerializer(EnumSerializer())),
]

BenchmarkResult._fields = [
  FieldMetadata("numericResult", "numeric_result", "_numeric_result", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("booleanResult", "boolean_result", "_boolean_result", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("customAdditionalResults", "custom_additional_results", "_custom_additional_results", CustomResult, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("numericResultPrivate", "numeric_result_private", "_numeric_result_private", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericResultPublic", "numeric_result_public", "_numeric_result_public", NumericResult, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("evaluationDate", "evaluation_date", "_evaluation_date", datetime, None, DateTimeSerializer(), optional=True),
  FieldMetadata("taskVersionId", "task_version_id", "_task_version_id", int, None, PredefinedSerializer(), optional=True),
]

CustomResult._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

NumericResult._fields = [
  FieldMetadata("value", "value", "_value", float, 0.0, PredefinedSerializer()),
  FieldMetadata("confidenceInterval", "confidence_interval", "_confidence_interval", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("unevenConfidenceInterval", "uneven_confidence_interval", "_uneven_confidence_interval", UnevenConfidenceInterval, None, KaggleObjectSerializer(), optional=True),
]

UnevenConfidenceInterval._fields = [
  FieldMetadata("plus", "plus", "_plus", float, 0.0, PredefinedSerializer()),
  FieldMetadata("minus", "minus", "_minus", float, 0.0, PredefinedSerializer()),
]

