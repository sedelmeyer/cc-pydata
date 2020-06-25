"""
This script contains the cookiecutter hooks that run immediately before the
generation of the ``cc-pydata`` template, but after completing the intial
build prompts.

For more information about cookiecutter hooks, please see:
https://cookiecutter.readthedocs.io/en/1.7.2/advanced/hooks.html

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
