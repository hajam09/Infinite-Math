#imports modules and files
from tkinter import*
import time
import ctypes

#root = Tk()

class resultWindow():
    def __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable        
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        #setting up window size and its background colour
        self.master = master
        self.master.title('INFINITE MATH')
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')

        # displays the school's logo
        self.logo = PhotoImage(file = "EastburyLogo.GIF")
        self.logoLabel = Label(self.master, image = self.logo, bg = '#9DC3E6')
        self.logoLabel.place(x = 1000, y = 90)#(x = 1000, y = 90)     

        # text's are placed on a specific locations, so that a value can be displayed next to each label
        self.lbl1 = Label(self.master, text = "SUMMARY : ", bg = '#9DC3E6', font = ('Ar Cena', 40))
        self.lbl1.place(x = 100, y = 90)

        self.lbl2 = Label(self.master, text = "FULL NAME : ", bg = '#9DC3E6', font = ('Ar Cena', 30))
        self.lbl2.place(x = 100, y = 180)

        self.lbl3 = Label(self.master, text = "DATE-OF-BIRTH : ", bg = '#9DC3E6', font = ('Ar Cena', 30))
        self.lbl3.place(x = 100, y = 240)

        self.lbl4 = Label(self.master, text = "YOUR SCORE : ", bg = '#9DC3E6', font = ('Ar Cena', 30))
        self.lbl4.place(x = 100, y = 300)

        self.lbl5 = Label(self.master, text = "DATE-OF-TEST : ", bg = '#9DC3E6', font = ('Ar Cena', 30))
        self.lbl5.place(x = 100, y = 360)

        # opens the file and reads the value that was stored by the enterTheDetails page to be placed next to specific label        
        file1 = open("name.txt", "r")
        self.box1 = Label(self.master, text = file1.read(), font = ('Ar Cena', 30), bg = '#9DC3E6', fg = '#7F7F7F')
        file1.close()
        self.box1.place(x = 450, y = 180)

        file2 = open("dob.txt", "r")
        self.box2 = Label(self.master, text = file2.read(), font = ('Ar Cena', 30), bg = '#9DC3E6', fg = '#7F7F7F')
        file2.close()
        self.box2.place(x = 450, y = 240)

        # an instruction that adds the value on each line from the Points.txt file
        # so the users points gained from the quiz can be displayed on the page.
        total = 0
        with open('Points.txt', 'r') as inp:
            for line in inp:
                try:
                    num = int(line)
                    total +=num
                except ValueError:
                    print(''.format(line))

        x = format(total)

        self.lbl7 = Label(self.master, text = x + '/15', font = ('Ar Cena', 30), bg = '#9DC3E6', fg = '#7F7F7F')
        self.lbl7.place(x = 450, y = 300)

        # displays the quiz attempt date
        now1 = time.strftime("%d/%m/%Y")
        self.lbl6 = Label(self.master, text = now1, font = ('Ar Cena', 30), bg = '#9DC3E6', fg = '#7F7F7F')
        self.lbl6.place(x = 450, y = 360)
        
#mainscreen = resultWindow(root)
#root.mainloop()
