from manimlib import*
# manimgl -w --hd --show_animation_progress --leave_progress_bars equ.py Equation_1
class Equation_1(Scene):
    def construct(self):
        s = [
            r'ax^2 + bx + c = 0, a \ne 0',
            r'x^2 + \frac bax + \frac ca = 0',
            r'x^2 + \frac bax = -\frac ca',
            r'x^2 + \frac bax + \frac {b^2}{4a^2} = \frac {b^2}{4a^2} - \frac ca',
            r'x^2 + 2 \cdot \frac b{2a}x + \left(\frac b{2a}\right)^2 = \frac {b^2}{4a^2} - \frac {4ac}{4a^2}',
            r'\left(x + \frac b{2a}\right)^2 = \frac {b^2 - 4ac}{4a^2}',
            r'x_{1, 2} + \frac b{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}',
            r'x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}'
        ]
        t = [Tex(st) for st in s]
        self.play(Write(t[0]))
        self.wait(3)
        for i in range(1, len(s)):
            self.play(TransformMatchingShapes(t[i - 1], t[i]))
            self.wait()

