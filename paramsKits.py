# File with classes of numbers kit in different throw-types

class Kit:
    """Class with all parameters"""

    def __init__(self, v0=0.0, a=0.0, t0=0.0, h=0.0, d=0.0):
        self._v0 = v0  # Initial speed
        self._alpha = a  # Angle of throw
        self._time = t0  # Flight time
        self._height = h  # Max / start height
        self._distance = d  # Flight distance

    def __repr__(self):
        v0 = f"V0 (initial speed): {self.v0}"
        alpha = f"a (angle of throw): {self.alpha}"
        time = f"T (flight time): {self.time}"
        height = f"H (initial speed): {self.height}"
        distance = f"D (initial speed): {self.distance}"
        return v0 + "\n" + alpha + "\n" + time + "\n" + height + "\n" + distance

    @property
    def v0(self):
        return self._v0

    @v0.setter
    def v0(self, value):
        self._v0 = value

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        self._alpha = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value


class Vertical(Kit):
    """Class with parameters of vertical throw"""

    def __init__(self, v0=0.0, t0=0.0, h=0.0):
        super().__init__(v0=v0, t0=t0, h=h)

    def by_v0(self):
        """Calculate all params by initial speed"""
        pass

    def by_time(self):
        """Calculate all params by flight time"""
        pass

    def by_height(self):
        """Calculate all params by max height"""
        pass
