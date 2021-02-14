# File with widget's classes

import tkinter as tk
from tkinter.ttk import Combobox

import config
import constants as const
import exceptions as exc
import style
import text
from messageboxes import ExceptionMb
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

    @staticmethod
    def __get_value_of(field):
        """Return value on field if it's exists"""
        if field is not None:
            return field.get_value()
        return ""

    @staticmethod
    def __set_value_to(value, field):
        """Set value to field if it's exists"""
        if field is not None:
            field.set_value(value)

    @staticmethod
    def __clear(field):
        """Clear field if it's exists"""
        if field is not None:
            field.clear()

    def __init__(self, window, throw_type, vertical_func):
        super().__init__(window)
        if throw_type == const.TrowType.VERTICAL:
            calc_func = vertical_func
        else:
            calc_func = lambda: None
        ParamRow.set_functions(upd_kit=self.update_config_kit,
                               upd_entries=self.update_entries,
                               clr_entries=self.clear_entries,
                               calc=calc_func)
        def_val = config.calculate_mode

        self.__calculate_mode = tk.IntVar(value=def_val)  # Radiobuttons values controller

        self.__v0 = ParamRow(self, const.Modes.V0,
                             variable=self.__calculate_mode)
        need_alpha = throw_type == const.TrowType.ALPHA
        need_distance = throw_type in (const.TrowType.ALPHA, const.TrowType.HORIZONTAL)
        self.__alpha = ParamRow(self, const.Modes.ALPHA,
                                variable=self.__calculate_mode) if need_alpha else None
        self.__time = ParamRow(self, const.Modes.TIME,
                               variable=self.__calculate_mode)
        self.__height = ParamRow(self, const.Modes.HEIGHT,
                                 variable=self.__calculate_mode)
        self.__distance = ParamRow(self, const.Modes.DISTANCE,
                                   variable=self.__calculate_mode) if need_distance else None

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

    def __get_entries_dict(self):
        """Generate dict from entries"""
        entries_dict = {text.v0: self.__get_value_of(self.__v0),
                        text.alpha: self.__get_value_of(self.__alpha),
                        text.time: self.__get_value_of(self.__time),
                        text.height: self.__get_value_of(self.__height),
                        text.distance: self.__get_value_of(self.__distance)}
        return entries_dict

    def update_config_kit(self):
        """Set values from entries to config kit"""
        kit_dict = self.__get_entries_dict()
        config.kit.set_params(kit_dict)

    def update_entries(self):
        """Set values from config kit to entries"""
        self.__set_value_to(config.kit.v0, self.__v0)
        self.__set_value_to(config.kit.alpha, self.__alpha)
        self.__set_value_to(config.kit.time, self.__time)
        self.__set_value_to(config.kit.height, self.__height)
        self.__set_value_to(config.kit.distance, self.__distance)

    def clear_entries(self):
        """Delete all from entries"""
        entries = (self.__v0, self.__alpha, self.__time, self.__height, self.__distance)
        for e in entries:
            if e is not None:
                e.clear()


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


def exceptions_tracker(func):
    def wrapper(*args):
        try:
            func(*args)
        except exc.EntryContentError as e:
            ExceptionMb(e).show()

    return wrapper


class ParamRow:
    """Class of widgets of throw params"""
    update_kit_func = None
    update_entries_func = None
    calc_func = None
    clear_entries_func = None

    @classmethod
    def set_functions(cls, upd_kit, upd_entries, clr_entries, calc):
        """Define functions for actions after click button"""
        cls.update_kit_func = upd_kit
        cls.update_entries_func = upd_entries
        cls.clear_entries_func = clr_entries
        cls.calc_func = calc

    def __change_mode(self):
        """Change calculate mode"""
        config.calculate_mode = self.__row_ind

    def __init__(self, window, row_ind, variable=None):
        """
        :param name: text for label (title)
        :param but: create button or not
        """
        self.__row_ind = row_ind
        self.__name = text.modes[self.__row_ind]
        self._label = tk.Label(window, text=self.__name, font=(style.font_name, 12))
        self._entry = tk.Entry(window, font=(style.font_name, 12), width=12)

        button = tk.Radiobutton(window,
                                variable=variable,
                                value=row_ind,
                                command=self.__change_mode)

        self._button = (None if variable is None else button)

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

    def get_value(self):
        """Return entry's value"""
        return str(self._entry.get())

    def set_value(self, value):
        """Set value to the entry"""
        self.clear()
        self._entry.insert(0, str(value))

    def clear(self):
        """Clear th entry"""
        self._entry.delete(0, tk.END)
