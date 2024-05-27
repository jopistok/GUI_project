from tkinter import Tk, Label, Button, Toplevel
import firstTaskWindow as task1
import secondTaskWindow as task2
import thirdTaskWindow as task3

class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.title("Решатель Линала OVER 9000")
        self.geometry("640x480")
        self.resizable(False,False)

        nameLabel = Label(self, text="Решатель Линала\nOVER 9000", font=("GOST type b", 30, "italic"))

        buttonFirstTask = Button(text="Задача №1", font=("GOST type b", 20, "italic"), command=self.firstTask)
        buttonSecondTask = Button(text="Задача №2", font=("GOST type b", 20, "italic"), command=self.secondTask)
        buttonThirdTask = Button(text="Решение СЛАУ", font=("GOST type b", 20, "italic"), command=self.thirdTask)
        buttonQuit = Button(text="Выход", font=("GOST type b", 20, "italic"), command=self.destroy)

        copyrightLabel = Label(self, text='Над проектом работали: ТО "Ракитин Андрей Петрович, Сафуанова Алина\nИльдаровна, Вовк Екатерина Александровна"', font=("GOST type b", 14, "italic"))

        self.columnconfigure(index=0, weight=1)
        for r in range(6): self.rowconfigure(index=r, weight=1)
        
        nameLabel.grid(row=0,column=0)
        buttonFirstTask.grid(row=1,column=0)
        buttonSecondTask.grid(row=2,column=0)
        buttonThirdTask.grid(row=3,column=0)
        buttonQuit.grid(row=4,column=0)
        copyrightLabel.grid(row=5,column=0)
        pass
    
    def firstTask(self):
        self.withdraw()

        window = task1.FirstTaskInputApp(self)
        
        window.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(window))
        pass

    def secondTask(self):
        self.withdraw()

        window = task2.SecondTaskInputApp(self)
        
        window.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(window))
        pass
    
    def thirdTask(self):
        self.withdraw()

        window = task3.TrirdTaskSizeApp(self)
        
        window.protocol("WM_DELETE_WINDOW", lambda: self.closeWindow(window))
        pass
    

    def closeWindow(self, window):
        self.deiconify()
        window.destroy()
        pass


if __name__ == '__main__':
    MainApp().mainloop()
