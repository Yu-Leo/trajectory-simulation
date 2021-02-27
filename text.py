# File with phrases, witch used in interface

import constants as const

throw_type_title = "Тип броска"

throw_types = ("Вертикально",
               "Горизонтально",
               "Под углом к горизонту")

read_from_file = "Считать из файла"
clear = "Очистить"
calculate = "Расчёт"
save = "Сохранить"
theory = "Теория"

modes = {
    const.Modes.V0: "V0",
    const.Modes.ALPHA: "a",
    const.Modes.TIME: "T",
    const.Modes.HEIGHT: "H",
    const.Modes.DISTANCE: "D",
}

number_only = "В данное поле необходимо ввести число."
range_exceeding = "В данное поле можно ввести только положительное число."

units = ["м/с", "рад", "с", "м"]

incorrect = "Некорректные данные"
impossible = "Бросок с данными параметрами невозможен"


def error_in_field(field):
    return f'Ошибка в поле "{field}".'


class ExceptionTexts:
    def __init__(self, field_name="", type_error=number_only, range_error=range_exceeding):
        self.title = error_in_field(field_name)
        self.type_error = type_error
        self.range_error = range_error


def exception_text(index):
    return ExceptionTexts(field_name=modes[index])
