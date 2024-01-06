import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Make a new turtle
    Teddy = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="user", prompt="Choose a shape and store it in a variable")

    if shape =="circle":
        Teddy.speed(5)
        Teddy.circle(radius=100)
    # Draw the shape requested by the user using if-elif-else statements
    elif shape =="square":
        Teddy.speed(5)
        for i in range(4):
            Teddy.forward(100)
            Teddy.right(90)
    elif shape =="triangle":
        for i in range(3):
            Teddy.forward(100)
            Teddy.right(120)
    # Call the turtle .done() method
    turtle.done()
