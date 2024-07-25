from manim import *

class TriangleSymmetry(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0, 1, 0], [-1, -1, 0], [1, -1, 0])
        triangle.set_fill(BLUE, opacity=0.5)
        triangle.set_stroke(color=WHITE, width=2)
        labels = VGroup(
            Tex("A").next_to(triangle.get_vertices()[0], UP),
            Tex("B").next_to(triangle.get_vertices()[1], DOWN),
            Tex("C").next_to(triangle.get_vertices()[2], DOWN)
        )
        
        # Show the original triangle
        self.play(Create(triangle), Write(labels))
        self.wait(1)
        
        # 120 degree rotation
        rotation_120 = triangle.copy().rotate(120 * DEGREES)
        labels_120 = VGroup(
            Tex("C").next_to(rotation_120.get_vertices()[0], UP),
            Tex("A").next_to(rotation_120.get_vertices()[1], DOWN),
            Tex("B").next_to(rotation_120.get_vertices()[2], DOWN)
        )
        self.play(Transform(triangle, rotation_120), Transform(labels, labels_120))
        self.wait(1)
        
        # Reflection
        reflection = triangle.copy().flip(axis=RIGHT)
        labels_reflection = VGroup(
            Tex("C").next_to(reflection.get_vertices()[0], UP),
            Tex("B").next_to(reflection.get_vertices()[1], DOWN),
            Tex("A").next_to(reflection.get_vertices()[2], DOWN)
        )
        self.play(Transform(triangle, reflection), Transform(labels, labels_reflection))
        self.wait(1)
        
        # Combined transformation (120 degree rotation + reflection)
        combined_transform = rotation_120.copy().flip(axis=RIGHT)
        labels_combined = VGroup(
            Tex("B").next_to(combined_transform.get_vertices()[0], UP),
            Tex("C").next_to(combined_transform.get_vertices()[1], DOWN),
            Tex("A").next_to(combined_transform.get_vertices()[2], DOWN)
        )
        self.play(Transform(triangle, combined_transform), Transform(labels, labels_combined))
        self.wait(1)
        
        # Show the equivalence with 240 degree rotation
        rotation_240 = Polygon([0, 1, 0], [-1, -1, 0], [1, -1, 0])
        rotation_240.rotate(240 * DEGREES)
        rotation_240.set_fill(BLUE, opacity=0.5)
        rotation_240.set_stroke(color=WHITE, width=2)
        labels_240 = VGroup(
            Tex("B").next_to(rotation_240.get_vertices()[0], UP),
            Tex("C").next_to(rotation_240.get_vertices()[1], DOWN),
            Tex("A").next_to(rotation_240.get_vertices()[2], DOWN)
        )
        self.play(Transform(triangle, rotation_240), Transform(labels, labels_240))
        self.wait(2)
        
        # End scene
        self.play(FadeOut(triangle), FadeOut(labels))

if __name__ == "__main__":
    from manim import *
    config.media_width = "100%"
    scene = TriangleSymmetry()
    scene.render()

