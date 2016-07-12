"""pyvalidators simple useage test case."""

from unittest import TestCase

from pyvalidators.ipaddr import is_valid_ipaddr
from pyvalidators.phone import is_valid_phone
from pyvalidators.email import is_valid_email


class SimpleUseageTestCase(TestCase):
    """Simple useage test."""

    def test_is_valid_ipaddr(self):
        self.assertFalse(is_valid_ipaddr('127.0.0'))
        self.assertFalse(is_valid_ipaddr('asdf'))
        self.assertFalse(is_valid_ipaddr('127.0.0.sdf'))
        self.assertFalse(is_valid_ipaddr('127.0.0.1.'))
        self.assertFalse(is_valid_ipaddr('127.0'))

    def test_is_valid_phone(self):
        self.assertFalse(is_valid_phone('188002333'))
        self.assertFalse(is_valid_phone('1110023333'))

    def test_is_valid_email(self):
        self.assertFalse(is_valid_email('188002333'))
        self.assertTrue(is_valid_email('12345@qq.com'))
