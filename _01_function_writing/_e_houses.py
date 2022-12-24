"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import random
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    carlos = turtle.Turtle()
    carlos.penup()
    carlos.goto(-300,-300)
    carlos.pendown()
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    def draw_house(height):
        pointyRoof = True
        if height == 'small':
            heightInt = 60
        elif height == 'medium':
            heightInt = 120
        elif height == 'large':
            heightInt = 250
            pointyRoof = False

        carlos.left(90)
        carlos.forward(heightInt)
        if pointyRoof == True:
            draw_pointy_roof()
        else:
            draw_flat_roof()
        carlos.forward(heightInt)
        carlos.left(90)
        carlos.pencolor("green")
        carlos.forward(25)
        carlos.pencolor("black")

    def draw_pointy_roof():
        carlos.right(60)
        carlos.forward(10)
        carlos.right(60)
        carlos.forward(10)
        carlos.right(60)

    def draw_flat_roof():
        carlos.right(90)
        carlos.forward(25)
        carlos.right(90)
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    for i in range(9):
        size = random.randint(1,3)
        if size == 1:
            sizeString = 'small'
        if size == 2:
            sizeString = 'medium'
        if size == 3:
            sizeString = 'large'
        draw_house(sizeString)
        i += 1
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    pass
