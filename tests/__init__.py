import contextlib
import json
import os
from pathlib import Path
import re


#: Define absolute path to cc-pydata cookiecutter project directory
CCDIR = Path(__file__).resolve().parents[1]

#: Define path to cookiecutter.json defaults file
CCJSON = CCDIR / 'cookiecutter.json'


def get_default_template_args(filepath):
    """Load cookiecutter.json to dictionary object

    :param filepath: string containing filepath to cookiecutter.json file
    :return: dictionary object containing cookiecutter default arguments
    """
    with open(filepath, 'rt') as fp:
        json_dict = json.load(fp)
    return json_dict


@contextlib.contextmanager
def working_directory(directory):
    """Change working directory temporarily with context manager"""
    original_directory = os.getcwd()
    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(original_directory)
