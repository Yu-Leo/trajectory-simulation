# File with classes of numbers kit in different throw-types

class Vertical:
    """Class with parameters of vertical throw"""

    def __init__(self, v0=0, t0=0, h=0):
        self.__v0 = v0  # Initial speed
        self.__time = t0
        self.__height = h

    def by_v0(self):
        """Calculate all params by initial speed"""
        pass

    def by_time(self):
        """Calculate all params by flight time"""
        pass

    def by_height(self):
        """Calculate all params by max height"""
        pass
