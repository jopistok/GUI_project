from tkinter import Tk, Label, Button, Toplevel
from tkinter import ttk
import linal_1 as solver


class FirstTaskInputApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Задача №1")
        self.geometry("640x480")
        self.resizable(False,False)

        self.ErrorState = False

        nameLabel = Label(self, text="Задача №1", font=("GOST type b", 30, "italic"))

        vectors = ['i', 'j', 'k']

        for c in range(2): self.columnconfigure(index=c, weight=1)
        for r in range(6): self.rowconfigure(index=r, weight=1)
        
        firstVectorLabel = Label(self, text="Вектор е1", font=("GOST type b", 20, "italic"))
        firstAngleLabel = Label(self, text="Угол поворота(в градусах)", font=("GOST type b", 20, "italic"))
        firstCombobox = ttk.Combobox(self, values=vectors, state="readonly", font=("GOST type b", 16, "italic"), width=1)
        firstEntry = ttk.Entry(self)
        firstCombobox.set('i')
        
        
        secondVectorLabel = Label(self, text="Вектор е2", font=("GOST type b", 20, "italic"))
        secondAngleLabel = Label(self, text="Угол поворота(в градусах)", font=("GOST type b", 20, "italic"))
        secondCombobox = ttk.Combobox(self, values=vectors, state="readonly", font=("GOST type b", 16, "italic"), width=1)
        secondEntry = ttk.Entry(self)
        secondCombobox.set('i')

        solveButton = Button(self, text="Решить", font=("GOST type b", 20, "italic"), command=lambda: self.makeOutput(firstCombobox, firstEntry, secondCombobox, secondEntry))

        nameLabel.grid(row=0, column=0, columnspan=2, sticky="NSEW")

        firstVectorLabel.grid(row=1, column=0, sticky="NSEW")
        firstCombobox.grid(row=1,column=1)
        firstAngleLabel.grid(row=2, column=0, sticky="NSEW")
        firstEntry.grid(row=2, column=1)
        
        secondVectorLabel.grid(row=3, column=0, sticky="NSEW")
        secondCombobox.grid(row=3,column=1)
        secondAngleLabel.grid(row=4, column=0, sticky="NSEW")
        secondEntry.grid(row=4, column=1)

        solveButton.grid(row=5, column=0, columnspan=2)

        pass

    def switchErrorState(self):
        self.ErrorState = not self.ErrorState
        pass

    def makeOutput(self, firstCombobox, firstEntry, secondCombobox, secondEntry):
        def readInput(value):
            try:
                return float(value)
            except ValueError:
                if self.ErrorState == False:
                    self.ErrorState = True
                    self.callWarningWindow()
                return None
        
        e1 = firstCombobox.get()
        e2 = secondCombobox.get()

        angle1 = readInput(firstEntry.get())
        angle2 = readInput(secondEntry.get())


        answer = solver.solve(e1, angle1, e2, angle2)
        self.withdraw()

        outputWindow = FirstTaskOutputApp(self)
        outputWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(outputWindow))
        outputWindow.update(answer)
        
        pass

    def closeWindow(self, window):
        self.deiconify()
        window.destroy()
        pass

    def callWarningWindow(self):
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
        pass
            

class FirstTaskOutputApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        
        self.title("Задача №1")
        self.geometry("640x480")
        self.resizable(False,False)

        for c in range(5): self.columnconfigure(index=c, weight=1)
        for r in range(14): self.rowconfigure(index=r, weight=1)
        
        nameLabel = Label(self, text="Решение", font=("GOST type b", 30, "italic"))

        firstTextLabel = Label(self, text="Матрица поворота для е1:", font=("GOST type b", 20, "italic"))
        secondTextLabel = Label(self, text="Матрица поворота для е2:", font=("GOST type b", 20, "italic"))
        thirdTextLabel = Label(self, text="Итоговая матрица поворота:", font=("GOST type b", 20, "italic"))
        
        firstMatrixLabel = Label(self, text="T =", font=("GOST type b", 20, "italic"))
        secondMatrixLabel = Label(self, text="T =", font=("GOST type b", 20, "italic"))
        thirdMatrixLabel = Label(self, text="T =", font=("GOST type b", 20, "italic"))

        firstMatrixElement00Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement01Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement02Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement10Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement11Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement12Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement20Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement21Label = Label(self, font=("GOST type b", 15, "italic"))
        firstMatrixElement22Label = Label(self, font=("GOST type b", 15, "italic"))

        self.firstMatrix = [[firstMatrixElement00Label, firstMatrixElement01Label, firstMatrixElement02Label],
                       [firstMatrixElement10Label, firstMatrixElement11Label, firstMatrixElement12Label],
                       [firstMatrixElement20Label, firstMatrixElement21Label, firstMatrixElement22Label]]

        secondMatrixElement00Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement01Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement02Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement10Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement11Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement12Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement20Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement21Label = Label(self, font=("GOST type b", 15, "italic"))
        secondMatrixElement22Label = Label(self, font=("GOST type b", 15, "italic"))

        self.secondMatrix = [[secondMatrixElement00Label, secondMatrixElement01Label, secondMatrixElement02Label],
                        [secondMatrixElement10Label, secondMatrixElement11Label, secondMatrixElement12Label],
                        [secondMatrixElement20Label, secondMatrixElement21Label, secondMatrixElement22Label]]

        thirdMatrixElement00Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement01Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement02Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement10Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement11Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement12Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement20Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement21Label = Label(self, font=("GOST type b", 15, "italic"))
        thirdMatrixElement22Label = Label(self, font=("GOST type b", 15, "italic"))

        self.thirdMatrix = [[thirdMatrixElement00Label, thirdMatrixElement01Label, thirdMatrixElement02Label],
                       [thirdMatrixElement10Label, thirdMatrixElement11Label, thirdMatrixElement12Label],
                       [thirdMatrixElement20Label, thirdMatrixElement21Label, thirdMatrixElement22Label]]

#
        nameLabel.grid(row=0,column=0, columnspan=5)

        firstTextLabel.grid(row=1,column=1, columnspan=3)
        secondTextLabel.grid(row=5,column=1, columnspan=3)
        thirdTextLabel.grid(row=9,column=1, columnspan=3)
        
        firstMatrixLabel.grid(row=3, column=0)
        secondMatrixLabel.grid(row=7, column=0)
        thirdMatrixLabel.grid(row=11, column=0)

        firstMatrixElement00Label.grid(row=2, column=1)
        firstMatrixElement01Label.grid(row=2, column=2)
        firstMatrixElement02Label.grid(row=2, column=3)
        firstMatrixElement10Label.grid(row=3, column=1)
        firstMatrixElement11Label.grid(row=3, column=2)
        firstMatrixElement12Label.grid(row=3, column=3)
        firstMatrixElement20Label.grid(row=4, column=1)
        firstMatrixElement21Label.grid(row=4, column=2)
        firstMatrixElement22Label.grid(row=4, column=3)

        secondMatrixElement00Label.grid(row=6, column=1)
        secondMatrixElement01Label.grid(row=6, column=2)
        secondMatrixElement02Label.grid(row=6, column=3)
        secondMatrixElement10Label.grid(row=7, column=1)
        secondMatrixElement11Label.grid(row=7, column=2)
        secondMatrixElement12Label.grid(row=7, column=3)
        secondMatrixElement20Label.grid(row=8, column=1)
        secondMatrixElement21Label.grid(row=8, column=2)
        secondMatrixElement22Label.grid(row=8, column=3)

        thirdMatrixElement00Label.grid(row=10, column=1)
        thirdMatrixElement01Label.grid(row=10, column=2)
        thirdMatrixElement02Label.grid(row=10, column=3)
        thirdMatrixElement10Label.grid(row=11, column=1)
        thirdMatrixElement11Label.grid(row=11, column=2)
        thirdMatrixElement12Label.grid(row=11, column=3)
        thirdMatrixElement20Label.grid(row=12, column=1)
        thirdMatrixElement21Label.grid(row=12, column=2)
        thirdMatrixElement22Label.grid(row=12, column=3)

        pass
    
    def update(self, answer):
        for i in range(3):
            for j in range(3):
                self.firstMatrix[i][j]["text"] = round(answer[0][i][j], 6)
        for i in range(3):
            for j in range(3):
                self.secondMatrix[i][j]["text"] = round(answer[1][i][j], 6)
        for i in range(3):
            for j in range(3):
                self.thirdMatrix[i][j]["text"] = round(answer[2][i][j], 6)
        
        pass
        


if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window = FirstTaskInputApp(root)
    root.mainloop()
