from manimlib import*
def MyTex(*tex_strings, keyword = [], font = None):
    replace = {
        "[" : "", "]" : "", "{" : "", "}" : "", "_" : "", " " : "", "^" : "",
        "\\[" : "[", "\\]" : "]", "\\{" : "{", "\\}" : "}", "\\_" : "-",
        "\\pm" : "±",
        "\\frac" : "-", "\\sqrt" : "√-",
        "\\cos" : "cos", "\\sin" : "sin",
        "\\theta" : "θ"
    }
    tex = Tex(*tex_strings)
    ans = VGroup()
    for txt in tex_strings:
        aftertxt = ""
        l = len(txt)
        i = 0
        while i + 6 < l:
            if txt[i : i + 5] == "\\frac":
                j = i + 5       # j 分子结束下标
                if txt[j] == "{":
                    cnt = 1     # 开括号 - 闭括号
                    while cnt:
                        j += 1
                        if txt[j] == "{" : cnt += 1
                        elif txt[j] == "}" : cnt -= 1
                # print(txt, i, j)
                txt = txt[0 : i] + txt[i + 5 : j + 1] + "\\frac" + txt[j + 1 :]
                i = j
            i += 1
        i = 0
        while i < l:
            found = False
            for k in replace:
                v = replace[k]
                if i + len(k) <= l and txt[i : i + len(k)] == k:
                    aftertxt += v
                    i += len(k)
                    found = True
                    break
            if found: continue
            aftertxt += txt[i]
            i += 1
        if font: text = Text(aftertxt, font = font, slant = ITALIC, t2s = {s : NORMAL for s in ["+", "-", "=", *keyword]})
        else: text = Text(aftertxt, slant = ITALIC, t2s = {s : NORMAL for s in ["+", "-", "=", *keyword]})
        for i in range(len(tex[0])): text[i].replace(tex[0][i], stretch = True)
        ans.add(text)
    return ans

class MyTexTest(Scene):
    def construct(self):
        t = MyTex("ax^2 + bx + c = 0", keyword = ["2", "0"])
        self.play(Write(t))
        u = MyTex(r"x_{1, 2} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", keyword = ["1", ",", "2", "±", "4", "√"])
        self.play(TransformMatchingShapes(t, u), run_time = 3)
        v = MyTex(r"e^{i\theta} = \cos \theta + i \sin \theta", font = "Sans", keyword = ["sin", "cos"])
        self.play(FadeOut(u), Write(v))
