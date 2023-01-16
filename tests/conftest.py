"""
Pytest fixtures for building and cleaning up the generated documentation.
"""
from __future__ import absolute_import, unicode_literals

import os
from shutil import rmtree

import pytest
from sphinx.cmd.build import build_main


@pytest.fixture(scope='session')
def html_dir():
    """
    Build the HTML output for the documentation and provide its path to tests.
    """
    docs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'docs')
    build_path = os.path.join(docs_path, '_test', 'html')
    os.chdir(docs_path)
    result = build_main(['sphinx-build', '-b', 'html', '.', build_path])
    assert result == 0
    yield build_path
    rmtree(build_path)
