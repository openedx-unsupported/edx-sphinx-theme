edx-sphinx-theme  |Travis|_ |Codecov|_
======================================
.. |Travis| image:: https://travis-ci.org/edx/edx-sphinx-theme.svg?branch=master
.. _Travis: https://travis-ci.org/edx/edx-sphinx-theme

.. |Codecov| image:: http://codecov.io/github/edx/edx-sphinx-theme/coverage.svg?branch=master
.. _Codecov: http://codecov.io/github/edx/edx-sphinx-theme?branch=master

edx-sphinx-theme is a Sphinx theme for `Open edX`_ documentation.  It should be
used for all documentation in repositories in the ``edx`` GitHub organization
which is intended to be used with the `Sphinx`_ documentation system.

.. _Open edX: https://open.edx.org/
.. _Sphinx: http://www.sphinx-doc.org/en/stable/

Overview
--------

This theme makes the following changes to the default Sphinx output:

* Displays the edX logo
* Adds a link to a feedback form that identifies which page the feedback came from

To use edx-sphinx-theme for a repository's documentation:

* ``pip install edx-sphinx-theme`` or equivalent (add ``edx-sphinx-theme``
  to any appropriate requirements files)
* Add ``edx_theme`` to the ``extensions`` list in conf.py (it adds the
  feedback form URL to the rendering context for each page).
* Update the ``html_theme`` and ``html_theme_path`` values in conf.py so the
  theme can be located and loaded.
* Use the ``AUTHOR`` and ``COPYRIGHT`` constants where appropriate in conf.py
  (these defaults are only provided as a convenience, the repository is free
  to use other values if appropriate).

For example:

.. code-block:: python

    import edx_theme

    extensions = ['edx_theme']

    copyright = edx_theme.COPYRIGHT
    author = edx_theme.AUTHOR

    html_theme = 'edx_theme'
    html_theme_path = [edx_theme.get_html_theme_path()]

    latex_documents = [
        (master_doc, 'edx-sphinx-theme.tex', 'edx-sphinx-theme Documentation',
         author, 'manual'),
    ]

Documentation
-------------

The full documentation is at https://edx-sphinx-theme.readthedocs.org.

License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help
