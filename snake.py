from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DEGREE = 90
DOWN_DEGREE = 270
LEFT_DEGREE = 180
RIGHT_DEGREE = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITIONS:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN_DEGREE:
            self.segments[0].setheading(UP_DEGREE)

    def down(self):
        if self.segments[0].heading() != UP_DEGREE:
            self.segments[0].setheading(DOWN_DEGREE)

    def left(self):
        if self.segments[0].heading() != RIGHT_DEGREE:
            self.segments[0].setheading(LEFT_DEGREE)

    def right(self):
        if self.segments[0].heading() != LEFT_DEGREE:
            self.segments[0].setheading(RIGHT_DEGREE)