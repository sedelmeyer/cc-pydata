import contextlib
import shlex
import subprocess
import tempfile
from unittest import TestCase

import tests


class TestTemplateToxConfig(TestCase):
    """Test that template's default tox configuration runs without error"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # build cookie template in temp directory
            self.builtdir = tests.bake_cookiecutter_template(output_dir=tmpdir)
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_template_tox_runs(self):
        """Ensure tox runs for default template"""
        with tests.working_directory(self.builtdir):
            # run 'git init' so that scm_setuptools versioning works
            subprocess.call(shlex.split('git init'))
            # check that setup.py will return version
            result = subprocess.check_call(
                shlex.split('tox')
            )
            self.assertEqual(result, 0)
