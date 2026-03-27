import enum
from kagglesdk.kaggle_object import *
from typing import Optional

class HatsLocation(enum.Enum):
  HATS_LOCATION_UNSPECIFIED = 0
  HOMEPAGE = 1
  COMPETITIONS = 2
  DATASETS = 3
  NOTEBOOKS = 4
  COURSES = 5
  DISCUSSIONS = 6
  MODELS = 7

class SurveyType(enum.Enum):
  SURVEY_TYPE_UNSPECIFIED = 0
  SURVEY_TYPE_HATS = 1
  SURVEY_TYPE_DATA_SCIENCE_AND_MACHINE_LEARNING_SURVEY = 2

class DismissHatsRequest(KaggleObject):
  r"""
  Attributes:
    location (HatsLocation)
    user_clicked_link (bool)
  """

  def __init__(self):
    self._location = HatsLocation.HATS_LOCATION_UNSPECIFIED
    self._user_clicked_link = False
    self._freeze()

  @property
  def location(self) -> 'HatsLocation':
    return self._location

  @location.setter
  def location(self, location: 'HatsLocation'):
    if location is None:
      del self.location
      return
    if not isinstance(location, HatsLocation):
      raise TypeError('location must be of type HatsLocation')
    self._location = location

  @property
  def user_clicked_link(self) -> bool:
    return self._user_clicked_link

  @user_clicked_link.setter
  def user_clicked_link(self, user_clicked_link: bool):
    if user_clicked_link is None:
      del self.user_clicked_link
      return
    if not isinstance(user_clicked_link, bool):
      raise TypeError('user_clicked_link must be of type bool')
    self._user_clicked_link = user_clicked_link


class DismissHatsResponse(KaggleObject):
  r"""
  """

  pass

class DismissSurveyRequest(KaggleObject):
  r"""
  Attributes:
    location (HatsLocation)
    user_clicked_survey (bool)
    survey_type (SurveyType)
  """

  def __init__(self):
    self._location = HatsLocation.HATS_LOCATION_UNSPECIFIED
    self._user_clicked_survey = False
    self._survey_type = SurveyType.SURVEY_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def location(self) -> 'HatsLocation':
    return self._location

  @location.setter
  def location(self, location: 'HatsLocation'):
    if location is None:
      del self.location
      return
    if not isinstance(location, HatsLocation):
      raise TypeError('location must be of type HatsLocation')
    self._location = location

  @property
  def user_clicked_survey(self) -> bool:
    return self._user_clicked_survey

  @user_clicked_survey.setter
  def user_clicked_survey(self, user_clicked_survey: bool):
    if user_clicked_survey is None:
      del self.user_clicked_survey
      return
    if not isinstance(user_clicked_survey, bool):
      raise TypeError('user_clicked_survey must be of type bool')
    self._user_clicked_survey = user_clicked_survey

  @property
  def survey_type(self) -> 'SurveyType':
    return self._survey_type

  @survey_type.setter
  def survey_type(self, survey_type: 'SurveyType'):
    if survey_type is None:
      del self.survey_type
      return
    if not isinstance(survey_type, SurveyType):
      raise TypeError('survey_type must be of type SurveyType')
    self._survey_type = survey_type


class DismissSurveyResponse(KaggleObject):
  r"""
  """

  pass

class GetUserHatsStatusRequest(KaggleObject):
  r"""
  Attributes:
    location (HatsLocation)
  """

  def __init__(self):
    self._location = HatsLocation.HATS_LOCATION_UNSPECIFIED
    self._freeze()

  @property
  def location(self) -> 'HatsLocation':
    return self._location

  @location.setter
  def location(self, location: 'HatsLocation'):
    if location is None:
      del self.location
      return
    if not isinstance(location, HatsLocation):
      raise TypeError('location must be of type HatsLocation')
    self._location = location


class GetUserHatsStatusResponse(KaggleObject):
  r"""
  Attributes:
    show_prompt (bool)
      Deprecated: use survey_type enum instead
    show_diversity_study_prompt (bool)
      Deprecated: used to show the 2020 diversity study
    survey_type (SurveyType)
      What type of survey to show
  """

  def __init__(self):
    self._show_prompt = False
    self._show_diversity_study_prompt = False
    self._survey_type = SurveyType.SURVEY_TYPE_UNSPECIFIED
    self._freeze()

  @property
  def show_prompt(self) -> bool:
    """Deprecated: use survey_type enum instead"""
    return self._show_prompt

  @show_prompt.setter
  def show_prompt(self, show_prompt: bool):
    if show_prompt is None:
      del self.show_prompt
      return
    if not isinstance(show_prompt, bool):
      raise TypeError('show_prompt must be of type bool')
    self._show_prompt = show_prompt

  @property
  def show_diversity_study_prompt(self) -> bool:
    """Deprecated: used to show the 2020 diversity study"""
    return self._show_diversity_study_prompt

  @show_diversity_study_prompt.setter
  def show_diversity_study_prompt(self, show_diversity_study_prompt: bool):
    if show_diversity_study_prompt is None:
      del self.show_diversity_study_prompt
      return
    if not isinstance(show_diversity_study_prompt, bool):
      raise TypeError('show_diversity_study_prompt must be of type bool')
    self._show_diversity_study_prompt = show_diversity_study_prompt

  @property
  def survey_type(self) -> 'SurveyType':
    """What type of survey to show"""
    return self._survey_type

  @survey_type.setter
  def survey_type(self, survey_type: 'SurveyType'):
    if survey_type is None:
      del self.survey_type
      return
    if not isinstance(survey_type, SurveyType):
      raise TypeError('survey_type must be of type SurveyType')
    self._survey_type = survey_type


DismissHatsRequest._fields = [
  FieldMetadata("location", "location", "_location", HatsLocation, HatsLocation.HATS_LOCATION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userClickedLink", "user_clicked_link", "_user_clicked_link", bool, False, PredefinedSerializer()),
]

DismissHatsResponse._fields = []

DismissSurveyRequest._fields = [
  FieldMetadata("location", "location", "_location", HatsLocation, HatsLocation.HATS_LOCATION_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("userClickedSurvey", "user_clicked_survey", "_user_clicked_survey", bool, False, PredefinedSerializer()),
  FieldMetadata("surveyType", "survey_type", "_survey_type", SurveyType, SurveyType.SURVEY_TYPE_UNSPECIFIED, EnumSerializer()),
]

DismissSurveyResponse._fields = []

GetUserHatsStatusRequest._fields = [
  FieldMetadata("location", "location", "_location", HatsLocation, HatsLocation.HATS_LOCATION_UNSPECIFIED, EnumSerializer()),
]

GetUserHatsStatusResponse._fields = [
  FieldMetadata("showPrompt", "show_prompt", "_show_prompt", bool, False, PredefinedSerializer()),
  FieldMetadata("showDiversityStudyPrompt", "show_diversity_study_prompt", "_show_diversity_study_prompt", bool, False, PredefinedSerializer()),
  FieldMetadata("surveyType", "survey_type", "_survey_type", SurveyType, SurveyType.SURVEY_TYPE_UNSPECIFIED, EnumSerializer()),
]

