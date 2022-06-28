from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tokenize import String
import webbrowser
import os


# Create a tkinter window
win = Tk()


# Create a window with dimensions
content = ttk.Frame(win)
frame = ttk.Frame(content, width=500, height=300)
win.title('Python Assistant!')
win.resizable(width=False,height=False)

# Functions
    # Search Functions
def searchG():
    sG = searchEntry.get()
    webbrowser.open('www.google.com/search?q=' + str(sG), new=2)
def searchW():
    sW = searchEntry.get()
    webbrowser.open('https://en.wikipedia.org/wiki/' + str(sW), new=2)
def searchYT():
    sYT = searchEntry.get()
    webbrowser.open('https://www.youtube.com/results?search_query=' + str(sYT), new=2)
    # Math Entry Functions
answer = 0
def solutionA():
    global answer
    entryOne = mathFN.get()
    entryTwo = mathSN.get()
    answer = int(float(entryOne)) + int(float(entryTwo))
    answerDisplay = ttk.Label(content, font=("", 10),text=f"Solution = {answer: .3f}".ljust(110)).place(x=20,y=260)
    print(answer)
def solutionS():
    global answer
    entryOne = mathFN.get()
    entryTwo = mathSN.get()
    answer = int(float(entryOne)) - int(float(entryTwo))
    answerDisplay = ttk.Label(content, font=("", 10),text=f"Solution = {answer: .3f}".ljust(110)).place(x=20,y=260)
    print(answer)
def solutionM():
    global answer
    entryOne = mathFN.get()
    entryTwo = mathSN.get()
    answer = int(float(entryOne)) * int(float(entryTwo))
    answerDisplay = ttk.Label(content, width=100, font=("", 10),text=f"Solution = {answer: .3f}".ljust(110)).place(x=20,y=260)
    print(answer)
def solutionD():
    global answer
    entryOne = mathFN.get()
    entryTwo = mathSN.get()
    answer = int(float(entryOne)) / int(float(entryTwo))
    answerDisplay = ttk.Label(content, width=100, font=("", 10),text=f"Solution = {answer: .3f}".ljust(110)).place(x=20,y=260)
    print(answer)
    # PC Control Funtions
confirm = 0
def shutdownB():
    global confirm
    confirm+=1
    print(confirm)

def restartB():
    global confirm
    confirm+=2
    print(confirm)

def sleepB():
    global confirm
    confirm+=3
    print(confirm)

def confirmC():
    global confirm
    if confirm == 1:
        pleaseW = ttk.Label(content, text="Please wait....").place(x=395,y=255)
        os.system("shutdown /s")
        print("Hibernating...")
    elif confirm == 2:
        pleaseW = ttk.Label(content, text="Please wait....").place(x=395,y=255)
        os.system("shutdown /r")
        print("Restarting...")
    elif confirm == 3:
        pleaseW = ttk.Label(content, text="Please wait....").place(x=395,y=255)
        os.system("shutdown /h")
        print("Shutting Down...")
    else:
        pass

# Inner window content
    # Title
title = ttk.Label(content, text="Windows Assistant!", font=("Microsoft New Tai Lue", 15)).place(x=170,y=20)
    # Search Google, Wiki, YT
searchTitle = ttk.Label(content, text="Search", font=("", 10)).place(x=50,y=70)
searchEntry = ttk.Entry(content)
searchEntry.place(x=10,y=100)
google = ttk.Button(content, text="Google", command=searchG).place(x=30,y=130)
wiki = ttk.Button(content, text="Wikipedia", command=searchW).place(x=30,y=160)
youtube = ttk.Button(content, text="YouTube", command=searchYT).place(x=30,y=190)
    # Math Solver
mathTitle = ttk.Label(content, text="Math Solver", font=("", 10)).place(x=220,y=70)
mathFN = ttk.Entry(content)
mathFN.place(x=190,y=100)
mathSN = ttk.Entry(content)
mathSN.place(x=190,y=130)
mathSolverA = ttk.Button(content, text="Add", command=solutionA).place(x=175,y=160)
mathSolverS = ttk.Button(content, text="Subtract", command=solutionS).place(x=255,y=160)
mathSolverM = ttk.Button(content, text="Multiply", command=solutionM).place(x=175,y=190)
mathSolverD = ttk.Button(content, text="Divide", command=solutionD).place(x=255,y=190)
    # Sleep, Restart, Shut Down
rss = ttk.Label(content, text="PC Control", font=("", 10)).place(x=400,y=70)
line = ttk.Label(content, text="|", font=(", 15")).place(x=428,y=188)
restart = ttk.Button(content, text="Restart", command=restartB).place(x=395,y=100)
sleep = ttk.Button(content, text="Sleep", command=sleepB).place(x=395,y=130)
shutdown = ttk.Button(content, text="Shut down", command=shutdownB).place(x=395,y=160)
rssConfirm = ttk.Button(content, text="Confirm", command=confirmC).place(x=395,y=220) 

#Window
content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=5, rowspan=6)



win.mainloop()
