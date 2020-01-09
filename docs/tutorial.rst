.. _tutorial:

Tutorial
========

This tutorial walks through the basic use of the Cookiecutter PyData template, as well as some of this template's more important features.

.. contents:: Tutorial Contents
  :local:
  :depth: 1
  :backlinks: none

.. _getting started:

Generating a new template
-------------------------

.. todo::

    * Update this section to ensure prompt details better reflect recent template changes

.. contents:: In this section
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

The below listed prompts will be presented on the commandline after generating your project (see Step 1 above). For each prompt, default values will be presented in brackets (i.e. ``full_name [Michael Sedelmeyer]:``).

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

Once you have Git version control initiated (see Step 3 above), you can build your working Pipenv environment::

Via the Pipfile, your newly created local package is installed as an editable. For example, the line in the Pipfile that reads...::

  package_name = {editable = true,path = "."}

...is equivalent to running this from the command line...::

  pipenv install -e .

...which is similar to running the following command in plain old Pip if you were not working from a virtual environment::

  pip install -e .

For a more complete overview of how to use Pipenv for package and dependencies management, please see the Pipenv_ project page.

**CONGRATULATIONS! You've stood up a new PyData data science project template!**

**Now it's time to explore some of the features of this template!**

.. _packaging:

Packaging characteristics of this template
------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Using Pipenv to manage your project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Include basic Pipenv_ usage for this project
    * Discuss ``pipenv shell``
    * Discuss use of Pipfile versus ```install requires`` and link to an article discussing the differences

Managing environment variables with the ``.env`` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Discuss the purpose and usage of the ``.env`` file
    * Specify the importance of never committing your ``.env`` file to git history
    * Discuss Pipenv's default behavior for importing ``.env`` files and the means by which to programmatically access those variables
    * Include this link `Pipenv loading of .env`_


Accessing modules in your package from a Jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    Describe usage of ``from <your-package-name> import <module-name>`` behavior in Jupyter notebooks

Versioning your project
^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Describe versioning of project using `setuptools_scm`_
    * Include link to article `Single-sourcing the package version`_

Documenting your project using Sphinx and GitHub Pages
------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Getting started with Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resulting project template is configured to use reStructuredText_ and Sphinx_ to generate and maintain your resulting project documentation.

.. todo::

    * Describe the basic usage of Sphinx to build and maintain documentation
    * Specify that the ``docs/_build`` directory should not be committed to git history
    * Discuss the significance of reStructuredText_ versus Markdown
    * Include links to important resources line `reStructuredText primer`_

Hosting your project documentation using GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Describe the basic nuances of managing git branches and pushing to gh-pages in conjunction with Sphinx
    * Lay out basic ``bash`` workflow

Test configuration and continuous integration with TravisCI
-----------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Unit-testing your project and using the PyTest runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Explain where and how should unit tests be included for this package
    * Describe the use of the PyTest runner and associated configuration established for test coverage reporting

Configuring and leveraging TravisCI for your project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

    * Describe the basic .travis.yml configuration
    * Describe basic steps to set up CI integration with TravisCI for your project


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

.. _Pipenv loading of .env: https://pipenv.kennethreitz.org/en/latest/advanced/#automatic-loading-of-env
.. _Single-sourcing the package version: _https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
.. _reStructuredText primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
