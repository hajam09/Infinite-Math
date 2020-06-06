# importing modules and files
from tkinter import*
import enterTheDetails
import Questions
import ctypes

#root = Tk()

class TACpage3():
    def  __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        # setting up the window size and background colour
        self.master = master
        self.master.title('INFINITE MATH: Terms and Conditions')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        # still image
        self.TC = PhotoImage(file = 'TACpg3.GIF')
        self.PhotoLabel = Label(self.master, image = self.TC, bg = '#9DC3E6')
        self.PhotoLabel.place(x = 0, y = 0)

        # back button to go to main menu
        self.backButtonImage = PhotoImage(file = 'BackButton.GIF')
        self.backImage = Button(self.master, image = self.backButtonImage, bg = '#9DC3E6', command = self.toBackPG)
        self.backImage.place(x = 1, y = 643)

        # next button to go to question page        
        self.beginButtonImage = PhotoImage(file = 'BeginTest.GIF')        
        self.beginImage = Button(self.master, image = self.beginButtonImage, bg = '#9DC3E6', command = self.toNextPG)        
        self.beginImage.place(x = 1096, y = 643)

        # when the back button is clicked this subroutine is executed
    def toBackPG(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        backpage = enterTheDetails.EnterDetailWindow2(root1)

        #when the begin button is clicked this subroutine is executed
    def toNextPG(self):
        self.master.withdraw()
        root2 = Toplevel(self.master)
        nextpage = Questions.questionWindow(root2)

#mainscreen = TACpage3(root)
#root.mainloop()
