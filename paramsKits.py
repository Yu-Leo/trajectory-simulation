# File with classes of numbers kit in different throw-types

import constants as const
import exceptions as exc
import text


class Kit:
    """Class with all parameters"""
    DIGITS_AFTER_DOT = 5  # Number of digits after the dot

    @staticmethod
    def __check_value(field_ind, value):
        """If value is correct, return it in float else raise Exception"""
        if value is None:
            return None
        if isinstance(value, str):
            if value == "":
                return None
            try:
                fl = float(value)
            except ValueError:
                raise exc.EntryContentError(field=field_ind, exception_type=exc.TYPE_ERROR)
            else:
                return fl
        elif isinstance(value, float):
            return value
        else:
            raise exc.EntryContentError(field=field_ind, exception_type=exc.TYPE_ERROR)

    def __init__(self, v0=None, a=None, t=None, h=None, d=None):
        self._v0 = v0  # Initial speed
        self._alpha = a  # Angle of throw
        self._time = t  # Flight time
        self._height = h  # Max / start height
        self._distance = d  # Flight distance

    def __repr__(self):
        v0 = f"V0 (initial speed): {self.v0}"
        alpha = f"a (angle of throw): {self.alpha}"
        time = f"T (flight time): {self.time}"
        height = f"H (initial speed): {self.height}"
        distance = f"D (initial speed): {self.distance}"
        return v0 + "\n" + alpha + "\n" + time + "\n" + height + "\n" + distance

    def __getitem__(self, key):
        kit_dict = {text.v0: self._v0,
                    text.alpha: self._alpha,
                    text.time: self._time,
                    text.height: self._height,
                    text.distance: self._distance}
        return kit_dict.get(key, "ERROR")

    def set_params(self, kit_dict):
        """Set all params from kit"""
        self._v0 = Kit.__check_value(const.Modes.V0, kit_dict[text.v0])
        self._alpha = Kit.__check_value(const.Modes.ALPHA, kit_dict[text.alpha])
        self._time = Kit.__check_value(const.Modes.TIME, kit_dict[text.time])
        self._height = Kit.__check_value(const.Modes.HEIGHT, kit_dict[text.height])
        self._distance = Kit.__check_value(const.Modes.DISTANCE, kit_dict[text.distance])

    @property
    def v0(self):
        return self._v0

    @property
    def alpha(self):
        return self._alpha

    @property
    def time(self):
        return self._time

    @property
    def height(self):
        return self._height

    @property
    def distance(self):
        return self._distance


class Vertical(Kit):
    """Class with parameters of vertical throw"""

    def __init__(self, v0=None, t=None, h=None):
        super().__init__(v0=v0, t=t, h=h)

    def by_v0(self):
        """Calculate all params by initial speed"""
        self._height = round((self.v0 ** 2 / (2 * const.G)), Kit.DIGITS_AFTER_DOT)
        self._time = round((self.v0 / const.G), Kit.DIGITS_AFTER_DOT)

    def by_time(self):
        """Calculate all params by flight time"""
        self._v0 = round((self.time * const.G), Kit.DIGITS_AFTER_DOT)
        self.by_v0()

    def by_height(self):
        """Calculate all params by max height"""
        self._v0 = round((2 * const.G * self.height) ** 0.5, Kit.DIGITS_AFTER_DOT)
        self.by_v0()
