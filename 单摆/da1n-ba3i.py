from manimlib import*
class da1n_ba3i(Scene):
    def construct(self):
        self.prmt = { 'g' : 9.8, 'L' : 3, 'mu' : 0.1, 'theta' : 3 * PI / 4, 'theta_dot' : 0 }
        rod = VGroup(
            Line(ORIGIN, self.prmt['L'] * DOWN),
            Dot(point = self.prmt['L'] * DOWN, radius = 0.1, color = GREEN)
        ).rotate_about_origin(self.prmt['theta'])
        def get_theta_double_dot(theta : float):
            return -self.prmt['mu'] * self.prmt['theta_dot'] - self.prmt['g'] / self.prmt['L'] * math.sin(self.prmt['theta'])

        def update_rod(mob, dt):
            repeat = 1000
            ddt = dt / repeat
            for i in range(repeat):
                self.prmt['theta'] += self.prmt['theta_dot'] * ddt
                self.prmt['theta_dot'] += get_theta_double_dot(self.prmt['theta_dot']) * ddt

            mob.rotate_about_origin(self.prmt['theta_dot'] * dt)

        self.add(rod.add_updater(update_rod))
