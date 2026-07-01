import importlib
import pkgutil
import unittest


class ImportSmokeTest(unittest.TestCase):
    def test_all_kagglesdk_modules_import(self):
        kagglesdk = importlib.import_module("kagglesdk")
        failures = []

        for module in pkgutil.walk_packages(kagglesdk.__path__, kagglesdk.__name__ + "."):
            try:
                importlib.import_module(module.name)
            except Exception as exc:
                failures.append(f"{module.name}: {type(exc).__name__}: {exc}")

        self.assertEqual([], failures)

    def test_kaggle_client_instantiates_with_subclients(self):
        module = importlib.import_module("kagglesdk")
        KaggleClient = module.KaggleClient
        client = KaggleClient()
        expected_groups = (
            "admin",
            "agents",
            "benchmarks",
            "blobs",
            "common",
            "competitions",
            "datasets",
            "discussions",
            "education",
            "kernels",
            "models",
            "search",
            "security",
            "users",
        )

        missing = [name for name in expected_groups if not hasattr(client, name)]
        self.assertEqual([], missing)

        subclient_count = sum(
            1
            for group_name in expected_groups
            for attr_name in vars(getattr(client, group_name))
            if attr_name.endswith("_client")
        )
        self.assertEqual(21, subclient_count)


if __name__ == "__main__":
    unittest.main()
