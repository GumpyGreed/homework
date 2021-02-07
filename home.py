import turtle

screen = turtle.getscreen()
t = turtle.Turtle()



class DrowShape:
    def draw(self, sides, angle):
        for distance in sides:
            t.forward(distance)
            t.left(angle)

class Roof(DrowShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 120

class Wall(DrowShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90

class Door(DrowShape):
    def __init__(self, sides):
        self.sides = sides
        self.angle = 90

h1 = Wall([100]*4)
h1.draw(h1.sides, h1.angle)
t.penup()
t.left(90)
t.forward(100)
t.right(90)
t.pendown()
h2 = Roof([100]*3)
h2.draw(h2.sides, h2.angle)
t.penup()
t.right(90)
t.forward(100)
t.left(90)
t.forward(60)
t.left(90)
t.pendown()
h3 = Door([20]*4)
h3.draw(h3.sides, h3.angle)

screen.mainloop()