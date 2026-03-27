import enum

class CompetitionError(enum.Enum):
  """Used via WithErrorInfo"""
  COMPETITION_ERROR_UNSPECIFIED = 0
  RULES_ACCEPTANCE_REQUIRED = 1
  """User needs to accept the rules of a competition."""
  NEW_ENTRANTS_NOT_ALLOWED = 2
  """Competition does not allow new entrants."""

