from manim import *

class HomologyIn3D(ThreeDScene):
    def construct(self):
        # Adjust camera settings
        # Camera settings
        self.move_camera(phi=25 * DEGREES, theta=-45 * DEGREES, frame_center=(0, 0, 0))

        # Function to create a grid of objects
        def create_object_grid(n, object_type, **kwargs):
            grid = VGroup(*[object_type(**kwargs) for _ in range(n*n)])
            grid.arrange_in_grid(n, n, buff=1)
            return grid

        # Initial single Torus
        torus = Torus().set_fill(opacity=0.3)
        description_text = Text("1 Torus", font_size=24)
        homology_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 1, \ ", r"H_2 = 1").to_edge(UP)

        # Create and animate the grid
        for n in [1, 2, 4]:  # You can add more numbers here
            new_grid = create_object_grid(n, Torus, major_radius=0.5, minor_radius=0.2).set_fill(opacity=0.3)
            new_description = Text(f"{n*n} Tori", font_size=24)
            new_homology = MathTex(rf"H_0 = {n*n}, \ ", r"H_1 = 1, \ ", r"H_2 = 1").to_edge(UP)

            self.play(Transform(torus, new_grid), Transform(description_text, new_description), Transform(homology_text, new_homology))
            self.wait(2)

        self.clear()
        # Solid Sphere (H0=1, H1=0, H2=0)
        solid_sphere = Sphere()
        solid_sphere.scale(0.75)
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

