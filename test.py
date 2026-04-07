import sys
from json import JSONDecodeError

from kagglesdk.datasets.services.dataset_api_service import DatasetApiClient
from kagglesdk.datasets.types.dataset_api_service import ApiDownloadDatasetRequest
from kagglesdk.models.services.model_api_service import ModelApiClient
from kagglesdk.models.types.model_api_service import (
    ApiListModelInstanceVersionFilesRequest,
    ApiDownloadModelInstanceVersionRequest,
)
from kagglesdk.models.types.model_enums import ModelFramework
from kagglesdk import KaggleClient, KaggleEnv


# An example that illustrates how to use the generated API.
# This exercises all the derived, conditional endpoints.
# Requests cannot be reused since the #framework property is deleted.
# That's done to ensure it won't show up in the body of a POST, although
# currently all Request objects that include #framework use GET.


def download_dataset(client: DatasetApiClient):
    # Download a small dataset that's on localhost.
    request = ApiDownloadDatasetRequest()
    request.owner_slug = "shreyanshverma27"
    request.dataset_slug = "online-sales-dataset-popular-marketplace-data"
    try:
        response = client.download_dataset(request)
        print(response.method())
    except JSONDecodeError as e:
        print("Download request succeeded, but no download was performed")

    request = ApiDownloadDatasetRequest()
    request.owner_slug = "shreyanshverma27"
    request.dataset_slug = "online-sales-dataset-popular-marketplace-data"
    request.file_name = "Online Sales Data.csv"
    try:
        response = client.download_dataset(request)
        print(response.method())
    except JSONDecodeError as e:
        print("Download request succeeded, but no download was performed")


def list_model_version_files(client: ModelApiClient):
    request = ApiListModelInstanceVersionFilesRequest()
    request.owner_slug = "google"
    request.model_slug = "recurrentgemma"
    request.instance_slug = "2b"
    request.framework = ModelFramework.MODEL_FRAMEWORK_FLAX
    request.version_number = 1
    response = client.list_model_instance_version_files(request)
    for file in response.files:
        print(file.name)

    request = ApiListModelInstanceVersionFilesRequest()
    request.owner_slug = "google"
    request.model_slug = "recurrentgemma"
    request.instance_slug = "2b"
    request.framework = ModelFramework.MODEL_FRAMEWORK_FLAX
    response = client.list_model_instance_version_files(request)
    for file in response.files:
        print(file.name)


def download_model_instance_version(client: ModelApiClient):
    # Download a smallish model that's on localhost.
    request = ApiDownloadModelInstanceVersionRequest()
    request.owner_slug = "google"
    request.model_slug = "yamnet"
    request.instance_slug = "classification-tflite"
    request.version_number = 1
    request.framework = ModelFramework.MODEL_FRAMEWORK_TF_LITE
    try:
        response = client.download_model_instance_version(request)
        print(response.method())
    except JSONDecodeError as e:
        print("Download request succeeded, but no download was performed")

    request = ApiDownloadModelInstanceVersionRequest()
    request.owner_slug = "google"
    request.model_slug = "yamnet"
    request.instance_slug = "classification-tflite"
    request.version_number = 1
    request.path = "1.tflite"
    request.framework = ModelFramework.MODEL_FRAMEWORK_TF_LITE
    try:
        response = client.download_model_instance_version(request)
        print(response.method())
    except JSONDecodeError as e:
        print("Download request succeeded, but no download was performed")


def _build_kaggle_client(args):
    env = KaggleEnv.STAGING if "--staging" in args else KaggleEnv.ADMIN if "--admin" in args else KaggleEnv.LOCAL
    verbose = "--verbose" in args or "-v" in args
    return KaggleClient(env=env, verbose=verbose)


def main(args):
    try:
        with _build_kaggle_client(args) as kaggle_client:
            download_dataset(kaggle_client.datasets.dataset_api_client)
            list_model_version_files(kaggle_client.models.model_api_client)
            download_model_instance_version(kaggle_client.models.model_api_client)

    except Exception as e:
        if "--verbose" in args or "-v" in args:
            raise
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
