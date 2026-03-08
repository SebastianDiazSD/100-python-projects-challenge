from turtle import Turtle

class CodedName(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.start_x = -300
        self.start_y = -50
        self.goto(self.start_x, self.start_y)

        # Decoration turtle for banners and flag
        self.decor = Turtle()
        self.decor.hideturtle()
        self.decor.penup()

    def write_name(self, code):
        self.goto(self.xcor(), self.ycor())
        self.write(code, align="left", font=("Arial", 24, "normal"))
        self.sety(self.ycor() - 40)
        self.setx(self.xcor() + 20)

    def reset_position(self):
        self.clear()
        self.goto(self.start_x, self.start_y)

    def draw_flag_banner(self):
        # Yellow stripe (top half)
        self.decor.goto(-400, 300)
        self.decor.color("gold")
        self.decor.begin_fill()
        for _ in range(2):
            self.decor.forward(800)
            self.decor.right(90)
            self.decor.forward(150)
            self.decor.right(90)
        self.decor.end_fill()

        # Blue stripe (next quarter)
        self.decor.goto(-400, 150)
        self.decor.color("blue")
        self.decor.begin_fill()
        for _ in range(2):
            self.decor.forward(800)
            self.decor.right(90)
            self.decor.forward(75)
            self.decor.right(90)
        self.decor.end_fill()

        # Red stripe (bottom quarter)
        self.decor.goto(-400, 75)
        self.decor.color("red")
        self.decor.begin_fill()
        for _ in range(2):
            self.decor.forward(800)
            self.decor.right(90)
            self.decor.forward(75)
            self.decor.right(90)
        self.decor.end_fill()

    def draw_title_text(self):
        self.decor.goto(0, 260)
        self.decor.color("black")
        self.decor.write("💥 Colombian NATO Name Generator 💥", align="center", font=("Courier", 24, "bold"))

    def show_goodbye(self):
        self.decor.goto(0, -380)
        self.decor.color("green")
        self.decor.write("¡Gracias por jugar, parcero! 🇨🇴", align="center", font=("Arial", 20, "bold"))
