"""
{{cookiecutter.package_name}}.cli
{% for _ in cookiecutter.package_name %}{{"~"}}{% endfor %}~~~~

This module that contains the command line app for ``{{cookiecutter.package_name}}``.


Why does this file exist, and why not put this in ``__main__``?

You might be tempted to import things from ``__main__`` later, but that will
cause problems: the code will get executed twice:

* When you run ``python -m {{cookiecutter.package_name}}``, python will execute
  ``__main__.py`` as a script. That means there won't be any
  ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

* When you ``import __main__`` it will get executed again (as a module) because
  there's no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

* Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration


**Module functions:**

.. autosummary::

   main

|
"""
import argparse


parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    """Placeholder function for testing and to illustrate cli

    Prints list of input arguments

    :param args: ``str`` or ``NoneType``, default is ``None``
    """
    args = parser.parse_args(args=args)
    print(args.names)
