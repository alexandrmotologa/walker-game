import turtle as t
from lib import *

windowSetup(WIDTH, HEIGHT)

showMario(marioX, 0)
t.listen()
t.onkey(moveRight, 'Right')
t.onkey(moveLeft, 'Left')

t.mainloop()