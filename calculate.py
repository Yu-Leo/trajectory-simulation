# File with functions, which read values from entries and write results

import config
import constants as const
from paramsKits import Vertical as VerticalKit


def vertical_mode(value):
    """Calculate params in vertical mode"""
    if config.calculate_mode == const.Modes.V0:
        kit = VerticalKit(v0=value)
        kit.by_v0()

    print("calc by", value)
