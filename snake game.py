import turtle
import random
import time 


delay = 0.1
score = 0
highscore = 0

win = turtle.Screen()

win.title("Snake Game")
win.bgcolor("black")
win.setup(width = 600, height = 600)
win.tracer(0)


#making snake's head

head = turtle.Turtle()
head.color("white")
head.shape('square')
head.speed(0)
head.direction = "Stop"
head.penup()
head.goto(0,0)

#making food for snake

food = turtle.Turtle()
colors = random.choice(['red','green'])
shapes = random.choice(['square','circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)



segments = []

#drawing the attributes

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)


pen.write("Score : 0  High Score : 0",align = "center", font = ("arial", 24, "bold"))


#function for moving the snake

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x-20)

win.listen()
win.onkeypress(go_up, "w")
win.onkeypress(go_down, "s")
win.onkeypress(go_right, "d")
win.onkeypress(go_left, "a")

while True:
    win.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red','green'])
        shapes = random.choice(['square','circle'])
        
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        score = 0
        delay = 0.1
        pen.clear()
        
        pen.write("Score : {}  High Score : {}".format(score,highscore),align = "center",font = ("arial", 24, "bold"))
    
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.01
        score += 10

        if score > highscore:
            highscore = score
        
        pen.clear()
        pen.write("Score  {}  High Score  {}".format(score,highscore),align = "center",font = ("arial", 24, "bold"))
    
    for index in range(len(segments) -1,0,-1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red','green'])
            shapes = random.choice(['square','circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()

            pen.write("Score  {}  High Score  {}".format(score,highscore),align = "center",font = ("arial", 24, "bold"))
    
    time.sleep(delay)


win.mainloop()

