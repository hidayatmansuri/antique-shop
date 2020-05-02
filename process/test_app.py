from django.apps import apps
from django.test import TestCase
from .apps import ProcessConfig

class TestProcessConfig(TestCase):
    def test_app(self):
        self.assertEqual("process", ProcessConfig.name)
        self.assertEqual("process", apps.get_app_config("process").name)