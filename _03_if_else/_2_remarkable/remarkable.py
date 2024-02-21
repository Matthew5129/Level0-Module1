from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    user = simpledialog.askstring(title="user", prompt="What is your name?")
    if user == "Matthew":
        messagebox.showinfo(title="user", message="You are awesome!")
    elif user == "Maddox":
        messagebox.showinfo(title="user", message="You are awesome and sus")
    elif user == "Hello":
        messagebox.showinfo(title="user", message="Hello")
    elif user == "Ben":
        messagebox.showinfo(title="You are the suspicious one who needs more improved behavior!")
    elif user == "Please stop asking me that it's starting to annoy me!":
        messagebox.showinfo(title="user", message="Ok since you are annoyed i will stop now. PS i am an AI")
    else:
        messagebox.showinfo(title="user", message="Sorry, that is not one of the names. Try again!")
