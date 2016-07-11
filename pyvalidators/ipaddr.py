"""ip address validator."""
import re


class IPAddrValidator(object):
    """IP address validator."""

    IP_ADDRESS_REGEX = ('^(((\d{1,2})|(1\d{2,2})|(2[0-4][0-9])|'
                        '(25[0-5]))\.){3,3}((\d{1,2})|(1\d{2,2})|'
                        '(2[0-4][0-9])|(25[0-5]))$')

    @classmethod
    def is_valid(cls, ipaddr):
        """Validate ip address is valid."""
        if re.match(cls.IP_ADDRESS_REGEX, ipaddr):
            return True
        else:
            return False
