# Main application's code

import tkinter as tk

from calculate import horizontal_mode as calc_horizontal
from calculate import vertical_mode as calc_vertical
from widgets import DrawingField, Menu
from windowsParameters import WindowParams


class MainWindow(tk.Tk):
    """Application's main window"""

    def __init__(self):
        super().__init__()
        self.parameters = WindowParams(title="Abandoned body's trajectory simulation",
                                       width=740, height=475)
        self.title(self.parameters.title)
        self.geometry(self.parameters.geometry())
        self.resizable(*self.parameters.resizable)
        try:
            self.iconbitmap(self.parameters.ico_path)
        except tk.TclError:  # Icon display error
            pass  # Default Tkinter's icon

        self.__drawing_field = DrawingField(self)
        self.__settings = Menu(self,
                               vertical_func=calc_vertical,
                               horizontal_func=calc_horizontal)

    def run(self):
        """Launching the app"""
        self.__drawing_field.draw()
        self.__settings.draw()
        self.mainloop()


window = MainWindow()
window.run()
