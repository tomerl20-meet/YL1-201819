from turtle import*
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 = Ball(90, "green", 4)
ball2 = Ball(40, "black", 4)

def check_collision(b1, b2):
	r1 = b1.radius
	r2 = b2.radius
	D = math.sqrt(math.pow((b2.xcor()-b1.xcor()),2) + math.pow((b2.ycor()-b1.ycor()),2))
	if 	r1+r2 >= D:
		b1.color("pink")
		print("collision")
	else:
		print("not collision")

check_collision(ball1,ball2)

ball_list = (ball1, ball2)
def list_collision(ball_list) 


turtle.mainloop()