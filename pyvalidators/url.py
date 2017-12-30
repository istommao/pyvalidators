"""url."""
import re

URL_REGEX = '[a-zA-Z]+://[^s]*'


def is_valid_url(url):
    return re.match(URL_REGEX, url)
