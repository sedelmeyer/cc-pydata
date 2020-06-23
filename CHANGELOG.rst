Changelog
=========

.. _future-releases:

Future releases
---------------

.. todo::

    * Improve template README.rst placeholder instructions for replicating and adding to a ``cc-pydata`` project
    * Create a ``gh-pages`` script to automate docs publishing steps

.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage
.. _cookiecutter-datascience: https://github.com/drivendata/cookiecutter-data-science
.. _pytest-cookies: https://github.com/hackebrot/pytest-cookies
.. _tox: https://tox.readthedocs.io/en/latest/
.. _`Azure Pipelines`: https://azure.microsoft.com/en-us/services/devops/pipelines/

v0.3.0 (Under development)
--------------------------

* Add ``tox`` to project repo for testing with ``py36``, ``py37``, ``py38``
* Refactor testing for clearer organization of default template vs. options tests

.. todo::

    * Add tox_ option to template
    * Add pre- and post-gen hooks
    * Clean up template gen options
    * Make Travis-CI an option
    * Add `Azure Pipelines`_ option to template
    * Add default Python version argument to template


v0.2.1 (2020-06-17)
-------------------

* Add ``setup.py`` packaging and setuptools-scm versioning to project
* Add unit tests and TravisCI to project

v0.2.0 (2020-06-14)
-------------------

* Add standard submodule placeholders to ``cc-pydata`` template
* Add basic logging config and functionality to template
* Add logging documentation to ``cc-pydata`` tutorial
* Add ``sphinx.ext.autosummary`` api starter documentation to template docs

v0.1.7 (2020-05-31)
-------------------

* Add requirements and links to other useful resources to ``README.rst``
* Add basic Sphinx usage instructions to docs
* Add basic unit testing info to docs

v0.1.6 (2020-05-26)
-------------------

* Fix ``gh-pages`` tutorial instructions
* Fix template ``setup.cfg`` ``--pyargs`` to prevent travis-ci build failure

v0.1.5 (2020-01-13)
-------------------

* Add GitHub Pages ``git`` workflow to the project tutorial
* Fix setuptools-scm and static path in the template ``conf.py`` file

v0.1.4 (2020-01-11)
-------------------

* Add ``notebooks`` directory to template
* Add template directory structure to the project documentation

v0.1.3 (2020-01-10)
-------------------

* Add initial template ``README.rst`` to the template
* Add Sphinx and flake8 to template Pipfile
* Add Sphinx documentation skeleton with Jinja fields to template
* Add initial content to the project tutorial

v0.1.2 (2020-01-06)
-------------------

* Add initial Sphinx documentation skeleton to project

v0.1.1 (2020-01-04)
-------------------

* Simplify packaging and remove tox.ini and MANIFEST.in from template
* Add travis.yml, .editorconfig, and Pipfile to template
* Add initial readme to project

v0.1.0 (2020-01-02)
-------------------

* Add basic python packaging files to template

v0.0.0 (2020-01-01)
-------------------

* Initial template with placeholder directories
