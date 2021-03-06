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

#: Load ``cookicutter.json`` to dictionary
json_dict = tests.get_default_template_args(tests.CCJSON)

#: Define ``'license'`` choice variable argument options
license_list = json_dict['license']


class TestBuildTemplateOption(TestCase):
    """Test optional cookiecutter template build arguments"""

    def setUp(self):
        """Generate temporary directory in which to render templates"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_build_pre_hook_invalid_package_name_fails(self):
        """Ensure template build fails with invalid ``package_name``"""
        with self.assertRaises(Exception):
            extra_context = {'package_name': 'test-invalid'}
            tests.bake_cookiecutter_template(
                output_dir=self.tmpdir,
                extra_context=extra_context
            )

    def test_license_open_source_options(self):
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

    def test_license_not_open_source(self):
        """Ensure 'Not open source' license option builds correctly"""
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

    def test_travis_yes_yaml(self):
        """Ensure travis 'yes' option builds with ``travis.yml`` file"""
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

    def test_travis_yes_badge(self):
        """Ensure travis 'yes' option includes badge in docs"""
        extra_context = {'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        readme_content = tests.read_template_file(builtdir, 'README.rst')
        print(readme_content)
        self.assertTrue(
            '\n.. image:: https://travis-ci.com/' in readme_content
        )
        self.assertIsNone(tests.find_jinja_brackets(readme_content))
        conf_content = tests.read_template_file(builtdir, 'docs/conf.py')
        self.assertTrue("'travis_button': 'true'," in conf_content)
        self.assertIsNone(tests.find_jinja_brackets(conf_content))

    def test_travis_no_yaml(self):
        """Ensure travis 'no' option removes ``.travis.yml``"""
        extra_context = {'travis': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        travis_path = os.path.join(builtdir, '.travis.yml')
        self.assertFalse(
            os.path.exists(travis_path)
        )

    def test_travis_no_badge(self):
        """Ensure travis 'no' option does not include badge in docs"""
        extra_context = {'travis': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        readme_content = tests.read_template_file(builtdir, 'README.rst')
        self.assertTrue(
            '.. image:: https://travis-ci.com/' not in readme_content
        )
        self.assertIsNone(tests.find_jinja_brackets(readme_content))
        conf_content = tests.read_template_file(builtdir, 'docs/conf.py')
        self.assertTrue("'travis_button': 'false'," in conf_content)
        self.assertIsNone(tests.find_jinja_brackets(conf_content))

    def test_tox_yes_ini(self):
        """Ensure tox 'yes' option builds with ``tox.ini`` file"""
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

    def test_tox_yes_pipfile(self):
        """Ensure tox 'yes' option adds tox install to ``Pipfile``"""
        extra_context = {'tox': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, 'Pipfile')
        self.assertTrue('tox' in content)
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_tox_yes_travis_yes_yaml(self):
        """Ensure tox and travis 'yes' option builds correct ``.travis.yml``"""
        extra_context = {'tox': 'yes', 'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, '.travis.yml')
        self.assertTrue('TOXENV' in content)
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_tox_no_ini(self):
        """Ensure tox 'no' option removes ``tox.ini``"""
        extra_context = {'tox': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        tox_path = os.path.join(builtdir, 'tox.ini')
        self.assertFalse(
            os.path.exists(tox_path)
        )

    def test_tox_no_pipfile(self):
        """Ensure tox 'no' option removes ``tox`` install from ``Pipfile``"""
        extra_context = {'tox': 'no'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, 'Pipfile')
        self.assertTrue('tox' not in content)
        self.assertIsNone(tests.find_jinja_brackets(content))

    def test_tox_no_travis_yes_yaml(self):
        """Ensure tox 'no' option builds with correct ``.travis.yml``"""
        extra_context = {'tox': 'no', 'travis': 'yes'}
        builtdir = tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        content = tests.read_template_file(builtdir, '.travis.yml')
        self.assertTrue('TOXENV' not in content)
        self.assertIsNone(tests.find_jinja_brackets(content))
