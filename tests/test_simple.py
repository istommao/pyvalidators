"""pyvalidators simple useage test case."""

from unittest import TestCase

from pyvalidators.ipaddr import is_valid_ipaddr
from pyvalidators.phone import is_valid_phone
from pyvalidators.email import is_valid_email
from pyvalidators.idcard import is_valid_idcard


class SimpleUseageTestCase(TestCase):
    """Simple useage test."""

    def test_is_valid_ipaddr(self):
        """Validate ipaddr."""
        self.assertFalse(is_valid_ipaddr('127.0.0'))
        self.assertFalse(is_valid_ipaddr('asdf'))
        self.assertFalse(is_valid_ipaddr('127.0.0.sdf'))
        self.assertFalse(is_valid_ipaddr('127.0.0.1.'))
        self.assertFalse(is_valid_ipaddr('127.0'))

    def test_is_valid_phone(self):
        """Validate phone."""
        self.assertFalse(is_valid_phone('188002333'))
        self.assertFalse(is_valid_phone('1110023333'))

    def test_is_valid_email(self):
        """Validate email."""
        self.assertFalse(is_valid_email('188002333'))
        self.assertTrue(is_valid_email('12345@qq.com'))

    def test_is_valid_idcard(self):
        """Validate idcard."""
        self.assertFalse(is_valid_idcard('188002333'))
        self.assertTrue(is_valid_idcard('220582197707198132'))
        self.assertTrue(is_valid_idcard('330200197307222708'))
        self.assertTrue(is_valid_idcard(330200197307222708))
