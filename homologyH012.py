from manim import *

class HomologyIn3D(ThreeDScene):
    def construct(self):
        # Adjust camera settings
        self.move_camera(phi=25 * DEGREES, theta=-90 * DEGREES, frame_center=(0, 0, 0))

        # Solid Sphere (H0=1, H1=0, H2=0)
        solid_sphere = Sphere()
        solid_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 0, \ ", r"H_2 = 0").to_edge(UP)
        description_text = Text("Ball", font_size=24).next_to(solid_sphere, DOWN)

        # Hollow Sphere (H0=1, H1=0, H2=1)
        hollow_sphere = Sphere().set_fill(opacity=0.3)
        hollow_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 0, \ ", r"H_2 = 1").to_edge(UP)
        hollow_description = Text("Transition to Sphere", font_size=24).next_to(hollow_sphere, DOWN)

        # Torus (H0=1, H1=1, H2=1)
        torus = Torus().set_fill(opacity=0.3)
        torus_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 1, \ ", r"H_2 = 1").to_edge(UP)
        torus_description = Text("Torus surface", font_size=24).next_to(torus, DOWN)

        # Adjust the scale if necessary
        self.scale_objects([solid_sphere, hollow_sphere, torus, description_text, hollow_description, torus_description])

        # Solid Sphere Scene
        self.play(Create(solid_sphere), Write(description_text))
        self.play(Write(solid_text))
        self.wait(2)

        # Transition to Hollow Sphere
        self.play(Transform(solid_sphere, hollow_sphere), Transform(description_text, hollow_description))
        self.play(Transform(solid_text, hollow_text))
        self.wait(2)

        self.play(Transform(hollow_sphere, torus),FadeOut(solid_sphere),Transform(description_text, torus_description),Transform(solid_text, torus_text))
        self.wait(2)
        self.clear()

    def scale_objects(self, objects):
        for obj in objects:
            obj.scale(0.75)  # Scale down by 25%

if __name__ == "__main__":
    HomologyIn3D().render()
