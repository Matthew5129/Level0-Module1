import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bobby = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="user", prompt="Choose a shape and store it in a variable")

    if shape == "circle":
        bobby.speed(10)
        bobby.circle(radius=100)
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "square":
        bobby.speed(10)
        for i in range(4):
            bobby.forward(100)
            bobby.right(90)
    if shape == "triangle":
        for i in range(3):
            bobby.speed(5)
            bobby.forward(110)
            bobby.right(120)
    # Call the turtle .done() method
    turtle.done()
