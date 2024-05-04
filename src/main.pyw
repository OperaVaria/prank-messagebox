"""
Prank messagebox app.
"""

# Imports:
import tkinter as tk
from tkinter import ttk
# from time import sleep
from modules_pmb.window_class import Window
from modules_pmb.container_class import Container


class GUI(ttk.Frame):
    def __init__(self, parent, window):
        super().__init__(parent)

        self.lbl_text = tk.StringVar(parent, "<a question you would rather say \"x\" to>")
        self.switched_flag = False

        parent.grid_rowconfigure(0, weight=2)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_columnconfigure(1, weight=1)

        self.lbl_main = ttk.Label(parent, textvariable=self.lbl_text,
                                  anchor="center", justify="center")
        self.lbl_main.grid(row=0, column=0, columnspan=2)

        self.btn_left = ttk.Button(parent, text="x (desired)",
                                   command=self.press_yes)
        self.btn_left.grid(row=1, column=0)

        self.btn_right = ttk.Button(parent, text="y (forced)",
                                    command=self.press_no)
        self.btn_right.grid(row=1, column=1)
        self.btn_left.bind("<Enter>", self.switch_buttons)

        self.btn_exit = ttk.Button(parent, text="Exit", command=lambda: window.destroy())

    def switch_buttons(self, event):
        # sleep(0.13) - Optionally you can make it just barely possible.
        if not self.switched_flag:
            self.btn_left.grid(row=1, column=1)
            self.btn_right.grid(row=1, column=0)
            self.switched_flag = not self.switched_flag
        elif self.switched_flag:
            self.btn_left.grid(row=1, column=0)
            self.btn_right.grid(row=1, column=1)
            self.switched_flag = not self.switched_flag
        return event

    def press_yes(self):
        self.lbl_text.set("<got me>")
        set_exit(self)
        return

    def press_no(self):
        self.lbl_text.set("<got im>")
        set_exit(self)
        return


def set_exit(gui):
    gui.btn_left.destroy()
    gui.btn_right.destroy()
    gui.btn_exit.grid(row=1, column=0, columnspan=2)
    return


if __name__ == "__main__":
    wdw_main = Window("Question", "400x200", False, False,
                      "#1F2933", False)
    frm_main = Container(wdw_main, 400, 200, "both", True, "#1F2933",
                         "#E4E7EB", "#151C23", "Calibri")
    gui_main = GUI(frm_main.cont, wdw_main)
    wdw_main.mainloop()
