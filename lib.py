import turtle as t
from turtle import Turtle
from random import randint

# WINDOW SETUP
marioFrame = 1
marioTo = "right"
marioScore = 0

marioX = 0

WIDTH = 1000
HEIGHT = 500

coinX = randint(-400, +400)
bombX = randint(-400, +400)

# create 3 separate pens
t_mario = Turtle()
t_coin = Turtle()
t_bomb = Turtle()

def showScore():
    global marioScore
    t.hideturtle()
    t.clear()
    t.penup()
    t.setposition(0,-200)
    style = ('Courier', 40, 'bold')
    if marioScore >= 0:
        t.clear()
        t.write(f'{marioScore}', font = style)
    else:
        t.clear()
        t.setposition(-100, -200)
        t.write("HA-HA-HA", font = style)
        t.hideturtle()

def moveRight():
    global marioX, marioFrame, marioTo, marioScore, coinX, bombX

    marioTo = "right"
    width_start = WIDTH / 2 - 50
    if marioX < width_start:
        marioX += 50
        if coinX in range(marioX-40, marioX+40):
            marioScore+=10
            coinX = randint(-400, +400)
            showCoin(coinX)
        if bombX in range(marioX-40, marioX+40):
            marioScore -= 10
            bombX = randint(-400, +400)
            showBomb(bombX)
    else:
        marioX += 0
    marioFrame += 1
    if marioFrame >= 5:
        marioFrame = 1
    showMario(marioX, 0)
    showScore()

def moveLeft():
    global marioX, marioFrame, marioTo, marioScore, coinX, bombX
    
    marioTo = "left"
    width_start = -WIDTH / 2 + 50
    if marioX > width_start:
        marioX -= 50
        if coinX in range(marioX-40, marioX+40):
            marioScore += 10
            coinX = randint(-400, +400)
            showCoin(coinX)
        if bombX in range(marioX-40, marioX+40):
            marioScore -= 10
            bombX = randint(-400, +400)
            showBomb(bombX)
    else:
        marioX += 0
    marioFrame += 1
    if marioFrame >= 5:
        marioFrame = 1
    showMario(marioX, 0)
    showScore()

# WINDOW SIZE
def windowSetup(width, height):
    t.setup(width, height)
    t.showturtle

# DISPLAY AN IMAGE COIN
def showCoin(x):
    global t_coin
    
    name = f'images/coin.gif'
    s = t.Screen()
    s.addshape(name)
    
    t_coin.penup()
    t_coin.setposition(x,0)
    
    t_coin.pendown()
    t_coin.shape(name)

# DISPLAY AN IMAGE BOMB
def showBomb(x):
    global t_bomb

    name = f'images/bomb.gif'
    s = t.Screen()
    s.addshape(name)

    t_bomb.penup()
    t_bomb.setposition(x, 0)

    t_bomb.pendown()
    t_bomb.shape(name)

# DISPLAY THE MAIN CHARACTER
def showMario(x,y):
    global t_mario, marioFrame, marioTo
    
    t_mario.penup()
    name = f'images/mario_{marioTo}({marioFrame}).gif'
    s = t.Screen()
    s.addshape(name)
    
    t_mario.setposition(x,y)
    t_mario.shape(name)