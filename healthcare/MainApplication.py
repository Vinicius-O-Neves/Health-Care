from tkinter import *
from tkinter import ttk

from healthcare.ui.imccalculator.BmiCalculatorScreen import BMICalculatorScreen


class MainApplication:

    def __int__(self):
        self.w = Tk()
        self.w.title("Health Care")
        self.app_width = 386
        self.app_height = 680
        self.screen_width = self.w.winfo_screenwidth()
        self.screen_height = self.w.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.app_width / 2)
        self.y = (self.screen_height / 2) - (self.app_height / 2) - 30
        self.w.geometry(f'{self.app_width}x{self.app_height}+{int(self.x)}+{int(self.y)}')
        self.w.maxsize(self.app_width, self.app_height)
        self.w.minsize(self.app_width, self.app_height)

        tabControl = ttk.Notebook(self.w)
        tabControl.place(x=0, y=0, width=self.app_width, height=self.app_height)

        bmiCalculatorScreen = BMICalculatorScreen(tabControl).w
        frame2 = Frame(tabControl)
        frame2.pack(fill="both", expand=1)
        tabControl.add(bmiCalculatorScreen, text="IMC Calculator")
        tabControl.add(frame2, text="Calorias Calculator")

        self.w.mainloop()
