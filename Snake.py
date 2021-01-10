import turtle
import time
import random

delay = 0.08

# Starting Score
score = 0
high_score = 0

# Create the window and set the background colour
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0) # Turns off the screen updates

# Create the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Create the snake food
food = turtle.Turtle()
food.speed(0)
food.shape("turtle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Write score on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Game Over Message
game_over = turtle.Turtle()
game_over.speed(0)
game_over.shape("square")
game_over.color("yellow")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 200)


# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
def game_over_message():
    window.bgcolor("red")
    game_over.write("Game Over", align="center", font=("Courier", 35, "normal"))
    time.sleep(3)
    # Reset the background color
    window.bgcolor("blue")
    # Delete the Game Over message
    game_over.clear()

def reset_game():
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    
    # Clear the segments list
    segments.clear()

    # Reset the score
    score = 0
    
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Reset the speed
    delay = 0.08

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        game_over_message()
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        reset_game()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            game_over_message()
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            reset_game()

    time.sleep(delay)

window.mainloop()


