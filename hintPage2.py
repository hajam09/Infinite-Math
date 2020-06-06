#imports modules and files
from tkinter import*
import hintPage1
import Questions
import ctypes

#root = Tk()

class HP2():
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

        self.hintpage2Image =PhotoImage(file = 'HintPage2.GIF')
        self.hintPhoto = Label(self.master, image = self.hintpage2Image, bg = '#9DC3E6')
        self.hintPhoto.pack()

        # back button to go back to the hint page 1
        self.backButtonImage = PhotoImage(file = 'BackButton.GIF')
        self.backImage = Button(self.master, image = self.backButtonImage, bg = '#9DC3E6', command = self.toBackPG)
        self.backImage.place(x = 1, y = 643)

        # command executed when the back button is clicked
    def toBackPG(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        backpage = hintPage1.HP1(root1)

        # exit button to go back to the question page
        self.exitButtonImage = PhotoImage(file = 'ExitButton.GIF')        
        self.exitImage = Button(self.master, image = self.exitButtonImage, bg = '#9DC3E6', command = self.toCurrentPG)        
        self.exitImage.place(x = 1096, y = 643)
        
        # command executed when the back button is clicked
    def toCurrentPG(self):
        self.master.withdraw()
        root2 = Toplevel(self.master)
        currentPG = Questions.questionWindow(root2)

#mainscreen = HP2(root)
#root.mainloop()
