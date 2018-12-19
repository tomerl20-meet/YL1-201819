from turtle import *
colormode(255) 
class Square(Turtle):
 def __init__(self, side):
   Turtle.__init__(self)
   self.side = side
   self.shape("square")
   self.shapesize(side*side)
 def random_color(self):
 	r = random.randit(0,255)
 	g = random.randit(0,255)
 	b = random.randit(0,255)
 	self.color(r,g,b)
S = Square(5)
S.random_color()

mainloop()