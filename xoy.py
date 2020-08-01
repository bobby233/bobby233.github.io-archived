from manimlib.imports import Scene
from manimlib.imports import TexMobject, Axes, VGroup, TextMobject, Dot, Line
from manimlib.imports import LEFT, DOWN, RIGHT, UP, RED, YELLOW
from manimlib.imports import Write, ShowCreation, DrawBorderThenFill, FadeOutAndShiftDown, Transform, FadeOut, ApplyMethod
from numpy import array

class xOy(Scene):
    def construct(self):
        title = TextMobject("第25题")
        teller = TextMobject("讲解人：宋昊政")
        title.scale(2)
        teller.scale(0.5)
        teller.shift(DOWN)

        self.play(
            DrawBorderThenFill(title),
            DrawBorderThenFill(teller)
        )
        self.wait(0.5)
        self.play(
            FadeOutAndShiftDown(title),
            FadeOutAndShiftDown(teller)
        )
        self.wait(0.5)

        ## Title --> Display all

        axes = Axes(
            x_min=-2, x_max=9,
            y_max=6
        )
        axes.scale(0.6)
        axes.shift(3*LEFT + 2*DOWN)
        axes.add_coordinates([1], [1])
        xlabel = TexMobject("x").move_to(axes.c2p(9, -0.5))
        ylabel = TexMobject("y").move_to(axes.c2p(-0.5, 6))
        original = TexMobject("O").move_to(axes.c2p(-0.5, -0.5))
        group = VGroup(axes, xlabel, ylabel, original).scale(0.7)
        group.shift(3*RIGHT + 0.8*UP)
        # Axes --> Ques
        ques = TextMobject("25、如图，在直角坐标平面内，已知点", "A", "(", "8", ",0)，点", "B", "(", "3", ",0)，", "点C是点A关于点B的对称点", ".\\\ （1）求点C的坐标；", alignment="")
        # , "（2）如果点P在y轴上，过点P作直线l//x轴，点A关于直线l的对称点是点D，那么当三角形BCD的面积等于10时，求点P的坐标."
        ques.shift(3.1*UP)
        ques.scale(0.6)

        self.play(
            ShowCreation(axes, run_time=6),
            Write(ques, run_time=6)
        )
        self.play(
            Write(xlabel),
            Write(ylabel),
            Write(original)
        )
        self.wait(5)

        ## Display all --> Transform dots

        dot_a = Dot(axes.c2p(8, 0))
        dot_b = Dot(axes.c2p(3, 0))
        let_a = ques[1].copy()
        let_b = ques[5].copy()
        let_a.next_to(dot_a, DOWN, 0.1)
        let_b.next_to(dot_b, DOWN, 0.1)

        self.play(
            ShowCreation(dot_a),
            ShowCreation(dot_b),
            Transform(ques[1].copy(), let_a),
            Transform(ques[5].copy(), let_b)
        )
        self.wait()

        ## Transform dots --> AB's lenth

        l_ab = Line(dot_a, dot_b, color=RED)
        self.play(ShowCreation(l_ab))
        self.wait()

        sol_l_ab = TexMobject("AB", "= |8-3| = 5")
        sol_l_ab[0].set_color(RED)
        sol_l_ab.scale(0.6)
        sol_l_ab.next_to(ques, DOWN, buff=0.6)
        sol_l_ab.shift(3.5*LEFT)
        self.play(
            Transform(l_ab.copy(), sol_l_ab[0]),
            Write(sol_l_ab[1])
        )
        self.wait()

        ## AB's lenth --> BC = AB

        self.play(ApplyMethod(ques[-2].set_color, YELLOW))
        self.wait()
        known0 = TextMobject("又$\\because$", "点C是点A关于点B的对称点", "（已知）")
        known0[1].set_color(YELLOW)
        known0.scale(0.6)
        known0.next_to(sol_l_ab, DOWN)
        known0.align_to(sol_l_ab, LEFT)
        
        self.play(
            Write(known0[0]),
            Transform(ques[-2].copy(), known0[1]),
            Write(known0[2])
        )
        self.wait()
