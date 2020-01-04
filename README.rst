===================
cookiecutter-pydata
===================

Cookiecutter_ template for generating a "reasonably standardized" skeleton for a Python-based data science project.

Summary
-------

This Cookiecutter_ template allows for the creation of a "reasonably standardized", but flexible project structure [#]_ when starting a new Python-based data science project. The benefits of using such a structure and implementing it with Cookiecutter is that it:

* Takes the guesswork and low-value manual labor out of standing up a new data science project
* Allows you to get started right away on your data science work when stating a new project
* Creates a sense of consistency across your projects, making it easier for yourself and others to interpret and replicate your analyses and findings.

.. contents:: Table of Contents

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

* Tox_ for managing test environments for Python >=3.5
* Pytest_ for testing Python >=3.5
* Version configuration with `setuptools_scm`_
* Pipenv_ for package management and for generating a repeatable virtual environment
* Packaging of modules, installed into your working environment as an editable library (i.e. ``-e .``) and easily imported into Jupyter notebooks with natural syntax such as ``from module_name import function_name``

*TODO*

* Travis-CI_ (or perhaps `Azure Pipelines`_)for continuous testing.
* Project documentation generated using Sphinx_ and reStructuredText_, ready for hosting alongside your project on GitHub pages. 

Requirements
------------

TODO

Getting started
---------------

TODO

Directory structure
-------------------

TODO

Changelog
---------

TODO

Other resources
---------------

TODO


.. rubric:: Footnotes

.. [#]  The "reasonably standardized", but flexible project structure comprising this Cookiecutter template was heavily inspired by the `drivendata/cookiecutter-data-science`_ template. For a full overview of that template please see the `Cookiecutter Data Science`_.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`drivendata/cookiecutter-data-science`: https://github.com/drivendata/cookiecutter-data-science
.. _`ionelmc/cookiecutter-pylibrary`: https://github.com/ionelmc/cookiecutter-pylibrary
.. _Packaging a python library: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _Packaging pitfalls: https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
.. _Cookiecutter Data Science: https://drivendata.github.io/cookiecutter-data-science/
.. _Travis-CI: http://travis-ci.org/
.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _setuptools_scm: https://github.com/pypa/setuptools_scm/
.. _Pytest: http://pytest.org/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/#
.. _Azure Pipelines: https://azure.microsoft.com/en-us/services/devops/pipelines/