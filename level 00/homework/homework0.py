from turtle import *


#we want to paint house

#step 1: draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")
left(90)
forward(100)   #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20,180)
pendown()

color("blue")
left(30)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)

penup()
goto(180,180)
pendown()

forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)

exitonclick()