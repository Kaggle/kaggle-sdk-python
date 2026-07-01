from kagglesdk.kaggle_object import *

class EnvVariable(KaggleObject):
  r"""
  Environment variable on a DOCKER_IMAGE BenchmarkTask's container.

    - `key`: variable name (e.g. `API_BASE_URL`).
    - `value`: literal value, OR (when `is_secret_name` is true) the name
      of a UserSecret on the caller's account.
    - `is_secret_name`: when true, the system resolves `value` against the
      caller's UserSecrets at runtime and injects the resolved secret.

  Attributes:
    key (str)
    value (str)
    is_secret_name (bool)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
    self._is_secret_name = False
    self._freeze()

  @property
  def key(self) -> str:
    return self._key

  @key.setter
  def key(self, key: str):
    if key is None:
      del self.key
      return
    if not isinstance(key, str):
      raise TypeError('key must be of type str')
    self._key = key

  @property
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

  @property
  def is_secret_name(self) -> bool:
    return self._is_secret_name

  @is_secret_name.setter
  def is_secret_name(self, is_secret_name: bool):
    if is_secret_name is None:
      del self.is_secret_name
      return
    if not isinstance(is_secret_name, bool):
      raise TypeError('is_secret_name must be of type bool')
    self._is_secret_name = is_secret_name


class UserSecret(KaggleObject):
  r"""
  UserSecret to create/update on the caller's account before running a
  DOCKER_IMAGE BenchmarkTask.

    - `name`: secret label (matched against existing UserSecrets by Label).
    - `value`: plaintext secret value.
    - `override_existing`: when true, replace any existing secret with the
      same name. When false, fail with AlreadyExists on a name collision.

  Attributes:
    name (str)
    value (str)
    override_existing (bool)
  """

  def __init__(self):
    self._name = ""
    self._value = ""
    self._override_existing = False
    self._freeze()

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
  def value(self) -> str:
    return self._value

  @value.setter
  def value(self, value: str):
    if value is None:
      del self.value
      return
    if not isinstance(value, str):
      raise TypeError('value must be of type str')
    self._value = value

  @property
  def override_existing(self) -> bool:
    return self._override_existing

  @override_existing.setter
  def override_existing(self, override_existing: bool):
    if override_existing is None:
      del self.override_existing
      return
    if not isinstance(override_existing, bool):
      raise TypeError('override_existing must be of type bool')
    self._override_existing = override_existing


EnvVariable._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
  FieldMetadata("isSecretName", "is_secret_name", "_is_secret_name", bool, False, PredefinedSerializer()),
]

UserSecret._fields = [
  FieldMetadata("name", "name", "_name", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
  FieldMetadata("overrideExisting", "override_existing", "_override_existing", bool, False, PredefinedSerializer()),
]

