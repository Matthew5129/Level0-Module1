from tkinter import *
import tkinter as tk
from tkinter import simpledialog

window_width = 600
window_height = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
color = simpledialog.askstring(title="bob", prompt="what color would you like?")
# 2. Use if-else statements to draw the tomato in the color that they chose

#    You can modify the code below or draw your own tomato
canvas.create_rectangle(290, 150, 310, 250, fill="green")
canvas.create_oval(75, 200, 400, 450, fill=color, outline=color)
canvas.create_oval(200, 200, 525, 450, fill=color, outline=color)

root.mainloop()
