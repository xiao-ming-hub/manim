# 爱尔可斯定理一 - Echols Theorem I
from manimlib import*
def return_random_from_word(word):
    x = list(range(len(word)))
    random.shuffle(x)
    return x

class WriteRandom(LaggedStart):
    CONFIG = {
        "lag_ratio": 0.05,
        "run_time": 2.5,
        "anim_kwargs": {},
        "anim_type": Write
    }
    def __init__(self, text, **kwargs):
        digest_config(self, kwargs)
        super().__init__(*[
            self.anim_type(text[0][i], **self.anim_kwargs)
            for i in return_random_from_word(text[0])
        ])

class FadeOutRandom(WriteRandom):
    CONFIG = {
        "anim_type": FadeOut,
        "remover": True,
        "run_time": 1
    }

class EcholsTheoremI_1(Scene):
    def construct(self):
        title = Text('爱尔可斯定理一    Echols Theorem I').shift(UP * 0.5)
        intro = VGroup(
            TexText(r'若 $\triangle ABC$ 和 $\triangle DEF$ 都是正三角形，'),
            TexText(r'则由线段 $AD$、$BE$、$CF$ 的中心构成的三角形也是正三角形。')
        ).arrange(DOWN)
        intro[1].align_to(intro[0], LEFT)
        intro.scale(0.5).next_to(title, DOWN)
        self.wait()
        self.play(DrawBorderThenFill(title, run_time = 3), *[WriteRandom(x) for x in intro])
        self.wait(2)
        self.play(FadeOut(title), *[FadeOutRandom(x) for x in intro])

class EcholsTheoremI_2(Scene):
    def construct(self):
        pass
