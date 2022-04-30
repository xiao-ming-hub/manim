from manimlib import*
class aa(Scene):
    def construct(self):
        a = Text('Hello world!')
        self.play(Write(a))
        self.wait()
        self.play(a.scale, 2)
