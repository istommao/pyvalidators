"""ip address validator."""
import re


class IPAddrValidator(object):
    """IP address validator."""

    IP_ADDRESS_REGEX = ('((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}'
                        '(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))')

    @classmethod
    def is_valid(cls, ipaddr):
        """Validate ip address is valid."""
        if re.match(cls.IP_ADDRESS_REGEX, ipaddr):
            return True
        else:
            return False
