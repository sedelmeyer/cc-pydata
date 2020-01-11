Cookiecutter PyData
===================

Cookiecutter PyData is a Cookiecutter_ template for generating "reasonably standardized" skeletons for Python-based data science projects.

.. image:: https://travis-ci.com/sedelmeyer/cc-pydata.svg?branch=master
    :target: https://travis-ci.com/sedelmeyer/cc-pydata

* **GitHub repo:** https://github.com/sedelmeyer/cc-pydata
* **Full project documentation:** https://sedelmeyer.github.io/cc-pydata


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

Initiate the template using Cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have met the basic requirements listed above, generating a new Cookiecutter PyData project skeleton is as easy as executing this in your command line::

  cookiecutter gh:sedelmeyer/cc-pydata

Alternatively, if you have a local working copy of the ``cookiecutter-pydata`` project in which you've made customizations to the template, you can run::

  cookiecutter <path-to-directory>/cc-pydata

**For a complete overview on how to generate and configure your Cookiecutter PyData data science project,** please see `this project's full tutorial`_.

Directory structure
-------------------

Below is a high level overview of the resulting directory structure when you generate a Cookiecutter PyData data science project.

**For a complete overview of the resulting project directory,** please see `this project's full tutorial`_.

.. code::

    PyData Project Directory
    │
    ├── README.rst         <- The top-level README for developers using this project
    ├── CHANGLOG.rst       <- Used to document version-by-version changes to the project
    ├── Pipfile            <- Requirements file for reproducing the analysis environment
    │                         using the Pipenv package manager (see pipenv.readthedocs.io)
    ├── .env               <- Sets project-specific environmnt variables such as credentials
    │                         that you do not want committed to Git history (see
    │                         pipenv.readthedocs.io/en/latest/advanced/#automatic-loading-of-env)
    ├── data               <- All data files related to the project. Files contained in this
    │                         directory are ommitted from Git history via the .gitignore file    │
    ├── docs               <- A default Sphinx project for generating documentation
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    ├── notebooks          <- Jupyter notebooks, named using a number and descriptive title
    │                         so sequential run order and purpose are explicit, e.g.
    │                         `001-EDA-property-assessments`
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    ├── src                <- Source code for use in this project
    ├── .travis.yml        <- Configuration for TravisCI services (see travis-ci.com)
    ├── setup.py           <- Setup script for the project using setuptools (see
    │                         packaging.python.org/guides/distributing-packages-using-setuptools)
    └── setup.cfg          <- contains option defaults for setup.py commands

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

.. _`this project's full tutorial`: https://sedelmeyer.github.io/cc-pydata/tutorial.html
