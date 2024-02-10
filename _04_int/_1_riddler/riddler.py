from tkinter import messagebox, simpledialog
import tkinter as tk
tk.Tk()

user = simpledialog.askstring(title="Question 1", prompt="What did the scientist get when he crossed a chicken and a cow?")
if user == "Roost beef!":
    messagebox.showinfo(title="user", message="Good!")
else:
    messagebox.showinfo(title="user", message="Wrong!")


user = simpledialog.askstring(title="Question 2", prompt="Imagine you are in the days of the dinosaurs, and one is chasing after you, about to eat you... What do you do?")
if user == "Easy, stop imagining!":
    messagebox.showinfo(title="user", message="Nice!")
else:
    messagebox.showinfo(title="user", message="Wrong!")


user = simpledialog.askstring(title="Question 3", prompt="What do you call a stampede of giant ducks?")
if user == "An earthquack!":
    messagebox.showinfo(title="user", message="Awesome!")
else:
    messagebox.showinfo(title="user", message="Wrong!")


user = simpledialog.askstring(title="Question 4", prompt="Why did the duck laugh when he performed funny jokes with himself with his ventriloquist dummy?")
if user == "He quacked himself up!":
    messagebox.showinfo(title="user", message="Well done!")
else:
    messagebox.showinfo(title="user", message="Wrong!")

messagebox.showinfo(title="user", message="")
