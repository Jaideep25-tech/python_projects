import turtle
import random
import time

screen = turtle.Screen()  # Create a screen
turtle.title('Happy Mothers Day')
screen.setup(width=800, height=500)
screen.bgcolor('black')
screen.tracer(2)
tt = turtle.Turtle()  # Create a pen by which we will write any thing
tt.hideturtle()  # Hide the Pen Arrow

colors_pen = ['green', 'white', 'blue', 'yellow', 'pink', 'purple', 'violet', 'gray']
colors_fill = ['green', 'blue', 'white', 'yellow', 'pink', 'purple', 'violet', 'gray']
tt.speed('fastest')


def gg():
    for i in range(16):

        x, y = random.randrange(-350, 350), random.randrange(-230, 230)
        tt1 = turtle.Turtle()
        tt1.color(random.choice(colors_pen))

        tt1.write('Happy', font=('chiller', 95, 'italic bold'), align='right')
        time.sleep(1)
        tt1.clear()
        tt1.write('Mothers', font=('chiller', 90, 'italic bold'), align='center')
        time.sleep(1)
        tt1.clear()
        tt1.write('Day', font=('chiller', 95, 'italic bold'), align='left')
        time.sleep(1)
        tt1.clear()
        tt1.write('Happy Mothers Day', font=('chiller', 95, 'italic bold'), align='center')
        time.sleep(1)
        tt1.clear()
        tt.penup()
        tt.goto(x, y)
        tt.pendown()
        tt.begin_fill()
        tt.color(random.choice(colors_pen))
        for i in range(6):
            tt.forward(30)
            tt.right(144)
        tt.end_fill()


while True:
    gg()
    tt.clear()
turtle.mainloop()