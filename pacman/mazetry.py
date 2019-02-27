from turtle import *



class maze(Turtle):

	def __init__(self, x,y):
		Turtle.__init__(self)
		self.shape("turtle")
		self.goto(x,y)