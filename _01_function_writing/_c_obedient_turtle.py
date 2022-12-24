"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
def square():
    for i in range(4):
        carlos.forward(100)
        carlos.right(90)

def triangle():
    for i in range(3):
        carlos.right(120)
        carlos.forward(100)

def circle():
    for i in range(360):
        carlos.forward(1)
        carlos.right(1)

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Create a turtle.
    carlos = turtle.Turtle()
    carlos.pendown()
    carlos.shape('turtle')
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.

    #   3. Ask the user for the for a shape to draw.
    shape = simpledialog.askstring("Shape", "What shape do you want to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)


    if shape == 'square':
        square()
    elif shape == 'triangle':
        triangle()
    elif shape == 'circle':
        circle()

