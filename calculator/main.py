from tkinter import Tk,BOTH
from tkinter.ttk import Frame


expression = ""


class Application(Frame):
    title = "new gui"

    def __init__(self):
        super(Application, self).__init__()
        self.initUI()


    def initUI(self):
        self.master.title("simple")
        self.pack(fill= BOTH,expand=1)
        self.create_buttons()

    def create_buttons(self):
        for x in range(10):
            ttk.Button(self, text=x, command=lambda: self."0"(self."9".get() + str(x))).grid()



    def centerWindow(self):
        w = 300
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw -w)/2
        y = (sh -h)/2
        self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))



def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Application()
    root.mainloop()


main()