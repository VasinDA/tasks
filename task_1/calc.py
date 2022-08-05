import tkinter as tk
import tkinter.ttk as ttk

class CalculatorAPP(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title = ('Calculator')
        self.master.resizable(False, False)
        self.create_widgets()
    
    def create_widgets(self):
        self.digit1_ent = ttk.Entry(width=10)
        self.digit2_ent = ttk.Entry(width=10)
        self.equal_lbl = tk.Label(text = '=')
        self.result_lbl = tk.Label()
        self.add_btn = ttk.Button(text = '+', width=10, command = self.getResault('+'))
        self.sbt_btn = ttk.Button(text = '-', width=10)
        self.multi_btn = ttk.Button(text = '*', width=10)
        self.sub_btn = ttk.Button(text = '/', width=10)

        self.digit1_ent.grid(row=0, column=0)
        self.digit2_ent.grid(row=0, column=1)
        self.equal_lbl.grid(row=0, column=2)
        self.result_lbl.grid(row=0, column=3)
        self.add_btn.grid(row=1, column=0)
        self.sbt_btn.grid(row=1, column=1)
        self.multi_btn.grid(row=1, column=2)
        self.sub_btn.grid(row=1, column=3)
    
    def getResault(self, operarion):
        num1 = self.digit1_ent
        num2 = self.digit2_ent
        match operarion:
            case '+':
                resault = num1 + num2
        self.result_lbl['text'] = resault


    

root = tk.Tk()
app = CalculatorAPP(master=root)
root.mainloop()