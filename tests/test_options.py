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


class TestBuildTemplateOption(TestCase):
    """Test default cookiecutter template build"""

    def setUp(self):
        """Build template in temporary directory"""
        with contextlib.ExitStack() as stack:
            # open temp directory context manager
            self.tmpdir = tmpdir = stack.enter_context(
                tempfile.TemporaryDirectory()
            )
            # ensure context manager closes after tests
            self.addCleanup(stack.pop_all().close)

    def test_build_fails_invalid_package_name(self):
        """Ensure template build fails with invalid package name"""
        raise NotImplementedError

    def test_open_source_license_options(self):
        """Ensure open source license options build"""
        raise NotImplementedError

    def test_not_open_source_license_option(self):
        """Ensure non-open source license option builds"""
        raise NotImplementedError

    def test_travis_option_yes(self):
        """Ensure travis option builds"""
        raise NotImplementedError

    def test_travis_option_no(self):
        """Ensure non-travis option builds"""
        raise NotImplementedError

    def test_tox_option_yes(self):
        """Ensure tox option builds and passes tests"""
        raise NotImplementedError

    def test_tox_option_no(self):
        """Ensure non-tox option builds"""
        raise NotImplementedError
