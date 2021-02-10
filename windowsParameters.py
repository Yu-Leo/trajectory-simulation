# File with window's parameters class

class WindowParameters:
    def __init__(self, title="", width=None, height=None, padx=None, pady=None):
        self.title = title
        self.__width = width
        self.__height = height
        self.__padx = padx
        self.__pady = pady
        self.resizable = (False, False)
        self.ico_path = ""  # Path to application's icon

    def geometry(self):
        """Geometry by Tkinter's standard"""
        if self.__width is None and self.__height is None \
                and self.__padx is None and self.__pady is None:
            return ""

        if self.__width is None or self.__height is None:
            return f"+{self.__padx}+{self.__pady}"
        if self.__padx is None or self.__pady is None:
            return f"{self.__width}x{self.__height}"
        return f"{self.__width}x{self.__height}+{self.__padx}+{self.__pady}"


class DrawingFieldParameters:
    def __init__(self, bg="", width=None, height=None, padx=None, pady=None):
        self.bg = bg
        self.width = width
        self.height = height
        self.padx = padx
        self.pady = pady
