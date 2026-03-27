from kagglesdk.diagnostics.types.metrics_service import RecordPageLoadMetricsRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class MetricsClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def record_page_load_metrics(self, request: RecordPageLoadMetricsRequest = None):
    r"""
    Frontend calls this method after page load to keep track of page load
    latency.

    Args:
      request (RecordPageLoadMetricsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = RecordPageLoadMetricsRequest()

    self._client.call("diagnostics.MetricsService", "RecordPageLoadMetrics", request, None)
