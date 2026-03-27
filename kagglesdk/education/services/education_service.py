from kagglesdk.education.types.education_service import AddLessonsToTrackRequest, Certificate, EditLessonRequest, GetCertificateRequest, GetExerciseVersionsRequest, GetExerciseVersionsResponse, GetLearnCertificateUploadUrlRequest, GetLearnCertificateUploadUrlResponse, GetTrackRequest, GetTracksRequest, GetTracksResponse, LearnLesson, LearnTrack, ReorderTracksRequest, ReorderTracksResponse, RescoreExerciseVersionRequest, RescoreResponse, TrackEducationRequest, TrackExerciseInteractionRequest, TrackExerciseInteractionResponse
from kagglesdk.kaggle_http_client import KaggleHttpClient

class EducationClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def add_lessons_to_track(self, request: AddLessonsToTrackRequest = None) -> LearnTrack:
    r"""
    Args:
      request (AddLessonsToTrackRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = AddLessonsToTrackRequest()

    return self._client.call("education.EducationService", "AddLessonsToTrack", request, LearnTrack)

  def get_certificate(self, request: GetCertificateRequest = None) -> Certificate:
    r"""
    Args:
      request (GetCertificateRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCertificateRequest()

    return self._client.call("education.EducationService", "GetCertificate", request, Certificate)

  def get_learn_certificate_upload_url(self, request: GetLearnCertificateUploadUrlRequest = None) -> GetLearnCertificateUploadUrlResponse:
    r"""
    Args:
      request (GetLearnCertificateUploadUrlRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetLearnCertificateUploadUrlRequest()

    return self._client.call("education.EducationService", "GetLearnCertificateUploadUrl", request, GetLearnCertificateUploadUrlResponse)

  def get_exercise_versions(self, request: GetExerciseVersionsRequest = None) -> GetExerciseVersionsResponse:
    r"""
    Args:
      request (GetExerciseVersionsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetExerciseVersionsRequest()

    return self._client.call("education.EducationService", "GetExerciseVersions", request, GetExerciseVersionsResponse)

  def get_tracks(self, request: GetTracksRequest = None) -> GetTracksResponse:
    r"""
    Args:
      request (GetTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTracksRequest()

    return self._client.call("education.EducationService", "GetTracks", request, GetTracksResponse)

  def get_track(self, request: GetTrackRequest = None) -> LearnTrack:
    r"""
    Args:
      request (GetTrackRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetTrackRequest()

    return self._client.call("education.EducationService", "GetTrack", request, LearnTrack)

  def reorder_tracks(self, request: ReorderTracksRequest = None) -> ReorderTracksResponse:
    r"""
    Args:
      request (ReorderTracksRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ReorderTracksRequest()

    return self._client.call("education.EducationService", "ReorderTracks", request, ReorderTracksResponse)

  def rescore_exercise_version(self, request: RescoreExerciseVersionRequest = None) -> RescoreResponse:
    r"""
    Args:
      request (RescoreExerciseVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RescoreExerciseVersionRequest()

    return self._client.call("education.EducationService", "RescoreExerciseVersion", request, RescoreResponse)

  def track_education(self, request: TrackEducationRequest = None):
    r"""
    Args:
      request (TrackEducationRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TrackEducationRequest()

    self._client.call("education.EducationService", "TrackEducation", request, None)

  def track_exercise_interaction(self, request: TrackExerciseInteractionRequest = None) -> TrackExerciseInteractionResponse:
    r"""
    Args:
      request (TrackExerciseInteractionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = TrackExerciseInteractionRequest()

    return self._client.call("education.EducationService", "TrackExerciseInteraction", request, TrackExerciseInteractionResponse)

  def edit_lesson(self, request: EditLessonRequest = None) -> LearnLesson:
    r"""
    Args:
      request (EditLessonRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = EditLessonRequest()

    return self._client.call("education.EducationService", "EditLesson", request, LearnLesson)
