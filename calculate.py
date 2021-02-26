# File with functions, which read values from entries and write results

import config
import constants as const
from paramsKits import Vertical, Horizontal, Alpha


def vertical_mode():
    """Calculate params in vertical mode"""
    if config.calculate_mode == const.Modes.V0:
        value = config.kit.v0
        kit = Vertical(v0=value)
        kit.by_v0()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.TIME:
        value = config.kit.time
        kit = Vertical(t=value)
        kit.by_time()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.HEIGHT:
        value = config.kit.height
        kit = Vertical(h=value)
        kit.by_height()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    else:
        raise ValueError("Vertical, invalid value of config.calculate_mode")


def horizontal_mode():
    """Calculate params in horizontal mode"""
    if config.calculate_mode == const.Modes.TIME:
        v0 = config.kit.v0
        time = config.kit.time
        kit = Horizontal(v0=v0, t=time)
        kit.by_v0_and_time()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.HEIGHT:
        v0 = config.kit.v0
        height = config.kit.height
        kit = Horizontal(v0=v0, h=height)
        kit.by_v0_and_height()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.DISTANCE:
        v0 = config.kit.v0
        distance = config.kit.distance
        kit = Horizontal(v0=v0, d=distance)
        kit.by_v0_and_dist()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)
    else:
        raise ValueError("Horizontal, invalid value of config.calculate_mode")


def alpha_mode():
    """Calculate params in horizontal mode"""
    if config.calculate_mode == const.Modes.ALPHA:
        v0 = config.kit.v0
        alpha = config.kit.alpha
        kit = Alpha(v0=v0, a=alpha)
        kit.by_v0_and_alpha()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)

    elif config.calculate_mode == const.Modes.TIME:
        v0 = config.kit.v0
        time = config.kit.time
        kit = Alpha(v0=v0, t=time)
        kit.by_v0_and_time()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)

    elif config.calculate_mode == const.Modes.HEIGHT:
        v0 = config.kit.v0
        height = config.kit.height
        kit = Alpha(v0=v0, h=height)
        kit.by_v0_and_height()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)

    elif config.calculate_mode == const.Modes.DISTANCE:
        v0 = config.kit.v0
        distance = config.kit.distance
        kit = Alpha(v0=v0, d=distance)
        kit.by_v0_and_distance()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit)

    else:
        raise ValueError("Alpha, invalid value of config.calculate_mode")
