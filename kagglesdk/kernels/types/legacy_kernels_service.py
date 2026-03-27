from datetime import datetime
from kagglesdk.abuse.types.abuse_enums import PrivatedModerationStatus
from kagglesdk.common.types.common_types import PageMessage
from kagglesdk.common.types.vote import VoteButton
from kagglesdk.competitions.types.submission import KernelSubmission
from kagglesdk.datasets.types.dataset_types import KernelOutputDatasetReference
from kagglesdk.education.types.education_service import LearnSeriesNavigationData
from kagglesdk.kaggle_object import *
from kagglesdk.kernels.types.kernels_enums import KernelVersionType, KernelWorkerStatus
from kagglesdk.kernels.types.kernels_service import CheckNewerColabVersionResponse, Kernel, KernelRun, KernelSessionScore
from kagglesdk.kernels.types.kernels_types import DataSource, DataSourceReference, KernelSessionOutputFile
from kagglesdk.models.types.model_types import KernelOutputModelInstanceReference
from kagglesdk.users.types.group_types import CollaboratorList
from kagglesdk.users.types.user import User
from typing import Optional, List

class GetKernelViewModelRequest(KaggleObject):
  r"""
  Attributes:
    author_user_name (str)
    kernel_slug (str)
    kernel_version_id (int)
      Technically KernelSessionId
    tab (str)
    version_number (int)
      User-visible version number (increments from 1 on each saved version)
      More natural alternative to kernel_version_id when that id is not known.
  """

  def __init__(self):
    self._author_user_name = None
    self._kernel_slug = None
    self._kernel_version_id = 0
    self._tab = None
    self._version_number = None
    self._freeze()

  @property
  def author_user_name(self) -> str:
    return self._author_user_name or ""

  @author_user_name.setter
  def author_user_name(self, author_user_name: Optional[str]):
    if author_user_name is None:
      del self.author_user_name
      return
    if not isinstance(author_user_name, str):
      raise TypeError('author_user_name must be of type str')
    self._author_user_name = author_user_name

  @property
  def kernel_slug(self) -> str:
    return self._kernel_slug or ""

  @kernel_slug.setter
  def kernel_slug(self, kernel_slug: Optional[str]):
    if kernel_slug is None:
      del self.kernel_slug
      return
    if not isinstance(kernel_slug, str):
      raise TypeError('kernel_slug must be of type str')
    self._kernel_slug = kernel_slug

  @property
  def kernel_version_id(self) -> int:
    """Technically KernelSessionId"""
    return self._kernel_version_id

  @kernel_version_id.setter
  def kernel_version_id(self, kernel_version_id: int):
    if kernel_version_id is None:
      del self.kernel_version_id
      return
    if not isinstance(kernel_version_id, int):
      raise TypeError('kernel_version_id must be of type int')
    self._kernel_version_id = kernel_version_id

  @property
  def tab(self) -> str:
    return self._tab or ""

  @tab.setter
  def tab(self, tab: Optional[str]):
    if tab is None:
      del self.tab
      return
    if not isinstance(tab, str):
      raise TypeError('tab must be of type str')
    self._tab = tab

  @property
  def version_number(self) -> int:
    r"""
    User-visible version number (increments from 1 on each saved version)
    More natural alternative to kernel_version_id when that id is not known.
    """
    return self._version_number or 0

  @version_number.setter
  def version_number(self, version_number: Optional[int]):
    if version_number is None:
      del self.version_number
      return
    if not isinstance(version_number, int):
      raise TypeError('version_number must be of type int')
    self._version_number = version_number


class GetKernelViewModelResponse(KaggleObject):
  r"""
  Attributes:
    redirect_url (str)
    kernel (Kernel)
    kernel_run (KernelRun)
    author (User)
    base_url (str)
    collaborators (CollaboratorList)
    initial_tab (str)
    output_files (KernelSessionOutputFile)
    page_messages (PageMessage)
    data_sources (DataSourceReference)
    renderable_data_sources (DataSource)
    download_all_files_url (str)
    submission (KernelSubmission)
    best_submission_score (KernelSessionScore)
    menu_links (LinkModel)
    vote_button (VoteButton)
    can_write (bool)
    current_user_fork_parent_session_id (int)
    simplified_viewer (bool)
    kernel_output_dataset (KernelOutputDatasetReference)
    learn_series_navigation_data (LearnSeriesNavigationData)
    show_sharing_controls (bool)
    show_unchanged_copy_warning (bool)
    moderation_status (PrivatedModerationStatus)
    is_reported_banner_dismissed (bool)
    show_admin_allowlist (bool)
    is_reported_modal_dismissed (bool)
    failed_package_manager_url (str)
    requirements_file_download_url (str)
    description (str)
    is_package_session (bool)
    check_newer_colab_version_state (CheckNewerColabVersionResponse)
    kernel_output_model_instance (KernelOutputModelInstanceReference)
    total_version_count (int)
    current_version_number (int)
  """

  def __init__(self):
    self._redirect_url = None
    self._kernel = None
    self._kernel_run = None
    self._author = None
    self._base_url = None
    self._collaborators = None
    self._initial_tab = None
    self._output_files = []
    self._page_messages = []
    self._data_sources = []
    self._renderable_data_sources = []
    self._download_all_files_url = None
    self._submission = None
    self._best_submission_score = None
    self._menu_links = []
    self._vote_button = None
    self._can_write = False
    self._current_user_fork_parent_session_id = None
    self._simplified_viewer = False
    self._kernel_output_dataset = None
    self._learn_series_navigation_data = None
    self._show_sharing_controls = False
    self._show_unchanged_copy_warning = False
    self._moderation_status = PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED
    self._is_reported_banner_dismissed = False
    self._show_admin_allowlist = False
    self._is_reported_modal_dismissed = False
    self._failed_package_manager_url = None
    self._requirements_file_download_url = None
    self._description = None
    self._is_package_session = False
    self._check_newer_colab_version_state = None
    self._kernel_output_model_instance = None
    self._total_version_count = 0
    self._current_version_number = None
    self._freeze()

  @property
  def redirect_url(self) -> str:
    return self._redirect_url or ""

  @redirect_url.setter
  def redirect_url(self, redirect_url: Optional[str]):
    if redirect_url is None:
      del self.redirect_url
      return
    if not isinstance(redirect_url, str):
      raise TypeError('redirect_url must be of type str')
    self._redirect_url = redirect_url

  @property
  def kernel(self) -> Optional['Kernel']:
    return self._kernel

  @kernel.setter
  def kernel(self, kernel: Optional['Kernel']):
    if kernel is None:
      del self.kernel
      return
    if not isinstance(kernel, Kernel):
      raise TypeError('kernel must be of type Kernel')
    self._kernel = kernel

  @property
  def kernel_run(self) -> Optional['KernelRun']:
    return self._kernel_run

  @kernel_run.setter
  def kernel_run(self, kernel_run: Optional['KernelRun']):
    if kernel_run is None:
      del self.kernel_run
      return
    if not isinstance(kernel_run, KernelRun):
      raise TypeError('kernel_run must be of type KernelRun')
    self._kernel_run = kernel_run

  @property
  def author(self) -> Optional['User']:
    return self._author

  @author.setter
  def author(self, author: Optional['User']):
    if author is None:
      del self.author
      return
    if not isinstance(author, User):
      raise TypeError('author must be of type User')
    self._author = author

  @property
  def base_url(self) -> str:
    return self._base_url or ""

  @base_url.setter
  def base_url(self, base_url: Optional[str]):
    if base_url is None:
      del self.base_url
      return
    if not isinstance(base_url, str):
      raise TypeError('base_url must be of type str')
    self._base_url = base_url

  @property
  def collaborators(self) -> Optional['CollaboratorList']:
    return self._collaborators

  @collaborators.setter
  def collaborators(self, collaborators: Optional['CollaboratorList']):
    if collaborators is None:
      del self.collaborators
      return
    if not isinstance(collaborators, CollaboratorList):
      raise TypeError('collaborators must be of type CollaboratorList')
    self._collaborators = collaborators

  @property
  def initial_tab(self) -> str:
    return self._initial_tab or ""

  @initial_tab.setter
  def initial_tab(self, initial_tab: Optional[str]):
    if initial_tab is None:
      del self.initial_tab
      return
    if not isinstance(initial_tab, str):
      raise TypeError('initial_tab must be of type str')
    self._initial_tab = initial_tab

  @property
  def output_files(self) -> Optional[List[Optional['KernelSessionOutputFile']]]:
    return self._output_files

  @output_files.setter
  def output_files(self, output_files: Optional[List[Optional['KernelSessionOutputFile']]]):
    if output_files is None:
      del self.output_files
      return
    if not isinstance(output_files, list):
      raise TypeError('output_files must be of type list')
    if not all([isinstance(t, KernelSessionOutputFile) for t in output_files]):
      raise TypeError('output_files must contain only items of type KernelSessionOutputFile')
    self._output_files = output_files

  @property
  def page_messages(self) -> Optional[List[Optional['PageMessage']]]:
    return self._page_messages

  @page_messages.setter
  def page_messages(self, page_messages: Optional[List[Optional['PageMessage']]]):
    if page_messages is None:
      del self.page_messages
      return
    if not isinstance(page_messages, list):
      raise TypeError('page_messages must be of type list')
    if not all([isinstance(t, PageMessage) for t in page_messages]):
      raise TypeError('page_messages must contain only items of type PageMessage')
    self._page_messages = page_messages

  @property
  def data_sources(self) -> Optional[List[Optional['DataSourceReference']]]:
    return self._data_sources

  @data_sources.setter
  def data_sources(self, data_sources: Optional[List[Optional['DataSourceReference']]]):
    if data_sources is None:
      del self.data_sources
      return
    if not isinstance(data_sources, list):
      raise TypeError('data_sources must be of type list')
    if not all([isinstance(t, DataSourceReference) for t in data_sources]):
      raise TypeError('data_sources must contain only items of type DataSourceReference')
    self._data_sources = data_sources

  @property
  def renderable_data_sources(self) -> Optional[List[Optional['DataSource']]]:
    return self._renderable_data_sources

  @renderable_data_sources.setter
  def renderable_data_sources(self, renderable_data_sources: Optional[List[Optional['DataSource']]]):
    if renderable_data_sources is None:
      del self.renderable_data_sources
      return
    if not isinstance(renderable_data_sources, list):
      raise TypeError('renderable_data_sources must be of type list')
    if not all([isinstance(t, DataSource) for t in renderable_data_sources]):
      raise TypeError('renderable_data_sources must contain only items of type DataSource')
    self._renderable_data_sources = renderable_data_sources

  @property
  def download_all_files_url(self) -> str:
    return self._download_all_files_url or ""

  @download_all_files_url.setter
  def download_all_files_url(self, download_all_files_url: Optional[str]):
    if download_all_files_url is None:
      del self.download_all_files_url
      return
    if not isinstance(download_all_files_url, str):
      raise TypeError('download_all_files_url must be of type str')
    self._download_all_files_url = download_all_files_url

  @property
  def submission(self) -> Optional['KernelSubmission']:
    return self._submission

  @submission.setter
  def submission(self, submission: Optional['KernelSubmission']):
    if submission is None:
      del self.submission
      return
    if not isinstance(submission, KernelSubmission):
      raise TypeError('submission must be of type KernelSubmission')
    self._submission = submission

  @property
  def best_submission_score(self) -> Optional['KernelSessionScore']:
    return self._best_submission_score

  @best_submission_score.setter
  def best_submission_score(self, best_submission_score: Optional['KernelSessionScore']):
    if best_submission_score is None:
      del self.best_submission_score
      return
    if not isinstance(best_submission_score, KernelSessionScore):
      raise TypeError('best_submission_score must be of type KernelSessionScore')
    self._best_submission_score = best_submission_score

  @property
  def menu_links(self) -> Optional[List[Optional['LinkModel']]]:
    return self._menu_links

  @menu_links.setter
  def menu_links(self, menu_links: Optional[List[Optional['LinkModel']]]):
    if menu_links is None:
      del self.menu_links
      return
    if not isinstance(menu_links, list):
      raise TypeError('menu_links must be of type list')
    if not all([isinstance(t, LinkModel) for t in menu_links]):
      raise TypeError('menu_links must contain only items of type LinkModel')
    self._menu_links = menu_links

  @property
  def vote_button(self) -> Optional['VoteButton']:
    return self._vote_button

  @vote_button.setter
  def vote_button(self, vote_button: Optional['VoteButton']):
    if vote_button is None:
      del self.vote_button
      return
    if not isinstance(vote_button, VoteButton):
      raise TypeError('vote_button must be of type VoteButton')
    self._vote_button = vote_button

  @property
  def can_write(self) -> bool:
    return self._can_write

  @can_write.setter
  def can_write(self, can_write: bool):
    if can_write is None:
      del self.can_write
      return
    if not isinstance(can_write, bool):
      raise TypeError('can_write must be of type bool')
    self._can_write = can_write

  @property
  def current_user_fork_parent_session_id(self) -> int:
    return self._current_user_fork_parent_session_id or 0

  @current_user_fork_parent_session_id.setter
  def current_user_fork_parent_session_id(self, current_user_fork_parent_session_id: Optional[int]):
    if current_user_fork_parent_session_id is None:
      del self.current_user_fork_parent_session_id
      return
    if not isinstance(current_user_fork_parent_session_id, int):
      raise TypeError('current_user_fork_parent_session_id must be of type int')
    self._current_user_fork_parent_session_id = current_user_fork_parent_session_id

  @property
  def simplified_viewer(self) -> bool:
    return self._simplified_viewer

  @simplified_viewer.setter
  def simplified_viewer(self, simplified_viewer: bool):
    if simplified_viewer is None:
      del self.simplified_viewer
      return
    if not isinstance(simplified_viewer, bool):
      raise TypeError('simplified_viewer must be of type bool')
    self._simplified_viewer = simplified_viewer

  @property
  def kernel_output_dataset(self) -> Optional['KernelOutputDatasetReference']:
    return self._kernel_output_dataset

  @kernel_output_dataset.setter
  def kernel_output_dataset(self, kernel_output_dataset: Optional['KernelOutputDatasetReference']):
    if kernel_output_dataset is None:
      del self.kernel_output_dataset
      return
    if not isinstance(kernel_output_dataset, KernelOutputDatasetReference):
      raise TypeError('kernel_output_dataset must be of type KernelOutputDatasetReference')
    self._kernel_output_dataset = kernel_output_dataset

  @property
  def kernel_output_model_instance(self) -> Optional['KernelOutputModelInstanceReference']:
    return self._kernel_output_model_instance

  @kernel_output_model_instance.setter
  def kernel_output_model_instance(self, kernel_output_model_instance: Optional['KernelOutputModelInstanceReference']):
    if kernel_output_model_instance is None:
      del self.kernel_output_model_instance
      return
    if not isinstance(kernel_output_model_instance, KernelOutputModelInstanceReference):
      raise TypeError('kernel_output_model_instance must be of type KernelOutputModelInstanceReference')
    self._kernel_output_model_instance = kernel_output_model_instance

  @property
  def learn_series_navigation_data(self) -> Optional['LearnSeriesNavigationData']:
    return self._learn_series_navigation_data

  @learn_series_navigation_data.setter
  def learn_series_navigation_data(self, learn_series_navigation_data: Optional['LearnSeriesNavigationData']):
    if learn_series_navigation_data is None:
      del self.learn_series_navigation_data
      return
    if not isinstance(learn_series_navigation_data, LearnSeriesNavigationData):
      raise TypeError('learn_series_navigation_data must be of type LearnSeriesNavigationData')
    self._learn_series_navigation_data = learn_series_navigation_data

  @property
  def show_sharing_controls(self) -> bool:
    return self._show_sharing_controls

  @show_sharing_controls.setter
  def show_sharing_controls(self, show_sharing_controls: bool):
    if show_sharing_controls is None:
      del self.show_sharing_controls
      return
    if not isinstance(show_sharing_controls, bool):
      raise TypeError('show_sharing_controls must be of type bool')
    self._show_sharing_controls = show_sharing_controls

  @property
  def show_unchanged_copy_warning(self) -> bool:
    return self._show_unchanged_copy_warning

  @show_unchanged_copy_warning.setter
  def show_unchanged_copy_warning(self, show_unchanged_copy_warning: bool):
    if show_unchanged_copy_warning is None:
      del self.show_unchanged_copy_warning
      return
    if not isinstance(show_unchanged_copy_warning, bool):
      raise TypeError('show_unchanged_copy_warning must be of type bool')
    self._show_unchanged_copy_warning = show_unchanged_copy_warning

  @property
  def moderation_status(self) -> 'PrivatedModerationStatus':
    return self._moderation_status

  @moderation_status.setter
  def moderation_status(self, moderation_status: 'PrivatedModerationStatus'):
    if moderation_status is None:
      del self.moderation_status
      return
    if not isinstance(moderation_status, PrivatedModerationStatus):
      raise TypeError('moderation_status must be of type PrivatedModerationStatus')
    self._moderation_status = moderation_status

  @property
  def is_reported_banner_dismissed(self) -> bool:
    return self._is_reported_banner_dismissed

  @is_reported_banner_dismissed.setter
  def is_reported_banner_dismissed(self, is_reported_banner_dismissed: bool):
    if is_reported_banner_dismissed is None:
      del self.is_reported_banner_dismissed
      return
    if not isinstance(is_reported_banner_dismissed, bool):
      raise TypeError('is_reported_banner_dismissed must be of type bool')
    self._is_reported_banner_dismissed = is_reported_banner_dismissed

  @property
  def show_admin_allowlist(self) -> bool:
    return self._show_admin_allowlist

  @show_admin_allowlist.setter
  def show_admin_allowlist(self, show_admin_allowlist: bool):
    if show_admin_allowlist is None:
      del self.show_admin_allowlist
      return
    if not isinstance(show_admin_allowlist, bool):
      raise TypeError('show_admin_allowlist must be of type bool')
    self._show_admin_allowlist = show_admin_allowlist

  @property
  def is_reported_modal_dismissed(self) -> bool:
    return self._is_reported_modal_dismissed

  @is_reported_modal_dismissed.setter
  def is_reported_modal_dismissed(self, is_reported_modal_dismissed: bool):
    if is_reported_modal_dismissed is None:
      del self.is_reported_modal_dismissed
      return
    if not isinstance(is_reported_modal_dismissed, bool):
      raise TypeError('is_reported_modal_dismissed must be of type bool')
    self._is_reported_modal_dismissed = is_reported_modal_dismissed

  @property
  def failed_package_manager_url(self) -> str:
    return self._failed_package_manager_url or ""

  @failed_package_manager_url.setter
  def failed_package_manager_url(self, failed_package_manager_url: Optional[str]):
    if failed_package_manager_url is None:
      del self.failed_package_manager_url
      return
    if not isinstance(failed_package_manager_url, str):
      raise TypeError('failed_package_manager_url must be of type str')
    self._failed_package_manager_url = failed_package_manager_url

  @property
  def requirements_file_download_url(self) -> str:
    return self._requirements_file_download_url or ""

  @requirements_file_download_url.setter
  def requirements_file_download_url(self, requirements_file_download_url: Optional[str]):
    if requirements_file_download_url is None:
      del self.requirements_file_download_url
      return
    if not isinstance(requirements_file_download_url, str):
      raise TypeError('requirements_file_download_url must be of type str')
    self._requirements_file_download_url = requirements_file_download_url

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
  def is_package_session(self) -> bool:
    return self._is_package_session

  @is_package_session.setter
  def is_package_session(self, is_package_session: bool):
    if is_package_session is None:
      del self.is_package_session
      return
    if not isinstance(is_package_session, bool):
      raise TypeError('is_package_session must be of type bool')
    self._is_package_session = is_package_session

  @property
  def check_newer_colab_version_state(self) -> Optional['CheckNewerColabVersionResponse']:
    return self._check_newer_colab_version_state or None

  @check_newer_colab_version_state.setter
  def check_newer_colab_version_state(self, check_newer_colab_version_state: Optional[Optional['CheckNewerColabVersionResponse']]):
    if check_newer_colab_version_state is None:
      del self.check_newer_colab_version_state
      return
    if not isinstance(check_newer_colab_version_state, CheckNewerColabVersionResponse):
      raise TypeError('check_newer_colab_version_state must be of type CheckNewerColabVersionResponse')
    self._check_newer_colab_version_state = check_newer_colab_version_state

  @property
  def total_version_count(self) -> int:
    return self._total_version_count

  @total_version_count.setter
  def total_version_count(self, total_version_count: int):
    if total_version_count is None:
      del self.total_version_count
      return
    if not isinstance(total_version_count, int):
      raise TypeError('total_version_count must be of type int')
    self._total_version_count = total_version_count

  @property
  def current_version_number(self) -> int:
    return self._current_version_number or 0

  @current_version_number.setter
  def current_version_number(self, current_version_number: Optional[int]):
    if current_version_number is None:
      del self.current_version_number
      return
    if not isinstance(current_version_number, int):
      raise TypeError('current_version_number must be of type int')
    self._current_version_number = current_version_number


class KernelVersionHistory(KaggleObject):
  r"""
  Attributes:
    id (int)
    is_fork_parent (bool)
    is_notebook (bool)
    language_name (str)
    last_run_time (datetime)
    lines_changed_from_previous (int)
    lines_deleted_from_previous (int)
    lines_inserted_from_previous (int)
    output_files_total_size_bytes (int)
    run_info (KernelVersionRunInfo)
    status (KernelWorkerStatus)
    title (str)
    url (str)
    version_number (int)
    has_version_number (bool)
    is_redacted (bool)
    version_type (KernelVersionType)
  """

  def __init__(self):
    self._id = 0
    self._is_fork_parent = False
    self._is_notebook = False
    self._language_name = None
    self._last_run_time = None
    self._lines_changed_from_previous = 0
    self._lines_deleted_from_previous = 0
    self._lines_inserted_from_previous = 0
    self._output_files_total_size_bytes = 0
    self._run_info = None
    self._status = KernelWorkerStatus.QUEUED
    self._title = None
    self._url = ""
    self._version_number = 0
    self._has_version_number = False
    self._is_redacted = False
    self._version_type = KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED
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
  def is_fork_parent(self) -> bool:
    return self._is_fork_parent

  @is_fork_parent.setter
  def is_fork_parent(self, is_fork_parent: bool):
    if is_fork_parent is None:
      del self.is_fork_parent
      return
    if not isinstance(is_fork_parent, bool):
      raise TypeError('is_fork_parent must be of type bool')
    self._is_fork_parent = is_fork_parent

  @property
  def is_notebook(self) -> bool:
    return self._is_notebook

  @is_notebook.setter
  def is_notebook(self, is_notebook: bool):
    if is_notebook is None:
      del self.is_notebook
      return
    if not isinstance(is_notebook, bool):
      raise TypeError('is_notebook must be of type bool')
    self._is_notebook = is_notebook

  @property
  def language_name(self) -> str:
    return self._language_name or ""

  @language_name.setter
  def language_name(self, language_name: Optional[str]):
    if language_name is None:
      del self.language_name
      return
    if not isinstance(language_name, str):
      raise TypeError('language_name must be of type str')
    self._language_name = language_name

  @property
  def last_run_time(self) -> datetime:
    return self._last_run_time

  @last_run_time.setter
  def last_run_time(self, last_run_time: datetime):
    if last_run_time is None:
      del self.last_run_time
      return
    if not isinstance(last_run_time, datetime):
      raise TypeError('last_run_time must be of type datetime')
    self._last_run_time = last_run_time

  @property
  def lines_changed_from_previous(self) -> int:
    return self._lines_changed_from_previous

  @lines_changed_from_previous.setter
  def lines_changed_from_previous(self, lines_changed_from_previous: int):
    if lines_changed_from_previous is None:
      del self.lines_changed_from_previous
      return
    if not isinstance(lines_changed_from_previous, int):
      raise TypeError('lines_changed_from_previous must be of type int')
    self._lines_changed_from_previous = lines_changed_from_previous

  @property
  def lines_deleted_from_previous(self) -> int:
    return self._lines_deleted_from_previous

  @lines_deleted_from_previous.setter
  def lines_deleted_from_previous(self, lines_deleted_from_previous: int):
    if lines_deleted_from_previous is None:
      del self.lines_deleted_from_previous
      return
    if not isinstance(lines_deleted_from_previous, int):
      raise TypeError('lines_deleted_from_previous must be of type int')
    self._lines_deleted_from_previous = lines_deleted_from_previous

  @property
  def lines_inserted_from_previous(self) -> int:
    return self._lines_inserted_from_previous

  @lines_inserted_from_previous.setter
  def lines_inserted_from_previous(self, lines_inserted_from_previous: int):
    if lines_inserted_from_previous is None:
      del self.lines_inserted_from_previous
      return
    if not isinstance(lines_inserted_from_previous, int):
      raise TypeError('lines_inserted_from_previous must be of type int')
    self._lines_inserted_from_previous = lines_inserted_from_previous

  @property
  def output_files_total_size_bytes(self) -> int:
    return self._output_files_total_size_bytes

  @output_files_total_size_bytes.setter
  def output_files_total_size_bytes(self, output_files_total_size_bytes: int):
    if output_files_total_size_bytes is None:
      del self.output_files_total_size_bytes
      return
    if not isinstance(output_files_total_size_bytes, int):
      raise TypeError('output_files_total_size_bytes must be of type int')
    self._output_files_total_size_bytes = output_files_total_size_bytes

  @property
  def run_info(self) -> Optional['KernelVersionRunInfo']:
    return self._run_info

  @run_info.setter
  def run_info(self, run_info: Optional['KernelVersionRunInfo']):
    if run_info is None:
      del self.run_info
      return
    if not isinstance(run_info, KernelVersionRunInfo):
      raise TypeError('run_info must be of type KernelVersionRunInfo')
    self._run_info = run_info

  @property
  def status(self) -> 'KernelWorkerStatus':
    return self._status

  @status.setter
  def status(self, status: 'KernelWorkerStatus'):
    if status is None:
      del self.status
      return
    if not isinstance(status, KernelWorkerStatus):
      raise TypeError('status must be of type KernelWorkerStatus')
    self._status = status

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
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
  def version_number(self) -> int:
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
  def has_version_number(self) -> bool:
    return self._has_version_number

  @has_version_number.setter
  def has_version_number(self, has_version_number: bool):
    if has_version_number is None:
      del self.has_version_number
      return
    if not isinstance(has_version_number, bool):
      raise TypeError('has_version_number must be of type bool')
    self._has_version_number = has_version_number

  @property
  def is_redacted(self) -> bool:
    return self._is_redacted

  @is_redacted.setter
  def is_redacted(self, is_redacted: bool):
    if is_redacted is None:
      del self.is_redacted
      return
    if not isinstance(is_redacted, bool):
      raise TypeError('is_redacted must be of type bool')
    self._is_redacted = is_redacted

  @property
  def version_type(self) -> 'KernelVersionType':
    return self._version_type

  @version_type.setter
  def version_type(self, version_type: 'KernelVersionType'):
    if version_type is None:
      del self.version_type
      return
    if not isinstance(version_type, KernelVersionType):
      raise TypeError('version_type must be of type KernelVersionType')
    self._version_type = version_type


class KernelVersionRunInfo(KaggleObject):
  r"""
  Attributes:
    dockerfile_url (str)
    docker_hub_url (str)
    docker_image_id (str)
    docker_image_name (str)
    exit_code (int)
    failure_message (str)
    is_valid_status (bool)
    run_time_seconds (float)
    succeeded (bool)
    timeout_exceeded (bool)
    used_all_space (bool)
  """

  def __init__(self):
    self._dockerfile_url = None
    self._docker_hub_url = None
    self._docker_image_id = None
    self._docker_image_name = None
    self._exit_code = 0
    self._failure_message = None
    self._is_valid_status = False
    self._run_time_seconds = None
    self._succeeded = False
    self._timeout_exceeded = False
    self._used_all_space = None
    self._freeze()

  @property
  def dockerfile_url(self) -> str:
    return self._dockerfile_url or ""

  @dockerfile_url.setter
  def dockerfile_url(self, dockerfile_url: Optional[str]):
    if dockerfile_url is None:
      del self.dockerfile_url
      return
    if not isinstance(dockerfile_url, str):
      raise TypeError('dockerfile_url must be of type str')
    self._dockerfile_url = dockerfile_url

  @property
  def docker_hub_url(self) -> str:
    return self._docker_hub_url or ""

  @docker_hub_url.setter
  def docker_hub_url(self, docker_hub_url: Optional[str]):
    if docker_hub_url is None:
      del self.docker_hub_url
      return
    if not isinstance(docker_hub_url, str):
      raise TypeError('docker_hub_url must be of type str')
    self._docker_hub_url = docker_hub_url

  @property
  def docker_image_id(self) -> str:
    return self._docker_image_id or ""

  @docker_image_id.setter
  def docker_image_id(self, docker_image_id: Optional[str]):
    if docker_image_id is None:
      del self.docker_image_id
      return
    if not isinstance(docker_image_id, str):
      raise TypeError('docker_image_id must be of type str')
    self._docker_image_id = docker_image_id

  @property
  def docker_image_name(self) -> str:
    return self._docker_image_name or ""

  @docker_image_name.setter
  def docker_image_name(self, docker_image_name: Optional[str]):
    if docker_image_name is None:
      del self.docker_image_name
      return
    if not isinstance(docker_image_name, str):
      raise TypeError('docker_image_name must be of type str')
    self._docker_image_name = docker_image_name

  @property
  def exit_code(self) -> int:
    return self._exit_code

  @exit_code.setter
  def exit_code(self, exit_code: int):
    if exit_code is None:
      del self.exit_code
      return
    if not isinstance(exit_code, int):
      raise TypeError('exit_code must be of type int')
    self._exit_code = exit_code

  @property
  def failure_message(self) -> str:
    return self._failure_message or ""

  @failure_message.setter
  def failure_message(self, failure_message: Optional[str]):
    if failure_message is None:
      del self.failure_message
      return
    if not isinstance(failure_message, str):
      raise TypeError('failure_message must be of type str')
    self._failure_message = failure_message

  @property
  def is_valid_status(self) -> bool:
    return self._is_valid_status

  @is_valid_status.setter
  def is_valid_status(self, is_valid_status: bool):
    if is_valid_status is None:
      del self.is_valid_status
      return
    if not isinstance(is_valid_status, bool):
      raise TypeError('is_valid_status must be of type bool')
    self._is_valid_status = is_valid_status

  @property
  def run_time_seconds(self) -> float:
    return self._run_time_seconds or 0.0

  @run_time_seconds.setter
  def run_time_seconds(self, run_time_seconds: Optional[float]):
    if run_time_seconds is None:
      del self.run_time_seconds
      return
    if not isinstance(run_time_seconds, float):
      raise TypeError('run_time_seconds must be of type float')
    self._run_time_seconds = run_time_seconds

  @property
  def succeeded(self) -> bool:
    return self._succeeded

  @succeeded.setter
  def succeeded(self, succeeded: bool):
    if succeeded is None:
      del self.succeeded
      return
    if not isinstance(succeeded, bool):
      raise TypeError('succeeded must be of type bool')
    self._succeeded = succeeded

  @property
  def timeout_exceeded(self) -> bool:
    return self._timeout_exceeded

  @timeout_exceeded.setter
  def timeout_exceeded(self, timeout_exceeded: bool):
    if timeout_exceeded is None:
      del self.timeout_exceeded
      return
    if not isinstance(timeout_exceeded, bool):
      raise TypeError('timeout_exceeded must be of type bool')
    self._timeout_exceeded = timeout_exceeded

  @property
  def used_all_space(self) -> bool:
    return self._used_all_space or False

  @used_all_space.setter
  def used_all_space(self, used_all_space: Optional[bool]):
    if used_all_space is None:
      del self.used_all_space
      return
    if not isinstance(used_all_space, bool):
      raise TypeError('used_all_space must be of type bool')
    self._used_all_space = used_all_space


class LinkModel(KaggleObject):
  r"""
  Attributes:
    count (int)
    href (str)
    report_event_category (str)
    report_event_type (str)
    show_zero_count_explicitly (bool)
    show_on_mobile (bool)
    tab (str)
    text (str)
    title (str)
  """

  def __init__(self):
    self._count = None
    self._href = None
    self._report_event_category = None
    self._report_event_type = None
    self._show_zero_count_explicitly = False
    self._show_on_mobile = None
    self._tab = None
    self._text = None
    self._title = None
    self._freeze()

  @property
  def count(self) -> int:
    return self._count or 0

  @count.setter
  def count(self, count: Optional[int]):
    if count is None:
      del self.count
      return
    if not isinstance(count, int):
      raise TypeError('count must be of type int')
    self._count = count

  @property
  def href(self) -> str:
    return self._href or ""

  @href.setter
  def href(self, href: Optional[str]):
    if href is None:
      del self.href
      return
    if not isinstance(href, str):
      raise TypeError('href must be of type str')
    self._href = href

  @property
  def report_event_category(self) -> str:
    return self._report_event_category or ""

  @report_event_category.setter
  def report_event_category(self, report_event_category: Optional[str]):
    if report_event_category is None:
      del self.report_event_category
      return
    if not isinstance(report_event_category, str):
      raise TypeError('report_event_category must be of type str')
    self._report_event_category = report_event_category

  @property
  def report_event_type(self) -> str:
    return self._report_event_type or ""

  @report_event_type.setter
  def report_event_type(self, report_event_type: Optional[str]):
    if report_event_type is None:
      del self.report_event_type
      return
    if not isinstance(report_event_type, str):
      raise TypeError('report_event_type must be of type str')
    self._report_event_type = report_event_type

  @property
  def show_zero_count_explicitly(self) -> bool:
    return self._show_zero_count_explicitly

  @show_zero_count_explicitly.setter
  def show_zero_count_explicitly(self, show_zero_count_explicitly: bool):
    if show_zero_count_explicitly is None:
      del self.show_zero_count_explicitly
      return
    if not isinstance(show_zero_count_explicitly, bool):
      raise TypeError('show_zero_count_explicitly must be of type bool')
    self._show_zero_count_explicitly = show_zero_count_explicitly

  @property
  def show_on_mobile(self) -> bool:
    return self._show_on_mobile or False

  @show_on_mobile.setter
  def show_on_mobile(self, show_on_mobile: Optional[bool]):
    if show_on_mobile is None:
      del self.show_on_mobile
      return
    if not isinstance(show_on_mobile, bool):
      raise TypeError('show_on_mobile must be of type bool')
    self._show_on_mobile = show_on_mobile

  @property
  def tab(self) -> str:
    return self._tab or ""

  @tab.setter
  def tab(self, tab: Optional[str]):
    if tab is None:
      del self.tab
      return
    if not isinstance(tab, str):
      raise TypeError('tab must be of type str')
    self._tab = tab

  @property
  def text(self) -> str:
    return self._text or ""

  @text.setter
  def text(self, text: Optional[str]):
    if text is None:
      del self.text
      return
    if not isinstance(text, str):
      raise TypeError('text must be of type str')
    self._text = text

  @property
  def title(self) -> str:
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title


GetKernelViewModelRequest._fields = [
  FieldMetadata("authorUserName", "author_user_name", "_author_user_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelSlug", "kernel_slug", "_kernel_slug", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernelVersionId", "kernel_version_id", "_kernel_version_id", int, 0, PredefinedSerializer()),
  FieldMetadata("tab", "tab", "_tab", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, None, PredefinedSerializer(), optional=True),
]

GetKernelViewModelResponse._fields = [
  FieldMetadata("redirectUrl", "redirect_url", "_redirect_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("kernel", "kernel", "_kernel", Kernel, None, KaggleObjectSerializer()),
  FieldMetadata("kernelRun", "kernel_run", "_kernel_run", KernelRun, None, KaggleObjectSerializer()),
  FieldMetadata("author", "author", "_author", User, None, KaggleObjectSerializer()),
  FieldMetadata("baseUrl", "base_url", "_base_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("collaborators", "collaborators", "_collaborators", CollaboratorList, None, KaggleObjectSerializer()),
  FieldMetadata("initialTab", "initial_tab", "_initial_tab", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("outputFiles", "output_files", "_output_files", KernelSessionOutputFile, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("pageMessages", "page_messages", "_page_messages", PageMessage, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("dataSources", "data_sources", "_data_sources", DataSourceReference, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("renderableDataSources", "renderable_data_sources", "_renderable_data_sources", DataSource, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("downloadAllFilesUrl", "download_all_files_url", "_download_all_files_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("submission", "submission", "_submission", KernelSubmission, None, KaggleObjectSerializer()),
  FieldMetadata("bestSubmissionScore", "best_submission_score", "_best_submission_score", KernelSessionScore, None, KaggleObjectSerializer()),
  FieldMetadata("menuLinks", "menu_links", "_menu_links", LinkModel, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("voteButton", "vote_button", "_vote_button", VoteButton, None, KaggleObjectSerializer()),
  FieldMetadata("canWrite", "can_write", "_can_write", bool, False, PredefinedSerializer()),
  FieldMetadata("currentUserForkParentSessionId", "current_user_fork_parent_session_id", "_current_user_fork_parent_session_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("simplifiedViewer", "simplified_viewer", "_simplified_viewer", bool, False, PredefinedSerializer()),
  FieldMetadata("kernelOutputDataset", "kernel_output_dataset", "_kernel_output_dataset", KernelOutputDatasetReference, None, KaggleObjectSerializer()),
  FieldMetadata("learnSeriesNavigationData", "learn_series_navigation_data", "_learn_series_navigation_data", LearnSeriesNavigationData, None, KaggleObjectSerializer()),
  FieldMetadata("showSharingControls", "show_sharing_controls", "_show_sharing_controls", bool, False, PredefinedSerializer()),
  FieldMetadata("showUnchangedCopyWarning", "show_unchanged_copy_warning", "_show_unchanged_copy_warning", bool, False, PredefinedSerializer()),
  FieldMetadata("moderationStatus", "moderation_status", "_moderation_status", PrivatedModerationStatus, PrivatedModerationStatus.PRIVATED_MODERATION_STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("isReportedBannerDismissed", "is_reported_banner_dismissed", "_is_reported_banner_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("showAdminAllowlist", "show_admin_allowlist", "_show_admin_allowlist", bool, False, PredefinedSerializer()),
  FieldMetadata("isReportedModalDismissed", "is_reported_modal_dismissed", "_is_reported_modal_dismissed", bool, False, PredefinedSerializer()),
  FieldMetadata("failedPackageManagerUrl", "failed_package_manager_url", "_failed_package_manager_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("requirementsFileDownloadUrl", "requirements_file_download_url", "_requirements_file_download_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("description", "description", "_description", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isPackageSession", "is_package_session", "_is_package_session", bool, False, PredefinedSerializer()),
  FieldMetadata("checkNewerColabVersionState", "check_newer_colab_version_state", "_check_newer_colab_version_state", CheckNewerColabVersionResponse, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("kernelOutputModelInstance", "kernel_output_model_instance", "_kernel_output_model_instance", KernelOutputModelInstanceReference, None, KaggleObjectSerializer()),
  FieldMetadata("totalVersionCount", "total_version_count", "_total_version_count", int, 0, PredefinedSerializer()),
  FieldMetadata("currentVersionNumber", "current_version_number", "_current_version_number", int, None, PredefinedSerializer(), optional=True),
]

KernelVersionHistory._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("isForkParent", "is_fork_parent", "_is_fork_parent", bool, False, PredefinedSerializer()),
  FieldMetadata("isNotebook", "is_notebook", "_is_notebook", bool, False, PredefinedSerializer()),
  FieldMetadata("languageName", "language_name", "_language_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("lastRunTime", "last_run_time", "_last_run_time", datetime, None, DateTimeSerializer()),
  FieldMetadata("linesChangedFromPrevious", "lines_changed_from_previous", "_lines_changed_from_previous", int, 0, PredefinedSerializer()),
  FieldMetadata("linesDeletedFromPrevious", "lines_deleted_from_previous", "_lines_deleted_from_previous", int, 0, PredefinedSerializer()),
  FieldMetadata("linesInsertedFromPrevious", "lines_inserted_from_previous", "_lines_inserted_from_previous", int, 0, PredefinedSerializer()),
  FieldMetadata("outputFilesTotalSizeBytes", "output_files_total_size_bytes", "_output_files_total_size_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("runInfo", "run_info", "_run_info", KernelVersionRunInfo, None, KaggleObjectSerializer()),
  FieldMetadata("status", "status", "_status", KernelWorkerStatus, KernelWorkerStatus.QUEUED, EnumSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("versionNumber", "version_number", "_version_number", int, 0, PredefinedSerializer()),
  FieldMetadata("hasVersionNumber", "has_version_number", "_has_version_number", bool, False, PredefinedSerializer()),
  FieldMetadata("isRedacted", "is_redacted", "_is_redacted", bool, False, PredefinedSerializer()),
  FieldMetadata("versionType", "version_type", "_version_type", KernelVersionType, KernelVersionType.KERNEL_VERSION_TYPE_UNSPECIFIED, EnumSerializer()),
]

KernelVersionRunInfo._fields = [
  FieldMetadata("dockerfileUrl", "dockerfile_url", "_dockerfile_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerHubUrl", "docker_hub_url", "_docker_hub_url", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageId", "docker_image_id", "_docker_image_id", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("dockerImageName", "docker_image_name", "_docker_image_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("exitCode", "exit_code", "_exit_code", int, 0, PredefinedSerializer()),
  FieldMetadata("failureMessage", "failure_message", "_failure_message", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("isValidStatus", "is_valid_status", "_is_valid_status", bool, False, PredefinedSerializer()),
  FieldMetadata("runTimeSeconds", "run_time_seconds", "_run_time_seconds", float, None, PredefinedSerializer(), optional=True),
  FieldMetadata("succeeded", "succeeded", "_succeeded", bool, False, PredefinedSerializer()),
  FieldMetadata("timeoutExceeded", "timeout_exceeded", "_timeout_exceeded", bool, False, PredefinedSerializer()),
  FieldMetadata("usedAllSpace", "used_all_space", "_used_all_space", bool, None, PredefinedSerializer(), optional=True),
]

LinkModel._fields = [
  FieldMetadata("count", "count", "_count", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("href", "href", "_href", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reportEventCategory", "report_event_category", "_report_event_category", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("reportEventType", "report_event_type", "_report_event_type", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("showZeroCountExplicitly", "show_zero_count_explicitly", "_show_zero_count_explicitly", bool, False, PredefinedSerializer()),
  FieldMetadata("showOnMobile", "show_on_mobile", "_show_on_mobile", bool, None, PredefinedSerializer(), optional=True),
  FieldMetadata("tab", "tab", "_tab", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("text", "text", "_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
]

