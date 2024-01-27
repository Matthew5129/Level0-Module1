import turtle
from tkinter import messagebox, simpledialog, Tk

"""
* Write a python program that asks the user a minimum of 3 riddles.
simpledialog.askstring(title="What do you call a chic) 
* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct!
"""

user = simpledialog.askstring(title="user", prompt="What do you call a chicken with a bad sunburn?")
if user =="Fried Chicken!":
    messagebox.showinfo("How did u get dat right? Yer a pro at dis!")
else:
    messagebox.showinfo("Wrong!")
