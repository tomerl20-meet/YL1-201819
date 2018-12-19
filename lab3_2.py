import turtle
#screen = turtle.Screen()

#screen.addshape("turl.gif")
#turtle.shape("turl.gif")
for i in range(360):
	turtle.forward(90)
	turtle.right(45)
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(40)
	turtle.penup()
	turtle.home()
	turtle.pendown()
	turtle.right(i)
turtle.mainloop()
