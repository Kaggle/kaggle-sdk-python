import enum

class HarnessType(enum.Enum):
  r"""
  The implementation of a Harness. This value + the harness slug represent the
  concrete implementation used to execute an agent against Kaggle.
  Saved to the DB. Do not modify existing values.
  """
  HARNESS_TYPE_UNSPECIFIED = 0
  HARNESS_TYPE_HARBOR_CANONICAL = 1
  """A canonical harbor agent, executed via the harbor --agent flag."""
  HARNESS_TYPE_KERNEL_GAME_ARENA = 2
  """A kernel-backed Game Arena harness."""
  HARNESS_TYPE_KERNEL_COMPS_BENCH = 3
  """A kernel-backed competitions benchmark harness."""

