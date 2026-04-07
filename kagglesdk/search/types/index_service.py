from kagglesdk.kaggle_object import *
from kagglesdk.search.types.search_enums import DocumentType
from typing import Optional, List

class BatchForceIndexDocumentsRequest(KaggleObject):
  r"""
  Attributes:
    document_type (DocumentType)
      The type of the documents to force-index, all will be the same type
    db_ids (int)
      The IDs of the documents to force-index
  """

  def __init__(self):
    self._document_type = DocumentType.DOCUMENT_TYPE_UNSPECIFIED
    self._db_ids = []
    self._freeze()

  @property
  def document_type(self) -> 'DocumentType':
    """The type of the documents to force-index, all will be the same type"""
    return self._document_type

  @document_type.setter
  def document_type(self, document_type: 'DocumentType'):
    if document_type is None:
      del self.document_type
      return
    if not isinstance(document_type, DocumentType):
      raise TypeError('document_type must be of type DocumentType')
    self._document_type = document_type

  @property
  def db_ids(self) -> Optional[List[int]]:
    """The IDs of the documents to force-index"""
    return self._db_ids

  @db_ids.setter
  def db_ids(self, db_ids: Optional[List[int]]):
    if db_ids is None:
      del self.db_ids
      return
    if not isinstance(db_ids, list):
      raise TypeError('db_ids must be of type list')
    if not all([isinstance(t, int) for t in db_ids]):
      raise TypeError('db_ids must contain only items of type int')
    self._db_ids = db_ids


BatchForceIndexDocumentsRequest._fields = [
  FieldMetadata("documentType", "document_type", "_document_type", DocumentType, DocumentType.DOCUMENT_TYPE_UNSPECIFIED, EnumSerializer()),
  FieldMetadata("dbIds", "db_ids", "_db_ids", int, [], ListSerializer(PredefinedSerializer())),
]

