from tkinter import *
import datetime
import os

#Setting the root window for Tkinter GUI
rw= Tk()
rw.configure(background="plum1")
rw.geometry("370x400+30+30")
rw.title("AR-B Program")
rw.resizable(False, False)

#Input user's name and print greeting message
name= input("\nEnter your name:")
print("\nHello!", name)

#Shows the current date and time
now= datetime.datetime.now()
print("\nCurrent date and time is:")
print(now.strftime("%Y-%m-%d\n%H:%M:%S"))


#Function to run dice rolling program
def rolldice():
        import diceroll
        os.system("diceroll.py")

def guessinggame():
        import numberguess
        os.system("numberguess.py")
        
def youtubesearch():
        import vidsearch
        os.system("vidsearch.py")

def minicalculator():
        import calculator
        os.system("calculator.py")

def mainexit():
        rw.destroy()

def helptext():
        f = open("helpfile.txt", "r")
        for x in f:
          print(x)
        f.close()
        
#~Start of GUI~
#Setting the GUI's label
labelfont= ("arial","16","bold")
homelabel= Label(rw, text="Welcome to AR-B's\n Home Interface", fg="DarkOrchid2", bg="plum1")
homelabel.config(font= labelfont)
homelabel.place(x = 30, y = 10 + 30, width=300)


#Setting the button fontstyle
buttonfont= ("arial", "10", "bold")

#Button to run dice rolling minigame
BtnDR= Button(rw, text="Roll Some Dices", command= rolldice)
BtnDR.configure(bg="MediumOrchid3", fg="white")
BtnDR.configure(font= buttonfont)
BtnDR.place(x = 35, y = 90 + 30, width=130, height=50)

#Button to run number guessing minigame
BtnG= Button(rw, text="Guess A Number", command= guessinggame)
BtnG.configure(bg="MediumOrchid3", fg="white")
BtnG.configure(font= buttonfont)
BtnG.place(x = 200, y = 90 + 30, width=130, height=50)

#Button to run a video searcher for youtube
BtnVS= Button(rw, text="Search for a video", command= youtubesearch)
BtnVS.configure(bg="MediumOrchid3", fg="white")
BtnVS.configure(font= buttonfont)
BtnVS.place(x = 35, y = 170 + 30, width=130, height=50)

#Button to run a mini calculator
BtnC= Button(rw, text="Use a calculator", command= minicalculator)
BtnC.configure(bg="MediumOrchid3", fg="white")
BtnC.configure(font= buttonfont)
BtnC.place(x = 200, y = 170 + 30, width=130, height=50)

#Button to quit the main program
BtnQ= Button(rw, text="Quit Program", command= mainexit)
BtnQ.configure(bg="MediumOrchid3", fg="white")
BtnQ.configure(font= buttonfont)
BtnQ.place(x = 115, y = 250 + 30, width=130, height=40)

BtnH= Button(rw, text="Help", command= helptext)
BtnH.configure(bg="MediumOrchid3", fg="white")
BtnH.configure(font= buttonfont)
BtnH.place(x = 115, y = 305 + 30, width=130, height=40)

#Every code goes above this line
#This is to loop the GUI so it does not close until user closes it
rw.mainloop()
