.. _tutorial:

Tutorial
========

This tutorial walks through the basic use of the Cookiecutter PyData template, as well as some of this template's more important features.

.. contents:: Tutorial Contents
  :local:
  :depth: 1
  :backlinks: top

.. _directory structure:

Resulting directory structure
-----------------------------

When you generate a Cookiecutter PyData data science project from this template (see :ref:`getting started`), the resulting project will have the following directory structure::

    PyData Project Directory
    │
    ├── LICENSE
    ├── README.rst         <- Top-level README for developers
    ├── CHANGLOG.rst       <- Used to document version-by-version changes
    ├── Pipfile            <- Requirements file for reproducing the analysis environment
    │                         using the Pipenv package manager (see pipenv.readthedocs.io)
    ├── .env               <- Sets project-specific environmnt variables such as credentials
    │                         that you do not want committed to Git history (see
    │                         pipenv.readthedocs.io/en/latest/advanced/#automatic-loading-of-env)
    ├── data               <- All data files related to the project. Files contained in this
    │   |                     directory are ommitted from Git history via the .gitignore file
    │   ├── raw            <- The original data file(s), this data should never be modified
    │   ├── interim        <- Intermediate data that has been transformed
    │   └── processed      <- The final data set(s) for modeling
    │
    ├── docs               <- A default Sphinx project for generating documentation
    │   └── _static
    │       └── figures    <- Generated graphics and figures to be used in Sphinx generated docs
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks, named using a number and descriptive title
    │                         so sequential run order and purpose are explicit, e.g.
    │                         `001-EDA-property-assessments`
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials
    │   └── third-party    <- Third-party and copyrighted materials you do not want committed to
    │                         Git history
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── src                <- Source code for use in this project
    │   └── <module_name>
    │       ├── __init__.py    <- Makes src a Python module
    │       ├── __main__.py    <- Entry point module
    │       └── cli.py         <- Module for creating the command line app
    │
    ├── .gitignore         <- Specified files to exclude from Git history (as a default, `.env`,
    │                         `./data/` files, and `*/third-party/` files are all excluded)
    ├── .travis.yml        <- Configuration for TravisCI services (see travis-ci.com)
    ├── setup.py           <- Setup script for the project using setuptools (see
    │                         packaging.python.org/guides/distributing-packages-using-setuptools)
    └── setup.cfg          <- contains option defaults for setup.py commands

.. _getting started:

Generating a new template
-------------------------

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

  * Main author of this library or application (used in ``setup.py`` and ``docs/conf.py``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``email``

  * Contact email of the author (used in ``setup.py``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``website``

  * Website of the author (not yet used in resulting template).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``github_username``

  * GitHub user name of this project (used for GitHub links in ``setup.py`` and ``docs/conf.py``).
  * Can be set in your ``~/.cookiecutterrc`` config file.

* ``project_name``

  * Verbose project name, used in headings (docs, readme, etc).

* ``repo_name``

  * Repository name on GitHub (and project's root directory name, used in ``setup.py``, ``docs/conf.py``, and for GitHub links).

* ``package_name``

  * Python package name (whatever you would import).

* ``distribution_name``

  * PyPI distribution name (what you would ``pip install``).

* ``project_short_description``

  * One line description of the project (used in ``README.rst``, ``setup.py``, and ``docs/conf.py``).

* ``release_date``

  * Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.rst``).

* ``year_from``

  * Copyright year (used in Sphinx ``conf.py``).

* ``version``

  * Release version (used in ``setup.py`` and ``docs/conf.py``).

* ``scm_versioning``

  * Enables the use of `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_ (there is currently no option to turn this off, all projects will include this capability by default).

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

  * If you want the Travis-CI_ badge and configuration (currently, this project will always generate with Tracis-CI configuration).

3. Initiate git version control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first thing you should do once your template has been generated is to ``cd`` into your new repository and initiate ``git``::

  cd <newly-generate-directory>
  git init

This step will be required prior to inititating your Pipenv environment because ``setuptools-scm`` is used for versioning your newly generated package. If Git has not yet been initiated for your project, Pipenv install of your local package will fail in the next step below.

4. Install your new Pipenv environment from the Pipfile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have Git version control initiated (see Step 3 above), you can build your working Pipenv virtual environment::

    pipenv install --dev

Note that the ``--dev`` option is specified so that both development and package dependencies are installed in your Pipenv environment.

To activate your environment after it has been created::

    pipenv shell

To deactivate your environment::

    exit

For a more complete overview of how to use Pipenv for package and dependencies management, please see the Pipenv_ project page.

**Congratulations!** You've stood up a new PyData data science project template!

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

Please note that, via the Pipfile, your newly created local package is installed as an editable. For example, the line in the Pipfile that reads::

  package_name = {editable = true,path = "."}

...is equivalent to running this from the command line::

    pipenv install -e .

...which is similar to running the following command in plain old Pip if you were not working from a virtual environment::

    pip install -e .


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

Outlined here is the basic Git workflow for hosting your Sphinx-generated project documentation on `GitHub Pages`_. There are several different methods for configuring GitHub to host your project documentation. The one we will use here is to use a separate ``gh-pages`` Git branch for just your Sphinx-generate site content.

While GitHub can be configured to use the base directory of your ``master`` branch or the ``./docs`` directory of your ``master`` branch, using a separate ``gh-pages`` branch for your site content has the added benefit of keeping your source content separate from your Sphinx-generated build content. This will help to keep your master branch git history storage from ballooning with built site content, particularly when that content can be rebuilt at any time using your historical Git commits.

The basic steps for publishing your GitHub pages content are as follows:

* After running ``make html`` to generate your site content, you need to first create an orphaned ``gh-pages`` branch. Note that this only needs to be done the first time you create this branch::

    git checkout --orphan gh-pages

* By default, all existing files not excluded by your ``.gitignore`` will be staged in your new branch. You will need to remove them all from staging with this command::

    git rm --cached -r .

* Once they're removed from staging and no longer tracked by Git, you can delete them from the gh-pages branch all together. (Don't worry, they will still exist on your ``master`` branch.)::

    git clean -id

* You will then receive a prompt asking you what you want to do. The command you want to specify is ``c`` (clean). By cleaning your repo, your ``gh-pages`` branch will be left containing only your ``.git/`` directory, as well as any other files previously ignored by Git as specified by your ``.gitignore`` file (including your ``docs/_build/html/`` site content).

* Now, to be certain we don't delete or commit any of the other files you had ignored by Git on your ``master`` branch (because these will vanish from your ``master`` branch too if you accidentally delete them), you want to checkout your master version of ``.gitignore``::

    git checkout master -- .gitignore

* If you type ``git status`` you will see that this command has placed your master .gitignore in your ``gh-pages`` staging area, and you will see that Git has gone back to ignoring the other files you'd like ignored. Commit it as such::

    git commit -m "git: add .gitignore from master"

* Now you want to place all of your Sphinx-generated site content into your ``gh-pages`` base directory for rendering by GitHub Pages::

    cp -r docs/_build/html/* .

* Next, add a blank ``.nojekyll`` file to your directory to tell GitHub that you are not using Jekyll (the default site generator for GitHub Pages) to generate your site::

    touch .nojekyll

* If you check ``git status``, you will see that your site content is now visible to git because we have taken it out of the previously ignored ``docs/_build/`` directory.

* Add your site content files to your staging area and commit them::

    git add -A
    git commit -m "docs: add <current release version> site content"

* Then, push the changes to GitHub::

    git push origin gh-pages

* Once committed and pushed, you can return to any of your other branches to continue work on your project::

    git checkout master

* Next time you want to return to your ``gh-pages`` branch to load your latest Sphinx-generated site content to GitHub Pages, you can just checkout that branch and follow the above outlined process again starting with the step of copying over your latest .gitignore in case you've made any edits to it on ``master``::

    git checkout gh-pages
    git checkout master -- .gitignore
    ...

Accessing your new site on GitHub Pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have pushed the first version of your ``gh-pages`` branch to GitHub, GitHub will automatically generate a new site. To view this site, go to your project repo on GitHub, go to Settings, and scroll down until you see the GitHub Pages section of your settings.

There should now appear a hyperlink indicating the URL at which your new site is located. Follow that link and you can preview your site.

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

.. _GitHub Pages: https://pages.github.com/
