# Program 3
# This program uses loops to draw a row of 4 identical houses matching the sample house in the assignment

#Ferran Perez Rovira
# Date Completed: sept 12th 2022

# what does your first line of code need to be?  add it below.
import turtle

turtle.speed(10)
turtle.shape('arrow')


# your code for the houses goes here

#functions




#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#  IMPORTANT
#
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
#  EXPAND THE CANVAS TO AS LARGE AS YOU CAN TO FULLY SEE THE HOUSES
def pillar():
  turtle.begin_fill()
  turtle.pendown()
  turtle.fillcolor('beige')
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(400)
  turtle.right(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(50)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(400)
  turtle.right(90)
  turtle.forward(10)
  turtle.left(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(50)
  turtle.penup()
  turtle.end_fill()


def door():
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('gray')
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.circle(50, 180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
def roof():
  turtle.pendown()
  turtle.begin_fill()
  turtle.fillcolor('#9F8170')
  turtle.forward(300)
  turtle.left(100)
  turtle.forward(30)
  turtle.left(80)
  turtle.forward(293.376765)
  turtle.left(80)
  turtle.forward(30)
  turtle.left(100)
  turtle.end_fill()
def window():
  turtle.pendown()
  turtle.begin_fill()
  turtle.fillcolor('light blue')
  for i in range(3):
    if i == 0:
      turtle.forward(40)
      turtle.left(90)
      turtle.forward(40)
      turtle.left(90)
      turtle.forward(40)
      turtle.left(90)
      turtle.forward(40)
      turtle.left(90)
    elif i == 1:
      turtle.left(-90)

      turtle.forward(-20)
      turtle.left(90)
      turtle.forward(40)
      turtle.right(90)
      turtle.forward(40)
      turtle.right(90)
      turtle.forward(40)
      turtle.right(90)
      turtle.forward(40)
    elif i == 2:
      turtle.right(90)
      turtle.forward(20)
      turtle.right(90)
      turtle.forward(-20)
      turtle.forward(60)
  turtle.end_fill()
  turtle.penup()


def house():
  turtle.penup()
  pillar()
  turtle.forward(25)
  door()
  turtle.forward(25)
  pillar()
  turtle.forward(-250)
  turtle.right(-90)
  turtle.forward(440)
  turtle.right(90)
  turtle.forward(-25)
  roof()
  turtle.penup()
  turtle.forward(80)
  
  turtle.right(90)
  turtle.forward(70)
  
  turtle.left(90)
  window()
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(90)
  turtle.right(270)
  window()
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(80)
  turtle.right(270)
  window()

  turtle.forward(-210)
  turtle.left(90)
  
  turtle.forward(87)
  turtle.left(90)
  turtle.forward(20)
  turtle.right(90)
  window()
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(90)
  turtle.right(270)
  window()
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.forward(80)
  turtle.right(270)
  window()

  
  turtle.forward(140)
  turtle.left(90)
  turtle.forward(130)




#CODE
turtle.penup()
turtle.goto(-700,-250)

for i in range(5):
  house()