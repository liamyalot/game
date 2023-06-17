import turtle
import time
from playsound import playsound
import random

def left():
    global moveShipBy
    moveShipBy = -3
    
def right():
    global moveShipBy
    moveShipBy = 3
    
def space():
    global bullet
    global spaceship
    
    if bullet.isvisible() == False:
        bullet.goto(spaceship.xcor(), spaceship.ycor()+45)
        bullet.showturtle()
        playsound("kiblast.mp3", False)
        
def getEnemies():
    e = None
    enemies = []
    for x in range(1,26):
        e= turtle.Turtle()
        e.hideturtle()
        e.shape("enemy.gif")
        e.penup()
        e.goto(random.randint(-350, 350), int(800*x))
        e.showturtle()
        enemies.append(e)
        
    return enemies
    
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

scr = turtle.Screen()
scr.title("SPACE ATTACK")
scr.setup(800,600)
scr.bgpic("space-bg.gif")
scr.tracer(0)

turtle.register_shape("ship.gif")
turtle.register_shape("bullet.gif")
turtle.register_shape("enemy.gif")

spaceship = turtle.Turtle()
spaceship.shape("ship.gif")
spaceship.penup()
spaceship.speed(0)
spaceship.goto(0, -200)

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.shape("bullet.gif")
bullet.penup()

enemies = getEnemies()

moveShipBy = 0

while True:
    
    spaceship.forward(moveShipBy)
    
    if bullet.isvisible():
        bullet.setheading(90)
        bullet.forward(25)
        
    if bullet.ycor() > (scr.window_height()/2):
        bullet.hideturtle()
    

    
    if spaceship.xcor() > 325:
        moveShipBy = 0
    elif spaceship.xcor() < -325:
        moveShipBy = 0
        
        for enemy in enemies:
            if (enemy.ycor() > -350):
                enemy.setheading(270)
                enemy.forward(3)
    
    scr.update()
    time.sleep(0.02)