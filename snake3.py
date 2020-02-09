#/usr/bin/env python3
#using turtle module
import turtle
import time
import random

delay=0.1# delay the while loop
score=0
#file link
with open('C:\\Users\\Lenovo\\PycharmProjects\\snake\\highscore.txt', 'r') as file:
    high_score=int(file.read())
    file.close()

#create a screen
wn=turtle.Screen()#creates a window
wn.title("Snake Game using Python3")
wn.bgcolor('black')#background color
wn.setup(width=600, height=600)#screen setup
wn.tracer(0)#turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction='stop'

#createing food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-260,260),random.randint(-260,260))

#list for snake body
segments=[]

#create the score
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.shape('square')
pen.penup()
pen.hideturtle()
pen.goto(0, -260)
pen.write("Score:0  High Score:"+str(high_score), align='center', font=('Courier', 24, 'normal'))

#fuctions for key press
def go_up():
    if head.direction!='down':
        head.direction='up'

def go_down():
    if head.direction != 'up':
        head.direction='down'

def go_right():
    if head.direction != 'left':
        head.direction='right'

def go_left():
    if head.direction != 'right':
        head.direction='left'


#function to move snake
def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)

#keybord binding(on press)
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

#main game loop
while True:
    wn.update()
    #check for collision with borders
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction='stop'

        #hide or clear the body segements
        for seg in segments:
            seg.goto(1000,1000)
        segments.clear()

        #reset the score
        score=0
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score, high_score), align='center', font=('Courier', 24, 'normal'))

        #reset delay
        delay=0.1

    #check the body collision
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction='stop'

            #clear and hide the body segments
            for seg in segments:
                seg.goto(1000, 1000)
            segments.clear()

            # reset the score
            score = 0
            pen.clear()
            pen.write("Score:{}  High Score:{}".format(score, high_score), align='center',
                      font=('Courier', 24, 'normal'))

            # reset delay
            delay = 0.1

    #check the snake head collision with food
    if head.distance(food)<20:#move the food
        x=random.randint(-260, 260)
        y=random.randint(-260, 260)
        food.goto(x,y)

        #create the segments
        newSegment=turtle.Turtle()
        newSegment.speed(0)
        newSegment.penup()
        newSegment.color('grey')
        newSegment.shape('square')
        segments.append(newSegment)

        #update the score
        score+=10
        if score>high_score:
            with open('C:\\Users\\Lenovo\\PycharmProjects\\snake\\highscore.txt','w') as file:
                high_score = score
                file.write(str(high_score))
                file.close()

        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score), align='center', font=('Courier', 24, 'normal'))

        #Increase the speed
        delay-=0.001

    #move the oth segment where the head is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    #move the segment where the privious segment is there
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x, y)

    move()

    time.sleep(delay)


wn.mainloop() #infinte loop