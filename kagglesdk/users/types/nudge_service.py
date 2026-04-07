import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class CheckResult(enum.Enum):
  CHECK_RESULT_UNDEFINED = 0
  OK = 1
  CUSTOM_NUDGES_DISABLED = 2
  """Negative check result causes:"""
  DATASET_FEEDBACKS_NUDGES_DISABLED = 3
  CAN_SEE_EXPRESSION = 4
  NOT_FOUND = 5
  USER_AADC = 6
  USER_SEEN_ALREADY = 7

class NudgePage(enum.Enum):
  NUDGE_PAGE_ANY = 0
  NUDGE_PAGE_COMPETITIONS = 1
  NUDGE_PAGE_PROFILE = 2
  NUDGE_PAGE_LANDING = 3
  NUDGE_PAGE_DATASETS = 4
  NUDGE_PAGE_EDITOR = 5

class NudgeReactions(enum.Enum):
  REASON_UNSPECIFIED = 0
  USER_DISMISSED = 1
  ACCEPTED = 2
  AUTO_DISMISSED = 3

class AddNudgeRequest(KaggleObject):
  r"""
  Attributes:
    name (str)
      The name to use for the nudge (is used as a key)
  """

  def __init__(self):
    self._name = ""
    self._freeze()

  @property
  def name(self) -> str:
    """The name to use for the nudge (is used as a key)"""
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name


class AddNudgeResponse(KaggleObject):
  r"""
  Attributes:
    nudge_id (int)
      The id of the newly created nudge.
  """

  def __init__(self):
    self._nudge_id = 0
    self._freeze()

  @property
  def nudge_id(self) -> int:
    """The id of the newly created nudge."""
    return self._nudge_id

  @nudge_id.setter
  def nudge_id(self, nudge_id: int):
    if nudge_id is None:
      del self.nudge_id
      return
    if not isinstance(nudge_id, int):
      raise TypeError('nudge_id must be of type int')
    self._nudge_id = nudge_id


class CheckCustomNudgeRequest(KaggleObject):
  r"""
  Attributes:
    nudge_id (int)
      Id of custom nudge to check for. Built-in nudges return a NOT_FOUND check
      result.
    variant (int)
      What variant of the custom nudge to check for. Ignored if null.
  """

  def __init__(self):
    self._nudge_id = 0
    self._variant = None
    self._freeze()

  @property
  def nudge_id(self) -> int:
    r"""
    Id of custom nudge to check for. Built-in nudges return a NOT_FOUND check
    result.
    """
    return self._nudge_id

  @nudge_id.setter
  def nudge_id(self, nudge_id: int):
    if nudge_id is None:
      del self.nudge_id
      return
    if not isinstance(nudge_id, int):
      raise TypeError('nudge_id must be of type int')
    self._nudge_id = nudge_id

  @property
  def variant(self) -> int:
    """What variant of the custom nudge to check for. Ignored if null."""
    return self._variant or 0

  @variant.setter
  def variant(self, variant: Optional[int]):
    if variant is None:
      del self.variant
      return
    if not isinstance(variant, int):
      raise TypeError('variant must be of type int')
    self._variant = variant


class CheckCustomNudgeResponse(KaggleObject):
  r"""
  Attributes:
    check_result (CheckResult)
  """

  def __init__(self):
    self._check_result = CheckResult.CHECK_RESULT_UNDEFINED
    self._freeze()

  @property
  def check_result(self) -> 'CheckResult':
    return self._check_result

  @check_result.setter
  def check_result(self, check_result: 'CheckResult'):
    if check_result is None:
      del self.check_result
      return
    if not isinstance(check_result, CheckResult):
      raise TypeError('check_result must be of type CheckResult')
    self._check_result = check_result


class CheckForNudgeRequest(KaggleObject):
  r"""
  """

  pass

class CheckForNudgeResponse(KaggleObject):
  r"""
  Attributes:
    potential_nudges (PotentialNudge)
  """

  def __init__(self):
    self._potential_nudges = []
    self._freeze()

  @property
  def potential_nudges(self) -> Optional[List[Optional['PotentialNudge']]]:
    return self._potential_nudges

  @potential_nudges.setter
  def potential_nudges(self, potential_nudges: Optional[List[Optional['PotentialNudge']]]):
    if potential_nudges is None:
      del self.potential_nudges
      return
    if not isinstance(potential_nudges, list):
      raise TypeError('potential_nudges must be of type list')
    if not all([isinstance(t, PotentialNudge) for t in potential_nudges]):
      raise TypeError('potential_nudges must contain only items of type PotentialNudge')
    self._potential_nudges = potential_nudges


class GetNudgeConfigRequest(KaggleObject):
  r"""
  """

  pass

class GetNudgeConfigResponse(KaggleObject):
  r"""
  Attributes:
    nudges (NudgeConfig)
      All of the nudges defined in the system.
  """

  def __init__(self):
    self._nudges = []
    self._freeze()

  @property
  def nudges(self) -> Optional[List[Optional['NudgeConfig']]]:
    """All of the nudges defined in the system."""
    return self._nudges

  @nudges.setter
  def nudges(self, nudges: Optional[List[Optional['NudgeConfig']]]):
    if nudges is None:
      del self.nudges
      return
    if not isinstance(nudges, list):
      raise TypeError('nudges must be of type list')
    if not all([isinstance(t, NudgeConfig) for t in nudges]):
      raise TypeError('nudges must contain only items of type NudgeConfig')
    self._nudges = nudges


class NudgeConfig(KaggleObject):
  r"""
  Attributes:
    nudge_id (int)
      The internal id of the nudge, to be used by auto-form.
    type (str)
      The type of the nudge.
    is_built_in (bool)
      Whether this nudge is a built-in nudge (and thus not editable).
    showing_nudge_response (ShowingNudgeResponse)
      The FE should mock out the ShowingNudge handler and use this instead.
  """

  def __init__(self):
    self._nudge_id = 0
    self._type = ""
    self._is_built_in = False
    self._showing_nudge_response = None
    self._freeze()

  @property
  def nudge_id(self) -> int:
    """The internal id of the nudge, to be used by auto-form."""
    return self._nudge_id

  @nudge_id.setter
  def nudge_id(self, nudge_id: int):
    if nudge_id is None:
      del self.nudge_id
      return
    if not isinstance(nudge_id, int):
      raise TypeError('nudge_id must be of type int')
    self._nudge_id = nudge_id

  @property
  def type(self) -> str:
    """The type of the nudge."""
    return self._type

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type

  @property
  def is_built_in(self) -> bool:
    """Whether this nudge is a built-in nudge (and thus not editable)."""
    return self._is_built_in

  @is_built_in.setter
  def is_built_in(self, is_built_in: bool):
    if is_built_in is None:
      del self.is_built_in
      return
    if not isinstance(is_built_in, bool):
      raise TypeError('is_built_in must be of type bool')
    self._is_built_in = is_built_in

  @property
  def showing_nudge_response(self) -> Optional['ShowingNudgeResponse']:
    """The FE should mock out the ShowingNudge handler and use this instead."""
    return self._showing_nudge_response

  @showing_nudge_response.setter
  def showing_nudge_response(self, showing_nudge_response: Optional['ShowingNudgeResponse']):
    if showing_nudge_response is None:
      del self.showing_nudge_response
      return
    if not isinstance(showing_nudge_response, ShowingNudgeResponse):
      raise TypeError('showing_nudge_response must be of type ShowingNudgeResponse')
    self._showing_nudge_response = showing_nudge_response


class PotentialNudge(KaggleObject):
  r"""
  Attributes:
    type (str)
      What kind of nudge to show (or NO_NUDGE).
    page (NudgePage)
      the pages that this nudge is allowed to show on
    priority (int)
      what priority value to use when evaluating which nudge to show to user.
      Higher priority value == more important
    variant (int)
      What variant this nudge is. Variants are different versions of the same
      nudge Currently no display differences between variants, it's only for
      selecting different groups of users
  """

  def __init__(self):
    self._type = ""
    self._page = NudgePage.NUDGE_PAGE_ANY
    self._priority = 0
    self._variant = None
    self._freeze()

  @property
  def type(self) -> str:
    """What kind of nudge to show (or NO_NUDGE)."""
    return self._type

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type

  @property
  def page(self) -> 'NudgePage':
    """the pages that this nudge is allowed to show on"""
    return self._page

  @page.setter
  def page(self, page: 'NudgePage'):
    if page is None:
      del self.page
      return
    if not isinstance(page, NudgePage):
      raise TypeError('page must be of type NudgePage')
    self._page = page

  @property
  def priority(self) -> int:
    r"""
    what priority value to use when evaluating which nudge to show to user.
    Higher priority value == more important
    """
    return self._priority

  @priority.setter
  def priority(self, priority: int):
    if priority is None:
      del self.priority
      return
    if not isinstance(priority, int):
      raise TypeError('priority must be of type int')
    self._priority = priority

  @property
  def variant(self) -> int:
    r"""
    What variant this nudge is. Variants are different versions of the same
    nudge Currently no display differences between variants, it's only for
    selecting different groups of users
    """
    return self._variant or 0

  @variant.setter
  def variant(self, variant: Optional[int]):
    if variant is None:
      del self.variant
      return
    if not isinstance(variant, int):
      raise TypeError('variant must be of type int')
    self._variant = variant


class ReactToNudgeRequest(KaggleObject):
  r"""
  Attributes:
    nudge_id (int)
      Which nudge to dismiss
    reaction (NudgeReactions)
      Whether the user acted upon the nudge (clicked the call to action) or just
      dismissed it
    dont_show_again (bool)
      Whether the user wants these messages to never show for them again
  """

  def __init__(self):
    self._nudge_id = 0
    self._reaction = NudgeReactions.REASON_UNSPECIFIED
    self._dont_show_again = False
    self._freeze()

  @property
  def nudge_id(self) -> int:
    """Which nudge to dismiss"""
    return self._nudge_id

  @nudge_id.setter
  def nudge_id(self, nudge_id: int):
    if nudge_id is None:
      del self.nudge_id
      return
    if not isinstance(nudge_id, int):
      raise TypeError('nudge_id must be of type int')
    self._nudge_id = nudge_id

  @property
  def reaction(self) -> 'NudgeReactions':
    r"""
    Whether the user acted upon the nudge (clicked the call to action) or just
    dismissed it
    """
    return self._reaction

  @reaction.setter
  def reaction(self, reaction: 'NudgeReactions'):
    if reaction is None:
      del self.reaction
      return
    if not isinstance(reaction, NudgeReactions):
      raise TypeError('reaction must be of type NudgeReactions')
    self._reaction = reaction

  @property
  def dont_show_again(self) -> bool:
    """Whether the user wants these messages to never show for them again"""
    return self._dont_show_again

  @dont_show_again.setter
  def dont_show_again(self, dont_show_again: bool):
    if dont_show_again is None:
      del self.dont_show_again
      return
    if not isinstance(dont_show_again, bool):
      raise TypeError('dont_show_again must be of type bool')
    self._dont_show_again = dont_show_again


class ReactToNudgeResponse(KaggleObject):
  r"""
  """

  pass

class ShowingNudgeRequest(KaggleObject):
  r"""
  Attributes:
    type (str)
      type of the nudge that the user will see.
    variant (int)
      What variant the user will see
  """

  def __init__(self):
    self._type = ""
    self._variant = None
    self._freeze()

  @property
  def type(self) -> str:
    """type of the nudge that the user will see."""
    return self._type

  @type.setter
  def type(self, type: str):
    if type is None:
      del self.type
      return
    if not isinstance(type, str):
      raise TypeError('type must be of type str')
    self._type = type

  @property
  def variant(self) -> int:
    """What variant the user will see"""
    return self._variant or 0

  @variant.setter
  def variant(self, variant: Optional[int]):
    if variant is None:
      del self.variant
      return
    if not isinstance(variant, int):
      raise TypeError('variant must be of type int')
    self._variant = variant


class ShowingNudgeResponse(KaggleObject):
  r"""
  Attributes:
    user_nudge_id (int)
      Unique Id to identify the nudge, used to dismiss
      If value is 0 then this is a duplicate and the nudge should not be shown to
      the user
    title (str)
      Note the following fields are only populated for custom nudges. Built-in
      nudges are already defined on the FE. The title/header of the nudge.
    body (str)
      The body/message of the nudge.
    action_text (str)
      The text to display for the call to action.
    action_href (str)
      The link to visit when the call to action is clicked.
    opt_out_text (str)
      The message to show for opting out of future similar messages.
    graphic_file_name (str)
      The graphic to use, needs to be uploaded to
      /static/images/community/nudges/
  """

  def __init__(self):
    self._user_nudge_id = 0
    self._title = None
    self._body = None
    self._action_text = None
    self._action_href = None
    self._opt_out_text = None
    self._graphic_file_name = None
    self._freeze()

  @property
  def user_nudge_id(self) -> int:
    r"""
    Unique Id to identify the nudge, used to dismiss
    If value is 0 then this is a duplicate and the nudge should not be shown to
    the user
    """
    return self._user_nudge_id

  @user_nudge_id.setter
  def user_nudge_id(self, user_nudge_id: int):
    if user_nudge_id is None:
      del self.user_nudge_id
      return
    if not isinstance(user_nudge_id, int):
      raise TypeError('user_nudge_id must be of type int')
    self._user_nudge_id = user_nudge_id

  @property
  def title(self) -> str:
    r"""
    Note the following fields are only populated for custom nudges. Built-in
    nudges are already defined on the FE. The title/header of the nudge.
    """
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
  def body(self) -> str:
    """The body/message of the nudge."""
    return self._body or ""

  @body.setter
  def body(self, body: Optional[str]):
    if body is None:
      del self.body
      return
    if not isinstance(body, str):
      raise TypeError('body must be of type str')
    self._body = body

  @property
  def action_text(self) -> str:
    """The text to display for the call to action."""
    return self._action_text or ""

  @action_text.setter
  def action_text(self, action_text: Optional[str]):
    if action_text is None:
      del self.action_text
      return
    if not isinstance(action_text, str):
      raise TypeError('action_text must be of type str')
    self._action_text = action_text

  @property
  def action_href(self) -> str:
    """The link to visit when the call to action is clicked."""
    return self._action_href or ""

  @action_href.setter
  def action_href(self, action_href: Optional[str]):
    if action_href is None:
      del self.action_href
      return
    if not isinstance(action_href, str):
      raise TypeError('action_href must be of type str')
    self._action_href = action_href

  @property
  def opt_out_text(self) -> str:
    """The message to show for opting out of future similar messages."""
    return self._opt_out_text or ""

  @opt_out_text.setter
  def opt_out_text(self, opt_out_text: Optional[str]):
    if opt_out_text is None:
      del self.opt_out_text
      return
    if not isinstance(opt_out_text, str):
      raise TypeError('opt_out_text must be of type str')
    self._opt_out_text = opt_out_text

  @property
  def graphic_file_name(self) -> str:
    r"""
    The graphic to use, needs to be uploaded to
    /static/images/community/nudges/
    """
    return self._graphic_file_name or ""

  @graphic_file_name.setter
  def graphic_file_name(self, graphic_file_name: Optional[str]):
    if graphic_file_name is None:
      del self.graphic_file_name
      return
    if not isinstance(graphic_file_name, str):
      raise TypeError('graphic_file_name must be of type str')
    self._graphic_file_name = graphic_file_name


class TestBigQueryNudgeRequest(KaggleObject):
  r"""
  Attributes:
    nudge_id (int)
      The id of the nudge to test.
  """

  def __init__(self):
    self._nudge_id = 0
    self._freeze()

  @property
  def nudge_id(self) -> int:
    """The id of the nudge to test."""
    return self._nudge_id

  @nudge_id.setter
  def nudge_id(self, nudge_id: int):
    if nudge_id is None:
      del self.nudge_id
      return
    if not isinstance(nudge_id, int):
      raise TypeError('nudge_id must be of type int')
    self._nudge_id = nudge_id


class TestBigQueryNudgeResponse(KaggleObject):
  r"""
  Attributes:
    user_count (int)
      The number of users returned for the nudge (ie how many users could receive
      it).
    error_message (str)
      If an exception was thrown, the details of the exception.
  """

  def __init__(self):
    self._user_count = 0
    self._error_message = None
    self._freeze()

  @property
  def user_count(self) -> int:
    r"""
    The number of users returned for the nudge (ie how many users could receive
    it).
    """
    return self._user_count

  @user_count.setter
  def user_count(self, user_count: int):
    if user_count is None:
      del self.user_count
      return
    if not isinstance(user_count, int):
      raise TypeError('user_count must be of type int')
    self._user_count = user_count

  @property
  def error_message(self) -> str:
    """If an exception was thrown, the details of the exception."""
    return self._error_message or ""

  @error_message.setter
  def error_message(self, error_message: Optional[str]):
    if error_message is None:
      del self.error_message
      return
    if not isinstance(error_message, str):
      raise TypeError('error_message must be of type str')
    self._error_message = error_message


AddNudgeRequest._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
]

AddNudgeResponse._fields = [
  FieldMetadata("nudgeId", "nudge_id", "_nudge_id", int, 0, PredefinedSerializer()),
]

CheckCustomNudgeRequest._fields = [
  FieldMetadata("nudgeId", "nudge_id", "_nudge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("variant", "variant", "_variant", int, None, PredefinedSerializer(), optional=True),
]

CheckCustomNudgeResponse._fields = [
  FieldMetadata("checkResult", "check_result", "_check_result", CheckResult, CheckResult.CHECK_RESULT_UNDEFINED, EnumSerializer()),
]

CheckForNudgeRequest._fields = []

CheckForNudgeResponse._fields = [
  FieldMetadata("potentialNudges", "potential_nudges", "_potential_nudges", PotentialNudge, [], ListSerializer(KaggleObjectSerializer())),
]

GetNudgeConfigRequest._fields = []

GetNudgeConfigResponse._fields = [
  FieldMetadata("nudges", "nudges", "_nudges", NudgeConfig, [], ListSerializer(KaggleObjectSerializer())),
]

NudgeConfig._fields = [
  FieldMetadata("nudgeId", "nudge_id", "_nudge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", str, "", PredefinedSerializer()),
  FieldMetadata("isBuiltIn", "is_built_in", "_is_built_in", bool, False, PredefinedSerializer()),
  FieldMetadata("showingNudgeResponse", "showing_nudge_response", "_showing_nudge_response", ShowingNudgeResponse, None, KaggleObjectSerializer()),
]

PotentialNudge._fields = [
  FieldMetadata("type", "type", "_type", str, "", PredefinedSerializer()),
  FieldMetadata("page", "page", "_page", NudgePage, NudgePage.NUDGE_PAGE_ANY, EnumSerializer()),
  FieldMetadata("priority", "priority", "_priority", int, 0, PredefinedSerializer()),
  FieldMetadata("variant", "variant", "_variant", int, None, PredefinedSerializer(), optional=True),
]

ReactToNudgeRequest._fields = [
  FieldMetadata("nudgeId", "nudge_id", "_nudge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("reaction", "reaction", "_reaction", NudgeReactions, NudgeReactions.REASON_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dontShowAgain", "dont_show_again", "_dont_show_again", bool, False, PredefinedSerializer()),
]

ReactToNudgeResponse._fields = []

ShowingNudgeRequest._fields = [
  FieldMetadata("type", "type", "_type", str, "", PredefinedSerializer()),
  FieldMetadata("variant", "variant", "_variant", int, None, PredefinedSerializer(), optional=True),
]

ShowingNudgeResponse._fields = [
  FieldMetadata("userNudgeId", "user_nudge_id", "_user_nudge_id", int, 0, PredefinedSerializer()),
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("body", "body", "_body", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("actionText", "action_text", "_action_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("actionHref", "action_href", "_action_href", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("optOutText", "opt_out_text", "_opt_out_text", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("graphicFileName", "graphic_file_name", "_graphic_file_name", str, None, PredefinedSerializer(), optional=True),
]

TestBigQueryNudgeRequest._fields = [
  FieldMetadata("nudgeId", "nudge_id", "_nudge_id", int, 0, PredefinedSerializer()),
]

TestBigQueryNudgeResponse._fields = [
  FieldMetadata("userCount", "user_count", "_user_count", int, 0, PredefinedSerializer()),
  FieldMetadata("errorMessage", "error_message", "_error_message", str, None, PredefinedSerializer(), optional=True),
]

