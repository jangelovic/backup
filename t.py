from turtle import *

yeetTurtle = Turtle()
screen = yeetTurtle.getscreen()

yeetTurtle.forward(50)

def writeName():
	name = screen.textinput("name box", "What is your name")
	yeetTurtle.write(name, move=True, align="left", font=("Arial",30,"normal"))
	screen.listen()

screen.onkey(writeName, "w")

screen.listen()


screen.mainloop()