Cookiecutter PyData
===================

Cookiecutter PyData is a Cookiecutter_ template for generating a "reasonably standardized" skeleton for Python-based data science projects.

.. contents:: Contents
  :local:
  :backlinks: none

Summary
-------

This Cookiecutter_ template allows for the creation of a "reasonably standardized", but flexible project structure when starting a new Python-based data science project. The benefits of using such a structure and implementing it with Cookiecutter is that it:

* Takes the guesswork and low-value manual labor out of standing up a new data science project
* Allows you to get started right away on your data science work when stating a new project
* Creates a sense of consistency across your projects, making it easier for yourself and others to interpret and replicate your analyses and findings.

Design decisions
----------------

**This project is in no way complete.** This template is being actively developed and will evolve as my work and my development skills evolve. While I have attempted to embed Python best practices and standards into the design of this template, best practices and standards change over time. What's more, this template is designed to formalize the workflows (see `Getting started`_) and leverage the tools (see `Features`_) that work best for me across a wide range of projects. If you choose to adopt this template for your own use, you may find these workflows and tools do not work for you without making some changes yourself. For that reason, please feel free to fork and modify your own version.

Inspiration and sources
^^^^^^^^^^^^^^^^^^^^^^^

To begin this project, I took note of the workflows and design decisions I began repeating across a number of my projects, portions of which were heavily inspired by methods I had learned from others and from patterns codified by other great Cookiecutter templates.

For this reason, this template takes inspiration and borrows heavily from these other fabulous Cookiecutter templates available on GitHub:

* `drivendata/cookiecutter-data-science`_
* `ionelmc/cookiecutter-pylibrary`_

For additional background on these other projects and to better understand the elements of both that appealed most to me, please read:

* Ionel's packaging thoughts outlined in his posts on `Packaging a python library`_ and `Packaging pitfalls`_
* Driven Data's fabulous write-up on `Cookiecutter Data Science`_

Features
--------

* Pytest_ for testing Python >=3.5
* Version configuration with `setuptools_scm`_
* Pipenv_ for package management and for generating a repeatable environment
* Travis-CI_ for continuous testing.
* Packaging of modules, installed into your working environment as an editable library (i.e. ``-e .``) and easily imported into Jupyter notebooks with natural syntax such as ``from module_name import function_name``

*TODO*

* Perhaps add `Azure Pipelines`_ as a secondary CI option 
* Tox_ for managing test environments for Python >=3.5
* Project documentation generated using Sphinx_ and reStructuredText_, ready for hosting alongside your project on GitHub pages. 

Requirements
------------

TODO

Getting started
---------------

First generate your project::

  cookiecutter gh:sedelmeyer/cookiecutter-pydata

You will be asked for to enter these fields:

* ``full_name``
  
  * Main author of this library or application (used in ``AUTHORS.rst`` and ``setup.py``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``email``

  * Contact email of the author (used in ``AUTHORS.rst`` and ``setup.py``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``website``
  
  * Website of the author (used in ``AUTHORS.rst``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``github_username``
  
  * GitHub user name of this project (used for GitHub link).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``project_name``
  
  * Verbose project name, used in headings (docs, readme, etc).

* ``repo_name``
  
  * Repository name on GitHub (and project's root directory name).

* ``package_name``
  
  * Python package name (whatever you would import).

* ``distribution_name``
  
  * PyPI distribution name (what you would ``pip install``).

* ``project_short_description``
  
  * One line description of the project (used in ``README.rst`` and ``setup.py``).

* ``release_date``
  
  * Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.rst``).

* ``year_from``
  
  * Copyright year (used in Sphinx ``conf.py``).

* ``version``
  
  * Release version (see ``.bumpversion.cfg`` and in Sphinx ``conf.py``).

* ``scm_versioning``
  
  * Enables the use of `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_.

* ``license``
  
  * License to use. Available options:

    * MIT license
    * BSD 2-Clause license
    * BSD 3-Clause license
    * ISC license
    * Apache Software License 2.0

  * What license to pick? https://choosealicense.com/

* ``test_runner``
  
  * Test runner to use. Currently only configured for ``pytest``.

* ``linter``
  
  * Available options: ``flake8`` only

* ``command_line_interface``
  
  * Option to enable a CLI (a bin/executable file). Available options:

    * ``plain`` - a very simple command.
    * ``argparse`` - a command implemented with ``argparse``.
    * ``click`` - a command implemented with `click <http://click.pocoo.org/>`_ * ``no`` - no CLI at all.

* ``command_line_interface_bin_name``
  
  * Name of the CLI bin/executable file (set the console script name in ``setup.py``).

* ``travis``
  
  * If you want the Travis-CI_ badge and configuration.

Directory structure
-------------------

TODO

Other resources
---------------

TODO


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`drivendata/cookiecutter-data-science`: https://github.com/drivendata/cookiecutter-data-science
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _Packaging pitfalls: https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
.. _Cookiecutter Data Science: https://drivendata.github.io/cookiecutter-data-science/
.. _Travis-CI: http://travis-ci.org/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _setuptools_scm: https://github.com/pypa/setuptools_scm/
.. _Pytest: http://pytest.org/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/#
.. _Azure Pipelines: https://azure.microsoft.com/en-us/services/devops/pipelines/