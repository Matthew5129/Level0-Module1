from tkinter import messagebox, simpledialog
import tkinter as tk
tk.Tk()

score = 0
user = simpledialog.askstring(title="Question 1", prompt="What did the scientist get when he crossed a chicken and a cow?")
if user == "Roost beef":
    messagebox.showinfo(title="user", message="Good!")
    score = 1
else:
    messagebox.showinfo(title="user", message="Wrong!")
    score = 0

user = simpledialog.askstring(title="Question 2", prompt="Imagine you are in the days of the dinosaurs, and one is chasing after you, about to eat you... What do you do?")
if user == "Easy, stop imagining":
    messagebox.showinfo(title="user", message="Nice!")
    score = 2
else:
    messagebox.showinfo(title="user", message="Wrong!")
    score = -1

user = simpledialog.askstring(title="Question 3", prompt="What do you call a stampede of giant ducks?")
if user == "An earthquack":
    messagebox.showinfo(title="user", message="Awesome!")
    score = 3
else:
    messagebox.showinfo(title="user", message="Wrong!")
    score = -2

user = simpledialog.askstring(title="Question 4", prompt="Why did the chicken egg laugh when he performed funny jokes with his ventriloquist dummy?")
if user == "He cracked himself up":
    messagebox.showinfo(title="user", message="Well done!")
    score = 4
else:
    messagebox.showinfo(title="user", message="Wrong!")
    score = -3

user = simpledialog.askstring(title="Question 5", prompt="This is as light as a feather, yet no man can hold it for long. What am I?")
if user == "Your breath":
    messagebox.showinfo(title="user", message="Well done!")
    score = 5
else:
    messagebox.showinfo(title="user", message="Wrong!")
    score = -4

user = messagebox.showinfo(title="user", message="This is the last riddle of them all....If you get it right, you'll be the champion of riddler.py.")
user = simpledialog.askstring(title="Question 6", prompt="What toys do baby snakes take to bed?")
if user == "Their rattles":
    messagebox.showinfo(title="user", message="CONGRATULATIONS! YOU ARE OFFICIALLY THE CHAMPION OF RIDDLER.PY! YOU MAY NOW MOVE ON TO THE NEXT PYTHON ACTIVITY!")
    score = 6
else:
    messagebox.showinfo(title="user", message="Don't worry! You'll get it next time!")
    score = -100
