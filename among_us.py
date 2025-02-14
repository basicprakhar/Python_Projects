# Author: Prakhar Agrawal

from turtle import *
hideturtle()
pensize(10)
fillcolor('skyblue')
speed(8)

right(90)
begin_fill()
forward(50)
for pa_n in [
  (30, 200), (90, 200), (30, 50)
]:
  circle(pa_n[0], 180)
  forward(pa_n[1])
right(90)
forward(60)
end_fill()

penup()
goto(0, 100)
pendown()

fillcolor('white')
begin_fill()
for pa_n in range(2):
  forward(49)
  circle(40, 180)
end_fill()

penup()
goto(-122, 150)
pendown()

fillcolor('skyblue')
begin_fill()
left(180)
for pa_i in [20, 150]:
  forward(pa_i)
  circle(10, 90)
forward(20)
end_fill()
done()

# End of code
