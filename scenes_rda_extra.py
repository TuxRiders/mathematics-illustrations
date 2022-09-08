from manim import *

class ReactionDiffusionAdvectionExtra(Scene):
    def construct(self):

        title = Text("Classification of PDEs").shift(UP * 1.5)
        title2 = Text("Parabolic equations").shift(DOWN * 0)
        title3 = Text("Reaction-Diffusion-Advection PDE").shift(DOWN * 1.5)

        self.play(Write(title))
        self.wait(5)

        self.play(Write(title2))
        self.wait(5)

        self.play(Write(title3))
        self.wait(5)

        self.play(
            FadeOut(title),
            FadeOut(title2),
            ApplyMethod(title3.to_edge, UP)
        )
        self.wait(5)
