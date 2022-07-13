from manimlib import*
class UpdaterTest(Scene):
    def construct(self):
        axes  = Axes(
            x_range = [-1, 13, 1],
            y_range = [-1, 13, 1],
            width = 8, height = 8,
            axis_config = {
                "include_tip": True
            }
        )
        dot = Dot(point = axes.c2p(0, 8), color = BLUE)
        l1 = Line(axes.c2p(0, 8), axes.c2p(8, 0))
        for x in [axes, dot, l1]:
            self.play(Write(x), run_time = 1)

        l2 = Line().add_updater(lambda m : m.put_start_and_end_on(dot.get_center(), axes.c2p(0, 0)))
        self.add(l2)
        self.play(MoveAlongPath(dot, l1), run_time = 5)
        self.wait()
