"""pyvalidators base."""


class BaseValidator(object):

    def __init__(self, *args, **kwargs):
        super(BaseValidator, self).__init__(*args, **kwargs)

    def run_validate(self):
        """validate."""
        return self
