# File with phrases, witch used in interface

import constants as const

throw_type_title = "Тип броска"

throw_types = ("Вертикально",
               "Горизонтально",
               "Под углом к горизонту")

read_from_file = "Считать из файла"
calculate = "Расчёт"
save = "Сохранить"
theory = "Теория"

v0 = "V0"
alpha = "a"
time = "T"
height = "H"
distance = "D"

number_only = "В данное поле можно ввести только число."
range_exceeding = "В данное поле можно ввести только положительное число."


def error_in_field(field):
    return f'Ошибка в поле "{field}".'


class ExceptionTexts:
    def __init__(self, field_name="", type_error=number_only, range_error=range_exceeding):
        self.title = error_in_field(field_name)
        self.type_error = type_error
        self.range_error = range_error


exceptions_dict = {const.Modes.V0: ExceptionTexts(v0),
                   const.Modes.ALPHA: ExceptionTexts(alpha),
                   const.Modes.TIME: ExceptionTexts(time),
                   const.Modes.HEIGHT: ExceptionTexts(height),
                   const.Modes.DISTANCE: ExceptionTexts(distance)}
