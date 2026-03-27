import enum
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.cropped_image_upload import CroppedImageUpload
from kagglesdk.community.types.content_enums import ContentState
from kagglesdk.community.types.organization import Organization, OrganizationCategory, OrganizationDenialReason
from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_content_service import ListSearchContentDocument
from kagglesdk.users.types.user_avatar import UserAvatar
from typing import Optional, List

class ListOrganizationsOrderBy(enum.Enum):
  LIST_ORGANIZATIONS_ORDER_BY_UNSPECIFIED = 0
  LIST_ORGANIZATIONS_ORDER_BY_JOIN_DATE = 1
  """Join Date filter can only be used when the user_id filter is set."""
  LIST_ORGANIZATIONS_ORDER_BY_MEMBER_COUNT = 2

class CreateOrganizationInviteCodeRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to create an invite link for
  """

  def __init__(self):
    self._organization_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to create an invite link for"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id


class CreateOrganizationInviteCodeResponse(KaggleObject):
  r"""
  Attributes:
    invite_code (str)
      The full invite slug
  """

  def __init__(self):
    self._invite_code = ""
    self._freeze()

  @property
  def invite_code(self) -> str:
    """The full invite slug"""
    return self._invite_code

  @invite_code.setter
  def invite_code(self, invite_code: str):
    if invite_code is None:
      del self.invite_code
      return
    if not isinstance(invite_code, str):
      raise TypeError('invite_code must be of type str')
    self._invite_code = invite_code


class CreateOrganizationRequest(KaggleObject):
  r"""
  Attributes:
    display_name (str)
      The display name for the created organization
    slug (str)
      The slug for the created organization
    subtitle (str)
      An optional subtitle to display for this organization
    external_url (str)
      An optional external URL for this organization
    category (OrganizationCategory)
      The category this organization falls under, i.e. the type of organization
      this is
    owner_user_id (int)
      The user id that will become the owner and creator of the organization.
  """

  def __init__(self):
    self._display_name = ""
    self._slug = ""
    self._subtitle = None
    self._external_url = None
    self._category = OrganizationCategory.ORGANIZATION_CATEGORY_UNSPECIFIED
    self._owner_user_id = 0
    self._freeze()

  @property
  def display_name(self) -> str:
    """The display name for the created organization"""
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
    """The slug for the created organization"""
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
  def subtitle(self) -> str:
    """An optional subtitle to display for this organization"""
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def external_url(self) -> str:
    """An optional external URL for this organization"""
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
  def category(self) -> 'OrganizationCategory':
    r"""
    The category this organization falls under, i.e. the type of organization
    this is
    """
    return self._category

  @category.setter
  def category(self, category: 'OrganizationCategory'):
    if category is None:
      del self.category
      return
    if not isinstance(category, OrganizationCategory):
      raise TypeError('category must be of type OrganizationCategory')
    self._category = category

  @property
  def owner_user_id(self) -> int:
    """The user id that will become the owner and creator of the organization."""
    return self._owner_user_id

  @owner_user_id.setter
  def owner_user_id(self, owner_user_id: int):
    if owner_user_id is None:
      del self.owner_user_id
      return
    if not isinstance(owner_user_id, int):
      raise TypeError('owner_user_id must be of type int')
    self._owner_user_id = owner_user_id


class CreateOrganizationResponse(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The ID of the newly created organization
  """

  def __init__(self):
    self._organization_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The ID of the newly created organization"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id


class DeleteOrganizationMemberRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to remove this member from
    member_user_id (int)
      The member to remove from this organization
  """

  def __init__(self):
    self._organization_id = 0
    self._member_user_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to remove this member from"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def member_user_id(self) -> int:
    """The member to remove from this organization"""
    return self._member_user_id

  @member_user_id.setter
  def member_user_id(self, member_user_id: int):
    if member_user_id is None:
      del self.member_user_id
      return
    if not isinstance(member_user_id, int):
      raise TypeError('member_user_id must be of type int')
    self._member_user_id = member_user_id


class DeleteOrganizationRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to delete
  """

  def __init__(self):
    self._organization_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to delete"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id


class GetCurrentUserOrganizationsRequest(KaggleObject):
  r"""
  """

  pass

class GetCurrentUserOrganizationsResponse(KaggleObject):
  r"""
  Attributes:
    organizations (Organization)
      A list of organizations that the current user belongs to. Can be empty.
  """

  def __init__(self):
    self._organizations = []
    self._freeze()

  @property
  def organizations(self) -> Optional[List[Optional['Organization']]]:
    """A list of organizations that the current user belongs to. Can be empty."""
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[List[Optional['Organization']]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, list):
      raise TypeError('organizations must be of type list')
    if not all([isinstance(t, Organization) for t in organizations]):
      raise TypeError('organizations must contain only items of type Organization')
    self._organizations = organizations


class GetOrganizationMembersRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to fetch members for
  """

  def __init__(self):
    self._organization_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to fetch members for"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id


class GetOrganizationMembersResponse(KaggleObject):
  r"""
  Attributes:
    organization_members (UserAvatar)
      All of the organization's members
  """

  def __init__(self):
    self._organization_members = []
    self._freeze()

  @property
  def organization_members(self) -> Optional[List[Optional['UserAvatar']]]:
    """All of the organization's members"""
    return self._organization_members

  @organization_members.setter
  def organization_members(self, organization_members: Optional[List[Optional['UserAvatar']]]):
    if organization_members is None:
      del self.organization_members
      return
    if not isinstance(organization_members, list):
      raise TypeError('organization_members must be of type list')
    if not all([isinstance(t, UserAvatar) for t in organization_members]):
      raise TypeError('organization_members must contain only items of type UserAvatar')
    self._organization_members = organization_members


class GetOrganizationRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The ID of the organization to fetch
    organization_slug (str)
      The slug of the organization to fetch
    invite_code (str)
    include_counts (bool)
      Counts are computed via the list search content service, and aren't always
      necessary to include
  """

  def __init__(self):
    self._organization_id = None
    self._organization_slug = None
    self._invite_code = None
    self._include_counts = False
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The ID of the organization to fetch"""
    return self._organization_id or 0

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    del self.organization_slug
    self._organization_id = organization_id

  @property
  def organization_slug(self) -> str:
    """The slug of the organization to fetch"""
    return self._organization_slug or ""

  @organization_slug.setter
  def organization_slug(self, organization_slug: str):
    if organization_slug is None:
      del self.organization_slug
      return
    if not isinstance(organization_slug, str):
      raise TypeError('organization_slug must be of type str')
    del self.organization_id
    self._organization_slug = organization_slug

  @property
  def invite_code(self) -> str:
    return self._invite_code or ""

  @invite_code.setter
  def invite_code(self, invite_code: Optional[str]):
    if invite_code is None:
      del self.invite_code
      return
    if not isinstance(invite_code, str):
      raise TypeError('invite_code must be of type str')
    self._invite_code = invite_code

  @property
  def include_counts(self) -> bool:
    r"""
    Counts are computed via the list search content service, and aren't always
    necessary to include
    """
    return self._include_counts

  @include_counts.setter
  def include_counts(self, include_counts: bool):
    if include_counts is None:
      del self.include_counts
      return
    if not isinstance(include_counts, bool):
      raise TypeError('include_counts must be of type bool')
    self._include_counts = include_counts


class JoinOrganizationRequest(KaggleObject):
  r"""
  Attributes:
    invite_code (str)
      The URL part corresponding with an organization invite code
  """

  def __init__(self):
    self._invite_code = ""
    self._freeze()

  @property
  def invite_code(self) -> str:
    """The URL part corresponding with an organization invite code"""
    return self._invite_code

  @invite_code.setter
  def invite_code(self, invite_code: str):
    if invite_code is None:
      del self.invite_code
      return
    if not isinstance(invite_code, str):
      raise TypeError('invite_code must be of type str')
    self._invite_code = invite_code


class ListOrganizationContentRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to fetch listed content for
  """

  def __init__(self):
    self._organization_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to fetch listed content for"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id


class ListOrganizationContentResponse(KaggleObject):
  r"""
  Attributes:
    model_documents (ListSearchContentDocument)
      Organization-owned models
    dataset_documents (ListSearchContentDocument)
      Organization-owned datasets
    competition_documents (ListSearchContentDocument)
      Organization-owned competitions
    benchmark_documents (ListSearchContentDocument)
      Organization-owned benchmarks
  """

  def __init__(self):
    self._model_documents = []
    self._dataset_documents = []
    self._competition_documents = []
    self._benchmark_documents = []
    self._freeze()

  @property
  def model_documents(self) -> Optional[List[Optional['ListSearchContentDocument']]]:
    """Organization-owned models"""
    return self._model_documents

  @model_documents.setter
  def model_documents(self, model_documents: Optional[List[Optional['ListSearchContentDocument']]]):
    if model_documents is None:
      del self.model_documents
      return
    if not isinstance(model_documents, list):
      raise TypeError('model_documents must be of type list')
    if not all([isinstance(t, ListSearchContentDocument) for t in model_documents]):
      raise TypeError('model_documents must contain only items of type ListSearchContentDocument')
    self._model_documents = model_documents

  @property
  def dataset_documents(self) -> Optional[List[Optional['ListSearchContentDocument']]]:
    """Organization-owned datasets"""
    return self._dataset_documents

  @dataset_documents.setter
  def dataset_documents(self, dataset_documents: Optional[List[Optional['ListSearchContentDocument']]]):
    if dataset_documents is None:
      del self.dataset_documents
      return
    if not isinstance(dataset_documents, list):
      raise TypeError('dataset_documents must be of type list')
    if not all([isinstance(t, ListSearchContentDocument) for t in dataset_documents]):
      raise TypeError('dataset_documents must contain only items of type ListSearchContentDocument')
    self._dataset_documents = dataset_documents

  @property
  def competition_documents(self) -> Optional[List[Optional['ListSearchContentDocument']]]:
    """Organization-owned competitions"""
    return self._competition_documents

  @competition_documents.setter
  def competition_documents(self, competition_documents: Optional[List[Optional['ListSearchContentDocument']]]):
    if competition_documents is None:
      del self.competition_documents
      return
    if not isinstance(competition_documents, list):
      raise TypeError('competition_documents must be of type list')
    if not all([isinstance(t, ListSearchContentDocument) for t in competition_documents]):
      raise TypeError('competition_documents must contain only items of type ListSearchContentDocument')
    self._competition_documents = competition_documents

  @property
  def benchmark_documents(self) -> Optional[List[Optional['ListSearchContentDocument']]]:
    """Organization-owned benchmarks"""
    return self._benchmark_documents

  @benchmark_documents.setter
  def benchmark_documents(self, benchmark_documents: Optional[List[Optional['ListSearchContentDocument']]]):
    if benchmark_documents is None:
      del self.benchmark_documents
      return
    if not isinstance(benchmark_documents, list):
      raise TypeError('benchmark_documents must be of type list')
    if not all([isinstance(t, ListSearchContentDocument) for t in benchmark_documents]):
      raise TypeError('benchmark_documents must contain only items of type ListSearchContentDocument')
    self._benchmark_documents = benchmark_documents


class ListOrganizationsFilter(KaggleObject):
  r"""
  Attributes:
    user_id (int)
      Optionally filter by organizations which contain a certain user.
  """

  def __init__(self):
    self._user_id = None
    self._freeze()

  @property
  def user_id(self) -> int:
    """Optionally filter by organizations which contain a certain user."""
    return self._user_id or 0

  @user_id.setter
  def user_id(self, user_id: Optional[int]):
    if user_id is None:
      del self.user_id
      return
    if not isinstance(user_id, int):
      raise TypeError('user_id must be of type int')
    self._user_id = user_id


class ListOrganizationsRequest(KaggleObject):
  r"""
  Attributes:
    page_size (int)
    page_token (str)
    skip (int)
    filter (ListOrganizationsFilter)
    order_by (ListOrganizationsOrderBy)
    read_mask (FieldMask)
  """

  def __init__(self):
    self._page_size = 0
    self._page_token = None
    self._skip = None
    self._filter = None
    self._order_by = ListOrganizationsOrderBy.LIST_ORGANIZATIONS_ORDER_BY_UNSPECIFIED
    self._read_mask = None
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
  def filter(self) -> Optional['ListOrganizationsFilter']:
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['ListOrganizationsFilter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, ListOrganizationsFilter):
      raise TypeError('filter must be of type ListOrganizationsFilter')
    self._filter = filter

  @property
  def order_by(self) -> 'ListOrganizationsOrderBy':
    return self._order_by

  @order_by.setter
  def order_by(self, order_by: 'ListOrganizationsOrderBy'):
    if order_by is None:
      del self.order_by
      return
    if not isinstance(order_by, ListOrganizationsOrderBy):
      raise TypeError('order_by must be of type ListOrganizationsOrderBy')
    self._order_by = order_by

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


class ListOrganizationsResponse(KaggleObject):
  r"""
  Attributes:
    organizations (Organization)
    total_size (int)
    next_page_token (str)
  """

  def __init__(self):
    self._organizations = []
    self._total_size = 0
    self._next_page_token = ""
    self._freeze()

  @property
  def organizations(self) -> Optional[List[Optional['Organization']]]:
    return self._organizations

  @organizations.setter
  def organizations(self, organizations: Optional[List[Optional['Organization']]]):
    if organizations is None:
      del self.organizations
      return
    if not isinstance(organizations, list):
      raise TypeError('organizations must be of type list')
    if not all([isinstance(t, Organization) for t in organizations]):
      raise TypeError('organizations must contain only items of type Organization')
    self._organizations = organizations

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


class UpdateOrganizationAllowModelGatingRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
    allow_model_gating (bool)
  """

  def __init__(self):
    self._organization_id = 0
    self._allow_model_gating = False
    self._freeze()

  @property
  def organization_id(self) -> int:
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def allow_model_gating(self) -> bool:
    return self._allow_model_gating

  @allow_model_gating.setter
  def allow_model_gating(self, allow_model_gating: bool):
    if allow_model_gating is None:
      del self.allow_model_gating
      return
    if not isinstance(allow_model_gating, bool):
      raise TypeError('allow_model_gating must be of type bool')
    self._allow_model_gating = allow_model_gating


class UpdateOrganizationContentStateRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to update content state for
    content_state (ContentState)
      The content state to migrate this organization to
    denial_reason (OrganizationDenialReason)
      If applicable, this indicates the reason an organization was denied
  """

  def __init__(self):
    self._organization_id = 0
    self._content_state = ContentState.CONTENT_STATE_UNSPECIFIED
    self._denial_reason = None
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to update content state for"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def content_state(self) -> 'ContentState':
    """The content state to migrate this organization to"""
    return self._content_state

  @content_state.setter
  def content_state(self, content_state: 'ContentState'):
    if content_state is None:
      del self.content_state
      return
    if not isinstance(content_state, ContentState):
      raise TypeError('content_state must be of type ContentState')
    self._content_state = content_state

  @property
  def denial_reason(self) -> 'OrganizationDenialReason':
    """If applicable, this indicates the reason an organization was denied"""
    return self._denial_reason or OrganizationDenialReason.ORGANIZATION_DENIAL_REASON_UNSPECIFIED

  @denial_reason.setter
  def denial_reason(self, denial_reason: Optional['OrganizationDenialReason']):
    if denial_reason is None:
      del self.denial_reason
      return
    if not isinstance(denial_reason, OrganizationDenialReason):
      raise TypeError('denial_reason must be of type OrganizationDenialReason')
    self._denial_reason = denial_reason


class UpdateOrganizationOwnershipRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to remove this member from
    member_user_id (int)
      The member to remove from this organization
  """

  def __init__(self):
    self._organization_id = 0
    self._member_user_id = 0
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to remove this member from"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def member_user_id(self) -> int:
    """The member to remove from this organization"""
    return self._member_user_id

  @member_user_id.setter
  def member_user_id(self, member_user_id: int):
    if member_user_id is None:
      del self.member_user_id
      return
    if not isinstance(member_user_id, int):
      raise TypeError('member_user_id must be of type int')
    self._member_user_id = member_user_id


class UpdateOrganizationRequest(KaggleObject):
  r"""
  Attributes:
    organization_id (int)
      The organization to update
    display_name (str)
      The new display name for the organization
    subtitle (str)
      The new subtitle for this organization
    external_url (str)
      The new external URL for this organization
    image (CroppedImageUpload)
      The new avatar for this organization
    overview (str)
      The new overview for this organization
    category (OrganizationCategory)
      The new category for this organization
  """

  def __init__(self):
    self._organization_id = 0
    self._display_name = None
    self._subtitle = None
    self._external_url = None
    self._image = None
    self._overview = None
    self._category = None
    self._freeze()

  @property
  def organization_id(self) -> int:
    """The organization to update"""
    return self._organization_id

  @organization_id.setter
  def organization_id(self, organization_id: int):
    if organization_id is None:
      del self.organization_id
      return
    if not isinstance(organization_id, int):
      raise TypeError('organization_id must be of type int')
    self._organization_id = organization_id

  @property
  def display_name(self) -> str:
    """The new display name for the organization"""
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
  def subtitle(self) -> str:
    """The new subtitle for this organization"""
    return self._subtitle or ""

  @subtitle.setter
  def subtitle(self, subtitle: Optional[str]):
    if subtitle is None:
      del self.subtitle
      return
    if not isinstance(subtitle, str):
      raise TypeError('subtitle must be of type str')
    self._subtitle = subtitle

  @property
  def external_url(self) -> str:
    """The new external URL for this organization"""
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
  def image(self) -> Optional['CroppedImageUpload']:
    """The new avatar for this organization"""
    return self._image or None

  @image.setter
  def image(self, image: Optional[Optional['CroppedImageUpload']]):
    if image is None:
      del self.image
      return
    if not isinstance(image, CroppedImageUpload):
      raise TypeError('image must be of type CroppedImageUpload')
    self._image = image

  @property
  def overview(self) -> str:
    """The new overview for this organization"""
    return self._overview or ""

  @overview.setter
  def overview(self, overview: Optional[str]):
    if overview is None:
      del self.overview
      return
    if not isinstance(overview, str):
      raise TypeError('overview must be of type str')
    self._overview = overview

  @property
  def category(self) -> 'OrganizationCategory':
    """The new category for this organization"""
    return self._category or OrganizationCategory.ORGANIZATION_CATEGORY_UNSPECIFIED

  @category.setter
  def category(self, category: Optional['OrganizationCategory']):
    if category is None:
      del self.category
      return
    if not isinstance(category, OrganizationCategory):
      raise TypeError('category must be of type OrganizationCategory')
    self._category = category


class UpdateOrganizationSlugRequest(KaggleObject):
  r"""
  Attributes:
    old_organization_slug (str)
    new_organization_slug (str)
  """

  def __init__(self):
    self._old_organization_slug = ""
    self._new_organization_slug = ""
    self._freeze()

  @property
  def old_organization_slug(self) -> str:
    return self._old_organization_slug

  @old_organization_slug.setter
  def old_organization_slug(self, old_organization_slug: str):
    if old_organization_slug is None:
      del self.old_organization_slug
      return
    if not isinstance(old_organization_slug, str):
      raise TypeError('old_organization_slug must be of type str')
    self._old_organization_slug = old_organization_slug

  @property
  def new_organization_slug(self) -> str:
    return self._new_organization_slug

  @new_organization_slug.setter
  def new_organization_slug(self, new_organization_slug: str):
    if new_organization_slug is None:
      del self.new_organization_slug
      return
    if not isinstance(new_organization_slug, str):
      raise TypeError('new_organization_slug must be of type str')
    self._new_organization_slug = new_organization_slug


class UpdateOrganizationSlugResponse(KaggleObject):
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


CreateOrganizationInviteCodeRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
]

CreateOrganizationInviteCodeResponse._fields = [
  FieldMetadata("inviteCode", "invite_code", "_invite_code", str, "", PredefinedSerializer()),
]

CreateOrganizationRequest._fields = [
  FieldMetadata("displayName", "display_name", "_display_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", OrganizationCategory, OrganizationCategory.ORGANIZATION_CATEGORY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("ownerUserId", "owner_user_id", "_owner_user_id", int, 0, PredefinedSerializer()),
]

CreateOrganizationResponse._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
]

DeleteOrganizationMemberRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("memberUserId", "member_user_id", "_member_user_id", int, 0, PredefinedSerializer()),
]

DeleteOrganizationRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
]

GetCurrentUserOrganizationsRequest._fields = []

GetCurrentUserOrganizationsResponse._fields = [
  FieldMetadata("organizations", "organizations", "_organizations", Organization, [], ListSerializer(KaggleObjectSerializer())),
]

GetOrganizationMembersRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
]

GetOrganizationMembersResponse._fields = [
  FieldMetadata("organizationMembers", "organization_members", "_organization_members", UserAvatar, [], ListSerializer(KaggleObjectSerializer())),
]

GetOrganizationRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("organizationSlug", "organization_slug", "_organization_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("inviteCode", "invite_code", "_invite_code", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("includeCounts", "include_counts", "_include_counts", bool, False, PredefinedSerializer()),
]

JoinOrganizationRequest._fields = [
  FieldMetadata("inviteCode", "invite_code", "_invite_code", str, "", PredefinedSerializer()),
]

ListOrganizationContentRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
]

ListOrganizationContentResponse._fields = [
  FieldMetadata("modelDocuments", "model_documents", "_model_documents", ListSearchContentDocument, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("datasetDocuments", "dataset_documents", "_dataset_documents", ListSearchContentDocument, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("competitionDocuments", "competition_documents", "_competition_documents", ListSearchContentDocument, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("benchmarkDocuments", "benchmark_documents", "_benchmark_documents", ListSearchContentDocument, [], ListSerializer(KaggleObjectSerializer())),
]

ListOrganizationsFilter._fields = [
  FieldMetadata("userId", "user_id", "_user_id", int, None, PredefinedSerializer(), optional=True),
]

ListOrganizationsRequest._fields = [
  FieldMetadata("pageSize", "page_size", "_page_size", int, 0, PredefinedSerializer()),
  FieldMetadata("pageToken", "page_token", "_page_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("skip", "skip", "_skip", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("filter", "filter", "_filter", ListOrganizationsFilter, None, KaggleObjectSerializer()),
  FieldMetadata("orderBy", "order_by", "_order_by", ListOrganizationsOrderBy, ListOrganizationsOrderBy.LIST_ORGANIZATIONS_ORDER_BY_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("readMask", "read_mask", "_read_mask", FieldMask, None, FieldMaskSerializer()),
]

ListOrganizationsResponse._fields = [
  FieldMetadata("organizations", "organizations", "_organizations", Organization, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("totalSize", "total_size", "_total_size", int, 0, PredefinedSerializer()),
  FieldMetadata("nextPageToken", "next_page_token", "_next_page_token", str, "", PredefinedSerializer()),
]

UpdateOrganizationAllowModelGatingRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("allowModelGating", "allow_model_gating", "_allow_model_gating", bool, False, PredefinedSerializer()),
]

UpdateOrganizationContentStateRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("contentState", "content_state", "_content_state", ContentState, ContentState.CONTENT_STATE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("denialReason", "denial_reason", "_denial_reason", OrganizationDenialReason, None, EnumSerializer(), optional=True),
]

UpdateOrganizationOwnershipRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("memberUserId", "member_user_id", "_member_user_id", int, 0, PredefinedSerializer()),
]

UpdateOrganizationRequest._fields = [
  FieldMetadata("organizationId", "organization_id", "_organization_id", int, 0, PredefinedSerializer()),
  FieldMetadata("displayName", "display_name", "_display_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("subtitle", "subtitle", "_subtitle", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("externalUrl", "external_url", "_external_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("image", "image", "_image", CroppedImageUpload, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("overview", "overview", "_overview", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("category", "category", "_category", OrganizationCategory, None, EnumSerializer(), optional=True),
]

UpdateOrganizationSlugRequest._fields = [
  FieldMetadata("oldOrganizationSlug", "old_organization_slug", "_old_organization_slug", str, "", PredefinedSerializer()),
  FieldMetadata("newOrganizationSlug", "new_organization_slug", "_new_organization_slug", str, "", PredefinedSerializer()),
]

UpdateOrganizationSlugResponse._fields = [
  FieldMetadata("newUrl", "new_url", "_new_url", str, "", PredefinedSerializer()),
]

