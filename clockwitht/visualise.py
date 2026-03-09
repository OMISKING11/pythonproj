import turtle as a
import random

# Set up the screen
win = a.Screen()
win.bgcolor("black")
colours = "red", "yellow", "blue", "green", "pink", 
"purple", "violet"

# Create a turtle
t = a.Turtle()
t.speed(0)
t.pensize(0.5)

# Function to draw an circle
def draw_circle(t, size):
    for _ in range(360):
        # colour = random.choice(colours)
        t.pencolor("white")
        t.forward(size)
        t.right(1)
i = 1
while i < 10:
    draw_circle(t, 2)
    t.right(3.1415926535897932384626433832795)
    # draw_circle(t, 1)
    # t.right(45)

a.done()


        
    