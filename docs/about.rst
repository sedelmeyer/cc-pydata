.. _about:

About this project
==================

This page contains useful information to help you learn a bit more about the ``cc-pydata`` project and how it is configured.

* If your goal is to learn more about the Cookiecutter tool used as the basis for the ``cc-pydata`` project, your best source of information will be the official Cookiecutter_ documentation.

* If you just want to know what the ``cc-pydata`` project is, please see the :ref:`README<README>` documentation for the project.

* If you want to (a) learn more about the how to generate or use the resulting ``cc-pydata`` template or (b) better understand the features and functionality embedded in the resulting ``cc-pydata`` template, please see the :ref:`Tutorial` for this project.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

.. contents:: On this page
  :local:
  :depth: 1
  :backlinks: top

.. _development:

Development philosophy
----------------------

As is discussed in the :ref:`design` section of the ``cc-pydata`` documentation, I have sought to balance Python best practices and standards with my own needs across a wide range of projects. What's more, I've also sought to embed structural characteristics of other great Cookiecutter templates (see :ref:`sources`).

Starting from those initial principals, I hope to have built a Cookiecutter template that is flexible and robust enough for others to find useful for their own Python data science projects.

I have taken the time to :ref:`carefully test<project-testing>` and document the ``cc-pydata`` project, both for my own sake, as well as for the sake of others who might find this project and wish to use it themselves.

I hope that the :ref:`Tutorial` for this project not only enlightens the user, but provides (a) the blueprint needed for those who may not be familiar with all of the tools and methods employed in the template, and (b) enough of a foundation for those who wish `to fork <https://en.wikipedia.org/wiki/Fork_(software_development)>`_ and modify the project to better suit their own needs.

License
-------

The ``cc-pydata`` Cookiecutter template is offered for use under the MIT open source license.

The content of this license is shown below and can also be found in `the LICENSE file contained in the project repository on GitHub <https://github.com/sedelmeyer/cc-pydata/blob/master/LICENSE>`_:

    .. include:: ../LICENSE


Contributing
------------

As is mentioned above in the :ref:`development` section of this page, I have sought to balance best practices and features with my own particular needs. Therefore, I am not actively seeking contributions to the ``cc-pydata`` project from others. My primary reason being that, as soon as others begin adding features to this project, the more likely it will be that the template no longer fits my specific needs.

If however, you do see opportunities to improve this project and its resulting template, I am still interested in hearing from you.

If you'd like to suggest changes or to get in touch regarding the ``cc-pydata`` project, `please feel free to open an issue and we can discuss <https://github.com/sedelmeyer/cc-pydata/issues>`_.

I am not quite sure how firm I am on my position of "no contributions." Therefore, if you have great ideas on how to improve this project, there's a very good chance that I can be convinced!

.. _project-testing:

Project testing and test API
----------------------------

.. todo::

   Add content for...

   * test modules
   * tox automation
   * travis continuous integration

It has been my experience that testing a Cookiecutter template presents its own set of unique challenges.

Not only do you need to:

1. Test that the template renders, but you also need to
2. Test that the template renders appropriately according to whatever sorts of build options you provide when invoking the template, and you also need to
3. Test that the default functionality baked into template after it's been rendered functions appropriately as well (i.e. you need to perform tests within tests).

Thus far, I have been unable to find any clear documentation online on how to do this correctly.

Therefore, I am providing more detail than might otherwise be warranted on how I have configured my ``cc-pydata`` project tests to deal with (what I can only imagine are) common challenges encountered by anyone who has ever sought to thoroughly test their own custom Cookiecutter template.

.. contents:: In this section
  :local:
  :depth: 1
  :backlinks: top

Testing tools employed for this project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * Add links to appropriate sections ``tox``, ``tests``, ``travis``

I have sought to develop a thorough set of tests to ensure that the ``cc-pydata`` project and resulting template function as expected. Programatic tests for this project can be found in the ``tests`` directory, where I seek to test each unique feature of this template.

Tests for this project occur in several ways.

1. There are the programmatic tests using Python's standard ``unittest`` library to author test cases for each template feature I wish to test.

   * My governing principal here, is that I should not add any additional functionality into the template, or the means by which the overarching ``cc-pydata`` project renders the template, without also developing a test (or set of tests) to test that functionality.

   * There are additionally unit tests built into the rendered template produced by this project. Those in-template tests ensure that the baseline package provided in that rendered template functions correctly (presenting an opportunity for tests within tests).

2. There are a set of automated tests configured using ``tox`` to ensure that the ``cc-pydata`` project functions correctly on several different versions of Python (those versions are ``python 3.6``, ``python 3.7``, and ``python 3.8`` as of ``cc-pydata`` v0.3.0 at the time of my writing this).

   * This ``tox`` configuration also runs a documentation test build to ensure that the ``cc-pydata`` Sphinx-based documentation renders successfully and it runs a linter to ensure that the project code meets `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ standards.

   * Also, dependent on whether the ``tox`` option is enabled for the rendered ``cc-pydata`` template, the rendered template itself will also contain a ``tox``-automated test configuration as well to perform similar tasks for the resulting rendered template (and yet another layer of tests within tests).

3. Lastly, continuous integration is implemented using `Travis-CI <https://travis-ci.com/>`_ (and soon to also be implemented using `Azure Pipelines <https://azure.microsoft.com/en-us/services/devops/pipelines/>`_) to run and test automated builds each time committed revisions to the ``cc-pydata`` project are pushed to the GitHub-hosted remote ``develop`` or ``master`` branches for the project.

``tox`` test matrix and automation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * Describe ``tox`` and significance/benefits of the tool as a ``cc-pydata`` option
   * Add details about ``tox`` configuration with ``tox.ini``
   * Describe basic ``tox`` command line usage and syntax
   * Describe ``tox`` within ``tox`` usage

Continuous integration test builds with Travis-CI and Azure Pipelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * Describe ``.travis.yml`` configuration with ``tox``
   * Describe importance of Travis-CI and Azure, particularly for interpreters and operating systems not available on your local machine

Custom ``tests`` module using ``unittest`` and the ``pytest`` test-runner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run tests for the ``cc-pydata`` project, enter your development environment by running ``pipenv shell`` and run the the following command from your top-level of your project directory::

   pytest


You should see output similar to this:

.. code-block:: Bash

    ============================ test session starts =============================
    platform linux -- Python 3.7.5, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
    rootdir: /home/Code/cookiecutter-pydata, inifile: setup.cfg, testpaths: tests
    plugins: cov-2.10.0
    collected 28 items

    tests/test_defaults.py ..........                                       [ 35%]
    tests/test_options.py .........                                         [ 67%]
    tests/test_testutils.py .........                                       [100%]

    ============================= 28 passed in 5.55s =============================


Testing Cookiecutter template builds
""""""""""""""""""""""""""""""""""""

It's probably worth acknowledging that:

1. There exists a ``pytest`` plugin for testing Cookiecutter templates. That plug-in is named ``pytest-cookies``, and it provides a boilerplate-free experience for building and testing Cookiecutter templates

2. But, I do not use that plug-in in any way for testing this project

If you'd like to learn more about the ``pytest-cookies`` plug-in for your own use, `please see that project's documentation <https://pytest-cookies.readthedocs.io/en/latest/>`_.

While I use ``pytest`` as the test-runner for this project, I do not use the ``pytest`` framework for writing my tests. I have attempted to keep my tests written entirely using ``unittest`` from the Python standard library. This approach requires a bit more boilerplate in my test code, but it also helps to ensure that I am not locked into ``pytest`` as a testing requirement. Besides, I have also found a simple-enough approach to building and testing my Cookiecutter template using just ``unittest`` test cases. As a result, I haven't felt a need to use ``pytest`` or the ``pytest-cookies`` plug-in.

If you examine the ``TestCase`` classes in the ``tests.test_default`` and ``tests.test_options`` test modules, you will see that each ``TestCase`` contains a ``setUp()`` method that:

a. Uses the ``contextlib.ExitStack`` `context manager <https://docs.python.org/3/library/contextlib.html#contextlib.ExitStack>`_ to build a ``tempfile.TemporaryDirectory`` `temporary directory <https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory>`_ in which I can build each of my ``cc-pydata`` rendered templates for testing;

b. Uses the ``addCleanUp`` method to ensure the temporary directory gets cleaned up after each test, regardless if the test setup fails in any way.

Each test case additionally uses ``cookiecutter.main.cookiecutter``, `the main entry point to the cookiecutter command <https://cookiecutter.readthedocs.io/en/1.7.2/cookiecutter.html#module-cookiecutter.main>`_, which allows you to easily initiate a template build directly from your Python code.

By putting these pieces together, ``cc-pydata`` template test builds become predictable and easy to manage.

The structure of the ``tests`` module
"""""""""""""""""""""""""""""""""""""

As you will see in the ``tests`` module API documentation below, ``cc-pydata`` tests are split among several submodules.

1. :mod:`tests`: At the highest level are a set of utility functions that make testing easier and reduce boilerplate code in each test case. These utility functions themselves are tested in :mod:`tests.test_testutils`.
2. :mod:`tests.test_defaults`: Next are a set of tests focused on the default ``cc-pydata`` template build.
3. :mod:`tests.test_options`: This sub-module focuses on testing versions of the cc-pydata`` template produced when using the optional arguments available in the template.
4. :mod:`tests.toxtest`: Finally, there is a sub-module that only runs when explicitly called using the command ``pytest -s tests/test_toxtest.py``. This is a costly test to run because it not only renders the ``cc-pydata`` template, but it also invokes that template's own ``tox.ini`` to run all of its own ``tox`` environments. Think of it as tests-within-tests-within-tests, all running in their own embedded temporary environments. This sub-module can take a couple minutes to run, so considered yourself warned. See :mod:`tests.toxtest` for more detail.


API documentation for the ``tests`` module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. contents:: Module contents
  :local:
  :depth: 2
  :backlinks: top

.. automodule:: tests
   :members:

.. automodule:: tests.test_testutils
   :members:

.. automodule:: tests.test_defaults
   :members:

.. automodule:: tests.test_options
   :members:

.. automodule:: tests.toxtest
   :members:
