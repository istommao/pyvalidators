# coding: utf-8
"""pyvalidators email test case."""
from __future__ import unicode_literals

from unittest import TestCase

from pyvalidators.email import is_valid_email


class EmailTestCase(TestCase):
    """Email test."""

    def test_success(self):
        email = 'www@gmail.com'
        self.assertTrue(is_valid_email(email))

    def test_failure(self):
        email = '@gmail.com'
        self.assertFalse(is_valid_email(email))
