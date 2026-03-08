from turtle import Turtle

BARRIER_POSITIONS = [-200, 0, 200]

class BarrierBlock(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.goto(x, y)


class BarrierManager:

    def __init__(self):
        self.blocks = []
        self.create_barriers()

    def create_barriers(self):

        for base_x in BARRIER_POSITIONS:
            for row in range(2):
                for col in range(4):
                    block = BarrierBlock(base_x + col * 20, -200 + row * 20)
                    self.blocks.append(block)