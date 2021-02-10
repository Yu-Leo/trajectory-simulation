# File with widget's classes

import tkinter as tk
from tkinter.ttk import Combobox

import config
import constants as const
import style
import text
from windowsParameters import DrawingFieldParams, SizeParams


class DrawingField:
    """Field for simulation"""

    def __init__(self, window):
        self.__parameters = DrawingFieldParams(bg="white",
                                               width=500,
                                               height=430,
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
        self.__object = tk.Frame(window)  # Frame for all menu
        self.__parameters = SizeParams(None, None, padx=10, pady=10)

        self.__throw_type = ThrowType(self.__object, change_func=self.change_throw_params_list)
        self.__throw_params = ThrowParams(self.__object, config.trow_type)
        self.__buttons = Buttons(self.__object)

    def draw(self):
        self.__throw_type.draw()
        self.__throw_params.draw()
        self.__buttons.draw()

        self.__object.pack(side=tk.RIGHT,
                           padx=self.__parameters.padx,
                           pady=self.__parameters.pady,
                           fill=tk.Y)

    def change_throw_params_list(self, throw_type):
        self.__throw_params.hide()
        self.__throw_params = ThrowParams(self.__object, throw_type)
        self.__throw_params.draw()


class ThrowType:
    """Class of widget, which chose the throw type"""

    def __init__(self, window, change_func):
        self.__object = tk.Frame(window)
        self.__label = tk.Label(self.__object, text=text.throw_type_title, font=(style.font_name, 12))
        self.__menu = Combobox(self.__object, values=text.throw_types, state="readonly", width=22)
        self.__menu.current(config.trow_type)  # Default value
        self.__menu.bind("<<ComboboxSelected>>", lambda event: change_func(self.__menu.current()))

    def draw(self):
        self.__label.pack()
        self.__menu.pack()
        self.__object.pack(side=tk.TOP, anchor=tk.N, pady=20)


class ThrowParams:
    """Class of widgets, which set throw parameters"""

    def __init__(self, window, throw_type):
        self.__object = tk.Frame(window)  # Frame for params
        self.__v0 = ParamRow(self.__object, "V0")
        need_alpha = throw_type == const.TrowType.ALPHA
        need_distance = throw_type in (const.TrowType.ALPHA, const.TrowType.HORIZONTAL)
        self.__alpha = ParamRow(self.__object, "a", but=True) if need_alpha else None
        self.__time = ParamRow(self.__object, "T", but=True)
        self.__height = ParamRow(self.__object, "H", but=True)
        self.__distance = ParamRow(self.__object, "L", but=True) if need_distance else None
        self.__button = tk.Button(self.__object, text=text.read_from_file, font=(style.font_name, 10), width=18)

    def draw(self):
        self.__v0.draw(0)
        if self.__alpha is not None:
            self.__alpha.draw(1)
        self.__time.draw(2)
        self.__height.draw(3)
        if self.__distance is not None:
            self.__distance.draw(4)
        self.__button.grid(column=0, row=5, columnspan=3, pady=(5, 0))
        self.__object.pack(pady=(0, 20))

    def hide(self):
        self.__v0.hide()
        if self.__alpha is not None:
            self.__alpha.hide()
        self.__time.hide()
        self.__height.hide()
        if self.__distance is not None:
            self.__distance.hide()
        self.__button.grid_remove()
        self.__object.pack_forget()


class Buttons:
    """Class of buttons for interaction with app"""

    def __init__(self, window):
        self.__object = tk.Frame(window)  # Frame for buttons
        self.__calc_button = tk.Button(self.__object, text=text.calculate, font=style.Btn.font, width=18)
        self.__save_button = tk.Button(self.__object, text=text.save, font=style.Btn.font, width=18)
        self.__theory_button = tk.Button(self.__object, text=text.theory, font=style.Btn.font, width=18)

    def draw(self):
        self.__calc_button.pack(pady=5)
        self.__save_button.pack(pady=5)
        self.__theory_button.pack(pady=5)
        self.__object.pack(side=tk.BOTTOM)


class ParamRow:
    """Class of widgets of throw params"""

    def __init__(self, window, name, but=False):
        """
        :param name: text for label (title)
        :param but: create button or not
        """
        self._label = tk.Label(window, text=name, font="Arial 12")
        self._entry = tk.Entry(window)
        button = tk.Button(window, text="calc")
        self._button = (button if but else None)

    def draw(self, row):
        self._label.grid(column=0, row=row, padx=(0, 5), pady=5)
        self._entry.grid(column=1, row=row, padx=(0, 5), pady=5)
        if self._button is not None:
            self._button.grid(column=2, row=row, pady=5)

    def hide(self):
        self._label.grid_remove()
        self._entry.grid_remove()
        if self._button is not None:
            self._button.grid_remove()
