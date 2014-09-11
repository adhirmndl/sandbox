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

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

main()
