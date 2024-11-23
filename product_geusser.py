from tkinter import *
import math
import random
import tkinter.messagebox
import time

root = Tk()
root.geometry("500x500")
root.title("Number Guesser")
geussCount = 0

def too_low():
    tkinter.messagebox.showinfo("messagebox", "Your geuss is too low. Try again")

def too_high():
    tkinter.messagebox.showinfo("messagebox", "Your geuss is too high. Try again")

def check_number():
    global geussCount
    geussCount+=1 
    geussLabel.config(text = "You have made " + str(geussCount) + " Geusses so far")
    
    geuss = enter_geuss.get()
    geuss = int(geuss)
    if geuss < product:
        too_low()
    if geuss > product:
        too_high()
    if geuss == product:
        # Tk.quit(root)
        tkinter.messagebox.showinfo("Good Job!", "You geussed it right!")
        win_label = Label(root, text = "Good Job! You got it right!", font=("Calibri", 40, "bold"), fg = "red")
        win_label.place(x=500, y=200)
        secondsTillClose = 5
        win_label = Label(root, text = "Closing the display in "+ str(secondsTillClose), font=("Calibri", 20, "bold"), fg = "red")
        
        win_label.place(x=500, y=300)
        if secondsTillClose > 0:
            time.sleep(1)
            secondsTillClose-=1
            win_label.config(text = "Closing the display in "+ str(secondsTillClose), font=("Calibri", 20, "bold" ))
        if secondsTillClose == 0:
            Tk.quit(root)
        else:
            print("Error in seconds till close")



label = Label(root, text = "Welcome player. Let's get started!")
label.pack()

info1 = Label(root, text = "The aim of the game is to geuss the product of two numbers, each number between 1 and 10")
info1.place(x=500, y=50)

num1 = random.randint(1,10)
num2 = random.randint(1,10)

info2 = Label(root, text = "Here is the first number to get you started: " + str(num1))
info2.place(x=500, y=75)

product = num1 * num2

label_geuss = Label(root,text = "Take a geuss player")
label_geuss.place(x=500,y=100)

enter_geuss = Entry(root,width = 20)
enter_geuss.place(x=650, y=100)

button_geuss = Button(root, text = "Confirm", command=check_number)
button_geuss.place(x=800,y=100)

geussLabel = Label(root, text = "You have made " + str(geussCount) + " Geusses so far" )
geussLabel.place(x=500, y=135)

root.mainloop()
