"""
Go to the recipe to run the demonstration before starting this program
"""
x = 125
speed = 10
x2 = 375
speed2 = -10
def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(500, 250)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
def draw():
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    global x
    global speed
    for i in range(35):
        ellipse(x, 125, i * 5, i * 5)
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
    x += speed
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */
    if x == 375:
        speed = -speed
        background("#FFFFFF")
    
    # When the rings reach the left side of the sketch, reverse the direction again
    if x == 125:
        speed = -speed
        background("#FFFFFF")
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
    global x2
    global speed2
    
    for i in range(35):
        ellipse(x2, 125, i * 5, i * 5)
    
    x2 += speed2
    if x2 == 125:
        speed2 = -speed2
        background("#FFFFFF")
    
    if x2 == 375:
        speed2 = -speed2
        background("#FFFFFF")
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
