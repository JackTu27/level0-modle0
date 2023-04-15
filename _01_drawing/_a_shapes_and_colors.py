import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    jack = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    jack.shape('turtle')
    # Set your turtle's speed using .speed(2)
    jack.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    jack.color('green')
    jack.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    jack.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    jack.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        jack.forward(100)
        jack.left(90)


    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    jack.goto(5, 7)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    jack.begin_fill()
    jack.circle(50, steps=30)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    jack.end_fill()
    # Draw 3 more shapes with different fill colors!
    jack.begin_fill()
    for i in range(4):
        jack.forward(100)
        jack.left(90)
    jack.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
