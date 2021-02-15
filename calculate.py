# File with functions, which read values from entries and write results

import config
import constants as const
from paramsKits import Vertical as VerticalKit


def vertical_mode():
    """Calculate params in vertical mode"""
    if config.calculate_mode == const.Modes.V0:
        value = config.kit.v0
        kit = VerticalKit(v0=value)
        kit.by_v0()
        config.kit.set_params(config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.TIME:
        value = config.kit.time
        kit = VerticalKit(t=value)
        kit.by_time()
        config.kit.set_params(config.calculate_mode, kit)
    elif config.calculate_mode == const.Modes.HEIGHT:
        value = config.kit.height
        kit = VerticalKit(h=value)
        kit.by_height()
        config.kit.set_params(config.calculate_mode, kit)
    else:
        raise ValueError("config.calculate_mode error")


def horizontal_mode():
    """Calculate params in horizontal mode"""
    pass
