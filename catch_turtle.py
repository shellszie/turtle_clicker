import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Clicker")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic updates for smoother movement

t = turtle.Turtle()
t.shape("turtle")
# t.shapesize(10, 1, 6)
t.color("green")
t.penup()
t.speed(0)

# Create the turtle
# t1 = turtle.Turtle()
# t1.shape("turtle")
# # t.shapesize(10, 1, 6)
# t1.color("green")
# t1.penup()
# t1.speed(0)
#
# t2 = turtle.Turtle()
# t2.shape("turtle")
# t2.color("green")
# t2.penup()
# t2.speed(0)

# for x in range(8):
#   t_x = turtle.Turtle()
#   t2.shape("turtle")
#   t2.color("green")
#   t2.penup()
#   t2.speed(0)

# Score tracker
score = 0

# Display score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

# # Function to move the turtle randomly
def move_turtle():
#     print("in move_turtle " + turt)
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    t.goto(x, y)
    screen.update()  # Update the screen manually
    screen.ontimer(move_turtle, 1000)  # Move every second

# Function to increase score when turtle is clicked
def catch_turtle(x, y):
    global score
    score += 1
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))
    screen.update()  # Ensure score updates properly

# Bind click event to the turtle
t.onclick(catch_turtle)
# t2.onclick(catch_turtle)

# # Start the game
screen.ontimer(move_turtle, 1000)
# screen.ontimer(lambda: move_turtle(t1), 1000)
# screen.ontimer(lambda: move_turtle(t2), 1000)
screen.mainloop()
