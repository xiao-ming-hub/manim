from manimlib import*
class RandomMove(Scene):
    def construct(self):
        way = (UP, LEFT, DOWN, RIGHT)
        edge = (-6, 6, -3, 3)   # l, r, d, u
        face = 0                # 0 right, 1 up, 2 left, 3 down
        center = ORIGIN
        mob = Dot(radius = 0.02, fill_color = ORANGE)
        path = TracedPath(mob.get_center, stroke_width = 3, stroke_color = TEAL, stroke_opacity = 0.3)
        self.add(path, mob)
        while True:
            while True:
                nface = (face + random.randint(3, 5)) % 4
                x = center + way[nface] * random.random()
                if edge[0] <= x[0] and x[0] <= edge[1] and edge[2] <= x[1] and x[1] <= edge[3]:
                    face = nface
                    center = x
                    break
            mob.move_to(center)
            self.wait(0.2)
