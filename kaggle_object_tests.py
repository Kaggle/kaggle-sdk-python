import datetime
import unittest
from google.protobuf.field_mask_pb2 import FieldMask
from kagglesdk.common.types.common_types import Category
from kagglesdk.competitions.legacy.types.legacy_background_operation import (
    BackgroundOperation,
)
from kagglesdk.competitions.types.competition_service import ListCompetitionsRequest
from kagglesdk.datasets.data_viewer.types.dataviewer_service import (
    AndFilter,
    BooleanFilter,
    ConstantFilter,
    ColumnFilter,
    Filter,
    NotFilter,
    OrFilter,
)
from kagglesdk.kernels.types.kernels_enums import (
    AcceleratorType,
    EditorType,
    KernelVersionType,
)
from kagglesdk.kernels.types.kernels_service import KernelSession
from kagglesdk.kernels.types.kernels_types import (
    AccessBehavior,
    GetKernelListDetailsRequest,
)

Selector = ListCompetitionsRequest.Selector


class ListCompetitionsRequestTests(unittest.TestCase):

    def test_default_values(self):
        req = ListCompetitionsRequest()
        self.assertIsNone(req.selector)
        self.assertEqual(0, req.page_size)
        self.assertEqual("", req.page_token)

        selector = Selector()
        self.assertEqual([], selector.competition_ids)
        self.assertEqual(0, selector.list_for_user_id)
        self.assertFalse("list_for_user_id" in selector)
        self.assertEqual(0, selector.host_segment_id_filter)
        self.assertFalse("host_segment_id_filter" in selector)
        self.assertEqual([], selector.tag_ids)
        self.assertFalse("tag_ids" in selector)
        self.assertEqual(Selector.ListOption.LIST_OPTION_DEFAULT, selector.list_option)
        self.assertFalse("list_option" in selector)
        self.assertEqual(Selector.SortOption.SORT_OPTION_DEFAULT, selector.sort_option)
        self.assertFalse("sort_option" in selector)
        self.assertEqual(
            Selector.PrestigeFilter.PRESTIGE_FILTER_UNSPECIFIED,
            selector.prestige_filter,
        )
        self.assertFalse("prestige_filter" in selector)
        self.assertEqual(
            Selector.VisibilityFilter.VISIBILITY_FILTER_UNSPECIFIED,
            selector.visibility_filter,
        )
        self.assertFalse("visibility_filter" in selector)
        self.assertEqual(
            Selector.ParticipationFilter.PARTICIPATION_FILTER_UNSPECIFIED,
            selector.participation_filter,
        )
        self.assertFalse("participation_filter" in selector)
        self.assertEqual("", selector.search_query)
        self.assertFalse("search_query" in selector)
        self.assertFalse(selector.require_simulations)
        self.assertFalse("require_simulations" in selector)

    def test_type_safety(self):
        req = ListCompetitionsRequest()

        with self.assertRaises(Exception) as context:
            req.page_size = "14"
        self.assertEqual("page_size must be of type int", str(context.exception))

        with self.assertRaises(Exception) as context:
            req.page_token = 51
        self.assertEqual("page_token must be of type str", str(context.exception))

        with self.assertRaises(Exception) as context:
            req.selector = 21
        self.assertEqual(
            "selector must be of type ListCompetitionsRequest.Selector",
            str(context.exception),
        )

        with self.assertRaises(Exception) as context:
            req.selector = Selector()
            req.selector.list_option = "some value"
        self.assertEqual(
            "list_option must be of type ListCompetitionsRequest.Selector.ListOption",
            str(context.exception),
        )

        with self.assertRaises(Exception) as context:
            req.selector = Selector()
            req.selector.competition_ids = "some value"
        self.assertEqual("competition_ids must be of type list", str(context.exception))

        with self.assertRaises(Exception) as context:
            req.selector = Selector()
            req.selector.competition_ids = ["some value", 12]
        self.assertEqual(
            "competition_ids must contain only items of type int",
            str(context.exception),
        )

    def test_nonexisting_field(self):
        req = ListCompetitionsRequest()

        with self.assertRaises(Exception) as context:
            req.does_not_exist = 1
        self.assertEqual(
            "Unknown field for ListCompetitionsRequest: does_not_exist",
            str(context.exception),
        )

        with self.assertRaises(Exception) as context:
            "does_not_exist" in req
        self.assertEqual(
            'Protocol message ListCompetitionsRequest has no "does_not_exist" field.',
            str(context.exception),
        )

        with self.assertRaises(Exception) as context:
            del req.does_not_exist
        self.assertEqual(
            'Protocol message ListCompetitionsRequest has no "does_not_exist" field.',
            str(context.exception),
        )

    def test_clear_field(self):
        req = ListCompetitionsRequest()
        req.page_size = 10
        req.page_token = "some token"
        req.selector = Selector()

        self.assertTrue("page_size" in req)
        self.assertTrue("page_token" in req)
        self.assertTrue("selector" in req)

        req.page_size = None
        self.assertFalse("page_size" in req)
        req.page_token = None
        self.assertFalse("page_token" in req)
        req.selector = None
        self.assertFalse("selector" in req)

    def test_clear_field_with_del(self):
        req = ListCompetitionsRequest()
        req.page_size = 10
        req.page_token = "some token"
        req.selector = Selector()

        self.assertTrue("page_size" in req)
        self.assertTrue("page_token" in req)
        self.assertTrue("selector" in req)

        del req.page_size
        self.assertFalse("page_size" in req)
        del req.page_token
        self.assertFalse("page_token" in req)
        del req.selector
        self.assertFalse("selector" in req)

    def test_to_dict(self):
        req = ListCompetitionsRequest()
        req.page_size = 100
        req.selector = Selector()
        req.selector.competition_ids.extend([12, 15])
        req.selector.list_option = Selector.ListOption.LIST_OPTION_USER_ENTERED
        req.selector.sort_option = Selector.SortOption.SORT_OPTION_OLDEST
        req.selector.visibility_filter = Selector.VisibilityFilter.VISIBILITY_FILTER_PUBLIC
        req.selector.search_query = "some query"

        json_dict = ListCompetitionsRequest.to_dict(req)

        self.assertEqual(100, json_dict["pageSize"])
        self.assertEqual([12, 15], json_dict["selector"]["competitionIds"])
        self.assertEqual("LIST_OPTION_USER_ENTERED", json_dict["selector"]["listOption"])
        self.assertEqual("SORT_OPTION_OLDEST", json_dict["selector"]["sortOption"])
        self.assertEqual("VISIBILITY_FILTER_PUBLIC", json_dict["selector"]["visibilityFilter"])
        self.assertEqual("some query", json_dict["selector"]["searchQuery"])

    def test_to_dict_empty(self):
        json_dict = ListCompetitionsRequest.to_dict(ListCompetitionsRequest())
        self.assertEqual({}, json_dict)

        json_dict = ListCompetitionsRequest.to_dict(ListCompetitionsRequest(), ignore_defaults=False)
        self.assertEqual(0, json_dict["pageSize"])
        self.assertEqual("", json_dict["pageToken"])
        self.assertIsNone(json_dict["selector"])

    def test_from_dict(self):
        req = ListCompetitionsRequest.from_dict(
            {
                "pageSize": 200,
                "selector": {
                    "tagIds": [1, 3],
                    "hostSegmentIdFilter": 12,
                    "listOption": "LIST_OPTION_USER_HOSTED",
                    "sortOption": "SORT_OPTION_RECENTLY_CLOSED",
                    "participationFilter": "PARTICIPATION_FILTER_LIMITED",
                    "requireSimulations": True,
                },
            }
        )

        self.assertEqual(200, req.page_size)
        self.assertEqual("", req.page_token)
        self.assertEqual([], req.selector.competition_ids)
        self.assertEqual([1, 3], req.selector.tag_ids)
        self.assertEqual(12, req.selector.host_segment_id_filter)
        self.assertEqual(Selector.ListOption.LIST_OPTION_USER_HOSTED, req.selector.list_option)
        self.assertEqual(
            Selector.VisibilityFilter.VISIBILITY_FILTER_UNSPECIFIED,
            req.selector.visibility_filter,
        )
        self.assertEqual(
            Selector.ParticipationFilter.PARTICIPATION_FILTER_LIMITED,
            req.selector.participation_filter,
        )
        self.assertEqual(
            Selector.PrestigeFilter.PRESTIGE_FILTER_UNSPECIFIED,
            req.selector.prestige_filter,
        )
        self.assertEqual("", req.selector.search_query)
        self.assertTrue(req.selector.require_simulations)
        self.assertEqual(0, req.selector.list_for_user_id)


class GetKernelListDetailsRequestTests(unittest.TestCase):

    def test_default_values(self):
        req = GetKernelListDetailsRequest()
        self.assertEqual([], req.kernel_ids)
        self.assertEqual([], req.output_file_types)
        self.assertEqual(0, req.max_output_files_per_kernel)
        self.assertEqual(0, req.gcs_timeout_ms)
        self.assertIsNone(req.read_mask)
        self.assertFalse(req.want_output_files)
        self.assertFalse(req.exclude_results_files_outputs)
        self.assertEqual(AccessBehavior.RETURN_SHELL_ENTRY, req.unauthorized_access_behavior)
        self.assertEqual(AccessBehavior.RETURN_SHELL_ENTRY, req.deleted_access_behavior)

    def test_to_dict(self):
        req = GetKernelListDetailsRequest()
        req.kernel_ids = [101, 102, 103]
        req.output_file_types = ["csv", "sqlite"]
        req.want_output_files = True
        req.read_mask = FieldMask()
        req.read_mask.FromJsonString("author,id,dataSources")

        json_dict = GetKernelListDetailsRequest.to_dict(req)

        self.assertEqual([101, 102, 103], json_dict["kernelIds"])
        self.assertEqual(["csv", "sqlite"], json_dict["outputFileTypes"])
        self.assertTrue(json_dict["wantOutputFiles"])
        self.assertEqual("author,id,dataSources", json_dict["readMask"])

    def test_to_dict_empty(self):
        json_dict = GetKernelListDetailsRequest.to_dict(GetKernelListDetailsRequest())
        self.assertEqual({}, json_dict)

        json_dict = GetKernelListDetailsRequest.to_dict(GetKernelListDetailsRequest(), ignore_defaults=False)
        self.assertEqual([], json_dict["kernelIds"])
        self.assertEqual([], json_dict["outputFileTypes"])
        self.assertIsNone(json_dict["readMask"])
        self.assertEqual("RETURN_SHELL_ENTRY", json_dict["unauthorizedAccessBehavior"])
        self.assertFalse(json_dict["wantOutputFiles"])

    def test_from_dict(self):
        req = GetKernelListDetailsRequest.from_dict(
            {
                "kernelIds": [1, 5, 6, 9],
                "outputFileTypes": ["csv", "png"],
                "unauthorizedAccessBehavior": "RETURN_NOTHING",
                "maxOutputFilesPerKernel": 10,
                "readMask": "author,id",
            }
        )

        self.assertEqual([1, 5, 6, 9], req.kernel_ids)
        self.assertEqual(["csv", "png"], req.output_file_types)
        self.assertEqual(AccessBehavior.RETURN_NOTHING, req.unauthorized_access_behavior)
        self.assertEqual(10, req.max_output_files_per_kernel)
        self.assertEqual(["author", "id"], req.read_mask.paths)
        self.assertEqual(AccessBehavior.RETURN_SHELL_ENTRY, req.deleted_access_behavior)


class KernelSessionTests(unittest.TestCase):

    def test_to_dict(self):
        session = KernelSession()
        session.kernel_id = 12
        session.kernel_run_id = 45
        session.type = KernelVersionType.BATCH
        session.date_created = datetime.datetime.now()
        session.accelerator = AcceleratorType.TPU_V3_8

        json_dict = KernelSession.to_dict(session)

        self.assertEqual(12, json_dict["kernelId"])
        self.assertEqual(45, json_dict["kernelRunId"])
        self.assertEqual("BATCH", json_dict["type"])
        self.assertEqual(
            session.date_created.isoformat(timespec="milliseconds") + "Z",
            json_dict["dateCreated"],
        )
        self.assertEqual("TPU_V3_8", json_dict["accelerator"])

    def test_from_dict(self):
        session = KernelSession.from_dict(
            {
                "kernelId": 15,
                "kernelRunId": 13,
                "title": "some kernel",
                "type": "INTERACTIVE",
                "sourceType": "EDITOR_TYPE_NOTEBOOK",
                "accelerator": "GPU",
                "languageName": "Python",
                "versionName": "new version",
            }
        )

        self.assertEqual(15, session.kernel_id)
        self.assertEqual(13, session.kernel_run_id)
        self.assertEqual("some kernel", session.title)
        self.assertEqual(KernelVersionType.INTERACTIVE, session.type)
        self.assertEqual(EditorType.EDITOR_TYPE_NOTEBOOK, session.source_type)
        self.assertEqual(AcceleratorType.GPU, session.accelerator)
        self.assertEqual("Python", session.language_name)
        self.assertEqual("new version", session.version_name)
        self.assertEqual(0, session.version_number)
        self.assertIsNone(session.date_created)


class DataViewerFilterTests(unittest.TestCase):

    def test_to_dict(self):
        constant1 = ConstantFilter()
        constant1.value = True
        constant2 = ConstantFilter()
        constant2.value = False
        filter1 = Filter()
        filter1.constant_filter = constant1
        filter2 = Filter()
        filter2.constant_filter = constant2
        filter = Filter()
        filter.and_filter = AndFilter()
        filter.and_filter.filters.append(filter1)
        filter.and_filter.filters.append(filter2)

        json_dict = Filter.to_dict(filter)

        self.assertEqual(2, len(json_dict["andFilter"]["filters"]))
        self.assertTrue(json_dict["andFilter"]["filters"][0]["constantFilter"]["value"])
        self.assertIsNone(json_dict["andFilter"]["filters"][1]["constantFilter"].get("value"))

    def test_from_dict(self):
        filter = Filter.from_dict(
            {
                "orFilter": {
                    "filters": [
                        {
                            "constantFilter": {
                                "value": False,
                            }
                        },
                        {
                            "andFilter": {
                                "filters": [
                                    {
                                        "columnFilter": {
                                            "column": {
                                                "firestorePath": "/foo/bar",
                                            },
                                            "booleanFilter": {
                                                "value": True,
                                            },
                                        },
                                    },
                                    {
                                        "constantFilter": {
                                            "value": "True",
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                },
            }
        )

        self.assertIsNone(filter.and_filter)
        self.assertIsNone(filter.not_filter)
        self.assertIsNone(filter.column_filter)
        self.assertIsNone(filter.constant_filter)
        self.assertEqual(2, len(filter.or_filter.filters))
        self.assertFalse(filter.or_filter.filters[0].constant_filter.value)
        self.assertIsNone(filter.or_filter.filters[0].and_filter)
        self.assertIsNone(filter.or_filter.filters[0].or_filter)
        self.assertEqual(2, len(filter.or_filter.filters[1].and_filter.filters))
        self.assertEqual(
            "/foo/bar",
            filter.or_filter.filters[1].and_filter.filters[0].column_filter.column.firestore_path,
        )
        self.assertTrue(filter.or_filter.filters[1].and_filter.filters[0].column_filter.boolean_filter.value)
        self.assertTrue(filter.or_filter.filters[1].and_filter.filters[1].constant_filter.value)

    def test_oneof_clears_others(self):
        filter = Filter()

        filter.and_filter = AndFilter()
        self.assertIsNotNone(filter.and_filter)
        self.assertIsNone(filter.or_filter)
        self.assertIsNone(filter.not_filter)
        self.assertIsNone(filter.column_filter)
        self.assertIsNone(filter.constant_filter)

        filter.constant_filter = ConstantFilter()
        self.assertIsNone(filter.and_filter)
        self.assertIsNone(filter.or_filter)
        self.assertIsNone(filter.not_filter)
        self.assertIsNone(filter.column_filter)
        self.assertIsNotNone(filter.constant_filter)

        filter.column_filter = ColumnFilter()
        self.assertIsNone(filter.and_filter)
        self.assertIsNone(filter.or_filter)
        self.assertIsNone(filter.not_filter)
        self.assertIsNotNone(filter.column_filter)
        self.assertIsNone(filter.constant_filter)

        filter.or_filter = OrFilter()
        self.assertIsNone(filter.and_filter)
        self.assertIsNotNone(filter.or_filter)
        self.assertIsNone(filter.not_filter)
        self.assertIsNone(filter.column_filter)
        self.assertIsNone(filter.constant_filter)

        filter.not_filter = NotFilter()
        self.assertIsNone(filter.and_filter)
        self.assertIsNone(filter.or_filter)
        self.assertIsNotNone(filter.not_filter)
        self.assertIsNone(filter.column_filter)
        self.assertIsNone(filter.constant_filter)


class CategoryTests(unittest.TestCase):

    def test_clear_field(self):
        category = Category()
        category.id = 10
        category.name = "gpu"
        category.description = "GPU category"

        self.assertTrue("id" in category)
        self.assertTrue("name" in category)
        self.assertTrue("description" in category)

        category.id = None
        self.assertFalse("id" in category)
        category.name = None
        self.assertFalse("name" in category)
        category.description = None
        self.assertFalse("description" in category)
        category.description = ""
        self.assertTrue("description" in category)

    def test_clear_field_with_del(self):
        req = ListCompetitionsRequest()
        req.page_size = 10
        req.page_token = "some token"
        req.selector = Selector()

        self.assertTrue("page_size" in req)
        self.assertTrue("page_token" in req)
        self.assertTrue("selector" in req)

        del req.page_size
        self.assertFalse("page_size" in req)
        del req.page_token
        self.assertFalse("page_token" in req)
        del req.selector
        self.assertFalse("selector" in req)

    def test_to_dict(self):
        category = Category()
        category.id = 12
        category.name = "gpu"
        category.full_path = "/gpu"
        category.competition_count = 45
        category.script_count = 0
        category.dataset_count = None

        json_dict = Category.to_dict(category)

        self.assertEqual(12, json_dict["id"])
        self.assertEqual("gpu", json_dict["name"])
        self.assertFalse("description" in json_dict)
        self.assertEqual("/gpu", json_dict["fullPath"])
        self.assertEqual(45, json_dict["competitionCount"])
        self.assertFalse("datasetCount" in json_dict)
        self.assertFalse("scriptCount" in json_dict)
        self.assertFalse("totalCount" in json_dict)

    def test_from_dict(self):
        category = Category.from_dict(
            {
                "id": 15,
                "name": "gpu",
                "fullPath": "",
                "description": "GPU",
                "datasetCount": 12,
                "scriptCount": 21,
                "competitionCount": 0,
            }
        )

        self.assertEqual(15, category.id)
        # Optional field explicitly set to non-default
        self.assertEqual("gpu", category.name)
        self.assertTrue("name" in category)
        # Optional field explicitly set to default
        self.assertEqual("", category.full_path)
        self.assertTrue("full_path" in category)
        # Optional field not set
        self.assertEqual("", category.listing_url)
        self.assertFalse("listing_url" in category)
        # Optional field explicitly set to non-default
        self.assertEqual("GPU", category.description)
        self.assertTrue("description" in category)
        # Optional field not set
        self.assertFalse("", category.tag_url)
        self.assertFalse("tag_url" in category)
        # Non-optional field explicitly set to non-default
        self.assertEqual(12, category.dataset_count)
        self.assertTrue("dataset_count" in category)
        # Non-optional field explicitly set to non-default
        self.assertEqual(21, category.script_count)
        self.assertTrue("script_count" in category)
        # Non-optional field explicitly set to default
        self.assertEqual(0, category.competition_count)
        self.assertFalse("competition_count" in category)
        # Non-optional field not set
        self.assertEqual(0, category.total_count)
        self.assertFalse("total_count" in category)


class BackgroundOperationTests(unittest.TestCase):

    def test_oneof(self):
        operation = BackgroundOperation()

        operation.error = "some error"
        self.assertTrue("error" in operation)
        self.assertEqual("some error", operation.error)
        self.assertFalse("progress" in operation)
        self.assertEqual("", operation.progress)

        operation.progress = "90%"
        self.assertFalse("error" in operation)
        self.assertEqual("", operation.error)
        self.assertTrue("progress" in operation)
        self.assertEqual("90%", operation.progress)


if __name__ == "__main__":
    unittest.main()
