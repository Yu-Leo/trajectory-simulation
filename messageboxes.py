# File with messageboxes's classes

import tkinter.messagebox as mb

import exceptions as exc
import text


class ErrorMb:
    """Messagebox with Error-type"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class ExceptionMb(ErrorMb):
    """Messageboxes for my exceptions"""

    def __init__(self, exception):
        if exception.exception_type == exc.TYPE_ERROR:
            ErrorMb.__init__(self, title=text.exception_text(exception.field).title,
                             message=text.exception_text(exception.field).type_error)
        elif exception.exception_type == exc.RANGE_ERROR:
            ErrorMb.__init__(self, title=text.exception_text(exception.field).title,
                             message=text.exception_text(exception.field).range_error)
        elif exception.exception_type == exc.ALPHA_RANGE_ERROR:
            ErrorMb.__init__(self, title=text.exception_text(exception.field).title,
                             message=text.alpha_range_error)
        else:
            raise ValueError("Exception type error")
