# Main application's code

import tkinter as tk

from calculate import vertical_mode as calc_vertical
from widgets import DrawingField, Menu
from windowsParameters import WindowParams


class MainWindow(tk.Tk):
    """Application's main window"""

    def __init__(self):
        super().__init__()
        parameters = WindowParams(title="Abandoned body's trajectory simulation",
                                  width=740, height=450)
        self.title(parameters.title)
        self.geometry(parameters.geometry())
        self.resizable(*parameters.resizable)
        try:
            self.iconbitmap(parameters.ico_path)
        except tk.TclError:  # Icon display error
            pass  # Default Tkinter's icon

        self.__drawing_field = DrawingField(self)
        self.__settings = Menu(self, vertical_func=calc_vertical)

    def run(self):
        """Launching the app"""
        self.__drawing_field.draw()
        self.__settings.draw()
        self.mainloop()


window = MainWindow()
window.run()
