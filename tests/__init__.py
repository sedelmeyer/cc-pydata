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


def get_default_template_args(filepath):
    """Load cookiecutter.json to dictionary object

    :param filepath: string containing filepath to cookiecutter.json file
    :return: dictionary object containing cookiecutter default arguments
    """
    with open(filepath, 'rt') as fp:
        json_dict = json.load(fp)
    return json_dict


def bake_cookiecutter_template(
    output_dir, template=str(CCDIR), extra_context=None
):
    """Generate the cookiecutter template defined in this project repo
    """
    main.cookiecutter(
                template=template,
                no_input=True,
                extra_context=extra_context,
                output_dir=output_dir
            )


def find_jinja_brackets(input, regex=JINJA_REGEX):
    """Find all instances of input string that contains jinja brackets

    :param input: text within which to search for jinja brackets
    :type input: str
    :param regex: regular expression pattern, defaults to JINJA_REGEX
    :type regex: str, optional
    :return: list of string instances that match regex
    :rtype: list
    """
    regex_compiled = re.compile(regex)
    result = regex_compiled.findall(input)
    return result


@contextlib.contextmanager
def working_directory(directory):
    """Change working directory temporarily with context manager
    """
    original_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(original_directory)
