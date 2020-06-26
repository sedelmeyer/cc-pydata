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

   * This ``tox`` configuration also runs a documentation test build to ensures that the ``cc-pydata`` Sphinx-based documentation renders successfully and it runs a linter to ensure that the project code meets `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ linting standards.

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

.. todo::

   * Describe ``tests`` module configuration and structure
   * Describe ``pytest`` test-runner usage
   * Describe significance of ``tests.toxtest`` module and special usage


API documentation for the ``tests`` module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::

   * Add introduction to API section

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
