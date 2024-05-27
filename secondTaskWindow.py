from tkinter import Tk, Label, Button, Toplevel
from tkinter import ttk
import linal_2 as solver


class SecondTaskInputApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Задача №2")
        self.geometry("640x480")
        self.resizable(False,False)

        nameLabel = Label(self, text="Задача №2", font=("GOST type b", 30, "italic"))
        
        for c in range(10): self.columnconfigure(index=c, weight=1)
        for r in range(5): self.rowconfigure(index=r, weight=1)

        self.EntryList = [[ttk.Entry(self, width=5) for i in range(4)] for j in range(6)]

        self.ErrorState = False
        
        pVectorLabel = Label(self, text="p = ", font=("GOST type b", 20, "italic"))
        qVectorLabel = Label(self, text="q = ", font=("GOST type b", 20, "italic"))
        a1VectorLabel = Label(self, text="a1 = ", font=("GOST type b", 20, "italic"))
        a2VectorLabel = Label(self, text="a2 = ", font=("GOST type b", 20, "italic"))
        a3VectorLabel = Label(self, text="a3 = ", font=("GOST type b", 20, "italic"))
        a4VectorLabel = Label(self, text="a4 = ", font=("GOST type b", 20, "italic"))

        solveButton = Button(self, text="Решить", font=("GOST type b", 20, "italic"), command=lambda: self.makeOutput())

        nameLabel.grid(row=0, column=0, columnspan=10, sticky="NSEW")

        pVectorLabel.grid(row=1, column=0, sticky="NSEW")
        a1VectorLabel.grid(row=2, column=0, sticky="NSEW")
        a3VectorLabel.grid(row=3, column=0, sticky="NSEW")
        qVectorLabel.grid(row=1, column=5, sticky="NSEW")
        a2VectorLabel.grid(row=2, column=5, sticky="NSEW")
        a4VectorLabel.grid(row=3, column=5, sticky="NSEW")

        k = 1
        for i in range(0, len(self.EntryList), 2):
            
            for j in range(4):
                self.EntryList[i][j].grid(row=k, column=j+1)
                    
            for j in range(4):
                self.EntryList[i+1][j].grid(row=k, column=j+6)
            k+= 1
            

        solveButton.grid(row=4, column=0, columnspan=10)

        pass
    
    def makeOutput(self):
        def readInput(value):
            try:
                return float(value)
            except ValueError:
                if self.ErrorState == False:
                    self.switchErrorState()
                    self.callWarningWindow()
                return None
        
        inputNumbers = [readInput(self.EntryList[i][j].get()) for i in range(len(self.EntryList)) for j in range(len(self.EntryList[i]))]
        if (inputNumbers.count(None) == 0):

            
            answer = solver.solve(inputNumbers)
            
            
            outputWindow = SecondTaskOutputApp(self)
            self.withdraw()

            outputWindow.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(outputWindow))
            outputWindow.update(answer)
        
        pass

    def closeWindow(self, window):
        self.deiconify()
        window.destroy()
        pass

    def switchErrorState(self):
        self.ErrorState = not self.ErrorState
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
            

class SecondTaskOutputApp(Toplevel):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        
        self.title("Задача №1")
        self.geometry("960x720")
        self.resizable(False,False)

        for c in range(10): self.columnconfigure(index=c, weight=2)
        for r in range(15): self.rowconfigure(index=r, weight=1)
        for c in range(1,5): self.columnconfigure(index=c, weight=1)
        for c in range(6,10): self.columnconfigure(index=c, weight=1)
        
        nameLabel = Label(self, text="Решение", font=("GOST type b", 30, "italic"))

        firstPointLabel = Label(self, text="Новый базис {bj}:", font=("GOST type b", 20, "italic"))
        bVectorsLabels = [Label(self, text=f"b{i} =", font=("GOST type b", 15, "italic", "bold")) for i in range(1,5)]
        self.bVectorsValuesLabels = [[Label(self, font=("GOST type b", 15, "italic")) for i in range(4)] for j in range(4)]

        secondPointLabel = Label(self, text="Матрица перехода:", font=("GOST type b", 20, "italic"))
        nameMatrixLabel = Label(self, text="T(b->a) = ", font=("GOST type b", 20, "italic", "bold"))
        self.matrixLabels = [[Label(self, font=("GOST type b", 15, "italic")) for i in range(4)] for j in range(4)]

        thirdPointLabel = Label(self, text="Векторы p и q в базисе {bj}:", font=("GOST type b", 20, "italic"))
        pVectorLabel = Label(self, text="p = ", font=("GOST type b", 15, "italic", "bold"))
        qVectorLabel = Label(self, text="q = ", font=("GOST type b", 15, "italic", "bold"))
        self.thirdVectorsLabels = [[Label(self, font = ("GOST type b", 15, "italic")) for j in range(4)] for i in range(2)]

        fourthPointLabel = Label(self, text="Скалярное произведение p и q:", font=("GOST type b", 20, "italic"))
        pqLabel = Label(self, text="p*q = ", font=("GOST type b", 15, "italic", "bold"))
        self.pqValueLabel = Label(self, font=("GOST type b", 15, "italic"))

        fifthPointLabel = Label(self, text="Угол между p и q в градусах:", font=("GOST type b", 20, "italic"))
        angleLabel = Label(self, text="∠(p,q) = ", font=("GOST type b", 15, "italic", "bold"))
        self.angleValueLabel = Label(self, font=("GOST type b", 15, "italic"))
#
        nameLabel.grid(row=0,column=0, columnspan=10, sticky="NSEW")

        
        firstPointLabel.grid(row=1, column=0, columnspan=10, sticky="NSEW")
        m = 2
        for i in range(0, 4, 2):
            bVectorsLabels[i].grid(row=m, column=0, sticky="NSEW")
            bVectorsLabels[i+1].grid(row=m, column=5, sticky="NSEW")
            m+=1
        m = 2
        for i in range(0, len(self.bVectorsValuesLabels), 2):
            for j in range(1, len(self.bVectorsValuesLabels[i])+1):
                self.bVectorsValuesLabels[i][j-1].grid(row=m, column=j, sticky="NSEW")
                self.bVectorsValuesLabels[i+1][j-1].grid(row=m, column=(j+5), sticky="NSEW")
            m+=1 

        secondPointLabel.grid(row=4, column=0, columnspan=10, sticky="NSEW")
        nameMatrixLabel.grid(row=5, column=0, rowspan=4, columnspan=3, sticky="NSEW")
        for i in range(4):
            for j in range(4):
                self.matrixLabels[i][j].grid(row=(i+5),column=(j+4), sticky="NSEW")
        
        thirdPointLabel.grid(row=9, column=0, columnspan=10, sticky="NSEW")
        pVectorLabel.grid(row=10, column=0, sticky="NSEW")
        qVectorLabel.grid(row=10, column=5, sticky="NSEW")

        m=1
        for i in range(2):
            for j in range(4):
                self.thirdVectorsLabels[i][j].grid(row=10, column=j+m, sticky="NSEW")
            m+=5
        
        fourthPointLabel.grid(row=11, column=0, columnspan=10, sticky="NSEW")
        pqLabel.grid(row=12, column=4, sticky="NSEW")
        self.pqValueLabel.grid(row=12,column=5, sticky="NSEW")
        
        fifthPointLabel.grid(row=13, column=0, columnspan=10, sticky="NSEW")
        angleLabel.grid(row=14, column=4, sticky="NSEW")
        self.angleValueLabel.grid(row=14, column=5, sticky="NSEW")
        
        pass
    
    def update(self, answer):
        ans1 = answer[0]
        ans2 = answer[1]
        ans3 = answer[2]
        ans4 = answer[3]
        ans5 = answer[4]

        for i in range(4):
            for j in range(4):
                if j == 0:
                    self.bVectorsValuesLabels[i][j]['text'] = '['
                    self.matrixLabels[i][j]['text'] = '[' 
                    self.bVectorsValuesLabels[i][j]['text'] += str(round(ans1[i][j], 2))
                    self.matrixLabels[i][j]['text'] += str(round(ans2[i][j], 2))
                    continue
                self.bVectorsValuesLabels[i][j]['text'] = str(round(ans1[i][j], 2))
                self.matrixLabels[i][j]['text'] = str(round(ans2[i][j], 2))
                if j == 3:
                    self.bVectorsValuesLabels[i][j]['text'] += ']'
                    self.matrixLabels[i][j]['text'] += ']'
                

        for i in range(2):
            for j in range(4):
                if j == 0:
                    self.thirdVectorsLabels[i][j]["text"] = '['
                    self.thirdVectorsLabels[i][j]["text"] += str(round(ans3[i][j], 2))
                    continue
                self.thirdVectorsLabels[i][j]["text"] = str(round(ans3[i][j], 2))
                if j == 3:
                    self.thirdVectorsLabels[i][j]["text"] += ']'

        self.pqValueLabel['text'] = round(ans4, 2)
        self.angleValueLabel['text'] = round(ans5, 2)
        pass
        


if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    window = SecondTaskInputApp(root)
    root.mainloop()
