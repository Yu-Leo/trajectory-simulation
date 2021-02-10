# File with widget's classes

import tkinter as tk
from tkinter.ttk import Combobox

import constants as const
import text
from windowsParameters import DrawingFieldParams, SizeParams


class DrawingField:
    """Field for simulation"""

    def __init__(self, window):
        self.__parameters = DrawingFieldParams(bg="white",
                                               width=500,
                                               height=400,
                                               padx=10,
                                               pady=10)

        self.__object = tk.Canvas(window, bg=self.__parameters.bg,
                                  width=self.__parameters.width,
                                  height=self.__parameters.height)

    def draw(self):
        self.__object.pack(side=tk.LEFT,
                           padx=self.__parameters.padx,
                           pady=self.__parameters.pady)


class Menu:
    """Frame with simulation's menu"""

    def __init__(self, window):
        self.__object = tk.Frame(window)
        self.__parameters = SizeParams(None, None, padx=10, pady=10)

        self.__cast_type = ThrowType(self.__object)
        self.__cast_params = ThrowParams(self.__object)
        self.__buttons = Buttons(self.__object)

    def draw(self):
        self.__cast_type.draw()
        self.__cast_params.draw()
        self.__buttons.draw()

        self.__object.pack(side=tk.RIGHT,
                           padx=self.__parameters.padx,
                           pady=self.__parameters.pady)


class ThrowType:
    """Class of widget, which chose the throw type"""

    def __init__(self, window):
        self.__label = tk.Label(window, text=text.throw_type_title, font="Arial 12")
        self.__menu = Combobox(window, values=text.throw_types, state="readonly", width=22)
        self.__menu.current(const.DEFAULT_THROW_TYPE)

    def draw(self):
        self.__label.pack()
        self.__menu.pack()


class ThrowParams:
    """Class of widgets, which set throw parameters"""

    def __init__(self, window):
        pass

    def draw(self):
        pass


class Buttons:
    """Class of buttons for interaction with app"""

    def __init__(self, window):
        pass

    def draw(self):
        pass
