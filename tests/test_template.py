import contextlib
import os
from pathlib import Path
import re
import tempfile
from unittest import TestCase

from cookiecutter import main


#: Define absolute path to cc-pydata cookiecutter project directory
CCDIR = Path(__file__).resolve().parents[1]

#: Define default package_name for template
package_name = 'project_name'

#: Define list of top-level files expected in built template
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

#: Define list of src submodule directories expected in built template
template_submodules = [
    'data',
    'features',
    'logger',
    'models',
    'visualization',
]

#: Define list of sub-directories expected in built template
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


class TestBuildTemplate(TestCase):
    """Test default cookiecutter template build"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # build cookie template in temp directory
            main.cookiecutter(
                template=str(CCDIR),
                no_input=True,
                extra_context=None,
                output_dir=tmpdir
            )
            # get path to built template directory
            self.builtdir = Path(tmpdir).resolve() / 'project_name'
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_project_exists(self):
        """Ensure built template exists in temp dir"""
        self.assertTrue(os.path.isdir(self.builtdir))

    def test_jinja_rendered_files(self):
        """Ensure no curly brackets are left over from jinja build in files"""
        # define regex to find jinja brackets
        regex = re.compile('(\\{{|\\}}|\\{%|\\%})')
        # loop through all template files
        for subdir, dirs, files in os.walk(self.builtdir):
            for filename in files:
                filepath = subdir + os.sep + filename
                print(filepath)
                with open(filepath, 'r') as fn:
                    file_content = fn.read()
                # assert no jinja brackets are present in rendered files
                result = regex.findall(file_content)
                self.assertEqual(len(result), 0)

    def test_files_exist():
        """Ensure top-level files exist"""
        raise NotImplementedError

    def test_subdirs_exist():
        """Ensure top-level sub-directories exist"""
        raise NotImplementedError
