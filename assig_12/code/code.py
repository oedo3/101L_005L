 ########################################################################
 ##
 ## CS 101 Lab
 ## Program 12
 ## Name: Osay E.
 ## Email: ooenw7@umsystem.edu
 ##
 ## PROBLEM : Create write a program that uses the turtle import
 ## ERROR HANDLING
 ##      N/A
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import turtle
import time
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)

class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.begin_fill()
        turtle.color(self.fillcolor)
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()
if __name__ == "__main__":
    p = Point(-100, 100, "blue")
    p.draw()
    box = Box(-100, 100, 50, 25, "black")
    box.draw()
    b = BoxFilled(1, 2, 100, 200, "red", "blue")
    b.draw()
    circle = Circle(-200, 150, 50, 'black')
    circle.draw()
    c = CircleFilled(-200, 150, 50, 'red', 'yellow')
    c.draw()
    time.sleep(1)