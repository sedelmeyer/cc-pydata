"""
tests.test_options
~~~~~~~~~~~~~~~~~~

This module contains tests for optional ``cc-pydata`` template build options
"""
import contextlib
import os
import tempfile
from unittest import TestCase

import tests

#: Load cookicutter.json to dictionary
json_dict = tests.get_default_template_args(tests.CCJSON)

#: Define "license" choice variable argument options
license_list = json_dict['license']


class TestBuildTemplateOption(TestCase):
    """Test default cookiecutter template build"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_build_fails_invalid_package_name(self):
        """Ensure template build fails with invalid package name"""
        with self.assertRaises(Exception):
            extra_context = {'package_name': 'test-invalid'}
            tests.bake_cookiecutter_template(
                output_dir=self.tmpdir,
                extra_context=extra_context
            )

    def test_open_source_license_options(self):
        """Ensure open source license options build correctly"""
        open_source_licenses = [
            license_name for license_name in license_list
            if license_name != "Not open source"
        ]
        # iterate through list of open source licenses and bake each cookie
        for license_name in open_source_licenses:
            with tempfile.TemporaryDirectory() as tempdir:
                builtdir = tests.bake_cookiecutter_template(
                    output_dir=tempdir,
                    extra_context={
                        'license': license_name
                    }
                )
                # check the files affected by the license choice
                for filename in ['LICENSE', 'setup.py']:
                    content = tests.read_template_file(builtdir, filename)
                    # confirm that correct license name is listed in each file
                    self.assertTrue(
                        license_name.lower() in content.lower()
                    )
                    # confirm that neither file contains unrendered jinja
                    self.assertIsNone(tests.find_jinja_brackets(content))

    def test_not_open_source_license_option(self):
        """Ensure non-open source license option builds correctly"""
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context={
                'license': "Not open source"
            }
        )
        # confirm post_gen_project hook removes LICENSE file
        self.assertFalse(
            os.path.exists(os.path.join(builtdir, 'LICENSE'))
        )
        # confirm setup.py generates correctly
        content = tests.read_template_file(builtdir, 'setup.py')
        # confirm that no license classifier is listed
        self.assertTrue(
            'License ::' not in content
        )
        # confirm that file does not contain unrendered jinja
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_travis_option_yes(self):
        """Ensure travis option builds correctly"""
        extra_context = {'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        self.assertTrue(
            os.path.exists(os.path.join(builtdir, '.travis.yml'))
        )
        content = tests.read_template_file(builtdir, '.travis.yml')
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_travis_option_no(self):
        """Ensure non-travis option builds template and remove .travis.yml"""
        extra_context = {'travis': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        travis_path = os.path.join(builtdir, '.travis.yml')
        self.assertFalse(
            os.path.exists(travis_path)
        )

    def test_tox_option_yes_exists(self):
        """Ensure tox option builds correctly"""
        extra_context = {'tox': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        self.assertTrue(
            os.path.exists(os.path.join(builtdir, 'tox.ini'))
        )
        content = tests.read_template_file(builtdir, 'tox.ini')
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_tox_option_yes_travis_correct(self):
        """Ensure tox option builds with correct .travis.yml content"""
        extra_context = {'tox': 'yes', 'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, '.travis.yml')
        self.assertTrue('TOXENV' in content)
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_tox_option_no(self):
        """Ensure no tox option builds correctly and hook removes tox.ini"""
        extra_context = {'tox': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        tox_path = os.path.join(builtdir, 'tox.ini')
        self.assertFalse(
            os.path.exists(tox_path)
        )

    def test_tox_option_no_travis_correct(self):
        """Ensure no tox option builds with correct .travis.yml content"""
        extra_context = {'tox': 'no', 'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, '.travis.yml')
        self.assertTrue('TOXENV' not in content)
        self.assertIsNone(tests.find_jinja_brackets(content))
