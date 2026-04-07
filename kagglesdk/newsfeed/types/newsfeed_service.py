import enum

class ItemType(enum.Enum):
  r"""
  The ItemType enum defines all the possible newsfeed items that the front
  end knows how to render.
  """
  ITEM_TYPE_UNSPECIFIED = 0
  RAN_KERNEL = 1
  PUBLISHED_KERNEL = 2
  COMMENTED_ON_KERNEL = 3
  UPVOTED_KERNEL = 4
  DATASET_TRENDING = 5
  POSTED_DATASET = 6
  UPVOTED_DATASET = 8
  BLOG_POST = 9
  CREATED_TOPIC = 10
  REPLIED_TO_TOPIC = 11
  UPVOTED_TOPIC = 12
  COMPETITION_LAUNCH = 13
  COMPETITION_END = 14
  COMPETITION_FINAL = 15
  LEARN_CHALLENGE = 16

