from turtle import *


#lets draw khinkali
bgcolor("#fee8da")
speed(40)

#starting cordinates
penup()
goto(25, 150)
pendown()

#lets start making by corners
begin_fill()
color("#e0b277")
width(5)    
left(180)
forward(50)
left(90)
forward(40)
right(30)
forward(300)

#second corner
penup()
goto(25, 150)
pendown()
left(30)
forward(40)
left(30)
forward(300)

#the floor
right(30)
right(90)
forward(350)
end_fill()

#black detailed top
penup()
goto(25, 110)
pendown()
width(3)
color("#dbb989")
forward(50)

#details inside khinkali
#we will have three details inside so ill use numbers for it
#detail N1(left one)
penup()
goto(-10, 110)
pendown()
left(70)
color("#c2a06d")
width(4)
forward(280)


#detail N2(in center)
penup()
goto(5, 110)
pendown()
right(-20)
forward(265)

#detail N3(the right one)
penup()
goto(20, 110)
pendown()
right(-15)
forward(275)




exitonclick()