from tkinter import*
import mainMenu
import ctypes

#root = Tk()

class InstructionPG():
    def  __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        #setting up the window size and background colour
        self.master = master
        self.master.title('INFINITE MATH: Terms and Conditions')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        #setting up an image of the instruction page as a background
        self.IW = PhotoImage(file = 'InstructionWindow.GIF')
        self.PhotoLabel = Label(self.master, image = self.IW, bg = '#9DC3E6')
        self.PhotoLabel.place(x = 0, y = 0)

        #setting up a button, so when it is clicked it will go back to the main menu screen
        self.backButtonImage = PhotoImage(file = 'BackButton.GIF')
        self.backImage = Button(self.master, image = self.backButtonImage, bg = '#9DC3E6', command = self.toBackPG)
        self.backImage.place(x = 500, y = 643)

        #setting up a button, so when it is clicked it will open up the user documentation file
        self.Doc = PhotoImage(file = 'UserDoc.GIF')
        self.DocImg = Button(self.master, image = self.Doc, bg = '#9DC3E6')
        self.DocImg.place(x = 0, y = 605)

        #command executed when the back button is clicked
    def toBackPG(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        backpage = mainMenu.TitleScreen1(root1)

#mainscreen = InstructionPG(root)
#root.mainloop()
