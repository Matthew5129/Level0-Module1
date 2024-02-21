from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
first_number = simpledialog.askinteger(title="user", prompt="Give me one random number")
second_number = simpledialog.askfloat(title="user", prompt="Give me a second number")
user = simpledialog.askstring(title="user", prompt="Would you like to add, subtract, multiply, or divide?")
if user == "add":
    messagebox.showinfo(None, first_number + second_number)

if user == "subtract":
    messagebox.showinfo(None, first_number - second_number)

if user == "multiply":
    messagebox.showinfo(None, first_number * second_number)

if user == "divide":
    messagebox.showinfo(None, first_number / second_number)


window.mainloop()
