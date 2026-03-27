from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.vote import VoteType
from kagglesdk.competitions.types.competition_user import CompetitionUser
from kagglesdk.datasets.types.dataset_service import DataCreationBasicInfo, DataCreationSettings, ExistingDataInfo, ExistingDirectoryInfo, ExistingFileInfo
from kagglesdk.kaggle_object import *
from kagglesdk.licenses.types.licenses_types import LicenseGroupDto
from kagglesdk.models.types.model_enums import GatingAgreementModelsGatingStatus, GatingAgreementRequestsReviewStatus, GatingAgreementsApprovalMethod, GatingUserConsentsOrderByDirection, GetGatingUserConsentsOrderBy, ListModelsOrderBy, ModelCreateReferrer, ModelFramework
from kagglesdk.models.types.model_types import GatingUserConsent, GatingUserConsentsFilter, ListCompetitionModelInstance, ListCompetitionModelInstancesFilter, ListModelsFilter, Model, ModelCompetition, ModelInstance, ModelInstanceHistoryItem, ModelInstanceVersionReference, ModelReference, Owner, SampleTask
from kagglesdk.search.types.search_enums import PrivacyFilter
from typing import Optional, List, Dict

class AddModelTagRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    tag_id (int)
  """

  def __init__(self):
    self._model_id = 0
    self._tag_id = 0
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
  def tag_id(self) -> int:
    return self._tag_id

  @tag_id.setter
  def tag_id(self, tag_id: int):
    if tag_id is None:
      del self.tag_id
      return
    if not isinstance(tag_id, int):
      raise TypeError('tag_id must be of type int')
    self._tag_id = tag_id


class CopyModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    source_model_instance_version (ModelInstanceVersionReference)
    target_model (ModelReference)
      Note: Authorization for the target_model (models.update permission)
      is enforced by the underlying call to CreateModelInstance*Handler
  """

  def __init__(self):
    self._source_model_instance_version = None
    self._target_model = None
    self._freeze()

  @property
  def source_model_instance_version(self) -> Optional['ModelInstanceVersionReference']:
    return self._source_model_instance_version

  @source_model_instance_version.setter
  def source_model_instance_version(self, source_model_instance_version: Optional['ModelInstanceVersionReference']):
    if source_model_instance_version is None:
      del self.source_model_instance_version
      return
    if not isinstance(source_model_instance_version, ModelInstanceVersionReference):
      raise TypeError('source_model_instance_version must be of type ModelInstanceVersionReference')
    self._source_model_instance_version = source_model_instance_version

  @property
  def target_model(self) -> Optional['ModelReference']:
    r"""
    Note: Authorization for the target_model (models.update permission)
    is enforced by the underlying call to CreateModelInstance*Handler
    """
    return self._target_model

  @target_model.setter
  def target_model(self, target_model: Optional['ModelReference']):
    if target_model is None:
      del self.target_model
      return
    if not isinstance(target_model, ModelReference):
      raise TypeError('target_model must be of type ModelReference')
    self._target_model = target_model


class CreateGatingAgreementRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Currently owner can only be a published organization, which may change in
      the future. Org members or admins are authorized.
    content (str)
    approval_method (GatingAgreementsApprovalMethod)
    privacy_policy (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._content = ""
    self._approval_method = GatingAgreementsApprovalMethod.GATING_AGREEMENT_APPROVAL_METHOD_UNSPECIFIED
    self._privacy_policy = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    r"""
    Currently owner can only be a published organization, which may change in
    the future. Org members or admins are authorized.
    """
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def content(self) -> str:
    return self._content

  @content.setter
  def content(self, content: str):
    if content is None:
      del self.content
      return
    if not isinstance(content, str):
      raise TypeError('content must be of type str')
    self._content = content

  @property
  def approval_method(self) -> 'GatingAgreementsApprovalMethod':
    return self._approval_method

  @approval_method.setter
  def approval_method(self, approval_method: 'GatingAgreementsApprovalMethod'):
    if approval_method is None:
      del self.approval_method
      return
    if not isinstance(approval_method, GatingAgreementsApprovalMethod):
      raise TypeError('approval_method must be of type GatingAgreementsApprovalMethod')
    self._approval_method = approval_method

  @property
  def privacy_policy(self) -> str:
    return self._privacy_policy

  @privacy_policy.setter
  def privacy_policy(self, privacy_policy: str):
    if privacy_policy is None:
      del self.privacy_policy
      return
    if not isinstance(privacy_policy, str):
      raise TypeError('privacy_policy must be of type str')
    self._privacy_policy = privacy_policy


class CreateGatingUserConsentRequest(KaggleObject):
  r"""
  Attributes:
    agreement_id (int)
    request_data (str)
    confirm_meet_age_requirement (bool)
      User confirms they meet the age requirement for model gating.
  """

  def __init__(self):
    self._agreement_id = 0
    self._request_data = None
    self._confirm_meet_age_requirement = False
    self._freeze()

  @property
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id

  @property
  def request_data(self) -> str:
    return self._request_data or ""

  @request_data.setter
  def request_data(self, request_data: Optional[str]):
    if request_data is None:
      del self.request_data
      return
    if not isinstance(request_data, str):
      raise TypeError('request_data must be of type str')
    self._request_data = request_data

  @property
  def confirm_meet_age_requirement(self) -> bool:
    """User confirms they meet the age requirement for model gating."""
    return self._confirm_meet_age_requirement

  @confirm_meet_age_requirement.setter
  def confirm_meet_age_requirement(self, confirm_meet_age_requirement: bool):
    if confirm_meet_age_requirement is None:
      del self.confirm_meet_age_requirement
      return
    if not isinstance(confirm_meet_age_requirement, bool):
      raise TypeError('confirm_meet_age_requirement must be of type bool')
    self._confirm_meet_age_requirement = confirm_meet_age_requirement


class CreateModelDoiRequest(KaggleObject):
  r"""
  Request to create the DOI, (DataCite's Digital Object Identifier
  https://support.datacite.org/docs/api-create-dois)

  Attributes:
    model_id (int)
  """

  def __init__(self):
    self._model_id = 0
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


class CreateModelDoiResponse(KaggleObject):
  r"""
  Attributes:
    doi (str)
  """

  def __init__(self):
    self._doi = ""
    self._freeze()

  @property
  def doi(self) -> str:
    return self._doi

  @doi.setter
  def doi(self, doi: str):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi


class CreateModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Can be a user or an organization.
    model_slug (str)
    instance (ModelInstance)
    basic_info (DataCreationBasicInfo)
    referrer (ModelCreateReferrer)
    sigstore (bool)
      Model was signed and publsihed on sigstore.
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._instance = None
    self._basic_info = None
    self._referrer = None
    self._sigstore = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """Can be a user or an organization."""
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def instance(self) -> Optional['ModelInstance']:
    return self._instance

  @instance.setter
  def instance(self, instance: Optional['ModelInstance']):
    if instance is None:
      del self.instance
      return
    if not isinstance(instance, ModelInstance):
      raise TypeError('instance must be of type ModelInstance')
    self._instance = instance

  @property
  def basic_info(self) -> Optional['DataCreationBasicInfo']:
    return self._basic_info

  @basic_info.setter
  def basic_info(self, basic_info: Optional['DataCreationBasicInfo']):
    if basic_info is None:
      del self.basic_info
      return
    if not isinstance(basic_info, DataCreationBasicInfo):
      raise TypeError('basic_info must be of type DataCreationBasicInfo')
    self._basic_info = basic_info

  @property
  def referrer(self) -> 'ModelCreateReferrer':
    return self._referrer or ModelCreateReferrer.MODEL_CREATE_REFERRER_UNSPECIFIED

  @referrer.setter
  def referrer(self, referrer: Optional['ModelCreateReferrer']):
    if referrer is None:
      del self.referrer
      return
    if not isinstance(referrer, ModelCreateReferrer):
      raise TypeError('referrer must be of type ModelCreateReferrer')
    self._referrer = referrer

  @property
  def sigstore(self) -> bool:
    """Model was signed and publsihed on sigstore."""
    return self._sigstore or False

  @sigstore.setter
  def sigstore(self, sigstore: Optional[bool]):
    if sigstore is None:
      del self.sigstore
      return
    if not isinstance(sigstore, bool):
      raise TypeError('sigstore must be of type bool')
    self._sigstore = sigstore


class CreateModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Can be a user or an organization.
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    basic_info (DataCreationBasicInfo)
    version_notes (str)
    existing_directories (ExistingDirectoryInfo)
      For DatabundleVersionType: Fileset
    existing_files (ExistingFileInfo)
    referrer (ModelCreateReferrer)
    sigstore (bool)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._basic_info = None
    self._version_notes = ""
    self._existing_directories = []
    self._existing_files = []
    self._referrer = None
    self._sigstore = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """Can be a user or an organization."""
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

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
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def basic_info(self) -> Optional['DataCreationBasicInfo']:
    return self._basic_info

  @basic_info.setter
  def basic_info(self, basic_info: Optional['DataCreationBasicInfo']):
    if basic_info is None:
      del self.basic_info
      return
    if not isinstance(basic_info, DataCreationBasicInfo):
      raise TypeError('basic_info must be of type DataCreationBasicInfo')
    self._basic_info = basic_info

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
  def referrer(self) -> 'ModelCreateReferrer':
    return self._referrer or ModelCreateReferrer.MODEL_CREATE_REFERRER_UNSPECIFIED

  @referrer.setter
  def referrer(self, referrer: Optional['ModelCreateReferrer']):
    if referrer is None:
      del self.referrer
      return
    if not isinstance(referrer, ModelCreateReferrer):
      raise TypeError('referrer must be of type ModelCreateReferrer')
    self._referrer = referrer

  @property
  def existing_directories(self) -> Optional[List[Optional['ExistingDirectoryInfo']]]:
    """For DatabundleVersionType: Fileset"""
    return self._existing_directories

  @existing_directories.setter
  def existing_directories(self, existing_directories: Optional[List[Optional['ExistingDirectoryInfo']]]):
    if existing_directories is None:
      del self.existing_directories
      return
    if not isinstance(existing_directories, list):
      raise TypeError('existing_directories must be of type list')
    if not all([isinstance(t, ExistingDirectoryInfo) for t in existing_directories]):
      raise TypeError('existing_directories must contain only items of type ExistingDirectoryInfo')
    self._existing_directories = existing_directories

  @property
  def existing_files(self) -> Optional[List[Optional['ExistingFileInfo']]]:
    return self._existing_files

  @existing_files.setter
  def existing_files(self, existing_files: Optional[List[Optional['ExistingFileInfo']]]):
    if existing_files is None:
      del self.existing_files
      return
    if not isinstance(existing_files, list):
      raise TypeError('existing_files must be of type list')
    if not all([isinstance(t, ExistingFileInfo) for t in existing_files]):
      raise TypeError('existing_files must contain only items of type ExistingFileInfo')
    self._existing_files = existing_files

  @property
  def sigstore(self) -> bool:
    return self._sigstore or False

  @sigstore.setter
  def sigstore(self, sigstore: Optional[bool]):
    if sigstore is None:
      del self.sigstore
      return
    if not isinstance(sigstore, bool):
      raise TypeError('sigstore must be of type bool')
    self._sigstore = sigstore


class CreateModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Can be a user or an organization.
    model (Model)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """Can be a user or an organization."""
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model(self) -> Optional['Model']:
    return self._model

  @model.setter
  def model(self, model: Optional['Model']):
    if model is None:
      del self.model
      return
    if not isinstance(model, Model):
      raise TypeError('model must be of type Model')
    self._model = model


class DeleteModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_id (int)
  """

  def __init__(self):
    self._model_instance_id = 0
    self._freeze()

  @property
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id


class DeleteModelInstanceResponse(KaggleObject):
  r"""
  """

  pass

class DeleteModelInstanceVersionRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_version_id (int)
  """

  def __init__(self):
    self._model_instance_version_id = 0
    self._freeze()

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


class DeleteModelInstanceVersionResponse(KaggleObject):
  r"""
  """

  pass

class DeleteModelRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
  """

  def __init__(self):
    self._model_id = 0
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


class DeleteModelResponse(KaggleObject):
  r"""
  """

  pass

class GetDeletedModelRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
  """

  def __init__(self):
    self._id = 0
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id


class GetDeletedModelResponse(KaggleObject):
  r"""
  Attributes:
    id (int)
    doi (str)
  """

  def __init__(self):
    self._id = 0
    self._doi = None
    self._freeze()

  @property
  def id(self) -> int:
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
  def doi(self) -> str:
    return self._doi or ""

  @doi.setter
  def doi(self, doi: Optional[str]):
    if doi is None:
      del self.doi
      return
    if not isinstance(doi, str):
      raise TypeError('doi must be of type str')
    self._doi = doi


class GetGatingUserConsentsRequest(KaggleObject):
  r"""
  Attributes:
    agreement_id (int)
    page_size (int)
    page_token (str)
    skip (int)
    filter (GatingUserConsentsFilter)
      Null filter means that filter is not on, so ALL UserConsents get returned
    read_mask (FieldMask)
    order_by (GetGatingUserConsentsOrderBy)
    order_by_direction (GatingUserConsentsOrderByDirection)
  """

  def __init__(self):
    self._agreement_id = 0
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._filter = None
    self._read_mask = None
    self._order_by = GetGatingUserConsentsOrderBy.GET_GATING_USER_CONSENTS_ORDER_BY_REQUEST_TIME
    self._order_by_direction = GatingUserConsentsOrderByDirection.GATING_USER_CONSENTS_ORDER_BY_DIRECTION_ASC
    self._freeze()

  @property
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id

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
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def skip(self) -> int:
    return self._skip or 0

  @skip.setter
  def skip(self, skip: Optional[int]):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def filter(self) -> Optional['GatingUserConsentsFilter']:
    """Null filter means that filter is not on, so ALL UserConsents get returned"""
    return self._filter or None

  @filter.setter
  def filter(self, filter: Optional[Optional['GatingUserConsentsFilter']]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, GatingUserConsentsFilter):
      raise TypeError('filter must be of type GatingUserConsentsFilter')
    self._filter = filter

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask

  @property
  def order_by(self) -> 'GetGatingUserConsentsOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'GetGatingUserConsentsOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, GetGatingUserConsentsOrderBy):
      raise TypeError('order_by must be of type GetGatingUserConsentsOrderBy')
    self._order_by = order_by

  @property
  def order_by_direction(self) -> 'GatingUserConsentsOrderByDirection':
    return self._order_by_direction

  @order_by_direction.setter
  def order_by_direction(self, order_by_direction: 'GatingUserConsentsOrderByDirection'):
    if order_by_direction is None:
      del self.order_by_direction
      return
    if not isinstance(order_by_direction, GatingUserConsentsOrderByDirection):
      raise TypeError('order_by_direction must be of type GatingUserConsentsOrderByDirection')
    self._order_by_direction = order_by_direction


class GetGatingUserConsentsResponse(KaggleObject):
  r"""
  Attributes:
    user_consents (GatingUserConsent)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._user_consents = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def user_consents(self) -> Optional[List[Optional['GatingUserConsent']]]:
    return self._user_consents

  @user_consents.setter
  def user_consents(self, user_consents: Optional[List[Optional['GatingUserConsent']]]):
    if user_consents is None:
      del self.user_consents
      return
    if not isinstance(user_consents, list):
      raise TypeError('user_consents must be of type list')
    if not all([isinstance(t, GatingUserConsent) for t in user_consents]):
      raise TypeError('user_consents must contain only items of type GatingUserConsent')
    self._user_consents = user_consents

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size

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


class GetKernelOutputModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    kernel_id (int)
  """

  def __init__(self):
    self._kernel_id = 0
    self._freeze()

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


class GetModelByIdRequest(KaggleObject):
  r"""
  Attributes:
    id (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._id = 0
    self._read_mask = None
    self._freeze()

  @property
  def id(self) -> int:
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
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetModelGatingRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug


class GetModelInstanceHistoryRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_id (int)
    count (int)
  """

  def __init__(self):
    self._model_instance_id = 0
    self._count = 0
    self._freeze()

  @property
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id

  @property
  def count(self) -> int:
    return self._count

  @count.setter
  def count(self, count: int):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count


class GetModelInstanceHistoryResponse(KaggleObject):
  r"""
  Attributes:
    items (ModelInstanceHistoryItem)
    total_items (int)
  """

  def __init__(self):
    self._items = []
    self._total_items = 0
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['ModelInstanceHistoryItem']]]:
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['ModelInstanceHistoryItem']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, ModelInstanceHistoryItem) for t in items]):
      raise TypeError('items must contain only items of type ModelInstanceHistoryItem')
    self._items = items

  @property
  def total_items(self) -> int:
    return self._total_items

  @total_items.setter
  def total_items(self, total_items: int):
    if total_items is None:
      del self.total_items
      return
    if not isinstance(total_items, int):
      raise TypeError('total_items must be of type int')
    self._total_items = total_items


class GetModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    source_url (str)
    model_instance_version_id (int)
    model_instance_version_ref (ModelInstanceVersionReference)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._source_url = None
    self._model_instance_version_id = None
    self._model_instance_version_ref = None
    self._read_mask = None
    self._freeze()

  @property
  def source_url(self) -> str:
    return self._source_url or ""

  @source_url.setter
  def source_url(self, source_url: str):
    if source_url is None:
      del self.source_url
      return
    if not isinstance(source_url, str):
      raise TypeError('source_url must be of type str')
    del self.model_instance_version_id
    del self.model_instance_version_ref
    self._source_url = source_url

  @property
  def model_instance_version_id(self) -> int:
    return self._model_instance_version_id or 0

  @model_instance_version_id.setter
  def model_instance_version_id(self, model_instance_version_id: int):
    if model_instance_version_id is None:
      del self.model_instance_version_id
      return
    if not isinstance(model_instance_version_id, int):
      raise TypeError('model_instance_version_id must be of type int')
    del self.source_url
    del self.model_instance_version_ref
    self._model_instance_version_id = model_instance_version_id

  @property
  def model_instance_version_ref(self) -> Optional['ModelInstanceVersionReference']:
    return self._model_instance_version_ref or None

  @model_instance_version_ref.setter
  def model_instance_version_ref(self, model_instance_version_ref: Optional['ModelInstanceVersionReference']):
    if model_instance_version_ref is None:
      del self.model_instance_version_ref
      return
    if not isinstance(model_instance_version_ref, ModelInstanceVersionReference):
      raise TypeError('model_instance_version_ref must be of type ModelInstanceVersionReference')
    del self.source_url
    del self.model_instance_version_id
    self._model_instance_version_ref = model_instance_version_ref

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class GetModelInstanceUploaderConfigRequest(KaggleObject):
  r"""
  Attributes:
    current_model_instance_version_id (int)
      Id of the current model instance version used to populate existing
      files/directories
  """

  def __init__(self):
    self._current_model_instance_version_id = 0
    self._freeze()

  @property
  def current_model_instance_version_id(self) -> int:
    r"""
    Id of the current model instance version used to populate existing
    files/directories
    """
    return self._current_model_instance_version_id

  @current_model_instance_version_id.setter
  def current_model_instance_version_id(self, current_model_instance_version_id: int):
    if current_model_instance_version_id is None:
      del self.current_model_instance_version_id
      return
    if not isinstance(current_model_instance_version_id, int):
      raise TypeError('current_model_instance_version_id must be of type int')
    self._current_model_instance_version_id = current_model_instance_version_id


class GetModelInstanceVersionKernelUsageRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_version_id (int)
    model_mount_slug (str)
      When two models with the same slug are attached to the same notebook, a
      suffix is added to the model slug to prevent clashes.
  """

  def __init__(self):
    self._model_instance_version_id = 0
    self._model_mount_slug = ""
    self._freeze()

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
  def model_mount_slug(self) -> str:
    r"""
    When two models with the same slug are attached to the same notebook, a
    suffix is added to the model slug to prevent clashes.
    """
    return self._model_mount_slug

  @model_mount_slug.setter
  def model_mount_slug(self, model_mount_slug: str):
    if model_mount_slug is None:
      del self.model_mount_slug
      return
    if not isinstance(model_mount_slug, str):
      raise TypeError('model_mount_slug must be of type str')
    self._model_mount_slug = model_mount_slug


class GetModelInstanceVersionKernelUsageResponse(KaggleObject):
  r"""
  Attributes:
    rendered_usage (str)
  """

  def __init__(self):
    self._rendered_usage = ""
    self._freeze()

  @property
  def rendered_usage(self) -> str:
    return self._rendered_usage

  @rendered_usage.setter
  def rendered_usage(self, rendered_usage: str):
    if rendered_usage is None:
      del self.rendered_usage
      return
    if not isinstance(rendered_usage, str):
      raise TypeError('rendered_usage must be of type str')
    self._rendered_usage = rendered_usage


class GetModelLimitsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
    organization_id (int)
    exclude_model_instance_version_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._organization_id = None
    self._exclude_model_instance_version_id = None
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def organization_id(self) -> int:
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
  def exclude_model_instance_version_id(self) -> int:
    return self._exclude_model_instance_version_id or 0

  @exclude_model_instance_version_id.setter
  def exclude_model_instance_version_id(self, exclude_model_instance_version_id: Optional[int]):
    if exclude_model_instance_version_id is None:
      del self.exclude_model_instance_version_id
      return
    if not isinstance(exclude_model_instance_version_id, int):
      raise TypeError('exclude_model_instance_version_id must be of type int')
    self._exclude_model_instance_version_id = exclude_model_instance_version_id


class GetModelRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      For now, Models will only be accessed by {owner_slug}/{model_slug}
      In the future, these may become optional when we support a hash_link
    model_slug (str)
    framework (ModelFramework)
      framework, instance_slug, and instance_version_number are optional params.
      They must be used in tandem to target a specific instance version. Doing so
      may result in non-latest versions of other Model.instances because the
      integrity of the returned model card (description, etc.) should be accurate
      across all returned Model.instances.
    instance_slug (str)
    read_mask (FieldMask)
    instance_version_number (int)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = None
    self._instance_slug = None
    self._read_mask = None
    self._instance_version_number = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    r"""
    For now, Models will only be accessed by {owner_slug}/{model_slug}
    In the future, these may become optional when we support a hash_link
    """
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask

  @property
  def framework(self) -> 'ModelFramework':
    r"""
    framework, instance_slug, and instance_version_number are optional params.
    They must be used in tandem to target a specific instance version. Doing so
    may result in non-latest versions of other Model.instances because the
    integrity of the returned model card (description, etc.) should be accurate
    across all returned Model.instances.
    """
    return self._framework or ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED

  @framework.setter
  def framework(self, framework: Optional['ModelFramework']):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def instance_slug(self) -> str:
    return self._instance_slug or ""

  @instance_slug.setter
  def instance_slug(self, instance_slug: Optional[str]):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def instance_version_number(self) -> int:
    return self._instance_version_number or 0

  @instance_version_number.setter
  def instance_version_number(self, instance_version_number: Optional[int]):
    if instance_version_number is None:
      del self.instance_version_number
      return
    if not isinstance(instance_version_number, int):
      raise TypeError('instance_version_number must be of type int')
    self._instance_version_number = instance_version_number


class GetUserGatingConsentDataRequest(KaggleObject):
  r"""
  Attributes:
    agreement_id (int)
  """

  def __init__(self):
    self._agreement_id = 0
    self._freeze()

  @property
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id


class GetUserGatingConsentDataResponse(KaggleObject):
  r"""
  Attributes:
    consent_data_json (str)
  """

  def __init__(self):
    self._consent_data_json = None
    self._freeze()

  @property
  def consent_data_json(self) -> str:
    return self._consent_data_json or ""

  @consent_data_json.setter
  def consent_data_json(self, consent_data_json: Optional[str]):
    if consent_data_json is None:
      del self.consent_data_json
      return
    if not isinstance(consent_data_json, str):
      raise TypeError('consent_data_json must be of type str')
    self._consent_data_json = consent_data_json


class GetUserModelCountsRequest(KaggleObject):
  r"""
  Attributes:
    user_id (int)
  """

  def __init__(self):
    self._user_id = 0
    self._freeze()

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class GetUserModelCountsResponse(KaggleObject):
  r"""
  Attributes:
    model_count (int)
      Number of public models made by this user
    total_model_votes (int)
      The total score for this user's public models
    model_notebook_count (int)
      The number of notebooks created on this user's public models
    model_competition_count (int)
      The number of competitions using this user's public models
    total_model_views (int)
      The number of views on this user's public models
  """

  def __init__(self):
    self._model_count = 0
    self._total_model_votes = 0
    self._model_notebook_count = 0
    self._model_competition_count = 0
    self._total_model_views = 0
    self._freeze()

  @property
  def model_count(self) -> int:
    """Number of public models made by this user"""
    return self._model_count

  @model_count.setter
  def model_count(self, model_count: int):
    if model_count is None:
      del self.model_count
      return
    if not isinstance(model_count, int):
      raise TypeError('model_count must be of type int')
    self._model_count = model_count

  @property
  def total_model_votes(self) -> int:
    """The total score for this user's public models"""
    return self._total_model_votes

  @total_model_votes.setter
  def total_model_votes(self, total_model_votes: int):
    if total_model_votes is None:
      del self.total_model_votes
      return
    if not isinstance(total_model_votes, int):
      raise TypeError('total_model_votes must be of type int')
    self._total_model_votes = total_model_votes

  @property
  def model_notebook_count(self) -> int:
    """The number of notebooks created on this user's public models"""
    return self._model_notebook_count

  @model_notebook_count.setter
  def model_notebook_count(self, model_notebook_count: int):
    if model_notebook_count is None:
      del self.model_notebook_count
      return
    if not isinstance(model_notebook_count, int):
      raise TypeError('model_notebook_count must be of type int')
    self._model_notebook_count = model_notebook_count

  @property
  def model_competition_count(self) -> int:
    """The number of competitions using this user's public models"""
    return self._model_competition_count

  @model_competition_count.setter
  def model_competition_count(self, model_competition_count: int):
    if model_competition_count is None:
      del self.model_competition_count
      return
    if not isinstance(model_competition_count, int):
      raise TypeError('model_competition_count must be of type int')
    self._model_competition_count = model_competition_count

  @property
  def total_model_views(self) -> int:
    """The number of views on this user's public models"""
    return self._total_model_views

  @total_model_views.setter
  def total_model_views(self, total_model_views: int):
    if total_model_views is None:
      del self.total_model_views
      return
    if not isinstance(total_model_views, int):
      raise TypeError('total_model_views must be of type int')
    self._total_model_views = total_model_views


class IncrementModelViewCountRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
  """

  def __init__(self):
    self._model_id = 0
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


class ListCompetitionModelInstancesRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    page_size (int)
    page_token (str)
    filter (ListCompetitionModelInstancesFilter)
  """

  def __init__(self):
    self._competition_id = 0
    self._page_size = None
    self._page_token = None
    self._filter = None
    self._freeze()

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
  def page_size(self) -> int:
    return self._page_size or 0

  @page_size.setter
  def page_size(self, page_size: Optional[int]):
    if page_size is None:
      del self.page_size
      return
    if not isinstance(page_size, int):
      raise TypeError('page_size must be of type int')
    self._page_size = page_size

  @property
  def page_token(self) -> str:
    return self._page_token or ""

  @page_token.setter
  def page_token(self, page_token: Optional[str]):
    if page_token is None:
      del self.page_token
      return
    if not isinstance(page_token, str):
      raise TypeError('page_token must be of type str')
    self._page_token = page_token

  @property
  def filter(self) -> Optional['ListCompetitionModelInstancesFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListCompetitionModelInstancesFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListCompetitionModelInstancesFilter):
      raise TypeError('filter must be of type ListCompetitionModelInstancesFilter')
    self._filter = filter


class ListCompetitionModelInstancesResponse(KaggleObject):
  r"""
  Attributes:
    pinned_model_instances (ListCompetitionModelInstance)
    unpinned_model_instances (ListCompetitionModelInstance)
    next_page_token (str)
  """

  def __init__(self):
    self._pinned_model_instances = []
    self._unpinned_model_instances = []
    self._next_page_token = ""
    self._freeze()

  @property
  def pinned_model_instances(self) -> Optional[List[Optional['ListCompetitionModelInstance']]]:
    return self._pinned_model_instances

  @pinned_model_instances.setter
  def pinned_model_instances(self, pinned_model_instances: Optional[List[Optional['ListCompetitionModelInstance']]]):
    if pinned_model_instances is None:
      del self.pinned_model_instances
      return
    if not isinstance(pinned_model_instances, list):
      raise TypeError('pinned_model_instances must be of type list')
    if not all([isinstance(t, ListCompetitionModelInstance) for t in pinned_model_instances]):
      raise TypeError('pinned_model_instances must contain only items of type ListCompetitionModelInstance')
    self._pinned_model_instances = pinned_model_instances

  @property
  def unpinned_model_instances(self) -> Optional[List[Optional['ListCompetitionModelInstance']]]:
    return self._unpinned_model_instances

  @unpinned_model_instances.setter
  def unpinned_model_instances(self, unpinned_model_instances: Optional[List[Optional['ListCompetitionModelInstance']]]):
    if unpinned_model_instances is None:
      del self.unpinned_model_instances
      return
    if not isinstance(unpinned_model_instances, list):
      raise TypeError('unpinned_model_instances must be of type list')
    if not all([isinstance(t, ListCompetitionModelInstance) for t in unpinned_model_instances]):
      raise TypeError('unpinned_model_instances must contain only items of type ListCompetitionModelInstance')
    self._unpinned_model_instances = unpinned_model_instances

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


class ListModelCompetitionsRequest(KaggleObject):
  r"""
  Wrapper for request since it is identical to the ListCompetitionsRequest

  Attributes:
    model_id (int)
      Defines the query to perform.
    page_size (int)
      Page size and Page token to be forwarded to the ListCompetitionsRequest
    page_token (str)
  """

  def __init__(self):
    self._model_id = 0
    self._page_size = 0
    self._page_token = ""
    self._freeze()

  @property
  def model_id(self) -> int:
    """Defines the query to perform."""
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
  def page_size(self) -> int:
    """Page size and Page token to be forwarded to the ListCompetitionsRequest"""
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


class ListModelCompetitionsResponse(KaggleObject):
  r"""
  Attributes:
    model_competitions (ModelCompetition)
    next_page_token (str)
    thumbnail_image_urls (str)
      Signed thumbnail image URLs for the competitions returned on the response.
      Generated in bulk for performance.
    competition_users (CompetitionUser)
      Maps each competitionId from model_competitions to the current user's
      context on that competition
      TODO(b/307284127): Migrate above team info to the CompetitionUser message
    total_results (int)
  """

  def __init__(self):
    self._model_competitions = []
    self._next_page_token = ""
    self._thumbnail_image_urls = {}
    self._competition_users = {}
    self._total_results = 0
    self._freeze()

  @property
  def model_competitions(self) -> Optional[List[Optional['ModelCompetition']]]:
    return self._model_competitions

  @model_competitions.setter
  def model_competitions(self, model_competitions: Optional[List[Optional['ModelCompetition']]]):
    if model_competitions is None:
      del self.model_competitions
      return
    if not isinstance(model_competitions, list):
      raise TypeError('model_competitions must be of type list')
    if not all([isinstance(t, ModelCompetition) for t in model_competitions]):
      raise TypeError('model_competitions must contain only items of type ModelCompetition')
    self._model_competitions = model_competitions

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
  def thumbnail_image_urls(self) -> Optional[Dict[int, str]]:
    r"""
    Signed thumbnail image URLs for the competitions returned on the response.
    Generated in bulk for performance.
    """
    return self._thumbnail_image_urls

  @thumbnail_image_urls.setter
  def thumbnail_image_urls(self, thumbnail_image_urls: Optional[Dict[int, str]]):
    if thumbnail_image_urls is None:
      del self.thumbnail_image_urls
      return
    if not isinstance(thumbnail_image_urls, dict):
      raise TypeError('thumbnail_image_urls must be of type dict')
    if not all([isinstance(v, str) for k, v in thumbnail_image_urls]):
      raise TypeError('thumbnail_image_urls must contain only items of type str')
    self._thumbnail_image_urls = thumbnail_image_urls

  @property
  def competition_users(self) -> Optional[Dict[int, Optional['CompetitionUser']]]:
    r"""
    Maps each competitionId from model_competitions to the current user's
    context on that competition
    TODO(b/307284127): Migrate above team info to the CompetitionUser message
    """
    return self._competition_users

  @competition_users.setter
  def competition_users(self, competition_users: Optional[Dict[int, Optional['CompetitionUser']]]):
    if competition_users is None:
      del self.competition_users
      return
    if not isinstance(competition_users, dict):
      raise TypeError('competition_users must be of type dict')
    if not all([isinstance(v, CompetitionUser) for k, v in competition_users]):
      raise TypeError('competition_users must contain only items of type CompetitionUser')
    self._competition_users = competition_users

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


class ListModelInstancesByIdsRequest(KaggleObject):
  r"""
  Attributes:
    model_instance_ids (int)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._model_instance_ids = []
    self._read_mask = None
    self._freeze()

  @property
  def model_instance_ids(self) -> Optional[List[int]]:
    return self._model_instance_ids

  @model_instance_ids.setter
  def model_instance_ids(self, model_instance_ids: Optional[List[int]]):
    if model_instance_ids is None:
      del self.model_instance_ids
      return
    if not isinstance(model_instance_ids, list):
      raise TypeError('model_instance_ids must be of type list')
    if not all([isinstance(t, int) for t in model_instance_ids]):
      raise TypeError('model_instance_ids must contain only items of type int')
    self._model_instance_ids = model_instance_ids

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListModelInstancesRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
      List latest version for each instance. For model editors, this will include
      deleted and errored versions. For normal users, this will only include
      current versions.
    framework (ModelFramework)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._model_id = 0
    self._framework = None
    self._read_mask = None
    self._freeze()

  @property
  def model_id(self) -> int:
    r"""
    List latest version for each instance. For model editors, this will include
    deleted and errored versions. For normal users, this will only include
    current versions.
    """
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
  def framework(self) -> 'ModelFramework':
    return self._framework or ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED

  @framework.setter
  def framework(self, framework: Optional['ModelFramework']):
    if framework is None:
      del self.framework
      return
    if not isinstance(framework, ModelFramework):
      raise TypeError('framework must be of type ModelFramework')
    self._framework = framework

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListModelInstancesResponse(KaggleObject):
  r"""
  Attributes:
    instances (ModelInstance)
  """

  def __init__(self):
    self._instances = []
    self._freeze()

  @property
  def instances(self) -> Optional[List[Optional['ModelInstance']]]:
    return self._instances

  @instances.setter
  def instances(self, instances: Optional[List[Optional['ModelInstance']]]):
    if instances is None:
      del self.instances
      return
    if not isinstance(instances, list):
      raise TypeError('instances must be of type list')
    if not all([isinstance(t, ModelInstance) for t in instances]):
      raise TypeError('instances must contain only items of type ModelInstance')
    self._instances = instances


class ListModelInstanceVersionsRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    model_instance_version_ids (int)
  """

  def __init__(self):
    self._model_id = None
    self._model_instance_version_ids = []
    self._freeze()

  @property
  def model_id(self) -> int:
    return self._model_id or 0

  @model_id.setter
  def model_id(self, model_id: Optional[int]):
    if model_id is None:
      del self.model_id
      return
    if not isinstance(model_id, int):
      raise TypeError('model_id must be of type int')
    self._model_id = model_id

  @property
  def model_instance_version_ids(self) -> Optional[List[int]]:
    return self._model_instance_version_ids

  @model_instance_version_ids.setter
  def model_instance_version_ids(self, model_instance_version_ids: Optional[List[int]]):
    if model_instance_version_ids is None:
      del self.model_instance_version_ids
      return
    if not isinstance(model_instance_version_ids, list):
      raise TypeError('model_instance_version_ids must be of type list')
    if not all([isinstance(t, int) for t in model_instance_version_ids]):
      raise TypeError('model_instance_version_ids must contain only items of type int')
    self._model_instance_version_ids = model_instance_version_ids


class ListModelLicenseGroupsRequest(KaggleObject):
  r"""
  """

  pass

class ListModelLicenseGroupsResponse(KaggleObject):
  r"""
  Attributes:
    license_groups (LicenseGroupDto)
  """

  def __init__(self):
    self._license_groups = []
    self._freeze()

  @property
  def license_groups(self) -> Optional[List[Optional['LicenseGroupDto']]]:
    return self._license_groups

  @license_groups.setter
  def license_groups(self, license_groups: Optional[List[Optional['LicenseGroupDto']]]):
    if license_groups is None:
      del self.license_groups
      return
    if not isinstance(license_groups, list):
      raise TypeError('license_groups must be of type list')
    if not all([isinstance(t, LicenseGroupDto) for t in license_groups]):
      raise TypeError('license_groups must contain only items of type LicenseGroupDto')
    self._license_groups = license_groups


class ListModelsRequest(KaggleObject):
  r"""
  Attributes:
    filter (ListModelsFilter)
    order_by (ListModelsOrderBy)
    page_size (int)
    page_token (str)
    read_mask (FieldMask)
    skip (int)
    privacy_filter (PrivacyFilter)
  """

  def __init__(self):
    self._filter = None
    self._order_by = ListModelsOrderBy.LIST_MODELS_ORDER_BY_UNSPECIFIED
    self._page_size = 0
    self._page_token = ""
    self._read_mask = None
    self._skip = 0
    self._privacy_filter = None
    self._freeze()

  @property
  def filter(self) -> Optional['ListModelsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListModelsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListModelsFilter):
      raise TypeError('filter must be of type ListModelsFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListModelsOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListModelsOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListModelsOrderBy):
      raise TypeError('order_by must be of type ListModelsOrderBy')
    self._order_by = order_by

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
  def privacy_filter(self) -> 'PrivacyFilter':
    return self._privacy_filter or PrivacyFilter.ALL

  @privacy_filter.setter
  def privacy_filter(self, privacy_filter: Optional['PrivacyFilter']):
    if privacy_filter is None:
      del self.privacy_filter
      return
    if not isinstance(privacy_filter, PrivacyFilter):
      raise TypeError('privacy_filter must be of type PrivacyFilter')
    self._privacy_filter = privacy_filter

  @property
  def read_mask(self) -> FieldMask:
    return self._read_mask

  @read_mask.setter
  def read_mask(self, read_mask: FieldMask):
    if read_mask is None:
      del self.read_mask
      return
    if not isinstance(read_mask, FieldMask):
      raise TypeError('read_mask must be of type FieldMask')
    self._read_mask = read_mask


class ListModelsResponse(KaggleObject):
  r"""
  Attributes:
    models (Model)
    next_page_token (str)
    total_results (int)
    total_model_instances (int)
  """

  def __init__(self):
    self._models = []
    self._next_page_token = ""
    self._total_results = 0
    self._total_model_instances = 0
    self._freeze()

  @property
  def models(self) -> Optional[List[Optional['Model']]]:
    return self._models

  @models.setter
  def models(self, models: Optional[List[Optional['Model']]]):
    if models is None:
      del self.models
      return
    if not isinstance(models, list):
      raise TypeError('models must be of type list')
    if not all([isinstance(t, Model) for t in models]):
      raise TypeError('models must contain only items of type Model')
    self._models = models

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
  def total_model_instances(self) -> int:
    return self._total_model_instances

  @total_model_instances.setter
  def total_model_instances(self, total_model_instances: int):
    if total_model_instances is None:
      del self.total_model_instances
      return
    if not isinstance(total_model_instances, int):
      raise TypeError('total_model_instances must be of type int')
    self._total_model_instances = total_model_instances


class ListOwnersRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    filter (str)
  """

  def __init__(self):
    self._page_size = 0
    self._filter = None
    self._freeze()

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
  def filter(self) -> str:
    return self._filter or ""

  @filter.setter
  def filter(self, filter: Optional[str]):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, str):
      raise TypeError('filter must be of type str')
    self._filter = filter


class ListOwnersResponse(KaggleObject):
  r"""
  Attributes:
    owners (Owner)
    total_size (int)
  """

  def __init__(self):
    self._owners = []
    self._total_size = 0
    self._freeze()

  @property
  def owners(self) -> Optional[List[Optional['Owner']]]:
    return self._owners

  @owners.setter
  def owners(self, owners: Optional[List[Optional['Owner']]]):
    if owners is None:
      del self.owners
      return
    if not isinstance(owners, list):
      raise TypeError('owners must be of type list')
    if not all([isinstance(t, Owner) for t in owners]):
      raise TypeError('owners must contain only items of type Owner')
    self._owners = owners

  @property
  def total_size(self) -> int:
    return self._total_size

  @total_size.setter
  def total_size(self, total_size: int):
    if total_size is None:
      del self.total_size
      return
    if not isinstance(total_size, int):
      raise TypeError('total_size must be of type int')
    self._total_size = total_size


class ListSampleTasksRequest(KaggleObject):
  r"""
  """

  pass

class ListSampleTasksResponse(KaggleObject):
  r"""
  Attributes:
    tasks (SampleTask)
  """

  def __init__(self):
    self._tasks = []
    self._freeze()

  @property
  def tasks(self) -> Optional[List[Optional['SampleTask']]]:
    return self._tasks

  @tasks.setter
  def tasks(self, tasks: Optional[List[Optional['SampleTask']]]):
    if tasks is None:
      del self.tasks
      return
    if not isinstance(tasks, list):
      raise TypeError('tasks must be of type list')
    if not all([isinstance(t, SampleTask) for t in tasks]):
      raise TypeError('tasks must contain only items of type SampleTask')
    self._tasks = tasks


class ModelUploaderConfig(KaggleObject):
  r"""
  Attributes:
    existing_data (ExistingDataInfo)
  """

  def __init__(self):
    self._existing_data = None
    self._freeze()

  @property
  def existing_data(self) -> Optional['ExistingDataInfo']:
    return self._existing_data

  @existing_data.setter
  def existing_data(self, existing_data: Optional['ExistingDataInfo']):
    if existing_data is None:
      del self.existing_data
      return
    if not isinstance(existing_data, ExistingDataInfo):
      raise TypeError('existing_data must be of type ExistingDataInfo')
    self._existing_data = existing_data


class PinModelInstanceToCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    model_instance_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._model_instance_id = 0
    self._freeze()

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
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id


class PreviewGatingAgreementContentRequest(KaggleObject):
  r"""
  Attributes:
    raw_content (str)
  """

  def __init__(self):
    self._raw_content = ""
    self._freeze()

  @property
  def raw_content(self) -> str:
    return self._raw_content

  @raw_content.setter
  def raw_content(self, raw_content: str):
    if raw_content is None:
      del self.raw_content
      return
    if not isinstance(raw_content, str):
      raise TypeError('raw_content must be of type str')
    self._raw_content = raw_content


class RefreshRemoteModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    framework (ModelFramework)
    instance_slug (str)
    settings (DataCreationSettings)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._framework = ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED
    self._instance_slug = ""
    self._settings = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

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
  def instance_slug(self) -> str:
    return self._instance_slug

  @instance_slug.setter
  def instance_slug(self, instance_slug: str):
    if instance_slug is None:
      del self.instance_slug
      return
    if not isinstance(instance_slug, str):
      raise TypeError('instance_slug must be of type str')
    self._instance_slug = instance_slug

  @property
  def settings(self) -> Optional['DataCreationSettings']:
    return self._settings

  @settings.setter
  def settings(self, settings: Optional['DataCreationSettings']):
    if settings is None:
      del self.settings
      return
    if not isinstance(settings, DataCreationSettings):
      raise TypeError('settings must be of type DataCreationSettings')
    self._settings = settings


class RemoveModelTagRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    tag_id (int)
  """

  def __init__(self):
    self._model_id = 0
    self._tag_id = 0
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
  def tag_id(self) -> int:
    return self._tag_id

  @tag_id.setter
  def tag_id(self, tag_id: int):
    if tag_id is None:
      del self.tag_id
      return
    if not isinstance(tag_id, int):
      raise TypeError('tag_id must be of type int')
    self._tag_id = tag_id


class ReviewGatingUserConsentRequest(KaggleObject):
  r"""
  Attributes:
    agreement_id (int)
    user_id (int)
    review_status (GatingAgreementRequestsReviewStatus)
    expire_user_consent (bool)
    publisher_notes (str)
  """

  def __init__(self):
    self._agreement_id = 0
    self._user_id = 0
    self._review_status = None
    self._expire_user_consent = None
    self._publisher_notes = None
    self._freeze()

  @property
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id

  @property
  def user_id(self) -> int:
    return self._user_id

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id

  @property
  def review_status(self) -> 'GatingAgreementRequestsReviewStatus':
    return self._review_status or GatingAgreementRequestsReviewStatus.GATING_AGREEMENT_REQUESTS_REVIEW_STATUS_UNSPECIFIED

  @review_status.setter
  def review_status(self, review_status: Optional['GatingAgreementRequestsReviewStatus']):
    if review_status is None:
      del self.review_status
      return
    if not isinstance(review_status, GatingAgreementRequestsReviewStatus):
      raise TypeError('review_status must be of type GatingAgreementRequestsReviewStatus')
    self._review_status = review_status

  @property
  def expire_user_consent(self) -> bool:
    return self._expire_user_consent or False

  @expire_user_consent.setter
  def expire_user_consent(self, expire_user_consent: Optional[bool]):
    if expire_user_consent is None:
      del self.expire_user_consent
      return
    if not isinstance(expire_user_consent, bool):
      raise TypeError('expire_user_consent must be of type bool')
    self._expire_user_consent = expire_user_consent

  @property
  def publisher_notes(self) -> str:
    return self._publisher_notes or ""

  @publisher_notes.setter
  def publisher_notes(self, publisher_notes: Optional[str]):
    if publisher_notes is None:
      del self.publisher_notes
      return
    if not isinstance(publisher_notes, str):
      raise TypeError('publisher_notes must be of type str')
    self._publisher_notes = publisher_notes


class UnpinModelInstanceFromCompetitionRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    model_instance_id (int)
  """

  def __init__(self):
    self._competition_id = 0
    self._model_instance_id = 0
    self._freeze()

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
  def model_instance_id(self) -> int:
    return self._model_instance_id

  @model_instance_id.setter
  def model_instance_id(self, model_instance_id: int):
    if model_instance_id is None:
      del self.model_instance_id
      return
    if not isinstance(model_instance_id, int):
      raise TypeError('model_instance_id must be of type int')
    self._model_instance_id = model_instance_id


class UpdateModelGatingRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
    model_slug (str)
    agreement_id (int)
    gating_status (GatingAgreementModelsGatingStatus)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._agreement_id = 0
    self._gating_status = GatingAgreementModelsGatingStatus.GATING_AGREEMENT_MODELS_GATING_STATUS_UNSPECIFIED
    self._freeze()

  @property
  def owner_slug(self) -> str:
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def agreement_id(self) -> int:
    return self._agreement_id

  @agreement_id.setter
  def agreement_id(self, agreement_id: int):
    if agreement_id is None:
      del self.agreement_id
      return
    if not isinstance(agreement_id, int):
      raise TypeError('agreement_id must be of type int')
    self._agreement_id = agreement_id

  @property
  def gating_status(self) -> 'GatingAgreementModelsGatingStatus':
    return self._gating_status

  @gating_status.setter
  def gating_status(self, gating_status: 'GatingAgreementModelsGatingStatus'):
    if gating_status is None:
      del self.gating_status
      return
    if not isinstance(gating_status, GatingAgreementModelsGatingStatus):
      raise TypeError('gating_status must be of type GatingAgreementModelsGatingStatus')
    self._gating_status = gating_status


class UpdateModelInstanceRequest(KaggleObject):
  r"""
  Attributes:
    owner_slug (str)
      Can be a user or an organization.
    model_slug (str)
    instance (ModelInstance)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._owner_slug = ""
    self._model_slug = ""
    self._instance = None
    self._update_mask = None
    self._freeze()

  @property
  def owner_slug(self) -> str:
    """Can be a user or an organization."""
    return self._owner_slug

  @owner_slug.setter
  def owner_slug(self, owner_slug: str):
    if owner_slug is None:
      del self.owner_slug
      return
    if not isinstance(owner_slug, str):
      raise TypeError('owner_slug must be of type str')
    self._owner_slug = owner_slug

  @property
  def model_slug(self) -> str:
    return self._model_slug

  @model_slug.setter
  def model_slug(self, model_slug: str):
    if model_slug is None:
      del self.model_slug
      return
    if not isinstance(model_slug, str):
      raise TypeError('model_slug must be of type str')
    self._model_slug = model_slug

  @property
  def instance(self) -> Optional['ModelInstance']:
    return self._instance

  @instance.setter
  def instance(self, instance: Optional['ModelInstance']):
    if instance is None:
      del self.instance
      return
    if not isinstance(instance, ModelInstance):
      raise TypeError('instance must be of type ModelInstance')
    self._instance = instance

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class UpdateModelOwnerRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    user_id (int)
    organization_id (int)
  """

  def __init__(self):
    self._model_id = 0
    self._user_id = None
    self._organization_id = None
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
  def user_id(self) -> int:
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: int):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    del self.organization_id
    self._user_id = user_id

  @property
  def organization_id(self) -> int:
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    del self.user_id
    self._organization_id = organization_id


class UpdateModelOwnerResponse(KaggleObject):
  r"""
  Attributes:
    new_url (str)
  """

  def __init__(self):
    self._new_url = ""
    self._freeze()

  @property
  def new_url(self) -> str:
    return self._new_url

  @new_url.setter
  def new_url(self, new_url: str):
    if new_url is None:
      del self.new_url
      return
    if not isinstance(new_url, str):
      raise TypeError('new_url must be of type str')
    self._new_url = new_url


class UpdateModelRequest(KaggleObject):
  r"""
  Attributes:
    model (Model)
    update_mask (FieldMask)
  """

  def __init__(self):
    self._model = None
    self._update_mask = None
    self._freeze()

  @property
  def model(self) -> Optional['Model']:
    return self._model

  @model.setter
  def model(self, model: Optional['Model']):
    if model is None:
      del self.model
      return
    if not isinstance(model, Model):
      raise TypeError('model must be of type Model')
    self._model = model

  @property
  def update_mask(self) -> FieldMask:
    return self._update_mask

  @update_mask.setter
  def update_mask(self, update_mask: FieldMask):
    if update_mask is None:
      del self.update_mask
      return
    if not isinstance(update_mask, FieldMask):
      raise TypeError('update_mask must be of type FieldMask')
    self._update_mask = update_mask


class VoteOnModelRequest(KaggleObject):
  r"""
  Attributes:
    model_id (int)
    vote_type (VoteType)
  """

  def __init__(self):
    self._model_id = 0
    self._vote_type = VoteType.VOTE_TYPE_UNSPECIFIED
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
  def vote_type(self) -> 'VoteType':
    return self._vote_type

  @vote_type.setter
  def vote_type(self, vote_type: 'VoteType'):
    if vote_type is None:
      del self.vote_type
      return
    if not isinstance(vote_type, VoteType):
      raise TypeError('vote_type must be of type VoteType')
    self._vote_type = vote_type


AddModelTagRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

CopyModelInstanceVersionRequest._fields = [
  FieldMetadata("sourceModelInstanceVersion", "source_model_instance_version", "_source_model_instance_version", ModelInstanceVersionReference, None, KaggleObjectSerializer()),
  FieldMetadata("targetModel", "target_model", "_target_model", ModelReference, None, KaggleObjectSerializer()),
]

CreateGatingAgreementRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("content", "content", "_content", str, "", PredefinedSerializer()),
  FieldMetadata("approvalMethod", "approval_method", "_approval_method", GatingAgreementsApprovalMethod, GatingAgreementsApprovalMethod.GATING_AGREEMENT_APPROVAL_METHOD_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("privacyPolicy", "privacy_policy", "_privacy_policy", str, "", PredefinedSerializer()),
]

CreateGatingUserConsentRequest._fields = [
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
  FieldMetadata("requestData", "request_data", "_request_data", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("confirmMeetAgeRequirement", "confirm_meet_age_requirement", "_confirm_meet_age_requirement", bool, False, PredefinedSerializer()),
]

CreateModelDoiRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
]

CreateModelDoiResponse._fields = [
  FieldMetadata("doi", "doi", "_doi", str, "", PredefinedSerializer()),
]

CreateModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instance", "instance", "_instance", ModelInstance, None, KaggleObjectSerializer()),
  FieldMetadata("basicInfo", "basic_info", "_basic_info", DataCreationBasicInfo, None, KaggleObjectSerializer()),
  FieldMetadata("referrer", "referrer", "_referrer", ModelCreateReferrer, None, EnumSerializer(), optional=True),
  FieldMetadata("sigstore", "sigstore", "_sigstore", bool, None, PredefinedSerializer(), optional=True),
]

CreateModelInstanceVersionRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("basicInfo", "basic_info", "_basic_info", DataCreationBasicInfo, None, KaggleObjectSerializer()),
  FieldMetadata("versionNotes", "version_notes", "_version_notes", str, "", PredefinedSerializer()),
  FieldMetadata("existingDirectories", "existing_directories", "_existing_directories", ExistingDirectoryInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("existingFiles", "existing_files", "_existing_files", ExistingFileInfo, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("referrer", "referrer", "_referrer", ModelCreateReferrer, None, EnumSerializer(), optional=True),
  FieldMetadata("sigstore", "sigstore", "_sigstore", bool, None, PredefinedSerializer(), optional=True),
]

CreateModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("model", "model", "_model", Model, None, KaggleObjectSerializer()),
]

DeleteModelInstanceRequest._fields = [
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
]

DeleteModelInstanceResponse._fields = []

DeleteModelInstanceVersionRequest._fields = [
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
]

DeleteModelInstanceVersionResponse._fields = []

DeleteModelRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
]

DeleteModelResponse._fields = []

GetDeletedModelRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
]

GetDeletedModelResponse._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("doi", "doi", "_doi", str, None, PredefinedSerializer(), optional=True),
]

GetGatingUserConsentsRequest._fields = [
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", GatingUserConsentsFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", GetGatingUserConsentsOrderBy, GetGatingUserConsentsOrderBy.GET_GATING_USER_CONSENTS_ORDER_BY_REQUEST_TIME, EnumSerializer()),
  FieldMetadata("orderByDirection", "order_by_direction", "_order_by_direction", GatingUserConsentsOrderByDirection, GatingUserConsentsOrderByDirection.GATING_USER_CONSENTS_ORDER_BY_DIRECTION_ASC, EnumSerializer()),
]

GetGatingUserConsentsResponse._fields = [
  FieldMetadata("userConsents", "user_consents", "_user_consents", GatingUserConsent, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

GetKernelOutputModelInstanceRequest._fields = [
  FieldMetadata("kernelId", "kernel_id", "_kernel_id", int, 0, PredefinedSerializer()),
]

GetModelByIdRequest._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetModelGatingRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
]

GetModelInstanceHistoryRequest._fields = [
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
  FieldMetadata("count", "count", "_count", int, 0, PredefinedSerializer()),
]

GetModelInstanceHistoryResponse._fields = [
  FieldMetadata("items", "items", "_items", ModelInstanceHistoryItem, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalItems", "total_items", "_total_items", int, 0, PredefinedSerializer()),
]

GetModelInstanceRequest._fields = [
  FieldMetadata("sourceUrl", "source_url", "_source_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceVersionRef", "model_instance_version_ref", "_model_instance_version_ref", ModelInstanceVersionReference, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

GetModelInstanceUploaderConfigRequest._fields = [
  FieldMetadata("currentModelInstanceVersionId", "current_model_instance_version_id", "_current_model_instance_version_id", int, 0, PredefinedSerializer()),
]

GetModelInstanceVersionKernelUsageRequest._fields = [
  FieldMetadata("modelInstanceVersionId", "model_instance_version_id", "_model_instance_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelMountSlug", "model_mount_slug", "_model_mount_slug", str, "", PredefinedSerializer()),
]

GetModelInstanceVersionKernelUsageResponse._fields = [
  FieldMetadata("renderedUsage", "rendered_usage", "_rendered_usage", str, "", PredefinedSerializer()),
]

GetModelLimitsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("excludeModelInstanceVersionId", "exclude_model_instance_version_id", "_exclude_model_instance_version_id", int, None, PredefinedSerializer(), optional=True),
]

GetModelRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, None, EnumSerializer(), optional=True),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("instanceVersionNumber", "instance_version_number", "_instance_version_number", int, None, PredefinedSerializer(), optional=True),
]

GetUserGatingConsentDataRequest._fields = [
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
]

GetUserGatingConsentDataResponse._fields = [
  FieldMetadata("consentDataJson", "consent_data_json", "_consent_data_json", str, None, PredefinedSerializer(), optional=True),
]

GetUserModelCountsRequest._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
]

GetUserModelCountsResponse._fields = [
  FieldMetadata("modelCount", "model_count", "_model_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalModelVotes", "total_model_votes", "_total_model_votes", int, 0, PredefinedSerializer()),
  FieldMetadata("modelNotebookCount", "model_notebook_count", "_model_notebook_count", int, 0, PredefinedSerializer()),
  FieldMetadata("modelCompetitionCount", "model_competition_count", "_model_competition_count", int, 0, PredefinedSerializer()),
  FieldMetadata("totalModelViews", "total_model_views", "_total_model_views", int, 0, PredefinedSerializer()),
]

IncrementModelViewCountRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
]

ListCompetitionModelInstancesRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListCompetitionModelInstancesFilter, None, KaggleObjectSerializer()),
]

ListCompetitionModelInstancesResponse._fields = [
  FieldMetadata("pinnedModelInstances", "pinned_model_instances", "_pinned_model_instances", ListCompetitionModelInstance, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("unpinnedModelInstances", "unpinned_model_instances", "_unpinned_model_instances", ListCompetitionModelInstance, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

ListModelCompetitionsRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
]

ListModelCompetitionsResponse._fields = [
  FieldMetadata("modelCompetitions", "model_competitions", "_model_competitions", ModelCompetition, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("thumbnailImageUrls", "thumbnail_image_urls", "_thumbnail_image_urls", str, {}, MapSerializer(PredefinedSerializer())),
  FieldMetadata("competitionUsers", "competition_users", "_competition_users", CompetitionUser, {}, MapSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
]

ListModelInstancesByIdsRequest._fields = [
  FieldMetadata("modelInstanceIds", "model_instance_ids", "_model_instance_ids", int, [], ListSerializer(PredefinedSerializer())),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListModelInstancesRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, None, EnumSerializer(), optional=True),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListModelInstancesResponse._fields = [
  FieldMetadata("instances", "instances", "_instances", ModelInstance, [], ListSerializer(KaggleObjectSerializer())),
]

ListModelInstanceVersionsRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("modelInstanceVersionIds", "model_instance_version_ids", "_model_instance_version_ids", int, [], ListSerializer(PredefinedSerializer())),
]

ListModelLicenseGroupsRequest._fields = []

ListModelLicenseGroupsResponse._fields = [
  FieldMetadata("licenseGroups", "license_groups", "_license_groups", LicenseGroupDto, [], ListSerializer(KaggleObjectSerializer())),
]

ListModelsRequest._fields = [
  FieldMetadata("filter", "filter", "_filter", ListModelsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListModelsOrderBy, ListModelsOrderBy.LIST_MODELS_ORDER_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("privacyFilter", "privacy_filter", "_privacy_filter", PrivacyFilter, None, EnumSerializer(), optional=True),
]

ListModelsResponse._fields = [
  FieldMetadata("models", "models", "_models", Model, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
  FieldMetadata("totalResults", "total_results", "_total_results", int, 0, PredefinedSerializer()),
  FieldMetadata("totalModelInstances", "total_model_instances", "_total_model_instances", int, 0, PredefinedSerializer()),
]

ListOwnersRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("filter", "filter", "_filter", str, None, PredefinedSerializer(), optional=True),
]

ListOwnersResponse._fields = [
  FieldMetadata("owners", "owners", "_owners", Owner, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
]

ListSampleTasksRequest._fields = []

ListSampleTasksResponse._fields = [
  FieldMetadata("tasks", "tasks", "_tasks", SampleTask, [], ListSerializer(KaggleObjectSerializer())),
]

ModelUploaderConfig._fields = [
  FieldMetadata("existingData", "existing_data", "_existing_data", ExistingDataInfo, None, KaggleObjectSerializer()),
]

PinModelInstanceToCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
]

PreviewGatingAgreementContentRequest._fields = [
  FieldMetadata("rawContent", "raw_content", "_raw_content", str, "", PredefinedSerializer()),
]

RefreshRemoteModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("framework", "framework", "_framework", ModelFramework, ModelFramework.MODEL_FRAMEWORK_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("instanceSlug", "instance_slug", "_instance_slug", str, "", PredefinedSerializer()),
  FieldMetadata("settings", "settings", "_settings", DataCreationSettings, None, KaggleObjectSerializer()),
]

RemoveModelTagRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tagId", "tag_id", "_tag_id", int, 0, PredefinedSerializer()),
]

ReviewGatingUserConsentRequest._fields = [
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reviewStatus", "review_status", "_review_status", GatingAgreementRequestsReviewStatus, None, EnumSerializer(), optional=True),
  FieldMetadata("expireUserConsent", "expire_user_consent", "_expire_user_consent", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("publisherNotes", "publisher_notes", "_publisher_notes", str, None, PredefinedSerializer(), optional=True),
]

UnpinModelInstanceFromCompetitionRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, 0, PredefinedSerializer()),
  FieldMetadata("modelInstanceId", "model_instance_id", "_model_instance_id", int, 0, PredefinedSerializer()),
]

UpdateModelGatingRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("agreementId", "agreement_id", "_agreement_id", int, 0, PredefinedSerializer()),
  FieldMetadata("gatingStatus", "gating_status", "_gating_status", GatingAgreementModelsGatingStatus, GatingAgreementModelsGatingStatus.GATING_AGREEMENT_MODELS_GATING_STATUS_UNSPECIFIED, EnumSerializer()),
]

UpdateModelInstanceRequest._fields = [
  FieldMetadata("ownerSlug", "owner_slug", "_owner_slug", str, "", PredefinedSerializer()),
  FieldMetadata("modelSlug", "model_slug", "_model_slug", str, "", PredefinedSerializer()),
  FieldMetadata("instance", "instance", "_instance", ModelInstance, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

UpdateModelOwnerRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
]

UpdateModelOwnerResponse._fields = [
  FieldMetadata("newUrl", "new_url", "_new_url", str, "", PredefinedSerializer()),
]

UpdateModelRequest._fields = [
  FieldMetadata("model", "model", "_model", Model, None, KaggleObjectSerializer()),
  FieldMetadata("updateMask", "update_mask", "_update_mask", FieldMask, None, FieldMaskSerializer()),
]

VoteOnModelRequest._fields = [
  FieldMetadata("modelId", "model_id", "_model_id", int, 0, PredefinedSerializer()),
  FieldMetadata("voteType", "vote_type", "_vote_type", VoteType, VoteType.VOTE_TYPE_UNSPECIFIED, EnumSerializer()),
]

