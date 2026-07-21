import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class ExportEnrichedHackathonWriteUpsCsvRequest(KaggleObject):
  r"""
  Attributes:
    competition_id (int)
    competition_name (str)
    cancel (bool)
      Cancels current generation job by deleting marker file but does not cancel
      an already-running generation job and a corresponding CSV file will still
      be generated.
  """

  def __init__(self):
    self._competition_id = None
    self._competition_name = None
    self._cancel = None
    self._freeze()

  @property
  def competition_id(self) -> int:
    return self._competition_id or 0

  @competition_id.setter
  def competition_id(self, competition_id: Optional[int]):
    if competition_id is None:
      del self.competition_id
      return
    if not isinstance(competition_id, int):
      raise TypeError('competition_id must be of type int')
    self._competition_id = competition_id

  @property
  def competition_name(self) -> str:
    return self._competition_name or ""

  @competition_name.setter
  def competition_name(self, competition_name: Optional[str]):
    if competition_name is None:
      del self.competition_name
      return
    if not isinstance(competition_name, str):
      raise TypeError('competition_name must be of type str')
    self._competition_name = competition_name

  @property
  def cancel(self) -> bool:
    r"""
    Cancels current generation job by deleting marker file but does not cancel
    an already-running generation job and a corresponding CSV file will still
    be generated.
    """
    return self._cancel or False

  @cancel.setter
  def cancel(self, cancel: Optional[bool]):
    if cancel is None:
      del self.cancel
      return
    if not isinstance(cancel, bool):
      raise TypeError('cancel must be of type bool')
    self._cancel = cancel

  def endpoint(self):
    path = '/api/v1/competitions/{competition_name}/enriched-hackathon-write-ups-csv'
    return path.format_map(self.to_field_map(self))

  @staticmethod
  def endpoint_path():
    return '/api/v1/competitions/{competition_name}/enriched-hackathon-write-ups-csv'


class ExportEnrichedHackathonWriteUpsCsvResponse(KaggleObject):
  r"""
  Attributes:
    status (ExportEnrichedHackathonWriteUpsCsvResponse.Status)
    signed_url (str)
      TODO(b/533012382): Defer GCS URL signing to the UI
      Signed GCS URL. Only set when status=READY.
  """

  class Status(enum.Enum):
    STATUS_UNSPECIFIED = 0
    READY = 1
    """CSV is available; signed_url is populated."""
    GENERATING = 2
    """Generation was just enqueued or is in progress. Poll again later."""
    CANCELLED = 3
    """The generation marker was cleared in response to cancel=true."""

  def __init__(self):
    self._status = self.Status.STATUS_UNSPECIFIED
    self._signed_url = ""
    self._freeze()

  @property
  def status(self) -> 'ExportEnrichedHackathonWriteUpsCsvResponse.Status':
    return self._status

  @status.setter
  def status(self, status: 'ExportEnrichedHackathonWriteUpsCsvResponse.Status'):
    if status is None:
      del self.status
      return
    if not isinstance(status, ExportEnrichedHackathonWriteUpsCsvResponse.Status):
      raise TypeError('status must be of type ExportEnrichedHackathonWriteUpsCsvResponse.Status')
    self._status = status

  @property
  def signed_url(self) -> str:
    r"""
    TODO(b/533012382): Defer GCS URL signing to the UI
    Signed GCS URL. Only set when status=READY.
    """
    return self._signed_url

  @signed_url.setter
  def signed_url(self, signed_url: str):
    if signed_url is None:
      del self.signed_url
      return
    if not isinstance(signed_url, str):
      raise TypeError('signed_url must be of type str')
    self._signed_url = signed_url

  @property
  def signedUrl(self):
    return self.signed_url


ExportEnrichedHackathonWriteUpsCsvRequest._fields = [
  FieldMetadata("competitionId", "competition_id", "_competition_id", int, None, PredefinedSerializer(), optional=True),
  FieldMetadata("competitionName", "competition_name", "_competition_name", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("cancel", "cancel", "_cancel", bool, None, PredefinedSerializer(), optional=True),
]

ExportEnrichedHackathonWriteUpsCsvResponse._fields = [
  FieldMetadata("status", "status", "_status", ExportEnrichedHackathonWriteUpsCsvResponse.Status, ExportEnrichedHackathonWriteUpsCsvResponse.Status.STATUS_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("signedUrl", "signed_url", "_signed_url", str, "", PredefinedSerializer()),
]

