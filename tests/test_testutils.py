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

    def test_fix_cookiecutter_jinja_var_string(self):
        """Ensure function removed 'cookiecutter.' substring only"""
        values = [
            "cookiecutter.test",
            "test"
        ]
        for value in values:
            output = tests._fix_cookicutter_jinja_var(value)
            self.assertEqual(output, "test")

    def test_fix_cookiecutter_jinja_var_nonstring(self):
        """Ensure function returns input value when not of type str"""
        value = [
            "cookiecutter.test",
            "test"
        ]
        output = tests._fix_cookicutter_jinja_var(value)
        self.assertEqual(value, output)

    def test_render_json_dict_jinja(self):
        """Ensure only double curley bracket jinja values are rendered"""
        skipped_value1 = "{% now 'utc', '%Y' %}"
        skipped_value2 = ["{{}}", 1, "test"]
        json_dict = {
            'project_name': "test-project",
            'package_name': "{{ project_name|lower|replace(' ','_')|"
                            "replace('-','_') }}",
            'skipped_value1': skipped_value1,
            'skipped_value2': skipped_value2
        }
        new_dict = tests._render_json_dict_jinja(json_dict)
        self.assertEqual(new_dict['project_name'], "test-project")
        self.assertEqual(new_dict['package_name'], "test_project")
        self.assertEqual(new_dict['skipped_value1'], skipped_value1)
        self.assertEqual(new_dict['skipped_value2'], skipped_value2)

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
