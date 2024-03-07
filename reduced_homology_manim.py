from manim import *

class PathConnectedSpace(Scene):
    def construct(self):
        circle = Circle()
        self.play(ShowCreation(circle))
        text = MathTex("\\tilde{H}_0 = 0")
        self.play(Write(text))
        self.wait(2)

class TwoDiscretePoints(Scene):
    def construct(self):
        points = [Dot().move_to(LEFT), Dot().move_to(RIGHT)]
        self.play(*[ShowCreation(dot) for dot in points])
        text = MathTex("\\tilde{H}_0 = \\mathbb{Z}")
        self.play(Write(text))
        self.wait(2)

class ThreeSeparateCircles(Scene):
    def construct(self):
        circles = [Circle(radius=0.3).shift(LEFT + 2*LEFT*i) for i in range(3)]
        self.play(*[ShowCreation(circle) for circle in circles])
        text = MathTex("\\tilde{H}_0 = \\mathbb{Z}^2")
        self.play(Write(text))
        self.wait(2)

class TorusScene(Scene):
    def construct(self):
        torus = Circle() # Simplified representation
        handle = Line(UP, DOWN)
        self.play(ShowCreation(torus), ShowCreation(handle))
        text = MathTex("H_0 = \\mathbb{Z}, H_1 = \\mathbb{Z}^2, H_2 = \\mathbb{Z}\\\\"
                       "\\tilde{H}_0 = 0, \\tilde{H}_1 = \\mathbb{Z}^2, \\tilde{H}_2 = \\mathbb{Z}")
        self.play(Write(text))
        self.wait(2)

