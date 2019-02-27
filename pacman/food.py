import turtle
from turtle import *
turtle.penup()

turtle.register_shape("banana.gif")


class Food(Turtle):

	def __init__(self, x,y):
		Turtle.__init__(self)
		self.shape("banana.gif")
		self.pu()

		self.goto(x,y)