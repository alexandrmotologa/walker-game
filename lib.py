import turtle as t

# WINDOW SETUP
marioFrame = 1

marioX = 0
marioTo = "Right"
WIDTH = 1000
HEIGHT = 500

def moveRight():
    global marioX
    global marioFrame
    global marioTo
    marioTo = "Right"
    width_start = WIDTH / 2 - 50
    if marioX < width_start:
        marioX += 50
    else:
        marioX += 0
    marioFrame += 1
    if marioFrame >= 5:
        marioFrame = 1
    showMario(marioX, 0)

def moveLeft():
    global marioX
    global marioFrame
    global marioTo
    marioTo = "Left"
    width_start = -WIDTH / 2 + 50
    if marioX > width_start:
        marioX -= 50
    else:
        marioX += 0
    marioFrame += 1
    if marioFrame >= 5:
        marioFrame = 1
    showMario(marioX, 0)

def windowSetup(width, height):
    t.setup(width, height)
    t.showturtle

# DISPLAY AN IMAGE
def showImage(name):
    s = t.Screen()
    s.addshape(name)
    t.shape(name)

# DISPLAY THE MAIN CHARACTER
def showMario(x,y):
    t.penup()
    global marioFrame
    if marioTo == "Right":
        name = f'images/mario_right({marioFrame}).gif'
    if marioTo == "Left":
        name = f'images/mario_left({marioFrame}).gif'
    s = t.Screen()
    s.addshape(name)
    
    t.setposition(x,y)
    
    t.shape(name)