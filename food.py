from turtle import Turtle
import random

SCREEN_SIZE = 600
PADDING = 40
FIELD = 0.5 * (SCREEN_SIZE - PADDING)
COLOR = "tomato"

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed("fastest")
        self.refresh_food()
    

    def refresh_food(self):
        random_x = round(random.randint(-FIELD, FIELD), -1)
        if random_x % 20 != 0:
            random_x += 10
        random_y = round(random.randint(-FIELD, FIELD), -1)
        if random_y % 20 != 0:
            random_y += 10
        self.goto(x=random_x, y=random_y)
