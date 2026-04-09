import sys
from kagglesdk.competitions.services.competition_service import CompetitionClient
from kagglesdk.competitions.types.competition_service import GetCompetitionRequest
from kagglesdk.competitions.types.competition_service import ListCompetitionsRequest
from kagglesdk.datasets.types.dataset_service import (
    DatasetListItem,
    SearchDatasetsRequest,
)
from kagglesdk.datasets.services.dataset_service import DatasetClient
from kagglesdk.kernels.services.kernels_service import KernelsClient
from kagglesdk.kernels.types.kernels_enums import (
    KernelsListSortType,
    KernelsListViewType,
)
from kagglesdk.kernels.types.kernels_types import (
    KernelList,
    ListKernelIdsRequest,
    ListKernelsRequest,
    SearchKernelIdsRequest,
)
from kagglesdk.users.types.users_service import (
    GetCurrentUserRequest,
    SearchUsersSuggestionsRequest,
)
from kagglesdk.users.services.users_service import UsersClient
from kagglesdk import KaggleClient, KaggleEnv


def get_competition(client: CompetitionClient):
    competition = client.get_competition(competition_name="titanic")
    print("Competition:")
    print(f"/competitions/{competition.competition_name} {competition.title} {competition.brief_description}")
    print()


def list_competitions(client: CompetitionClient):
    request = ListCompetitionsRequest()
    request.page_size = 5
    request.selector = ListCompetitionsRequest.Selector()
    request.selector.list_option = ListCompetitionsRequest.Selector.ListOption.LIST_OPTION_ACTIVE
    request.selector.sort_option = ListCompetitionsRequest.Selector.SortOption.SORT_OPTION_NUM_TEAMS
    request.selector.visibility_filter = ListCompetitionsRequest.Selector.VisibilityFilter.VISIBILITY_FILTER_PUBLIC

    response = client.list_competitions(request)
    print("Competitions:")
    for competition in response.competitions:
        print(f'/competitions/{competition.competition_name} "{competition.title}" "{competition.brief_description}"')
    print()


def list_kernels(client: KernelsClient):
    request = ListKernelsRequest()
    request.kernel_filter_criteria = SearchKernelIdsRequest()
    request.kernel_filter_criteria.list_request = ListKernelIdsRequest()
    request.kernel_filter_criteria.list_request.competition_id = 3136  # Titanic
    request.kernel_filter_criteria.list_request.sort_by = KernelsListSortType.HOTNESS
    request.kernel_filter_criteria.list_request.page_size = 5
    request.kernel_filter_criteria.list_request.page = 1
    request.kernel_filter_criteria.list_request.group = KernelsListViewType.EVERYONE

    response = response = client.list_kernels(request)
    print("Kernels:")
    for kernel in response.kernels:
        print(f'/code/{kernel.current_url_slug} "{kernel.title}" by "{kernel.author.display_name}"')
    print()


def list_datasets(client: DatasetClient):
    request = SearchDatasetsRequest()

    response = client.search_datasets(request)

    print("Datasets:")
    for dataset in response.dataset_list.items[:5]:
        print(f'{dataset.dataset_url} by "{dataset.owner_name}"')
    print()


def get_current_user(client: UsersClient):
    current_user = client.get_current_user()

    print("Current user:")
    print(f'{current_user.id}/{current_user.user_name} "{current_user.display_name}"')
    print()


def search_users_suggestions(client: UsersClient):
    topic_id = 293861  # /discussions/getting-started/293861

    response = client.search_users_suggestions(query="yas", topic_id=topic_id, page_size=5)

    print("User suggestions:")
    for user in response.users_suggestions:
        print(f'{user.id}/{user.user_name} "{user.display_name}"')
    print()


def _build_kaggle_client(args):
    env = (
        KaggleEnv.STAGING
        if "--staging" in args
        else (KaggleEnv.ADMIN if "--admin" in args else KaggleEnv.QA if "--qa" in args else KaggleEnv.LOCAL)
    )
    verbose = "--verbose" in args or "-v" in args
    return KaggleClient(env=env, verbose=verbose)


def main(args):
    try:
        with _build_kaggle_client(args) as kaggle_client:
            if "--competitions" in args:
                get_competition(kaggle_client.competitions.competition_client)
                list_competitions(kaggle_client.competitions.competition_client)

            if "--code" in args:
                list_kernels(kaggle_client.kernels.kernels_client)

            if "--datasets" in args:
                list_datasets(kaggle_client.datasets.dataset_client)

            if "--users" in args:
                get_current_user(kaggle_client.users.users_client)
                search_users_suggestions(kaggle_client.users.users_client)
    except Exception as e:
        if "--verbose" in args or "-v" in args:
            raise
        print(e)


if __name__ == "__main__":
    main(sys.argv[1:])
