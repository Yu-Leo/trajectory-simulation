# File with classes of numbers kit in different throw-types

import constants as const
import exceptions as exc


class Kit:
    """Class with all parameters"""
    DIGITS_AFTER_DOT = 5  # Number of digits after the dot

    @staticmethod
    def __check_value(field_ind, throw_type, calculate_mode, value):
        """If value is correct, return it in float else raise Exception"""
        if value is None:
            return None
        if isinstance(value, str):
            if value == "":
                if (throw_type == const.ThrowType.HORIZONTAL and
                        field_ind == const.Modes.V0):
                    raise exc.EntryContentError(field=field_ind,
                                                exception_type=exc.TYPE_ERROR)
                if calculate_mode == field_ind:
                    raise exc.EntryContentError(field=field_ind,
                                                exception_type=exc.TYPE_ERROR)

                return None
            try:
                fl = float(value)
            except ValueError:
                raise exc.EntryContentError(field=field_ind, exception_type=exc.TYPE_ERROR)
            else:
                if fl <= 0:
                    raise exc.EntryContentError(field=field_ind, exception_type=exc.RANGE_ERROR)
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
        kit_dict = {const.Modes.V0: self._v0,
                    const.Modes.ALPHA: self._alpha,
                    const.Modes.TIME: self._time,
                    const.Modes.HEIGHT: self._height,
                    const.Modes.DISTANCE: self._distance}
        return kit_dict.get(key, "ERROR")

    def set_params(self, throw_type, calculate_mode, kit_dict):
        """Set all params from kit"""
        self._v0 = Kit.__check_value(const.Modes.V0, throw_type,
                                     calculate_mode, kit_dict[const.Modes.V0])
        self._alpha = Kit.__check_value(const.Modes.ALPHA, throw_type,
                                        calculate_mode, kit_dict[const.Modes.ALPHA])
        self._time = Kit.__check_value(const.Modes.TIME, throw_type,
                                       calculate_mode, kit_dict[const.Modes.TIME])
        self._height = Kit.__check_value(const.Modes.HEIGHT, throw_type,
                                         calculate_mode, kit_dict[const.Modes.HEIGHT])
        self._distance = Kit.__check_value(const.Modes.DISTANCE, throw_type,
                                           calculate_mode, kit_dict[const.Modes.DISTANCE])

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
        height = self.v0 ** 2 / (2 * const.G)
        self._height = round(height, Kit.DIGITS_AFTER_DOT)
        time = self.v0 / const.G
        self._time = round(time, Kit.DIGITS_AFTER_DOT)

    def by_time(self):
        """Calculate all params by flight time"""
        v0 = self.time * const.G
        self._v0 = round(v0, Kit.DIGITS_AFTER_DOT)
        self.by_v0()

    def by_height(self):
        """Calculate all params by max height"""
        v0 = (2 * const.G * self.height) ** 0.5
        self._v0 = round(v0, Kit.DIGITS_AFTER_DOT)
        self.by_v0()


class Horizontal(Kit):
    """Class with parameters of horizontal throw"""

    def __init__(self, v0=None, t=None, h=None, d=None):
        super().__init__(v0=v0, t=t, h=h, d=d)

    def by_v0_and_time(self):
        """Calculate all params by initial speed and flight time"""
        height = (const.G * self.time ** 2) / 2
        self._height = round(height, Kit.DIGITS_AFTER_DOT)
        distance = self.v0 * self.time
        self._distance = round(distance, Kit.DIGITS_AFTER_DOT)

    def by_v0_and_height(self):
        """
        Calculate all params by initial speed and height
        from which the throw was made
        """
        time = ((2 * self.height) / const.G) ** 0.5
        self._time = round(time, Kit.DIGITS_AFTER_DOT)
        self.by_v0_and_time()

    def by_v0_and_dist(self):
        """Calculate all params by initial speed and flight distance"""
        time = self.distance / self.v0
        self._time = round(time, Kit.DIGITS_AFTER_DOT)
        self.by_v0_and_time()


class Alpha(Kit):
    """Class with parameters of throw под углом к горизонту"""

    def __init__(self, v0=None, a=None, t=None, h=None, d=None):
        super().__init__(v0=v0, a=a, t=t, h=h, d=d)

    def by_v0_and_alpha(self):
        pass

    def by_v0_and_time(self):
        pass

    def by_v0_and_height(self):
        pass

    def by_v0_and_distance(self):
        pass
