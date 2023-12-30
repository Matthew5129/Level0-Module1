import math
import tkinter
from tkinter import simpledialog, messagebox
root = tkinter.Tk()

# Write a Python program that asks the user for the radius of a circle.
radius = simpledialog.askinteger(title="user", prompt="Give me the radius of a circle")
# Next, ask the user if they would like to calculate the area or circumference of a circle.
user = simpledialog.askstring(title="user", prompt="Would you like to calculate the area or circumference of a circle?")
value = 0
if user == "area":
    value = math.pi*radius*radius
elif user =="circumference":
    value = 2*math.pi*radius
messagebox.showinfo(title="user", message=value)
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr
