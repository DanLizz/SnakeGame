from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle("square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake.append(snake_part)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for snake_part_no in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[snake_part_no - 1].xcor()
            new_y = self.snake[snake_part_no - 1].ycor()
            self.snake[snake_part_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for snake_part in self.snake:
            snake_part.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
