from tkinter import*
import resultScreen
import hintPage1
import ctypes

#root = Tk()

class questionWindow():
    def __init__(self, master):

        #getting the windows screen's height and width and storing it in a variable
        user32 = ctypes.windll.user32
        screensize1 = user32.GetSystemMetrics(0)
        screensize2 = user32.GetSystemMetrics(1)
        overallScreenSize = str(screensize1) + 'x' + str(screensize2)

        #erases any values stores on the file        
        open("Points.txt", "w").close() #clears the contents of the file

        self.master = master
        self.master.title("INFINITE MATH: Questions")
        self.master.geometry(overallScreenSize)
        self.master.configure(bg = '#9DC3E6')
        
        self.c = Canvas(self.master, width = 1695, height = 695, bg = '#9DC3E6')
        self.c.place(x = 0, y = 0)
        
        #Questions to display
        global Questions
        Questions = ["1. NEXT NUMBER IN THE SEQUENCE 5, 10, 15, 20 ?", "2. SUM OF 10/5 AND 15/5 ?", "3. MILLIMETRES IN A METRE ?", "4. VALUE OF X? WHEN 5X + 3 = 28", "5. WHAT IS THE HYPOTENUSE, IF X = 4 AND Y = 3 ?", "6. VERTICES IN A CUBE ?", "7. NEXT NUMBER IN THE SEQUENCE 36, 25, 16, 9 ... ?", "8. WHAT IS 7092 / 3546 ?", "9. VALUE OF (10 - 5 x 5) / -15 ?", "10. WHAT IS THE GRADIENT OF THE EQUATION Y = -8x - 5 ?", "11. WHAT IS THE VALUE OF Y IF 2X + 2Y - 10 = 0 ? WHEN X = 1", "12. WHAT IS THE SUM OF FIRST 3 PRIME NUMBERS ?", "13. WHAT IS THE MEAN IF THE SUM OF f(x) = 50 and n = 5 ?", "14. WHAT IS THE TOTAL INTERIOR ANGLE OF A NONAGON ?", "15. WHAT IS THE INTERCEPT OF THE EQUATION Y = X^2 -2X ?"]
        global Answers
        Answers = [25, 5, 1000, 5, 5, 8, 4, 2, 1, -8, 4, 10, 10, 1260, 0]
        global QNumber
        QNumber = 0

        # Question Box
        self.photo2 = PhotoImage(file = "Question Box.gif")
        self.questionBox = Label(self.master, bg = "#9DC3E6", fg = "black", text = Questions[QNumber], font = ("Ar Cena", 40), width = 60, height = 1, relief = FLAT)
        self.questionBox.pack(side = TOP)
        self.questionBox.place(y = 80)

        # Answers
        global text1
        global text2        
        global text3
        global text4
        text1 = [25, 1, 10, 0, 7, 8, 2, 2, 1, -3, 8, 7, 5, 1200, 0]
        text2 = [20, 4, 100, 3, 5, 6, 8, 4, 3, 5, 3, 9, 10, 1280, 1]
        text3 = [5, 5, 1000, 2, 4, 4, 4, 3, 6, 5, 2, 10, 45, 1250, 2]
        text4 = [24, 2, 1, 5, 3, 0, 1, 24, 5, -8, 4, 5, 55, 1260, 3]
        
        
        # Buttons for Answer box
        self.answerBox1 = Button(self.master, bg = "white", fg = "black", command = self.button1, text = text1[QNumber], font =("Ar Cena", 40), width = 13)
        self.answerBox1.place(x = 280, y = 209)

        self.answerBox2 = Button(self.master, bg = "white", fg = "black", command = self.button2, text = text2[QNumber], font =("Ar Cena", 40), width = 13)
        self.answerBox2.place(x = 812, y = 209)

        self.answerBox3 = Button(self.master, bg = "white", fg = "black", command = self.button3, text = text3[QNumber], font =("Ar Cena", 40), width = 13)
        self.answerBox3.place(x = 280, y = 382)

        self.answerBox4 = Button(self.master, bg = "white", fg = "black", command = self.button4, text = text4[QNumber], font =("Ar Cena", 40), width = 13)
        self.answerBox4.place(x = 812, y = 382)

        # Help Button
        self.photo3 = PhotoImage(file = "HintButton.gif")
        self.hint = Button(self.master, image = self.photo3, bg = "#9DC3E6", command = self.hintScreen)
        self.hint.place(x = 30, y = 550)

    def hintScreen(self):
        self.master.withdraw()
        root1 = Toplevel(self.master)
        hintWindow = hintPage1.HP1(root1)

    def button1(self):

        global QNumber
        
        if int(text1[QNumber]) == Answers[QNumber]:
            store3 = open("Points.txt","a")
            store3.write(str("\n1")) # writes '1' to the text file if the user clicks the correct answer.
            store3.close()
        else:
            store4 = open("Points.txt","a") 
            store4.write(str("\n0")) # writes '0' to the text file if the user clicks the incorrect answer.
            store4.close()

        QNumber = QNumber + 1 # next question is loaded
        
        if QNumber != 15: # checks if the user has done all ten questions
            self.questionBox.configure(text = Questions[QNumber]) # changes text in question box to show next question
            self.answerBox1.configure(text = text1[QNumber]) # changes text in answer boxes to show next selection of answers
            self.answerBox2.configure(text = text2[QNumber])
            self.answerBox3.configure(text = text3[QNumber])
            self.answerBox4.configure(text = text4[QNumber])
        else:
            self.c.after(1000, self.resultsScreen)
            
    def button2(self):

        global QNumber
        
        if int(text2[QNumber]) == Answers[QNumber]:
                     
            store3 = open("Points.txt","a")
            store3.write("\n1")
            store3.close()
        else:
            store4 = open("Points.txt","a")
            store4.write("\n0")
            store4.close()
            
        QNumber = QNumber + 1
        
        if QNumber != 15:
            self.questionBox.configure(text = Questions[QNumber])
            self.answerBox1.configure(text = text1[QNumber])
            self.answerBox2.configure(text = text2[QNumber])
            self.answerBox3.configure(text = text3[QNumber])
            self.answerBox4.configure(text = text4[QNumber])
        else:
            self.c.after(1000, self.resultsScreen)

    def button3(self):

        global QNumber
        if int (text3[QNumber]) == Answers[QNumber]:

            store3 = open("Points.txt","a")
            store3.write("\n1")
            store3.close()
        else:
            store4 = open("Points.txt","a")
            store4.write("\n0")
            store4.close()

        QNumber = QNumber + 1
        
        if QNumber != 15:
            self.questionBox.configure(text = Questions[QNumber])
            self.answerBox1.configure(text = text1[QNumber])
            self.answerBox2.configure(text = text2[QNumber])
            self.answerBox3.configure(text = text3[QNumber])
            self.answerBox4.configure(text = text4[QNumber])
        else:
            self.c.after(1000, self.resultsScreen)

            
    def button4(self):

        global QNumber

        if int(text4[QNumber]) == Answers[QNumber]:
            store3 = open("Points.txt","a")
            store3.write("\n1")
            store3.close()
        else:            
            store4 = open("Points.txt", "a")
            store4.write("\n0")
            store4.close()
            
        QNumber = QNumber + 1
        
        if QNumber != 15:
            self.questionBox.configure(text = Questions[QNumber])
            self.answerBox1.configure(text = text1[QNumber])
            self.answerBox2.configure(text = text2[QNumber])
            self.answerBox3.configure(text = text3[QNumber])
            self.answerBox4.configure(text = text4[QNumber])
        else:
            self.c.after(1000, self.resultsScreen)

    def resultsScreen(self):
        self.master.withdraw()
        root2 = Toplevel(self.master)
        resultsWindow = resultScreen.resultWindow(root2)

#mainscreen = questionWindow(root)
#root.mainloop()
