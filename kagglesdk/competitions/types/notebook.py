from kagglesdk.kaggle_object import *
from typing import Optional

class CompetitionNotebook(KaggleObject):
  r"""
  Attributes:
    submission_id (int)
      The submissionId linked to this Notebook.
    title (str)
      The title of the Notebook.
    kernel_run_id (int)
      Denotes the specific Notebook Version; can optionally be part of the URL.
    author_user_name (str)
      The author of the Notebook; part of the Notebook's URL.
    slug (str)
      Slug of the Notebook, like `notebook-title`; part of the Notebook's URL.
    version (int)
      Version of the Notebook. Note this may not exist in some cases, and is not
      populated by GetLeaderboard since it is not used and we want to optimize
      performance there.
    version_name (str)
      Version title of the Notebook.
  """

  def __init__(self):
    self._submission_id = 0
    self._title = ""
    self._kernel_run_id = 0
    self._author_user_name = ""
    self._slug = ""
    self._version = None
    self._version_name = None
    self._freeze()

  @property
  def submission_id(self) -> int:
    """The submissionId linked to this Notebook."""
    return self._submission_id

  @submission_id.setter
  def submission_id(self, submission_id: int):
    if submission_id is None:
      del self.submission_id
      return
    if not isinstance(submission_id, int):
      raise TypeError('submission_id must be of type int')
    self._submission_id = submission_id

  @property
  def title(self) -> str:
    """The title of the Notebook."""
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
  def kernel_run_id(self) -> int:
    """Denotes the specific Notebook Version; can optionally be part of the URL."""
    return self._kernel_run_id

  @kernel_run_id.setter
  def kernel_run_id(self, kernel_run_id: int):
    if kernel_run_id is None:
      del self.kernel_run_id
      return
    if not isinstance(kernel_run_id, int):
      raise TypeError('kernel_run_id must be of type int')
    self._kernel_run_id = kernel_run_id

  @property
  def author_user_name(self) -> str:
    """The author of the Notebook; part of the Notebook's URL."""
    return self._author_user_name

  @author_user_name.setter
  def author_user_name(self, author_user_name: str):
    if author_user_name is None:
      del self.author_user_name
      return
    if not isinstance(author_user_name, str):
      raise TypeError('author_user_name must be of type str')
    self._author_user_name = author_user_name

  @property
  def slug(self) -> str:
    """Slug of the Notebook, like `notebook-title`; part of the Notebook's URL."""
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
  def version(self) -> int:
    r"""
    Version of the Notebook. Note this may not exist in some cases, and is not
    populated by GetLeaderboard since it is not used and we want to optimize
    performance there.
    """
    return self._version or 0

  @version.setter
  def version(self, version: Optional[int]):
    if version is None:
      del self.version
      return
    if not isinstance(version, int):
      raise TypeError('version must be of type int')
    self._version = version

  @property
  def version_name(self) -> str:
    """Version title of the Notebook."""
    return self._version_name or ""

  @version_name.setter
  def version_name(self, version_name: Optional[str]):
    if version_name is None:
      del self.version_name
      return
    if not isinstance(version_name, str):
      raise TypeError('version_name must be of type str')
    self._version_name = version_name


CompetitionNotebook._fields = [
  FieldMetadata("submissionId", "submission_id", "_submission_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, "", PredefinedSerializer()),
  FieldMetadata("kernelRunId", "kernel_run_id", "_kernel_run_id", int, 0, PredefinedSerializer()),
  FieldMetadata("authorUserName", "author_user_name", "_author_user_name", str, "", PredefinedSerializer()),
  FieldMetadata("slug", "slug", "_slug", str, "", PredefinedSerializer()),
  FieldMetadata("version", "version", "_version", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("versionName", "version_name", "_version_name", str, None, PredefinedSerializer(), optional=True),
]

