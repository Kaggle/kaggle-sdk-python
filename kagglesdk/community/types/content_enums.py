import enum


class ContentState(enum.Enum):
    """Keep synced with /Kaggle.Sdk/cloud/kaggle/moderation/sor.proto"""

    CONTENT_STATE_UNSPECIFIED = 0
    PENDING_CLASSIFICATION = 1
    r"""
  Awaiting abuse classification. This exists as a non-visible state prior to
  classification.
  """
    PUBLISHED = 2
    r"""
  Publicly viewable, although access may be restricted outside of its content
  state.
  """
    TEMPORARILY_QUARANTINED = 3
    r"""
  DEPRECATED, use SYSTEM_DELETED: Quarantined by an admin or by the system.
  This means that the content is only visible to the user and admins, however
  users are able to toggle their content out of this state.
  """
    PERMANENTLY_QUARANTINED = 4
    r"""
  DEPRECATED, use SYSTEM_DELETED: Quarantined by an admin or by the system,
  the user cannot toggle their content's state back to public.
  """
    USER_DELETED = 5
    r"""
  Deleted by the user. This data needs to be wiped out according to the
  table's data retention policy.
  """
    SYSTEM_DELETED = 6
    r"""
  Deleted by an admin or by a system account for moderation purposes. This
  data may need to be restored in the event of a successfull user appeal, and
  should not be wiped out.
  """
    PENDING_PERMANENT_DELETE = 7
    """Awaiting permanent deletion."""
    PERMANENTLY_DELETED = 10
    r"""
  All the data has been deleted, and thus satisfies wipeout. The data is in a
  state where it should not be restored. This state immediately follows
  PENDING_PERMANENT_DELETE, if the row is kept in the DB. This row could also
  be removed from the DB ('hard deleted'), as no data is associated with it.
  Whether a row is kept as PERMANENTLY_DELETED or removed from the DB is up
  to each team. For more details, see: http://shortn/_Z23aOje4MH
  """
    DRAFT = 8
    r"""
  Initial state of entity that has never been previously published.
  Unable to return back to Draft state once published.
  State flow chart example: http://screen/8vDypV7HPeuHBFK
  """
    UNPUBLISHED = 9
    r"""
  Intermediate stage that has either been upgraded from the Draft state or
  downgraded from the Published state.
  """
