import turtle
from turtle import *
turtle.penup()

turtle.register_shape("ghost.gif")
obj = turtle.clone()
obj.goto(200,0)

class ghost(Turtle):

	def __init__(self, x,y,speed):
		Turtle.__init__(self)
		self.shape("ghost.gif")
		self.pu()
		self.speed(speed)
		self.speed = speed
		self.direction = "up"

		self.goto(x,y)
	def up():
		self.y = self.y + self.speed
	def down():
		self.y = self.y - self.speed
	def right():
		self.x = self.x + self.speed
	def left():
		self.x = self.x - self.speed
	def move_ghost():
		directions = ["up", "down", "right", "left"]
		index = random.randint(0,3)
		direction = directions[index]
		while !CanMove(direction):
			index = random.randint(0,3)
			direction = directions[index]
		ghost.goto(self.xcor(),self.ycor)
		if direction == "Right" :
			self.x = self.x + self.speed
		if direction == "Left" :
			self.x = self.x - self.speed
		if direction == "Up" :
			self.y = self.y + self.speed
		if direction=="Down" :
			self.y = self.y - self.speed
		self.goto(self.x,self.y)
		while True:
			self.goto(self.x,self.y)
