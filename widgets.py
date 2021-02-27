# File with widget's classes

import tkinter as tk
from tkinter.ttk import Combobox

import config
import constants as const
import exceptions as exc
import operations
import style
import text
from messageboxes import ExceptionMb
from windowsParameters import DrawingFieldParams, SizeParams


class DrawingField(tk.Canvas):
    """Field for simulation"""

    def __init__(self, window):
        self.__parameters = DrawingFieldParams(bg="white",
                                               width=500,
                                               height=window.parameters.height,
                                               padx=10,
                                               pady=10)
        super().__init__(window, bg=self.__parameters.bg,
                         width=self.__parameters.width,
                         height=self.__parameters.height)

    def draw(self):
        self.pack(side=tk.LEFT,
                  padx=self.__parameters.padx,
                  pady=self.__parameters.pady)


def exceptions_tracker(func):
    def wrapper(*args):
        try:
            func(*args)
        except exc.EntryContentError as e:
            ExceptionMb(e).show()

    return wrapper


class Menu(tk.Frame):
    """Frame with simulation's menu"""

    def __init__(self, window, vertical_func, horizontal_func, alpha_func):
        super().__init__(window)
        self.__parameters = SizeParams(None, None, padx=(0, 15), pady=10)
        # Function, which called to calculation in vertical mode
        self.__vertical_func = vertical_func
        # Function, which called to calculation in horizontal mode
        self.__horizontal_func = horizontal_func
        # Function, which called to calculation in alpha mode
        self.__alpha_func = alpha_func
        self.__throw_type = ThrowType(self,
                                      change_func=self.change_throw_params_list)
        self.__throw_params = ThrowParams(self, config.throw_type)
        self.__buttons = Buttons(self,
                                 clear_func=self.clear,
                                 enter_func=self.enter,
                                 theory_func=operations.open_theory)

    def draw(self):
        self.__throw_type.draw()
        self.__throw_params.draw()
        self.__buttons.draw()

        self.pack(side=tk.RIGHT,
                  padx=self.__parameters.padx,
                  pady=self.__parameters.pady,
                  fill=tk.Y)

    def change_throw_params_list(self, throw_type):
        config.throw_type = throw_type
        self.__throw_params.hide()
        self.__throw_params = ThrowParams(self, throw_type)
        self.__throw_params.draw()

    @exceptions_tracker
    def enter(self):
        if config.throw_type == const.ThrowType.VERTICAL:
            calc_func = self.__vertical_func
        elif config.throw_type == const.ThrowType.HORIZONTAL:
            calc_func = self.__horizontal_func
        elif config.throw_type == const.ThrowType.ALPHA:
            calc_func = self.__alpha_func
        else:
            raise ValueError("invalid value of config.throw_type")

        self.__throw_params.update_config_kit()
        calc_func()
        self.__throw_params.update_entries()

    def clear(self):
        self.__throw_params.clear_entries()



class ThrowType(tk.Frame):
    """Class of widget, which chose the throw type"""

    def __init__(self, window, change_func):
        super().__init__(window)
        self.__label = tk.Label(self, text=text.throw_type_title,
                                font=style.Label.font)
        self.__menu = Combobox(self, values=text.throw_types,
                               state="readonly",
                               width=20,
                               font=(style.font_name, 10))
        self.__menu.current(config.throw_type)  # Default value
        self.__menu.bind("<<ComboboxSelected>>",
                         lambda event: change_func(self.__menu.current()))

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
            value = "" if value is None else value
            field.set_value(value)

    @staticmethod
    def __clear(field):
        """Clear field if it's exists"""
        if field is not None:
            field.clear()

    def __init__(self, window, throw_type):
        super().__init__(window)

        def_val = config.calculate_mode
        self.__calculate_mode = tk.IntVar(value=def_val)  # Radiobutton's values controller

        if throw_type in (const.ThrowType.HORIZONTAL, const.ThrowType.ALPHA):
            var_for_v0 = None
        else:
            var_for_v0 = self.__calculate_mode

        var_for_distance = self.__calculate_mode if throw_type == const.ThrowType.HORIZONTAL else None

        self.__v0 = ParamRow(self, const.Modes.V0,
                             variable=var_for_v0)
        need_alpha = throw_type == const.ThrowType.ALPHA
        need_distance = throw_type in (const.ThrowType.ALPHA, const.ThrowType.HORIZONTAL)
        self.__alpha = ParamRow(self, const.Modes.ALPHA,
                                variable=self.__calculate_mode) if need_alpha else None
        self.__time = ParamRow(self, const.Modes.TIME,
                               variable=self.__calculate_mode)
        self.__height = ParamRow(self, const.Modes.HEIGHT,
                                 variable=self.__calculate_mode)
        self.__distance = ParamRow(self, const.Modes.DISTANCE,
                                   variable=var_for_distance) if need_distance else None

        self.__button = tk.Button(self,
                                  text=text.read_from_file,
                                  font=(style.font_name, 11),
                                  width=style.Btn.width - 3,
                                  bg=style.Btn.colors["read"],
                                  state=tk.DISABLED)

    def draw(self):
        self.__v0.draw(0)
        if self.__alpha is not None:
            self.__alpha.draw(1)
        self.__time.draw(2)
        self.__height.draw(3)
        if self.__distance is not None:
            self.__distance.draw(4)
        self.__button.grid(column=1, row=5, columnspan=2, pady=(5, 0), ipadx=3)
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
        """Generate dictionary from entries"""
        entries_dict = {const.Modes.V0: self.__get_value_of(self.__v0),
                        const.Modes.ALPHA: self.__get_value_of(self.__alpha),
                        const.Modes.TIME: self.__get_value_of(self.__time),
                        const.Modes.HEIGHT: self.__get_value_of(self.__height),
                        const.Modes.DISTANCE: self.__get_value_of(self.__distance)}
        return entries_dict

    def update_config_kit(self):
        """Set values from entries to config kit"""
        kit_dict = self.__get_entries_dict()
        config.kit.set_params(config.throw_type, config.calculate_mode, kit_dict)

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

    def __init__(self, window, clear_func, enter_func, theory_func):
        super().__init__(window)
        self.__clear_button = tk.Button(self,
                                        text=text.clear,
                                        font=style.Btn.font,
                                        width=style.Btn.width,
                                        bg=style.Btn.colors["clear"],
                                        command=clear_func)
        self.__enter_button = tk.Button(self,
                                        text=text.calculate,
                                        font=style.Btn.font,
                                        width=style.Btn.width,
                                        bg=style.Btn.colors["enter"],
                                        command=enter_func)
        self.__save_button = tk.Button(self,
                                       text=text.save,
                                       font=style.Btn.font,
                                       width=style.Btn.width,
                                       bg=style.Btn.colors["save"],
                                       state=tk.DISABLED)
        self.__theory_button = tk.Button(self,
                                         text=text.theory,
                                         font=style.Btn.font,
                                         width=style.Btn.width,
                                         bg=style.Btn.colors["theory"],
                                         command=theory_func)

    def draw(self):
        self.__clear_button.pack(pady=5)
        self.__enter_button.pack(pady=5)
        self.__save_button.pack(pady=5)
        self.__theory_button.pack(pady=5)
        self.pack(side=tk.BOTTOM)


class ParamRow:
    """Class of widgets of throw params"""

    def __change_mode(self):
        """Change calculate mode"""
        config.calculate_mode = self.__row_ind

    @staticmethod
    def __get_units_of_measurement(row_ind):
        """Return string with units of measurement"""
        if row_ind == const.Modes.V0:
            return text.units[0]
        elif row_ind == const.Modes.ALPHA:
            return text.units[1]
        elif row_ind == const.Modes.TIME:
            return text.units[2]
        elif row_ind in (const.Modes.HEIGHT, const.Modes.DISTANCE):
            return text.units[3]
        else:
            raise ValueError("Invalid value of row_ind")

    def __init__(self, window, row_ind, variable=None):
        self.__row_ind = row_ind
        self.__name = text.modes[self.__row_ind]
        self._label = tk.Label(window, text=self.__name, font=style.Label.font)
        self._entry = tk.Entry(window, font=style.Label.font, width=12)
        units = self.__get_units_of_measurement(self.__row_ind)
        self._units_of_measurement = tk.Label(window, text=units,
                                              font=style.Label.font)
        button = tk.Radiobutton(window,
                                variable=variable,
                                value=row_ind,
                                command=self.__change_mode)
        self._button = (None if variable is None else button)

    def draw(self, row):
        self._label.grid(column=0, row=row, padx=(0, 5), pady=6)
        self._entry.grid(column=1, row=row, padx=(0, 5), pady=6)
        self._units_of_measurement.grid(column=2, row=row, padx=(0, 5), pady=6)
        if self._button is not None:
            self._button.grid(column=3, row=row, pady=(0, 6), padx=(5, 0))

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
