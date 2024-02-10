from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    user = simpledialog.askstring(title="user", prompt="What is your name?")
    if user == "Matthew":
        messagebox.showinfo(title="user", message="You are awesome!")
    elif user == "Maddox":
        messagebox.showinfo(title="user", message="You are awesome and sus and abusive sometimes! (no offense)")
    elif user == "Hello":
        messagebox.showinfo(title="user", message="")
    elif user == "Ben":
        messagebox.showinfo(title="You are the suspicious one who needs more improved behavior!")
    elif user == "Please stop asking me that it's starting to annoy me!":
        messagebox.showinfo(title="user", message="I understand you're feelings. I'll try not asking that question anymore.")
    else:
        messagebox.showinfo(title="user", message="Sorry, that is not one of the names. Try again!")
