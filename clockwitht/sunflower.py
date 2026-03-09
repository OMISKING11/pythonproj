import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Change background to black
screen.title("Sunflower Pattern")

# Create the turtle
sunflower = turtle.Turtle()
sunflower.speed(0)
sunflower.hideturtle()
sunflower.penup()

# Constants
num_seeds = 200  # Number of seeds
angle = 137.5  # Golden angle in degrees
radius = 8  # Increased radius for better spacing

# Draw the sunflower pattern
for n in range(num_seeds):
    theta = math.radians(angle * n)  # Convert angle to radians
    r = math.sqrt(n) * radius  # Radial distance
    x = r * math.cos(theta)  # X-coordinate
    y = r * math.sin(theta)  # Y-coordinate

    sunflower.goto(x, y)
    sunflower.color("cyan")
    sunflower.setheading(angle * n)  # Set the turtle's heading to face the current angle
    sunflower.begin_fill()
    for _ in range(3):  # Create a pointy triangle shape
        sunflower.forward(15)
        sunflower.left(120)
    sunflower.end_fill()
    radius += 0.1  # Slightly increase the radius for more gap between spots
    size = 0.5 + (n / num_seeds) * 2  # Gradually increase spot size
    sunflower.shapesize(stretch_wid=size, stretch_len=size)  # Apply the size to the spots
sunflower.speed("fastest")  # Set the speed to the fastest

# Keep the window open
screen.mainloop()