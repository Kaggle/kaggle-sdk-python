from kagglesdk.kaggle_object import *
from typing import Optional, List

class CroppedImageRectangle(KaggleObject):
  r"""
  Attributes:
    title (str)
      Title of the crop (e.g. 'thumbnail').
    top (int)
    left (int)
    width (int)
    height (int)
  """

  def __init__(self):
    self._title = None
    self._top = 0
    self._left = 0
    self._width = 0
    self._height = 0
    self._freeze()

  @property
  def title(self) -> str:
    """Title of the crop (e.g. 'thumbnail')."""
    return self._title or ""

  @title.setter
  def title(self, title: Optional[str]):
    if title is None:
      del self.title
      return
    if not isinstance(title, str):
      raise TypeError('title must be of type str')
    self._title = title

  @property
  def top(self) -> int:
    return self._top

  @top.setter
  def top(self, top: int):
    if top is None:
      del self.top
      return
    if not isinstance(top, int):
      raise TypeError('top must be of type int')
    self._top = top

  @property
  def left(self) -> int:
    return self._left

  @left.setter
  def left(self, left: int):
    if left is None:
      del self.left
      return
    if not isinstance(left, int):
      raise TypeError('left must be of type int')
    self._left = left

  @property
  def width(self) -> int:
    return self._width

  @width.setter
  def width(self, width: int):
    if width is None:
      del self.width
      return
    if not isinstance(width, int):
      raise TypeError('width must be of type int')
    self._width = width

  @property
  def height(self) -> int:
    return self._height

  @height.setter
  def height(self, height: int):
    if height is None:
      del self.height
      return
    if not isinstance(height, int):
      raise TypeError('height must be of type int')
    self._height = height


class CroppedImageUpload(KaggleObject):
  r"""
  This is the result of our <ImageUploader /> React component.

  Attributes:
    token (str)
      Token that represents the image blob.
      It's optional since you can crop an existing image by URL and thus just
      update the rectangle(s).
      DEPRECATED: Value types are deprecated in favor of `optional`, though this
      case may have been deemed difficult to migrate.
    crop_rectangles (CroppedImageRectangle)
      Cropped rectangles (i.e. for selecting a smaller rectangle from the image
      in the token).
  """

  def __init__(self):
    self._token = None
    self._crop_rectangles = []
    self._freeze()

  @property
  def token(self) -> str:
    r"""
    Token that represents the image blob.
    It's optional since you can crop an existing image by URL and thus just
    update the rectangle(s).
    DEPRECATED: Value types are deprecated in favor of `optional`, though this
    case may have been deemed difficult to migrate.
    """
    return self._token or None

  @token.setter
  def token(self, token: Optional[str]):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token

  @property
  def crop_rectangles(self) -> Optional[List[Optional['CroppedImageRectangle']]]:
    r"""
    Cropped rectangles (i.e. for selecting a smaller rectangle from the image
    in the token).
    """
    return self._crop_rectangles

  @crop_rectangles.setter
  def crop_rectangles(self, crop_rectangles: Optional[List[Optional['CroppedImageRectangle']]]):
    if crop_rectangles is None:
      del self.crop_rectangles
      return
    if not isinstance(crop_rectangles, list):
      raise TypeError('crop_rectangles must be of type list')
    if not all([isinstance(t, CroppedImageRectangle) for t in crop_rectangles]):
      raise TypeError('crop_rectangles must contain only items of type CroppedImageRectangle')
    self._crop_rectangles = crop_rectangles


CroppedImageRectangle._fields = [
  FieldMetadata("title", "title", "_title", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("top", "top", "_top", int, 0, PredefinedSerializer()),
  FieldMetadata("left", "left", "_left", int, 0, PredefinedSerializer()),
  FieldMetadata("width", "width", "_width", int, 0, PredefinedSerializer()),
  FieldMetadata("height", "height", "_height", int, 0, PredefinedSerializer()),
]

CroppedImageUpload._fields = [
  FieldMetadata("token", "token", "_token", str, None, PredefinedSerializer(), optional=True),
  FieldMetadata("cropRectangles", "crop_rectangles", "_crop_rectangles", CroppedImageRectangle, [], ListSerializer(KaggleObjectSerializer())),
]

