import enum

class CommentAuthorType(enum.Enum):
  COMMENT_AUTHOR_TYPE_UNSPECIFIED = 0
  r"""
  Default value of author type makes no claim about what type of author it
  is, and nothing special should be shown.
  """
  HOST = 1
  DATASET_CREATOR = 2
  TOPIC = 3
  COMMENT = 4
  ADMIN = 5
  MODEL_CREATOR = 6
  JUDGE = 7

class EmojiReaction(enum.Enum):
  EMOJI_REACTION_UNSPECIFIED = 0
  THANK_YOU = 1
  YAY = 2
  LOVE = 3
  KAGGLE = 4
  FUNNY = 5
  SURPRISE = 6

class FollowUpStatus(enum.Enum):
  NONE = 0
  IN_PROGRESS = 1
  DONE = 2

