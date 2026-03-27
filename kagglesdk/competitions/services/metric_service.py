from kagglesdk.competitions.types.evaluation_algorithm import CompetitionMetricVersion, EvaluationAlgorithm
from kagglesdk.competitions.types.metric_service import CompetitionMetricMetadata, CreateAdminMetricRequest, CreateCompetitionMetricRequest, CreateCompetitionMetricResponse, CreateEnvironmentMetricRequest, GetCompetitionMetricMetadataRequest, GetCompetitionMetricVersionRequest, ListCompetitionMetricsRequest, ListCompetitionMetricsResponse, UpdateCompetitionMetricMetadataRequest, UpdateCompetitionMetricRequest
from kagglesdk.kaggle_http_client import KaggleHttpClient

class MetricClient(object):

  def __init__(self, client: KaggleHttpClient):
    self._client = client

  def create_competition_metric(self, request: CreateCompetitionMetricRequest = None) -> CreateCompetitionMetricResponse:
    r"""
    Args:
      request (CreateCompetitionMetricRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateCompetitionMetricRequest()

    return self._client.call("competitions.MetricService", "CreateCompetitionMetric", request, CreateCompetitionMetricResponse)

  def create_admin_metric(self, request: CreateAdminMetricRequest = None):
    r"""
    Utility for admins to create a metric owned by the Metric account and share
    edit permission with the caller. This may take a few seconds to complete.

    Args:
      request (CreateAdminMetricRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateAdminMetricRequest()

    self._client.call("competitions.MetricService", "CreateAdminMetric", request, None)

  def update_competition_metric(self, request: UpdateCompetitionMetricRequest = None) -> EvaluationAlgorithm:
    r"""
    Allows admins to make manual updates to a metric on /admin/api

    Args:
      request (UpdateCompetitionMetricRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionMetricRequest()

    return self._client.call("competitions.MetricService", "UpdateCompetitionMetric", request, EvaluationAlgorithm)

  def get_competition_metric_version(self, request: GetCompetitionMetricVersionRequest = None) -> CompetitionMetricVersion:
    r"""
    Args:
      request (GetCompetitionMetricVersionRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionMetricVersionRequest()

    return self._client.call("competitions.MetricService", "GetCompetitionMetricVersion", request, CompetitionMetricVersion)

  def list_competition_metrics(self, request: ListCompetitionMetricsRequest = None) -> ListCompetitionMetricsResponse:
    r"""
    Args:
      request (ListCompetitionMetricsRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = ListCompetitionMetricsRequest()

    return self._client.call("competitions.MetricService", "ListCompetitionMetrics", request, ListCompetitionMetricsResponse)

  def get_competition_metric_metadata(self, request: GetCompetitionMetricMetadataRequest = None) -> CompetitionMetricMetadata:
    r"""
    Supports the Metric tab of the Kernel Editor

    Args:
      request (GetCompetitionMetricMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = GetCompetitionMetricMetadataRequest()

    return self._client.call("competitions.MetricService", "GetCompetitionMetricMetadata", request, CompetitionMetricMetadata)

  def update_competition_metric_metadata(self, request: UpdateCompetitionMetricMetadataRequest = None):
    r"""
    Supports saving changes on the Metric tab of the Kernel Editor

    Args:
      request (UpdateCompetitionMetricMetadataRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = UpdateCompetitionMetricMetadataRequest()

    self._client.call("competitions.MetricService", "UpdateCompetitionMetricMetadata", request, None)

  def create_environment_metric(self, request: CreateEnvironmentMetricRequest = None):
    r"""
    /admin/api endpoint for creating a Simulations metric

    Args:
      request (CreateEnvironmentMetricRequest):
        The request object; initialized to empty instance if not specified.
    """

    if request is None:
      request = CreateEnvironmentMetricRequest()

    self._client.call("competitions.MetricService", "CreateEnvironmentMetric", request, None)
