"""
tests.toxtest
~~~~~~~~~~~~~

This module contains tests to ensure the ``cc-pydata`` template's ``tox`` tests
run without error.

This is accomplished by rendering the ``cc-pydata`` template to a temporary
directory, then running that template's default ``tox`` configuration to
ensure all ``tox`` environment tests pass without error.

.. warning::

   Tests contained in this module can take considerable time to run and will,
   by default, be ignored when the ``pytest`` test-runner command is invoked.

      * This "ignore" behavior is the result of the naming convention used for
        this module.

In order to run the tests contained in this module, this module will need to
be explicitly specified while invoking the ``pytest`` command.

For example, use this command to run tests contained in this module:

.. code-block:: Bash

   pytest -s tests/toxtest.py

The ``-s`` option will disable all ``stdout`` capturing by ``pytest``, ensuring
that the underlying ``tox`` processes are made visible in ``stdout`` while
the template's ``tox`` script runs.
"""
import contextlib
import shlex
import subprocess
import tempfile
from unittest import TestCase

import tests


class TestTemplateToxConfig(TestCase):
    """Test that the rendered template's default ``tox`` configuration runs"""

    def setUp(self):
        """Render the ``cc-pydata`` template in a temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # build cookie template in temp directory
            self.builtdir = tests.bake_cookiecutter_template(
                output_dir=tmpdir,
                extra_context={'tox': 'yes'}
            )
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_template_tox_runs(self):
        """Ensure ``tox`` runs without error for the rendered template"""
        with tests.working_directory(self.builtdir):
            # run 'git init' so that scm_setuptools versioning works
            subprocess.call(shlex.split('git init'))
            # check that template tox runs wihtout error
            result = subprocess.check_call(
                shlex.split('tox')
            )
            self.assertEqual(result, 0)
