"""pyvalidators email."""
import re

EMAIL_REGEX = '[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'


def is_valid_email(email):
    """Validate email is valid."""
    if re.match(EMAIL_REGEX, email):
        return True
    else:
        return False
