"""ip address validator."""
import re

IP_ADDRESS_REGEX = (r'^(((\d{1,2})|(1\d{2,2})|(2[0-4][0-9])|'
                    r'(25[0-5]))\.){3,3}((\d{1,2})|(1\d{2,2})|'
                    r'(2[0-4][0-9])|(25[0-5]))$')


def is_valid_ipaddr(ipaddr):
    """Validate ip address is valid."""
    return re.match(IP_ADDRESS_REGEX, ipaddr)


class IPAddrValidator(object):
    """IP address validator."""

    @staticmethod
    def is_valid(ipaddr):
        """Validate ip address is valid."""
        return is_valid_ipaddr(ipaddr)
