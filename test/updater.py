from manimlib import*
import math
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
        p = Dot(point = axes.c2p(8, 0), color = BLUE)
        def update_q(mob):
            a, b = axes.p2c(p.get_center())
            mob.move_to(axes.c2p(0, a + b * (b - a) / (b + a)))

        q = Dot(color = BLUE).add_updater(update_q)
        l1 = Line(axes.c2p(0, 8), axes.c2p(8, 0))
        l2 = Line().add_updater(lambda m : m.put_start_and_end_on(axes.c2p(0, 0), p.get_center()))
        l3 = Line().add_updater(lambda m : m.put_start_and_end_on(p.get_center(), q.get_center()))
        arc1 = Arc(135 * DEGREES, 45 * DEGREES, radius = 0.5, arc_center = axes.c2p(8, 0), color = GREEN)
        def update_arc2(point):
            '''
            x, y = axes.p2c(p.get_center())
            deg = math.acos(x / abs(complex(x, y))) + 135 * DEGREES
            mob = Arc(deg, 45 * DEGREES, radius = 0.5, arc_center = p.get_center(), color = GREEN)
            '''
            return Dot(point = point() + UP)
        arc2 = Arc(135 * DEGREES, 45 * DEGREES, radius = 0.5, color = GREEN)
        arc2.add_updater(lambda m : m.move_arc_center_to(axes.c2p(0, 0)))
        self.add(axes, p, q, l1, l2, l3, arc1, arc2)
        self.wait()
        self.play(p.animate.move_to(axes.c2p(0, 8)), run_time = 5)

def debug_mob(mob : Mobject) -> VGroup:
    point = mob.get_points()
    return VGroup(*[Text("%d" % i, color = GREEN).move_to(point[i]).scale(0.2) for i in range(len(point))])

class TestArc(Scene):
    def construct(self):
        arc = Arc(0, 45 * DEGREES, arc_center = UP).scale(3)
        c = SmallDot(point = arc.get_arc_center(), color = RED)
        d = SmallDot(point = arc.get_points()[0], color = BLUE)
        self.add(arc, c, d)
        self.add(debug_mob(arc))
