from turtle import Turtle, Screen
timmy = Turtle()
jimmy = Turtle()
print(timmy)

timmy.shape("turtle") #me
jimmy.shape("turtle") #opo
jimmy.color("coral")
timmy.forward(180)
jimmy.forward(120)
timmy.color("teal")

myScreen = Screen()
print(myScreen.canvheight)
myScreen.exitonclick()
