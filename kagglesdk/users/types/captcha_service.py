from kagglesdk.kaggle_object import *

class GetCaptchaConfigRequest(KaggleObject):
  r"""
  Attributes:
    version (str)
      The ReCaptcha version. Valid values are `v2` or `v3`.
  """

  def __init__(self):
    self._version = ""
    self._freeze()

  @property
  def version(self) -> str:
    """The ReCaptcha version. Valid values are `v2` or `v3`."""
    return self._version

  @version.setter
  def version(self, version: str):
    if version is None:
      del self.version
      return
    if not isinstance(version, str):
      raise TypeError('version must be of type str')
    self._version = version


class GetCaptchaConfigResponse(KaggleObject):
  r"""
  Attributes:
    site_key (str)
      The ReCaptcha site key.
    enabled (bool)
      Whether captcha verification is enabled.
  """

  def __init__(self):
    self._site_key = ""
    self._enabled = False
    self._freeze()

  @property
  def site_key(self) -> str:
    """The ReCaptcha site key."""
    return self._site_key

  @site_key.setter
  def site_key(self, site_key: str):
    if site_key is None:
      del self.site_key
      return
    if not isinstance(site_key, str):
      raise TypeError('site_key must be of type str')
    self._site_key = site_key

  @property
  def enabled(self) -> bool:
    """Whether captcha verification is enabled."""
    return self._enabled

  @enabled.setter
  def enabled(self, enabled: bool):
    if enabled is None:
      del self.enabled
      return
    if not isinstance(enabled, bool):
      raise TypeError('enabled must be of type bool')
    self._enabled = enabled


class VerifyCaptchaRequest(KaggleObject):
  r"""
  Attributes:
    token (str)
      The ReCaptcha v3 response token.
  """

  def __init__(self):
    self._token = ""
    self._freeze()

  @property
  def token(self) -> str:
    """The ReCaptcha v3 response token."""
    return self._token

  @token.setter
  def token(self, token: str):
    if token is None:
      del self.token
      return
    if not isinstance(token, str):
      raise TypeError('token must be of type str')
    self._token = token


class VerifyCaptchaResponse(KaggleObject):
  r"""
  """

  pass

GetCaptchaConfigRequest._fields = [
  FieldMetadata("version", "version", "_version", str, "", PredefinedSerializer()),
]

GetCaptchaConfigResponse._fields = [
  FieldMetadata("siteKey", "site_key", "_site_key", str, "", PredefinedSerializer()),
  FieldMetadata("enabled", "enabled", "_enabled", bool, False, PredefinedSerializer()),
]

VerifyCaptchaRequest._fields = [
  FieldMetadata("token", "token", "_token", str, "", PredefinedSerializer()),
]

VerifyCaptchaResponse._fields = []

