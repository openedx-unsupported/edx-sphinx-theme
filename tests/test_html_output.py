#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the HTML output of documentation using ``edx-sphinx-theme``.
"""

from __future__ import absolute_import, unicode_literals

import codecs
import os
import re

import edx_theme


def test_feedback_form_url(html_dir):
    """Each page should have the correct feedback form URL"""
    for page in ['index', 'readme']:
        path = os.path.join(html_dir, '{}.html'.format(page))
        with codecs.open(path, 'r', 'utf-8') as file_obj:
            url = edx_theme.feedback_form_url('edx-sphinx-theme', page)
            assert url in file_obj.read()


def test_logo(html_dir):
    """The output should display the edX logo."""
    css_path = os.path.join(html_dir, '_static', 'css', 'theme.css')
    logo_filename = 'edx-logo-header.png'
    with codecs.open(css_path, 'r', 'utf-8') as css:
        pattern = r'\.icon-home:before[^}]+edx-logo-header\.png'
        assert re.search(pattern, css.read())
    logo_path = os.path.join(html_dir, '_static', 'css', logo_filename)
    assert os.path.exists(logo_path)
