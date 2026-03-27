from kagglesdk.kaggle_object import *
from typing import Optional, List

class CreateStardewItemRequest(KaggleObject):
  r"""
  Attributes:
    item (StardewItem)
  """

  def __init__(self):
    self._item = None
    self._freeze()

  @property
  def item(self) -> Optional['StardewItem']:
    return self._item

  @item.setter
  def item(self, item: Optional['StardewItem']):
    if item is None:
      del self.item
      return
    if not isinstance(item, StardewItem):
      raise TypeError('item must be of type StardewItem')
    self._item = item


class ListStardewItemsRequest(KaggleObject):
  r"""
  """

  pass

class ListStardewItemsResponse(KaggleObject):
  r"""
  Attributes:
    items (StardewItem)
  """

  def __init__(self):
    self._items = []
    self._freeze()

  @property
  def items(self) -> Optional[List[Optional['StardewItem']]]:
    return self._items

  @items.setter
  def items(self, items: Optional[List[Optional['StardewItem']]]):
    if items is None:
      del self.items
      return
    if not isinstance(items, list):
      raise TypeError('items must be of type list')
    if not all([isinstance(t, StardewItem) for t in items]):
      raise TypeError('items must contain only items of type StardewItem')
    self._items = items


class RemoveStardewItemRequest(KaggleObject):
  r"""
  Attributes:
    item (StardewItem)
  """

  def __init__(self):
    self._item = None
    self._freeze()

  @property
  def item(self) -> Optional['StardewItem']:
    return self._item

  @item.setter
  def item(self, item: Optional['StardewItem']):
    if item is None:
      del self.item
      return
    if not isinstance(item, StardewItem):
      raise TypeError('item must be of type StardewItem')
    self._item = item


class StardewItem(KaggleObject):
  r"""
  Attributes:
    id (int)
    buy_price (int)
    sell_price (int)
    image_url (str)
    name (str)
    notes (str)
  """

  def __init__(self):
    self._id = 0
    self._buy_price = 0
    self._sell_price = 0
    self._image_url = ""
    self._name = ""
    self._notes = None
    self._freeze()

  @property
  def id(self) -> int:
    return self._id

  @id.setter
  def id(self, id: int):
    if id is None:
      del self.id
      return
    if not isinstance(id, int):
      raise TypeError('id must be of type int')
    self._id = id

  @property
  def buy_price(self) -> int:
    return self._buy_price

  @buy_price.setter
  def buy_price(self, buy_price: int):
    if buy_price is None:
      del self.buy_price
      return
    if not isinstance(buy_price, int):
      raise TypeError('buy_price must be of type int')
    self._buy_price = buy_price

  @property
  def sell_price(self) -> int:
    return self._sell_price

  @sell_price.setter
  def sell_price(self, sell_price: int):
    if sell_price is None:
      del self.sell_price
      return
    if not isinstance(sell_price, int):
      raise TypeError('sell_price must be of type int')
    self._sell_price = sell_price

  @property
  def image_url(self) -> str:
    return self._image_url

  @image_url.setter
  def image_url(self, image_url: str):
    if image_url is None:
      del self.image_url
      return
    if not isinstance(image_url, str):
      raise TypeError('image_url must be of type str')
    self._image_url = image_url

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, name: str):
    if name is None:
      del self.name
      return
    if not isinstance(name, str):
      raise TypeError('name must be of type str')
    self._name = name

  @property
  def notes(self) -> str:
    return self._notes or ""

  @notes.setter
  def notes(self, notes: Optional[str]):
    if notes is None:
      del self.notes
      return
    if not isinstance(notes, str):
      raise TypeError('notes must be of type str')
    self._notes = notes


CreateStardewItemRequest._fields = [
  FieldMetadata("item", "item", "_item", StardewItem, None, KaggleObjectSerializer()),
]

ListStardewItemsRequest._fields = []

ListStardewItemsResponse._fields = [
  FieldMetadata("items", "items", "_items", StardewItem, [], ListSerializer(KaggleObjectSerializer())),
]

RemoveStardewItemRequest._fields = [
  FieldMetadata("item", "item", "_item", StardewItem, None, KaggleObjectSerializer()),
]

StardewItem._fields = [
  FieldMetadata("id", "id", "_id", int, 0, PredefinedSerializer()),
  FieldMetadata("buyPrice", "buy_price", "_buy_price", int, 0, PredefinedSerializer()),
  FieldMetadata("sellPrice", "sell_price", "_sell_price", int, 0, PredefinedSerializer()),
  FieldMetadata("imageUrl", "image_url", "_image_url", str, "", PredefinedSerializer()),
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("notes", "notes", "_notes", str, None, PredefinedSerializer(), optional=True),
]

