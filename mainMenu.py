#imports modules and files
from tkinter import*
import instruction
import enterTheDetails
import ctypes

#root = Tk()

class TitleScreen1():
    def __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)
        
        #setting up the window size and background colour
        self.master = master
        self.master.title('INFINITE MATH: Main Menu')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        #setting up the title photo that are to be set in the middle of the screen
        self.photo = PhotoImage(file = 'TitleScreenPhoto.GIF')
        self.photoLabel = Label(self.master, image = self.photo, bg = '#9DC3E6')
        self.photoLabel.pack(side = TOP)

        #setting up a button, so when it is clicked it will move onto the next screen
        self.photo1 = PhotoImage(file = 'EnterDetailbutton.GIF')    # storing the image of the button
        self.photoButton = Button(self.master, image = self.photo1, bg = '#9DC3E6', command = self.toPg2)
        self.photoButton.place(x = 565, y = 630)

        #setting up a button, so when it is clicked it will open up the instruction page
        self.photo2 = PhotoImage(file = 'InstructionButton.GIF')
        self.insButton = Button(self.master, image = self.photo2, bg = '#9DC3E6', command = self.toInstructionScreen)                                
        self.insButton.place(x = 0, y = 0)

        # when the button is clicked this function will be called so it can be executed
    def toPg2(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        #When photo1 is clicked the window will move to entertTheDetails window
        nextpage = enterTheDetails.EnterDetailWindow2(root1)

        # when the instruction button is clicked this function will be called so it can be executed
    def toInstructionScreen(self):
        self.master.withdraw()
        root2 = Toplevel(self.master)
        instructionPage = instruction.InstructionPG(root2)

#mainscreen = TitleScreen1(root)
#root.mainloop()
