Cookiecutter PyData
===================

Cookiecutter PyData is a Cookiecutter_ template for generating "reasonably standardized" skeletons for Python-based data science projects.

.. image:: https://travis-ci.com/sedelmeyer/cc-pydata.svg?branch=master
    :target: https://travis-ci.com/sedelmeyer/cc-pydata

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

.. note::

    This project is in no way complete. This template is being actively developed and will evolve as my work and my development skills evolve.

While I have attempted to embed Python best practices and standards into the design of this template, best practices and standards change over time. What's more, this template is designed to formalize the workflows (see `Getting started`_) and leverage the tools (see `Features`_) that work best for me across a wide range of projects. If you choose to adopt this template for your own use, you may find these workflows and tools do not work for you without making some changes yourself. For that reason, please feel free to fork and modify your own version.

.. _sources:

Inspiration and sources
^^^^^^^^^^^^^^^^^^^^^^^

To begin this project, I took note of the workflows and design decisions I began repeating across a number of my projects, portions of which were heavily inspired by methods I had learned from others and from patterns codified by other great Cookiecutter templates.

For this reason, this template takes inspiration and borrows heavily from these other fabulous Cookiecutter templates available on GitHub:

* `drivendata/cookiecutter-data-science`_
* `ionelmc/cookiecutter-pylibrary`_

For additional background on these other projects and to better understand the elements of both that appealed most to me, please read:

* Ionel's packaging thoughts outlined in his posts on `Packaging a python library`_ and `Packaging pitfalls`_
* Driven Data's fabulous write-up on `Cookiecutter Data Science`_

.. _features:

Features
--------

* Pytest_ for testing Python >=3.5
* Version configuration with `setuptools_scm`_
* Pipenv_ for package management and for generating a repeatable environment
* Travis-CI_ for continuous testing.
* Packaging of modules, installed into your working environment as an editable library (i.e. ``-e .``) and easily imported into Jupyter notebooks with natural syntax such as ``from module_name import function_name``
* Project documentation generated using Sphinx_ and reStructuredText_, ready for hosting alongside your project on GitHub pages.

.. todo::

    * Perhaps add `Azure Pipelines`_ as a secondary CI option
    * Tox_ for managing test environments for Python >=3.5

.. _requirements:

Requirements
------------

.. todo::

    * Include basic system requirements needed to generate and use this template

Getting started
---------------

.. todo::

    * Shorten this section in favor of the new Tutorial page

.. contents:: Contents
  :local:
  :backlinks: none

1. Initiate the template using Cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First generate your project::

  cookiecutter gh:sedelmeyer/cookiecutter-pydata

Alternatively, if you have a local working copy of the ``cookiecutter-pydata`` project in which you've made customizations to the template, you can run::

  cookiecutter <path-to-directory>/cookiecutter-pydata

2. Complete template prompts required to generate template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below listed prompts will be presented on the commandline after generating your project (see Step 1 above). For each prompt, default values will be presented in brackets (i.e. ``full_name [Michael Sedelmeyer]:  ``).

To modify defaults or customize these prompts, please see the ``cookiecutter.json`` file.

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

3. Initiate git version control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first thing you should do once your template has been generated is to ``cd`` into your new repository and initiate ``git``::

  cd <newly-generate-directory>
  git init

This step will be required prior to inititating your Pipenv environment because ``setuptools-scm`` is used for versioning your newly generated package. If Git has not yet been initiated for your project, Pipenv install of your local package will fail in the next step below.

4. Install your new Pipenv environment from the Pipfile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have Git version control initiated (see Step 3 above), you can build your working Pipenv environment ::

Via the Pipfile, your newly created local package is installed as an editable. For example, the line in the Pipfile that reads... ::

  package_name = {editable = true,path = "."}

...is equivalent to running this from the command line... ::

  pipenv install -e .

...which is similar to running the following command in plain old Pip if you were not working from a virtual environment ::

  pip install -e .

For a more complete overview of how to use Pipenv for package and dependencies management, please see the Pipenv_ project page.

.. _directory structure:

Directory structure
-------------------

.. todo::

    * Insert illustration of the directory structure
    * Describe design decisions related to this structure

.. _other resources:

Other resources
---------------

.. todo::

    * Include links to other useful resources

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
