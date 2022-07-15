from manimlib import*
class NewPoint(Point):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Test(Scene):
    def construct(self):
        p = Point()
