from kagglesdk.kaggle_object import *
from typing import List, Optional

class FeatureFlagState(KaggleObject):
  r"""
  Attributes:
    key (str)
    value (str)
  """

  def __init__(self):
    self._key = ""
    self._value = ""
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


class RecordPageLoadMetricsRequest(KaggleObject):
  r"""
  Attributes:
    page_url (str)
      Relative url of the page that was loaded.
      Examples: '/', '/competitions', '/competitions/titanic'.
    is_full_page_refresh (bool)
      Whether this request is a full page refresh or an in-app navigation where
      the data is fetched via AJAX and the page is updated with a full refresh.
      True for initial navigation/hard-refresh, false for Rapidash and
      react-router navigations
    is_react_router_navigation (bool)
      used to disambiguate between Rapidash and react-router page loads
    page_request_start_epoch_ms (int)
      Server-side timestamp when the request to 'page_url' was initiated by the
      frontend, i.e., right after the user clicks on a link to open a page. For
      react-router, this timestamp is client-side
    page_request_end_epoch_ms (int)
      Server-side timestamp when the request to 'page_url' was finished.
      The difference between 'page_request_end_epoch_ms' and
      'page_request_start_epoch_ms' is the time it takes to download the initial
      HTML/JSON/Assets for the page. For react-router, this timestamp is
      client-side
    page_load_start_epoch_ms (int)
      Client-side timestamp when the frontend starts loading the page.
      The difference between 'page_load_start_epoch_ms' and
      'page_request_end_epoch_ms' is the time it takes to parse the initial
      HTML/JSON/Assets.
    page_load_end_epoch_ms (int)
      Client-side timestamp when the frontend finishes loading the page. At this
      point, the page is assumed to be completely rendered and ready to be used
      by the user. The difference between 'page_load_end_epoch_ms' and
      'page_request_start_epoch_ms' is the total page load latency, i.e., time it
      takes to completely load the page after a user clicks on a link.
    feature_flags_state (FeatureFlagState)
      A subset of the feature flags state specified by the
      `AddFeatureFlagsToPageLoadTag` ops flag.
  """

  def __init__(self):
    self._page_url = ""
    self._is_full_page_refresh = False
    self._is_react_router_navigation = False
    self._page_request_start_epoch_ms = 0
    self._page_request_end_epoch_ms = 0
    self._page_load_start_epoch_ms = 0
    self._page_load_end_epoch_ms = 0
    self._feature_flags_state = []
    self._freeze()

  @property
  def page_url(self) -> str:
    r"""
    Relative url of the page that was loaded.
    Examples: '/', '/competitions', '/competitions/titanic'.
    """
    return self._page_url

  @page_url.setter
  def page_url(self, page_url: str):
    if page_url is None:
      del self.page_url
      return
    if not isinstance(page_url, str):
      raise TypeError('page_url must be of type str')
    self._page_url = page_url

  @property
  def is_full_page_refresh(self) -> bool:
    r"""
    Whether this request is a full page refresh or an in-app navigation where
    the data is fetched via AJAX and the page is updated with a full refresh.
    True for initial navigation/hard-refresh, false for Rapidash and
    react-router navigations
    """
    return self._is_full_page_refresh

  @is_full_page_refresh.setter
  def is_full_page_refresh(self, is_full_page_refresh: bool):
    if is_full_page_refresh is None:
      del self.is_full_page_refresh
      return
    if not isinstance(is_full_page_refresh, bool):
      raise TypeError('is_full_page_refresh must be of type bool')
    self._is_full_page_refresh = is_full_page_refresh

  @property
  def is_react_router_navigation(self) -> bool:
    """used to disambiguate between Rapidash and react-router page loads"""
    return self._is_react_router_navigation

  @is_react_router_navigation.setter
  def is_react_router_navigation(self, is_react_router_navigation: bool):
    if is_react_router_navigation is None:
      del self.is_react_router_navigation
      return
    if not isinstance(is_react_router_navigation, bool):
      raise TypeError('is_react_router_navigation must be of type bool')
    self._is_react_router_navigation = is_react_router_navigation

  @property
  def page_request_start_epoch_ms(self) -> int:
    r"""
    Server-side timestamp when the request to 'page_url' was initiated by the
    frontend, i.e., right after the user clicks on a link to open a page. For
    react-router, this timestamp is client-side
    """
    return self._page_request_start_epoch_ms

  @page_request_start_epoch_ms.setter
  def page_request_start_epoch_ms(self, page_request_start_epoch_ms: int):
    if page_request_start_epoch_ms is None:
      del self.page_request_start_epoch_ms
      return
    if not isinstance(page_request_start_epoch_ms, int):
      raise TypeError('page_request_start_epoch_ms must be of type int')
    self._page_request_start_epoch_ms = page_request_start_epoch_ms

  @property
  def page_request_end_epoch_ms(self) -> int:
    r"""
    Server-side timestamp when the request to 'page_url' was finished.
    The difference between 'page_request_end_epoch_ms' and
    'page_request_start_epoch_ms' is the time it takes to download the initial
    HTML/JSON/Assets for the page. For react-router, this timestamp is
    client-side
    """
    return self._page_request_end_epoch_ms

  @page_request_end_epoch_ms.setter
  def page_request_end_epoch_ms(self, page_request_end_epoch_ms: int):
    if page_request_end_epoch_ms is None:
      del self.page_request_end_epoch_ms
      return
    if not isinstance(page_request_end_epoch_ms, int):
      raise TypeError('page_request_end_epoch_ms must be of type int')
    self._page_request_end_epoch_ms = page_request_end_epoch_ms

  @property
  def page_load_start_epoch_ms(self) -> int:
    r"""
    Client-side timestamp when the frontend starts loading the page.
    The difference between 'page_load_start_epoch_ms' and
    'page_request_end_epoch_ms' is the time it takes to parse the initial
    HTML/JSON/Assets.
    """
    return self._page_load_start_epoch_ms

  @page_load_start_epoch_ms.setter
  def page_load_start_epoch_ms(self, page_load_start_epoch_ms: int):
    if page_load_start_epoch_ms is None:
      del self.page_load_start_epoch_ms
      return
    if not isinstance(page_load_start_epoch_ms, int):
      raise TypeError('page_load_start_epoch_ms must be of type int')
    self._page_load_start_epoch_ms = page_load_start_epoch_ms

  @property
  def page_load_end_epoch_ms(self) -> int:
    r"""
    Client-side timestamp when the frontend finishes loading the page. At this
    point, the page is assumed to be completely rendered and ready to be used
    by the user. The difference between 'page_load_end_epoch_ms' and
    'page_request_start_epoch_ms' is the total page load latency, i.e., time it
    takes to completely load the page after a user clicks on a link.
    """
    return self._page_load_end_epoch_ms

  @page_load_end_epoch_ms.setter
  def page_load_end_epoch_ms(self, page_load_end_epoch_ms: int):
    if page_load_end_epoch_ms is None:
      del self.page_load_end_epoch_ms
      return
    if not isinstance(page_load_end_epoch_ms, int):
      raise TypeError('page_load_end_epoch_ms must be of type int')
    self._page_load_end_epoch_ms = page_load_end_epoch_ms

  @property
  def feature_flags_state(self) -> Optional[List[Optional['FeatureFlagState']]]:
    r"""
    A subset of the feature flags state specified by the
    `AddFeatureFlagsToPageLoadTag` ops flag.
    """
    return self._feature_flags_state

  @feature_flags_state.setter
  def feature_flags_state(self, feature_flags_state: Optional[List[Optional['FeatureFlagState']]]):
    if feature_flags_state is None:
      del self.feature_flags_state
      return
    if not isinstance(feature_flags_state, list):
      raise TypeError('feature_flags_state must be of type list')
    if not all([isinstance(t, FeatureFlagState) for t in feature_flags_state]):
      raise TypeError('feature_flags_state must contain only items of type FeatureFlagState')
    self._feature_flags_state = feature_flags_state


FeatureFlagState._fields = [
  FieldMetadata("key", "key", "_key", str, "", PredefinedSerializer()),
  FieldMetadata("value", "value", "_value", str, "", PredefinedSerializer()),
]

RecordPageLoadMetricsRequest._fields = [
  FieldMetadata("pageUrl", "page_url", "_page_url", str, "", PredefinedSerializer()),
  FieldMetadata("isFullPageRefresh", "is_full_page_refresh", "_is_full_page_refresh", bool, False, PredefinedSerializer()),
  FieldMetadata("isReactRouterNavigation", "is_react_router_navigation", "_is_react_router_navigation", bool, False, PredefinedSerializer()),
  FieldMetadata("pageRequestStartEpochMs", "page_request_start_epoch_ms", "_page_request_start_epoch_ms", int, 0, PredefinedSerializer()),
  FieldMetadata("pageRequestEndEpochMs", "page_request_end_epoch_ms", "_page_request_end_epoch_ms", int, 0, PredefinedSerializer()),
  FieldMetadata("pageLoadStartEpochMs", "page_load_start_epoch_ms", "_page_load_start_epoch_ms", int, 0, PredefinedSerializer()),
  FieldMetadata("pageLoadEndEpochMs", "page_load_end_epoch_ms", "_page_load_end_epoch_ms", int, 0, PredefinedSerializer()),
  FieldMetadata("featureFlagsState", "feature_flags_state", "_feature_flags_state", FeatureFlagState, [], ListSerializer(KaggleObjectSerializer())),
]

