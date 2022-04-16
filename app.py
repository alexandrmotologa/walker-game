import turtle as t
from lib import *

windowSetup(WIDTH, HEIGHT)

showMario(marioX, 0)
showCoin(coinX)
showBomb(bombX)

t.listen()
t.onkey(moveRight, 'Right')
t.onkey(moveLeft, 'Left')

t.mainloop()