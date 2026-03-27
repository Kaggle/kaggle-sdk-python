from kagglesdk.competitions.types.hackathon_service import AddJudgeRequest, AssignPrizeRequest, CheckHackathonWriteupConflictRequest, CheckHackathonWriteupConflictResponse, CreateHackathonWriteUpRequest, DeleteHackathonWriteUpRequest, FinalizeHackathonPrizesRequest, GetCompetitionHackathonSettingsRequest, GetHackathonDeadlineTimeRequest, GetHackathonDeadlineTimeResponse, GetHackathonWriteupChecklistRequest, GetHackathonWriteUpRequest, HackathonWriteupChecklist, ListHackathonTracksRequest, ListHackathonTracksResponse, ListHackathonWriteUpsRequest, ListHackathonWriteUpsResponse, ListJudgesRequest, ListJudgesResponse, RemoveJudgeRequest, UpdateCompetitionHackathonSettingsRequest, UpdateHackathonTracksRequest, UpdateHackathonWriteUpRequest
from kagglesdk.competitions.types.hackathons import CompetitionHackathonSettings, HackathonWriteUp
from kagglesdk.kaggle_http_client import KaggleHttpClient

class HackathonClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def update_hackathon_tracks(self, request: UpdateHackathonTracksRequest = None):
    r"""
    Args:
      request (UpdateHackathonTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateHackathonTracksRequest()

    self._client.call("competitions.HackathonService", "UpdateHackathonTracks", request, None)

  def list_hackathon_tracks(self, request: ListHackathonTracksRequest = None) -> ListHackathonTracksResponse:
    r"""
    Args:
      request (ListHackathonTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListHackathonTracksRequest()

    return self._client.call("competitions.HackathonService", "ListHackathonTracks", request, ListHackathonTracksResponse)

  def add_judge(self, request: AddJudgeRequest = None):
    r"""
    Args:
      request (AddJudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddJudgeRequest()

    self._client.call("competitions.HackathonService", "AddJudge", request, None)

  def remove_judge(self, request: RemoveJudgeRequest = None):
    r"""
    Args:
      request (RemoveJudgeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RemoveJudgeRequest()

    self._client.call("competitions.HackathonService", "RemoveJudge", request, None)

  def list_judges(self, request: ListJudgesRequest = None) -> ListJudgesResponse:
    r"""
    Args:
      request (ListJudgesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListJudgesRequest()

    return self._client.call("competitions.HackathonService", "ListJudges", request, ListJudgesResponse)

  def update_competition_hackathon_settings(self, request: UpdateCompetitionHackathonSettingsRequest = None):
    r"""
    Args:
      request (UpdateCompetitionHackathonSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionHackathonSettingsRequest()

    self._client.call("competitions.HackathonService", "UpdateCompetitionHackathonSettings", request, None)

  def update_hackathon_write_up(self, request: UpdateHackathonWriteUpRequest = None) -> HackathonWriteUp:
    r"""
    Args:
      request (UpdateHackathonWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateHackathonWriteUpRequest()

    return self._client.call("competitions.HackathonService", "UpdateHackathonWriteUp", request, HackathonWriteUp)

  def create_hackathon_write_up(self, request: CreateHackathonWriteUpRequest = None) -> HackathonWriteUp:
    r"""
    Args:
      request (CreateHackathonWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateHackathonWriteUpRequest()

    return self._client.call("competitions.HackathonService", "CreateHackathonWriteUp", request, HackathonWriteUp)

  def get_hackathon_write_up(self, request: GetHackathonWriteUpRequest = None) -> HackathonWriteUp:
    r"""
    Args:
      request (GetHackathonWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHackathonWriteUpRequest()

    return self._client.call("competitions.HackathonService", "GetHackathonWriteUp", request, HackathonWriteUp)

  def delete_hackathon_write_up(self, request: DeleteHackathonWriteUpRequest = None):
    r"""
    Args:
      request (DeleteHackathonWriteUpRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = DeleteHackathonWriteUpRequest()

    self._client.call("competitions.HackathonService", "DeleteHackathonWriteUp", request, None)

  def assign_prize(self, request: AssignPrizeRequest = None):
    r"""
    Args:
      request (AssignPrizeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AssignPrizeRequest()

    self._client.call("competitions.HackathonService", "AssignPrize", request, None)

  def list_hackathon_write_ups(self, request: ListHackathonWriteUpsRequest = None) -> ListHackathonWriteUpsResponse:
    r"""
    Args:
      request (ListHackathonWriteUpsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListHackathonWriteUpsRequest()

    return self._client.call("competitions.HackathonService", "ListHackathonWriteUps", request, ListHackathonWriteUpsResponse)

  def get_competition_hackathon_settings(self, request: GetCompetitionHackathonSettingsRequest = None) -> CompetitionHackathonSettings:
    r"""
    Args:
      request (GetCompetitionHackathonSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionHackathonSettingsRequest()

    return self._client.call("competitions.HackathonService", "GetCompetitionHackathonSettings", request, CompetitionHackathonSettings)

  def finalize_hackathon_prizes(self, request: FinalizeHackathonPrizesRequest = None):
    r"""
    Args:
      request (FinalizeHackathonPrizesRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = FinalizeHackathonPrizesRequest()

    self._client.call("competitions.HackathonService", "FinalizeHackathonPrizes", request, None)

  def get_hackathon_writeup_checklist(self, request: GetHackathonWriteupChecklistRequest = None) -> HackathonWriteupChecklist:
    r"""
    Args:
      request (GetHackathonWriteupChecklistRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHackathonWriteupChecklistRequest()

    return self._client.call("competitions.HackathonService", "GetHackathonWriteupChecklist", request, HackathonWriteupChecklist)

  def check_hackathon_writeup_conflict(self, request: CheckHackathonWriteupConflictRequest = None) -> CheckHackathonWriteupConflictResponse:
    r"""
    Args:
      request (CheckHackathonWriteupConflictRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CheckHackathonWriteupConflictRequest()

    return self._client.call("competitions.HackathonService", "CheckHackathonWriteupConflict", request, CheckHackathonWriteupConflictResponse)

  def get_hackathon_deadline_time(self, request: GetHackathonDeadlineTimeRequest = None) -> GetHackathonDeadlineTimeResponse:
    r"""
    Args:
      request (GetHackathonDeadlineTimeRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHackathonDeadlineTimeRequest()

    return self._client.call("competitions.HackathonService", "GetHackathonDeadlineTime", request, GetHackathonDeadlineTimeResponse)
