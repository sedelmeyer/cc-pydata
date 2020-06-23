import contextlib
import os
import tempfile
from unittest import TestCase

import tests

#: Define ``project_name`` for default template
project_name = tests.get_default_template_args(tests.CCJSON)['project_name']

#: Define "license" argument options and match strings
license_list = tests.get_default_template_args(tests.CCJSON)['license']


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
        for license_name in license_list[:-1]:
            with tempfile.TemporaryDirectory() as tempdir:
                tests.bake_cookiecutter_template(
                    output_dir=tempdir,
                    extra_context={
                        'license': license_name
                    }
                )
                licpath = os.path.join(tempdir, project_name, 'LICENSE')
                setuppath = os.path.join(tempdir, project_name, 'setup.py')
                print(license_name)
                with open(licpath, 'r') as lic, open(setuppath, 'r') as setup:
                    license_text = lic.read()
                    setup_text = setup.read()
                # confirm that correct license name is listed in each file
                self.assertTrue(
                    license_name.lower() in license_text.lower()
                )
                self.assertTrue(
                    license_name.lower() in setup_text.lower()
                )
                # confirm that neither file contains unrendered jinja
                lic_jinja = tests.find_jinja_brackets(license_text)
                setup_jinja = tests.find_jinja_brackets(setup_text)
                self.assertEqual(len(lic_jinja), 0)
                self.assertEqual(len(setup_jinja), 0)

    def test_not_open_source_license_option(self):
        """Ensure non-open source license option builds correctly"""
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context={
                'license': license_list[-1]
            }
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        # confirm post_gen_project hook removes LICENSE file
        self.assertFalse(
            os.path.exists(os.path.join(builtdir, 'LICENSE'))
        )
        # confirm setup.py generates correctly
        setup_path = os.path.join(builtdir, 'setup.py')
        with open(setup_path, 'r') as setup:
            setup_text = setup.read()
        # confirm that no license classifier is listed
        self.assertTrue(
            'License ::' not in setup_text
        )
        # confirm that file does not contain unrendered jinja
        setup_jinja = tests.find_jinja_brackets(setup_text)
        self.assertEqual(len(setup_jinja), 0)

    def test_travis_option_yes(self):
        """Ensure travis option builds correctly"""
        extra_context = {'travis': 'yes'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        travis_path = os.path.join(builtdir, '.travis.yml')
        self.assertTrue(
            os.path.exists(travis_path)
        )
        with open(travis_path, 'r') as travis:
            travis_text = travis.read()

        results = tests.find_jinja_brackets(travis_text)
        self.assertEqual(len(results), 0)

    def test_travis_option_no(self):
        """Ensure non-travis option builds template and remove .travis.yml"""
        extra_context = {'travis': 'no'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        travis_path = os.path.join(builtdir, '.travis.yml')
        self.assertFalse(
            os.path.exists(travis_path)
        )

    def test_tox_option_yes_exists(self):
        """Ensure tox option builds correctly"""
        extra_context = {'tox': 'yes'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        tox_path = os.path.join(builtdir, 'tox.ini')
        self.assertTrue(
            os.path.exists(tox_path)
        )
        with open(tox_path, 'r') as tox:
            tox_text = tox.read()

        results = tests.find_jinja_brackets(tox_text)
        self.assertEqual(len(results), 0)

    def test_tox_option_yes_travis_correct(self):
        """Ensure tox option builds with correct .travis.yml content"""
        extra_context = {'tox': 'yes', 'travis': 'yes'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        filepath = os.path.join(builtdir, '.travis.yml')
        with open(filepath, 'r') as fp:
            filetext = fp.read()

        self.assertTrue('TOXENV' in filetext)
        results = tests.find_jinja_brackets(filetext)
        self.assertEqual(len(results), 0)

    def test_tox_option_no(self):
        """Ensure no tox option builds correctly and hook removes tox.ini"""
        extra_context = {'tox': 'no'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        tox_path = os.path.join(builtdir, 'tox.ini')
        self.assertFalse(
            os.path.exists(tox_path)
        )

    def test_tox_option_no_travis_correct(self):
        """Ensure no tox option builds with correct .travis.yml content"""
        extra_context = {'tox': 'no', 'travis': 'yes'}
        tests.bake_cookiecutter_template(
            output_dir=self.tmpdir,
            extra_context=extra_context
        )
        builtdir = os.path.join(self.tmpdir, project_name)
        filepath = os.path.join(builtdir, '.travis.yml')
        with open(filepath, 'r') as fp:
            filetext = fp.read()

        self.assertTrue('TOXENV' not in filetext)
        results = tests.find_jinja_brackets(filetext)
        self.assertEqual(len(results), 0)
