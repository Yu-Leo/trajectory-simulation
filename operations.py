# File with any operations in application

import webbrowser

import config
import constants as const


def open_theory():
    """Open web-page with theory"""
    if config.throw_type == const.ThrowType.VERTICAL:
        url = const.Theory.url_vertical
    elif config.throw_type == const.ThrowType.HORIZONTAL:
        url = const.Theory.url_horizontal
    elif config.throw_type == const.ThrowType.ALPHA:
        url = const.Theory.url_alpha
    else:
        raise ValueError("Open theory. Incorrect value in config.throw_type")
    webbrowser.open_new(url)
