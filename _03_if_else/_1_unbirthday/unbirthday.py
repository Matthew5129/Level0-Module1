from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    user = simpledialog.askstring(title="user", prompt="when is your birthday?")
    if user == "December 22st":
        messagebox.showinfo(title="user", message="Happy Birthday!")
    else:
        messagebox.showinfo(title="user", message="Happy Unbirthday!")
