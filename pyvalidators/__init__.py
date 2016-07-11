"""pyvalidators."""


from pyvalidators.phone import PhoneValidator
from pyvalidators.ipaddr import IPAddrValidator


def is_valid_phone(phone):
    """Validate phone is valid."""
    return PhoneValidator.is_valid(phone)


def is_valid_ipaddr(ipaddr):
    """Validate ip address is valid."""
    return IPAddrValidator.is_valid(ipaddr)


__all__ = [
    'is_valid_phone',
    'is_valid_ipaddr',
    'PhoneValidator',
    'IPAddrValidator'
]
