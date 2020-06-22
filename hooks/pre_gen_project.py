"""
This module contains functions that will run prior to generating the template

Using pre_gen_project actions is useful for ensuring valid names are passed
to cookiecutter arguments.
"""

import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.package_name}}'

if not re.match(MODULE_REGEX, module_name):
    """Ensure the template has been given a valid package_name"""
    print(
        'ERROR: The package name ({}) is not a valid Python module name. '
        'Please do not use a - and use _ instead'.format(module_name)
    )

    #Exit to cancel project
    sys.exit(1)
