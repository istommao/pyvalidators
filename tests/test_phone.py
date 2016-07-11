"""pyvalidators phone number test case."""

from unittest import TestCase

from pyvalidators.phone import PhoneValidator


class PhoneTestCase(TestCase):
    """Phone number test."""

    def test_success(self):
        phone = '18068823333'
        self.assertTrue(PhoneValidator.is_valid(phone))

    def test_failure(self):
        self.assertFalse(PhoneValidator.is_valid('188002333'))
        self.assertFalse(PhoneValidator.is_valid('1110023333'))

    def test_number_segment(self):
        self.assertEqual(PhoneValidator.number_segment('188002333'),
                         '无效的号码')

        self.assertEqual(PhoneValidator.number_segment('15868823333'),
                         '中国移动')
        self.assertEqual(PhoneValidator.number_segment('18068823333'),
                         '中国电信')
        self.assertEqual(PhoneValidator.number_segment('13068823333'),
                         '中国联通')
