#imports modules and files
from tkinter import*
import hintPage2
import ctypes

#root = Tk()

class HP1():
    def __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        # setting up the window size and background colour
        self.master = master
        self.master.title('INFINITE MATH')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        self.hintpage1Image =PhotoImage(file = 'HintPage1.GIF')
        self.hintPhoto = Label(self.master, image = self.hintpage1Image, bg = '#9DC3E6')
        self.hintPhoto.pack()

        # next button appears in the window
        self.nextButtonImage = PhotoImage(file = 'NextButton.GIF')
        self.nextImage = Button(self.master, image = self.nextButtonImage, bg = '#9DC3E6', command = self.toNextPG)
        self.nextImage.place(x = 1096, y = 643)

        # command executed when the next  button is clicked
    def toNextPG(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        nextpage = hintPage2.HP2(root1)

#mainscreen = HP1(root)
#root.mainloop()
