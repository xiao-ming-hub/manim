from manimlib import*
class ThreeBody(Scene):
    def construct(self):
        self.a = np.zeros((3, 3))
        self.v = np.array([[2.021456, 1.292308, 0.000000], [1.048120, -2.083008, 0.000000], [0.153656, 0.190323, 0.000000]])
        self.x = np.array([[-0.616501, -1.719321, 0.000000], [0.681670, -1.974953, 0.000000], [-0.761621, -0.478809, 0.000000]])
        m = (1.358534, 3.662875, 2.066816)
        g = 9.8
        colors = (RED, GREEN, BLUE)
        balls = VGroup(*[SmallDot(color = colors[i]) for i in range(3)])
        path = VGroup(*[TracingTail(balls[i].get_center, stroke_color = colors[i], min_distance_to_new_point = 0.01, time_traced = 2) for i in range(3)])
        def update_balls(mob, dt):
            n = 1000
            dt /= n
            for _ in range(n):
                self.a = np.zeros((3, 3))
                for i in range(3):
                    for j in range(3):
                        if i == j: continue
                        diff = self.x[j] - self.x[i]
                        vabs = 0.
                        for num in diff: vabs += num ** 2
                        vabs **= 1.5
                        self.a[i] += m[j] * diff / vabs
                self.a *= g
                self.v += self.a * dt
                self.x += self.v * dt
            for i in range(3):
                balls[i].move_to(self.x[i])
        def update_camera(mob, dt):
            mob.shift((sum(self.x) / 3 - mob.get_center()) * 0.01)
        balls.add_updater(update_balls)
        self.camera.frame.add_updater(update_camera)
        self.add(balls, path)
        self.wait(10)
