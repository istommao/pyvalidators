# coding: utf-8
"""pyvalidators url test case."""
from __future__ import unicode_literals

from unittest import TestCase

from pyvalidators.url import is_valid_url


class UrlTestCase(TestCase):
    """URL test."""

    def test_success(self):
        url = 'https://github.com/'
        self.assertTrue(is_valid_url(url))

    def test_failure(self):
        url = 'asdf.com'
        self.assertFalse(is_valid_url(url))
