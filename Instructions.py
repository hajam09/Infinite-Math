from tkinter import*
import mainMenu
import ctypes

#root = Tk()

class instructionWindow():
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

        self.photo = PhotoImage(file = 'Instructions.GIF')
        self.photoLabel = Label(self.master, image = self.photo, bg = '#9DC3E6')
        self.photoLabel.pack(side = TOP)

        # button to go back to the main menu
        self.photo1 = PhotoImage(file = 'BackButton.GIF')
        self.photoButton = Button(self.master, image = self.photo1, bg = '#9DC3E6', command = self.toMainMenu)
        self.photoButton.place(x = 718, y = 625)

        # command executed when the back button is clicked.
        def toMainMenu(self):
            self.master.withdraw()
            root2 = Toplevel(self.master)
            backmenu = mainMenu.TitleScreen1(root2)


#mainscreen = instructionWindow(root)
#root.mainloop()
