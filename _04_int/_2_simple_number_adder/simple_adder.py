from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()
# Write a Python program that asks the user for two numbers.
first_number = simpledialog.askinteger(title="user", prompt="Give me one random number")
second_number = simpledialog.askinteger(title="user", prompt="Give another number")
# Display the sum of the two numbers to the user.
messagebox.showinfo(None, "first_number + second_number = "+str(first_number + second_number))
window.mainloop()
