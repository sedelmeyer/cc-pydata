.. _tutorial:

Tutorial
========

This tutorial walks through the basic use of the Cookiecutter PyData (i.e. ``cc-pydata``) template, as well as some of this template's more important features.

.. contents:: Tutorial Contents
  :local:
  :depth: 1
  :backlinks: top

.. _directory structure:

``cc-pydata`` project template structure
----------------------------------------

When you generate a ``cc-pydata`` data science project from this template (see :ref:`getting started`), the resulting project will have the following directory structure::

    cc-pydata Project Directory
    │
    ├── LICENSE
    ├── README.rst        <- Top-level README for developers
    ├── CHANGLOG.rst      <- Documents version-by-version changes
    ├── Pipfile           <- Requirements file for reproducing the
    │                        analysis environment using the Pipenv
    │                        package manager
    │                        (see pipenv.readthedocs.io)
    ├── .env              <- Sets project-specific environmnt variables
    │                        such as credentials that you do not want
    │                        committed to Git history
    ├── data              <- All data files related to the project.
    │   |                    Files contained in this directory are
    │   │                    ommitted from Git history via .gitignore
    │   ├── raw           <- The original data file(s) that, for the
    │   │                    purpose of reproducibility, should never
    │   │                    be modified
    │   ├── interim       <- Data that has been cleaned or transformed
    │   └── processed     <- The final data set(s) used for modeling
    │
    ├── docs              <- A default Sphinx project for generating
    │   │                    project documentation
    │   └── _static
    │       └── figures   <- Generated graphics and figures to be used
    │                        in Sphinx generated docs
    ├── models            <- Trained and serialized models, model
    │                        predictions, or model summaries
    │
    ├── notebooks         <- Jupyter notebooks, named using a number
    │                        and descriptive title so sequential run-
    │                        order and purpose are explicit, e.g.
    │                        "001-EDA-property-assessments.ipynb"
    │
    ├── references        <- Data dictionaries, manuals, and all other
    │   │                    explanatory materials
    │   └── third-party   <- Third-party and copyrighted materials you
    │                        do not want committed to Git history
    │
    ├── reports           <- Generated analysis as HTML, PDF, etc.
    │   └── figures       <- Generated graphics and figures to be used
    │                        in reporting
    │
    ├── src               <- Source code for use in this project
    │   └── <package-name>
    │       ├── data           <- Submodule for downloading and
    │       │                     cleansing data
    │       ├── features       <- Submodule for generating engineered
    │       │                     features for modeling
    │       ├── models         <- Submodule for training models and
    │       │                     generating predictions
    │       ├── visualizations <- Submodule for generating
    │       │                     visualizations
    │       ├── logger         <- Submodule for project logging-related
    │       │                     functionality
    │       ├── __init__.py    <- Makes src a Python module
    │       ├── __main__.py    <- Entry point module
    │       └── cli.py         <- Module for creating the command line
    │                             interface for the project
    │
    ├── .gitignore        <- Specified files to exclude from Git
    │                        history (as a default, `.env`, `./data/`
    │                        files, and `*/third-party/` files are all
    │                        excluded)
    ├── .travis.yml       <- Configuration for Travis-CI services
    │                        (see travis-ci.com)
    ├── logging.json      <- Default logging configuration dictionary
    ├── setup.py          <- Setup script for the project using
    │                        setuptools
    └── setup.cfg         <- Option defaults for setup.py commands

.. _getting started:

Generating a new template
-------------------------

.. contents:: In this section
  :local:
  :backlinks: none

0. Ensure all prerequisites are met
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the :ref:`requirements` section of the :ref:`readme` README documentation to ensure basic system dependencies are met.

1. Initiate the template using Cookiecutter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Generating a ``cc-pydata`` project template is as simple as running the following command from your terminal::

  cookiecutter gh:sedelmeyer/cc-pydata

Alternatively, if you have a local working copy of the ``cc-pydata`` project in which you've made customizations to the template, you can run::

  cookiecutter <path-to-directory>/cc-pydata


2. Complete template prompts required to generate the template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The below listed prompts will be presented on the command line after generating your project (see Step 1 above). For each prompt, default values will be presented in brackets (i.e. ``full_name [Michael Sedelmeyer]:``).

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
    * ``click`` - a command implemented with `click <http://click.pocoo.org/>`_
    * ``no`` - no CLI at all.

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

.. _install-pipenv:

4. Install your new ``pipenv`` environment from the Pipfile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have Git version control initiated (see Step 3 above), you can build your working Pipenv_ virtual environment::

    pipenv install --dev

Note that the ``--dev`` option is specified so that both development and package dependencies are installed in your Pipenv environment.

To activate your environment after it has been created::

    pipenv shell

To deactivate your environment::

    exit

For a more complete overview of how to use ``pipenv`` for package and dependencies management, please see the Pipenv_ project page.

**Congratulations!** You've stood up a new ``cc-pydata`` data science project template!

**Now it's time to explore some of the features of this template!**

.. _packaging:

Packaging characteristics of this template
------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Using ``pipenv`` to manage your project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are new to ``pipenv`` for dependency and package management, it may take a little time to get used to it. The best place to start is by taking some time to review core principles, benefits, and usage on the Pipenv_ project page.

Chances are, if you have been using ``virtualenv`` or ``conda`` to manage your Python virtual environments up to this point, then you'll probably wonder how you've made it this far without using ``pipenv`` previously. As is described on the Pipenv_ project page:

    "**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. *Windows is a first-class citizen, in our world.*"

    "It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your ``Pipfile`` as you install/uninstall packages. It also generates the ever-important ``Pipfile.lock``, which is used to produce deterministic builds."


Adding / installing dependencies using ``pipenv``
"""""""""""""""""""""""""""""""""""""""""""""""""

As was shown in the section :ref:`install-pipenv` above, creating a ``pipenv`` environment and ``Pipfile.lock`` deterministic build is as easy as running ``pipenv install --dev`` from your ``cc-pydata`` project directory.

To add additional dependencies to your project, you can either:

#. Edit your ``Pipfile`` list of dependencies directly, adding application-specific dependencies under the ``[packages]`` section or development-specific dependencies under the ``[dev-packages]`` section of the ``Pipfile``, then run ``pipenv install --dev`` to install the dependencies and update the ``Pipfile.lock`` build document.

#. Or, more easily, you can run ``pipenv install <pip-package-name>`` to add and install a new application dependency, or ``pipenv install --dev <pip-package-name>`` to add and install a new development dependency. When you add a dependency in this manner, not only will the dependency be installed in your ``pipenv`` environment, but ``pipenv`` will also automatically updated your ``Pipfile`` and ``Pipfile.lock`` to reflect the newly added dependency.

There are many additional actions you can take to update and change dependencies using ``pipenv``.

* To learn more, please see the `documentation on the basic usage of Pipenv <https://pipenv.pypa.io/en/latest/basics/>`_.

* If your preference is to manage dependencies using the ``setup.py`` ``install_requires`` argument, please take some time to `read the distinctions between Pipfile vs. setup.py <https://pipenv.pypa.io/en/latest/advanced/#pipfile-vs-setuppy>`_, and think carefully about the distinctions between managing dependencies for a Python "application" such as that which you are creating with the ``cc-pydata`` template versus a Python "library", which the ``cc-pydata`` template is not.


Installing your local ``cc-pydata`` package as an editable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
If you inspect the ``cc-pydata`` template's default ``Pipfile``, you will see that ``pipenv`` will install your newly created local ``cc-pydata`` package as an "editable" under the ``[packages]`` section of that ``Pipfile``. More specifically, the line in the ``Pipfile`` that reads::

  package_name = {editable = true,path = "."}

...is equivalent to running this from the command line::

    pipenv install -e .

...which is similar to running the following command in plain old Pip if you were not working from a virtual environment::

    pip install -e .

.. _env:

Managing environment variables with the ``.env`` file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you generate a new ``cc-pydata`` project using this template, by default you will be provided with a ``.env`` file in which you can set environment variables specific to your project.

* This ``.env`` file can be used for setting secret keys, credentials, or filepaths you need for your project, but would like to keep secret.
* By default, the ``.gitignore`` for this project is set to ignore the ``.env`` file.
* It is strongly, strongly, strongly suggested that you NEVER commit your ``.env`` file to source control, or else you will have compromised any credentials saved to that file.

Typically, to load and access the environment variables saved to your ``.env`` you would need to use a tool such as `python-dotenv <https://saurabh-kumar.com/python-dotenv/>`_.

But alas, because we are using ``pipenv`` to manage our ``cc-pydata`` project environment, ``pipenv`` **will automatically load your** ``.env`` **environment variables to your environment when you enter your** ``pipenv shell`` **or use** ``pipenv run``.

For instance, if you have a secret key you wish to access programatically when running your ``cc-pydata`` package locally, you can add the following to your ``.env`` file::

    SECRET_KEY=YOURSECRETKEY

Then, to access that secret key from your code, you simply need to access it using the ``os.getenv`` method like this::

    import os

    SECRET_KEY = os.getenv("SECRET_KEY")

``pipenv`` will seamlessly take care of loading those ``.env``-stored enviroment variables in the background.

To learn more about this ``pipenv`` behavior, please see the documentation on `Pipenv loading of .env`_.


Accessing modules in your package from a Jupyter Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you would like to incorporate Jupyter notebooks into your ``cc-pydata`` project, you will first need to install the ``jupyter`` package in your ``pipenv`` environment::

    pipenv install --dev jupyter

Then, once ``jupyter`` is installed, you can start your notebook server by running::

    pipenv shell
    jupyter notebook

It is recommended that you create and store all Jupyter notebooks in the provided ``notebooks`` directory for consistency.

The ``cc-pydata`` package module is configured in such a way that, if you wish to import that package for your current notebook session, you simply use the following syntaxt for import::

    # example of importing the local `visualizations` module
    from <package-name> import visualizations

    # or, importing only one function from that module
    from <package-name>.visualizations import <function-name>


Therefore, there is no need to import `src`. Instead, you can use the more natural convention of importing your package based on its actual name.


Versioning your project
^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pydata`` template is configured to make use of `setuptools_scm`_ to manage and track your ``cc-pydata`` project's current version.

There are a number of different ways to maintain a Python project's current version. For a survey of different approaches to maintain a "single source of truth" for the version number of your project (i.e. where you only need to update the version in one single location), please see this article on `Single-sourcing the package version`_. ``cc-pydata`` makes use of option #7 in that article.

By using ``setuptools_scm``, your ``cc-pydata`` application pulls the version number directly from the latest ``git`` tag associated with your project. Therefore, instead of manually setting a global ``__version__`` variable in your application, you simply add a tag when you commit a new version of your application to ``master``.

Implications for choosing an effective `git` branching methodology
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To use ``setuptools_scm`` effectively, you'll likely want to use a proper/consistent ``git`` branching methodology while building and maintaining your project.

* At a minimum, you should perform all of your development work on separate non-``master`` ``git`` branches, and only when features are complete, "release" them by merging them into your ``master`` branch.

* Therefore, each time you merge a set of your changes into ``master``, that event should be considered a release.

* Thus, a release merged into ``master`` would require you tag it with a new version number.

For instance, say you have a set of tested features on a ``develop`` branch that are ready for release...

You would first merge it into ``master`` (and consider using the ``--no-ff`` argument to prevent fast-forward merges, `thus maintaining the context of your branches and the branching topology <https://stackoverflow.com/questions/9069061/what-is-the-difference-between-git-merge-and-git-merge-no-ff>`_ of your ``git`` history):

.. code-block:: Bash

    # Assuming your 'develop' branch is your current active branch
    git checkout master

    git merge --no-ff develop

    git tag -a v0.3.0 -m "Add a set of features that ..."

As you can see in the steps above, once the set of new features are merged into your ``master`` branch, you would then immediately add an "annotated" (designated by the ``-a`` argument) version tag, and comment it with a brief message describing the release.

Now, if you were to check the version of your project::

    python setup.py --version

...``setuptools_scm`` would provide you the following result:

.. code-block:: Bash

    v0.3.0

Then, once you have completed and tagged your merge into ``master``, you would push your latest release changes (including the new tag) to your desired ``remote`` and switch back your "development" branch so you don't accidentally make any additional changes to ``master``:

.. code-block:: Bash

    git push origin master
    git push origin v0.3.0
    git checkout develop
    git merge --no-ff master

Now, because you are past your prior release, if you were to re-run ``python setup.py --version``, you'd receive a result similar to this:

.. code-block:: Bash

    0.3.0.dev5+gefeb5a6.d20200620

Voilà! You have released a new version of your project!

To systematize your branching methodology in a manner similar to this, please take some time to:

* `Consider using the Git-flow methodology <https://nvie.com/posts/a-successful-git-branching-model/>`_
* Or, at a minimum, `the simpler GitHub flow methodology <https://guides.github.com/introduction/flow/>`_.

While you're at it, why not do yourself a favor and also add some some useful and consistent context to each of your commits by using the:

* `Conventional Commits specification for adding human and machine readable meaning to your commit messages <https://www.conventionalcommits.org/>`_.


Implications for using Semantic Versioning as a consistent version-numbering scheme
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

According to the ``setuptools_scm`` documentation, `it is required to always include a "patch version" in your tagged version numbers <https://github.com/pypa/setuptools_scm/#default-versioning-scheme>`_. That means:

* If you are releasing ``v0.3.0`` as was demonstrated in the previous section,
* Then be certain to include the final "``0``", which indicates the "patch version" of that release.

In fact, while you're at it, why not just consistently use Semantic Versioning (i.e. `SemVer`_) for every release you tag in ``git``.

* `SemVer`_ is clean, easy to use, and it conveys important meaning about the underlying code in your package and what has been modified from one version to the next.
* An added benefit, ``setuptools_scm`` is expected to switch to SemVer as its default behavior in the future.

At its core, SemVer uses the ``MAJOR.MINOR.PATCH`` increment scheme for version numbering. As is specified in the `SemVer`_ documentation:

1. You change the ``MAJOR`` version when you make incompatible API changes,
2. You change the ``MINOR`` version when you add functionality in a backwards compatible manner, and
3. You change the ``PATCH`` version when you make backwards compatible bug fixes.

Therefore, each version you release to ``master`` should always be tagged with three distinct period-separated digits, such as in the example:

.. code-block:: Bash

    git tag -a v0.3.0 -m "Add a set of features that ..."



Documenting your project using Sphinx and GitHub Pages
------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Getting started with Sphinx and reStructuredText
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The resulting project template is configured to use reStructuredText_ and Sphinx_ to generate and maintain your project documentation. By defult, ``sphinx`` has been added as a ``dev-packages`` requirement to `the template's base Pipfile <https://github.com/sedelmeyer/cc-pydata/blob/master/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Pipfile>`_. Therefore, when you run ``pipenv install --dev`` for the first time for your new project (see :ref:`install-pipenv`), ``sphinx`` will be installed to your ``pipenv`` virtual environment by default.

* **If you are new to Sphinx**, please see `the Sphinx documentation <https://www.sphinx-doc.org>`_
* **If you are new to reStructuredText**, a good starting place will be `the reStructuredText documentation provided by the Sphinx project <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_

.. _make-html:

Generating and previewing your site HTML
""""""""""""""""""""""""""""""""""""""""

Sphinx provides a convenient ``Makefile`` for performing basic site-building tasks. Generating (and re-generating) your Sphinx site's HTML is as easy as following the next two steps:

#. Navigate to your project's ``docs/`` directory::

    cd docs/

#. Run the ``make`` command for building your HTML::

    make html

If your reStructuredText contains any errors, Sphinx will tell you as it builds your HTML.

Your generated HTML, CSS, and related site files will now be located in the project's ``docs/_build/html/`` directory.

At any time you can preview your generated site content by opening your site's ``index.html`` file and navigating throughout your generated site files.

* If you are using Ubuntu, you can open your site content with your default web-browser by using this command::

    xdg-open docs/_built/html/index.html

* If you are using a different operating system, use the appropriate command or simply open the ``index.html`` with your system's GUI.

**It is recommended that you DO NOT** ``git commit`` **those generated site files to your** ``master`` **branch.** It is poor practice (and an inefficient use of git history storage) to commit your site source files and generate site HTML content to the same git branch. Instead, please refer to the section :ref:`gh-pages`. That section outlines a recommended workflow for managing and commiting your generated site content using `GitHub Pages`_.

.. _make-docs:

Auto-generating documentation for your custom package modules
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Sphinx is a powerful tool for auto-generating API documentation directly from the docstrings embedded within your code. In other words, if you take the time to document your code correctly using docstrings, your API reference material can largely write itself.

There are several approaches you can take to accomplish this. Options include:

1. Manual configuration of API reference materials using the ``sphinx.ext.autodoc`` `autodoc Sphinx extension <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_;

2. Manual configuration of API reference materials using the ``sphinx.ext.autosummary`` `autsummary Sphinx extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`_;

3. Fully automated generation of API reference materials using the ``sphinx-apidoc`` `command line utility, which relies on the autodoc extension <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`_;

4. Automatic generation of API reference materials by setting the ``autosummary`` extension's ``autosummary_generate = True`` `parameter in your Sphinx <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#confval-autosummary_generate>`_ ``conf.py`` file;

5. ...a combination of any of the approaches listed above.

Each approach listed above has its own pros and cons which are far too detailed to explore here. For a great comparison of using the ``automodule`` versus the ``autosummary`` extension, `please see this article by Roman Miroshnychenko <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-ii-6/>`_. Otherwise, please refer to the ``autodoc``, ``sphinx-apidoc``, ``autosummary``, and ``autosummary_generate`` links provided in the list above.

I am sure approaches other than those listed above exist as well, but you should be able to accomplish everything you need to accomplish using these tools, so I will save myself the time it would take to provide a more exhaustive list.

**If you have questions about the proper syntax for writing  Sphinx-friendly reStructuredText docstrings in your Python code**, please see:

* `Roman Miroshnychenko's article on autodocumenting your python code <https://romanvm.pythonanywhere.com/post/autodocumenting-your-python-code-sphinx-part-i-5/>`_

* `Thomas Cokelaer's example on how to document your Python docstrings <https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html>`_

You may also find Sphinx's `documentation on its Python Domain directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#the-python-domain>`_ to be extremely useful while trying to embed references within your docstrings.

Sphinx can also generate documentation from the Google- and Numpy-formatted docstring styles with the help of the ``sphinx.ext.napoleon`` Sphinx extension. If either of those docstring formats are your jam, please `see the napoleon documentation <https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html>`_.

.. note::

   * The first time you run ``make html`` as was described in :ref:`make-html`, the ``docs/modules.rst`` file contained in the default ``cc-pydata`` template will generate a starter "API Reference" page documenting all modules and functions already contained in the ``cc-pydata`` template. That initial ``modules.rst`` file makes use of the manual approach #1 listed above and uses the ``sphinx.ext.autodoc`` extension's ``automodule`` `directive <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-automodule>`_ to generate that starter documentation.

   * All Sphinx extensions listed above, including ``sphinx.ext.autodoc``, ``sphinx.ext.autosummary``, and ``sphinx.ext.napoleon`` are imported by default in the ``cc-pydata`` template's ``conf.py`` Sphinx configuration file.


Rationale for using reStructuredText instead of Markdown
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

GitHub, Jupyter notebooks, and other static site generators typically rely on Markdown as a lightweight markup language.

QUESTION:

* So then, why does the ``cc-pydata`` project template use reStructuredText instead of Markdown?
* Afterall, reStructuredText is a bit more verbose and not quite as frictionless for an author to use compared to Markdown.

ANSWER:

* Because benefits abound, particularly for technical writing (once you get past the initial learning curve).
* And, because the primary assumption is that you'll be writing technical content to document and support your Python-based ``cc-pydata`` project, reStructuredText is the better choice.

Here are a few primary reasons worth highlighting:

* reStructuredText supports semantic meaning in a manner not supported by Markdown,
* reStructuredText is extensible and standardized while any Markdown implementation that is feature-rich enough to even begin supporting moderate-to-heavy technical writing needs will come in many flavors which are not always portable between different platforms without tedious modification,
* reStructuredText is a stable "go-to", has been around for a while, and has been used heavily in the Python community since 2002,
* reStructuredText is the default markup language for Sphinx (see more about why we are using Sphinx in the section below) and integrates well with `Sphinx's more powerful directives <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`_

Rationale for using Sphinx instead of Jekyll, Pelican, or some other static site generator
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

GitHub Pages strongly favors GitHub's homegrown static site generator `Jekyll <https://jekyllrb.com/>`_ and it's hella simple to use for some basic web publishing needs.

* Unfortunately, Jekyll is a Ruby-based tool.
* That means, if you use Jekyll, you'll need to run both a Ruby environment and Python environment to publish your ``cc-pydata`` documentation.

Meanwhile, Sphinx is through-and-through a Python-based tool (in fact the documentation for the Python language itself is published using Sphinx)!

* The second major drawback for Jekyll is, it's not a tool custom-suited for documenting code.
* This drawback also applies to the Python-based `Pelican <https://docs.getpelican.com/>`_ site generator and many other static site generators.
* They typically provide no means for auto-generating project documentation directly from the custom code contained in your packaged Python library.
* Sphinx, on the otherhand, excels at this task!

As was illustrated above (see :ref:`make-docs`), Sphinx offers powerful built-in extensions such as `sphinx.ext.autodoc <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`_ for generating and organizing your project documentation, pulling documentation directly from the docstrings in your code.

Information about other popular "built-in" Sphinx extensions that help to make Sphinx a smart choice for technical documentation `can be found in the "Extensions" section of the Sphinx documentation <https://www.sphinx-doc.org/en/master/usage/extensions/index.html>`_.

Adding a logo to your Sphinx site
"""""""""""""""""""""""""""""""""

The default theme used for the Sphinx docs in the ``cc-pydata`` template is called `Alabaster <https://alabaster.readthedocs.io/en/latest/>`_. It's clean, responsive, and configurable. Did I mention it was clean?

The Alabaster theme provides a simple option for adding a site logo to the top of the lefthand navbar. A reasonable width for that logo image is 200 pixels. To add a logo to your ``cc-pydata`` project documentation, simply:

#. Save your 200-pixel-width image file (e.g. as .jpg or .png file) to the ``docs/`` directory, and name it ``docs/logo.png`` (with the appropriate file extension of course).
#. Go to the ``docs/conf.py`` file and uncomment the ``logo`` setting in the ``html_theme_options`` dictionary.
#. Then ``make html`` and your new logo image should appear in the generated site HTML.

Adding a favicon to your Sphinx site
""""""""""""""""""""""""""""""""""""

Similar to the site logo, if you wish to add a favicon image to your Alabaster-themed Sphinx site:

#. Generate your ``favicon.ico`` image at 16x16 pixels, or 32x32, or whatever size makes the most sense given current browser standards and backwards compatibility concerns (truthfully, I couldn't care less and would just choose a size that works for your browser of choice).
#. Save it as ``docs/favicon.ico``.
#. Go to the ``docs/conf.py`` file and uncomment the ``html_favicon = '_static/favicon.ico'`` line and ``make html`` again.

.. _gh-pages:

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

Test configuration and continuous integration with Travis-CI
------------------------------------------------------------

.. contents:: In this section
  :local:
  :backlinks: none

Unit-testing your project and using the ``pytest`` test-runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Location of ``cc-pydata`` unit tests
""""""""""""""""""""""""""""""""""""

The ``cc-pydata`` template, by default, provides a ``tests/`` directory at the same level as the ``src/`` directory.

* Opinions and rationale about where to store Python unit tests vary.
* Some people prefer storing unit tests directly within their modules, some under ``src/``, but outside their actual modules, and others in the manner we have done here for ``cc-pydata``.
* Sometimes circumstances and/or preferences warrant using one location over another.
* To keep things simple, and to make it easy to locate tests in your project, the current ``tests/`` location has been chosen for the ``cc-pydata`` template.
* However, you should feel free to relocate your unit tests to a different location if it makes sense for you or your project.

``pytest`` test-runner
""""""""""""""""""""""

* ``pytest`` and ``pytest-cov`` are installed as default ``dev-packages`` in the base ``Pipfile`` included with the ``cc-pydata`` project template.
* `Pytest`_ makes for a simple yet powerful test-runner for test discovery, reporting, and simple diagnostics; and `pytest-cov <https://pytest-cov.readthedocs.io/en/latest/readme.html>`_ produces coverage reports.

Running unit tests using ``pytest``
"""""""""""""""""""""""""""""""""""

At any time during development of your ``cc-pydata`` project, you can run your entire suite of unit tests. The two easiest methods for doing this are:

#. If you aren't currently in your project's ``pipenv`` environment, run::

    pipenv run pytest

#. If you are currently in your ``pipenv shell``, run::

    python -m pytest

    # or even more simply just the single word command...

    pytest

The ``pytest`` test-runner is a powerful command-line tool. There are far too many features to describe here. For a good overview:

* Please see `the documentation regarding the Usage and Invocations <https://docs.pytest.org/en/latest/usage.html>`_ of ``python -m pytest``;
* Additionally, you can see the complete listing of available ``pytest`` arguments in the "help" documentation by running ``pytest -h``.

Running ``pytest`` will provide a convenient summary as tests are run. As an example, your default ``cc-pydata`` test output will look something like this if there are no test failures:

.. code-block:: bash

    ============================== test session starts ===============================
    platform linux -- Python 3.7.5, pytest-5.4.3, py-1.8.1, pluggy-0.13.1
    rootdir: /home/Code/project_name, inifile: setup.cfg, testpaths: tests, project_name
    plugins: cov-2.10.0
    collected 11 items

    tests/test_project_name.py ...                                             [ 27%]
    tests/data/test_data.py .                                                  [ 36%]
    tests/features/test_features.py .                                          [ 45%]
    tests/logger/test_logger.py ....                                           [ 81%]
    tests/models/test_models.py .                                              [ 90%]
    tests/visualizations/test_visualizations.py .                              [100%]

    ----------- coverage: platform linux, python 3.7.5-final-0 -----------
    Name                                          Stmts   Miss Branch BrPart  Cover
    -------------------------------------------------------------------------------
    src/project_name/__init__.py                      7      2      0      0    71%
    src/project_name/__main__.py                      3      1      2      1    60%
    src/project_name/cli.py                           6      0      0      0   100%
    src/project_name/data/__init__.py                 2      0      0      0   100%
    src/project_name/features/__init__.py             2      0      0      0   100%
    src/project_name/logger/__init__.py              41      2     14      5    87%
    src/project_name/models/__init__.py               2      0      0      0   100%
    src/project_name/visualizations/__init__.py       2      0      0      0   100%
    -------------------------------------------------------------------------------
    TOTAL                                            65      5     16      6    86%


    =============================== 11 passed in 0.16s ===============================


Configuring and leveraging Travis-CI for your project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pydata`` project template is configured to use `Travis-CI`_ services for continuous integration testing.

* The ``.travis.yml`` file provided in the ``cc-pydata`` project template is used to configure your `Travis-CI`_ build.
* For a tutorial on how to use Travis-CI, please `see the official Travis-CI tutorial <https://docs.travis-ci.com/user/tutorial/>`_, and if you're new to continuous integration, please `see their article on core concepts for beginners <https://docs.travis-ci.com/user/for-beginners>`_.

The default ``.travis.yml`` configuration file
""""""""""""""""""""""""""""""""""""""""""""""

Below is a snippet showing what is contained in the ``cc-pydata`` default ``.travis.yml`` file (with comments added to describe what each item means).

.. code-block:: yaml

    # This first section tells travis-ci.com what coding language and
    # which distribution and versions to use for your build.
    language: python
    dist: xenial
    python:
    - 3.7

    # This section tells travis-ci what commands to runner.
    # Note that the first thing it will do is install our pipenv
    # environment.
    install:
    - pip install pipenv
    - pipenv install --system --deploy --ignore-pipfile

    # This tells travis-ci to only run builds when you push your master
    # or develop branches. Therefore, travis builds will ot run for any
    # other branches.
    branches:
    only:
    - master
    - develop

    # This defines the build "stages" you wish to run. Note here that
    # the "answers" stage will only be executed when your master branch
    # is pushed. The "test" stage on the otherhand, it will run for
    # both the master and develop branches as specified in the previous
    # section.
    stages:
    - test
    - name: answers
        if: branch = master

    # This section specifies what travis-ci should do for each stage
    # you have defined above. For the "test" stage you pipenv
    # environment will be installed and your tests will execute using
    # the pytest test runner set to verbose mode. For the "answers"
    # stage, the code in your cc-pydata package's main module will be
    # run.
    jobs:
    include:
        - stage: test
        script: pytest -v
        install:
            - pip install pipenv
            - pipenv install --system --deploy --dev --ignore-pipfile

        - stage: answers
        script:
        - python3 -m {{ cookiecutter.package_name }}


Setting up travis-ci.com to run CI builds for your project
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

In order for Travis-CI to run builds for your project when you push to your GitHub hosted ``master`` or ``develop`` remote branches, you will need to authorize Travis-CI for your GitHub account as well as the specific ``cc-pydata`` project repository on GitHub.

For instructions on how to accomplish this, please `see the Travis-CI instructions on how to get started with GitHub <https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci-using-github>`_.


Logging configuration and out-of-the-box ``cc-pydata`` logging features
-----------------------------------------------------------------------

The ``cc-pydata`` template provides some useful default, yet easily modified, logging capabilities out-of-the-box for your data science project.

The defaults provided (and described below), rely only on the ``logging`` `module included in Python's standard library <https://docs.python.org/3/library/logging.html>`_.

.. contents:: In this section
  :local:
  :backlinks: none


Default ``logging`` configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The default logging configuration of the ``cc-pydata`` application provides the flexibility to program logging events into your application, then to easily choose whether or not to enable logging of those events for any given session in which you import and run your application.

For intance:

* If you don't explicitly initialize an active handler during your session, a package-level do-nothing ``NullHandler`` will silence all logging events generated by your application.
* On the otherhand, if you do want events actively logged during your session, you easily use the custom ``logger.start_logging()`` function call provided in the base ``cc-pydata`` template.

More on both of these options are outlined below...

The package-level ``NullHandler`` initialized at import
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

As a default, a do-nothing handler (a.k.a. ``logging.NullHandler()``) is set at the time of import for your ``cc-pydata`` application. This behavior helps to ensure logs are not printed unless you explicity choose to activate logging while running your ``cc-pydata`` application.

To accomplish this, the top-level ``__init__.py`` file contains the following code::

    import logging


    logging.getLogger('<package-name>').addHandler(logging.NullHandler())

This ensures a handler is always found for your application's logging events, preventing unwanted logging to occur unless you explicity set a different handler. For more information on this, please see the ``logging`` `documentation's notes on best practices for configuring logging for a library <https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library>`_.


Initializing active logging with the ``<package-name>.logger.start_logging()`` function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To active logging for any given session during which you import and run your ``cc-pydata`` application, all you need to do is run the provided ``<package-name>.logger.start_logging()`` custom function.

As a default, ``start_logging`` will import the ``logging`` dictionary configuration specified in the provided ``logging.json`` file contained in the default ``cc-pydata`` project template.

If that ``logging.json`` file is not available, or if you call the ``start_logging`` function with its default arguments from an interactive Jupyter notebook session for a notebook located in the ``notebooks`` directory, a ``logging.basicConfig()`` `configuration <https://docs.python.org/3/library/logging.html#logging.basicConfig>`_ will be initialized at the ``INFO`` logging level, and log events will be output to ``sys.stdout``.

Diagram illustrating the Default ``cc-pydata`` project logging behavior
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Below is a flow diagram illustrating the default project logging behavior described above:

.. graphviz::

   digraph pydata_logging {
    rankdir=TB;
    {
    	node [shape = box, fontname = Monospace]
        1 [label = "import <package-name>"]
        2 [label = "<package-name>.logger.start_logging()"]
    };
    {
        node [shape = box, color = lightblue, style = filled, fontname = Monospace]
        a [label = "logging.NullHandler()"]
        b [label = "logging.config.dictConfig(\l    os.environ['LOG_CFG']\l)"]
        c [label = "logging.config.dictConfig(logging.json)"]
        d [label = "logging.basicConfig(\l    stream=sys.stdout,\l    level=logging.INFO\l)"]
    };
    {
        node [shape = diamond]
        i [label = "Does the\nLOG_CFG environment\nvariable exist?"]
        ii [label = "Does the\nlogging.json file\nexist in the\nactive directory?"]
    };
	1 -> a;
	a -> 2;
	2 -> i;
	i -> b [ label = "Yes" ];
	i -> ii [ label = "No" ];
	ii -> c [ label = "Yes" ];
	ii -> d [ label = "No" ];
   }

Customizing the provided ``logging.json`` configuration file
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

When calling ``<package-name>.logger.start_logging()`` from your ``cc-pydata`` project's root directory, you are effectively initializing your ``logging`` session with ``logging.config.dictConfig(logging.json)``.

The default ``logging.json`` configuration file provided with the ``cc-pydata`` template simply provides a single ``root`` handler that logs to ``sys.stdout`` at the ``INFO`` logging level.

To add additional handlers, change logging levels, change formatters, or add filters to this ``logging.json`` file, please see:

* Official ``logging.config.dictConfig`` `documentation <https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig>`_;

* Configuration `dictionary schema documentation <https://docs.python.org/3/library/logging.config.html#logging-config-dictschema>`_.


Functions provided in the custom ``<package-name>.logger`` module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``cc-pydata`` project template provides a built in custom logging module located at the ``<package-name>.logger`` namespace.

This ``logger`` module has been kept simple with the thought that users can build additional logging functionality to suite the needs of their own data science project.

The ``logger`` module comes with two provided functions:

.. list-table::

   * - ``<package-name>.logger.start_logging(...)``
     - Set up logging configuration for the ``cc-pydata`` project package
   * - ``<package-name>.logger.logfunc(...)``
     - Decorator wrap function call to provide log information when a function is called

Both ``logger`` functions are described in greater detail below.


The ``<package-name>.logger.start_logging()`` function
""""""""""""""""""""""""""""""""""""""""""""""""""""""

This function activates a ``logging`` configuration for the ``cc-pydata`` project package during your current session.

:param default_path: string file path for json formatted
                        logging configuration file (default is
                        ``'logging.json'``)
:param default_level: string indicating the default level
                        for logging, accepts the following
                        values: ``'DEBUG'``, ``'INFO'``, ``'WARNING'``,
                        ``'ERROR'``, ``'CRITICAL'`` (default is ``'INFO'``)
:param env_key: string indicating environment key if one exists
                (default is ``'LOG_CFG'``)

Example::

    from <package-name>.logger import start_logging


    start_logging()


    ...


The ``<package-name>.logger.logfunc()`` decorator function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This function acts as a ``functools.wraps`` `decorator for decorating functions or methods <https://docs.python.org/3/library/functools.html#functools.wraps>`_ to provide logging functionality to log details of the decorated function

:param orig_func: ``NoneType`` placeholder parameter
:param log: ``logging.getLogger`` object for logging, default is ``None``
:param funcname: boolean indicating whether to log name of function,
                    default is ``False``
:param argvals: boolean indicating whether to log function arguments,
                default is ``False``
:param docdescr: boolean indicating whether to log function docstring
                    short description, default is ``False``
:param runtime: boolean indicating whether to log function execution
                runtime in seconds, default is ``False``
:return: ``functools.wraps`` wrapper function

Please note that all logs are generate at the ``INFO`` logging level

Example::

    import logging
    from <package-name>.logger import logfunc


    log = logging.getLogger(__name__)


    @logfunc(log=log, funcname=True, runtime=True)
    def some_function(arg1, **kwargs):
        ...


For additional information on best practices and logging in Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are new to logging, or are considering logging for the first time in the context of a Python data science project, here are some additional resources I have found to be helpful:

* The Python standard library provides `an extensive tutorial and HOWTO for getting started with logging <https://docs.python.org/3/howto/logging.html>`_.

* The Python standard library provides `a more advanced "logging cookbook" with many great recipes <https://docs.python.org/3/howto/logging-cookbook.html>`_.

* Kenneth Reitz and Real Python provide `a clear and concise section on logging in The Hitchhiker's Guide to Python <https://docs.python-guide.org/writing/logging/>`_.

* Fang-Pen Lin provides `an overview of good logging practices (along with a sample dictionary configuration) on her blog <https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/>`_.

* Real Python provides `a clear introductory tutorial on logging in Python <https://realpython.com/python-logging/>`_.

* And, Ari Cohen provides `an interesting approach to logging decorators (which inspired my custom logfunc function) for data science projects <https://towardsdatascience.com/unit-testing-and-logging-for-data-science-d7fb8fd5d217>`_.

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

.. _Pipenv loading of .env: https://pipenv.kennethreitz.org/en/latest/advanced/#automatic-loading-of-env
.. _Single-sourcing the package version: https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
.. _reStructuredText primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

.. _GitHub Pages: https://pages.github.com/
.. _SemVer: https://semver.org/
