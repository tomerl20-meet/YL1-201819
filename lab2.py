import tkinter as tk
from tkinter import simpledialog

#a = [1,2,3,4,5]

#def num(list1):
#	b=[list1[0],list1[-1]]
#	return b

#d=[]
#print(num(a))
#c= [1,1,2,3,5,8,13,21,34,55,89]
#for num in c :
#	if num<5:
#		d.insert(1,num)
#print(d)


 #o = []
 #v = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 #f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#for num in v:
#	if num==
#		o.insert(1,num)
#print(o)
d=[]
a= [1,1,2,3,5,8,13,21,34,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]
for num in range(len(b)):
	c = b[num]
	for i in range(len(a)):
		if a[i]==c:
			d.append(c)
print(d)			


#answer = simpledialog.askstring("Input", "enter a number",parent=tk.Tk())
answer = input("enter a number")
for e in range(answer):
	if e!=0 and answer%e==0 and e!=1 and e!=answer:
		print("not a prime number")
		break
