import contextlib
import json
import os
from pathlib import Path
import re

from cookiecutter import main


#: Define absolute path to cc-pydata cookiecutter project directory
CCDIR = Path(__file__).resolve().parents[1]

#: Define path to cookiecutter.json defaults file
CCJSON = CCDIR / 'cookiecutter.json'

#: Define regex string required to identify all jinja-related brackets
JINJA_REGEX = '(\\{{|\\}}|\\{%|\\%}|\\{#|\\#})'


def get_default_template_args(filepath=CCJSON):
    """Load cookiecutter.json to dictionary object

    :param filepath: filepath to cookiecutter.json file, defaults to CCJSON
    :type filepath: str, optional
    :return: dictionary of cookiecutter default arguments
    :rtype: dict
    """
    with open(filepath, 'rt') as fp:
        json_dict = json.load(fp)
    return json_dict


def bake_cookiecutter_template(
    output_dir, template=str(CCDIR), extra_context=None
):
    """Generate the cookiecutter template defined in this project repo

    :param output_dir: directory path in which to generate template
    :type output_dir: str
    :param template: name of cookiecutter template, defaults to str(CCDIR)
    :type template: str, optional
    :param extra_context: dictionary of non-default arguments for cookiecutter
                          template build, defaults to None
    :type extra_context: dict, optional
    """
    main.cookiecutter(
                template=template,
                no_input=True,
                extra_context=extra_context,
                output_dir=output_dir
            )


def find_jinja_brackets(string, regex=JINJA_REGEX):
    """Find all instances of input string that contains jinja brackets

    :param string: text within which to search for jinja brackets
    :type string: str
    :param regex: regular expression pattern, defaults to JINJA_REGEX
    :type regex: str, optional
    :return: list of string instances that match regex
    :rtype: list
    """
    regex_compiled = re.compile(regex)
    result = regex_compiled.findall(string)
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
