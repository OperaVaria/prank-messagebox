"""
Prank messagebox app.

A simple Python TTk application where a yes or no option is forced on the user
for comedic effect.
"""

# Metadata variables:
__author__ = "OperaVaria"
__contact__ = "lcs_it@proton.me"
__version__ = "1.0.0"
__date__ = "2024.05.04"

# Licence:
__license__ = "GPLv3"
__copyright__ = "Copyright © 2024, Csaba Latosinszky"

"""
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>
"""

# Imports:
import tkinter as tk
from tkinter import ttk
# from time import sleep
from modules_pmb.window_class import Window
from modules_pmb.container_class import Container

# Strings to insert into the messagebox:
QUESTION = "Placeholder question"
OPTION_OTHER = "A"
OPTION_FORCED = "B (forced)"
RESPONSE_OTHER = "Got me!"
RESPONSE_FORCED = "Got im!"


class GUI(ttk.Frame):
    """Messagebox GUI contents as OOP-style class."""

    def __init__(self, parent, window):
        """Create grid and widgets."""
        super().__init__(parent)

        # GUI variables.
        self.lbl_text = tk.StringVar(parent, QUESTION)
        self.switched_flag = False

        # Grid structure.
        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        # Widgets.
        self.lbl_main = ttk.Label(parent, textvariable=self.lbl_text,
                                  anchor="center", justify="center")
        self.lbl_main.grid(row=0, column=0, columnspan=2)

        self.btn_left = ttk.Button(parent, text=OPTION_OTHER,
                                   command=self.press_other)
        self.btn_left.grid(row=1, column=0)

        self.btn_right = ttk.Button(parent, text=OPTION_FORCED,
                                    command=self.press_forced)
        self.btn_right.grid(row=1, column=1)

        self.btn_exit = ttk.Button(parent, text="Exit",
                                   command=window.destroy)

        # Bind cursor entrance to switch method.
        self.btn_left.bind("<Enter>", self.switch_buttons)


    def switch_buttons(self, event):
        """Method to swap buttons according to flag state."""

        # sleep(0.13) - Optionally you can make it just barely possible.
        # Also uncomment sleep import

        if not self.switched_flag:
            self.btn_left.grid(row=1, column=1)
            self.btn_right.grid(row=1, column=0)
            self.switched_flag = not self.switched_flag
        elif self.switched_flag:
            self.btn_left.grid(row=1, column=0)
            self.btn_right.grid(row=1, column=1)
            self.switched_flag = not self.switched_flag
        return event

    def press_other(self):
        """Actions when other option is pressed."""
        # Set label.
        self.lbl_text.set(RESPONSE_OTHER)
        # Call final state setup function.
        set_exit(self)
        return

    def press_forced(self):
        """Actions when forced option is pressed."""
        # Set label.
        self.lbl_text.set(RESPONSE_FORCED)
        # Call final state setup function.
        set_exit(self)
        return


def set_exit(gui):
    """Function to set up final state."""
    gui.btn_left.destroy()
    gui.btn_right.destroy()
    gui.btn_exit.grid(row=1, column=0, columnspan=2)
    return


# Launch app:
if __name__ == "__main__":
    wdw_main = Window("Question", "400x200", False, False,
                      "#1F2933", False)
    frm_main = Container(wdw_main, 400, 200, "both", True, "#1F2933",
                         "#E4E7EB", "#151C23", "Calibri")
    gui_main = GUI(frm_main.cont, wdw_main)
    wdw_main.mainloop()
