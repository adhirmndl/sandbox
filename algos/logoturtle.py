import turtle

def drawSpiral(myT, length):
	if length > 0:
		myT.forward(length)
		myT.right(90)
		drawSpiral(myT, length - 5)


def turtleTest():
	myTurtle = turtle.Turtle()
	myWindow = turtle.Screen()
	for i in range(5):
		drawSpiral(myTurtle, 100*i)
		myTurtle.left(90)
		myTurtle.forward(10 * i)
	myWindow.exitonclick()

def otree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)
import random
def tree(length, t):
    col = ['blue','red','green','white','yellow','violet','orange']
    if length > 5:
        t.color(col[random.randrange(0, len(col))])
        t.right(20)
        t.forward(length)
        tree(length - 5, t) 
        t.backward(length)
        t.left(40)
        t.forward(length)
        tree(length - 5, t)
        t.backward(length)
        t.right(20)

def main_tree():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(50,t)
    myWin.exitonclick()

def drawTriangle(points, color, myT):
    myT.fillcolor(color)
    myT.up()
    myT.goto(points[0][0], points[0][1])
    myT.down()
    myT.begin_fill()
    myT.goto(points[1][0], points[1][1])
    myT.goto(points[2][0], points[2][1])
    myT.goto(points[0][0], points[0][1])
    myT.end_fill()

def getMid(p1, p2):
    return (p1[0] + p2[0])/2 , (p1[1] + p2[1])/2

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
