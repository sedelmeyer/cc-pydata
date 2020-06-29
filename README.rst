Cookiecutter PyData
===================

Cookiecutter PyData (``cc-pydata``) is a Cookiecutter_ template for generating "reasonably standardized" skeletons for Python-based data science projects.

.. image:: https://travis-ci.com/sedelmeyer/cc-pydata.svg?branch=master
    :target: https://travis-ci.com/sedelmeyer/cc-pydata

.. image:: https://img.shields.io/badge/License-MIT-black.svg
    :target: https://github.com/sedelmeyer/cc-pydata/blob/master/LICENSE

* **GitHub repo:** https://github.com/sedelmeyer/cc-pydata
* **Full project documentation:** https://sedelmeyer.github.io/cc-pydata


.. contents:: Contents
  :local:
  :backlinks: top

Summary
-------

This Cookiecutter_ template allows for the creation of a "reasonably standardized", but flexible project structure when starting a new Python-based data science project. The benefits of using such a structure and implementing it with Cookiecutter is that it:

* Takes the guesswork and low-value manual labor out of standing up a new data science project,
* Allows you to get started right away on your data science work when starting a new project,
* Creates a sense of consistency across your projects, making it easier for yourself and others to interpret and replicate your analyses and findings.

.. _design:

Design decisions
----------------

While I have attempted to embed Python best practices and standards into the design of this template, best practices and standards change over time. What's more, this template is designed to formalize the workflows (see `Getting started`_) and leverage the tools (see `Features`_) that work best for me across a wide range of projects. If you choose to adopt this template for your own use, you may find these workflows and tools do not work for you without making some changes yourself. For that reason, please feel free to fork and modify your own version of this project.

.. _sources:

Inspiration and sources
^^^^^^^^^^^^^^^^^^^^^^^

When I started building this project, I took note of the workflows and design decisions I began repeating across a number of my Python-based analysis projects. Many of those workflows and decisions were inspired by methods I had learned from others and from patterns codified by other great Cookiecutter templates.

As a result, this template takes inspiration and borrows heavily from these other fabulous Cookiecutter templates available on GitHub:

* `drivendata/cookiecutter-data-science`_
* `ionelmc/cookiecutter-pylibrary`_

For additional background on these other projects and to better understand the elements of both that appealed most to me, please read:

* Ionel Cristian Mărie's articles on `Packaging a python library`_ and `Packaging pitfalls`_,
* Driven Data's fabulous write-up on the `Cookiecutter Data Science`_ template.

.. _features:

Features
--------

The default ``cc-pydata`` template makes use of the following tools and features:

* Pipenv_ for package management and for generating a repeatable environment;
* Automated testing using Tox_;
* Travis-CI_ for continuous integration;
* Versioning with `setuptools_scm`_;
* Out-of-the-box and easily modified ``logging`` functionality;
* Packaging of your custom source code, installed into your working environment as an editable library (i.e. ``-e .``) and easily imported into Jupyter notebooks with natural syntax such as ``from module_name import function_name``;
* Project documentation generated using Sphinx_ and reStructuredText_, ready for hosting alongside your project on GitHub pages.

To see functionality anticipated for future versions of the ``cc-pydata`` template, please see `the Changelog notes regarding future-releases <https://sedelmeyer.github.io/cc-pydata/changelog.html#future-releases>`_.

.. _requirements:

Requirements
------------

Basic prerequisites
^^^^^^^^^^^^^^^^^^^

This template and resulting ``cc-pydata`` project has been tested to work with the following installed dependencies. However, I suspect it will will work with a broader range of ``cookiecutter`` and ``pipenv`` versions than are shown here:

* ``python >= 3.6``
* ``cookiecutter >= 1.7``
* ``pipenv >= 2018-11-26``

For an in-depth review of testing perfomed on this project, please see `the write-up I have provided on "Project testing and the test API" <https://sedelmeyer.github.io/cc-pydata/about.html#project-testing-and-test-api>`_.

Installing ``cookiecutter``
"""""""""""""""""""""""""""

In order to generate this template, you will need ``cookiecutter`` installed on your machine. For instruction on how to install this, please see the `Cookiecutter installation documentation <https://cookiecutter.readthedocs.io/en/1.7.2/installation.html>`_.

Installing ``pipenv``
"""""""""""""""""""""

In addition, because the resulting ``cc-pydata`` project template is configured to use ``pipenv`` for package management, you will also want to enure that you have ``pipenv`` installed on your machine. For more information on ``pipenv`` please see `the documentation <https://pipenv.pypa.io/en/latest/>`_. For instructions on how to properly install ``pipenv``, please see `the official installation instructions <https://pipenv.pypa.io/en/latest/install/#installing-pipenv>`_.

Using an alternative to ``pipenv`` for package management
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you prefer NOT to use ``pipenv`` for packaging and virtual environment management in favor of an alternative such as ``conda`` or ``virtualenv``, you will need to modify the resulting template structure accordingly.


Getting started
---------------

Initiate the ``cc-pydata`` template using Cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have met the basic requirements listed above, generating a new ``cc-pydata`` project template is as easy as executing this in your command line::

  cookiecutter gh:sedelmeyer/cc-pydata

Alternatively, if you have a local working copy of the ``cc-pydata`` project in which you have made customizations to the template, you can run::

  cookiecutter <path-to-directory>/cc-pydata

**For a complete overview on how to generate and configure your** ``cc-pydata`` **data science project,** please see `this project's full tutorial`_.

``cc-pydata`` directory structure
---------------------------------

Below is a high level overview of the resulting directory structure when you generate a ``cc-pydata`` data science project template.

**For a complete overview of the resulting project directory,** please see `the full directory map provided in the tutorial <https://sedelmeyer.github.io/cc-pydata/tutorial.html#cc-pydata-project-template-structure>`_.

.. code::

    cc-pydata Project Directory
    │
    ├── README.rst         <- The top-level README for developers using
    │                         this project
    ├── CHANGLOG.rst       <- Used to document version-by-version
    │                         changes to the project
    ├── Pipfile            <- Requirements file for reproducing the
    │                         analysis environment using the Pipenv
    │                         package manager
    │                         (see pipenv.readthedocs.io)
    ├── .env               <- Sets project-specific environment
    │                         variables such as credentials that you
    │                         do not want committed to Git history
    ├── data/              <- All data files related to the project.
    │                         Files contained in this directory are
    │                         ommitted from Git history via the
    │                         .gitignore file
    ├── docs/              <- A default Sphinx project for generating
    │                         documentation
    ├── models/            <- Trained and serialized models, model
    │                         predictions, or model summaries
    ├── notebooks/         <- Jupyter notebooks, named using a number
    │                         and descriptive title so sequential run
    │                         order and purpose are explicit, e.g.
    │                         `001-EDA-property-assessments`
    ├── references/        <- Data dictionaries, manuals, and all
    │                         other explanatory materials
    ├── reports/           <- Generated analysis as HTML, LaTeX, etc.
    ├── src/               <- Source code for use in this project
    ├── .travis.yml        <- Configuration for Travis-CI services
    │                         (see travis-ci.com)
    ├── logging.json       <- Default logging configuration dictionary
    ├── setup.py           <- Setup script for the project using
    │                         setuptools
    ├── setup.cfg          <- contains option defaults for setup.pydata
    │                         commands
    └── tox.ini            <- Default tox-automated test configuration

.. _other resources:

Other resources
---------------

For further reading, please see `this project's full tutorial`_ as well as these other useful resources:

Cookiecutter resources
^^^^^^^^^^^^^^^^^^^^^^

* The Cookiecutter_ project on GitHub
* The official `Cookiecutter project documentation <https://cookiecutter.readthedocs.io/en/1.7.2/>`_
* Driven Data's `Cookiecutter Data Science project documentation <https://drivendata.github.io/cookiecutter-data-science/>`_, which helped to inspire my ``cc-pydata`` template
* Ionelmc's `ionelmc/cookiecutter-pylibrary`_ project on GitHub, another source of inspiration for my ``cc-pydata`` template

Tools leveraged by ``cc-pydata``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Pipenv_ for package and virtual environment management
* Travis-CI_ for continuous integration
* setuptools_scm_ for project versioning
* Sphinx_ and reStructuredText_ for authoring project documentation
* Pytest_ for use as a Python test-runner
* Tox_ for automated test configuration and matrix testing on multiple versions of Python

Articles related to Python packaging
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `Packaging a python library`_
* `Packaging pitfalls`_
* `Distributing packages using setuptools <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`drivendata/cookiecutter-data-science`: https://github.com/drivendata/cookiecutter-data-science
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _Packaging pitfalls: https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
.. _Cookiecutter Data Science: https://drivendata.github.io/cookiecutter-data-science/
.. _Travis-CI: http://travis-ci.com/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _setuptools_scm: https://github.com/pypa/setuptools_scm/
.. _Pytest: http://pytest.org/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/#
.. _Azure Pipelines: https://azure.microsoft.com/en-us/services/devops/pipelines/

.. _`this project's full tutorial`: https://sedelmeyer.github.io/cc-pydata/tutorial.html
