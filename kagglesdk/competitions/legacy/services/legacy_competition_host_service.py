from kagglesdk.competitions.legacy.types.legacy_background_operation import BackgroundOperation
from kagglesdk.competitions.legacy.types.legacy_competition_host_service import CompetitionSettings, GetHostChecklistRequest, GetHostEvaluationInfoRequest, HostChecklist, HostEvaluationInfo, InvalidateSubmissionsRequest, UpdateCompetitionSettingsRequest, UpdateSolutionColumnMappingRequest, UpdateSubmissionColumnMappingRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class LegacyCompetitionHostClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def update_competition_settings(self, request: UpdateCompetitionSettingsRequest = None) -> CompetitionSettings:
    r"""
    Args:
      request (UpdateCompetitionSettingsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionSettingsRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "UpdateCompetitionSettings", request, CompetitionSettings)

  def get_host_evaluation_info(self, request: GetHostEvaluationInfoRequest = None) -> HostEvaluationInfo:
    r"""
    Args:
      request (GetHostEvaluationInfoRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHostEvaluationInfoRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "GetHostEvaluationInfo", request, HostEvaluationInfo)

  def update_submission_column_mapping(self, request: UpdateSubmissionColumnMappingRequest = None) -> BackgroundOperation:
    r"""
    Args:
      request (UpdateSubmissionColumnMappingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSubmissionColumnMappingRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "UpdateSubmissionColumnMapping", request, BackgroundOperation)

  def update_solution_column_mapping(self, request: UpdateSolutionColumnMappingRequest = None) -> BackgroundOperation:
    r"""
    Args:
      request (UpdateSolutionColumnMappingRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateSolutionColumnMappingRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "UpdateSolutionColumnMapping", request, BackgroundOperation)

  def get_host_checklist(self, request: GetHostChecklistRequest = None) -> HostChecklist:
    r"""
    Gets details to render the host checklist page.

    Args:
      request (GetHostChecklistRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetHostChecklistRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "GetHostChecklist", request, HostChecklist)

  def invalidate_submissions(self, request: InvalidateSubmissionsRequest = None) -> BackgroundOperation:
    r"""
    Args:
      request (InvalidateSubmissionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = InvalidateSubmissionsRequest()

    return self._client.call("competitions.legacy.LegacyCompetitionHostService", "InvalidateSubmissions", request, BackgroundOperation)
