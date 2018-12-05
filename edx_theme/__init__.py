"""
A Sphinx theme for Open edX documentation.
"""

from __future__ import absolute_import, print_function, unicode_literals

import datetime
import os

import six
from six.moves.urllib.parse import quote

# When you change this, also update the CHANGELOG.rst file, thanks.
__version__ = '1.4.0'

# Use these constants in the conf.py for Sphinx in your repository
AUTHOR = 'edX Inc.'
COPYRIGHT = '{year}, edX Inc.'.format(year=datetime.datetime.now().year)

FEEDBACK_FORM_FMT = "https://docs.google.com/forms/d/1T5QGnYb_QnQoMO7T_eatq02miPTY40WVe3cgGphNAdY/" \
                    "viewform?entry.1952574704&entry.241692674={pageid}"


def get_html_theme_path():
    """
    Get the absolute path of the directory containing the theme files.
    """
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def feedback_form_url(project, page):
    """
    Create a URL for feedback on a particular page in a project.
    """
    return FEEDBACK_FORM_FMT.format(pageid=quote("{}: {}".format(project, page)))


def update_context(app, pagename, templatename, context, doctree):  # pylint: disable=unused-argument
    """
    Update the page rendering context to include ``feedback_form_url``.
    """
    context['feedback_form_url'] = feedback_form_url(app.config.project, pagename)


def setup(app):
    """
    Sphinx extension to update the rendering context with the feedback form URL.

    Arguments:
        app (Sphinx): Application object for the Sphinx process

    Returns:
        a dictionary of metadata (http://www.sphinx-doc.org/en/stable/extdev/#extension-metadata)
    """
    event = 'html-page-context' if six.PY3 else b'html-page-context'
    app.connect(event, update_context)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        'version': __version__,
    }
