from turtle import *
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("cyan")
        self.speed("fastest")
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.penup()
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)