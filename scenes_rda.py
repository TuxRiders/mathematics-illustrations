from manim import *

class ReactionDiffusionAdvection(Scene):
    def construct(self):

        title = Text("Reaction-Diffusion-Advection PDE")
        title.to_edge(UP)

        equation = MathTex(
            "\\frac{\partial u}{\partial t}","=","\\nabla \\cdot [D \\nabla u]",
            "-","\\nabla \\cdot \\left( \\textbf{v} u \\right)","+","f(u)"
        )


        arrow1 = Arrow(ORIGIN, [0, -1, 0], buff=0, color=ORANGE)
        arrow2 = Arrow(ORIGIN, [0, -1, 0], buff=0, color=BLUE)
        arrow3 = Arrow(ORIGIN, [0, -1, 0], buff=0, color=BLUE)
        arrow4 = Arrow(ORIGIN, [0, -1, 0], buff=0, color=GREEN)
        arrow5 = Arrow(ORIGIN, [0, -1, 0], buff=0, color=GREEN)
        arrow1.next_to(np.array([-0.85, 1.2, 0]), UP)
        arrow2.next_to(np.array([-2.2, 1.2, 0]), UP)
        arrow3.next_to(np.array([0.65, 1.2, 0]), UP)
        arrow4.next_to(np.array([-0.85, 1.2, 0]), UP)
        arrow5.next_to(np.array([-2.2, 1.2, 0]), UP)

        equation_c = MathTex("u=u \\left(x,y,z,t \\right)")

        equation_aux1 = MathTex(
            "{\\nabla f={\\begin{pmatrix}{\\frac {\\partial }{\\partial x}},\\ {\\frac {\\partial }{\\partial y}},\\ {\\frac {\\partial }{\\partial z}}\\end{pmatrix}}f={\\frac {\\partial f}{\\partial x}}\\mathbf {i} +{\\frac {\\partial f}{\\partial y}}\\mathbf {j} +{\\frac {\\partial f}{\\partial z}}\\mathbf {k} }"
        ).set_color(ORANGE)
        equation_aux1.scale(0.75)

        equation_aux2 = MathTex(
            "{ \\nabla \\cdot \\mathbf {F} ={\\begin{pmatrix}{\\frac {\\partial }{\\partial x}},\\ {\\frac {\\partial }{\\partial y}},\\ {\\frac {\\partial }{\\partial z}}\\end{pmatrix}}\\cdot {\\begin{pmatrix}F_{x},\\ F_{y},\\ F_{z}\\end{pmatrix}}={\\frac {\\partial F_{x}}{\\partial x}}+{\\frac {\\partial F_{y}}{\\partial y}}+{\\frac {\\partial F_{z}}{\\partial z}}}"
        ).set_color(BLUE)
        equation_aux2.scale(0.75)

        equation_aux3 = MathTex(
            "{\\displaystyle \\Delta f=\\nabla ^{2}\\!f=(\\nabla \\cdot \\nabla )f={\\frac {\\partial ^{2}\\!f}{\\partial x^{2}}}+{\\frac {\\partial ^{2}\\!f}{\\partial y^{2}}}+{\\frac {\\partial ^{2}\\!f}{\\partial z^{2}}}}"
        ).set_color(GREEN)
        equation_aux3.scale(0.75)

        equation_sample0 = MathTex(
            "\\rho c_{p}{\\frac {\\partial T}{\\partial t}}","-",
            "\\nabla \\cdot \\left(k\\nabla T\\right)","=","{\\dot {q}}_{V}"
        ).set_color(RED)

        equation_sample1 = MathTex(
            "\\frac{\\partial C_{\\mathrm{Mg}}}{\\partial t}","=","\\nabla \\cdot \\left(D_{\\mathrm{Mg}}^{e}"
            "\\nabla C_{\\mathrm{Mg}} \\right)","-","k_{1} C_{\\mathrm{Mg}} +k_{2} C_{\\mathrm{Film}} [\\mathrm{Cl}]^{2}"
        ).set_color(BLUE)

        equation_sample2 = MathTex(
            "\\frac {\\partial \\mathbf {u} }{\\partial t}","+","(\\mathbf {u} \\cdot \\nabla )\\mathbf {u}",
            "-","\\nu \\nabla ^{2}\\mathbf {u}","=","-\\nabla w+\\mathbf {g}"
        ).set_color(GREEN)

        sample0_title = Text("Heat transfer \n     in solids").set_color(RED)
        sample0_title.scale(0.75)
        sample1_title = Text("      Mass transfer \nin corrosion process").set_color(BLUE)
        sample1_title.scale(0.75)
        sample2_title = Text("Navier-Stokes \n  in fluid flow").set_color(GREEN)
        sample2_title.scale(0.75)

        sample1_title.to_edge(DOWN)
        sample0_title.next_to(sample1_title, LEFT, aligned_edge=UP)
        sample2_title.next_to(sample1_title, RIGHT, aligned_edge=UP)

        self.play(Write(title))
        self.wait(1)

        self.play(Write(equation))
        self.wait(1)

        equation_c.move_to(DOWN * 1.5)
        self.play(Write(equation_c))
        self.wait(1)

        self.play(Uncreate(equation_c))
        self.wait(1)

        self.play(ApplyMethod(equation.move_to, UP * 1))
        self.wait(1)

        equation_aux1.move_to(DOWN * 0.5)
        equation_aux2.move_to(DOWN * 1.7)
        equation_aux3.move_to(DOWN * 2.9)

        self.play(
            Write(equation_aux1),
            GrowArrow(arrow1)
        )
        self.wait(1)
        self.play(
            Write(equation_aux2),
            GrowArrow(arrow2),
            GrowArrow(arrow3)
        )
        self.wait(1)
        self.play(
            Write(equation_aux3),
            ReplacementTransform(arrow1, arrow4),
            ReplacementTransform(arrow2, arrow5),
        )
        self.wait(1)

        self.play(
            Uncreate(equation_aux1),
            Uncreate(equation_aux2),
            Uncreate(equation_aux3),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(arrow5),
        )
        self.wait(1)

        framebox0 = SurroundingRectangle(equation[0], buff = .1)
        framebox1 = SurroundingRectangle(equation[2], buff = .1)
        framebox2 = SurroundingRectangle(equation[4], buff = .1)
        framebox3 = SurroundingRectangle(equation[6], buff = .1)

        text0 = Text('Temporal evolution').next_to(framebox0, DOWN)
        text0.scale(0.75)
        text1 = Text('Diffusion').next_to(framebox1, DOWN)
        text1.scale(0.75)
        text2 = Text('Convection').next_to(framebox2, DOWN)
        text2.scale(0.75)
        text3 = Text('Source/Reaction').next_to(framebox3, DOWN)
        text3.scale(0.75)

        self.play(
            Create(framebox0),
            FadeIn(text0),
        )
        self.wait(1)
        self.play(
            FadeOut(text0),
            ReplacementTransform(framebox0,framebox1),
            FadeIn(text1),
        )
        self.wait(1)
        self.play(
            FadeOut(text1),
            ReplacementTransform(framebox1,framebox2),
            FadeIn(text2),
        )
        self.wait(1)
        self.play(
            FadeOut(text2),
            ReplacementTransform(framebox2,framebox3),
            FadeIn(text3),
        )
        self.wait(1)

        self.play(
            FadeOut(text3),
            FadeOut(framebox3),
        )
        self.wait(1)

        self.play(
            FadeOut(title),
            ApplyMethod(equation.to_edge, UP)
        )
        self.wait(1)

        self.play(
            Write(equation_sample0),
            Write(sample0_title)
        )
        self.wait(1)

        self.play(
            ApplyMethod(equation_sample0.move_to, UP * 1.5),
            Write(equation_sample1),
            Write(sample1_title)
        )
        self.wait(1)

        equation_sample2.move_to(DOWN * 1.5)
        self.play(
            Write(equation_sample2),
            Write(sample2_title)
        )
        self.wait(1)


        framebox0 = SurroundingRectangle(equation[0], buff = .1)
        framebox1 = SurroundingRectangle(equation[2], buff = .1)
        framebox2 = SurroundingRectangle(equation[4], buff = .1)
        framebox3 = SurroundingRectangle(equation[6], buff = .1)
        framebox0_equation0 = SurroundingRectangle(equation_sample0[0], buff = .1)
        framebox1_equation0 = SurroundingRectangle(equation_sample0[2], buff = .1)
        framebox2_equation0 = SurroundingRectangle(equation_sample0[4], buff = .1)
        framebox0_equation1 = SurroundingRectangle(equation_sample1[0], buff = .1)
        framebox1_equation1 = SurroundingRectangle(equation_sample1[2], buff = .1)
        framebox2_equation1 = SurroundingRectangle(equation_sample1[4], buff = .1)
        framebox0_equation2 = SurroundingRectangle(equation_sample2[0], buff = .1)
        framebox1_equation2 = SurroundingRectangle(equation_sample2[2], buff = .1)
        framebox2_equation2 = SurroundingRectangle(equation_sample2[4], buff = .1)
        framebox3_equation2 = SurroundingRectangle(equation_sample2[6], buff = .1)

        self.play(
            Create(framebox0),
            Create(framebox0_equation0),
            Create(framebox0_equation1),
            Create(framebox0_equation2),
        )
        self.wait(1)

        self.play(
            ReplacementTransform(framebox0,framebox1),
            ReplacementTransform(framebox0_equation0,framebox1_equation0),
            ReplacementTransform(framebox0_equation1,framebox1_equation1),
            ReplacementTransform(framebox0_equation2,framebox2_equation2),
        )
        self.wait(1)

        self.play(
            ReplacementTransform(framebox1,framebox3),
            ReplacementTransform(framebox1_equation0,framebox2_equation0),
            ReplacementTransform(framebox1_equation1,framebox2_equation1),
            ReplacementTransform(framebox2_equation2,framebox3_equation2),
        )
        self.wait(1)

        self.play(
            ReplacementTransform(framebox3,framebox2),
            FadeOut(framebox2_equation0),
            FadeOut(framebox2_equation1),
            ReplacementTransform(framebox3_equation2,framebox1_equation2),
        )
        self.wait(1)

        self.play(
            Uncreate(equation),
            Uncreate(equation_sample0),
            Uncreate(equation_sample1),
            Uncreate(equation_sample2),
            Uncreate(framebox1_equation2),
            Uncreate(framebox2),
            Uncreate(sample0_title),
            Uncreate(sample1_title),
            Uncreate(sample2_title),
        )

        self.wait(1)
