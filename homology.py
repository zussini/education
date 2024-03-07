from manim import *

class HomologyIn3D(Scene):
    def construct(self):
        # Solid Sphere (H0=1, H1=0, H2=0)
        solid_sphere = Sphere()
        solid_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 0, \ ", r"H_2 = 0").next_to(solid_sphere, DOWN)

        # Hollow Sphere (H0=1, H1=0, H2=1)
        hollow_sphere = Sphere().set_fill(opacity=0.5)
        hollow_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 0, \ ", r"H_2 = 1").next_to(hollow_sphere, DOWN)

        # Torus (H0=1, H1=1, H2=1)
        torus = Torus()
        torus_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 1, \ ", r"H_2 = 1").next_to(torus, DOWN)

        # Solid Sphere Scene
        self.play(Create(solid_sphere))
        self.play(Write(solid_text))
        self.wait(2)

        # Transition to Hollow Sphere
        self.play(ReplacementTransform(solid_sphere, hollow_sphere))
        self.play(Transform(solid_text, hollow_text))
        self.wait(2)

        # Transition to Torus
        self.play(ReplacementTransform(hollow_sphere, torus))
        self.play(Transform(solid_text, torus_text))
        self.wait(2)

        self.clear()

        # More complex shapes can be added similarly

if __name__ == "__main__":
    HomologyIn3D().render()

