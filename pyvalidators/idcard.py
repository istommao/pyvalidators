"""idcard validator."""
import re

IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9xX])?'


def is_valid_idcard(idcard):
    """Validate id card is valid."""
    return re.match(IDCARD_REGEX, idcard)
