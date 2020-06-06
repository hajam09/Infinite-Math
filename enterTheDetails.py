from tkinter import*
import mainMenu
import termsAndConditions
import ctypes

#root = Tk()

class EnterDetailWindow2():
    def __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        # setting up the window size and background colour
        self.master = master
        self.master.title('INFINITE MATH: Enter your Details')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        # assigning a image and placing it in a specific coordinates
        self.paper = PhotoImage(file = 'DetailFill.GIF')
        self.photoLabel = Label(self.master, image = self.paper, bg = '#9DC3E6')
        self.photoLabel.place(x = 1115, y = 50)

        # sub title text
        self.lbl = Label(self.master, text = 'PLEASE ENTER YOUR DETAILS:', bg = '#9DC3E6', font = ('Ar Cena', 40))
        self.lbl.place(x = 50, y = 50)

        # placing entry widget box, so that the user can input their details
        self.FN = Label(self.master, text = 'FIRST NAME :', bg = '#9DC3E6', font = ('Ar Cena', 28))
        self.FN.place(x = 50, y = 130)
        self.FN1 = Label(self.master, text = '"ENTER YOUR FIRST NAME BETWEEN 3 TO 12 CHARACTERS"', bg = '#9DC3E6', font = ('Ar Cena', 14))
        self.FN1.place(x = 650, y = 140)
        self.FNentry = Entry(self.master, width = 50)
        self.FNentry.place(x = 315, y = 150)

        self.SN = Label(self.master, text = 'LAST NAME :', bg = '#9DC3E6', font = ('Ar Cena', 28))
        self.SN.place(x = 50, y = 180)
        self.SN1 = Label(self.master, text = '"ENTER YOUR SECOND NAME BETWEEN 3 TO 12 CHARACTERS"', bg = '#9DC3E6', font = ('Ar Cena', 14))
        self.SN1.place(x = 650, y = 190)
        self.SNentry = Entry(self.master, width = 50)
        self.SNentry.place(x = 315, y = 200)

        self.DOB = Label(self.master, text = 'DATE-OF-BIRTH :', bg = '#9DC3E6', font = ('Ar Cena', 28))
        self.DOB.place(x = 50, y = 230)
        self.DOB1 = Label(self.master, text = '"ENTER YOUR DATE-OF-BIRTH IN THE \'DD/MM/YYYY\' FORMAT"', bg = '#9DC3E6', font = ('Ar Cena', 14))
        self.DOB1.place(x = 650, y = 240)
        self.DOBentry = Entry(self.master, width = 50)
        self.DOBentry.place(x = 315 , y = 250)

        #setting up an error message label so that the system can output the message
        self.Label = Label(self.master, font = ('Ar Cena', 20), bg = '#9DC3E6', fg = 'dark red')
        self.Label.place(x = 383, y = 350)

        # front and back button to navigate the window
        self.backButtonImage = PhotoImage(file = 'BackButton.GIF')
        self.backImage = Button(self.master, image = self.backButtonImage, bg = '#9DC3E6', command = self.toBackPG)
        self.backImage.place(x = 1, y = 643)

        self.nextButtonImage = PhotoImage(file = 'NextButton.GIF')        
        self.nextImage = Button(self.master, image = self.nextButtonImage, bg = '#9DC3E6', command = self.toNextPG)
        self.nextImage.place(x = 1096, y = 643)

        # command executed when the back button is clicked
    def toBackPG(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        backpage = mainMenu.TitleScreen1(root1)
        
    # command executed when the next  button is clicked
    def toNextPG(self):
        firstName = self.FNentry.get() # stores the users first name
        secondName = self.SNentry.get() # stores the users second name
        dateOB = self.DOBentry.get() # stores the users date-of-birth

        # presence check is carried out. If the user has left out any input box the screen will not change.
        if ((len(firstName) > 2) and (len(firstName) < 13)) and ((len(secondName) > 2) and (len(firstName) < 13)) and ((len(dateOB)) == 10):
            fullName = firstName + ' ' + secondName #joins the firstname and secondname
            nameFile = open('name.txt', 'w')    # opening a .txt file so the user's name and their date-of-birth can be stored in different files
            nameFile.write(fullName)            # users full name can be displayed on the result window
            nameFile.close()
            nameFile2 = open('dob.txt', 'w')
            nameFile2.write(dateOB)
            nameFile2.close()
            self.master.withdraw()
            root2 = Toplevel(self.master)
            nextpage = termsAndConditions.TACpage3(root2)
        elif firstName == '1' or firstName == '2' or firstName == '3' or firstName == '4' or firstName == '5' or firstName == '6' or firstName == '7' or firstName == '8' or firstName == '9' or firstName == '0':
            self.FNentry.delete(0, END)
            self.Label.configure(text = "PLEASE DO NOT ENTER ANY NUMBERS")
        elif secondName == '1' or secondName == '2' or secondName == '3' or secondName == '4' or secondName == '5' or secondName == '6' or secondName == '7' or secondName == '8' or secondName == '9' or secondName == '0':
            self.SNentry.delete(0, END)
            self.Label.configure(text = "PLEASE DO NOT ENTER ANY NUMBERS")
        elif firstName != "" and (len(firstName) < 3):
            self.FNentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR FIRST NAME BETWEEN 3 TO 12 CHARACTERS!")
        elif firstName != "" and len(firstName) > 12:
            self.FNentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR FIRST NAME BETWEEN 3 TO 12 CHARACTERS!")
        elif secondName != "" and len(secondName) < 3:
            self.SNentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR SECOND NAME BETWEEN 3 TO 12 CHARACTERS!")
        elif secondName != "" and len(secondName) > 12:
            self.SNentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR SECOND NAME BETWEEN 3 TO 12 CHARACTERS!")
        elif dateOB != "" and (len(dateOB) != 10):
            self.DOBentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR DATE-OF-BIRTH IN THE 'DD/MM/YYYY' FORMAT!")
        elif firstName == "" and secondName == "" and dateOB =="":
            self.FNentry.delete(0, END)
            self.SNentry.delete(0, END)
            self.DOBentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR DETAILS AGAIN")
        elif (firstName != "") and (len(firstName) < 3) and (len(firstName) > 12) and (secondName != "") and (len(secondName) < 3) and (len(secondName) > 12) and dateOB != "" and (len(dateOB) != 10):
            self.FNentry.delete(0, END)
            self.SNentry.delete(0, END)
            self.DOBentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR DETAILS AGAIN")
        else:
            self.FNentry.delete(0, END)
            self.SNentry.delete(0, END)
            self.DOBentry.delete(0, END)
            self.Label.configure(text = "PLEASE ENTER YOUR DETAILS AGAIN")
            
#mainscreen = EnterDetailWindow2(root)
#root.mainloop()
