from manim import *

wait_time = 1

single_variable_u = MathTex("u = u(t)", substrings_to_isolate=["u", "t"])
multi_variable_u = MathTex("u = u(x, t)", substrings_to_isolate=["u", "x", "t"])
ode_motion = MathTex("m","{d^2u", "\over", "dt^2}", "=-k", "{du", "\over", "dt}", substrings_to_isolate=["u", "t"])
# ode_kinteics = MathTex("{du", "\over", "dt}", "=-ku", substrings_to_isolate=["u", "t"])
ode_kinteics1 = MathTex("{du", "\over", "dt}", substrings_to_isolate=["u", "t"])
ode_kinteics2 = MathTex("=-ku", substrings_to_isolate=["u"])
ode_kinteics_solution = MathTex("\Rightarrow u({{t}}) = u_0 e^{-k{{t}}}", substrings_to_isolate=["u"])
# pde_heat = MathTex("{\partial u", "\over", "\partial {{t}}}", r"=\alpha", "{\partial ^{2} u", "\over", "\partial x^2}", substrings_to_isolate=["u", "x"])
pde_heat1 = MathTex("{\partial u", "\over", "\partial {{t}}}", substrings_to_isolate=["u"])
pde_heat2 = MathTex(r"=\alpha^2", "{\partial ^{2} u", "\over", "\partial x^2}", substrings_to_isolate=["u", "x"])

general_u = MathTex("u = u(x, y)")
general = MathTex("A", r"\frac{\partial^{2} u}{\partial x^{2}}+", "B", r"\frac{\partial^{2} u}{\partial x \partial y}+", "C", r"\frac{\partial^{2} u}{\partial y^{2}}", r"+D \frac{\partial u}{\partial x}+E \frac{\partial u}{\partial y}+F u+G=0")
parabolic_crit = MathTex("B^2-4AC = 0", substrings_to_isolate=["A", "B", "C"])
elliptic_crit = MathTex("B^2-4AC < 0", substrings_to_isolate=["A", "B", "C"])
hyperbolic_crit = MathTex("B^2-4AC > 0", substrings_to_isolate=["A", "B", "C"])

parabolic_example = MathTex(r"\text{Heat equation: }", r"\frac{\partial u}{\partial t} = \alpha^2 \frac{\partial ^{2} u}{\partial x^{2}}, \quad u = u(t, x)")
elliptic_example = MathTex(r"\text{Poisson's equation: }", r"\frac{\partial ^{2} u}{\partial x^{2}} + \frac{\partial ^{2} u}{\partial y^{2}} = f(x, y), \quad u = u(x, y)")
hyperbolic_example = MathTex(r"\text{Wave equation: }", r"\frac{\partial ^{2} u}{\partial t^{2}} = c^2 \frac{\partial ^{2} u}{\partial x^{2}}, \quad u = u(t, x)")

parabolic_general = MathTex("0", r"\frac{\partial^{2} u}{\partial t^{2}}+", "0", r"\frac{\partial^{2} u}{\partial t \partial x}+", r"(-\alpha^2)", r"\frac{\partial^{2} u}{\partial x^{2}}", r"+1 \frac{\partial u}{\partial t}+0 \frac{\partial u}{\partial x}+0 u+0=0")
elliptic_general = MathTex("1", r"\frac{\partial^{2} u}{\partial x^{2}}+", "0", r"\frac{\partial^{2} u}{\partial x \partial y}+", "1", r"\frac{\partial^{2} u}{\partial y^{2}}", r"+0 \frac{\partial u}{\partial x}+0 \frac{\partial u}{\partial y}+0 u-f=0")
hyperbolic_general = MathTex("1", r"\frac{\partial^{2} u}{\partial t^{2}}+", "0", r"\frac{\partial^{2} u}{\partial t \partial x}+", r"(-c^2)", r"\frac{\partial^{2} u}{\partial x^{2}}", r"+1 \frac{\partial u}{\partial t}+0 \frac{\partial u}{\partial x}+0 u+0=0")

title = Text("Differential equations")
title_ode = Text("Ordinary differential equation (ODE)").scale(0.75)
title_pde = Text("Partial differential equation (PDE)").scale(0.75)

single_variable_u.set_color_by_tex("u", YELLOW)
ode_motion.set_color_by_tex("u", YELLOW)
ode_kinteics1.set_color_by_tex("u", YELLOW)
ode_kinteics2.set_color_by_tex("u", YELLOW)
ode_kinteics_solution.set_color_by_tex("u", YELLOW)
ode_kinteics_solution.set_color_by_tex("u", YELLOW)

single_variable_u.set_color_by_tex("t", BLUE)
ode_motion.set_color_by_tex("t", BLUE)
ode_kinteics1.set_color_by_tex("t", BLUE)
ode_kinteics_solution.set_color_by_tex("t", BLUE, substring=False)

multi_variable_u.set_color_by_tex("u", YELLOW)
multi_variable_u.set_color_by_tex("t", BLUE, substring=False)
multi_variable_u.set_color_by_tex("x", RED)
pde_heat1.set_color_by_tex("u", YELLOW)
pde_heat1.set_color_by_tex("t", BLUE, substring=False)
pde_heat2.set_color_by_tex("u", YELLOW)
pde_heat2.set_color_by_tex("x", RED)

title_class = Text("Classification of PDEs")
title_second = Text("2nd order").scale(0.75)
title_linear = Text("linear").scale(0.75)

elliptic = Text("Elliptic PDE").scale(0.75)
parabolic = Text("Parabolic PDE").scale(0.75)
hyperbolic = Text("Hyperbolic PDE").scale(0.75)

elliptic_crit.set_color_by_tex("A", RED)
elliptic_crit.set_color_by_tex("B", BLUE)
elliptic_crit.set_color_by_tex("C", YELLOW)
parabolic_crit.set_color_by_tex("A", RED)
parabolic_crit.set_color_by_tex("B", BLUE)
parabolic_crit.set_color_by_tex("C", YELLOW)
hyperbolic_crit.set_color_by_tex("A", RED)
hyperbolic_crit.set_color_by_tex("B", BLUE)
hyperbolic_crit.set_color_by_tex("C", YELLOW)

parabolic_example[0].set_color(GREEN)
elliptic_example[0].set_color(GREEN)
hyperbolic_example[0].set_color(GREEN)

parabolic_general[0].set_color(RED)
parabolic_general[2].set_color(BLUE)
parabolic_general[4].set_color(YELLOW)
elliptic_general[0].set_color(RED)
elliptic_general[2].set_color(BLUE)
elliptic_general[4].set_color(YELLOW)
hyperbolic_general[0].set_color(RED)
hyperbolic_general[2].set_color(BLUE)
hyperbolic_general[4].set_color(YELLOW)

class PDE(Scene):
    def construct(self):

        title.to_edge(UP)
        self.play(Write(title))
        self.wait(wait_time)

        self.play(Write(title_ode))
        self.wait(wait_time)

        self.play(ApplyMethod(title_ode.move_to, UP * 2))
        self.wait(wait_time)

        self.play(Write(single_variable_u))
        self.wait(wait_time)

        self.play(ApplyMethod(single_variable_u.move_to, UP * 1))
        self.wait(wait_time)

        ode_motion.move_to(DOWN * 0.5)
        self.play(Write(ode_motion))
        self.wait(wait_time)


        ode_kinteics1.move_to(DOWN * 2)
        ode_kinteics2.move_to(ode_kinteics1, RIGHT)
        ode_kinteics1.shift(0.7 * LEFT)
        ode_kinteics2.shift(0.9 * RIGHT)
        self.play(AnimationGroup(Write(ode_kinteics1), Write(ode_kinteics2)))
        self.wait(wait_time)

        self.play(AnimationGroup(ApplyMethod(ode_kinteics1.move_to, LEFT * 3 + DOWN * 2),
                                 ApplyMethod(ode_kinteics2.move_to, LEFT * 1.9 + DOWN * 2)))
        self.wait(wait_time)

        ode_kinteics_solution.move_to(DOWN * 2 + RIGHT * 1.8)
        self.play(Write(ode_kinteics_solution))
        self.wait(wait_time)

        self.play(
            Uncreate(title_ode),
            Uncreate(single_variable_u),
            Uncreate(ode_motion),
            Uncreate(ode_kinteics1),
            Uncreate(ode_kinteics2),
            Uncreate(ode_kinteics_solution)
        )
        self.wait(wait_time)

        self.play(Write(title_pde))
        self.wait(wait_time)

        self.play(ApplyMethod(title_pde.move_to, UP * 2))
        self.wait(wait_time)

        self.play(Write(multi_variable_u))
        self.wait(wait_time)

        self.play(ApplyMethod(multi_variable_u.move_to, UP * 0.5))
        self.wait(wait_time)

        pde_heat1.move_to(DOWN * 1)
        pde_heat2.move_to(pde_heat1, RIGHT)
        pde_heat1.shift(0.9 * LEFT)
        pde_heat2.shift(1 * RIGHT)
        self.play(AnimationGroup(Write(pde_heat1), Write(pde_heat2)))
        self.wait(wait_time)

        self.play(
            Uncreate(title_pde),
            Uncreate(multi_variable_u),
            Uncreate(pde_heat1),
            Uncreate(pde_heat2),
            Uncreate(title),
        )
        self.wait(wait_time)


        title_class.to_edge(UP)
        self.play(Write(title_class))
        self.wait(wait_time)

        title_second.move_to(UP * 2)
        title_second.shift(LEFT * 2)
        title_linear.move_to(UP * 2)
        title_linear.shift(RIGHT * 2)

        self.play(Write(title_second))
        self.wait(wait_time)

        self.play(Write(title_linear))
        self.wait(wait_time)

        general_u.move_to(UP * 0.5)
        self.play(Write(general_u))
        self.wait(wait_time)

        general.move_to(DOWN * 1.5)
        self.play(Write(general))
        self.wait(wait_time)

        self.play(
            FadeOut(title_second),
            FadeOut(title_linear),
            FadeOut(general_u),
            ApplyMethod(general.move_to, UP * 1.5)
        )
        self.wait(wait_time)

        framebox1 = SurroundingRectangle(general[0], buff = .1, corner_radius=0.2, color=RED)
        framebox2 = SurroundingRectangle(general[2], buff = .1, corner_radius=0.2, color=BLUE)
        framebox3 = SurroundingRectangle(general[4], buff = .1, corner_radius=0.2, color=YELLOW)

        self.play(Create(framebox1))
        self.wait(wait_time)

        self.play(Create(framebox2))
        self.wait(wait_time)

        self.play(Create(framebox3))
        self.wait(wait_time)

        elliptic_crit.move_to(LEFT * 2 + UP * 0)
        self.play(Write(elliptic_crit))
        self.wait(wait_time)

        elliptic.move_to(RIGHT * 2 + DOWN * 0.1)
        self.play(Write(elliptic))
        self.wait(wait_time)

        parabolic_crit.move_to(LEFT * 2 + DOWN * 1)
        self.play(Write(parabolic_crit))
        self.wait(wait_time)

        parabolic.move_to(RIGHT * 2 + DOWN * 1.1)
        self.play(Write(parabolic))
        self.wait(wait_time)

        hyperbolic_crit.move_to(LEFT * 2 + DOWN * 2)
        self.play(Write(hyperbolic_crit))
        self.wait(wait_time)

        hyperbolic.move_to(RIGHT * 2 + DOWN * 2.1)
        self.play(Write(hyperbolic))
        self.wait(wait_time)

        parabolic_crit.save_state()
        parabolic.save_state()
        elliptic_crit.save_state()
        elliptic.save_state()
        hyperbolic_crit.save_state()
        hyperbolic.save_state()

        self.play(
            Uncreate(elliptic_crit),
            Uncreate(elliptic),
            Uncreate(parabolic_crit),
            Uncreate(parabolic),
            Uncreate(hyperbolic_crit),
            Uncreate(hyperbolic),
        )
        self.wait(wait_time)

        self.play(Write(parabolic_example))
        self.wait(wait_time)

        parabolic_general.shift(1.5 * DOWN)
        general_copy = general.copy()
        self.play(Transform(general_copy, parabolic_general))
        self.wait(wait_time)

        parabolic_crit.restore()
        parabolic.restore()
        parabolic_crit.to_edge(DOWN).shift(0.4 * UP)
        parabolic.to_edge(DOWN).shift(0.4 * UP)

        self.play(Write(parabolic_crit))
        self.wait(wait_time)

        self.play(Write(parabolic))
        self.wait(wait_time)

        self.play(
            Uncreate(parabolic_example),
            Uncreate(parabolic_general),
            Uncreate(general_copy),
            Uncreate(parabolic_crit),
            Uncreate(parabolic)
        )
        self.wait(wait_time)

        self.play(Write(elliptic_example))
        self.wait(wait_time)

        elliptic_general.shift(1.5 * DOWN)
        general_copy = general.copy()
        self.play(Transform(general_copy, elliptic_general))
        self.wait(wait_time)

        elliptic_crit.restore()
        elliptic.restore()
        elliptic_crit.to_edge(DOWN).shift(0.4 * UP)
        elliptic.to_edge(DOWN).shift(0.4 * UP)

        self.play(Write(elliptic_crit))
        self.wait(wait_time)

        self.play(Write(elliptic))
        self.wait(wait_time)

        self.play(
            Uncreate(elliptic_example),
            Uncreate(elliptic_general),
            Uncreate(general_copy),
            Uncreate(elliptic_crit),
            Uncreate(elliptic)
        )
        self.wait(wait_time)

        self.play(Write(hyperbolic_example))
        self.wait(wait_time)

        hyperbolic_general.shift(1.5 * DOWN)
        general_copy = general.copy()
        self.play(Transform(general_copy, hyperbolic_general))
        self.wait(wait_time)

        hyperbolic_crit.restore()
        hyperbolic.restore()
        hyperbolic_crit.to_edge(DOWN).shift(0.4 * UP)
        hyperbolic.to_edge(DOWN).shift(0.4 * UP)

        self.play(Write(hyperbolic_crit))
        self.wait(wait_time)

        self.play(Write(hyperbolic))
        self.wait(wait_time)

        self.play(
            Uncreate(hyperbolic_example),
            Uncreate(hyperbolic_general),
            Uncreate(general_copy),
            Uncreate(hyperbolic_crit),
            Uncreate(hyperbolic),
            Uncreate(framebox1),
            Uncreate(framebox2),
            Uncreate(framebox3),
            Uncreate(general)
        )
        self.wait(wait_time)

        self.play(
            Uncreate(title_class)
        )
        self.wait(wait_time)
