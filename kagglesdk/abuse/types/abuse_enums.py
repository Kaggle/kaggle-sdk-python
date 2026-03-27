import enum

class PrivatedModerationStatus(enum.Enum):
  PRIVATED_MODERATION_STATUS_UNSPECIFIED = 0
  PRIVATED_MODERATION_STATUS_NO_ABUSE = 1
  PERMANENTLY_PRIVATED = 3

class PolicyViolationSource(enum.Enum):
  """Be sure to add corresponding PolicyViolationSource to sql table"""
  POLICY_VIOLATION_SOURCE_UNSPECIFIED = 0
  r"""
  not sure who set the violation
  DO NOT USE
  """
  MODERATOR = 1
  """By moderator or admin"""
  USER_REPORTS = 2
  """From user reports"""
  KKB_ABUSE_DETECTION = 3
  """From user reports"""
  STRICT = 10
  r"""
  Will always result in a ban.  Catch all source, try to use the more
  specific source below or create new source.
  """
  STRICT_XXS = 12
  """Cross Site Scripting"""
  STRICT_MOVIE_LINK = 13
  """Movie link spam"""
  STRICT_DUPLICATE_POST = 14
  """When a duplicate post is detected"""
  STRICT_SELF_PROMOTION = 15
  """When self promotion is detected"""
  SPECULATIVE = 100
  r"""
  Rules that could cause high false positive.  Catch all source, try to use
  the more specific source below or create new source.
  """
  SPECULATIVE_SUSPICIOUS_WORDS = 101
  r"""
  List of words that are used a lot in spam but could cause high false
  positive
  """
  SPECULATIVE_NFL_TEAMS = 102
  """NFL team names used to catch streamer"""
  SPECULATIVE_INTERNATIONAL_CHARACTERS = 103
  r"""
  Non-english posts are generally an indicator of spam, but it does mean
  foreign language ended up getting banned
  """
  SPECULATIVE_EMAIL = 104
  r"""
  Sees a lot of email in spam posts, since user profile contains email it's
  usually not a legitimate post
  """
  AUTO_ML = 1000
  """Kaggle's own ML based protection using AUTO ML"""
  ARES = 1001
  """Ares protections"""
  GEMINI = 1002
  """Gemini prompt-based protections"""
  CLOUD_VISION = 1003
  """Cloud Vision image detection"""

