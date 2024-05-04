"""
window_class.py

Tkinter GUI window as a class.

Part of the "Prank Messagebox" project.

By OperaVaria, 2024.
"""

# Tkinter import:
import tkinter as tk
from platform import system


class Window(tk.Tk):
    """Tkinter GUI window as a Python class.
       General purpose, multi-platform."""

    def __init__(self, title, geometry, resizable_x, resizable_y, background, start_maximized):
        """Creates a window object."""
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable_x, resizable_y)
        self["bg"] = background
        # Maximized settings.
        if start_maximized and system() in ("Windows", "Darwin"):
            self.state("zoomed")  # On Windows and Mac, start with maximized window.
        elif start_maximized and system() == "Linux":
            self.state("normal")  # On Linux, start "normal" (no "zoomed" mode available).


# Display message when accidentally run:
if __name__ == "__main__":
    print("This file is an importable module and cannot be run.")
