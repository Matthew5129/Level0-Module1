from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
first_number = simpledialog.askinteger(title="user", prompt="Give me one random number")
second_number = simpledialog.askfloat(title="user", prompt="Give me a second number")
user = simpledialog.askstring(title="user", prompt="Would you like to add, subtract, multiply, or divide?")
if user == "multiply":
    messagebox.showinfo(None, first_number * second_number)


window.mainloop()
