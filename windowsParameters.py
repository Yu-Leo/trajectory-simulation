# File with window's parameters class

class SizeParams:
    """Class with size and paddings parameters"""

    def __init__(self, width, height, padx, pady):
        self.width = width
        self.height = height
        self.padx = padx
        self.pady = pady


class WindowParams(SizeParams):
    """Class of parameters for window"""

    def __init__(self, title="", width=None, height=None, padx=None, pady=None):
        self.title = title
        super().__init__(width, height, padx, pady)
        self.resizable = (False, False)
        self.ico_path = ""  # Path to application's icon

    def geometry(self):
        """Geometry by Tkinter's standard"""
        if (self.width, self.height, self.padx, self.pady) == [None] * 4:
            return ""
        if self.width is None or self.height is None:
            return f"+{self.padx}+{self.pady}"
        if self.padx is None or self.pady is None:
            return f"{self.width}x{self.height}"
        return f"{self.width}x{self.height}+{self.padx}+{self.pady}"


class DrawingFieldParams(SizeParams):
    """Class of parameters for drawing field"""

    def __init__(self, bg="", width=None, height=None, padx=None, pady=None):
        self.bg = bg
        super().__init__(width, height, padx, pady)
