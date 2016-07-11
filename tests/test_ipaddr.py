"""pyvalidators ipaddr test case."""

from unittest import TestCase

from pyvalidators.ipaddr import IPAddrValidator


class IPAddrTestCase(TestCase):
    """IP address test."""

    def test_success(self):
        ipaddr = '127.0.0.1'
        self.assertTrue(IPAddrValidator.is_valid(ipaddr))

    def test_failure(self):
        self.assertFalse(IPAddrValidator.is_valid('127.0.0'))
        self.assertFalse(IPAddrValidator.is_valid('asdf'))
        self.assertFalse(IPAddrValidator.is_valid('127.0.0.sdf'))
        self.assertFalse(IPAddrValidator.is_valid('127.0.0.1.'))
        self.assertFalse(IPAddrValidator.is_valid('127.0'))
