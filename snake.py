from turtle import Turtle
from random import choice

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_VECTOR = choice([UP, DOWN, RIGHT])

''' COLORS '''
HEAD = "#487C27"
TAIL_PRIMARY = "#487C27"
TAIL_SECONDARY = "#243E13"
MIX_FACTOR = 5

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = STARTING_VECTOR
        self.can_change_direction = True
        self.head.setheading(STARTING_VECTOR)

    def create_snake(self):
        first_position = True
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            if first_position:
                self.segments[0].color(HEAD)
                self.segments[0].shape("circle")
                self.segments[0].shapesize(1, 2)
                first_position = False

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        if len(self.segments) % MIX_FACTOR == 0:
            new_segment.color(TAIL_SECONDARY)
        else:
            new_segment.color(TAIL_PRIMARY)
        new_segment.penup()
        new_segment.goto(position)
        new_segment.setheading(STARTING_VECTOR)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.can_change_direction = True  # Allow direction change after moving

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # Moving directions
    def up(self):
        if self.head.heading() != DOWN and self.can_change_direction:
            self.head.setheading(UP)
            self.can_change_direction = False  # Prevent further direction change

    def down(self):
        if self.head.heading() != UP and self.can_change_direction:
            self.head.setheading(DOWN)
            self.can_change_direction = False

    def left(self):
        if self.head.heading() != RIGHT and self.can_change_direction:
            self.head.setheading(LEFT)
            self.can_change_direction = False

    def right(self):
        if self.head.heading() != LEFT and self.can_change_direction:
            self.head.setheading(RIGHT)
            self.can_change_direction = False  
