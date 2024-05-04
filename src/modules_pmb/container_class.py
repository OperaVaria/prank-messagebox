"""
container_class.py

Tkinter.ttk GUI container frame as a class.

By OperaVaria, 2024.
"""

# Built-in module imports:
from tkinter import ttk
from platform import system


class Container(ttk.Frame):
    """Ttk GUI container as a Python class.
       General purpose, multi-platform."""
    def __init__(self, window, width, height, fill, expand, background,
                 foreground, textcolor, font):
        """Creates a container (frame) object, placed into parent window."""
        super().__init__(window)
        self.cont = ttk.Frame(window, width=width, height=height)
        self.cont.pack(fill=fill, expand=expand)
        # Set ttk style:
        self.style = ttk.Style(self)
        # Ttk theme selection for different OSs:
        if system() == "Windows":
            self.style.theme_use("vista")
        elif system() == "Linux":
            self.style.theme_use("clam")
        elif system() == "Darwin":
            self.style.theme_use("aqua")
        # Ttk style configuration for application widgets:
        self.style.configure("TFrame", background=background)
        self.style.configure("TLabel", background=background, foreground=foreground,
                             font=(font, 14, "bold"))
        # Button setting for different themes:
        if self.style.theme_use() in ("vista", "aqua"):
            self.style.configure("TButton",  background=background, foreground=textcolor,
                                 font=(font, 16, "bold"), width=10, height=5, padding=10)
        elif self.style.theme_use() == "clam":
            self.style.configure("TButton",  background=foreground, foreground=textcolor,
                                 font=(font, 12, "bold"), width=10, height=5, padding=10)


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is an importable module and cannot be run.")
