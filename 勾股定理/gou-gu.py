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

        frame_scale = 1.5
        sc = Square(
            side_length = (rt['width'] ** 2 + rt['height'] ** 2) ** 0.5,
            stroke_color = BLUE_E
        ).move_to(t.get_vertices()[2], DL).rotate(np.arctan(rt['height'] / rt['width']), about_point = t.get_vertices()[2])
        fc = Tex('{c}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sc).scale(frame_scale)
        frame.generate_target()
        frame.target.scale(frame_scale).move_to(sc)
        self.wait()
        self.play(
            MoveToTarget(frame),
            ShowCreation(sc),
            TransformMatchingTex(c, fc),
            *[FadeOut(mob) for mob in [a, b]]
        )

        tg = VGroup(*[t.copy().rotate(PI / 2 * i, about_point = sc.get_center()) for i in range(1, 4)])
        sc.add_updater(lambda m : self.add(m))
        self.wait()
        self.play(*[Write(mob) for mob in tg])
        sc.clear_updaters()
        self.play(Uncreate(sc), FadeOut(fc))

        sa = Square(
            side_length = rt['width'],
            stroke_color = TEAL_E
        ).move_to(t.get_vertices()[1], DR)
        fa = Tex('{a}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sa).scale(frame_scale)
        sb = Square(
            side_length = rt['height'],
            stroke_color = GREEN_E
        ).move_to(sa.get_vertices()[1], UR)
        fb = Tex('{b}^2', isolate = tex_isolate, tex_to_color_map = tex_color).move_to(sb).scale(frame_scale)
        self.play(tg[0].animate.move_to(t.get_vertices()[2], DR))
        self.play(tg[1].animate.move_to(t.get_vertices()[2], DL))
        self.play(
            *[ShowCreation(mob) for mob in [sa, sb]],
            *[Write(mob) for mob in [fa, fb]]
        )

        fmt = Tex('{a}^2', '+', '{b}^2', '=', '{c}^2', tex_to_color_map = tex_color).scale(1.5).to_edge(DOWN, buff = 1.5).shift(frame.get_center())
        self.play(*[ReplacementTransform(x, y) for x, y in ((fa, fmt[0 : 2]), (fb, fmt[3 : 5]))])
        self.embed()

class Test(Scene):
    def construct(self):
        fmt = Tex('{a}^2', '+', '{b}^2', '=', '{c}^2')
        self.add(fmt[0])
