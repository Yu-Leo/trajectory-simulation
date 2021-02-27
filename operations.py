# File with any operations in application

import json  # Module for working with json format
import webbrowser  # Module for opening pages in web-browser

import config
import constants as const
import text


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


def generate_data():
    """Generate dictionary with parameters of throw by config file"""
    data = {}  # Dictionary with parameters of throw

    data[text.throw_type_title] = text.throw_types[config.throw_type]  # Throw type

    data[text.params_title] = {}  # Throw params
    data[text.params_title][text.params[0]] = config.kit.v0
    if config.throw_type == const.ThrowType.ALPHA:
        data[text.params_title][text.params[1]] = config.kit.alpha
    data[text.params_title][text.params[2]] = config.kit.time
    data[text.params_title][text.params[3]] = config.kit.height
    if config.throw_type in (const.ThrowType.HORIZONTAL, const.ThrowType.ALPHA):
        data[text.params_title][text.params[4]] = config.kit.distance
    return data


def save_parameters(filename):
    """Save parameters to file in .json format"""
    with open(filename, "w", encoding="utf-8") as file:
        data = generate_data()
        params_string = json.dumps(data,
                                   ensure_ascii=False,
                                   indent=2)
        file.write(params_string)
