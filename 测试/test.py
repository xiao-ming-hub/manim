from manimlib import *
class HelloWorld(Scene):
    def construct(self):
        t = Text('Hello world.')
        self.play(Write(t))
        self.wait(0.5)

        self.play(t.animate.scale(1.5))

class UpdaterTest(Scene):
    def construct(self):
        d1 = Dot(point = UL, color = BLUE)
        d2 = Dot(point = DOWN * 2, color = BLUE)
        l = Line().add_updater(lambda m : m.put_start_and_end_on(d1.get_center(), d2.get_center()))
        length = VGroup(
            Text('线段长度：'),
            DecimalNumber().add_updater(lambda m : m.set_value(l.get_length()))
        ).scale(0.75).arrange().to_corner(DR)
        self.add(d1, d2, l, length)

        self.play(d1.animate.shift(UP + RIGHT))
        self.play(d2.animate.shift(LEFT + DOWN * 2))

class CodeDisplay(Scene):
    def construct(self):
        s = '''#include <iostream>
int main() {
  std::cout << "Hello world." << std::endl;
  return 0;
}'''
        c = Code(s, language = 'cpp', code_style = 'dracula').scale(1.5)
        self.play(Write(c))

class ThreeDimTest(Scene):
    CONFIG = {
        'camera_class' : ThreeDCamera
    }
    def construct(self):
        t = Text('这是一个立方体').fix_in_frame().to_corner()
        c = Cube(stroke_color = WHITE)
        frame = self.camera.frame
        self.play(Write(t), FadeIn(c), frame.animate.set_euler_angles(theta = TAU / 3, phi = PI / 3))
        frame.add_updater(lambda m, dt : m.increment_theta(PI * dt / 6))
        self.play(c.animate.scale(1.5))

        self.play(Transform(t, Text('这是一个球').fix_in_frame().to_corner()))
        b = Sphere(color = BLUE)
        self.play(FadeTransform(c, b))

class MoveToTest(Scene):
    def construct(self):
        s = Square(fill_opacity = 1, fill_color = GREEN_D, stroke_color = GREEN)
        self.add(s)
        s1 = s.copy()
        s1.generate_target()
        s1.target.shift(DOWN * 2).scale(0.5)
        self.wait()
        self.play(MoveToTarget(s1))

class LaggedStartTest(Scene):
    def construct(self):
        mob = VGroup(
            Circle(),
            Square(),
            Triangle()
        ).arrange()
        self.play(LaggedStart(*[FadeIn(m, shift = UP * 0.5, rate_function = exponential_decay) for m in mob], lag_ratio = 0.1))

