import contextlib
import json
import os
from pathlib import Path
import re
import shlex
import shutil
import subprocess
import tempfile
from unittest import TestCase

from cookiecutter import main

import tests


#: Define ``project_name`` for default template
project_name = tests.get_default_template_args(tests.CCJSON)['project_name']

#: define ``package_name`` for default template
package_name = project_name.lower().replace('-', '_')

#: Define list of top-level files expected in default template
template_files = [
    '.editorconfig',
    '.env',
    '.gitignore',
    '.travis.yml',
    'CHANGELOG.rst',
    'LICENSE',
    'logging.json',
    'Pipfile',
    'README.rst',
    'setup.cfg',
    'setup.py',
]

#: Define list of src submodule directories expected in default template
template_submodules = [
    'data',
    'features',
    'logger',
    'models',
    'visualizations',
]

#: Define list of sub-directories expected in default template
template_directories = [
    'data',
    'data/raw',
    'data/interim',
    'data/processed',
    'docs',
    'docs/_static/figures',
    'docs/_templates',
    'models',
    'notebooks',
    'references',
    'references/third-party',
    'reports',
    'reports/figures',
    'src',
    *[
        'src/{}/{}'.format(package_name, submod)
        for submod in template_submodules
    ],
    'tests',
    *[
        'tests/{}'.format(submod)
        for submod in template_submodules
    ]
]


class TestBuildDefaultTemplate(TestCase):
    """Test default cookiecutter template build"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # build cookie template in temp directory
            tests.bake_cookiecutter_template(output_dir=tmpdir)
            # get path to built template directory
            self.builtdir = Path(tmpdir).resolve() / project_name
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_project_exists(self):
        """Ensure built template exists in temp dir"""
        self.assertTrue(os.path.isdir(self.builtdir))

    def test_jinja_rendered_dirs(self):
        """Ensire no jinja brackets left over after rendering directories"""
        # loop through all template sub-directories
        for subdir, dirs, files in os.walk(self.builtdir):
            # assert no jinja brackets are present in rendered dirnames
            result = tests.find_jinja_brackets(subdir)
            self.assertEqual(len(result), 0)

    def test_jinja_rendered_files(self):
        """Ensure no jinja brackets are left over after rendering files"""
        # loop through all template files for all sub-directories
        for subdir, dirs, files in os.walk(self.builtdir):
            for filename in files:
                filepath = subdir + os.sep + filename
                print(filepath)
                with open(filepath, 'r') as fn:
                    file_content = fn.read()
                # assert no jinja brackets are present in rendered files
                result = tests.find_jinja_brackets(file_content)
                self.assertEqual(len(result), 0)

    def test_files_exist(self):
        """Ensure specified top-level files exist"""
        for filename in template_files:
            self.assertTrue(os.path.exists(self.builtdir / filename))

    def test_subdirs_exist(self):
        """Ensure all expected sub-directories exist"""
        for dirname in template_directories:
            self.assertTrue(os.path.isdir(self.builtdir / dirname))

    def test_setup_py(self):
        """Ensure rendered template package setup.py returns version number"""
        # change active directory to new template directory
        with tests.working_directory(self.builtdir):
            # run 'git init' so that scm_setuptools versioning works
            subprocess.call(shlex.split('git init'))
            # check that setup.py will return version
            result = subprocess.check_call(
                shlex.split('python setup.py --version')
            )
        self.assertEqual(result, 0)

    def test_default_tests_pass(self):
        """Ensure all default unit-tests pass in rendered template"""
        with tests.working_directory(self.builtdir):
            # move package module out of src to top-level to prevent path error
            shutil.move(os.path.join('src', package_name), '.')
            # run default unit tests in built template and check results
            result = subprocess.check_call(shlex.split('python -m pytest'))
            self.assertEqual(result, 0)

    def test_default_docs_build(self):
        """Ensure default sphinx docs build in rendered template"""
        with tests.working_directory(self.builtdir / 'docs'):
            # run sphinx docs strict build test
            result = subprocess.check_call(
                shlex.split(
                    'sphinx-build -nW -b html -d _build/doctrees . _build/html'
                    )
                )
            self.assertEqual(result, 0)

    def test_default_docs_make_html(self):
        """Ensure default sphinx docs build in rendered template"""
        with tests.working_directory(self.builtdir / 'docs'):
            # run default sphinx make html command
            result = subprocess.check_call(shlex.split('make html'))
            self.assertEqual(result, 0)
