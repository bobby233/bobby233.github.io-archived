# 学习作品，仅作Manim学习和学校作业用
# 活动要求：
# 1.每个题要视频讲解 (D)
# 2.每个题，需要文字的简单思路(D)，小节(N)，还有考点罗列(D)
# 3.每个题还需要再提出一个问题 (D)
# 4.队长需要提供小队介绍(N)，团队照片(TN)，400字以内
# 5.队长还需要提供一份400字以内的小组活动小节，感悟，反思 (NT)

# DOC
# 简单思路：
#     第一问：先算出AB的长度，再通过中心对称的性质证出BC=AB，进而推导出点C的坐标
#     第二问：通过三角形BCD的面积和底边BC求出高AD的长度，然后通过轴对称的性质求出AM的长度，再利用平行线间距离的意义求出OP的长度，最后分类讨论求出点P的坐标
#         分类标准：1° 当点P在y轴正半轴时   2° 当点P在y轴负半轴时
# 考点罗列：
#     中心对称的性质 轴对称的性质 平行线间距离的意义 分类讨论
# 问题：
#     如果点Q在x轴上，过点Q作直线l'//y轴，点P关于直线l'的对称点是点E，那么当三角形CBE是以BE和CE为腰的等腰三角形时，求点Q的坐标

from manimlib.imports import Scene
from manimlib.imports import TexMobject, Axes, VGroup, TextMobject, Dot, Line, DashedLine, Polygon, Arc
from manimlib.imports import LEFT, DOWN, RIGHT, UP, RED, YELLOW, WHITE, BLUE, PI, WHITE
from manimlib.imports import Write, ShowCreation, DrawBorderThenFill, FadeOutAndShiftDown, Transform, FadeOut, ApplyMethod, FadeIn
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
        ques.shift(3.1*UP)
        ques.scale(0.6)

        self.play(
            ShowCreation(axes, run_time=6),
            FadeIn(ques)
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

        ## Transform dots --> Draw C

        l_ab = Line(dot_a, dot_b, color=RED)
        self.play(ShowCreation(l_ab))
        self.wait(3)

        drawing = Arc(arc_center=dot_b.get_center(), start_angle=-PI*1.1, angle=PI/7, color=RED, radius=2.1)
        self.play(ShowCreation(drawing))
        self.wait()

        dot_c = Dot(axes.c2p(-2, 0))
        let_c = TextMobject("C")
        let_c.scale(0.6)
        let_c.next_to(dot_c, LEFT, buff=0.1)

        self.play(
            ShowCreation(dot_c),
            Write(let_c)
        )
        self.wait(3)

        ## Draw C --> Route

        route0 = TexMobject("AB")
        route0.set_color(RED)
        route0.shift(3.5*LEFT+1.5*UP)
        self.play(Write(route0))
        self.wait()

        route1 = TexMobject("BC=", "AB")
        route1[1].set_color(RED)
        route1.shift(3.5*LEFT)
        self.play(
            Write(route1[0]),
            Transform(fade:=route0.copy(), route1[1])
        )
        self.wait()

        route2 = TexMobject("C")
        route2.shift(3.5*LEFT+1.5*DOWN)
        self.play(Write(route2))
        self.wait(3)

        self.play(
            FadeOut(route0),
            FadeOut(route1),
            FadeOut(route2),
            FadeOut(fade)
        )
        self.wait()

        ## Route --> AB's lenth

        sol_l_ab = TexMobject("AB", "= |8-3|", "= 5")
        sol_l_ab[0].set_color(RED)
        sol_l_ab.scale(0.6)
        sol_l_ab.next_to(ques, DOWN, buff=0.6)
        sol_l_ab.shift(3.5*LEFT)
        self.play(
            Transform(l_ab.copy(), sol_l_ab[0]),
            Write(sol_l_ab[1]),
            Write(sol_l_ab[2])
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
        self.wait(6.5)

        property00 = TextMobject("中心对称的对称点所连线段经过对称中心．")
        property00.scale(0.7)
        property00.next_to(known0, DOWN)
        property00.align_to(known0, LEFT)
        property01 = TextMobject("而且被对称中心平分")
        property01.scale(0.7)
        property01.next_to(property00, DOWN)
        property01.align_to(property00, LEFT)

        self.play(Write(property00, run_time=5))
        self.play(Write(property01, run_time=2))
        self.wait()

        sol_bceab = TextMobject("$\\therefore BC =$", "$AB$", "$= 5$", "（", "中心对称的性质", "）")
        sol_bceab[1].set_color(RED)
        sol_bceab.scale(0.6)
        sol_bceab.next_to(known0, DOWN)
        sol_bceab.align_to(known0, LEFT)

        self.play(
            Write(sol_bceab[0]),
            Write(sol_bceab[1]),
            Transform(sol_l_ab[2].copy(), sol_bceab[2]),
            Write(sol_bceab[3]),
            Transform(property00, sol_bceab[4]),
            Transform(property01, sol_bceab[4]),
            Write(sol_bceab[5]),
            run_time = 3
        )
        self.wait()

        ## BC = AB --> C's pos

        sol_c_pos = TexMobject("\\therefore", "C", "(", "3-5", ", 0)")
        sol_c_pos.scale(0.6)
        sol_c_pos.next_to(sol_bceab, DOWN)
        sol_c_pos.align_to(sol_bceab, LEFT)

        self.play(Write(sol_c_pos))
        self.wait()

        csol_c_pos = TexMobject("\\therefore C(", "-2", ", 0)")
        csol_c_pos.scale(0.6)
        csol_c_pos.next_to(sol_bceab, DOWN)
        csol_c_pos.align_to(sol_bceab, LEFT)
        self.play(
            Transform(sol_c_pos[3], csol_c_pos[1]),
            Transform(sol_c_pos[4], csol_c_pos[2])
        )
        self.wait()

class two(Scene):
    def construct(self):
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
        ques = TextMobject("25、如图，在直角坐标平面内，已知点A(8,0)，点B(3,0)，点C是点A关于点B的对称点", ".\\\ （2）如果点P在y轴上，过点P作直线", "l//x轴", "，点A关于直线l的对称点是点D，", "那么当", "三角形BCD的面积等于10", "时，求点P的坐标.", alignment='')
        ques.shift(3.1*UP)
        ques.scale(0.6)
        self.add(group, ques)

        dot_c = Dot(axes.c2p(-2, 0))
        let_c = TextMobject("C")
        let_c.scale(0.6)
        let_c.next_to(dot_c, DOWN, buff=0.1)
        dot_a = Dot(axes.c2p(8, 0))
        dot_b = Dot(axes.c2p(3, 0))
        let_a = TextMobject("A").scale(0.6)
        let_b = TextMobject("B").scale(0.6)
        let_a.next_to(dot_a, DOWN, 0.1)
        let_b.next_to(dot_b, DOWN, 0.1)
        self.add(dot_c, let_c, dot_a, let_a, dot_b, let_b)

        ## Display all --> Draw \triangle BCD
        dot_p = Dot(axes.c2p(0, 2))
        let_p = TextMobject("P")
        let_p.scale(0.6)
        let_p.next_to(dot_p, LEFT, buff=0.1)
        let_p.shift(0.3*UP)
        
        self.wait(2)
        self.play(
            ShowCreation(dot_p),
            Write(let_p),
            run_time=1.5
        )
        self.wait()

        l_l = Line(axes.c2p(-2, 2), axes.c2p(9, 2))
        let_l = TexMobject("l")
        let_l.scale(0.6)
        let_l.next_to(l_l, LEFT, buff=0.1)

        self.play(
            ShowCreation(l_l),
            Write(let_l),
            run_time=1.5
        )
        self.wait()

        dot_d = Dot(axes.c2p(8, 4))
        let_d = TextMobject("D")
        let_d.scale(0.6)
        let_d.next_to(dot_d, UP, buff=0.1)
        l_ad = DashedLine(dot_a, dot_d)

        self.play(
            ShowCreation(dot_d),
            Write(let_d),
            ShowCreation(l_ad),
            run_time=1.5
        )
        self.wait()

        l_cd = Line(dot_c, dot_d)
        l_bd = Line(dot_b, dot_d)

        self.play(
            ShowCreation(l_cd),
            ShowCreation(l_bd),
            run_time=1.5
        )
        self.wait(7)

        ## Draw \triangle BCD --> Route

        route0 = TexMobject("{S}_{\\triangle BCD}")
        route0.shift(3.5*LEFT+1.5*UP)
        tri_bcd = Polygon(dot_b.get_center(), dot_c.get_center(), dot_d.get_center(),
                          color=WHITE, fill_color=BLUE, fill_opacity=0.3)
        self.play(
            ShowCreation(tri_bcd),
            Write(route0)
        )
        self.wait(2)

        route1 = TexMobject("AD")
        route1.set_color(BLUE)
        route1.shift(3.5*LEFT+0.5*UP)
        self.play(
            ApplyMethod(l_ad.set_color, BLUE),
            Write(route1)
        )
        self.wait(2)

        route2 = TexMobject("AM = \\frac{1}{2}AD")
        route2.set_color(RED)
        route2.shift(3.5*LEFT+0.5*DOWN)
        dot_m = Dot(axes.c2p(8, 2))
        let_m = TextMobject("M")
        let_m.scale(0.6)
        let_m.next_to(dot_m, UP, buff=0.1)
        let_m.shift(0.3*RIGHT)
        l_am = DashedLine(dot_a, dot_m, color=RED)
        self.play(
            ShowCreation(dot_m),
            Write(let_m),
            ShowCreation(l_am),
            Write(route2)
        )
        self.wait(5)

        route3 = TexMobject("OP = AM")
        route3.set_color(RED)
        route3.shift(3.5*LEFT+1.5*DOWN)
        l_op = Line(axes.c2p(0,0), dot_p, color=RED)
        self.play(
            Transform(l_am.copy(), l_op),
            Write(route3)
        )
        self.wait(5)

        route4 = TexMobject("P")
        route4.shift(3.5*LEFT+2.5*DOWN)
        self.play(Write(route4))
        self.wait()

        self.play(
            FadeOut(route0),
            FadeOut(route1),
            FadeOut(route2),
            FadeOut(route3),
            FadeOut(route4)
        )
        self.wait(2)

        ## Route --> Solution

        sol_s_tri_bcd = TexMobject("\\because", "{{S}_{\\triangle BCD}}", "=10", alignment='')
        sol_s_tri_bcd.scale(0.6)
        sol_s_tri_bcd.next_to(ques, DOWN, buff=0.6)
        sol_s_tri_bcd.align_to(ques, LEFT)

        self.play(
            Write(sol_s_tri_bcd[0]),
            Transform(tr0:=ques[5].copy(), sol_s_tri_bcd[1]),
            Transform(tr:=ques[5].copy(), sol_s_tri_bcd[2])
        )
        self.wait(2)

        csol_s_tri_bcd = TexMobject("\\because", "{S}_{\\triangle BCD}", "=\\frac{1}{2}BC\\times", "AD", "=10",
                                    alignment='')
        csol_s_tri_bcd[3].set_color(BLUE)
        csol_s_tri_bcd.scale(0.6)
        csol_s_tri_bcd.next_to(ques, DOWN, buff=0.6)
        csol_s_tri_bcd.align_to(ques, LEFT)
        cn_s_tri = TextMobject("（三角形的面积公式）")
        cn_s_tri.scale(0.6)
        cn_s_tri.next_to(csol_s_tri_bcd, buff=0.1)

        self.play(
            Transform(sol_s_tri_bcd[0], csol_s_tri_bcd[0]),
            Transform(tr0, csol_s_tri_bcd[1]),
            Write(csol_s_tri_bcd[2]),
            Write(csol_s_tri_bcd[3]),
            Transform(tr, csol_s_tri_bcd[4]),
            Write(cn_s_tri)
        )
        self.wait(3)

        sol_l_bc = TextMobject("$BC = 5$（已证）")
        sol_l_bc.scale(0.6)
        sol_l_bc.align_to(csol_s_tri_bcd, LEFT)
        sol_l_bc.next_to(csol_s_tri_bcd, DOWN)
        self.play(Write(sol_l_bc))
        self.wait()

        sol_l_ad = TexMobject("\\therefore", "AD", "= 4")
        sol_l_ad[1].set_color(BLUE)
        sol_l_ad.shift(4.4*LEFT+0.4*UP)
        sol_l_ad.scale(0.6)
        eproperty = TextMobject("（等式性质）")
        eproperty.scale(0.6)
        eproperty.next_to(sol_l_ad)

        self.play(
            Write(sol_l_ad),
            Write(eproperty)
        )
        self.wait(4)

        self.play(ApplyMethod(ques[3].set_color, YELLOW))
        self.wait()
        sol_l_am0 = TextMobject("又$\\because$", "点A关于直线l的对称点是点D", "（已知）")
        sol_l_am0[1].set_color(YELLOW)
        sol_l_am0.scale(0.6)
        sol_l_am0.next_to(sol_l_ad, DOWN)
        sol_l_am0.align_to(sol_l_ad, LEFT)
        self.play(
            Write(sol_l_am0[0]),
            Transform(tr:=ques[3].copy(), sol_l_am0[1]),
            Write(sol_l_am0[2])
        )
        self.wait(7)

        property0 = TextMobject("对称轴是对称点连线的垂直平分线")
        property0.scale(0.6)
        property0.next_to(sol_l_am0, DOWN)
        property0.align_to(sol_l_am0, LEFT)
        self.play(Write(property0))
        self.wait(2)

        sol_l_am1 = TexMobject("\\therefore", "AM", "= \\frac{1}{2}", "AD", "= 2")
        sol_l_am1[1].set_color(RED)
        sol_l_am1[3].set_color(BLUE)
        sol_l_am1.scale(0.6)
        sol_l_am1.next_to(sol_l_am0, DOWN)
        sol_l_am1.align_to(sol_l_am0, LEFT)
        csol_l_am1 = TextMobject("（轴对称的性质）")
        csol_l_am1.scale(0.6)
        csol_l_am1.next_to(sol_l_am1)
        self.play(
            Write(sol_l_am1[0]),
            Write(sol_l_am1[1]),
            Write(sol_l_am1[2]),
            Transform(sol_l_ad[1].copy(), sol_l_am1[3]),
            Transform(sol_l_ad[2].copy(), sol_l_am1[4]),
            Transform(property0, csol_l_am1)
        )
        self.wait(4)

        self.play(
            ApplyMethod(ques[3].set_color, WHITE),
            ApplyMethod(tr.set_color, WHITE),
            ApplyMethod(ques[2].set_color, YELLOW),
        )
        self.wait()
        sol_l_op0 = TextMobject("又$\\because$", "$l // x$", "轴", "（已知）")
        sol_l_op0[1].set_color(YELLOW)
        sol_l_op0[2].set_color(YELLOW)
        sol_l_op0.scale(0.6)
        sol_l_op0.align_to(sol_l_am1, LEFT)
        sol_l_op0.next_to(sol_l_am1, DOWN)
        self.play(
            Write(sol_l_op0[0]),
            Transform(ques[2].copy(), sol_l_op0[1]),
            Transform(ques[2].copy(), sol_l_op0[2]),
            Write(sol_l_op0[3])
        )
        self.wait(5)

        property1 = TextMobject("平行线之间的距离处处相等")
        property1.scale(0.6)
        property1.next_to(sol_l_op0, DOWN)
        property1.align_to(sol_l_op0, LEFT)
        self.play(Write(property1))
        self.wait()

        sol_l_op1 = TexMobject("\\therefore", "OP", "=", "AM", "= 2")
        sol_l_op1[1].set_color(RED)
        sol_l_op1[3].set_color(RED)
        sol_l_op1.scale(0.6)
        sol_l_op1.align_to(sol_l_op0, LEFT)
        sol_l_op1.next_to(sol_l_op0, DOWN)
        csol_l_op1 = TextMobject("（平行线间距离的意义）")
        csol_l_op1.scale(0.6)
        csol_l_op1.next_to(sol_l_op1)
        
        self.play(
            Write(sol_l_op1[0]),
            Write(sol_l_op1[1]),
            Write(sol_l_op1[2]),
            Transform(tr.copy(), sol_l_op1[3]),
            Transform(sol_l_am1[4], sol_l_op1[4]),
            Transform(property1, csol_l_op1)
        )
        self.wait()

class last(Scene):
    def construct(self):
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
        ques = TextMobject("25、如图，在直角坐标平面内，已知点A(8,0)，点B(3,0)，点C是点A关于点B的对称点.\\\ （2）", "如果点P在y轴上", "，过点P作直线l//x轴，点A关于直线l的对称点是点D，那么当三角形BCD的面积等于10时，求点P的坐标.", alignment='')
        ques.shift(3.1*UP)
        ques.scale(0.6)
        dot_c = Dot(axes.c2p(-2, 0))
        let_c = TextMobject("C")
        let_c.scale(0.6)
        let_c.next_to(dot_c, DOWN, buff=0.1)
        dot_a = Dot(axes.c2p(8, 0))
        dot_b = Dot(axes.c2p(3, 0))
        let_a = TextMobject("A").scale(0.6)
        let_b = TextMobject("B").scale(0.6)
        let_a.next_to(dot_a, DOWN, 0.1)
        let_b.next_to(dot_b, DOWN, 0.1)
        dot_p = Dot(axes.c2p(0, 2))
        let_p = TextMobject("P")
        let_p.scale(0.6)
        let_p.next_to(dot_p, LEFT, buff=0.1)
        let_p.shift(0.3*UP)
        l_l = Line(axes.c2p(-2, 2), axes.c2p(9, 2))
        let_l = TexMobject("l")
        let_l.scale(0.6)
        let_l.next_to(l_l, LEFT, buff=0.1)
        dot_d = Dot(axes.c2p(8, 4))
        let_d = TextMobject("D")
        let_d.scale(0.6)
        let_d.next_to(dot_d, UP, buff=0.1)
        l_ad = DashedLine(dot_a, dot_d)
        l_cd = Line(dot_c, dot_d)
        l_bd = Line(dot_b, dot_d)

        self.add(group, ques, dot_c, let_c, dot_a, let_a, dot_b, let_b, dot_p, let_p, l_l, let_l, dot_d, let_d, l_ad, l_bd, l_cd)

        sol_s_tri_bcd = TexMobject("\\because", "{{S}_{\\triangle BCD}}", "=10", alignment='')
        sol_s_tri_bcd.scale(0.6)
        sol_s_tri_bcd.next_to(ques, DOWN, buff=0.6)
        sol_s_tri_bcd.align_to(ques, LEFT)
        csol_s_tri_bcd = TexMobject("\\because", "{S}_{\\triangle BCD}", "=\\frac{1}{2}BC\\times", "AD", "=10",
                                    alignment='')
        csol_s_tri_bcd.scale(0.6)
        csol_s_tri_bcd.next_to(ques, DOWN, buff=0.6)
        csol_s_tri_bcd.align_to(ques, LEFT)
        cn_s_tri = TextMobject("（三角形的面积公式）")
        cn_s_tri.scale(0.6)
        cn_s_tri.next_to(csol_s_tri_bcd, buff=0.1)
        sol_l_bc = TextMobject("$BC = 5$（已证）")
        sol_l_bc.scale(0.6)
        sol_l_bc.align_to(csol_s_tri_bcd, LEFT)
        sol_l_bc.next_to(csol_s_tri_bcd, DOWN)
        sol_l_ad = TexMobject("\\therefore", "AD", "= 4")
        sol_l_ad.shift(4.4*LEFT+0.4*UP)
        sol_l_ad.scale(0.6)
        eproperty = TextMobject("（等式性质）")
        eproperty.scale(0.6)
        eproperty.next_to(sol_l_ad)
        sol_l_am0 = TextMobject("又$\\because$", "点A关于直线l的对称点是点D", "（已知）")
        sol_l_am0.scale(0.6)
        sol_l_am0.next_to(sol_l_ad, DOWN)
        sol_l_am0.align_to(sol_l_ad, LEFT)
        property0 = TextMobject("对称轴是对称点连线的垂直平分线")
        property0.scale(0.6)
        property0.next_to(sol_l_am0, DOWN)
        property0.align_to(sol_l_am0, LEFT)
        sol_l_am1 = TexMobject("\\therefore", "AM", "= \\frac{1}{2}", "AD", "= 2")
        sol_l_am1.scale(0.6)
        sol_l_am1.next_to(sol_l_am0, DOWN)
        sol_l_am1.align_to(sol_l_am0, LEFT)
        csol_l_am1 = TextMobject("（轴对称的性质）")
        csol_l_am1.scale(0.6)
        csol_l_am1.next_to(sol_l_am1)
        sol_l_op0 = TextMobject("又$\\because$", "$l // x$", "轴", "（已知）")
        sol_l_op0.scale(0.6)
        sol_l_op0.align_to(sol_l_am1, LEFT)
        sol_l_op0.next_to(sol_l_am1, DOWN)
        property1 = TextMobject("平行线之间的距离处处相等")
        property1.scale(0.6)
        property1.next_to(sol_l_op0, DOWN)
        property1.align_to(sol_l_op0, LEFT)
        sol_l_op1 = TexMobject("\\therefore", "OP", "=", "AM", "= 2")
        sol_l_op1.scale(0.6)
        sol_l_op1.align_to(sol_l_op0, LEFT)
        sol_l_op1.next_to(sol_l_op0, DOWN)
        csol_l_op1 = TextMobject("（平行线间距离的意义）")
        csol_l_op1.scale(0.6)
        csol_l_op1.next_to(sol_l_op1)

        group = VGroup(csol_s_tri_bcd, cn_s_tri, sol_l_bc, sol_l_ad, eproperty, sol_l_am0, sol_l_am1, csol_l_am1, sol_l_op0, sol_l_op1, csol_l_op1)
        self.add(group)

        self.play(ApplyMethod(group.scale, 0.6))
        self.play(ApplyMethod(group.shift, UP+1.4*LEFT))
        self.wait()

        self.play(ApplyMethod(ques[1].set_color, YELLOW))
        self.wait(7)

        kind0 = TextMobject("1° 当点P在y轴正半轴上时，")
        kind0.scale(0.6)
        kind0.next_to(group, DOWN)
        kind0.align_to(group, LEFT)
        kind1 = TextMobject("2° 当点P在y轴负半轴上时，")
        kind1.scale(0.6)
        kind1.next_to(kind0, DOWN)
        kind1.align_to(kind0, LEFT)

        self.play(
            Write(kind0),
            Write(kind1)
        )
        self.wait()

        kind0_p = TexMobject("P(0, 0+2)")
        kind0_p.scale(0.6)
        kind0_p.next_to(kind0, DOWN)
        kind0_p.align_to(kind0, LEFT)
        nkind1 = kind1.copy()
        nkind1.next_to(kind0_p, DOWN)
        nkind1.align_to(kind0_p, LEFT)

        self.play(
            Write(kind0_p),
            Transform(kind1, nkind1)
        )

        nkind0_p = TexMobject("P(0, 2)")
        nkind0_p.scale(0.6)
        nkind0_p.next_to(kind0, DOWN)
        nkind0_p.align_to(kind0, LEFT)

        self.play(Transform(kind0_p, nkind0_p))

        kind1_p = TexMobject("P(0, 0-2)")
        kind1_p.scale(0.6)
        kind1_p.next_to(kind1, DOWN)
        kind1_p.align_to(kind1, LEFT)

        self.play(Write(kind1_p))

        nkind1_p = TexMobject("P(0, -2)")
        nkind1_p.scale(0.6)
        nkind1_p.next_to(kind1, DOWN)
        nkind1_p.align_to(kind1, LEFT)

        ans = TextMobject("$\\therefore$综上所述，当点P在y轴正半轴上时，P(0, 2)；当点P在y轴负半轴上时，P(0, -2).",alignment='')
        ans.scale(0.6)
        ans.next_to(nkind1_p, DOWN)
        ans.align_to(nkind1_p, LEFT)

        self.play(
            Transform(kind1_p, nkind1_p),
            Write(ans)
        )
        self.wait()

class sum(Scene):
    def construct(self):
        t = TextMobject("总结")
        t.to_edge(UP)

        one = TextMobject("第一问：先算出$AB$的长度，再通过中心对称的性质证出$BC=AB$，进而推导出点$C$的坐标", alignment='')
        two = TextMobject("第二问：通过$\\triangle BCD$的面积和底边$BC$求出高$AD$的长度，然后通过轴对称的性质求出$AM$的长度，再利用平行线间距离的意义求出$OP$的长度，最后分类讨论求出点$P$的坐标", alignment='')
        one.scale(0.7)
        one.next_to(t, DOWN, buff=1)
        one.to_edge(LEFT)
        two.scale(0.7)
        two.next_to(one, DOWN)
        two.align_to(one, LEFT)

        self.play(FadeIn(t), FadeIn(one), FadeIn(two))
        self.wait()
