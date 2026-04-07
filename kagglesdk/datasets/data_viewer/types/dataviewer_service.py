from datetime import datetime
import enum
from kagglesdk.kaggle_object import *
from typing import Optional, List

class DataViewType(enum.Enum):
  TABULAR = 0
  URL = 1
  RAW = 2

class SortDirection(enum.Enum):
  ASC = 0
  DESC = 1

class DataRawType(enum.Enum):
  MARKDOWN = 0
  JSON = 1
  TEXT = 2

class DataTableType(enum.Enum):
  CSV = 0
  """Table is a csv file in cloud storage."""
  BIGQUERY = 1
  SQLITE = 2
  EXCEL = 3
  PARQUET = 4

class DataUrlType(enum.Enum):
  IMAGE = 0
  PDF = 1
  AUDIO = 2
  VIDEO = 3

class AndFilter(KaggleObject):
  r"""
  Attributes:
    filters (Filter)
      When evaluated, all these filters have to be true for the overall filter to
      become true
  """

  def __init__(self):
    self._filters = []
    self._freeze()

  @property
  def filters(self) -> Optional[List[Optional['Filter']]]:
    r"""
    When evaluated, all these filters have to be true for the overall filter to
    become true
    """
    return self._filters

  @filters.setter
  def filters(self, filters: Optional[List[Optional['Filter']]]):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, list):
      raise TypeError('filters must be of type list')
    if not all([isinstance(t, Filter) for t in filters]):
      raise TypeError('filters must contain only items of type Filter')
    self._filters = filters


class BooleanFilter(KaggleObject):
  r"""
  Attributes:
    value (bool)
      For booleans, we only allow to filter by equality
  """

  def __init__(self):
    self._value = False
    self._freeze()

  @property
  def value(self) -> bool:
    """For booleans, we only allow to filter by equality"""
    return self._value

  @value.setter
  def value(self, value: bool):
    if value is None:
      del self.value
      return
    if not isinstance(value, bool):
      raise TypeError('value must be of type bool')
    self._value = value


class Column(KaggleObject):
  r"""
  Attributes:
    firestore_path (str)
      Firestore path uniquely identifying the column
  """

  def __init__(self):
    self._firestore_path = ""
    self._freeze()

  @property
  def firestore_path(self) -> str:
    """Firestore path uniquely identifying the column"""
    return self._firestore_path

  @firestore_path.setter
  def firestore_path(self, firestore_path: str):
    if firestore_path is None:
      del self.firestore_path
      return
    if not isinstance(firestore_path, str):
      raise TypeError('firestore_path must be of type str')
    self._firestore_path = firestore_path


class ColumnFilter(KaggleObject):
  r"""
  Attributes:
    column (Column)
      Which column to filter on
    boolean_filter (BooleanFilter)
    numeric_filter (NumericFilter)
    date_time_filter (DateTimeFilter)
    string_filter (StringFilter)
  """

  def __init__(self):
    self._column = None
    self._boolean_filter = None
    self._numeric_filter = None
    self._date_time_filter = None
    self._string_filter = None
    self._freeze()

  @property
  def column(self) -> Optional['Column']:
    """Which column to filter on"""
    return self._column

  @column.setter
  def column(self, column: Optional['Column']):
    if column is None:
      del self.column
      return
    if not isinstance(column, Column):
      raise TypeError('column must be of type Column')
    self._column = column

  @property
  def boolean_filter(self) -> Optional['BooleanFilter']:
    return self._boolean_filter or None

  @boolean_filter.setter
  def boolean_filter(self, boolean_filter: Optional['BooleanFilter']):
    if boolean_filter is None:
      del self.boolean_filter
      return
    if not isinstance(boolean_filter, BooleanFilter):
      raise TypeError('boolean_filter must be of type BooleanFilter')
    del self.numeric_filter
    del self.date_time_filter
    del self.string_filter
    self._boolean_filter = boolean_filter

  @property
  def numeric_filter(self) -> Optional['NumericFilter']:
    return self._numeric_filter or None

  @numeric_filter.setter
  def numeric_filter(self, numeric_filter: Optional['NumericFilter']):
    if numeric_filter is None:
      del self.numeric_filter
      return
    if not isinstance(numeric_filter, NumericFilter):
      raise TypeError('numeric_filter must be of type NumericFilter')
    del self.boolean_filter
    del self.date_time_filter
    del self.string_filter
    self._numeric_filter = numeric_filter

  @property
  def date_time_filter(self) -> Optional['DateTimeFilter']:
    return self._date_time_filter or None

  @date_time_filter.setter
  def date_time_filter(self, date_time_filter: Optional['DateTimeFilter']):
    if date_time_filter is None:
      del self.date_time_filter
      return
    if not isinstance(date_time_filter, DateTimeFilter):
      raise TypeError('date_time_filter must be of type DateTimeFilter')
    del self.boolean_filter
    del self.numeric_filter
    del self.string_filter
    self._date_time_filter = date_time_filter

  @property
  def string_filter(self) -> Optional['StringFilter']:
    return self._string_filter or None

  @string_filter.setter
  def string_filter(self, string_filter: Optional['StringFilter']):
    if string_filter is None:
      del self.string_filter
      return
    if not isinstance(string_filter, StringFilter):
      raise TypeError('string_filter must be of type StringFilter')
    del self.boolean_filter
    del self.numeric_filter
    del self.date_time_filter
    self._string_filter = string_filter


class ConstantFilter(KaggleObject):
  r"""
  Attributes:
    value (bool)
      For completeness only
  """

  def __init__(self):
    self._value = False
    self._freeze()

  @property
  def value(self) -> bool:
    """For completeness only"""
    return self._value

  @value.setter
  def value(self, value: bool):
    if value is None:
      del self.value
      return
    if not isinstance(value, bool):
      raise TypeError('value must be of type bool')
    self._value = value


class DataRaw(KaggleObject):
  r"""
  Attributes:
    data (str)
      Raw responses contain the file data as a string.
    type (DataRawType)
    total_bytes (int)
    preview_bytes (int)
  """

  def __init__(self):
    self._data = ""
    self._type = DataRawType.MARKDOWN
    self._total_bytes = 0
    self._preview_bytes = 0
    self._freeze()

  @property
  def data(self) -> str:
    """Raw responses contain the file data as a string."""
    return self._data

  @data.setter
  def data(self, data: str):
    if data is None:
      del self.data
      return
    if not isinstance(data, str):
      raise TypeError('data must be of type str')
    self._data = data

  @property
  def type(self) -> 'DataRawType':
    return self._type

  @type.setter
  def type(self, type: 'DataRawType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DataRawType):
      raise TypeError('type must be of type DataRawType')
    self._type = type

  @property
  def total_bytes(self) -> int:
    return self._total_bytes

  @total_bytes.setter
  def total_bytes(self, total_bytes: int):
    if total_bytes is None:
      del self.total_bytes
      return
    if not isinstance(total_bytes, int):
      raise TypeError('total_bytes must be of type int')
    self._total_bytes = total_bytes

  @property
  def preview_bytes(self) -> int:
    return self._preview_bytes

  @preview_bytes.setter
  def preview_bytes(self, preview_bytes: int):
    if preview_bytes is None:
      del self.preview_bytes
      return
    if not isinstance(preview_bytes, int):
      raise TypeError('preview_bytes must be of type int')
    self._preview_bytes = preview_bytes


class DataRow(KaggleObject):
  r"""
  Attributes:
    row_number (int)
      The row number identifier.
    text (str)
      The raw data for a particular row. Each value represents one column.
  """

  def __init__(self):
    self._row_number = 0
    self._text = []
    self._freeze()

  @property
  def row_number(self) -> int:
    """The row number identifier."""
    return self._row_number

  @row_number.setter
  def row_number(self, row_number: int):
    if row_number is None:
      del self.row_number
      return
    if not isinstance(row_number, int):
      raise TypeError('row_number must be of type int')
    self._row_number = row_number

  @property
  def text(self) -> Optional[List[str]]:
    """The raw data for a particular row. Each value represents one column."""
    return self._text

  @text.setter
  def text(self, text: Optional[List[str]]):
    if text is None:
      del self.text
      return
    if not isinstance(text, list):
      raise TypeError('text must be of type list')
    if not all([isinstance(t, str) for t in text]):
      raise TypeError('text must contain only items of type str')
    self._text = text


class DataTable(KaggleObject):
  r"""
  Attributes:
    type (DataTableType)
    total_rows (int)
      The total number of rows contained in this file.
    rows_returned (int)
      The total number of rows returned in this request.
      This could be different than total_rows if there are query filters applied.
    rows (DataRow)
      The raw row data for the returned file.
  """

  def __init__(self):
    self._type = DataTableType.CSV
    self._total_rows = 0
    self._rows_returned = 0
    self._rows = []
    self._freeze()

  @property
  def type(self) -> 'DataTableType':
    return self._type

  @type.setter
  def type(self, type: 'DataTableType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DataTableType):
      raise TypeError('type must be of type DataTableType')
    self._type = type

  @property
  def total_rows(self) -> int:
    """The total number of rows contained in this file."""
    return self._total_rows

  @total_rows.setter
  def total_rows(self, total_rows: int):
    if total_rows is None:
      del self.total_rows
      return
    if not isinstance(total_rows, int):
      raise TypeError('total_rows must be of type int')
    self._total_rows = total_rows

  @property
  def rows_returned(self) -> int:
    r"""
    The total number of rows returned in this request.
    This could be different than total_rows if there are query filters applied.
    """
    return self._rows_returned

  @rows_returned.setter
  def rows_returned(self, rows_returned: int):
    if rows_returned is None:
      del self.rows_returned
      return
    if not isinstance(rows_returned, int):
      raise TypeError('rows_returned must be of type int')
    self._rows_returned = rows_returned

  @property
  def rows(self) -> Optional[List[Optional['DataRow']]]:
    """The raw row data for the returned file."""
    return self._rows

  @rows.setter
  def rows(self, rows: Optional[List[Optional['DataRow']]]):
    if rows is None:
      del self.rows
      return
    if not isinstance(rows, list):
      raise TypeError('rows must be of type list')
    if not all([isinstance(t, DataRow) for t in rows]):
      raise TypeError('rows must contain only items of type DataRow')
    self._rows = rows


class DataUrl(KaggleObject):
  r"""
  Attributes:
    url (str)
      Image responses contain the url of the image to preview.
    type (DataUrlType)
  """

  def __init__(self):
    self._url = ""
    self._type = DataUrlType.IMAGE
    self._freeze()

  @property
  def url(self) -> str:
    """Image responses contain the url of the image to preview."""
    return self._url

  @url.setter
  def url(self, url: str):
    if url is None:
      del self.url
      return
    if not isinstance(url, str):
      raise TypeError('url must be of type str')
    self._url = url

  @property
  def type(self) -> 'DataUrlType':
    return self._type

  @type.setter
  def type(self, type: 'DataUrlType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DataUrlType):
      raise TypeError('type must be of type DataUrlType')
    self._type = type


class DataView(KaggleObject):
  r"""
  //// Response objects / messages //////

  Attributes:
    type (DataViewType)
      The type of this DataView.
    data_table (DataTable)
      The data returned for tabular files.
    data_url (DataUrl)
      The data returned for image files.
    data_raw (DataRaw)
      The raw data returned for 'other' files.
  """

  def __init__(self):
    self._type = DataViewType.TABULAR
    self._data_table = None
    self._data_url = None
    self._data_raw = None
    self._freeze()

  @property
  def type(self) -> 'DataViewType':
    """The type of this DataView."""
    return self._type

  @type.setter
  def type(self, type: 'DataViewType'):
    if type is None:
      del self.type
      return
    if not isinstance(type, DataViewType):
      raise TypeError('type must be of type DataViewType')
    self._type = type

  @property
  def data_table(self) -> Optional['DataTable']:
    """The data returned for tabular files."""
    return self._data_table or None

  @data_table.setter
  def data_table(self, data_table: Optional['DataTable']):
    if data_table is None:
      del self.data_table
      return
    if not isinstance(data_table, DataTable):
      raise TypeError('data_table must be of type DataTable')
    del self.data_url
    del self.data_raw
    self._data_table = data_table

  @property
  def data_url(self) -> Optional['DataUrl']:
    """The data returned for image files."""
    return self._data_url or None

  @data_url.setter
  def data_url(self, data_url: Optional['DataUrl']):
    if data_url is None:
      del self.data_url
      return
    if not isinstance(data_url, DataUrl):
      raise TypeError('data_url must be of type DataUrl')
    del self.data_table
    del self.data_raw
    self._data_url = data_url

  @property
  def data_raw(self) -> Optional['DataRaw']:
    """The raw data returned for 'other' files."""
    return self._data_raw or None

  @data_raw.setter
  def data_raw(self, data_raw: Optional['DataRaw']):
    if data_raw is None:
      del self.data_raw
      return
    if not isinstance(data_raw, DataRaw):
      raise TypeError('data_raw must be of type DataRaw')
    del self.data_table
    del self.data_url
    self._data_raw = data_raw


class DateTimeFilter(KaggleObject):
  r"""
  Attributes:
    operator (DateTimeFilter.DateTimeOperator)
      Operator to use for comparisons
    operand (datetime)
      Operand to compare against
  """

  class DateTimeOperator(enum.Enum):
    EQUALS = 0
    LESS_THAN = 1
    GREATER_THAN = 2
    LESS_EQUALS = 3
    GREATER_EQUALS = 4

  def __init__(self):
    self._operator = self.DateTimeOperator.EQUALS
    self._operand = None
    self._freeze()

  @property
  def operator(self) -> 'DateTimeFilter.DateTimeOperator':
    """Operator to use for comparisons"""
    return self._operator

  @operator.setter
  def operator(self, operator: 'DateTimeFilter.DateTimeOperator'):
    if operator is None:
      del self.operator
      return
    if not isinstance(operator, DateTimeFilter.DateTimeOperator):
      raise TypeError('operator must be of type DateTimeFilter.DateTimeOperator')
    self._operator = operator

  @property
  def operand(self) -> datetime:
    """Operand to compare against"""
    return self._operand

  @operand.setter
  def operand(self, operand: datetime):
    if operand is None:
      del self.operand
      return
    if not isinstance(operand, datetime):
      raise TypeError('operand must be of type datetime')
    self._operand = operand


class Filter(KaggleObject):
  r"""
  Attributes:
    column_filter (ColumnFilter)
    constant_filter (ConstantFilter)
    and_filter (AndFilter)
    or_filter (OrFilter)
    not_filter (NotFilter)
  """

  def __init__(self):
    self._column_filter = None
    self._constant_filter = None
    self._and_filter = None
    self._or_filter = None
    self._not_filter = None
    self._freeze()

  @property
  def column_filter(self) -> Optional['ColumnFilter']:
    return self._column_filter or None

  @column_filter.setter
  def column_filter(self, column_filter: Optional['ColumnFilter']):
    if column_filter is None:
      del self.column_filter
      return
    if not isinstance(column_filter, ColumnFilter):
      raise TypeError('column_filter must be of type ColumnFilter')
    del self.constant_filter
    del self.and_filter
    del self.or_filter
    del self.not_filter
    self._column_filter = column_filter

  @property
  def constant_filter(self) -> Optional['ConstantFilter']:
    return self._constant_filter or None

  @constant_filter.setter
  def constant_filter(self, constant_filter: Optional['ConstantFilter']):
    if constant_filter is None:
      del self.constant_filter
      return
    if not isinstance(constant_filter, ConstantFilter):
      raise TypeError('constant_filter must be of type ConstantFilter')
    del self.column_filter
    del self.and_filter
    del self.or_filter
    del self.not_filter
    self._constant_filter = constant_filter

  @property
  def and_filter(self) -> Optional['AndFilter']:
    return self._and_filter or None

  @and_filter.setter
  def and_filter(self, and_filter: Optional['AndFilter']):
    if and_filter is None:
      del self.and_filter
      return
    if not isinstance(and_filter, AndFilter):
      raise TypeError('and_filter must be of type AndFilter')
    del self.column_filter
    del self.constant_filter
    del self.or_filter
    del self.not_filter
    self._and_filter = and_filter

  @property
  def or_filter(self) -> Optional['OrFilter']:
    return self._or_filter or None

  @or_filter.setter
  def or_filter(self, or_filter: Optional['OrFilter']):
    if or_filter is None:
      del self.or_filter
      return
    if not isinstance(or_filter, OrFilter):
      raise TypeError('or_filter must be of type OrFilter')
    del self.column_filter
    del self.constant_filter
    del self.and_filter
    del self.not_filter
    self._or_filter = or_filter

  @property
  def not_filter(self) -> Optional['NotFilter']:
    return self._not_filter or None

  @not_filter.setter
  def not_filter(self, not_filter: Optional['NotFilter']):
    if not_filter is None:
      del self.not_filter
      return
    if not isinstance(not_filter, NotFilter):
      raise TypeError('not_filter must be of type NotFilter')
    del self.column_filter
    del self.constant_filter
    del self.and_filter
    del self.or_filter
    self._not_filter = not_filter


class GetDataViewResponse(KaggleObject):
  r"""
  Attributes:
    data_view (DataView)
      The materialized view of the file.
  """

  def __init__(self):
    self._data_view = None
    self._freeze()

  @property
  def data_view(self) -> Optional['DataView']:
    """The materialized view of the file."""
    return self._data_view

  @data_view.setter
  def data_view(self, data_view: Optional['DataView']):
    if data_view is None:
      del self.data_view
      return
    if not isinstance(data_view, DataView):
      raise TypeError('data_view must be of type DataView')
    self._data_view = data_view


class NotFilter(KaggleObject):
  r"""
  Attributes:
    filter (Filter)
      When evaluated, the given filter has to return false for the overall filter
      to become true
  """

  def __init__(self):
    self._filter = None
    self._freeze()

  @property
  def filter(self) -> Optional['Filter']:
    r"""
    When evaluated, the given filter has to return false for the overall filter
    to become true
    """
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['Filter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, Filter):
      raise TypeError('filter must be of type Filter')
    self._filter = filter


class NumericFilter(KaggleObject):
  r"""
  Attributes:
    operator (NumericFilter.NumericOperator)
      Operator to use for comparisons
    operand (float)
      Operand to compare against (using double as the widest numerical type)
  """

  class NumericOperator(enum.Enum):
    EQUALS = 0
    LESS_THAN = 1
    GREATER_THAN = 2
    LESS_EQUALS = 3
    GREATER_EQUALS = 4

  def __init__(self):
    self._operator = self.NumericOperator.EQUALS
    self._operand = 0.0
    self._freeze()

  @property
  def operator(self) -> 'NumericFilter.NumericOperator':
    """Operator to use for comparisons"""
    return self._operator

  @operator.setter
  def operator(self, operator: 'NumericFilter.NumericOperator'):
    if operator is None:
      del self.operator
      return
    if not isinstance(operator, NumericFilter.NumericOperator):
      raise TypeError('operator must be of type NumericFilter.NumericOperator')
    self._operator = operator

  @property
  def operand(self) -> float:
    """Operand to compare against (using double as the widest numerical type)"""
    return self._operand

  @operand.setter
  def operand(self, operand: float):
    if operand is None:
      del self.operand
      return
    if not isinstance(operand, float):
      raise TypeError('operand must be of type float')
    self._operand = operand


class OrFilter(KaggleObject):
  r"""
  Attributes:
    filters (Filter)
      When evaluated, one of these filters have to be true for the overall filter
      to become true
  """

  def __init__(self):
    self._filters = []
    self._freeze()

  @property
  def filters(self) -> Optional[List[Optional['Filter']]]:
    r"""
    When evaluated, one of these filters have to be true for the overall filter
    to become true
    """
    return self._filters

  @filters.setter
  def filters(self, filters: Optional[List[Optional['Filter']]]):
    if filters is None:
      del self.filters
      return
    if not isinstance(filters, list):
      raise TypeError('filters must be of type list')
    if not all([isinstance(t, Filter) for t in filters]):
      raise TypeError('filters must contain only items of type Filter')
    self._filters = filters


class SortBy(KaggleObject):
  r"""
  Attributes:
    column (Column)
      What column to sort by
    direction (SortDirection)
      Which direction?
  """

  def __init__(self):
    self._column = None
    self._direction = SortDirection.ASC
    self._freeze()

  @property
  def column(self) -> Optional['Column']:
    """What column to sort by"""
    return self._column

  @column.setter
  def column(self, column: Optional['Column']):
    if column is None:
      del self.column
      return
    if not isinstance(column, Column):
      raise TypeError('column must be of type Column')
    self._column = column

  @property
  def direction(self) -> 'SortDirection':
    """Which direction?"""
    return self._direction

  @direction.setter
  def direction(self, direction: 'SortDirection'):
    if direction is None:
      del self.direction
      return
    if not isinstance(direction, SortDirection):
      raise TypeError('direction must be of type SortDirection')
    self._direction = direction


class StringFilter(KaggleObject):
  r"""
  Attributes:
    operator (StringFilter.StringOperator)
      Operator to use for comparisons (we only allow IN here, but might extend in
      the future)
    operands (str)
      Operands to compare against .
      - IN uses the whole list of operands to compare against.
      - EQUALS and CONTAINS use only the first one.
  """

  class StringOperator(enum.Enum):
    IN = 0
    EQUALS = 1
    CONTAINS = 2

  def __init__(self):
    self._operator = self.StringOperator.IN
    self._operands = []
    self._freeze()

  @property
  def operator(self) -> 'StringFilter.StringOperator':
    r"""
    Operator to use for comparisons (we only allow IN here, but might extend in
    the future)
    """
    return self._operator

  @operator.setter
  def operator(self, operator: 'StringFilter.StringOperator'):
    if operator is None:
      del self.operator
      return
    if not isinstance(operator, StringFilter.StringOperator):
      raise TypeError('operator must be of type StringFilter.StringOperator')
    self._operator = operator

  @property
  def operands(self) -> Optional[List[str]]:
    r"""
    Operands to compare against .
    - IN uses the whole list of operands to compare against.
    - EQUALS and CONTAINS use only the first one.
    """
    return self._operands

  @operands.setter
  def operands(self, operands: Optional[List[str]]):
    if operands is None:
      del self.operands
      return
    if not isinstance(operands, list):
      raise TypeError('operands must be of type list')
    if not all([isinstance(t, str) for t in operands]):
      raise TypeError('operands must contain only items of type str')
    self._operands = operands


class TableQuery(KaggleObject):
  r"""
  //// Request objects / messages //////

  Attributes:
    skip (int)
      Row offset
    take (int)
      How many rows to return
    filter (Filter)
      Since we can combine filters in an AND and OR fashion, the top level filter
      only needs to be a single entry (which itself can be a combination of
      filters)
    selected_columns (Column)
      Which columns to return
    sorts (SortBy)
      Which columns to sort on
  """

  def __init__(self):
    self._skip = 0
    self._take = 0
    self._filter = None
    self._selected_columns = []
    self._sorts = []
    self._freeze()

  @property
  def skip(self) -> int:
    """Row offset"""
    return self._skip

  @skip.setter
  def skip(self, skip: int):
    if skip is None:
      del self.skip
      return
    if not isinstance(skip, int):
      raise TypeError('skip must be of type int')
    self._skip = skip

  @property
  def take(self) -> int:
    """How many rows to return"""
    return self._take

  @take.setter
  def take(self, take: int):
    if take is None:
      del self.take
      return
    if not isinstance(take, int):
      raise TypeError('take must be of type int')
    self._take = take

  @property
  def filter(self) -> Optional['Filter']:
    r"""
    Since we can combine filters in an AND and OR fashion, the top level filter
    only needs to be a single entry (which itself can be a combination of
    filters)
    """
    return self._filter

  @filter.setter
  def filter(self, filter: Optional['Filter']):
    if filter is None:
      del self.filter
      return
    if not isinstance(filter, Filter):
      raise TypeError('filter must be of type Filter')
    self._filter = filter

  @property
  def selected_columns(self) -> Optional[List[Optional['Column']]]:
    """Which columns to return"""
    return self._selected_columns

  @selected_columns.setter
  def selected_columns(self, selected_columns: Optional[List[Optional['Column']]]):
    if selected_columns is None:
      del self.selected_columns
      return
    if not isinstance(selected_columns, list):
      raise TypeError('selected_columns must be of type list')
    if not all([isinstance(t, Column) for t in selected_columns]):
      raise TypeError('selected_columns must contain only items of type Column')
    self._selected_columns = selected_columns

  @property
  def sorts(self) -> Optional[List[Optional['SortBy']]]:
    """Which columns to sort on"""
    return self._sorts

  @sorts.setter
  def sorts(self, sorts: Optional[List[Optional['SortBy']]]):
    if sorts is None:
      del self.sorts
      return
    if not isinstance(sorts, list):
      raise TypeError('sorts must be of type list')
    if not all([isinstance(t, SortBy) for t in sorts]):
      raise TypeError('sorts must contain only items of type SortBy')
    self._sorts = sorts


AndFilter._fields = [
  FieldMetadata("filters", "filters", "_filters", Filter, [], ListSerializer(KaggleObjectSerializer())),
]

BooleanFilter._fields = [
  FieldMetadata("value", "value", "_value", bool, False, PredefinedSerializer()),
]

Column._fields = [
  FieldMetadata("firestorePath", "firestore_path", "_firestore_path", str, "", PredefinedSerializer()),
]

ColumnFilter._fields = [
  FieldMetadata("column", "column", "_column", Column, None, KaggleObjectSerializer()),
  FieldMetadata("booleanFilter", "boolean_filter", "_boolean_filter", BooleanFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("numericFilter", "numeric_filter", "_numeric_filter", NumericFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("dateTimeFilter", "date_time_filter", "_date_time_filter", DateTimeFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("stringFilter", "string_filter", "_string_filter", StringFilter, None, KaggleObjectSerializer(), optional=True),
]

ConstantFilter._fields = [
  FieldMetadata("value", "value", "_value", bool, False, PredefinedSerializer()),
]

DataRaw._fields = [
  FieldMetadata("data", "data", "_data", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", DataRawType, DataRawType.MARKDOWN, EnumSerializer()),
  FieldMetadata("totalBytes", "total_bytes", "_total_bytes", int, 0, PredefinedSerializer()),
  FieldMetadata("previewBytes", "preview_bytes", "_preview_bytes", int, 0, PredefinedSerializer()),
]

DataRow._fields = [
  FieldMetadata("rowNumber", "row_number", "_row_number", int, 0, PredefinedSerializer()),
  FieldMetadata("text", "text", "_text", str, [], ListSerializer(PredefinedSerializer())),
]

DataTable._fields = [
  FieldMetadata("type", "type", "_type", DataTableType, DataTableType.CSV, EnumSerializer()),
  FieldMetadata("totalRows", "total_rows", "_total_rows", int, 0, PredefinedSerializer()),
  FieldMetadata("rowsReturned", "rows_returned", "_rows_returned", int, 0, PredefinedSerializer()),
  FieldMetadata("rows", "rows", "_rows", DataRow, [], ListSerializer(KaggleObjectSerializer())),
]

DataUrl._fields = [
  FieldMetadata("url", "url", "_url", str, "", PredefinedSerializer()),
  FieldMetadata("type", "type", "_type", DataUrlType, DataUrlType.IMAGE, EnumSerializer()),
]

DataView._fields = [
  FieldMetadata("type", "type", "_type", DataViewType, DataViewType.TABULAR, EnumSerializer()),
  FieldMetadata("dataTable", "data_table", "_data_table", DataTable, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("dataUrl", "data_url", "_data_url", DataUrl, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("dataRaw", "data_raw", "_data_raw", DataRaw, None, KaggleObjectSerializer(), optional=True),
]

DateTimeFilter._fields = [
  FieldMetadata("operator", "operator", "_operator", DateTimeFilter.DateTimeOperator, DateTimeFilter.DateTimeOperator.EQUALS, EnumSerializer()),
  FieldMetadata("operand", "operand", "_operand", datetime, None, DateTimeSerializer()),
]

Filter._fields = [
  FieldMetadata("columnFilter", "column_filter", "_column_filter", ColumnFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("constantFilter", "constant_filter", "_constant_filter", ConstantFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("andFilter", "and_filter", "_and_filter", AndFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("orFilter", "or_filter", "_or_filter", OrFilter, None, KaggleObjectSerializer(), optional=True),
  FieldMetadata("notFilter", "not_filter", "_not_filter", NotFilter, None, KaggleObjectSerializer(), optional=True),
]

GetDataViewResponse._fields = [
  FieldMetadata("dataView", "data_view", "_data_view", DataView, None, KaggleObjectSerializer()),
]

NotFilter._fields = [
  FieldMetadata("filter", "filter", "_filter", Filter, None, KaggleObjectSerializer()),
]

NumericFilter._fields = [
  FieldMetadata("operator", "operator", "_operator", NumericFilter.NumericOperator, NumericFilter.NumericOperator.EQUALS, EnumSerializer()),
  FieldMetadata("operand", "operand", "_operand", float, 0.0, PredefinedSerializer()),
]

OrFilter._fields = [
  FieldMetadata("filters", "filters", "_filters", Filter, [], ListSerializer(KaggleObjectSerializer())),
]

SortBy._fields = [
  FieldMetadata("column", "column", "_column", Column, None, KaggleObjectSerializer()),
  FieldMetadata("direction", "direction", "_direction", SortDirection, SortDirection.ASC, EnumSerializer()),
]

StringFilter._fields = [
  FieldMetadata("operator", "operator", "_operator", StringFilter.StringOperator, StringFilter.StringOperator.IN, EnumSerializer()),
  FieldMetadata("operands", "operands", "_operands", str, [], ListSerializer(PredefinedSerializer())),
]

TableQuery._fields = [
  FieldMetadata("skip", "skip", "_skip", int, 0, PredefinedSerializer()),
  FieldMetadata("take", "take", "_take", int, 0, PredefinedSerializer()),
  FieldMetadata("filter", "filter", "_filter", Filter, None, KaggleObjectSerializer()),
  FieldMetadata("selectedColumns", "selected_columns", "_selected_columns", Column, [], ListSerializer(KaggleObjectSerializer())),
  FieldMetadata("sorts", "sorts", "_sorts", SortBy, [], ListSerializer(KaggleObjectSerializer())),
]

