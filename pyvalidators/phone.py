# coding: utf-8
"""phone validator.
    13[0-9], 14[5,7], 15[0, 1, 2, 3, 5, 6, 7, 8, 9], 17[1, 3, 6, 7, 8], 18[0-9], 170[0-9]

    CHINA MOBILE: 134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705
    CHINA UNICOM: 130,131,132,155,156,185,186,145,176,1709
    CHINA TELECOM: 133,153,180,181,189,173,177,1700

"""
from __future__ import unicode_literals

import re


CHINA_PHONE_REGEX = '^1(3[0-9]|4[57]|5[0-35-9]|7[1356-8]|8[0-9]|70)\\d{8}$'


def is_valid_phone(phone):
    """Validate phone is valid."""
    return re.match(CHINA_PHONE_REGEX, phone)


class PhoneValidator(object):
    """Phone validator."""

    CHINA_MOBILE_REGEX = ('(^1(3[4-9]|4[7]|5[0-27-9]|7[8]|8[2-478])\\d{8}$)|'
                          '(^1705\\d{7}$)')

    CHINA_UNICOM_REGEX = ('(^1(3[0-2]|4[5]|5[56]|7[6]|8[56])\\d{8}$)|'
                          '(^1709\\d{7}$)')

    CHINA_TELECOM_REGEX = '(^1(33|53|73|77|8[019])\\d{8}$)|(^1700\\d{7}$)'

    @classmethod
    def is_valid(cls, phone):
        """Validate phone number is valid."""
        return is_valid_phone(phone)

    @classmethod
    def number_segment(cls, phone):
        """Check phone number segment."""
        if cls.is_valid(phone) is None:
            return '无效的号码'

        if re.match(cls.CHINA_MOBILE_REGEX, phone):
            result = '中国移动'
        elif re.match(cls.CHINA_UNICOM_REGEX, phone):
            result = '中国联通'
        elif re.match(cls.CHINA_TELECOM_REGEX, phone):
            result = '中国电信'
        else:
            result = '未知号码段'

        return result
