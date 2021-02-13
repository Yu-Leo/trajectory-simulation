# File with my exceptions

TYPE_ERROR = 0
RANGE_ERROR = 1
WARNING = 2


class EntryContentError(ValueError):
    """Invalid values in entries"""

    def __init__(self, field, exception_type, message=""):
        self.field = field  # Field index
        self.exception_type = exception_type
        self.text = message  # Additional information

    def __str__(self):
        return repr(f"Field index: {self.field}")
