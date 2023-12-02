from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    user = simpledialog.askstring(title="user", prompt="What is your name?")
    if user == "Matthew":
      messagebox.showinfo(title="user", message="You are cool")
    elif user == "Maddox":
      messagebox.showinfo(title="user", message="You are also cool")
    elif user == "Shrek":
      messagebox.showinfo(title="user", message="You are a fat ogre")
