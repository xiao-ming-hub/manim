from manimlib import *
class JumpPoint(Scene):
    def construct(self):
        self.x = UP * 2 + RIGHT
        self.v = LEFT * 10.2 + UP * 2.2
        self.a = 4.9 * DOWN
        dot = Dot(color = GREEN)
        botl = Line(np.array((-3, -3, 0)), np.array((3, -3, 0)))
        lftl = Line(np.array((-3, -3, 0)), np.array((-3, 3, 0)))
        rgtl = Line(np.array((3, -3, 0)), np.array((3, 3, 0)))
        tail = TracingTail(lambda : self.x, stroke_color = BLUE, time_traced = 2)
        path = TracedPath(lambda : self.x, stroke_color = GREY_E)
        def update_dot(mob : Dot, dt):
            i = 1000
            dt /= i
            while i > 0:
                self.v += self.a * dt
                if self.x[1] < mob.get_radius() - 3: self.v[1] *= -1
                if self.x[0] < mob.get_radius() - 3 or self.x[0] > 3 - mob.get_radius(): 
                        self.v[0] *= -1
                self.v *= 1 - dt * 0.01
                self.x += self.v * dt
                i -= 1
            mob.move_to(self.x)

        self.add(path, tail, dot, botl, lftl, rgtl)
        dot.add_updater(update_dot)
