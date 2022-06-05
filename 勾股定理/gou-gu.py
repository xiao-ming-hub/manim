from manimlib import*
class GouGu(Scene):
    def construct(self):
        rt = {'width' : 4, 'height' : 3}
        frame = self.camera.frame
        tex_color = {'{a}' : TEAL_B, '{b}' : GREEN_B, '{c}' : BLUE_B}
        tex_isolate = ['{a}', '{b}', '{c}']

        t = np.array((rt['width'] / 2, -rt['height'] / 2, 0))
        t = Polygon(
            t, t + UP * rt['height'], t + LEFT * rt['width'],
            stroke_color = PURPLE_E
        )
        self.wait()
        self.play(ShowCreation(t))

        a = Tex('{a}', tex_to_color_map = tex_color).next_to(t, DOWN)
        b = Tex('{b}', tex_to_color_map = tex_color).next_to(t)
        c = Tex('{c}', tex_to_color_map = tex_color).next_to(t, UL, buff = -1.3)
        self.play(*[Write(mob) for mob in [a, b, c]])
        self.wait()

        frame_scale = 1.5
        sa = Square(
            side_length = rt['width'],
            stroke_color = TEAL_E,
        ).next_to(t, DOWN, buff = 0)
        fa = Tex('{a}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sa).scale(frame_scale)
        sb = Square(
            side_length = rt['height'],
            stroke_color = GREEN_E,
        ).next_to(t, buff = 0)
        fb = Tex('{b}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sb).scale(frame_scale)
        sc = Square(
            side_length = (rt['width'] ** 2 + rt['height'] ** 2) ** 0.5,
            stroke_color = BLUE_E
        ).move_to(t.get_vertices()[2], DL).rotate(np.arctan(rt['height'] / rt['width']), about_point = t.get_vertices()[2])
        fc = Tex('{c}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sc).scale(frame_scale)
        self.play(
            frame.animate.scale(frame_scale),
            *[ShowCreation(m) for m in [sa, sb, sc]],
            *[TransformMatchingTex(x, y) for x, y in [(a, fa), (b, fb), (c, fc)]],
        )

        self.remove(t)

        self.embed()

