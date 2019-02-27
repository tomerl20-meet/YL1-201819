import turtle
from ghost import *
turtle.ht()
ghost = ghost(0,0,3)
while True:
	ghost.forward(2)
def change_direction():
	if ghost.x == obj.x and ghost.y == obj.y:
		ghost.random.choice(directions)
turtle.mainloop()