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
        config.kit.set_params(kit)
