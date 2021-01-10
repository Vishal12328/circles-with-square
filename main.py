import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(length, angle):
    for vishal in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for vishal in range(200):
   square(100, 90)
   my_turtle.right(11)
