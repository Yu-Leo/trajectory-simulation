# File with widget's classes

import tkinter as tk
from tkinter.ttk import Combobox

from PIL import Image as PilImage
from PIL import ImageTk

import config
import constants as const
import style
import text
from windowsParameters import DrawingFieldParams, SizeParams


class DrawingField(tk.Canvas):
    """Field for simulation"""

    def __init__(self, window):
        self.__parameters = DrawingFieldParams(bg="white",
                                               width=500,
                                               height=430,
                                               padx=10,
                                               pady=10)
        super().__init__(window, bg=self.__parameters.bg,
                         width=self.__parameters.width,
                         height=self.__parameters.height)

    def draw(self):
        self.pack(side=tk.LEFT,
                  padx=self.__parameters.padx,
                  pady=self.__parameters.pady)


class Menu(tk.Frame):
    """Frame with simulation's menu"""

    def __init__(self, window, vertical_func):
        super().__init__(window)
        self.__parameters = SizeParams(None, None, padx=(0, 15), pady=10)
        self.__vertical_func = vertical_func  # Function, which called to calculation in vertical mode
        self.__throw_type = ThrowType(self, change_func=self.change_throw_params_list)
        self.__throw_params = ThrowParams(self, config.trow_type, self.__vertical_func)
        self.__buttons = Buttons(self)

    def draw(self):
        self.__throw_type.draw()
        self.__throw_params.draw()
        self.__buttons.draw()

        self.pack(side=tk.RIGHT,
                  padx=self.__parameters.padx,
                  pady=self.__parameters.pady,
                  fill=tk.Y)

    def change_throw_params_list(self, throw_type):
        self.__throw_params.hide()
        self.__throw_params = ThrowParams(self, throw_type, self.__vertical_func)
        self.__throw_params.draw()


class ThrowType(tk.Frame):
    """Class of widget, which chose the throw type"""

    def __init__(self, window, change_func):
        super().__init__(window)
        self.__label = tk.Label(self, text=text.throw_type_title, font=(style.font_name, 12))
        self.__menu = Combobox(self, values=text.throw_types, state="readonly", width=22)
        self.__menu.current(config.trow_type)  # Default value
        self.__menu.bind("<<ComboboxSelected>>", lambda event: change_func(self.__menu.current()))

    def draw(self):
        self.__label.pack(pady=5)
        self.__menu.pack()
        self.pack(side=tk.TOP, anchor=tk.N, pady=15)


class ThrowParams(tk.Frame):
    """Class of widgets, which set throw parameters"""

    def __init__(self, window, throw_type, vertical_func):
        super().__init__(window)
        if throw_type == const.TrowType.VERTICAL:
            calc_func = vertical_func
        else:
            calc_func = lambda: None
        ParamRow.set_functions(upd_kit=self.update_config_kit,
                               upd_entries=self.update_entries,
                               calc=calc_func)

        self.__v0 = ParamRow(self, text.v0, but=True)
        need_alpha = throw_type == const.TrowType.ALPHA
        need_distance = throw_type in (const.TrowType.ALPHA, const.TrowType.HORIZONTAL)
        self.__alpha = ParamRow(self, text.alpha, but=True) if need_alpha else None
        self.__time = ParamRow(self, text.time, but=True)
        self.__height = ParamRow(self, text.height, but=True)
        self.__distance = ParamRow(self, text.distance, but=True) if need_distance else None

        self.__button = tk.Button(self, text=text.read_from_file, font=(style.font_name, 10), width=18)

    def draw(self):
        self.__v0.draw(0)
        if self.__alpha is not None:
            self.__alpha.draw(1)
        self.__time.draw(2)
        self.__height.draw(3)
        if self.__distance is not None:
            self.__distance.draw(4)
        self.__button.grid(column=0, row=5, columnspan=3, pady=(5, 0))
        self.pack()

    def hide(self):
        self.__v0.hide()
        if self.__alpha is not None:
            self.__alpha.hide()
        self.__time.hide()
        self.__height.hide()
        if self.__distance is not None:
            self.__distance.hide()
        self.__button.grid_remove()
        self.pack_forget()

    def update_config_kit(self):
        """Set values from entries to config kit"""
        config.kit.v0 = self.__get_value_of(self.__v0)
        config.kit.alpha = self.__get_value_of(self.__alpha)
        config.kit.time = self.__get_value_of(self.__time)
        config.kit.height = self.__get_value_of(self.__height)
        config.kit.distance = self.__get_value_of(self.__distance)

    def update_entries(self):
        """Set values from config kit to entries"""
        self.__set_value_to(config.kit.v0, self.__v0)
        self.__set_value_to(config.kit.alpha, self.__alpha)
        self.__set_value_to(config.kit.time, self.__time)
        self.__set_value_to(config.kit.height, self.__height)
        self.__set_value_to(config.kit.distance, self.__distance)

    @staticmethod
    def __get_value_of(field):
        """Return value on field if field is exists"""
        if field is not None:
            return field.get_value()
        return ""

    @staticmethod
    def __set_value_to(value, field):
        """Set value to field if field is exists"""
        if field is not None:
            field.set_value(value)


class Buttons(tk.Frame):
    """Class of buttons for interaction with app"""

    def __init__(self, window):
        super().__init__(window)
        self.__calc_button = tk.Button(self, text=text.calculate, font=style.Btn.font, width=18)
        self.__save_button = tk.Button(self, text=text.save, font=style.Btn.font, width=18)
        self.__theory_button = tk.Button(self, text=text.theory, font=style.Btn.font, width=18)

    def draw(self):
        self.__calc_button.pack(pady=5)
        self.__save_button.pack(pady=5)
        self.__theory_button.pack(pady=5)
        self.pack(side=tk.BOTTOM)


class ParamRow:
    """Class of widgets of throw params"""
    update_kit_func = None
    update_entries_func = None
    calc_func = None

    @classmethod
    def set_functions(cls, upd_kit, upd_entries, calc):
        """Define functions for actions after click button"""
        cls.update_kit_func = upd_kit
        cls.update_entries_func = upd_entries
        cls.calc_func = calc

    @staticmethod
    def __get_image():
        try:
            image = PilImage.open(f"img/calc_icon32.ico")
            image = image.resize((18, 18), PilImage.ANTIALIAS)
            return ImageTk.PhotoImage(image)
        except FileNotFoundError:
            return None

    @staticmethod
    def __call_calc(i):
        """Change calculate mode, update config kit and and call calculate_func"""
        config.calculate_mode = i
        ParamRow.update_kit_func()
        ParamRow.calc_func()
        ParamRow.update_entries_func()

    def __init__(self, window, name, but=False):
        """
        :param name: text for label (title)
        :param but: create button or not
        """
        self.__name = name
        self._label = tk.Label(window, text=self.__name, font=(style.font_name, 12))
        self._entry = tk.Entry(window, font=(style.font_name, 12), width=12)
        calc_image = ParamRow.__get_image()

        button = tk.Button(window,
                           image=calc_image,
                           command=self.__operation)
        button.image = calc_image

        self._button = (button if but else None)

    def draw(self, row):
        self._label.grid(column=0, row=row, padx=(0, 5), pady=6)
        self._entry.grid(column=1, row=row, padx=(0, 5), pady=6)
        if self._button is not None:
            self._button.grid(column=2, row=row, pady=(0, 6), padx=(5, 0))

    def hide(self):
        self._label.grid_remove()
        self._entry.grid_remove()
        if self._button is not None:
            self._button.grid_remove()

    def __operation(self):
        """Actions to be performed after clicking"""
        calc_mode = {text.v0: const.Modes.V0,
                     text.height: const.Modes.HEIGHT,
                     text.time: const.Modes.TIME}.get(self.__name, "ERROR")
        ParamRow.__call_calc(calc_mode)

    def get_value(self):
        """Return entry's value"""
        return str(self._entry.get())

    def set_value(self, value):
        """Set value to the entry"""
        self._entry.delete(0, tk.END)
        self._entry.insert(0, str(value))
