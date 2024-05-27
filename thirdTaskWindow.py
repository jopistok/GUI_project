from tkinter import Tk, Label, Button, Toplevel
from tkinter import ttk
import linal_3 as solver
import numpy as np

class TrirdTaskSizeApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Решение СЛАУ")
        self.geometry("320x240")
        self.resizable(False,False)

        self.ErrorState = False

        for c in range(3): self.columnconfigure(index=c, weight=1)
        for r in range(4): self.rowconfigure(index=r, weight=1)

        Label(self, text="Решение СЛАУ", font=("GOST type b", 20, "italic")).grid(row=0,column=0,columnspan=3,sticky="NSEW")
        Label(self, text="Введите размер матрицы", font=("GOST type b", 15, "italic")).grid(row=1,column=0,columnspan=3,sticky="NSEW")

        self.Entries = [ttk.Entry(self, width=5) for i in range(2)]

        self.Entries[0].grid(row=2,column=0)
        Label(self, text="X", font=("GOST type b", 15, "italic")).grid(row=2,column=1,sticky="NSEW")
        self.Entries[1].grid(row=2,column=2)

        Button(self, text="Готово", font=("GOST type b", 15, "italic"), command=lambda:self.makeInputWindow()).grid(row=3,column=1)

    def switchErrorState(self):
        self.ErrorState = not self.ErrorState
        return

    def callWarningWindow(self):
        if (self.ErrorState):
            return
        self.switchErrorState()
        def warningDestroy(window):
            self.switchErrorState()
            window.destroy()
        warning = Toplevel(self)
        warning.title("Ошибка")
        warning.geometry("160x60")
        warning.resizable(False, False)
        warning.protocol("WM_DELETE_WINDOW", lambda: warningDestroy(warning))
        Label(warning, text="Ошибка ввода данных", font=("GOST type b", 12, "italic")).grid(row=0, column=0)
        Button(warning, text="Изменить данные", font=("GOST type b", 12, "italic"), command=lambda: warningDestroy(warning)).grid(row=1, column=0)
        return

    def closeWindow(self, window):
        self.deiconify()
        window.destroy()
        return
    
    def makeInputWindow(self):
        def readInput(value):
            try:
                if int(value, base=10) > 0:
                    return int(value, base=10)
                else:
                    raise ValueError
            except ValueError:
                self.callWarningWindow()
                return None
        self.size = [readInput(self.Entries[0].get()), readInput(self.Entries[1].get())]

        window = TrirdTaskInputApp(self)
        self.withdraw()
        window.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(window))

    
        window.size = self.size

        window.update()
        
        return


        
class TrirdTaskInputApp(Toplevel):
    def __init__(self, size, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Решение СЛАУ")
        self.geometry("640x480")
        self.resizable(True,True)

        self.size = None

        self.ErrorState = False

        return

    def switchErrorState(self):
        self.ErrorState = not self.ErrorState
        return

    def callWarningWindow(self):
        if (self.ErrorState):
            return
        self.switchErrorState()
        def warningDestroy(window):
            self.switchErrorState()
            window.destroy()
        warning = Toplevel(self)
        warning.title("Ошибка")
        warning.geometry("160x60")
        warning.resizable(False, False)
        warning.protocol("WM_DELETE_WINDOW", lambda: warningDestroy(warning))
        Label(warning, text="Ошибка ввода данных", font=("GOST type b", 12, "italic")).grid(row=0, column=0, sticky="NSEW")
        Button(warning, text="Изменить данные", font=("GOST type b", 12, "italic"), command=lambda: warningDestroy(warning)).grid(row=1, column=0)
        return

    def update(self):
        
        size = self.size

        Label(self, text="Введите коэффициенты СЛАУ", font=("GOST type b", 18, "italic")).grid(row=0, column=0, columnspan=size[1]*2+2, sticky="NSEW")
        
        for c in range(size[1]*2+2): self.columnconfigure(index=c, weight=1)
        for r in range(size[0]+2): self.rowconfigure(index=r, weight=1)
        
        LabelsVariables = [[Label(self, text=f'x{i+1}', font=("GOST type b", 12, "italic")) for i in range(size[1])] for  j in range(size[0])]
        
        LabelsEquals = [Label(self, text='=', font=("GOST type b", 12, "italic")) for i in range(size[0])]

        self.EntriesMatrixList = [[ttk.Entry(self, width = 5) for i in range(size[1])] for j in range(size[0])]

        self.FreeMatrixList = [ttk.Entry(self, width = 5) for i in range(size[0])]

        for i in range(0, size[0]):
            for j in range(0, size[1]):
                if j != size[1]-1:
                    LabelsVariables[i][j]["text"] = str(LabelsVariables[i][j]["text"]) + '\t+'
                self.EntriesMatrixList[i][j].grid(row=i+1, column=2*j)
                LabelsVariables[i][j].grid(row=i+1, column=2*j+1, sticky="NSEW")
        for i in range(0, size[0]):
            LabelsEquals[i].grid(row=i+1, column=2*j+2, sticky="NSEW")
            self.FreeMatrixList[i].grid(row=i+1, column=2*j+3)

        Button(self, text = "Решить", font=("GOST type b", 20, "italic"), command = lambda: self.solve()).grid(row=i+2, column=0, columnspan=size[1]*2+2)
        
        return

    def closeWindow(self, window):
        self.deiconify()
        window.destroy()
        return

    def solve(self):

        def readInput(value):
            try:
                return float(value)
            except ValueError:
                if self.ErrorState == False:
                    self.callWarningWindow()
                return None

        A = np.array([[readInput(self.EntriesMatrixList[i][j].get()) for j in range(len(self.EntriesMatrixList[i]))] for i in range(len(self.EntriesMatrixList))], float)
        B = np.array([[readInput(self.FreeMatrixList[i].get()) for i in range(len(self.FreeMatrixList))]], float).T

        answer = solver.solve(A, B)
        
        self.withdraw()

        window = TrirdTaskOutputApp(self)
        window.update(answer)
        window.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(window))
        pass

        
        
            

class TrirdTaskOutputApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Решение СЛАУ")
        self.geometry("640x480")
        self.resizable(True,True)

        for c in range(2): self.columnconfigure(index=c, weight=1)
        for r in range(3): self.rowconfigure(index=r, weight=1)
        
        Label(self, text = "Решение СЛАУ", font=("GOST type b", 20, "italic")).grid(row=0,column=0, columnspan=2, sticky="NSEW")
        

    def update(self, answer):
        if answer == -1:
            Label(self, text = "К сожалению, СЛАУ несовместна,\nрешений не существует", font=("GOST type b", 20, "italic")).grid(row=1,column=0, columnspan=2, rowspan=2, sticky="NSEW")
        elif answer[-1]:
            Label(self, text = "СЛАУ совместна, имеет одно решение:", font=("GOST type b", 20, "italic")).grid(row=1,column=0, columnspan=2, sticky="NSEW")
            output = str(answer[0])
            while output.count('  ') != 0:
                output = output.replace('  ', ' ')
            Label(self, text = "X = " + output.replace(' ', '; '), font=("GOST type b", 20, "italic")).grid(row=2,column=0, columnspan=2, sticky="NSEW")
        else:
            Label(self, text = "СЛАУ совместна, имеет бесконечно много \nрешений, вот одно из них", font=("GOST type b", 20, "italic")).grid(row=1,column=0, columnspan=2, sticky="NSEW")
            output = str(answer[0])
            while output.count('  ') != 0:
                output = output.replace('  ', ' ')
            Label(self, text = "X = " + output.replace(' ', '; '), font=("GOST type b", 20, "italic")).grid(row=2,column=0, columnspan=2, sticky="NSEW")
            for r in range(4+len(answer[1])): self.rowconfigure(index=r, weight=1)
            Label(self, text = "Фундаментальная система решений СЛАУ:", font=("GOST type b", 20, "italic")).grid(row=3,column=0, columnspan=2, sticky="NSEW")
            for i in range(len(answer[1])):
                output = str(answer[1][i])
                while output.count('  ') != 0:
                    output = output.replace('  ', ' ')
                Label(self, text = output.replace(' ', '; '), font=("GOST type b", 20, "italic")).grid(row=4+i,column=0, columnspan=2, sticky="NSEW")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window = TrirdTaskSizeApp(root)
    root.mainloop()
