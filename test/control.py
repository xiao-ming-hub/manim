from manimlib import*
class Control_1(Scene):
    def construct(self):
        self.move_dot = MotionMobject(Dot(radius = 0.2))
        where = VGroup(
            Text("x = "), DecimalNumber(),
            Text(", y = "), DecimalNumber()
        ).to_edge(DOWN)
        def update_where(m : VGroup):
            m[1].set_value(self.move_dot.get_center()[0])
            m[3].set_value(self.move_dot.get_center()[1])
            m.arrange()

        where.add_updater(update_where)
        self.add(where, self.move_dot)

class Control_2(Scene):
    def construct(self):
        def button_click(m : Square):
            # self.play(Rotating(m, PI / 2, run_time = 1, rate_function = rush_into))
            to = [UP, DOWN, LEFT, RIGHT]
            self.play(m.animate.shift(random.choice(to)), run_time = 1)

        square = Button(Square(side_length = 1), on_click = button_click)
        self.add(square)
