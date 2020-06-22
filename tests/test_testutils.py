import os
import tempfile
from unittest import TestCase

import tests


class TestTestsFunctions(TestCase):
    """Test utility functions contained in the tests __init__.py file"""

    def test_working_directory(self):
        """Ensure working_directory context manager works as expected"""
        with tempfile.TemporaryDirectory() as tempdir:
            original_directory = os.getcwd()
            with tests.working_directory(tempdir):
                self.assertEqual(tempdir, os.getcwd())
            self.assertEqual(original_directory, os.getcwd())

    def test_get_default_template_args(self):
        """Ensure default template arg"""
        json_dict = tests.get_default_template_args(tests.CCJSON)
        self.assertEqual(type(json_dict), dict)
