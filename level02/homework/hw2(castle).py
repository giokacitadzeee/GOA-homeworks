from turtle import *

#main stuff
speed(40)
bgcolor("cyan")



#starting cordinates
penup()
goto(-400, -400)
left(90)
pendown()

#castle1
color("red")
begin_fill()
forward(700)
left(90)
forward(250)
left(90)
forward(700)
left(90)
forward(250)
end_fill()

#windows castle
color("black")
penup()
goto(-550, -100)
pendown()
color("white")
begin_fill()
left(90)
left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

#window2 castle
penup()
goto(-550, 100)
pendown()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#cubes on the castle
penup()
color("gray")
goto(-400, 300)
begin_fill()
pendown()
right(90)
forward(60)
left(90)
forward(70)
left(90)
forward(60)
end_fill()

#flag
color("black")
goto(-525, 300)
right(90)
right(90)
width(5)
forward(120)
left(90)
color("red")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#another cube
penup()
color("gray")
width(1)
goto(-650, 300)
begin_fill()
pendown()
left(90)
forward(60)
right(90)
forward(70)
right(90)
forward(60)
end_fill()

#wall
penup()
goto(-650, 100)
pendown()
right(90)
forward(350)

#wall with gate
penup()
goto(-400, 100)
pendown()
left(180)
forward(800)
penup()
goto(400, -400)
pendown()


#second castle
color("green")
begin_fill()
left(90)
forward(700)
right(90)
forward(250)
right(90)
forward(700)
right(90)
end_fill()
color("black")
forward(1050)



#cube on second castle
penup()
goto(400, 300)
color("gray")
begin_fill()
pendown()
right(90)
forward(60)
right(90)
forward(70)
right(90)
forward(60)
end_fill()

#second cube on second tower
penup()
goto(650, 300)
begin_fill()
pendown()
left(180)
forward(60)
left(90)
forward(70)
left(90)
forward(60)
end_fill()
color("black")

#flag between
goto(525, 300)
left(180)
width(5)
forward(120)
right(180)
color("green")
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

#another wall
penup()
goto(650, 100)
pendown()
width(1)
color("black")
right(90)
forward(300)


#floor for the castle
penup()
goto(-950, -400)
pendown()
goto(950, -400)


#windows castle2
penup()
goto(550, -100)
color("white")
begin_fill()
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


#second castle window2
penup()
goto(550, 100)
color("white")
begin_fill()
pendown()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#gate
penup()
goto(-150, -400)
pendown()
left(90)
color("grey")
begin_fill()
forward(300)
right(90)
forward(300)
right(90)
forward(300)
end_fill()

#sun
penup()
goto(-75, 300)
pendown()
color("orange")
begin_fill()
circle(150)
end_fill()


exitonclick()