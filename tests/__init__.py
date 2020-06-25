"""
tests
~~~~~

This module contains global variables and utility functions required for
testing the ``cc-pydata`` cookiecutter template.

Unit tests for these functions can be found in tests.test_testutils submodule

**Module Variables:**

.. autosummary::

   CCDIR
   CCJSON
   JINJA_REGEX

**Module Functions:**

.. autosummary::

   _fix_cookicutter_jinja_var
   _render_json_dict_jinja
   get_default_template_args
   bake_cookiecutter_template
   find_jinja_brackets
   working_directory

|
"""
import contextlib
import json
import os
from pathlib import Path
import re

import jinja2

from cookiecutter import main


#: Define absolute path to cc-pydata cookiecutter project directory
CCDIR = str(Path(__file__).resolve().parents[1])

#: Define path to cookiecutter.json default choice variables file
CCJSON = os.path.join(CCDIR, 'cookiecutter.json')

#: Define regex string required to identify all jinja-related brackets
JINJA_REGEX = '(\\{{|\\}}|\\{%|\\%}|\\{#|\\#})'


def _fix_cookicutter_jinja_var(value, replace='cookiecutter.'):
    """Remove 'cookiecutter.' string from 'cookiecutter.varname' jinja strings

    Can be used to remove different substrings as well by passing a string
    to the optional ``replace`` parameter.

    :param value: The string value within which to replace text
    :type value: str
    :param replace: The string to be removed from the ``value`` input,
                    defaults to 'cookiecutter.'
    :type replace: str, optional
    :return: Returns the input value with the ``replace`` string removed
             if ``value`` is of type str, otherwise it just returns the
             ``value`` input
    """
    if type(value) is str:
        return value.replace(replace, "")
    else:
        return value


def _render_json_dict_jinja(json_dict):
    """Render jinja-templated choice variables in cookiecutter.json dictionary

    .. note::

       This function only modifies dictionary values that are strings containing
       double curly bracket jinja variables such as '{{ varname }}'. All other
       dictionary values are left unmodified.

    :param json_dict: cookiecutter choice variables dictionary
    :type json_dict: dict
    :return: Cookiecutter choice variable dictionary with jinja-templated
             values rendered
    :rtype: dict
    """
    for key, value in json_dict.items():
        if type(value) is str:
            if find_jinja_brackets(value, regex='(\\{{|\\}})'):
                json_dict[key] = jinja2.Template(
                    _fix_cookicutter_jinja_var(value)
                ).render(json_dict)
    return json_dict


def get_default_template_args(filepath=CCJSON):
    """Load cookiecutter.json to dictionary object

    :param filepath: filepath to cookiecutter.json file, defaults to CCJSON
    :type filepath: str, optional
    :return: dictionary of cookiecutter default arguments
    :rtype: dict
    """
    with open(filepath, 'rt') as fp:
        json_dict = json.load(fp)
    json_dict = _render_json_dict_jinja(json_dict)
    return json_dict


def bake_cookiecutter_template(
    output_dir, template=CCDIR, extra_context=None
):
    """Generate the cookiecutter template defined in this project repo

    :param output_dir: directory path in which to generate template
    :type output_dir: str
    :param template: name of cookiecutter template, defaults to CCDIR
    :type template: str, optional
    :param extra_context: dictionary of non-default arguments for cookiecutter
                          template build, defaults to None
    :type extra_context: dict, optional
    :return: path to built cookiecutter template directory
    :rtype: str
    """
    main.cookiecutter(
                template=template,
                no_input=True,
                extra_context=extra_context,
                output_dir=output_dir
            )
    repo_name = os.listdir(output_dir)[0]
    builtdir = os.path.join(output_dir, repo_name)
    return builtdir


def find_jinja_brackets(string, regex=JINJA_REGEX):
    """Find all instances of input string that contains jinja brackets

    :param string: text within which to search for jinja brackets
    :type string: str
    :param regex: regular expression pattern, defaults to JINJA_REGEX
    :type regex: str, optional
    :return: regex search result, True if pattern found, None if not
    :rtype: bool or NoneType
    """
    regex_compiled = re.compile(regex)
    result = regex_compiled.search(string)
    return result


@contextlib.contextmanager
def working_directory(directory):
    """Change working directory temporarily with context manager

    :param directory: path to desired working directory
    :type directory: str
    """
    original_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(original_directory)
