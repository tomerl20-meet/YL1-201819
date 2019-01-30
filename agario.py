import turtle
import time
import random
import math
from ball import Ball
global score
score = 0
turtle.colormode(1)
turtle.tracer(0)
turtle.hideturtle()
running = True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball = Ball(-10, 0, 2, 2, 40, "pink")
number_of_balls = 5
minimum_ball_radius = 10
maximum_ball_radius = 70
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
BALLS=[]
for i in range (number_of_balls):
	x=random.randint(-screen_width+maximum_ball_radius,screen_width - maximum_ball_radius)
	y= random.randint(-screen_height + maximum_ball_radius,screen_height-maximum_ball_radius)
	dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	r = random.randint( minimum_ball_radius, maximum_ball_radius)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x, y, dx, dy, r, color)
	BALLS.append(new_ball)

def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width,screen_height)

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	d = math.sqrt(math.pow(ball_b.xcor()-ball_a.xcor(),2)+math.pow(ball_b.ycor()-ball_a.ycor(),2))
	if d <=ball_a.r+ball_b.r:
		return True
	else:
		return False
def check_all_balls_collision():
	global running, score
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_a, ball_b):
				r1 = ball_a.r
				r2 = ball_b.r
				
				x=random.randint(-screen_width+maximum_ball_radius,screen_width - maximum_ball_radius)
				y= random.randint(-screen_height + maximum_ball_radius,screen_height-maximum_ball_radius)
				dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				while dx == 0:
					dx = random.randint(minimum_ball_dx,maximum_ball_dx)

				dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				while dy == 0:
					dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				r = random.randint( minimum_ball_radius, maximum_ball_radius)
				color = (random.random(), random.random(), random.random())
				if ball_a.r<ball_b.r:
					if ball_b == my_ball:
						score+=10
						turtle.clear()
						turtle.pencolor("pink")
						turtle.write("Score: " + str(score), align="left", font=('ariel',40,'normal'))
						
					if ball_a == my_ball:
						turtle.clearscreen()
						turtle.bgcolor("black")
						print("eaten")
						turtle.pencolor("red")
						turtle.write("game over!", align="center", font=('arial',100,'normal'))
						turtle.pencolor("purple")
						turtle.penup()
						turtle.goto(-188, 150)
						turtle.pendown()
						turtle.write("youre score:" + str(score), align="left", font=('ariel',50,'normal'))
						turtle.hideturtle()
						running = False			
					ball_a.new_ball(x,y,dx,dy,r,color)
					ball_b.r = ball_b.r + 1
					ball_b.shapesize(ball_b.r/10)
				else:
					if ball_a == my_ball:
						score+=10
						turtle.clear()
						turtle.pencolor("pink")
						turtle.write("Score: " + str(score), align="left", font=('ariel',40,'normal'))
					if ball_b == my_ball:
						turtle.clearscreen()
						turtle.bgcolor("black")
						
						print("eaten")

						turtle.pencolor("red")
						turtle.write("game over!", align="center", font=('arial',100,'normal'))
						turtle.pencolor("purple")
						turtle.penup()
						turtle.goto(-188, 150)
						turtle.pendown()
						turtle.write("youre score:" + str(score), font=('ariel',50,'normal'))
						turtle.hideturtle()
						running = False
					ball_b.new_ball(x,y,dx,dy,r,color)
					ball_a.r = ball_a.r + 1
					ball_a.shapesize(ball_a.r/10)
	if ball_a.r > maximum_ball_radius or ball_b.r > maximum_ball_radius:
		#running = False
		print("w")
		ball_b.new_ball(x,y,dx,dy,r,color)
		ball_a.new_ball(x,y,dx,dy,r,color)
def movearound():
	x = turtle.getcanvas().winfo_pointerx()-screen_width*2
	y =screen_height*1.44 -turtle.getcanvas().winfo_pointery()
	my_ball.goto(x,y)
while running==True:
	if screen_width!=turtle.getcanvas().winfo_width()/2 or screen_height!=turtle.getcanvas().winfo_height()/2:
		screen_width = turtle.getcanvas().winfo_width()/2
		screen_height = turtle.getcanvas().winfo_height()/2
	movearound()
	move_all_balls()
	check_all_balls_collision()
	turtle.update()
	time.sleep(0.03)





turtle.update()
turtle.mainloop()