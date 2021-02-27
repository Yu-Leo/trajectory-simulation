# File with constants

from math import pi


class ThrowType:
    VERTICAL = 0
    HORIZONTAL = 1
    ALPHA = 2

    DEFAULT = VERTICAL


class Modes:
    V0 = 0
    ALPHA = 1
    TIME = 2
    HEIGHT = 3
    DISTANCE = 4

    DEFAULT = TIME


G = 9.8  # Gravitational acceleration

MAX_ALPHA = pi / 2


class Theory:
    url_vertical = "http://ru.solverbook.com/spravochnik/mexanika/kinematika/uskorenie-svobodnogo-padeniya/"
    url_horizontal = "http://ru.solverbook.com/spravochnik/mexanika/kinematika/dvizhenie-tela-broshennogo-gorizontalno/"
    url_alpha = "http://ru.solverbook.com/spravochnik/mexanika/kinematika/dvizhenie-tela-broshennogo-pod-uglom-k-gorizontu/"
