import tkinter
import tkinter.ttk
import tkinter.messagebox

class CalculatorAPP(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Calculator')
        self.master.resizable(False, False)
        self.expression = ''
        self.style = tkinter.ttk.Style(master)
        self.style.theme_use('clam')
        self.create_widgets()
                 
    def create_widgets(self):
        self.digit1_ent = tkinter.ttk.Entry(width=10)
        self.digit2_ent = tkinter.ttk.Entry(width=10)
        self.equal_lbl = tkinter.ttk.Label(text = '=')
        self.result_lbl = tkinter.ttk.Label()
        self.add_btn = tkinter.ttk.Button(text = '+', command=lambda: self.getResault('+'), width=10)
        self.sbt_btn = tkinter.ttk.Button(text = '-', command=lambda: self.getResault('-'), width=10)
        self.multi_btn = tkinter.ttk.Button(text = '*', command=lambda: self.getResault('*'), width=10)
        self.sub_btn = tkinter.ttk.Button(text = '/', command=lambda: self.getResault('/'), width=10)
        self.clear_btn = tkinter.ttk.Button(text='Clear', command=self.clearCalc, width=10)

        self.digit1_ent.grid(row=0, column=0, padx=5, pady=5)
        self.digit2_ent.grid(row=0, column=1, padx=5, pady=5)
        self.equal_lbl.grid(row=0, column=2, padx=5, pady=5)
        self.result_lbl.grid(row=0, column=3, padx=5, pady=5)
        self.add_btn.grid(row=1, column=0, padx=5, pady=5)
        self.sbt_btn.grid(row=1, column=1, padx=5, pady=5)
        self.multi_btn.grid(row=1, column=2, padx=5, pady=5)
        self.sub_btn.grid(row=1, column=3, padx=5, pady=5)
        self.clear_btn.grid(row=2, column=0, padx=5, pady=5)

    def getResault(self, operation):
        self.expression = self.digit1_ent.get() + operation + self.digit2_ent.get()
        try:
            resault = round(eval(self.expression), 4)
            self.result_lbl['text'] = resault
            tkinter.messagebox.showinfo('Answer', f'{resault}')
            self.expression = ''
        except:
            self.result_lbl['text'] = 'Error'
            tkinter.messagebox.showinfo('Answer', 'Error')
            self.expression = ''

    def clearCalc(self):
        self.digit1_ent.delete(0, tkinter.END)
        self.digit2_ent.delete(0, tkinter.END)
        self.result_lbl['text'] = self.expression

root = tkinter.Tk()
app = CalculatorAPP(master=root)
root.mainloop()