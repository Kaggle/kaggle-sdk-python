import enum

class AccountError(enum.Enum):
  """Used via WithErrorInfo"""
  ACCOUNT_ERROR_UNSPECIFIED = 0
  PHONE_VERIFICATION_REQUIRED = 1
  """User needs to verify their phone number."""
  LOGIN_REQUIRED = 2
  """User needs to login."""
  IDENTITY_VERIFICATION_REQUIRED = 3
  """User needs to verify their identity with Persona."""

