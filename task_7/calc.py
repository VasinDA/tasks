import tkinter as tk
import tkinter.ttk as ttk

class CalculatorAPP(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title = 'Calculator'
        self.create_widgets()
        self.pack(padx=10, pady=10, ipadx=10)