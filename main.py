# Main application's code

import tkinter as tk

from windowParameters import WindowParameters


class MainWindow:
    """Application's main window"""

    def __init__(self):
        self.__root = tk.Tk()
        self.__parameters = WindowParameters(title="Abandoned body's flight path simulation",
                                             width=800,
                                             height=500)
        self.__root.title(self.__parameters.title)
        self.__root.geometry(self.__parameters.geometry())
        self.__root.resizable(*self.__parameters.resizable)
        try:
            self.__root.iconbitmap(self.__parameters.ico_path)
        except tk.TclError:  # Icon display error
            pass  # Default Tkinter's icon

    def run(self):
        """Launching the app"""
        self.__root.mainloop()


window = MainWindow()
window.run()
