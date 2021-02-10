# File with widget's classes

import tkinter as tk

from windowsParameters import DrawingFieldParameters


class DrawingField:
    """Field for simulation"""

    def __init__(self, window):
        self.__parameters = DrawingFieldParameters(bg="white",
                                                   width=500,
                                                   height=400,
                                                   padx=10,
                                                   pady=10)

        self.__field = tk.Canvas(window, bg=self.__parameters.bg,
                                 width=self.__parameters.width,
                                 height=self.__parameters.height)

    def draw(self):
        self.__field.pack(side=tk.LEFT,
                          padx=self.__parameters.padx,
                          pady=self.__parameters.pady)
