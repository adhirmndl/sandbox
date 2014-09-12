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
    col = ["red", "orange", "blue", "yellow", "white", "gray", "green", "magenta", "pink"]
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

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(50,t)
    myWin.exitonclick()

main()
