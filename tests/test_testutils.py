import os
import tempfile
from unittest import TestCase

import tests


class TestTestsUtilityFunctions(TestCase):
    """Test utility functions contained in the tests/__init__.py file"""

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

    def test_bake_cookie_template(self):
        """Ensure cookie baking recipe works"""
        with tempfile.TemporaryDirectory() as tempdir:
            project_name = 'test_project'
            tests.bake_cookiecutter_template(
                output_dir=tempdir,
                extra_context={
                    'project_name': project_name
                }
            )
            self.assertTrue(
                os.path.isdir(os.path.join(tempdir, project_name))
            )

    def test_find_jinja_brackets(self):
        """Ensure find_jinja_brackets finds all bracket types"""
        string = "{{ test }}, {% test %}, {# test #}"
        results = tests.find_jinja_brackets(string)
        self.assertEqual(len(results), 6)

    def test_find_jinja_brackets_ignores_json(self):
        """Ensure find_jinja_brackets ignores json and dict brackets"""
        string = "{ test }"
        results = tests.find_jinja_brackets(string)
        self.assertEqual(len(results), 0)
