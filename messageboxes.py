# File with messageboxes's classes

import tkinter.messagebox as mb

"""
from constants import Exceptions as ConstEx
from exceptions import FloatEntryContentError as FloatError
from exceptions import IntEntryContentError as IntError
from text import int_exceptions, float_exceptions
"""
import exceptions as exc
from text import exceptions_dict


class ErrorMb:
    """Messagebox типа Error"""

    def __init__(self, title, message):
        self.title = title
        self.message = message

    def show(self):
        mb.showerror(self.title, self.message)


class ExceptionMb(ErrorMb):
    """Messagebox-ы самописных ошибок"""

    def __init__(self, exception):
        if exception.exception_type == exc.TYPE_ERROR:
            ErrorMb.__init__(self, title=exceptions_dict[exception.field].title,
                             message=exceptions_dict[exception.field].type_error)
        elif exception.exception_type == exc.RANGE_ERROR:
            ErrorMb.__init__(self, title=exceptions_dict[exception.field].title,
                             message=exceptions_dict[exception.field].range_error)
        else:
            raise ValueError("Exception type error")
